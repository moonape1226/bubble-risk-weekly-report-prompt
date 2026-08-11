#!/usr/bin/env python3
"""Deterministic macro-data fetch for the bubble-risk weekly report.

Fetches FRED series (with EIA / US Treasury fallback) via urllib + a custom
User-Agent, computes week-over-week deltas vs the prior-run date, and prints
one JSON block to stdout. Also emits non-FRED blocks: cftc_lev_funds
(leveraged-fund net position in UST futures), move_index (^MOVE via Yahoo
chart endpoint), ofr_repo (OFR tri-party repo volume), and the derived
repo_stress (SOFR-IORB spreads + SRF usage) and vix_spx_comove (VIX and
S&P 500 rising over the same window) blocks. Never prints API keys.
stdlib only.

Usage: python3 fetch_macro.py <prior_run_date YYYY-MM-DD | none>
"""
import json, math, os, sys, urllib.request, urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

UA = {"User-Agent": "bubble-risk-weekly"}
CONTRACT_PATH = Path(__file__).resolve().parents[1] / "report_contract.json"
try:
    REPORT_CONTRACT = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    MACRO_SCHEMA = REPORT_CONTRACT["macro_schema"]
    TAIPEI_TZ = ZoneInfo(REPORT_CONTRACT["timezone"])
    CONTRACT_VERSION = REPORT_CONTRACT["version"]
    MACRO_SCHEMA_VERSION = MACRO_SCHEMA["version"]
    DECOMPOSITION_IDENTITY_TOLERANCE_BPS = REPORT_CONTRACT["calibration"][
        "decomposition_identity_tolerance_bps"
    ]
    VIX_COMOVE_CHG_PCT = REPORT_CONTRACT["calibration"]["vix_comove_chg_pct"]
    VIX_COMOVE_TRAILING_DAYS = REPORT_CONTRACT["calibration"][
        "vix_comove_trailing_days"
    ]
    SP500_COMOVE_CHG_PCT = REPORT_CONTRACT["direction_thresholds"][
        "sp500_chg_pct"
    ]
except (OSError, UnicodeError, ValueError, KeyError, TypeError) as exc:
    raise SystemExit(f"ERROR: cannot load canonical report contract: {exc}")
FRED_KEY = os.environ.get("FRED_API_KEY", "")
EIA_KEY = os.environ.get("EIA_API_KEY", "")
PRIOR = sys.argv[1] if len(sys.argv) > 1 else "none"

# FRED series we want, with unit hint for delta formatting
FRED_SERIES = dict(MACRO_SCHEMA["series_units"])

# Low-frequency series need a wider window: quarterly prints are often
# months old, and YoY series need the year-ago base observation in range
QUARTERLY_SERIES = {"BOGZ1FL153064486Q"}
YOY_SERIES = {"CPIAUCSL"}
WIDE_WINDOW_SERIES = QUARTERLY_SERIES | YOY_SERIES

# Monthly series: FRED keeps an observation in range only while
# observation_start <= its period END, so a 21-day window silently drops the
# latest month on late-month runs (publication lag adds more slack needed)
MONTHLY_SERIES = {"JPNASSETS"}

# Published with a ~1-week lag: the latest observation usually predates the
# prior-run date, so a pick-vs-PRIOR delta degenerates to no_new_obs / 0.
# Compute the delta inside the series' own timeline instead (latest vs ~7d
# earlier observation).
LAGGED_TRAILING_DAYS = dict(MACRO_SCHEMA["trailing_delta_days"])
ALIGNMENT_PROOF_SERIES = set(MACRO_SCHEMA["alignment_proof_series"])

# obs lists kept for cross-series alignment (e.g. repo_stress spreads)
OBS_CACHE = {}


def execution_now():
    """Wall clock used for execution-year partition selection.

    The report contract is keyed to Asia/Taipei, so the fallback must not
    switch calendar years eight hours late by consulting UTC here.
    """
    return datetime.now(TAIPEI_TZ)

def _get_bytes(url, timeout=20):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()

def _get(url, timeout=20):
    return _get_bytes(url, timeout).decode()


def parsed_observation(day, value, *, positive=False):
    """Return a canonical finite observation tuple, else ``None``."""
    if not isinstance(day, str):
        return None
    try:
        parsed = datetime.strptime(day, "%Y-%m-%d")
    except ValueError:
        return None
    if parsed.strftime("%Y-%m-%d") != day:
        return None
    try:
        numeric = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(numeric) or (positive and numeric <= 0):
        return None
    return day, numeric


def canonical_observations(observations):
    """Return newest-first, unique-date observations.

    Duplicate copies of the same print are harmless, but two different values
    for one date make alignment and delta selection ambiguous and are treated
    as an upstream schema/data failure.
    """
    by_date = {}
    for day, value in observations:
        if day in by_date and by_date[day] != value:
            raise ValueError(f"conflicting observations for {day}")
        by_date[day] = value
    return sorted(by_date.items(), reverse=True)

def fetch_window(sid):
    """(lookback-before-prior, default-back) in days, by series frequency."""
    if sid in WIDE_WINDOW_SERIES:
        return 540, 540
    if sid in MONTHLY_SERIES:
        return 90, 120
    return 21, 120

def fred_obs(series_id):
    """Return list of (date, float) desc, newest first. Raises on failure."""
    lookback, default_back = fetch_window(series_id)
    start = (datetime.now(timezone.utc) - timedelta(days=default_back)).strftime("%Y-%m-%d")
    if PRIOR != "none":
        start = (datetime.strptime(PRIOR, "%Y-%m-%d") - timedelta(days=lookback)).strftime("%Y-%m-%d")
    url = ("https://api.stlouisfed.org/fred/series/observations"
           f"?series_id={series_id}&api_key={FRED_KEY}&file_type=json"
           f"&observation_start={start}&sort_order=desc")
    data = json.loads(_get(url))
    if not isinstance(data, dict) or not isinstance(data.get("observations"), list):
        raise ValueError("FRED observations is not an array")
    out = []
    for o in data["observations"]:
        if not isinstance(o, dict):
            continue
        v = o.get("value", ".")
        if v in (".", "", None):
            continue
        observation = parsed_observation(o.get("date"), v)
        if observation:
            out.append(observation)
    return canonical_observations(out)

def treasury_10y(real=False):
    """US Treasury fallback for DGS10 / DFII10.

    Returns ``(observations_desc, metadata)``.  Metadata preserves partition
    failures so a successful prior-year request cannot disguise a failed
    current-year request as a current observation.
    """
    ds = "daily_treasury_real_yield_curve" if real else "daily_treasury_yield_curve"
    field = "TC_10YEAR" if real else "BC_10YEAR"
    import re
    now = execution_now()
    current_year = now.year
    years = [current_year]
    if PRIOR != "none":
        try:
            prior_year = datetime.strptime(PRIOR, "%Y-%m-%d").year
        except ValueError:
            prior_year = current_year
        if prior_year != current_year:
            years.append(prior_year)
    # A baseline or same-year prior in early January still needs the preceding
    # partition: the most recent valid market observation is often in December.
    if now.month == 1 and current_year - 1 not in years:
        years.append(current_year - 1)
    rows = []
    failed_years = []
    empty_years = []
    # Treasury partitions this endpoint by calendar year.  On an early-January
    # run the latest observation is in the current-year response while the
    # prior-run baseline is in the prior-year response.  Fetch each partition
    # independently so one failed/empty request does not discard the other.
    for year in years:
        url = ("https://home.treasury.gov/resource-center/data-chart-center/"
               f"interest-rates/pages/xml?data={ds}&field_tdr_date_value={year}")
        try:
            xml = _get(url)
        except (OSError, ValueError, KeyError):
            failed_years.append(year)
            continue
        # Parse one Atom entry at a time.  A document-wide `.*?` can pair the
        # date of an entry whose yield is null with the next entry's yield.
        entries = re.findall(r"<entry(?:\s[^>]*)?>.*?</entry>", xml, re.S)
        valid_before = len(rows)
        for entry in entries:
            date_match = re.search(r"<d:NEW_DATE\b[^>]*>([^<]+)", entry)
            value_match = re.search(r"<d:%s\b[^>]*>([^<]+)" % field, entry)
            if not date_match or not value_match:
                continue
            observation = parsed_observation(
                date_match.group(1)[:10], value_match.group(1)
            )
            if observation:
                rows.append(observation)
        valid_count = len(rows) - valid_before
        if valid_count == 0:
            try:
                root = ET.fromstring(xml)
                valid_empty_feed = root.tag.rsplit("}", 1)[-1] == "feed"
            except (ET.ParseError, TypeError):
                valid_empty_feed = False
            # An empty current-year feed is legitimate only before the first
            # January market observation; elsewhere it is indistinguishable
            # from schema drift and must not let prior-year rows look current.
            if (year == current_year and now.month == 1 and now.day <= 7
                    and not entries and valid_empty_feed):
                empty_years.append(year)
            else:
                failed_years.append(year)
    rows = canonical_observations(rows)
    return rows, {
        "requested_years": years,
        "failed_years": failed_years,
        "empty_years": empty_years,
    }

def eia_wti():
    url = ("https://api.eia.gov/v2/petroleum/pri/spt/data/"
           f"?api_key={EIA_KEY}&facets[series][]=RWTC&data[]=value"
           "&sort[0][column]=period&sort[0][direction]=desc&length=30")
    data = json.loads(_get(url))
    if not isinstance(data, dict):
        raise ValueError("EIA root is not an object")
    out = []
    for o in data.get("response", {}).get("data", []):
        if not isinstance(o, dict) or o.get("value") in (None, ""):
            continue
        observation = parsed_observation(o.get("period"), o.get("value"))
        if observation:
            out.append(observation)
    return canonical_observations(out)

def pick(obs, on_or_before=None):
    """latest, or latest on-or-before a date."""
    if not obs:
        return None
    if on_or_before is None:
        return obs[0]
    for d, v in obs:
        if d <= on_or_before:
            return (d, v)
    return None

def series_block(sid, unit):
    """Fetch one series with fallbacks; return a result dict."""
    obs, source = [], None
    fallback_meta = None
    try:
        obs = fred_obs(sid)
        if obs:
            source = "FRED API"
    except (OSError, ValueError, KeyError, TypeError, AttributeError, IndexError):
        # Malformed upstream JSON must degrade this series, not terminate the
        # complete macro artifact.
        obs = []
    # fallbacks for the rate series
    if not obs and sid in ("DGS10", "DFII10"):
        try:
            obs, fallback_meta = treasury_10y(real=(sid == "DFII10"))
            # Fail closed on the current partition.  Prior-year rows are useful
            # history only; they cannot prove that the current endpoint had no
            # newer observation when its request itself failed.
            current_year = fallback_meta["requested_years"][0]
            if current_year in fallback_meta["failed_years"]:
                obs = []
            elif obs:
                source = "US Treasury"
        except (OSError, ValueError, KeyError, TypeError, AttributeError, IndexError):
            obs = []
    if not obs and sid == "DCOILWTICO" and EIA_KEY:
        try:
            obs = eia_wti()
            if obs:
                source = "EIA"
        except (OSError, ValueError, KeyError, TypeError, AttributeError, IndexError):
            obs = []
    if not obs:
        res = {"status": "fetch_failed", "source": None}
        if fallback_meta and fallback_meta["failed_years"]:
            res["fallback_failed_years"] = fallback_meta["failed_years"]
        return res
    OBS_CACHE[sid] = obs
    latest = obs[0]
    res = {"status": "ok", "source": source,
           "latest_date": latest[0], "latest": latest[1]}
    if sid in ALIGNMENT_PROOF_SERIES:
        res["alignment_observations"] = [
            {"date": day, "value": value} for day, value in obs[:32]
        ]
    if fallback_meta and fallback_meta["failed_years"]:
        # A prior partition failure can remove the comparison point without
        # invalidating a successfully fetched current level.
        res["fallback_failed_years"] = fallback_meta["failed_years"]
    if sid in LAGGED_TRAILING_DAYS:
        base_target = (datetime.strptime(latest[0], "%Y-%m-%d")
                       - timedelta(days=LAGGED_TRAILING_DAYS[sid])).strftime(
                           "%Y-%m-%d")
        base = pick(obs, base_target)
        base_age = (
            (datetime.strptime(latest[0], "%Y-%m-%d")
             - datetime.strptime(base[0], "%Y-%m-%d")).days
            if base else None
        )
        target_days = LAGGED_TRAILING_DAYS[sid]
        if (base and base[0] != latest[0]
                and target_days <= base_age <= target_days + 7):
            res["prior_date"], res["prior"] = base
            delta = latest[1] - base[1]
            if unit == "pct":
                res["delta_bps"] = round(delta * 100, 1)
            res["delta_abs"] = round(delta, 3)
            res["delta_note"] = ("trailing ~7d within the series' own timeline "
                                 "(publication lag; not aligned to prior-run date)")
        return res
    prior = pick(obs, PRIOR) if PRIOR != "none" else None
    if prior and prior[0] != latest[0]:
        delta = latest[1] - prior[1]
        res["prior_date"], res["prior"] = prior[0], prior[1]
        if unit == "pct":
            res["delta_bps"] = round(delta * 100, 1)
        if unit in ("usd", "usd_bn") and prior[1]:
            res["chg_pct"] = round(delta / prior[1] * 100, 2)
        res["delta_abs"] = round(delta, 3)
    elif prior and sid not in WIDE_WINDOW_SERIES:
        # prior-run date and latest valid observation coincide (holiday /
        # weekend gap): the weekly change is 0 by construction, not unknown
        res["prior_date"], res["prior"] = prior[0], prior[1]
        res["no_new_obs"] = True
        if unit == "pct":
            res["delta_bps"] = 0.0
        if unit in ("usd", "usd_bn"):
            res["chg_pct"] = 0.0
        res["delta_abs"] = 0.0
    if sid in YOY_SERIES:
        base_target = (datetime.strptime(latest[0], "%Y-%m-%d")
                       - timedelta(days=365)).strftime("%Y-%m-%d")
        base = pick(obs, base_target)
        age_policy = MACRO_SCHEMA["yoy_base_age_days"][sid]
        base_age = ((datetime.strptime(latest[0], "%Y-%m-%d")
                     - datetime.strptime(base[0], "%Y-%m-%d")).days
                    if base else None)
        if (not base or not base[1] or base_age < age_policy["min"]
                or base_age > age_policy["max"]
                or (age_policy.get("same_month_previous_year") and (
                    int(base[0][:4]) != int(latest[0][:4]) - 1
                    or base[0][5:7] != latest[0][5:7]))):
            # This source is consumed as YoY inflation, not as a CPI index
            # level.  A current print without a valid year-ago base cannot
            # satisfy that contract and must enter the normal fallback path.
            return {"status": "fetch_failed", "source": None,
                    "reason": "year-ago base observation unavailable"}
        res["yoy_base_date"], res["yoy_base"] = base[0], base[1]
        res["yoy_pct"] = round((latest[1] / base[1] - 1) * 100, 2)
    return res

def sp500_trend():
    """Fetch S&P 500 daily and compute 200-DMA / 52-week MA and % deviation."""
    start = (datetime.now(timezone.utc) - timedelta(days=600)).strftime("%Y-%m-%d")
    url = ("https://api.stlouisfed.org/fred/series/observations"
           f"?series_id=SP500&api_key={FRED_KEY}&file_type=json"
           f"&observation_start={start}&sort_order=desc")
    try:
        data = json.loads(_get(url))
        raw_observations = data.get("observations", [])
        if not isinstance(raw_observations, list):
            raise ValueError("FRED observations is not an array")
    except (OSError, ValueError, TypeError, AttributeError):
        return {"status": "fetch_failed", "source": None}
    obs = []
    for o in raw_observations:
        try:
            v = o.get("value", ".")
            if v not in (".", "", None):
                observation = parsed_observation(o.get("date"), v, positive=True)
                if observation:
                    obs.append(observation)
        except (KeyError, TypeError, AttributeError, ValueError):
            continue
    try:
        obs = canonical_observations(obs)
    except ValueError:
        return {"status": "fetch_failed", "source": "FRED API"}
    if len(obs) < 200:
        return {"status": "fetch_failed", "source": "FRED API"}
    vals = [v for _, v in obs]
    latest_date, latest_raw = obs[0]
    latest = round(latest_raw, 2)
    ma200 = round(sum(vals[:200]) / 200, 2)
    if ma200 <= 0:
        return {"status": "fetch_failed", "source": "FRED API"}
    res = {"status": "ok", "source": "FRED API",
           "latest_date": latest_date, "latest": latest,
           "ma200": ma200,
           "dev200_pct": round((latest - ma200) / ma200 * 100, 2),
           # bounded proof so the derived vix_spx_comove window can be
           # reproduced without refetching SP500
           "alignment_observations": [
               {"date": day, "value": round(value, 2)}
               for day, value in obs[:32]
           ]}
    if len(vals) >= 252:
        ma52w = round(sum(vals[:252]) / 252, 2)
        res["ma52w"] = ma52w
        res["dev52w_pct"] = round((latest - ma52w) / ma52w * 100, 2)
    prior = pick(obs, PRIOR) if PRIOR != "none" else None
    if prior and prior[0] != latest_date:
        prior_spot = round(prior[1], 2)
        res["prior_spot_date"], res["prior_spot"] = prior[0], prior_spot
        res["chg_pct"] = round((latest - prior_spot) / prior_spot * 100, 2)
    elif prior:
        res["prior_spot_date"], res["prior_spot"] = prior[0], round(prior[1], 2)
        res["chg_pct"] = 0.0
        res["no_new_obs"] = True
    return res

def cftc_lev_funds():
    """Aggregate leveraged-fund net position in UST futures (CFTC TFF).

    Contract-count sum of Lev_Money long minus short across the six CBT
    Treasury contracts, from the current-year history zip (trend) merged
    with the latest weekly file. No API key.
    """
    import csv, io, zipfile
    markets = ("UST BOND", "ULTRA UST BOND", "UST 2Y NOTE", "UST 5Y NOTE",
               "UST 10Y NOTE", "ULTRA UST 10Y")

    def parse(text, acc):
        for line in text.splitlines():
            if not line.strip() or line.startswith('"Market_and_Exchange_Names"'):
                continue
            try:
                f = next(csv.reader([line]))
            except (csv.Error, StopIteration, UnicodeError):
                continue
            if len(f) < 17 or not f[0].startswith(markets):
                continue
            try:
                report_day = f[2].strip()
                if parsed_observation(report_day, 0) is None:
                    continue
                acc[report_day] = (
                    acc.get(report_day, 0) + int(f[14]) - int(f[15])
                )
            except ValueError:
                continue

    by_date = {}
    year = execution_now().year
    for yr in (year, year - 1):
        # prior-year archive only when the current year is too short for the
        # 8-week trend + delta_4w (early-January runs, or missing new-year zip)
        if yr != year and len(by_date) >= 9:
            break
        try:
            raw = _get_bytes(f"https://www.cftc.gov/files/dea/history/fut_fin_txt_{yr}.zip",
                             timeout=45)
            parse(zipfile.ZipFile(io.BytesIO(raw)).read("FinFutYY.txt").decode("latin-1"),
                  by_date)
        except (OSError, ValueError, KeyError, EOFError, RuntimeError,
                csv.Error, UnicodeError, zipfile.BadZipFile):
            pass
    try:
        weekly = {}
        parse(_get("https://www.cftc.gov/dea/newcot/FinFutWk.txt", timeout=30), weekly)
        by_date.update(weekly)
    except (OSError, ValueError, csv.Error, UnicodeError):
        pass
    if not by_date:
        return {"status": "fetch_failed", "source": None}
    dates = sorted(by_date)
    res = {"status": "ok", "source": "CFTC TFF futures-only (weekly + history zip)",
           "latest_date": dates[-1], "net_contracts": by_date[dates[-1]],
           "markets": list(markets),
           "recent_weeks": [{"date": d, "net": by_date[d]} for d in dates[-8:]]}
    if len(dates) >= 5:
        res["delta_4w"] = by_date[dates[-1]] - by_date[dates[-5]]
    return res

def move_index():
    """^MOVE via Yahoo Finance chart endpoint (unofficial; may break)."""
    url = ("https://query1.finance.yahoo.com/v8/finance/chart/%5EMOVE"
           "?range=3mo&interval=1d")
    try:
        r = json.loads(_get(url, timeout=20))["chart"]["result"][0]
        pairs = zip(r["timestamp"], r["indicators"]["quote"][0]["close"])
    except (OSError, ValueError, KeyError, IndexError, TypeError):
        return {"status": "fetch_failed", "source": None}
    obs = []
    for t, c in pairs:
        if c is None:
            continue
        try:
            date = datetime.fromtimestamp(
                float(t), tz=timezone.utc).strftime("%Y-%m-%d")
            close = round(float(c), 2)
            if not math.isfinite(close) or close <= 0:
                continue
        except (OSError, OverflowError, TypeError, ValueError):
            # One malformed Yahoo observation must not abort the whole fetch.
            continue
        obs.append((date, close))
    if not obs:
        return {"status": "fetch_failed", "source": "Yahoo chart API"}
    try:
        obs = canonical_observations(obs)
    except ValueError:
        return {"status": "fetch_failed", "source": "Yahoo chart API"}
    res = {"status": "ok", "source": "Yahoo Finance chart API (^MOVE, unofficial)",
           "latest_date": obs[0][0], "latest": obs[0][1]}
    prior = pick(obs, PRIOR) if PRIOR != "none" else None
    if prior and prior[0] != obs[0][0]:
        res["prior_date"], res["prior"] = prior
        res["delta_abs"] = round(obs[0][1] - prior[1], 2)
    elif prior:
        res["prior_date"], res["prior"] = prior
        res["delta_abs"] = 0.0
        res["no_new_obs"] = True
    return res

def ofr_repo():
    """OFR Short-term Funding Monitor: tri-party repo transaction volume.

    TRIV1 = excluding Federal Reserve transactions: keeps the private-funding
    volume clean of ON RRP / SRF footprints, which are tracked separately
    (RPONTTLD) - the include-Fed variant is REPO-TRI_TV_TOT-P.
    """
    mnemonic = "REPO-TRIV1_TV_TOT-P"
    url = f"https://data.financialresearch.gov/v1/series/full?mnemonic={mnemonic}"
    try:
        agg = json.loads(_get(url, timeout=30))[mnemonic]["timeseries"]["aggregation"]
        obs = []
        for item in agg:
            if not isinstance(item, (list, tuple)) or len(item) != 2:
                continue
            observation = parsed_observation(item[0], item[1])
            if observation and observation[1] >= 0:
                obs.append(observation)
    except (OSError, ValueError, KeyError, TypeError):
        return {"status": "fetch_failed", "source": None}
    if not obs:
        return {"status": "fetch_failed", "source": "OFR STFM"}
    try:
        obs = canonical_observations(obs)
    except ValueError:
        return {"status": "fetch_failed", "source": "OFR STFM"}
    latest_volume = round(obs[0][1] / 1e9, 1)
    res = {"status": "ok", "source": f"OFR Short-term Funding Monitor ({mnemonic})",
           "latest_date": obs[0][0],
           "transaction_volume_usd_bn": latest_volume}
    prior = pick(obs, PRIOR) if PRIOR != "none" else None
    if prior and prior[0] != obs[0][0]:
        res["prior_date"] = prior[0]
        prior_volume = round(prior[1] / 1e9, 1)
        res["prior_transaction_volume_usd_bn"] = prior_volume
        if prior_volume:
            res["chg_pct"] = round(
                (latest_volume - prior_volume) / prior_volume * 100, 2
            )
    elif prior:
        res["prior_date"] = prior[0]
        res["prior_transaction_volume_usd_bn"] = round(prior[1] / 1e9, 1)
        res["chg_pct"] = 0.0
        res["no_new_obs"] = True
    return res

def derived_t10yie():
    """T10YIE fallback = DGS10 - DFII10 on their latest SHARED observation
    date; mixed-date subtraction fabricates a level. None when no shared date."""
    # Only use the bounded observation proof emitted with the artifact; a
    # derived leg outside that proof could not be independently cross-checked
    # by the validator.
    dn = dict(OBS_CACHE.get("DGS10", [])[:32])
    dr = dict(OBS_CACHE.get("DFII10", [])[:32])
    shared = set(dn) & set(dr)
    if not shared:
        return None
    d = max(shared)
    policy = MACRO_SCHEMA["derived_series"]["T10YIE"]
    return {"status": "derived", "source": policy["source"],
            "latest_date": d, "latest": round(dn[d] - dr[d], 3),
            "derived_from": {
                policy["left"]: {"date": d, "value": dn[d]},
                policy["right"]: {"date": d, "value": dr[d]},
            }}

def repo_stress_block(series):
    """Derived repo-stress block (SOFR-IORB spreads + SRF usage).

    Each SOFR observation is paired with the latest IORB print on or before
    that observation date; a strictly older IORB date is disclosed.  A newer
    IORB print is never paired backward because that could cross an FOMC move.
    SOFR99 may lag SOFR, so it receives its own as-of IORB lookup.
    """
    sofr, iorb = series.get("SOFR", {}), series.get("IORB", {})
    rs = {}
    if sofr.get("status") == "ok" and iorb.get("status") == "ok":
        as_of = sofr["latest_date"]
        # no IORB print at/before the SOFR date -> no spread; falling back to
        # a possibly NEWER iorb.latest would mix dates undisclosed
        iorb_al = pick(OBS_CACHE.get("IORB", [])[:32], as_of)
        if iorb_al:
            rs.update({"as_of": as_of,
                       "sofr": sofr["latest"], "iorb": iorb_al[1],
                       "iorb_date": iorb_al[0],
                       "sofr_iorb_bps": round(
                           (sofr["latest"] - iorb_al[1]) * 100, 1)})
            s99 = series.get("SOFR99", {})
            if s99.get("status") == "ok":
                # same rule per leg: SOFR99 at/before as_of, and IORB at/before
                # the SOFR99 date - otherwise omit rather than fabricate a value
                s99_al = pick(OBS_CACHE.get("SOFR99", [])[:32], as_of)
                iorb_99 = (pick(OBS_CACHE.get("IORB", [])[:32], s99_al[0])
                           if s99_al else None)
                if s99_al and iorb_99:
                    rs["sofr99"] = s99_al[1]
                    rs["sofr99_date"] = s99_al[0]
                    rs["sofr99_iorb"] = iorb_99[1]
                    rs["sofr99_iorb_date"] = iorb_99[0]
                    rs["sofr99_iorb_bps"] = round(
                        (s99_al[1] - iorb_99[1]) * 100, 1)
    # SRF is an independent leg.  Keep it even when SOFR/IORB failed or could
    # not be safely paired; otherwise a single rate-series outage erases usable
    # official-liquidity evidence.
    srf = series.get("RPONTTLD", {})
    if srf.get("status") == "ok":
        rs["srf_usage_bn"] = srf["latest"]
        rs["srf_date"] = srf["latest_date"]
    has_spread = "sofr_iorb_bps" in rs
    has_srf = "srf_usage_bn" in rs
    if has_spread and has_srf:
        return {"status": "ok", **rs}
    if has_spread or has_srf:
        return {"status": "partial", **rs}
    return {"status": "unavailable"}

def vix_spx_comove_block(series, sp500):
    """Derived VIX / S&P 500 co-movement block.

    Equity and volatility normally move against each other; both rising over
    the same window is the crowded-optionality warning read (hedging demand
    bid up while the index still makes ground).

    FRED publishes SP500 a business day ahead of VIXCLS, so a prior-run-date
    delta degenerates to no_new_obs on most runs.  The window is therefore a
    trailing ~7d pair taken from the dates the two series actually share,
    read from the bounded proofs emitted with this artifact so the validator
    can reproduce every selected leg. A co-movement claim assembled from two
    different windows is never emitted.
    """
    def unavailable(note):
        return {"status": "unavailable", "comove": False, "note": note}

    vix = series.get("VIXCLS", {})
    if vix.get("status") != "ok" or sp500.get("status") != "ok":
        return unavailable("VIXCLS or sp500_trend unavailable")
    vix_obs = {item["date"]: item["value"]
               for item in vix.get("alignment_observations", [])}
    sp500_obs = {item["date"]: item["value"]
                 for item in sp500.get("alignment_observations", [])}
    shared = sorted(set(vix_obs) & set(sp500_obs), reverse=True)
    if not shared:
        return unavailable("VIXCLS and sp500_trend share no observation date")
    latest = shared[0]
    target = (datetime.strptime(latest, "%Y-%m-%d")
              - timedelta(days=VIX_COMOVE_TRAILING_DAYS)).strftime("%Y-%m-%d")
    base = next((day for day in shared if day <= target), None)
    if base is None:
        return unavailable("no shared base observation at or before the "
                           "trailing window target")
    window_days = (datetime.strptime(latest, "%Y-%m-%d")
                   - datetime.strptime(base, "%Y-%m-%d")).days
    if window_days > VIX_COMOVE_TRAILING_DAYS * 2:
        return unavailable("shared trailing base is older than twice the "
                           "trailing window")
    if vix_obs[base] <= 0 or sp500_obs[base] <= 0:
        return unavailable("a trailing base level is not positive")
    vix_chg_pct = round(
        (vix_obs[latest] - vix_obs[base]) / vix_obs[base] * 100, 2)
    sp500_chg_pct = round(
        (sp500_obs[latest] - sp500_obs[base]) / sp500_obs[base] * 100, 2)
    comove = (sp500_chg_pct >= SP500_COMOVE_CHG_PCT
              and vix_chg_pct >= VIX_COMOVE_CHG_PCT)
    return {"status": "ok", "as_of": latest, "base_date": base,
            "window_days": window_days,
            "vix": vix_obs[latest], "vix_base": vix_obs[base],
            "vix_chg_pct": vix_chg_pct,
            "sp500": sp500_obs[latest], "sp500_base": sp500_obs[base],
            "sp500_chg_pct": sp500_chg_pct,
            "comove": comove,
            "note": (f"trailing ~{VIX_COMOVE_TRAILING_DAYS}d on the shared "
                     "VIXCLS/SP500 timeline (publication lag differs; not "
                     "aligned to the prior-run date); co-movement thresholds "
                     f"S&P 500 ≥ +{SP500_COMOVE_CHG_PCT}%, "
                     f"VIX ≥ +{VIX_COMOVE_CHG_PCT}%")}

def decomposition_block(series, baseline=False):
    """10Y weekly-change decomposition. Rebuilding ΔT10YIE from the identity
    ΔDGS10 − ΔDFII10 is valid only when both legs cover the same window
    (same latest and prior dates); with ΔT10YIE unavailable the driver is
    'unknown' rather than judged from the real leg alone."""
    n, r, ty = series.get("DGS10", {}), series.get("DFII10", {}), series.get("T10YIE", {})
    names = ("DGS10", "DFII10", "T10YIE")
    if baseline:
        return {"status": "baseline_no_prior", "driver": "baseline",
                "freshness": "not_applicable", "stale_series": [],
                "d_dgs10_bps": None, "d_dfii10_bps": None,
                "d_t10yie_bps": None,
                "note": "baseline run; no prior comparison date"}
    d = {k: series.get(k, {}).get("delta_bps") for k in names}
    delta_series = [k for k in names if d[k] is not None]
    stale_series = [k for k in delta_series
                    if series.get(k, {}).get("no_new_obs")]
    if delta_series and len(stale_series) == len(delta_series):
        freshness = "all_stale"
    elif stale_series:
        freshness = "partial_stale"
    else:
        freshness = "updated"
    if d["DGS10"] is None or d["DFII10"] is None:
        return {"status": "unavailable_no_daily_history",
                "driver": None,
                "freshness": freshness, "stale_series": stale_series,
                "d_dgs10_bps": d["DGS10"],
                "d_dfii10_bps": d["DFII10"],
                "d_t10yie_bps": d["T10YIE"],
                "note": "daily history unavailable for DGS10 or DFII10"}
    note = "weekly change in bps; computed from daily history"
    w_n = (n.get("latest_date"), n.get("prior_date"))
    w_r = (r.get("latest_date"), r.get("prior_date"))
    w_t = (ty.get("latest_date"), ty.get("prior_date"))
    rebuilt = False
    if d["T10YIE"] is None and w_n == w_r:
        d["T10YIE"] = round(d["DGS10"] - d["DFII10"], 1)
        rebuilt = True
    t = d["T10YIE"]
    if t is None:
        driver = "unknown"
        note += ("; ΔT10YIE unavailable and not rebuilt "
                 "(DGS10/DFII10 windows differ - identity does not hold)")
    elif not d["DGS10"] and not d["DFII10"] and not t:
        # All-zero changes need no window alignment to attribute.  This says
        # nothing about freshness: zero can come from fresh unchanged prints,
        # all-stale holiday data, or a mixture of the two.
        driver = "none"
    elif (not rebuilt and w_n == w_r == w_t
          and abs(d["DGS10"] - d["DFII10"] - t)
          > DECOMPOSITION_IDENTITY_TOLERANCE_BPS):
        driver = "unknown"
        note += "; same-window decomposition identity residual exceeds tolerance"
    elif not rebuilt and not w_n == w_r == w_t:
        # a direct ΔT10YIE from a different window breaks the identity too
        driver = "unknown"
        note += ("; ΔT10YIE covers a different window than DGS10/DFII10 - "
                 "driver not judged (identity does not hold across windows)")
    elif abs(t) > abs(d["DFII10"]):
        driver = "breakeven"
    elif abs(d["DFII10"]) > abs(t):
        driver = "real-rate"
    else:
        driver = "mixed"
    if driver == "none":
        note += "; all three weekly changes are zero"
    if freshness == "all_stale":
        note += ("; all delta-bearing input series have no new observations "
                 "since the prior run")
    elif freshness == "partial_stale":
        note += ("; no new observations for " + ", ".join(stale_series)
                 + "; remaining delta-bearing input series updated")
    else:
        note += "; all available delta-bearing input series updated"
    return {"status": "ok",
            "d_dgs10_bps": d["DGS10"], "d_dfii10_bps": d["DFII10"],
            "d_t10yie_bps": t, "driver": driver,
            "freshness": freshness, "stale_series": stale_series,
            "note": note}

def main():
    if PRIOR != "none":
        # strict ISO check: strptime alone accepts unpadded "2026-7-9", which
        # would poison the lexicographic date comparisons in pick()
        try:
            canonical = datetime.strptime(PRIOR, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            canonical = None
        if canonical != PRIOR:
            print(f"ERROR: prior_run_date must be 'none' or YYYY-MM-DD, got: {PRIOR}",
                  file=sys.stderr)
            sys.exit(2)
        if datetime.strptime(PRIOR, "%Y-%m-%d").date() >= execution_now().date():
            print("ERROR: prior_run_date must be strictly before the Asia/Taipei execution date",
                  file=sys.stderr)
            sys.exit(2)
    generated_at = execution_now().astimezone(TAIPEI_TZ).isoformat(
        timespec="seconds")
    out = {"contract_version": CONTRACT_VERSION,
           "macro_schema_version": MACRO_SCHEMA_VERSION,
           "generated_at": generated_at,
           "prior_run_date": PRIOR, "fred_key_present": bool(FRED_KEY),
           "eia_key_present": bool(EIA_KEY), "series": {}}
    for sid, unit in FRED_SERIES.items():
        out["series"][sid] = series_block(sid, unit)
    out["sp500_trend"] = sp500_trend()
    out["cftc_lev_funds"] = cftc_lev_funds()
    out["move_index"] = move_index()
    out["ofr_repo"] = ofr_repo()
    out["repo_stress"] = repo_stress_block(out["series"])
    # T10YIE derive fallback if it failed but DGS10/DFII10 ok
    t = out["series"].get("T10YIE", {})
    if t.get("status") != "ok":
        n, r = out["series"].get("DGS10", {}), out["series"].get("DFII10", {})
        if n.get("status") == "ok" and r.get("status") == "ok":
            blk = derived_t10yie()
            if blk:
                out["series"]["T10YIE"] = blk
    out["decomposition"] = decomposition_block(
        out["series"], baseline=(PRIOR == "none"))
    out["vix_spx_comove"] = vix_spx_comove_block(
        out["series"], out["sp500_trend"])
    print("===MACRO_JSON_START===")
    print(json.dumps(out, ensure_ascii=False, indent=2, allow_nan=False))
    print("===MACRO_JSON_END===")

if __name__ == "__main__":
    main()

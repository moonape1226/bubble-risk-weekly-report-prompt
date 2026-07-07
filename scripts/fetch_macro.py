#!/usr/bin/env python3
"""Deterministic macro-data fetch for the bubble-risk weekly report.

Fetches FRED series (with EIA / US Treasury fallback) via urllib + a custom
User-Agent, computes week-over-week deltas vs the prior-run date, and prints
one JSON block to stdout. Also emits non-FRED blocks: cftc_lev_funds
(leveraged-fund net position in UST futures), move_index (^MOVE via Yahoo
chart endpoint), ofr_repo (OFR tri-party repo volume), and a derived
repo_stress block (SOFR-IORB spreads + SRF usage). Never prints API keys.
stdlib only.

Usage: python3 fetch_macro.py <prior_run_date YYYY-MM-DD | none>
"""
import json, os, sys, urllib.request, urllib.error
from datetime import datetime, timedelta, timezone

UA = {"User-Agent": "bubble-risk-weekly"}
FRED_KEY = os.environ.get("FRED_API_KEY", "")
EIA_KEY = os.environ.get("EIA_API_KEY", "")
PRIOR = sys.argv[1] if len(sys.argv) > 1 else "none"

# FRED series we want, with unit hint for delta formatting
FRED_SERIES = {
    "DGS10": "pct", "DFII10": "pct", "T10YIE": "pct",
    "BAMLH0A0HYM2": "pct", "BAMLC0A0CM": "pct",
    "DFEDTARU": "pct", "DFEDTARL": "pct", "WALCL": "usd_mn", "DCOILWTICO": "usd",
    "ECBASSETSW": "eur_mn", "JPNASSETS": "jpy_100mn",
    "BOGZ1FL153064486Q": "level",
    "T5YIFR": "pct", "CPIAUCSL": "level",
    "THREEFYTP10": "pct", "SOFR": "pct", "SOFR99": "pct", "IORB": "pct",
    "RPONTSYD": "usd_bn", "LNFACBW027SBOG": "usd_bn",
}

# Low-frequency series need a wider window: quarterly prints are often
# months old, and YoY series need the year-ago base observation in range
QUARTERLY_SERIES = {"BOGZ1FL153064486Q"}
YOY_SERIES = {"CPIAUCSL"}
WIDE_WINDOW_SERIES = QUARTERLY_SERIES | YOY_SERIES

def _get_bytes(url, timeout=20):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()

def _get(url, timeout=20):
    return _get_bytes(url, timeout).decode()

def fred_obs(series_id):
    """Return list of (date, float) desc, newest first. Raises on failure."""
    lookback = 540 if series_id in WIDE_WINDOW_SERIES else 21
    default_back = 540 if series_id in WIDE_WINDOW_SERIES else 120
    start = (datetime.now(timezone.utc) - timedelta(days=default_back)).strftime("%Y-%m-%d")
    if PRIOR != "none":
        try:
            start = (datetime.strptime(PRIOR, "%Y-%m-%d") - timedelta(days=lookback)).strftime("%Y-%m-%d")
        except ValueError:
            pass
    url = ("https://api.stlouisfed.org/fred/series/observations"
           f"?series_id={series_id}&api_key={FRED_KEY}&file_type=json"
           f"&observation_start={start}&sort_order=desc")
    data = json.loads(_get(url))
    out = []
    for o in data.get("observations", []):
        v = o.get("value", ".")
        if v not in (".", ""):
            out.append((o["date"], float(v)))
    return out

def treasury_10y(real=False):
    """US Treasury daily yield curve fallback for DGS10 / DFII10. Returns desc list."""
    year = datetime.now(timezone.utc).strftime("%Y")
    ds = "daily_treasury_real_yield_curve" if real else "daily_treasury_yield_curve"
    field = "TC_10YEAR" if real else "BC_10YEAR"
    url = ("https://home.treasury.gov/resource-center/data-chart-center/"
           f"interest-rates/pages/xml?data={ds}&field_tdr_date_value={year}")
    xml = _get(url)
    import re
    rows = []
    for m in re.finditer(r"<d:NEW_DATE[^>]*>([^<]+).*?<d:%s[^>]*>([^<]+)" % field, xml, re.S):
        d = m.group(1)[:10]
        rows.append((d, float(m.group(2))))
    rows.sort(reverse=True)
    return rows

def eia_wti():
    url = ("https://api.eia.gov/v2/petroleum/pri/spt/data/"
           f"?api_key={EIA_KEY}&facets[series][]=RWTC&data[]=value"
           "&sort[0][column]=period&sort[0][direction]=desc&length=30")
    data = json.loads(_get(url))
    out = []
    for o in data.get("response", {}).get("data", []):
        if o.get("value") not in (None, ""):
            out.append((o["period"], float(o["value"])))
    return out

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
    try:
        obs = fred_obs(sid)
        if obs:
            source = "FRED API"
    except (OSError, ValueError, KeyError):  # OSError covers URLError / HTTPError / TimeoutError
        obs = []
    # fallbacks for the rate series
    if not obs and sid in ("DGS10", "DFII10"):
        try:
            obs = treasury_10y(real=(sid == "DFII10"))
            if obs:
                source = "US Treasury"
        except (OSError, ValueError, KeyError):
            obs = []
    if not obs and sid == "DCOILWTICO" and EIA_KEY:
        try:
            obs = eia_wti()
            if obs:
                source = "EIA"
        except (OSError, ValueError, KeyError):
            obs = []
    if not obs:
        return {"status": "fetch_failed", "source": None}
    latest = obs[0]
    prior = pick(obs, PRIOR) if PRIOR != "none" else None
    res = {"status": "ok", "source": source,
           "latest_date": latest[0], "latest": latest[1]}
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
        if base:
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
    except (OSError, ValueError):  # OSError covers URLError / HTTPError / TimeoutError
        return {"status": "fetch_failed", "source": None}
    obs = []
    for o in data.get("observations", []):
        v = o.get("value", ".")
        if v not in (".", ""):
            obs.append((o["date"], float(v)))  # newest-first
    if len(obs) < 200:
        return {"status": "fetch_failed", "source": "FRED API"}
    vals = [v for _, v in obs]
    latest_date, latest = obs[0]
    ma200 = sum(vals[:200]) / 200
    res = {"status": "ok", "source": "FRED API",
           "latest_date": latest_date, "latest": round(latest, 2),
           "ma200": round(ma200, 2),
           "dev200_pct": round((latest - ma200) / ma200 * 100, 2)}
    if len(vals) >= 252:
        ma52w = sum(vals[:252]) / 252
        res["ma52w"] = round(ma52w, 2)
        res["dev52w_pct"] = round((latest - ma52w) / ma52w * 100, 2)
    prior = pick(obs, PRIOR) if PRIOR != "none" else None
    if prior and prior[0] != latest_date:
        res["prior_spot_date"], res["prior_spot"] = prior[0], round(prior[1], 2)
        res["chg_pct"] = round((latest - prior[1]) / prior[1] * 100, 2)
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
            f = next(csv.reader([line]))
            if len(f) < 17 or not f[0].startswith(markets):
                continue
            try:
                acc[f[2].strip()] = acc.get(f[2].strip(), 0) + int(f[14]) - int(f[15])
            except ValueError:
                continue

    by_date = {}
    year = datetime.now(timezone.utc).year
    try:
        raw = _get_bytes(f"https://www.cftc.gov/files/dea/history/fut_fin_txt_{year}.zip",
                         timeout=45)
        parse(zipfile.ZipFile(io.BytesIO(raw)).read("FinFutYY.txt").decode("latin-1"),
              by_date)
    except (OSError, ValueError, KeyError, zipfile.BadZipFile):
        pass
    try:
        weekly = {}
        parse(_get("https://www.cftc.gov/dea/newcot/FinFutWk.txt", timeout=30), weekly)
        by_date.update(weekly)
    except (OSError, ValueError):
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
    obs = [(datetime.fromtimestamp(t, tz=timezone.utc).strftime("%Y-%m-%d"),
            round(float(c), 2)) for t, c in pairs if c is not None]
    if not obs:
        return {"status": "fetch_failed", "source": "Yahoo chart API"}
    obs.sort(reverse=True)
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
    """OFR Short-term Funding Monitor: tri-party repo outstanding volume."""
    mnemonic = "REPO-TRI_TV_TOT-P"
    url = f"https://data.financialresearch.gov/v1/series/full?mnemonic={mnemonic}"
    try:
        agg = json.loads(_get(url, timeout=30))[mnemonic]["timeseries"]["aggregation"]
        obs = [(d, float(v)) for d, v in agg if v is not None]
    except (OSError, ValueError, KeyError, TypeError):
        return {"status": "fetch_failed", "source": None}
    if not obs:
        return {"status": "fetch_failed", "source": "OFR STFM"}
    obs.sort(reverse=True)
    res = {"status": "ok", "source": f"OFR Short-term Funding Monitor ({mnemonic})",
           "latest_date": obs[0][0], "latest_usd_bn": round(obs[0][1] / 1e9, 1)}
    prior = pick(obs, PRIOR) if PRIOR != "none" else None
    if prior and prior[0] != obs[0][0]:
        res["prior_date"] = prior[0]
        res["prior_usd_bn"] = round(prior[1] / 1e9, 1)
        if prior[1]:
            res["chg_pct"] = round((obs[0][1] - prior[1]) / prior[1] * 100, 2)
    elif prior:
        res["prior_date"] = prior[0]
        res["prior_usd_bn"] = round(prior[1] / 1e9, 1)
        res["chg_pct"] = 0.0
        res["no_new_obs"] = True
    return res

def main():
    out = {"prior_run_date": PRIOR, "fred_key_present": bool(FRED_KEY),
           "eia_key_present": bool(EIA_KEY), "series": {}}
    for sid, unit in FRED_SERIES.items():
        out["series"][sid] = series_block(sid, unit)
    out["sp500_trend"] = sp500_trend()
    out["cftc_lev_funds"] = cftc_lev_funds()
    out["move_index"] = move_index()
    out["ofr_repo"] = ofr_repo()
    # derived repo-stress convenience block (SOFR-IORB spreads + SRF usage)
    sofr = out["series"].get("SOFR", {})
    iorb = out["series"].get("IORB", {})
    if sofr.get("status") == "ok" and iorb.get("status") == "ok":
        rs = {"status": "ok", "as_of": sofr["latest_date"],
              "sofr": sofr["latest"], "iorb": iorb["latest"],
              "sofr_iorb_bps": round((sofr["latest"] - iorb["latest"]) * 100, 1)}
        s99 = out["series"].get("SOFR99", {})
        if s99.get("status") == "ok":
            rs["sofr99_iorb_bps"] = round((s99["latest"] - iorb["latest"]) * 100, 1)
        srf = out["series"].get("RPONTSYD", {})
        if srf.get("status") == "ok":
            rs["srf_usage_bn"] = srf["latest"]
            rs["srf_date"] = srf["latest_date"]
        out["repo_stress"] = rs
    else:
        out["repo_stress"] = {"status": "unavailable"}
    # T10YIE derive fallback if it failed but DGS10/DFII10 ok
    t = out["series"].get("T10YIE", {})
    if t.get("status") != "ok":
        n, r = out["series"].get("DGS10", {}), out["series"].get("DFII10", {})
        if n.get("status") == "ok" and r.get("status") == "ok":
            out["series"]["T10YIE"] = {"status": "derived", "source": "DGS10 - DFII10",
                                       "latest_date": n["latest_date"],
                                       "latest": round(n["latest"] - r["latest"], 3)}
    # 10Y decomposition (weekly change) if all three have deltas
    d = {}
    for k in ("DGS10", "DFII10", "T10YIE"):
        s = out["series"].get(k, {})
        d[k] = s.get("delta_bps")
    # T10YIE may be level-derived (DGS10 - DFII10) with no daily-history delta;
    # reconstruct its weekly delta from the identity so the third term and driver hold.
    if d["T10YIE"] is None and d["DGS10"] is not None and d["DFII10"] is not None:
        d["T10YIE"] = round(d["DGS10"] - d["DFII10"], 1)
    if all(d[k] is not None for k in ("DGS10", "DFII10")):
        t = d.get("T10YIE")
        if not d["DGS10"] and not d["DFII10"] and not t:
            driver = "none"
        elif abs(t or 0) > abs(d["DFII10"] or 0):
            driver = "breakeven"
        elif abs(d["DFII10"] or 0) > abs(t or 0):
            driver = "real-rate"
        else:
            driver = "mixed"
        note = "weekly change in bps; computed from daily history"
        if any(out["series"].get(k, {}).get("no_new_obs")
               for k in ("DGS10", "DFII10", "T10YIE")):
            note += "; no new observations since the prior run (delta 0 by construction)"
        out["decomposition"] = {
            "d_dgs10_bps": d["DGS10"], "d_dfii10_bps": d["DFII10"],
            "d_t10yie_bps": t, "driver": driver, "note": note,
        }
    else:
        out["decomposition"] = {"status": "unavailable_no_daily_history"}
    print("===MACRO_JSON_START===")
    print(json.dumps(out, ensure_ascii=False, indent=2))
    print("===MACRO_JSON_END===")

if __name__ == "__main__":
    main()

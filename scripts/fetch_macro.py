#!/usr/bin/env python3
"""Deterministic macro-data fetch for the bubble-risk weekly report.

Fetches FRED series (with EIA / US Treasury fallback) via urllib + a custom
User-Agent, computes week-over-week deltas vs the prior-run date, and prints
one JSON block to stdout. Never prints API keys. stdlib only.

Usage: python3 fetch_macro.py <prior_run_date YYYY-MM-DD | none>
"""
import json, os, sys, urllib.request, urllib.error
from datetime import datetime, timedelta

UA = {"User-Agent": "bubble-risk-weekly"}
FRED_KEY = os.environ.get("FRED_API_KEY", "")
EIA_KEY = os.environ.get("EIA_API_KEY", "")
PRIOR = sys.argv[1] if len(sys.argv) > 1 else "none"

# FRED series we want, with unit hint for delta formatting
FRED_SERIES = {
    "DGS10": "pct", "DFII10": "pct", "T10YIE": "pct",
    "BAMLH0A0HYM2": "pct", "BAMLC0A0CM": "pct",
    "DFEDTARU": "pct", "WALCL": "usd_mn", "DCOILWTICO": "usd",
}

def _get(url, timeout=20):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode()

def fred_obs(series_id):
    """Return list of (date, float) desc, newest first. Raises on failure."""
    start = "2025-01-01"
    if PRIOR != "none":
        try:
            start = (datetime.strptime(PRIOR, "%Y-%m-%d") - timedelta(days=21)).strftime("%Y-%m-%d")
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
    year = datetime.utcnow().strftime("%Y")
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
    except (urllib.error.URLError, urllib.error.HTTPError, ValueError, KeyError):
        obs = []
    # fallbacks for the rate series
    if not obs and sid in ("DGS10", "DFII10"):
        try:
            obs = treasury_10y(real=(sid == "DFII10"))
            if obs:
                source = "US Treasury"
        except Exception:
            obs = []
    if not obs and sid == "DCOILWTICO" and EIA_KEY:
        try:
            obs = eia_wti()
            if obs:
                source = "EIA"
        except Exception:
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
        res["delta_bps"] = round(delta * 100, 1) if unit == "pct" else None
        res["delta_abs"] = round(delta, 3)
    return res

def main():
    out = {"prior_run_date": PRIOR, "fred_key_present": bool(FRED_KEY),
           "eia_key_present": bool(EIA_KEY), "series": {}}
    for sid, unit in FRED_SERIES.items():
        out["series"][sid] = series_block(sid, unit)
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
    if all(d[k] is not None for k in ("DGS10", "DFII10")):
        out["decomposition"] = {
            "d_dgs10_bps": d["DGS10"], "d_dfii10_bps": d["DFII10"],
            "d_t10yie_bps": d.get("T10YIE"),
            "driver": ("breakeven" if abs(d.get("T10YIE") or 0) > abs(d["DFII10"] or 0)
                       else "real-rate" if abs(d["DFII10"] or 0) > abs(d.get("T10YIE") or 0)
                       else "mixed"),
            "note": "weekly change in bps; computed from daily history",
        }
    else:
        out["decomposition"] = {"status": "unavailable_no_daily_history"}
    print("===MACRO_JSON_START===")
    print(json.dumps(out, ensure_ascii=False, indent=2))
    print("===MACRO_JSON_END===")

if __name__ == "__main__":
    main()

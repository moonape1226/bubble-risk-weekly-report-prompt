#!/usr/bin/env python3
"""Eval-only: run scripts/fetch_macro.py as if it executed on a past date.

Usage: python3 evals/judgment/asof_fetch.py <run-date YYYY-MM-DD> <prior-run-date|none>

Production code is untouched. The wrapper freezes the fetcher's clock at
<run-date> 09:30 Asia/Taipei and rewrites each upstream request/response so no
observation published after the cutoff (run-date minus one day, i.e. the US
evening before a Taipei-morning run) is visible:

- FRED: observation_end + realtime_start/realtime_end (ALFRED vintage as of cutoff)
- EIA: end=<cutoff>
- Treasury XML: entries dated after cutoff removed
- CFTC TFF: rows whose Tuesday report date + 3 days (Friday release) > cutoff removed
- Yahoo ^MOVE: range=3mo replaced by period1/period2 ending at cutoff
- OFR STFM: aggregation points after cutoff removed

Prints the fetcher's complete marker-delimited artifact unchanged otherwise.
"""
import datetime as _dt
import importlib.util
import io
import json
import os
import re
import sys
import urllib.error
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_env():
    env = ROOT / ".env"
    if not env.exists():
        return
    for line in env.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def main():
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    run_date, prior = sys.argv[1], sys.argv[2]
    run_day = _dt.datetime.strptime(run_date, "%Y-%m-%d").date()
    cutoff = (run_day - _dt.timedelta(days=1)).isoformat()
    taipei = _dt.timezone(_dt.timedelta(hours=8))
    frozen = _dt.datetime(run_day.year, run_day.month, run_day.day, 9, 30, tzinfo=taipei)

    load_env()
    sys.argv = [str(ROOT / "scripts" / "fetch_macro.py"), prior]
    spec = importlib.util.spec_from_file_location("fetch_macro", ROOT / "scripts" / "fetch_macro.py")
    fm = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fm)

    class FrozenDatetime(_dt.datetime):
        @classmethod
        def now(cls, tz=None):
            return frozen.astimezone(tz) if tz else frozen.replace(tzinfo=None)

    fm.datetime = FrozenDatetime
    fm.execution_now = lambda: frozen

    def real_get_bytes(url, timeout=20):
        # Build-time rate limiting (FRED: 120 req/min) must not masquerade as a
        # genuine outage: retry 429/5xx with jittered backoff before giving up.
        import random
        import time
        for attempt in range(5):
            try:
                return fm_get_bytes(url, timeout)
            except urllib.error.HTTPError as e:
                if e.code != 429 and e.code < 500 or attempt == 4:
                    raise
            time.sleep(2 ** attempt + random.random())

    fm_get_bytes = fm._get_bytes

    def cftc_visible(report_day):
        try:
            d = _dt.date.fromisoformat(report_day)
        except ValueError:
            return True
        return (d + _dt.timedelta(days=3)).isoformat() <= cutoff

    def filter_cftc_text(text):
        keep = []
        for line in text.splitlines(keepends=True):
            parts = line.split(",")
            # f[2] is the ISO report date (see memory: cftc-date-format-iso)
            day = parts[2].strip().strip('"') if len(parts) > 2 else ""
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", day) and not cftc_visible(day):
                continue
            keep.append(line)
        return "".join(keep)

    # Degraded-case injection: ASOF_FAIL=SID1,SID2,... makes those FRED series
    # (or a host keyword such as "yahoo", "cftc", "financialresearch") fail as a
    # network error, so the fetcher's own degradation path produces the artifact.
    fail = {x.strip() for x in os.environ.get("ASOF_FAIL", "").split(",") if x.strip()}
    obs_end_map = dict(x.split("=", 1) for x in os.environ.get("ASOF_OBS_END", "").split(",") if "=" in x)

    def patched_get_bytes(url, timeout=20):
        sid_m = re.search(r"series_id=([^&]+)", url)
        if (sid_m and sid_m.group(1) in fail) or any(h in url for h in fail if h.islower()):
            raise urllib.error.URLError("asof_fetch: injected failure")
        if "api.stlouisfed.org/fred/series/observations" in url:
            # Per-series observation_end from the archived run's own Raw data
            # (ASOF_OBS_END=SID=YYYY-MM-DD,...) reproduces what that run saw;
            # series it did not record fall back to the generic cutoff.
            obs_end = obs_end_map.get(sid_m.group(1), cutoff)
            rt = max(cutoff, obs_end)
            try:
                return real_get_bytes(
                    url + f"&observation_end={obs_end}&realtime_start={rt}&realtime_end={rt}", timeout)
            except urllib.error.HTTPError as e:
                if e.code != 400 or b"does not exist in ALFRED" not in e.read():
                    raise
            # Licensed series (e.g. SP500) have no vintages. observation_end=cutoff
            # matched the date the run actually saw in 4 of 5 archived runs
            # checked (08-31..11-08); per-case fidelity is measured by build_cases.
            print(f"asof_fetch: {sid_m.group(1)} not in ALFRED; observation_end={obs_end} (no vintage)",
                  file=sys.stderr)
            return real_get_bytes(url + f"&observation_end={obs_end}", timeout)
        if "api.eia.gov" in url:
            return real_get_bytes(url + f"&end={cutoff}", timeout)
        if "home.treasury.gov" in url:
            xml = real_get_bytes(url, timeout).decode()

            def drop_late(m):
                d = re.search(r"<d:NEW_DATE\b[^>]*>([^<]+)", m.group(0))
                return "" if d and d.group(1)[:10] > cutoff else m.group(0)

            return re.sub(r"<entry(?:\s[^>]*)?>.*?</entry>", drop_late, xml, flags=re.S).encode()
        if "cftc.gov/files/dea/history" in url:
            raw = real_get_bytes(url, timeout)
            zin = zipfile.ZipFile(io.BytesIO(raw))
            buf = io.BytesIO()
            with zipfile.ZipFile(buf, "w") as zout:
                for name in zin.namelist():
                    data = zin.read(name)
                    if name == "FinFutYY.txt":
                        data = filter_cftc_text(data.decode("latin-1")).encode("latin-1")
                    zout.writestr(name, data)
            return buf.getvalue()
        if "cftc.gov/dea/newcot" in url:
            return filter_cftc_text(real_get_bytes(url, timeout).decode("latin-1")).encode("latin-1")
        if "finance.yahoo.com" in url:
            end = _dt.datetime.combine(_dt.date.fromisoformat(cutoff) + _dt.timedelta(days=1),
                                       _dt.time(), tzinfo=_dt.timezone.utc)
            start = end - _dt.timedelta(days=92)
            url = url.replace("range=3mo", f"period1={int(start.timestamp())}&period2={int(end.timestamp())}")
            return real_get_bytes(url, timeout)
        if "data.financialresearch.gov" in url:
            data = json.loads(real_get_bytes(url, timeout))
            for series in data.values():
                agg = series.get("timeseries", {}).get("aggregation")
                if isinstance(agg, list):
                    series["timeseries"]["aggregation"] = [
                        p for p in agg
                        if not (isinstance(p, (list, tuple)) and isinstance(p[0], str) and p[0] > cutoff)
                    ]
            return json.dumps(data).encode()
        raise RuntimeError(f"asof_fetch: unhandled upstream URL host: {url.split('?')[0]}")

    fm._get_bytes = patched_get_bytes
    fm.main()


if __name__ == "__main__":
    main()

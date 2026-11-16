#!/usr/bin/env python3
"""Build frozen evidence bundles for the judgment-layer eval.

Usage: python3 evals/judgment/build_cases.py <archive-dir> [--only CASE_ID ...]

<archive-dir> holds report-YYYY-MM-DD/{report.md,score.json} pulled from the
archive repo. Output:

  evals/judgment/cases/<case_id>/   visible to the model under test
      macro.txt          complete marker-delimited artifact (asof_fetch.py)
      evidence.md        non-API evidence from that run's appendix, neutralised
      prior.json         which prior run exists and its format (legacy score / none / forecast)
      prior_forecast.json  synthetic forecast prior (flip-* cases only)
  evals/judgment/reference/<case_id>/   NEVER visible to the model under test
      score.json, report.md   archived output of the real run (model-derived)
      meta.json               tags, fidelity of macro reconstruction, provenance

Only runs whose appendix is source-keyed (2026-07-16 onward) are replayable.
"""
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CASES, REF = HERE / "cases", HERE / "reference"

MARKER = re.compile(r"\[[a-z0-9_]+\]\s*")
NEUTRAL_STATUS = {
    "✓ SEARCH-VERIFIED": "searched: in-window result found (see search results)",
    "✓ DIRECT": "direct fetch succeeded (see direct values)",
    "✗ NOT DISCLOSED": "searched: completed, no in-window disclosure found",
    "⛔ FETCH FAILED": "search/fetch attempted: technical failure, no result",
}

# Synthetic degraded variants: (case_id, base date, prior override, ASOF_FAIL,
# evidence edit, tag, description). Bases are real replay cases.
DEGRADED = [
    ("deg-baseline", "2026-11-08", "none", "", None, "baseline",
     "No prior run at all: baseline deltas, 前次結論：無前次（基準）."),
    ("deg-fred-down", "2026-11-08", None, "ALL_FRED", None, "fred-down",
     "FRED key unusable: all FRED series fail incl. NASDAQ100, so R1 is unavailable; Treasury/EIA fallbacks only."),
    ("deg-sp500-fail", "2026-09-13", None, "SP500", None, "comove-unavailable",
     "SP500 fails: no 200-DMA deviation, vix_spx_comove unavailable; R1 still computable."),
    ("deg-repo-partial", "2026-11-08", None, "SOFR99,RPONTTLD", None, "repo-partial",
     "repo_stress keeps only usable legs; composite `all` aggregation unsatisfied; funding-stress evidence partial."),
    ("deg-ig-oas-fail", "2026-10-18", None, "BAMLC0A0CM", None, "required-source-missing",
     "Required IG OAS fails: must be FETCH FAILED, never cited, and weighed in 資料缺漏 for R3."),
    ("deg-t10yie-derived", "2026-09-13", None, "T10YIE", None, "derived-breakeven",
     "T10YIE fails: derived from DGS10-DFII10 on a shared date (status derived)."),
    ("deg-search-gaps", "2026-11-08", None, "", "drop_search", "search-missing",
     "Search evidence missing for analyst TP + hyperscaler financing (R2/R3 inputs): no fabrication, gap weighed."),
    ("deg-zero-screens", "2026-08-13", None, "", "zero_screens", "zero-result",
     "Eligible zero-result screens completed with zero hits: success, not NOT DISCLOSED."),
]
# Flip-discipline subset: a replay re-run with a synthetic forecast prior whose
# answer is "yes", dated the real previous run. Keeping yes or flipping to no
# must follow the flip rule (cited evidence dated after the prior run).
FLIP_DATES = ("2026-07-20", "2026-08-06", "2026-08-24", "2026-09-13", "2026-10-18", "2026-11-08")
FLIP_PRIOR_ANSWER = "yes"
DROP_SEARCH = ("valuation.analyst_tp_decomposition", "ai.hyperscaler_financing_mix")
ZERO_SCREENS = ("speculation.ai_rename_spac", "speculation.microcap_moonshots",
                "speculation.insider_form4", "structural.us_single_stock_etf")
FRED_ROW = re.compile(r"FRED (?:series=)?([A-Z0-9]+)")


def run_obs_dates(md):
    """Latest observation date per FRED series as recorded by the archived run."""
    seen = {}
    for c in table(md, "### Raw data", "### Coverage"):
        m = FRED_ROW.match(c[3]) if len(c) > 4 else None
        if m and re.fullmatch(r"\d{4}-\d{2}-\d{2}", c[4]):
            seen[m.group(1)] = max(seen.get(m.group(1), ""), c[4])
    return seen


def table(md, start, stop):
    sec = md.split(start, 1)[1].split(stop, 1)[0]
    rows = []
    for line in sec.splitlines():
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and cells[0] != "source_id":
            rows.append(cells)
    return rows


def evidence_md(date, md, edit=None):
    raw = table(md, "### Raw data", "### Coverage")
    cov = table(md, "### Coverage", "### SEARCH-VERIFIED traceability")
    sv = table(md, "### SEARCH-VERIFIED traceability", "## 本次分數存檔")
    out = [f"# Frozen evidence for run date {date}",
           "",
           "Results of the web searches and direct fetches performed for this run. Treat each row as the",
           "complete output of that search/fetch; nothing else was found. Values are quoted from sources;",
           "classification and status labels are yours to decide.",
           "", "## Search / fetch outcomes", "",
           "| source_id | source bullet | method | outcome |", "|---|---|---|---|"]
    dropped = set()
    for c in cov:
        if len(c) < 4 or "API" in c[3]:
            continue
        sid, status = c[0], c[3]
        key = next((k for k in NEUTRAL_STATUS if status.startswith(k)), None)
        outcome = NEUTRAL_STATUS.get(key, f"unrecognised archived status: {status}")
        comp = re.search(r"components=(\S+)", status)
        if comp:
            outcome += f" (components: {comp.group(1).replace('not_disclosed', 'none_found')})"
        if edit == "drop_search" and sid in DROP_SEARCH:
            outcome, dropped = NEUTRAL_STATUS["⛔ FETCH FAILED"], dropped | {sid}
        if edit == "zero_screens" and sid in ZERO_SCREENS:
            outcome = "searched: screen completed successfully with zero matching results"
            dropped |= {sid}
        method = re.sub(r"[（(].*?[）)]", "", c[2]).strip()
        out.append(f"| {sid} | {c[1]} | {method} | {outcome} |")
    out += ["", "## Search results", "",
            "| source_id | finding | search query | result URL / source | published / data date |",
            "|---|---|---|---|---|"]
    for c in sv:
        if len(c) < 5 or c[0] in dropped:
            continue
        out.append(f"| {c[0]} | {MARKER.sub('', c[1])} | {c[2]} | {c[3]} | {c[4]} |")
    out += ["", "## Direct-fetch values (non-API)", "",
            "| source_id | item | value | source URL | data date |", "|---|---|---|---|---|"]
    for c in raw:
        if len(c) < 5 or "FRED" in c[3] or "derived" in c[1] or "derived" in c[3] \
                or "衍生" in c[3] or not c[3].startswith("http") or c[0] in dropped:
            continue
        out.append(f"| {c[0]} | {MARKER.sub('', c[1])} | {c[2]} | {c[3]} | {c[4]} |")
    return "\n".join(out) + "\n"


def macro_fidelity(macro_txt, md):
    body = macro_txt.split("===MACRO_JSON_START===")[1].split("===MACRO_JSON_END===")[0]
    art = json.loads(body)
    have = {k: (b.get("latest_date"), b.get("latest")) for k, b in art["series"].items()
            if b.get("status") in ("ok", "derived")}
    sp = art.get("sp500_trend", {})
    if sp.get("status") == "ok":
        have["SP500"] = (sp["latest_date"], sp["latest"])
    same = date_diff = value_diff = 0
    diffs = []
    latest = run_obs_dates(md)
    for c in table(md, "### Raw data", "### Coverage"):
        m = FRED_ROW.match(c[3]) if len(c) > 4 else None
        if not m or m.group(1) not in have or c[4] != latest.get(m.group(1)) \
                or re.search(r"yoy|chg|delta|prior|ma200|ma52w|dev|base|streak|Δ", c[1], re.I):
            continue
        try:
            rv = float(c[2].replace(",", "").split()[0])
        except ValueError:
            continue
        d, v = have[m.group(1)]
        if c[4] != d:
            date_diff += 1
            diffs.append(f"{m.group(1)} run={c[4]} replay={d}")
        elif abs(rv - v) > max(0.011, abs(v) * 5e-4):
            value_diff += 1
            diffs.append(f"{m.group(1)} {c[4]} run={rv} replay={v}")
        else:
            same += 1
    statuses = {k: b.get("status") for k, b in art["series"].items()}
    failed = sorted(k for k, s in statuses.items() if s not in ("ok", "derived"))
    for k in ("sp500_trend", "cftc_lev_funds", "move_index", "ofr_repo", "repo_stress", "vix_spx_comove"):
        if art.get(k, {}).get("status") not in ("ok", "derived"):
            failed.append(k)
    fallback = sorted(k for k, b in art["series"].items()
                      if b.get("status") == "ok" and b.get("source") not in (None, "FRED API"))
    return {"same": same, "date_diff": date_diff, "value_diff": value_diff,
            "diffs": diffs, "non_ok": failed, "fallback_source": fallback}


def fetch(date, prior, fail="", obs_end=None):
    env = dict(os.environ)
    env["ASOF_OBS_END"] = ",".join(f"{k}={v}" for k, v in (obs_end or {}).items())
    env["ASOF_FAIL"] = fail if fail != "ALL_FRED" else ""
    if fail == "ALL_FRED":
        env["FRED_API_KEY"] = ""
    p = subprocess.run([sys.executable, str(HERE / "asof_fetch.py"), date, prior],
                       capture_output=True, text=True, env=env, timeout=600)
    if p.returncode != 0 or "===MACRO_JSON_END===" not in p.stdout:
        raise RuntimeError(f"asof_fetch {date} failed: {p.stderr[-500:]}")
    return p.stdout, p.stderr.strip()


# US bond-market holidays in the replay window (SIFMA): a holiday between the
# prior run and this run thins the delta window.
US_HOLIDAYS = ("2026-07-03", "2026-09-07", "2026-10-12", "2026-11-11")


def ndx_bucket(macro_txt):
    body = macro_txt.split("===MACRO_JSON_START===")[1].split("===MACRO_JSON_END===")[0]
    ndx = json.loads(body).get("ndx_drawdown", {})
    if ndx.get("status") != "ok":
        return None, "r1:unavailable"
    dd = ndx["drawdown_pct"]
    return dd, "r1:<5%" if dd < 5 else "r1:5-15%" if dd < 15 else "r1:>=15%"


def tags_for(date, prior, prior_kind, bucket):
    t = [f"prior:{prior_kind}", bucket]
    if prior != "none" and any(prior < h <= date for h in US_HOLIDAYS):
        t.append("holiday-gap")
    return t


def synthetic_prior_forecast(prior_date, contract, r1_drawdown_pct):
    from datetime import date as _d, timedelta
    day = _d.fromisoformat(prior_date)
    iso = day.isocalendar()
    return {
        "date": prior_date, "iso_week": f"{iso[0]}-W{iso[1]:02d}",
        "weekday": day.strftime("%A"), "timezone": contract["timezone"],
        "question_version": contract["question"]["version"],
        "resolution_version": contract["resolution"]["version"],
        "answer": FLIP_PRIOR_ANSWER,
        "horizon_end": (day + timedelta(days=contract["question"]["horizon_days"])).isoformat(),
        "prior_date": None, "prior_answer": None, "flip_evidence": [],
        "r1_drawdown_pct": r1_drawdown_pct, "resolution": None,
    }


def main():
    archive = Path(sys.argv[1])
    only = set(sys.argv[sys.argv.index("--only") + 1:]) if "--only" in sys.argv else None
    dates = sorted(p.name[7:] for p in archive.glob("report-*"))
    keyed = [d for d in dates if "| source_id | 指標" in (archive / f"report-{d}/report.md").read_text()]
    prev = {d: dates[i - 1] if i else "none" for i, d in enumerate(dates)}
    jobs = [(f"replay-{d}", d, prev[d], "", None, "replay", "Historical replay.") for d in keyed]
    jobs += [(cid, base, pr if pr else prev[base], fail, edit, tag, desc)
             for cid, base, pr, fail, edit, tag, desc in DEGRADED]
    jobs += [(f"flip-{d}", d, prev[d], "", None, "flip",
              f"Replay with a synthetic forecast prior answering {FLIP_PRIOR_ANSWER} on {prev[d]}: "
              "keep it, or flip only with cited evidence dated after the prior run.")
             for d in FLIP_DATES]
    contract = json.loads((HERE.parents[1] / "report_contract.json").read_text())
    for cid, date, prior, fail, edit, tag, desc in jobs:
        if only and cid not in only:
            continue
        md = (archive / f"report-{date}/report.md").read_text()
        cdir, rdir = CASES / cid, REF / cid
        for d in (cdir, rdir):
            shutil.rmtree(d, ignore_errors=True)
            d.mkdir(parents=True)
        macro, fetch_log = fetch(date, prior, fail, run_obs_dates(md))
        (cdir / "macro.txt").write_text(macro)
        ev = evidence_md(date, md, edit)
        (cdir / "evidence.md").write_text(ev)
        prior_kind = "none" if prior == "none" else "forecast-yes" if tag == "flip" else "legacy"
        (cdir / "prior.json").write_text(json.dumps({
            "prior_date": None if prior == "none" else prior,
            "prior_format": {"none": "no prior run (baseline)",
                             "legacy": "legacy score.json report (no forecast)",
                             "forecast-yes": "forecast.json (see prior_forecast.json)"}[prior_kind],
        }, ensure_ascii=False, indent=2) + "\n")
        if tag == "flip":
            (cdir / "prior_forecast.json").write_text(json.dumps(
                synthetic_prior_forecast(prior, contract, json.loads((REF / f"replay-{prior}" / "meta.json").read_text())["ndx_drawdown_pct"]), ensure_ascii=False, indent=2) + "\n")
        drawdown, bucket = ndx_bucket(macro)
        shutil.copy(archive / f"report-{date}/score.json", rdir / "score.json")
        shutil.copy(archive / f"report-{date}/report.md", rdir / "report.md")
        fid = macro_fidelity(macro, md)
        meta = {"case_id": cid, "run_date": date, "prior_date": prior, "kind": tag,
                "prior_kind": prior_kind, "ndx_drawdown_pct": drawdown,
                "description": desc, "asof_fail": fail, "evidence_edit": edit,
                "tags": ([tag] if tag in ("replay", "flip") else ["degraded", tag])
                + tags_for(date, prior, prior_kind, bucket),
                "reference": "archived production output (model-derived, not human-verified)",
                "macro_fidelity": fid, "fetch_log": fetch_log}
        (rdir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n")
        print(f"{cid}: prior={prior} fidelity same={fid['same']} date_diff={fid['date_diff']} "
              f"value_diff={fid['value_diff']} non_ok={','.join(fid['non_ok']) or '-'} "
              f"fallback={','.join(fid['fallback_source']) or '-'} "
              f"evidence_rows={ev.count(chr(10) + '| ')}")


if __name__ == "__main__":
    main()

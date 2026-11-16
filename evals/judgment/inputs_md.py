#!/usr/bin/env python3
"""Render evals/judgment/inputs.md: the case set for human review (inputs sign-off)."""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent


def outcome_counts(ev):
    sec = ev.split("## Search / fetch outcomes", 1)[1].split("## Search results", 1)[0]
    counts = {}
    for line in sec.splitlines():
        if line.startswith("| ") and not line.startswith("| source_id"):
            o = line.rstrip(" |").rsplit("| ", 1)[-1]
            o = re.sub(r" \(.*", "", o)
            counts[o] = counts.get(o, 0) + 1
    return counts


def main():
    metas = [json.loads(p.read_text()) for p in sorted((HERE / "reference").glob("*/meta.json"))]
    order = {"replay": 0, "flip": 1}
    metas.sort(key=lambda m: (order.get(m["kind"], 2), m["case_id"]))
    lines = ["# Judgment-layer eval: input set", "",
             f"{len(metas)} cases: {sum(m['kind'] == 'replay' for m in metas)} historical replays "
             f"(every archived run with a source-keyed appendix, 2026-07-16 onward), "
             f"{sum(m['kind'] == 'flip' for m in metas)} flip-discipline variants (same replay, synthetic "
             f"forecast prior answering yes) and "
             f"{sum(m['kind'] not in ('replay', 'flip') for m in metas)} degraded variants.",
             "",
             "Question under test: 自報告日起 182 天內，AI 泡沫是否破裂？ (yes/no). No case has a known "
             "answer yet (earliest window ends 2027-01-14), so there is no gold label; grading is "
             "validator + rubric + cross-date consistency.",
             "",
             "Each case = `cases/<id>/macro.txt` (as-of fetcher artifact) + `cases/<id>/evidence.md` "
             "(that run's non-API search/fetch results, status labels neutralised) + `cases/<id>/prior.json` "
             "(+ `prior_forecast.json` for flip cases). "
             "The archived production output for comparison sits in `reference/<id>/` and is never shown to the model.",
             "",
             "Macro fidelity = FRED latest-level rows in the archived report reproduced by the replay "
             "(same date and value / differing).",
             "",
             "| id | tags | prior | NDX drawdown % | macro fidelity | non-ok macro blocks | evidence outcomes (found / none / failed / direct) |",
             "|---|---|---|---|---|---|---|"]
    for m in metas:
        ev = (HERE / "cases" / m["case_id"] / "evidence.md").read_text()
        c = outcome_counts(ev)
        f = m["macro_fidelity"]
        lines.append(
            f"| {m['case_id']} | {', '.join(m['tags'])} | {m['prior_date']} ({m['prior_kind']}) | "
            f"{m['ndx_drawdown_pct'] if m['ndx_drawdown_pct'] is not None else 'unavailable'} | "
            f"{f['same']} same / {f['date_diff'] + f['value_diff']} diff | {', '.join(f['non_ok']) or '-'}"
            f"{' (fallback: ' + ', '.join(f['fallback_source']) + ')' if f['fallback_source'] else ''} | "
            f"{c.get('searched: in-window result found', 0)} / {c.get('searched: completed, no in-window disclosure found', 0)}"
            f" / {c.get('search/fetch attempted: technical failure, no result', 0)}"
            f" / {c.get('direct fetch succeeded', 0)} |")
    lines += ["", "## Per case", ""]
    for m in metas:
        f = m["macro_fidelity"]
        lines += [f"### {m['case_id']}", "",
                  f"- run date {m['run_date']}, prior {m['prior_date']}; {m['description']}",
                  f"- injected macro failure: `{m['asof_fail'] or 'none'}`; evidence edit: `{m['evidence_edit'] or 'none'}`",
                  f"- macro differences vs archived run: {'; '.join(f['diffs']) or 'none'}",
                  f"- prior: {m['prior_kind']}"
                  + (" — synthetic forecast prior answering yes, see `prior_forecast.json`" if m["kind"] == "flip" else ""),
                  f"- files: `cases/{m['case_id']}/evidence.md`, `cases/{m['case_id']}/macro.txt`, `cases/{m['case_id']}/prior.json`", ""]
    (HERE / "inputs.md").write_text("\n".join(lines) + "\n")
    print(f"wrote {HERE / 'inputs.md'} ({len(metas)} cases)")


if __name__ == "__main__":
    main()

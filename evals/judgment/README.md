# Judgment-layer eval (forecast-judgment)

Gates changes to `bubble-risk-weekly-prompt.md` / `report_contract.json` / `scripts/validate_report.py`. Each case replays one archived run as a frozen bundle (as-of fetcher artifact + that run's search results) and has headless `claude -p` (Opus 5.5) execute the prompt in `MODE: DRY-RUN` with no network. No case has a known answer yet (earliest 182-day window ends 2027-01-14), so grading is validator + rubric + set-level consistency, not accuracy.

## Files

- `cases/<id>/` — what the model sees: `macro.txt`, `evidence.md`, `prior.json`, and `prior_forecast.json` for flip cases. `reference/<id>/` holds the archived report and `meta.json` (never shown to the model). `inputs.md` lists all 32 cases.
- `build_cases.py` / `inputs_md.py` — rebuild the cases from a local copy of the archive repo (refetches FRED/Treasury/etc. as of each run date) and regenerate `inputs.md`.
- `run_eval.mjs` — runner (from the build-eval scaffold). Writes `.claude/hillclimb/forecast-judgment/<variant>/results.jsonl`, `errors.jsonl`, `out/<id>_rep<k>/{report.md,forecast.json}` and `traces/` (gitignored).
- `summarize.py` — set-level metrics into `<variant>/summary.json`.
- `canary/run.sh` — judge sanity check: an "I don't know" report and a wrong-question report must both score low.

## Isolation

`evidence.md` is untrusted web-search text, so the model under test runs with `--permission-mode dontAsk` and Claude Code's Bash sandbox (writes confined to the temp workspace, no network, no unsandboxed fallback). File tools may write only `report.md` and `forecast.json`. Grading never reads the workspace except those two files: the validator runs from the repo against the repo's prompt, contract and case files in a fresh directory, and so does the judge. If the model changed any app or case file in its workspace copy, the row records `tampered` and `valid` is 0. The 2026-11-16 baseline ran before this lock-down (the model's Bash was effectively unrestricted); its 64 outputs were re-validated with the repo validator and case files and matched every recorded `valid`.

## Metrics

Per case: `valid` (validator exit 0 on the final files), `first_pass` (the model's first validator call passed), `judgment` (share of applicable criteria passed by a Sonnet 5.5 judge: path_status, no_fabrication, both_sides, decision, gaps, flip), `yes`. Set level (`summarize.py`): yes rate, anchoring (flip case answer equals its replay twin's answer), rep agreement, answer changes across replay dates.

## Run

```sh
node evals/judgment/run_eval.mjs --flow .claude/hillclimb/forecast-judgment --variant v1 --model claude-opus-5-5 --reps 2 --concurrency 5 --timeout-s 2700
python3 evals/judgment/summarize.py .claude/hillclimb/forecast-judgment/v1
```

Start only one copy at a time: two concurrent runs on the same variant both run every missing case and overwrite each other's traces. A changed prompt, contract, validator or runner changes the harness sha; the runner then refuses until a human re-runs it with `--approve-harness`. Results resume per (case, rep); rerunning the same command fills in only missing rows. Measured cost: about $2.08 per case-rep (range $1.32–2.50), so 32 × 2 ≈ $130 and about 70 minutes at concurrency 5.

## Baseline (2026-11-16, prompt at adc0824)

64/64 ok. valid 1.000, first_pass 0.031, judgment 0.777, yes 0.188. Anchoring 2/12: with a synthetic prior answering yes, the model keeps yes in 10 of 12 flip runs, while the same evidence without a forecast prior gives no in all 36 replay runs. Rep agreement 30/32; no answer changes across the 18 replay dates. Most common judge failure: no_fabrication (claims not in the inputs, e.g. historical margin-debt benchmarks).

`baseline/` side files: `results.flip-r1null.jsonl` holds the first flip run, made when the synthetic prior had `r1_drawdown_pct: null` (the model used that null as "new evidence" to flip; superseded). `results.dup.jsonl` holds 20 duplicate rows from two overlapping reruns. `errors.superseded.jsonl` holds 43 usage-limit failures, each later rerun successfully.

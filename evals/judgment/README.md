# Judgment-layer eval (forecast-judgment)

Gates changes to `bubble-risk-weekly-prompt.md` / `report_contract.json` / `scripts/validate_report.py`. Each case replays one archived run as a frozen bundle (as-of fetcher artifact + that run's search results) and has headless `claude -p` (Opus 5.5) execute the prompt in `MODE: DRY-RUN` with no network. No case has a known answer yet (earliest 182-day window ends 2027-01-14), so grading is validator + rubric + set-level consistency, not accuracy.

## Files

- `cases/<id>/` — what the model sees: `macro.txt`, `evidence.md`, `prior.json`, and `prior_forecast.json` for flip cases. `reference/<id>/` holds the archived report and `meta.json` (never shown to the model). `inputs.md` lists all 32 cases.
- `build_cases.py` / `inputs_md.py` — rebuild the cases from a local copy of the archive repo (refetches FRED/Treasury/etc. as of each run date) and regenerate `inputs.md`.
- `run_eval.mjs` — runner (from the build-eval scaffold). Writes `.claude/hillclimb/forecast-judgment/<variant>/results.jsonl`, `errors.jsonl`, `out/<id>_rep<k>/{report.md,forecast.json}` and `traces/` (gitignored).
- `summarize.py` — set-level metrics into `<variant>/summary.json`.
- `canary/run.sh` — judge sanity check: an "I don't know" report and a wrong-question report must both score low.

## Isolation

`evidence.md` is untrusted web-search text, so the model under test runs with `--permission-mode dontAsk`, sandbox settings (no network, no home reads, no unsandboxed fallback), file reads limited to the workspace (`Read/Glob/Grep(./**)`, `Read(~/**)` denied) and file writes limited to `report.md` and `forecast.json`. Observed on 2026-11-16 (Claude Code 2.1.325): Bash effectively allows only the built-in read-only commands (`ls`, `cat`, ...) and the exact validator command; compound commands and python heredocs are denied, so sandbox auto-allow did not take effect. That is stricter than the production routine, which has full Bash. Outputs are read only as regular files (a symlinked or hard-linked `report.md` is refused and marked tampered). Grading never reads the workspace except those two files: the validator runs from the repo against the repo's prompt, contract and case files in a fresh directory, and so does the judge. If the model changed any app or case file in its workspace copy, the row records `tampered` and `valid` is 0. The 2026-11-16 baseline ran before this lock-down (the model's Bash was effectively unrestricted); its 64 outputs were re-validated with the repo validator and case files and matched every recorded `valid`.

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

## Flip-rule comparison (2026-11-17, flow `.claude/hillclimb/forecast-flip-rule`)

All variants ran on claude-opus-5-5 under the locked-down runner. `baseline` is the prompt at 7b06fad (symmetric flip rule). `v1` makes the flip rule asymmetric and adds `yes_basis` (diff kept as `v1.patch`). `v2` = v1 plus the anti-fabrication change (removes the prompt's own unsourced margin-debt "+40–50% at 1999/2007/2021 tops" benchmark, which the judge cannot see and scored as fabrication; rule 6 now covers historical benchmarks and company financials). `v3` = v2 with the final runner (judge `flip` criterion rewritten to the asymmetric rule; `harness_paths` resolved against the runner's repo; API error text and status read from the result event).

| | baseline | v1 | v2 | v3 |
|---|---|---|---|---|
| cases × reps | 14 × 2 | 14 × 2 | 6 × 2 | 26 × 1 |
| valid | 26/28 | 28/28 | 11/12 | 26/26 |
| anchoring (flip answer = replay answer) | 2/11 | 10/12 | 5/5 | — |
| decision fails | 6 | 0 | 0 | 0 |
| no_fabrication fails | 6 | 14 | 1 | 0 |
| judgment excluding `flip` | 0.835 | 0.800 | 0.904 | 0.967 |

On the 12 case-reps v2 shares with the others (flip and replay 07-20, 08-06, 08-24), no_fabrication fails were 5 / 11 / 1 for baseline / v1 / v2. v3 covers the remaining 26 of the 32 cases; against the original 64-run baseline on the same cases (rep0 / rep1): no_fabrication fails 12 / 12 → 0, decision fails 2 / 1 → 0, yes answers 3 / 5 → 0, where the original yes answers were the three flip cases (anchoring) plus one rep each of the borderline deg-baseline and deg-repo-partial. The judge's `flip` criterion in baseline–v2 still encoded the symmetric rule, so v1/v2 `flip` fails are expected and excluded above. The two invalid rows in baseline and one in v2 fail on appendix formatting unrelated to the flip rule. Per-variant results, summaries and model outputs are committed; traces are not.

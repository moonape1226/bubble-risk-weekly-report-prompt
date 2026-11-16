# Judgment-layer eval: input set

32 cases: 18 historical replays (every archived run with a source-keyed appendix, 2026-07-16 onward), 6 flip-discipline variants (same replay, synthetic forecast prior answering yes) and 8 degraded variants.

Question under test: 自報告日起 182 天內，AI 泡沫是否破裂？ (yes/no). No case has a known answer yet (earliest window ends 2027-01-14), so there is no gold label; grading is validator + rubric + cross-date consistency.

Each case = `cases/<id>/macro.txt` (as-of fetcher artifact) + `cases/<id>/evidence.md` (that run's non-API search/fetch results, status labels neutralised) + `cases/<id>/prior.json` (+ `prior_forecast.json` for flip cases). The archived production output for comparison sits in `reference/<id>/` and is never shown to the model.

Macro fidelity = FRED latest-level rows in the archived report reproduced by the replay (same date and value / differing).

| id | tags | prior | NDX drawdown % | macro fidelity | non-ok macro blocks | evidence outcomes (found / none / failed / direct) |
|---|---|---|---|---|---|---|
| replay-2026-07-16 | replay, prior:legacy, r1:<5% | 2026-07-13 (legacy) | 3.78 | 7 same / 0 diff | - | 31 / 10 / 0 / 0 |
| replay-2026-07-20 | replay, prior:legacy, r1:5-15% | 2026-07-16 (legacy) | 6.74 | 7 same / 0 diff | - | 30 / 11 / 0 / 0 |
| replay-2026-07-23 | replay, prior:legacy, r1:5-15% | 2026-07-20 (legacy) | 5.42 | 7 same / 0 diff | - | 34 / 7 / 0 / 0 |
| replay-2026-07-27 | replay, prior:legacy, r1:5-15% | 2026-07-23 (legacy) | 8.26 | 7 same / 0 diff | - | 34 / 7 / 0 / 0 |
| replay-2026-07-30 | replay, prior:legacy, r1:5-15% | 2026-07-27 (legacy) | 11.31 | 7 same / 0 diff | - | 34 / 7 / 0 / 0 |
| replay-2026-08-03 | replay, prior:legacy, r1:5-15% | 2026-07-30 (legacy) | 7.78 | 7 same / 0 diff | - | 31 / 10 / 0 / 0 |
| replay-2026-08-06 | replay, prior:legacy, r1:<5% | 2026-08-03 (legacy) | 3.83 | 7 same / 0 diff | - | 32 / 9 / 0 / 0 |
| replay-2026-08-10 | replay, prior:legacy, r1:<5% | 2026-08-06 (legacy) | 3.06 | 7 same / 0 diff | - | 30 / 11 / 0 / 0 |
| replay-2026-08-13 | replay, prior:legacy, r1:<5% | 2026-08-10 (legacy) | 2.99 | 7 same / 0 diff | - | 31 / 10 / 0 / 0 |
| replay-2026-08-17 | replay, prior:legacy, r1:<5% | 2026-08-13 (legacy) | 2.0 | 7 same / 0 diff | - | 32 / 9 / 0 / 0 |
| replay-2026-08-20 | replay, prior:legacy, r1:<5% | 2026-08-17 (legacy) | 4.03 | 22 same / 0 diff | - | 28 / 13 / 0 / 0 |
| replay-2026-08-24 | replay, prior:legacy, r1:<5% | 2026-08-20 (legacy) | 4.41 | 21 same / 0 diff | - | 27 / 14 / 0 / 0 |
| replay-2026-08-27 | replay, prior:legacy, r1:<5% | 2026-08-24 (legacy) | 4.68 | 21 same / 0 diff | - | 27 / 14 / 0 / 0 |
| replay-2026-08-31 | replay, prior:legacy, r1:<5% | 2026-08-27 (legacy) | 4.0 | 18 same / 0 diff | - | 22 / 19 / 0 / 0 |
| replay-2026-09-03 | replay, prior:legacy, r1:<5% | 2026-08-31 (legacy) | 4.95 | 18 same / 0 diff | - | 25 / 16 / 0 / 0 |
| replay-2026-09-13 | replay, prior:legacy, r1:<5%, holiday-gap | 2026-09-03 (legacy) | 4.21 | 18 same / 0 diff | - | 27 / 14 / 0 / 0 |
| replay-2026-10-18 | replay, prior:legacy, r1:<5%, holiday-gap | 2026-09-13 (legacy) | 4.13 | 18 same / 0 diff | - | 28 / 13 / 0 / 0 |
| replay-2026-11-08 | replay, prior:legacy, r1:5-15% | 2026-10-18 (legacy) | 13.56 | 17 same / 0 diff | - | 32 / 8 / 0 / 1 |
| flip-2026-07-20 | flip, prior:forecast-yes, r1:5-15% | 2026-07-16 (forecast-yes) | 6.74 | 7 same / 0 diff | - | 30 / 11 / 0 / 0 |
| flip-2026-08-06 | flip, prior:forecast-yes, r1:<5% | 2026-08-03 (forecast-yes) | 3.83 | 7 same / 0 diff | - | 32 / 9 / 0 / 0 |
| flip-2026-08-24 | flip, prior:forecast-yes, r1:<5% | 2026-08-20 (forecast-yes) | 4.41 | 21 same / 0 diff | - | 27 / 14 / 0 / 0 |
| flip-2026-09-13 | flip, prior:forecast-yes, r1:<5%, holiday-gap | 2026-09-03 (forecast-yes) | 4.21 | 18 same / 0 diff | - | 27 / 14 / 0 / 0 |
| flip-2026-10-18 | flip, prior:forecast-yes, r1:<5%, holiday-gap | 2026-09-13 (forecast-yes) | 4.13 | 18 same / 0 diff | - | 28 / 13 / 0 / 0 |
| flip-2026-11-08 | flip, prior:forecast-yes, r1:5-15% | 2026-10-18 (forecast-yes) | 13.56 | 17 same / 0 diff | - | 32 / 8 / 0 / 1 |
| deg-baseline | degraded, baseline, prior:none, r1:5-15% | none (none) | 13.56 | 17 same / 0 diff | - | 32 / 8 / 0 / 1 |
| deg-fred-down | degraded, fred-down, prior:legacy, r1:unavailable | 2026-10-18 (legacy) | unavailable | 1 same / 3 diff | BAMLC0A0CM, BAMLH0A0HYM2, BOGZ1FL153064486Q, CPIAUCSL, DFEDTARL, DFEDTARU, ECBASSETSW, IORB, JPNASSETS, LNFACBW027SBOG, RPONTTLD, SOFR, SOFR99, T5YIFR, THREEFYTP10, VIXCLS, WALCL, sp500_trend, repo_stress, vix_spx_comove (fallback: DCOILWTICO, DFII10, DGS10) | 32 / 8 / 0 / 1 |
| deg-ig-oas-fail | degraded, required-source-missing, prior:legacy, r1:<5%, holiday-gap | 2026-09-13 (legacy) | 4.13 | 17 same / 0 diff | BAMLC0A0CM | 28 / 13 / 0 / 0 |
| deg-repo-partial | degraded, repo-partial, prior:legacy, r1:5-15% | 2026-10-18 (legacy) | 13.56 | 15 same / 0 diff | RPONTTLD, SOFR99, repo_stress | 32 / 8 / 0 / 1 |
| deg-search-gaps | degraded, search-missing, prior:legacy, r1:5-15% | 2026-10-18 (legacy) | 13.56 | 17 same / 0 diff | - | 30 / 8 / 2 / 1 |
| deg-sp500-fail | degraded, comove-unavailable, prior:legacy, r1:<5%, holiday-gap | 2026-09-03 (legacy) | 4.21 | 17 same / 0 diff | sp500_trend, vix_spx_comove | 27 / 14 / 0 / 0 |
| deg-t10yie-derived | degraded, derived-breakeven, prior:legacy, r1:<5%, holiday-gap | 2026-09-03 (legacy) | 4.21 | 17 same / 1 diff | - | 27 / 14 / 0 / 0 |
| deg-zero-screens | degraded, zero-result, prior:legacy, r1:<5% | 2026-08-10 (legacy) | 2.99 | 7 same / 0 diff | - | 27 / 10 / 0 / 0 |

## Per case

### replay-2026-07-16

- run date 2026-07-16, prior 2026-07-13; Historical replay.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/replay-2026-07-16/evidence.md`, `cases/replay-2026-07-16/macro.txt`, `cases/replay-2026-07-16/prior.json`

### replay-2026-07-20

- run date 2026-07-20, prior 2026-07-16; Historical replay.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/replay-2026-07-20/evidence.md`, `cases/replay-2026-07-20/macro.txt`, `cases/replay-2026-07-20/prior.json`

### replay-2026-07-23

- run date 2026-07-23, prior 2026-07-20; Historical replay.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/replay-2026-07-23/evidence.md`, `cases/replay-2026-07-23/macro.txt`, `cases/replay-2026-07-23/prior.json`

### replay-2026-07-27

- run date 2026-07-27, prior 2026-07-23; Historical replay.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/replay-2026-07-27/evidence.md`, `cases/replay-2026-07-27/macro.txt`, `cases/replay-2026-07-27/prior.json`

### replay-2026-07-30

- run date 2026-07-30, prior 2026-07-27; Historical replay.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/replay-2026-07-30/evidence.md`, `cases/replay-2026-07-30/macro.txt`, `cases/replay-2026-07-30/prior.json`

### replay-2026-08-03

- run date 2026-08-03, prior 2026-07-30; Historical replay.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/replay-2026-08-03/evidence.md`, `cases/replay-2026-08-03/macro.txt`, `cases/replay-2026-08-03/prior.json`

### replay-2026-08-06

- run date 2026-08-06, prior 2026-08-03; Historical replay.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/replay-2026-08-06/evidence.md`, `cases/replay-2026-08-06/macro.txt`, `cases/replay-2026-08-06/prior.json`

### replay-2026-08-10

- run date 2026-08-10, prior 2026-08-06; Historical replay.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/replay-2026-08-10/evidence.md`, `cases/replay-2026-08-10/macro.txt`, `cases/replay-2026-08-10/prior.json`

### replay-2026-08-13

- run date 2026-08-13, prior 2026-08-10; Historical replay.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/replay-2026-08-13/evidence.md`, `cases/replay-2026-08-13/macro.txt`, `cases/replay-2026-08-13/prior.json`

### replay-2026-08-17

- run date 2026-08-17, prior 2026-08-13; Historical replay.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/replay-2026-08-17/evidence.md`, `cases/replay-2026-08-17/macro.txt`, `cases/replay-2026-08-17/prior.json`

### replay-2026-08-20

- run date 2026-08-20, prior 2026-08-17; Historical replay.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/replay-2026-08-20/evidence.md`, `cases/replay-2026-08-20/macro.txt`, `cases/replay-2026-08-20/prior.json`

### replay-2026-08-24

- run date 2026-08-24, prior 2026-08-20; Historical replay.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/replay-2026-08-24/evidence.md`, `cases/replay-2026-08-24/macro.txt`, `cases/replay-2026-08-24/prior.json`

### replay-2026-08-27

- run date 2026-08-27, prior 2026-08-24; Historical replay.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/replay-2026-08-27/evidence.md`, `cases/replay-2026-08-27/macro.txt`, `cases/replay-2026-08-27/prior.json`

### replay-2026-08-31

- run date 2026-08-31, prior 2026-08-27; Historical replay.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/replay-2026-08-31/evidence.md`, `cases/replay-2026-08-31/macro.txt`, `cases/replay-2026-08-31/prior.json`

### replay-2026-09-03

- run date 2026-09-03, prior 2026-08-31; Historical replay.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/replay-2026-09-03/evidence.md`, `cases/replay-2026-09-03/macro.txt`, `cases/replay-2026-09-03/prior.json`

### replay-2026-09-13

- run date 2026-09-13, prior 2026-09-03; Historical replay.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/replay-2026-09-13/evidence.md`, `cases/replay-2026-09-13/macro.txt`, `cases/replay-2026-09-13/prior.json`

### replay-2026-10-18

- run date 2026-10-18, prior 2026-09-13; Historical replay.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/replay-2026-10-18/evidence.md`, `cases/replay-2026-10-18/macro.txt`, `cases/replay-2026-10-18/prior.json`

### replay-2026-11-08

- run date 2026-11-08, prior 2026-10-18; Historical replay.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/replay-2026-11-08/evidence.md`, `cases/replay-2026-11-08/macro.txt`, `cases/replay-2026-11-08/prior.json`

### flip-2026-07-20

- run date 2026-07-20, prior 2026-07-16; Replay with a synthetic forecast prior answering yes on 2026-07-16: keep it, or flip only with cited evidence dated after the prior run.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: forecast-yes — synthetic forecast prior answering yes, see `prior_forecast.json`
- files: `cases/flip-2026-07-20/evidence.md`, `cases/flip-2026-07-20/macro.txt`, `cases/flip-2026-07-20/prior.json`

### flip-2026-08-06

- run date 2026-08-06, prior 2026-08-03; Replay with a synthetic forecast prior answering yes on 2026-08-03: keep it, or flip only with cited evidence dated after the prior run.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: forecast-yes — synthetic forecast prior answering yes, see `prior_forecast.json`
- files: `cases/flip-2026-08-06/evidence.md`, `cases/flip-2026-08-06/macro.txt`, `cases/flip-2026-08-06/prior.json`

### flip-2026-08-24

- run date 2026-08-24, prior 2026-08-20; Replay with a synthetic forecast prior answering yes on 2026-08-20: keep it, or flip only with cited evidence dated after the prior run.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: forecast-yes — synthetic forecast prior answering yes, see `prior_forecast.json`
- files: `cases/flip-2026-08-24/evidence.md`, `cases/flip-2026-08-24/macro.txt`, `cases/flip-2026-08-24/prior.json`

### flip-2026-09-13

- run date 2026-09-13, prior 2026-09-03; Replay with a synthetic forecast prior answering yes on 2026-09-03: keep it, or flip only with cited evidence dated after the prior run.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: forecast-yes — synthetic forecast prior answering yes, see `prior_forecast.json`
- files: `cases/flip-2026-09-13/evidence.md`, `cases/flip-2026-09-13/macro.txt`, `cases/flip-2026-09-13/prior.json`

### flip-2026-10-18

- run date 2026-10-18, prior 2026-09-13; Replay with a synthetic forecast prior answering yes on 2026-09-13: keep it, or flip only with cited evidence dated after the prior run.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: forecast-yes — synthetic forecast prior answering yes, see `prior_forecast.json`
- files: `cases/flip-2026-10-18/evidence.md`, `cases/flip-2026-10-18/macro.txt`, `cases/flip-2026-10-18/prior.json`

### flip-2026-11-08

- run date 2026-11-08, prior 2026-10-18; Replay with a synthetic forecast prior answering yes on 2026-10-18: keep it, or flip only with cited evidence dated after the prior run.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: forecast-yes — synthetic forecast prior answering yes, see `prior_forecast.json`
- files: `cases/flip-2026-11-08/evidence.md`, `cases/flip-2026-11-08/macro.txt`, `cases/flip-2026-11-08/prior.json`

### deg-baseline

- run date 2026-11-08, prior none; No prior run at all: baseline deltas, 前次結論：無前次（基準）.
- injected macro failure: `none`; evidence edit: `none`
- macro differences vs archived run: none
- prior: none
- files: `cases/deg-baseline/evidence.md`, `cases/deg-baseline/macro.txt`, `cases/deg-baseline/prior.json`

### deg-fred-down

- run date 2026-11-08, prior 2026-10-18; FRED key unusable: all FRED series fail incl. NASDAQ100, so R1 is unavailable; Treasury/EIA fallbacks only.
- injected macro failure: `ALL_FRED`; evidence edit: `none`
- macro differences vs archived run: DGS10 run=2026-11-05 replay=2026-11-06; DFII10 run=2026-11-05 replay=2026-11-06; DCOILWTICO run=2026-11-03 replay=2026-11-06
- prior: legacy
- files: `cases/deg-fred-down/evidence.md`, `cases/deg-fred-down/macro.txt`, `cases/deg-fred-down/prior.json`

### deg-ig-oas-fail

- run date 2026-10-18, prior 2026-09-13; Required IG OAS fails: must be FETCH FAILED, never cited, and weighed in 資料缺漏 for R3.
- injected macro failure: `BAMLC0A0CM`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/deg-ig-oas-fail/evidence.md`, `cases/deg-ig-oas-fail/macro.txt`, `cases/deg-ig-oas-fail/prior.json`

### deg-repo-partial

- run date 2026-11-08, prior 2026-10-18; repo_stress keeps only usable legs; composite `all` aggregation unsatisfied; funding-stress evidence partial.
- injected macro failure: `SOFR99,RPONTTLD`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/deg-repo-partial/evidence.md`, `cases/deg-repo-partial/macro.txt`, `cases/deg-repo-partial/prior.json`

### deg-search-gaps

- run date 2026-11-08, prior 2026-10-18; Search evidence missing for analyst TP + hyperscaler financing (R2/R3 inputs): no fabrication, gap weighed.
- injected macro failure: `none`; evidence edit: `drop_search`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/deg-search-gaps/evidence.md`, `cases/deg-search-gaps/macro.txt`, `cases/deg-search-gaps/prior.json`

### deg-sp500-fail

- run date 2026-09-13, prior 2026-09-03; SP500 fails: no 200-DMA deviation, vix_spx_comove unavailable; R1 still computable.
- injected macro failure: `SP500`; evidence edit: `none`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/deg-sp500-fail/evidence.md`, `cases/deg-sp500-fail/macro.txt`, `cases/deg-sp500-fail/prior.json`

### deg-t10yie-derived

- run date 2026-09-13, prior 2026-09-03; T10YIE fails: derived from DGS10-DFII10 on a shared date (status derived).
- injected macro failure: `T10YIE`; evidence edit: `none`
- macro differences vs archived run: T10YIE run=2026-09-11 replay=2026-09-10
- prior: legacy
- files: `cases/deg-t10yie-derived/evidence.md`, `cases/deg-t10yie-derived/macro.txt`, `cases/deg-t10yie-derived/prior.json`

### deg-zero-screens

- run date 2026-08-13, prior 2026-08-10; Eligible zero-result screens completed with zero hits: success, not NOT DISCLOSED.
- injected macro failure: `none`; evidence edit: `zero_screens`
- macro differences vs archived run: none
- prior: legacy
- files: `cases/deg-zero-screens/evidence.md`, `cases/deg-zero-screens/macro.txt`, `cases/deg-zero-screens/prior.json`


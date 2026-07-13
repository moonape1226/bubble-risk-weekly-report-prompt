# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A twice-weekly (Mon + Thu, Asia/Taipei) market "bubble risk" report in Traditional Chinese. The entire behaviour is defined by `bubble-risk-weekly-prompt.md` — **that prompt is the source of truth; this file only describes the surrounding mechanics.**

This directory is a clone of the prompt repo `moonape1226/bubble-risk-weekly-report-prompt`. A Claude cloud routine fetches the prompt and executes it; reports are written to a **separate** archive repo `moonape1226/bubble-risk-archive` at runtime. No reports are stored here. (Editing the prompt locally and pushing to the prompt repo is ordinary git — the connector-only rule below applies only to how the routine archives reports.)

## Data sources & the network gotcha

- FRED API is primary (all macro series); fallbacks are US Treasury XML (rates) and EIA (`RWTC`, WTI). SEC EDGAR is used for insider Form 4 screens. Spot quotes come via WebFetch/WebSearch (not yfinance).
- Keys in `.env` (never printed): `FRED_API_KEY`, `EIA_API_KEY` (also read in `scripts/fetch_macro.py`).
- **WebFetch to FRED hosts is WAF-blocked (HTTP 403).** Workaround: fetch with Python `urllib` over Bash using a custom User-Agent `bubble-risk-weekly`. Many sources are tagged `[primary: SEARCH]` to dodge 403s.

`scripts/fetch_macro.py` (stdlib only) fetches 20 FRED series + `SP500` (200-DMA / 52-week deviation), computes week-over-week deltas vs the prior-run date, and degrades gracefully per series (`ok` / `derived` / `fetch_failed`). It also emits non-FRED blocks: `cftc_lev_funds` (leveraged-fund net position in UST futures, from CFTC's keyless weekly file + current-year history zip), `move_index` (^MOVE via Yahoo's chart JSON endpoint — unofficial, may break), `ofr_repo` (OFR STFM tri-party repo volume, keyless), and a derived `repo_stress` block (SOFR−IORB / SOFR99−IORB spreads date-aligned to the SOFR print + SRF usage `RPONTTLD`). When the prior-run date and the latest valid observation coincide (holiday/weekend runs), it emits `no_new_obs: true` with zero deltas instead of dropping the delta. Usage: `python3 scripts/fetch_macro.py <prior-run-date|none>`.

`scripts/validate_report.py <report.md> [--coverage-rows N | --prompt <prompt.md>]` is the deterministic pre-archive gate (locked 12-section skeleton, exact final disclaimer line, score-JSON schema/arithmetic/tier — the score block must parse to a JSON object or the run fails, §1/§2 bar-vs-score consistency, §2 five locked anchors, §3 three indicator rows + 結論 trigger-state line, 總評 line cross-checked against §1 Δ and §3 結論; `--prompt` counts the top-level `# Data sources` bullets and enforces the Coverage-table row count). The routine must re-run it until exit 0 before the connector write. Tests: `python3 -m unittest discover -s tests` (also run in CI).

## Methodology (locked)

Six dimensions, fixed weights summing to 100: 估值溢價 22 / 市場廣度 13 / 投機行為 18 / 散戶情緒 12 / 貨幣與信貸環境 20 / 結構性槓桿 15. Tiers: 低 0-19 / 溫和 20-39 / 警戒 40-64 / 高 65-84 / 極度狂熱 85-100 (half-up rounding). Historical-anchor similarity uses a deterministic "checklist v2" against 1997 / 1998 / 1999 / 2000-03 / 2021-12.

## Report archival & git policy (cloud routine)

- 12 mandatory sections in a locked order/wording, a JSON score block, and a fixed disclaimer last line.
- Archived date-keyed: `report-YYYY-MM-DD/{score.json, report.md}` in the archive repo, written **atomically** (both or neither). A same-day rerun overwrites in place.
- The routine archives **only through the GitHub connector file-write API to `main`.** Forbidden inside the routine: local `git`/`gh` CLI, clone, curl/REST, GitPython. There is no `FORCE COMMIT` flag (overwrite is the default). `MODE: DRY-RUN` skips the commit.

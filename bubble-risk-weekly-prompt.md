You are producing a weekly market bubble risk report in Traditional Chinese (zh-TW), with financial terminology kept in English (P/E, OAS, Mag 7, Fear & Greed, capex, hyperscaler, token growth, etc.).

# Task

Generate a full six-dimension bubble risk assessment for the current week.

# Run mode

Default is **production** — write to the archive repo at the end of the run.

If the invocation context contains the string `DRY RUN` or `DRY-RUN` (case-insensitive) anywhere, switch to **dry-run mode**:

- Still fetch prior week data (read-only, harmless)
- Generate the full report normally
- Print the would-be JSON inline so the user can inspect it
- **Skip the GitHub commit step entirely**
- Add a single line at the top of the report: `> [DRY RUN] this report was not committed to archive.`

# Prior week reference

Before generating this week's report, use the GitHub connector to fetch the most recent prior week's data from the archive repo `moonape1226/bubble-risk-archive`. The archive is organized as one folder per week (`report-YYYY-Www/`), each containing `score.json` + `report.md`:

1. List all folders matching `report-YYYY-Www/` at the repo root.
2. **Filter to folders whose week is strictly before the current ISO week** — this prevents a same-week RUN NOW re-run from reading its own earlier write.
3. From the filtered list, sort by folder name descending.
4. Starting from the latest folder, read `report-<candidate>/score.json`. If that file is missing, unreadable, or cannot be parsed as valid JSON matching the schema below, skip that folder and try the next older candidate. Do not treat a partial folder as the prior week.
5. Use the first candidate with a valid `score.json` as the prior-week reference — schema:
   ```json
   {
     "week": "2026-W21",
     "valuation": 80,
     "breadth": 32,
     "speculation": 65,
     "retail": 58,
     "monetary": 63,
     "structural": 62,
     "total": 62,
     "tier": "警戒"
   }
   ```
6. Use these values as 上週分數 in 視覺化 §1 and compute Δ for each dimension.
7. If the filtered list is empty, the repo is missing, or every candidate folder lacks a usable `score.json`, mark this as 基準週 — the 上週 / Δ columns all fill —, and skip Δ-based ⚠ flags.

# Fetch protocol

**Parallelism (required):** Issue independent fetches / searches as parallel tool calls within a single message, not sequentially. If the runtime does not actually parallelize tool calls in one message, fall back to: emit a batch plan, then execute each batch at the runtime's highest available concurrency. Do not begin scoring until all required batches have returned. Batch by source type:

- FRED series in one parallel batch, preferring FRED API / JSON / CSV endpoints over scraping web pages
- Market data (Yahoo, multpl / GuruFocus, Cboe) in one parallel batch
- Static / often-blocked pages (CNN F&G, AAII, slickcharts, etf.com, openinsider) in one WebSearch-primary batch; WebFetch is optional confirmation, not required for success
- News / web searches (BofA survey, JPM survey, IPO heat, +AI rename, leveraged ETF approvals across KRX / TWSE / JPX / ESMA) in one parallel batch

**Coverage checklist (required):** For every bullet under `# Data sources`, attempt the preferred retrieval method and mark one final status. Do not begin scoring any dimension until all its required items are marked.

- `✓ API` — obtained from an official machine-readable endpoint such as FRED API / JSON / CSV.
- `✓ DIRECT` — obtained from the named source by WebFetch or equivalent direct page access.
- `✓ SEARCH-VERIFIED` — obtained through WebSearch because the named source is search-oriented, dynamically rendered, or blocked by WebFetch. This is a successful retrieval, not a fetch failure, but the appendix must show traceability.
- `✗ NOT DISCLOSED` — best-effort item has no current disclosure.
- `⛔ FETCH FAILED` — no usable current value was obtained from direct fetch, API, or WebSearch.

For `✓ SEARCH-VERIFIED`, record in 數據附錄: search query, result title, result URL, publisher/source, publication or data date if visible, retrieval timestamp, and the originally intended source. If WebFetch returned 403 but WebSearch found a current usable value, do not label the item ⛔; mention the direct-fetch 403 only in the appendix note.

**Source-preferred method:** Data-source bullets may include a `[primary: ...]` tag. Known-403 / WAF-protected sources tagged `[primary: SEARCH]` should use WebSearch first, without spending a mandatory WebFetch round. FRED sources tagged `[primary: API]` should use a keyless endpoint such as `https://fred.stlouisfed.org/graph/fredgraph.csv?id=<SERIES>`. Untagged sources default to `[primary: DIRECT]` with `✓ SEARCH-VERIFIED` as an allowed secondary path.

Best-effort items — those explicitly tagged in `# Data sources` (AI token volume growth, hyperscaler AI customer concentration, OpenAI / Anthropic revenue, PBoC aggregate financing, Asian regulator approvals from KRX / TWSE / JPX, upcoming AI IPO timing, analyst TP upgrade decomposition, AI infrastructure debt financing / vendor-financing loops) — may be marked ✗ NOT DISCLOSED instead of ⛔ FETCH FAILED. ✗ NOT DISCLOSED is not a failure.

**Timeout policy:** If any single direct fetch exceeds ~90 seconds, try the source's API or WebSearch path if available. If no path returns a current usable value, mark ⛔ FETCH FAILED and move on. Never block report generation on one stuck source.

# Data sources (fetch fresh data each run)

## Valuation

- S&P 500 P/E and Shiller CAPE: multpl.com or gurufocus.com [primary: SEARCH] (record the exact result URL / date)
- Mag 7 weighted P/E and AI leader P/S vs 10-year averages (Mag 7 = AAPL, MSFT, NVDA, AMZN, GOOGL, META, TSLA)
- **Analyst TP upgrade decomposition for Mag 7 / TSMC / AI semi bellwethers [primary: SEARCH]** (best-effort): scan top-tier sell-side TP raises in the past 14 days (Morgan Stanley, Goldman Sachs, JPMorgan, Bernstein, BofA, UBS) and split each upgrade into (a) EPS-revision contribution and (b) target-PE-expansion contribution. Decomposition: `ΔTP ≈ ΔEPS × PE_old + ΔPE × EPS_new`. Record analyst, ticker, old TP → new TP, EPS estimate Δ, target PE Δ, which component dominates, and the analyst's stated rationale. Sources: Bloomberg / Reuters / CNBC / MarketWatch summaries; Taiwan: 經濟日報 / udn money / cnyes. If no qualifying upgrade in 14d, mark ✗ NOT DISCLOSED.

## Breadth

- S&P 500 equal-weight (RSP) vs cap-weight (SPY) YTD divergence
- Top-10 concentration in S&P 500
- Advance/decline ratio, new high/low ratio

## Retail Sentiment

- CNN Fear & Greed Index: cnn.com/markets/fear-and-greed [primary: SEARCH] (record the exact result URL / date)
- Margin Debt: FINRA monthly data; also compute margin debt / total US equity market cap (Wilshire 5000 / FRED WILL5000IND if available, or S&P 500 market cap proxy) to avoid scoring absolute debt level alone
- Retail survey: AAII Investor Sentiment [primary: SEARCH]
- Social sentiment proxies: Reddit r/wallstreetbets top weekly posts, X (Twitter) cashtag chatter on meme tickers

## Institutional Sentiment

- BofA Fund Manager Survey and JPM institutional survey (monthly)

## Monetary & Credit

- Fed funds rate: FRED series DFEDTARU and DFEDTARL [primary: API, fredgraph.csv?id=DFEDTARU / DFEDTARL]
- High Yield OAS: FRED series BAMLH0A0HYM2 [primary: API, fredgraph.csv?id=BAMLH0A0HYM2]
- Investment Grade OAS: FRED series BAMLC0A0CM [primary: API, fredgraph.csv?id=BAMLC0A0CM]
- 10Y Treasury yield: FRED series DGS10 [primary: API, fredgraph.csv?id=DGS10]
- WTI crude oil price: FRED series DCOILWTICO [primary: API, fredgraph.csv?id=DCOILWTICO]
- Fed balance sheet: FRED series WALCL [primary: API, fredgraph.csv?id=WALCL]
- Global central bank liquidity cross-check: ECB balance sheet, BOJ balance sheet, and PBoC aggregate financing / liquidity operations (PBoC is best-effort; if no current PBoC/NBS English summary found, mark ✗ NOT DISCLOSED)

## AI Fundamentals

- Hyperscaler capex guidance: latest quarterly earnings from MSFT, GOOGL, AMZN, META
  - Track current FY capex guidance vs prior quarter's guidance
- AI token volume growth rate: search for reported metrics from Anthropic, OpenAI, Google quarterly disclosures (best-effort; cite if disclosed this quarter, else skip)
- OpenAI / Anthropic annualized revenue: most recent public disclosure or press leak (The Information, Reuters, CNBC) (best-effort; if no current-quarter disclosure or credible press leak, mark ✗ NOT DISCLOSED)
- Hyperscaler AI customer concentration: any disclosure on % of backlog from top AI customers (best-effort; usually qualitative from earnings calls)

## Speculative Behavior

- Search for past 7 days: "AI rename" / "+AI ticker change" / SPAC announcement / no-revenue speculative IPO surge
- IPO market heat: weekly IPO count, first-day return, and no-revenue / negative-EBITDA issuer share
- **Microcap thematic moonshots [primary: SEARCH]**: scan the week's biggest single-day stock movers for tickers under $1B market cap that gained ≥100% in one session (or sustained ≥50% over 2-3 sessions). Qualify the move as a moonshot signal only if the catalyst is a press release / 8-K / corporate announcement that stacks **two or more** hot themes (e.g. quantum computing, AI, lunar / space / NASA, fusion, robotics, defense, autonomous, nuclear, gene editing, weight-loss, crypto-treasury) **against weak fundamentals** (most recent quarterly revenue ≤ $5M, negative EBITDA, low cash). For each qualifying ticker record: ticker, single-day %, market cap, stacked themes, last-quarter revenue, cash position, and the source press release URL. Sources: Finviz biggest-gainers screener, Benzinga / MarketWatch movers, Yahoo Finance day's gainers, StockTwits trending. Example pattern (Astrotech ASTC, 2026-05-27, +516%): quantum + lunar + NASA stacked on quarterly revenue $343k.
- Upcoming AI IPOs: OpenAI, Anthropic, xAI, SpaceX timing and valuation (cite concrete S-1 filing or named-source report within the past 30 days; if none, mark ✗ NOT DISCLOSED rather than reporting unsourced rumor)
- Insider selling at AI / market-leadership companies: Form 4 clusters and sale-to-buy ratio [primary: SEC EDGAR]. Every named insider or dollar-amount claim must include Form 4 filing date, transaction date, issuer ticker, SEC EDGAR filing URL, and sale/buy amount within the past 14 days. If those filing-level details are not available within the past 14 days, mark ✗ NOT DISCLOSED and do not report stale names or dollar amounts from older news.

## Structural Leverage

- US leveraged ETF AUM: etf.com / ETFGI database [primary: SEARCH]; at minimum track NVDL, TSLL, CONL, TQQQ, SOXL, and SQQQ
- US single-stock leveraged ETF approvals: SEC EDGAR ETF filings and ETF.com new launches feed
- Global leveraged product approvals: KRX / Korea FSC, TWSE / Taiwan FSC, JPX / Japan FSA, ESMA announcements, and ETFGI weekly reports (Asian regulator feeds are fragmented and not published weekly; treat each regulator as best-effort and mark ✗ NOT DISCLOSED if no English-language disclosure found this week)
  - Record approving market / regulator, underlying stock, leverage multiple, inverse or long direction, and expected AUM / size if available
- 0DTE option volume: CBOE daily market statistics; SpotGamma / Goldman Derivatives Insights summaries if public
- Options total volume: OCC monthly volume report
- Cross-asset derivatives / correlation checks: VIX term structure, Cboe SKEW, and rolling stock-bond correlation
- Cross-reference only: FINRA margin debt or FRED series BOGZ1FL073164003.Q, including the margin debt / equity market cap ratio from Retail Sentiment as a confirmation check only (primary margin debt scoring remains under retail sentiment; do not double-count it here)
- **AI infrastructure debt financing / vendor-financing loops [primary: SEARCH]** (best-effort): scan the past 30 days for disclosed debt financing, private credit facilities, ABS / asset-backed facilities, delayed-draw term loans, convertible debt, or sale-leaseback financing tied to AI GPU clusters, neoclouds, or data centers (CoreWeave, Crusoe, Lambda, Nebius, Applied Digital, xAI / OpenAI infrastructure vehicles, Stargate-related entities). Record borrower, amount, date, financing type, collateral / customer-contract backing if disclosed, pricing / rating if disclosed, use of proceeds, and source URL. Separately track Nvidia / hyperscaler circular-financing exposure: disclosed equity investments, customer purchase commitments, capacity backstops, vendor-financing-like arrangements, or guarantees where the recipient is also a buyer of GPUs / compute. Quantify only named disclosed deal amounts; do not invent a circular-financing ratio. If no new disclosure is found in the past 30 days, mark ✗ NOT DISCLOSED for the weekly event signal and optionally cite the latest outstanding disclosed facilities as background, not as 本週新增訊號.

# Output structure

**Mandatory section order — emit exactly these sections in this exact order. Do not merge, reorder, drop, or rename:**

1. Report title (`# <YYYY-Www> 市場泡沫風險評估週報` plus a one-line meta with 報告日期、週次、上週基準/基準週)
2. `## §1 六維度風險條圖` — chart only (see 視覺化 spec below for exact columns)
3. `## §2 歷史錨點相似度` — chart only
4. `## §3 三角訊號` — chart plus a short interpretation paragraph
5. `## 六維度評分` — separate rationale table or per-dimension subsections, with sources and dates (not folded into §1)
6. `## 綜合分數` — explicit weight × score table that sums to total + risk tier
7. `## 歷史泡沫週期對比` — narrative interpretation referencing §2 (not just the §2 table again)
8. `## 機構情緒對照`
9. `## 本週新增訊號` — Δ deltas and trigger events; if 基準週, say so
10. `## 數據附錄` — raw data + SEARCH-VERIFIED tracking entries (see Fetch protocol)
11. `## 本週分數存檔` — the fenced JSON block (see Persistence spec)
12. Closing disclaimer line: `本報告為相對風險溫度計，非擇時訊號。`

For every mandatory item above: if current evidence is unavailable or a source fails, keep the heading / item in place and use the section-appropriate placeholder (`本週無...資料`, `基準週`, `FETCH FAILED`, or `—`). Skipping a mandatory heading is forbidden under any condition.

**Report skeleton lock — before drafting, instantiate this skeleton and fill it in. Keep every heading below exactly as written, in this order. Do not print extra top-level or second-level sections, and do not merge adjacent sections:**

````markdown
# <YYYY-Www> 市場泡沫風險評估週報
> 報告日期：<YYYY-MM-DD>；週次：<YYYY-Www>；上週基準：<report-YYYY-Www or 基準週>

## §1 六維度風險條圖
| 維度 | 條圖 | 本週 | 上週 | Δ |

## §2 歷史錨點相似度
| 錨點 | 相似度 | 條圖 | 標記 |

## §3 三角訊號
| 指標 | 當週數值 | vs 上週 |
<short interpretation paragraph>

## 六維度評分

## 綜合分數

## 歷史泡沫週期對比

## 機構情緒對照

## 本週新增訊號

## 數據附錄

## 本週分數存檔
```json
<score JSON>
```

本報告為相對風險溫度計，非擇時訊號。
````

**Internal self-check before final output (do not print this checklist):**

- The report contains exactly the 12 mandatory items above, with no renamed, missing, duplicated, or merged sections.
- §1 / §2 / §3 use only their required columns; rationale and sources are outside the visualization tables.
- `## 六維度評分` and `## 綜合分數` remain independent sections after §3.
- `## 機構情緒對照` is always emitted, even when it only says `本週無新機構調查數據。`
- The final visible line is exactly `本報告為相對風險溫度計，非擇時訊號。`

**Hard rules for the visualization tables (§1 / §2 / §3):**

- §1 must use exactly these columns: `維度 | 條圖 | 本週 | 上週 | Δ`. No extra columns (no `核心論述`, no `來源`, no `權重` inline). Rationale and sources belong in `## 六維度評分`, not §1.
- §2 must use exactly: `錨點 | 相似度 | 條圖 | 標記`. No extra columns (no `核心類比特徵`).
- §3 must use exactly: `指標 | 當週數值 | vs 上週`.
- Do not fold `## 六維度評分` or `## 綜合分數` into the §1 table. They are separate sections by design — §1 is a glance-able heatmap, the rationale tables are the audit trail.

## 六維度評分

For each dimension, give a score 0-100 and a one-sentence rationale citing specific data points with sources.

### 1. 估值溢價 (weight 22%)

Score based on:

- S&P 500 P/E, Shiller CAPE vs 10-year average (primary)
- Mag 7 weighted P/E vs historical
- AI fundamentals reality check: is hyperscaler capex guidance still being raised? Is token growth sustaining? If capex guidance starts being cut, valuation risk rises sharply even if P/E unchanged.
- **TP-upgrade phase signal**: classify each major sell-side TP raise on Mag 7 / TSMC / AI semi bellwethers this period as (a) **EPS-driven** — target PE roughly stable, upgrade explained by earnings revision — or (b) **multiple-driven** — target PE expands while EPS revision is modest, often justified by "long-duration AI demand" / "structural re-rating" / "should trade at premium to historical band". Multiple-driven upgrades happening across 2+ bellwethers in the same quarter is a late-cycle signal (price chases narrative-based PE re-rating, not earnings). Calibration anchor: 2026-Q2 Morgan Stanley TSMC raise argued 20–30× target PE is reasonable while the EPS revision did less lifting than the PE expansion itself. Caveat: a structural re-rating from cyclical-semi to AI-infrastructure-utility can partially justify multiple expansion — do not auto-flag any PE rise as bubble, but do flag when the dominant lever of TP upgrades shifts from E to multiple across multiple names.

### 2. 市場廣度 (weight 13%)

Score based on:

- RSP vs SPY YTD divergence
- Top-10 concentration
- Advance/decline, new high/low

### 3. 投機行為 (weight 18%)

Score based on:

- +AI rename cases this week
- SPAC / shell IPO activity
- IPO count, first-day pop, and no-revenue / negative-EBITDA issuer share
- Microcap thematic moonshots this week (see Data sources for screening criteria: ≥100% single-day, <$1B cap, 2+ stacked hot themes, weak fundamentals). Count and name each qualifying ticker. This is the primary indicator for the "no-revenue stock surge" category — historical bubble peaks (1999, 2021/12) saw multiple moonshots per week
- Insider selling clusters among AI / market leaders
- OpenAI / Anthropic revenue trajectory (concentration risk indicator)
- Upcoming mega-IPO pipeline (liquidity drain risk)

### 4. 散戶情緒 (weight 12%)

Score based on:

- CNN Fear & Greed
- Margin Debt monthly change and margin debt / equity market cap ratio
- AAII retail survey
- Social sentiment proxies: Reddit r/wallstreetbets top weekly posts, X (Twitter) cashtag chatter on meme tickers
- Note: institutional sentiment reported separately below, not scored here

### 5. 貨幣與信貸環境 (weight 20%)

Score based on:

- Fed funds rate path and forward guidance
- HY OAS level and weekly change
- IG OAS
- Fed balance sheet movement
- Global liquidity cross-check: ECB / BOJ balance sheets and PBoC aggregate financing or liquidity operations. Use as confirmation, not a separate seventh dimension.
- **三角交叉訊號**: Compare current state of {S&P 500, WTI oil, 10Y yield}. Flag if all three are at multi-month highs simultaneously, which is historically unstable.

### 6. 結構性槓桿 (weight 15%)

Score based on:

- US leveraged ETF AUM: aggregate AUM for single-stock products (NVDL, TSLL, CONL, etc.) and broad leveraged products (TQQQ, SOXL, SQQQ) vs 12-month average, plus week-over-week change
- US single-stock leveraged ETF approvals / launches in the past 30 days
- Global leveraged product diffusion: non-US market approvals this week for single-stock leveraged / inverse ETFs (Korea, Taiwan, Japan, Europe)
- 0DTE option share of SPX option volume (rolling 5-day)
- Options total volume / cash equity volume ratio
- VIX term structure, SKEW, and stock-bond correlation as confirmation signals for crowded optionality / cross-asset complacency
- Cross-reference margin debt / equity market cap ratio from 散戶情緒 as confirmation only; do not double-count it in 結構性槓桿 scoring
- AI infrastructure debt financing / vendor-financing loops: disclosed AI data-center / GPU-backed debt facilities, private credit / ABS issuance, and Nvidia / hyperscaler customer-financing ties. Treat this as structural leverage inside the AI capex trade, not as general macro credit conditions; do not create a seventh dimension or change the 15% weight.

**Rubric anchor points:**

- 0-20: Leveraged ETF AUM near 12-month lows; 0DTE share < 30%; no global approvals; no recent AI infrastructure debt disclosure
- 21-40: AUM rising moderately; 0DTE share 30-45%; isolated single-market approvals; AI debt disclosures are small / refinancing-only
- 41-60: AUM growing steadily; 0DTE share 45-55%; 1 market approval in the past 4 weeks; AI infrastructure debt is present but matched to disclosed customer contracts with stable terms
- 61-80: AUM accelerating; 0DTE share 55-65%; 2+ market approvals in the past 4 weeks; new large AI infrastructure debt / private credit / ABS facilities or visible Nvidia / hyperscaler customer-financing loops expand this month
- 81-100: AUM rising vertically; 0DTE share persistently > 65%; 「全球槓桿擴散訊號」triggered this week; or AI infrastructure financing shows multiple large, collateral-light, circular, or covenant-stretched deals in the same month

**Special rule:**

- If 2+ non-US markets approve single-stock leveraged / inverse ETFs in the same week, set this dimension's score floor to 81 and flag 「全球槓桿擴散訊號」.
- When triggered, 本週新增訊號 must list approving markets, underlying stocks, leverage multiple, and expected AUM / size if available.
- AI infrastructure debt financing is a best-effort structural-leverage signal. If no current disclosure is found, mark ✗ NOT DISCLOSED and do not penalize the source coverage score. If disclosed deal amounts are available, include them in 數據附錄 with issuer, amount, date, financing type, and source; use stale disclosures only as background unless they occurred inside the required weekly / monthly window.

## 綜合分數

Weighted total 0-100 using weights 22/13/18/12/20/15 + risk tier label (低 / 溫和 / 警戒 / 高 / 極度狂熱).

## 歷史泡沫週期對比

For each of the following reference points, give a similarity percentage and a one-line rationale:

- 1997 (early infrastructure buildout)
- 1998 (LTCM shock, mid-cycle)
- 1999 (late euphoria)
- 2000 March (peak)
- 2021 December (meme + zero-rate peak)

Then provide a 2-sentence interpretation: which historical phase does the current week most resemble, and what does that imply about position in the cycle? The similarity assessment should include the 結構性槓桿 dimension, especially for 1999 / 2000 March / 2021 December comparisons. Interpret 結構性槓桿 in period-adjusted terms rather than requiring identical instruments: for 1999 / 2000 March, use proxies such as margin debt, index futures / options speculation, and retail leverage; for 2021 December, use meme leverage, options / 0DTE where available, and leveraged product adoption.

## 機構情緒對照

If new BofA Fund Manager Survey or JPM institutional survey was released since last week, report:

- Top consensus positioning (long / short)
- Tail risk concerns
- Cash levels
- Note: high consensus expectation of a future crash is itself a contrarian signal. AAII may be mentioned only as retail contrast, not as institutional data.

If no new data this week, still emit this section heading and state: "本週無新機構調查數據。"

## 本週新增訊號

Dimensions with score changes from last week + reasons. If no prior week data available, mark as "基準週".

If 「全球槓桿擴散訊號」triggered this week, list all approving markets, underlying stocks, leverage multiples, and expected AUM / size if available.

## 數據附錄

Raw data table with sources, FRED series IDs, and timestamps.

## 本週分數存檔

After all sections above, output a fenced JSON block (label `json`) for next week's run to read. Schema must match exactly:

```json
{
  "week": "<ISO week, e.g. 2026-W21>",
  "valuation": <int 0-100>,
  "breadth": <int 0-100>,
  "speculation": <int 0-100>,
  "retail": <int 0-100>,
  "monetary": <int 0-100>,
  "structural": <int 0-100>,
  "total": <int 0-100, weighted with 22/13/18/12/20/15>,
  "tier": "<低|溫和|警戒|高|極度狂熱>"
}
```

Generate all report sections, including the 視覺化 section below, before invoking the archive write. Then write this JSON to `moonape1226/bubble-risk-archive` **via the GitHub connector's file-write API**, using whatever write mechanism the connector provides. The routine must complete the write autonomously inside the same session — it is the routine's job, not the user's.

**Required end-state (this is what matters, not the mechanism):** when the run finishes, `report-<week>/score.json` and `report-<week>/report.md` must both exist on the `main` branch of `moonape1226/bubble-risk-archive`, with no pull request left open and no review pending. If the connector reaches `main` by opening a branch and pull request that it then merges within the same session, that is fine — do not avoid the connector's native flow, but do not leave anything un-merged or waiting for a human.

**Strictly forbidden:**

- Do NOT clone the repo to local disk, `/tmp`, or any working directory
- Do NOT run `git` CLI commands (`git clone`, `git add`, `git commit`, `git push`)
- Do NOT ask the user to run shell commands or `git push` manually
- Do NOT print a PAT, token, or personal access credential anywhere in the report
- Do NOT defer the commit with phrases like "請執行以下指令完成推送"
- Do NOT leave a pull request open or waiting for human review — if the connector's flow uses a PR, it must be merged to `main` in the same session
- Do NOT use any write method other than the GitHub connector's file-write operation(s). This includes gh CLI, GitPython / libgit2 / pygit2, subprocess wrappers around git, and direct curl / HTTP calls to the GitHub REST or Contents API.

**Required behavior:**

1. Check if folder `report-<week>/` already exists for the current ISO week (use the connector's read/list API — listing the folder or checking for `report-<week>/score.json` both work).
2. **If it exists**: this is a same-week re-run (likely RUN NOW for testing). Default behavior is to **skip the commit step** to avoid commit log churn. Add a line to the report: `> Same-week folder already exists in archive; commit skipped. Add 「FORCE COMMIT」 to the invocation context to overwrite.`
3. **If it does not exist OR the invocation context contains `FORCE COMMIT`**: use the connector's file-write operation(s) to write both files under one folder per week so they land on `main` (see Required end-state above). Prefer one multi-file commit if supported; otherwise write the two files as one archive-write step. Do not re-run the same-week skip check between the two file writes. Write:
   - `report-<week>/score.json` — the JSON block above
   - `report-<week>/report.md` — the full markdown report
   - Commit / PR title: `weekly archive <week>` (or `weekly archive <week> [forced overwrite]` when overwriting)
   - Target branch: `main` (if the connector opens a PR to get there, merge it in-session; leave nothing open)
4. If the connector call fails (auth, rate limit, network), state the actual error at the end of the report; do not silently skip and do not fall back to local git, gh CLI, or any other write method.
5. If no GitHub connector file-read / file-write tool is available in the runtime at all, state: `GitHub connector unavailable in this environment; enable the GitHub connector in routine settings and rerun.` Then leave the report and JSON inline, with no fallback commit attempt.

**Skip this entire commit step if in dry-run mode** (see `# Run mode` at the top). The JSON block above should still be printed inline so the user can inspect it.

## 視覺化規格（§1 / §2 / §3 渲染細節）

This subsection defines how §1 / §2 / §3 must be rendered. They appear at the **top** of the report per the Mandatory section order above, not here. Do not emit a second copy below.

三個區塊一律使用 **Markdown 表格**呈現，由 Markdown 渲染器處理欄寬對齊。

**嚴格禁止事項：**

- 不得使用 ASCII 框線字元（╔ ╗ ║ ═ ╠ ╣ ╬ ┌ ┐ └ ┘ ─ │ 等）
- 不得將表格包在 code fence 內（包進去就無法渲染成表格）
- 不得手動補空格對齊欄位（交給 Markdown 處理）

**通用規則：**

- ▰ 代表填滿，▱ 代表空白，每個條圖固定 10 格
- 填滿格數 = floor(分數 / 10)，例如 63 分 → ▰▰▰▰▰▰▱▱▱▱
- 基準週（無前週資料）：上週欄填 —，Δ 欄填 —

### §1 六維度風險條圖

| 維度 | 條圖 | 本週 | 上週 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▰▱▱ | 80 | — | — |
| 市場廣度 | ▰▰▰▱▱▱▱▱▱▱ | 32 | — | — |
| 投機行為 | ▰▰▰▰▰▰▱▱▱▱ | 65 | — | — |
| 散戶情緒 | ▰▰▰▰▰▱▱▱▱▱ | 58 | — | — |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▱▱▱▱ | 63 | — | — |
| 結構性槓桿 | ▰▰▰▰▰▰▱▱▱▱ | 62 | — | — |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **62【警戒】** | — | — |

上方為格式範例，實際數值依本週評分填入。

- 加權總分使用 22/13/18/12/20/15 權重計算
- 風險等級：低 / 溫和 / 警戒 / 高 / 極度狂熱
- 若 |Δ| >= 10，在 Δ 欄數值後加 ⚠
- 若觸發「全球槓桿擴散訊號」，在「結構性槓桿」列的「本週」欄分數後加 ◆

### §2 歷史錨點相似度

| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1997 早期建設 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 1998 LTCM 衝擊 | 28% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 52% | ▰▰▰▰▰▱▱▱▱▱ | ◀ 最貼近 |
| 2000/3 頂點 | 32% | ▰▰▰▱▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |

上方為格式範例。最高相似度的列在「標記」欄填「◀ 最貼近」，其餘留白。

### §3 三角訊號

| 指標 | 當週數值 | vs 上週 |
|---|---|---|
| S&P 500 | 7,473 | ▲ +3.5%（前週 ~7,217） |
| WTI 原油 | $92.1 /bbl | ▲ +5.5%（前週 ~$87.3） |
| 10Y Treasury | 4.57% | ▲ +12 bps（前週 ~4.45%） |

上方為格式範例，方向符號用 ▲（上）/ ▼（下）。

表格下方以一段普通文字（非表格、非 code fence）呈現解讀：

> 三者狀態：{穩定共存 / 同向偏高（不穩定）/ 出現分歧（[哪項在重新定價]）}

必要時加 ⚠ 觸發線說明。

# Constraints

- Source-cite every numeric claim with URL or FRED series ID.
- Source-cite every time-sensitive concrete claim used for scoring deltas or weekly event signals with a source date inside the relevant window: past 14 days for insider transactions, IPO filings / timing, and ETF approvals / launches; past 7 days for weekly news events. If the source date is stale, missing, or ambiguous, use it only as background context and do not factor it into scoring deltas or "本週新增訊號". Stock-of-state indicators such as CAPE, P/E, margin debt level, and AUM level are exempt from the within-window publication-date rule, but still need a current snapshot date.
- If a data source is unreachable and no API or WebSearch path obtains a current usable value, state so explicitly; do not fabricate.
- Do not report named insider-selling claims unless supported by SEC EDGAR Form 4 filing URLs and filing / transaction dates from the past 14 days.
- Do not extend signals to specific trading strategies or holdings unless explicitly asked.
- End every report with: "本報告為相對風險溫度計，非擇時訊號。"

> [DRY RUN] this report was not committed to archive.

# 2026-08-24 AI 泡沫破裂預測報告

報告日期：2026-08-24｜ISO 週次：2026-W35｜預測窗口：2026-08-24 → 2027-02-22｜前次基準：report-2026-08-20（4天前）

## 結論

**結論：no**

三條路徑目前都不在進行中：NASDAQ-100 距 52 週高點回撤 4.41%，離 R1 門檻還差約 21.5%（`valuation.ndx_drawdown`）；top-4 hyperscaler 2026 capex 合計仍年增約 77%，四家都沒有下修跡象（`ai.hyperscaler_capex`）；HY OAS 2.75% 等信用定價也沒有出現 AI 信用事件的前兆（`monetary.hy_oas`）。估值與槓桿雖然極端，但這只說明泡沫存在，看不到能在 182 天內觸發破裂的催化劑或傳導。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29308.86（2026-08-21），252 個交易日內最高收盤 30660.6（2026-06-02），距 52 週高點回撤 4.41%（`valuation.ndx_drawdown`）。R1 門檻水位為 22995.45，自最新收盤還需再跌約 21.5% 才會觸及。S&P 500 收在 7674.37（2026-08-21），高於 200 日均線 8.15%、高於 52 週均線 9.61%（`valuation.sp500_trend`），價格延伸偏高，有均值回歸風險，但距離崩跌所需的幅度仍遠。VIX 16.01（2026-08-20）；近 7 日 VIX +9.43%、S&P 500 −2.02%，屬正常的反向走勢，沒有出現同漲的警戒讀數（`structural.vix_spx_comove`）。估值處於極端區：Shiller CAPE ≈41.2、trailing P/E ≈26.2（`valuation.sp500_pe_cape`），Mag 7 加權本益比 ≈29.5x（`valuation.mag7_multiples`）。

**判讀：** 目前離 R1 很遠。窗口內要再跌約 21.5%，需要盈利或信用端的明確衝擊，例如 hyperscaler 下修 capex，或利率再上行（CPI 3.3%、FedWatch 尾端為升息）壓縮高倍數估值。目前看不到這類催化劑已經啟動。

### R2 資本支出收縮

依 2026-08-13 的 Q2 財報後彙整，Microsoft、Alphabet、Amazon、Meta 2026 capex 合計 ≈$725bn，年增約 77%（`ai.hyperscaler_capex`）。現有證據只提供四家合計數，沒有逐家拆分，因此無法逐家核實相較前次正式指引的方向。各家方向：Microsoft 未能逐家核實、Alphabet 未能逐家核實、Amazon 未能逐家核實、Meta 未能逐家核實。不過，合計數大幅年增，且沒有任何一家下修的報導，因此可下修家數判定為 0／4。需求側仍在擴張：Anthropic run-rate ≈$65B（年增約 7 倍）、OpenAI ≈$40B（`ai.openai_anthropic_revenue`、`ai.token_growth`）；GPU 現貨租金高於合約價 2 倍以上，產能已被利用率吸收（`ai.compute_supply_demand`）。窗口內依季度節奏還有 Q3 2026 與 Q4 2026 兩輪財報，但本次證據沒有具體財報日期。

**判讀：** 目前沒有任何一家下修，距 R2 很遠。要在窗口內觸發，需要兩家在 Q3 或 Q4 財報下修指引；目前需求與定價證據都朝反方向。

### R3 AI 信用事件

本次的 AI 信用定價掃描與 AI 基礎設施債務融資掃描，都沒有找到 30／14 日窗內的合格披露。因此本次沒有個別借款人的利差、CDS、評等行動或違約訊號可引用，也沒有已知的 AI 資料中心借款人處於困境。整體信用定價很緊：HY OAS 2.75%（`monetary.hy_oas`）、IG OAS 0.82%（`monetary.ig_oas`），截至 2026-08-20 與前次持平。repo 資金壓力（SOFR−IORB）為 −2.0bps，SOFR99−IORB 為 6.0bps，SRF 動用（Standing Repo Facility usage）為 0（`monetary.repo_stress_srf`）。銀行對 NBFI 放款約 $2.03T，週變動 0%（`structural.nbfi_bank_loans`）。

**判讀：** 目前沒有任何訊號指向 R3。要在窗口內觸發，需要大型 neocloud 或資料中心借款人出現付款違約或 distressed exchange；在 HY OAS 2.75% 的融資環境下，再融資牆短期內難以轉成違約。

## 支持 yes 的證據

- [整體] 估值處於歷史極端：Shiller CAPE ≈41.2、trailing P/E ≈26.2（2026-08-20），下行空間一旦打開會很大（`valuation.sp500_pe_cape`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）很大：年化 AI 終端營收 ≈$105bn（OpenAI 40＋Anthropic 65）vs 年化 capex ≈$725bn（分母：top-4 hyperscaler），回本壓力將來可能迫使 capex 收縮（`ai.revenue_capex_gap`）。
- [R1] 槓桿與投機部位擁擠：美股槓桿 ETF 總 AUM 創紀錄 ≈$198bn（2026-08-17）（`structural.leveraged_etf_aum`）；SPX 0DTE 佔比創紀錄 ≈62.4%（2026-08-14）（`structural.zero_dte`）；FINRA margin debt YoY ≈+38.6%（2026-07）（`retail.margin_debt`），接近歷史頂部常見區間。
- [R1] 利率端緩衝有限：CPI YoY 3.3%（2026-07）（`monetary.cpi_yoy`）、10Y 期限溢價（term premium）0.8393%（2026-08-14）（`monetary.term_premium`）、FedWatch 9/16 按兵不動 ≈68.4% 且尾端為升息（`monetary.fedwatch`），回撤時 Fed 降息托底的空間受限。
- [R1] S&P 500 高於 200 日均線 8.15%（2026-08-21），NASDAQ-100 自 2026-06-02 高點已小幅回落（`valuation.sp500_trend`、`valuation.ndx_drawdown`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.41%（2026-08-21），距 R1 門檻 22995.45 還需再跌約 21.5%（`valuation.ndx_drawdown`）。
- [R2] top-4 hyperscaler 2026 capex 合計 ≈$725bn、年增約 77%（2026-08-13），四家沒有任何下修（`ai.hyperscaler_capex`）。
- [R3] 信用定價沒有壓力：HY OAS 2.75%、IG OAS 0.82%（2026-08-20）（`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）−2.0bps、SRF 動用 0（`monetary.repo_stress_srf`）。
- [R2] 需求端持續強勁：Anthropic run-rate ≈$65B、年增約 7 倍，OpenAI ≈$40B（2026-08-17）（`ai.openai_anthropic_revenue`、`ai.token_growth`）；GPU 現貨租金高於合約價 2 倍以上（2026-08-13）（`ai.compute_supply_demand`）。
- [整體] 情緒並不亢奮，廣度也在擴散：CNN Fear & Greed 55（2026-08-21）（`retail.fear_greed`）；AAII 偏空 39.9% 高於偏多 35.5%（2026-08-19）（`retail.aaii`）；RSP YTD 領先 SPY ≈5pp（2026-08-17）（`breadth.rsp_spy`）。

## 與前期比較

前次結論：yes（report-2026-08-20）
本次結論：翻轉
翻轉依據：
- 前次 forecast.json 沒有 `yes_basis` 欄位（此欄位建立前的格式），沒有需要逐項回應的決定性理由。重新檢視後，前次 yes 不符合 rule 1 的舉證門檻：NASDAQ-100 距 52 週高點回撤 4.41%（2026-08-21），沒有回撤正在進行的證據（`valuation.ndx_drawdown`）。
- R2 沒有進行中：top-4 hyperscaler 2026 capex 合計 ≈$725bn、年增約 77%（2026-08-13），四家沒有下修（`ai.hyperscaler_capex`）。
- R3 沒有進行中：HY OAS 2.75%（2026-08-20），與前次持平，信用端沒有重定價（`monetary.hy_oas`）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下 best-effort 來源完成掃描但沒有合格披露（✗ NOT DISCLOSED）：valuation.analyst_tp_decomposition、valuation.ai_credit_schism、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.pboc、monetary.private_credit_liquidity、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（event_scan 無 30 日內事件）、ai.depreciation_life、ai.capital_cycle（event_scan 無 30 日內事件）、structural.global_leveraged_approvals、structural.ai_infrastructure_debt。其中 valuation.ai_credit_schism 與 structural.ai_infrastructure_debt 是 R3 的直接來源，空白會降低 R3 的可見度。不過整體 HY／IG OAS 與 repo 資金壓力都很平靜，私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）也沒有披露，因此這些缺漏不太可能把答案改為 yes。

最大的不確定性：

1. R2 的逐家指引方向：現有證據只有 top-4 合計數，沒有逐家拆分。若 Q3 財報（窗口內）有兩家下修，會直接推向 yes；目前需求證據推向 no。
2. 利率與通膨：CPI 3.3%、FedWatch 尾端為升息。若 Fed 轉向升息、10Y 期限溢價（term premium）再上行，會壓縮高倍數估值，推向 R1，也就是 yes。
3. AI 信用定價的可見度：本次 AI 個別發行人利差與 AI 基礎設施債務融資都沒有窗內資料。若之後出現 neocloud 利差急升或再融資失敗，會推向 R3，也就是 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7674.37 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 8.15 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29308.86 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 4.41 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1 季資料，家庭股票配置 %） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.75 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.82 | FRED API (series_id=BAMLC0A0CM) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.69 | FRED API (series_id=DGS10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.35 | FRED API (series_id=DFII10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.34 | FRED API (series_id=T10YIE) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD） | 86.48 | FRED API (series_id=DCOILWTICO) | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料，%） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.34 | FRED API (series_id=T5YIFR) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 0.8393 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.63 | FRED API (series_id=SOFR) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.71 | FRED API (series_id=SOFR99) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-24 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,745,699（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,927,307（€5.93T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,442,957（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.01 | FRED API (series_id=VIXCLS) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of；base 2026-08-13，comove=false） | 16.01 | FRED API (series_id=VIXCLS, SP500) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2026.1422（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-12 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（槓桿基金美債期貨淨部位，口） | -7218048 | CFTC TFF futures-only | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.4 | Yahoo Finance chart API (^MOVE) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2328.6 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |

10Y 分解：ΔDGS10 0.0bps ≈ ΔDFII10 0.0bps + ΔT10YIE 0.0bps，判讀：無變動。freshness 為 partial_stale：stale_series 為 DGS10、DFII10（這兩腿無新觀測），T10YIE 有更新。

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl / GuruFocus [SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | 賣方摘要 WebSearch（90d＋same quarter） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✗ NOT DISCLOSED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | CNN [SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | FINRA / GuruFocus WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | AAII [SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WSB / X WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | naaim.org [SEARCH] | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM | BofA / JPM WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED-direct） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | Reuters / TreasuryDirect WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | CME FedWatch [SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | PBoC / NBS WebSearch | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | BDC 披露 WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | 財報摘要 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | 供應商披露 WebSearch | ✓ SEARCH-VERIFIED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | Bloomberg / CNBC WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | 財報電話 WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | 產業披露 WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch：quarterly_state（top-5 capex vs FCF、發債）＋30 日 event_scan | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | 綜合披露 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | 10-K / 10-Q WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch：quarterly_state（供需增速）＋30 日 event_scan | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | 新聞 WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | stockanalysis / Renaissance WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | Finviz / Benzinga [SEARCH]（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | Bloomberg / CNBC WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | Cboe [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | ETF.com [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com WebSearch（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | KRX / TWSE / JPX / ESMA WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | OCC WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | FINRA / GuruFocus WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | 信用市場 WebSearch（30d） | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）＋WebSearch 補充掃描（無合格事件） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | trailing P/E ≈26.2、Shiller CAPE ≈41.2（原定 multpl / GuruFocus） | Shiller CAPE S&P 500 P/E August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio （GuruFocus） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權本益比 ≈29.5x（S&P 500 ≈25.6x） | Magnificent 7 weighted P/E August 2026 | https://www.fool.com/investing/2026/08/14/the-best-magnificent-seven-stocks-to-buy-in-august/ （Motley Fool） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| breadth.rsp_spy | RSP 領先 SPY YTD ≈5pp | RSP vs SPY YTD 2026 breadth | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 top-10 集中度 ≈36.5% | S&P 500 top 10 concentration 2026 | https://www.ebc.com/forex/rsp-vs-spy （EBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.advance_decline | 領導由 top-100 向 bottom-400 擴散、廣度確認多頭 | market breadth advance decline August 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 55（Greed） | CNN Fear and Greed today August 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）≈1,417,225、YoY ≈+38.6%、MoM −5.7%（原定 FINRA） | FINRA margin debt July 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt （GuruFocus） | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| retail.aaii | AAII 偏多 35.5%、偏空 39.9%（週結 2026-08-19） | AAII investor sentiment August 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 標售無明顯 tail、12.10% allotted at high | US Treasury 30-year auction August 2026 | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2026/R_20260813_3.pdf （TreasuryDirect） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| monetary.fedwatch | FedWatch 9/16 按兵不動 ≈68.4%、尾端為升息 | CME FedWatch September 2026 hold probability | https://en.macromicro.me/series/1645/probability-fed-rate-decrease （MacroMicro） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_capex | top-4（MSFT、GOOGL、AMZN、META）2026 capex 合計 ≈$725bn、+77% YoY（Q2 2026 財報後） | hyperscaler 2026 capex guidance Microsoft Google Amazon Meta | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.token_growth | Anthropic run-rate 年增約 7 倍、API 佔營收多數 | Anthropic token growth revenue 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html （CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.openai_anthropic_revenue | OpenAI ≈$40B、Anthropic ≈$65B run-rate | OpenAI Anthropic annualized revenue August 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html （CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.compute_supply_demand | GPU 現貨租金高於合約價 2 倍以上，產能被利用率吸收 | AI GPU rental pricing utilization August 2026 | https://www.uncoveralpha.com/p/amazon-google-microsoft-meta-q2-earnings （UncoverAlpha） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex > FCF、2026 hyperscaler 發債擴張 | hyperscaler external financing capex FCF debt 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow （FactSet） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 ≈105（OpenAI 40＋Anthropic 65）vs 年化 capex ≈725（$bn；分母：top-4） | AI revenue to capex gap 2026 | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.capital_cycle | [quarterly_state] 供給側 capex 年增約 77%、需求側 token／營收成長並存 | AI capex growth rate supply demand 2026 | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日窗掃描：0 件合格事件 | AI rename SPAC ticker change August 2026 | Renaissance Capital / SEC EDGAR / 新聞掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD IPO ≈232 件（截至 2026-08-21），單週無無營收 AI IPO 暴衝 | US IPO count August 2026 | https://stockanalysis.com/ipos/2026/ （StockAnalysis） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日窗掃描：0 檔合格 | microcap 100% single day surge quantum AI August 2026 | Finviz / Benzinga / StockTwits movers 掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 10 月 IPO、估值 ≈$2T | Anthropic OpenAI IPO 2026 | https://finance.yahoo.com/markets/article/spacex-openai-and-anthropic-here-are-the-most-anticipated-ipos-in-2026-114439441.html （Yahoo Finance） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 14 日窗合格 Form 4 集中賣出：0 起 | insider Form 4 AI executives August 2026 | SEC EDGAR / openinsider 掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.52（日讀數；9 日均總量 0.85） | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio （thetrading.tools） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美股槓桿 ETF 總 AUM 創紀錄 ≈$198bn；TQQQ 31.3、SOXL 17.3（$bn） | leveraged ETF AUM record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| structural.us_single_stock_etf | 單一個股槓桿 ETF 30 日窗新核准／上市：0 件 | single-stock leveraged ETF launch SEC August 2026 | SEC EDGAR / ETF.com new launches 掃描 | — | 2026-08-24T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 8 月佔比創紀錄 ≈62.4% | 0DTE SPX volume share August 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august （Cboe） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| structural.options_volume | OCC YTD 日均 >71（百萬口），量能高檔（2026-07 資料） | OCC options volume 2026 | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/historical-volume-statistics （OCC） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 16.01、期限結構 contango（IVTS ≈0.82）、SKEW 偏高 | VIX term structure SKEW August 2026 | https://www.thetrading.tools/vix-term-structure （thetrading.tools） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt／市值交叉檢核（2026-07 月資料，YoY +38.6%；主讀數見 retail.margin_debt） | FINRA margin debt equity market cap ratio 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt （GuruFocus） | 2026-07-01 | 2026-08-24T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-24",
  "iso_week": "2026-W35",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-22",
  "prior_date": "2026-08-20",
  "prior_answer": "yes",
  "flip_evidence": ["valuation.ndx_drawdown", "ai.hyperscaler_capex", "monetary.hy_oas"],
  "yes_basis": [],
  "r1_drawdown_pct": 4.41,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

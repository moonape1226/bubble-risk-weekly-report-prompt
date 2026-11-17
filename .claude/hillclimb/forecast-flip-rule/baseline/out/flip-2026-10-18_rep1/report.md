> [DRY RUN] this report was not committed to archive.

# 2026-10-18 AI 泡沫破裂預測報告

報告日期：2026-10-18｜ISO 週次：2026-W42｜預測窗口：2026-10-18 → 2027-04-18｜前次基準：report-2026-09-13（35天前）

## 結論

**結論：yes**

維持前次 yes：R3 與 R1 的傳導鏈在前次之後進一步升溫——CoreWeave 5Y CDS 於 2026-10-15 創紀錄 1,194.5 bps（`valuation.ai_credit_schism`），HY OAS 自前次基準走闊 58 bps 至 3.23%（`monetary.hy_oas`），而 Fed 目標區間上調 25 bps 至 3.75–4.00%（`monetary.fed_funds`）壓縮了緩衝空間。前次之後沒有任何新證據削弱三條路徑，依翻轉紀律不構成改判依據。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29935.59（2026-10-15），252 交易日最高收盤 31224.69（2026-10-06），距 52 週高點回撤 4.13%；R1 門檻水位為 23418.52，自最新收盤還需再下跌約 21.77% 才會觸發（`valuation.ndx_drawdown`）。指數 10 月初才創高，價格面尚未出現回撤啟動；但情緒與廣度已明顯轉弱：CNN Fear & Greed 約 18（極度恐懼，2026-10-16，`retail.fear_greed`），10-16 上漲家數約 29 對下跌 71（`breadth.advance_decline`），IPO 市場兩週內第 4 檔撤件或延後（2026-10-16，`speculation.ipo_heat`）。估值仍處極端：Shiller CAPE 約 40.54（2026-10-16，`valuation.sp500_pe_cape`），BofA 10 月調查科技股淨加碼約 37、為 2020 年 8 月以來最高（`institutional.bofa_jpm_survey`），部位擁擠。S&P 500 距 200 日均線 +5.34%、距 52 週均線 +6.78%（2026-10-16，`valuation.sp500_trend`），延伸幅度溫和。

**判讀：** 價格距門檻仍遠（需再跌約 21.77%），但情緒、廣度、IPO 撤件與擁擠部位同時轉弱；若 R3 的 AI 信用壓力（CoreWeave CDS 紀錄高點）演變為實際信用事件，或窗口內季報出現 capex／營收失望，在高 CAPE 與擁擠部位下 182 天內完成 25% 回撤是可行路徑。

### R2 資本支出收縮

本次取得的最近官方指引為 2026-07-28 季報（2026 Q2）後的合計數：Microsoft、Alphabet、Amazon、Meta 四家 2026 capex 合計約 725（CNBC，`ai.hyperscaler_capex`）。本次證據未提供四家各自的指引數字；依 carry-forward，四家方向均記為「未見下修」——Microsoft 未見下修、Alphabet 未見下修（CNBC 標題指出 Alphabet 季報後市場對 capex 審視升高）、Amazon 未見下修、Meta 未見下修。目前已下修家數：0／4。下一輪（2026 Q3）季報落在窗口內，確切日期未在本次證據中取得。年化 AI 終端營收（Anthropic run-rate 約 65，2026-08-17）對 top-4 capex 約 725 的落差仍大（`ai.revenue_capex_gap`，分母僅含 top-4，不含 Oracle 與 neocloud）。

**判讀：** R2 距成立最遠——需兩家在窗口內正式下修。窗口內有兩輪季報，但目前沒有任何一家下修的證據；R2 較可能作為 R1／R3 的後續結果而非起點。

### R3 AI 信用事件

符合 R3 規模門檻的主要候選為 CoreWeave（AI 算力為主業的大型借款人）。其 5Y CDS 於 2026-10-15 報導創紀錄 1,194.5 bps，報導標題指 AI 信用疑慮推升科技業違約保險至紀錄高點（`valuation.ai_credit_schism`）——信用端已開始重定價，而 NASDAQ-100 仍貼近高點，屬股債分歧的後期訊號。融資面：Lambda 取得約 1 十億美元 GPU 擔保融資（2026-10-01，`structural.ai_infrastructure_debt`），顯示 GPU 抵押債務仍在疊加。整體高收益信用 HY OAS 3.23%（2026-10-15，較前次基準 +58 bps，`monetary.hy_oas`），IG OAS 0.84%（+4 bps，`monetary.ig_oas`）。本次證據未見任何破產申請、寬限期後違約、covenant waiver 或 distressed exchange；近期到期與再融資時程未在本次證據中取得。

**判讀：** 尚無實際信用事件，但 CDS 紀錄高點代表市場對 CoreWeave 類借款人的違約定價已大幅上升；窗口內若融資市場持續收緊（HY 走闊、Fed 升息）而再融資遭阻，distressed exchange 是最可能的觸發形式，並可回頭觸發 R1。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 於 2026-10-15 創紀錄 1,194.5 bps，AI 信用疑慮推升科技違約保險至紀錄高點；信用端已重定價而股價未跟上（`valuation.ai_credit_schism`）。
- [整體] 信用與利率波動同步惡化：HY OAS 3.23%（2026-10-15，較 2026-09-11 +58 bps，`monetary.hy_oas`）；MOVE 101.1（2026-10-16，較前次 82.21 上升 18.89，`structural.treasury_basis_trade`）。
- [整體] 貨幣條件收緊、緩衝空間縮小：Fed 目標區間上調 25 bps 至 3.75–4.00%（2026-10-17，`monetary.fed_funds`），10Y 殖利率 5.10%（+14 bps，`monetary.dgs10`）、實質殖利率 2.78%（+18 bps，`monetary.dfii10`），CPI YoY 3.72%（2026-09 資料，`monetary.cpi_yoy`）限制 Fed 在 AI 主導下跌時降息托底。
- [R1] 情緒與風險偏好急轉：CNN Fear & Greed 約 18 極度恐懼（2026-10-16，`retail.fear_greed`）、上漲 29 對下跌 71（2026-10-16，`breadth.advance_decline`）、IPO 兩週內第 4 檔撤件或延後（2026-10-16，`speculation.ipo_heat`）。
- [R1] 估值與部位擁擠：Shiller CAPE 約 40.54（2026-10-16，`valuation.sp500_pe_cape`）；BofA 10 月調查科技股淨加碼約 37、2020 年 8 月以來最高（2026-10-13，`institutional.bofa_jpm_survey`）；單一個股槓桿 ETF 規模約 40.04（2026-10-16，`structural.leveraged_etf_aum`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收（Anthropic run-rate 約 65，2026-08-17）對 top-4 2026 capex 約 725（分母：top-4，不含 Oracle）落差懸殊（`ai.revenue_capex_gap`）。

## 支持 no 的證據

- [R1] NASDAQ-100 於 2026-10-06 才創 252 日高點 31224.69，2026-10-15 收盤 29935.59，距 52 週高點回撤 4.13%，需再跌約 21.77% 至 23418.52 才觸發 R1（`valuation.ndx_drawdown`）。
- [R2] 四大 hyperscaler 2026 capex 合計約 725（2026-07-28），本次證據未見任何一家下修，0／4（`ai.hyperscaler_capex`）。
- [整體] 美元資金管道未見失序：SOFR−IORB −1 bp、SOFR99−IORB +7 bps（2026-10-15），SRF 動用 0（2026-10-16）（`monetary.repo_stress_srf`）；10Y 標售 bid-to-cover 約 2.77、需求強勁（2026-10-07，`monetary.treasury_auctions`）；IG OAS 僅 +4 bps 至 0.84%（`monetary.ig_oas`）。
- [R3] AI 基礎設施融資管道仍開放：Lambda 取得約 1 十億美元 GPU 擔保融資（2026-10-01，`structural.ai_infrastructure_debt`）；Anthropic 目標 11 月中上市（2026-10-05，`speculation.upcoming_ai_ipos`），股權資金仍可取得。
- [R1] 價格延伸與波動度溫和：S&P 500 距 200 日均線 +5.34%（2026-10-16，`valuation.sp500_trend`）；VIX 16.46（2026-10-15），7 日 S&P 500 −0.27%、VIX +6.81%，未出現同漲警戒（`structural.vix_spx_comove`）。
- [整體] 算力需求未見崩價：H100 隨選中位租金約 4.20（2026-10-07，`ai.compute_supply_demand`）。

## 與前期比較

前次結論：yes（report-2026-09-13）

本次結論：維持

- R3：CoreWeave 5Y CDS 創紀錄 1,194.5 bps（2026-10-15）——為前次之後的新證據，方向強化 yes，不支持翻轉。
- 信用／波動：HY OAS 由 2.65% 走闊至 3.23%、MOVE 由 82.21 升至 101.1——強化 yes。
- 政策：Fed 目標區間上調 25 bps、10Y 升至 5.10%——收緊金融條件，強化 yes。
- R1：NASDAQ-100 於 2026-10-06 創新高，回撤水位與前次大致相同，距門檻仍遠——未改變 R1 判讀，亦不構成翻轉 no 的新證據。
- R2：無新 capex 指引（最近為 2026-07-28），0／4 下修——與前次相同。前次之後無任何新證據削弱路徑分析，故維持 yes。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源完成檢索但無合格披露（✗ NOT DISCLOSED），不作為證據：valuation.analyst_tp_decomposition、retail.social_sentiment、retail.naaim、monetary.fedwatch、monetary.private_credit_liquidity、ai.token_growth、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（event_scan 30 日無事件）、ai.depreciation_life、ai.capital_cycle（兩組件皆無披露）、speculation.equity_put_call、structural.global_leveraged_approvals。其中私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）與 hyperscaler 融資結構事件掃描若有披露，可能直接影響 R3 判讀；缺漏使 R3 證據集中於單一 CDS 報導。

程序註記：檢索紀錄稱美債基差交易槓桿的三個 script 區塊失敗，但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 均為 status ok，本報告以 artifact 為準記 ✓ API。

最大不確定性：

1. CoreWeave 的近期到期與再融資時程未取得——若窗口內有大額再融資遭阻，R3 可能直接成立（推向 yes）；若順利展延，R3 時程延後（推向 no）。
2. 窗口內季報的四家 capex 指引——任一家下修會使 R2 與 R1 同步升溫（推向 yes）；全面上修則削弱 yes。
3. Fed 政策路徑：目標區間剛上調，CPI 3.72%；若升息延續，信用利差進一步走闊（推向 yes）；若轉向官方市場功能回應（official market-functioning backstop），可延緩 R1／R3（推向 no）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest | 7659.44 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 5.34 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 6.78 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29935.59 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 4.13 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q2） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 4.0 | FRED API (series_id=DFEDTARU) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.75 | FRED API (series_id=DFEDTARL) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 3.23 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.84 | FRED API (series_id=BAMLC0A0CM) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 5.1 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.78 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.35 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 101.91 | FRED API (series_id=DCOILWTICO) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.33 | FRED API (series_id=T5YIFR) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest | 1.0729 | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.89 | FRED API (series_id=SOFR) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.97 | FRED API (series_id=SOFR99) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.9 | FRED API (series_id=IORB) | 2026-10-18 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest | 0.0 | FRED API (series_id=RPONTTLD) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6755639.0（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5943911.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6250253.0（¥625.03T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.46 | FRED API (series_id=VIXCLS) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 16.46 | FRED API (series_id=VIXCLS, SP500) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2097.9713（$2.10T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -6883343 | CFTC TFF futures-only | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 101.1 | Yahoo Finance chart API (^MOVE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2264.1 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（multpl） | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（月頻 carry-forward） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py BOGZ1FL153064486Q | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py DFEDTARU, DFEDTARL | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py BAMLH0A0HYM2 | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py BAMLC0A0CM | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py DGS10 | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | scripts/fetch_macro.py DFII10 | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py T10YIE（FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py DCOILWTICO | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | scripts/fetch_macro.py CPIAUCSL yoy_pct | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py T5YIFR | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py THREEFYTP10 | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py SOFR, SOFR99, IORB, RPONTTLD | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch | ✗ NOT DISCLOSED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py WALCL | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py ECBASSETSW, JPNASSETS | ✓ API（ECBASSETSW ok；JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（季頻 carry-forward） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch（quarterly_state carry；event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch（季頻組合） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch（quarterly_state carry；event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch＋SEC EDGAR 8-K（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch movers screen（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✗ NOT DISCLOSED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py VIXCLS＋vix_spx_comove | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py LNFACBW027SBOG | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds, move_index, ofr_repo | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.54 | Shiller PE CAPE ratio current October 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 成員 MSFT 前瞻本益比 24.5 | Magnificent 7 forward P/E valuation October 2026 | https://articlegateway.com/?p=146 | 2026-09-24 | 2026-10-18T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 紀錄 1,194.5 bps | AI credit fears tech default insurance record highs October 2026 | https://www.businessday.co.za/world/international-companies/2026-10-15-ai-credit-fears-push-tech-default-insurance-to-record-highs/（BusinessDay） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 報酬約 12.08 | RSP equal weight vs SPY YTD performance 2026 | https://pro.thestreet.com/market-commentary/rsp-vs-spy-does-diversification-require-equal-weight（TheStreet） | 2026-07-18 | 2026-10-18T09:30:00+08:00 |
| breadth.top10_concentration | 前十大集中度約 38.9 | S&P 500 top 10 concentration percent record 2026 | https://walnutinvest.com/stats/market-concentration-statistics | 2026-07-31 | 2026-10-18T09:30:00+08:00 |
| breadth.advance_decline | 上漲家數約 29 對下跌 71 | market breadth October 16 2026 percent above 200-day advance decline | https://www.thetrading.tools/market-breadth | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 極度恐懼約 18（原定來源 CNN） | CNN Fear and Greed Index October 16 2026 extreme fear | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.margin_debt | margin debt 約 1.45 兆美元（2026-08 月資料） | FINRA margin debt August 2026 year over year | https://www.thetrading.tools/margin-debt（原定來源 FINRA） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.7 | AAII sentiment survey week ending October 14 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA 10 月 FMS 科技股淨加碼約 37，2020 年 8 月以來最高 | BofA October 2026 fund manager survey tech overweight cash | https://www.bloomberg.com/news/articles/2026-10-13/bofa-poll-shows-investors-most-exposed-to-tech-stocks-since-2020（Bloomberg） | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.77 | Treasury 10-year note auction October 7 2026 bid-to-cover | https://www.rttnews.com/3697286/ten-year-note-auction-attracts-strong-demand.aspx（RTTNews） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate social financing 2026 total | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm（SteelOrbis） | 2026-08-15 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 725（2026 Q2 季報） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65 | OpenAI Anthropic annualized revenue run rate 2026 | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選中位租金約 4.20 | GPU rental price index HBM DRAM contract price October 2026 | https://uvik.net/blog/gpu-price-index/ | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 2026 年 hyperscaler 發債預估約 190（背景，非新證據） | hyperscaler bond issuance 2026 capex versus free cash flow | https://www.twentyfouram.com/insights/oracle-clears-the-supply-cloud-with-record-demand（TwentyFour AM） | 2026-02-02 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic run-rate 約 65；分母 top-4 capex 約 725 取自 ai.hyperscaler_capex | AI revenue versus capex gap 2026 annualized | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement October 2026 | 檢查來源：SEC EDGAR 8-K、SPACInsider、Boardroom Alpha | — | 2026-10-18T09:30:00+08:00 |
| speculation.ipo_heat | 兩週內第 4 檔 IPO 撤件或延後 | IPO market October 16 2026 pulled postponed Firmus Oura | https://www.ipox.com/ipox/the-ipox-update-10162026（IPOX） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描（0 件符合 2+ 主題×弱基本面） | biggest stock gainers week October 12-16 2026 microcap 100% | 檢查來源：Tapeboard movers archive、Financial Modeling Prep daily gainers、Yahoo movers | — | 2026-10-18T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 11 月中上市 | Anthropic IPO October 2026 timing valuation S-1 | https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market（CNN） | 2026-10-05 | 2026-10-18T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件合格） | insider selling Form 4 October 2026 Nvidia AI executives SEC | 檢查來源：SEC EDGAR NVDA Form 4 列表（窗內申報無 filing-level 具名／金額細節） | — | 2026-10-18T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.04 | single stock leveraged ETF assets October 2026 weekly flows | https://www.etfaction.com/single-stock-traders-pile-into-tsll-and-intw-as-levered-flows-surge/（ETF Action） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval October 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed | — | 2026-10-18T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 月度 ADV 創紀錄約 3.4 百萬口（2026-09 月資料） | Cboe September 2026 derivatives volume 0DTE SPX record | https://www.cboe.com/insights/posts/market-metrics-that-matter-derivatives-september-2026-volume-highlights（Cboe） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.options_volume | 9 月總結算量約 1,486,062,415 口（2026-09 月資料） | OCC September 2026 monthly volume data | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report（OCC） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 約 14.84、SKEW 154.34 | VIX term structure SKEW October 2026 options brief | https://www.home.saxo/content/articles/options/the-middle-got-cheaper-the-edge-did-not---options-brief---12-october-2026-12102026（Saxo） | 2026-10-12 | 2026-10-18T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 1.45 兆美元（2026-08 月資料） | margin debt to market cap August 2026 | https://www.thetrading.tools/margin-debt | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Lambda GPU 擔保融資約 1 十億美元 | AI data center debt Lambda CoreWeave financing October 2026 | https://valueaddvc.com/pulse/ai-data-center-debt-financing-risk-2026 | 2026-10-01 | 2026-10-18T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-10-18",
  "iso_week": "2026-W42",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "yes",
  "horizon_end": "2027-04-18",
  "prior_date": "2026-09-13",
  "prior_answer": "yes",
  "flip_evidence": [],
  "r1_drawdown_pct": 4.13,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

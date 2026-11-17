> [DRY RUN] this report was not committed to archive.

# 2026-10-18 AI 泡沫破裂預測報告

報告日期：2026-10-18｜ISO 週次：2026-W42｜預測窗口：2026-10-18 → 2027-04-18｜前次基準：report-2026-09-13（35天前）

## 結論

**結論：no**

三條路徑都沒有已在進行、且可望於 182 天內完成的跡象：NASDAQ-100 距 52 週高點回撤 4.13%，距 R1 門檻還要再跌約 21.77%（`valuation.ndx_drawdown`）；四大 hyperscaler 的 capex 指引沒有任何一家下修的證據（`ai.hyperscaler_capex`）。CoreWeave 5Y CDS 創紀錄（1,194.5 bps，`valuation.ai_credit_schism`）與 HY OAS 走闊 58 bps 是本次最強的 yes 側訊號，但仍屬信用重定價，不是 R3 所要求的違約或 distressed exchange。在基準率之下，這些證據還不足以支持 yes。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,935.59（2026-10-15）；252 個交易日最高收盤 31,224.69（2026-10-06）；距 52 週高點回撤 4.13%。R1 門檻水位 23,418.52（`valuation.ndx_drawdown`），也就是從最新收盤還要再跌約 21.77% 才會觸發。高點僅在 9 天前，指數仍貼近高位。S&P 500 收 7,659.44（2026-10-16），高於 200 日 MA 5.34%、高於 52 週 MA 6.78%（`valuation.sp500_trend`），仍處於價格延伸區。VIX 16.46，VIX 與 S&P 500 未同步上升（`structural.vix_spx_comove`）。不過情緒面已經轉弱：CNN Fear & Greed 約 18，屬極度恐懼（2026-10-16，`retail.fear_greed`）；上漲對下跌家數約 29 比 71（`breadth.advance_decline`）；兩週內已有第 4 檔 IPO 撤件或延後（`speculation.ipo_heat`）。

**判讀：** 距門檻仍遠，再跌約 21.77% 才會成立。要在窗口內推過門檻，需要信用事件（R3）或 capex 下修（R2）引發的強制去槓桿，或者在 Fed 升息後利率衝擊持續擴大；目前 VIX 與 repo 都沒有失序跡象。

### R2 資本支出收縮

本次證據只含四大 hyperscaler 2026 capex 合計約 725（十億美元級，CNBC，2026-07-28，`ai.hyperscaler_capex`，沿用最近一次財報季的指引）。Microsoft、Alphabet、Amazon、Meta 各自的最新指引數字，以及相對前次指引的方向，本次證據都沒有逐家拆分，因此逐家方向記為「不可得」。可以確認的是，至今沒有任何證據顯示四家之中有哪一家下修，已下修家數為 0。下一輪季報與 2027 年初的年度指引都落在窗口內，但確切日期本次證據沒有提供。需求側的對照：Anthropic 年化 run-rate 約 65（十億美元，2026-08-17，`ai.openai_anthropic_revenue`）；H100 隨選中位租金約 4.20（美元／小時，2026-10-07，`ai.compute_supply_demand`），目前沒有搭配利用率下滑的證據。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 65 vs 年化 capex 約 725（分母：top-4，未含 Oracle 與 neocloud；分子只含 Anthropic），比值約 9%（`ai.revenue_capex_gap`）。缺口很大，但這屬於脆弱度問題，不是下修事件。

**判讀：** 沒有任何一家下修，距「兩家下修」的門檻還很遠。窗口內有兩個財報季，若 HY 利差持續走闊、股價回落，可能促使管理層轉趨保守，但目前沒有指引方向轉變的證據。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）正在擴大：CoreWeave 5Y CDS 創紀錄，達 1,194.5 bps（2026-10-15，`valuation.ai_credit_schism`）。若假設回收率 40%，市場隱含的年化違約強度約 20%，換算到 6 個月約一成，屬高風險但仍遠低於多數情境。CoreWeave 以 AI 算力為主業，但其負債金額本次證據沒有載明，因此是否符合 R3 的 50 億美元門檻需要另行確認。AI infrastructure debt financing / vendor-financing loops 仍在擴張：Lambda 取得約 10 億美元的 GPU 擔保融資（2026-10-01，`structural.ai_infrastructure_debt`），顯示資金市場仍對 neocloud 開放。整體信用環境：HY OAS 3.23%，較前次 +58 bps（`monetary.hy_oas`）；IG OAS 0.84%，只 +4 bps（`monetary.ig_oas`）。本次證據沒有破產申請、付款違約、covenant waiver 或 distressed exchange 的披露。

**判讀：** R3 是三條路徑中最接近的一條，CDS 已處於困境定價區，但目前只有價格訊號，沒有違約事件。在窗口內推過門檻，需要 CoreWeave 等借款人出現再融資失敗、寬限期後付款違約，或完成 distressed exchange；而 Lambda 的新融資顯示融資管道仍然暢通。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 於 2026-10-15 創紀錄，達 1,194.5 bps，AI 信用定價分歧開始反映在信用端；隱含年化違約強度約 20%（`valuation.ai_credit_schism`）。
- [整體] 信用與利率同步收緊：HY OAS 3.23%（2026-10-15，較前次 +58 bps，`monetary.hy_oas`）；Fed 目標區間上緣由 3.75% 升至 4.00%（2026-10-17，`monetary.fed_funds`）；10Y 殖利率 5.10%（`monetary.dgs10`）；CPI YoY 3.72%（2026-09 月資料，`monetary.cpi_yoy`）；WTI 101.91（`monetary.wti`）。通膨壓力限制了 Fed 緩衝 AI 主導回撤的空間。
- [R1] 風險偏好急轉：Fear & Greed 約 18，屬極度恐懼（2026-10-16，`retail.fear_greed`）；上漲對下跌約 29 比 71（`breadth.advance_decline`）；兩週內第 4 檔 IPO 撤件或延後（2026-10-16，`speculation.ipo_heat`）；MOVE 101.1，較前次 82.21 大幅上升（`structural.treasury_basis_trade`）。
- [R1] 部位擁擠：BofA 2026-10 FMS 科技股淨加碼約 37%，為 2020 年 8 月以來最高（`institutional.bofa_jpm_survey`）；Shiller CAPE 約 40.54（`valuation.sp500_pe_cape`）；S&P 500 高於 200 日 MA 5.34%（`valuation.sp500_trend`）。一旦開始下跌，跌幅可能放大。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）約 65 vs 725，比值約 9%（`ai.revenue_capex_gap`），ROI 壓力是窗口內財報季的潛在下修誘因。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.13%，高點只在 2026-10-06，距門檻 23,418.52 還要再跌約 21.77%（`valuation.ndx_drawdown`）。
- [R2] 四大 hyperscaler 2026 capex 合計約 725，沒有任何一家下修的證據，已下修家數為 0，達 R2 需要兩家（`ai.hyperscaler_capex`）。
- [R3] AI 信用事件只到價格層面，沒有違約或 distressed exchange；Lambda 於 2026-10-01 仍取得約 10 億美元 GPU 擔保融資，融資管道暢通（`structural.ai_infrastructure_debt`）。
- [整體] 融資市場運作正常：SOFR−IORB −1 bps、SOFR99−IORB +7 bps（2026-10-15），SRF 動用 0（2026-10-16，`monetary.repo_stress_srf`）；IG OAS 只有 0.84%（`monetary.ig_oas`）；VIX 16.46，VIX 與 S&P 500 未同步上升（`structural.vix_spx_comove`），尚未進入強制去槓桿階段。
- [整體] 基準率：任一 182 天窗口內 R1–R3 都屬罕見事件；目前的證據說明泡沫存在、下行空間大，但三條路徑都沒有已在進行的觸發事件。需求側仍在擴張：Anthropic run-rate 約 65（`ai.openai_anthropic_revenue`），Anthropic 目標 11 月中上市（`speculation.upcoming_ai_ipos`）。

## 與前期比較

前次結論：yes（report-2026-09-13）
本次結論：翻轉
翻轉依據：

- 前次 forecast 沒有記錄 `yes_basis`（該欄位建立前的舊預測），因此沒有可逐項驗證的前次 yes 理由；依規則，yes 每次都必須重新取得，不能沿用。R1：NASDAQ-100 距 52 週高點回撤 4.13%，與前次 4.21% 幾乎相同，距門檻仍要再跌約 21.77%，沒有任何路徑已在進行的證據（`valuation.ndx_drawdown`）。
- R2：四大 hyperscaler capex 指引仍沿用合計約 725，沒有任何一家下修，R2 條件的距離與前次相同（`ai.hyperscaler_capex`）。
- R3：CoreWeave CDS 1,194.5 bps 創紀錄，是前次以後新出現的最強負面訊號，但仍屬價格訊號而非違約事件；以基準率衡量，不足以讓 yes 勝出（`valuation.ai_credit_schism`）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源為 ✗ NOT DISCLOSED（完成掃描但無合格披露）：analyst TP 分解、social sentiment、NAAIM、FedWatch、私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）、token growth、backlog 重複計算風險（RPO double-counting）、折舊年限變動（depreciation useful-life change）、hyperscaler 融資結構（capex vs FCF / 發債）的 event_scan、資本週期階段（capital cycle stage）兩組件、put/call、全球槓桿產品核准。其中私募信貸贖回壓力與 hyperscaler 融資事件的缺漏若實際存在 gate proration / breach 或大型 SPV 融資問題，可能強化 R3 判斷，屬於可能改變答案方向的缺口，但本次沒有證據顯示存在。

資料一致性備註：搜尋紀錄將美債基差交易槓桿列為「script 三區塊 fetch_failed」，但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 三塊皆為 `status: ok`；本報告以 artifact 為準，記 ✓ API。hyperscaler capex 只取得四家合計值，逐家指引與方向不可得，這會降低 R2 判讀的精細度，但不影響「無下修證據」的結論。

最大的不確定性：

1. 10 月下旬至 11 月初的 hyperscaler 季報（確切日期本次證據未提供）：若有兩家下修 capex，R2 直接成立，會推向 yes；若維持或上修，則強化 no。
2. CoreWeave 等 neocloud 的再融資：CDS 已處困境定價區，一旦出現付款違約或 distressed exchange，R3 成立，並可能經由信用傳導觸發 R1，會推向 yes。
3. Fed 升息後的利率路徑：10Y 5.10%、CPI 3.72%，若進一步升息或期限溢價跳升，會推向 yes；若 Anthropic IPO（目標 11 月中）順利完成，則有助穩定 AI 風險偏好，推向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7659.44 | FRED API (series_id=SP500) sp500_trend | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日 MA 偏離 %） | 5.34 | FRED API (series_id=SP500) sp500_trend | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週 MA 偏離 %） | 6.78 | FRED API (series_id=SP500) sp500_trend | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29935.59 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-06 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 4.13 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2 觀測，家庭股票配置 %） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 4.0（%） | FRED API (series_id=DFEDTARU) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.75（%） | FRED API (series_id=DFEDTARL) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 3.23（%） | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 58.0（bps，較 2026-09-11） | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.84（%） | FRED API (series_id=BAMLC0A0CM) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 5.1（%） | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | 14.0（bps） | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.78（%） | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.35（%） | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 101.91（美元／桶） | FRED API (series_id=DCOILWTICO) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72（%） | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.33（%） | FRED API (series_id=T5YIFR) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 1.0729（%） | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.89（%） | FRED API (series_id=SOFR) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.97（%） | FRED API (series_id=SOFR99) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.9（%） | FRED API (series_id=IORB) | 2026-10-18 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用 transaction volume） | 0.0（十億美元） | FRED API (series_id=RPONTTLD) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,755,639（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,943,911（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（no_new_obs） | 6,250,253（¥625.03T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.46 | FRED API (series_id=VIXCLS) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（comove=false，base 2026-10-08，window 7 日） | 16.46 | FRED API (SP500 paired, script block vix_spx_comove) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 6.81（%） | FRED API (SP500 paired, script block vix_spx_comove) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -0.27（%） | FRED API (SP500 paired, script block vix_spx_comove) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2097.9713（$2.10T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位） | -6,883,343（口） | CFTC TFF futures-only, cftc_lev_funds | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -309,307（口） | CFTC TFF futures-only, cftc_lev_funds | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 101.1 | Yahoo chart API ^MOVE, move_index | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party transaction volume） | 2264.1（十億美元） | OFR STFM REPO-TRIV1_TV_TOT-P, ofr_repo | 2026-10-16 | 2026-10-18T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（multpl） | ✓ SEARCH-VERIFIED（CAPE；P/E 未取得） |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py BOGZ1FL153064486Q | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py BAMLH0A0HYM2 | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py BAMLC0A0CM | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py DGS10 | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py DFII10 | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py T10YIE（FRED 直接） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py DCOILWTICO | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py CPIAUCSL yoy_pct | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py T5YIFR | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py THREEFYTP10 | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch | ✗ NOT DISCLOSED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py WALCL | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py ECBASSETSW＋JPNASSETS | ✓ API（ECBASSETSW ok；JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（沿用最近財報季） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch；quarterly_state 為 stock_of_state，event_scan 為 30d 掃描 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch＋既有 bullets 組合 | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動（depreciation useful-life change） | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch；quarterly_state 為 stock_of_state，event_scan 為 30d 掃描 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch＋SEC EDGAR 8-K（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch movers 掃描（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✗ NOT DISCLOSED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py VIXCLS＋vix_spx_comove | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py LNFACBW027SBOG | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds＋move_index＋ofr_repo | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.54 | Shiller PE CAPE ratio current October 2026 multpl | https://www.multpl.com/shiller-pe（multpl；原定來源 multpl / gurufocus） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 成員 MSFT 前瞻本益比 24.5 | Magnificent 7 forward P/E valuation October 2026 | https://articlegateway.com/?p=146 | 2026-09-24 | 2026-10-18T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 紀錄 1,194.5 bps | AI credit fears tech default insurance record highs October 2026 | https://www.businessday.co.za/world/international-companies/2026-10-15-ai-credit-fears-push-tech-default-insurance-to-record-highs/（BusinessDay） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 報酬約 12.08% | RSP equal weight vs SPY YTD performance 2026 | https://pro.thestreet.com/market-commentary/rsp-vs-spy-does-diversification-require-equal-weight（TheStreet） | 2026-07-18 | 2026-10-18T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度約 38.9% | S&P 500 top 10 concentration percent record 2026 | https://walnutinvest.com/stats/market-concentration-statistics | 2026-07-31 | 2026-10-18T09:30:00+08:00 |
| breadth.advance_decline | 上漲家數約 29 對下跌 71 | market breadth October 16 2026 percent above 200-day advance decline | https://www.thetrading.tools/market-breadth | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 約 18（極度恐懼） | CNN Fear and Greed Index October 16 2026 extreme fear | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/（原定來源 cnn.com） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-08 月資料）約 1.45 兆美元 | FINRA margin debt August 2026 year over year | https://www.thetrading.tools/margin-debt（原定來源 FINRA） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.7%（週結束 2026-10-14） | AAII sentiment survey week ending October 14 2026 | https://www.aaii.com/sentimentsurvey | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA 2026-10 FMS 科技股淨加碼約 37%，2020 年 8 月以來最高 | BofA October 2026 fund manager survey tech overweight cash | https://www.bloomberg.com/news/articles/2026-10-13/bofa-poll-shows-investors-most-exposed-to-tech-stocks-since-2020（Bloomberg） | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.77 | Treasury 10-year note auction October 7 2026 bid-to-cover | https://www.rttnews.com/3697286/ten-year-note-auction-attracts-strong-demand.aspx（RTTNews） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate social financing 2026 total | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm | 2026-08-15 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 725（沿用 2026-07 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65 | OpenAI Anthropic annualized revenue run rate 2026 | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選中位租金約 4.20 | GPU rental price index HBM DRAM contract price October 2026 | https://uvik.net/blog/gpu-price-index/ | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 2026 年 hyperscaler 發債預估約 190 | hyperscaler bond issuance 2026 capex versus free cash flow | https://www.twentyfouram.com/insights/oracle-clears-the-supply-cloud-with-record-demand | 2026-02-02 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic run-rate 約 65（分母沿用 ai.hyperscaler_capex top-4 約 725） | AI revenue versus capex gap 2026 annualized | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement October 2026 | 檢查來源：SEC EDGAR 8-K、SPACInsider、Boardroom Alpha（窗內無合格事件） | — | 2026-10-18T09:30:00+08:00 |
| speculation.ipo_heat | 兩週內第 4 檔 IPO 撤件或延後 | IPO market October 16 2026 pulled postponed Firmus Oura | https://www.ipox.com/ipox/the-ipox-update-10162026（IPOX） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（0 件符合 2+ 主題×弱基本面） | biggest stock gainers week October 12-16 2026 microcap 100% | 檢查來源：Tapeboard movers archive、Financial Modeling Prep daily gainers、Yahoo movers（PFAI 10/7 +116.7% 落在窗外） | — | 2026-10-18T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 11 月中上市 | Anthropic IPO October 2026 timing valuation S-1 | https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market（CNN） | 2026-10-05 | 2026-10-18T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件合格） | insider selling Form 4 October 2026 Nvidia AI executives SEC | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表（10/9 有申報但無具名申報人／金額等 filing-level 細節） | — | 2026-10-18T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.04 | single stock leveraged ETF assets October 2026 weekly flows | https://www.etfaction.com/single-stock-traders-pile-into-tsll-and-intw-as-levered-flows-surge/（ETF Action；原定來源 etf.com / ETFGI） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval October 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed（窗內無合格核准或上市） | — | 2026-10-18T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 月度 ADV 創紀錄約 3.4 百萬口（2026-09 月資料） | Cboe September 2026 derivatives volume 0DTE SPX record | https://www.cboe.com/insights/posts/market-metrics-that-matter-derivatives-september-2026-volume-highlights（Cboe） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.options_volume | OCC 2026-09 總結算量約 1,486,062,415 口 | OCC September 2026 monthly volume data | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report（OCC） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
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
  "answer": "no",
  "horizon_end": "2027-04-18",
  "prior_date": "2026-09-13",
  "prior_answer": "yes",
  "flip_evidence": ["valuation.ndx_drawdown", "ai.hyperscaler_capex", "valuation.ai_credit_schism"],
  "yes_basis": [],
  "r1_drawdown_pct": 4.13,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

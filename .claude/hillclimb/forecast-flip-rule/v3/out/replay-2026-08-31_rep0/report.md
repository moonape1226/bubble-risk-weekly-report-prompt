> [DRY RUN] this report was not committed to archive.

# 2026-08-31 AI 泡沫破裂預測報告

報告日期：2026-08-31｜ISO 週次：2026-W36｜預測窗口：2026-08-31 → 2027-03-01｜前次基準：report-2026-08-27（4天前）

## 結論

**結論：no**

三條路徑都未在進行中：NASDAQ-100 距 52 週高點回撤僅 4.00%，距 R1 門檻仍需再跌約 21.9%（`valuation.ndx_drawdown`）；信用端無壓力訊號，HY OAS 2.63%、IG OAS 0.79%（`monetary.hy_oas`、`monetary.ig_oas`），且 CoreWeave 於 2026-08-10 仍能完成 $2.6bn GPU 抵押融資（`structural.ai_infrastructure_debt`）。估值與集中度顯示泡沫存在，但本次沒有證據顯示破裂會在 182 天內完成。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29433.43（2026-08-28），252 個交易日最高收盤 30660.6（2026-06-02），距 52 週高點回撤 4.00%（`valuation.ndx_drawdown`）。R1 門檻水位為 22995.45，自最新收盤須再下跌約 6437.98 點（約 21.9%）才會觸發。S&P 500 仍在 200 日均線之上 8.33%、52 週均線之上 9.76%（`valuation.sp500_trend`），屬價格延伸而非破位；VIX 14.51（2026-08-27）且 7 日窗口內 VIX 下跌 9.37%、S&P 500 上漲 1.18%，未出現 crowded-optionality 同漲讀數（`structural.vix_spx_comove`）。估值偏高——Shiller CAPE 41.59（`valuation.sp500_pe_cape`）、前十大集中度 37.6%（`breadth.top10_concentration`）——放大了一旦下跌的幅度，但本身不是時點催化劑。

**判讀：** R1 距離遙遠（需再跌約 21.9%）；要在窗口內觸發，需要一個外部催化劑，例如 hyperscaler 財報引發 capex/ROI 重估、AI 信用事件傳導，或利率／期限溢價急升造成估值壓縮，目前皆未出現。

### R2 資本支出收縮

本次取得的來源只揭露四大 hyperscaler（Microsoft、Alphabet、Amazon、Meta）2026 capex 合計約 $725bn（CNBC，2026-07-28，`ai.hyperscaler_capex`），未逐家列出最新正式指引數字與相對前次指引的方向；因此個別公司的 上修 / 持平 / 下修 本次無法逐家確立。已取得的來源中沒有任何一家下修的披露，故目前已確認下修家數為 0（共需 2 家）。該 CNBC 報導指出 Alphabet 財報後 capex 受到更高審視，但這是市場反應，不是指引下修。窗口內的下一次財報日期本次來源未提供，未能確立。

**判讀：** R2 尚未啟動；要在窗口內成立，需在後續兩輪財報（窗口涵蓋 2026 年秋季與 2027 年初的財報季）中有兩家將年度 capex 指引下修，目前只有「審視升高」的市場敘事，沒有指引方向轉折的證據。

### R3 AI 信用事件

本次唯一取得的 AI 基礎設施信用事件是 CoreWeave 於 2026-08-10 完成 DDTL 5.5 融資 $2.6bn（以 GPU 為抵押，`structural.ai_infrastructure_debt`），顯示該借款人仍能進入信用市場、取得新額度，屬反向（非違約）訊號。CoreWeave 的總負債是否 ≥ USD 5bn、近期到期與再融資牆，本次來源未提供，未能確立；其他 neocloud 借款人亦無在窗口內的資料。AI 發行人的債券利差／CDS 本次未取得可用披露。整體信用環境寬鬆：HY OAS 2.63%、IG OAS 0.79%，與前次持平（`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 −1 bp、SOFR99−IORB 7 bp，SRF 動用僅 $0.001bn（`monetary.repo_stress_srf`）。

**判讀：** R3 無任何 distress 訊號（無違約、covenant waiver、distressed exchange 或 going-concern 語言的披露）；要在窗口內成立，需出現一家大型 AI 算力借款人的再融資失敗或違約，前提通常是信用利差先明顯走闊，目前沒有看到。

## 支持 yes 的證據

- [R1] 估值處於極端高位：Shiller CAPE 41.59（2026-08-01），代表一旦出現催化劑，下行幅度可能很大，`valuation.sp500_pe_cape`。
- [R1] 價格延伸：S&P 500 在 200 日均線之上 8.33%（2026-08-28），均值回歸風險上升，`valuation.sp500_trend`。
- [整體] 槓桿與投機部位偏高：FINRA margin debt $1.42T、YoY 38.6%（2026-07 資料），`retail.margin_debt`；槓桿 ETF 總 AUM 約 $198bn、TQQQ 約 $37.3bn（2026-08-28），`structural.leveraged_etf_aum`；SPX 0DTE 約佔 60% 期權量（2026-08-28），`structural.zero_dte`。
- [R1] 市場廣度轉弱：成分股在 50 日均線之上比率僅 54%（2026-08-28），前十大集中度 37.6%（2026-07-31），`breadth.advance_decline`、`breadth.top10_concentration`。
- [R2] 四大 hyperscaler 2026 capex 合計約 $725bn，Alphabet 財報後市場對 capex 的審視升高（2026-07-28），是 R2 未來可能轉向的前提，`ai.hyperscaler_capex`。
- [整體] 通膨仍高、Fed 緩衝空間有限：CPI YoY 3.3%（2026-07），10Y 期限溢價（term premium）0.8682%、7 日上升 2.9 bp（2026-08-21），`monetary.cpi_yoy`、`monetary.term_premium`。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤僅 4.00%（2026-08-28），距 R1 門檻 22995.45 尚需再跌約 21.9%，`valuation.ndx_drawdown`。
- [R3] 信用利差極窄且無變化：HY OAS 2.63%、IG OAS 0.79%（2026-08-27），信用市場未對 AI 或整體風險重新定價，`monetary.hy_oas`、`monetary.ig_oas`。
- [R3] CoreWeave 2026-08-10 完成 $2.6bn GPU 抵押 DDTL 5.5 融資，AI 算力借款人仍有暢通的融資管道，`structural.ai_infrastructure_debt`。
- [整體] 資金市場平穩：repo 資金壓力（SOFR−IORB）−1 bp（2026-08-27），SRF 動用 $0.001bn（2026-08-28），`monetary.repo_stress_srf`；MOVE 70.97（2026-08-28），`structural.treasury_basis_trade`。
- [R1] 波動與情緒未過熱：VIX 14.51 且 7 日下跌 9.37%（2026-08-27），`structural.vix_spx_comove`；CNN Fear & Greed 中性 54（2026-08-28），`retail.fear_greed`；AAII 看空 44.4% 高於看多 32.9%（2026-08-26），`retail.aaii`。
- [R2] 已取得的來源中沒有任何 hyperscaler 下修 capex 指引；2026 合計約 $725bn 為擴張水位（2026-07-28），`ai.hyperscaler_capex`。
- [整體] 基準率：任一 182 天窗口內 R1–R3 皆屬罕見；Mag 7 加權前瞻本益比約 24（2026-08-03），估值極端集中在指數層級而非 AI 龍頭，`valuation.mag7_multiples`。

## 與前期比較

前次結論：無前次預測（report-2026-08-27 為舊格式評分報告）

本次為新格式下的首次預測；舊格式評分不轉換為 yes/no，flip_evidence 為空。自 2026-08-27 以來的主要變化：NASDAQ-100 最新收盤 29433.43（2026-08-28），S&P 500 較前次下跌 0.25%；DGS10、DFII10、HY OAS、IG OAS 無新觀測（持平），T10YIE 下降 2 bp、T5YIFR 下降 3 bp；RPONTTLD 自 $0.101bn 降至 $0.001bn。上述變化都沒有改變三條路徑的距離。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源為 ✗ NOT DISCLOSED（搜尋完成但窗口內無合格披露）：valuation.analyst_tp_decomposition、valuation.ai_credit_schism、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.treasury_auctions、monetary.pboc、monetary.private_credit_liquidity、ai.token_growth、ai.openai_anthropic_revenue、ai.customer_concentration_rpo、ai.compute_supply_demand、ai.hyperscaler_financing_mix、ai.revenue_capex_gap、ai.depreciation_life、ai.capital_cycle、speculation.upcoming_ai_ipos、structural.global_leveraged_approvals。其中最可能影響答案的是 valuation.ai_credit_schism（AI 發行人利差／CDS）與 monetary.private_credit_liquidity：若其中出現利差顯著走闊或 gate proration / breach，會讓 R3 更接近；但目前整體 HY/IG 利差極窄，缺口不太可能單獨翻轉答案。

資料一致性備註：case/evidence.md 的搜尋結果表將 structural.treasury_basis_trade 標為「script blocks fetch_failed」，但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 三塊均為 status ok；本報告以 macro artifact 為準（✓ API）。

最大的不確定性：

1. R2 逐家指引：本次來源只給四家合計約 $725bn，未逐家列出指引與方向，也未給下一次財報日期；若秋季財報有兩家下修，會直接推向 yes。
2. R3 借款人規模與到期牆：CoreWeave 等借款人的總負債與再融資時程本次未能確立；若出現再融資失敗，會推向 yes（並可能經由 R1 傳導）。
3. 利率與期限溢價：CPI YoY 3.3% 與期限溢價上升限制 Fed 緩衝空間；若長端利率急升造成估值壓縮，會推向 R1。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7711.76 | FRED API (series_id=SP500) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 8.33 | FRED API (series_id=SP500) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29433.43 | FRED API (series_id=NASDAQ100) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-31T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.0 | FRED API (series_id=NASDAQ100) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q1，%） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-31T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（%） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-30 | 2026-08-31T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（%） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-30 | 2026-08-31T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.63 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.79 | FRED API (series_id=BAMLC0A0CM) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.67 | FRED API (series_id=DGS10) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.34 | FRED API (series_id=DFII10) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.31 | FRED API (series_id=T10YIE) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD） | 83.9 | FRED API (series_id=DCOILWTICO) | 2026-08-25 | 2026-08-31T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料，%） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-31T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.32 | FRED API (series_id=T5YIFR) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（%，Kim-Wright） | 0.8682 | FRED API (series_id=THREEFYTP10) | 2026-08-21 | 2026-08-31T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.64 | FRED API (series_id=SOFR) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.72 | FRED API (series_id=SOFR99) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-31 | 2026-08-31T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（十億美元，SRF 動用 read） | 0.001 | FRED API (series_id=RPONTTLD) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6730912.0（$6.73T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-26 | 2026-08-31T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5913041.0（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-21 | 2026-08-31T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-31T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 14.51 | FRED API (series_id=VIXCLS) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of；base_date 2026-08-20，window 7 日） | 14.51 | FRED API (series_id=SP500 paired) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（%） | -9.37 | FRED API (series_id=SP500 paired) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2026.2859（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-19 | 2026-08-31T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約合計，口數） | -7003041 | CFTC TFF futures-only | 2026-08-25 | 2026-08-31T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 70.97 | Yahoo Finance chart API (^MOVE) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（十億美元） | 2355.4 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave DDTL 5.5 融資（GPU 抵押，十億美元） | 2.6 | https://investors.coreweave.com/news/news-details/2026/CoreWeave-Closes-2-6-Billion-Loan-Facility-Expanding-Financing-Flexibility-for-AI-Infrastructure/default.aspx | 2026-08-10 | 2026-08-31T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | gurufocus / multpl，WebSearch | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | CNBC，WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | 賣方 TP 上修，WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | AI 發行人利差／CDS，WebSearch（14d） | ✗ NOT DISCLOSED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | Yahoo Finance，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | Pensions & Investments，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | StockCharts（50 日均線之上比率 proxy），WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | CNN，WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | FINRA via Advisor Perspectives，WebSearch | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | AAII，WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | Reddit / X，WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | naaim.org / ycharts，WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM survey | 新聞摘要，WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（FRED） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（FRED BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（FRED BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（FRED DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（FRED T10YIE 直接取得） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（FRED DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（FRED CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（FRED T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（FRED THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series | scripts/fetch_macro.py repo_stress（FRED） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | Reuters / Bloomberg 標售摘要，WebSearch（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | CME FedWatch，WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（FRED WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（FRED ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | PBoC / NBS 英文摘要，WebSearch | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | BDC / interval fund 披露，WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | 財報摘要，WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | 公司披露，WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | The Information / Reuters / CNBC，WebSearch | ✗ NOT DISCLOSED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | 法說會／RPO 披露，WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | GPU 租價／HBM／利用率，WebSearch | ✗ NOT DISCLOSED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state 與 30d event_scan，WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | 組件組合，WebSearch | ✗ NOT DISCLOSED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | 10-K / 10-Q，WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | quarterly_state 與 30d event_scan，WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | SPACInsider / Boardroom Alpha / Businesswire，WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | Seeking Alpha，WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | Finviz / Benzinga / StockTitan，WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | S-1 / 具名報導，WebSearch（30d） | ✗ NOT DISCLOSED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | thetrading.tools，WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | 新聞彙整，WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | KRX / TWSE / JPX / ESMA / ETFGI，WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | Cboe insights，WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | OCC 月報 via Mondo Visione，WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | thetrading.tools，WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（FRED VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | currentmarketvaluation，WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | 公司新聞稿，WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 41.59（原定來源 multpl / gurufocus） | shiller cape ratio august 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-08-01 | 2026-08-31T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權前瞻本益比 24（原定來源 Mag 7 P/E） | magnificent 7 forward pe august 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html（CNBC） | 2026-08-03 | 2026-08-31T09:30:00+08:00 |
| breadth.rsp_spy | equal-weight 對 cap-weight YTD：9.67% 對 8.38% | rsp vs spy ytd 2026 | https://finance.yahoo.com/markets/stocks/articles/rsp-vs-spy-does-equal-185007075.html（Yahoo Finance） | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度 37.6% | sp500 top 10 concentration 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/（Pensions & Investments） | 2026-07-31 | 2026-08-31T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 50 日均線之上比率 54%（A/D proxy） | market breadth advance decline august 2026 | https://articles.stockcharts.com/article/mindfulinvestor-2026-08-weakening-market-breadth-could-signal-trouble-ahead/（StockCharts） | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 中性 54 | cnn fear greed index august 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）$1.42T、YoY 38.6% | finra margin debt july 2026 | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026（Advisor Perspectives，原定來源 FINRA） | 2026-07-31 | 2026-08-31T09:30:00+08:00 |
| retail.aaii | AAII 看多 32.9%、看空 44.4% | aaii sentiment august 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-08-26 | 2026-08-31T09:30:00+08:00 |
| monetary.fedwatch | FedWatch 9 月維持利率 58.6% | cme fedwatch september 2026 | https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html（CME Group） | 2026-08-25 | 2026-08-31T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 $725bn（2026 Q2 財報季） | hyperscaler capex 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-08-31T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 掃描，0 件符合窗內 | +AI rename SPAC aug 24-31 2026 | 檢查來源：SPACInsider、Boardroom Alpha、Businesswire | — | 2026-08-31T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 39 件、BRVE 首週漲 67% | ipo market august 2026 | https://seekingalpha.com/article/4933637-august-kicks-off-with-flurry-of-biotech-ipos（Seeking Alpha） | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描，0 件符合 2+ 主題×弱基本面 | microcap moonshot quantum ai aug 24-31 2026 | 檢查來源：Finviz、Benzinga、StockTitan | — | 2026-08-31T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 集中賣出掃描，0 件 | insider form 4 nvidia aug 2026 | 檢查來源：SEC EDGAR（NVDA Form 4） | — | 2026-08-31T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.52（日讀數）、9 日均 0.85 | cboe equity put call ratio august 2026 | https://www.thetrading.tools/put-call-ratio（thetrading.tools，原定來源 Cboe） | 2026-08-19 | 2026-08-31T09:30:00+08:00 |
| structural.leveraged_etf_aum | 槓桿 ETF 總 AUM 約 $198bn；TQQQ 約 $37.3bn、SOXL 約 $22bn | leveraged etf aum record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing，原定來源 etf.com / ETFGI） | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| structural.us_single_stock_etf | 單一個股槓桿 ETF 30 日核准／上市，0 件經查證日期 | single stock leveraged etf launch aug 2026 | 檢查來源：SEC EDGAR、ETF.com | — | 2026-08-31T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔期權量約 60% | 0dte spx share 2026 | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/（Cboe） | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| structural.options_volume | OCC 月報（2026-07 月資料）ETF 期權 YoY 26%、總日均量 71 | occ july 2026 options volume | https://mondovisione.com/media-and-resources/news/occ-july-2026-monthly-volume-data-202686（Mondo Visione，原定來源 OCC） | 2026-07-31 | 2026-08-31T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 期限結構 contango、股債相關轉正、SKEW 143.9 | vix term structure skew august 2026 | https://www.thetrading.tools/vix-term-structure（thetrading.tools） | 2026-08-24 | 2026-08-31T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率 confirmation（2026-07 月資料，$1.42T） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php（Current Market Valuation） | 2026-07-31 | 2026-08-31T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave DDTL 5.5 融資收官 $2.6bn（GPU 抵押） | coreweave debt facility august 2026 | https://investors.coreweave.com/news/news-details/2026/CoreWeave-Closes-2-6-Billion-Loan-Facility-Expanding-Financing-Flexibility-for-AI-Infrastructure/default.aspx（CoreWeave IR） | 2026-08-10 | 2026-08-31T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-31",
  "iso_week": "2026-W36",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-03-01",
  "prior_date": "2026-08-27",
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 4.0,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

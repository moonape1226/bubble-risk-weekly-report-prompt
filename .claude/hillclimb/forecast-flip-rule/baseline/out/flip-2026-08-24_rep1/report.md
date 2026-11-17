> [DRY RUN] this report was not committed to archive.

# 2026-08-24 AI 泡沫破裂預測報告

報告日期：2026-08-24｜ISO 週次：2026-W35｜預測窗口：2026-08-24 → 2027-02-22｜前次基準：report-2026-08-20（4天前）

## 結論

**結論：yes**

依翻轉紀律維持 report-2026-08-20 的 yes：2026-08-20 之後的新資料只有 NASDAQ-100 回撤由 4.03% 微擴至 4.41%（`valuation.ndx_drawdown`）、SRF 動用 0 與 MOVE 73.4（`monetary.repo_stress_srf`、`structural.treasury_basis_trade`）等小幅變動，沒有任何一項改變 R1–R3 的路徑分析，因此不具翻轉條件。需明確揭露：若不受翻轉紀律約束，單看本次證據相對基準率，支持 no 的一方較強（R2 capex 仍在上修、R3 無信用事件、HY OAS 2.75%），下一次運行若出現日期在 2026-08-20 之後、能改變路徑分析的新證據，應重新評估。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29308.86（2026-08-21），252 個交易日最高收盤 30660.6（2026-06-02），距 52 週高點回撤 4.41%（`valuation.ndx_drawdown`）。R1 門檻水位為 22995.45，自最新收盤須再下跌約 21.54% 才觸及。前次（2026-08-20）回撤為 4.03%，本次略擴。S&P 500 收 7674.37（2026-08-21），高於 200 日均線 8.15%、高於 52 週均線 9.61%（`valuation.sp500_trend`），價格延伸仍明顯；估值端 Shiller CAPE 約 41.2、trailing P/E 約 26.2（`valuation.sp500_pe_cape`），Mag 7 加權本益比約 29.5x（`valuation.mag7_multiples`）。波動面 VIX 16.01（2026-08-20），近 7 日 VIX +9.43%、S&P 500 −2.02%，屬正常反向關係、未出現同漲警戒（`structural.vix_spx_comove`）。

**判讀：** R1 距門檻仍遠（須再跌約 21.54%），目前沒有強制去槓桿或信用重定價的觸發跡象；推過門檻需要一個能引發集中平倉的催化劑——例如下一輪 hyperscaler 財報 capex 指引轉弱、Anthropic IPO（目標 10 月）定價失利，或槓桿 ETF／0DTE 部位在急跌中放大賣壓。

### R2 資本支出收縮

本次證據僅取得 top-4 合計：Microsoft、Alphabet、Amazon、Meta 2026 年 capex 指引合計約 $725bn，年增約 +77%（2026-08-13 彙整，對應 2026Q2 財報；`ai.hyperscaler_capex`）。個別公司指引數值未在本次證據中逐家取得，因此逐家方向如下：

- Microsoft：最新為 2026Q2 財報季指引，逐家數值本次未取得；未見下修披露。
- Alphabet：同上，2026Q2 財報季指引；未見下修披露。
- Amazon：同上，2026Q2 財報季指引；未見下修披露。
- Meta：同上，2026Q2 財報季指引；未見下修披露。

目前四家之中下修者為 0 家。下一輪（2026Q3）財報預計落在預測窗口內，但具體日期未在本次證據中取得。需求側：Anthropic 年化營收約 $65B、OpenAI 約 $40B（2026-08-17，`ai.openai_anthropic_revenue`），GPU 現貨租金高於合約價 2 倍以上、產能被利用率吸收（`ai.compute_supply_demand`）。

**判讀：** R2 目前離解析最遠——合計 capex 仍以約 +77% 年增上修，需求端訊號未見 order digestion；要在窗口內觸發，需要兩家在 2026Q3 或 2026Q4 財報中下修指引，通常須先有 R1 型股價重挫或 AI 需求明顯降溫作為前導。

### R3 AI 信用事件

本次 AI 信用定價分歧與 AI 基礎設施債務融資兩項掃描均已完成，但在各自窗口內無合格披露（未見 CoreWeave、Oracle 或其他 neocloud 的利差／CDS 異動、違約、covenant waiver 或 distressed exchange 報導），因此無法直接評估 R3 候選借款人的當期信用定價。整體信用市場仍緊：HY OAS 2.75%、IG OAS 0.82%（2026-08-20，`monetary.hy_oas`、`monetary.ig_oas`），近 4 日無變動。repo 資金壓力（SOFR−IORB）為 −2.0 bps，SOFR99−IORB 6.0 bps（2026-08-20），SRF 動用 0（2026-08-21，`monetary.repo_stress_srf`）。銀行對 NBFI 放款 $2.03T（2026-08-12，`structural.nbfi_bank_loans`）。

**判讀：** R3 沒有任何進行中的困境訊號；整體信用利差處於歷史低檔、融資管道暢通。推過門檻需要某個負債 ≥ 50 億美元的 AI 算力借款人出現再融資失敗或付款違約——在 HY OAS 2.75% 的環境下，窗口內發生的前提是信用環境先急速收緊。

## 支持 yes 的證據

- [R1] NASDAQ-100 回撤較前次（4.03%）加深，最新距 52 週高點回撤 4.41%（2026-08-21），且 S&P 500 高於 200 日均線 8.15%，價格延伸顯著，回落空間大（`valuation.ndx_drawdown`、`valuation.sp500_trend`）。
- [整體] 估值處於極端區：Shiller CAPE 約 41.2、trailing P/E 約 26.2（2026-08-20，`valuation.sp500_pe_cape`），Mag 7 加權本益比約 29.5x（2026-08-14，`valuation.mag7_multiples`）。
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）：OpenAI 約 $40B＋Anthropic 約 $65B ≈ $105bn 年化終端營收 vs 年化 capex 約 $725bn（分母：top-4 MSFT／GOOGL／AMZN／META，未含 Oracle；2026-08-17，`ai.revenue_capex_gap`）。
- [R1] 槓桿與投機部位偏高：美股槓桿 ETF 總 AUM 約 $198bn 創新高（2026-08-17，`structural.leveraged_etf_aum`），SPX 0DTE 佔比約 62.4% 創紀錄（2026-08-14，`structural.zero_dte`），FINRA margin debt YoY 約 +38.6%（2026-07 月資料，`retail.margin_debt`）。
- [整體] Fed 緩衝空間有限：CPI YoY 3.3%（2026-07 月資料，`monetary.cpi_yoy`），FedWatch 9/16 按兵不動約 68.4%、尾端為升息（2026-08-20，`monetary.fedwatch`），10Y 期限溢價（term premium）0.8393%（2026-08-14，`monetary.term_premium`）。
- [R1] Anthropic 目標 10 月 IPO、估值約 $2T（2026-08-17，`speculation.upcoming_ai_ipos`），窗口內的大型供給事件可能成為情緒轉折點。

## 支持 no 的證據

- [R2] Top-4 hyperscaler 2026 capex 指引合計約 $725bn、年增約 +77%（2026-08-13，`ai.hyperscaler_capex`），四家之中 0 家下修，距 R2 的「兩家下修」最遠。
- [R3] 信用市場緊：HY OAS 2.75%、IG OAS 0.82%（2026-08-20，`monetary.hy_oas`、`monetary.ig_oas`），repo 資金壓力（SOFR−IORB）−2.0 bps、SRF 動用 0（`monetary.repo_stress_srf`），無資金壓力跡象。
- [R1] R1 須自 29308.86 再跌約 21.54% 至 22995.45 才觸發（`valuation.ndx_drawdown`）；基準率上 182 天內 25% 回撤屬少見事件。
- [R2] AI 需求端仍強：Anthropic 年化營收約 $65B、OpenAI 約 $40B（2026-08-17，`ai.openai_anthropic_revenue`），Anthropic run-rate 年增約 7 倍（`ai.token_growth`），GPU 現貨租金高於合約價 2 倍以上（2026-08-13，`ai.compute_supply_demand`）。
- [R1] 廣度擴散而非收窄：RSP 領先 SPY YTD 約 5pp（2026-08-17，`breadth.rsp_spy`），領導由 top-100 向 bottom-400 擴散（`breadth.advance_decline`）。
- [整體] 情緒未達極端：CNN Fear & Greed 55（Greed，2026-08-21，`retail.fear_greed`），AAII 偏空 39.9% 高於偏多 35.5%（2026-08-19，`retail.aaii`），MOVE 73.4（2026-08-21，`structural.treasury_basis_trade`）。

## 與前期比較

前次結論：yes（report-2026-08-20）

本次結論：維持

- NASDAQ-100 回撤由 4.03% 擴至 4.41%（2026-08-21，`valuation.ndx_drawdown`）：方向偏 yes 但幅度僅 0.38 個百分點，距 R1 門檻仍約 21.54%，未改變 R1 分析。
- S&P 500 由 7641.16 升至 7674.37（+0.43%，`valuation.sp500_trend`），10Y 分解三腿 Δ 皆為 0（無變動；DGS10、DFII10 無新觀測），屬雜訊級變動。
- repo 資金壓力與 SRF 動用維持 0（2026-08-21，`monetary.repo_stress_srf`）、MOVE 由 73.18 升至 73.4（`structural.treasury_basis_trade`），未出現 R3 傳導。
- CNN Fear & Greed 55（2026-08-21，`retail.fear_greed`）與 YTD IPO 約 232 件（2026-08-21，`speculation.ipo_heat`）為新觀測，但不涉 R1–R3 任一路徑的觸發機制。
- 其餘支持 no 的主要證據（capex +77%、HY OAS 2.75%）的資料日期均在 2026-08-20 當日或之前，不構成翻轉所需的新證據；因此依翻轉紀律維持 yes。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源掃描完成但無合格披露（✗ NOT DISCLOSED）：`valuation.analyst_tp_decomposition`、`valuation.ai_credit_schism`、`retail.social_sentiment`、`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.pboc`、`monetary.private_credit_liquidity`、`ai.customer_concentration_rpo`、`ai.hyperscaler_financing_mix`（event_scan 無 30 日內事件）、`ai.depreciation_life`、`ai.capital_cycle`（event_scan 無 30 日內事件）、`structural.global_leveraged_approvals`、`structural.ai_infrastructure_debt`。其中 `valuation.ai_credit_schism` 與 `structural.ai_infrastructure_debt` 的缺漏最可能影響答案：R3 候選借款人的個別信用定價本次不可見，若存在未被報導的利差急擴，R3 的距離可能被低估。

最大的不確定性：

- 2026Q3 hyperscaler 財報（日期未在本次證據中取得）：任兩家下修 capex 指引即直接解析 R2 為 yes；若再度上修則強化 no。
- Anthropic 10 月 IPO：定價或首日表現失利可能成為 R1 的情緒觸發；順利完成則延長 AI 估值擴張。
- Fed 路徑：CPI 3.3% 與 FedWatch 升息尾端限制了 Fed 對 AI 主導回撤的緩衝，若通膨再升溫、Fed 轉鷹，R1 的觸發門檻實際上降低。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7674.37 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 8.15 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 9.61 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29308.86 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.41 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1 家庭股票配置 %） | 45.76080873390133（約 45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.75 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.82 | FRED API (series_id=BAMLC0A0CM) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.69 | FRED API (series_id=DGS10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.35 | FRED API (series_id=DFII10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.34 | FRED API (series_id=T10YIE) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 86.48 | FRED API (series_id=DCOILWTICO) | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.34 | FRED API (series_id=T5YIFR) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8393 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.63 | FRED API (series_id=SOFR) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.71 | FRED API (series_id=SOFR99) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-08-24 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6745699.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5927307.0（€5.93T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.01 | FRED API (series_id=VIXCLS) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 16.01 | FRED API (series_id=VIXCLS, SP500) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2026.1422（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-12 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7218048 | CFTC TFF futures-only | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.4 | Yahoo Finance chart API (^MOVE) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2328.6 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值 / S&P 500 P/E and Shiller CAPE | multpl / GuruFocus [SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值 / Mag 7 weighted P/E | 市場資料 [SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值 / Analyst TP upgrade decomposition | 賣方摘要 [SEARCH]，90d＋同季 | ✗ NOT DISCLOSED |
| valuation.sp500_trend | 估值 / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值 / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值 / AI 信用定價分歧 | 信用市場 [SEARCH]，14d | ✗ NOT DISCLOSED |
| breadth.rsp_spy | 廣度 / S&P 500 equal-weight | 市場資料 [SEARCH] | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度 / Top-10 concentration | 市場資料 [SEARCH] | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度 / Advance/decline ratio | 市場資料 [SEARCH] | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶 / CNN Fear & Greed Index | CNN [SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶 / Margin Debt: FINRA | FINRA / GuruFocus [SEARCH]，月頻 stock-of-state | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶 / Retail survey: AAII | AAII [SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶 / Social sentiment proxies | WSB / X [SEARCH]，7d | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶 / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶 / NAAIM Exposure Index | naaim.org [SEARCH] | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | 機構 / BofA Fund Manager Survey | BofA / JPM [SEARCH] | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣 / Fed funds rate: FRED | scripts/fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣 / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣 / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣 / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣 / 10Y Treasury real yield | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣 / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣 / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣 / CPI YoY: FRED | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣 / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣 / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | 貨幣 / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣 / 美債標售需求 | Reuters / TreasuryDirect [SEARCH]，14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣 / Fed funds rate path expectations | CME FedWatch [SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣 / Fed balance sheet: FRED | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣 / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣 / PBoC aggregate financing | PBoC / NBS [SEARCH] | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | 貨幣 / Private-credit / non-bank fund liquidity stress | BDC 披露 [SEARCH]，30d | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | 財報摘要 [SEARCH]，stock-of-state | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI / AI token volume growth rate | 供應商披露 [SEARCH] | ✓ SEARCH-VERIFIED |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | Bloomberg / CNBC [SEARCH] | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration | 財報電話 [SEARCH] | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | 產業披露 [SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構 | 財報／發債 [SEARCH]；quarterly_state 沿用 top-5 季頻；event_scan 30d 無合格事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口 | 綜合披露 [SEARCH]，stock-of-state | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動 | 10-K / 10-Q [SEARCH]，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI / 資本週期階段 | 產業披露 [SEARCH]；quarterly_state 沿用；event_scan 30d 無合格事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機 / Search for past 7 days | 新聞 [SEARCH]，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機 / IPO market heat | stockanalysis / Renaissance [SEARCH] | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機 / Microcap thematic moonshots | Finviz / Benzinga [SEARCH]，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機 / Upcoming AI IPOs | Bloomberg / CNBC [SEARCH]，30d | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機 / Insider selling at AI | SEC EDGAR [SEARCH]，14d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機 / Cboe equity-only put/call ratio | Cboe [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構 / US leveraged ETF AUM | ETF.com [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構 / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com [SEARCH]，30d | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | 結構 / Global leveraged product approvals | KRX / TWSE / JPX / ESMA [SEARCH]，7d | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構 / 0DTE option volume | Cboe [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構 / Options total volume | OCC [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構 / Cross-asset derivatives / correlation checks | Cboe / SpotGamma [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構 / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構 / Cross-reference only: FINRA margin debt | FINRA / GuruFocus [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構 / AI infrastructure debt financing / vendor-financing loops | 信用市場 [SEARCH]，30d | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | 結構 / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構 / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）＋[SEARCH] | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | trailing P/E 約 26.2、Shiller CAPE 約 41.2 | Shiller CAPE S&P 500 P/E August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權本益比約 29.5x（S&P 500 約 25.6x） | Magnificent 7 weighted P/E August 2026 | https://www.fool.com/investing/2026/08/14/the-best-magnificent-seven-stocks-to-buy-in-august/（Motley Fool） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| breadth.rsp_spy | RSP 領先 SPY YTD 約 5pp | RSP vs SPY YTD 2026 breadth | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 top-10 集中度約 36.5% | S&P 500 top 10 concentration 2026 | https://www.ebc.com/forex/rsp-vs-spy（EBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.advance_decline | 領導由 top-100 向 bottom-400 擴散、廣度確認多頭 | market breadth advance decline August 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 55（Greed） | CNN Fear and Greed today August 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）約 1,417,225、YoY 約 +38.6%、MoM −5.7% | FINRA margin debt July 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt（GuruFocus／FINRA） | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| retail.aaii | AAII 偏多 35.5%、偏空 39.9%（週結 2026-08-19） | AAII investor sentiment August 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 標售無明顯 tail、12.10% allotted at high | US Treasury 30-year auction August 2026 | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2026/R_20260813_3.pdf（TreasuryDirect） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| monetary.fedwatch | FedWatch 9/16 按兵不動約 68.4%、尾端為升息 | CME FedWatch September 2026 hold probability | https://en.macromicro.me/series/1645/probability-fed-rate-decrease（MacroMicro） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_capex | top-4 2026 capex 合計約 $725bn（+77% YoY，2026Q2 財報季） | hyperscaler 2026 capex guidance Microsoft Google Amazon Meta | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.token_growth | Anthropic run-rate 年增約 7 倍、API 佔營收多數 | Anthropic token growth revenue 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html（CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.openai_anthropic_revenue | OpenAI 約 $40B、Anthropic 約 $65B run-rate | OpenAI Anthropic annualized revenue August 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html（CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.compute_supply_demand | GPU 現貨租金高於合約價 2 倍以上、產能被利用率吸收 | AI GPU rental pricing utilization August 2026 | https://www.uncoveralpha.com/p/amazon-google-microsoft-meta-q2-earnings（UncoverAlpha） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex > FCF、2026 hyperscaler 發債擴張（capex 由現金流轉向舉債） | hyperscaler external financing capex FCF debt 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow（FactSet） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.capital_cycle | [quarterly_state] 供給側 capex 年增約 77%、需求側 token／營收成長並存 | AI capex growth rate supply demand 2026 | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.revenue_capex_gap | 終端營收 OpenAI 40＋Anthropic 65 ≈ $105bn vs 年化 capex 約 $725bn（分母：top-4） | AI revenue to capex gap 2026 | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描：0 件合格事件 | AI rename SPAC ticker change August 2026 | Renaissance Capital／SEC EDGAR／新聞掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD IPO 約 232 件（截至 2026-08-21），無單週無營收 AI IPO 暴衝 | US IPO count August 2026 | https://stockanalysis.com/ipos/2026/（StockAnalysis） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描：0 檔合格 | microcap 100% single day surge quantum AI August 2026 | Finviz／Benzinga／StockTwits movers 掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 10 月 IPO、估值約 $2T | Anthropic OpenAI IPO 2026 | https://finance.yahoo.com/markets/article/spacex-openai-and-anthropic-here-are-the-most-anticipated-ipos-in-2026-114439441.html（Yahoo Finance） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 14 日內合格 Form 4 集中賣出：0 起 | insider Form 4 AI executives August 2026 | SEC EDGAR／openinsider 掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.52（日讀數；9 日均總量 0.85） | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio（The Trading Tools） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美股槓桿 ETF 總 AUM 約 $198bn 創新高；TQQQ 31.3、SOXL 17.3（$bn） | leveraged ETF AUM record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| structural.us_single_stock_etf | 美單一個股槓桿 ETF 30 日新核准／上市：0 件 | single-stock leveraged ETF launch SEC August 2026 | SEC EDGAR／ETF.com new launches 掃描 | — | 2026-08-24T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 8 月佔比約 62.4% 創紀錄 | 0DTE SPX volume share August 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| structural.options_volume | OCC YTD 日均逾 71M 口（2026-07 月資料） | OCC options volume 2026 | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/historical-volume-statistics（OCC） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 16.01、期限結構 contango（IVTS 約 0.82）、SKEW 偏高 | VIX term structure SKEW August 2026 | https://www.thetrading.tools/vix-term-structure（The Trading Tools） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt／市值交叉檢核（2026-07 月資料，YoY +38.6%） | FINRA margin debt equity market cap ratio 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt（GuruFocus／FINRA） | 2026-07-01 | 2026-08-24T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-24",
  "iso_week": "2026-W35",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "yes",
  "horizon_end": "2027-02-22",
  "prior_date": "2026-08-20",
  "prior_answer": "yes",
  "flip_evidence": [],
  "r1_drawdown_pct": 4.41,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

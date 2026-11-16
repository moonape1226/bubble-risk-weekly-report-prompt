> [DRY RUN] this report was not committed to archive.

# 2026-08-13 AI 泡沫破裂預測報告

報告日期：2026-08-13｜ISO 週次：2026-W33｜預測窗口：2026-08-13 → 2027-02-11｜前次基準：report-2026-08-10（3天前）

## 結論

**結論：no**

三條路徑目前都離觸發很遠：NASDAQ-100 距 52 週高點回撤只有 2.99%，還要再跌約 22.69% 才達 R1 門檻；hyperscaler 2026 capex 合計 ≈$725B 且仍在上修，R2 需要的兩家下修看不到跡象。AI 信用端確實開始重定價（CoreWeave 貸款利差 +100–125bp、Oracle CDS ≈75bp），但距離 R3 要求的破產／違約／distressed exchange 仍隔著好幾個階段，因此不足以推翻低基率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,742.6（2026-08-12），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 2.99%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，自最新收盤還需再跌約 22.69% 才會觸發。脆弱度偏高：S&P 500 7,748.5（2026-08-12）高於 200 日均線 9.67%、高於 52 週均線 11.23%（`valuation.sp500_trend`）；S&P 500 trailing P/E 29.85、Shiller CAPE 42.34（`valuation.sp500_pe_cape`，2026-08-12）；FINRA margin debt（2026-06 月資料）$1.502T、YoY +51.5%，落在歷史頂部附近常見的 +40–50% 區間之上（`retail.margin_debt`）。但當下的催化劑讀數平靜：VIX 15.28（2026-08-11），過去 7 天 VIX −7.39%、S&P 500 −0.11%，沒有同步上漲的警戒讀數（`structural.vix_spx_comove`）；HY OAS 2.72%、IG OAS 0.79%（2026-08-11，`monetary.hy_oas`、`monetary.ig_oas`）。貨幣面緩衝有限：CPI YoY 3.3%（2026-07 月資料，`monetary.cpi_yoy`），CME FedWatch 顯示 9/16 會議升息定價 ≈45%、沒有降息定價（`monetary.fedwatch`，2026-08-12），一旦 AI 主導的下跌出現，Fed 很難像過去那樣迅速降息。

**判讀：** 距離門檻很遠。在 182 天內再跌約 22.69%，需要一個真正的催化劑，例如 AI 信用重定價擴散到 hyperscaler、Fed 在通膨 3.3% 下升息，或 OpenAI IPO 定價失利帶動 AI 權益重估。估值與槓桿代表一旦開始下跌，跌幅可能很大，但目前沒有證據顯示下跌已經開始。

### R2 資本支出收縮

最新正式指引來自 2026 Q2 財報季（2026-07 下旬）。彙總來源顯示 Microsoft、Alphabet、Amazon、Meta 2026 capex 合計 ≈$725B，且相較前一次指引仍在上修（`ai.hyperscaler_capex`，CNBC 2026-07-28）。逐家看：Microsoft、Alphabet、Amazon、Meta 的個別指引數值本次證據沒有逐家取得，彙總來源方向為上修，四家都沒有看到下修報導，目前下修家數為 0／4。下一輪正式指引（Q3 財報）預計在 2026-10 下旬、Q4 財報在 2027-01 下旬至 02 初，都落在窗口內；確切日期本次證據沒有取得。融資面壓力正在累積：top-5 hyperscaler capex 已超過 FCF（Alphabet Q2 FCF 轉負），2026 發債 ≈$182B（`ai.hyperscaler_financing_mix`，2026-07-24）。需求面仍然緊：HBM 合約價 ≈+40%、H200 租金中位 ≈$3.99/hr、Blackwell 售罄（`ai.compute_supply_demand`，2026-08-01）。

**判讀：** 遠未觸發。在算力供不應求、指引剛上修的情況下，要在窗口內兩次財報季累積兩家下修，大概需要 R1 級的權益下跌或融資通道收緊迫使管理層轉向，可以視為 R1／R3 的下游結果，而不是獨立的起點。

### R3 AI 信用事件

在可能達到 R3 規模門檻（負債 ≥ 50 億美元、以 AI 資料中心／算力為主業）的借款人中，CoreWeave 最值得關注。它剛完成 $2.6B 貸款，但被迫把利差調高 +100–125bp 並接受 covenant（`structural.ai_infrastructure_debt`，2026-07-29）。信用市場同時出現 AI 信用定價分歧（equity-vs-credit schism）往後期移動的訊號：CoreWeave 貸款利差走闊，Oracle 5Y CDS ≈75bp（7 年高），Fitch／Moody's 發出預警（`valuation.ai_credit_schism`，2026-08-03）。本次證據沒有看到任何付款違約、covenant waiver、distressed exchange 或 going-concern 措辭。hyperscaler 表外結構也在擴大，Meta El Paso 資料中心由 BlackRock 主導 >$12B 債券（20-30yr triple-net lease），屬於 hyperscaler 融資結構（capex vs FCF／發債）中的 SPV 型融資（`ai.hyperscaler_financing_mix`，2026-07-20）。近期到期與再融資牆的具體數字本次證據沒有披露。

**判讀：** 方向是往壞的一邊走（信用開始重定價、貸方要求 covenant），但 R3 需要破產、超過寬限期的違約或完成 distressed exchange。從「利差走闊、融資仍能完成」走到那一步，通常需要融資通道實際關閉或主要客戶承諾落空，在 182 天內完成的可能性仍低於一半。

## 支持 yes 的證據

- [R3] AI 信用開始重定價：CoreWeave 貸款利差被迫 +100–125bp 並加上 covenant，Oracle 5Y CDS ≈75bp 創 7 年高，Fitch／Moody's 預警（2026-08-03，`valuation.ai_credit_schism`；CoreWeave $2.6B facility 2026-07-29，`structural.ai_infrastructure_debt`）。
- [整體] hyperscaler 融資結構（capex vs FCF／發債）轉向舉債：top-5 capex 已超過 FCF、Alphabet Q2 FCF 轉負、2026 發債 ≈$182B（2026-07-24），另有 Meta 表外 SPV >$12B（2026-07-20）（`ai.hyperscaler_financing_mix`）。
- [R1] 估值與槓桿處於極端區：S&P 500 trailing P/E 29.85、CAPE 42.34（2026-08-12，`valuation.sp500_pe_cape`）；S&P 500 高於 200 日均線 9.67%（2026-08-12，`valuation.sp500_trend`）；margin debt（2026-06 月資料）YoY +51.5%（`retail.margin_debt`）。
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）巨大：年化 AI 終端營收 ≈$72B 對年化 capex ≈$725B（分母：top-4＋Oracle；沿用最近組合值，資料日 2026-06-15，`ai.revenue_capex_gap`）；Microsoft 商用 RPO $678B 中 ≈32% 繫於 OpenAI（2026-07-30，`ai.customer_concentration_rpo`）。
- [R1] 貨幣緩衝受限：CPI YoY 3.3%（2026-07 月資料，`monetary.cpi_yoy`），FedWatch 9/16 升息定價 ≈45%、沒有降息定價（2026-08-12，`monetary.fedwatch`）。
- [R1] 結構性槓桿高：US 槓桿 ETF 總 AUM 創新高 ≈$198B（2026-07-23，`structural.leveraged_etf_aum`）；0DTE 佔 SPX 期權量 ≈65%（Cboe Q2，2026-07-31，`structural.zero_dte`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 2.99%（最新收盤 29,742.6，2026-08-12），距門檻 22,995.45 還差約 22.69%，起點離觸發非常遠（`valuation.ndx_drawdown`）。
- [R2] hyperscaler 2026 capex 合計 ≈$725B 且仍上修，四家都沒有下修（2026-07-28，`ai.hyperscaler_capex`）；算力供不應求：HBM 合約 ≈+40%、Blackwell 售罄（2026-08-01，`ai.compute_supply_demand`）。
- [整體] 廣義信用與資金市場平靜：HY OAS 2.72%、IG OAS 0.79%（2026-08-11，`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）−1bp、SOFR99−IORB +8bp（2026-08-11）、SRF 動用 0（2026-08-12）（`monetary.repo_stress_srf`）；MOVE 72.09（2026-08-12，`structural.treasury_basis_trade`）。
- [R3] AI 基建借款人仍然借得到錢：CoreWeave 雖然付出更高利差，仍完成 $2.6B 融資（2026-07-29，`structural.ai_infrastructure_debt`），本次沒有看到任何違約或 distressed exchange。
- [整體] 情緒沒有到亢奮：CNN Fear & Greed ≈61（2026-08-12，`retail.fear_greed`）；AAII Bull 37.0%／Bear 38.0%（2026-08-06，`retail.aaii`）；≈71.6% 成分股在 50DMA 之上，廣度健康（2026-08-11，`breadth.advance_decline`）。
- [整體] 美債標售需求（auction tail／bid-to-cover）穩健：3Y BTC 2.71、10Y BTC 2.58，需求略高於均值（2026-08-12，`monetary.treasury_auctions`）。

## 與前期比較

前次結論：無前次預測（report-2026-08-10 為舊格式評分報告）

本次是新格式的第一次預測，flip_evidence 為空。自 2026-08-10 以來的主要變化：

- NASDAQ-100 收盤由 29,621.8（2026-08-10）升到 29,742.6（2026-08-12），R1 距離略為拉大。
- DGS10 −2bp 到 4.70%、DFII10 持平 2.43%、T10YIE −3bp 到 2.26%。三者窗口不一致，driver 判讀為 不可判（視窗不一致）。
- HY OAS +2bp 到 2.72%、IG OAS +1bp 到 0.79%，信用利差只是微幅走闊。
- MOVE 由 75.46 降到 72.09，OFR tri-party repo transaction volume 由 $2,331.9bn 增到 $2,385.3bn（+2.29%）。
- 5y5y forward inflation −5bp 到 2.28%；10Y 期限溢價（term premium）0.8257%（2026-08-07，序列自身 trailing ≈7d −4.2bp）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED 的來源（搜尋完成但沒有當期合格披露）：valuation.analyst_tp_decomposition（唯一找到的是 Susquehanna TSMC 目標 $575→$600，2026-07-16，不屬於指定的 top-tier 賣方，也沒有披露 EPS Δ／target PE Δ，無法拆解）、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.pboc、monetary.private_credit_liquidity、ai.token_growth、ai.openai_anthropic_revenue（最近一次披露是 2026-05-29，屬上一季，不是當季披露；搜尋摘要寫 Anthropic ≈$47B，但該 URL 標題是 $30B run-rate，兩者不一致，因此不當作新證據）、ai.depreciation_life、ai.capital_cycle（兩個組件都沒有可用披露，本次不判定資本週期階段（capital cycle stage））、structural.global_leveraged_approvals。其中私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）的缺漏影響最大，因為它是 R3 的傳導通道；但缺漏只代表沒有新披露，不是壓力訊號，不會改變答案。

零件數篩選：speculation.ai_rename_spac、speculation.microcap_moonshots、speculation.insider_form4、structural.us_single_stock_etf 都完成搜尋，在各自窗口內找到 0 件合格事件（過去 7 天沒有 +AI 更名／SPAC、沒有合格 microcap moonshot，過去 14 天沒有合格 Form 4 叢集，過去 30 天沒有新的 US 單一股票槓桿 ETF 核准／上市）。這些結果只表示沒有命中，不作為正面證據引用。harness 沒有保留這四個篩選的原始查詢字串，traceability 的 search query 欄只依篩選定義描述範圍，這是可追溯性的弱點。

資料時效：breadth.rsp_spy 的 RSP 對 SPY YTD 數字（+9.67% 對 +8.38%）資料日是 2026-06-10，距報告日約兩個月，只當背景，不當作當期證據。ai.revenue_capex_gap 的分子沿用 2026-05-29 的 run-rate，不是新披露。

最大的不確定性：

1. OpenAI IPO（目標 9 月、估值 ≈$730–850B，`speculation.upcoming_ai_ipos`，2026-07-28）：如果定價失利或延後，可能成為 AI 權益重估的觸發點，會把答案推向 yes；如果順利定價，則強化 no。
2. Q3 財報季（2026-10 下旬）的 capex 指引與 FCF：如果出現第一家下修，或 Alphabet 之外更多家 FCF 轉負、發債加速，R2／R3 的機率會上升，推向 yes。
3. 9/16 FOMC：在 CPI 3.3% 下如果升息，會壓縮估值並收緊 AI 基建融資，推向 yes；如果暫停，則維持 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7748.5 | FRED API (series_id=SP500) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線偏離 %） | 9.67 | FRED API (series_id=SP500) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29742.6 | FRED API (series_id=NASDAQ100) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 2.99 | FRED API (series_id=NASDAQ100) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q1 家庭股票配置 %） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.72 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.79 | FRED API (series_id=BAMLC0A0CM) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.7 | FRED API (series_id=DGS10) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.43 | FRED API (series_id=DFII10) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.26 | FRED API (series_id=T10YIE) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl） | 84.77 | FRED API (series_id=DCOILWTICO) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料，%） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.28 | FRED API (series_id=T5YIFR) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 0.8257 | FRED API (series_id=THREEFYTP10) | 2026-08-07 | 2026-08-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.64 | FRED API (series_id=SOFR) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.73 | FRED API (series_id=SOFR99) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-13 | 2026-08-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6748567.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-05 | 2026-08-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5923023.0（€5.92T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-07 | 2026-08-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.28 | FRED API (series_id=VIXCLS) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（7 日窗，base 2026-08-04） | 15.28 | FRED API (series_id=VIXCLS / SP500) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2002.4852（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-29 | 2026-08-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7423067 | CFTC TFF futures-only | 2026-08-04 | 2026-08-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 72.09 | Yahoo Finance chart API (^MOVE) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2385.3 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | Fool／SSGA WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 WebSearch（90d＋同季） | ✗ NOT DISCLOSED（無 top-tier 同季可拆解升級） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 24/7 Wall St WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-06-10，僅背景） |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | RBC Wealth Management WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | Investing.com breadth WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA／Advisor Perspectives WebSearch | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／YCharts [primary: SEARCH] | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok／DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直接） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（repo_stress block） | ✓ API（SOFR ok／SOFR99 ok／IORB ok／RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | Reuters／RTTNews recap [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok／JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | investing／Yicai WebSearch | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | 報導 WebSearch | ✗ NOT DISCLOSED（最近披露 2026-05-29 屬上一季） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce／jarvislabs [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報／發債 [primary: SEARCH]；quarterly_state＋30d event_scan | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 [primary: SEARCH]（沿用最近組合值） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K／10-Q [primary: SEARCH]（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速＋進出場事件 [primary: SEARCH]；quarterly_state＋30d event_scan | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | WebSearch 7d 篩選 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | IPOScoop／Renaissance WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／StockAnalysis [primary: SEARCH] | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | S-1／具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 篩選（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe／thetrading.tools [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com／ETFGI [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com launches 篩選（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC monthly volume report | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove block） | ✓ API（VIXCLS ok／vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 Retail Sentiment margin debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）＋WebSearch 事件掃描 | ✓ API（cftc_lev_funds ok／move_index ok／ofr_repo ok；WebSearch 事件掃描無當期披露） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.85、Shiller CAPE 42.34（原定來源 multpl.com） | S&P 500 trailing P/E CAPE August 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl）；https://www.multpl.com/shiller-pe | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E ≈29x vs 指數 ≈25.6x、佔市值 ≈33.9% | Magnificent 7 weighted PE vs S&P 500 August 2026 | https://www.fool.com/research/magnificent-seven-sp-500/ （Motley Fool） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 貸款利差 +100–125bp、Oracle 5Y CDS ≈75bp（7 年高）、Fitch／Moody's 預警 | CoreWeave Oracle CDS spread AI credit widening August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm （Tech Times） | 2026-08-03 | 2026-08-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 等權 YTD +9.67% vs SPY +8.38%（資料日偏舊，僅背景） | RSP vs SPY equal weight YTD total return August 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St） | 2026-06-10 | 2026-08-13T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 ≈37% | S&P 500 top 10 concentration percent 2026 | https://www.rbcwealthmanagement.com/en-us/insights/the-great-narrowing-sp-500-concentration （RBC Wealth Management） | 2026-07-24 | 2026-08-13T09:30:00+08:00 |
| breadth.advance_decline | ≈71.6% S&P 500 成分股在 50DMA 之上 | S&P 500 percent above 50 day moving average August 2026 | https://www.investing.com/indices/s-p-500-stocks-above-50-day-average （Investing.com） | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed ≈61（Greed） | CNN Fear and Greed Index August 12 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-06 月資料）$1.502T、YoY +51.5%（原定來源 FINRA） | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-08-13T09:30:00+08:00 |
| retail.aaii | AAII Bull 37.0%／Neutral 25.0%／Bear 38.0%（週結束 2026-08-05） | AAII investor sentiment survey week August 5 2026 | https://seekingalpha.com/article/4932187-aaii-sentiment-survey-optimism-jumps （Seeking Alpha） | 2026-08-06 | 2026-08-13T09:30:00+08:00 |
| monetary.treasury_auctions | 3Y（2026-08-11）BTC 2.71、tail −0.5bp；10Y（2026-08-12）BTC 2.58、需求略高於均值 | US Treasury 3 year 10 year auction bid to cover August 2026 | https://www.rttnews.com/3679611/ten-year-note-auction-attracts-modestly-above-average-demand.aspx （RTTNews） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 9/16 升息定價 ≈45%、無降息定價 | CME FedWatch September 2026 rate hike probability | https://cryptobriefing.com/traders-45-percent-chance-september-fed-rate-hike/ （Crypto Briefing，引 CME FedWatch） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler（MSFT／GOOGL／AMZN／META）2026 capex 合計 ≈$725B、仍上修（Q2 2026 財報季） | hyperscaler capex 2026 725 billion raised Q2 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-08-13T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft 商用 RPO $678B、≈32% 繫單一客戶（OpenAI） | Microsoft RPO backlog 678 billion OpenAI 2026 | https://www.benzinga.com/trading-ideas/long-ideas/26/07/60816147/microsofts-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer （Benzinga） | 2026-07-30 | 2026-08-13T09:30:00+08:00 |
| ai.compute_supply_demand | H200 租金中位 ≈$3.99/hr、HBM 合約 ≈+40%、Blackwell 售罄 | H200 GPU rental HBM DRAM 2026 shortage Blackwell | https://jarvislabs.ai/blog/h200-price （Jarvislabs） | 2026-08-01 | 2026-08-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 超越 FCF（Alphabet Q2 FCF 轉負）、2026 發債 ≈$182B | hyperscaler capex FCF debt issuance 182 billion 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure （Sage Advisory） | 2026-07-24 | 2026-08-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan][spv_deal] Meta El Paso 資料中心 BlackRock 主導 >$12B 債券（20-30yr triple-net lease、表外結構） sponsor_equity_split=undisclosed;residual_value_guarantee=undisclosed;lease_term=20-30yr;debt_tenor=undisclosed;lead_lenders=BlackRock/JPMorgan/MS; | direct fetch（無搜尋查詢；hyperscaler 30d event_scan 直接取頁） | https://www.landgate.com/news/blackrock-s-12-billion-bond-sale-signals-a-new-financing-playbook-for-data-center-developers （Landgate） | 2026-07-20 | 2026-08-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 ≈$72B vs 年化 capex ≈$725B（分母：top-4＋Oracle；沿用最近組合值） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-06-15 | 2026-08-13T09:30:00+08:00 |
| speculation.ai_rename_spac | 過去 7 天 +AI 更名／ticker change／SPAC／無營收投機 IPO：0 件合格事件 | 依篩選定義：past-7-day AI rename / +AI ticker change / SPAC announcement（harness 未保存原始查詢字串） | WebSearch 新聞篩選 | — | 2026-08-13T09:30:00+08:00 |
| speculation.ipo_heat | 2026-08-12／08-13 各 ≈12 檔定價、平均首日 ≈18% | US IPO pricings week August 2026 IPOScoop | https://www.iposcoop.com/current-year-pricings/ （IPOScoop） | 2026-08-13 | 2026-08-13T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週 <$1B 單日 ≥100% 且多主題疊加弱基本面：0 件合格標的 | 依篩選定義：biggest single-day gainers under $1B market cap, multi-theme press release（harness 未保存原始查詢字串） | Finviz／StockAnalysis movers 篩選 | — | 2026-08-13T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 9 月上市、估值 ≈$730–850B，Anthropic 持續推進 | OpenAI Anthropic IPO timing valuation 2026 | https://cryptobriefing.com/openai-ipo-filing-trillion-valuation/ （Crypto Briefing） | 2026-07-28 | 2026-08-13T09:30:00+08:00 |
| speculation.insider_form4 | 過去 14 天 AI／市場領導股 Form 4 合格叢集：0 件 | 依篩選定義：SEC EDGAR Form 4 filings AI leaders past 14 days（harness 未保存原始查詢字串） | SEC EDGAR Form 4 篩選 | — | 2026-08-13T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity-only put/call 0.54 | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio （thetrading.tools，引 Cboe） | 2026-08-07 | 2026-08-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創新高 ≈$198B（原定來源 etf.com／ETFGI） | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing） | 2026-07-23 | 2026-08-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 過去 30 天 US 單一股票槓桿 ETF 核准／上市：0 件 | 依篩選定義：SEC EDGAR ETF filings / ETF.com launches single-stock leveraged past 30 days（harness 未保存原始查詢字串） | Leverage Shares／Tradr／SEC EDGAR／ETF.com 篩選 | — | 2026-08-13T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量 ≈65%（Cboe Q2 2026） | 0DTE SPX options share Cboe Q2 2026 65% | https://ca.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4768656 （Investing.com） | 2026-07-31 | 2026-08-13T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月總量 1,603,491,559 口（≈16.0 億口） | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-08-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 135.59、VIX 15.28、MOVE 74.67 | VIX SKEW MOVE bond volatility August 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-10-2026-spx-skew-collapses-on-upside-chasing （Cboe） | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-06 月資料）$1.502T、YoY +51.5%（交叉引用，不重複計入） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-08-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B 貸款被迫調高利差 +100–125bp 並附 covenant | CoreWeave 2.6 billion loan spread covenant August 2026 | https://www.stocktitan.net/news/CRWV/core-weave-closes-2-6-billion-loan-facility-expanding-financing-gwhngwnf0jt5.html （StockTitan） | 2026-07-29 | 2026-08-13T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-13",
  "iso_week": "2026-W33",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-11",
  "prior_date": "2026-08-10",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 2.99,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

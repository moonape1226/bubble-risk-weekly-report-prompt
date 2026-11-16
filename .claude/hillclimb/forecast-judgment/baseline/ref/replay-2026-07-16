> [DRY RUN] this report was not committed to archive.

# 2026-07-16 AI 泡沫破裂預測報告

報告日期：2026-07-16｜ISO 週次：2026-W29｜預測窗口：2026-07-16 → 2027-01-14｜前次基準：report-2026-07-13（3天前）

## 結論

**結論：no**

三條路徑目前都離觸發很遠：NASDAQ-100 距 52 週高點回撤 3.78%，還要從最新收盤再跌約 22.06% 才到 R1 門檻（`valuation.ndx_drawdown`）。hyperscaler 2026 capex 合計約 $700B，最近一次指引仍是上修（`ai.hyperscaler_capex`），HY OAS 2.72% 也顯示信用市場沒有系統性重定價（`monetary.hy_oas`）。Oracle CDS 走闊和 Blue Owl 的 gate proration / breach 是值得追蹤的早期裂縫，但還不足以推翻 182 天窗口內「不破裂」的 base rate。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29502.6（2026-07-15），252 個交易日最高收盤 30660.6（2026-06-02），距 52 週高點回撤 3.78%（`valuation.ndx_drawdown`）。R1 門檻水位 22995.45，換算下來，最新收盤還要再跌約 22.06% 才會觸及。背景條件如下：S&P 500 最新 7572.4（2026-07-15），比 200 日均線高 8.51%、比 52 週均線高 10.25%（`valuation.sp500_trend`）。Shiller CAPE 42.18、trailing P/E 32.59（`valuation.sp500_pe_cape`）。Top-10 集中度 35.59%（`breadth.top10_concentration`）。FINRA margin debt $1.416T，YoY +53.7%（`retail.margin_debt`），已落在歷史頂部附近常見的 +40–50% 以上區間。這些讀數說明一旦下跌，跌幅可能很大。不過情緒面並不亢奮：CNN Fear & Greed 46（Fear）（`retail.fear_greed`），AAII Bull 36.3%／Bear 37.2%（`retail.aaii`）。VIX 15.67 與 S&P 500 在 7 日窗口內沒有同向上漲（VIX −7.28%、S&P 500 +1.2%，comove=false，`structural.vix_spx_comove`）。MOVE 68.48，低於 2026-07-13 的 77.77（`structural.treasury_basis_trade`），波動面沒有壓力。

**判讀：** 距 R1 還很遠。要在窗口內觸發，需要一次約 22% 以上的急跌，通常得有外生催化劑配合，例如 R3 型信用事件、hyperscaler 財報引發 capex 預期反轉，或 10Y 期限溢價（term premium）急升引發估值重定價。目前沒有任何一項已經發生。

### R2 資本支出收縮

最新可得資料是 2026-05-15 的彙整報導：Microsoft、Alphabet、Amazon、Meta 等 hyperscaler 的 2026 年 capex 合計約 $700B，最近一季（2026 Q1 財報季）指引方向是上修（`ai.hyperscaler_capex`）。本次證據只有彙整數字，沒有逐家的指引金額或方向，因此不另外為 Microsoft、Alphabet、Amazon、Meta 逐家標註上修／持平。可以確認的是：彙整報導的方向是整體上修，且沒有任何一家下修的紀錄，目前已知下修家數為 0。下一輪（2026 Q2）財報日期不在本次證據內，但依季度節奏應落在 7 月下旬至 8 月初，屬於窗口內第一個關鍵節點；2026 Q3 財報季（約 10 月下旬至 11 月初）也在窗口內。需求面方面，Anthropic run-rate 約 $47B、OpenAI 約 $25B（`ai.openai_anthropic_revenue`），伺服器 DRAM 2Q26 合約價季增 +58–63%（`ai.compute_supply_demand`），都顯示算力需求仍緊。AI 營收對 capex 缺口（revenue-to-capex gap）仍大：年化 capex 約 $700B，而 AI 終端營收只在低百億級（分母：MSFT／GOOGL／AMZN／META 合計；Oracle 本次無季頻更新，未納入）（`ai.revenue_capex_gap`）。

**判讀：** 距 R2 很遠，四家都還在上修。要在窗口內觸發，至少兩家須在 Q2 或 Q3 財報下修指引，通常需要 R1 型市場衝擊或需求明顯降溫（GPU 租價與利用率同步走弱）作為前提，目前證據指向相反方向。

### R3 AI 信用事件

規模夠格的 AI 基礎設施借款人以 CoreWeave 為代表。2026-07-12 報導顯示 CoreWeave 取得 $8.5B delayed-draw term loan，同時 Nvidia 相關循環融資曝險約 $24.9B（`structural.ai_infrastructure_debt`），說明 AI infrastructure debt financing / vendor-financing loops 仍在擴張，融資管道暢通，而不是收縮。AI 信用定價分歧（equity-vs-credit schism）方面，Oracle 5 年期 CDS 約 198bp，同期 CDX.NA.IG 約 95bp（2026-07-10，`valuation.ai_credit_schism`）。AI 相關信用利差相對 IG 基準明顯走闊，是後期訊號。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）方面，Blue Owl OCIC Q2 redemption-request ratio 達 18.8%，觸發 quarterly redemption cap 的 gate proration / breach（2026-07-02，`monetary.private_credit_liquidity`）。整體信用市場仍平靜：HY OAS 2.72%（`monetary.hy_oas`）、IG OAS 0.79%（`monetary.ig_oas`），銀行對 NBFI 放款 $2.00T 持平（`structural.nbfi_bank_loans`）。本次證據中，沒有任何 ≥ $5bn 的 AI 資料中心借款人出現付款違約、covenant waiver、distressed exchange 或 going-concern 字樣。

**判讀：** 距 R3 仍遠，但這是三條路徑中惡化最快的一條。Oracle CDS 已是 IG 基準約兩倍，私募信貸也出現實際 gate proration / breach。要在窗口內觸發，需要某家 neocloud 失去再融資管道、出現超過寬限期的違約或 distressed exchange；目前融資仍能取得，例如 CoreWeave 的新 DDTL。

## 支持 yes 的證據

- [R3] Oracle 5 年期 CDS 約 198bp，CDX.NA.IG 約 95bp（2026-07-10），AI 信用定價分歧（equity-vs-credit schism）往利差走闊方向發展，股價卻還在高點附近，屬後期訊號（`valuation.ai_credit_schism`）。
- [R3] Blue Owl OCIC Q2 redemption-request ratio 18.8%，觸發 quarterly redemption cap 的 gate proration / breach（2026-07-02）。這是私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）的實際事件，不只是結構性限制（`monetary.private_credit_liquidity`）。
- [R3] CoreWeave $8.5B DDTL 與 Nvidia 循環融資約 $24.9B（2026-07-12），AI infrastructure debt financing / vendor-financing loops 規模持續擴大，一旦需求放緩，傳導鏈會很長（`structural.ai_infrastructure_debt`）。
- [R1] FINRA margin debt $1.416T、YoY +53.7%（2026-05 月資料），落在 1999／2007／2021 頂部附近常見的區間（`retail.margin_debt`）。Shiller CAPE 42.18（2026-07-15，`valuation.sp500_pe_cape`），下行空間大。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 capex 約 $700B，AI 終端營收只在低百億級（2026-05-15，`ai.revenue_capex_gap`）。如果回報遲遲不出現，capex 指引最終有下修壓力。
- [整體] 美國槓桿 ETF 總 AUM 約 $198B 創紀錄（2026-07-10，`structural.leveraged_etf_aum`），OCC 6 月期權成交 1,603,491,559 口、YoY +45%（`structural.options_volume`），槓桿與投機部位擁擠，NAAIM 82.95（`retail.naaim`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 3.78%（2026-07-15），距 R1 門檻 22995.45 還要再跌約 22.06%（`valuation.ndx_drawdown`）。在 182 天內完成這種跌幅並不常見。
- [R2] hyperscaler 2026 capex 合計約 $700B，最近一次（2026 Q1 財報季）指引仍上修，四家中下修 0 家（`ai.hyperscaler_capex`）。伺服器 DRAM 2Q26 合約價 +58–63% QoQ，顯示算力需求緊，沒有閒置（`ai.compute_supply_demand`）。
- [R3] HY OAS 2.72%（2026-07-14，`monetary.hy_oas`）、IG OAS 0.79%（`monetary.ig_oas`）都處於歷史偏緊水準；repo 資金壓力（SOFR−IORB）為 −2bps，SRF 動用僅 $0.102bn（`monetary.repo_stress_srf`），沒有融資市場壓力。
- [R3] CoreWeave 仍能取得 $8.5B 新 DDTL（2026-07-12，`structural.ai_infrastructure_debt`）。主要 AI 基礎設施借款人的再融資管道暢通，與違約或 distressed exchange 的前提相反。
- [整體] 情緒面沒有亢奮：CNN Fear & Greed 46（Fear，2026-07-15，`retail.fear_greed`），AAII Bear 37.2% 略高於 Bull 36.3%（`retail.aaii`），VIX／S&P 500 沒有同向上漲（`structural.vix_spx_comove`）。典型的泡沫頂部情緒尚未出現。
- [整體] AI 終端需求仍在成長：Anthropic run-rate 約 $47B、OpenAI 約 $25B（2026-05-15，`ai.openai_anthropic_revenue`）。

## 與前期比較

前次結論：無前次預測（report-2026-07-13 為舊格式評分報告）

前次為舊格式評分報告，不轉換為 yes/no，flip_evidence 為空。以下為 2026-07-13 之後的主要資料變化：

- NASDAQ-100 由 29264.1（2026-07-13）回升至 29502.6（2026-07-15），距 52 週高點回撤 3.78%（`valuation.ndx_drawdown`）。
- MOVE 由 77.77 降至 68.48（`structural.treasury_basis_trade`），VIX 由 17.16 降至 15.67（`structural.vix_spx_comove`），波動面降溫。
- 10Y 殖利率 −4bps 至 4.58%（`monetary.dgs10`），HY OAS +3bps 至 2.72%（`monetary.hy_oas`），變動都很小。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源完成搜尋但無合格披露（✗ NOT DISCLOSED），對本次答案的影響如下：

- valuation.analyst_tp_decomposition、retail.social_sentiment、institutional.bofa_jpm_survey、ai.token_growth、ai.customer_concentration_rpo、ai.depreciation_life、speculation.upcoming_ai_ipos、structural.global_leveraged_approvals：都是輔助性訊號，缺漏不會改變三條路徑的距離判斷。
- ai.hyperscaler_financing_mix、ai.capital_cycle：兩個 component 都沒有取得當期披露（quarterly_state 與 event_scan 皆無）。hyperscaler 融資結構（capex vs FCF／發債）若出現大規模表外融資，可能讓 R3 的傳導路徑更具體，但不會直接觸發 R1–R3。
- speculation.insider_form4 以 openinsider 搜尋完成篩選，結果為 0 件；SEC EDGAR 一手 URL 因 egress 受限無法取得，所以「0 件」的完整度略低。此項不影響本次答案。
- structural.treasury_basis_trade：搜尋紀錄中有一筆 Yahoo MOVE 77.77（標為 2026-07-14），但腳本 move_index 為 ok，且 77.77 對應 artifact 中 2026-07-13 的 prior 值。本次以腳本值 68.48（2026-07-15）為準，未採用該搜尋值。
- 10Y 分解：ΔDGS10 −4bps、ΔDFII10 −3bps、ΔT10YIE −3bps，判讀：不可判（視窗不一致）。

最大的不確定性：

1. Microsoft、Alphabet、Amazon、Meta 的 2026 Q2 財報（預計 7 月下旬至 8 月初，確切日期不在本次證據內）。若有兩家下修 capex 指引，R2 會直接觸發，並可能帶動 R1，答案會轉向 yes。
2. Oracle／CoreWeave 等 AI 基礎設施信用。CDS 若繼續走闊，或 neocloud 再融資受阻，R3 可能提前觸發並連帶衝擊 R1，答案會轉向 yes。
3. 私募信貸贖回壓力是否擴散到多檔基金（Q3 redemption-request ratio 走勢）。若形成 net inflow→outflow flip，會加速信用傳導，答案偏向 yes；若 Q2 是高峰（PitchBook 引述 BofA 的看法），則支持維持 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest | 7572.4 | FRED API (series_id=SP500) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 8.51 | FRED API (series_id=SP500) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest | 29502.6 | FRED API (series_id=NASDAQ100) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-16T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 3.78 | FRED API (series_id=NASDAQ100) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q1） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-16T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5 | FRED API (series_id=DFEDTARL) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.72 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.79 | FRED API (series_id=BAMLC0A0CM) | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.58 | FRED API (series_id=DGS10) | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.33 | FRED API (series_id=DFII10) | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.23 | FRED API (series_id=T10YIE) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 79.2 | FRED API (series_id=DCOILWTICO) | 2026-07-13 | 2026-07-16T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-16T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.21 | FRED API (series_id=T5YIFR) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.7788 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-16T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.63 | FRED API (series_id=SOFR) | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.72 | FRED API (series_id=SOFR99) | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-07-16 | 2026-07-16T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.102 | FRED API (series_id=RPONTTLD) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6735609.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-08 | 2026-07-16T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5970516.0（€5.97T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-10 | 2026-07-16T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6395509.0（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-16T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.67 | FRED API (series_id=VIXCLS) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 15.67 | FRED API (series_id=VIXCLS, SP500) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 1995.0783（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-01 | 2026-07-16T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7573044 | CFTC TFF futures-only | 2026-07-07 | 2026-07-16T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 68.48 | Yahoo Finance chart API (^MOVE) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2405.1 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | MarketXLS WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | S&P DJI dashboard WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | McClellan WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH]（MacroMicro 鏡像） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA／Advisor Perspectives WebSearch | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／ycharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED DFEDTARU / DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（FRED BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（FRED BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（FRED DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（FRED T10YIE） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（FRED DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（FRED CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（FRED T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（FRED THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（SOFR／SOFR99／IORB／RPONTTLD） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | Reuters／TradingView [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME／MacroMicro [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（FRED WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW／JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Bloomberg WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]（30d） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／The Information WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報＋30d 融資事件 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K／10-Q [primary: SEARCH]（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速＋30d 進出場事件 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis／Axios WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／Benzinga／StockTitan movers [primary: SEARCH]（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | S-1／具名報導 WebSearch（30d） | ✗ NOT DISCLOSED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR [primary]（egress 受限）→ openinsider WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe／ycharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com／cryptobriefing [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | SEC／ETF.com WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe／Saxo WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 Retail Sentiment margin debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | WebSearch [primary: SEARCH]（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds／move_index／ofr_repo） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.59 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio（multpl） | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.18 | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E 約 40（trailing） | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026（MarketXLS） | 2026-05-15 | 2026-07-16T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS 約 198bp vs CDX.NA.IG 約 95bp | Oracle CoreWeave CDS spread vs CDX IG July 2026 | https://www.investing.com/analysis/oracle-and-coreweave-credit-default-swap-spreads-widening-omen-or-jitters-200670506（Investing.com） | 2026-07-10 | 2026-07-16T09:30:00+08:00 |
| breadth.rsp_spy | RSP +9.67% vs SPY +8.38% YTD | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/26/forget-the-magnificent-seven-this-equal-weight-sp-fund-beats-the-mega-caps-for-just-0-20/（24/7 Wall St.） | 2026-06-26 | 2026-07-16T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 35.59% | S&P 500 top 10 concentration percent 2026 | https://www.spglobal.com/spdji/en/documents/performance-reports/dashboard-sp-500-factor.pdf（S&P DJI） | 2026-04-30 | 2026-07-16T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 2008／下跌 2749，A/D 線建設性 | NYSE advance decline breadth July 2026 | https://www.mcoscillator.com/market_breadth_data/（McClellan） | 2026-07-13 | 2026-07-16T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 46（Fear） | CNN Fear and Greed Index today July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed（MacroMicro；原定 cnn.com） | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-05 月資料）$1.416T、+53.7% YoY | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra（Advisor Perspectives；原定 FINRA） | 2026-05-31 | 2026-07-16T09:30:00+08:00 |
| retail.aaii | AAII Bull 36.3%／Bear 37.2% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-07-09 | 2026-07-16T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 82.95 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number（YCharts） | 2026-07-08 | 2026-07-16T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y bid-to-cover 2.565、30Y bid-to-cover 2.44 | US Treasury 10Y 30Y auction July 2026 bid to cover | https://www.tradingview.com/news/macenews:30b090608094b:0-us-treasury-30-year-bond-auction-high-yield-5-058-bid-cover-ratio-at-2-44/（TradingView／MNI） | 2026-07-09 | 2026-07-16T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 FOMC 約 70% 持平 | CME FedWatch rate hold probability July 2026 | https://en.macromicro.me/series/78109/probability-fed-rate-325-350-2026（MacroMicro；原定 CME） | 2026-07-08 | 2026-07-16T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance（Bloomberg） | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio 18.8%，quarterly redemption cap gate proration / breach | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://pitchbook.com/news/articles/private-credit-bdc-redemption-requests-likely-to-peak-in-q2-2026-bofa（PitchBook） | 2026-07-02 | 2026-07-16T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 約 $700B、仍上修（2026 Q1 財報季） | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html（Yahoo Finance） | 2026-05-15 | 2026-07-16T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 約 $47B／OpenAI 約 $25B run-rate | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-05-15 | 2026-07-16T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 2Q26 合約價 +58–63% QoQ | DRAM HBM contract price 2Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260602-13074.html（TrendForce） | 2026-06-02 | 2026-07-16T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex 約 $700B vs AI 終端營收低百億級 | AI revenue to capex gap 2026 | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html（Yahoo Finance） | 2026-05-15 | 2026-07-16T09:30:00+08:00 |
| speculation.ai_rename_spac | General Fusion（GFUZ）SPAC 上市 | AI rename SPAC July 2026 General Fusion | https://www.morningstar.com/news/pr-newswire/20260710ln02448/（Morningstar／PR Newswire） | 2026-07-10 | 2026-07-16T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD 約 200 檔 IPO、募資 $141.2B | US IPO market 2026 YTD count proceeds | https://www.axios.com/2026/07/13/us-ipo-market-record-proceeds（Axios） | 2026-07-13 | 2026-07-16T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot 0 件 | microcap 100% single day quantum AI moonshot July 2026 | Finviz／Benzinga／StockTitan movers screener | — | 2026-07-16T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 cluster 0 件（EDGAR egress 受限） | insider Form 4 cluster AI leaders July 2026 openinsider | SEC EDGAR／openinsider | — | 2026-07-16T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.62（daily） | Cboe equity put call ratio July 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio（YCharts；原定 Cboe） | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 約 $198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing；原定 etf.com） | 2026-07-10 | 2026-07-16T09:30:00+08:00 |
| structural.us_single_stock_etf | GraniteShares SK hynix 2x long／inverse（SKUU／SKDD）上市 | single-stock leveraged ETF launch July 2026 SK Hynix Tradr | https://www.globenewswire.com/news-release/2026/07/14/3326857/0/en/GraniteShares-Launches-the-First-U-S-Listed-Leveraged-ETFs-on-SK-hynix.html（GlobeNewswire） | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 成交約 63% | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/（Cboe） | 2026-02-28 | 2026-07-16T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月成交 1,603,491,559 口、+45% YoY | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-07-16T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 期限結構 contango、Cboe SKEW 149.6 | VIX term structure SKEW July 2026 | https://www.home.saxo/content/articles/options/options-brief---calm-on-top-nervous-underneath---1-july-2026-01072026（Saxo） | 2026-07-01 | 2026-07-16T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-05 月資料）$1.416T、+53.7% YoY（交叉引用） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra（Advisor Perspectives） | 2026-05-31 | 2026-07-16T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $8.5B DDTL、Nvidia 循環融資 $24.9B | AI data center debt CoreWeave Nvidia circular financing July 2026 | https://www.techtimes.com/articles/320239/20260712/nvidia-circular-financing-249b-coreweave-debt-puts-pension-funds-risk.htm（Tech Times） | 2026-07-12 | 2026-07-16T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-07-16",
  "iso_week": "2026-W29",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-01-14",
  "prior_date": "2026-07-13",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 3.78,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

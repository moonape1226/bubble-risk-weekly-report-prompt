> [DRY RUN] this report was not committed to archive.
# 2026-08-03 AI 泡沫破裂預測報告

報告日期：2026-08-03｜ISO 週次：2026-W32｜預測窗口：2026-08-03 → 2027-02-01｜前次基準：report-2026-07-30（4天前）

## 結論

**結論：no**

三條路徑目前都沒有進行中的觸發：NASDAQ-100 距 52 週高點回撤 7.78%，距 R1 門檻還要再跌約 18.67%；四大 hyperscaler 2026 capex 合計仍在上修（≈$725B），沒有任何一家下修。CoreWeave 5Y CDS ≈675bp 顯示 R3 信用端確實在重定價，但本次未見破產、付款違約或 distressed exchange 的證據，高估值與槓桿只說明泡沫存在，不足以證明它會在 182 天內破裂。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 28,274.2（2026-07-31），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 7.78%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，需自最新收盤再下跌約 18.67% 才會觸發。周邊讀數：S&P 500 為 7,489.72，高於 200 日均線 6.63%、高於 52 週均線 8.2%（`valuation.sp500_trend`）；VIX 15.99，7 日 VIX 下跌 13.94% 而 S&P 500 上漲 1.05%，co-movement 警戒未成立（`structural.vix_spx_comove`）。Nasdaq-100 廣度偏弱：僅 48.0% 成分股站上 50 日均線、63.7% 站上 200 日均線（`breadth.advance_decline`）；Mag 7 對其餘 493 檔的估值溢價已收斂到 ≈10%（`valuation.mag7_multiples`）。估值仍高：S&P 500 trailing P/E 28.84、Shiller CAPE 40.91（`valuation.sp500_pe_cape`）。

**判讀：** R1 距門檻還很遠（再跌約 18.67%），且波動度與信用利差都沒有顯示急跌正在醞釀；要在窗口內觸發，需要 R3 類信用事件或 R2 capex 轉向這類外部衝擊引發的系統性去槓桿，目前兩者都未成形。

### R2 資本支出收縮

2026-07-28 的彙總報導指出，Microsoft、Alphabet、Amazon、Meta 的 2026 capex 計畫在最近一次財報（2026 Q2 季報季）後續上修，合計 ≈$725B（+77% YoY）（`ai.hyperscaler_capex`）。本次取得的來源只有四家合計，沒有逐家的指引數字，所以四家的方向只能依彙總報導記為「上修／未見下修」，個別指引金額本次未建立。截至目前，四家中下修的家數為 0。同期 top-5 capex 已超過 FCF、續靠外部融資，五大 2026 發債 ≈$159B（+47% YoY），Amazon 遭 S&P 降至 BBB-（`ai.hyperscaler_financing_mix`）。需求端讀數仍偏緊：伺服器 DRAM 交期 30–40 週、3Q26 合約價 +13–18% QoQ（`ai.compute_supply_demand`）。另一方面，AI 營收對 capex 缺口（revenue-to-capex gap）很大：年化 AI 終端營收 ≈$72B（Anthropic ≈$47B＋OpenAI ≈$25B）對年化 capex ≈$725B（分母：top-4 hyperscaler 合計，未含 Oracle 與 neocloud），本次無新組件披露可判斷缺口是擴大還是收斂（`ai.revenue_capex_gap`）。

**判讀：** R2 目前離觸發最遠——最新一次指引全面上修，零家下修。窗口（至 2027-02-01）大致涵蓋接下來兩次季報季，但具體財報日期本次未取得。要觸發，需要至少兩家在下兩次財報中主動下修；以 capex 超過 FCF、評級下調的融資壓力來看，這是可能的轉折機制，但目前沒有任何一家釋出下修訊號。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）出現實際重定價：2026-07-30 報導 CoreWeave 5Y CDS ≈675bp、Oracle 5Y CDS ≈200bp，hyperscaler 債利差 ≈78bp（`valuation.ai_credit_schism`）。在 AI infrastructure debt financing / vendor-financing loops 方面，Nebius 於 2026-07-17 完成首筆 $775M 擔保債務融資（GPU 基建擔保），代表 neocloud 仍能進入擔保債市場（`structural.ai_infrastructure_debt`）。可能達到 R3 規模門檻的借款人中，CoreWeave 是本次信用定價最弱的名字，但其總負債是否 ≥ 50 億美元，本次取得的來源並未提供，因此不能斷定它符合規模門檻；本次也沒有取得任何借款人的到期牆、契約豁免、付款遲延或 going-concern 揭露。廣義信用仍然很緊：HY OAS 2.84%、IG OAS 0.80%（2026-07-30）（`monetary.hy_oas`、`monetary.ig_oas`）。

**判讀：** R3 是三條路徑中最接近的一條：個別 neocloud 的 CDS 已處於高壓力區間，但 CDS 走闊不等於違約。要在窗口內觸發，需要一家負債 ≥ 50 億美元的 AI 算力借款人實際申請破產、逾寬限期違約或完成 distressed exchange；目前 neocloud 仍能取得擔保融資、HY 利差維持低檔，沒有證據顯示事件已在進行中。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS ≈675bp、Oracle 5Y CDS ≈200bp（2026-07-30），AI 雲端信用已開始重定價，信用端走在股價前面是典型的後期訊號（`valuation.ai_credit_schism`）。
- [R2] top-5 hyperscaler capex 已超過 FCF、續靠外部融資，Amazon 遭 S&P 降至 BBB-（2026-07-24）；五大 2026 發債 ≈$159B（+47% YoY，2026-07-22），融資約束是未來下修 capex 的潛在機制（`ai.hyperscaler_financing_mix`）。
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收 ≈$72B 對年化 capex ≈$725B（分母：top-4 hyperscaler），回本壓力大（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`）。
- [R1] 槓桿與估值極端：FINRA 6 月 margin debt $1.502T、YoY +51.5%（`retail.margin_debt`）；Shiller CAPE 40.91、trailing P/E 28.84（2026-07-31）（`valuation.sp500_pe_cape`）；US 槓桿 ETF AUM 創高 ≈$198B（`structural.leveraged_etf_aum`）——一旦下跌，跌幅可能被放大。
- [R1] 內部廣度轉弱：Nasdaq-100 僅 48.0% 成分股站上 50 日均線、10 日淨新高 ≈0.1%（2026-07-29）（`breadth.advance_decline`）；MOVE 由 77.09 升至 83.02（2026-07-31）（`structural.treasury_basis_trade`）；10Y 期限溢價（term premium）0.8376%、trailing 7 日 +5.9bp（2026-07-24）（`monetary.term_premium`）。
- [整體] Fed 緩衝空間有限：FOMC 7/29 鷹派持平（9-3）（`monetary.fedwatch`），CPI YoY 3.46%（2026-06 月資料）（`monetary.cpi_yoy`），一旦 AI 引發回撤，降息托底的空間受通膨限制。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 7.78%（2026-07-31），門檻水位 22,995.45，需再跌約 18.67% 才觸發，在 182 天內完成需要目前沒有的衝擊（`valuation.ndx_drawdown`）。
- [R2] hyperscaler 2026 capex 合計 ≈$725B（+77% YoY），最近一次財報後續上修，四家中下修家數為 0（2026-07-28）（`ai.hyperscaler_capex`）。
- [R3] 廣義信用市場沒有傳染：HY OAS 2.84%、IG OAS 0.80%（2026-07-30）（`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 0bp、SRF 動用 0（`monetary.repo_stress_srf`）。
- [R3] neocloud 仍能取得融資：Nebius 2026-07-17 完成 $775M 擔保債務融資（`structural.ai_infrastructure_debt`），融資市場沒有關門。
- [R2] AI 算力需求端仍緊：伺服器 DRAM 交期 30–40 週、3Q26 合約價 +13–18% QoQ（2026-07-03），沒有 order digestion 或利用率下滑的跡象（`ai.compute_supply_demand`）。
- [整體] 情緒已不亢奮、波動度下降：CNN Fear & Greed ≈39（Fear，2026-07-31）（`retail.fear_greed`）；AAII Bear 42.1%（2026-07-30）（`retail.aaii`）；VIX 15.99、VIX/S&P 500 co-movement 未成立（`structural.vix_spx_comove`）。

## 與前期比較

前次結論：無前次預測（report-2026-07-30 為舊格式評分報告）

本次為新格式下第一份預測，前次為舊格式評分報告，其分數不轉換為 yes/no，flip_evidence 為空。自 2026-07-30 起的主要變化：

- MOVE 由 77.09 升至 83.02（2026-07-31），債市波動度上升。
- S&P 500 由 7,437.63 升至 7,489.72（+0.7%），VIX 由 17.09 降至 15.99。
- DGS10、DFII10 無新觀測（4.68%、2.41%）；T10YIE +1bp 至 2.28%，視窗不一致，10Y 變動歸因判讀：不可判（視窗不一致）。
- CoreWeave CDS ≈675bp 的報導日期為 2026-07-30，與前次基準同日，是本次最主要的 R3 壓力讀數。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED（搜尋完成但無合格當期披露）：retail.social_sentiment、institutional.bofa_jpm_survey、monetary.treasury_auctions、monetary.private_credit_liquidity、ai.token_growth、ai.customer_concentration_rpo、ai.depreciation_life、ai.capital_cycle、structural.global_leveraged_approvals。其中私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）與 backlog 重複計算風險（RPO double-counting）的缺席與 R3 最相關：若存在未揭露的 gate proration / breach，可能讓 R3 傳導路徑比目前看到的更近，但單憑缺漏不足以翻轉答案。資本週期階段（capital cycle stage）本次增速證據不足，不判定週期階段。內部人 Form 4 螢幕在 14 日內找到一筆線索，但缺少完整的 filing-level 欄位（獨立的申報日與單筆 Form 4 filing URL），依規則不列為具名證據，以 0 件計。

最大的不確定性：

1. CoreWeave 等 neocloud 的實際負債規模與近期到期／再融資需求本次未建立——若證實負債 ≥ 50 億美元且有逼近的到期牆，R3 會明顯接近，推向 yes。
2. 下兩次 hyperscaler 財報的 capex 指引（具體日期本次未取得）——若兩家以上因融資壓力下修，R2 直接觸發，並可能帶動 R1，推向 yes；若持續上修則強化 no。
3. Fed 路徑：CPI YoY 3.46%、FOMC 鷹派持平，若通膨迫使政策維持偏緊而 AI 信用持續走闊，回撤緩衝會變小，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7489.72 | FRED API (series_id=SP500) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 6.63 | FRED API (series_id=SP500) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 8.2 | FRED API (series_id=SP500) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28274.2 | FRED API (series_id=NASDAQ100) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 7.78 | FRED API (series_id=NASDAQ100) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q1 季資料） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-03T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-02 | 2026-08-03T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-02 | 2026-08-03T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.84 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.8 | FRED API (series_id=BAMLC0A0CM) | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.68 | FRED API (series_id=DGS10) | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.41 | FRED API (series_id=DFII10) | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.28 | FRED API (series_id=T10YIE) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | 1.0 | FRED API (series_id=T10YIE) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 84.25 | FRED API (series_id=DCOILWTICO) | 2026-07-27 | 2026-08-03T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-08-03T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.3 | FRED API (series_id=T5YIFR) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest | 0.8376 | FRED API (series_id=THREEFYTP10) | 2026-07-24 | 2026-08-03T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 日） | 5.9 | FRED API (series_id=THREEFYTP10) | 2026-07-24 | 2026-08-03T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.65 | FRED API (series_id=SOFR) | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.73 | FRED API (series_id=SOFR99) | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-08-03 | 2026-08-03T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6738190.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-29 | 2026-08-03T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5944015.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-24 | 2026-08-03T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6395509.0（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-08-03T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.99 | FRED API (series_id=VIXCLS) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 15.99 | FRED API (VIXCLS × SP500 derived block) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | -13.94 | FRED API (VIXCLS × SP500 derived block) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | 1.05 | FRED API (VIXCLS × SP500 derived block) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2004.9941（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-22 | 2026-08-03T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7481041 | CFTC TFF futures-only (cftc_lev_funds) | 2026-07-28 | 2026-08-03T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 83.02 | Yahoo Finance chart API ^MOVE (move_index) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index prior | 77.09 | Yahoo Finance chart API ^MOVE (move_index) | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2293.2 | OFR STFM REPO-TRIV1_TV_TOT-P (ofr_repo) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | Advisor Perspectives，WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報摘要 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | Pensions & Investments，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | streetstats NQ100 breadth proxy，WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA via Advisor Perspectives，WebSearch | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | r/wallstreetbets / X cashtag，WebSearch | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | YCharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查，WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（FRED API） | ✓ API |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（FRED API） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（FRED API） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（FRED API） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED API） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（FRED API，FRED-direct） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（FRED API） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（FRED API，yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（FRED API） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（FRED API，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（FRED API；SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） | ✓ API |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | Reuters / Bloomberg auction recap [primary: SEARCH] | ✗ NOT DISCLOSED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（FRED API） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（FRED API；ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Bloomberg，WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC / interval fund 披露 [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報彙總報導，WebSearch | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic / OpenAI / Google 披露，WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch AI 彙整，WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話會議 [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：FactSet 季頻彙整；event_scan：30 日發債掃描 [primary: SEARCH] | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露（Epoch AI＋hyperscaler capex 彙總）[primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K / 10-Q / 財報電話 [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | quarterly_state：供需增速 proxies；event_scan：30 日進出場事件 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC / no-revenue IPO | Reuters / Benzinga / Boardroom Alpha，WebSearch | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | valueaddvc，WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz / Benzinga / StockTwits / Yahoo movers [primary: SEARCH] | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導（Benzinga），WebSearch | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 [primary: SEC EDGAR] | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | YCharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com / 財經報導 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire 新發行公告，WebSearch | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX / TWSE / JPX / ESMA / ETFGI，WebSearch | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe 季報摘要，WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC monthly volume report | theocc.com，WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Saxo options brief，WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（FRED VIXCLS＋vix_spx_comove block） | ✓ API |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 retail.margin_debt，WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | 公司新聞稿 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED API） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok）；WebSearch 補充無合格事件 | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 28.84（原定來源 multpl.com） | S&P 500 trailing P/E August 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 40.91（原定來源 multpl.com） | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 對其餘 493 檔溢價 ≈10% | Magnificent 7 valuation premium compressed 2026 | https://www.advisorperspectives.com/articles/2026/07/09/magnificent-sevens-weakness-become-problem-wall-street （Advisor Perspectives） | 2026-07-09 | 2026-08-03T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標價 $288，目標 PE 未擴張（EPS-driven） | Morgan Stanley NVDA target 288 July 2026 EPS | https://www.gurufocus.com/news/8955458/morgan-stanley-upgrades-nvidia-nvda-with-a-288-target-price （GuruFocus） | 2026-07-13 | 2026-08-03T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5Y CDS ≈200bp、CoreWeave 5Y CDS ≈675bp、hyperscaler 債利差 ≈78bp | Oracle CoreWeave CDS AI credit repricing hyperscaler spread August 2026 | https://www.techtimes.com/articles/322222/20260730/coreweave-cds-hits-50-default-odds-bond-market-calls-time-gpu-debt-spiral.htm （Tech Times） | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD +9.67% vs SPY YTD +8.38% | RSP vs SPY equal weight YTD 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St.） | 2026-06-10 | 2026-08-03T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 ≈40% | S&P 500 top 10 concentration percent 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/ （Pensions & Investments） | 2026-07-02 | 2026-08-03T09:30:00+08:00 |
| breadth.advance_decline | Nasdaq-100 48.0% >50DMA、63.7% >200DMA、10 日淨新高 ≈0.1% | Nasdaq 100 breadth percent above 50 day 200 day July 2026 | https://streetstats.finance/markets/breadth-momentum/NQ100 （StreetStats） | 2026-07-29 | 2026-08-03T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed ≈39（Fear） | CNN Fear and Greed Index July 31 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives／FINRA） | 2026-07-20 | 2026-08-03T09:30:00+08:00 |
| retail.aaii | AAII Bear 42.1%／Neutral 26.9%／Bull 31.0% | AAII investor sentiment survey July 30 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| retail.naaim | NAAIM 84.02 → 79.70 | NAAIM exposure index July 2026 | https://ycharts.com/indicators/naaim_number （YCharts） | 2026-07-29 | 2026-08-03T09:30:00+08:00 |
| monetary.fedwatch | FOMC 7/29 鷹派持平（9-3）、CME FedWatch 9 月路徑分歧 ≈63% | FOMC July 29 2026 hold FedWatch September cut probability | https://growbeansprout.com/tools/fedwatch （Beansprout FedWatch） | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.pboc | 人行 7/24 MLF 淨投放 ≈¥100B（5 個月最大） | PBoC MLF net injection liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-24/pboc-adds-most-liquidity-to-economy-in-five-months-to-aid-growth （Bloomberg） | 2026-07-24 | 2026-08-03T09:30:00+08:00 |
| ai.hyperscaler_capex | MSFT / GOOGL / AMZN / META 2026 capex 合計 ≈$725B（+77% YoY）續上修（2026 Q2 季報季） | hyperscaler capex 2026 725B raised Meta Amazon Alphabet Microsoft | https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion （Tom's Hardware） | 2026-07-28 | 2026-08-03T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic run-rate ≈$47B、OpenAI ≈$25B | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-06-15 | 2026-08-03T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 交期 30–40 週、3Q26 合約價 +13–18% QoQ | DRAM contract price 3Q26 TrendForce lead time | https://www.trendforce.com/presscenter/news/20260703-13134.html （TrendForce） | 2026-07-03 | 2026-08-03T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超越 FCF、續靠外部融資、Amazon 遭 S&P 降至 BBB- | hyperscaler capex FCF debt Amazon downgrade BBB- 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow （FactSet） | 2026-07-24 | 2026-08-03T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 五大 hyperscaler 2026 發債 ≈$159B（+47% YoY） | hyperscaler bond issuance 159B 2026 AI credit | https://cryptobriefing.com/tech-giants-record-159b-bonds-ai/ （Crypto Briefing） | 2026-07-22 | 2026-08-03T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 ≈$72B（Anthropic ≈$47B＋OpenAI ≈$25B） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-06-15 | 2026-08-03T09:30:00+08:00 |
| ai.revenue_capex_gap | 分母：top-4 hyperscaler 年化 capex ≈$725B | hyperscaler capex 2026 725B raised Meta Amazon Alphabet Microsoft | https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion （Tom's Hardware） | 2026-07-28 | 2026-08-03T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／no-revenue IPO 螢幕：合格 0 件 | AI rename SPAC no revenue IPO July 27 August 3 2026 | Reuters / Benzinga / Boardroom Alpha SPAC 螢幕 | — | 2026-08-03T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD 86 檔、募資 ≈$251B、JMKE 首日收平、aftermarket 轉弱 | US IPO market 2026 Jersey Mike's Cerebras aftermarket | https://valueaddvc.com/blog/ipo-market-2026-which-companies-are-going-public-and-what-the-window-looks-like （ValueAdd VC） | 2026-08-01 | 2026-08-03T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot 螢幕：合格 0 件 | microcap 100% single day quantum AI fusion moonshot July August 2026 | Finviz / Benzinga / StockTwits / Yahoo movers 螢幕 | — | 2026-08-03T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 ≈$1T IPO、Anthropic 續進 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground （Benzinga） | 2026-07-28 | 2026-08-03T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 cluster 螢幕：具完整 filing-level 欄位的合格件數 0 件 | CoreWeave insider Form 4 July 2026 Intrator SEC | SEC EDGAR Form 4 company filing index（browse-edgar） | — | 2026-08-03T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.63（日讀數） | Cboe equity put call ratio July 31 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio （YCharts） | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高 ≈$198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing） | 2026-07-23 | 2026-08-03T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x 單股槓桿 ETF＋ELOL（TSLA+SpaceX）發行 | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | https://www.manilatimes.net/2026/07/30/tmt-newswire/globenewswire/two-industry-leaders-one-ticker-leverage-shares-by-themes-launches-elol/2395125 （GlobeNewswire via Manila Times） | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量 ≈65%（Cboe Q2 2026） | 0DTE SPX options share volume Cboe Q2 2026 | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641 （Investing.com） | 2026-05-31 | 2026-08-03T09:30:00+08:00 |
| structural.options_volume | OCC 總量（2026-06 月資料）16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-08-03T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW ≈139.9、VIX 17.09（term structure contango） | VIX SKEW term structure July 31 2026 | https://www.home.saxo/content/articles/options/index-up-average-stock-down---options-brief---31-july-2026-31072026 （Saxo） | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt（2026-06 月資料）$1.502T、+51.5% YoY（交叉引用 retail.margin_debt） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-08-03T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Nebius $775M 首筆擔保債務融資（GPU 基建擔保） | AI data center debt financing Nebius secured facility July 2026 | https://nebius.com/newsroom/nebius-raises-775-million-in-first-secured-debt-financing-to-accelerate-global-buildout （Nebius） | 2026-07-17 | 2026-08-03T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-03",
  "iso_week": "2026-W32",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-01",
  "prior_date": "2026-07-30",
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 7.78,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

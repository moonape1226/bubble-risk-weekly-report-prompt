> [DRY RUN] this report was not committed to archive.
# 2026-09-13 AI 泡沫破裂預測報告
報告日期：2026-09-13｜ISO 週次：2026-W37｜預測窗口：2026-09-13 → 2027-03-14｜前次基準：report-2026-09-03（10天前）

## 結論

**結論：no**

三條路徑目前都沒有「已在進行中」的證據：NASDAQ-100 距 52 週高點僅回撤 4.21%（R1 門檻需再跌約 21.7%），四大 hyperscaler 2026 capex 合計仍約 $725bn、未見任何下修（R2），HY OAS 2.70% 與 IG OAS 0.80% 顯示信用市場並未對 AI 借款人重定價（R3）。9/16 FOMC 高機率升息與油價上行是需要追蹤的催化劑，但尚不足以推翻 182 天窗口內三項條件皆不成立的基準情境。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

`valuation.ndx_drawdown`：NASDAQ-100 最新收盤 29,368.44（2026-09-11），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 4.21%。R1 門檻水位為 22,995.45，自最新收盤需再下跌約 21.7% 才觸及。S&P 500（`valuation.sp500_trend`）收 7,656.98（2026-09-11），仍高於 200 日均線 6.90%、高於 52 週均線 8.33%，但較前次基準日（7,747.71）下跌 1.17%。估值仍處高檔：Shiller CAPE 約 40.73（`valuation.sp500_pe_cape`，2026-09-01），前十大成分股佔 S&P 500 約 38%（`breadth.top10_concentration`）。波動開始抬頭：VIX 由 14.32 升至 17.84（`structural.vix_spx_comove`，2026-09-03 → 2026-09-10，+24.58%），同期 S&P 500 −2.01%，屬正常的反向走勢（comove=false），非 crowded-optionality 警戒；call skew 位於第 91 百分位（`structural.cross_asset_derivatives`，2026-09-10）。

**判讀：** R1 距離門檻仍遠（回撤 4.21% vs 需 25%）。要在窗口內成立，需要一個足以讓 NASDAQ-100 跌破 22,995.45 的衝擊——例如 9/16 FOMC 意外鷹派連續升息、油價持續推升通膨、或 AI 龍頭財報引發 capex/營收預期重估。高 CAPE 與高集中度意味著一旦觸發跌幅會很大，但目前沒有證據顯示這類去槓桿已經開始。

### R2 資本支出收縮

`ai.hyperscaler_capex`：根據 2026-07-28 的 Q2 財報季彙整（CNBC），Microsoft、Alphabet、Amazon、Meta 2026 年 capex 指引合計約 $725bn；本次取得的證據只有合計值，未逐家列出各自指引金額，因此四家的逐家方向判讀為：Microsoft 未提供逐家數據、Alphabet 未提供逐家數據、Amazon 未提供逐家數據、Meta 未提供逐家數據——證據中沒有任何一家下修的報導，目前已下修家數為 0／4。同一報導指出市場對 capex 的檢視趨嚴（Alphabet 財報後股價受挫）。需求側：Anthropic 年化 run-rate 約 $65bn（`ai.openai_anthropic_revenue`，2026-08-17）；年化 AI 終端營收約 $105bn vs 年化 capex 約 $725bn（`ai.revenue_capex_gap`；分母：top-4，Oracle 本次無可組合數據），AI 營收對 capex 缺口仍大。算力價格：H100 中位租金約 $3.38/hr（`ai.compute_supply_demand`，2026-08-31），單看價格未伴隨利用率下滑或訂單消化證據，不構成過剩訊號。

**判讀：** R2 尚未開始。窗口內落有兩次財報季（2026 年 10 月下旬的 Q3 財報與 2027 年 1 月下旬至 2 月初的 Q4 財報，日期為慣例推估、本次未取得確切日期），Q4 財報通常給出 2027 年 capex 指引，是 R2 最主要的觸發點。要成立需要兩家以上下修——在 run-rate 營收仍快速成長、算力租金未崩的情況下，目前沒有證據指向這個方向。

### R3 AI 信用事件

本次 14 日內未取得 AI 發債人（Oracle、CoreWeave、neocloud）的利差／CDS 定價報導，故無法直接觀察 AI 信用定價分歧。廣義信用市場平穩：HY OAS 2.70%（`monetary.hy_oas`，2026-09-10，+5 bps）、IG OAS 0.80%（`monetary.ig_oas`，−1 bp），均處於極緊水位。`structural.ai_infrastructure_debt`：30 日內唯一新揭露是 Qualcomm 給予 Amazon 約 $4bn 認股權證的資料中心基礎建設交易（2026-09-08），屬 vendor-financing 型安排（供應商以股權誘因換取客戶採購），但不是債務壓力事件。repo 資金面無壓力：SOFR−IORB −3 bps、SOFR99−IORB +5 bps、SRF 動用 0（`monetary.repo_stress_srf`，2026-09-10/11）。

**判讀：** 證據中沒有任何 ≥$5bn 負債的 AI 算力借款人出現違約、寬限期、covenant waiver 或 distressed exchange 跡象。R3 要在窗口內成立，需要一家大型 neocloud 在再融資或客戶合約失效時出現流動性斷裂；這通常會先在利差、私募信貸贖回或 HY OAS 上露出前兆，目前三者都沒有。

## 支持 yes 的證據

- [整體] 9/16 FOMC 升息 25 bps 的市場隱含機率約 85.5%（2026-09-12），而 Fed funds 目前為 3.50%–3.75%；在估值極高時轉向緊縮是歷史上泡沫破裂最常見的催化劑（`monetary.fedwatch`、`monetary.fed_funds`）。
- [R1] 通膨與利率壓力同步上升：WTI 由 $92.55 升至 $97.26（+5.09%，2026-09-09）、CPI YoY 3.35%（2026-08 月資料）、10Y 殖利率 4.95%（+18 bps，2026-09-10），壓縮高估值成長股的折現空間（`monetary.wti`、`monetary.cpi_yoy`、`monetary.dgs10`）。
- [R1] 估值與集中度處於泡沫區：Shiller CAPE 約 40.73（2026-09-01），前十大佔 S&P 500 約 38%（2026-09-01），一旦觸發跌幅會被放大（`valuation.sp500_pe_cape`、`breadth.top10_concentration`）。
- [R2] AI 營收對 capex 缺口仍大：年化 AI 終端營收約 $105bn vs top-4 年化 capex 約 $725bn（2026-08-17 / 2026-07-28），市場對 capex 回報的檢視已趨嚴（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`）。
- [R1] 波動率抬頭：VIX 17.84（2026-09-10，七日 +24.58%）、MOVE 82.21（2026-09-11，+7.53），債市與股市的避險需求同時上升（`structural.vix_spx_comove`、`structural.treasury_basis_trade`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤僅 4.21%（2026-09-11），距 R1 門檻 22,995.45 仍需再跌約 21.7%（`valuation.ndx_drawdown`）。
- [R3] 信用市場無重定價：HY OAS 2.70%、IG OAS 0.80%（2026-09-10），repo 資金壓力（SOFR−IORB）為 −3 bps、SRF 動用 0（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`）。
- [R2] 四大 hyperscaler 2026 capex 指引合計約 $725bn（2026-07-28），證據中 0／4 下修；需求端 Anthropic 年化 run-rate 約 $65bn（2026-08-17）仍在擴張（`ai.hyperscaler_capex`、`ai.openai_anthropic_revenue`）。
- [整體] 散戶情緒已偏恐懼而非亢奮：CNN Fear & Greed 約 35（2026-09-10）、AAII 看多約 38.0%（2026-09-10）；單一個股槓桿 ETF 本週流出約 $751m、規模約 $40.74bn（2026-09-08），槓桿正在降溫而非堆疊（`retail.fear_greed`、`retail.aaii`、`structural.leveraged_etf_aum`）。
- [整體] 投機篩選低溫：7 日內 +AI 改名／SPAC 0 件、microcap moonshot 0 件，30 日內美國單一個股槓桿 ETF 新核准／上市 0 件（`speculation.ai_rename_spac`、`speculation.microcap_moonshots`、`structural.us_single_stock_etf`）。

## 與前期比較

前次結論：yes（report-2026-09-03）
本次結論：翻轉
翻轉依據：
- 前次 forecast.json 未記錄 `yes_basis`（該欄位為新增欄位），因此沒有可逐項延續的 yes 理由；`yes` 必須每次重新取得，本次以當前證據重新檢驗後未達門檻。
- `valuation.ndx_drawdown`：回撤由前次 4.95% 收窄至 4.21%（2026-09-11），R1 並未朝門檻推進。
- `ai.hyperscaler_capex`：最新指引（2026-07-28）合計約 $725bn，無任何一家下修，R2 未啟動。
- `monetary.hy_oas`：HY OAS 2.70%（2026-09-10），較前次僅 +5 bps，信用端沒有出現 R3 的前兆。
- `structural.ai_infrastructure_debt`：30 日內唯一 AI 基建融資揭露是 Qualcomm–Amazon 約 $4bn 認股權證（2026-09-08），屬 vendor-financing 型安排而非債務壓力事件。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源為 ✗ NOT DISCLOSED（搜尋完成、無窗口內合格揭露）：valuation.analyst_tp_decomposition、valuation.ai_credit_schism、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.private_credit_liquidity、ai.token_growth、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（quarterly_state 有值、event_scan 30 日內無事件）、ai.depreciation_life、ai.capital_cycle、speculation.upcoming_ai_ipos、structural.global_leveraged_approvals。其中 valuation.ai_credit_schism 與 monetary.private_credit_liquidity 的缺漏最可能影響 R3 判讀：若 AI 發債人利差已悄悄走闊而未被搜尋到，R3 的前兆可能被低估；但 HY OAS 與 repo 資料平穩，降低了這個風險。

其他資料注意事項：
- 外部證據摘要將美債基差交易槓桿標為腳本三區塊 fetch_failed，但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 均為 status ok；本報告以 artifact 為準記 ✓ API。
- speculation.insider_form4：搜尋到一筆 NVDA Form 4（SEC EDGAR，2026-09-02），但證據未分別列出申報日與交易日，不符合 filing-level 完整欄位要求，故依規則記 0 件且不列名。
- ai.hyperscaler_capex 只取得四家合計值，逐家指引方向無法逐一核對；若其中有一家已小幅下修而未被彙整報導，R2 的距離會比本文所述更近。
- 10Y 分解：ΔDGS10 +18 bps、ΔDFII10 +13 bps、ΔT10YIE +1 bp，driver 判讀為 不可判（視窗不一致）。

主要不確定性：
1. 2026-09-16 FOMC：若如市場預期升息且釋出持續緊縮訊號，加上 WTI 逼近 $100，可能觸發估值重估，推向 yes（R1）。
2. 2027 年 1 月下旬至 2 月初 Q4 財報的 2027 年 capex 指引：若兩家以上下修即直接觸發 R2，推向 yes；若持續上修則強化 no。
3. AI 發債人信用定價：本次無直接資料；一旦 neocloud 利差或私募信貸贖回出現壓力，R3 與 R1 會同時升溫，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7656.98 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 6.9 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.33 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29368.44 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 4.21 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q2 季資料） | 48.2301354474（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（上限） | 3.75（%） | FRED API (series_id=DFEDTARU) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（下限） | 3.5（%） | FRED API (series_id=DFEDTARL) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.7（%） | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 5.0（bps） | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.8（%） | FRED API (series_id=BAMLC0A0CM) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.95（%） | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | 18.0（bps） | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.55（%） | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | 13.0（bps） | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.36（%） | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | 1.0（bps） | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 97.26（美元／桶） | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO chg_pct | 5.09（%） | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-08 月資料） | 3.35（%） | FRED API (series_id=CPIAUCSL) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.32（%） | FRED API (series_id=T5YIFR) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8892（%） | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.62（%） | FRED API (series_id=SOFR) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.7（%） | FRED API (series_id=SOFR99) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65（%） | FRED API (series_id=IORB) | 2026-09-13 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用） | 0.0（十億美元） | FRED API (series_id=RPONTTLD) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6740619.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5912178.0（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6446620.0（¥644.66T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 17.84 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（comove=false） | 17.84 | FRED API (derived block) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 24.58（%） | FRED API (derived block) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | −2.01（%） | FRED API (derived block) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2027.9777（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -6863118（口） | CFTC TFF (cftc_lev_funds) | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 82.21 | Yahoo chart ^MOVE (move_index) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2271.6（十億美元） | OFR STFM (ofr_repo) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（multpl / gurufocus） | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✗ NOT DISCLOSED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py BOGZ1FL153064486Q | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py DFEDTARU＋DFEDTARL | ✓ API（DFEDTARU ok、DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py BAMLH0A0HYM2 | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py BAMLC0A0CM | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py DGS10 | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | scripts/fetch_macro.py DFII10 | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py T10YIE（FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py DCOILWTICO | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | scripts/fetch_macro.py CPIAUCSL yoy_pct | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py T5YIFR | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py THREEFYTP10 | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py SOFR、SOFR99、IORB、RPONTTLD | ✓ API（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py WALCL | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py ECBASSETSW＋JPNASSETS | ✓ API（ECBASSETSW ok、JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state，Q2 財報） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch（quarterly_state stock-of-state；event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch（stock-of-state 組合） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch（quarterly_state stock-of-state；event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✗ NOT DISCLOSED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR ＋ WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR ＋ ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe insights） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報摘要） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py VIXCLS＋vix_spx_comove | ✓ API（VIXCLS ok、vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py LNFACBW027SBOG | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds、move_index、ofr_repo | ✓ API（cftc_lev_funds ok、move_index ok、ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.73 | S&P 500 Shiller CAPE ratio current September 2026 multpl | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio （GuruFocus；原定 multpl / gurufocus） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | Magnificent 7 forward P/E valuation September 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html （CNBC） | 2026-08-03 | 2026-09-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 至 7 月止 YTD 報酬約 13% | RSP equal weight vs SPY S&P 500 YTD performance September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/ （24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.top10_concentration | 前十大集中度約 38% | S&P 500 top 10 concentration percentage September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/ （24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 200 日均線之上約 53% | market breadth advance decline new highs lows September 2026 percent stocks above 200-day | https://condoredge.com/stocks/market-breadth （Condor Edge） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 約 35（恐懼） | CNN Fear and Greed Index today September 2026 reading | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| retail.margin_debt | margin debt 約 $1.42T（2026-07 月資料） | FINRA margin debt August 2026 record year over year | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026 （Advisor Perspectives；原定 FINRA） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.0% | AAII sentiment survey results week September 10 2026 bullish bearish neutral | https://www.aaii.com/sentimentsurvey （AAII） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.71 | Treasury auction results September 2026 tail bid-to-cover 10-year | https://thevaultreport.com/treasury-auctions （The Vault Report） | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.fedwatch | 9/16 FOMC 升息 25 bps 隱含機率約 85.5% | CME FedWatch September 12 2026 probability 25 basis point hike | https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html （Yahoo Finance；原定 CME FedWatch） | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate financing 2026 total social financing | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm （SteelOrbis） | 2026-08-15 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 指引合計約 $725bn（Q2 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 $65bn | OpenAI Anthropic annualized revenue run rate September 2026 | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| ai.compute_supply_demand | H100 中位租金約 $3.38/hr | GPU rental price HBM DRAM contract price September 2026 utilization | https://www.thundercompute.com/blog/ai-gpu-rental-market-trends （Thunder Compute） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 增額債務佔 capex 約 32% | hyperscaler capex vs free cash flow debt issuance 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $105bn（分母：top-4 capex 約 $725bn） | AI revenue vs capex gap 2026 annualized run rate | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement September 7-13 2026 | 檢查來源：SPACInsider、Businesswire SPAC newsroom、Boardroom Alpha（窗內無合格事件） | — | 2026-09-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 22 檔 | IPO priced week September 8 2026 first day return debut | https://www.iposcoop.com/current-year-pricings/ （IPOScoop） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（0 件符合 2+ 主題×弱基本面） | biggest stock gainers week September 7 2026 microcap 100% quantum AI | 檢查來源：Finviz、Benzinga、StockTitan、Yahoo movers（Tenon +77%、AEON +35% 皆未達門檻） | — | 2026-09-13T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 14 日掃描（0 件具完整申報日＋交易日欄位） | insider selling Form 4 September 2026 Nvidia AI executives SEC filing | 檢查來源：SEC EDGAR Form 4 檢索（一筆 2026-09-02 結果未分列交易日，不計入） | — | 2026-09-13T09:30:00+08:00 |
| speculation.equity_put_call | equity put/call 約 0.67（日／5 日均值未標示） | Cboe equity put call ratio September 2026 reading | https://www.thetrading.tools/put-call-ratio （The Trading Tools；原定 Cboe） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 $40.74bn、流出約 $751m | leveraged ETF assets under management September 2026 record single stock | https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/ （ETF Action；原定 etf.com） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval September 2026 | 檢查來源：SEC EDGAR、ETF.com 新上市 feed（窗內無合格核准或上市） | — | 2026-09-13T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比創紀錄約 62%（2026-08） | 0DTE options share SPX volume September 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august （Cboe） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.options_volume | 2026-08 月總結算量約 1.44 十億口 | OCC options volume August 2026 monthly report | https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/ （Traders Magazine；原定 OCC） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 收在約 17 以上、call skew 第 91 百分位 | fear gauge VIX hedges September 10 2026 volatility | https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html （CNBC） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 $1.42T（2026-07 月資料） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php （Current Market Valuation） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Qualcomm 對 Amazon 認股權證約 $4bn（資料中心基礎建設交易） | Qualcomm warrants Amazon 4 billion AI infrastructure deal September 2026 | https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html （CNBC） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-09-13",
  "iso_week": "2026-W37",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-03-14",
  "prior_date": "2026-09-03",
  "prior_answer": "yes",
  "flip_evidence": ["valuation.ndx_drawdown", "ai.hyperscaler_capex", "monetary.hy_oas", "structural.ai_infrastructure_debt"],
  "yes_basis": [],
  "r1_drawdown_pct": 4.21,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

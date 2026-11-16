> [DRY RUN] this report was not committed to archive.

# 2026-07-16 AI 泡沫破裂預測報告

報告日期：2026-07-16｜ISO 週次：2026-W29｜預測窗口：2026-07-16 → 2027-01-14｜前次基準：report-2026-07-13（3天前）

## 結論

**結論：no**

三條路徑目前都還遠離觸發點：NASDAQ-100 距 52 週高點回撤 3.78%，離 R1 門檻仍需再跌 ≈22.06%；hyperscaler 2026 capex 合計 ≈$700B 且仍在上修，沒有任何一家下修（`ai.hyperscaler_capex`）。HY OAS 2.72%、IG OAS 0.79% 都還很緊（`monetary.hy_oas`、`monetary.ig_oas`）。Oracle CDS 走闊與 Blue Owl 的 gate proration / breach 是真實的早期壓力，但還不足以推翻「182 天內不破裂」這個基準情境。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,502.6（2026-07-15）。252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 3.78%。R1 門檻水位 22,995.45，從最新收盤還要再跌 ≈22.06% 才會觸發（`valuation.ndx_drawdown`）。

脆弱度偏高。S&P 500 收在 7,572.4，高於 200 日均線 8.51%、高於 52 週均線 10.25%（`valuation.sp500_trend`）。Shiller CAPE 42.18、trailing P/E 32.59（`valuation.sp500_pe_cape`）。FINRA margin debt $1.416T，YoY +53.7%（2026-05 月資料，`retail.margin_debt`），已落在歷史頂部常見的 +40–50% 區間之上。

觸發條件與市況並不吻合。VIX 15.67，近 7 日 S&P 500 +1.2% 而 VIX −7.28%，沒有同漲的 crowded-optionality 訊號（`structural.vix_spx_comove`）。MOVE 從 77.77 降到 68.48（`structural.treasury_basis_trade`）。CNN Fear & Greed 46（Fear，`retail.fear_greed`），AAII Bull 36.3%／Bear 37.2%（`retail.aaii`），情緒並不亢奮。

宏觀緩衝有限。CPI YoY 3.46%（2026-06，`monetary.cpi_yoy`）、5y5y 2.21%（`monetary.t5yifr`），Fed funds 3.50–3.75%（`monetary.fed_funds`）。通膨仍高於目標，壓縮了 Fed 在急跌時大幅降息托底的空間。10Y 4.58%：ΔDGS10 −4bps、ΔDFII10 −3bps、ΔT10YIE −3bps，判讀為 `不可判（視窗不一致）`（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。10Y 期限溢價（term premium）0.7788%，trailing ≈7d +4.7bps（Kim-Wright，2026-07-10，`monetary.term_premium`）。

**判讀：** R1 距門檻還有 ≈22% 的跌幅空間，以目前的波動度與情緒，182 天內要完成 25% 回撤，需要一個外生衝擊。可能的衝擊包括 R2 指引轉向、R3 信用事件傳導，或通膨迫使利率再定價。估值與 margin debt 決定的是「一旦下跌會跌多深」，不能證明下跌已經開始。

### R2 資本支出收縮

本次證據只有合計口徑：hyperscaler 2026 capex 合計 ≈$700B 且「仍上修」（2026-05-15 報導，即最近一季財報後的指引，`ai.hyperscaler_capex`）。

- Microsoft、Alphabet、Amazon、Meta 各家的個別指引數字，本次沒有逐家取得。依該報導的上修敘述，四家方向均為上修或持平，沒有任何一家被報導下修。
- 目前下修家數為 0／4，R2 需要 2／4。
- 182 天窗口涵蓋至少兩輪季度財報。確切財報日期不在本次證據內。

供給面仍緊。伺服器 DRAM 2Q26 合約價 QoQ +58–63%（TrendForce，2026-06-02，`ai.compute_supply_demand`），代表算力需求仍在追趕供給，看不出 order digestion。AI 營收對 capex 缺口（revenue-to-capex gap）：已披露年化 AI 終端營收 ≈$72B（Anthropic ≈$47B＋OpenAI ≈$25B run-rate，2026-05-15，`ai.openai_anthropic_revenue`），年化 capex ≈$700B（分母為該報導的 hyperscaler 合計口徑，未單獨納入 Oracle 或 neocloud，`ai.revenue_capex_gap`）。缺口很大，但沒有新組件披露，不能判定在擴大還是收斂。

**判讀：** R2 目前最遠。要在窗口內成立，需要四家中有兩家從「上修」直接轉為「下修」。比較可能的路徑是 R1 大跌或融資成本急升，迫使 capex 紀律改變；在 DRAM 價格與 capex 仍在上行的情況下，接下來兩季出現兩家下修的條件尚未具備。

### R3 AI 信用事件

符合規模門檻的借款人中，CoreWeave 最具代表性（AI 算力為主業、負債遠超 50 億美元）。過去 30 日內又披露 $8.5B 的 delayed-draw term loan（2026-07-12）。同篇報導統計 Nvidia 相關的 vendor-financing 循環曝險 $24.9B（`structural.ai_infrastructure_debt`），顯示 AI infrastructure debt financing / vendor-financing loops 仍在加碼。

AI 信用定價分歧（equity-vs-credit schism）已轉向信貸端重定價：Oracle 5yr CDS ≈198bp，CDX.NA.IG ≈95bp（2026-07-10，`valuation.ai_credit_schism`）。同期 IG OAS 只有 0.79%、HY OAS 2.72%（`monetary.hy_oas`），所以走闊集中在 AI 個名，沒有擴散到整體信用。

非銀行端：私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）已出現實際事件。Blue Owl OCIC Q2 redemption-request ratio 18.8%，超過 quarterly redemption cap（5%）而發生 gate proration / breach（2026-07-02，`monetary.private_credit_liquidity`）。

本次證據沒有任何 AI 基礎設施借款人出現付款違約、covenant waiver、distressed exchange 或 going-concern 文字。repo 資金壓力（SOFR−IORB）為 −2bps，SOFR99−IORB +7bps（2026-07-14）。SRF 動用（Standing Repo Facility usage）$0.102bn（2026-07-15，`monetary.repo_stress_srf`），融資市場平穩。

**判讀：** R3 是三條路徑中動能最明確的一條：信用定價分歧開始走闊、私募信貸出現 gate proration / breach、neocloud 槓桿持續上升。但 R3 要求的是「已發生」違約或 distressed exchange，目前沒有任何借款人接近這一步。要在窗口內成立，需要 neocloud 失去融資管道或主要客戶合約出問題，同時遇上再融資時點；本次證據未揭露 2026 下半年的具體到期牆。

## 支持 yes 的證據

- [R3] Oracle 5yr CDS ≈198bp，CDX.NA.IG 約 95bp（2026-07-10）。AI 信用定價分歧（equity-vs-credit schism）開始由信貸端走闊，股價卻仍接近高點，屬後期訊號（`valuation.ai_credit_schism`）。
- [R3] CoreWeave 新增 $8.5B DDTL，Nvidia 相關循環融資曝險 $24.9B（2026-07-12）。AI infrastructure debt financing / vendor-financing loops 持續加碼，使 R3 的潛在規模與傳導面擴大（`structural.ai_infrastructure_debt`）。
- [整體] Blue Owl OCIC Q2 redemption-request ratio 18.8%，quarterly redemption cap 出現 gate proration / breach（2026-07-02）。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）已出現實際事件，可能收緊 AI 基礎設施的非銀行融資來源（`monetary.private_credit_liquidity`）。
- [R1] FINRA margin debt $1.416T、YoY +53.7%（2026-05 月資料），超過 1999／2007／2021 頂部附近的 +40–50% 區間（`retail.margin_debt`）。US 槓桿 ETF AUM ≈$198B（2026-07-10，`structural.leveraged_etf_aum`）。一旦下跌，被迫去槓桿會放大跌幅。
- [R1] Shiller CAPE 42.18、trailing P/E 32.59（2026-07-15，`valuation.sp500_pe_cape`）。S&P 500 高於 200 日均線 8.51%（`valuation.sp500_trend`）。估值與價格延伸都處於歷史極端。
- [R1] CPI YoY 3.46%（2026-06，`monetary.cpi_yoy`）、10Y 期限溢價（term premium）0.7788%（`monetary.term_premium`）。Fed 托底空間受通膨限制，利率端可能成為外生衝擊。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 3.78%（2026-07-15），距 R1 門檻 22,995.45 還要再跌 ≈22.06%（`valuation.ndx_drawdown`）。在 182 天內完成這段跌幅需要罕見級別的衝擊。
- [R2] hyperscaler 2026 capex 合計 ≈$700B 且仍上修（2026-05-15），四家中 0 家下修（`ai.hyperscaler_capex`）。伺服器 DRAM 2Q26 合約價 QoQ +58–63%（2026-06-02，`ai.compute_supply_demand`），需求端仍在追趕供給。
- [整體] HY OAS 2.72%、IG OAS 0.79%（2026-07-14，`monetary.hy_oas`、`monetary.ig_oas`）。整體信用市場沒有重定價，AI 個名走闊尚未擴散。
- [整體] repo 資金壓力（SOFR−IORB）−2bps、SRF 動用 $0.102bn（`monetary.repo_stress_srf`）。MOVE 從 77.77 降到 68.48（2026-07-15），CFTC 槓桿基金美債期貨淨部位 −7,573,044 口（`structural.treasury_basis_trade`）。融資與美債市場沒有失序跡象。
- [R1] VIX 15.67，近 7 日 S&P 500 +1.2%、VIX −7.28%，無同漲警訊（`structural.vix_spx_comove`）。CNN Fear & Greed 46（`retail.fear_greed`）、AAII Bear 37.2%（`retail.aaii`），情緒並未亢奮。RSP YTD +9.67% 優於 SPY +8.38%（`breadth.rsp_spy`），漲勢有所擴散，不是只靠少數權值股撐盤的頂部型態。

## 與前期比較

前次結論：無前次預測（report-2026-07-13 為舊格式評分報告）

本次結論：首次以 yes/no 格式作答，flip_evidence 為空陣列。舊格式評分不轉換為 yes/no。

- 與 2026-07-13 相比：10Y −4bps、HY OAS +3bps、IG OAS +1bps、VIX 從 17.16 降到 15.67、MOVE 從 77.77 降到 68.48。S&P 500 +0.76%。
- 2026-07-13 之後的新事件有 CoreWeave $8.5B DDTL 報導（2026-07-12 發布，前次基準前一日）與 GraniteShares SK hynix 2x 單一個股槓桿 ETF 上市（2026-07-14，`structural.us_single_stock_etf`）。都屬於槓桿持續累積的訊號，不是破裂事件。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `speculation.insider_form4`：SEC EDGAR 一手 Form 4 filing URL 因 egress 受限無法取得，這項篩選沒有完成，不能標為 0 件。內部人賣壓屬情緒佐證，不在 R1–R3 的傳導核心，這個缺口不會改變結論。
- `structural.zero_dte`：只找到 2026-02-28 的 0DTE 佔比（≈63%），超過四個月，不是當期快照，因此不採用。0DTE 屬短期波動放大器，無法單獨改變 182 天的判斷。

其他未披露或證據不足的項目（✗ NOT DISCLOSED，不作證據）：analyst TP decomposition、social sentiment、BofA／JPM 調查、token growth、customer concentration、hyperscaler 融資結構（capex vs FCF / 發債）兩個組件、折舊年限變動、資本週期階段兩個組件、upcoming AI IPOs、global leveraged approvals。其中 hyperscaler 融資結構與資本週期階段的缺漏影響最大，因為它們直接關係到 capex 能否持續（R2）以及表外 SPV 風險（R3）。

主要不確定性：

1. **下一輪 hyperscaler 財報（窗口內至少兩輪）**：四家各自的指引沒有逐家取得。若兩家同時轉為下修，結論會直接翻為 yes；目前證據指向上修，傾向維持 no。
2. **neocloud 再融資與 AI 信用走闊是否擴散**：Oracle CDS 已走闊、私募信貸出現 gate proration / breach。若走闊擴散到 HY OAS、CoreWeave 等借款人失去融資管道，R3 及其觸發的 R1 都會加速，將答案推向 yes。
3. **通膨與利率**：CPI 3.46%、期限溢價上升。若通膨迫使長端利率急升，高估值的 NASDAQ-100 對折現率特別敏感，R1 風險會上升。

數據說明：evidence 中有一筆 MOVE 77.77（標示 2026-07-14，以 WebSearch 補值）。但 macro artifact 的 `move_index` 狀態為 ok，77.77 是其 2026-07-13 的 prior 值、2026-07-15 最新值為 68.48。依協議以腳本為準，該搜尋值不採用。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7572.4 | FRED API (series_id=SP500) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 8.51 | FRED API (series_id=SP500) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 10.25 | FRED API (series_id=SP500) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29502.6 | FRED API (series_id=NASDAQ100) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-16T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 3.78 | FRED API (series_id=NASDAQ100) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1，家庭股票配置 %） | 45.76080873390133（≈45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-16T09:30:00+08:00 |
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
| monetary.walcl | WALCL latest | 6,735,609（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-08 | 2026-07-16T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,970,516（€5.97T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-10 | 2026-07-16T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,395,509（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-16T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.67 | FRED API (series_id=VIXCLS) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（7 日窗，base 2026-07-08） | 15.67 | fetch_macro.py derived block (VIXCLS/SP500) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | -7.28 | fetch_macro.py derived block (VIXCLS/SP500) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | 1.2 | fetch_macro.py derived block (VIXCLS/SP500) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 1995.0783（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-01 | 2026-07-16T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位） | -7,573,044 口 | CFTC TFF (cftc_lev_funds) | 2026-07-07 | 2026-07-16T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 68.48 | Yahoo chart ^MOVE (move_index) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2405.1（十億美元，tri-party transaction volume） | OFR STFM REPO-TRIV1_TV_TOT-P (ofr_repo) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation｜Mag 7 weighted P/E and AI leader P/S | MarketXLS 搜尋 | ✓ SEARCH-VERIFIED（資料日 2026-05-15，非當週） |
| valuation.analyst_tp_decomposition | Valuation｜Analyst TP upgrade decomposition | 賣方研報 [primary: SEARCH]，90d＋同季 | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation｜S&P 500 price-trend deviation | fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation｜NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation｜AI 信用定價分歧 | 信用市場 [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst 搜尋 | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth｜Top-10 concentration in S&P 500 | S&P DJI dashboard 搜尋 | ✓ SEARCH-VERIFIED（資料日 2026-04-30） |
| breadth.advance_decline | Breadth｜Advance/decline ratio, new high/low ratio | McClellan 搜尋 | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment｜CNN Fear & Greed Index | cnn.com [primary: SEARCH]，MacroMicro 鏡像 | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment｜Margin Debt: FINRA monthly data | FINRA／Advisor Perspectives 搜尋（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment｜Social sentiment proxies | WSB／cashtag 搜尋，7d | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment｜Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment｜NAAIM Exposure Index | naaim／ycharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | Institutional Sentiment｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查搜尋 | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | fetch_macro.py（DFEDTARU ok、DFEDTARL ok） | ✓ API |
| monetary.hy_oas | Monetary & Credit｜High Yield OAS | fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit｜Investment Grade OAS | fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit｜10Y Treasury yield | fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit｜10Y Treasury real yield / TIPS | fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit｜10Y breakeven inflation rate | fetch_macro.py（T10YIE，FRED 直接） | ✓ API |
| monetary.wti | Monetary & Credit｜WTI crude oil price | fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit｜CPI YoY: FRED series CPIAUCSL | fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit｜5y5y forward inflation expectation | fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series | fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） | ✓ API |
| monetary.treasury_auctions | Monetary & Credit｜美債標售需求（auction tail / bid-to-cover） | Reuters／TradingView [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit｜Fed funds rate path expectations | CME／MacroMicro [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit｜Fed balance sheet: FRED series WALCL | fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit｜Global central bank liquidity cross-check | fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | Monetary & Credit｜PBoC aggregate financing | Bloomberg 搜尋 | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]，30d | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI Fundamentals｜Hyperscaler capex guidance | 季報搜尋（stock-of-state，carry 最近一季） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals｜AI token volume growth rate | Anthropic／OpenAI／Google 搜尋 | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals｜OpenAI / Anthropic annualized revenue | Epoch／The Information 搜尋 | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals｜Hyperscaler AI customer concentration | 財報電話 [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報 quarterly_state＋30d event_scan [primary: SEARCH]；兩組件皆搜尋完成無披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 [primary: SEARCH]（carry 各組件最近披露） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals｜GPU / 伺服器折舊年限變動 | 10-K／10-Q [primary: SEARCH]，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals｜資本週期階段（capital cycle stage） | 供需增速 quarterly_state＋30d event_scan [primary: SEARCH]；兩組件皆搜尋完成無披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior｜Search for past 7 days: AI rename / SPAC | 7d 搜尋 | ✓ SEARCH-VERIFIED（1 件：General Fusion SPAC） |
| speculation.ipo_heat | Speculative Behavior｜IPO market heat | stockanalysis／Axios 搜尋 | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior｜Microcap thematic moonshots | Finviz／Benzinga／StockTitan movers [primary: SEARCH] | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior｜Upcoming AI IPOs | S-1／具名報導搜尋，30d | ✗ NOT DISCLOSED |
| speculation.insider_form4 | Speculative Behavior｜Insider selling at AI / market-leadership companies | SEC EDGAR [primary: SEC EDGAR]；EDGAR egress 受限，一手 filing URL 無法取得 | ⛔ FETCH FAILED |
| speculation.equity_put_call | Speculative Behavior｜Cboe equity-only put/call ratio | Cboe／ycharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage｜US leveraged ETF AUM | etf.com／cryptobriefing [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage｜US single-stock leveraged ETF approvals | SEC／ETF.com 搜尋，30d | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | Structural Leverage｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA 搜尋，7d | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage｜0DTE option volume | Cboe 搜尋；唯一結果資料日 2026-02-28，無當期快照 | ⛔ FETCH FAILED |
| structural.options_volume | Structural Leverage｜Options total volume: OCC monthly | theocc.com 搜尋 | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage｜Cross-asset derivatives / correlation checks | Cboe／Saxo 搜尋 | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage｜VIX / S&P 500 co-movement | fetch_macro.py（VIXCLS ok、vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage｜Cross-reference only: FINRA margin debt | 交叉引用 retail.margin_debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]，30d | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage｜Bank loans to nondepository financial institutions | fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage｜美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok；aggregation any） | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.59 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.18 | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E ≈40 trailing | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026 （MarketXLS） | 2026-05-15 | 2026-07-16T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS ≈198bp vs CDX.NA.IG ≈95bp | Oracle CoreWeave CDS spread vs CDX IG July 2026 | https://www.investing.com/analysis/oracle-and-coreweave-credit-default-swap-spreads-widening-omen-or-jitters-200670506 （Investing.com） | 2026-07-10 | 2026-07-16T09:30:00+08:00 |
| breadth.rsp_spy | RSP +9.67% vs SPY +8.38% YTD | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/26/forget-the-magnificent-seven-this-equal-weight-sp-fund-beats-the-mega-caps-for-just-0-20/ （24/7 Wall St.） | 2026-06-26 | 2026-07-16T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 35.59% | S&P 500 top 10 concentration percent 2026 | https://www.spglobal.com/spdji/en/documents/performance-reports/dashboard-sp-500-factor.pdf （S&P DJI） | 2026-04-30 | 2026-07-16T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 2008／下跌 2749 | NYSE advance decline breadth July 2026 | https://www.mcoscillator.com/market_breadth_data/ （McClellan） | 2026-07-13 | 2026-07-16T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 46（Fear） | CNN Fear and Greed Index today July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed （MacroMicro；原定 cnn.com） | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-05 月資料）$1.416T、YoY +53.7% | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives；原定 FINRA） | 2026-05-31 | 2026-07-16T09:30:00+08:00 |
| retail.aaii | AAII Bull 36.3%／Bear 37.2% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-09 | 2026-07-16T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 82.95 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number （YCharts；原定 naaim.org） | 2026-07-08 | 2026-07-16T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y bid-to-cover 2.565、30Y bid-to-cover 2.44 | US Treasury 10Y 30Y auction July 2026 bid to cover | https://www.tradingview.com/news/macenews:30b090608094b:0-us-treasury-30-year-bond-auction-high-yield-5-058-bid-cover-ratio-at-2-44/ （TradingView／MNI） | 2026-07-09 | 2026-07-16T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 會議 ≈70% 持平 | CME FedWatch rate hold probability July 2026 | https://en.macromicro.me/series/78109/probability-fed-rate-325-350-2026 （MacroMicro；原定 CME） | 2026-07-08 | 2026-07-16T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance （Bloomberg） | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio 18.8%，quarterly redemption cap gate proration / breach | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://pitchbook.com/news/articles/private-credit-bdc-redemption-requests-likely-to-peak-in-q2-2026-bofa （PitchBook） | 2026-07-02 | 2026-07-16T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計 ≈$700B、仍上修（最近一季財報指引） | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html （Yahoo Finance） | 2026-05-15 | 2026-07-16T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic ≈$47B／OpenAI ≈$25B run-rate | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-05-15 | 2026-07-16T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 2Q26 合約價 +58–63% QoQ | DRAM HBM contract price 2Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260602-13074.html （TrendForce） | 2026-06-02 | 2026-07-16T09:30:00+08:00 |
| ai.revenue_capex_gap | 分母：年化 capex ≈$700B（hyperscaler 合計口徑）；分子取 ai.openai_anthropic_revenue | AI revenue to capex gap 2026 | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html （Yahoo Finance） | 2026-05-15 | 2026-07-16T09:30:00+08:00 |
| speculation.ai_rename_spac | General Fusion（GFUZ）SPAC 上市 | AI rename SPAC July 2026 General Fusion | https://www.morningstar.com/news/pr-newswire/20260710ln02448/ （PR Newswire via Morningstar） | 2026-07-10 | 2026-07-16T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD ≈200 檔 IPO、募資 $141.2B | US IPO market 2026 YTD count proceeds | https://www.axios.com/2026/07/13/us-ipo-market-record-proceeds （Axios） | 2026-07-13 | 2026-07-16T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot 0 件 | microcap 100% single day quantum AI moonshot July 2026 | Finviz／Benzinga／StockTitan movers screener | 2026-07-16 | 2026-07-16T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.62（日讀數） | Cboe equity put call ratio July 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio （YCharts；原定 Cboe） | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM ≈$198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing；原定 etf.com） | 2026-07-10 | 2026-07-16T09:30:00+08:00 |
| structural.us_single_stock_etf | GraniteShares SK hynix SKUU／SKDD 2x 上市 | single-stock leveraged ETF launch July 2026 SK Hynix Tradr | https://www.globenewswire.com/news-release/2026/07/14/3326857/0/en/GraniteShares-Launches-the-First-U-S-Listed-Leveraged-ETFs-on-SK-hynix.html （GlobeNewswire） | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月 1,603,491,559 口、+45% YoY | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-07-16T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 期限結構 contango、Cboe SKEW 149.6 | VIX term structure SKEW July 2026 | https://www.home.saxo/content/articles/options/options-brief---calm-on-top-nervous-underneath---1-july-2026-01072026 （Saxo） | 2026-07-01 | 2026-07-16T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-05 月資料）$1.416T、YoY +53.7%（交叉引用） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives） | 2026-05-31 | 2026-07-16T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $8.5B DDTL；Nvidia 循環融資曝險 $24.9B | AI data center debt CoreWeave Nvidia circular financing July 2026 | https://www.techtimes.com/articles/320239/20260712/nvidia-circular-financing-249b-coreweave-debt-puts-pension-funds-risk.htm （Tech Times） | 2026-07-12 | 2026-07-16T09:30:00+08:00 |

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

> [DRY RUN] this report was not committed to archive.

# 2026-10-18 AI 泡沫破裂預測報告
報告日期：2026-10-18｜ISO 週次：2026-W42｜預測窗口：2026-10-18 → 2027-04-18｜前次基準：report-2026-09-13（35天前）

## 結論

**結論：yes**

決定性路徑是 R3 → R1 的信用傳導：CoreWeave 5Y CDS 於 2026-10-15 創 1,194.5 bps 紀錄（`valuation.ai_credit_schism`），同時 HY OAS 自前次基準以來走闊 58 bps 至 3.23%（`monetary.hy_oas`），而 Fed 目標區間反而上調 25 bps 至 3.75%–4.00%（`monetary.fed_funds`），政策緩衝空間收窄。前次 yes 的判斷沒有被任何新證據削弱，反而在信用與利率端得到強化，因此維持 yes。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,935.59（2026-10-15），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 4.13%（`valuation.ndx_drawdown`）。R1 門檻水位為 23,418.52，自最新收盤須再下跌 6,517.07 點、約 21.77% 才觸及。高點僅在 9 天前創下，指數目前處於高位回落初段，而非已進入深度回撤。

價格面仍偏延伸：S&P 500 於 2026-10-16 收 7,659.44，高於 200 日均線 5.34%、高於 52 週均線 6.78%，自前次基準以來僅 +0.03%（`valuation.sp500_trend`）；Shiller CAPE 約 40.54（2026-10-16，`valuation.sp500_pe_cape`）。情緒端已急轉：CNN Fear & Greed 約 18、極度恐懼（2026-10-16，`retail.fear_greed`），2026-10-16 上漲對下跌家數約 29 對 71（`breadth.advance_decline`），MOVE 由 82.21 升至 101.1（`structural.treasury_basis_trade`）。VIX 在 2026-10-08 → 2026-10-15 的 7 日窗內 +6.81%、S&P 500 −0.27%，未構成同漲警戒（`structural.vix_spx_comove`）。

**判讀：** R1 距門檻仍遠（尚需約 21.77% 的跌幅），但高估值（CAPE 約 40.54）與迅速惡化的情緒、債市波動同時存在，代表一旦信用事件或利率衝擊落地，下跌空間大；窗口內推過門檻需要 R3 型信用衝擊或利率再度急升引發的強制去槓桿。

### R2 資本支出收縮

本次可得的 hyperscaler capex 證據為 2026-07-28 CNBC 報導（Q2 財報季）：四大 hyperscaler 2026 年 capex 合計約 725（十億美元級），且市場在 Alphabet 財報後已對 capex 加強審視（`ai.hyperscaler_capex`）。Microsoft、Alphabet、Amazon、Meta 個別的最新正式指引數值與相對前次指引的方向，本次證據未逐家揭露；以合計值與報導脈絡判讀，目前四家中下修家數為 0，均屬沿用 Q2 財報季的指引（stock-of-state carry-forward）。下一輪（Q3）財報季落在窗口內，但具體日期本次證據未取得。

需求側：Anthropic 年化 run-rate 約 65（十億美元級，2026-08-17，`ai.openai_anthropic_revenue`），並傳出目標 11 月中上市（2026-10-05，`speculation.upcoming_ai_ipos`）。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 65（僅 Anthropic）vs 年化 capex 約 725（分母：top-4 hyperscaler；Oracle 與 neocloud 本次無可用組件），分子僅覆蓋單一公司，無法判斷缺口擴大或收斂（`ai.revenue_capex_gap`）。供給端價格：H100 隨選中位租金約 4.20（美元／小時，2026-10-07，`ai.compute_supply_demand`），本次無配對的利用率或庫存證據，不能單獨解讀為產能過剩。

**判讀：** R2 目前離觸發最遠——0 家下修，且需在窗口內出現至少兩家下修。可推動 R2 的情境是 R1 回撤或 R3 信用事件迫使管理層在 Q3 或 Q4 財報中收斂指引；單靠目前證據看不到這條路徑已啟動。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）出現實質走闊：2026-10-15 報導 CoreWeave 5Y CDS 達 1,194.5 bps 紀錄，報導標題為「AI credit fears push tech default insurance to record highs」（`valuation.ai_credit_schism`）。CoreWeave 是以 AI 算力為主業的借款人；其負債規模本次證據未載明，但它是 R3 規模門檻的最主要候選。AI infrastructure debt financing / vendor-financing loops：Lambda 於 2026-10-01 披露約 1 十億美元的 GPU 擔保融資（`structural.ai_infrastructure_debt`），顯示 neocloud 仍靠以 GPU 為擔保的債務擴張。

宏觀信用環境同步轉緊：HY OAS 3.23%（2026-10-15，較 2026-09-11 +58 bps，`monetary.hy_oas`），IG OAS 0.84%（+4 bps，`monetary.ig_oas`）；10Y 殖利率 5.10%、實質殖利率 2.78%（`monetary.dgs10`、`monetary.dfii10`）抬高再融資成本；IPO 市場兩週內第 4 檔撤件或延後（2026-10-16，`speculation.ipo_heat`），股權融資窗口收窄。未見違約、寬限期付款逾期、covenant waiver 或 distressed exchange 的報導。

**判讀：** 約 1,195 bps 的 5Y CDS 已是 distressed 區間的定價，信用市場顯示 R3 已在進行中，而非僅屬估值疑慮；R3 成立仍需實際破產、逾寬限期違約或 distressed exchange。窗口內推過門檻的觸發因素包括：股權融資窗口關閉（IPO 撤件）、利率上升下的再融資、以及任何大客戶承諾減少。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 於 2026-10-15 創 1,194.5 bps 紀錄，AI 信用定價分歧已由「信用與非 AI 無差」轉為信用端急速重定價，屬後期訊號（`valuation.ai_credit_schism`）。
- [整體] 信用環境轉緊與政策反向：HY OAS 自 2.65% 升至 3.23%（2026-10-15，+58 bps，`monetary.hy_oas`），Fed 目標區間上調至 3.75%–4.00%（2026-10-17，`monetary.fed_funds`），CPI YoY 3.72%（2026-09 月資料，`monetary.cpi_yoy`）限制降息托底空間。
- [R3] 股權與債務融資窗口同時收窄：兩週內第 4 檔 IPO 撤件或延後（2026-10-16，`speculation.ipo_heat`），10Y 殖利率 5.10%、自前次基準以來 +14 bps（2026-10-15，`monetary.dgs10`），neocloud 仍持續以 GPU 擔保舉債（Lambda 約 1 十億美元，2026-10-01，`structural.ai_infrastructure_debt`）。
- [R1] 估值極端且情緒急轉：Shiller CAPE 約 40.54（2026-10-16，`valuation.sp500_pe_cape`），Fear & Greed 約 18 極度恐懼（2026-10-16，`retail.fear_greed`），上漲對下跌家數約 29 對 71（2026-10-16，`breadth.advance_decline`），BofA 10 月調查科技股淨加碼約 37、為 2020 年 8 月以來最高（2026-10-13，`institutional.bofa_jpm_survey`）——擁擠部位遇上恐慌情緒，下跌時易放大。
- [整體] 債市波動與槓桿上升：MOVE 自 82.21 升至 101.1（2026-10-16），槓桿基金美債期貨淨空單 −6,883,343 口、4 週再增 309,307 口（2026-10-13），美債基差交易槓桿（Treasury basis-trade leverage）擴張中（`structural.treasury_basis_trade`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.13%，高點僅在 2026-10-06，距 R1 門檻 23,418.52 仍需約 21.77% 跌幅（`valuation.ndx_drawdown`）；S&P 500 仍高於 200 日均線 5.34%（2026-10-16，`valuation.sp500_trend`）。
- [R2] 四大 hyperscaler 2026 年 capex 合計約 725，本次無任何一家下修的證據（2026-07-28，`ai.hyperscaler_capex`）；需求側 Anthropic run-rate 約 65 且計畫 11 月中上市（`ai.openai_anthropic_revenue`、`speculation.upcoming_ai_ipos`）。
- [整體] 融資管線未失序：SOFR−IORB −1.0 bps、SOFR99−IORB 7.0 bps（2026-10-15），SRF 動用 0.0（2026-10-16，`monetary.repo_stress_srf`）；10Y 標售 bid-to-cover 約 2.77、需求強勁（2026-10-07，`monetary.treasury_auctions`）；IG OAS 僅 0.84%（`monetary.ig_oas`）。
- [整體] 基準率：任意 182 天窗口內 R1–R3 皆屬少見事件；VIX 7 日窗未出現與股價同漲的擁擠選擇權警戒（2026-10-15，`structural.vix_spx_comove`）。
- [R3] 本次證據中未見任何 AI 算力借款人的實際違約、逾寬限期付款或 distressed exchange；Lambda 仍能取得約 1 十億美元新融資（2026-10-01，`structural.ai_infrastructure_debt`）。

## 與前期比較

前次結論：yes（report-2026-09-13）

本次結論：維持

- NASDAQ-100 回撤由前次的 4.21% 變為本次 4.13%，期間創新高後回落（`valuation.ndx_drawdown`）；R1 距離幾乎不變，不構成改判理由。
- 信用端惡化：HY OAS +58 bps 至 3.23%（`monetary.hy_oas`），CoreWeave 5Y CDS 於 2026-10-15 創紀錄（`valuation.ai_credit_schism`）——強化 R3 路徑，與前次 yes 方向一致。
- 政策與利率：Fed 目標區間上調 25 bps（`monetary.fed_funds`），10Y 實質殖利率自前次基準以來 +18 bps（`monetary.dfii10`），托底空間縮小，方向支持 yes。
- 情緒由擁擠轉恐慌：Fear & Greed 約 18（`retail.fear_greed`），IPO 撤件增加（`speculation.ipo_heat`）；屬傳導加速訊號。
- 支持 no 的新證據有限：repo 資金壓力（SOFR−IORB）仍平穩、SRF 動用為 0（`monetary.repo_stress_srf`），美債標售需求穩健（`monetary.treasury_auctions`）；這些顯示融資管線未失序，但不足以推翻信用端重定價，依翻轉紀律不改判。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

未揭露（✗ NOT DISCLOSED）的 optional 來源：`valuation.analyst_tp_decomposition`、`retail.social_sentiment`、`retail.naaim`、`monetary.fedwatch`、`monetary.private_credit_liquidity`、`ai.token_growth`、`ai.customer_concentration_rpo`、`ai.hyperscaler_financing_mix`（quarterly_state 可得：2026 年 hyperscaler 發債預估約 190，2026-02-02 背景值；30 日 event_scan 無披露）、`ai.depreciation_life`、`ai.capital_cycle`（增速證據不足，本次不判定週期階段）、`speculation.equity_put_call`、`structural.global_leveraged_approvals`。其中私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）與 hyperscaler 融資結構事件掃描若有披露，可能強化 R3；目前缺漏不改變答案。

資料品質註記：
- `structural.treasury_basis_trade`：harness 檢索紀錄稱腳本三個區塊 fetch_failed，但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 皆為 `status: ok`；依 artifact 判定為 ✓ API 並使用其數值，WebSearch 補充路徑無窗內披露。
- `ai.hyperscaler_capex` 只取得四家合計約 725，未取得逐家指引與方向；R2 下修家數 0 是根據 Q2 財報季的 carry-forward 推得。
- `breadth.rsp_spy`（2026-07-18）與 `breadth.top10_concentration`（2026-07-31）為較舊的快照，`valuation.mag7_multiples` 只有 MSFT 前瞻本益比 24.5（2026-09-24），未取得 Mag 7 加權值；均不影響答案。
- 10Y Δ 分解：ΔDGS10 +14 bps、ΔDFII10 +18 bps、ΔT10YIE −1 bps，判讀為不可判（視窗不一致）。

主要不確定性：
1. CoreWeave 等 AI 算力借款人的實際債務規模與到期結構本次未取得；若確認未達 50 億美元門檻或近期無大額到期，R3 路徑減弱，推向 no。
2. Q3 hyperscaler 財報（窗口內）：若四家維持或上修 capex，R2 遠離且 AI 需求敘事獲支撐，推向 no；若出現下修，R2 與 R1 同時加速，推向 yes。
3. Anthropic 上市（目標 11 月中）：順利定價可重開股權融資窗口，推向 no；延後或折價則確認風險偏好退潮，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7659.44 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 5.34 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 6.78 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29935.59 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 4.13 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026-Q2 季資料，%） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（%） | 4.0 | FRED API (series_id=DFEDTARU) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（%） | 3.75 | FRED API (series_id=DFEDTARL) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 3.23 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 58.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.84 | FRED API (series_id=BAMLC0A0CM) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 5.1 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | 14.0 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.78 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | 18.0 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.35 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（美元／桶） | 101.91 | FRED API (series_id=DCOILWTICO) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料，%） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.33 | FRED API (series_id=T5YIFR) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 1.0729 | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.89 | FRED API (series_id=SOFR) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.97 | FRED API (series_id=SOFR99) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.9 | FRED API (series_id=IORB) | 2026-10-18 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用 transaction volume，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6755639.0（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5943911.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6250253.0（¥625.03T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.46 | FRED API (series_id=VIXCLS) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（7 日窗，base 2026-10-08） | 16.46 | FRED API derived block vix_spx_comove (VIXCLS + SP500) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 6.81 | FRED API derived block vix_spx_comove (VIXCLS + SP500) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | −0.27 | FRED API derived block vix_spx_comove (VIXCLS + SP500) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2097.9713（$2.10T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六個 CBT 美債期貨合計，口） | -6883343 | CFTC TFF futures-only (CFTC) | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -309307 | CFTC TFF futures-only (CFTC) | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 101.1 | Yahoo Finance chart API (^MOVE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index delta_abs | 18.89 | Yahoo Finance chart API (^MOVE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2264.1 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED（僅 CAPE；trailing P/E 未取得） |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch 財經摘要 | ✓ SEARCH-VERIFIED（僅 MSFT 前瞻 P/E） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch 賣方 TP 調升（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend 區塊（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown 區塊（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch 14 日 AI 信用定價 | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ✓ SEARCH-VERIFIED（2026-07-18 快照） |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED（2026-07-31 快照） |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch（月度 stock-of-state，2026-08 月資料） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch Reddit / X | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py FRED BOGZ1FL153064486Q | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch（primary: SEARCH） | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✓ SEARCH-VERIFIED（BofA 10 月；JPM 未披露） |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py FRED API | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py FRED API | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py FRED API | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py FRED API | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py FRED API | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py FRED API（FRED 直接取得，非 derived） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py FRED API | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py FRED API（yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py FRED API | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py FRED API | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py FRED API＋repo_stress 區塊 | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch 14 日標售回顧 | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch CME FedWatch | ✗ NOT DISCLOSED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py FRED API | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py FRED API | ✓ API（ECBASSETSW ok；JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch 30 日 BDC / interval fund 披露 | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state，Q2 財報季 carry-forward） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED（Anthropic；OpenAI 未披露） |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch GPU 租價 / HBM | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch：quarterly_state 季頻 carry；event_scan 30 日事件掃描 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | 組合既有 bullets（Anthropic run-rate；top-4 capex） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動（depreciation useful-life change） | WebSearch 30 日 10-K / 10-Q 掃描 | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch：quarterly_state 增速對比；event_scan 30 日進出場事件 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch＋SEC EDGAR 8-K 7 日掃描 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch IPOX 週報 | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch movers 掃描 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch 30 日 | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 14 日掃描 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✗ NOT DISCLOSED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED（單一個股槓桿 ETF 合計；個別 ticker 未取得） |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR ETF 申報＋ETF.com 30 日掃描 | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch KRX / TWSE / JPX / ESMA 7 日 | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | Cboe insights WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | OCC 月報 WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch（VIX / SKEW） | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py FRED VIXCLS＋vix_spx_comove 區塊 | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（cross-check only） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch 30 日 | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py FRED API | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds / move_index / ofr_repo（皆 ok）；WebSearch 補充無窗內披露 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.54 | Shiller PE CAPE ratio current October 2026 multpl | https://www.multpl.com/shiller-pe （multpl；原定來源 multpl.com / gurufocus.com） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.mag7_multiples | MSFT 前瞻本益比 24.5 | Magnificent 7 forward P/E valuation October 2026 | https://articlegateway.com/?p=146 （原定來源：Mag 7 加權 P/E） | 2026-09-24 | 2026-10-18T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 紀錄 1,194.5 bps | AI credit fears tech default insurance record highs October 2026 | https://www.businessday.co.za/world/international-companies/2026-10-15-ai-credit-fears-push-tech-default-insurance-to-record-highs/ （BusinessDay） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 報酬約 12.08 | RSP equal weight vs SPY YTD performance 2026 | https://pro.thestreet.com/market-commentary/rsp-vs-spy-does-diversification-require-equal-weight （TheStreet Pro） | 2026-07-18 | 2026-10-18T09:30:00+08:00 |
| breadth.top10_concentration | 前十大集中度約 38.9 | S&P 500 top 10 concentration percent record 2026 | https://walnutinvest.com/stats/market-concentration-statistics （Walnut） | 2026-07-31 | 2026-10-18T09:30:00+08:00 |
| breadth.advance_decline | 上漲家數約 29 對下跌 71 | market breadth October 16 2026 percent above 200-day advance decline | https://www.thetrading.tools/market-breadth （thetrading.tools） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 極度恐懼約 18 | CNN Fear and Greed Index October 16 2026 extreme fear | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ （finhacker；原定來源 CNN） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-08 月資料）約 1.45 兆美元 | FINRA margin debt August 2026 year over year | https://www.thetrading.tools/margin-debt （原定來源 FINRA） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.7（週至 2026-10-14） | AAII sentiment survey week ending October 14 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA 10 月 FMS：科技股淨加碼約 37，2020 年 8 月以來最高 | BofA October 2026 fund manager survey tech overweight cash | https://www.bloomberg.com/news/articles/2026-10-13/bofa-poll-shows-investors-most-exposed-to-tech-stocks-since-2020 （Bloomberg） | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.77 | Treasury 10-year note auction October 7 2026 bid-to-cover | https://www.rttnews.com/3697286/ten-year-note-auction-attracts-strong-demand.aspx （RTTNews） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate social financing 2026 total | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm （SteelOrbis） | 2026-08-15 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 725（Q2 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65 | OpenAI Anthropic annualized revenue run rate 2026 | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選中位租金約 4.20 | GPU rental price index HBM DRAM contract price October 2026 | https://uvik.net/blog/gpu-price-index/ （Uvik） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 2026 年 hyperscaler 發債預估約 190 | hyperscaler bond issuance 2026 capex versus free cash flow | https://www.twentyfouram.com/insights/oracle-clears-the-supply-cloud-with-record-demand （TwentyFour AM） | 2026-02-02 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic run-rate 約 65（分母取 ai.hyperscaler_capex top-4 約 725） | AI revenue versus capex gap 2026 annualized | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement October 2026 | 檢查來源：SEC EDGAR 8-K、SPACInsider、Boardroom Alpha | — | 2026-10-18T09:30:00+08:00 |
| speculation.ipo_heat | 兩週內第 4 檔 IPO 撤件或延後 | IPO market October 16 2026 pulled postponed Firmus Oura | https://www.ipox.com/ipox/the-ipox-update-10162026 （IPOX） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（0 件符合 2+ 主題×弱基本面） | biggest stock gainers week October 12-16 2026 microcap 100% | 檢查來源：Tapeboard movers archive、Financial Modeling Prep daily gainers、Yahoo movers（PFAI 10/7 +116.7% 落在窗外） | — | 2026-10-18T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 11 月中上市 | Anthropic IPO October 2026 timing valuation S-1 | https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market （CNN） | 2026-10-05 | 2026-10-18T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件合格） | insider selling Form 4 October 2026 Nvidia AI executives SEC | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表（10/9 有申報但無 filing-level 細節） | — | 2026-10-18T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.04 | single stock leveraged ETF assets October 2026 weekly flows | https://www.etfaction.com/single-stock-traders-pile-into-tsll-and-intw-as-levered-flows-surge/ （ETF Action；原定來源 etf.com / ETFGI） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval October 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed | — | 2026-10-18T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 月度 ADV 創紀錄約 3.4 百萬口（2026-09 月資料） | Cboe September 2026 derivatives volume 0DTE SPX record | https://www.cboe.com/insights/posts/market-metrics-that-matter-derivatives-september-2026-volume-highlights （Cboe） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.options_volume | 9 月總結算量約 1,486,062,415 口（2026-09 月資料） | OCC September 2026 monthly volume data | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report （OCC） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 約 14.84、SKEW 154.34 | VIX term structure SKEW October 2026 options brief | https://www.home.saxo/content/articles/options/the-middle-got-cheaper-the-edge-did-not---options-brief---12-october-2026-12102026 （Saxo） | 2026-10-12 | 2026-10-18T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 1.45 兆美元（2026-08 月資料） | margin debt to market cap August 2026 | https://www.thetrading.tools/margin-debt （cross-check only） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Lambda GPU 擔保融資約 1 十億美元 | AI data center debt Lambda CoreWeave financing October 2026 | https://valueaddvc.com/pulse/ai-data-center-debt-financing-risk-2026 （ValueAdd VC） | 2026-10-01 | 2026-10-18T09:30:00+08:00 |

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

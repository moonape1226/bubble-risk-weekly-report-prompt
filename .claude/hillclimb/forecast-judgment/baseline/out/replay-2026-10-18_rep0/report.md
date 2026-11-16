> [DRY RUN] this report was not committed to archive.

# 2026-10-18 AI 泡沫破裂預測報告

報告日期：2026-10-18｜ISO 週次：2026-W42｜預測窗口：2026-10-18 → 2027-04-18｜前次基準：report-2026-09-13（35天前）

## 結論

**結論：no**

三條路徑都還離觸發有一段距離：NASDAQ-100 距 52 週高點回撤 4.13%，要觸發 R1 還需再跌約 21.77%；可得證據中沒有任何 hyperscaler 下修 capex 指引，也沒有 AI 算力借款人違約。決定方向的是 R3 的壓力訊號（CoreWeave 5Y CDS 創紀錄 1,194.5 bps）與 Fed 升息至 3.75–4.00%：兩者都讓風險升高，但在 182 天內都還不足以壓過不觸發的基準狀態。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,935.59（2026-10-15），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 4.13%（`valuation.ndx_drawdown`）。R1 門檻水位為 23,418.52，自最新收盤須再下跌約 21.77% 才觸及。同期 S&P 500 於 2026-10-16 收 7,659.44，仍高於 200 日均線 5.34%、高於 52 週均線 6.78%（`valuation.sp500_trend`），趨勢延伸程度溫和。估值面 Shiller CAPE 約 40.54（2026-10-16，`valuation.sp500_pe_cape`），處於極端高位，代表一旦下跌空間大。情緒面已轉為恐懼：CNN Fear & Greed 約 18（極度恐懼，2026-10-16，`retail.fear_greed`），2026-10-16 上漲家數約 29、下跌約 71（`breadth.advance_decline`），MOVE 由 82.21 升至 101.1（`structural.treasury_basis_trade`）。另一方面，機構持倉仍擁擠：BofA 10 月 FMS 科技股淨加碼約 37%，為 2020 年 8 月以來最高（2026-10-13，`institutional.bofa_jpm_survey`）。VIX 為 16.46（2026-10-15），7 日窗口（2026-10-08 → 2026-10-15）VIX +6.81%、S&P 500 −0.27%，未出現同漲的 crowded-optionality 讀數（`structural.vix_spx_comove`）。

**判讀：** 高估值加上擁擠持倉，代表回撤若發生幅度會大；但要在窗口內觸發 R1，需在現有 4.13% 回撤上再跌約 21.77%，通常要靠信用事件（R3）或 capex 指引下修（R2）帶動的被迫去槓桿才會發生，目前尚未看到這類傳導。

### R2 資本支出收縮

- Microsoft：本次證據未取得逐家正式指引數字，相較前次指引的方向無法核實。
- Alphabet：同上，未取得逐家指引數字與方向。
- Amazon：同上，未取得逐家指引數字與方向。
- Meta：同上，未取得逐家指引數字與方向。

可得的彙總：四大 hyperscaler 2026 capex 合計約 725（CNBC 彙總，2026-07-28，Q2 財報季；之後尚無新一季財報，沿用為 current，`ai.hyperscaler_capex`）。本次證據中未見任何一家下修指引的報導，因此以可得證據計，已下修家數為 0，但逐家方向未能逐一核實。需求側的同期訊號：H100 隨選中位租金約 4.20（2026-10-07，`ai.compute_supply_demand`），單憑價格無法判斷利用率是否轉弱。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收（分子僅 Anthropic run-rate 約 65，2026-08-17）對 2026 capex 約 725（分母：top-4，不含 Oracle），分子約為分母的一成；因沒有同口徑的前值，本次無法判定缺口是擴大還是收斂（`ai.revenue_capex_gap`）。具體下次財報日不在本次證據內，但 Q3 財報季（10 月下旬）與次一季財報（通常含次年度指引）都落在窗口內。

**判讀：** R2 目前離觸發最遠，0 家下修，而 R2 需要四家中至少兩家下修。窗口內有兩次財報季，能推過門檻的情境是：R1 或 R3 先出現，促使管理層在次年度指引中轉為保守，或 AI 營收對 capex 缺口遲遲沒有收斂、引發股東壓力。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）已明顯轉向信貸端重定價：CoreWeave 5Y CDS 創紀錄達 1,194.5 bps，同一報導指 AI 信用疑慮把科技業違約保險推升到紀錄高位（2026-10-15，`valuation.ai_credit_schism`）。CoreWeave 是最接近 R3 規模門檻的 AI 算力借款人。融資管道仍然開著：Lambda 於 2026-10-01 前後取得約 10 億美元 GPU 擔保融資（`structural.ai_infrastructure_debt`），屬 AI infrastructure debt financing / vendor-financing loops 持續擴張而非斷流。整體信用市場同步走闊但仍不算緊：HY OAS 由 2.65% 升至 3.23%（+58 bps，2026-10-15，`monetary.hy_oas`），IG OAS 0.84%（+4 bps，`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 −1 bp、SOFR99−IORB 為 +7 bps，SRF 動用（Standing Repo Facility usage）為 0（`monetary.repo_stress_srf`），沒有融資市場失序。本次證據未包含 CoreWeave 等借款人的到期時程、契約豁免、評等動作或付款違約。

**判讀：** R3 是三條路徑中壓力上升最快的一條。CDS 逼近 1,200 bps 代表市場對其違約風險的定價已大幅升高，但 R3 要求窗口內實際發生破產申請、超過寬限期的違約或 distressed exchange。在融資管道仍開、repo 平穩的情況下，近期觸發仍需要再融資失敗或大客戶合約變故這類催化劑；一旦發生，會經由 R1 擴散。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 達紀錄 1,194.5 bps（2026-10-15），AI 信用疑慮把科技業違約保險推到紀錄高位，AI 信用定價分歧（equity-vs-credit schism）已轉為信貸端先行重定價（`valuation.ai_credit_schism`）。
- [整體] 貨幣條件收緊：Fed funds 目標區間由 3.50–3.75% 升至 3.75–4.00%（2026-10-17，`monetary.fed_funds`），10Y 殖利率 5.1%（2026-10-15，+14 bps，`monetary.dgs10`），實質利率 DFII10 2.78%（+18 bps，`monetary.dfii10`），CPI YoY 3.72%（2026-09，`monetary.cpi_yoy`），WTI 101.91（2026-10-14，`monetary.wti`），Fed 在 AI 主導的回撤中出手緩衝的空間有限。
- [R1] 信用與波動率同步惡化：HY OAS 自前次基準以來 +58 bps 至 3.23%（2026-10-15，`monetary.hy_oas`），MOVE 由 82.21 升至 101.1（2026-10-16，`structural.treasury_basis_trade`）。
- [R1] 估值極端而持倉擁擠：Shiller CAPE 約 40.54（2026-10-16，`valuation.sp500_pe_cape`）；BofA 10 月 FMS 科技股淨加碼約 37%，為 2020 年 8 月以來最高（2026-10-13，`institutional.bofa_jpm_survey`）。
- [整體] 風險偏好開始退潮：兩週內第 4 檔 IPO 撤件或延後（2026-10-16，`speculation.ipo_heat`）；Fear & Greed 約 18，處於極度恐懼（2026-10-16，`retail.fear_greed`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.13%（2026-10-15 收盤 29,935.59 對 2026-10-06 高點 31,224.69），距 R1 門檻 23,418.52 仍需再跌約 21.77%（`valuation.ndx_drawdown`）。
- [R2] 四大 hyperscaler 2026 capex 合計約 725（2026-07-28），可得證據中沒有任何一家下修（`ai.hyperscaler_capex`）；AI 融資管道仍開，Lambda 於 2026-10-01 取得約 10 億美元 GPU 擔保融資（`structural.ai_infrastructure_debt`）。
- [R3] 融資市場沒有失序：SOFR−IORB −1 bp、SOFR99−IORB +7 bps、SRF 動用為 0（2026-10-15／2026-10-16，`monetary.repo_stress_srf`）；IG OAS 僅 0.84%（`monetary.ig_oas`）；10Y 期限溢價（term premium）1.0729%，7 日 −1.2 bps（2026-10-09，`monetary.term_premium`）；美債標售需求（auction tail / bid-to-cover）穩健，10Y 標售 bid-to-cover 約 2.77（2026-10-07，`monetary.treasury_auctions`）。
- [整體] 價格延伸溫和、沒有拋物線式加速：S&P 500 僅高於 200 日均線 5.34%（2026-10-16，`valuation.sp500_trend`），且 VIX 與 S&P 500 未同漲（7 日窗口 2026-10-08 → 2026-10-15，`structural.vix_spx_comove`）；散戶看多比例約 38.7%（2026-10-14，`retail.aaii`），並未亢奮。
- [整體] 基準狀態：任一 182 天窗口內，R1–R3 都不觸發才是常態；目前三條路徑都沒有走到一半，CDS 走闊屬於風險定價，還不是違約事件（`valuation.ai_credit_schism`）。

## 與前期比較

前次結論：無前次預測（report-2026-09-13 為舊格式評分報告）

本次為新格式首份預測，flip_evidence 為空。自 2026-09-13 以來的主要變化：

- Fed funds 上限由 3.75% 升至 4.00%（升息 25 bps），10Y 殖利率 +14 bps 至 5.1%，DFII10 +18 bps；ΔT10YIE −1 bp 與另兩腿的窗口不一致，分解判讀：不可判（視窗不一致）。
- HY OAS +58 bps 至 3.23%，MOVE +18.89 至 101.1，信用與利率波動同步升溫。
- NASDAQ-100 在 2026-10-06 創 252 日新高後回落，目前回撤 4.13%；S&P 500 相較前次基準幾乎持平（+0.03%）。
- CoreWeave 5Y CDS 創紀錄 1,194.5 bps，為 R3 路徑上最大的新增訊號。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `breadth.rsp_spy`：唯一結果是 2026-07-18 的 RSP YTD 報酬約 12.08，既過時又缺 SPY 對照，無法算出當前背離。此缺口不會改變結論，因為廣度只影響脆弱度判斷，不是觸發條件。
- `breadth.top10_concentration`：唯一結果是 2026-07-31 的前十大集中度約 38.9，已非當前快照。不會改變結論，理由同上。

其他限制：`valuation.mag7_multiples` 只取得單一成員 MSFT 前瞻本益比 24.5（2026-09-24），未取得 Mag 7 加權 P/E 與 P/S 對十年均值的比較；`valuation.sp500_pe_cape` 只有 CAPE，沒有 trailing P/E；`ai.hyperscaler_capex` 只有四家彙總，缺逐家指引方向，這是 R2 判讀的主要缺口；`monetary.private_credit_liquidity`、`ai.depreciation_life`、`ai.customer_concentration_rpo` 與 `ai.capital_cycle` 本次無合格披露；`ai.hyperscaler_financing_mix` 的 30 日 event_scan 沒有找到事件。另外，evidence 中的搜尋紀錄稱 script 的三個基差區塊失敗，但 macro artifact 顯示 `cftc_lev_funds`／`move_index`／`ofr_repo` 皆為 ok，本次以 artifact 為準。

最大的不確定性：

1. CoreWeave 等 AI 算力借款人的再融資時程（本次證據未涵蓋到期資料）：若出現再融資失敗或 distressed exchange，會直接觸發 R3，並可能帶動 R1，推向 yes。
2. 10 月下旬起的 hyperscaler Q3 財報與次一季的次年度指引：若兩家以上轉為下修，即觸發 R2，推向 yes；若維持或上修，則支持 no。
3. Fed 升息路徑與 10Y 5% 以上的殖利率：通膨仍在 3.72%，若續升息使實質利率再走高，將壓縮高估值科技股，推向 yes。Anthropic 預計 11 月中 IPO（2026-10-05 報導）是窗口內的情緒測試點。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7659.44 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 5.34 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 6.78 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29935.59 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.13 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2，FRED 季度起始日） | 48.2301354474（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 4.0（%） | FRED API (series_id=DFEDTARU) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.75（%） | FRED API (series_id=DFEDTARL) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 3.23（%） | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 58.0（bps） | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.84（%） | FRED API (series_id=BAMLC0A0CM) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 5.1（%） | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | 14.0（bps） | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.78（%） | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | 18.0（bps） | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.35（%） | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 101.91（美元／桶） | FRED API (series_id=DCOILWTICO) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72（%） | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.33（%） | FRED API (series_id=T5YIFR) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 1.0729（%） | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7d） | -1.2（bps） | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.89（%） | FRED API (series_id=SOFR) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.97（%） | FRED API (series_id=SOFR99) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.9（%） | FRED API (series_id=IORB) | 2026-10-18 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用 transaction volume） | 0.0（十億美元） | FRED API (series_id=RPONTTLD) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps（SOFR−IORB，兩腿同為 2026-10-15） | -1.0（bps） | FRED API (series_id=SOFR, IORB) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,755,639.0（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,943,911.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（無新觀測） | 6,250,253.0（¥625.03T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.46 | FRED API (series_id=VIXCLS) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of） | 16.46 | FRED API (series_id=VIXCLS, SP500) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日窗口） | 6.81（%） | FRED API (series_id=VIXCLS, SP500) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日窗口） | -0.27（%） | FRED API (series_id=VIXCLS, SP500) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2,097.9713（$2.10T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位） | -6,883,343（口） | CFTC TFF futures-only (cftc_lev_funds) | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -309,307（口） | CFTC TFF futures-only (cftc_lev_funds) | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 101.1 | Yahoo Finance chart API (^MOVE, move_index) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2,264.1（十億美元） | OFR STFM (REPO-TRIV1_TV_TOT-P, ofr_repo) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED（僅 CAPE；trailing P/E 未取得） |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED（僅取得 MSFT 單一成員前瞻 P/E；加權值未取得） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ⛔ FETCH FAILED（唯一結果為 2026-07-18 過時值且缺 SPY） |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ⛔ FETCH FAILED（唯一結果為 2026-07-31 過時值） |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（月頻 stock-of-state，沿用 2026-08） | ✓ SEARCH-VERIFIED（YoY 與市值比未取得） |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM | WebSearch | ✓ SEARCH-VERIFIED（BofA 10 月；JPM 未取得） |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | fetch_macro.py（DFEDTARU ok、DFEDTARL ok） | ✓ API |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） | ✓ API |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch） | ✗ NOT DISCLOSED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✗ NOT DISCLOSED（僅 2026-08-15 發布之 1–7 月值，非當前） |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state，沿用 Q2 財報季） | ✓ SEARCH-VERIFIED（僅四家彙總） |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✗ NOT DISCLOSED（最新為 2026-08-17 上季披露，非本季） |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch：quarterly_state 沿用最近揭露；event_scan 30d 掃描無事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch（stock-of-state，逐組件沿用） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch：quarterly_state 與 event_scan 30d 皆無披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch＋SEC EDGAR 8-K（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED（週 IPO 數與首日報酬未取得） |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch movers 掃描（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✗ NOT DISCLOSED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED（單一個股槓桿 ETF 合計；逐檔未取得） |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED（股債相關性未取得） |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | fetch_macro.py（VIXCLS ok、vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（僅交叉檢核） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py 三區塊（cftc_lev_funds ok、move_index ok、ofr_repo ok），aggregation any | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.54（原定來源 multpl.com） | Shiller PE CAPE ratio current October 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.mag7_multiples | MSFT 前瞻本益比 24.5（Mag 7 單一成員；原定為加權 P/E） | Magnificent 7 forward P/E valuation October 2026 | https://articlegateway.com/?p=146 | 2026-09-24 | 2026-10-18T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 紀錄 1,194.5 bps | AI credit fears tech default insurance record highs October 2026 | https://www.businessday.co.za/world/international-companies/2026-10-15-ai-credit-fears-push-tech-default-insurance-to-record-highs/ （BusinessDay） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| breadth.advance_decline | 上漲家數約 29 對下跌 71 | market breadth October 16 2026 percent above 200-day advance decline | https://www.thetrading.tools/market-breadth | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 約 18（極度恐懼；原定來源 CNN） | CNN Fear and Greed Index October 16 2026 extreme fear | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-08 月資料）約 1.45 兆美元（原定來源 FINRA） | FINRA margin debt August 2026 year over year | https://www.thetrading.tools/margin-debt | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.7%（週止 2026-10-14） | AAII sentiment survey week ending October 14 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA 10 月 FMS 科技股淨加碼約 37%，2020 年 8 月以來最高 | BofA October 2026 fund manager survey tech overweight cash | https://www.bloomberg.com/news/articles/2026-10-13/bofa-poll-shows-investors-most-exposed-to-tech-stocks-since-2020 （Bloomberg） | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.77 | Treasury 10-year note auction October 7 2026 bid-to-cover | https://www.rttnews.com/3697286/ten-year-note-auction-attracts-strong-demand.aspx （RTTNews） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 725（Q2 財報季彙總） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選中位租金約 4.20 | GPU rental price index HBM DRAM contract price October 2026 | https://uvik.net/blog/gpu-price-index/ | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 2026 年 hyperscaler 發債預估約 190（沿用最近揭露） | hyperscaler bond issuance 2026 capex versus free cash flow | https://www.twentyfouram.com/insights/oracle-clears-the-supply-cloud-with-record-demand | 2026-02-02 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 分子：Anthropic 年化 run-rate 約 65（OpenAI 無披露，不納入） | AI revenue versus capex gap 2026 annualized | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 分母：top-4 hyperscaler 2026 capex 合計約 725（不含 Oracle） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement October 2026 | 檢查來源：SEC EDGAR 8-K、SPACInsider、Boardroom Alpha | — | 2026-10-18T09:30:00+08:00 |
| speculation.ipo_heat | 兩週內第 4 檔 IPO 撤件或延後 | IPO market October 16 2026 pulled postponed Firmus Oura | https://www.ipox.com/ipox/the-ipox-update-10162026 （IPOX） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描（0 件符合兩個以上主題且基本面疲弱；PFAI 10/7 +116.7% 落在窗外） | biggest stock gainers week October 12-16 2026 microcap 100% | 檢查來源：Tapeboard movers archive、Financial Modeling Prep daily gainers、Yahoo movers | — | 2026-10-18T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 11 月中上市 | Anthropic IPO October 2026 timing valuation S-1 | https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market （CNN） | 2026-10-05 | 2026-10-18T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件合格；10/9 申報缺 filing-level 細節） | insider selling Form 4 October 2026 Nvidia AI executives SEC | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-10-18T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.04 | single stock leveraged ETF assets October 2026 weekly flows | https://www.etfaction.com/single-stock-traders-pile-into-tsll-and-intw-as-levered-flows-surge/ （ETF Action） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval October 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed | — | 2026-10-18T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 9 月 ADV 創紀錄約 3.4 百萬口（2026-09 月資料） | Cboe September 2026 derivatives volume 0DTE SPX record | https://www.cboe.com/insights/posts/market-metrics-that-matter-derivatives-september-2026-volume-highlights （Cboe） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.options_volume | OCC 9 月總結算量約 1,486,062,415 口（2026-09 月資料） | OCC September 2026 monthly volume data | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report （OCC） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 約 14.84、SKEW 154.34 | VIX term structure SKEW October 2026 options brief | https://www.home.saxo/content/articles/options/the-middle-got-cheaper-the-edge-did-not---options-brief---12-october-2026-12102026 （Saxo） | 2026-10-12 | 2026-10-18T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 1.45 兆美元（2026-08 月資料，僅交叉檢核） | margin debt to market cap August 2026 | https://www.thetrading.tools/margin-debt | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Lambda GPU 擔保融資約 10 億美元 | AI data center debt Lambda CoreWeave financing October 2026 | https://valueaddvc.com/pulse/ai-data-center-debt-financing-risk-2026 | 2026-10-01 | 2026-10-18T09:30:00+08:00 |

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
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 4.13,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

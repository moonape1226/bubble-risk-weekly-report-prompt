> [DRY RUN] this report was not committed to archive.

# 2026-10-18 AI 泡沫破裂預測報告
報告日期：2026-10-18｜ISO 週次：2026-W42｜預測窗口：2026-10-18 → 2027-04-18｜前次基準：report-2026-09-13（35天前）

## 結論

**結論：no**

三條路徑都還沒有一條已經啟動、或看得出會在窗口內走完：NASDAQ-100 距 52 週高點回撤 4.13%，離 R1 門檻還要再跌約 21.77%（`valuation.ndx_drawdown`）；四大 hyperscaler 都沒有下修 capex 指引的已知紀錄（`ai.hyperscaler_capex`）。CoreWeave 5Y CDS 1,194.5 bps 創紀錄（`valuation.ai_credit_schism`）是 R3 最強的警訊，但本次證據中沒有任何違約、破產或 distressed exchange，這只能說明脆弱度高、催化劑在累積，不足以推翻「182 天內通常不會破裂」的基準情境。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,935.59（2026-10-15），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 4.13%（`valuation.ndx_drawdown`）。R1 門檻水位為 23,418.52，要從最新收盤再跌約 21.77% 才會觸及。S&P 500 收在 7,659.44（2026-10-16），高於 200 日均線 5.34%、高於 52 週均線 6.78%，距前次基準日只變動 +0.03%（`valuation.sp500_trend`）。

這段期間市場內部轉弱：上漲家數約 29 對下跌約 71（2026-10-16，`breadth.advance_decline`），CNN Fear & Greed 約 18、屬極度恐懼（2026-10-16，`retail.fear_greed`），兩週內已有第 4 檔 IPO 撤件或延後（2026-10-16，`speculation.ipo_heat`）。估值脆弱度仍在高檔：Shiller CAPE 約 40.54（2026-10-16，`valuation.sp500_pe_cape`），BofA 10 月經理人調查的科技股淨加碼約 37、為 2020 年 8 月以來最高（2026-10-13，`institutional.bofa_jpm_survey`），代表部位擁擠。VIX 7 日窗（2026-10-08 → 2026-10-15）上升 6.81%，同期 S&P 500 下跌 0.27%，沒有出現同漲的 crowded-optionality 讀數（`structural.vix_spx_comove`）。

**判讀：** R1 距門檻還很遠（還需要再跌約 21.77%）。情緒與市場寬度轉弱，加上 HY OAS 走闊，下行風險確實升高，但要在窗口內觸發，需要一次系統性的 AI 重定價。最可能的觸發點是 R3 信用事件外溢，或 hyperscaler 季報下修 capex 引發連鎖拋售，目前兩者都還沒發生。

### R2 資本支出收縮

本次取得的最新資料是四大 hyperscaler（Microsoft、Alphabet、Amazon、Meta）2026 年 capex 合計約 725（十億美元），出自 2026-07-28 的 CNBC 報導（對應 2026 Q2 財報季，`ai.hyperscaler_capex`）。各家個別指引數值與方向本次沒有取得，結果如下：

- Microsoft：最新官方指引數值本次未取得（2026 Q2 財報季）；相較前次指引，沒有下修的已知紀錄。
- Alphabet：最新官方指引數值本次未取得（2026 Q2 財報季）；報導指財報後市場對其 capex 的審視加劇，但沒有下修的已知紀錄。
- Amazon：最新官方指引數值本次未取得（2026 Q2 財報季）；沒有下修的已知紀錄。
- Meta：最新官方指引數值本次未取得（2026 Q2 財報季）；沒有下修的已知紀錄。

目前已知下修家數為 0 / 4。下一次季報日期本次證據沒有列出，但 182 天窗口必然涵蓋接下來兩個財報季。需求面方面，H100 隨選中位租金約 4.20（美元／小時，2026-10-07，`ai.compute_supply_demand`），只有單點水位，看不出利用率是否惡化。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 65（十億美元，只有 Anthropic run-rate，2026-08-17）對比年化 capex 約 725（十億美元；分母只涵蓋 top-4，Oracle 本次未取得季頻數值、未納入）（`ai.revenue_capex_gap`）。缺口很大，但沒有前值可以判斷擴大或收斂。

**判讀：** R2 目前沒有任何一家下修，要在窗口內有兩家下修，需要連續兩個財報季出現明確的需求轉弱或融資受限。本次證據沒有看到這種轉折。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）出現明確的信貸端重定價：CoreWeave 5Y CDS 達到紀錄的 1,194.5 bps，報導標題指 AI 信用疑慮把科技股違約保險推到紀錄高點（2026-10-15，`valuation.ai_credit_schism`）。AI infrastructure debt financing / vendor-financing loops：Lambda 完成約 10 億美元的 GPU 擔保融資（2026-10-01，`structural.ai_infrastructure_debt`），說明 neocloud 仍能借到錢，但也代表槓桿繼續疊加。廣義信用方面，HY OAS 由 2.65% 升到 3.23%（+58 bps，2026-10-15，`monetary.hy_oas`），IG OAS 只從 0.80% 升到 0.84%（`monetary.ig_oas`）。

CoreWeave 等借款人的總負債是否 ≥ 50 億美元、近期到期牆與再融資需求，本次沒有任何來源佐證，因此 R3 規模門檻是否成立「本次未確立」。本次證據也沒有付款違約、寬限期、covenant waiver、distressed exchange 或 going-concern 字樣。

**判讀：** R3 是三條路徑中離觸發最近的一條。CDS 逾 1,100 bps 屬於高度困境的定價，但市場定價困境不等於窗口內一定違約，而且 Lambda 這類融資顯示市場還沒關門。要推過門檻，需要具名借款人錯過付款或啟動 distressed exchange；值得追的是後續到期與 covenant 披露。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 達紀錄 1,194.5 bps（2026-10-15），AI 信用疑慮把科技股違約保險推到紀錄高點；信貸端已先於股價重定價，是典型的後期訊號（`valuation.ai_credit_schism`）。
- [整體] 政策緩衝空間收窄：Fed 目標區間上限由 3.75% 升到 4.00%（DFEDTARU，2026-10-17），10Y 殖利率 5.10%（2026-10-15），CPI YoY 3.72%（2026-09），AI 帶動的下跌較難靠降息接住（`monetary.fed_funds`、`monetary.dgs10`、`monetary.cpi_yoy`）。
- [R1] 信用與波動同步升溫：HY OAS +58 bps 到 3.23%（2026-10-15），MOVE 由 82.21 升到 101.1（2026-10-16）（`monetary.hy_oas`、`structural.treasury_basis_trade`）。
- [R1] 市場內部轉弱、風險偏好退潮：上漲約 29 對下跌約 71（2026-10-16），Fear & Greed 約 18、極度恐懼（2026-10-16），兩週內第 4 檔 IPO 撤件或延後（2026-10-16）（`breadth.advance_decline`、`retail.fear_greed`、`speculation.ipo_heat`）。
- [R1] 估值與部位都很擁擠：Shiller CAPE 約 40.54（2026-10-16），BofA 科技股淨加碼約 37、為 2020 年 8 月以來最高（2026-10-13），一旦出現催化劑，下跌幅度會很大（`valuation.sp500_pe_cape`、`institutional.bofa_jpm_survey`）。
- [R3] AI infrastructure debt financing 繼續疊加：Lambda 約 10 億美元 GPU 擔保融資（2026-10-01），以 GPU 作抵押的槓桿讓 neocloud 對 GPU 殘值與租金更敏感（`structural.ai_infrastructure_debt`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.13%（2026-10-15），R1 門檻 23,418.52 還要再跌約 21.77%；S&P 500 仍高於 200 日均線 5.34%（2026-10-16），價格結構還沒破壞（`valuation.ndx_drawdown`、`valuation.sp500_trend`）。
- [R2] 四大 hyperscaler 2026 capex 合計約 725（十億美元，2026-07-28），本次證據中下修家數為 0 / 4，離「兩家下修」的門檻還很遠（`ai.hyperscaler_capex`）。
- [R3] 本次證據沒有任何 AI 基建借款人違約、破產或 distressed exchange；Lambda 在 2026-10-01 仍完成約 10 億美元的 GPU 擔保融資，代表融資管道還開著；IG OAS 只有 0.84%（+4 bps）（`structural.ai_infrastructure_debt`、`monetary.ig_oas`）。
- [整體] 資金市場平穩、沒有失序：repo 資金壓力（SOFR−IORB）為 −1 bp、SOFR99−IORB 為 7 bps（2026-10-15），SRF 動用（Standing Repo Facility usage）為 0（2026-10-16）；OFR tri-party repo transaction volume 約 2,264.1（十億美元）、較前次基準 −0.33%（`monetary.repo_stress_srf`、`structural.treasury_basis_trade`）。
- [整體] 美債標售需求（auction tail / bid-to-cover）穩健：10Y 標售 bid-to-cover 約 2.77、報導稱需求強勁（2026-10-07），沒有出現財政供給壓力的事件證據（`monetary.treasury_auctions`）。
- [整體] AI 需求與資本市場仍在運作：Anthropic 年化 run-rate 約 65（十億美元，2026-08-17），目標 11 月中上市（2026-10-05）；H100 隨選中位租金約 4.20（2026-10-07）（`ai.openai_anthropic_revenue`、`speculation.upcoming_ai_ipos`、`ai.compute_supply_demand`）。
- [整體] 基準情境：任意 182 天窗口內 R1–R3 都不發生才是常態；本次證據顯示的是脆弱度與壓力在升高，不是已經啟動、會在窗口內完成的路徑（`valuation.ndx_drawdown`）。

## 與前期比較

前次結論：yes（report-2026-09-13）
本次結論：翻轉
翻轉依據：
- 前次 forecast.json 沒有 `yes_basis` 欄位（寫於該欄位存在之前），沒有逐項的決定性理由可以核對。重新檢視後，前次的 yes 依照規則 1 不成立：R1 回撤由前次的 4.21% 變成本次距 52 週高點回撤 4.13%，距門檻還要再跌約 21.77%，R1 沒有任何進展（`valuation.ndx_drawdown`）。
- R2 仍然沒有任何一家 hyperscaler 下修 capex；最新已知的合計指引約 725（十億美元，2026-07-28），兩家下修的門檻沒有任何進度（`ai.hyperscaler_capex`）。
- R3 的信用壓力確實升高（CoreWeave 5Y CDS 1,194.5 bps，2026-10-15），但沒有違約、破產或 distressed exchange，借款人是否達到 50 億美元規模門檻本次也未確立；這只是脆弱度訊號，不足以讓 yes 成立（`valuation.ai_credit_schism`）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

未披露（✗ NOT DISCLOSED）的來源及其影響：
- valuation.analyst_tp_decomposition、retail.social_sentiment、retail.naaim、monetary.fedwatch、ai.token_growth、ai.customer_concentration_rpo、ai.depreciation_life、speculation.equity_put_call、structural.global_leveraged_approvals：都屬於情緒或背景類輸入，不直接對應 R1–R3 門檻，缺漏不太可能改變結論。
- monetary.private_credit_liquidity：30 日內沒有 gate proration / breach 或 net inflow→outflow flip 的披露。如果實際上已經出現贖回壓力，會加重 R3 傳導風險，是可能把結論推向 yes 的缺口之一。
- ai.hyperscaler_financing_mix（quarterly_state 有值：2026 年 hyperscaler 發債預估約 190，2026-02-02；event_scan 30 日內沒有披露）與 ai.capital_cycle（兩個組件都沒有當期披露）：沒有 SPV／表外融資事件，也無法判定資本週期階段，增速證據不足，本次不判定週期階段。
- 證據檔的 outcome 表把 structural.treasury_basis_trade 記為「script 三區塊 fetch_failed」，但 macro artifact 的 cftc_lev_funds、move_index、ofr_repo 三塊都是 status ok，日期也都在 14 日窗內。本報告以 validator 讀取的 macro artifact 為準，標為 ✓ API；這個不一致不影響結論方向。
- ai.hyperscaler_capex 只取得四家合計值，沒有逐家的指引數值與方向；ai.openai_anthropic_revenue 與 ai.revenue_capex_gap 的 Anthropic run-rate 是 2026-08-17（Q3）的資料，屬於沿用值，不是本季新披露。CoreWeave 等借款人的總負債本次未確立。

最大的不確定性：
1. 下一輪 hyperscaler 季報（日期本次未取得，但必然落在窗口內）：如果兩家以上下修 capex，或因融資受限壓低指引，R2 會直接成立，並可能帶動 R1，是把結論推向 yes 的主要因素；如果再度上修，結論會更穩固地維持 no。
2. CoreWeave 等 neocloud 的再融資：CDS 逾 1,100 bps 代表市場已經在定價困境；如果出現錯過付款或 distressed exchange，而且負債規模達門檻，R3 會成立，並可能經由信用外溢觸發 R1，推向 yes。
3. 利率與通膨：Fed 剛升息、10Y 在 5.10%、CPI 3.72%；如果升息週期延續，會壓縮高估值科技股並加重槓桿借款人的利息負擔，推向 yes；如果通膨回落、利率走穩，推向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7659.44 | FRED API (series_id=SP500) sp500_trend | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 5.34 | FRED API (series_id=SP500) sp500_trend | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 6.78 | FRED API (series_id=SP500) sp500_trend | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29935.59 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-06 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 4.13 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（家庭股票配置 %，2026Q2） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 4.0 | FRED API (series_id=DFEDTARU) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.75 | FRED API (series_id=DFEDTARL) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 3.23 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 58.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.84 | FRED API (series_id=BAMLC0A0CM) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 5.1 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（decomposition ΔDGS10） | 14.0 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.78 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps（decomposition ΔDFII10） | 18.0 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.35 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps（ΔT10YIE，視窗與 DGS10/DFII10 不一致） | -1.0 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（美元／桶） | 101.91 | FRED API (series_id=DCOILWTICO) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.33 | FRED API (series_id=T5YIFR) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright 10Y 期限溢價 %） | 1.0729 | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7d） | -1.2 | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.89 | FRED API (series_id=SOFR) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.97 | FRED API (series_id=SOFR99) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.9 | FRED API (series_id=IORB) | 2026-10-18 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6755639.0（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5943911.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6250253.0（¥625.03T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.46 | FRED API (series_id=VIXCLS) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（7 日窗終點） | 16.46 | FRED API vix_spx_comove block | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 6.81 | FRED API vix_spx_comove block | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -0.27 | FRED API vix_spx_comove block | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2097.9713（$2.10T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（槓桿基金美債期貨淨部位，口） | -6883343 | CFTC TFF cftc_lev_funds | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -309307 | CFTC TFF cftc_lev_funds | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 101.1 | Yahoo chart API (^MOVE) move_index | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index delta_abs（較前次基準 2026-09-11 的 82.21） | 18.89 | Yahoo chart API (^MOVE) move_index | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2264.1 | OFR STFM ofr_repo (REPO-TRIV1_TV_TOT-P) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |

註：10Y 分解 ΔDGS10 +14 bps ≈ ΔDFII10 +18 bps + ΔT10YIE −1 bp，判讀：不可判（視窗不一致）。repo 資金壓力（SOFR−IORB）−1 bp、SOFR99−IORB 7 bps（as_of 2026-10-15，iorb_date／sofr99_iorb_date 皆為 2026-10-15，同日）。

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebSearch | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED（只取得 MSFT 前瞻本益比） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py FRED SP500 | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py FRED NASDAQ100 | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail / Margin Debt: FINRA | WebSearch（月頻沿用） | ✓ SEARCH-VERIFIED（YoY 未取得） |
| retail.aaii | Retail / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail / Household equity allocation | scripts/fetch_macro.py FRED BOGZ1FL153064486Q | ✓ API |
| retail.naaim | Retail / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional / BofA Fund Manager Survey | WebSearch | ✓ SEARCH-VERIFIED（BofA 10 月；JPM 未取得） |
| monetary.fed_funds | Monetary / Fed funds rate: FRED | scripts/fetch_macro.py DFEDTARU＋DFEDTARL | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary / High Yield OAS | scripts/fetch_macro.py BAMLH0A0HYM2 | ✓ API |
| monetary.ig_oas | Monetary / Investment Grade OAS | scripts/fetch_macro.py BAMLC0A0CM | ✓ API |
| monetary.dgs10 | Monetary / 10Y Treasury yield | scripts/fetch_macro.py DGS10 | ✓ API |
| monetary.dfii10 | Monetary / 10Y Treasury real yield | scripts/fetch_macro.py DFII10 | ✓ API |
| monetary.t10yie | Monetary / 10Y breakeven inflation rate | scripts/fetch_macro.py T10YIE（FRED 直取） | ✓ API |
| monetary.wti | Monetary / WTI crude oil price | scripts/fetch_macro.py DCOILWTICO | ✓ API |
| monetary.cpi_yoy | Monetary / CPI YoY: FRED | scripts/fetch_macro.py CPIAUCSL yoy_pct | ✓ API |
| monetary.t5yifr | Monetary / 5y5y forward inflation expectation | scripts/fetch_macro.py T5YIFR | ✓ API |
| monetary.term_premium | Monetary / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py THREEFYTP10 | ✓ API |
| monetary.repo_stress_srf | Monetary / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py SOFR／SOFR99／IORB／RPONTTLD | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary / 美債標售需求 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary / Fed funds rate path expectations | WebSearch | ✗ NOT DISCLOSED |
| monetary.walcl | Monetary / Fed balance sheet: FRED | scripts/fetch_macro.py WALCL | ✓ API |
| monetary.ecb_boj | Monetary / Global central bank liquidity cross-check | scripts/fetch_macro.py ECBASSETSW＋JPNASSETS | ✓ API（ECBASSETSW ok；JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | WebSearch（季頻沿用） | ✓ SEARCH-VERIFIED（只取得四家合計） |
| ai.token_growth | AI / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED（Anthropic；OpenAI 未取得） |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構 | WebSearch：quarterly_state 季頻沿用＋event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口 | WebSearch（組件沿用） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI / 資本週期階段 | WebSearch：quarterly_state＋event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculation / Search for past 7 days | WebSearch＋SEC EDGAR 8-K（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculation / IPO market heat | WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculation / Microcap thematic moonshots | WebSearch movers screen（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculation / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculation / Insider selling at AI | SEC EDGAR Form 4＋WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculation / Cboe equity-only put/call ratio | WebSearch | ✗ NOT DISCLOSED |
| structural.leveraged_etf_aum | Structural / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED（單一個股槓桿 ETF 合計；個別 ticker 未取得） |
| structural.us_single_stock_etf | Structural / US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural / 0DTE option volume | WebSearch Cboe | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural / Options total volume | WebSearch OCC | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED（VIX／SKEW；股債相關未取得） |
| structural.vix_spx_comove | Structural / VIX / S&P 500 co-movement | scripts/fetch_macro.py VIXCLS＋vix_spx_comove | ✓ API |
| structural.margin_debt_crosscheck | Structural / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural / Bank loans to nondepository financial institutions | scripts/fetch_macro.py LNFACBW027SBOG | ✓ API |
| structural.treasury_basis_trade | Structural / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds／move_index／ofr_repo（any） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.54（原定來源 multpl.com） | Shiller PE CAPE ratio current October 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 成員 MSFT 前瞻本益比 24.5 | Magnificent 7 forward P/E valuation October 2026 | https://articlegateway.com/?p=146 | 2026-09-24 | 2026-10-18T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 紀錄 1,194.5 bps | AI credit fears tech default insurance record highs October 2026 | https://www.businessday.co.za/world/international-companies/2026-10-15-ai-credit-fears-push-tech-default-insurance-to-record-highs/ （BusinessDay） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 報酬約 12.08% | RSP equal weight vs SPY YTD performance 2026 | https://pro.thestreet.com/market-commentary/rsp-vs-spy-does-diversification-require-equal-weight （TheStreet） | 2026-07-18 | 2026-10-18T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度約 38.9% | S&P 500 top 10 concentration percent record 2026 | https://walnutinvest.com/stats/market-concentration-statistics | 2026-07-31 | 2026-10-18T09:30:00+08:00 |
| breadth.advance_decline | 上漲家數約 29 對下跌 71 | market breadth October 16 2026 percent above 200-day advance decline | https://www.thetrading.tools/market-breadth | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 約 18（極度恐懼；原定來源 cnn.com） | CNN Fear and Greed Index October 16 2026 extreme fear | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-08 月資料）約 1.45 兆美元 | FINRA margin debt August 2026 year over year | https://www.thetrading.tools/margin-debt | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.7%（截至 2026-10-14 當週） | AAII sentiment survey week ending October 14 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA 10 月 FMS 科技股淨加碼約 37%，2020 年 8 月以來最高 | BofA October 2026 fund manager survey tech overweight cash | https://www.bloomberg.com/news/articles/2026-10-13/bofa-poll-shows-investors-most-exposed-to-tech-stocks-since-2020 （Bloomberg） | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.77 | Treasury 10-year note auction October 7 2026 bid-to-cover | https://www.rttnews.com/3697286/ten-year-note-auction-attracts-strong-demand.aspx （RTTNews） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| monetary.pboc | 2026 年 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate social financing 2026 total | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm （SteelOrbis） | 2026-08-15 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 725（十億美元；2026 Q2 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65（十億美元） | OpenAI Anthropic annualized revenue run rate 2026 | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選中位租金約 4.20（美元／小時） | GPU rental price index HBM DRAM contract price October 2026 | https://uvik.net/blog/gpu-price-index/ | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 2026 年 hyperscaler 發債預估約 190（十億美元） | hyperscaler bond issuance 2026 capex versus free cash flow | https://www.twentyfouram.com/insights/oracle-clears-the-supply-cloud-with-record-demand （TwentyFour AM） | 2026-02-02 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic run-rate 約 65（十億美元）；分母取 ai.hyperscaler_capex top-4 約 725 | AI revenue versus capex gap 2026 annualized | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement October 2026 | 檢查來源：SEC EDGAR 8-K、SPACInsider、Boardroom Alpha（窗內無合格事件） | — | 2026-10-18T09:30:00+08:00 |
| speculation.ipo_heat | 兩週內第 4 檔 IPO 撤件或延後 | IPO market October 16 2026 pulled postponed Firmus Oura | https://www.ipox.com/ipox/the-ipox-update-10162026 （IPOX） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（0 件符合 2+ 主題×弱基本面） | biggest stock gainers week October 12-16 2026 microcap 100% | 檢查來源：Tapeboard movers archive、Financial Modeling Prep daily gainers、Yahoo movers（PFAI 10/7 +116.7% 落在窗外） | — | 2026-10-18T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 11 月中上市 | Anthropic IPO October 2026 timing valuation S-1 | https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market （CNN） | 2026-10-05 | 2026-10-18T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件合格） | insider selling Form 4 October 2026 Nvidia AI executives SEC | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表（10/9 有申報但無具名申報人／金額等 filing-level 細節） | — | 2026-10-18T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.04（十億美元） | single stock leveraged ETF assets October 2026 weekly flows | https://www.etfaction.com/single-stock-traders-pile-into-tsll-and-intw-as-levered-flows-surge/ （ETF Action） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval October 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed（窗內無合格核准或上市） | — | 2026-10-18T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 月度 ADV 創紀錄約 3.4 百萬口（2026-09 月資料） | Cboe September 2026 derivatives volume 0DTE SPX record | https://www.cboe.com/insights/posts/market-metrics-that-matter-derivatives-september-2026-volume-highlights （Cboe） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.options_volume | OCC 9 月總結算量約 1,486,062,415 口（2026-09 月資料） | OCC September 2026 monthly volume data | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report （OCC） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 約 14.84、SKEW 154.34 | VIX term structure SKEW October 2026 options brief | https://www.home.saxo/content/articles/options/the-middle-got-cheaper-the-edge-did-not---options-brief---12-october-2026-12102026 （Saxo） | 2026-10-12 | 2026-10-18T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率的分子約 1.45 兆美元（2026-08 月資料；市值分母未取得） | margin debt to market cap August 2026 | https://www.thetrading.tools/margin-debt | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Lambda GPU 擔保融資約 10 億美元 | AI data center debt Lambda CoreWeave financing October 2026 | https://valueaddvc.com/pulse/ai-data-center-debt-financing-risk-2026 （ValueAdd VC） | 2026-10-01 | 2026-10-18T09:30:00+08:00 |

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

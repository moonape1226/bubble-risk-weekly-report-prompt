> [DRY RUN] this report was not committed to archive.

# 2026-10-18 AI 泡沫破裂預測報告
報告日期：2026-10-18｜ISO 週次：2026-W42｜預測窗口：2026-10-18 → 2027-04-18｜前次基準：report-2026-09-13（35天前）

## 結論

**結論：no**

三條路徑目前都還沒有出現已經啟動、而且可能在 182 天內走完的證據。NASDAQ-100 距 52 週高點只回撤 4.13%（`valuation.ndx_drawdown`），本次也沒有任何 hyperscaler 下修 capex 指引的證據（`ai.hyperscaler_capex`）。最接近觸發的是 R3：CoreWeave 5Y CDS 創下 1,194.5 bps 的紀錄（`valuation.ai_credit_schism`），但目前沒有付款違約、破產申請或 distressed exchange 的跡象，信用重定價還不足以推翻「窗口內通常不會破裂」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤為 29,935.59（2026-10-15）。252 個交易日內最高收盤為 31,224.69（2026-10-06），距 52 週高點回撤 4.13%。R1 門檻為 23,418.52，也就是指數要從最新收盤再跌約 21.77% 才會觸發（`valuation.ndx_drawdown`）。S&P 500 最新為 7,659.44（2026-10-16），高於 200 日均線 5.34%、高於 52 週均線 6.78%，與前次基準日相比只變動 +0.03%（`valuation.sp500_trend`）。

不利的宏觀背景正在累積。Fed 目標區間上調 25 bps 至 3.75%–4.00%（`monetary.fed_funds`）；10Y 殖利率 5.10%，比前次基準高 14 bps（`monetary.dgs10`）；CPI YoY 3.72%（2026-09 月資料，`monetary.cpi_yoy`）；WTI 為 $101.91（`monetary.wti`）。這代表 Fed 若要為 AI 主導的跌勢提供緩衝，空間有限。另一方面，情緒已經相當悲觀：CNN Fear & Greed 約 18（極度恐懼，2026-10-16，`retail.fear_greed`），上漲家數約 29、下跌家數約 71（`breadth.advance_decline`），但指數本身仍貼近高點。VIX 與 S&P 500 沒有同向上漲：2026-10-08 → 2026-10-15 期間 VIX +6.81%、S&P 500 −0.27%，comove 為 false（`structural.vix_spx_comove`）。

**判讀：** 距離 R1 還很遠，需要再跌約 21.77%。要在窗口內觸發，大概需要信用事件（R3）或 capex 下修（R2）引發的連鎖去槓桿，加上利率維持高位。目前利率與信用條件在收緊，但指數還沒有出現有意義的跌勢。

### R2 資本支出收縮

本次取得的 hyperscaler capex 證據只有四家合計值：Microsoft、Alphabet、Amazon、Meta 的 2026 年 capex 合計約 725（CNBC，2026-07-28，對應 2026 年第 2 季財報後的指引，`ai.hyperscaler_capex`）。逐家的最新正式指引數字，以及與各自前一次指引相比的方向（上修／持平／下修），本次證據沒有提供，所以四家都只能記為「本次未取得逐家方向」。目前沒有任何一家被證實下修。下一輪季報與 2027 年度指引會落在窗口內，但具體財報日期本次沒有取得。需求面的旁證包括：Anthropic 年化 run-rate 約 65（2026-08-17，`ai.openai_anthropic_revenue`）；H100 隨選中位租金約 4.20（2026-10-07，`ai.compute_supply_demand`），單看價格無法判斷產能缺口。年化 AI 終端營收（只有 Anthropic）約 65，對比年化 capex 約 725（分母只涵蓋 top-4，未含 Oracle 與 neocloud），缺口仍大（`ai.revenue_capex_gap`）。

**判讀：** 本次沒有任何一家下修的證據，R2 要求四家中至少兩家下修，屬於遠端情境。窗口內的季報是主要觸發點：若 R1 或 R3 先發生，加上融資成本上升，可能迫使管理層下修。但目前的證據都不支持這個方向已經啟動。

### R3 AI 信用事件

AI 信用定價正在明顯重定價：CoreWeave 5Y CDS 創紀錄 1,194.5 bps（BusinessDay，2026-10-15，`valuation.ai_credit_schism`）。整體 HY OAS 為 3.23%，比前次基準走闊 58 bps（`monetary.hy_oas`），信用端的走闊早於股價（NASDAQ-100 只回撤 4.13%），符合 AI 信用定價分歧（equity-vs-credit schism）的後期訊號型態。融資活動仍在進行：Lambda 完成約 10 億美元 GPU 擔保融資（2026-10-01，`structural.ai_infrastructure_debt`），顯示 AI infrastructure debt financing / vendor-financing loops 仍然可以取得資金。CoreWeave 的總負債是否達到 R3 的 50 億美元門檻、近期到期與再融資時程，本次來源都沒有確立。本次也沒有任何付款違約、寬限期、covenant waiver、distressed exchange 或 going-concern 披露。

**判讀：** R3 是三條路徑中最接近的一條。CDS 走到紀錄高位，代表市場正在為違約風險定價，但距離實際的破產、超過寬限期違約或 distressed exchange 仍有一段距離。要在窗口內觸發，需要出現再融資失敗、主要客戶合約生變，或 distressed exchange 的公告。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 創紀錄 1,194.5 bps（2026-10-15），AI 基建借款人的信用端正在重定價，而股價端還沒跟上（`valuation.ai_credit_schism`）。
- [整體] 融資條件同步收緊：Fed 目標上限 4.00%（2026-10-17，比前次基準 +25 bps），10Y 殖利率 5.10%（2026-10-15，+14 bps），HY OAS 3.23%（+58 bps），MOVE 從 82.21 升到 101.1（2026-10-16）（`monetary.fed_funds`、`monetary.dgs10`、`monetary.hy_oas`、`structural.treasury_basis_trade`）。
- [整體] Fed 緩衝空間受限：CPI YoY 3.72%（2026-09 月資料），WTI $101.91（2026-10-14），降低了跌勢中迅速寬鬆的可能（`monetary.cpi_yoy`、`monetary.wti`）。
- [R1] 估值與部位擁擠：Shiller CAPE 約 40.54（2026-10-16）；BofA 10 月 FMS 科技股淨加碼約 37，為 2020 年 8 月以來最高（2026-10-13）（`valuation.sp500_pe_cape`、`institutional.bofa_jpm_survey`）。
- [R1] 投機需求開始退潮：IPO 市場兩週內第 4 檔撤件或延後（2026-10-16），市場寬度弱，上漲約 29 對下跌約 71（2026-10-16）（`speculation.ipo_heat`、`breadth.advance_decline`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點只回撤 4.13%（2026-10-15），52 週高點 31,224.69 是 2026-10-06 才創下；要觸發 R1 還需再跌約 21.77% 至 23,418.52（`valuation.ndx_drawdown`）。
- [R2] 本次證據沒有任何一家 hyperscaler 下修 capex：四家 2026 年合計 capex 約 725（2026-07-28），R2 需要四家中至少兩家下修（`ai.hyperscaler_capex`）。
- [R3] AI 基建融資管道仍然暢通：Lambda 約 10 億美元 GPU 擔保融資（2026-10-01）；同時沒有任何違約、寬限期或 distressed exchange 披露（`structural.ai_infrastructure_debt`）。
- [整體] repo 資金壓力（SOFR−IORB）沒有失序：SOFR 3.89% 對 IORB 3.9%（2026-10-15，利差 −1 bp），SOFR99 3.97%，SRF 動用（Standing Repo Facility usage）為 0.0（2026-10-16）（`monetary.repo_stress_srf`）。
- [整體] 價格趨勢沒有失速：S&P 500 高於 200 日均線 5.34%（2026-10-16），VIX 與 S&P 500 沒有同向上漲（2026-10-15 comove false）（`valuation.sp500_trend`、`structural.vix_spx_comove`）。

## 與前期比較

前次結論：無前次預測（report-2026-09-13 為舊格式評分報告）

前次是舊格式評分報告，其評分不會換算成 yes/no，所以 flip_evidence 為 []。自 2026-09-13 以來的主要證據變化：

- Fed 目標區間上調 25 bps 至 3.75%–4.00%（`monetary.fed_funds`）；10Y 殖利率 +14 bps 至 5.10%，10Y 實質殖利率 +18 bps 至 2.78%，breakeven −1 bp。三者的觀測視窗不一致，10Y Δ 分解判讀為「不可判（視窗不一致）」（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。
- HY OAS 走闊 58 bps 至 3.23%（`monetary.hy_oas`）；MOVE 由 82.21 升至 101.1（`structural.treasury_basis_trade`）。
- NASDAQ-100 在 2026-10-06 創 52 週新高後小幅回落，目前距 52 週高點回撤 4.13%（`valuation.ndx_drawdown`）。
- 美債基差交易槓桿（Treasury basis-trade leverage）：CFTC 槓桿基金美債期貨淨空部位擴大到 −6,883,343 口（2026-10-13，4 週 Δ −309,307）（`structural.treasury_basis_trade`）。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `monetary.ig_oas`：腳本的 BAMLC0A0CM 回傳 fetch_failed，本次證據中也沒有任何 IG OAS 的 WebSearch 備援結果，所以沒有取得當期值。這個缺口不太可能改變結論，因為 HY OAS（+58 bps）與 CoreWeave CDS 已經涵蓋信用端訊號；不過 IG OAS 若大幅走闊，會強化 R3 對 hyperscaler 發債成本的傳導判讀。

部分取得或資料日期較舊的項目（不改變結論，但削弱寬度與需求面的判讀）：`valuation.mag7_multiples` 只取得 MSFT 前瞻 P/E 24.5（2026-09-24），沒有 Mag 7 加權值與 10 年均值；`breadth.rsp_spy`（2026-07-18）與 `breadth.top10_concentration`（2026-07-31）的資料日期較舊；`ai.hyperscaler_capex` 只有四家合計值，沒有逐家方向；`ai.hyperscaler_financing_mix` 的 event_scan 沒有披露（quarterly_state 背景：2026 年 hyperscaler 發債預估約 190，2026-02-02）；`ai.capital_cycle` 兩個組件都沒有披露，增速證據不足，本次不判定資本週期階段（capital cycle stage）。harness 的 evidence 表把 `structural.treasury_basis_trade` 標成「script 三區塊 fetch_failed」，但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 三個區塊都是 status ok，本報告以 artifact 為準，記為 ✓ API。

最大的不確定性：

1. CoreWeave 等 AI 基建借款人的負債規模與再融資時程（本次未確立）。若證實負債 ≥ 50 億美元、近期有大額到期，而且 CDS 持續走闊，R3 會明顯靠近 yes。
2. 窗口內的 hyperscaler 季報與 2027 年度 capex 指引（日期本次未取得）。若有兩家下修，會直接觸發 R2；若繼續上修，則支持 no。
3. 利率路徑：Fed 已升息且 CPI 3.72%，若 10Y 殖利率續升，壓縮高估值科技股的估值，R1 與 R3 都會同時往 yes 推進；若通膨回落、市場預期轉向寬鬆，則支持 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7659.44 | FRED API (series_id=SP500) sp500_trend | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 5.34 | FRED API (series_id=SP500) sp500_trend | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 6.78 | FRED API (series_id=SP500) sp500_trend | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29935.59 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-06 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.13 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻） | 23418.52 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q2 季資料，家庭股票配置 %） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標上限 %） | 4.0 | FRED API (series_id=DFEDTARU) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標下限 %） | 3.75 | FRED API (series_id=DFEDTARL) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 3.23 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps（較前次基準） | 58.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 5.1 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | 14.0 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.78 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | 18.0 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.35 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | -1.0 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（美元/桶） | 101.91 | FRED API (series_id=DCOILWTICO) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.33 | FRED API (series_id=T5YIFR) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 1.0729 | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.89 | FRED API (series_id=SOFR) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.97 | FRED API (series_id=SOFR99) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.9 | FRED API (series_id=IORB) | 2026-10-18 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6755639.0（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5943911.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6250253.0（¥625.03T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.46 | FRED API (series_id=VIXCLS) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of） | 16.46 | FRED API vix_spx_comove block | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日） | 6.81 | FRED API vix_spx_comove block | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2097.9713（$2.10T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -6883343 | CFTC TFF cftc_lev_funds | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 101.1 | Yahoo chart ^MOVE move_index | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2264.1 | OFR STFM ofr_repo | 2026-10-16 | 2026-10-18T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED（CAPE；P/E 未單獨取得） |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED（部分：僅 MSFT 前瞻 P/E） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch 14 日掃描 | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-07-18） |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-07-31） |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（2026-08 月資料沿用） | ✓ SEARCH-VERIFIED（YoY 與市值比未取得） |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey | WebSearch | ✓ SEARCH-VERIFIED（BofA；JPM 未取得） |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py（DFEDTARU ok、DFEDTARL ok） | ✓ API |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2 ok） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM fetch_failed）；WebSearch 備援無結果 | ⛔ FETCH FAILED（BAMLC0A0CM：script fetch_failed，無 search 備援值） |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10 ok） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | scripts/fetch_macro.py（DFII10 ok） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE FRED 直接取得） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO ok） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR ok） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py（THREEFYTP10 ok） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） | ✓ API |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch 14 日 | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch | ✗ NOT DISCLOSED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py（WALCL ok） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch 30 日 | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（沿用最近季報指引） | ✓ SEARCH-VERIFIED（僅四家合計值） |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED（Anthropic） |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch：quarterly_state 沿用；event_scan 30 日掃描無披露 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch＋組件組合（分母 top-4） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch 30 日 | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch：quarterly_state 與 event_scan 皆無披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch＋SEC EDGAR 8-K 7 日掃描 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch 7 日 | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch movers 7 日掃描 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch 30 日 | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR Form 4 14 日掃描 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✗ NOT DISCLOSED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED（單一個股槓桿 ETF 合計） |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed 30 日 | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch 7 日 | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED（VIX、SKEW；股債相關未取得） |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS ok、vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch 30 日 | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG ok） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok） | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.54 | Shiller PE CAPE ratio current October 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.mag7_multiples | MSFT 前瞻本益比 24.5（Mag 7 成員） | Magnificent 7 forward P/E valuation October 2026 | https://articlegateway.com/?p=146 | 2026-09-24 | 2026-10-18T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 紀錄 1,194.5 bps | AI credit fears tech default insurance record highs October 2026 | https://www.businessday.co.za/world/international-companies/2026-10-15-ai-credit-fears-push-tech-default-insurance-to-record-highs/ （BusinessDay） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 報酬約 12.08 | RSP equal weight vs SPY YTD performance 2026 | https://pro.thestreet.com/market-commentary/rsp-vs-spy-does-diversification-require-equal-weight （TheStreet） | 2026-07-18 | 2026-10-18T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度約 38.9 | S&P 500 top 10 concentration percent record 2026 | https://walnutinvest.com/stats/market-concentration-statistics | 2026-07-31 | 2026-10-18T09:30:00+08:00 |
| breadth.advance_decline | 上漲家數約 29 對下跌 71 | market breadth October 16 2026 percent above 200-day advance decline | https://www.thetrading.tools/market-breadth | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 18（極度恐懼） | CNN Fear and Greed Index October 16 2026 extreme fear | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ （原定來源 cnn.com） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-08 月資料）約 1.45 兆美元 | FINRA margin debt August 2026 year over year | https://www.thetrading.tools/margin-debt （原定來源 FINRA） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.7%（週止 2026-10-14） | AAII sentiment survey week ending October 14 2026 | https://www.aaii.com/sentimentsurvey | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA 10 月 FMS 科技股淨加碼約 37，2020 年 8 月以來最高 | BofA October 2026 fund manager survey tech overweight cash | https://www.bloomberg.com/news/articles/2026-10-13/bofa-poll-shows-investors-most-exposed-to-tech-stocks-since-2020 （Bloomberg） | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.77 | Treasury 10-year note auction October 7 2026 bid-to-cover | https://www.rttnews.com/3697286/ten-year-note-auction-attracts-strong-demand.aspx （RTTNews） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate social financing 2026 total | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm | 2026-08-15 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_capex | MSFT／GOOGL／AMZN／META 2026 capex 合計約 725（2026 Q2 財報後） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65 | OpenAI Anthropic annualized revenue run rate 2026 | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選中位租金約 4.20 | GPU rental price index HBM DRAM contract price October 2026 | https://uvik.net/blog/gpu-price-index/ | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 2026 年 hyperscaler 發債預估約 190 | hyperscaler bond issuance 2026 capex versus free cash flow | https://www.twentyfouram.com/insights/oracle-clears-the-supply-cloud-with-record-demand | 2026-02-02 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收（僅 Anthropic）約 65 vs 年化 capex 約 725（分母：top-4） | AI revenue versus capex gap 2026 annualized | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios；分母取自 ai.hyperscaler_capex） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement October 2026 | 檢查來源：SEC EDGAR 8-K、SPACInsider、Boardroom Alpha（窗內無合格事件） | — | 2026-10-18T09:30:00+08:00 |
| speculation.ipo_heat | 兩週內第 4 檔 IPO 撤件或延後 | IPO market October 16 2026 pulled postponed Firmus Oura | https://www.ipox.com/ipox/the-ipox-update-10162026 （IPOX） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描（0 件符合 2+ 主題×弱基本面） | biggest stock gainers week October 12-16 2026 microcap 100% | 檢查來源：Tapeboard movers archive、Financial Modeling Prep daily gainers、Yahoo movers（PFAI 2026-10-07 +116.7% 落在窗外） | — | 2026-10-18T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 11 月中上市 | Anthropic IPO October 2026 timing valuation S-1 | https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market （CNN） | 2026-10-05 | 2026-10-18T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件合格） | insider selling Form 4 October 2026 Nvidia AI executives SEC | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表（2026-10-09 有申報但無具名申報人／金額等 filing-level 細節） | — | 2026-10-18T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.04 | single stock leveraged ETF assets October 2026 weekly flows | https://www.etfaction.com/single-stock-traders-pile-into-tsll-and-intw-as-levered-flows-surge/ （ETF Action） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval October 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed（窗內無合格核准或上市） | — | 2026-10-18T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 月度 ADV 創紀錄約 3.4 百萬口（2026-09） | Cboe September 2026 derivatives volume 0DTE SPX record | https://www.cboe.com/insights/posts/market-metrics-that-matter-derivatives-september-2026-volume-highlights （Cboe） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.options_volume | OCC 2026-09 總結算量約 1,486,062,415 口 | OCC September 2026 monthly volume data | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report （OCC） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 約 14.84、SKEW 154.34 | VIX term structure SKEW October 2026 options brief | https://www.home.saxo/content/articles/options/the-middle-got-cheaper-the-edge-did-not---options-brief---12-october-2026-12102026 （Saxo） | 2026-10-12 | 2026-10-18T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-08 月資料）約 1.45 兆美元（市值比基數） | margin debt to market cap August 2026 | https://www.thetrading.tools/margin-debt | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
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
  "yes_basis": [],
  "r1_drawdown_pct": 4.13,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

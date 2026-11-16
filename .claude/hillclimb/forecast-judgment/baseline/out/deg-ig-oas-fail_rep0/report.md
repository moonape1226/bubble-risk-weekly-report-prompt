> [DRY RUN] this report was not committed to archive.

# 2026-10-18 AI 泡沫破裂預測報告

報告日期：2026-10-18｜ISO 週次：2026-W42｜預測窗口：2026-10-18 → 2027-04-18｜前次基準：report-2026-09-13（35天前）

## 結論

**結論：no**

三條路徑都還沒走到能在 182 天內完成解析的位置：NASDAQ-100 距 52 週高點回撤 4.13%，離 R1 門檻還要再跌約 21.77%；R2 沒有任何一家 hyperscaler 下修 capex 的證據。最強的反方訊號是 CoreWeave 5Y CDS 創紀錄的 1,194.5 bps（R3），但同期 AI 借款人仍能取得新融資，repo 資金壓力（SOFR−IORB）也很平靜，信用壓力還沒傳導成違約或 distressed exchange。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

依 `valuation.ndx_drawdown`：NASDAQ-100 最新收盤 29,935.59（2026-10-15），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 4.13%。R1 門檻為 23,418.52，從最新收盤還要再跌約 21.77% 才會觸發。高點只在九天前，所以這是剛從峰值回落的初期，不是正在進行的熊市。

背景讀數：S&P 500 為 7,659.44（2026-10-16），仍高於 200 日均線 5.34%、高於 52 週均線 6.78%（`valuation.sp500_trend`），價格延伸還沒消化完。情緒端已經轉向防禦：CNN Fear & Greed 約 18，屬「極度恐懼」（`retail.fear_greed`，2026-10-16）；2026-10-16 上漲家數約 29 對下跌 71（`breadth.advance_decline`）。VIX 在 2026-10-08 → 2026-10-15 的 7 日窗口上升 6.81%、S&P 500 同期下跌 0.27%，屬正常的反向走勢，未出現同漲警戒（`structural.vix_spx_comove`，comove=false）。估值方面，Shiller CAPE 約 40.54（`valuation.sp500_pe_cape`，2026-10-16），BofA 10 月調查的科技股淨加碼約 37，為 2020 年 8 月以來最高（`institutional.bofa_jpm_survey`，2026-10-13），兩者都顯示部位擁擠、下行空間大。

**判讀：** 距 R1 還很遠（還要再跌約 21.77%）。要在窗口內觸發，需要一次信用或盈餘衝擊把擁擠的科技部位逼到被迫去槓桿；以目前讀數看，指數只回落了 4% 左右，情緒恐懼卻沒有伴隨流動性失序，較像修正，不像崩跌的開端。

### R2 資本支出收縮

依 `ai.hyperscaler_capex`（CNBC，2026-07-28，2026 年 7 月財報季）：四大 hyperscaler 2026 年 capex 合計約 725。這次檢索只取得四家合計值，沒有取得 Microsoft、Alphabet、Amazon、Meta 各自的最新正式指引數字，也沒有各家相對前次指引的方向：

- Microsoft：個別指引數字本次未取得；方向無法判定（可得證據中沒有下修紀錄）。
- Alphabet：個別指引數字本次未取得；方向無法判定（可得證據中沒有下修紀錄）。來源標題提到 Alphabet 財報後市場對 capex 的檢視更嚴格，但這是市場反應，不是指引下修。
- Amazon：個別指引數字本次未取得；方向無法判定（可得證據中沒有下修紀錄）。
- Meta：個別指引數字本次未取得；方向無法判定（可得證據中沒有下修紀錄）。

目前已確認下修的家數：0 家（四家中）。下一次財報的具體日期不在這次的證據中；依季度節奏，窗口內會有兩輪 hyperscaler 財報（2026 年第 3 季與第 4 季），下修若要發生就在這兩個時點。需求端參考：Anthropic 年化 run-rate 約 65（`ai.openai_anthropic_revenue`，2026-08-17）；AI 營收對 capex 缺口（revenue-to-capex gap）為年化 AI 終端營收（只計 Anthropic）約 65，對比 2026 年 capex 約 725（分母：top-4，不含 Oracle，因為本次沒有取得 Oracle 季頻 capex），兩者皆為來源所載數值；這是單點讀數，本次無法判斷缺口在擴大還是收斂（`ai.revenue_capex_gap`）。H100 隨選中位租金約 4.20（`ai.compute_supply_demand`，2026-10-07）是單點價格，沒有利用率或庫存證據配合，不能讀成產能過剩。

**判讀：** 距 R2 很遠。R2 需要四家中兩家正式下修，而最近一次可得的指引是合計約 725 的擴張水位，看不到下修。可能推進 R2 的是：若 R1 或 R3 先發生，迫使管理層在接下來兩輪財報中收縮指引。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）正在往信用端重新定價的方向走：CoreWeave 5Y CDS 達紀錄的 1,194.5 bps（`valuation.ai_credit_schism`，2026-10-15，報導標題為 AI 信用疑慮把科技股違約保險推上紀錄高點）。CoreWeave 以 AI 算力為主業，是最可能的 R3 候選；但這次的證據沒有載明它的負債總額、近期到期結構、評等動作或任何付款違約、covenant waiver、going-concern 字句，所以本報告無法確認它已達 ≥ 50 億美元門檻，也看不到違約前兆事件。

AI infrastructure debt financing / vendor-financing loops：Lambda 取得約 10 億美元的 GPU 擔保融資（`structural.ai_infrastructure_debt`，2026-10-01），顯示 neocloud 仍能進入融資市場，再融資管道沒有關閉。整體信用背景在惡化：HY OAS 由 2.65% 升至 3.23%（+58 bps，2026-09-11 → 2026-10-15，`monetary.hy_oas`）；Fed 目標區間上調 25 bps 至 3.75%–4.00%（`monetary.fed_funds`，2026-10-17）；CPI 年增 3.72%（2026-09 月資料，`monetary.cpi_yoy`），壓縮了 Fed 為 AI 主導的下跌提供緩衝的空間。資金面沒有失序：repo 資金壓力（SOFR−IORB）為 −1 bps、SOFR99−IORB 為 +7 bps（2026-10-15），SRF 動用（Standing Repo Facility usage）為 0（2026-10-16，`monetary.repo_stress_srf`）。

**判讀：** 三條路徑中 R3 最接近，但還沒到門檻。CDS 達 1,194.5 bps 代表市場已為 CoreWeave 定價出顯著的違約風險，但 R3 要求的是窗口內實際發生破產、超過寬限期的違約或完成 distressed exchange。要觸發，需要再融資管道關閉（目前 Lambda 交易顯示管道仍開著）或大客戶合約違約；若 HY OAS 持續擴大、再加上一次 Fed 升息，這條路徑的時間表會縮短。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 達紀錄的 1,194.5 bps（2026-10-15），AI 信用端已開始重新定價，這是三條路徑中最接近觸發的訊號 `valuation.ai_credit_schism`
- [整體] HY OAS 自前次基準以來擴大 58 bps 至 3.23%（2026-10-15），廣義信用條件在收緊，會抬高高槓桿 AI 借款人的再融資成本 `monetary.hy_oas`
- [整體] Fed 目標區間上調 25 bps 至 3.75%–4.00%（2026-10-17），CPI 年增 3.72%（2026-09 月資料），一旦 AI 資產下跌，政策緩衝空間有限 `monetary.fed_funds` `monetary.cpi_yoy`
- [R1] 部位擁擠：BofA 10 月調查科技股淨加碼約 37，為 2020 年 8 月以來最高（2026-10-13）；Shiller CAPE 約 40.54（2026-10-16）。一旦出現催化劑，下行幅度可能很大 `institutional.bofa_jpm_survey` `valuation.sp500_pe_cape`
- [R1] 風險偏好退潮：兩週內第 4 檔 IPO 撤件或延後（2026-10-16），Fear & Greed 約 18（極度恐懼，2026-10-16），上漲對下跌家數約 29 對 71（2026-10-16） `speculation.ipo_heat` `retail.fear_greed` `breadth.advance_decline`
- [整體] 美債波動上升：MOVE 為 101.1（2026-10-16），較前次基準上升 18.89，10Y 殖利率為 5.1%（2026-10-15） `structural.treasury_basis_trade` `monetary.dgs10`

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.13%（2026-10-15），從最新收盤還要再跌約 21.77% 才到 R1 門檻 23,418.52；高點只在 2026-10-06，價格離峰值不遠 `valuation.ndx_drawdown`
- [R2] 最近可得的 hyperscaler capex 指引為四家合計約 725（2026-07-28），沒有任何一家下修的證據；R2 需要四家中兩家正式下修 `ai.hyperscaler_capex`
- [R3] Lambda 仍取得約 10 億美元 GPU 擔保融資（2026-10-01），AI 基建的再融資管道仍開著，CDS 走闊還沒變成融資斷裂 `structural.ai_infrastructure_debt`
- [整體] repo 資金壓力（SOFR−IORB）為 −1 bps、SOFR99−IORB 為 +7 bps（2026-10-15），SRF 動用為 0（2026-10-16），沒有資金面失序可以把信用壓力迅速放大 `monetary.repo_stress_srf`
- [R1] S&P 500 仍高於 200 日均線 5.34%（2026-10-16）；VIX 與 S&P 500 在 2026-10-08 → 2026-10-15 沒有同漲（comove=false），VIX 為 16.46，市場在恐懼中但沒有恐慌 `valuation.sp500_trend` `structural.vix_spx_comove`
- [整體] 基本盤：任意 182 天窗口內，R1–R3 都不發生才是常態；Anthropic 年化 run-rate 約 65（2026-08-17）且 Anthropic 目標 11 月中上市（2026-10-05），顯示需求端與資本市場對 AI 仍有承接 `ai.openai_anthropic_revenue` `speculation.upcoming_ai_ipos`

## 與前期比較

前次結論：無前次預測（report-2026-09-13 為舊格式評分報告）

本次是新格式下的第一份 yes/no 預測，`flip_evidence` 為空。自 2026-09-13 以來的重要變化：

- Fed 目標區間上調 25 bps（3.50%–3.75% → 3.75%–4.00%），IORB 同步由 3.65% 升至 3.9%。
- HY OAS 由 2.65% 升至 3.23%（+58 bps）；MOVE 上升 18.89 至 101.1。
- 10Y 殖利率 +14 bps 至 5.1%，10Y 實質殖利率 +18 bps 至 2.78%，10Y breakeven −1 bp 至 2.35%；三腿視窗不一致，判讀：不可判（視窗不一致）。
- NASDAQ-100 於 2026-10-06 創下 252 日新高後回落 4.13%；S&P 500 與前次基準幾乎持平（+0.03%）。
- 本次新取得 CoreWeave 5Y CDS 紀錄高點（1,194.5 bps）與兩週內 4 檔 IPO 撤件／延後；這兩點讓 R3 成為本次最需要盯的路徑，但還不足以支持 yes。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `monetary.ig_oas`（BAMLC0A0CM）：腳本回報 fetch_failed，WebSearch 也沒有取得當期 IG OAS 數值。影響：IG OAS 用來確認信用壓力是否已從 HY 擴散到投資級（hyperscaler 發債主要落在投資級）。HY OAS 與 CoreWeave CDS 已經涵蓋高收益與 AI 信用端，IG 缺漏不太可能改變本次 no 的結論；但若 IG 也大幅擴大，代表 hyperscaler 融資成本上升、R2 壓力增加，會讓 no 的把握降低。

其他未取得資料（✗ NOT DISCLOSED，非技術失敗）：analyst TP 拆解、social sentiment、NAAIM、FedWatch、私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）、token growth、客戶集中度與 backlog 重複計算風險（RPO double-counting）、折舊年限變動（depreciation useful-life change）、資本週期階段（capital cycle stage）、hyperscaler 融資結構（capex vs FCF / 發債）的 30 日事件掃描、put/call、全球槓桿產品核准。其中私募信貸贖回壓力與 hyperscaler 融資事件與 R3 最相關，缺漏讓 R3 的傳導判讀較不完整。

另外，R2 只取得四大 hyperscaler 合計 capex，沒有個別指引與方向，所以 R2 的「0 家下修」是根據可得證據中沒有下修紀錄，不是逐家確認。

最大的不確定性：

1. CoreWeave 的負債規模與再融資時程：本次證據沒有它的負債總額或近期到期日。若確認負債 ≥ 50 億美元且有窗口內到期、CDS 繼續擴大，會把答案推向 yes。
2. 窗口內兩輪 hyperscaler 財報：任兩家下修 capex 就會觸發 R2；若指引續揚，R2 幾乎排除。
3. Fed 政策路徑：CPI 3.72% 下若再升息，會同時加重 R1（估值）與 R3（再融資）的壓力，推向 yes；若停止升息，則有利 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7659.44 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 5.34 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 6.78 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（對前次基準 %） | 0.03 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29935.59 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.13 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻） | 23418.52 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（家計部門股票配置 %，2026 Q2） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 4.0 | FRED API (series_id=DFEDTARU) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU delta_bps | 25.0 | FRED API (series_id=DFEDTARU) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.75 | FRED API (series_id=DFEDTARL) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 3.23 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 58.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 prior（前次基準 %） | 2.65 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-11 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（10Y 殖利率 %） | 5.1 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | 14.0 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（10Y 實質殖利率 %） | 2.78 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | 18.0 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（10Y breakeven %） | 2.35 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | -1.0 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（WTI 美元） | 101.91 | FRED API (series_id=DCOILWTICO) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（CPI 年增 %，2026-09 月資料） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（5y5y forward %） | 2.33 | FRED API (series_id=T5YIFR) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（10Y 期限溢價（term premium）%，Kim-Wright） | 1.0729 | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7d） | -1.2 | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.89 | FRED API (series_id=SOFR) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.97 | FRED API (series_id=SOFR99) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.9 | FRED API (series_id=IORB) | 2026-10-18 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB prior（前次基準 %） | 3.65 | FRED API (series_id=IORB) | 2026-09-13 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6755639.0（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5943911.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（無新觀測） | 6250253.0（¥625.03T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.46 | FRED API (series_id=VIXCLS) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 16.46 | FRED API (series_id=VIXCLS, SP500) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日，base 2026-10-08） | 6.81 | FRED API (series_id=VIXCLS) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日，base 2026-10-08） | -0.27 | FRED API (series_id=SP500) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2097.9713（$2.10T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG chg_pct | 2.14 | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -6883343 | CFTC TFF futures-only (cftc_lev_funds) | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -309307 | CFTC TFF futures-only (cftc_lev_funds) | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 101.1 | Yahoo Finance chart API (^MOVE, move_index) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index delta_abs（對前次基準變動） | 18.89 | Yahoo Finance chart API (^MOVE, move_index) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2264.1 | OFR STFM (REPO-TRIV1_TV_TOT-P, ofr_repo) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED（僅取得 CAPE，P/E 未取得） |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch | ✓ SEARCH-VERIFIED（僅取得 MSFT 前瞻 P/E，加權 P/E 未取得） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch [primary: SEARCH]，90d＋同季 | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500，sp500_trend） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100，ndx_drawdown） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch（stock-of-state，沿用 2026-08 月資料） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch，7d | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch [primary: SEARCH] | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✓ SEARCH-VERIFIED（BofA 10 月；JPM 未取得） |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（FRED API） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（FRED BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（FRED BAMLC0A0CM）＋ WebSearch fallback | ⛔ FETCH FAILED（BAMLC0A0CM 腳本 fetch_failed；WebSearch 無當期值） |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（FRED DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（FRED T10YIE） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（FRED DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（FRED CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（FRED T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（FRED THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（FRED API，repo_stress） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch [primary: SEARCH] | ✗ NOT DISCLOSED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（FRED WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（FRED ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok，無新觀測） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch [primary: SEARCH]，30d | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state，2026 年 7 月財報季） | ✓ SEARCH-VERIFIED（僅取得四家合計） |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險 | WebSearch [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch [primary: SEARCH]；quarterly_state 沿用，event_scan 30d 完成但無披露 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch [primary: SEARCH]，組合 Anthropic run-rate 與 top-4 capex | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch [primary: SEARCH]，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch [primary: SEARCH]；兩組件皆完成但無可用披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch＋SEC EDGAR 8-K，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch，7d | ✓ SEARCH-VERIFIED（僅取得撤件／延後事件，週 IPO 數與首日報酬未取得） |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch [primary: SEARCH]，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch，30d | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR Form 4＋WebSearch，14d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch [primary: SEARCH] | ✗ NOT DISCLOSED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED（取得單一個股槓桿 ETF 合計規模；個別 ticker 未取得） |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR ETF 申報＋ETF.com 新上市 feed，30d | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（KRX / TWSE / JPX / ESMA / ETFGI），7d | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED（VIX、SKEW；stock-bond correlation 未取得） |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（FRED VIXCLS＋vix_spx_comove） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（confirmation only） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch [primary: SEARCH]，30d | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）；WebSearch 補充無當期披露 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.54（原定來源：multpl.com） | Shiller PE CAPE ratio current October 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.mag7_multiples | MSFT 前瞻本益比 24.5（Mag 7 成員） | Magnificent 7 forward P/E valuation October 2026 | https://articlegateway.com/?p=146（articlegateway） | 2026-09-24 | 2026-10-18T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 紀錄 1,194.5 bps | AI credit fears tech default insurance record highs October 2026 | https://www.businessday.co.za/world/international-companies/2026-10-15-ai-credit-fears-push-tech-default-insurance-to-record-highs/（BusinessDay） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 報酬約 12.08 | RSP equal weight vs SPY YTD performance 2026 | https://pro.thestreet.com/market-commentary/rsp-vs-spy-does-diversification-require-equal-weight（TheStreet Pro） | 2026-07-18 | 2026-10-18T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度約 38.9 | S&P 500 top 10 concentration percent record 2026 | https://walnutinvest.com/stats/market-concentration-statistics（Walnut） | 2026-07-31 | 2026-10-18T09:30:00+08:00 |
| breadth.advance_decline | 上漲家數約 29 對下跌 71 | market breadth October 16 2026 percent above 200-day advance decline | https://www.thetrading.tools/market-breadth（thetrading.tools） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 18（極度恐懼；原定來源：cnn.com） | CNN Fear and Greed Index October 16 2026 extreme fear | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/（finhacker） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.margin_debt | margin debt 約 1.45 兆美元（2026-08 月資料；原定來源：FINRA） | FINRA margin debt August 2026 year over year | https://www.thetrading.tools/margin-debt（thetrading.tools） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.7（週至 2026-10-14） | AAII sentiment survey week ending October 14 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA 10 月 FMS 科技股淨加碼約 37，2020 年 8 月以來最高 | BofA October 2026 fund manager survey tech overweight cash | https://www.bloomberg.com/news/articles/2026-10-13/bofa-poll-shows-investors-most-exposed-to-tech-stocks-since-2020（Bloomberg） | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.77 | Treasury 10-year note auction October 7 2026 bid-to-cover | https://www.rttnews.com/3697286/ten-year-note-auction-attracts-strong-demand.aspx（RTTNews） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| monetary.pboc | 2026 年 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate social financing 2026 total | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm（SteelOrbis） | 2026-08-15 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 725（2026 年 7 月財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65 | OpenAI Anthropic annualized revenue run rate 2026 | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選中位租金約 4.20 | GPU rental price index HBM DRAM contract price October 2026 | https://uvik.net/blog/gpu-price-index/（Uvik） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 2026 年 hyperscaler 發債預估約 190（沿用背景值） | hyperscaler bond issuance 2026 capex versus free cash flow | https://www.twentyfouram.com/insights/oracle-clears-the-supply-cloud-with-record-demand（TwentyFour AM） | 2026-02-02 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic run-rate 約 65（分子；分母取 ai.hyperscaler_capex 的 top-4 合計約 725） | AI revenue versus capex gap 2026 annualized | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement October 2026 | 檢查來源：SEC EDGAR 8-K、SPACInsider、Boardroom Alpha | — | 2026-10-18T09:30:00+08:00 |
| speculation.ipo_heat | 兩週內第 4 檔 IPO 撤件或延後 | IPO market October 16 2026 pulled postponed Firmus Oura | https://www.ipox.com/ipox/the-ipox-update-10162026（IPOX） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描（0 件符合 2+ 主題×弱基本面；PFAI 10/7 +116.7% 落在窗外） | biggest stock gainers week October 12-16 2026 microcap 100% | 檢查來源：Tapeboard movers archive、Financial Modeling Prep daily gainers、Yahoo movers | — | 2026-10-18T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 11 月中上市 | Anthropic IPO October 2026 timing valuation S-1 | https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market（CNN） | 2026-10-05 | 2026-10-18T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件合格；NVDA 10/9 申報無 filing-level 細節） | insider selling Form 4 October 2026 Nvidia AI executives SEC | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-10-18T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.04 | single stock leveraged ETF assets October 2026 weekly flows | https://www.etfaction.com/single-stock-traders-pile-into-tsll-and-intw-as-levered-flows-surge/（ETF Action） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市掃描（0 件） | single stock leveraged ETF launch approval October 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed | — | 2026-10-18T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 9 月 ADV 創紀錄約 3.4 百萬口 | Cboe September 2026 derivatives volume 0DTE SPX record | https://www.cboe.com/insights/posts/market-metrics-that-matter-derivatives-september-2026-volume-highlights（Cboe） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.options_volume | OCC 9 月總結算量約 1,486,062,415 口（2026-09 月資料） | OCC September 2026 monthly volume data | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report（OCC） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 約 14.84、SKEW 154.34 | VIX term structure SKEW October 2026 options brief | https://www.home.saxo/content/articles/options/the-middle-got-cheaper-the-edge-did-not---options-brief---12-october-2026-12102026（Saxo） | 2026-10-12 | 2026-10-18T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 1.45 兆美元（2026-08 月資料，confirmation only） | margin debt to market cap August 2026 | https://www.thetrading.tools/margin-debt（thetrading.tools） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Lambda GPU 擔保融資約 10 億美元 | AI data center debt Lambda CoreWeave financing October 2026 | https://valueaddvc.com/pulse/ai-data-center-debt-financing-risk-2026（ValueAdd VC） | 2026-10-01 | 2026-10-18T09:30:00+08:00 |

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

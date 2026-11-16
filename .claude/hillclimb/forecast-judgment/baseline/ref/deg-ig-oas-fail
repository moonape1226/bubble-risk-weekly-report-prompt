> [DRY RUN] this report was not committed to archive.

# 2026-10-18 AI 泡沫破裂預測報告

報告日期：2026-10-18｜ISO 週次：2026-W42｜預測窗口：2026-10-18 → 2027-04-18｜前次基準：report-2026-09-13（35天前）

## 結論

**結論：no**

三條路徑目前都離解析門檻很遠：NASDAQ-100 距 52 週高點回撤 4.13%，還要再跌約 21.77% 才會觸及 R1；四大 hyperscaler 2026 capex 合計約 725，沒有任何一家下修的證據（R2）。CoreWeave 5Y CDS 創紀錄的 1,194.5 bps，加上 HY OAS 走闊，確實讓 R3 的信用壓力升高，但目前看不到付款違約、破產或 distressed exchange 的跡象，不足以推翻「182 天內三條件皆不成立」這個基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

依 `valuation.ndx_drawdown`：NASDAQ-100 最新收盤 29,935.59（2026-10-15），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 4.13%。R1 門檻水位 23,418.52，從最新收盤還要再跌約 21.77% 才會觸及。指數兩週前才創高；S&P 500 最新 7,659.44（2026-10-16），仍高於 200 日均線 5.34%、高於 52 週均線 6.78%（`valuation.sp500_trend`），趨勢延伸的幅度不算極端。可能把 R1 推向 yes 的環境因素包括：Fed 目標區間上調 25 bps 至 3.75%–4.00%（`monetary.fed_funds`），CPI YoY 3.72%（2026-09，`monetary.cpi_yoy`），WTI 101.91 美元（`monetary.wti`），10Y 殖利率 5.1%（`monetary.dgs10`）——政策端緩衝回撤的空間有限。另一方面，`structural.vix_spx_comove` 的 7 日窗口（2026-10-08 → 2026-10-15）中 VIX +6.81%、S&P 500 −0.27%，未觸發同漲警戒（comove=false）。

**判讀：** R1 距門檻約 21.77%，需要的是一次完整的熊市級下跌，而非一般修正。窗口內要推過門檻，得有信用事件（R3）或 capex 指引下修（R2）作催化，或利率／通膨衝擊迫使估值大幅重訂價；目前有前置壓力（升息、高油價、HY 走闊），但尚未看到傳導成指數層級的拋售。

### R2 資本支出收縮

依 `ai.hyperscaler_capex`：最近一次可取得的指引為 2026-07-28（Q2 財報季）的報導，Microsoft、Alphabet、Amazon、Meta 2026 capex 合計約 725（CNBC，報導標題指 Alphabet 財報後 capex 受到更多審視）。本次證據只有四家合計值，沒有逐家的指引數字，因此各家相對前次正式指引的方向只能記為「未提供指引（本次證據未載逐家數字）」；目前沒有任何一家下修的證據，已下修家數為 0/4。具體的下一次財報日期本次證據未載明；不過 182 天的窗口必然涵蓋至少兩個季度財報週期，每家至少有兩次更新指引的機會。

需求面參考：Anthropic 年化 run-rate 約 65（2026-08-17，`ai.openai_anthropic_revenue`），且據報目標 11 月中上市（2026-10-05，`speculation.upcoming_ai_ipos`）。H100 隨選中位租金約 4.20（2026-10-07，`ai.compute_supply_demand`），目前沒有搭配利用率下滑或 order digestion 的證據，不能讀成過剩訊號。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 65（僅 Anthropic）對年化 capex 約 725（分母：top-4，未含 Oracle），缺口仍大，但這是持續已久的狀態，不是新的轉折（`ai.revenue_capex_gap`）。

**判讀：** R2 需要四家中至少兩家下修，目前為 0 家。窗口內的兩個財報週期是唯一的觸發點；若 R1／R3 先發生、迫使管理層防禦性縮減，R2 才可能跟著成立。目前證據不支持兩家同時下修。

### R3 AI 信用事件

依 `valuation.ai_credit_schism`：CoreWeave 5Y CDS 達紀錄高點 1,194.5 bps（2026-10-15，BusinessDay 報導 AI 信用憂慮把科技股違約保險推升至紀錄高點）。這是 AI 信用定價分歧（equity-vs-credit schism）往「信貸端先重訂價」方向發展的明確訊號：NASDAQ-100 距高點僅 4.13%，信用端卻已在為 AI 算力借款人計入顯著的違約風險。CoreWeave 是最可能符合 R3 主業條件的借款人之一，但其負債規模、近期到期與再融資時程，本次證據都未載明。依 `structural.ai_infrastructure_debt`：Lambda 取得約 1 十億美元 GPU 擔保融資（2026-10-01），代表 AI infrastructure debt financing / vendor-financing loops 的融資管道仍然開放。整體信用環境：HY OAS 3.23%（2026-10-15），較前次基準（2026-09-11，2.65%）走闊 58 bps（`monetary.hy_oas`）；IG OAS 本次未取得（見資料缺漏）。美債基差交易槓桿（Treasury basis-trade leverage）方面，CFTC 槓桿基金淨部位 −6,883,343 口（2026-10-13，4 週變化 −309,307），MOVE 從 82.21 升至 101.1（`structural.treasury_basis_trade`）。repo 資金壓力（SOFR−IORB）為 −1 bp、SOFR99−IORB 為 7 bps，SRF 動用（Standing Repo Facility usage）為 0（`monetary.repo_stress_srf`）。

**判讀：** R3 是三條路徑中最接近的一條。CDS 紀錄高點反映市場已在定價違約可能性，但 R3 要求的是已實際發生的破產申請、超過寬限期的違約或 distressed exchange，目前沒有任何這類跡象，而同業仍能取得新融資。窗口內若出現再融資失敗、契約豁免或 distressed exchange 協商，R3 可能成立，並經由信用傳導觸發 R1。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 達紀錄高點 1,194.5 bps（2026-10-15），AI 信用定價分歧（equity-vs-credit schism）轉為信貸端先走闊，屬於後期訊號 `valuation.ai_credit_schism`
- [整體] HY OAS 從 2.65%（2026-09-11）走闊至 3.23%（2026-10-15），+58 bps；同期 MOVE 從 82.21 升至 101.1（2026-10-16），信用與利率波動同步升溫 `monetary.hy_oas` `structural.treasury_basis_trade`
- [R1] Fed 目標區間上限從 3.75% 升至 4.0%（2026-10-17），CPI YoY 3.72%（2026-09）、WTI 101.91（2026-10-14）、10Y 殖利率 5.1%（2026-10-15），Fed 緩衝 AI 主導回撤的空間受限 `monetary.fed_funds` `monetary.cpi_yoy` `monetary.wti` `monetary.dgs10`
- [R1] IPO 市場轉冷：兩週內已有第 4 檔 IPO 撤件或延後（2026-10-16）；CNN Fear & Greed 約 18，屬極度恐懼（2026-10-16） `speculation.ipo_heat` `retail.fear_greed`
- [R1] 估值與部位擁擠：Shiller CAPE 約 40.54（2026-10-16）；BofA 10 月 FMS 科技股淨加碼約 37，為 2020 年 8 月以來最高（2026-10-13） `valuation.sp500_pe_cape` `institutional.bofa_jpm_survey`
- [R1] 市場廣度轉弱：上漲家數約 29 對下跌 71（2026-10-16） `breadth.advance_decline`

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.13%（2026-10-15），距 R1 門檻水位 23,418.52 還要再跌約 21.77%；高點才在 2026-10-06 創下 `valuation.ndx_drawdown`
- [R2] 四大 hyperscaler 2026 capex 合計約 725（2026-07-28），沒有任何一家下修的證據，已下修家數 0/4 `ai.hyperscaler_capex`
- [R3] AI 算力借款人仍能取得新融資：Lambda 取得約 1 十億美元 GPU 擔保融資（2026-10-01），R3 要求的實際違約／破產／distressed exchange 目前都沒有出現 `structural.ai_infrastructure_debt`
- [整體] repo 資金壓力（SOFR−IORB）為 −1 bp、SOFR99−IORB 為 7 bps（2026-10-15），SRF 動用（Standing Repo Facility usage）為 0（2026-10-16），短期融資市場沒有失序跡象 `monetary.repo_stress_srf`
- [R2] AI 終端需求仍在擴張：Anthropic 年化 run-rate 約 65（2026-08-17），且據報目標 11 月中上市（2026-10-05） `ai.openai_anthropic_revenue` `speculation.upcoming_ai_ipos`
- [R1] S&P 500 高於 200 日均線 5.34%（2026-10-16）、7 日窗口 VIX/S&P 500 未同漲（comove=false，2026-10-15），趨勢與選擇權面都沒有失控的延伸 `valuation.sp500_trend` `structural.vix_spx_comove`

## 與前期比較

前次結論：無前次預測（report-2026-09-13 為舊格式評分報告）

前次為舊格式評分報告，沒有 yes/no 預測可比較，本次 flip_evidence 為空。自 2026-09-13 以來的主要變化：

- Fed 目標區間上調 25 bps（3.50%–3.75% → 3.75%–4.00%）。
- HY OAS 走闊 58 bps（2.65% → 3.23%）；MOVE 從 82.21 升至 101.1。
- 10Y 殖利率 +14 bps、10Y 實質殖利率 +18 bps、T10YIE −1 bp。三腿視窗不一致，10Y 變動歸因判讀：不可判（視窗不一致）。
- CoreWeave 5Y CDS 創紀錄（1,194.5 bps，2026-10-15）。
- NASDAQ-100 在 2026-10-06 創新高後回落 4.13%；S&P 500 與前次基準相比幾乎持平（+0.03%）。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `monetary.ig_oas`（BAMLC0A0CM）：script 回傳 fetch_failed，WebSearch fallback 也未取得當期值。影響評估：IG OAS 是整體信用傳導的確認指標，缺值會削弱對 R3→R1 傳導的判斷；不過 HY OAS（+58 bps）與 CoreWeave CDS 已涵蓋信用端的方向訊號，除非 IG 出現與 HY 截然不同的劇烈走闊，否則不太可能改變本次結論。

其他未披露的來源（✗ NOT DISCLOSED，非技術失敗）：analyst TP decomposition、social sentiment、NAAIM、FedWatch、私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）、token growth、backlog 重複計算風險（RPO double-counting）、hyperscaler 融資結構（capex vs FCF / 發債）的 30 日 event_scan、折舊年限變動（depreciation useful-life change）、資本週期階段（capital cycle stage）、put/call、global leveraged approvals。其中私募信貸贖回壓力與 hyperscaler 融資事件的缺口，與 R3 的判斷最直接相關。

主要不確定性：

1. **CoreWeave 等 AI 算力借款人的再融資路徑**：CDS 已在紀錄高點，但負債規模與到期時程本次未取得。若窗口內出現再融資失敗或 distressed exchange，將直接把答案推向 yes（R3，並可能傳導到 R1）。
2. **窗口內兩個財報週期的 capex 指引**：本次只有四家合計值、沒有逐家數字。若有兩家同時下修，將推向 yes（R2）；維持或上修則強化 no。
3. **利率與通膨路徑**：10Y 殖利率 5.1%、Fed 剛升息、WTI 超過 100。若繼續升息或殖利率再上行，會提高估值重訂價的風險，推向 yes（R1）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7659.44 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | dev200_pct（距 200 日均線偏離 %） | 5.34 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（NASDAQ-100 最新收盤） | 29935.59 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.13 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（家計股票配置 %，2026 Q2） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 4.0 | FRED API (series_id=DFEDTARU) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.75 | FRED API (series_id=DFEDTARL) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 3.23 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（10Y 殖利率 %） | 5.1 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（10Y 實質殖利率 %） | 2.78 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（10Y breakeven %） | 2.35 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（WTI 美元） | 101.91 | FRED API (series_id=DCOILWTICO) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（CPI YoY %，2026-09 月資料） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（5y5y forward %） | 2.33 | FRED API (series_id=T5YIFR) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（10Y 期限溢價（term premium）%，Kim-Wright） | 1.0729 | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.89 | FRED API (series_id=SOFR) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.97 | FRED API (series_id=SOFR99) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.9 | FRED API (series_id=IORB) | 2026-10-18 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用 transaction volume，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.walcl | WALCL latest（Fed 資產負債表） | 6,755,639（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（ECB 資產負債表） | 5,943,911（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（BOJ 資產負債表） | 6,250,253（¥625.03T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.46 | FRED API (series_id=VIXCLS) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（7 日窗口 base 2026-10-08，comove=false） | 16.46 | FRED API (series_id=VIXCLS, SP500) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（銀行對 NBFI 放款） | 2097.9713（$2.10T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（槓桿基金美債期貨淨部位，口） | -6883343 | CFTC TFF futures-only | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（^MOVE） | 101.1 | Yahoo Finance chart API (^MOVE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2264.1 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com，WebSearch primary | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch | ✓ SEARCH-VERIFIED（僅取得 MSFT 前瞻本益比） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API sp500_trend=ok |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API ndx_drawdown=ok |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API BOGZ1FL153064486Q=ok |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch primary | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（FRED API） | ✓ API DFEDTARU=ok; DFEDTARL=ok |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（FRED API） | ✓ API BAMLH0A0HYM2=ok |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（FRED API）；WebSearch fallback | ⛔ FETCH FAILED BAMLC0A0CM=fetch_failed；WebSearch fallback 未取得當期值 |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（FRED API） | ✓ API DGS10=ok |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED API） | ✓ API DFII10=ok |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（FRED API） | ✓ API T10YIE=ok |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（FRED API） | ✓ API DCOILWTICO=ok |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（FRED API，yoy_pct） | ✓ API CPIAUCSL=ok |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（FRED API） | ✓ API T5YIFR=ok |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（FRED API） | ✓ API THREEFYTP10=ok |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（FRED API） | ✓ API SOFR=ok; SOFR99=ok; IORB=ok; RPONTTLD=ok |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch primary | ✗ NOT DISCLOSED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（FRED API） | ✓ API WALCL=ok |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（FRED API） | ✓ API ECBASSETSW=ok; JPNASSETS=ok |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | WebSearch primary | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch primary | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch primary；quarterly_state stock-of-state＋event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch primary（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch primary（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch primary；quarterly_state stock-of-state＋event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch primary（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR Form 4＋WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch primary | ✗ NOT DISCLOSED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR ETF filings＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（FRED VIXCLS＋SP500） | ✓ API VIXCLS=ok; vix_spx_comove=ok |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch primary（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED API） | ✓ API LNFACBW027SBOG=ok |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds／move_index／ofr_repo）；WebSearch 補充 | ✓ API cftc_lev_funds=ok; move_index=ok; ofr_repo=ok |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.54（預定來源 multpl.com） | Shiller PE CAPE ratio current October 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 成員 MSFT 前瞻本益比 24.5 | Magnificent 7 forward P/E valuation October 2026 | https://articlegateway.com/?p=146 | 2026-09-24 | 2026-10-18T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 紀錄 1,194.5 bps | AI credit fears tech default insurance record highs October 2026 | https://www.businessday.co.za/world/international-companies/2026-10-15-ai-credit-fears-push-tech-default-insurance-to-record-highs/（BusinessDay） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 報酬約 12.08 | RSP equal weight vs SPY YTD performance 2026 | https://pro.thestreet.com/market-commentary/rsp-vs-spy-does-diversification-require-equal-weight（TheStreet Pro） | 2026-07-18 | 2026-10-18T09:30:00+08:00 |
| breadth.top10_concentration | 前十大集中度約 38.9 | S&P 500 top 10 concentration percent record 2026 | https://walnutinvest.com/stats/market-concentration-statistics | 2026-07-31 | 2026-10-18T09:30:00+08:00 |
| breadth.advance_decline | 上漲家數約 29 對下跌 71 | market breadth October 16 2026 percent above 200-day advance decline | https://www.thetrading.tools/market-breadth | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 極度恐懼約 18（預定來源 CNN） | CNN Fear and Greed Index October 16 2026 extreme fear | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-08 月資料）約 1.45 兆美元（預定來源 FINRA） | FINRA margin debt August 2026 year over year | https://www.thetrading.tools/margin-debt | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.7（週至 2026-10-14） | AAII sentiment survey week ending October 14 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA 10 月 FMS 科技股淨加碼約 37，為 2020 年 8 月以來最高 | BofA October 2026 fund manager survey tech overweight cash | https://www.bloomberg.com/news/articles/2026-10-13/bofa-poll-shows-investors-most-exposed-to-tech-stocks-since-2020（Bloomberg） | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.77 | Treasury 10-year note auction October 7 2026 bid-to-cover | https://www.rttnews.com/3697286/ten-year-note-auction-attracts-strong-demand.aspx（RTTNews） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣（2026-07 累計資料） | PBoC aggregate social financing 2026 total | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm（SteelOrbis） | 2026-08-15 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 725（Q2 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65 | OpenAI Anthropic annualized revenue run rate 2026 | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選中位租金約 4.20 | GPU rental price index HBM DRAM contract price October 2026 | https://uvik.net/blog/gpu-price-index/ | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 2026 年 hyperscaler 發債預估約 190（背景；event_scan 30 日內無披露） | hyperscaler bond issuance 2026 capex versus free cash flow | https://www.twentyfouram.com/insights/oracle-clears-the-supply-cloud-with-record-demand（TwentyFour AM） | 2026-02-02 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic run-rate 約 65；分母取 ai.hyperscaler_capex 的 top-4 合計約 725 | AI revenue versus capex gap 2026 annualized | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement October 2026 | 檢查來源：SEC EDGAR 8-K、SPACInsider、Boardroom Alpha（窗內無合格事件） | — | 2026-10-18T09:30:00+08:00 |
| speculation.ipo_heat | 兩週內第 4 檔 IPO 撤件或延後 | IPO market October 16 2026 pulled postponed Firmus Oura | https://www.ipox.com/ipox/the-ipox-update-10162026（IPOX） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（0 件符合 2+ 主題×弱基本面） | biggest stock gainers week October 12-16 2026 microcap 100% | 檢查來源：Tapeboard movers archive、Financial Modeling Prep daily gainers、Yahoo movers（PFAI 10/7 +116.7% 落在窗外） | — | 2026-10-18T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 11 月中上市 | Anthropic IPO October 2026 timing valuation S-1 | https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market（CNN） | 2026-10-05 | 2026-10-18T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件合格） | insider selling Form 4 October 2026 Nvidia AI executives SEC | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表（10/9 有申報但無具名申報人／金額等 filing-level 細節） | — | 2026-10-18T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.04 | single stock leveraged ETF assets October 2026 weekly flows | https://www.etfaction.com/single-stock-traders-pile-into-tsll-and-intw-as-levered-flows-surge/（ETF Action） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval October 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed（窗內無合格核准或上市） | — | 2026-10-18T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 月度 ADV 創紀錄約 3.4 百萬口（2026-09 月資料） | Cboe September 2026 derivatives volume 0DTE SPX record | https://www.cboe.com/insights/posts/market-metrics-that-matter-derivatives-september-2026-volume-highlights（Cboe） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.options_volume | 9 月總結算量約 1,486,062,415 口（2026-09 月資料） | OCC September 2026 monthly volume data | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report（OCC） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 約 14.84、SKEW 154.34 | VIX term structure SKEW October 2026 options brief | https://www.home.saxo/content/articles/options/the-middle-got-cheaper-the-edge-did-not---options-brief---12-october-2026-12102026（Saxo） | 2026-10-12 | 2026-10-18T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 1.45 兆美元（2026-08 月資料，僅作確認） | margin debt to market cap August 2026 | https://www.thetrading.tools/margin-debt | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Lambda GPU 擔保融資約 1 十億美元 | AI data center debt Lambda CoreWeave financing October 2026 | https://valueaddvc.com/pulse/ai-data-center-debt-financing-risk-2026（ValueAdd VC） | 2026-10-01 | 2026-10-18T09:30:00+08:00 |

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

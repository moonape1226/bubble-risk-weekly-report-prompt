> [DRY RUN] this report was not committed to archive.

# 2026-10-18 AI 泡沫破裂預測報告

報告日期：2026-10-18｜ISO 週次：2026-W42｜預測窗口：2026-10-18 → 2027-04-18｜前次基準：report-2026-09-13（35天前）

## 結論

**結論：no**

三條路徑都尚未接近觸發：NASDAQ-100 距 52 週高點回撤僅 4.13%（R1 需 25%），四大 hyperscaler 最近一次指引仍是擴張而非下修（R2），R3 雖出現 CoreWeave 5Y CDS 紀錄高位（約 1,194.5 bps）這類信用重定價，但尚無破產、付款違約或 distressed exchange 的跡象。信用與資金面壓力確實升溫（HY OAS 擴大 58 bps、Fed 升息 25 bps），但不足以推翻「182 天內三者皆不發生」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,935.59（2026-10-15），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 4.13%（`valuation.ndx_drawdown`）。R1 門檻水位為 23,418.52，自最新收盤須再下跌約 21.77% 才會觸及。指數高點僅在九天前，代表市場仍貼近高位；但同期情緒與廣度已明顯轉弱：CNN Fear & Greed 約 18（極度恐懼，2026-10-16，`retail.fear_greed`），上漲對下跌家數約 29 對 71（2026-10-16，`breadth.advance_decline`），VIX 16.46（2026-10-15，`structural.vix_spx_comove`）且 MOVE 由 82.21 升至 101.1（`structural.treasury_basis_trade`）。估值面 Shiller CAPE 約 40.54（2026-10-16，`valuation.sp500_pe_cape`），S&P 500 高於 200 日均線 5.34%（`valuation.sp500_trend`），下行空間大，但這屬於脆弱度而非時點證據。

**判讀：** 距觸發仍遠（還需約 21.77% 跌幅）。要在窗口內觸發，需要一個傳導型催化劑——例如 R3 型 AI 信用事件、hyperscaler 季報下修 capex、或升息與 10Y 5.10% 引發的估值壓縮連鎖——把目前的情緒恐慌轉成持續性拋售。

### R2 資本支出收縮

可取得的最新官方指引是 2026-07-28 CNBC 彙整的四大 hyperscaler（Microsoft、Alphabet、Amazon、Meta）2026 年 capex 合計約 725（`ai.hyperscaler_capex`，擷取結果未列分家數字）。逐家狀況：Microsoft、Alphabet、Amazon、Meta 的分家最新指引與相對前次指引方向，均未包含在本次取得的證據中——本次無法逐家判定上修／持平／下修；可確認的是截至 2026-07-28 的彙整報導呈現的是合計擴張，而非下修，目前已確認下修的家數為 0。下一輪（Q3）與再下一輪（Q4）季報都會落在窗口內，但具體日期本次未取得。需求端旁證：Anthropic 年化 run-rate 約 65（2026-08-17，`ai.openai_anthropic_revenue`），H100 隨選中位租金約 4.20（2026-10-07，`ai.compute_supply_demand`）；單一租金價格本身不構成產能過剩證據。

**判讀：** 尚未啟動。需在窗口內兩次季報中有兩家把當年度或次年度 capex 指引下修；以目前「合計約 725 且仍擴張」的狀態，最可能的觸發途徑是 R1 大幅回撤或融資成本上升迫使管理層收手，目前沒有直接證據顯示任何一家正在轉向。

### R3 AI 信用事件

符合規模門檻的主要候選是 CoreWeave：其 5Y CDS 達紀錄 1,194.5 bps（2026-10-15，`valuation.ai_credit_schism`），報導標題即為「AI credit fears push tech default insurance to record highs」，屬於信貸端開始重定價的後期訊號。AI infrastructure debt financing / vendor-financing loops 方面，Lambda 於 2026-10-01 取得約 1 十億美元 GPU 擔保融資（`structural.ai_infrastructure_debt`），顯示市場仍對 neocloud 開放融資管道。整體信用環境同步轉緊：HY OAS 由 2.65% 升至 3.23%（+58 bps，`monetary.hy_oas`），IG OAS 0.84%（+4 bps，`monetary.ig_oas`）。本次證據中未見任何 AI 資料中心借款人的付款違約、寬限期、covenant waiver、distressed exchange 或 going-concern 字眼，也未取得具體到期牆資料。

**判讀：** 三條路徑中最接近的一條，但仍未觸發。CDS 在千點以上意味市場已為違約定價，然而 R3 需要實際的破產、超過寬限期違約或完成 distressed exchange；若窗口內 CoreWeave 類借款人遭遇再融資失敗、主要客戶合約縮減，或 Lambda 式新融資管道關閉，此路徑可能轉為 yes，並可能經由信用傳導觸發 R1。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 於 2026-10-15 達紀錄 1,194.5 bps，報導指 AI 信用疑慮推升科技業違約保險至紀錄高位——信貸端已先於股價重定價 `valuation.ai_credit_schism`
- [整體] HY OAS 由 2.65%（2026-09-11）擴大至 3.23%（2026-10-15），+58 bps，信用環境轉緊 `monetary.hy_oas`
- [整體] Fed 目標區間上緣由 3.75% 升至 4.00%（2026-10-17），CPI YoY 3.72%（2026-09 資料），Fed 在 AI 主導回撤時的緩衝空間有限 `monetary.fed_funds` `monetary.cpi_yoy`
- [R1] 情緒與廣度惡化：CNN Fear & Greed 約 18（極度恐懼，2026-10-16），上漲對下跌家數約 29 對 71（2026-10-16） `retail.fear_greed` `breadth.advance_decline`
- [R1] 10Y 殖利率 5.10%（2026-10-15，+14 bps），實質殖利率 2.78%（+18 bps），對 CAPE 約 40.54 的估值構成折現壓力 `monetary.dgs10` `monetary.dfii10` `valuation.sp500_pe_cape`
- [整體] IPO 市場兩週內第 4 檔撤件或延後（2026-10-16），MOVE 由 82.21 升至 101.1（2026-10-16），風險偏好降溫 `speculation.ipo_heat` `structural.treasury_basis_trade`

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.13%（2026-10-15），距 R1 門檻 23,418.52 還需約 21.77% 跌幅，且高點就在 2026-10-06 `valuation.ndx_drawdown`
- [R2] 四大 hyperscaler 2026 capex 合計約 725（2026-07-28），仍在擴張，目前沒有任何一家被證據顯示下修 `ai.hyperscaler_capex`
- [R3] AI 基礎設施仍可融資：Lambda 於 2026-10-01 取得約 1 十億美元 GPU 擔保融資，未見違約、寬限期或 distressed exchange 跡象 `structural.ai_infrastructure_debt`
- [整體] repo 資金面無失序：SOFR−IORB 為 −1 bps、SOFR99−IORB 為 7 bps（2026-10-15），SRF 動用 0（2026-10-16） `monetary.repo_stress_srf`
- [整體] IG OAS 僅 0.84%（+4 bps，2026-10-15），投資級信用未出現系統性重定價 `monetary.ig_oas`
- [R2] AI 需求端仍在成長：Anthropic 年化 run-rate 約 65（2026-08-17），並據報目標 11 月中上市（2026-10-05） `ai.openai_anthropic_revenue` `speculation.upcoming_ai_ipos`

## 與前期比較

前次結論：無前次預測（report-2026-09-13 為舊格式評分報告）

前次為舊格式評分報告，不轉譯為 yes/no，`flip_evidence` 為空。自 2026-09-13 以來值得注意的變化：

- HY OAS +58 bps、MOVE +18.89、Fed 升息 25 bps，信用與利率波動同步升溫。
- CoreWeave 5Y CDS 於 2026-10-15 創紀錄，R3 路徑的市場定價明顯惡化。
- NASDAQ-100 於 2026-10-06 創 252 日新高，目前回撤僅 4.13%，R1 距離幾乎未縮短。
- 情緒由偏多轉為極度恐懼（Fear & Greed 約 18），但 S&P 500 相對 2026-09-11 僅變動 +0.03%。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- valuation.mag7_multiples（required）：僅取得單一成員 MSFT 的前瞻本益比，無 Mag 7 加權 P/E 與 AI 龍頭 P/S 對十年均值的比較。缺口只影響估值脆弱度判讀，不影響 R1–R3 時點判斷，不會改變結論。
- breadth.rsp_spy（required）：唯一結果為 2026-07-18 的 RSP YTD 數字，早於前次基準日且無 SPY 對照，不是當期快照。對結論影響有限（廣度惡化已由上漲／下跌家數反映）。
- breadth.top10_concentration（required）：唯一結果日期 2026-07-31，早於前次基準日，不是當期快照。集中度屬脆弱度指標，不改變時點判斷。

其他未披露（✗ NOT DISCLOSED）來源中，對答案最可能有影響的是私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）與 GPU / 伺服器折舊年限變動：前者若出現 gate proration / breach 會加強 R3 傳導，後者若出現年限縮短會削弱 capex 回收邏輯。另外 evidence 檔的美債基差交易槓桿列記載「script 三區塊 fetch_failed」，但 macro artifact 三個區塊皆為 `status: ok`；本報告以 artifact 為準記 `✓ API`。

最大不確定性：

1. CoreWeave 等 AI 借款人的到期與再融資時程本次未取得；若窗口內有大額到期而市場仍維持千點級 CDS，R3 會朝 yes 推進。
2. 四大 hyperscaler 的 Q3／Q4 季報 capex 指引：分家數字與日期本次未取得；若出現兩家下修，R2 直接成立。
3. 貨幣政策：Fed 已升息至 3.75%–4.00%、CPI 3.72%、WTI 101.91；若持續升息推高 10Y，可能放大 R1 估值壓縮，偏向 yes；若信用壓力迫使政策轉向，則偏向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest | 7659.44 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 5.34 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest | 29935.59 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 4.13 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026-Q2 資料） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 4.0 | FRED API (series_id=DFEDTARU) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.75 | FRED API (series_id=DFEDTARL) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 3.23 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.84 | FRED API (series_id=BAMLC0A0CM) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 5.1 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.78 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.35 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 101.91 | FRED API (series_id=DCOILWTICO) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 資料） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.33 | FRED API (series_id=T5YIFR) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest | 1.0729 | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.89 | FRED API (series_id=SOFR) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.97 | FRED API (series_id=SOFR99) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.9 | FRED API (series_id=IORB) | 2026-10-18 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest | 0.0 | FRED API (series_id=RPONTTLD) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6755639.0（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5943911.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6250253.0（¥625.03T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.46 | FRED API (series_id=VIXCLS) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 16.46 | FRED API (series_id=VIXCLS, SP500) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2097.9713（$2.10T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -6883343 | CFTC TFF futures-only | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 101.1 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2264.1 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |

補充判讀（皆取自 macro artifact）：10Y Δ 分解 ΔDGS10 +14 bps、ΔDFII10 +18 bps、ΔT10YIE −1 bps，判讀：不可判（視窗不一致）。10Y 期限溢價（term premium）1.0729%（Kim-Wright，2026-10-09，trailing 7d −1.2 bps）。repo 資金壓力（SOFR−IORB）−1 bps、SOFR99−IORB 7 bps（皆 2026-10-15），SRF 動用（Standing Repo Facility usage）0（2026-10-16）。VIX / S&P 500 co-movement：window 2026-10-08 → 2026-10-15（7 天），VIX +6.81%、S&P 500 −0.27%，comove=false。CFTC 槓桿基金淨部位 4 週變動 −309,307 口。household equity allocation 48.23%（2026-Q2）。

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebSearch | ✓ SEARCH-VERIFIED（僅 CAPE；trailing P/E 未取得） |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ⛔ FETCH FAILED（僅單一成員 MSFT 前瞻 P/E，無加權值） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ⛔ FETCH FAILED（僅 2026-07-18 RSP 數字，非當期快照） |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ⛔ FETCH FAILED（僅 2026-07-31 數字，非當期快照） |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey | WebSearch | ✓ SEARCH-VERIFIED（BofA；JPM 未取得） |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py（DFEDTARU ok、DFEDTARL ok） | ✓ API |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | scripts/fetch_macro.py | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | scripts/fetch_macro.py | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） | ✓ API |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch | ✗ NOT DISCLOSED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✗ NOT DISCLOSED（唯一結果為 2026-08-15 的 1–7 月資料，非當期） |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state，沿用最近季報） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch（quarterly_state stock-of-state＋event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch（stock-of-state 組合） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch（quarterly_state stock-of-state＋event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch＋SEC EDGAR（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR＋WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✗ NOT DISCLOSED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED（單一個股槓桿 ETF 合計；個別代號未取得） |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS ok、vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok） | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.54（原定來源 multpl.com） | Shiller PE CAPE ratio current October 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 紀錄 1,194.5 bps | AI credit fears tech default insurance record highs October 2026 | https://www.businessday.co.za/world/international-companies/2026-10-15-ai-credit-fears-push-tech-default-insurance-to-record-highs/（BusinessDay） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| breadth.advance_decline | 上漲家數約 29 對下跌 71 | market breadth October 16 2026 percent above 200-day advance decline | https://www.thetrading.tools/market-breadth（thetrading.tools） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 18（極度恐懼；原定來源 cnn.com） | CNN Fear and Greed Index October 16 2026 extreme fear | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/（finhacker.cz） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-08 月資料）約 1.45 兆美元 | FINRA margin debt August 2026 year over year | https://www.thetrading.tools/margin-debt（thetrading.tools） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.7（週至 2026-10-14） | AAII sentiment survey week ending October 14 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA FMS（2026-10）科技股淨加碼約 37，2020 年 8 月以來最高 | BofA October 2026 fund manager survey tech overweight cash | https://www.bloomberg.com/news/articles/2026-10-13/bofa-poll-shows-investors-most-exposed-to-tech-stocks-since-2020（Bloomberg） | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.77 | Treasury 10-year note auction October 7 2026 bid-to-cover | https://www.rttnews.com/3697286/ten-year-note-auction-attracts-strong-demand.aspx（RTTNews） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 725（2026-Q2 季報後彙整） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65 | OpenAI Anthropic annualized revenue run rate 2026 | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選中位租金約 4.20 | GPU rental price index HBM DRAM contract price October 2026 | https://uvik.net/blog/gpu-price-index/（Uvik） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 2026 年 hyperscaler 發債預估約 190（沿用之 stock-of-state 背景；event_scan 30 日無合格披露） | hyperscaler bond issuance 2026 capex versus free cash flow | https://www.twentyfouram.com/insights/oracle-clears-the-supply-cloud-with-record-demand（TwentyFour AM） | 2026-02-02 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic run-rate 約 65（分母沿用 ai.hyperscaler_capex top-4 合計約 725） | AI revenue versus capex gap 2026 annualized | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement October 2026 | 檢查來源：SEC EDGAR 8-K、SPACInsider、Boardroom Alpha | — | 2026-10-18T09:30:00+08:00 |
| speculation.ipo_heat | 兩週內第 4 檔 IPO 撤件或延後 | IPO market October 16 2026 pulled postponed Firmus Oura | https://www.ipox.com/ipox/the-ipox-update-10162026（IPOX） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描（0 件符合 2+ 主題×弱基本面；PFAI 2026-10-07 +116.7% 落在窗外） | biggest stock gainers week October 12-16 2026 microcap 100% | 檢查來源：Tapeboard movers archive、Financial Modeling Prep daily gainers、Yahoo movers | — | 2026-10-18T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 11 月中上市 | Anthropic IPO October 2026 timing valuation S-1 | https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market（CNN） | 2026-10-05 | 2026-10-18T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件合格；NVDA 2026-10-09 申報無 filing-level 細節） | insider selling Form 4 October 2026 Nvidia AI executives SEC | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-10-18T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.04 | single stock leveraged ETF assets October 2026 weekly flows | https://www.etfaction.com/single-stock-traders-pile-into-tsll-and-intw-as-levered-flows-surge/（ETF Action） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval October 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed | — | 2026-10-18T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 月度 ADV 創紀錄約 3.4 百萬口（2026-09 月資料） | Cboe September 2026 derivatives volume 0DTE SPX record | https://www.cboe.com/insights/posts/market-metrics-that-matter-derivatives-september-2026-volume-highlights（Cboe） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.options_volume | OCC 9 月總結算量約 1,486,062,415 口（2026-09 月資料） | OCC September 2026 monthly volume data | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report（OCC） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 約 14.84、SKEW 154.34 | VIX term structure SKEW October 2026 options brief | https://www.home.saxo/content/articles/options/the-middle-got-cheaper-the-edge-did-not---options-brief---12-october-2026-12102026（Saxo） | 2026-10-12 | 2026-10-18T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-08 月資料）對股票市值比率基數約 1.45 兆美元 | margin debt to market cap August 2026 | https://www.thetrading.tools/margin-debt（thetrading.tools） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
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

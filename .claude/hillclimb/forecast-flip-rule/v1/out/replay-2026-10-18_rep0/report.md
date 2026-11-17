> [DRY RUN] this report was not committed to archive.

# 2026-10-18 AI 泡沫破裂預測報告
報告日期：2026-10-18｜ISO 週次：2026-W42｜預測窗口：2026-10-18 → 2027-04-18｜前次基準：report-2026-09-13（35天前）

## 結論

**結論：no**

三條路徑都還沒有進入「已在途中」的狀態：NASDAQ-100 僅自高點回落 4.13%，距 R1 門檻尚需再跌約 21.77%；四大 hyperscaler 最新 capex 合計仍在 ≈$725bn 的高檔，本次未見任何下修。最接近的是 R3，CoreWeave 5Y CDS 創紀錄 1,194.5 bps（2026-10-15）顯示信用端已在重定價，但本次證據中沒有付款違約、破產申請或 distressed exchange，也沒有確認其負債達 R3 門檻，因此不足以推翻「182 天內三者皆不發生」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,935.59（2026-10-15），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 4.13%（`valuation.ndx_drawdown`）。R1 門檻水位為 23,418.52，需自最新收盤再下跌約 21.77% 才會觸發。脆弱度方面：Shiller CAPE ≈40.54（2026-10-16，`valuation.sp500_pe_cape`），S&P 500 收 7,659.44、高於 200 日均線 5.34%、高於 52 週均線 6.78%（2026-10-16，`valuation.sp500_trend`），估值與價格延伸都偏高。催化與傳導方面：10Y 殖利率 5.10%、實質殖利率 2.78%（2026-10-15，`monetary.dgs10`、`monetary.dfii10`），Fed 目標區間上限自 3.75% 升到 4.00%（`monetary.fed_funds`），CPI YoY 3.72%（2026-09 月資料，`monetary.cpi_yoy`），表示 Fed 緩衝 AI 主導下跌的空間有限；MOVE 自 82.21 升到 101.1（`structural.treasury_basis_trade`），HY OAS 走闊 58 bps 至 3.23%（`monetary.hy_oas`）。情緒面已偏恐慌：CNN Fear & Greed ≈18（極度恐懼，2026-10-16，`retail.fear_greed`），上漲對下跌家數約 29 比 71（2026-10-16，`breadth.advance_decline`）。

**判讀：** R1 距離尚遠，現有回撤僅約門檻的六分之一。要在窗口內成立，需要一個能把 NASDAQ-100 再壓低約 22% 的傳導事件，例如 R3 信用事件外溢、利率再上台階造成估值壓縮，或 Q3／Q4 財報季的 capex 指引轉向；目前恐慌情緒與信用走闊是早期徵兆，但尚不構成已在途中的回撤。

### R2 資本支出收縮

本次取得的 capex 指引證據是四家合計：Microsoft、Alphabet、Amazon、Meta 2026 年 capex 合計約 $725bn（CNBC 2026-07-28，2026 年第二季財報季，`ai.hyperscaler_capex`）。檢索結果沒有逐家列出最新指引數值與相對前次指引的方向（上修／持平／下修），因此本報告無法逐家標註方向。能確認的是：本次檢索沒有發現四家中任何一家下修，目前已下修家數為 0 家（就已取得證據而言）。具體的下次財報日期本次未取得；依季度財報節奏，2026 年第三季與第四季兩輪財報都落在預測窗口（至 2027-04-18）內，是 R2 的兩個主要檢查點。需求側旁證：Anthropic 年化 run-rate 約 $65bn（2026-08-17，`ai.openai_anthropic_revenue`），H100 隨選中位租金約 $4.20（2026-10-07，`ai.compute_supply_demand`），沒有看到需求崩落的訊號；AI 營收對 capex 缺口（revenue-to-capex gap）以已披露數據組合為年化 AI 終端營收 ≈$65bn（僅 Anthropic）vs 2026 capex ≈$725bn（分母：top-4，未含 Oracle），缺口很大，但沒有前次組合值可比較擴大或收斂（`ai.revenue_capex_gap`）。

**判讀：** R2 未見啟動。要在窗口內成立，需在兩輪財報中出現至少兩家下修當年度或次年度 capex 指引；最可能的觸發是 R1 式股價大跌或 R3 信用收緊迫使融資成本上升，但目前沒有任何一家下修的證據。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）出現明確的信用端重定價：CoreWeave 5Y CDS 創紀錄 1,194.5 bps，AI 信用疑慮把科技業違約保險推到紀錄高點（BusinessDay 2026-10-15，`valuation.ai_credit_schism`）。CoreWeave 以 AI 算力為主業，是 R3 最直接的候選借款人，但其負債總額、近期到期債務與再融資需求不在本次證據中，是否跨過 50 億美元門檻需另行確認。AI infrastructure debt financing / vendor-financing loops 方面，Lambda 取得約 $1bn 的 GPU 擔保融資（2026-10-01，`structural.ai_infrastructure_debt`），顯示 neocloud 仍能進入債務市場。本次證據中沒有付款違約、寬限期、covenant waiver、distressed exchange 或 going-concern 文字。整體信用環境：HY OAS 3.23%（+58 bps）（`monetary.hy_oas`），IG OAS 0.84%（+4 bps）（`monetary.ig_oas`），repo 資金壓力（SOFR−IORB）為 −1 bp、SRF 動用為 0（`monetary.repo_stress_srf`），尚未形成系統性資金壓力。

**判讀：** R3 是三條路徑中最接近的一條：CDS 紀錄高位代表市場已為重大信用損失定價。但 R3 需要實際的破產、超過寬限期的違約或完成的 distressed exchange，目前沒有任何此類事件；若窗口內出現再融資失敗、評等連降或主要客戶合約中斷，可能在 182 天內完成，並經由 R1 外溢。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 創紀錄 1,194.5 bps（2026-10-15），AI 信用疑慮推升科技業違約保險至紀錄高點，信用端已在為 AI 算力借款人重定價，而 NASDAQ-100 只回落 4.13%，是典型的信用先行訊號（`valuation.ai_credit_schism`、`valuation.ndx_drawdown`）。
- [整體] 自 2026-09-11 以來 HY OAS 走闊 58 bps 至 3.23%（2026-10-15），MOVE 自 82.21 升至 101.1（2026-10-16），風險溢價與債市波動同步上升（`monetary.hy_oas`、`structural.treasury_basis_trade`）。
- [R1] 利率與政策緩衝受限：10Y 殖利率 5.10%、實質殖利率 2.78%（2026-10-15），Fed 目標區間升至 3.75%–4.00%（2026-10-17），CPI YoY 3.72%（2026-09 月資料），WTI 101.91（2026-10-14），Fed 難以降息托底（`monetary.dgs10`、`monetary.dfii10`、`monetary.fed_funds`、`monetary.cpi_yoy`、`monetary.wti`）。
- [R1] 估值與部位極端：Shiller CAPE ≈40.54（2026-10-16），BofA 10 月 FMS 科技股淨加碼約 37、為 2020 年 8 月以來最高（2026-10-13），部位擁擠使回撤放大的空間大（`valuation.sp500_pe_cape`、`institutional.bofa_jpm_survey`）。
- [整體] 風險偏好轉弱：CNN Fear & Greed ≈18（極度恐懼，2026-10-16），上漲對下跌家數約 29 比 71（2026-10-16），兩週內第 4 檔 IPO 撤件或延後（2026-10-16）（`retail.fear_greed`、`breadth.advance_decline`、`speculation.ipo_heat`）。

## 支持 no 的證據

- [R1] NASDAQ-100 最新收盤 29,935.59（2026-10-15）僅距 52 週高點回撤 4.13%，R1 門檻 23,418.52 需再跌約 21.77%；S&P 500 仍高於 200 日均線 5.34%（2026-10-16），長期趨勢未破（`valuation.ndx_drawdown`、`valuation.sp500_trend`）。
- [R2] 四大 hyperscaler 2026 capex 合計約 $725bn（2026-07-28），本次檢索未發現任何一家下修，R2 需兩家下修才成立，目前為 0 家（`ai.hyperscaler_capex`）。
- [R3] 本次證據中沒有任何 AI 算力借款人的破產、違約或 distressed exchange；Lambda 仍在 2026-10-01 取得約 $1bn GPU 擔保融資，市場融資管道仍開放（`structural.ai_infrastructure_debt`）。
- [整體] 資金市場平穩：repo 資金壓力（SOFR−IORB）為 −1 bp（2026-10-15），SOFR99−IORB 為 7 bps，SRF 動用 0（2026-10-16）；IG OAS 僅 0.84%（2026-10-15）；10Y 美債標售 bid-to-cover 約 2.77、需求強勁（2026-10-07）（`monetary.repo_stress_srf`、`monetary.ig_oas`、`monetary.treasury_auctions`）。
- [R2] AI 需求面未見崩落：Anthropic 年化 run-rate 約 $65bn（2026-08-17）並規劃 11 月中上市（2026-10-05），H100 隨選中位租金約 $4.20（2026-10-07），支撐 capex 計畫延續（`ai.openai_anthropic_revenue`、`speculation.upcoming_ai_ipos`、`ai.compute_supply_demand`）。

## 與前期比較

前次結論：無前次預測（report-2026-09-13 為舊格式評分報告）

前次為舊格式六維度評分報告，不轉換為 yes／no，flip_evidence 為空。自 2026-09-11（前次基準最近交易日）以來的主要變化：

- HY OAS 由 2.65% 升至 3.23%（+58 bps），IG OAS 由 0.80% 升至 0.84%（`monetary.hy_oas`、`monetary.ig_oas`）。
- 10Y 殖利率 +14 bps、實質殖利率 +18 bps、10Y breakeven −1 bp；因 T10YIE 與 DGS10／DFII10 視窗不一致，本次 Δ 歸因判讀：不可判（視窗不一致）（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。
- Fed 目標區間上調 25 bps 至 3.75%–4.00%；IORB 由 3.65% 升至 3.90%（`monetary.fed_funds`、`monetary.repo_stress_srf`）。
- MOVE 由 82.21 升至 101.1；CFTC 槓桿基金美債期貨淨空單 4 週增加 309,307 口至 −6,883,343 口（`structural.treasury_basis_trade`）。
- S&P 500 由 7,656.98 到 7,659.44，幾乎持平（+0.03%）（`valuation.sp500_trend`）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED（檢索完成但窗口內無合格披露）：`valuation.analyst_tp_decomposition`、`retail.social_sentiment`、`retail.naaim`、`monetary.fedwatch`、`monetary.private_credit_liquidity`、`ai.token_growth`、`ai.customer_concentration_rpo`、`ai.hyperscaler_financing_mix`（quarterly_state 有值：2026 年 hyperscaler 發債預估約 $190bn，2026-02-02；event_scan 30 日內無披露）、`ai.depreciation_life`、`ai.capital_cycle`（兩組件皆無可用披露，本次不判定資本週期階段）、`speculation.equity_put_call`、`structural.global_leveraged_approvals`。其中最可能影響答案的是 `monetary.private_credit_liquidity` 與 `ai.hyperscaler_financing_mix` 的 event_scan：若存在未被檢索到的私募信貸 gate proration / breach 或大型 SPV 融資壓力，會提高 R3 的近端可能性；但這兩項缺漏都是「未見事件」而非「事件被遮蔽」，不足以把答案推向 yes。

其他資料限制：`valuation.mag7_multiples` 只取得成員 MSFT 前瞻 P/E 24.5（2026-09-24），未取得 Mag 7 加權 P/E 與 P/S 對 10 年均值；`breadth.rsp_spy`（2026-07-18）與 `breadth.top10_concentration`（2026-07-31）資料日期偏舊，只作背景；`retail.margin_debt` 只有水位約 $1.45T（2026-08 月資料），YoY 與 margin debt／市值比本次未取得；`ai.hyperscaler_capex` 只有四家合計，沒有逐家方向；`structural.leveraged_etf_aum` 只有單一個股槓桿 ETF 總規模，未取得 NVDL、TSLL 等逐檔 AUM。另外，harness 的檢索紀錄寫美債基差交易槓桿的 script 三區塊失敗，但 macro artifact 顯示 `cftc_lev_funds`、`move_index`、`ofr_repo` 皆為 status ok，本報告以 macro artifact 為準。

最大的不確定性：

1. CoreWeave 的負債規模、到期結構與再融資進度（R3）：若確認負債 ≥ 50 億美元且窗口內有大額到期或客戶合約問題，CDS 紀錄高位可能轉成實際信用事件，會把答案推向 yes。
2. 2026 年第三季與第四季 hyperscaler 財報（R2）：任兩家下修 capex 指引即直接成立 yes；若維持或上修，則進一步支持 no。
3. 利率路徑：10Y 已在 5.10%、CPI 3.72%，若 Fed 再升息或期限溢價擴大，估值壓縮可能加速 R1；若通膨回落，Fed 恢復緩衝空間，支持 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 40.54 | https://www.multpl.com/shiller-pe | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.mag7_multiples | MSFT 前瞻 P/E（Mag 7 成員） | 24.5 | https://articlegateway.com/?p=146 | 2026-09-24 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest | 7659.44 | FRED API (series_id=SP500) sp500_trend | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 5.34 | FRED API (series_id=SP500) sp500_trend | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 6.78 | FRED API (series_id=SP500) sp500_trend | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29935.59 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-06 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 4.13 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level | 23418.52 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS（bps，紀錄高位） | 1,194.5 | https://www.businessday.co.za/world/international-companies/2026-10-15-ai-credit-fears-push-tech-default-insurance-to-record-highs/ | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 報酬（%） | 12.08 | https://pro.thestreet.com/market-commentary/rsp-vs-spy-does-diversification-require-equal-weight | 2026-07-18 | 2026-10-18T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度（%） | 38.9 | https://walnutinvest.com/stats/market-concentration-statistics | 2026-07-31 | 2026-10-18T09:30:00+08:00 |
| breadth.advance_decline | 上漲對下跌家數 | 29 對 71 | https://www.thetrading.tools/market-breadth | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed（極度恐懼） | 18 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-08 月資料，兆美元） | 1.45 | https://www.thetrading.tools/margin-debt | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| retail.aaii | AAII 看多比例（%） | 38.7 | https://www.aaii.com/sentimentsurvey | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2，FRED 觀測日 2026-04-01） | 48.2301354474（≈48.23%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-10-18T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA FMS 科技股淨加碼（%，2020-08 以來最高） | 37 | https://www.bloomberg.com/news/articles/2026-10-13/bofa-poll-shows-investors-most-exposed-to-tech-stocks-since-2020 | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 4.0 | FRED API (series_id=DFEDTARU) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.75 | FRED API (series_id=DFEDTARL) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 3.23 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 58.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.84 | FRED API (series_id=BAMLC0A0CM) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 5.1 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | 14.0 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.78 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | 18.0 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.35 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | -1.0 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 101.91 | FRED API (series_id=DCOILWTICO) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.33 | FRED API (series_id=T5YIFR) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 1.0729 | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（序列自身 trailing 7 日） | -1.2 | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.89 | FRED API (series_id=SOFR) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.97 | FRED API (series_id=SOFR99) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.9 | FRED API (series_id=IORB) | 2026-10-18 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover | 2.77 | https://www.rttnews.com/3697286/ten-year-note-auction-attracts-strong-demand.aspx | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,755,639（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,943,911（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（無新觀測） | 6,250,253（¥625.03T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模（兆人民幣） | 22.25 | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm | 2026-08-15 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計（十億美元，2026Q2 財報季） | 725 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate（十億美元） | 65 | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選中位租金（美元／小時） | 4.20 | https://uvik.net/blog/gpu-price-index/ | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic run-rate（十億美元） | 65 | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 分母：top-4 hyperscaler 2026 capex（十億美元） | 725 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| speculation.ipo_heat | 兩週內 IPO 撤件或延後檔數 | 4 | https://www.ipox.com/ipox/the-ipox-update-10162026 | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標上市時點（11 月中） | 11 月中 | https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market | 2026-10-05 | 2026-10-18T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模（十億美元） | 40.04 | https://www.etfaction.com/single-stock-traders-pile-into-tsll-and-intw-as-levered-flows-surge/ | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 月度 ADV（百萬口，2026-09 月資料，紀錄） | 3.4 | https://www.cboe.com/insights/posts/market-metrics-that-matter-derivatives-september-2026-volume-highlights | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.options_volume | OCC 總結算量（口，2026-09 月資料） | 1,486,062,415 | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 水位 | 14.84 | https://www.home.saxo/content/articles/options/the-middle-got-cheaper-the-edge-did-not---options-brief---12-october-2026-12102026 | 2026-10-12 | 2026-10-18T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW | 154.34 | https://www.home.saxo/content/articles/options/the-middle-got-cheaper-the-edge-did-not---options-brief---12-october-2026-12102026 | 2026-10-12 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.46 | FRED API (series_id=VIXCLS) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（窗口 2026-10-08 → 2026-10-15，comove=false） | 16.46 | FRED API (series_id=SP500) vix_spx_comove | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 6.81 | FRED API (series_id=SP500) vix_spx_comove | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -0.27 | FRED API (series_id=SP500) vix_spx_comove | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt／市值比率基數（2026-08 月資料，兆美元） | 1.45 | https://www.thetrading.tools/margin-debt | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Lambda GPU 擔保融資（十億美元） | 1 | https://valueaddvc.com/pulse/ai-data-center-debt-financing-risk-2026 | 2026-10-01 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2097.9713（$2.10T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（口） | -6,883,343 | CFTC TFF cftc_lev_funds | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -309,307 | CFTC TFF cftc_lev_funds | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 101.1 | Yahoo chart API (^MOVE) move_index | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index delta_abs | 18.89 | Yahoo chart API (^MOVE) move_index | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2264.1 | OFR STFM ofr_repo | 2026-10-16 | 2026-10-18T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（multpl） | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch | ✓ SEARCH-VERIFIED（僅成員 MSFT 前瞻 P/E；加權值未取得） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d 且同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-07-18，偏舊） |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-07-31，偏舊） |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED（2026-08 月資料；YoY 與市值比未取得） |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✓ SEARCH-VERIFIED（BofA 10 月；JPM 未取得） |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（FRED BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（FRED BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（FRED DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（FRED T10YIE，FRED 直接取得） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（FRED DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（FRED T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch | ✗ NOT DISCLOSED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok，無新觀測） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED（四家合計；逐家方向未取得） |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED（Anthropic；OpenAI 未取得） |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險 | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch（quarterly_state 沿用；event_scan 30d 無披露） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch＋既有 bullets 組合 | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch（兩組件皆檢索完成、無可用披露） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch＋SEC EDGAR 8-K（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch movers 掃描（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✗ NOT DISCLOSED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED（單一個股槓桿 ETF 總規模；逐檔未取得） |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED（VIX、SKEW；股債相關未取得） |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py 三區塊（cftc_lev_funds、move_index、ofr_repo） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.54（預定來源 multpl／gurufocus） | Shiller PE CAPE ratio current October 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.mag7_multiples | MSFT 前瞻本益比 24.5（預定來源 Mag 7 加權 P/E） | Magnificent 7 forward P/E valuation October 2026 | https://articlegateway.com/?p=146 （articlegateway） | 2026-09-24 | 2026-10-18T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 紀錄 1,194.5 bps | AI credit fears tech default insurance record highs October 2026 | https://www.businessday.co.za/world/international-companies/2026-10-15-ai-credit-fears-push-tech-default-insurance-to-record-highs/ （BusinessDay） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 報酬約 12.08 | RSP equal weight vs SPY YTD performance 2026 | https://pro.thestreet.com/market-commentary/rsp-vs-spy-does-diversification-require-equal-weight （TheStreet Pro） | 2026-07-18 | 2026-10-18T09:30:00+08:00 |
| breadth.top10_concentration | 前十大集中度約 38.9 | S&P 500 top 10 concentration percent record 2026 | https://walnutinvest.com/stats/market-concentration-statistics （Walnut） | 2026-07-31 | 2026-10-18T09:30:00+08:00 |
| breadth.advance_decline | 上漲約 29 對下跌 71 | market breadth October 16 2026 percent above 200-day advance decline | https://www.thetrading.tools/market-breadth （thetrading.tools） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 極度恐懼約 18（預定來源 CNN） | CNN Fear and Greed Index October 16 2026 extreme fear | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ （finhacker） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.margin_debt | margin debt 約 1.45 兆美元（2026-08 月資料，預定來源 FINRA） | FINRA margin debt August 2026 year over year | https://www.thetrading.tools/margin-debt （thetrading.tools） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.7 | AAII sentiment survey week ending October 14 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA FMS 科技股淨加碼約 37，2020-08 以來最高 | BofA October 2026 fund manager survey tech overweight cash | https://www.bloomberg.com/news/articles/2026-10-13/bofa-poll-shows-investors-most-exposed-to-tech-stocks-since-2020 （Bloomberg） | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.77 | Treasury 10-year note auction October 7 2026 bid-to-cover | https://www.rttnews.com/3697286/ten-year-note-auction-attracts-strong-demand.aspx （RTTNews） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate social financing 2026 total | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm （SteelOrbis） | 2026-08-15 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 725（2026Q2 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65 | OpenAI Anthropic annualized revenue run rate 2026 | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選中位租金約 4.20 | GPU rental price index HBM DRAM contract price October 2026 | https://uvik.net/blog/gpu-price-index/ （Uvik） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 2026 年 hyperscaler 發債預估約 190 | hyperscaler bond issuance 2026 capex versus free cash flow | https://www.twentyfouram.com/insights/oracle-clears-the-supply-cloud-with-record-demand （TwentyFour AM） | 2026-02-02 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic run-rate 約 65（分母取自 ai.hyperscaler_capex） | AI revenue versus capex gap 2026 annualized | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement October 2026 | 檢查來源：SEC EDGAR 8-K、SPACInsider、Boardroom Alpha（窗內無合格事件） | — | 2026-10-18T09:30:00+08:00 |
| speculation.ipo_heat | 兩週內第 4 檔 IPO 撤件或延後 | IPO market October 16 2026 pulled postponed Firmus Oura | https://www.ipox.com/ipox/the-ipox-update-10162026 （IPOX） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（0 件符合 2+ 主題×弱基本面） | biggest stock gainers week October 12-16 2026 microcap 100% | 檢查來源：Tapeboard movers archive、Financial Modeling Prep daily gainers、Yahoo movers（PFAI 10/7 +116.7% 落在窗外） | — | 2026-10-18T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 11 月中上市 | Anthropic IPO October 2026 timing valuation S-1 | https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market （CNN） | 2026-10-05 | 2026-10-18T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件合格） | insider selling Form 4 October 2026 Nvidia AI executives SEC | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表（10/9 有申報但無具名申報人／金額等 filing-level 細節） | — | 2026-10-18T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.04 | single stock leveraged ETF assets October 2026 weekly flows | https://www.etfaction.com/single-stock-traders-pile-into-tsll-and-intw-as-levered-flows-surge/ （ETF Action） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval October 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed（窗內無合格核准或上市） | — | 2026-10-18T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 月度 ADV 創紀錄約 3.4 百萬口（2026-09 月資料） | Cboe September 2026 derivatives volume 0DTE SPX record | https://www.cboe.com/insights/posts/market-metrics-that-matter-derivatives-september-2026-volume-highlights （Cboe） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.options_volume | OCC 9 月總結算量約 1,486,062,415 口 | OCC September 2026 monthly volume data | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report （OCC） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 約 14.84、SKEW 154.34 | VIX term structure SKEW October 2026 options brief | https://www.home.saxo/content/articles/options/the-middle-got-cheaper-the-edge-did-not---options-brief---12-october-2026-12102026 （Saxo） | 2026-10-12 | 2026-10-18T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 1.45 兆美元（2026-08 月資料） | margin debt to market cap August 2026 | https://www.thetrading.tools/margin-debt （thetrading.tools） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
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

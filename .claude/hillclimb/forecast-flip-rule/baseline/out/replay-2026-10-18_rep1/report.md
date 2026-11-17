> [DRY RUN] this report was not committed to archive.

# 2026-10-18 AI 泡沫破裂預測報告

報告日期：2026-10-18｜ISO 週次：2026-W42｜預測窗口：2026-10-18 → 2027-04-18｜前次基準：report-2026-09-13（35天前）

## 結論

**結論：no**

三條路徑都還沒有進入「窗口內可完成」的軌道：NASDAQ-100 只比 2026-10-06 的 52 週高點低 4.13%，距 R1 門檻還要再跌約 21.77%；四大 hyperscaler 也還沒有任何一家下修 capex 指引。CoreWeave 5Y CDS 創紀錄的 1,194.5 bps，加上 Fed 在 CPI 3.72% 時升息，是本次最強的反向訊號，但它們代表的是信用壓力在升溫，還不是 R3 所定義的違約或 distressed exchange，所以不足以推翻「182 天內不發生」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,935.59（2026-10-15），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 4.13%。R1 門檻水位為 23,418.52，也就是說，指數要從最新收盤再跌約 21.77% 才會觸發（`valuation.ndx_drawdown`）。高點才在兩週前出現，指數仍貼近頂部：S&P 500 為 7,659.44（2026-10-16），高於 200 日均線 5.34%、高於 52 週均線 6.78%，相對前次基準日幾乎持平（+0.03%）（`valuation.sp500_trend`）。脆弱面正在累積。市場寬度轉弱，上漲對下跌家數約 29 比 71（2026-10-16，`breadth.advance_decline`）；CNN Fear & Greed 約 18，落在極度恐懼區（2026-10-16，`retail.fear_greed`）；但 BofA 10 月調查顯示科技股淨加碼約 37%，為 2020 年 8 月以來最高（`institutional.bofa_jpm_survey`），代表部位仍然擁擠。Shiller CAPE 約 40.54（2026-10-16，`valuation.sp500_pe_cape`）。VIX/S&P 500 co-movement 在 2026-10-08 → 2026-10-15 的 7 日窗口內為 VIX +6.81%、S&P 500 −0.27%，`comove: false`，屬於正常的反向走勢，並非 crowded-optionality 警戒（`structural.vix_spx_comove`）。

**判讀：** R1 距離觸發還很遠。要在 2027-04-18 前成立，需要一次從高點起算 25% 的急跌，觸發點可能是利率與信用同步重定價（10Y 5.10%、HY OAS 走闊、Fed 升息），或是 R3 信用事件外溢。目前擁擠部位加上弱勢寬度，會讓一旦發生的下跌更深；但「已經在跌」的證據只有 4.13%，不足以判定 R1 會在窗口內完成。

### R2 資本支出收縮

本次可取得的官方指引是 2026 Q2 財報季（2026-07-28 CNBC 彙整）四大 hyperscaler 的 2026 capex 合計約 725（十億美元），沿用為現行 stock-of-state 值（`ai.hyperscaler_capex`）。本次證據沒有逐家拆分 Microsoft、Alphabet、Amazon、Meta 各自的指引數字，也沒有各家相對前次指引的方向，因此四家各自是上修、持平或下修無法逐一標註，只能記為「本次證據未逐家揭露」。同一篇報導以「Alphabet 財報遭市場冷對待、capex 受到更多審視」為題，代表市場對 capex 的耐心在下降，但沒有任何一家下修的披露。目前已下修家數：0（就已取得證據而言）。下一輪季報（2026 Q3）應會落在窗口內，但確切日期不在本次證據中。需求端方面，Anthropic 年化 run-rate 約 65（十億美元，2026-08-17，`ai.openai_anthropic_revenue`）；H100 隨選中位租金約 4.20 美元/小時（2026-10-07，`ai.compute_supply_demand`），本次沒有配套的利用率或庫存證據，因此不判定為產能過剩。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 65（僅 Anthropic）對年化 capex 約 725（分母：top-4，不含 Oracle），比值約 9%，缺口仍大，但沒有新的組件披露可判斷缺口是擴大還是收斂（`ai.revenue_capex_gap`）。

**判讀：** R2 尚未啟動。要成立，四家中至少兩家必須在窗口內兩次季報（2026 Q3、2026 Q4）之中下修指引。較可能的觸發是 R1 式的股價重挫，或融資成本上升（10Y 5.10%、Fed 升息）迫使管理層收縮；但截至目前沒有任何一家轉向，只有市場審視在升溫。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）在這次明顯朝信用端重定價：CoreWeave 5Y CDS 創紀錄的 1,194.5 bps，報導標題為「AI credit fears push tech default insurance to record highs」（2026-10-15，`valuation.ai_credit_schism`）。以常見的 40% 回收率假設粗算，這個水位對應年化違約強度約 20%，半年累計約一成。這是困境區的定價，但仍不是違約。AI infrastructure debt financing / vendor-financing loops 方面，30 日內有 Lambda 約 10 億美元的 GPU 擔保融資（2026-10-01，`structural.ai_infrastructure_debt`），顯示 neocloud 仍能取得資金。整體高收益信用同步走闊：HY OAS 3.23%，較前次基準 +58 bps（2026-10-15，`monetary.hy_oas`）；IG OAS 只有 0.84%（+4 bps，`monetary.ig_oas`）。本次證據沒有載明 CoreWeave、Lambda 或其他借款人的負債總額、近期到期牆，也沒有付款違約、covenant waiver、distressed exchange 或 going-concern 等字眼，因此無法逐一確認誰跨過 50 億美元門檻。以 CDS 水位來看，CoreWeave 是最值得追蹤的候選者。

**判讀：** 三條路徑中 R3 最接近，因為 CDS 已經創下紀錄；但市場本身定價的半年違約可能性仍約一成，而且 Lambda 這類融資仍在進行，信用市場尚未關門。要在窗口內成立，需要有負債 ≥ 50 億美元的 AI 算力借款人出現超過寬限期的付款違約、破產申請，或完成 distressed exchange。最可能的路徑是再融資受阻加上客戶合約重談。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 達 1,194.5 bps 的紀錄高位（2026-10-15），AI 信用端已開始重定價，股價卻還貼近高點，屬於後期分歧訊號（`valuation.ai_credit_schism`）。
- [整體] 利率端沒有緩衝：Fed 目標區間上調至 3.75%–4.00%（較前次 +25 bps，2026-10-17），CPI YoY 3.72%（2026-09 資料），WTI 101.91 美元（2026-10-14），代表 AI 主導的下跌很難等到 Fed 降息托底（`monetary.fed_funds`、`monetary.cpi_yoy`、`monetary.wti`）。
- [R1] 10Y 殖利率 5.10%、實質殖利率 2.78%（2026-10-15），前次以來分別 +14 bps 與 +18 bps，長天期折現率上升對高 duration 的 AI 股估值最不利（`monetary.dgs10`、`monetary.dfii10`）。
- [R3] HY OAS 自 2.65% 走闊至 3.23%（+58 bps，2026-10-15），MOVE 自 82.21 升至 101.1（2026-10-16），信用與債市波動同步升溫（`monetary.hy_oas`、`structural.treasury_basis_trade`）。
- [R1] 部位擁擠而寬度轉弱：BofA 10 月調查科技股淨加碼約 37%，為 2020 年 8 月以來最高（2026-10-13）；上漲對下跌家數約 29 比 71（2026-10-16）；Shiller CAPE 約 40.54（2026-10-16）（`institutional.bofa_jpm_survey`、`breadth.advance_decline`、`valuation.sp500_pe_cape`）。
- [整體] 風險偏好開始退潮：兩週內已有第 4 檔 IPO 撤件或延後（2026-10-16），CNN Fear & Greed 約 18（2026-10-16）（`speculation.ipo_heat`、`retail.fear_greed`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.13%（2026-10-15），高點才在 2026-10-06 創下；要到 R1 門檻 23,418.52 還需再跌約 21.77%，182 天內完成這種幅度並不常見（`valuation.ndx_drawdown`）。
- [R2] 四大 hyperscaler 2026 capex 合計約 725（十億美元，2026-07-28），本次證據中沒有任何一家下修指引，R2 需要兩家轉向，目前是 0 家（`ai.hyperscaler_capex`）。
- [R3] 資金面沒有失序：SOFR−IORB 為 −1 bp、SOFR99−IORB 為 +7 bps（2026-10-15），SRF（RPONTTLD）動用 0（2026-10-16）；IG OAS 只有 0.84%；10Y 標售 bid-to-cover 約 2.77、需求強勁（2026-10-07）（`monetary.repo_stress_srf`、`monetary.ig_oas`、`monetary.treasury_auctions`）。
- [R3] AI 算力借款人仍能融資：Lambda 約 10 億美元 GPU 擔保融資（2026-10-01）；單一個股槓桿 ETF 規模約 40.04（十億美元）、資金持續流入（2026-10-16），代表風險資本尚未撤離（`structural.ai_infrastructure_debt`、`structural.leveraged_etf_aum`）。
- [整體] AI 需求端仍在擴張：Anthropic 年化 run-rate 約 65（十億美元，2026-08-17），並以 11 月中上市為目標（2026-10-05），一級市場仍願意承接大型 AI 發行（`ai.openai_anthropic_revenue`、`speculation.upcoming_ai_ipos`）。
- [R1] S&P 500 仍高於 200 日均線 5.34%（2026-10-16），VIX/S&P 500 未出現同向上升（`comove: false`，2026-10-15），價格趨勢尚未破壞（`valuation.sp500_trend`、`structural.vix_spx_comove`）。

## 與前期比較

前次結論：無前次預測（report-2026-09-13 為舊格式評分報告）

前次為舊格式評分報告，其分數不轉換為 yes/no；以下僅彙整自 2026-09-13 以來的重要數據變化：

- Fed 目標區間由 3.50%–3.75% 上調至 3.75%–4.00%，IORB 由 3.65% 升至 3.90%（`monetary.fed_funds`、`monetary.repo_stress_srf`）。
- 10Y 殖利率 4.96% → 5.10%（+14 bps）、DFII10 2.60% → 2.78%（+18 bps）、T10YIE 2.36% → 2.35%（−1 bp）；三腿視窗不一致，Δ 分解判讀為不可判（視窗不一致）（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。
- HY OAS 2.65% → 3.23%（+58 bps），IG OAS 0.80% → 0.84%（+4 bps）（`monetary.hy_oas`、`monetary.ig_oas`）。
- MOVE 82.21 → 101.1；CFTC 槓桿基金美債期貨淨空部位 4 週擴大 309,307 口至 −6,883,343 口（2026-10-13）（`structural.treasury_basis_trade`）。
- S&P 500 7,656.98 → 7,659.44（+0.03%）；NASDAQ-100 在 2026-10-06 創 52 週高點後回落 4.13%（`valuation.sp500_trend`、`valuation.ndx_drawdown`）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源檢索成功但沒有合格的當期披露（✗ NOT DISCLOSED），不作為證據引用：`valuation.analyst_tp_decomposition`、`retail.social_sentiment`、`retail.naaim`、`monetary.fedwatch`、`monetary.private_credit_liquidity`、`ai.token_growth`、`ai.customer_concentration_rpo`、`ai.hyperscaler_financing_mix`（quarterly_state 有 2026-02-02 的 2026 年 hyperscaler 發債預估約 190（十億美元）作背景；30 日 event_scan 無披露）、`ai.depreciation_life`、`ai.capital_cycle`（兩個組件皆無披露，本次不判定資本週期階段）、`speculation.equity_put_call`、`structural.global_leveraged_approvals`。其中 `monetary.private_credit_liquidity` 與 `ai.hyperscaler_financing_mix` 的事件掃描缺漏最可能影響 R3 判讀：若窗口內出現私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）或大型 hyperscaler 表外融資，R3 與 R1 的傳導會加快。不過本次的缺漏是「無披露」而非「抓取失敗」，不會改變結論。

資料品質注意：

- `breadth.rsp_spy`（RSP YTD 約 12.08%，資料日 2026-07-18）與 `breadth.top10_concentration`（前十大集中度約 38.9%，2026-07-31）只取得約三個月前的快照，也沒有 SPY 的對照值，因此不作為證據引用。
- `valuation.mag7_multiples` 只取得成員 MSFT 的前瞻 P/E 24.5（2026-09-24），Mag 7 加權 P/E 與 AI 龍頭 P/S 對 10 年均值都沒有取得。
- `retail.margin_debt` 只有 2026-08 的水位（約 1.45 兆美元），YoY 與 margin debt／股票市值比率都沒有取得。
- `ai.hyperscaler_capex` 只有四家合計值，沒有逐家指引與方向。這是 R2 判讀最大的資料缺口；若逐家資料顯示已有一家在 Q2 下修，R2 的距離會縮短。
- 檢索紀錄寫明 `structural.treasury_basis_trade` 的三個腳本區塊皆為 fetch_failed，但交付的 macro artifact 顯示 `cftc_lev_funds`、`move_index`、`ofr_repo` 都是 `status: ok` 且在 14 日窗口內。本報告以 artifact（validator 驗證的依據）為準，記為 ✓ API；兩份紀錄互相矛盾，正式執行時應先追查。

最大的不確定性：

1. **2026 Q3 hyperscaler 季報（預期在窗口內，確切日期未取得）**：若有兩家下修，R2 會直接成立，答案翻為 yes；若持續上修，則強化 no。
2. **CoreWeave 等 AI 算力借款人的再融資**：CDS 1,194.5 bps 代表市場預期再融資條件會惡化；負債規模與到期牆本次沒有取得。一旦出現 distressed exchange 或付款違約，答案就會偏向 yes，並可能經由 R1 傳導。
3. **Fed 政策路徑**：本次未取得 CME FedWatch 快照。若 CPI 3.72% 與 WTI 約 100 美元迫使 Fed 繼續升息，10Y 5% 以上的折現率壓力會推向 yes；若通膨回落、Fed 暫停，則支持 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7659.44 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend ma200 | 7271.44 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 5.34 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 6.78 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（相對前次基準） | 0.03 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29935.59 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.13 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2 觀測，家戶股票配置 %） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-10-18T09:30:00+08:00 |
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
| monetary.t10yie | T10YIE delta_bps | -1.0 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl） | 101.91 | FRED API (series_id=DCOILWTICO) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.33 | FRED API (series_id=T5YIFR) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 1.0729 | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7d） | -1.2 | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.89 | FRED API (series_id=SOFR) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.97 | FRED API (series_id=SOFR99) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.9 | FRED API (series_id=IORB) | 2026-10-18 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps（SOFR−IORB，同日 2026-10-15） | -1.0 | FRED API (series_id=SOFR, IORB) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr99_iorb_bps（SOFR99−IORB，同日 2026-10-15） | 7.0 | FRED API (series_id=SOFR99, IORB) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.walcl | WALCL latest（百萬美元） | 6,755,639（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（百萬歐元） | 5,943,911（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（億日圓） | 6,250,253（¥625.03T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.46 | FRED API (series_id=VIXCLS) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of） | 16.46 | FRED API (series_id=VIXCLS / SP500) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（2026-10-08 → 2026-10-15） | 6.81 | FRED API (series_id=VIXCLS / SP500) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（2026-10-08 → 2026-10-15） | -0.27 | FRED API (series_id=VIXCLS / SP500) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（十億美元） | 2,097.9713（$2.10T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG chg_pct | 2.14 | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -6,883,343 | CFTC TFF futures-only | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -309,307 | CFTC TFF futures-only | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 101.1 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index delta_abs（相對 2026-09-11） | 18.89 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2264.1 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED（僅取得 CAPE；S&P 500 P/E 未取得） |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch | ✓ SEARCH-VERIFIED（僅取得成員 MSFT 前瞻 P/E；加權 P/E 與 P/S 對 10 年均值未取得） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED（無同季合格 TP 上調） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API（sp500_trend ok） |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API（ndx_drawdown ok） |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch 14d | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-07-18，偏舊；無 SPY 對照） |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-07-31，偏舊） |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch（stock-of-state，2026-08 月資料） | ✓ SEARCH-VERIFIED（YoY 與市值比率未取得） |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch 7d | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API（BOGZ1FL153064486Q ok） |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch（primary: SEARCH） | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✓ SEARCH-VERIFIED（BofA 10 月調查；JPM 未取得） |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（FRED API） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（FRED BAMLH0A0HYM2） | ✓ API（BAMLH0A0HYM2 ok） |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（FRED BAMLC0A0CM） | ✓ API（BAMLC0A0CM ok） |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（FRED DGS10） | ✓ API（DGS10 ok） |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED DFII10） | ✓ API（DFII10 ok） |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（FRED T10YIE） | ✓ API（T10YIE ok，FRED 直取） |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（FRED DCOILWTICO） | ✓ API（DCOILWTICO ok） |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（FRED CPIAUCSL yoy_pct） | ✓ API（CPIAUCSL ok） |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（FRED T5YIFR） | ✓ API（T5YIFR ok） |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（FRED THREEFYTP10，Kim-Wright） | ✓ API（THREEFYTP10 ok） |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress（FRED API） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch 14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch） | ✗ NOT DISCLOSED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（FRED WALCL） | ✓ API（WALCL ok） |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（FRED ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing / liquidity operations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch 30d | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state，沿用 2026 Q2 財報季） | ✓ SEARCH-VERIFIED（僅四家合計；逐家指引未取得） |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED（Anthropic；OpenAI 未取得） |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch（quarterly_state stock-of-state；event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch＋既有 bullets 組合 | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動（depreciation useful-life change） | WebSearch 30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch（quarterly_state stock-of-state；event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch 7d（SEC EDGAR 8-K、SPACInsider、Boardroom Alpha） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch 7d | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch 7d（movers 篩選） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch 30d | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 14d＋WebSearch | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✗ NOT DISCLOSED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED（單一個股槓桿 ETF 合計；個別代號 AUM 未取得） |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR ETF 申報＋ETF.com 新上市 feed 30d | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch 7d（KRX、TWSE、JPX、ESMA、ETFGI） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED（VIX、SKEW；股債相關性未取得） |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（FRED VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（僅交叉確認） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch 30d | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API（LNFACBW027SBOG ok） |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds、move_index、ofr_repo（aggregation any） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.54 | Shiller PE CAPE ratio current October 2026 multpl | https://www.multpl.com/shiller-pe （multpl；預定來源 multpl.com / gurufocus.com） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 成員 MSFT 前瞻 P/E 24.5 | Magnificent 7 forward P/E valuation October 2026 | https://articlegateway.com/?p=146 （articlegateway；預定來源 Mag 7 加權 P/E） | 2026-09-24 | 2026-10-18T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 紀錄 1,194.5 bps | AI credit fears tech default insurance record highs October 2026 | https://www.businessday.co.za/world/international-companies/2026-10-15-ai-credit-fears-push-tech-default-insurance-to-record-highs/ （BusinessDay） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 報酬約 12.08% | RSP equal weight vs SPY YTD performance 2026 | https://pro.thestreet.com/market-commentary/rsp-vs-spy-does-diversification-require-equal-weight （TheStreet Pro） | 2026-07-18 | 2026-10-18T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度約 38.9% | S&P 500 top 10 concentration percent record 2026 | https://walnutinvest.com/stats/market-concentration-statistics （Walnut） | 2026-07-31 | 2026-10-18T09:30:00+08:00 |
| breadth.advance_decline | 上漲約 29 對下跌約 71 | market breadth October 16 2026 percent above 200-day advance decline | https://www.thetrading.tools/market-breadth （thetrading.tools） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 18（極度恐懼） | CNN Fear and Greed Index October 16 2026 extreme fear | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ （FinHacker；預定來源 cnn.com） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-08 月資料）約 1.45 兆美元 | FINRA margin debt August 2026 year over year | https://www.thetrading.tools/margin-debt （thetrading.tools；預定來源 FINRA） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.7%（週止 2026-10-14） | AAII sentiment survey week ending October 14 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA FMS 科技股淨加碼約 37%，2020 年 8 月以來最高 | BofA October 2026 fund manager survey tech overweight cash | https://www.bloomberg.com/news/articles/2026-10-13/bofa-poll-shows-investors-most-exposed-to-tech-stocks-since-2020 （Bloomberg） | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.77（需求強勁） | Treasury 10-year note auction October 7 2026 bid-to-cover | https://www.rttnews.com/3697286/ten-year-note-auction-attracts-strong-demand.aspx （RTTNews） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| monetary.pboc | 2026 年 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate social financing 2026 total | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm （SteelOrbis） | 2026-08-15 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 725（十億美元，2026 Q2 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65（十億美元） | OpenAI Anthropic annualized revenue run rate 2026 | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選中位租金約 4.20 美元/小時 | GPU rental price index HBM DRAM contract price October 2026 | https://uvik.net/blog/gpu-price-index/ （Uvik） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 2026 年 hyperscaler 發債預估約 190（十億美元） | hyperscaler bond issuance 2026 capex versus free cash flow | https://www.twentyfouram.com/insights/oracle-clears-the-supply-cloud-with-record-demand （TwentyFour AM） | 2026-02-02 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 分子：Anthropic 年化 run-rate 約 65（十億美元） | AI revenue versus capex gap 2026 annualized | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 分母：top-4 hyperscaler 2026 capex 合計約 725（十億美元，沿用 ai.hyperscaler_capex） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement October 2026 | 檢查來源：SEC EDGAR 8-K、SPACInsider、Boardroom Alpha（窗內無合格事件） | — | 2026-10-18T09:30:00+08:00 |
| speculation.ipo_heat | 兩週內第 4 檔 IPO 撤件或延後 | IPO market October 16 2026 pulled postponed Firmus Oura | https://www.ipox.com/ipox/the-ipox-update-10162026 （IPOX） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描（0 件符合 2+ 主題×弱基本面；PFAI 2026-10-07 +116.7% 落在窗外） | biggest stock gainers week October 12-16 2026 microcap 100% | 檢查來源：Tapeboard movers archive、Financial Modeling Prep daily gainers、Yahoo movers | — | 2026-10-18T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 11 月中上市 | Anthropic IPO October 2026 timing valuation S-1 | https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market （CNN） | 2026-10-05 | 2026-10-18T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件合格；NVDA 2026-10-09 有申報但無具名申報人／金額等 filing-level 細節） | insider selling Form 4 October 2026 Nvidia AI executives SEC | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-10-18T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.04（十億美元），TSLL 等資金流入 | single stock leveraged ETF assets October 2026 weekly flows | https://www.etfaction.com/single-stock-traders-pile-into-tsll-and-intw-as-levered-flows-surge/ （ETF Action；預定來源 etf.com / ETFGI） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval October 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed（窗內無合格核准或上市） | — | 2026-10-18T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 月度 ADV 創紀錄約 3.4 百萬口（2026-09） | Cboe September 2026 derivatives volume 0DTE SPX record | https://www.cboe.com/insights/posts/market-metrics-that-matter-derivatives-september-2026-volume-highlights （Cboe） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.options_volume | OCC 2026-09 總結算量約 1,486,062,415 口 | OCC September 2026 monthly volume data | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report （OCC） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 約 14.84、Cboe SKEW 154.34 | VIX term structure SKEW October 2026 options brief | https://www.home.saxo/content/articles/options/the-middle-got-cheaper-the-edge-did-not---options-brief---12-october-2026-12102026 （Saxo） | 2026-10-12 | 2026-10-18T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-08 月資料）約 1.45 兆美元，作市值比率交叉確認基數 | margin debt to market cap August 2026 | https://www.thetrading.tools/margin-debt （thetrading.tools；預定來源 FINRA） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
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
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 4.13,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

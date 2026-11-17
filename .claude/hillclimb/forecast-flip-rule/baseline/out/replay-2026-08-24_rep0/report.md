> [DRY RUN] this report was not committed to archive.

# 2026-08-24 AI 泡沫破裂預測報告

報告日期：2026-08-24｜ISO 週次：2026-W35｜預測窗口：2026-08-24 → 2027-02-22｜前次基準：report-2026-08-20（4天前）

## 結論

**結論：no**

三條路徑目前都離觸發很遠：NASDAQ-100 只比 2026-06-02 高點低 4.41%，要觸及 R1 門檻還得再跌約 21.54%；HY OAS 2.75%、IG OAS 0.82%（2026-08-20），信用市場沒有開始重定價，也沒有任何 hyperscaler 下修 capex 的披露（top-4 合計 2026 capex ≈$725bn，+77% YoY）。估值與槓桿雖然偏高，說明泡沫存在、下跌時傷害大，但窗口內缺少已啟動的催化與傳導，不足以推翻基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,308.86（2026-08-21），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 4.41%（`valuation.ndx_drawdown`）。R1 門檻是 22,995.45（高點 × 0.75）；以最新收盤計，指數還得再跌約 21.54% 才會觸發。脆弱度方面：S&P 500 收在 7,674.37（2026-08-21），高於 200 日均線 8.15%、高於 52 週均線 9.61%（`valuation.sp500_trend`）；Shiller CAPE ≈41.2，trailing P/E ≈26.2（`valuation.sp500_pe_cape`）；Mag 7 加權 P/E ≈29.5x（`valuation.mag7_multiples`）；top-10 集中度 ≈36.5%（`breadth.top10_concentration`）。槓桿面，margin debt（2026-07）YoY ≈+38.6%，但 MoM −5.7%（`retail.margin_debt`）；美股槓桿 ETF AUM 創新高，約 $198bn（`structural.leveraged_etf_aum`）。VIX 與 S&P 500 在 2026-08-13 → 2026-08-20 的 7 日窗內是 VIX +9.43%、S&P 500 −2.02%，屬正常的反向走勢，沒有出現 crowded-optionality 同漲訊號（`structural.vix_spx_comove`）。情緒面沒有過熱：CNN Fear & Greed 55（`retail.fear_greed`）；AAII 偏多 35.5%、偏空 39.9%（`retail.aaii`）。窗口內可能的催化：Anthropic 據報目標 10 月 IPO、估值 ≈$2T（`speculation.upcoming_ai_ipos`），這會帶來大量新股供給；FedWatch 定價 9/16 按兵不動 ≈68.4%，尾端情境是升息（`monetary.fedwatch`）。

**判讀：** 距離門檻還很遠（約 21.54%）。要在窗口內觸發，需要估值大幅壓縮的催化，例如 R2/R3 先出事、通膨迫使 Fed 轉向升息，或大型 IPO 供給加上槓桿 ETF／margin 被迫去槓桿形成連鎖賣壓。目前這些傳導都還沒啟動。

### R2 資本支出收縮

最新可得的 hyperscaler capex 證據（2026-08-13，Q2 2026 財報季後的彙整）是 top-4（Microsoft、Alphabet、Amazon、Meta）2026 capex 合計 ≈$725bn、+77% YoY（`ai.hyperscaler_capex`）。各家逐一來看：

- Microsoft：本次證據只有 top-4 合計，沒有逐家拆出指引數值；相較前次指引的方向，本次證據未揭露，也沒有任何下修披露。
- Alphabet：同上，僅有合計、無逐家數值；未見下修披露。
- Amazon：同上，僅有合計、無逐家數值；未見下修披露。
- Meta：同上，僅有合計、無逐家數值；未見下修披露。

已確認下修的家數：0／4。下次財報的確切日期本次證據沒有提供；依季報節奏，窗口內（至 2027-02-22）應會涵蓋 Q3 2026（約 10 月下旬）與 Q4 2026（約 1 月下旬至 2 月初）兩輪財報，但這只是節奏推估，不是已確認日期。需求面目前支撐 capex：Anthropic 年化營收 ≈$65B、OpenAI ≈$40B（`ai.openai_anthropic_revenue`）；Anthropic run-rate 年增約 7 倍（`ai.token_growth`）；GPU 現貨租金高於合約價 2 倍以上，新增產能被利用率吸收（`ai.compute_supply_demand`）。反方向的壓力來自 AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收 ≈$105bn，對比年化 capex ≈$725bn（分母只含 top-4：MSFT／GOOGL／AMZN／META；Oracle 沒有可組合的數值，未納入），缺口很大（`ai.revenue_capex_gap`）。因為前次是舊格式評分報告，沒有可比的組合值，本次無法判斷缺口是擴大還是收斂。

**判讀：** 尚未啟動。目前是全面擴張，沒有任何一家下修。要在窗口內觸發，需要在 Q3／Q4 財報中有兩家下修當年度或次年度指引，最可能的前提是需求端（GPU 利用率、AI 營收成長）明顯轉弱，或 R1 回撤迫使管理層收縮。目前證據指向相反方向。

### R3 AI 信用事件

本次對 AI 信用定價分歧（equity-vs-credit schism）與 AI infrastructure debt financing / vendor-financing loops 的 14 日／30 日掃描都完成了，但都沒有找到窗口內的合格披露。因此，本次無法列出任何符合 R3 規模門檻（負債 ≥ USD 5bn、以 AI 資料中心／算力為主業）的候選借款人的當期利差、CDS、評等動作或近期到期資料，也沒有找到任何付款違約、covenant waiver、distressed exchange 或 going-concern 措辭的披露。整體信用環境仍然寬鬆：HY OAS 2.75%（`monetary.hy_oas`）、IG OAS 0.82%（`monetary.ig_oas`），兩者都是 2026-08-20 的數值，相對前次無變動。資金面方面：repo 資金壓力（SOFR−IORB）為 −2.0bp，SOFR99−IORB 為 6.0bp（2026-08-20）；SRF 動用（Standing Repo Facility usage）為 0（2026-08-21）（`monetary.repo_stress_srf`）。銀行對 NBFI 放款約 $2.03T（2026-08-12，週變動 0）（`structural.nbfi_bank_loans`）。

**判讀：** 證據上離觸發最遠。R3 需要大型 AI 算力借款人實際違約或完成 distressed exchange，通常會先出現信用利差走闊、再融資受阻與評等下調等前兆，而本次可觀察的信用與資金指標都沒有這些前兆。主要盲點是個別 neocloud 發行人的當期定價本次沒有取得，詳見資料缺漏。

## 支持 yes 的證據

- [R1] 估值處於歷史極端：Shiller CAPE ≈41.2、trailing P/E ≈26.2（2026-08-20，`valuation.sp500_pe_cape`），Mag 7 加權 P/E ≈29.5x（2026-08-14，`valuation.mag7_multiples`），S&P 500 top-10 集中度 ≈36.5%（2026-08-17，`breadth.top10_concentration`）。一旦出現催化，下跌幅度可能很大。
- [R1] 槓桿堆積：margin debt（2026-07）YoY ≈+38.6%，接近歷史頂部常見的 +40–50% 區間（`retail.margin_debt`）；美股槓桿 ETF AUM 創新高，約 $198bn，其中 TQQQ ≈$31.3bn、SOXL ≈$17.3bn（2026-08-17，`structural.leveraged_etf_aum`）；SPX 0DTE 佔比創紀錄，約 62.4%（2026-08-14，`structural.zero_dte`）。回撤時可能觸發被迫去槓桿。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）很大：年化 AI 終端營收 ≈$105bn，對比 top-4 年化 capex ≈$725bn（2026-08-17，`ai.revenue_capex_gap`、`ai.hyperscaler_capex`）。如果回報遲遲沒有跟上，未來的指引存在下修壓力。
- [整體] Fed 緩衝空間有限：CPI YoY 3.3%（2026-07，`monetary.cpi_yoy`），FedWatch 定價 9/16 按兵不動 ≈68.4%、尾端為升息（2026-08-20，`monetary.fedwatch`），10Y 殖利率 4.69%（2026-08-20，`monetary.dgs10`），10Y 期限溢價（term premium）0.8393%（2026-08-14，`monetary.term_premium`），WTI $86.48（2026-08-18，`monetary.wti`）。如果發生 AI 引領的回撤，降息救市的空間受限。
- [R1] 窗口內有供給催化：Anthropic 據報目標 10 月 IPO、估值 ≈$2T（2026-08-17，`speculation.upcoming_ai_ipos`）；S&P 500 高於 200 日均線 8.15%（2026-08-21，`valuation.sp500_trend`），均值回歸的空間不小。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.41%（2026-08-21 收盤 29,308.86，對比 2026-06-02 高點 30,660.60），要觸及 R1 門檻 22,995.45 還得再跌約 21.54%（`valuation.ndx_drawdown`）。
- [R3] 信用市場沒有重定價：HY OAS 2.75%、IG OAS 0.82%（2026-08-20，`monetary.hy_oas`、`monetary.ig_oas`），沒有出現 R3 通常需要的利差走闊前兆。
- [R2] capex 仍在擴張：top-4 2026 capex 合計 ≈$725bn、+77% YoY，沒有任何下修披露（2026-08-13，`ai.hyperscaler_capex`）；GPU 現貨租金高於合約價 2 倍以上，產能被利用率吸收（2026-08-13，`ai.compute_supply_demand`）。
- [R2] 終端需求快速成長：Anthropic 年化營收 ≈$65B、OpenAI ≈$40B（2026-08-17，`ai.openai_anthropic_revenue`）；Anthropic run-rate 年增約 7 倍（2026-08-17，`ai.token_growth`）。這支撐 capex 指引維持或上修。
- [整體] 資金與國債市場平穩：repo 資金壓力（SOFR−IORB）−2.0bp、SRF 動用 0（`monetary.repo_stress_srf`）；MOVE 73.4（2026-08-21），美債期貨槓桿基金淨空部位近 4 週縮小 244,468 口（`structural.treasury_basis_trade`）；銀行對 NBFI 放款約 $2.03T，持平（`structural.nbfi_bank_loans`）。
- [R1] 情緒與投機沒有過熱：CNN Fear & Greed 55（2026-08-21，`retail.fear_greed`）；AAII 偏空 39.9% 高於偏多 35.5%（`retail.aaii`）；RSP 的 YTD 表現領先 SPY 約 5pp，廣度擴散（`breadth.rsp_spy`、`breadth.advance_decline`）；microcap moonshot 與 +AI 改名／SPAC 掃描都是 0 件（`speculation.microcap_moonshots`、`speculation.ai_rename_spac`）。

## 與前期比較

前次結論：無前次預測（report-2026-08-20 為舊格式評分報告）

前次是舊格式評分報告，不把它的評分換算成 yes/no；本次是第一個 yes/no 預測，flip_evidence 為空。自 2026-08-20 以來的主要變化：

- 10Y 拆解：ΔDGS10、ΔDFII10、ΔT10YIE 都是 0bp，判讀為無變動。其中 DGS10 與 DFII10 沒有新觀測（stale_series，最新仍是 2026-08-20），T10YIE 有更新到 2026-08-21，Δ 同樣為 0。
- S&P 500 由 7,641.16（2026-08-20）升到 7,674.37（2026-08-21），+0.43%。
- MOVE 由 73.18 升到 73.4；OFR tri-party repo transaction volume 由 $2,400.4bn 降到 $2,328.6bn（−2.99%）。這些都屬於雜訊等級的變動。
- 10Y 期限溢價（term premium）在序列自身的 trailing 7 日內 +1.4bp，來到 0.8393%（2026-08-14）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源的檢索已完成，但窗口內沒有合格披露（✗ NOT DISCLOSED），本次不作為證據引用：`valuation.analyst_tp_decomposition`、`valuation.ai_credit_schism`、`retail.social_sentiment`、`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.pboc`、`monetary.private_credit_liquidity`、`ai.customer_concentration_rpo`、`ai.hyperscaler_financing_mix`（quarterly_state 有取得：top-5 capex 已超過 FCF、2026 發債擴張；event_scan 在 30 日內沒有新事件）、`ai.depreciation_life`、`ai.capital_cycle`（quarterly_state 有取得：供給側 capex 年增 ≈77%；event_scan 在 30 日內沒有新事件）、`structural.global_leveraged_approvals`、`structural.ai_infrastructure_debt`。其中對答案影響最大的是 `valuation.ai_credit_schism` 與 `structural.ai_infrastructure_debt`：R3 的候選借款人本次沒有逐一取得當期利差或到期資料。如果其中有正在惡化的 neocloud 再融資，R3 的距離可能比本文估計的近。不過整體 HY／IG OAS 處於低檔，大型 AI 信用事件通常會先外溢到整體利差，因此判斷這個缺口目前不足以翻轉答案。`monetary.private_credit_liquidity` 也沒有披露，所以私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）這條傳導本次無法驗證。

最大的三個不確定性：

1. Q3 2026 hyperscaler 財報（依節奏約 10 月下旬，日期未確認）。如果有兩家下修 capex 指引，R2 就會直接觸發，並可能引發 R1。這是把答案推向 yes 的主要風險。
2. 通膨與 Fed 路徑。CPI 3.3%、FedWatch 尾端為升息；如果升息情境成真，加上 10Y 期限溢價（term premium）上升，估值壓縮可能放大 R1。這會把答案推向 yes。
3. Anthropic 等大型 AI IPO 的時程與定價。成功定價會強化需求敘事，推向 no；發行失敗或供給過量則可能成為 R1 的催化，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 41.2（trailing P/E ≈26.2） | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E | 29.5（x；S&P 500 ≈25.6x） | https://www.fool.com/investing/2026/08/14/the-best-magnificent-seven-stocks-to-buy-in-august/ | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest | 7674.37 | FRED API (series_id=SP500)；fetch_macro.py sp500_trend | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 8.15（%） | FRED API (series_id=SP500)；fetch_macro.py sp500_trend | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 9.61（%） | FRED API (series_id=SP500)；fetch_macro.py sp500_trend | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29308.86 | FRED API (series_id=NASDAQ100)；fetch_macro.py ndx_drawdown | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100)；fetch_macro.py ndx_drawdown | 2026-06-02 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 4.41（%） | FRED API (series_id=NASDAQ100)；fetch_macro.py ndx_drawdown | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level | 22995.45 | FRED API (series_id=NASDAQ100)；fetch_macro.py ndx_drawdown | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| breadth.rsp_spy | RSP 對 SPY YTD 領先 | 5（pp） | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 top-10 集中度 | 36.5（%） | https://www.ebc.com/forex/rsp-vs-spy | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed | 55（Greed） | https://www.cnn.com/markets/fear-and-greed | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-07 月資料） | 1,417,225（YoY ≈+38.6%，MoM −5.7%） | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt | 2026-07-31 | 2026-08-24T09:30:00+08:00 |
| retail.aaii | AAII 偏多／偏空（週結 2026-08-19） | 35.5（%）／39.9（%） | https://www.aaii.com/sentimentsurvey | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1） | 45.76080873390133（%，2026Q1） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75（%） | FRED API (series_id=DFEDTARU) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5（%） | FRED API (series_id=DFEDTARL) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.75（%） | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.82（%） | FRED API (series_id=BAMLC0A0CM) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.69（%） | FRED API (series_id=DGS10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.35（%） | FRED API (series_id=DFII10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.34（%） | FRED API (series_id=T10YIE) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 86.48（USD/bbl） | FRED API (series_id=DCOILWTICO) | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料） | 3.3（%） | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.34（%） | FRED API (series_id=T5YIFR) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8393（%） | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.63（%） | FRED API (series_id=SOFR) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.71（%） | FRED API (series_id=SOFR99) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65（%） | FRED API (series_id=IORB) | 2026-08-24 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用） | 0.0（$0bn） | FRED API (series_id=RPONTTLD) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 標售 allotted at high | 12.10（%；無明顯 tail） | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2026/R_20260813_3.pdf | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| monetary.fedwatch | FedWatch 9/16 按兵不動定價 | 68.4（%；尾端為升息） | https://en.macromicro.me/series/1645/probability-fed-rate-decrease | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6745699.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5927307.0（€5.93T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_capex | top-4 2026 capex 合計 | 725（$bn，+77% YoY） | https://valueaddvc.com/ai-spending | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.token_growth | Anthropic run-rate 年增 | 7（倍） | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic／OpenAI run-rate | 65（$B）／40（$B） | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.compute_supply_demand | GPU 現貨租金對合約價 | 2（倍以上） | https://www.uncoveralpha.com/p/amazon-google-microsoft-meta-q2-earnings | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 vs 年化 capex（分母：top-4） | 105（$bn）vs 725（$bn） | https://valueaddvc.com/ai-spending | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD IPO 件數（截至 2026-08-21） | 232 | https://stockanalysis.com/ipos/2026/ | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 目標估值（目標 10 月） | 2（$T） | https://finance.yahoo.com/markets/article/spacex-openai-and-anthropic-here-are-the-most-anticipated-ipos-in-2026-114439441.html | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call（daily） | 0.52（9 日均總量 0.85） | https://www.thetrading.tools/put-call-ratio | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美股槓桿 ETF 總 AUM | 198（$bn；TQQQ 31.3、SOXL 17.3） | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比（8 月） | 62.4（%） | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| structural.options_volume | OCC YTD 日均量（2026-07 資料） | 71（M 口以上） | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/historical-volume-statistics | 2026-07-31 | 2026-08-24T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX／IVTS | 16.01（IVTS ≈0.82，contango；SKEW 偏高） | https://www.thetrading.tools/vix-term-structure | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.01 | FRED API (series_id=VIXCLS) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 16.01（comove=false） | FRED SP500 共同時間軸；fetch_macro.py derived block vix_spx_comove | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日窗，base 2026-08-13） | 9.43（%） | FRED SP500 共同時間軸；fetch_macro.py derived block vix_spx_comove | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日窗，base 2026-08-13） | -2.02（%） | FRED SP500 共同時間軸；fetch_macro.py derived block vix_spx_comove | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt YoY 交叉檢核（2026-07 月資料） | 38.6（%） | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt | 2026-07-31 | 2026-08-24T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2026.1422（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-12 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六個 CBT 美債期貨合約合計） | -7,218,048（口） | CFTC TFF futures-only（fetch_macro.py cftc_lev_funds） | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | 244,468（口） | CFTC TFF futures-only（fetch_macro.py cftc_lev_funds） | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.4 | Yahoo Finance chart API（^MOVE；fetch_macro.py move_index） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2328.6（$bn，transaction volume） | OFR STFM REPO-TRIV1_TV_TOT-P（fetch_macro.py ofr_repo） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值 / S&P 500 P/E and Shiller CAPE | multpl / GuruFocus，WebSearch primary | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值 / Mag 7 weighted P/E and AI leader P/S | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值 / Analyst TP upgrade decomposition | 賣方摘要 WebSearch（90d＋同季） | ✗ NOT DISCLOSED（無同季合格 TP 上修） |
| valuation.sp500_trend | 估值 / S&P 500 price-trend deviation | fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值 / NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值 / AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✗ NOT DISCLOSED（14 日內無合格披露） |
| breadth.rsp_spy | 廣度 / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度 / Top-10 concentration in S&P 500 | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度 / Advance/decline ratio, new high/low ratio | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶 / CNN Fear & Greed Index | CNN，WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶 / Margin Debt: FINRA monthly data | FINRA／GuruFocus WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶 / Retail survey: AAII Investor Sentiment | AAII，WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶 / Social sentiment proxies | WSB／X WebSearch（7d） | ✗ NOT DISCLOSED（無顯著討論） |
| retail.household_equity_allocation | 散戶 / Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶 / NAAIM Exposure Index | naaim.org WebSearch | ✗ NOT DISCLOSED（無當週數值） |
| institutional.bofa_jpm_survey | 機構 / BofA Fund Manager Survey and JPM institutional survey | BofA／JPM WebSearch（月頻） | ✗ NOT DISCLOSED（無新一期調查） |
| monetary.fed_funds | 貨幣 / Fed funds rate: FRED series DFEDTARU and DFEDTARL | fetch_macro.py（DFEDTARU ok、DFEDTARL ok） | ✓ API |
| monetary.hy_oas | 貨幣 / High Yield OAS | fetch_macro.py（BAMLH0A0HYM2 ok） | ✓ API |
| monetary.ig_oas | 貨幣 / Investment Grade OAS | fetch_macro.py（BAMLC0A0CM ok） | ✓ API |
| monetary.dgs10 | 貨幣 / 10Y Treasury yield | fetch_macro.py（DGS10 ok） | ✓ API |
| monetary.dfii10 | 貨幣 / 10Y Treasury real yield / TIPS | fetch_macro.py（DFII10 ok） | ✓ API |
| monetary.t10yie | 貨幣 / 10Y breakeven inflation rate | fetch_macro.py（T10YIE ok，FRED 直取） | ✓ API |
| monetary.wti | 貨幣 / WTI crude oil price | fetch_macro.py（DCOILWTICO ok） | ✓ API |
| monetary.cpi_yoy | 貨幣 / CPI YoY: FRED series CPIAUCSL | fetch_macro.py（CPIAUCSL yoy_pct ok） | ✓ API |
| monetary.t5yifr | 貨幣 / 5y5y forward inflation expectation | fetch_macro.py（T5YIFR ok） | ✓ API |
| monetary.term_premium | 貨幣 / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | fetch_macro.py（THREEFYTP10 ok） | ✓ API |
| monetary.repo_stress_srf | 貨幣 / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok；repo_stress status ok） | ✓ API |
| monetary.treasury_auctions | 貨幣 / 美債標售需求（auction tail / bid-to-cover） | Reuters／TreasuryDirect WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣 / Fed funds rate path expectations | CME FedWatch，WebSearch primary | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣 / Fed balance sheet: FRED series WALCL | fetch_macro.py（WALCL ok） | ✓ API |
| monetary.ecb_boj | 貨幣 / Global central bank liquidity cross-check | fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | 貨幣 / PBoC aggregate financing / liquidity operations | PBoC／NBS WebSearch | ✗ NOT DISCLOSED（無當期英文摘要） |
| monetary.private_credit_liquidity | 貨幣 / Private-credit / non-bank fund liquidity stress | BDC／interval fund 披露 WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無合格披露） |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | 財報摘要 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI / AI token volume growth rate | 供應商披露 WebSearch | ✓ SEARCH-VERIFIED |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | Bloomberg／CNBC WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 WebSearch | ✗ NOT DISCLOSED（無合格披露） |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | 產業披露 WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構（capex vs FCF / 發債） | 財報／發債 WebSearch：quarterly_state（stock-of-state）＋ event_scan（30d，無新事件） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口（revenue-to-capex gap） | 綜合披露 WebSearch（分母 top-4） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無變動披露） |
| ai.capital_cycle | AI / 資本週期階段（capital cycle stage） | 產業披露 WebSearch：quarterly_state（stock-of-state）＋ event_scan（30d，無新事件） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機 / Search for past 7 days: AI rename / SPAC | 新聞／SEC EDGAR／Renaissance WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機 / IPO market heat | stockanalysis／Renaissance WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機 / Microcap thematic moonshots | Finviz／Benzinga／StockTwits WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機 / Upcoming AI IPOs | Bloomberg／CNBC／Yahoo WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機 / Insider selling at AI / market-leadership companies | SEC EDGAR／openinsider WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機 / Cboe equity-only put/call ratio | Cboe，WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構 / US leveraged ETF AUM | etf.com／ETFGI，WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構 / US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com WebSearch（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | 結構 / Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED（7 日內無英文披露） |
| structural.zero_dte | 結構 / 0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構 / Options total volume | OCC WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構 / Cross-asset derivatives / correlation checks | Cboe／SpotGamma WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構 / VIX / S&P 500 co-movement | fetch_macro.py（VIXCLS ok、vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | 結構 / Cross-reference only: FINRA margin debt | FINRA／GuruFocus WebSearch（交叉檢核） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構 / AI infrastructure debt financing / vendor-financing loops | 信用市場 WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無新披露） |
| structural.nbfi_bank_loans | 結構 / Bank loans to nondepository financial institutions | fetch_macro.py（LNFACBW027SBOG ok） | ✓ API |
| structural.treasury_basis_trade | 結構 / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok）＋ WebSearch（無額外平倉事件） | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | trailing P/E ≈26.2、Shiller CAPE ≈41.2（原定來源：multpl／GuruFocus） | Shiller CAPE S&P 500 P/E August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E ≈29.5x（S&P 500 ≈25.6x） | Magnificent 7 weighted P/E August 2026 | https://www.fool.com/investing/2026/08/14/the-best-magnificent-seven-stocks-to-buy-in-august/（The Motley Fool） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| breadth.rsp_spy | RSP 領先 SPY YTD ≈5pp | RSP vs SPY YTD 2026 breadth | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 top-10 集中度 ≈36.5% | S&P 500 top 10 concentration 2026 | https://www.ebc.com/forex/rsp-vs-spy（EBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.advance_decline | 領導由 top-100 向 bottom-400 擴散，廣度確認多頭 | market breadth advance decline August 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 55（Greed） | CNN Fear and Greed today August 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-07 月資料）≈1,417,225、YoY ≈+38.6%、MoM −5.7% | FINRA margin debt July 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt（GuruFocus，原定 FINRA） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |
| retail.aaii | AAII 偏多 35.5%、偏空 39.9%（週結 2026-08-19） | AAII investor sentiment August 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 標售無明顯 tail、12.10% allotted at high | US Treasury 30-year auction August 2026 | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2026/R_20260813_3.pdf（TreasuryDirect） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| monetary.fedwatch | FedWatch 9/16 按兵不動 ≈68.4%，尾端為升息 | CME FedWatch September 2026 hold probability | https://en.macromicro.me/series/1645/probability-fed-rate-decrease（MacroMicro，原定 CME FedWatch） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_capex | top-4 2026 capex 合計 ≈$725bn（+77% YoY） | hyperscaler 2026 capex guidance Microsoft Google Amazon Meta | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.token_growth | Anthropic run-rate 年增約 7 倍，API 佔營收多數 | Anthropic token growth revenue 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html（CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.openai_anthropic_revenue | OpenAI ≈$40B、Anthropic ≈$65B run-rate | OpenAI Anthropic annualized revenue August 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html（CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.compute_supply_demand | GPU 現貨租金高於合約價 2 倍以上，產能被利用率吸收 | AI GPU rental pricing utilization August 2026 | https://www.uncoveralpha.com/p/amazon-google-microsoft-meta-q2-earnings（UncoverAlpha） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超過 FCF，2026 hyperscaler 發債擴張（capex 由現金流轉向舉債） | hyperscaler external financing capex FCF debt 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow（FactSet） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.revenue_capex_gap | OpenAI 40＋Anthropic 65 → ≈$105bn vs 年化 capex ≈$725bn（分母：top-4） | AI revenue to capex gap 2026 | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.capital_cycle | [quarterly_state] 供給側 capex 年增 ≈77%，需求側 token／營收成長並存 | AI capex growth rate supply demand 2026 | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 掃描：7 日內合格事件 0 件 | AI rename SPAC ticker change August 2026 | Renaissance Capital／SEC EDGAR／新聞掃描（無合格 in-window 事件） | — | 2026-08-24T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD IPO ≈232 件（截至 2026-08-21），沒有單週無營收 AI IPO 暴衝 | US IPO count August 2026 | https://stockanalysis.com/ipos/2026/（StockAnalysis） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（≥100% 單日、<$1B、2 個以上主題、弱基本面）：0 檔 | microcap 100% single day surge quantum AI August 2026 | Finviz／Benzinga／StockTwits movers 掃描（無合格 ticker） | — | 2026-08-24T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 10 月 IPO、估值 ≈$2T | Anthropic OpenAI IPO 2026 | https://finance.yahoo.com/markets/article/spacex-openai-and-anthropic-here-are-the-most-anticipated-ipos-in-2026-114439441.html（Yahoo Finance） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 14 日內合格 Form 4 集中賣出：0 起 | insider Form 4 AI executives August 2026 | SEC EDGAR／openinsider 掃描（14 日窗內無合格 cluster） | — | 2026-08-24T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.52（daily；9 日均總量 0.85） | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio（The Trading Tools，原定 Cboe） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美股槓桿 ETF 總 AUM 創新高，約 $198bn；TQQQ 31.3、SOXL 17.3 | leveraged ETF AUM record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing，原定 etf.com／ETFGI） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| structural.us_single_stock_etf | 美股單一個股槓桿 ETF 30 日內新核准／上市：0 件 | single-stock leveraged ETF launch SEC August 2026 | SEC EDGAR／ETF.com new launches 掃描（30 日窗內無合格核准） | — | 2026-08-24T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 8 月佔比創紀錄，約 62.4% | 0DTE SPX volume share August 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| structural.options_volume | OCC YTD 日均量超過 71M 口，量能高檔 | OCC options volume 2026 | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/historical-volume-statistics（OCC） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 16.01、期限結構 contango（IVTS ≈0.82）、SKEW 偏高 | VIX term structure SKEW August 2026 | https://www.thetrading.tools/vix-term-structure（The Trading Tools） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt／市值交叉檢核（見 retail.margin_debt，YoY +38.6%） | FINRA margin debt equity market cap ratio 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt（GuruFocus） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-24",
  "iso_week": "2026-W35",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-22",
  "prior_date": "2026-08-20",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 4.41,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

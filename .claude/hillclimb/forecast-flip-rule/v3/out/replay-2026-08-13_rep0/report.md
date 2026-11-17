> [DRY RUN] this report was not committed to archive.

# 2026-08-13 AI 泡沫破裂預測報告
報告日期：2026-08-13｜ISO 週次：2026-W33｜預測窗口：2026-08-13 → 2027-02-11｜前次基準：report-2026-08-10（3天前）

## 結論

**結論：no**

三條路徑都沒有在 182 天內完成的跡象：NASDAQ-100 距 52 週高點回撤 2.99%，離 R1 門檻還需再跌約 22.69%（`valuation.ndx_drawdown`）；hyperscaler 2026 capex 合計約 $725B、仍在上修，沒有任何一家下修（`ai.hyperscaler_capex`）。CoreWeave 貸款利差走闊與 Oracle CDS 升至 7 年高點（`valuation.ai_credit_schism`）是真實的信用端裂縫，但目前只是重定價，還不是違約或 distressed exchange，不足以推翻低基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,742.6（2026-08-12），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 2.99%；R1 門檻水位為 22,995.45，從最新收盤還需再跌約 22.69% 才會觸發（`valuation.ndx_drawdown`）。估值很高、價格也偏離趨勢：S&P 500 trailing P/E 29.85、Shiller CAPE 42.34（`valuation.sp500_pe_cape`），S&P 500 7,748.5 高於 200 日均線 9.67%、高於 52 週均線 11.23%（`valuation.sp500_trend`）。槓桿和投機也偏熱：FINRA 6 月 margin debt $1.502T、YoY +51.5%（`retail.margin_debt`），US 槓桿 ETF AUM 約 $198B 創新高（`structural.leveraged_etf_aum`），0DTE 約佔 SPX 期權量 65%（`structural.zero_dte`）。不過目前沒有壓力在傳導：VIX 15.28，VIX/S&P 500 同步上漲訊號為 false（`structural.vix_spx_comove`），HY OAS 只有 2.72%（`monetary.hy_oas`）。可能的觸發點是貨幣政策：FedWatch 顯示 9/16 會議約 45% 升息定價、沒有降息定價（`monetary.fedwatch`），CPI YoY 3.3%（`monetary.cpi_yoy`），Fed 用降息托底的空間有限。

**判讀：** R1 離觸發還很遠（回撤不到 3%，還差約 22.69%）。要在窗口內成立，需要升息衝擊、AI 信用事件外溢（R3→R1）或 capex 下修（R2→R1）這類觸發點，再加上槓桿部位被迫平倉；目前波動率與信用利差都沒有出現這種傳導。

### R2 資本支出收縮

本次證據只有 hyperscaler 2026 capex 合計約 $725B，且方向仍是上修（CNBC，2026-07-28，涵蓋 7 月下旬 Q2 財報季；`ai.hyperscaler_capex`）。本次取得的來源沒有拆出 Microsoft、Alphabet、Amazon、Meta 各家的指引數字，所以各家的具體金額本次未確立；但已知證據中，四家都沒有下修（0/4），整體方向為上修。下一次財報的具體日期本次沒有取得來源；182 天窗口（至 2027-02-11）依季度財報節奏應涵蓋後續兩次財報。壓力確實存在：CNBC 報導 Alphabet 財報後 capex 受到市場質疑；top-5 hyperscaler capex 已超過 FCF（Alphabet Q2 FCF 轉負），2026 年發債約 $182B（`ai.hyperscaler_financing_mix`）。另一方面，需求端仍強：Microsoft 商用 RPO 約 $678B（`ai.customer_concentration_rpo`），HBM 合約價約 +40%、Blackwell 售罄（`ai.compute_supply_demand`）。

**判讀：** R2 目前是 0/4，方向是上修而不是下修。要在窗口內成立，需要在接下來兩次財報中有兩家改為下修；觸發條件可能是 FCF 轉負引發股東壓力、發債成本上升，或 R1 回撤迫使管理層收縮。目前沒有任何一家轉向的證據。

### R3 AI 信用事件

信用端已經開始重定價：CoreWeave 的 $2.6B 貸款被迫調高利差 +100–125bp，並加上 covenant（2026-07-29；`structural.ai_infrastructure_debt`）；Oracle 5Y CDS 約 75bp，為 7 年高點，Fitch/Moody's 也發出預警（2026-08-03；`valuation.ai_credit_schism`）。本次證據沒有出現任何付款違約、covenant waiver、distressed exchange 或 going-concern 字樣。CoreWeave 等 neocloud 的總負債是否達 R3 的 50 億美元門檻，本次沒有來源支持，所以未確立；Oracle 不以 AI 資料中心為主業，是否落在 R3 範圍也不明確。表外結構持續擴大：Meta El Paso 資料中心由 BlackRock 主導、超過 $12B 的債券（20-30yr triple-net lease、表外結構，2026-07-20；`ai.hyperscaler_financing_mix`），代表 AI 基建風險正轉向租約和 SPV。

**判讀：** R3 處在「利差走闊、條款收緊」的早期階段，離違約或 distressed exchange 還有好幾步。要在窗口內成立，需要某個大型 neocloud 遇到再融資失敗或主要客戶合約出問題；目前市場仍願意放款（$2.6B 已完成），只是要求更高的價格。

## 支持 yes 的證據

- [R3] CoreWeave $2.6B 貸款被迫調高利差 +100–125bp 並加上 covenant（2026-07-29），Oracle 5Y CDS 約 75bp，為 7 年高點（2026-08-03）：信用端在股價還沒反應前先重定價，是典型的後期訊號 `structural.ai_infrastructure_debt` `valuation.ai_credit_schism`
- [R2] top-5 hyperscaler capex 已超過 FCF（Alphabet Q2 FCF 轉負），2026 年發債約 $182B（2026-07-24），Meta El Paso 超過 $12B 表外債券（2026-07-20）：capex 越來越依賴舉債，一旦融資成本上升，下修壓力就會增加 `ai.hyperscaler_financing_mix`
- [R1] FedWatch 9/16 約 45% 升息定價、沒有降息定價（2026-08-12），CPI YoY 3.3%（2026-07）：升息衝擊是高估值資產最直接的觸發點，Fed 也沒有空間托底 `monetary.fedwatch` `monetary.cpi_yoy`
- [R1] 估值與槓桿處於極端：CAPE 42.34（2026-08-12），margin debt YoY +51.5%（2026-06），槓桿 ETF AUM 約 $198B 創新高，S&P 500 高於 200 日均線 9.67%；一旦出事，下跌幅度會很大 `valuation.sp500_pe_cape` `retail.margin_debt` `structural.leveraged_etf_aum` `valuation.sp500_trend`
- [整體] AI 終端年化營收約 $72B，對比年化 capex 約 $725B（分母：top-4＋Oracle；沿用 2026-06-15 的組合值，不是新證據）；Microsoft RPO 約 32% 繫於 OpenAI 單一客戶（2026-07-30），集中度風險高 `ai.revenue_capex_gap` `ai.customer_concentration_rpo`

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 2.99%（2026-08-12），還需再跌約 22.69% 才到 R1 門檻 22,995.45；在 182 天內從接近高點直接跌 25% 是少見事件 `valuation.ndx_drawdown`
- [R2] hyperscaler 2026 capex 合計約 $725B，仍在上修（2026-07-28），四家都沒有下修；需求端 Blackwell 售罄、HBM 合約價約 +40%（2026-08-01），沒有產能過剩或訂單消化的證據 `ai.hyperscaler_capex` `ai.compute_supply_demand`
- [整體] 整體信用與資金市場平穩：HY OAS 2.72%、IG OAS 0.79%（2026-08-11），SOFR−IORB 為 −1bp、SRF 動用 0（2026-08-11/12），MOVE 72.09（2026-08-12）；AI 信用的重定價還沒有擴散到整體市場 `monetary.hy_oas` `monetary.ig_oas` `monetary.repo_stress_srf` `structural.treasury_basis_trade`
- [R3] CoreWeave 雖然付出更高利差，仍完成 $2.6B 融資（2026-07-29）：融資管道仍然暢通，離破產或 distressed exchange 還很遠 `structural.ai_infrastructure_debt`
- [R1] 沒有恐慌或拋售前兆：VIX 15.28、VIX/S&P 500 同步上漲訊號為 false（2026-08-11），CNN Fear & Greed 約 61（Greed，不是極端），10Y 美債標售需求略高於平均（2026-08-12） `structural.vix_spx_comove` `retail.fear_greed` `monetary.treasury_auctions`

## 與前期比較

前次結論：無前次預測（report-2026-08-10 為舊格式評分報告）

上一份報告是舊格式評分報告，沒有 yes/no 結論，因此本次沒有翻轉判斷，flip_evidence 為空。2026-08-10 以來，macro 資料的主要變化如下：

- DGS10 −2bp 至 4.70%、T10YIE −3bp，DFII10 持平；因為三者的視窗不一致，驅動因素判定為 不可判（視窗不一致）。
- HY OAS +2bp 至 2.72%、IG OAS +1bp 至 0.79%，幅度很小。
- S&P 500 −0.06%，MOVE 從 75.46 降到 72.09，市場沒有出現壓力。
- WALCL、ECB、BOJ 資產負債表與銀行對 NBFI 放款都沒有新觀測（持平）。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- breadth.rsp_spy：唯一取得的 RSP vs SPY YTD 數字（+9.67% vs +8.38%）資料日期為 2026-06-10，對 2026-08-13 的 snapshot 來說已經過時，沒有取得當前可用值，所以標為 FETCH FAILED。廣度只是脆弱度的參考，不在 R1–R3 的觸發鏈上，這個缺口不會改變結論。

主要不確定性：

- 下一輪 hyperscaler 財報（具體日期本次未取得來源）：如果有兩家在 FCF 轉負的壓力下下修 capex，R2 就會直接成立，推向 yes。
- AI 信用重定價會不會惡化：CoreWeave 等 neocloud 的總負債與到期結構本次未確立；如果出現再融資失敗或 distressed exchange，可能同時觸發 R3 和 R1，推向 yes。
- 9/16 FOMC：如果升息落地，高估值與高槓桿（margin debt YoY +51.5%）可能被迫去槓桿，推向 yes；如果按兵不動，則支持 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 29.85 | https://www.multpl.com/s-p-500-pe-ratio | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE | 42.34 | https://www.multpl.com/shiller-pe | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest | 7748.5 | FRED API (series_id=SP500) sp500_trend | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 9.67 | FRED API (series_id=SP500) sp500_trend | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 11.23 | FRED API (series_id=SP500) sp500_trend | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29742.6 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-06-02 | 2026-08-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 2.99 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level | 22995.45 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 貸款利差調高／Oracle 5Y CDS | +100–125bp（Oracle CDS ≈75bp） | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm | 2026-08-03 | 2026-08-13T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-06 月資料）／YoY | $1.502T／+51.5% | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-13T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed | ≈61（Greed） | https://www.cnn.com/markets/fear-and-greed | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1） | 45.76（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75（%） | FRED API (series_id=DFEDTARU) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5（%） | FRED API (series_id=DFEDTARL) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.72（%） | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.79（%） | FRED API (series_id=BAMLC0A0CM) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.7（%） | FRED API (series_id=DGS10) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | -2.0（bp） | FRED API (series_id=DGS10) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.43（%） | FRED API (series_id=DFII10) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.26（%） | FRED API (series_id=T10YIE) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | -3.0（bp） | FRED API (series_id=T10YIE) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 84.77（USD/bbl） | FRED API (series_id=DCOILWTICO) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料） | 3.3（%） | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.28（%） | FRED API (series_id=T5YIFR) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8257（%） | FRED API (series_id=THREEFYTP10) | 2026-08-07 | 2026-08-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.64（%） | FRED API (series_id=SOFR) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.73（%） | FRED API (series_id=SOFR99) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65（%） | FRED API (series_id=IORB) | 2026-08-13 | 2026-08-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用） | 0.0（$bn） | FRED API (series_id=RPONTTLD) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 9/16 升息定價 | ≈45%（無降息定價） | https://cryptobriefing.com/traders-45-percent-chance-september-fed-rate-hike/ | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.treasury_auctions | 3Y／10Y 標售 bid-to-cover | 3Y 2.71／10Y 2.58 | https://www.rttnews.com/3679611/ten-year-note-auction-attracts-modestly-above-average-demand.aspx | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6748567.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-05 | 2026-08-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5923023.0（€5.92T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-07 | 2026-08-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-13T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計（仍上修） | ≈$725B | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-07-28 | 2026-08-13T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft 商用 RPO／單一客戶佔比 | $678B／≈32%（OpenAI） | https://www.benzinga.com/trading-ideas/long-ideas/26/07/60816147/microsofts-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer | 2026-07-30 | 2026-08-13T09:30:00+08:00 |
| ai.compute_supply_demand | H200 租金中位／HBM 合約 | ≈$3.99/hr／≈+40% | https://jarvislabs.ai/blog/h200-price | 2026-08-01 | 2026-08-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 超越 FCF（Alphabet Q2 FCF 轉負）、2026 發債 | ≈$182B | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure | 2026-07-24 | 2026-08-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan][spv_deal] Meta El Paso 資料中心 BlackRock 主導債券（triple-net lease、表外結構） sponsor_equity_split=undisclosed;residual_value_guarantee=undisclosed;lease_term=20-30yr;debt_tenor=undisclosed;lead_lenders=BlackRock/JPMorgan/MS; | >$12B | https://www.landgate.com/news/blackrock-s-12-billion-bond-sale-signals-a-new-financing-playbook-for-data-center-developers | 2026-07-20 | 2026-08-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 vs 年化 capex（分母：top-4＋Oracle；沿用組合值） | ≈$72B vs ≈$725B | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-06-15 | 2026-08-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM（記錄高） | ≈$198B | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-07-23 | 2026-08-13T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量（Cboe Q2） | ≈65% | https://ca.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4768656 | 2026-07-31 | 2026-08-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.28 | FRED API (series_id=VIXCLS) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（comove=false） | 15.28 | FRED API vix_spx_comove（SP500 配對） | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | -7.39（%） | FRED API vix_spx_comove（SP500 配對） | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B 貸款調高利差＋covenant | +100–125bp | https://www.stocktitan.net/news/CRWV/core-weave-closes-2-6-billion-loan-facility-expanding-financing-gwhngwnf0jt5.html | 2026-07-29 | 2026-08-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2002.4852（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-29 | 2026-08-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7423067（口） | CFTC TFF cftc_lev_funds | 2026-08-04 | 2026-08-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 72.09 | Yahoo Finance chart API (^MOVE) move_index | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2385.3（$bn，transaction volume） | OFR STFM ofr_repo | 2026-08-12 | 2026-08-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | Fool / SSGA WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報摘要 WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 24/7 Wall St WebSearch | ⛔ FETCH FAILED 僅取得 2026-06-10 舊數據，無當前 snapshot |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | RBC Wealth Management WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | Investing.com breadth WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA / Advisor Perspectives WebSearch | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB / cashtag WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim.org / YCharts WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API DFEDTARU ok；DFEDTARL ok |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series | scripts/fetch_macro.py repo_stress | ✓ API SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | Reuters / RTTNews recap WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要 WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API ECBASSETSW ok；JPNASSETS ok |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | investing / Yicai WebSearch | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC / interval fund 披露 WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報／財經報導 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic / OpenAI / Google 披露 WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | 具名報導 WebSearch；唯一結果為上一季（2026-05-29），非本季披露 | ✗ NOT DISCLOSED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話會摘要 WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce / GPU 租金 WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：季報／發債統計 WebSearch；event_scan：30d 融資事件 WebSearch | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 WebSearch（沿用組合值） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K / 10-Q WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | quarterly_state：供需增速披露 WebSearch；event_scan：30d 進出場事件 WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | Reuters / Benzinga / SEC WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | IPOScoop / Renaissance WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz / StockAnalysis gainers WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | S-1／具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR / openinsider / secform4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe / thetrading.tools WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com / 財經報導 WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | SEC EDGAR / 發行商新聞稿 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX / TWSE / JPX / ESMA WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe insights WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API VIXCLS ok；vix_spx_comove ok |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 retail.margin_debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | 融資新聞 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds／move_index／ofr_repo（any） | ✓ API cftc_lev_funds ok；move_index ok；ofr_repo ok |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.85、CAPE 42.34（原定來源 multpl） | S&P 500 trailing P/E CAPE August 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio（multpl） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 ≈29x vs 指數 ≈25.6x、佔市值 ≈33.9% | Magnificent 7 weighted PE vs S&P 500 August 2026 | https://www.fool.com/research/magnificent-seven-sp-500/（Motley Fool） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Susquehanna TSMC 目標 $575→$600，EPS-driven（EPS／PE 分量未披露） | Susquehanna TSMC price target 600 July 2026 earnings | https://www.tipranks.com/news/tsmc-stock-price-forecast-top-analysts-raise-targets-ahead-of-q2-earnings（TipRanks） | 2026-07-16 | 2026-08-13T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 貸款利差 +100–125bp、Oracle CDS ≈75bp（7 年高）、Fitch/Moody's 預警 | CoreWeave Oracle CDS spread AI credit widening August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm（Tech Times） | 2026-08-03 | 2026-08-13T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 ≈37% | S&P 500 top 10 concentration percent 2026 | https://www.rbcwealthmanagement.com/en-us/insights/the-great-narrowing-sp-500-concentration（RBC Wealth Management） | 2026-07-24 | 2026-08-13T09:30:00+08:00 |
| breadth.advance_decline | ≈71.6% S&P 500 成分股在 50DMA 上 | S&P 500 percent above 50 day moving average August 2026 | https://www.investing.com/indices/s-p-500-stocks-above-50-day-average（Investing.com） | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed ≈61（Greed） | CNN Fear and Greed Index August 12 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives） | 2026-07-20 | 2026-08-13T09:30:00+08:00 |
| retail.aaii | AAII Bull 37.0%／Neutral 25.0%／Bear 38.0%（週結束 2026-08-05） | AAII investor sentiment survey week August 5 2026 | https://seekingalpha.com/article/4932187-aaii-sentiment-survey-optimism-jumps（Seeking Alpha） | 2026-08-06 | 2026-08-13T09:30:00+08:00 |
| monetary.treasury_auctions | 3Y 08-11 BTC 2.71、tail −0.5bp；10Y 08-12 BTC 2.58，需求略高於均值 | US Treasury 3 year 10 year auction bid to cover August 2026 | https://www.rttnews.com/3679611/ten-year-note-auction-attracts-modestly-above-average-demand.aspx（RTTNews） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 9/16 ≈45% 升息、無降息定價 | CME FedWatch September 2026 rate hike probability | https://cryptobriefing.com/traders-45-percent-chance-september-fed-rate-hike/（Crypto Briefing） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計 ≈$725B、仍上修（Q2 財報季） | hyperscaler capex 2026 725 billion raised Q2 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-08-13T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO ≈$678B、≈32% 繫單一客戶（OpenAI） | Microsoft RPO backlog 678 billion OpenAI 2026 | https://www.benzinga.com/trading-ideas/long-ideas/26/07/60816147/microsofts-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer（Benzinga） | 2026-07-30 | 2026-08-13T09:30:00+08:00 |
| ai.compute_supply_demand | HBM 合約 ≈+40%、H200 租金 ≈$3.99/hr、Blackwell 售罄 | H200 GPU rental HBM DRAM 2026 shortage Blackwell | https://jarvislabs.ai/blog/h200-price（Jarvislabs） | 2026-08-01 | 2026-08-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 超越 FCF、2026 發債 ≈$182B | hyperscaler capex FCF debt issuance 182 billion 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure（Sage Advisory） | 2026-07-24 | 2026-08-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan][spv_deal] Meta El Paso 資料中心 BlackRock 主導 >$12B 債券（triple-net lease、表外結構） sponsor_equity_split=undisclosed;residual_value_guarantee=undisclosed;lease_term=20-30yr;debt_tenor=undisclosed;lead_lenders=BlackRock/JPMorgan/MS; | hyperscaler capex FCF debt issuance 182 billion 2026 | https://www.landgate.com/news/blackrock-s-12-billion-bond-sale-signals-a-new-financing-playbook-for-data-center-developers（Landgate） | 2026-07-20 | 2026-08-13T09:30:00+08:00 |
| ai.revenue_capex_gap | AI 終端年化營收 ≈$72B vs 年化 capex ≈$725B（分母：top-4＋Oracle；沿用組合值） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-06-15 | 2026-08-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收 IPO 螢幕：合格 0 件 | AI rename ticker SPAC no revenue IPO August 6-13 2026 | Reuters／Benzinga／SEC EDGAR 螢幕 | — | 2026-08-13T09:30:00+08:00 |
| speculation.ipo_heat | 08-12／08-13 各 ≈12 檔定價、平均首日 ≈18% | US IPO pricings week August 2026 IPOScoop | https://www.iposcoop.com/current-year-pricings/（IPOScoop） | 2026-08-13 | 2026-08-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot 螢幕：合格 0 件 | microcap 100% single day quantum fusion nuclear AI August 2026 | Finviz／StockAnalysis gainers 螢幕 | — | 2026-08-13T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 9 月上市、估值 ≈$730–850B；Anthropic 續進 | OpenAI Anthropic IPO timing valuation 2026 | https://cryptobriefing.com/openai-ipo-filing-trillion-valuation/（Crypto Briefing） | 2026-07-28 | 2026-08-13T09:30:00+08:00 |
| speculation.insider_form4 | AI／領導股 Form 4 賣壓 cluster 螢幕（14d）：合格 0 件 | AI leadership insider Form 4 sale July 30 August 13 2026 SEC | openinsider／secform4／SEC EDGAR 螢幕 | — | 2026-08-13T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity-only put/call 0.54（daily） | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio（thetrading.tools） | 2026-08-07 | 2026-08-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM ≈$198B（記錄高） | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing） | 2026-07-23 | 2026-08-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 08-11 新發 6 檔單股 2x 槓桿 ETF（Leverage Shares／Tradr） | single-stock leveraged ETF launch August 11 2026 Leverage Shares Tradr | https://www.globenewswire.com/news-release/2026/08/11/3342794/0/en/leverage-shares-by-themes-launches-three-new-2x-etfs-targeting-ai-infrastructure-and-connectivity-leaders.html（GlobeNewswire） | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量 ≈65%（Cboe Q2 2026） | 0DTE SPX options share Cboe Q2 2026 65% | https://ca.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4768656（Investing.com） | 2026-07-31 | 2026-08-13T09:30:00+08:00 |
| structural.options_volume | OCC 6 月總量 1,603,491,559 口（≈16.0 億口） | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-08-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 135.59、VIX 15.28、MOVE 74.67（週報） | VIX SKEW MOVE bond volatility August 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-10-2026-spx-skew-collapses-on-upside-chasing（Cboe） | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt $1.502T、+51.5% YoY（交叉引用 retail.margin_debt） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives） | 2026-07-20 | 2026-08-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B 貸款被迫調高利差 +100–125bp＋covenant | CoreWeave 2.6 billion loan spread covenant August 2026 | https://www.stocktitan.net/news/CRWV/core-weave-closes-2-6-billion-loan-facility-expanding-financing-gwhngwnf0jt5.html（StockTitan） | 2026-07-29 | 2026-08-13T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-13",
  "iso_week": "2026-W33",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-11",
  "prior_date": "2026-08-10",
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 2.99,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

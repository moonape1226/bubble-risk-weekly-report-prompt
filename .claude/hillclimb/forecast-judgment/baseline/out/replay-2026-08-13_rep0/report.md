> [DRY RUN] this report was not committed to archive.

# 2026-08-13 AI 泡沫破裂預測報告

報告日期：2026-08-13｜ISO 週次：2026-W33｜預測窗口：2026-08-13 → 2027-02-11｜前次基準：report-2026-08-10（3天前）

## 結論

**結論：no**

三條路徑都離解析門檻很遠：NASDAQ-100 只比 52 週高點低 2.99%，要再跌約 22.69% 才會觸發 R1；hyperscaler 2026 capex 合計約 $725B，指引仍在上修，四家公司沒有任何一家下修。AI 信用端確實開始重定價（CoreWeave 貸款利差被迫調高 100–125bp、Oracle CDS 約 75bp，為 7 年高點），但沒有出現違約或 distressed exchange 的跡象，HY OAS 也只有 2.72%，市場廣泛的信用壓力尚未出現。所以這些證據還不足以推翻「182 天內不破裂」的基準。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29742.6（2026-08-12），252 個交易日內最高收盤 30660.6（2026-06-02），距 52 週高點回撤 2.99%。R1 門檻水位為 22995.45，從最新收盤還要再跌約 22.69% 才會觸及（`valuation.ndx_drawdown`）。這段窗口內最深的一次回落是 2026-07-29 收盤 27192.31（較 06-02 高點低約 11.3%），之後兩週內已收復大半。S&P 500 收在 7748.5（2026-08-12），比 200 日均線 7065.31 高 9.67%、比 52 週均線高 11.23%（`valuation.sp500_trend`）。指數漲幅偏高，修正風險升高，但這還不是正在發生的回撤。估值相當拉伸：S&P 500 trailing P/E 約 29.85、Shiller CAPE 約 42.34（`valuation.sp500_pe_cape`），Mag 7 約 29x、指數約 25.6x，Mag 7 佔市值約 33.9%（`valuation.mag7_multiples`）。這說明一旦下跌，跌幅可能很大。可能的時序催化劑主要在貨幣面：CME FedWatch 對 9/16 FOMC 的升息定價約 45%，完全沒有降息定價（`monetary.fedwatch`）。CPI YoY 為 3.3%（2026-07 資料，`monetary.cpi_yoy`），Fed 用降息托住 AI 帶頭下跌的空間有限。另一方面，VIX 為 15.28（`structural.vix_spx_comove`），沒有出現股價與波動率同步上升的 crowded-optionality 讀數。

**判讀：** R1 離門檻還很遠（還需再跌約 22.69%）。要在窗口內成立，需要一次「Fed 意外升息＋AI 信用重定價擴散到股權」的組合衝擊，讓 NASDAQ-100 在 2027-02-11 前從高點跌掉四分之一；目前價格趨勢與波動率都沒有顯示這種跌勢已經開始。

### R2 資本支出收縮

最近一輪財報（2026 Q2，7 月底公布）之後，CNBC 2026-07-28 報導 Microsoft、Alphabet、Amazon、Meta 的 2026 capex 合計約 $725B，方向是仍在上修（`ai.hyperscaler_capex`）。本次證據只有彙總口徑，沒有四家各自的指引數字，因此逐家標示如下：Microsoft：上修（彙總口徑，個別數值未取得）；Alphabet：上修（彙總口徑，個別數值未取得；同篇報導指出 Alphabet 財報後市場對 capex 的檢視變嚴）；Amazon：上修（彙總口徑，個別數值未取得）；Meta：上修（彙總口徑，個別數值未取得）。目前四家中下修家數為 0。需求面也沒有降溫跡象：H200 租金中位數約 $3.99/hr、HBM 合約價約 +40%、Blackwell 售罄（`ai.compute_supply_demand`，2026-08-01）；Microsoft 商用 RPO 約 $678B（`ai.customer_concentration_rpo`，2026-07-30）。下一輪財報（2026 Q3）預計在窗口內公布，但確切日期不在本次證據中；2027 年初的 Q4 財報可能落在窗口尾端或窗口之後。

**判讀：** R2 離門檻很遠。兩家下修需要指引方向在一到兩個財報季內反轉，而目前方向仍是上修、算力仍然短缺。可能推動 R2 的情境是：R1 式的股價大跌或融資成本急升，迫使 FCF 已轉負的公司（Alphabet Q2 FCF 轉負，`ai.hyperscaler_financing_mix`）在 Q3／Q4 財報時下修。

### R3 AI 信用事件

AI 信用端在 14 日窗內已經開始重定價：CoreWeave 貸款利差被迫調高 100–125bp 並加上 covenant，Oracle 5Y CDS 約 75bp（7 年高點），Fitch／Moody's 也發出預警（`valuation.ai_credit_schism`，2026-08-03）。CoreWeave 的 $2.6B 貸款融資已於 2026-07-29 完成，代價是更高的利差與 covenant（`structural.ai_infrastructure_debt`）。這代表貸款人還願意放款，但開始要求更多風險補償。CoreWeave 屬於以 AI 算力為主業的借款人，但本次證據沒有其總負債數字，因此無法在本報告中驗證它是否達到 ≥ 50 億美元的門檻。另一個可能達到規模門檻的是 Meta El Paso 資料中心的表外融資結構（>$12B 債券，BlackRock 主導，20-30 年 triple-net lease，`ai.hyperscaler_financing_mix`，2026-07-20）。這筆融資剛完成發行，沒有壓力訊號。本次證據中沒有任何 R3 借款人出現付款違約、covenant waiver、distressed exchange 或 going-concern 字樣。廣泛信用市場仍然很緊：HY OAS 2.72%、IG OAS 0.79%（`monetary.hy_oas`、`monetary.ig_oas`，2026-08-11）。repo 資金壓力（SOFR−IORB）為 −1bp，SRF 動用為 0（`monetary.repo_stress_srf`）。

**判讀：** R3 是三條路徑中最接近的一條，但仍然只停在利差走闊的階段。要在窗口內成立，需要一家以 AI 為主業、負債 ≥ 50 億美元的借款人從「調高票息後仍能再融資」惡化到付款違約或 distressed exchange。這通常要等再融資窗口關閉，或主要客戶合約出問題；目前兩者都沒有證據。

## 支持 yes 的證據

- [R3] AI 信用端已開始重定價：CoreWeave 貸款利差被迫調高 100–125bp 並加上 covenant，Oracle 5Y CDS 約 75bp 為 7 年高點，Fitch／Moody's 發出預警（2026-08-03），符合「信貸端先走闊、股價未跟上」的後期訊號 `valuation.ai_credit_schism` `structural.ai_infrastructure_debt`
- [R2] hyperscaler 融資結構轉向舉債：top-5 capex 已超過 FCF，Alphabet Q2 FCF 轉負，2026 年發債約 $182B（2026-07-24），再加上 Meta El Paso >$12B 表外融資（2026-07-20），capex 越來越依賴外部融資，對利率與信用利差也更敏感 `ai.hyperscaler_financing_mix`
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）很大：年化 AI 終端營收約 $72B，對照年化 capex 約 $725B（分母：top-4＋Oracle；2026-06-15 組合值沿用），回本壓力是 R2 反轉的結構性來源 `ai.revenue_capex_gap`
- [R1] 槓桿與投機堆積：FINRA 6 月 margin debt $1.502T，YoY +51.5%（落在歷史頂部附近 +40–50% 的區間）；US 槓桿 ETF AUM 約 $198B 創新高；2026-08-11 新發 6 檔單股 2x 槓桿 ETF `retail.margin_debt` `structural.leveraged_etf_aum` `structural.us_single_stock_etf`
- [R1] 估值與延伸：Shiller CAPE 約 42.34、trailing P/E 約 29.85（2026-08-12），S&P 500 比 200 日均線高 9.67%（2026-08-12），一旦出現衝擊，下跌空間很大 `valuation.sp500_pe_cape` `valuation.sp500_trend`
- [R1] 貨幣面沒有支撐：CME FedWatch 9/16 升息定價約 45%、無降息定價（2026-08-12），CPI YoY 3.3%（2026-07），Fed 難以降息托底 `monetary.fedwatch` `monetary.cpi_yoy`
- [R2] 客戶集中：Microsoft 商用 RPO 約 $678B，其中約 32% 繫於單一客戶 OpenAI（2026-07-30），終端客戶出狀況就可能連動 backlog 與 capex `ai.customer_concentration_rpo`

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 2.99%（2026-08-12），還要再跌約 22.69% 才會到達 R1 門檻 22995.45；07-29 那次約 11.3% 的回落也已收復大半 `valuation.ndx_drawdown`
- [R2] hyperscaler 2026 capex 合計約 $725B，指引仍在上修，四家下修家數為 0（2026-07-28）；要達到兩家下修，需要在一到兩個財報季內反轉 `ai.hyperscaler_capex`
- [R2] 算力需求仍然短缺：H200 租金中位數約 $3.99/hr、HBM 合約價約 +40%、Blackwell 售罄（2026-08-01），看不到產能過剩或訂單消化的跡象 `ai.compute_supply_demand`
- [R3] 廣泛信用與資金市場平穩：HY OAS 2.72%、IG OAS 0.79%（2026-08-11）；SOFR−IORB −1bp、SRF 動用 0（2026-08-11／08-12）；CoreWeave 雖被調高利差，仍完成 $2.6B 融資（2026-07-29），再融資窗口仍然開著 `monetary.hy_oas` `monetary.ig_oas` `monetary.repo_stress_srf` `structural.ai_infrastructure_debt`
- [整體] 沒有失序訊號：VIX 15.28、七日窗 VIX −7.39% 而 S&P 500 −0.11%，沒有股價與波動率同步上升（2026-08-11）；MOVE 72.09（2026-08-12）；槓桿基金美債期貨淨部位 −7423067 口，4 週變動 +149977 口（2026-08-04），美債基差交易槓桿（Treasury basis-trade leverage）沒有平倉跡象 `structural.vix_spx_comove` `structural.treasury_basis_trade`
- [整體] 美債標售需求（auction tail / bid-to-cover）穩健：3Y（08-11）bid-to-cover 2.71、tail −0.5bp，10Y（08-12）bid-to-cover 2.58、需求略高於均值，看不到財政供給壓力 `monetary.treasury_auctions`
- [整體] 市場情緒沒有到極端：CNN Fear & Greed 約 61（Greed，2026-08-12）；AAII Bull 37.0%／Bear 38.0%（週結束 08-05）；Cboe equity put/call 0.54（2026-08-07）；+AI 改名／SPAC 與 microcap moonshot 篩選都是 0 件 `retail.fear_greed` `retail.aaii` `speculation.equity_put_call` `speculation.ai_rename_spac` `speculation.microcap_moonshots`

## 與前期比較

前次結論：無前次預測（report-2026-08-10 為舊格式評分報告）

report-2026-08-10 是舊格式的六面向評分報告，沒有 yes/no 預測，因此這次不適用翻轉紀律，flip_evidence 為空。舊評分不會轉換成 yes/no。與 2026-08-10 相比的 macro 變動：DGS10 −2.0bp 到 4.7%，DFII10 持平，T10YIE −3.0bp；但 T10YIE 的 Δ 視窗與另外兩腿不同，10Y 分解判讀：不可判（視窗不一致）。HY OAS +2bp、IG OAS +1bp，S&P 500 −0.06%，MOVE 從 75.46 降到 72.09，WTI +1.21% 到 84.77。WALCL、ECBASSETSW、LNFACBW027SBOG 沒有新觀測（持平）。這些變動都很小，不影響三條路徑的判讀。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `breadth.rsp_spy`（必要來源）：搜尋只找到 2026-06-10 的 RSP vs SPY YTD 比較（+9.67% vs +8.38%），比執行日早兩個月，不能當作現行快照，所以標為 ⛔ FETCH FAILED。廣度只是 R1 脆弱度的佐證，而 Top-10 集中度約 37% 與 >50DMA 比例約 71.6% 仍可用，因此這個缺口不會改變結論。

非成功但不影響結論的來源（✗ NOT DISCLOSED）：analyst TP decomposition（唯一的同季結果是 Susquehanna TSMC 目標 $575→$600，不屬於指定的 top-tier 券商，也沒有 EPS／PE 拆解數字）、社群情緒、NAAIM、BofA／JPM 調查、PBoC、私募信貸贖回壓力（private-credit / non-bank fund liquidity stress，30 日內沒有 redemption-request ratio、gate proration / breach 或 net inflow→outflow flip 的披露）、token growth、OpenAI／Anthropic 年化營收（唯一結果是 2026-05-29 的上一季資料，而且報導標題的 $30B 與摘要的 $47B 不一致，不能當作當季披露）、折舊年限變動（depreciation useful-life change）、資本週期階段（capital cycle stage，兩個組件都沒有可用證據；增速證據不足，本次不判定週期階段）、全球槓桿商品核准。私募信貸贖回壓力無披露，是 R3 判讀中最大的盲點：如果非銀行基金正在累積贖回壓力而沒被觀察到，R3 的距離可能被高估。backlog 重複計算風險（RPO double-counting）本次只有 Microsoft 對 OpenAI 一家的披露，無法把多家供應商的承諾加總。

主要不確定性：

1. 9/16 FOMC：升息定價約 45%。如果實際升息，同時打擊高估值股權與已轉向舉債的 hyperscaler 融資，會把答案推向 yes（R1 與 R3 同時受壓）。
2. AI 信用重定價會不會擴散：CoreWeave 利差與 Oracle CDS 持續走闊，如果擴散到更多 neocloud 並造成再融資失敗，R3 會快速接近門檻，也可能透過股價連動觸發 R1。這是推向 yes 的主要路徑。
3. 2026 Q3 財報季（確切日期不在本次證據中）：如果有兩家 hyperscaler 下修 capex，R2 會直接成立；目前方向是上修，比較可能推向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7748.5 | FRED API (series_id=SP500) sp500_trend | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 9.67 | FRED API (series_id=SP500) sp500_trend | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 11.23 | FRED API (series_id=SP500) sp500_trend | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29742.6 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-06-02 | 2026-08-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（回撤 %） | 2.99 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1，家庭股票配置 %） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.72 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.79 | FRED API (series_id=BAMLC0A0CM) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.7 | FRED API (series_id=DGS10) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（對 2026-08-10） | -2.0 | FRED API (series_id=DGS10) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.43 | FRED API (series_id=DFII10) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.26 | FRED API (series_id=T10YIE) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD） | 84.77 | FRED API (series_id=DCOILWTICO) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.28 | FRED API (series_id=T5YIFR) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（%，Kim-Wright） | 0.8257 | FRED API (series_id=THREEFYTP10) | 2026-08-07 | 2026-08-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.64 | FRED API (series_id=SOFR) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.73 | FRED API (series_id=SOFR99) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-13 | 2026-08-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6748567.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-05 | 2026-08-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5923023.0（€5.92T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-07 | 2026-08-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.28 | FRED API (series_id=VIXCLS) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of，comove=false） | 15.28 | FRED API vix_spx_comove block | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（七日窗，base 2026-08-04） | -7.39 | FRED API vix_spx_comove block | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（七日窗） | -0.11 | FRED API vix_spx_comove block | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（十億美元） | 2002.4852（$2.00T） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-29 | 2026-08-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7423067 | CFTC TFF cftc_lev_funds | 2026-08-04 | 2026-08-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 149977 | CFTC TFF cftc_lev_funds | 2026-08-04 | 2026-08-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（^MOVE） | 72.09 | Yahoo chart API move_index | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2385.3 | OFR STFM ofr_repo (REPO-TRIV1_TV_TOT-P) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S vs 10-year averages | Fool research SEARCH（AI leader P/S vs 10 年均值未取得） | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 [primary: SEARCH]，90d＋同季 | ✗ NOT DISCLOSED（無指定 top-tier 券商的可拆解同季上調） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場 [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) YTD divergence | 24/7 Wall St SEARCH | ⛔ FETCH FAILED（僅取得 2026-06-10 舊值，無現行快照） |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | RBC Wealth Management SEARCH | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | Investing.com breadth SEARCH（以 >50DMA 比例為代理） | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA via Advisor Perspectives SEARCH，stock-of-state | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | AAII [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag SEARCH，7d | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／YCharts [primary: SEARCH] | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 SEARCH | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | RTTNews auction recap [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | investing／Yicai SEARCH | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC／interval fund 披露 [primary: SEARCH]，30d | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報彙總報導 SEARCH，stock-of-state（2026 Q2 財報） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 SEARCH | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | VentureBeat 等報導 SEARCH | ✗ NOT DISCLOSED（僅上一季 2026-05-29 結果） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話會議報導 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | jarvislabs／TrendForce [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報／發債報導 [primary: SEARCH]；quarterly_state 沿用、event_scan 30d | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 [primary: SEARCH]，stock-of-state 沿用 | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q [primary: SEARCH]，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速＋進出場事件 [primary: SEARCH]；quarterly_state 沿用、event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days +AI rename / SPAC | Reuters／Benzinga／SEC SEARCH，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | IPOScoop SEARCH，7d | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／StockAnalysis gainers [primary: SEARCH]，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 SEARCH，30d | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR／openinsider [primary: SEC EDGAR]，14d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | thetrading.tools [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing／etf.com [primary: SEARCH]（個別 ticker AUM 未取得） | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire 發行公告 SEARCH，30d | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA SEARCH，7d | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe Q2 2026 slides SEARCH | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC monthly | OCC 月報 SEARCH | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe insights SEARCH（股債相關性未取得） | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | FINRA via Advisor Perspectives，交叉引用 | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | 融資公告 [primary: SEARCH]，30d | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）；WebSearch 補充無新事件 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.85（原定來源 multpl／gurufocus） | S&P 500 trailing P/E CAPE August 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.34 | S&P 500 trailing P/E CAPE August 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E 約 29x vs 指數約 25.6x、佔市值約 33.9% | Magnificent 7 weighted PE vs S&P 500 August 2026 | https://www.fool.com/research/magnificent-seven-sp-500/ （The Motley Fool） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 貸款利差 +100–125bp、Oracle 5Y CDS 約 75bp（7 年高）、Fitch／Moody's 預警 | CoreWeave Oracle CDS spread AI credit widening August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm （Tech Times） | 2026-08-03 | 2026-08-13T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度約 37% | S&P 500 top 10 concentration percent 2026 | https://www.rbcwealthmanagement.com/en-us/insights/the-great-narrowing-sp-500-concentration （RBC Wealth Management） | 2026-07-24 | 2026-08-13T09:30:00+08:00 |
| breadth.advance_decline | S&P 500 成分股 >50DMA 比例約 71.6%（A/D 代理；原定 A/D 與新高新低比未取得） | S&P 500 percent above 50 day moving average August 2026 | https://www.investing.com/indices/s-p-500-stocks-above-50-day-average （Investing.com） | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 61（Greed） | CNN Fear and Greed Index August 12 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives，原定 FINRA） | 2026-07-20 | 2026-08-13T09:30:00+08:00 |
| retail.aaii | AAII Bull 37.0%／Neutral 25.0%／Bear 38.0%（週結束 2026-08-05） | AAII investor sentiment survey week August 5 2026 | https://seekingalpha.com/article/4932187-aaii-sentiment-survey-optimism-jumps （Seeking Alpha，原定 aaii.com） | 2026-08-06 | 2026-08-13T09:30:00+08:00 |
| monetary.treasury_auctions | 3Y（08-11）bid-to-cover 2.71、tail −0.5bp；10Y（08-12）bid-to-cover 2.58、需求略高於均值 | US Treasury 3 year 10 year auction bid to cover August 2026 | https://www.rttnews.com/3679611/ten-year-note-auction-attracts-modestly-above-average-demand.aspx （RTTNews） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 9/16 升息定價約 45%、無降息定價 | CME FedWatch September 2026 rate hike probability | https://cryptobriefing.com/traders-45-percent-chance-september-fed-rate-hike/ （Crypto Briefing，原定 CME FedWatch） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| ai.hyperscaler_capex | MSFT／GOOGL／AMZN／META 2026 capex 合計約 $725B、仍上修（2026 Q2 財報） | hyperscaler capex 2026 725 billion raised Q2 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-08-13T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft 商用 RPO 約 $678B、約 32% 繫單一客戶（OpenAI） | Microsoft RPO backlog 678 billion OpenAI 2026 | https://www.benzinga.com/trading-ideas/long-ideas/26/07/60816147/microsofts-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer （Benzinga） | 2026-07-30 | 2026-08-13T09:30:00+08:00 |
| ai.compute_supply_demand | H200 租金中位約 $3.99/hr、HBM 合約約 +40%、Blackwell 售罄 | H200 GPU rental HBM DRAM 2026 shortage Blackwell | https://jarvislabs.ai/blog/h200-price （Jarvislabs） | 2026-08-01 | 2026-08-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 超越 FCF（Alphabet Q2 FCF 轉負）、2026 發債約 $182B | hyperscaler capex FCF debt issuance 182 billion 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure （Sage Advisory） | 2026-07-24 | 2026-08-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan][spv_deal] Meta El Paso 資料中心表外結構 >$12B 債券（BlackRock 主導，triple-net lease） sponsor_equity_split=undisclosed;residual_value_guarantee=undisclosed;lease_term=20-30yr;debt_tenor=undisclosed;lead_lenders=BlackRock/JPMorgan/MS; | hyperscaler capex vs free cash flow debt 2026 | https://www.landgate.com/news/blackrock-s-12-billion-bond-sale-signals-a-new-financing-playbook-for-data-center-developers （Landgate） | 2026-07-20 | 2026-08-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $72B vs 年化 capex 約 $725B（分母：top-4＋Oracle；沿用組合值） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-06-15 | 2026-08-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收 IPO 合格事件 0 件 | AI rename ticker SPAC no revenue IPO August 6-13 2026 | Reuters／Benzinga／SEC 螢幕 | — | 2026-08-13T09:30:00+08:00 |
| speculation.ipo_heat | 08-12／08-13 各約 12 檔定價、平均首日約 18% | US IPO pricings week August 2026 IPOScoop | https://www.iposcoop.com/current-year-pricings/ （IPOScoop） | 2026-08-13 | 2026-08-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot 合格 0 件 | microcap 100% single day quantum fusion nuclear AI August 2026 | Finviz／StockAnalysis gainers 螢幕 | — | 2026-08-13T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 9 月上市、估值約 $730–850B；Anthropic 續進 | OpenAI Anthropic IPO timing valuation 2026 | https://cryptobriefing.com/openai-ipo-filing-trillion-valuation/ （Crypto Briefing） | 2026-07-28 | 2026-08-13T09:30:00+08:00 |
| speculation.insider_form4 | 過去 14 日 AI／領導股合格 Form 4 賣壓 cluster 0 件 | AI leadership insider Form 4 sale July 30 August 13 2026 SEC | openinsider／secform4／SEC EDGAR 螢幕 | — | 2026-08-13T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity-only put/call 0.54（日讀數） | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio （thetrading.tools，原定 Cboe） | 2026-08-07 | 2026-08-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 約 $198B（記錄高） | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing，原定 etf.com） | 2026-07-23 | 2026-08-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 08-11 新發 6 檔單股 2x 槓桿 ETF（Leverage Shares／Tradr） | single-stock leveraged ETF launch August 11 2026 Leverage Shares Tradr | https://www.globenewswire.com/news-release/2026/08/11/3342794/0/en/leverage-shares-by-themes-launches-three-new-2x-etfs-targeting-ai-infrastructure-and-connectivity-leaders.html （GlobeNewswire） | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量約 65%（Cboe Q2 2026） | 0DTE SPX options share Cboe Q2 2026 65% | https://ca.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4768656 （Investing.com） | 2026-07-31 | 2026-08-13T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月總量 1,603,491,559 口（約 16.0 億口） | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-08-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 135.59、VIX 15.28、MOVE 74.67 | VIX SKEW MOVE bond volatility August 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-10-2026-spx-skew-collapses-on-upside-chasing （Cboe） | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt（2026-06 月資料）$1.502T、+51.5% YoY（交叉引用） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-08-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B 貸款融資，被迫調高利差 +100–125bp＋covenant | CoreWeave 2.6 billion loan spread covenant August 2026 | https://www.stocktitan.net/news/CRWV/core-weave-closes-2-6-billion-loan-facility-expanding-financing-gwhngwnf0jt5.html （StockTitan） | 2026-07-29 | 2026-08-13T09:30:00+08:00 |

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
  "r1_drawdown_pct": 2.99,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

> [DRY RUN] this report was not committed to archive.

# 2026-07-27 AI 泡沫破裂預測報告

報告日期：2026-07-27｜ISO 週次：2026-W31｜預測窗口：2026-07-27 → 2027-01-25｜前次基準：report-2026-07-23（4天前）

## 結論

**結論：no**

三條路徑目前都離觸發條件很遠。NASDAQ-100 距 52 週高點回撤 8.26%，還要再跌約 18.25% 才到 R1 門檻；四家 hyperscaler 中已知的唯一新指引（Alphabet，2026-07-22）是上修 capex，不是下修。私募信貸贖回壓力（BCRED gate proration / breach）和 AI 信用定價分歧屬於真實的後期訊號，但 HY／IG OAS 仍很緊、repo 市場平穩，現有證據不足以推翻「182 天內三條件都不成立」這個基準。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 28,128.34（2026-07-24）；252 個交易日最高收盤 30,660.6（2026-06-02）；距 52 週高點回撤 8.26%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，從最新收盤還要再跌約 18.25%（約 5,133 點）才會觸及。如果窗口內指數先創新高，門檻會跟著上移。

背景：S&P 500 為 7,411.98（2026-07-24），高於 200 日均線 5.8%、高於 52 週均線 7.4%（`valuation.sp500_trend`），屬中度延伸，不是極端偏離。VIX 18.58（2026-07-24），7 日視窗（2026-07-17 → 2026-07-24）VIX −1.01%、S&P 500 −0.61%，co-movement 為 false（`structural.vix_spx_comove`）。窗口內最近的催化劑是 2026-07-29 FOMC：CME FedWatch 顯示約 61% 持平、約 38% 升息（`monetary.fedwatch`）；同時 CPI YoY 3.46%（2026-06 資料，`monetary.cpi_yoy`）、10Y 殖利率 4.71%（2026-07-23，`monetary.dgs10`），這些都限制了 Fed 以降息緩衝 AI 主導回檔的空間。

**判讀：** R1 距門檻還有約 18 個百分點，近期沒有已經在進行的急跌。要在窗口內觸發，需要一個外部衝擊，例如升息落地加上 AI 信用重定價、或 hyperscaler 財報下修 capex 造成的連鎖拋售，把跌幅從 8.26% 擴大到 25%。

### R2 資本支出收縮

- Alphabet：2026-07-22（2026 Q2 財報）將 2026 年 capex 指引上修至約 $195–205B，方向為上修（`ai.hyperscaler_capex`）。
- Microsoft：本次證據沒有載明其最新正式指引或方向，方向不可判。
- Amazon：本次證據沒有載明其最新正式指引或方向，方向不可判。
- Meta：本次證據沒有載明其最新正式指引或方向，方向不可判。
- 同一來源的 hyperscaler 2026 年 capex 合計約 $725B 以上（2026-07-22，`ai.hyperscaler_capex`）。

目前已知下修家數為 0／4（Alphabet 上修，其餘三家本次證據未載明）。其餘三家的下一次財報日期不在本次證據內，不在此推估；窗口（至 2027-01-25）在正常財報節奏下會涵蓋多次季度財報。需求面：伺服器 DRAM 3Q26 合約價 +13–18% QoQ、交期 30–40 週以上（2026-07-03，`ai.compute_supply_demand`），代表算力供給仍然吃緊，沒有出現 order digestion 的證據。

**判讀：** R2 需要四家中兩家下修，目前沒有任何一家下修，最新的訊號（Alphabet）甚至是上修。只有在 R1 式市場重挫或融資成本急升、迫使管理層在窗口內財報同時收縮指引時，R2 才可能成立。

### R3 AI 信用事件

- 符合 R3 規模門檻（以 AI 算力為主業、負債 ≥ 50 億美元）最明確的借款人是 CoreWeave：已披露以 GPU 擔保的債務約 $24.9B（2026-07-12，`structural.ai_infrastructure_debt`）。同一來源列出 Broadcom／Anthropic $35B、Oracle $38B 加上密州 $16.3B 的融資，但這些借款人或交易主體的主業是否為 AI 資料中心／算力，本次證據無法確認，暫不列入 R3 候選。
- 信用定價：AI 單一發行人利差走闊，而 CDX IG 持平；hyperscaler 2026 年發債約 $182B（2026-07-16，`valuation.ai_credit_schism`），符合 AI 信用定價分歧（equity-vs-credit schism）中「信貸端先重定價」的後期型態，但本次證據沒有發行人層級的利差或 CDS 數值。
- 傳導通道：BCRED Q2 的 redemption-request ratio 約 10% NAV，超過 5% quarterly redemption cap，發生 gate proration / breach（50% 比例撥付），並出現 net inflow→outflow flip（淨流出約 $1.2B，2026-07-23，`monetary.private_credit_liquidity`），屬私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）的實際事件。
- 整體信用環境：HY OAS 2.77%、IG OAS 0.79%（皆 2026-07-23，`monetary.hy_oas`、`monetary.ig_oas`），仍處緊縮區間。
- 本次證據沒有任何候選借款人出現付款違約、covenant waiver、distressed exchange 或 going-concern 字句，也沒有近期到期牆的具體金額。

**判讀：** R3 有傳導管線（私募信貸贖回、AI 單一發行人利差走闊），但沒有任何違約或困境交換的前兆。要在窗口內成立，需要 CoreWeave 等級的借款人在再融資時失去市場准入，而目前 HY 利差 2.77% 不支持這種情境。

## 支持 yes 的證據

- [R3] BCRED Q2 redemption-request ratio 約 10% NAV，超過 5% quarterly redemption cap，發生 gate proration / breach（50% 比例撥付），淨流出約 $1.2B（2026-07-23），是私募信貸贖回壓力的實際事件，而不是單純的結構存在（`monetary.private_credit_liquidity`）。
- [R3] AI 信用定價分歧：AI 單一發行人利差走闊而 CDX IG 平穩，hyperscaler 2026 年發債約 $182B（2026-07-16）；信貸端先於股權端重定價是典型的後期訊號（`valuation.ai_credit_schism`）。
- [R3] AI infrastructure debt financing / vendor-financing loops 規模持續擴大：CoreWeave GPU 擔保債務約 $24.9B、Broadcom／Anthropic $35B、Oracle $38B 加上密州 $16.3B（2026-07-12），以 GPU 為擔保品的槓桿讓 R3 一旦觸發就會很劇烈（`structural.ai_infrastructure_debt`）。
- [整體] 散戶槓桿與估值處於歷史頂部區：FINRA margin debt $1.502T、YoY +51.5%（2026-06 資料，2026-07-20 發布，落在 1999／2007／2021 頂部附近的 +40–50% 區間以上）（`retail.margin_debt`）；Shiller CAPE 40.46、trailing P/E 28.52（2026-07-24，`valuation.sp500_pe_cape`）。
- [R1] 政策與利率逆風：CME FedWatch 顯示 2026-07-29 約 38% 升息機率（2026-07-25，`monetary.fedwatch`），CPI YoY 3.46%（`monetary.cpi_yoy`），10Y 殖利率 4.71%（`monetary.dgs10`），20Y 標售 tail +0.5bp、dealer takedown 14.67%（2026-07-22，`monetary.treasury_auctions`），Fed 緩衝回檔的空間有限。
- [R1] 部位擁擠與廣度轉薄：NAAIM Exposure Index 84.02（2026-07-22，`retail.naaim`）；NYSE 新高家數由 175 降至 78（2026-07-21，`breadth.advance_decline`）；Top-10 集中度約 37%（`breadth.top10_concentration`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）仍大：年化 capex 約 $725B，而 AI 終端營收只在低百億級（分母：來源所列 hyperscaler 合計，非全產業；capex 組件 2026-07-22、營收組件 2026-06-15）（`ai.revenue_capex_gap`）；Alphabet 上修 capex 也讓回本壓力更集中在未來幾個季度。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 8.26%（2026-07-24），距 R1 門檻 22,995.45 還要再跌約 18.25%，182 天內這個幅度的跌勢需要一個目前看不到的衝擊（`valuation.ndx_drawdown`）。
- [R2] 唯一已知的新指引是上修：Alphabet 於 2026-07-22 將 2026 capex 上修至約 $195–205B，hyperscaler 合計約 $725B 以上，四家中已知下修家數為 0（`ai.hyperscaler_capex`）。
- [R2] 算力需求仍然吃緊：伺服器 DRAM 3Q26 合約價 +13–18% QoQ、交期 30–40 週以上（2026-07-03），沒有 order digestion 或庫存堆積的證據（`ai.compute_supply_demand`）。
- [R3] 整體信用利差仍緊：HY OAS 2.77%、IG OAS 0.79%（2026-07-23，與前次持平），市場沒有替大規模違約定價（`monetary.hy_oas`、`monetary.ig_oas`）。
- [整體] 美債與 repo 市場沒有失序：repo 資金壓力（SOFR−IORB）為 −1.0bp、SOFR99−IORB 為 +7.0bp（2026-07-23），SRF 動用（Standing Repo Facility usage）只有 $0.001bn（2026-07-24）（`monetary.repo_stress_srf`）；MOVE 76.82（2026-07-24）、槓桿基金美債期貨淨部位 −7,462,516 口，4 週變動 −45,392 口（2026-07-21）（`structural.treasury_basis_trade`）。
- [R1] 情緒不是狂熱：CNN Fear & Greed 39（Fear，2026-07-24，`retail.fear_greed`）、AAII Bear 42.3% 高於 Bull 29.6%（2026-07-23，`retail.aaii`）、VIX／S&P 500 co-movement 為 false（`structural.vix_spx_comove`），反向指標不支持近期頂部急跌。
- [整體] 龍頭估值沒有脫離盈餘：Mag 7 相對其餘 493 檔僅溢價約 10%、NVDA NTM P/E 約 18.7（2026-07-08，`valuation.mag7_multiples`）；Morgan Stanley NVDA 目標價 $288 為 EPS-driven，target PE 沒有擴張（2026-07-13，`valuation.analyst_tp_decomposition`）。

## 與前期比較

前次結論：無前次預測（report-2026-07-23 為舊格式評分報告）

前次為舊格式評分報告，不轉換為 yes／no；flip_evidence 為空。自 2026-07-23 以來的主要變化：

- NASDAQ-100 由 28,454.81（2026-07-23）降至 28,128.34（2026-07-24），回撤擴大到 8.26%，仍遠離 R1 門檻。
- 10Y 分解：ΔDGS10 0.0bp、ΔDFII10 0.0bp（DGS10、DFII10 自 2026-07-23 起無新觀測）、ΔT10YIE −2.0bp；判讀：不可判（視窗不一致）。
- HY／IG OAS、Fed funds（3.50–3.75%）、WALCL $6.75T 都沒有變化；S&P 500 +0.05%；VIX −0.12。
- 新事件：Alphabet capex 上修（2026-07-22）、BCRED gate proration / breach（2026-07-23）、20Y 標售 tail +0.5bp（2026-07-22）。

## 資料缺漏與不確定性

⛔ FETCH FAILED 來源：

- `structural.zero_dte`（required）：只找到 2026-02 的 Cboe 記錄（0DTE 佔 SPX 約 56%），沒有當期數值。0DTE 是短線投機強度的確認指標，不會改變三條路徑的距離，因此不影響結論。
- `structural.options_volume`（required）：只找到 OCC 2026-06 月報頁面（7 月尚未發布），證據中沒有可引用的成交量數值。同樣只是確認指標，不影響結論。

✗ NOT DISCLOSED（篩選完成但沒有合格披露）：`institutional.bofa_jpm_survey`、`ai.token_growth`、`ai.openai_anthropic_revenue`（只找到 Epoch 2026-06-15 的 Anthropic 約 $47B／OpenAI 約 $25B run-rate，屬前一季，只作背景）、`ai.customer_concentration_rpo`、`ai.hyperscaler_financing_mix`（quarterly_state 可用：Alphabet Q2 FCF −$5.9B、AI 相關 IG 發債累計約 $218–250B；但 30 日內沒有發行人層級的融資事件，event_scan 為 not_disclosed）、`ai.depreciation_life`、`ai.capital_cycle`（兩個組件都沒有可用披露，本次不判定資本週期階段）、`structural.global_leveraged_approvals`。其中 `ai.hyperscaler_financing_mix` 的 FCF 轉負是值得追蹤的 hyperscaler 融資結構（capex vs FCF / 發債）訊號，但只是單一公司、單一季度，不足以改變 R2／R3 判讀。

其他資料品質註記：`structural.cross_asset_derivatives` 的搜尋結果把 VIX 18.58 標為 2026-07-22，但 FRED VIXCLS 顯示 18.58 是 2026-07-24 的值（2026-07-22 為 16.64），因此本報告的 VIX 一律以 VIXCLS 為準，該來源只引用 SKEW。`speculation.insider_form4` 沒有取得一手 SEC EDGAR Form 4 URL，因此記為 0 件，不列出任何具名交易。美債期限結構的 rolling stock-bond correlation 本次沒有取得。

最大的三個不確定性：

1. Microsoft、Amazon、Meta 的最新 capex 指引與方向本次證據未載明。若其中兩家在窗口內財報下修，R2 會直接成立，結論會轉為 yes；目前產業訊號（Alphabet 上修、DRAM 吃緊）指向相反方向。
2. 2026-07-29 FOMC 約 38% 升息機率。若升息落地並引發長端利率上行，會同時加壓 R1（估值）與 R3（再融資成本），使結論往 yes 移動。
3. 私募信貸贖回壓力是否擴散：目前只有 BCRED 一檔的 gate proration / breach。如果多檔基金跟進、AI 單一發行人利差擴大到 HY 指數層級，R3 和 R1 的連動風險會明顯上升。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7411.98 | FRED API (series_id=SP500) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線偏離） | 5.8% | FRED API (series_id=SP500) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線偏離） | 7.4% | FRED API (series_id=SP500) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28128.34 | FRED API (series_id=NASDAQ100) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤） | 8.26% | FRED API (series_id=NASDAQ100) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q1，家庭股票配置 % 金融資產） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-27T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限） | 3.75% | FRED API (series_id=DFEDTARU) | 2026-07-26 | 2026-07-27T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限） | 3.5% | FRED API (series_id=DFEDTARL) | 2026-07-26 | 2026-07-27T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.77% | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.79% | FRED API (series_id=BAMLC0A0CM) | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.71% | FRED API (series_id=DGS10) | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.43% | FRED API (series_id=DFII10) | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.26% | FRED API (series_id=T10YIE) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | -2.0 bp | FRED API (series_id=T10YIE) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 84.38（USD/bbl） | FRED API (series_id=DCOILWTICO) | 2026-07-20 | 2026-07-27T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46% | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-27T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.28% | FRED API (series_id=T5YIFR) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright 10Y 期限溢價） | 0.7787% | FRED API (series_id=THREEFYTP10) | 2026-07-17 | 2026-07-27T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.64% | FRED API (series_id=SOFR) | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.72% | FRED API (series_id=SOFR99) | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65% | FRED API (series_id=IORB) | 2026-07-27 | 2026-07-27T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（Fed 隔夜 repo 操作 transaction volume） | 0.001（$bn） | FRED API (series_id=RPONTTLD) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps（SOFR−IORB，兩腿皆 2026-07-23） | -1.0 bp | FRED API (series_id=SOFR, IORB) | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr99_iorb_bps（SOFR99−IORB，兩腿皆 2026-07-23） | 7.0 bp | FRED API (series_id=SOFR99, IORB) | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6747378.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5949077.0（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-17 | 2026-07-27T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6395509.0（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-27T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 18.58 | FRED API (series_id=VIXCLS) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of 2026-07-24，base 2026-07-17，7 日視窗） | 18.58 | FRED API (series_id=VIXCLS, SP500) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | -1.01% | FRED API (series_id=VIXCLS, SP500) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -0.61% | FRED API (series_id=VIXCLS, SP500) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2012.1032（$2.01T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-15 | 2026-07-27T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六個 CBT 美債期貨合約槓桿基金淨部位） | -7462516（口） | CFTC TFF futures-only | 2026-07-21 | 2026-07-27T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -45392（口） | CFTC TFF futures-only | 2026-07-21 | 2026-07-27T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 76.82 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2304.9（$bn） | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation｜S&P 500 P/E and Shiller CAPE | multpl.com，WebSearch primary | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation｜Mag 7 weighted P/E and AI leader P/S vs 10-year averages | CNBC／Morgan Stanley 摘要，WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation｜Analyst TP upgrade decomposition for Mag 7 / TSMC / AI semi bellwethers | 賣方 TP 調升，WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | Valuation｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導，WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) YTD divergence | 247wallst，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth｜Top-10 concentration in S&P 500 | P&I，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth｜Advance/decline ratio, new high/low ratio | Leuthold NYSE breadth，WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment｜CNN Fear & Greed Index | CNN F&G（MacroMicro 鏡像），WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment｜Margin Debt: FINRA monthly data | FINRA via Advisor Perspectives，WebSearch | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment｜Retail survey: AAII Investor Sentiment | aaii.com，WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment｜Social sentiment proxies | r/wallstreetbets／cashtag，WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment｜NAAIM Exposure Index | YCharts，WebSearch primary | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | Institutional Sentiment｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查報導，WebSearch | ✗ NOT DISCLOSED（搜尋完成，無當期新調查） |
| monetary.fed_funds | Monetary & Credit｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit｜美債標售需求（auction tail / bid-to-cover） | 標售回顧，WebSearch primary（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit｜Fed funds rate path expectations | CME FedWatch 摘要，WebSearch primary | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit｜Global central bank liquidity cross-check — ECB / BOJ balance sheets | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit｜PBoC aggregate financing / liquidity operations | Bloomberg 摘要，WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit｜Private-credit / non-bank fund liquidity stress | BDC 披露，WebSearch primary（30d） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI Fundamentals｜Hyperscaler capex guidance | 季報 capex 指引，WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals｜AI token volume growth rate | Anthropic／OpenAI／Google 披露，WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI Fundamentals｜OpenAI / Anthropic annualized revenue | Epoch／報導，WebSearch | ✗ NOT DISCLOSED（只有前一季 2026-06-15 資料） |
| ai.customer_concentration_rpo | AI Fundamentals｜Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話，WebSearch primary | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals｜AI compute supply/demand and overcapacity risk | TrendForce，WebSearch primary | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：季報 capex／FCF＋發債趨勢；event_scan：30d 發行人層級融資，WebSearch primary | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露，WebSearch primary（carry-forward） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q／法說，WebSearch primary（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals｜資本週期階段（capital cycle stage） | quarterly_state：供需增速；event_scan：30d 進出場事件，WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior｜Search for past 7 days: AI rename / SPAC / no-revenue IPO | Boardroom Alpha 等，WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | Speculative Behavior｜IPO market heat | Renaissance Capital，WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior｜Microcap thematic moonshots | Finviz／Benzinga／StockTwits／Yahoo movers，WebSearch primary（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior｜Upcoming AI IPOs | 具名報導，WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior｜Insider selling at AI / market-leadership companies | SEC EDGAR／openinsider（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior｜Cboe equity-only put/call ratio | YCharts，WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage｜US leveraged ETF AUM | etf.com 等，WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage｜US single-stock leveraged ETF approvals | 發行商新聞稿／ETF.com，WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | Structural Leverage｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA，WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage｜0DTE option volume | Cboe，WebSearch | ⛔ FETCH FAILED（只取得 2026-02 記錄，無當期值） |
| structural.options_volume | Structural Leverage｜Options total volume | OCC 月報，WebSearch | ⛔ FETCH FAILED（只取得 6 月月報頁面，無可引用數值） |
| structural.cross_asset_derivatives | Structural Leverage｜Cross-asset derivatives / correlation checks | Cboe／Yahoo，WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage｜Cross-reference only: FINRA margin debt | 交叉引用 Retail Sentiment margin debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage｜AI infrastructure debt financing / vendor-financing loops | WebSearch primary（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py：cftc_lev_funds、move_index、ofr_repo（any） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 28.52 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 40.46 | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 對其餘 493 溢價約 10%、NVDA NTM P/E 約 18.7 | Magnificent 7 valuation premium cheapest decade July 2026 | https://www.cnbc.com/2026/07/08/magnificent-seven-stocks-are-the-cheapest-in-a-decade-by-one-measure.html （CNBC） | 2026-07-08 | 2026-07-27T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標價 $288（約 22× EPS；target PE 未擴張，EPS-driven；舊目標價未載明） | Morgan Stanley NVDA target 288 July 2026 EPS | https://www.gurufocus.com/news/8955458/morgan-stanley-upgrades-nvidia-nvda-with-a-288-target-price （GuruFocus） | 2026-07-13 | 2026-07-27T09:30:00+08:00 |
| valuation.ai_credit_schism | AI 單一發行人利差走闊 vs CDX IG 平穩；hyperscaler 2026 發債約 $182B | AI issuer credit spread CDS widening vs CDX IG July 2026 | https://247wallst.com/investing/2026/07/16/the-ai-revolution-is-reshaping-credit-markets-here-is-what-it-really-says-about-risk/ （24/7 Wall St.） | 2026-07-16 | 2026-07-27T09:30:00+08:00 |
| breadth.rsp_spy | RSP +12.39% YTD，領先 SPY 約 5pp | RSP vs SPY equal weight YTD 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St.，資料日 2026-07-24） | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度約 37% | S&P 500 top 10 concentration percent 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/ （Pensions & Investments） | 2026-07-15 | 2026-07-27T09:30:00+08:00 |
| breadth.advance_decline | NYSE A/D 線創 12 月新高；新高家數 78（前值 175） | NYSE advance decline new highs July 2026 | https://research.leutholdgroup.com/categories/nyse-advancedecline.1440 （Leuthold Group） | 2026-07-21 | 2026-07-27T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 39（Fear） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/series/22748/cnn-fear-and-greed （MacroMicro，原定來源 cnn.com） | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-06 月資料）$1.502T，YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives，原定來源 FINRA） | 2026-07-20 | 2026-07-27T09:30:00+08:00 |
| retail.aaii | AAII Bull 29.6%／Bear 42.3% | AAII investor sentiment survey July 23 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| retail.social_sentiment | WEN（Wendy's）r/wallstreetbets 軋空 +25%（非 AI 標的） | WEN Wendys wallstreetbets short squeeze July 2026 | https://altindex.com/wallstreetbets （AltIndex） | 2026-07-25 | 2026-07-27T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 84.02 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number （YCharts，原定來源 naaim.org） | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| monetary.treasury_auctions | 20Y 標售 high yield 5.163%、tail +0.5bp、dealer takedown 14.67% | US Treasury 20Y auction July 22 2026 tail bid to cover | https://investinglive.com/news/us-treasury-auctions-off-13-billion-of-20-year-bonds-at-a-high-yield-of-5-163 （investingLive） | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 2026-07-29 FOMC：約 61% 持平／約 38% 升息 | CME FedWatch July 29 2026 hike hold probability | https://www.cnbc.com/2026/07/13/-a-july-rate-hike-from-the-fed-the-odds-are-rising.html （CNBC，原定來源 CME FedWatch） | 2026-07-25 | 2026-07-27T09:30:00+08:00 |
| monetary.pboc | 人行 LPR 持穩、MLF 淨投放 ¥100B | PBoC MLF net injection LPR July 2026 | https://www.bloomberg.com/news/articles/2026-07-24/pboc-adds-most-liquidity-to-economy-in-five-months-to-aid-growth （Bloomberg） | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| monetary.private_credit_liquidity | BCRED Q2 redemption-request ratio 約 10% NAV，超過 5% quarterly redemption cap；gate proration / breach（50% 比例撥付）；淨流出約 $1.2B | Blackstone BCRED Q2 2026 redemption 5% cap breach proration | https://www.benzinga.com/markets/private-markets/26/07/60649546/blackstone-says-bcred-redemptions-have-materially-slowed （Benzinga） | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| ai.hyperscaler_capex | Alphabet 2026 capex 指引上修至約 $195–205B（Q2 財報）；hyperscaler 2026 capex 合計約 $725B 以上 | Alphabet raises 2026 capex 205B Q2 hyperscaler | https://mlq.ai/news/alphabet-raises-2026-capex-guidance-to-195-205b-cloud-revenue-surges-82/ （MLQ.ai） | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 +13–18% QoQ、交期 30–40 週以上 | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html （TrendForce） | 2026-07-03 | 2026-07-27T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] Alphabet FY26 capex 上修至約 $205B，Q2 FCF −$5.9B | Alphabet capex 205B Q2 2026 FCF negative debt | https://mlq.ai/news/alphabet-raises-2026-capex-guidance-to-195-205b-cloud-revenue-surges-82/ （MLQ.ai） | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] AI 相關 IG 發債累計約 $218–250B（發債趨勢，非單一發行人事件） | AI bond issuance 250B July 2026 hyperscaler | https://www.morningstar.com/bonds/bond-issuance-backing-ai-investment-tops-250b-testing-limits-voracious-investor-demand （Morningstar） | 2026-07-08 | 2026-07-27T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex 約 $725B vs AI 終端營收低百億級（分母：來源所列 hyperscaler 合計；營收組件 2026-06-15，capex 組件 2026-07-22） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-06-15 | 2026-07-27T09:30:00+08:00 |
| speculation.ai_rename_spac | 2 件合格 SPAC：BRTMU $325M（AI 標的）、SCATU $100M | SPAC IPO announcement July 21 2026 AI | https://www.boardroomalpha.com/research/spac-market-update-july-21-2026-cdaq （Boardroom Alpha） | 2026-07-21 | 2026-07-27T09:30:00+08:00 |
| speculation.ipo_heat | Renaissance IPO Index +16.7% YTD，pipeline 持續建置 | US IPO market 2026 Renaissance IPO index YTD | https://www.renaissancecapital.com/IPO-Center/Stats （Renaissance Capital） | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| speculation.microcap_moonshots | 7 日內合格 microcap moonshot 0 件 | microcap 100% single day quantum AI fusion moonshot July 2026 | Finviz biggest gainers、Benzinga movers、StockTwits trending、Yahoo day gainers | — | 2026-07-27T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 程序（估值 $965B，投資人會議）；OpenAI 傳目標 9 月 | Anthropic OpenAI IPO July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html （CNBC） | 2026-07-15 | 2026-07-27T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 cluster 0 件（無一手 EDGAR filing URL，不列具名交易） | insider Form 4 cluster AI leaders July 2026 openinsider | SEC EDGAR、openinsider | — | 2026-07-27T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.61（日讀數） | Cboe equity put call ratio July 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio （YCharts，原定來源 Cboe） | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 約 $198B（個別 NVDL／TSLL／CONL／TQQQ／SOXL／SQQQ 未拆分） | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing，原定來源 etf.com） | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| structural.us_single_stock_etf | Tradr 5 檔 2X 單股 ETF、Leverage Shares 6 檔 ±2X 單股 ETF 上市 | single-stock leveraged ETF launch July 2026 Tradr Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-07 | 2026-07-27T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 150.19；VIX 期限結構 contango（VIX 水位改用 VIXCLS） | VIX term structure SKEW July 2026 | https://finance.yahoo.com/quote/%5ESKEW/history/ （Yahoo Finance，原定來源 Cboe） | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-06 月資料）$1.502T、YoY +51.5%，交叉引用 Retail Sentiment，不重複計算 | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-07-27T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Broadcom／Anthropic $35B；Oracle $38B 加上密州 $16.3B；CoreWeave GPU 擔保債務 $24.9B | AI data center debt financing July 2026 Broadcom Anthropic Oracle CoreWeave | https://www.techtimes.com/articles/320239/20260712/nvidia-circular-financing-249b-coreweave-debt-puts-pension-funds-risk.htm （Tech Times） | 2026-07-12 | 2026-07-27T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-07-27",
  "iso_week": "2026-W31",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-01-25",
  "prior_date": "2026-07-23",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 8.26,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

> [DRY RUN] this report was not committed to archive.

# 2026-08-10 AI 泡沫破裂預測報告

報告日期：2026-08-10｜ISO 週次：2026-W33｜預測窗口：2026-08-10 → 2027-02-08｜前次基準：report-2026-08-06（4天前）

## 結論

**結論：no**

三條路徑都沒有已在進行、且可望於 182 天內完成的跡象：NASDAQ-100 距 52 週高點回撤 3.06%，離 R1 門檻尚需再跌約 22.63%；hyperscaler 2026 capex 合計仍在上修（≈$725B，`ai.hyperscaler_capex`），R2 方向相反。R3 端 CoreWeave CDS ≈855bp 與貸款加碼條款是真實壓力（`valuation.ai_credit_schism`），但 HY OAS 2.71%、repo 資金壓力（SOFR−IORB）0bp 顯示信用與資金市場尚未傳導，不足以推翻基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,722.30（2026-08-07），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 3.06%（`valuation.ndx_drawdown`）。R1 門檻水位 22,995.45；自最新收盤需再下跌約 22.63% 才觸及。7 月底曾回落至 27,192.31（2026-07-29）後迅速收復。估值面偏高：S&P 500 trailing P/E ≈29.7、Shiller CAPE ≈42.2（2026-08-07，`valuation.sp500_pe_cape`），S&P 500 高於 200 日均線 10.04%、高於 52 週均線 11.63%（2026-08-07，`valuation.sp500_trend`），代表脆弱度高、回檔幅度一旦啟動可能很大。但同期 VIX 14.9（2026-08-07）且 trailing 7 日 VIX −6.82%、S&P 500 +3.58%，未出現同漲的 crowded-optionality 讀數（`structural.vix_spx_comove`）；廣度擴散而非收窄：RSP 等權 YTD +15.6% 領先 SPY +13.5%（2026-08-07，`breadth.rsp_spy`），約 64% 成分股位於 50DMA 之上（2026-08-03，`breadth.advance_decline`）。

**判讀：** R1 距門檻很遠（需再跌約 22.63%），目前沒有進行中的下跌；窗口內若要觸發，需要 R3 型信用事件或 R2 型 capex 轉向成為催化劑，引發估值從 CAPE ≈42 的高位快速壓縮。

### R2 資本支出收縮

本次取得的來源只提供四家合計：hyperscaler 2026 capex 合計 ≈$725B，Q2 財報季後仍在上修（CNBC，2026-07-28，`ai.hyperscaler_capex`）。Microsoft、Alphabet、Amazon、Meta 各自的最新指引數值，本次來源未逐家列出，個別金額與逐家方向（上修／持平）不在此填補；來源描述合計仍在上修，本次未見任一家下修的披露，目前已確認的下修家數為 0/4。需求側佐證：Microsoft 商用 RPO ≈$678B（2026-07-30，`ai.customer_concentration_rpo`），HBM/DRAM 合約價續升、H200 租金中位 ≈$4.39/hr、供給缺口延至 1H2027（2026-08-01，`ai.compute_supply_demand`），屬於供不應求而非 order digestion。窗口內下一輪財報（約 2026 年 10 月下旬，本次來源未確立確切日期）是 R2 唯一的正式催化點；下一輪之後的 2027 年 1 月底至 2 月初財報部分可能落在窗口末端（2027-02-08）之前。

**判讀：** R2 方向與解析條件相反（仍在上修），需要至少兩家在一至兩次財報內由上修轉為下修；以目前供給缺口延至 1H2027 的證據，這不是窗口內的基本情境。

### R3 AI 信用事件

信用定價出現明顯的局部壓力：CoreWeave 5Y CDS 一度 ≈855bp（已回落），Oracle 5Y CDS ≈215bp，Q2 AI-linked CDS 交易 ≈$650M，投資人要求 AI 貸款加入 covenant（2026-08-03，`valuation.ai_credit_schism`）。CoreWeave 為與 Anthropic 掛鉤的 $2.6B 貸款調高收益率（+100–125bp）並增加 covenant，Nebius 另有 $775M 融資（2026-07-29，`structural.ai_infrastructure_debt`）。CoreWeave 是最可能符合 R3 規模門檻的 AI 算力主業借款人，但其總負債本次來源未確立，無法正式確認 ≥ 50 億美元；本次來源中也沒有任何借款人出現逾寬限期違約、破產申請、distressed exchange 或 going-concern 字樣。寬信用仍很緊：HY OAS 2.71%、IG OAS 0.78%（2026-08-06，`monetary.hy_oas`、`monetary.ig_oas`），repo 資金壓力（SOFR−IORB）0bp、SOFR99−IORB 8bp、SRF 動用（Standing Repo Facility usage）0（`monetary.repo_stress_srf`）。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）本次 30 日窗內無披露。

**判讀：** R3 是三條路徑中最接近的一條——AI 信用定價分歧（equity-vs-credit schism）已呈現信貸端重定價（CDS 走闊、貸款加碼與 covenant），屬後期訊號；但從定價壓力到實際違約／distressed exchange 仍需再融資受阻或關鍵客戶合約失效，本次未見近期到期牆或付款失誤的證據，窗口內完成的可能性仍低於一半。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 一度 ≈855bp、Oracle 5Y CDS ≈215bp，AI 貸款投資人開始要求 covenant，顯示信貸端已對 AI 算力借款人重定價（2026-08-03，`valuation.ai_credit_schism`）。
- [R3] CoreWeave 為 $2.6B Anthropic 掛鉤貸款調高收益率 +100–125bp 並加 covenant，Nebius 新增 $775M 融資，AI infrastructure debt financing / vendor-financing loops 的融資成本上升（2026-07-29，`structural.ai_infrastructure_debt`）。
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收 ≈$72B vs 年化 capex ≈$725B（分母：top-4＋Oracle），缺口約十倍（2026-06-15 組件，`ai.revenue_capex_gap`）；Microsoft RPO ≈$678B 中 ≈32% 繫於 OpenAI，backlog 重複計算風險（RPO double-counting）與單一客戶集中並存（2026-07-30，`ai.customer_concentration_rpo`）。
- [R1] 估值與槓桿處於高位：Shiller CAPE ≈42.2、trailing P/E ≈29.7（2026-08-07，`valuation.sp500_pe_cape`）；FINRA margin debt $1.502T、YoY +51.5%（2026-06 月資料，`retail.margin_debt`）；US 槓桿 ETF 總 AUM 記錄高 ≈$198B（2026-07-23，`structural.leveraged_etf_aum`）——一旦下跌，去槓桿可放大幅度。
- [整體] 美債標售需求（auction tail / bid-to-cover）轉弱：5Y 標售連 14 次 tail、bid-to-cover 為 2022-09 以來最差，7Y tail 0.8bp（2026-07-28，`monetary.treasury_auctions`）；10Y 期限溢價（term premium）0.8681%，trailing 7 日 +3bp（2026-07-31，`monetary.term_premium`），財政供給壓力可能推高折現率。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 3.06%（2026-08-07），R1 門檻 22,995.45 需再跌約 22.63%，且 7 月底的回落已收復（`valuation.ndx_drawdown`）。
- [R2] hyperscaler 2026 capex 合計 ≈$725B、Q2 財報後仍在上修，本次未見任一家下修的披露（2026-07-28，`ai.hyperscaler_capex`）；HBM/DRAM 合約價續升、供給缺口延至 1H2027（2026-08-01，`ai.compute_supply_demand`），需求側仍超過供給。
- [R3] 寬信用與資金市場未傳導：HY OAS 2.71%、IG OAS 0.78%（2026-08-06，`monetary.hy_oas`、`monetary.ig_oas`）；SOFR−IORB 0bp、SRF 動用 0（2026-08-06／2026-08-07，`monetary.repo_stress_srf`）；MOVE 72.03（2026-08-07，`structural.treasury_basis_trade`）。
- [整體] 波動與情緒未達極端：VIX 14.9 且 7 日 VIX −6.82% 對 S&P 500 +3.58%，無同漲訊號（2026-08-07，`structural.vix_spx_comove`）；CNN Fear & Greed ≈64（2026-08-07，`retail.fear_greed`）；AAII Bull 37.0%／Bear 38.0%（2026-08-06，`retail.aaii`）。
- [R1] 市場廣度擴散而非收窄：RSP 等權 YTD +15.6% 領先 SPY +13.5%（2026-08-07，`breadth.rsp_spy`）；Mag 7 對指數溢價處於近十年低位（≈29x vs ≈25.6x，2026-07-20，`valuation.mag7_multiples`），集中度風險未進一步惡化。

## 與前期比較

前次結論：無前次預測（report-2026-08-06 為舊格式評分報告）

- report-2026-08-06 為舊格式評分報告，其評分不轉換為 yes／no；本次結論 `no` 完全由本次證據與基準率得出。
- 與 2026-08-06 相比，NASDAQ-100 由 29,373.33 升至 29,722.30（2026-08-07），S&P 500 +0.62%；DGS10、DFII10、HY OAS、IG OAS、SOFR 均無新觀測（Δ 0），T10YIE −1bp、T5YIFR −1bp、VIX 由 15.15 降至 14.9、MOVE 由 76.12 降至 72.03。
- 10Y 分解：ΔDGS10 0bp、ΔDFII10 0bp、ΔT10YIE −1bp；判讀 `不可判（視窗不一致）`（freshness partial_stale，stale_series：DGS10、DFII10）。
- `flip_evidence` 為 `[]`。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源檢索完成但無合格披露（✗ NOT DISCLOSED，均為 best-effort）：retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.pboc、monetary.private_credit_liquidity、ai.token_growth、ai.openai_anthropic_revenue（最近披露為 2026-06-15，非本季，故不作本 bullet 的當期證據；僅於 ai.revenue_capex_gap 以 carry-forward 組件標註日期使用）、ai.hyperscaler_financing_mix（quarterly_state 可用，event_scan 30 日內無新發債事件）、ai.depreciation_life、ai.capital_cycle、structural.global_leveraged_approvals。其中 monetary.private_credit_liquidity 與 ai.hyperscaler_financing_mix 的 event_scan 缺漏最可能影響 R3：若有未被捕捉的 gate proration / breach 或大型表外融資受阻，R3 會更接近。speculation.insider_form4 搜尋結果僅見第三方彙整頁、缺 SEC EDGAR filing URL，不構成合格件數，記為 0 件；structural.us_single_stock_etf 唯一結果的 GlobeNewswire 發布日為 2026-07-07，超出 30 日窗，僅作背景，記為 0 件。structural.zero_dte 的 ≈65% 數據日為 2026-05-31，較舊，只作背景。

最大的不確定性：

1. CoreWeave 的總負債與近期到期／再融資需求本次未確立——若證實 ≥ 50 億美元且有窗口內到期牆、CDS 再度走闊，R3 會顯著接近，推向 yes。
2. 2026 年 10 月下旬的 hyperscaler 財報——若兩家以上首次下修 capex 指引即直接觸發 R2，推向 yes；若續上修則強化 no。
3. 美債標售需求與 10Y 期限溢價——若 tail 持續擴大推升長端利率，可能成為估值壓縮（R1）的催化劑，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 29.7 | https://www.multpl.com/s-p-500-pe-ratio | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE | 42.2 | https://www.multpl.com/shiller-pe | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E（vs 指數 ≈25.6x） | 29x | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026 | 2026-07-20 | 2026-08-10T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標 $285→$288（EPS-driven） | 288 | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044 | 2026-07-13 | 2026-08-10T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7757.64 | FRED API (series_id=SP500) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 10.04 | FRED API (series_id=SP500) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 11.63 | FRED API (series_id=SP500) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29722.3 | FRED API (series_id=NASDAQ100) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-10T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 3.06 | FRED API (series_id=NASDAQ100) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS（峰值後回落） | 855bp | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm | 2026-08-03 | 2026-08-10T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5Y CDS | 215bp | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm | 2026-08-03 | 2026-08-10T09:30:00+08:00 |
| breadth.rsp_spy | RSP 等權 YTD 總報酬（SPY +13.5%） | +15.6% | https://www.benzinga.com/etfs/sector-etfs/26/08/60862370/rsp-etf-is-beating-voo-spy-as-sp-500-equal-weight-fund-nears-100-billion-milestone | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 | 36.4%（≈37%） | https://www.rbcwealthmanagement.com/en-us/insights/the-great-narrowing-sp-500-concentration | 2026-07-24 | 2026-08-10T09:30:00+08:00 |
| breadth.advance_decline | S&P 500 成分股高於 50DMA 比例 | 64% | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/ | 2026-08-03 | 2026-08-10T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed（Greed） | 64 | https://www.cnn.com/markets/fear-and-greed | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-06 月資料，YoY +51.5%） | 1.502（$1.502T） | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-10T09:30:00+08:00 |
| retail.aaii | AAII Bull（Neutral 25.0%／Bear 38.0%） | 37.0% | https://www.aaii.com/sentimentsurvey | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1，家庭股票佔金融資產 %） | 45.76080873390133（≈45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-10T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標上限） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-09 | 2026-08-10T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標下限） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-09 | 2026-08-10T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 2.71 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（IG OAS %） | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（10Y 殖利率 %） | 4.69 | FRED API (series_id=DGS10) | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（10Y 實質殖利率 %） | 2.43 | FRED API (series_id=DFII10) | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（10Y breakeven %） | 2.25 | FRED API (series_id=T10YIE) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（WTI 美元／桶） | 81.96 | FRED API (series_id=DCOILWTICO) | 2026-08-03 | 2026-08-10T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料，CPI YoY %） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-08-10T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（5y5y forward %） | 2.28 | FRED API (series_id=T5YIFR) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright 10Y 期限溢價 %） | 0.8681 | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-10T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 日） | 3.0 | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-10T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.65 | FRED API (series_id=SOFR) | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.73 | FRED API (series_id=SOFR99) | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-10 | 2026-08-10T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（Fed 隔夜 repo 操作 transaction volume，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| monetary.treasury_auctions | 7Y 標售 tail | 0.8bp | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026 | 2026-07-28 | 2026-08-10T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 9/16 一次動作隱含機率（方向分歧） | 62% | https://growbeansprout.com/tools/fedwatch | 2026-08-10 | 2026-08-10T09:30:00+08:00 |
| monetary.walcl | WALCL latest（Fed 資產負債表） | 6748567.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-05 | 2026-08-10T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（ECB 資產負債表） | 5941248.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-31 | 2026-08-10T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（BOJ 資產負債表） | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-10T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計（Q2 財報後仍上修） | 725（≈$725B） | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-07-28 | 2026-08-10T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft 商用 RPO（≈32% 繫於 OpenAI） | 678（$678B） | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/ | 2026-07-30 | 2026-08-10T09:30:00+08:00 |
| ai.compute_supply_demand | H200 租金中位（HBM 缺口延至 1H2027） | 4.39（$/hr） | https://jarvislabs.ai/blog/h200-price | 2026-08-01 | 2026-08-10T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收（vs 年化 capex ≈$725B，分母：top-4＋Oracle） | 72（≈$72B） | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-06-15 | 2026-08-10T09:30:00+08:00 |
| speculation.ipo_heat | APMD 首日漲幅（JMKE 募資 $1B） | +56% | https://seekingalpha.com/article/4710009-us-ipo-weekly-recap-august-kicks-off-with-one-small-pricing | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI IPO 目標估值 | 1（≈$1T） | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground | 2026-07-28 | 2026-08-10T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity-only put/call（daily） | 0.55 | https://ycharts.com/indicators/cboe_equity_put_call_ratio | 2026-08-03 | 2026-08-10T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM（記錄高） | 198（≈$198B） | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-07-23 | 2026-08-10T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量（Cboe Q2） | 65% | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641 | 2026-05-31 | 2026-08-10T09:30:00+08:00 |
| structural.options_volume | OCC 總量（2026-06 月資料） | 1,603,491,559 口 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report | 2026-07-02 | 2026-08-10T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW（VIX ≈16，contango） | 140 | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 14.9 | FRED API (series_id=VIXCLS) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（共同時間軸，comove=false） | 14.9 | scripts/fetch_macro.py vix_spx_comove（FRED SP500 共同時間軸） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（base 2026-07-31，7 日） | -6.82 | scripts/fetch_macro.py vix_spx_comove（FRED SP500 共同時間軸） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（base 2026-07-31，7 日） | 3.58 | scripts/fetch_macro.py vix_spx_comove（FRED SP500 共同時間軸） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt 交叉引用（2026-06 月資料，YoY +51.5%） | 1.502（$1.502T） | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-10T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave Anthropic 掛鉤貸款（調高收益率 +100–125bp，加 covenant；Nebius $775M） | 2.6（$2.6B） | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic | 2026-07-29 | 2026-08-10T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（銀行對 NBFI 放款，十億美元） | 2002.4852（$2.00T） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-29 | 2026-08-10T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7423067 | CFTC TFF futures-only（cftc_lev_funds） | 2026-08-04 | 2026-08-10T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 149977 | CFTC TFF futures-only（cftc_lev_funds） | 2026-08-04 | 2026-08-10T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（^MOVE） | 72.03 | Yahoo Finance chart API（move_index，unofficial） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2309.0 | OFR STFM REPO-TRIV1_TV_TOT-P（ofr_repo） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | SSGA／advisorperspectives WebSearch | ✓ SEARCH-VERIFIED（AI leader P/S vs 10 年均值未取得） |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方 TP 調升 WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | financecharts／benzinga WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | RBC／財經媒體 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | StockCharts breadth WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA／Advisor Perspectives WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py FRED BOGZ1FL153064486Q | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／YCharts [primary: SEARCH] | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py FRED API | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py FRED BAMLH0A0HYM2 | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py FRED BAMLC0A0CM | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py FRED DGS10 | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py FRED DFII10 | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py FRED T10YIE（FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py FRED DCOILWTICO | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py FRED CPIAUCSL yoy_pct | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py FRED T5YIFR | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py FRED THREEFYTP10（Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py FRED API＋repo_stress block | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | Reuters／Bloomberg recap WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py FRED WALCL | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py FRED ECBASSETSW＋JPNASSETS | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | investing／Yicai WebSearch | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／報導 WebSearch（需本季披露；最近為 2026-06-15） | ✗ NOT DISCLOSED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce／jarvislabs [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：季報／Sage Advisory WebSearch；event_scan：30 日發債掃描，無新事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 WebSearch（carry-forward 組件） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K／10-Q WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速＋進出場事件 WebSearch；兩組件皆無可引證披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | Reuters／Benzinga／IPOX SPAC 螢幕 WebSearch | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | Renaissance／SeekingAlpha WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／StockAnalysis／StockTitan gainers 螢幕 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | S-1／具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 篩選（14d；第三方頁缺 EDGAR URL 者不計） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe／YCharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com／cryptobriefing [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com／GlobeNewswire（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC monthly | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe／Saxo WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py FRED VIXCLS＋vix_spx_comove block | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 retail.margin_debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | Bloomberg 等 [primary: SEARCH]（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py FRED LNFACBW027SBOG | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds／move_index／ofr_repo（WebSearch 無新增披露） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E ≈29.7（原定來源 multpl／gurufocus） | S&P 500 trailing P/E CAPE August 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio（multpl） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE ≈42.2 | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 ≈29x vs 指數 ≈25.6x，溢價近十年低（原定來源 SSGA／advisorperspectives） | Magnificent 7 valuation premium lowest decade 2026 | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026（SSGA） | 2026-07-20 | 2026-08-10T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標 $285→$288，EPS revision 主導（Q3 同季） | Morgan Stanley NVDA target 288 July 2026 AI demand | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044（Investing.com） | 2026-07-13 | 2026-08-10T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS ≈855bp（回落）、Oracle CDS ≈215bp、Q2 AI-linked CDS ≈$650M | CoreWeave CDS Oracle spread AI credit August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm（Tech Times） | 2026-08-03 | 2026-08-10T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD +15.6% vs SPY +13.5%（原定來源 financecharts） | RSP vs SPY equal weight YTD August 2026 concentration | https://www.benzinga.com/etfs/sector-etfs/26/08/60862370/rsp-etf-is-beating-voo-spy-as-sp-500-equal-weight-fund-nears-100-billion-milestone（Benzinga） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| breadth.top10_concentration | Top-10 集中度 ≈37%（36.4%） | S&P 500 top 10 concentration percent August 2026 | https://www.rbcwealthmanagement.com/en-us/insights/the-great-narrowing-sp-500-concentration（RBC Wealth Management） | 2026-07-24 | 2026-08-10T09:30:00+08:00 |
| breadth.advance_decline | ≈64% 成分股在 50DMA 上、A/D 創高、McClellan 動能轉緩 | S&P 500 breadth percent above 50 day moving average August 2026 | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/（StockCharts） | 2026-08-03 | 2026-08-10T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed ≈64（Greed） | CNN Fear and Greed Index August 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives，原定來源 FINRA） | 2026-07-20 | 2026-08-10T09:30:00+08:00 |
| retail.aaii | AAII Bull 37.0%／Neutral 25.0%／Bear 38.0% | AAII investor sentiment survey week August 6 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.treasury_auctions | 5Y 連 14 次 tail、BTC 2022-09 以來最差；7Y tail 0.8bp | US Treasury 5 year 7 year auction tail bid to cover July 2026 | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026（TFTC，原定來源 Reuters／Bloomberg recap） | 2026-07-28 | 2026-08-10T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 9/16 一次動作 ≈62%、方向分歧 | CME FedWatch September 2026 probability Fed | https://growbeansprout.com/tools/fedwatch（Beansprout，原定來源 CME FedWatch） | 2026-08-10 | 2026-08-10T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計 ≈$725B、Q2 後仍上修 | hyperscaler capex 2026 725B raised Q2 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-08-10T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO ≈$678B、≈32% 繫於 OpenAI | Microsoft RPO backlog 678 billion OpenAI 2026 | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/（TradingView／Benzinga） | 2026-07-30 | 2026-08-10T09:30:00+08:00 |
| ai.compute_supply_demand | HBM/DRAM 合約續升、H200 租金 ≈$4.39/hr、缺口延至 1H2027 | H200 GPU rental HBM DRAM 2026 shortage 2027 | https://jarvislabs.ai/blog/h200-price（Jarvislabs） | 2026-08-01 | 2026-08-10T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 超越 FCF、2026 發債規模 ≈$182B、表外 SPV >$120B（背景，carried 季頻狀態） | hyperscaler capex FCF debt issuance 182 billion off balance sheet SPV 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure（Sage Advisory） | 2026-07-24 | 2026-08-10T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 ≈$72B（Anthropic ≈$47B＋OpenAI ≈$25B，2026-06-15 組件）vs 年化 capex ≈$725B（分母：top-4＋Oracle） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-06-15 | 2026-08-10T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收投機 IPO 合格件數 0（2026-08-03 至 2026-08-10） | AI rename ticker SPAC no revenue IPO August 3-10 2026 | 檢查來源：Reuters、Benzinga、IPOX SPAC 螢幕 | — | 2026-08-10T09:30:00+08:00 |
| speculation.ipo_heat | APMD 首日 +56%、JMKE $1B 收平、IOND $3.1B 直接上市 | US IPO pricings week August 2026 Renaissance Apnimed | https://seekingalpha.com/article/4710009-us-ipo-weekly-recap-august-kicks-off-with-one-small-pricing（Seeking Alpha，原定來源 Renaissance） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot 合格 0 件 | microcap 100% single day quantum fusion nuclear space AI August 2026 | 檢查來源：Finviz、StockAnalysis、StockTitan gainers 螢幕 | — | 2026-08-10T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 ≈$1T IPO、Anthropic 續進 IPO 程序（具名報導） | OpenAI Anthropic IPO timing 1 trillion 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground（Benzinga） | 2026-07-28 | 2026-08-10T09:30:00+08:00 |
| speculation.insider_form4 | 合格 Form 4 cluster 0 件（搜尋僅得第三方彙整頁，無 SEC EDGAR filing URL，不計入） | Snowflake Tempus AI Form 4 insider sale July August 2026 SEC | 檢查來源：SEC EDGAR、StockTitan Form 4 彙整頁 | — | 2026-08-10T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.55（daily） | Cboe equity put call ratio August 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio（YCharts） | 2026-08-03 | 2026-08-10T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 記錄高 ≈$198B（原定來源 etf.com） | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing） | 2026-07-23 | 2026-08-10T09:30:00+08:00 |
| structural.us_single_stock_etf | 30 日窗內合格單股槓桿 ETF 核准／發行 0 件（唯一結果發布日 2026-07-07，窗外） | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | 檢查來源：SEC EDGAR、ETF.com、GlobeNewswire | — | 2026-08-10T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量 ≈65%（Cboe Q2 2026） | 0DTE SPX options share Cboe Q2 2026 65% | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641（Investing.com，原定來源 Cboe） | 2026-05-31 | 2026-08-10T09:30:00+08:00 |
| structural.options_volume | OCC 6 月總量 16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-08-10T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW ≈140、VIX ≈16 contango、債市波動偏高 | VIX SKEW bond volatility MOVE August 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher（Cboe） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt $1.502T、+51.5% YoY（交叉引用 retail.margin_debt） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives） | 2026-07-20 | 2026-08-10T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B Anthropic 掛鉤貸款調高票息＋covenant；Nebius $775M | CoreWeave 2.6 billion loan Anthropic covenant July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic（Bloomberg） | 2026-07-29 | 2026-08-10T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-10",
  "iso_week": "2026-W33",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-08",
  "prior_date": "2026-08-06",
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 3.06,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

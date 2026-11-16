> [DRY RUN] this report was not committed to archive.

# 2026-08-13 AI 泡沫破裂預測報告
報告日期：2026-08-13｜ISO 週次：2026-W33｜預測窗口：2026-08-13 → 2027-02-11｜前次基準：report-2026-08-10（3天前）

## 結論

**結論：no**

三條路徑都沒有進入完成段：NASDAQ-100 距 52 週高點僅回撤 2.99%（R1 門檻需再跌 22.69%），四家 hyperscaler 在 2026 Q2 財報仍上修 capex、尚無一家下修（R2）。AI 信用端已出現 CoreWeave 貸款利差走闊與 Oracle CDS 7 年高的早期重定價（R3 的領先訊號），但整體 HY OAS 2.72%、repo 資金壓力與 SRF 動用皆平靜，尚不足以推翻 182 天窗口內三條件都不發生的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

FRED NASDAQ100 最新收盤 29,742.6（2026-08-12），252 交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 2.99%；R1 門檻水位 22,995.45，自最新收盤還需再跌約 22.69% 才觸及（`valuation.ndx_drawdown`）。估值與槓桿顯示脆弱度高：S&P 500 trailing P/E ≈29.85、Shiller CAPE ≈42.34（`valuation.sp500_pe_cape`，2026-08-12）；S&P 500 7,748.5 高於 200 日均線 9.67%、高於 52 週均線 11.23%（`valuation.sp500_trend`，2026-08-12）；FINRA 6 月 margin debt $1.502T、YoY +51.5%，落在歷史頂部附近常見的 +40–50% 以上區間（`retail.margin_debt`）。但觸發與傳導面偏弱：VIX 15.28（2026-08-11），vix_spx_comove 窗口 2026-08-04 → 2026-08-11（7 日）內 VIX −7.39%、S&P 500 −0.11%，未出現 crowded-optionality 同漲讀數（`structural.vix_spx_comove`）；CNN Fear & Greed ≈61（Greed，`retail.fear_greed`）、AAII Bull 37.0%／Bear 38.0%（`retail.aaii`），情緒並非極端亢奮。政策緩衝有限：CPI YoY 3.3%（2026-07 月資料，`monetary.cpi_yoy`）、Fed funds 目標區間 3.50%–3.75%（`monetary.fed_funds`），CME FedWatch 顯示 9/16 會議 ≈45% 升息、無降息定價（`monetary.fedwatch`），一旦下跌，Fed 不易快速降息托底。10Y 殖利率 4.70%（2026-08-11），ΔDGS10 −2.0bp、ΔDFII10 0.0bp、ΔT10YIE −3.0bp（T10YIE 最新觀測為 2026-08-12，視窗與另兩腿不同），判讀：不可判（視窗不一致）（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。

**判讀：** R1 距離完成很遠（需再跌約 22.69%）。要在窗口內觸發，需要一個傳導型催化劑——例如 R3 信用重定價擴散、Q3 財報季 capex 指引轉向，或 9 月升息疊加高 margin debt 的被迫去槓桿；目前這些都只是可能性，尚無已啟動的證據。

### R2 資本支出收縮

本次證據只有四家 hyperscaler 的合計值：2026 年 capex 合計 ≈$725B，且在 2026 Q2 財報（2026-07 下旬）仍為上修（`ai.hyperscaler_capex`，CNBC 2026-07-28）。逐家（Microsoft、Alphabet、Amazon、Meta）的最新官方指引數字與逐家方向不在本次證據中，故不逐家列數；依合計報導，四家相較前次指引的方向為上修，目前下修家數為 0／4。同一報導指出市場已開始質疑 capex（Alphabet 財報後股價遭拋售），且 top-5 capex 已超過 FCF、Alphabet Q2 FCF 轉負、2026 發債 ≈$182B（`ai.hyperscaler_financing_mix`）——這是 hyperscaler 融資結構（capex vs FCF / 發債）從現金流轉向舉債的訊號，會提高未來下修指引的誘因，但尚未成為下修本身。需求側仍緊：Blackwell 售罄、HBM 合約價 ≈+40%、H200 租金中位 ≈$3.99/hr（`ai.compute_supply_demand`，2026-08-01），與 capex 下修所需的「需求轉弱」相反。下一次財報（2026 Q3）將落在窗口內，具體日期不在本次證據中。

**判讀：** R2 尚未起步（0／4 下修，且最新方向仍是上修）。窗口內可能的觸發點是 2026 Q3 與 Q4 兩次財報；要成立需兩家同時把當年度或次年度指引下修，通常要先看到 R1 型股價懲罰持續或融資成本明顯上升，目前證據不支持在窗口內完成。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）出現早期重定價：CoreWeave 為完成 $2.6B 貸款被迫將利差調高 +100–125bp 並接受 covenant，Oracle 5Y CDS ≈75bp 為 7 年高，Fitch／Moody's 已發出預警（`valuation.ai_credit_schism`，2026-08-03；`structural.ai_infrastructure_debt`，2026-07-29）。這是「信貸端開始走闊而股價未跟上」的後期型讀數。但 R3 需要的是破產申請、超過寬限期的付款違約或 distressed exchange：本次證據沒有任何借款人出現漏付、covenant waiver、distressed exchange 或 going-concern 字樣；CoreWeave 仍能以較高利差完成新貸款，代表再融資管道仍開放。CoreWeave 的總負債規模、到期牆與評等動作不在本次證據中，無法在此確認其是否達到 ≥ 50 億美元門檻。hyperscaler 端的表外結構持續擴大：Meta El Paso 資料中心由 BlackRock 主導 >$12B 債券（20-30yr triple-net lease，表外結構，`ai.hyperscaler_financing_mix`，2026-07-20），風險轉移到 SPV／投資人端，但借款人背後有 hyperscaler 租約支撐。整體信用環境仍緊：HY OAS 2.72%、IG OAS 0.79%（2026-08-11，`monetary.hy_oas`、`monetary.ig_oas`）。

**判讀：** R3 已從「無訊號」進入「定價開始重估」，是三條路徑中最接近移動的一條，但距違約／distressed exchange 仍有多步距離。窗口內要成立，需要 neocloud 端再融資失敗（利差進一步跳升、無法續作設施）或主要客戶承諾撤回；目前融資仍可取得，判斷不會在 182 天內完成。

## 支持 yes 的證據

- [R3] CoreWeave $2.6B 貸款被迫調高利差 +100–125bp 並加 covenant，Oracle 5Y CDS ≈75bp 為 7 年高，Fitch／Moody's 預警——AI 信用端開始重定價而股價仍近高點（`valuation.ai_credit_schism` 2026-08-03；`structural.ai_infrastructure_debt` 2026-07-29）。
- [整體] hyperscaler 融資結構（capex vs FCF / 發債）轉向舉債：top-5 capex 已超過 FCF、Alphabet Q2 FCF 轉負、2026 發債 ≈$182B，另有 Meta El Paso >$12B 表外債券結構（`ai.hyperscaler_financing_mix` 2026-07-24／2026-07-20）。
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）仍大：年化 AI 終端營收 ≈$72B vs 年化 capex ≈$725B（分母：top-4＋Oracle，`ai.revenue_capex_gap` 2026-06-15）；Microsoft 商用 RPO ≈$678B 中 ≈32% 繫於 OpenAI 單一客戶（`ai.customer_concentration_rpo` 2026-07-30）。
- [R1] 槓桿與估值脆弱度高：FINRA 6 月 margin debt $1.502T、YoY +51.5%（`retail.margin_debt`），Shiller CAPE ≈42.34（`valuation.sp500_pe_cape` 2026-08-12），US 槓桿 ETF AUM 記錄高 ≈$198B（`structural.leveraged_etf_aum` 2026-07-23），0DTE 佔 SPX 期權量 ≈65%（`structural.zero_dte` 2026-07-31）。
- [R1] 政策緩衝有限：CPI YoY 3.3%（2026-07 月資料，`monetary.cpi_yoy`），CME FedWatch 9/16 ≈45% 升息、無降息定價（`monetary.fedwatch` 2026-08-12）。

## 支持 no 的證據

- [R1] NASDAQ-100 最新收盤 29,742.6（2026-08-12），距 52 週高點回撤 2.99%，距 R1 門檻 22,995.45 仍需再跌約 22.69%（`valuation.ndx_drawdown`）。
- [R2] 四家 hyperscaler 2026 capex 合計 ≈$725B，在 Q2 財報仍上修，下修家數 0／4（`ai.hyperscaler_capex` 2026-07-28）；算力仍供不應求：Blackwell 售罄、HBM 合約 ≈+40%、H200 租金 ≈$3.99/hr（`ai.compute_supply_demand` 2026-08-01）。
- [R3] 整體信用與資金面平靜：HY OAS 2.72%、IG OAS 0.79%（`monetary.hy_oas`、`monetary.ig_oas` 2026-08-11），repo 資金壓力（SOFR−IORB）−1.0bp、SOFR99−IORB 8.0bp、SRF 動用 0.0（`monetary.repo_stress_srf` 2026-08-11／2026-08-12）；CoreWeave 仍能完成新貸款，再融資管道未關閉（`structural.ai_infrastructure_debt` 2026-07-29）。
- [整體] 美債市場未見失序：MOVE 72.09（2026-08-12）、CFTC 槓桿基金美債期貨淨部位 −7,423,067 口且 4 週變動 +149,977（2026-08-04）、OFR tri-party repo transaction volume $2,385.3bn（`structural.treasury_basis_trade`）；3Y 標售 bid-to-cover 2.71、10Y 2.58 需求略高於均值（`monetary.treasury_auctions` 2026-08-12）。
- [整體] 情緒偏熱但未極端：CNN Fear & Greed ≈61（`retail.fear_greed` 2026-08-12），AAII Bull 37.0%／Bear 38.0%（`retail.aaii` 2026-08-06），VIX／S&P 500 未同漲（`structural.vix_spx_comove` 2026-08-11）。

## 與前期比較

前次結論：無前次預測（report-2026-08-10 為舊格式評分報告）

report-2026-08-10 為舊格式評分報告，不轉換為 yes/no，本次為新格式下的首次預測，flip_evidence 為 []。與 2026-08-10 的 macro 比較：10Y 殖利率 −2.0bp、HY OAS +2.0bp、5y5y −5.0bp、S&P 500 −0.06%、MOVE 由 75.46 降至 72.09，均屬窗口內雜訊，不影響路徑判讀。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED（檢索完成但無合格當期披露，皆為 best-effort 來源）：valuation.analyst_tp_decomposition（唯一同季結果為 Susquehanna TSMC $575→$600，2026-07-16，不在指定的 top-tier 賣方清單內，且未披露 EPS Δ 與 target PE Δ，無法分解）、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.pboc、monetary.private_credit_liquidity、ai.token_growth、ai.openai_anthropic_revenue（最新 run-rate 報導日期 2026-05-29，屬上一季，非當季披露；且來源標題寫 $30B run-rate、摘要值為 ≈$47B，數字不一致）、ai.depreciation_life、ai.capital_cycle（quarterly_state 與 event_scan 皆無可引證披露，增速證據不足，本次不判定週期階段）、structural.global_leveraged_approvals。其中 monetary.private_credit_liquidity 與 ai.capital_cycle 的 event_scan 若有未被捕捉的贖回或租約取消事件，會偏向 yes，但這是對 R3／R2 先行指標的缺口，不足以單獨改變結論。

零結果篩查（✓ SEARCH-VERIFIED（0 件））：speculation.ai_rename_spac、speculation.microcap_moonshots、speculation.insider_form4、structural.us_single_stock_etf 本次均為 0 件合格事件——過去 7 日無 AI 改名／SPAC、無合格 microcap moonshot，過去 14 日無合格 Form 4 cluster，過去 30 日無 US single-stock 槓桿 ETF 核准／上市。這些只代表篩查未命中，不作為支持任一方向的正向證據。evidence 檔未記錄這四項篩查的逐字 search query，traceability 表中的 query 欄以篩查定義描述。

其他資料限制：breadth.rsp_spy 的 RSP vs SPY 數值資料日為 2026-06-10，已舊兩個月，僅作背景；breadth.advance_decline 只取得 >50DMA 比例（≈71.6%），未取得 A/D 與新高／新低比；valuation.mag7_multiples 未取得 AI leader P/S vs 10 年均值；ai.hyperscaler_capex 只有四家合計值，缺逐家指引數字。

最大不確定性：

1. 2026 Q3 財報季（落在窗口內，具體日期不在本次證據中）：若兩家以上 hyperscaler 因 FCF 轉負與發債成本把指引下修，R2 直接成立並可能帶動 R1，會把答案推向 yes。
2. CoreWeave 等 neocloud 的再融資軌跡：利差再跳升或設施無法續作會讓 R3 加速；其總負債與到期牆本次未取得，是 R3 判讀的主要盲點，會推向 yes。
3. 9/16 FOMC：≈45% 升息定價若兌現，疊加 margin debt YoY +51.5% 的槓桿水位，可能觸發去槓桿式回撤（推向 yes）；若不升息且通膨回落，則強化 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 29.85 | https://www.multpl.com/s-p-500-pe-ratio | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE | 42.34 | https://www.multpl.com/shiller-pe | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E vs 指數（佔市值 ≈33.9%） | ≈29x vs ≈25.6x | https://www.fool.com/research/magnificent-seven-sp-500/ | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7748.5 | FRED API (series_id=SP500) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 9.67 | FRED API (series_id=SP500) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 11.23 | FRED API (series_id=SP500) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29742.6 | FRED API (series_id=NASDAQ100) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 2.99 | FRED API (series_id=NASDAQ100) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 貸款利差調高／Oracle 5Y CDS | +100–125bp（Oracle CDS ≈75bp） | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm | 2026-08-03 | 2026-08-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 等權 vs SPY YTD 總報酬（舊資料，背景） | +9.67% vs +8.38% | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ | 2026-06-10 | 2026-08-13T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 | ≈37% | https://www.rbcwealthmanagement.com/en-us/insights/the-great-narrowing-sp-500-concentration | 2026-07-24 | 2026-08-13T09:30:00+08:00 |
| breadth.advance_decline | S&P 500 成分股 >50DMA 比例 | ≈71.6% | https://www.investing.com/indices/s-p-500-stocks-above-50-day-average | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed | ≈61（Greed） | https://www.cnn.com/markets/fear-and-greed | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-06 月資料）／YoY | $1.502T／+51.5% | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-13T09:30:00+08:00 |
| retail.aaii | AAII Bull／Neutral／Bear（週結束 2026-08-05） | 37.0%／25.0%／38.0% | https://seekingalpha.com/article/4932187-aaii-sentiment-survey-optimism-jumps | 2026-08-06 | 2026-08-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q1，家戶股票配置 %） | 45.76080873390133（≈45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.72 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 2.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.79 | FRED API (series_id=BAMLC0A0CM) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.7 | FRED API (series_id=DGS10) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | -2.0 | FRED API (series_id=DGS10) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.43 | FRED API (series_id=DFII10) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | 0.0 | FRED API (series_id=DFII10) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.26 | FRED API (series_id=T10YIE) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | -3.0 | FRED API (series_id=T10YIE) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD） | 84.77 | FRED API (series_id=DCOILWTICO) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.28 | FRED API (series_id=T5YIFR) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR delta_bps | -5.0 | FRED API (series_id=T5YIFR) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 0.8257 | FRED API (series_id=THREEFYTP10) | 2026-08-07 | 2026-08-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7d） | -4.2 | FRED API (series_id=THREEFYTP10) | 2026-08-07 | 2026-08-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.64 | FRED API (series_id=SOFR) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.73 | FRED API (series_id=SOFR99) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-13 | 2026-08-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.treasury_auctions | 3Y／10Y 標售 bid-to-cover（3Y 2026-08-11 tail −0.5bp；10Y 2026-08-12） | 3Y 2.71／10Y 2.58 | https://www.rttnews.com/3679611/ten-year-note-auction-attracts-modestly-above-average-demand.aspx | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 9/16 升息定價 | ≈45%（無降息定價） | https://cryptobriefing.com/traders-45-percent-chance-september-fed-rate-hike/ | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,748,567（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-05 | 2026-08-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,923,023（€5.92T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-07 | 2026-08-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,442,957（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-13T09:30:00+08:00 |
| ai.hyperscaler_capex | MSFT＋GOOGL＋AMZN＋META 2026 capex 合計（Q2 財報後，仍上修） | ≈$725B | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-07-28 | 2026-08-13T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft 商用 RPO／單一客戶（OpenAI）佔比 | $678B／≈32% | https://www.benzinga.com/trading-ideas/long-ideas/26/07/60816147/microsofts-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer | 2026-07-30 | 2026-08-13T09:30:00+08:00 |
| ai.compute_supply_demand | H200 租金中位／HBM 合約價變動 | ≈$3.99/hr／≈+40% | https://jarvislabs.ai/blog/h200-price | 2026-08-01 | 2026-08-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 超越 FCF（Alphabet Q2 FCF 轉負）、2026 發債 | ≈$182B | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure | 2026-07-24 | 2026-08-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan][spv_deal] Meta El Paso 資料中心 BlackRock 主導債券（triple-net lease、表外結構） sponsor_equity_split=undisclosed;residual_value_guarantee=undisclosed;lease_term=20-30yr;debt_tenor=undisclosed;lead_lenders=BlackRock/JPMorgan/MS; | >$12B | https://www.landgate.com/news/blackrock-s-12-billion-bond-sale-signals-a-new-financing-playbook-for-data-center-developers | 2026-07-20 | 2026-08-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 vs 年化 capex（分母：top-4＋Oracle） | ≈$72B vs ≈$725B | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-06-15 | 2026-08-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價（2026-08-12／2026-08-13 各日）／平均首日報酬 | ≈12 檔/日（首日 ≈18%） | https://www.iposcoop.com/current-year-pricings/ | 2026-08-13 | 2026-08-13T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 9 月上市估值 | ≈$730–850B | https://cryptobriefing.com/openai-ipo-filing-trillion-valuation/ | 2026-07-28 | 2026-08-13T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity-only put/call（daily） | 0.54 | https://www.thetrading.tools/put-call-ratio | 2026-08-07 | 2026-08-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM（記錄高） | ≈$198B | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-07-23 | 2026-08-13T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量（Cboe Q2 2026） | ≈65% | https://ca.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4768656 | 2026-07-31 | 2026-08-13T09:30:00+08:00 |
| structural.options_volume | OCC 總量（2026-06 月資料） | 1,603,491,559 口（≈16.0 億口） | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report | 2026-07-02 | 2026-08-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW／VIX／MOVE（Cboe 週評） | 135.59／15.28／74.67 | https://www.cboe.com/insights/posts/week-of-8-10-2026-spx-skew-collapses-on-upside-chasing | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.28 | FRED API (series_id=VIXCLS) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（窗口 2026-08-04 → 2026-08-11） | 15.28 | FRED API (VIXCLS／SP500 共同時間軸，block vix_spx_comove) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | -7.39 | FRED API (block vix_spx_comove) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -0.11 | FRED API (block vix_spx_comove) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt（2026-06 月資料）／YoY（交叉確認，不重複計入） | $1.502T／+51.5% | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B 貸款設施：利差調高＋covenant | +100–125bp | https://www.stocktitan.net/news/CRWV/core-weave-closes-2-6-billion-loan-facility-expanding-financing-gwhngwnf0jt5.html | 2026-07-29 | 2026-08-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2002.4852（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-29 | 2026-08-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六個 CBT 美債期貨合計，口） | -7423067 | CFTC TFF (block cftc_lev_funds) | 2026-08-04 | 2026-08-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 149977 | CFTC TFF (block cftc_lev_funds) | 2026-08-04 | 2026-08-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 72.09 | Yahoo Finance chart API (^MOVE, block move_index) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2385.3 | OFR STFM (REPO-TRIV1_TV_TOT-P, block ofr_repo) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation｜S&P 500 P/E and Shiller CAPE | multpl.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation｜Mag 7 weighted P/E and AI leader P/S vs 10-year averages | Motley Fool research WebSearch（AI leader P/S vs 10 年均值未取得） | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation｜Analyst TP upgrade decomposition | 賣方 TP 調升 WebSearch [primary: SEARCH]，90d＋同季 | ✗ NOT DISCLOSED（唯一同季結果 Susquehanna 不在 top-tier 清單且無 EPS／PE 分解） |
| valuation.sp500_trend | Valuation｜S&P 500 price-trend deviation | scripts/fetch_macro.py：FRED SP500 → sp500_trend block | ✓ API |
| valuation.ndx_drawdown | Valuation｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py：FRED NASDAQ100 → ndx_drawdown block | ✓ API |
| valuation.ai_credit_schism | Valuation｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導 WebSearch [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) YTD divergence | 24/7 Wall St WebSearch（資料日 2026-06-10，舊） | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth｜Top-10 concentration in S&P 500 | RBC Wealth Management WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth｜Advance/decline ratio, new high/low ratio | Investing.com breadth WebSearch（僅 >50DMA 比例） | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment｜CNN Fear & Greed Index | cnn.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment｜Margin Debt: FINRA monthly data | FINRA 6 月資料 via Advisor Perspectives WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment｜Retail survey: AAII Investor Sentiment | aaii.com 週調查 WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment｜Social sentiment proxies | WSB／cashtag WebSearch，7d | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment｜Household equity allocation | scripts/fetch_macro.py：FRED BOGZ1FL153064486Q | ✓ API |
| retail.naaim | Retail Sentiment｜NAAIM Exposure Index | naaim.org／YCharts WebSearch [primary: SEARCH] | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment｜BofA Fund Manager Survey and JPM institutional survey | 月度調查 WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py：FRED DFEDTARU＋DFEDTARL | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit｜High Yield OAS | scripts/fetch_macro.py：FRED BAMLH0A0HYM2 | ✓ API |
| monetary.ig_oas | Monetary & Credit｜Investment Grade OAS | scripts/fetch_macro.py：FRED BAMLC0A0CM | ✓ API |
| monetary.dgs10 | Monetary & Credit｜10Y Treasury yield | scripts/fetch_macro.py：FRED DGS10 | ✓ API |
| monetary.dfii10 | Monetary & Credit｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py：FRED DFII10 | ✓ API |
| monetary.t10yie | Monetary & Credit｜10Y breakeven inflation rate | scripts/fetch_macro.py：FRED T10YIE（FRED 直取，非 derived） | ✓ API |
| monetary.wti | Monetary & Credit｜WTI crude oil price | scripts/fetch_macro.py：FRED DCOILWTICO | ✓ API |
| monetary.cpi_yoy | Monetary & Credit｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py：FRED CPIAUCSL yoy_pct | ✓ API |
| monetary.t5yifr | Monetary & Credit｜5y5y forward inflation expectation | scripts/fetch_macro.py：FRED T5YIFR | ✓ API |
| monetary.term_premium | Monetary & Credit｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py：FRED THREEFYTP10（Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py：FRED SOFR／SOFR99／IORB／RPONTTLD → repo_stress block | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok；repo_stress status ok） |
| monetary.treasury_auctions | Monetary & Credit｜美債標售需求（auction tail / bid-to-cover） | RTTNews／Reuters auction recap WebSearch [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit｜Fed funds rate path expectations | CME FedWatch 摘要 WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py：FRED WALCL | ✓ API |
| monetary.ecb_boj | Monetary & Credit｜Global central bank liquidity cross-check — ECB / BOJ balance sheets | scripts/fetch_macro.py：FRED ECBASSETSW＋JPNASSETS | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit｜PBoC aggregate financing / liquidity operations | investing／Yicai WebSearch | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | Monetary & Credit｜Private-credit / non-bank fund liquidity stress | BDC／interval fund 披露 WebSearch [primary: SEARCH]，30d | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals｜Hyperscaler capex guidance | Q2 2026 財報報導 WebSearch（stock-of-state；僅合計值） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals｜OpenAI / Anthropic annualized revenue | VentureBeat／媒體 WebSearch（最新 2026-05-29，非當季） | ✗ NOT DISCLOSED |
| ai.customer_concentration_rpo | AI Fundamentals｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話會報導 WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals｜AI compute supply/demand and overcapacity risk | jarvislabs／TrendForce WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：Sage Advisory 季頻彙整；event_scan：30d 發債／SPV 掃描（Landgate） | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI Fundamentals｜AI 營收對 capex 缺口（revenue-to-capex gap） | Epoch AI 組合披露 WebSearch（carry-forward stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q／法說會 WebSearch [primary: SEARCH]，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals｜資本週期階段（capital cycle stage） | quarterly_state：供需增速披露；event_scan：30d 進出場／取消事件 WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior｜Search for past 7 days: AI rename / SPAC | WebSearch 篩查，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior｜IPO market heat | IPOScoop WebSearch，7d | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior｜Microcap thematic moonshots | Finviz／StockAnalysis movers 篩查 [primary: SEARCH]，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior｜Upcoming AI IPOs | 具名報導 WebSearch，30d | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 篩查 [primary: SEC EDGAR]，14d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior｜Cboe equity-only put/call ratio | thetrading.tools／Cboe WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage｜US leveraged ETF AUM | cryptobriefing／etf.com WebSearch [primary: SEARCH]（僅總 AUM） | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage｜US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com launches 篩查，30d | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA／ETFGI WebSearch，7d | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage｜0DTE option volume | Cboe Q2 2026 簡報 WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage｜Options total volume: OCC monthly volume report | theocc.com 6 月報告 WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage｜Cross-asset derivatives / correlation checks | Cboe insights WebSearch（stock-bond correlation 未取得） | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage｜VIX / S&P 500 co-movement | scripts/fetch_macro.py：FRED VIXCLS＋vix_spx_comove block | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage｜Cross-reference only: FINRA margin debt | 交叉引用 Retail Sentiment margin debt（Advisor Perspectives） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage｜AI infrastructure debt financing / vendor-financing loops | StockTitan 等 WebSearch [primary: SEARCH]，30d | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py：FRED LNFACBW027SBOG | ✓ API |
| structural.treasury_basis_trade | Structural Leverage｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py：cftc_lev_funds／move_index／ofr_repo；WebSearch 補充無合格事件 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E ≈29.85、CAPE ≈42.34（預定來源 multpl／gurufocus） | S&P 500 trailing P/E CAPE August 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio（multpl） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 ≈29x vs 指數 ≈25.6x、佔市值 ≈33.9%（預定來源 Mag 7 weighted P/E） | Magnificent 7 weighted PE vs S&P 500 August 2026 | https://www.fool.com/research/magnificent-seven-sp-500/（Motley Fool） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 貸款利差 +100–125bp、Oracle CDS ≈75bp（7 年高）、Fitch／Moody's 預警 | CoreWeave Oracle CDS spread AI credit widening August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm（Tech Times） | 2026-08-03 | 2026-08-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 等權 YTD +9.67% vs SPY +8.38%（資料日舊，背景） | RSP vs SPY equal weight YTD total return August 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St） | 2026-06-10 | 2026-08-13T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 ≈37% | S&P 500 top 10 concentration percent 2026 | https://www.rbcwealthmanagement.com/en-us/insights/the-great-narrowing-sp-500-concentration（RBC Wealth Management） | 2026-07-24 | 2026-08-13T09:30:00+08:00 |
| breadth.advance_decline | ≈71.6% S&P 500 成分股在 50DMA 上（A/D 比代理） | S&P 500 percent above 50 day moving average August 2026 | https://www.investing.com/indices/s-p-500-stocks-above-50-day-average（Investing.com） | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed ≈61（Greed） | CNN Fear and Greed Index August 12 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| retail.margin_debt | FINRA 6 月 margin debt $1.502T、YoY +51.5%（預定來源 FINRA） | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives） | 2026-07-20 | 2026-08-13T09:30:00+08:00 |
| retail.aaii | AAII Bull 37.0%／Neutral 25.0%／Bear 38.0%（週結束 2026-08-05） | AAII investor sentiment survey week August 5 2026 | https://seekingalpha.com/article/4932187-aaii-sentiment-survey-optimism-jumps（Seeking Alpha） | 2026-08-06 | 2026-08-13T09:30:00+08:00 |
| monetary.treasury_auctions | 3Y 2026-08-11 BTC 2.71 tail −0.5bp、10Y 2026-08-12 BTC 2.58 需求略高於均值 | US Treasury 3 year 10 year auction bid to cover August 2026 | https://www.rttnews.com/3679611/ten-year-note-auction-attracts-modestly-above-average-demand.aspx（RTTNews） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 9/16 ≈45% 升息、無降息定價 | CME FedWatch September 2026 rate hike probability | https://cryptobriefing.com/traders-45-percent-chance-september-fed-rate-hike/（Crypto Briefing，引 CME FedWatch） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計 ≈$725B、Q2 仍上修（逐家數字未取得） | hyperscaler capex 2026 725 billion raised Q2 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-08-13T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO ≈$678B、≈32% 繫單一客戶（OpenAI） | Microsoft RPO backlog 678 billion OpenAI 2026 | https://www.benzinga.com/trading-ideas/long-ideas/26/07/60816147/microsofts-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer（Benzinga） | 2026-07-30 | 2026-08-13T09:30:00+08:00 |
| ai.compute_supply_demand | HBM 合約 ≈+40%、H200 租金 ≈$3.99/hr、Blackwell 售罄 | H200 GPU rental HBM DRAM 2026 shortage Blackwell | https://jarvislabs.ai/blog/h200-price（Jarvislabs） | 2026-08-01 | 2026-08-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 超越 FCF、2026 發債 ≈$182B | hyperscaler capex FCF debt issuance 182 billion 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure（Sage Advisory） | 2026-07-24 | 2026-08-13T09:30:00+08:00 |
| ai.revenue_capex_gap | AI 終端年化營收 ≈$72B vs 年化 capex ≈$725B（分母：top-4＋Oracle） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-06-15 | 2026-08-13T09:30:00+08:00 |
| speculation.ai_rename_spac | 0 件：過去 7 日無合格 AI rename／+AI ticker change／SPAC／無營收投機 IPO 事件 | 篩查定義：AI rename、+AI ticker change、SPAC announcement、no-revenue speculative IPO（2026-08-06 → 2026-08-13；逐字 query 未記錄） | WebSearch 新聞結果（AI rename／SPAC 公告） | — | 2026-08-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 2026-08-12／2026-08-13 各 ≈12 檔定價、平均首日 ≈18% | US IPO pricings week August 2026 IPOScoop | https://www.iposcoop.com/current-year-pricings/（IPOScoop） | 2026-08-13 | 2026-08-13T09:30:00+08:00 |
| speculation.microcap_moonshots | 0 件：過去 7 日無 <$1B 市值、單日 ≥100% 且疊加兩個以上題材的合格 moonshot | 篩查定義：biggest single-day gainers under $1B market cap ≥100%（2026-08-06 → 2026-08-13；逐字 query 未記錄） | Finviz／StockAnalysis movers | — | 2026-08-13T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 9 月上市 ≈$730–850B、Anthropic 續進 | OpenAI Anthropic IPO timing valuation 2026 | https://cryptobriefing.com/openai-ipo-filing-trillion-valuation/（Crypto Briefing） | 2026-07-28 | 2026-08-13T09:30:00+08:00 |
| speculation.insider_form4 | 0 件：過去 14 日無附 Form 4 filing URL／日期的合格 insider 賣出 cluster | 篩查定義：SEC EDGAR Form 4 AI／市值領導股 insider sales（2026-07-30 → 2026-08-13；逐字 query 未記錄） | SEC EDGAR | — | 2026-08-13T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.54（daily） | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio（thetrading.tools） | 2026-08-07 | 2026-08-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 記錄高 ≈$198B（預定來源 etf.com） | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing） | 2026-07-23 | 2026-08-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 0 件：過去 30 日無合格 US single-stock 槓桿 ETF 核准／上市 | 篩查定義：SEC EDGAR ETF filings＋ETF.com new launches single-stock leveraged（2026-07-14 → 2026-08-13；逐字 query 未記錄） | Leverage Shares／Tradr 公告、SEC EDGAR、ETF.com | — | 2026-08-13T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量 ≈65%（Cboe Q2 2026） | 0DTE SPX options share Cboe Q2 2026 65% | https://ca.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4768656（Investing.com） | 2026-07-31 | 2026-08-13T09:30:00+08:00 |
| structural.options_volume | OCC 6 月總量 16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-08-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 135.59、VIX 15.28、MOVE 74.67 | VIX SKEW MOVE bond volatility August 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-10-2026-spx-skew-collapses-on-upside-chasing（Cboe） | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt $1.502T、+51.5% YoY（交叉引用） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives） | 2026-07-20 | 2026-08-13T09:30:00+08:00 |
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
  "r1_drawdown_pct": 2.99,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

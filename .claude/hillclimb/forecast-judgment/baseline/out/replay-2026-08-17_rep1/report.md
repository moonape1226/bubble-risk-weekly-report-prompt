> [DRY RUN] this report was not committed to archive.

# 2026-08-17 AI 泡沫破裂預測報告

報告日期：2026-08-17｜ISO 週次：2026-W34｜預測窗口：2026-08-17 → 2027-02-15｜前次基準：report-2026-08-13（4天前）

## 結論

**結論：no**

三條路徑都未進入完成段：NASDAQ-100 僅距高點 2.00%，需再跌約 23.47% 才觸及 R1；四大 hyperscaler 在 2026-07 下旬 Q2 財報後合計 capex 仍在上修（≈$725B），R2 目前 0/4 下修。最強的反方訊號是 CoreWeave 5Y CDS ≈855bp 與貸款被迫加價＋covenant（R3），但它仍在 2026-07-29 完成 $2.6B 融資、未見任何違約或 distressed exchange，且 HY OAS 2.71% 顯示信用壓力尚未外溢，不足以推翻 182 天窗口內的 no 基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 30,046.14（2026-08-14），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 2.00%；R1 門檻水位 22,995.45，自最新收盤須再下跌約 23.47% 才會觸及（`valuation.ndx_drawdown`）。

背景脆弱度高：S&P 500 trailing P/E ≈29.8、Shiller CAPE ≈42.2（`valuation.sp500_pe_cape`，2026-08-14）；S&P 500 7,785.76 高於 200 日均線 10.05%、高於 52 週均線 11.6%（`valuation.sp500_trend`，2026-08-14）；Mag 7 ≈29x vs 指數 ≈25.6x、佔市值 ≈33.9%（`valuation.mag7_multiples`），Top-10 集中度 ≈37%（`breadth.top10_concentration`，2026-07-24）。FINRA 6 月 margin debt $1.502T、YoY +51.5%，已落在歷史頂部附近常見的 +40–50% 區間（`retail.margin_debt`）。

但時點訊號不支持即刻崩跌：VIX 14.63（2026-08-13），2026-08-06→08-13 的 7 日窗內 VIX −3.43%、S&P 500 +1.15%，未出現同漲的 crowded-optionality 警戒（`structural.vix_spx_comove`）；CNN Fear & Greed ≈65（Greed，`retail.fear_greed`），AAII Bull 38.5%／Bear 38.1% 並不極端（`retail.aaii`）；成分股 ≈71.6% 站上 50DMA，廣度健康（`breadth.advance_decline`）。窗口內可預見的催化劑：2026-10 下旬與 2027-01／02 兩輪 hyperscaler 季報（確切日期未在本次證據中），以及據報 OpenAI 目標 9 月上市、估值 ≈$730–850B（`speculation.upcoming_ai_ipos`，2026-07-28；該來源標題另寫 trillion 估值，可信度有限）——大型 AI IPO 的供給與定價是情緒峰值的典型標記，但不是回撤本身。

**判讀：** R1 距門檻仍有約 23.47% 的距離，短期波動與信用指標都平靜；要在窗口內成立，需要一個外生衝擊把高估值與 margin debt 槓桿同時引爆，例如 R3 型 AI 信用事件、季報 capex 指引轉向或通膨迫使 Fed 轉鷹，目前三者都未發生。

### R2 資本支出收縮

本次證據只取得合計值：2026-07-28 Q2 財報季後，四大 hyperscaler（Microsoft、Alphabet、Amazon、Meta）2026 年 capex 合計 ≈$725B，方向為「仍上修」（`ai.hyperscaler_capex`）。逐家指引數值未包含在本次檢索結果中，不臆造個別數字；逐家方向：Microsoft、Alphabet、Amazon、Meta 皆無下修報導，合計層級為上修，因此目前已下修家數為 0/4。CNBC 同篇標題指出 Alphabet 財報因 capex 被市場「panned」，顯示股價端已開始懲罰 capex，但公司端尚未退讓。

相關壓力：top-5 capex 已超過 FCF、Alphabet Q2 FCF 轉負、2026 發債 ≈$182B（`ai.hyperscaler_financing_mix`，2026-07-24），代表 hyperscaler 融資結構（capex vs FCF / 發債）已從現金流轉向債務；Microsoft 商用 RPO ≈$678B、其中 ≈32% 繫於 OpenAI（`ai.customer_concentration_rpo`，2026-07-30）。需求側目前仍緊：H200 租金 ≈$3.99/hr、HBM 合約價 ≈+40%、Blackwell 售罄（`ai.compute_supply_demand`，2026-08-01），沒有利用率下滑或訂單消化證據。

**判讀：** R2 離成立最遠——合計指引仍在上修、四家皆無下修報導，且算力供給仍短缺。窗口內有兩輪季報（2026-10 下旬、2027-01／02），要成立需兩家在其中一輪就把 2026 或 2027 年指引下修；觸發條件會是股價持續懲罰 capex、FCF 轉負擴大到更多家，或 OpenAI 類大客戶承諾縮水。

### R3 AI 信用事件

最接近 R3 規模門檻的借款人是 CoreWeave（AI 算力為主業；本次證據未載其負債總額，但其公開融資規模使其為主要候選）。信用定價已明顯惡化：5Y CDS ≈855bp、Oracle CDS 處多年高點，AI 貸款投資人要求 covenant（`valuation.ai_credit_schism`，2026-08-03）；CoreWeave $2.6B 貸款被迫將利差調高 +100–125bp 並加上 covenant（`structural.ai_infrastructure_debt`，2026-07-29）。這是 AI 信用定價分歧（equity-vs-credit schism）的後期型態：信貸端開始重定價，而 NASDAQ-100 仍在高點附近。

反方：同一筆 $2.6B 融資確實完成，表示市場仍願意提供資金（只是更貴）；hyperscaler 層級仍能以表外結構大額融資，例如 Meta El Paso 資料中心 >$12B 債券（BlackRock 主導、20–30 年 triple-net lease，`ai.hyperscaler_financing_mix`，2026-07-20）；整體 HY OAS 2.71%、IG OAS 0.79%（`monetary.hy_oas`、`monetary.ig_oas`，2026-08-13）處於緊縮水位，repo 資金壓力（SOFR−IORB）為 −3bp、SOFR99−IORB +5bp、SRF 動用（Standing Repo Facility usage）0.0（`monetary.repo_stress_srf`），融資市場沒有失序跡象。本次證據中沒有任何借款人出現漏付、covenant waiver、distressed exchange 或 going-concern 語言。

**判讀：** R3 是三條路徑中最有動能的一條：CDS ≈855bp 已是市場隱含高違約風險的水位，且加價＋covenant 意味再融資成本快速上升。但從「融資變貴」到「破產／超過寬限期違約／完成 distressed exchange」通常需要融資管道真正關閉；要在窗口內成立，需要再融資失敗、大客戶（OpenAI 等）承諾縮水或 GPU 抵押品價值下跌三者之一發生。若成立，將經由信用重定價直接傳導到 R1。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS ≈855bp、Oracle CDS 多年高，AI 貸款投資人要求 covenant（2026-08-03），信貸端已開始重定價而股價未跟上（`valuation.ai_credit_schism`）。
- [R3] CoreWeave $2.6B 貸款被迫調高利差 +100–125bp 並加 covenant（2026-07-29），再融資成本快速上升（`structural.ai_infrastructure_debt`）。
- [R1] FINRA 6 月 margin debt $1.502T、YoY +51.5%（2026-07-20 發布），落在 1999／2007／2021 頂部附近常見的 +40–50% 區間（`retail.margin_debt`）；同時 US 槓桿 ETF AUM 創記錄 ≈$198B（`structural.leveraged_etf_aum`，2026-07-23），2026-08-11 又新發 6 檔單股 2x 槓桿 ETF（`structural.us_single_stock_etf`）。
- [R2] top-5 hyperscaler capex 已超越 FCF、Alphabet Q2 FCF 轉負、2026 發債 ≈$182B（`ai.hyperscaler_financing_mix`，2026-07-24），capex 的資金來源轉為債務，市場已開始懲罰 capex（`ai.hyperscaler_capex`，2026-07-28 CNBC 標題）。
- [R1] 估值極端：CAPE ≈42.2、trailing P/E ≈29.8（`valuation.sp500_pe_cape`，2026-08-14），S&P 500 高於 200 日均線 10.05%（`valuation.sp500_trend`），回撤一旦啟動的下行空間大。
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收 ≈$72B vs 年化 capex ≈$725B（分母：top-4＋Oracle，2026-06-15 組合值，`ai.revenue_capex_gap`）；Microsoft RPO ≈32% 繫於單一客戶 OpenAI（`ai.customer_concentration_rpo`），backlog 重複計算風險（RPO double-counting）集中在同一 counterparty。
- [整體] Fed 緩衝空間有限：CPI YoY 3.3%（2026-07，`monetary.cpi_yoy`）、5y5y 2.30%（`monetary.t5yifr`），CME FedWatch 9/16 ≈69% 維持不變且無降息定價（`monetary.fedwatch`，2026-08-14）。

## 支持 no 的證據

- [R2] 四大 hyperscaler 2026 capex 合計 ≈$725B 且在 Q2 財報後仍上修（2026-07-28），四家之中目前 0 家下修（`ai.hyperscaler_capex`）。
- [R1] NASDAQ-100 收盤 30,046.14（2026-08-14），距 52 週高點回撤 2.00%，距 R1 門檻 22,995.45 仍需再跌約 23.47%（`valuation.ndx_drawdown`）。
- [R3] 整體信用未外溢：HY OAS 2.71%、IG OAS 0.79%（2026-08-13，`monetary.hy_oas`、`monetary.ig_oas`）；SOFR−IORB −3bp、SRF 動用 0.0（`monetary.repo_stress_srf`）；銀行對 NBFI 放款 $2.02T 持平（`structural.nbfi_bank_loans`）。
- [R2] 算力仍供不應求：H200 租金 ≈$3.99/hr、HBM 合約 ≈+40%、Blackwell 售罄（2026-08-01，`ai.compute_supply_demand`），沒有利用率下滑或訂單消化的證據。
- [R3] 融資管道仍開：CoreWeave 仍完成 $2.6B 融資（`structural.ai_infrastructure_debt`），Meta El Paso >$12B 表外債券順利發行（`ai.hyperscaler_financing_mix`，2026-07-20）。
- [R1] 波動與情緒未失控：VIX 14.63、7 日窗 VIX −3.43% 與 S&P 500 +1.15% 未同漲（`structural.vix_spx_comove`）；MOVE 69.58（`structural.treasury_basis_trade`，2026-08-14）；BofA 8 月 FMS 現金 3.9%、淨 41% 預期成長轉弱，機構並非一致樂觀（`institutional.bofa_jpm_survey`）。
- [整體] 基準率：任意 182 天窗口內 R1–R3 皆屬罕見事件；目前三條路徑都沒有進入完成段——R1 回撤僅 2.00%（`valuation.ndx_drawdown`）、R2 0/4 下修（`ai.hyperscaler_capex`）、R3 無任何違約或 distressed exchange 揭露（`structural.ai_infrastructure_debt`）。

## 與前期比較

前次結論：無前次預測（report-2026-08-13 為舊格式評分報告）

前次為舊格式評分報告，其分數不轉換為 yes/no；flip_evidence 為空。自 2026-08-13 以來的主要變化：

- 多數 FRED 序列在 2026-08-13 之後沒有新觀測（DGS10、DFII10、HY／IG OAS、SOFR 皆 Δ 0），10Y breakeven 與 5y5y 各 +3bp。
- S&P 500 較前次 −0.17%（7,798.99 → 7,785.76），NASDAQ-100 仍在高點附近。
- 美債基差交易槓桿（Treasury basis-trade leverage）的槓桿基金淨空單在 2026-08-11 收斂至 −7,250,927 口（4 週 +311,947），MOVE 69.58。
- 本次新納入的證據多為 2026-07 下旬至 08 上旬的既有披露，CoreWeave 信用重定價為最值得追蹤的變化。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `breadth.rsp_spy`：檢索只取得 2026-06-10 的 RSP vs SPY YTD 數值（+9.67% vs +8.38%），沒有當期可用值，依規則標 ⛔。廣度只是 R1 的確認指標，且 `breadth.advance_decline`（≈71.6% 站上 50DMA）已提供當期廣度讀數，此缺口不會改變結論。

其他未揭露（✗ NOT DISCLOSED）且與判斷相關的來源：`monetary.private_credit_liquidity`（過去 30 日無 BDC 贖回揭露，無法確認私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）是否升溫——若存在 gate proration / breach，會強化 R3）；`ai.openai_anthropic_revenue`（唯一結果為 2026-05-29、非當季，且其標題 $30B 與摘要 $47B 不一致，故不採用）；`valuation.analyst_tp_decomposition`（唯一結果為 Susquehanna TSMC $575→$600，不在指定的頂級賣方之列，且未揭露 EPS／PE 拆解）；`ai.capital_cycle`、`ai.depreciation_life`、`ai.token_growth`、`retail.naaim`、`retail.social_sentiment`、`monetary.pboc`、`structural.global_leveraged_approvals`。另 `monetary.treasury_auctions` 的 30Y 標售數值（BTC 2.39、5.216%）所附 URL 標題指 10 年期標售，歸屬未能確認，僅作背景、不列為證據；`ai.hyperscaler_capex` 只有合計值，缺逐家指引。

最大的不確定性：

1. CoreWeave 再融資路徑：若下一筆融資失敗或被迫走 distressed exchange，R3 直接成立並可能經由信用重定價推動 R1——會把結論推向 yes。其負債總額與近期到期表不在本次證據中。
2. 2026-10 下旬 Q3 財報季的 capex 指引：若 Alphabet（FCF 已轉負）與另一家同時下修，R2 成立——推向 yes；若繼續上修則強化 no。
3. 通膨與 Fed：CPI 3.3%、FedWatch 無降息定價，若通膨再升使 Fed 轉鷹，將削弱市場對高估值的支撐——推向 yes；反之降息空間打開則推向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 29.8 | https://www.multpl.com/s-p-500-pe-ratio | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE | 42.2 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E vs 指數（佔市值 ≈33.9%） | ≈29x vs ≈25.6x | https://www.fool.com/research/magnificent-seven-sp-500/ | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest | 7785.76 | FRED API (series_id=SP500) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（%） | 10.05 | FRED API (series_id=SP500) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（%） | 11.6 | FRED API (series_id=SP500) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 30046.14 | FRED API (series_id=NASDAQ100) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-17T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（%） | 2.0 | FRED API (series_id=NASDAQ100) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS／貸款利差調高 | ≈855bp／+100–125bp | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm | 2026-08-03 | 2026-08-17T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 | ≈37% | https://www.rbcwealthmanagement.com/en-us/insights/the-great-narrowing-sp-500-concentration | 2026-07-24 | 2026-08-17T09:30:00+08:00 |
| breadth.advance_decline | S&P 500 成分股 >50DMA 比例 | ≈71.6% | https://www.investing.com/indices/s-p-500-stocks-above-50-day-average | 2026-08-11 | 2026-08-17T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed | ≈65（Greed） | https://www.cnn.com/markets/fear-and-greed | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-06 月資料）／YoY | $1.502T／+51.5% | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-17T09:30:00+08:00 |
| retail.aaii | AAII Bull／Neutral／Bear（週結束 2026-08-12） | 38.5%／23.3%／38.1% | https://www.aaii.com/sentimentsurvey | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1 資料，FRED 期初日期標記；家庭股票佔金融資產 %） | 45.76 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-17T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA FMS 8 月：現金水位／淨成長預期 | 3.9%／淨 −41% | https://www.tradingview.com/news/macenews:d7660a8e2094b:0-bofa-global-research-fund-manager-survey-global-investors-increasingly-more-cautious-about-growth-and-inflation-in-august/ | 2026-08-12 | 2026-08-17T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（%） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-16 | 2026-08-17T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（%） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-16 | 2026-08-17T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.71 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.79 | FRED API (series_id=BAMLC0A0CM) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%；no_new_obs，Δ 0） | 4.63 | FRED API (series_id=DGS10) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%；no_new_obs，Δ 0） | 2.39 | FRED API (series_id=DFII10) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.27 | FRED API (series_id=T10YIE) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | 3.0 | FRED API (series_id=T10YIE) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl） | 84.77 | FRED API (series_id=DCOILWTICO) | 2026-08-11 | 2026-08-17T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料，%） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-17T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.3 | FRED API (series_id=T5YIFR) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（%；Kim-Wright） | 0.8257 | FRED API (series_id=THREEFYTP10) | 2026-08-07 | 2026-08-17T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7d） | -4.2 | FRED API (series_id=THREEFYTP10) | 2026-08-07 | 2026-08-17T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API (series_id=SOFR99) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-17 | 2026-08-17T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（十億美元，SRF 動用 read） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 標售 bid-to-cover／得標利率（URL 標題指 10 年期，歸屬待確認） | BTC 2.39／5.216% | https://www.rttnews.com/3679611/ten-year-note-auction-attracts-modestly-above-average-demand.aspx | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 9/16 維持不變機率 | ≈69% | https://growbeansprout.com/tools/fedwatch | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6759955.0（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-12 | 2026-08-17T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5923023.0（€5.92T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-07 | 2026-08-17T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-17T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計（Q2 財報後仍上修） | ≈$725B | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-07-28 | 2026-08-17T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft 商用 RPO／單一客戶（OpenAI）佔比 | $678B／≈32% | https://www.benzinga.com/trading-ideas/long-ideas/26/07/60816147/microsofts-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer | 2026-07-30 | 2026-08-17T09:30:00+08:00 |
| ai.compute_supply_demand | H200 租金中位／HBM 合約價變動 | ≈$3.99/hr／≈+40% | https://jarvislabs.ai/blog/h200-price | 2026-08-01 | 2026-08-17T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 超越 FCF（Alphabet Q2 FCF 轉負）／2026 發債 | ≈$182B | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure | 2026-07-24 | 2026-08-17T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan][spv_deal] Meta El Paso 資料中心 BlackRock 主導債券（表外 triple-net lease 結構） sponsor_equity_split=undisclosed; residual_value_guarantee=undisclosed; lease_term=20-30yr; debt_tenor=undisclosed; lead_lenders=BlackRock/JPMorgan/MS; | >$12B | https://www.landgate.com/news/blackrock-s-12-billion-bond-sale-signals-a-new-financing-playbook-for-data-center-developers | 2026-07-20 | 2026-08-17T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 vs 年化 capex（分母：top-4＋Oracle） | ≈$72B vs ≈$725B | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-06-15 | 2026-08-17T09:30:00+08:00 |
| speculation.ipo_heat | 本週 US IPO 定價檔數（YTD 226 檔） | ≈11 檔 | https://www.iposcoop.com/current-year-pricings/ | 2026-08-17 | 2026-08-17T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI IPO 估值區間（目標 9 月上市） | ≈$730–850B | https://cryptobriefing.com/openai-ipo-filing-trillion-valuation/ | 2026-07-28 | 2026-08-17T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity-only put/call（未標示 daily 或 5 日平均） | 0.54 | https://www.thetrading.tools/put-call-ratio | 2026-08-07 | 2026-08-17T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM（記錄高） | ≈$198B | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-07-23 | 2026-08-17T09:30:00+08:00 |
| structural.us_single_stock_etf | 2026-08-11 新發單股 2x 槓桿 ETF（Leverage Shares／Tradr 合計；所附稿為 Leverage Shares 三檔） | 6 檔 | https://www.globenewswire.com/news-release/2026/08/11/3342794/0/en/leverage-shares-by-themes-launches-three-new-2x-etfs-targeting-ai-infrastructure-and-connectivity-leaders.html | 2026-08-11 | 2026-08-17T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量（Cboe 2026 Q2） | ≈65% | https://ca.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4768656 | 2026-07-31 | 2026-08-17T09:30:00+08:00 |
| structural.options_volume | OCC 總量（2026-06 月資料） | 1,603,491,559 口（≈16.0 億口） | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report | 2026-07-02 | 2026-08-17T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW／VIX／MOVE | ≈135／14.63／≈75 | https://www.cboe.com/insights/posts/week-of-8-10-2026-spx-skew-collapses-on-upside-chasing | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 14.63 | FRED API (series_id=VIXCLS) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of；comove=false，window_days 7，base_date 2026-08-06） | 14.63 | FRED API (series_id=VIXCLS / SP500) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（%） | -3.43 | FRED API (series_id=VIXCLS / SP500) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（%） | 1.15 | FRED API (series_id=VIXCLS / SP500) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt（2026-06 月資料，交叉引用）／YoY | $1.502T／+51.5% | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-17T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B 貸款利差調高＋covenant／5Y CDS | +100–125bp／≈855bp | https://www.stocktitan.net/news/CRWV/core-weave-closes-2-6-billion-loan-facility-expanding-financing-gwhngwnf0jt5.html | 2026-07-29 | 2026-08-17T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2016.0821（$2.02T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-05 | 2026-08-17T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六檔 UST 期貨槓桿基金淨部位，口） | -7250927 | CFTC TFF futures-only | 2026-08-11 | 2026-08-17T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 311947 | CFTC TFF futures-only | 2026-08-11 | 2026-08-17T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 69.58 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party transaction volume，十億美元） | 2381.8 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |

10Y 分解（`decomposition`）：ΔDGS10 0bp、ΔDFII10 0bp、ΔT10YIE +3bp；freshness = partial_stale（stale_series：DGS10、DFII10 自 2026-08-13 起無新觀測），T10YIE 視窗不同，判讀：不可判（視窗不一致）。repo_stress（as_of 2026-08-13，iorb_date／sofr99_date／sofr99_iorb_date 皆 2026-08-13）：SOFR−IORB −3bp、SOFR99−IORB +5bp、SRF 0.0（srf_date 2026-08-14）。

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl / gurufocus [primary: SEARCH]，multpl 直接頁亦取得同值 | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | Motley Fool research 頁 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方 TP 上修掃描（90d＋同季）[primary: SEARCH] | ✗ NOT DISCLOSED（僅 Susquehanna TSMC $575→$600，非指定頂級賣方且無 EPS／PE 拆解） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API（sp500_trend ok） |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API（ndx_drawdown ok） |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場 14 日掃描 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) YTD divergence | 24/7 Wall St WebSearch | ⛔ FETCH FAILED（僅取得 2026-06-10 舊值，無當期可用值） |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | RBC Wealth Management WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | Investing.com breadth WebSearch（>50DMA 比例） | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA via Advisor Perspectives WebSearch（stock-of-state，6 月資料） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag WebSearch | ✗ NOT DISCLOSED（無顯著討論） |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API（BOGZ1FL153064486Q ok） |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／YCharts [primary: SEARCH] | ✗ NOT DISCLOSED（無當週值） |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✓ SEARCH-VERIFIED（BofA 8 月；JPM 無新調查） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok／DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API（ok） |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API（ok） |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API（ok，no_new_obs） |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API（ok，no_new_obs） |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直接取得） | ✓ API（ok） |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API（ok） |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（yoy_pct） | ✓ API（ok，2026-07 月資料） |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API（ok） |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（Kim-Wright） | ✓ API（ok） |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok／SOFR99 ok／IORB ok／RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | Reuters／RTTNews recap [primary: SEARCH] | ✓ SEARCH-VERIFIED（URL 標題與 30Y 數值歸屬不一致，僅作背景） |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py | ✓ API（ok） |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py | ✓ API（ECBASSETSW ok／JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | investing／Yicai WebSearch | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC／interval fund 30 日披露掃描 [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報報導 WebSearch（stock-of-state，Q2 財報；僅合計值） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | 報導 WebSearch | ✗ NOT DISCLOSED（無當季披露；2026-05-29 結果標題與數值不一致） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話報導 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | GPU 租金／HBM 報價 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：Sage Advisory top-5 capex vs FCF／發債；event_scan：30 日大額融資掃描（Meta El Paso 表外債券） | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | epoch.ai 組合披露（stock-of-state carry） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q 30 日掃描 [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | quarterly_state：供需增速對比；event_scan：30 日進出場事件掃描；兩者皆無可用披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC / no-revenue IPO | Reuters／Benzinga／SEC 7 日螢幕 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | IPOScoop WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／StockAnalysis gainers 螢幕 [primary: SEARCH] | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | S-1／具名報導 30 日掃描 | ✓ SEARCH-VERIFIED（來源標題與估值數字不一致，低權重） |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR／openinsider／secform4 14 日螢幕 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | thetrading.tools [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com／報導 [primary: SEARCH] | ✓ SEARCH-VERIFIED（僅總 AUM，未逐檔） |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | Leverage Shares／Tradr 發行公告 30 日掃描 | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA 7 日掃描 | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe Q2 簡報報導 WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC monthly volume report | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe insights WebSearch（stock-bond correlation 未取得） | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok／vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | Advisor Perspectives（交叉引用 Retail Sentiment） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | 30 日融資掃描 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API（ok） |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds／move_index／ofr_repo；WebSearch 無新增揭露 | ✓ API（cftc_lev_funds ok／move_index ok／ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E ≈29.8、CAPE ≈42.2（原定來源 multpl／gurufocus） | S&P 500 trailing P/E Shiller CAPE multpl August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio （GuruFocus） | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 ≈29x vs 指數 ≈25.6x、佔市值 ≈33.9%（原定來源 Mag 7 加權 P/E） | Magnificent 7 weighted PE vs S&P 500 August 2026 | https://www.fool.com/research/magnificent-seven-sp-500/ （Motley Fool） | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS ≈855bp、貸款利差 +100–125bp、Oracle CDS 多年高 | CoreWeave Oracle CDS spread AI credit widening August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm （Tech Times） | 2026-08-03 | 2026-08-17T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 ≈37% | S&P 500 top 10 concentration percent 2026 | https://www.rbcwealthmanagement.com/en-us/insights/the-great-narrowing-sp-500-concentration （RBC Wealth Management） | 2026-07-24 | 2026-08-17T09:30:00+08:00 |
| breadth.advance_decline | ≈71.6% S&P 500 成分股在 50DMA 上（A/D、新高新低比未取得） | S&P 500 percent above 50 day moving average August 2026 | https://www.investing.com/indices/s-p-500-stocks-above-50-day-average （Investing.com） | 2026-08-11 | 2026-08-17T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed ≈65（Greed） | CNN Fear and Greed Index August 14 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives，原定來源 FINRA） | 2026-07-20 | 2026-08-17T09:30:00+08:00 |
| retail.aaii | AAII Bull 38.5%／Neutral 23.3%／Bear 38.1%（週結束 2026-08-12） | AAII investor sentiment survey week August 12 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA 8 月 FMS：現金 3.9%、淨 41% 預期成長轉弱 | BofA Global Fund Manager Survey August 2026 cash levels | https://www.tradingview.com/news/macenews:d7660a8e2094b:0-bofa-global-research-fund-manager-survey-global-investors-increasingly-more-cautious-about-growth-and-inflation-in-august/ （TradingView／MNI） | 2026-08-12 | 2026-08-17T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 2026-08-13 BTC 2.39、5.216%、indirect 66.8%（URL 標題指 10 年期標售，歸屬待確認） | US Treasury 30 year bond auction August 13 2026 bid to cover | https://www.rttnews.com/3679611/ten-year-note-auction-attracts-modestly-above-average-demand.aspx （RTTNews） | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 9/16 ≈69% 維持不變、無降息定價（原定來源 CME FedWatch） | CME FedWatch September 2026 rate probability | https://growbeansprout.com/tools/fedwatch （Beansprout） | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計 ≈$725B、仍上修（Q2 財報） | hyperscaler capex 2026 725 billion raised Q2 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-08-17T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO ≈$678B、≈32% 繫單一客戶（OpenAI） | Microsoft RPO backlog 678 billion OpenAI 2026 | https://www.benzinga.com/trading-ideas/long-ideas/26/07/60816147/microsofts-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer （Benzinga） | 2026-07-30 | 2026-08-17T09:30:00+08:00 |
| ai.compute_supply_demand | HBM 合約 ≈+40%、H200 租金 ≈$3.99/hr、Blackwell 售罄 | H200 GPU rental HBM DRAM 2026 shortage Blackwell | https://jarvislabs.ai/blog/h200-price （JarvisLabs） | 2026-08-01 | 2026-08-17T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 超越 FCF、2026 發債 ≈$182B | hyperscaler capex FCF debt issuance 182 billion 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure （Sage Advisory） | 2026-07-24 | 2026-08-17T09:30:00+08:00 |
| ai.revenue_capex_gap | AI 終端年化營收 ≈$72B vs 年化 capex ≈$725B（分母：top-4＋Oracle） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-06-15 | 2026-08-17T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收 IPO 合格件數 0 | AI rename ticker SPAC no revenue IPO August 10-17 2026 | Reuters／Benzinga／SEC 螢幕 | — | 2026-08-17T09:30:00+08:00 |
| speculation.ipo_heat | 本週約 11 檔定價、YTD 226 檔（首日報酬與無營收占比未取得） | US IPO pricings week August 2026 IPOScoop | https://www.iposcoop.com/current-year-pricings/ （IPOScoop） | 2026-08-17 | 2026-08-17T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot 合格 0 件 | microcap 100% single day quantum fusion nuclear AI August 2026 | Finviz／StockAnalysis gainers 螢幕 | — | 2026-08-17T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 9 月上市 ≈$730–850B、Anthropic 續進（標題另寫 trillion 估值） | OpenAI Anthropic IPO timing valuation 2026 | https://cryptobriefing.com/openai-ipo-filing-trillion-valuation/ （Crypto Briefing） | 2026-07-28 | 2026-08-17T09:30:00+08:00 |
| speculation.insider_form4 | 過去 14 日 AI／領導股合格 Form 4 賣壓 cluster 0 件 | AI leadership insider Form 4 sale August 3-17 2026 SEC | openinsider／secform4／SEC EDGAR 螢幕 | — | 2026-08-17T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.54 | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio （thetrading.tools，原定來源 Cboe） | 2026-08-07 | 2026-08-17T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 記錄高 ≈$198B | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing，原定來源 etf.com） | 2026-07-23 | 2026-08-17T09:30:00+08:00 |
| structural.us_single_stock_etf | 2026-08-11 新發 6 檔單股 2x 槓桿 ETF（Leverage Shares／Tradr） | single-stock leveraged ETF launch August 11 2026 Leverage Shares Tradr | https://www.globenewswire.com/news-release/2026/08/11/3342794/0/en/leverage-shares-by-themes-launches-three-new-2x-etfs-targeting-ai-infrastructure-and-connectivity-leaders.html （GlobeNewswire） | 2026-08-11 | 2026-08-17T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量 ≈65%（Cboe 2026 Q2） | 0DTE SPX options share Cboe Q2 2026 65% | https://ca.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4768656 （Investing.com） | 2026-07-31 | 2026-08-17T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月總量 16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-08-17T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW ≈135、VIX 14.63、MOVE ≈75 | VIX SKEW MOVE bond volatility August 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-10-2026-spx-skew-collapses-on-upside-chasing （Cboe） | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt $1.502T、+51.5% YoY（交叉引用 Retail Sentiment） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-08-17T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B 貸款利差 +100–125bp＋covenant、5Y CDS ≈855bp | CoreWeave 2.6 billion loan spread covenant CDS August 2026 | https://www.stocktitan.net/news/CRWV/core-weave-closes-2-6-billion-loan-facility-expanding-financing-gwhngwnf0jt5.html （StockTitan） | 2026-07-29 | 2026-08-17T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-17",
  "iso_week": "2026-W34",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-15",
  "prior_date": "2026-08-13",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 2.0,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

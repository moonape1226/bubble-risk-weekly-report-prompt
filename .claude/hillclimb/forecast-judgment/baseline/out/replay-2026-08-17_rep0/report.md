> [DRY RUN] this report was not committed to archive.

# 2026-08-17 AI 泡沫破裂預測報告
報告日期：2026-08-17｜ISO 週次：2026-W34｜預測窗口：2026-08-17 → 2027-02-15｜前次基準：report-2026-08-13（4天前）

## 結論

**結論：no**

三條路徑都還沒有啟動：NASDAQ-100 距 52 週高點只回撤 2.00%，要再跌約 23.47% 才會觸發 R1；hyperscaler 2026 capex 合計約 $725B，報導口徑仍在上修，R2 目前 0/4 家下修。最強的反方訊號是 CoreWeave 5Y CDS 約 855bp、新貸款被迫加碼 +100–125bp 並附 covenant，但它在 2026-07-29 仍完成 $2.6B 融資，HY OAS 也只有 2.71%。這代表 AI 信用在重定價，但離 R3 要求的違約、破產或 distressed exchange 還有距離，因此維持 base rate，判 no。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 30,046.14（2026-08-14），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 2.00%。R1 門檻水位 22,995.45，從最新收盤還要再跌約 23.47% 才會觸及（`valuation.ndx_drawdown`）。

背景數據：
- S&P 500 為 7,785.76（2026-08-14），比 200 日均線高 10.05%、比 52 週均線高 11.6%，價格延伸偏大（`valuation.sp500_trend`）。
- 估值偏高：trailing P/E 29.8、CAPE 42.2（2026-08-14，`valuation.sp500_pe_cape`）；Mag 7 加權 P/E 約 29x，指數約 25.6x（`valuation.mag7_multiples`）。
- 避險情緒低：VIX 14.63（2026-08-13）。在 2026-08-06→2026-08-13 的 7 日共享窗口內，S&P 500 +1.15%、VIX −3.43%，沒有出現同漲（comove=false，`structural.vix_spx_comove`）。
- 槓桿面偏高：FINRA 6 月 margin debt $1.502T，YoY +51.5%（`retail.margin_debt`）；美國槓桿 ETF AUM 約 $198B，創紀錄（`structural.leveraged_etf_aum`）；0DTE 約占 SPX 期權量 65%（`structural.zero_dte`）。

**判讀：** 回撤距門檻還很遠。高估值與高槓桿讓下跌一旦發生時幅度會很大，但 182 天內要跌 25%，需要外部觸發。可能的觸發包括：hyperscaler 財報季出現 capex 或 AI 營收失望、CoreWeave 類信用事件外溢，或利率與期限溢價急升。目前這些觸發都沒有成形。

### R2 資本支出收縮

本次證據沒有取得四家公司各自的指引數值。可確認的是：2026-07-28 的 CNBC 報導指出，hyperscaler 2026 capex 合計約 $725B，且仍在上修（`ai.hyperscaler_capex`）。各公司情況如下：

- Microsoft：最新指引為 2026 Q2 財報季（2026-07 下旬）。個別數值未取得；合計層級為上修，未見下修報導。
- Alphabet：同上，2026 Q2 財報季。CNBC 提到 Alphabet 財報後 capex 受到市場檢視，但沒有下修報導；Alphabet Q2 FCF 轉負（`ai.hyperscaler_financing_mix`）。
- Amazon：同上，2026 Q2 財報季。個別數值未取得，未見下修報導。
- Meta：同上，2026 Q2 財報季。個別數值未取得，未見下修報導。另有 BlackRock 主導、規模超過 $12B 的 El Paso 資料中心表外融資，顯示 Meta 仍在擴張（`ai.hyperscaler_financing_mix`）。

目前下修家數為 0/4。依季報節奏，2026 Q3（10 月下旬）與 2026 Q4（2027 年 1 月下旬至 2 月初）兩輪財報都落在窗口內，確切日期本次未取得。需求端仍偏緊：Blackwell 售罄、HBM 合約價約 +40%、H200 租金約 $3.99/hr（2026-08-01，`ai.compute_supply_demand`）。

**判讀：** 這條路徑離觸發最遠。要在窗口內成立，需要兩家公司在 Q3 或 Q4 財報中把指引轉為下修，而目前方向是上修，供給也仍然緊。可能的推力有三個：Alphabet 一類 FCF 轉負引發股東壓力；AI 營收對 capex 缺口（年化約 $72B 對約 $725B）長期無法收斂；R1 大幅回撤後被迫節制支出。

### R3 AI 信用事件

AI 算力為主業、最可能觸及 R3 規模門檻的借款人是 CoreWeave（總負債本次證據未列示）。

- 2026-07-29 完成 $2.6B 貸款，但被迫把利差調高 +100–125bp 並加上 covenant（`structural.ai_infrastructure_debt`）。
- 5Y CDS 約 855bp；Oracle CDS 也在多年高點（2026-08-03，`valuation.ai_credit_schism`）。Oracle 不以 AI 資料中心為主業，不直接適用 R3。

這是 AI 信用定價分歧（equity-vs-credit schism）中，信貸端開始重定價的訊號。不過證據中沒有付款違約、covenant waiver、distressed exchange 或 going-concern 字樣。整體信用環境也平穩：HY OAS 2.71%、IG OAS 0.79%（2026-08-13，`monetary.hy_oas`、`monetary.ig_oas`）。

**判讀：** R3 是三條路徑中最接近的一條，但仍有距離。855bp 的 CDS 反映市場要求明顯的違約補償，但借款人仍能在市場籌到資金。要在窗口內成立，需要再融資管道關閉（例如股價重挫、客戶承諾被削減、或 OpenAI 一類單一客戶出問題），並在 6 個月內演變成實際違約或 distressed exchange。這種速度通常需要 R1 或 R2 先發生。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 約 855bp，$2.6B 貸款被迫加碼 +100–125bp 並附 covenant（2026-07-29／2026-08-03），Oracle CDS 也在多年高點。AI 信用端已開始重定價（`valuation.ai_credit_schism`、`structural.ai_infrastructure_debt`）。
- [整體] hyperscaler 融資結構（capex vs FCF / 發債）轉向舉債：top-5 capex 已超過 FCF（Alphabet Q2 FCF 轉負），2026 發債約 $182B（2026-07-24）；Meta El Paso 有超過 $12B 的表外融資（2026-07-20）（`ai.hyperscaler_financing_mix`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 $72B，年化 capex 約 $725B（分母：top-4＋Oracle，2026-06-15）。Microsoft RPO $678B 中約 32% 繫於 OpenAI 單一客戶（2026-07-30），顯示營收集中（`ai.revenue_capex_gap`、`ai.customer_concentration_rpo`）。
- [整體] 估值與槓桿偏極端：CAPE 42.2（2026-08-14）、margin debt YoY +51.5%（6 月資料）、槓桿 ETF AUM 約 $198B 創紀錄。這些代表一旦下跌，幅度會很大（`valuation.sp500_pe_cape`、`retail.margin_debt`、`structural.leveraged_etf_aum`）。
- [R1] S&P 500 比 200 日均線高 10.05%（2026-08-14），0DTE 約占 SPX 期權量 65%（Cboe Q2），價格延伸偏大，選擇權投機也重（`valuation.sp500_trend`、`structural.zero_dte`）。
- [整體] Fed 緩衝空間有限：CME FedWatch 顯示 9/16 會議維持不變約 69%，市場未定價降息（2026-08-14）；CPI YoY 3.3%（2026-07 月資料）；10Y 期限溢價（term premium）0.8257%（2026-08-07）（`monetary.fedwatch`、`monetary.cpi_yoy`、`monetary.term_premium`）。

## 支持 no 的證據

- [R1] NASDAQ-100 最新收盤 30,046.14（2026-08-14），距 52 週高點回撤 2.00%，要再跌約 23.47% 才會到 R1 門檻 22,995.45（`valuation.ndx_drawdown`）。
- [R2] hyperscaler 2026 capex 合計約 $725B 且仍在上修（2026-07-28），四家都沒有下修報導。需求端偏緊：Blackwell 售罄、HBM 合約價約 +40%（2026-08-01）（`ai.hyperscaler_capex`、`ai.compute_supply_demand`）。
- [R3] 整體信用環境平穩：HY OAS 2.71%、IG OAS 0.79%（2026-08-13）。CoreWeave 在 2026-07-29 仍完成 $2.6B 貸款，再融資管道未關閉（`monetary.hy_oas`、`monetary.ig_oas`、`structural.ai_infrastructure_debt`）。
- [整體] 資金與債市沒有失序跡象：
  - repo 資金壓力（SOFR−IORB）−3bp，SOFR99−IORB +5bp（2026-08-13）；SRF 動用（Standing Repo Facility usage）0.0（2026-08-14）（`monetary.repo_stress_srf`）。
  - MOVE 69.58（2026-08-14）（`structural.treasury_basis_trade`）。
  - VIX 14.63，與 S&P 500 沒有同漲（`structural.vix_spx_comove`）。
- [整體] 情緒沒有到狂熱：AAII 看多 38.5%、看空 38.1%（週結束 2026-08-12）；CNN Fear & Greed 約 65（2026-08-14）；BofA 8 月 FMS 現金水位 3.9%，淨 41% 預期成長轉弱（2026-08-12），屬謹慎而非亢奮（`retail.aaii`、`retail.fear_greed`、`institutional.bofa_jpm_survey`）。

## 與前期比較

前次結論：無前次預測（report-2026-08-13 為舊格式評分報告）

這是新格式下的第一份 yes/no 預測，flip_evidence 為 []。舊格式的六維評分不轉換為 yes/no。

自 2026-08-13 以來可觀察的變化：
- DGS10、DFII10 沒有新觀測（Δ 0bp）。
- T10YIE +3.0bp，driver 不可判（視窗不一致）。
- MOVE 從 69.23 升到 69.58。
- CFTC 槓桿基金美債期貨淨空單 4 週內減少 311,947 口。

這些都不足以改變路徑判讀。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `breadth.rsp_spy`：搜尋只找到 2026-06-10 的 RSP vs SPY YTD 數值（+9.67% vs +8.38%），對 2026-08-17 而言不是當期快照，因此判定沒有可用的當期值。廣度只是脆弱度的輔助讀數；Top-10 集中度約 37%、約 71.6% 成分股在 50DMA 之上仍可用，這個缺口不會改變答案。

NOT DISCLOSED 來源（僅說明，不作證據）：

- `valuation.analyst_tp_decomposition`：唯一命中是 Susquehanna 的 TSMC 目標價 $575→$600，Susquehanna 不在指定的 top-tier 名單內，也缺 EPS／PE 拆解。
- `ai.openai_anthropic_revenue`：最新披露日期 2026-05-29，屬前一季；而且結果數值（Anthropic 約 $47B）與來源標題（$30B）不一致。
- `ai.capital_cycle`：兩個 component 都沒有找到可用披露，本次不判定資本週期階段（capital cycle stage）。
- 其他未披露來源：`retail.social_sentiment`、`retail.naaim`、`monetary.pboc`、`monetary.private_credit_liquidity`（私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）30 日內沒有 redemption-request ratio 或 gate proration / breach 披露）、`ai.token_growth`、`ai.depreciation_life`、`structural.global_leveraged_approvals`。私募信貸若在窗口內出現 net inflow→outflow flip，可能把 R3 傳導加速，這是本次無法觀察的盲點。

資料品質註記：

- `monetary.treasury_auctions`：30Y 標售（2026-08-13，BTC 2.39、5.216%）所附 URL 的標題是 10 年期標售，來源與描述不一致，本次不作證據引用。
- `structural.cross_asset_derivatives`：來源的 MOVE 約 75，與 script 的 69.58 不一致，以 script 值為準；rolling stock-bond correlation 未取得。
- `structural.us_single_stock_etf`：結果稱 6 檔，但 GlobeNewswire 標題只列 3 檔（Leverage Shares），其餘歸屬 Tradr 但沒有獨立 URL。
- 四家 hyperscaler 的個別 capex 指引數值未取得，只有合計約 $725B。

最大的不確定性：

1. 2026 Q3／Q4 hyperscaler 財報。若出現兩家下修指引，或 AI 營收明顯失望，會直接推向 yes（R2），並可能經由估值重評帶動 R1。
2. CoreWeave 再融資與客戶承諾。CDS 從約 855bp 繼續走闊、出現 covenant waiver，或 OpenAI 承諾被削減，會推向 yes（R3）；若再融資持續順利，則支持 no。
3. 利率與財政。期限溢價與標售需求若轉弱，導致 10Y 急升，可能成為 R1 的估值觸發；目前 MOVE 與 repo 平穩，支持 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 29.8 | https://www.multpl.com/s-p-500-pe-ratio | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE | 42.2 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E vs 指數（Mag 7 占市值約 33.9%） | 29x vs 25.6x（約） | https://www.fool.com/research/magnificent-seven-sp-500/ | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest | 7785.76 | FRED API (series_id=SP500) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 10.05 | FRED API (series_id=SP500) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 11.6 | FRED API (series_id=SP500) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 30046.14 | FRED API (series_id=NASDAQ100) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-17T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 2.0 | FRED API (series_id=NASDAQ100) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS／貸款利差調高 | 855bp（約）／+100–125bp | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm | 2026-08-03 | 2026-08-17T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 | 37%（約） | https://www.rbcwealthmanagement.com/en-us/insights/the-great-narrowing-sp-500-concentration | 2026-07-24 | 2026-08-17T09:30:00+08:00 |
| breadth.advance_decline | S&P 500 成分股 >50DMA 比例（廣度代理） | 71.6%（約） | https://www.investing.com/indices/s-p-500-stocks-above-50-day-average | 2026-08-11 | 2026-08-17T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed | 65（約，Greed） | https://www.cnn.com/markets/fear-and-greed | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-06 月資料）／YoY | $1.502T／+51.5% | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-17T09:30:00+08:00 |
| retail.aaii | AAII Bull／Neutral／Bear（週結束 2026-08-12） | 38.5%／23.3%／38.1% | https://www.aaii.com/sentimentsurvey | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q1） | 45.76 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-17T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA FMS 8 月：現金水位／淨預期成長轉弱 | 3.9%／淨 41% | https://www.tradingview.com/news/macenews:d7660a8e2094b:0-bofa-global-research-fund-manager-survey-global-investors-increasingly-more-cautious-about-growth-and-inflation-in-august/ | 2026-08-12 | 2026-08-17T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-16 | 2026-08-17T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-16 | 2026-08-17T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.71 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.79 | FRED API (series_id=BAMLC0A0CM) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.63 | FRED API (series_id=DGS10) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.39 | FRED API (series_id=DFII10) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.27 | FRED API (series_id=T10YIE) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | +3.0 | FRED API (series_id=T10YIE) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 84.77 | FRED API (series_id=DCOILWTICO) | 2026-08-11 | 2026-08-17T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-17T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.3 | FRED API (series_id=T5YIFR) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8257 | FRED API (series_id=THREEFYTP10) | 2026-08-07 | 2026-08-17T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7d） | -4.2 | FRED API (series_id=THREEFYTP10) | 2026-08-07 | 2026-08-17T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.62 | FRED API (series_id=SOFR) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.7 | FRED API (series_id=SOFR99) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-08-17 | 2026-08-17T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用 read，transaction volume） | 0.0（十億美元） | FRED API (series_id=RPONTTLD) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress SOFR−IORB（bps） | -3.0 | FRED API (series_id=SOFR, IORB) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress SOFR99−IORB（bps） | 5.0 | FRED API (series_id=SOFR99, IORB) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 標售 bid-to-cover／得標利率（來源標題不一致，僅備查） | 2.39／5.216% | https://www.rttnews.com/3679611/ten-year-note-auction-attracts-modestly-above-average-demand.aspx | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 9/16 維持不變 | 69%（約） | https://growbeansprout.com/tools/fedwatch | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6759955.0（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-12 | 2026-08-17T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5923023.0（€5.92T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-07 | 2026-08-17T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-17T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計（2026 Q2 財報季，仍上修） | $725B（約） | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-07-28 | 2026-08-17T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft 商用 RPO／單一客戶（OpenAI）占比 | $678B／32%（約） | https://www.benzinga.com/trading-ideas/long-ideas/26/07/60816147/microsofts-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer | 2026-07-30 | 2026-08-17T09:30:00+08:00 |
| ai.compute_supply_demand | H200 租金中位／HBM 合約價變動 | $3.99/hr／+40%（約） | https://jarvislabs.ai/blog/h200-price | 2026-08-01 | 2026-08-17T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 2026 hyperscaler 發債（top-5 capex 已超越 FCF） | $182B（約） | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure | 2026-07-24 | 2026-08-17T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan][spv_deal] Meta El Paso 資料中心 BlackRock 主導債券，表外結構 triple-net lease sponsor_equity_split=undisclosed;residual_value_guarantee=undisclosed;lease_term=20-30yr;debt_tenor=undisclosed;lead_lenders=BlackRock/JPMorgan/MS; | >$12B | https://www.landgate.com/news/blackrock-s-12-billion-bond-sale-signals-a-new-financing-playbook-for-data-center-developers | 2026-07-20 | 2026-08-17T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 vs 年化 capex（分母：top-4＋Oracle） | $72B vs $725B（約） | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-06-15 | 2026-08-17T09:30:00+08:00 |
| speculation.ipo_heat | 2026-08-17 起當週 IPO 行事曆檔數／YTD 定價檔數 | 11 檔（約）／226 檔 | https://www.iposcoop.com/current-year-pricings/ | 2026-08-17 | 2026-08-17T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 9 月上市估值區間 | $730–850B（約） | https://cryptobriefing.com/openai-ipo-filing-trillion-valuation/ | 2026-07-28 | 2026-08-17T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity-only put/call（日／5 日均未標明） | 0.54 | https://www.thetrading.tools/put-call-ratio | 2026-08-07 | 2026-08-17T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM（記錄高） | $198B（約） | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-07-23 | 2026-08-17T09:30:00+08:00 |
| structural.us_single_stock_etf | 2026-08-11 新發單股 2x 槓桿 ETF 檔數（Leverage Shares／Tradr） | 6 檔 | https://www.globenewswire.com/news-release/2026/08/11/3342794/0/en/leverage-shares-by-themes-launches-three-new-2x-etfs-targeting-ai-infrastructure-and-connectivity-leaders.html | 2026-08-11 | 2026-08-17T09:30:00+08:00 |
| structural.zero_dte | 0DTE 占 SPX 期權量（Cboe Q2 2026） | 65%（約） | https://ca.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4768656 | 2026-07-31 | 2026-08-17T09:30:00+08:00 |
| structural.options_volume | OCC 總量（2026-06 月資料） | 1,603,491,559 口（約 16.0 億口） | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report | 2026-07-02 | 2026-08-17T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW／VIX／MOVE（MOVE 與 script 不一致） | 135（約）／14.63／75（約） | https://www.cboe.com/insights/posts/week-of-8-10-2026-spx-skew-collapses-on-upside-chasing | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 14.63 | FRED API (series_id=VIXCLS) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 14.63 | FRED API (series_id=VIXCLS, SP500) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（base 2026-08-06，window 7d） | -3.43 | FRED API (series_id=VIXCLS, SP500) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（comove=false） | 1.15 | FRED API (series_id=VIXCLS, SP500) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt／YoY（2026-06 月資料，交叉確認） | $1.502T／+51.5% | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-17T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B 貸款利差調高＋covenant／5Y CDS | +100–125bp／855bp（約） | https://www.stocktitan.net/news/CRWV/core-weave-closes-2-6-billion-loan-facility-expanding-financing-gwhngwnf0jt5.html | 2026-07-29 | 2026-08-17T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2016.0821（$2.02T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-05 | 2026-08-17T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約合計） | -7,250,927 口 | CFTC TFF (cftc_lev_funds) | 2026-08-11 | 2026-08-17T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | +311,947 口 | CFTC TFF (cftc_lev_funds) | 2026-08-11 | 2026-08-17T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 69.58 | Yahoo chart ^MOVE (move_index) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party transaction volume） | 2381.8（$2.38T） | OFR STFM (ofr_repo) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |

10Y 分解（decomposition）：ΔDGS10 0.0bp、ΔDFII10 0.0bp、ΔT10YIE +3.0bp；driver 不可判（視窗不一致）。freshness 為 partial_stale，stale_series 為 DGS10、DFII10，T10YIE 有新觀測。repo_stress 的 SOFR、IORB、SOFR99 參考日均為 2026-08-13；SRF（RPONTTLD）日期為 2026-08-14，與利差不同日。

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation｜S&P 500 P/E and Shiller CAPE | multpl / gurufocus [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation｜Mag 7 weighted P/E and AI leader P/S | Fool / SSGA WebSearch；AI leader P/S vs 10 年均值未取得 | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation｜Analyst TP upgrade decomposition | 賣方研報 WebSearch（90d＋同季）；唯一命中 Susquehanna TSMC $575→$600，不在指定 top-tier 名單內，且無 EPS／PE 拆解 | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) YTD divergence | 24/7 Wall St WebSearch；只找到 2026-06-10 的過期 YTD 值，沒有當期快照 | ⛔ FETCH FAILED |
| breadth.top10_concentration | Breadth｜Top-10 concentration in S&P 500 | RBC / 財經媒體 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth｜Advance/decline ratio, new high/low ratio | Investing.com breadth WebSearch；以 >50DMA 比例作代理，A/D 與 NH/NL 比率本身未取得 | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment｜Margin Debt: FINRA monthly data | FINRA / Advisor Perspectives WebSearch（stock-of-state，沿用 6 月資料；market cap 比率未計算） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment｜Social sentiment proxies | WSB / cashtag WebSearch（7d），完成但無顯著討論 | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment｜NAAIM Exposure Index | naaim / YCharts [primary: SEARCH]，無當週值 | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch；BofA 8 月取得，JPM 未取得 | ✓ SEARCH-VERIFIED |
| monetary.fed_funds | Monetary & Credit｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit｜High Yield OAS | scripts/fetch_macro.py（FRED BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit｜Investment Grade OAS | scripts/fetch_macro.py（FRED BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit｜10Y Treasury yield | scripts/fetch_macro.py（FRED DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit｜10Y breakeven inflation rate | scripts/fetch_macro.py（FRED T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit｜WTI crude oil price | scripts/fetch_macro.py（FRED DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit｜5y5y forward inflation expectation | scripts/fetch_macro.py（FRED T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit｜美債標售需求（auction tail / bid-to-cover） | Reuters / RTTNews recap [primary: SEARCH]（14d）；URL 標題與 30Y 描述不一致 | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | Monetary & Credit｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit｜PBoC aggregate financing / liquidity operations | investing / Yicai WebSearch，無當期英文摘要 | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | Monetary & Credit｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]（30d），無合格披露 | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals｜Hyperscaler capex guidance | 季報 WebSearch（stock-of-state，2026 Q2 財報季）；個別公司數值未取得 | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals｜AI token volume growth rate | Anthropic / OpenAI / Google WebSearch，當季無披露 | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals｜OpenAI / Anthropic annualized revenue | VentureBeat 等 WebSearch；最新為 2026-05-29（前一季），且數值與來源標題不一致 | ✗ NOT DISCLOSED |
| ai.customer_concentration_rpo | AI Fundamentals｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals｜AI compute supply/demand and overcapacity risk | TrendForce / jarvislabs [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報／發債 [primary: SEARCH]；quarterly_state＝Sage Advisory，event_scan（30d）＝Meta El Paso 表外融資 | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI Fundamentals｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 [primary: SEARCH]（stock-of-state，沿用 2026-06-15 組合值） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K / 10-Q [primary: SEARCH]（30d），無變動披露 | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals｜資本週期階段（capital cycle stage） | 供需增速＋進出場事件 WebSearch；兩個 component 都完成但無可用披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior｜Search for past 7 days: AI rename / SPAC | Reuters / Benzinga / SEC WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior｜IPO market heat | IPOScoop / Renaissance WebSearch；首日報酬與無營收占比未取得 | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior｜Microcap thematic moonshots | Finviz / StockAnalysis gainers [primary: SEARCH]（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior｜Upcoming AI IPOs | S-1 / 具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior｜Insider selling at AI / market-leadership companies | SEC EDGAR / openinsider / secform4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior｜Cboe equity-only put/call ratio | Cboe / thetrading.tools [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage｜US leveraged ETF AUM | etf.com / cryptobriefing [primary: SEARCH]；個別 ticker AUM 未取得 | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage｜US single-stock leveraged ETF approvals | Leverage Shares / Tradr 發行公告 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | Structural Leverage｜Global leveraged product approvals | KRX / TWSE / JPX / ESMA WebSearch（7d），無英文披露 | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage｜0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage｜Options total volume: OCC monthly volume report | theocc.com WebSearch（6 月資料） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage｜Cross-asset derivatives / correlation checks | Cboe WebSearch；stock-bond correlation 未取得 | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage｜Cross-reference only: FINRA margin debt | 交叉引用 Retail Sentiment margin debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo，aggregation any）；WebSearch 無額外 unwind 披露 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.8、CAPE 42.2（原定來源 multpl / gurufocus） | S&P 500 trailing P/E Shiller CAPE multpl August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 約 29x vs 指數約 25.6x | Magnificent 7 weighted PE vs S&P 500 August 2026 | https://www.fool.com/research/magnificent-seven-sp-500/（Motley Fool） | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 約 855bp、貸款利差 +100–125bp、Oracle CDS 多年高 | CoreWeave Oracle CDS spread AI credit widening August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm（Tech Times） | 2026-08-03 | 2026-08-17T09:30:00+08:00 |
| breadth.top10_concentration | Top-10 集中度約 37% | S&P 500 top 10 concentration percent 2026 | https://www.rbcwealthmanagement.com/en-us/insights/the-great-narrowing-sp-500-concentration（RBC Wealth Management） | 2026-07-24 | 2026-08-17T09:30:00+08:00 |
| breadth.advance_decline | 約 71.6% 成分股 >50DMA | S&P 500 percent above 50 day moving average August 2026 | https://www.investing.com/indices/s-p-500-stocks-above-50-day-average（Investing.com） | 2026-08-11 | 2026-08-17T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 65（原定來源 cnn.com） | CNN Fear and Greed Index August 14 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| retail.margin_debt | FINRA 6 月 margin debt $1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives） | 2026-07-20 | 2026-08-17T09:30:00+08:00 |
| retail.aaii | AAII 38.5／23.3／38.1 | AAII investor sentiment survey week August 12 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA 8 月 FMS 現金 3.9% | BofA Global Fund Manager Survey August 2026 cash levels | https://www.tradingview.com/news/macenews:d7660a8e2094b:0-bofa-global-research-fund-manager-survey-global-investors-increasingly-more-cautious-about-growth-and-inflation-in-august/（MNI via TradingView） | 2026-08-12 | 2026-08-17T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 標售 BTC 2.39、5.216%、indirect 66.8%（URL 標題為 10 年期） | US Treasury 30 year bond auction August 13 2026 bid to cover | https://www.rttnews.com/3679611/ten-year-note-auction-attracts-modestly-above-average-demand.aspx（RTTNews） | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.fedwatch | 9/16 維持不變約 69%（原定來源 CME FedWatch） | CME FedWatch September 2026 rate probability | https://growbeansprout.com/tools/fedwatch（Beansprout FedWatch tool） | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計約 $725B、仍上修 | hyperscaler capex 2026 725 billion raised Q2 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-08-17T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO 約 $678B、約 32% 繫於 OpenAI | Microsoft RPO backlog 678 billion OpenAI 2026 | https://www.benzinga.com/trading-ideas/long-ideas/26/07/60816147/microsofts-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer（Benzinga） | 2026-07-30 | 2026-08-17T09:30:00+08:00 |
| ai.compute_supply_demand | HBM 合約約 +40%、H200 約 $3.99/hr、Blackwell 售罄 | H200 GPU rental HBM DRAM 2026 shortage Blackwell | https://jarvislabs.ai/blog/h200-price（JarvisLabs） | 2026-08-01 | 2026-08-17T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 超越 FCF、2026 發債約 $182B | hyperscaler capex FCF debt issuance 182 billion 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure（Sage Advisory） | 2026-07-24 | 2026-08-17T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan][spv_deal] Meta El Paso 資料中心 BlackRock 主導超過 $12B 債券，表外結構 sponsor_equity_split=undisclosed;residual_value_guarantee=undisclosed;lease_term=20-30yr;debt_tenor=undisclosed;lead_lenders=BlackRock/JPMorgan/MS; | BlackRock 12 billion bond Meta El Paso data center | https://www.landgate.com/news/blackrock-s-12-billion-bond-sale-signals-a-new-financing-playbook-for-data-center-developers（Landgate） | 2026-07-20 | 2026-08-17T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $72B vs 年化 capex 約 $725B（top-4＋Oracle） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-06-15 | 2026-08-17T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收 IPO 合格事件 0 件 | AI rename ticker SPAC no revenue IPO August 10-17 2026 | Reuters／Benzinga／SEC EDGAR 篩選 | — | 2026-08-17T09:30:00+08:00 |
| speculation.ipo_heat | 2026-08-17 起當週約 11 檔、YTD 226 檔 | US IPO pricings week August 2026 IPOScoop | https://www.iposcoop.com/current-year-pricings/（IPOScoop） | 2026-08-17 | 2026-08-17T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot 合格 0 件 | microcap 100% single day quantum fusion nuclear AI August 2026 | Finviz／StockAnalysis gainers 篩選 | — | 2026-08-17T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 9 月上市，約 $730–850B；Anthropic 續進 | OpenAI Anthropic IPO timing valuation 2026 | https://cryptobriefing.com/openai-ipo-filing-trillion-valuation/（Crypto Briefing） | 2026-07-28 | 2026-08-17T09:30:00+08:00 |
| speculation.insider_form4 | 過去 14 日 AI／領導股合格 Form 4 賣壓 cluster 0 件 | AI leadership insider Form 4 sale August 3-17 2026 SEC | openinsider／secform4／SEC EDGAR 篩選 | — | 2026-08-17T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.54 | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio（thetrading.tools） | 2026-08-07 | 2026-08-17T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF AUM 約 $198B | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing） | 2026-07-23 | 2026-08-17T09:30:00+08:00 |
| structural.us_single_stock_etf | 2026-08-11 新發單股 2x 槓桿 ETF（結果稱 6 檔，URL 標題列 3 檔） | single-stock leveraged ETF launch August 11 2026 Leverage Shares Tradr | https://www.globenewswire.com/news-release/2026/08/11/3342794/0/en/leverage-shares-by-themes-launches-three-new-2x-etfs-targeting-ai-infrastructure-and-connectivity-leaders.html（GlobeNewswire） | 2026-08-11 | 2026-08-17T09:30:00+08:00 |
| structural.zero_dte | 0DTE 約占 SPX 期權量 65% | 0DTE SPX options share Cboe Q2 2026 65% | https://ca.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4768656（Investing.com） | 2026-07-31 | 2026-08-17T09:30:00+08:00 |
| structural.options_volume | OCC 6 月總量約 16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-08-17T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 約 135、VIX 14.63、MOVE 約 75 | VIX SKEW MOVE bond volatility August 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-10-2026-spx-skew-collapses-on-upside-chasing（Cboe） | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt $1.502T、+51.5% YoY（交叉確認） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives） | 2026-07-20 | 2026-08-17T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B 貸款利差 +100–125bp＋covenant、5Y CDS 約 855bp | CoreWeave 2.6 billion loan spread covenant CDS August 2026 | https://www.stocktitan.net/news/CRWV/core-weave-closes-2-6-billion-loan-facility-expanding-financing-gwhngwnf0jt5.html（StockTitan） | 2026-07-29 | 2026-08-17T09:30:00+08:00 |

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

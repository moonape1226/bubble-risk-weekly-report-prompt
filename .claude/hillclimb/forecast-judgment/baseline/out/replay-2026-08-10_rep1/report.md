> [DRY RUN] this report was not committed to archive.

# 2026-08-10 AI 泡沫破裂預測報告
報告日期：2026-08-10｜ISO 週次：2026-W33｜預測窗口：2026-08-10 → 2027-02-08｜前次基準：report-2026-08-06（4天前）

## 結論

**結論：no**

三條路徑目前都離觸發很遠：NASDAQ-100 距 52 週高點回撤 3.06%，還要從最新收盤再跌約 22.63% 才會觸及 R1；四家 hyperscaler 2026 capex 合計約 $725B，而且仍在上修，沒有任何一家下修（R2 為 0/4）。R3 只見 CoreWeave 信用重定價（5Y CDS 約 855bp、$2.6B 貸款調高票息並加 covenant），但 HY OAS 2.71%、repo 資金壓力為 0bp，尚無違約或 distressed exchange 的傳導證據。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29722.3（2026-08-07）；252 個交易日最高收盤 30660.6（2026-06-02）；距 52 週高點回撤 3.06%。R1 門檻為 22995.45，要從最新收盤再跌約 22.63% 才會觸及（`valuation.ndx_drawdown`）。窗口內曾出現的最低點是 2026-07-29 的 27192.31，之後一路反彈，回到高點附近。

估值的脆弱度很高，但價格趨勢仍向上：S&P 500 7757.64（2026-08-07），比 200 日均線高 10.04%、比 52 週均線高 11.63%，自前次基準以來上漲 0.62%（`valuation.sp500_trend`）。trailing P/E 約 29.7、Shiller CAPE 約 42.2（2026-08-07，`valuation.sp500_pe_cape`）。FINRA 6 月 margin debt 為 $1.502T，YoY +51.5%，落在歷史頂部區間（`retail.margin_debt`）。

波動與情緒面目前沒有出現急跌前兆：VIX 14.9（2026-08-07），7 日變動 −6.82%，同期 S&P 500 +3.58%，未出現 crowded-optionality 式的同漲（`structural.vix_spx_comove`）。CNN Fear & Greed 約 64（Greed，`retail.fear_greed`）；AAII Bull 37.0%／Bear 38.0%（2026-08-06，`retail.aaii`），都不是極端亢奮讀數。

利率面：DGS10 4.69%、DFII10 2.43%（2026-08-06，自前次基準無新觀測，持平），T10YIE 2.25%（2026-08-07，−1bp）。本週 10Y Δ 分解：ΔDGS10 0bp、ΔDFII10 0bp、ΔT10YIE −1bp，判讀為不可判（視窗不一致）；DGS10 與 DFII10 為 stale series（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。

**判讀：** R1 距離觸發很遠。窗口內要觸發，需要一次約 23% 的指數級急跌，通常得有外生催化：信用事件外溢（R3→R1）、hyperscaler 財報季引發 capex／ROI 重估，或利率端衝擊。高 CAPE 與 margin debt YoY +51.5% 會放大下跌幅度，但目前沒有證據顯示急跌已經開始。

### R2 資本支出收縮

- Microsoft、Alphabet、Amazon、Meta：檢索結果只有四家 2026 capex 合計約 $725B 且「仍上修」（CNBC，2026-07-28，Q2 財報季，`ai.hyperscaler_capex`），沒有個別列出逐家的指引數字。逐家方向因此只能記為：未取得逐家數字，但無任何一家下修的報導。同一篇報導的標題顯示 Alphabet 財報後 capex 受到更多審視，不過這是市場反應，不是指引下修。
- 已下修家數：0/4。
- 下一次財報：確切日期不在本次證據中。按季度節奏推算，窗口（至 2027-02-08）內應涵蓋兩次 hyperscaler 財報。
- 相關佐證：GPU／記憶體供給仍偏緊。HBM／DRAM 合約價續升、H200 租金中位約 $4.39/hr，缺口預期延續到 1H2027（2026-08-01，`ai.compute_supply_demand`）。這屬於需求健康而非 order digestion 的讀數，短期內不利於 capex 下修。
- 反向壓力：AI 營收對 capex 缺口（revenue-to-capex gap）很大。年化 AI 終端營收約 $72B，年化 capex 約 $725B（分母：top-4＋Oracle；營收組件資料日 2026-06-15，屬沿用值，`ai.revenue_capex_gap`）。Microsoft 商用 RPO 約 $678B，其中約 32% 繫於單一客戶 OpenAI（2026-07-30，`ai.customer_concentration_rpo`）。本次只有單一供應商披露，無法加總跨供應商的同一 counterparty 承諾，所以不量化 backlog 重複計算風險（RPO double-counting）。

**判讀：** R2 目前沒有任何進展（0/4），最新方向是上修。窗口內要觸發，至少要有兩家在接下來的財報中下修指引。這通常需要股價重挫（R1→R2）、大客戶承諾違約（如 OpenAI 相關 RPO），或算力供給轉為過剩，而這三者目前都沒有證據。

### R3 AI 信用事件

- CoreWeave（最可能符合 R3 主業條件的借款人；其總負債是否達 50 億美元，不在本次證據中驗證）：5Y CDS 峰值約 855bp，已回落；報導標題稱其利差曾擴大 125 點，AI 貸款投資人開始要求 covenant（2026-08-03，`valuation.ai_credit_schism`）。CoreWeave 繫於 Anthropic 合約的 $2.6B 貸款調高票息約 100–125bp 並加上 covenant（Bloomberg，2026-07-29，`structural.ai_infrastructure_debt`）。
- Nebius：$775M 融資（同一來源，2026-07-29，`structural.ai_infrastructure_debt`），未見困境訊號。
- Oracle 5Y CDS 約 215bp；Q2 AI 相關 CDS 約 $650M（`valuation.ai_credit_schism`）。Oracle 不以 AI 資料中心為主業，不屬 R3 借款人，只作 AI 信用定價分歧（equity-vs-credit schism）的參考：信用端已開始重定價，但股權端（NASDAQ-100 回撤僅 3.06%）尚未跟進。
- 廣義信用環境寬鬆：HY OAS 2.71%、IG OAS 0.78%（2026-08-06，`monetary.hy_oas`、`monetary.ig_oas`）。repo 資金壓力（SOFR−IORB）：SOFR 3.65% 對 IORB 3.65%，利差 0bp，SOFR99 3.73%（皆 2026-08-06）。SRF 動用（RPONTTLD）為 0（2026-08-07，`monetary.repo_stress_srf`）。
- 本次證據沒有任何付款違約、covenant waiver、distressed exchange 或 going-concern 語句。

**判讀：** R3 有重定價跡象，但距違約仍遠。貸方用提高票息和加 covenant 的方式繼續提供資金，這代表融資管道仍開著，不是斷裂。窗口內要觸發，需要 CoreWeave 這類高槓桿 neocloud 失去再融資能力，或主要客戶合約出問題。CDS 約 855bp 是本次最接近 yes 的單一訊號，但它已從峰值回落。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 峰值約 855bp、利差曾擴大 125 點，$2.6B Anthropic 掛鉤貸款調高票息約 100–125bp 並加 covenant（2026-07-29 至 2026-08-03）。AI infrastructure debt financing 的定價已開始反映信用風險，這是 R3 先行指標，也可能外溢到 R1（`valuation.ai_credit_schism`、`structural.ai_infrastructure_debt`）。
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 $72B，年化 capex 約 $725B（分母：top-4＋Oracle），兩者約差 10 倍。ROI 一旦被重估，R1 與 R2 可能同時啟動（`ai.revenue_capex_gap`）。
- [R1] 槓桿與估值處於歷史頂部區：FINRA 6 月 margin debt $1.502T、YoY +51.5%（`retail.margin_debt`），Shiller CAPE 約 42.2（2026-08-07，`valuation.sp500_pe_cape`），US 槓桿 ETF 總 AUM 創記錄約 $198B（2026-07-23，`structural.leveraged_etf_aum`）。一旦觸發，強制去槓桿會放大回撤。
- [R2] 客戶集中度高：Microsoft 商用 RPO 約 $678B，約 32% 繫於 OpenAI（2026-07-30，`ai.customer_concentration_rpo`）。單一 counterparty 一旦出事，會同時衝擊 backlog 與 capex 計畫。
- [整體] 美債標售需求（auction tail / bid-to-cover）轉弱：5Y 連續 14 次 tail，bid-to-cover 為 2022-09 以來最差（2026-07-28，`monetary.treasury_auctions`）。10Y 期限溢價（term premium）0.8681%（Kim-Wright，2026-07-31，trailing 7 日 +3bp，`monetary.term_premium`）。財政供給壓力是潛在的利率衝擊來源。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 3.06%，最新收盤 29722.3 距 R1 門檻 22995.45 還差約 22.63%，且 7 月底低點後已反彈（`valuation.ndx_drawdown`）。
- [R2] hyperscaler 2026 capex 合計約 $725B 且仍上修，Q2 財報季沒有任何一家下修（2026-07-28，`ai.hyperscaler_capex`）。HBM／DRAM 合約價續升、H200 租金約 $4.39/hr、缺口延到 1H2027（2026-08-01，`ai.compute_supply_demand`），需求面不支持近期 capex 收縮。
- [R3] 廣義信用與資金面平靜：HY OAS 2.71%、IG OAS 0.78%（2026-08-06，`monetary.hy_oas`、`monetary.ig_oas`），SOFR−IORB 0bp，SRF 動用為 0（`monetary.repo_stress_srf`）。銀行對 NBFI 放款 2002.4852（十億美元，約 $2.00T，2026-07-29）持平（`structural.nbfi_bank_loans`）。CoreWeave 的利差上行仍被局部吸收，沒有外溢跡象。
- [R1] 廣度改善而不是窄化：RSP 等權 YTD +15.6%，領先 SPY 的 +13.5%（2026-08-07，`breadth.rsp_spy`）；約 64% 成分股站上 50DMA、A/D 線創高（2026-08-03，`breadth.advance_decline`）。Mag 7 對指數溢價接近十年低（約 29x vs 約 25.6x，`valuation.mag7_multiples`），集中度風險比估值表面看起來低。
- [整體] 美債市場槓桿沒有失序跡象：MOVE 72.03（2026-08-07，較前次 −4.09）；CFTC 槓桿基金美債期貨淨部位 −7423067 口（2026-08-04，4 週變動 +149977，空頭小幅回補）；OFR tri-party repo transaction volume $2309.0bn（2026-08-07，`structural.treasury_basis_trade`）。美債基差交易槓桿（Treasury basis-trade leverage）未見平倉壓力。
- [R1] 波動與情緒未達極端：VIX 14.9，7 日 −6.82%，未與指數同漲（`structural.vix_spx_comove`）；CNN Fear & Greed 約 64（`retail.fear_greed`）；Cboe equity put/call 0.55（2026-08-03，`speculation.equity_put_call`），略高於 0.50 的投機警戒線。

## 與前期比較

前次結論：無前次預測（report-2026-08-06 為舊格式評分報告）

前次是舊格式評分報告，不轉換為 yes／no；flip_evidence 為 []。自 2026-08-06 以來可觀測的變化如下：

- S&P 500 由 7709.96 升至 7757.64（+0.62%）；NASDAQ-100 由 29373.33 升至 29722.3，回撤收斂。
- VIX 由 15.15 降至 14.9；MOVE 由 76.12 降至 72.03；OFR tri-party repo transaction volume −2.03%。
- T10YIE 與 T5YIFR 各 −1bp；DGS10、DFII10、HY／IG OAS 無新觀測（持平）。
- 本次新增的信用面重點是 CoreWeave 的 CDS 與貸款重定價（2026-07-29 至 2026-08-03 資料）。它強化了 R3 的觀察，但沒有改變 no 的判斷。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED 與 0 件 來源（均不改變答案）：

- `retail.social_sentiment`、`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.pboc`、`ai.token_growth`、`ai.depreciation_life`、`structural.global_leveraged_approvals`：搜尋完成，但窗口內無合格披露。這些都是情緒／背景類輔助來源，補上也不會改變三條路徑的距離。
- `monetary.private_credit_liquidity`：過去 30 日沒有 redemption-request ratio、gate proration / breach 或 net inflow→outflow flip 的新披露。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）是 R3 的潛在傳導通道，若出現多基金 gate proration / breach，可能推向 yes，本次無法確認。
- `ai.openai_anthropic_revenue`：最近一筆 run-rate（Anthropic 約 $47B、OpenAI 約 $25B）資料日為 2026-06-15，屬上一季，不符合「當季披露」，所以不作新證據。`ai.revenue_capex_gap` 的分子沿用該組件並標註資料日期。
- `ai.hyperscaler_financing_mix`：quarterly_state 已取得（top-5 capex 超越 FCF、表外 SPV 超過 $120B、2026 發債規模約 $182B，2026-07-24），但 30 日 event_scan 沒有新的 hyperscaler 融資事件，依 all 聚合規則記為 ✗ NOT DISCLOSED。hyperscaler 融資結構（capex vs FCF / 發債）的表外部分與 R3 相關，下次若有新 SPV 交易需重新檢視。
- `ai.capital_cycle`：供需增速證據不足，本次不判定資本週期階段（capital cycle stage）；30 日內也無取消／延後事件。
- `speculation.insider_form4`：0 件。檢索到的 Form 4 摘要來自第三方聚合頁，缺 SEC EDGAR filing URL 與 filing date，不符合合格條件，因此不列名、不列金額。
- `speculation.ai_rename_spac`、`speculation.microcap_moonshots`：過去 7 日合格事件 0 件。
- `structural.us_single_stock_etf`：0 件。唯一命中的 Leverage Shares 新單股槓桿 ETF 新聞稿，URL 日期為 2026-07-07（在 30 日窗外），與搜尋摘要所列的 2026-07-30 不一致；ELOL 的發行日也沒有獨立來源。日期有歧義，只作背景。
- `structural.zero_dte` 的資料日為 2026-05-31（Cboe Q2 簡報），較舊，只作背景。

最大的不確定性：

1. 下一輪 hyperscaler 財報（確切日期不在本次證據中，窗口內預計有兩次）：只要兩家下修 capex 即觸發 R2，偏向 yes；若持續上修則維持 no。
2. CoreWeave 等 neocloud 的再融資：CDS 約 855bp 與貸款加 covenant 顯示貸方態度轉趨保守。若後續融資失敗或主要客戶合約出問題，R3 可能啟動並外溢到 R1，偏向 yes。
3. 美債標售需求與 10Y 期限溢價：5Y 連續 tail 若擴大為國債市場失序（Treasury market dysfunction），會成為 R1 的外生催化，偏向 yes；目前 MOVE 與 repo 資金壓力仍平靜。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 29.7 | https://www.multpl.com/s-p-500-pe-ratio | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE | 42.2 | https://www.multpl.com/shiller-pe | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E vs 指數 | 29x vs 25.6x（約） | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026 | 2026-07-20 | 2026-08-10T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標價（EPS-driven） | $285 → $288 | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044 | 2026-07-13 | 2026-08-10T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest | 7757.64 | FRED API (series_id=SP500) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 10.04 | FRED API (series_id=SP500) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 11.63 | FRED API (series_id=SP500) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（vs 前次基準） | 0.62 | FRED API (series_id=SP500) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29722.3 | FRED API (series_id=NASDAQ100) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-10T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 3.06 | FRED API (series_id=NASDAQ100) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 峰值（回落）／Oracle 5Y CDS | 855bp（約）／215bp（約） | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm | 2026-08-03 | 2026-08-10T09:30:00+08:00 |
| breadth.rsp_spy | RSP vs SPY YTD 總報酬 | +15.6% vs +13.5% | https://www.benzinga.com/etfs/sector-etfs/26/08/60862370/rsp-etf-is-beating-voo-spy-as-sp-500-equal-weight-fund-nears-100-billion-milestone | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 | 36.4% | https://www.rbcwealthmanagement.com/en-us/insights/the-great-narrowing-sp-500-concentration | 2026-07-24 | 2026-08-10T09:30:00+08:00 |
| breadth.advance_decline | S&P 500 成分股 >50DMA 比例 | 64%（約） | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/ | 2026-08-03 | 2026-08-10T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed | 64（約，Greed） | https://www.cnn.com/markets/fear-and-greed | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-06 月資料）／YoY | $1.502T／+51.5% | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-10T09:30:00+08:00 |
| retail.aaii | AAII Bull／Neutral／Bear | 37.0%／25.0%／38.0% | https://www.aaii.com/sentimentsurvey | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1） | 45.76080873390133（約 45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-10T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-09 | 2026-08-10T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-09 | 2026-08-10T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.71 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.69 | FRED API (series_id=DGS10) | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.43 | FRED API (series_id=DFII10) | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.25 | FRED API (series_id=T10YIE) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 81.96 | FRED API (series_id=DCOILWTICO) | 2026-08-03 | 2026-08-10T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-08-10T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.28 | FRED API (series_id=T5YIFR) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8681 | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-10T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 日） | 3.0 | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-10T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.65 | FRED API (series_id=SOFR) | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.73 | FRED API (series_id=SOFR99) | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-08-10 | 2026-08-10T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| monetary.treasury_auctions | 5Y 標售連續 tail 次數 | 14 次（bid-to-cover 為 2022-09 以來最差） | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026 | 2026-07-28 | 2026-08-10T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 9/16 一次動作 | 62%（約，方向分歧） | https://growbeansprout.com/tools/fedwatch | 2026-08-10 | 2026-08-10T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6748567.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-05 | 2026-08-10T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5941248.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-31 | 2026-08-10T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-10T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計（仍上修） | $725B（約） | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-07-28 | 2026-08-10T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft 商用 RPO／OpenAI 佔比 | $678B／32%（約） | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/ | 2026-07-30 | 2026-08-10T09:30:00+08:00 |
| ai.compute_supply_demand | H200 租金中位 | $4.39/hr（約，HBM 缺口延至 1H2027） | https://jarvislabs.ai/blog/h200-price | 2026-08-01 | 2026-08-10T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 vs 年化 capex（top-4＋Oracle） | $72B vs $725B（約） | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-06-15 | 2026-08-10T09:30:00+08:00 |
| speculation.ipo_heat | APMD 首日漲幅／JMKE 募資 | +56%／$1B | https://seekingalpha.com/article/4710009-us-ipo-weekly-recap-august-kicks-off-with-one-small-pricing | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI IPO 目標估值 | $1T（約） | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground | 2026-07-28 | 2026-08-10T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity-only put/call（日／5 日均未標明） | 0.55 | https://ycharts.com/indicators/cboe_equity_put_call_ratio | 2026-08-03 | 2026-08-10T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM（記錄高） | $198B（約） | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-07-23 | 2026-08-10T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量（Cboe Q2） | 65%（約） | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641 | 2026-05-31 | 2026-08-10T09:30:00+08:00 |
| structural.options_volume | OCC 總量（2026-06 月資料） | 1,603,491,559 口 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report | 2026-07-02 | 2026-08-10T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW／VIX（contango） | 140／16（約） | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 14.9 | FRED API (series_id=VIXCLS) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 14.9 | scripts/fetch_macro.py vix_spx_comove block（FRED） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（base 2026-07-31，7 日） | -6.82 | scripts/fetch_macro.py vix_spx_comove block（FRED） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（base 2026-07-31，7 日） | 3.58 | scripts/fetch_macro.py vix_spx_comove block（FRED） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-06 月資料，交叉引用）／YoY | $1.502T／+51.5% | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-10T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B Anthropic 掛鉤貸款票息調升 | +100–125bp | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic | 2026-07-29 | 2026-08-10T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Nebius 融資 | $775M | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic | 2026-07-29 | 2026-08-10T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2002.4852（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-29 | 2026-08-10T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約合計，口） | -7423067 | CFTC TFF futures-only（scripts/fetch_macro.py） | 2026-08-04 | 2026-08-10T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | 149977 | CFTC TFF futures-only（scripts/fetch_macro.py） | 2026-08-04 | 2026-08-10T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 72.03 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index delta_abs | -4.09 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2309.0 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | SSGA 等 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報摘要 [primary: SEARCH]（90d＋同季） | ✓ SEARCH-VERIFIED（MS NVDA 2026-07-13；EPS／PE Δ 未披露，僅標 EPS-driven） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧 | 信用市場 WebSearch [primary: SEARCH]（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | Benzinga WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | RBC WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | StockCharts WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | Advisor Perspectives WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／YCharts [primary: SEARCH] | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（repo_stress block） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | 標售 recap WebSearch [primary: SEARCH]（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | PBoC／NBS 英文摘要 WebSearch | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC／interval fund 披露 [primary: SEARCH]（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報／財經媒體 WebSearch（stock-of-state，Q2 財報季） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／具名報導 WebSearch（需當季披露） | ✗ NOT DISCLOSED（最近披露 2026-06-15 屬上季） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話／媒體 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce／GPU 租金 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：Sage Advisory WebSearch；event_scan：30 日 hyperscaler 發債／SPV 掃描 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 [primary: SEARCH]（沿用組件逐一標日） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K／10-Q／法說 [primary: SEARCH]（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | quarterly_state：供需增速 proxies；event_scan：30 日進出場事件 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | Reuters／Benzinga／IPOX SPAC 螢幕 WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | Renaissance／Seeking Alpha WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／StockAnalysis／StockTitan 螢幕 [primary: SEARCH]（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 [primary: SEC EDGAR]（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | YCharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com／媒體 [primary: SEARCH] | ✓ SEARCH-VERIFIED（總量；個別 NVDL／TSLL 等未取得） |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com／GlobeNewswire（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA／ETFGI（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe insights WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove block） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用散戶 margin debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | Bloomberg 等 [primary: SEARCH]（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）；WebSearch 平倉新聞 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok；WebSearch 平倉事件：無合格披露） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.7（原定來源 multpl） | S&P 500 trailing P/E CAPE August 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio（multpl） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.2（原定來源 multpl） | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 約 29x vs 指數約 25.6x，溢價近十年低 | Magnificent 7 valuation premium lowest decade 2026 | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026（SSGA） | 2026-07-20 | 2026-08-10T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA $285→$288，EPS-driven | Morgan Stanley NVDA target 288 July 2026 AI demand | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044（Investing.com） | 2026-07-13 | 2026-08-10T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 約 855bp（回落）、Oracle CDS 約 215bp、Q2 AI-linked CDS 約 $650M | CoreWeave CDS Oracle spread AI credit August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm（Tech Times） | 2026-08-03 | 2026-08-10T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD +15.6% vs SPY +13.5% | RSP vs SPY equal weight YTD August 2026 concentration | https://www.benzinga.com/etfs/sector-etfs/26/08/60862370/rsp-etf-is-beating-voo-spy-as-sp-500-equal-weight-fund-nears-100-billion-milestone（Benzinga） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| breadth.top10_concentration | Top-10 集中度 36.4% | S&P 500 top 10 concentration percent August 2026 | https://www.rbcwealthmanagement.com/en-us/insights/the-great-narrowing-sp-500-concentration（RBC Wealth Management） | 2026-07-24 | 2026-08-10T09:30:00+08:00 |
| breadth.advance_decline | 約 64% 成分股 >50DMA、A/D 創高、McClellan 動能轉緩 | S&P 500 breadth percent above 50 day moving average August 2026 | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/（StockCharts） | 2026-08-03 | 2026-08-10T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 64（Greed） | CNN Fear and Greed Index August 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| retail.margin_debt | FINRA 2026-06 margin debt $1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives；原定 FINRA） | 2026-07-20 | 2026-08-10T09:30:00+08:00 |
| retail.aaii | AAII Bull 37.0%／Neutral 25.0%／Bear 38.0% | AAII investor sentiment survey week August 6 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.treasury_auctions | 5Y 連 14 次 tail、bid-to-cover 為 2022-09 以來最差；7Y tail 0.8bp | US Treasury 5 year 7 year auction tail bid to cover July 2026 | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026（TFTC；原定 Reuters／Bloomberg recap） | 2026-07-28 | 2026-08-10T09:30:00+08:00 |
| monetary.fedwatch | 9/16 FOMC 約 62% 一次動作、方向分歧 | CME FedWatch September 2026 probability Fed | https://growbeansprout.com/tools/fedwatch（Beansprout；原定 CME FedWatch） | 2026-08-10 | 2026-08-10T09:30:00+08:00 |
| ai.hyperscaler_capex | 2026 hyperscaler capex 合計約 $725B、仍上修（Q2 財報季） | hyperscaler capex 2026 725B raised Q2 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-08-10T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO 約 $678B、約 32% 繫於 OpenAI | Microsoft RPO backlog 678 billion OpenAI 2026 | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/（Benzinga via TradingView） | 2026-07-30 | 2026-08-10T09:30:00+08:00 |
| ai.compute_supply_demand | HBM／DRAM 合約續升、H200 租金約 $4.39/hr、缺口延至 1H2027 | H200 GPU rental HBM DRAM 2026 shortage 2027 | https://jarvislabs.ai/blog/h200-price（JarvisLabs） | 2026-08-01 | 2026-08-10T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 超越 FCF、表外 SPV 超過 $120B、2026 發債規模約 $182B | hyperscaler capex FCF debt issuance 182 billion off balance sheet SPV 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure（Sage Advisory） | 2026-07-24 | 2026-08-10T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $72B（Anthropic 約 $47B＋OpenAI 約 $25B，2026-06-15 沿用）vs 年化 capex 約 $725B（top-4＋Oracle） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI）；分母見 ai.hyperscaler_capex | 2026-06-15 | 2026-08-10T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收投機 IPO：合格 0 件 | AI rename ticker SPAC no revenue IPO August 3-10 2026 | Reuters／Benzinga／IPOX SPAC 螢幕 | 2026-08-10 | 2026-08-10T09:30:00+08:00 |
| speculation.ipo_heat | APMD 首日 +56%、JMKE $1B 收平、IOND $3.1B 直接上市 | US IPO pricings week August 2026 Renaissance Apnimed | https://seekingalpha.com/article/4710009-us-ipo-weekly-recap-august-kicks-off-with-one-small-pricing（Seeking Alpha；原定 Renaissance） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot：合格 0 件 | microcap 100% single day quantum fusion nuclear space AI August 2026 | Finviz／StockAnalysis／StockTitan gainers 螢幕 | 2026-08-10 | 2026-08-10T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標約 $1T IPO、Anthropic 續進 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground（Benzinga） | 2026-07-28 | 2026-08-10T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 合格 0 件（命中結果只有第三方聚合頁，缺 EDGAR filing URL／filing date） | Snowflake Tempus AI Form 4 insider sale July August 2026 SEC | SEC EDGAR Form 4 檢索；StockTitan 聚合頁（非 EDGAR） | — | 2026-08-10T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.55 | Cboe equity put call ratio August 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio（YCharts；原定 Cboe） | 2026-08-03 | 2026-08-10T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 記錄高約 $198B | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing；原定 etf.com） | 2026-07-23 | 2026-08-10T09:30:00+08:00 |
| structural.us_single_stock_etf | 單股槓桿 ETF 核准／發行：合格 0 件（唯一命中的新聞稿 URL 日期 2026-07-07 在窗外，與所列日期不一致） | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | SEC EDGAR ETF filings／ETF.com／GlobeNewswire | — | 2026-08-10T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量約 65%（Cboe Q2 2026） | 0DTE SPX options share Cboe Q2 2026 65% | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641（Investing.com；原定 Cboe） | 2026-05-31 | 2026-08-10T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 總量 1,603,491,559 口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-08-10T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 約 140、VIX 約 16 contango、債市波動偏高 | VIX SKEW bond volatility MOVE August 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher（Cboe） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt $1.502T、YoY +51.5%（交叉引用） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives） | 2026-07-20 | 2026-08-10T09:30:00+08:00 |
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
  "r1_drawdown_pct": 3.06,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

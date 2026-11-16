> [DRY RUN] this report was not committed to archive.

# 2026-08-10 AI 泡沫破裂預測報告
報告日期：2026-08-10｜ISO 週次：2026-W33｜預測窗口：2026-08-10 → 2027-02-08｜前次基準：report-2026-08-06（4天前）

## 結論

**結論：no**

三條路徑都離觸發很遠：NASDAQ-100 距 52 週高點回撤 3.06%，要再跌約 22.63% 才觸及 R1；hyperscaler 2026 capex 合計 ≈$725B 仍在上修、四家中無一下修（R2）。R3 端 CoreWeave 信用定價明顯承壓（5Y CDS ≈855bp、$2.6B 貸款被迫加價並加 covenant），但仍是重定價而非違約，且 HY OAS 2.71%／repo 資金壓力為零顯示整體信用與融資環境寬鬆，不足以在 182 天內推翻低基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

FRED `NASDAQ100` 最新收盤 29,722.30（2026-08-07），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 3.06%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，自最新收盤還需再跌約 22.63% 才會觸及。7 月底曾短暫回落至 27,192.31（2026-07-29），隨後一週內強彈回 29,700 附近。

脆弱度面：S&P 500 7,757.64（2026-08-07）高於 200 日均線 10.04%、高於 52 週均線 11.63%（`valuation.sp500_trend`）；Shiller CAPE ≈42.2、trailing P/E ≈29.7（`valuation.sp500_pe_cape`）；FINRA 6 月 margin debt $1.502T、YoY +51.5%，已落在歷史頂部附近常見的 +40–50% 區間之上（`retail.margin_debt`）。催化面：VIX 14.9、7 日內 VIX −6.82% 而 S&P 500 +3.58%，co-movement 未觸發（`structural.vix_spx_comove`）；CNN Fear & Greed ≈64（Greed，`retail.fear_greed`）；RSP 等權 YTD +15.6% 領先 SPY +13.5%，漲勢擴散而非更集中（`breadth.rsp_spy`）。

**判讀：** R1 距離很遠——估值與槓桿顯示一旦下跌幅度會很大，但目前沒有資金面或信用面的傳導跡象；需要 R3 型信用事件、hyperscaler 季報引發的 capex／ROI 重估，或利率端（10Y 期限溢價持續上行、美債標售需求轉弱）衝擊，才可能在窗口內產生 25% 級回撤。

### R2 資本支出收縮

本次證據為 CNBC 2026-07-28 對 Q2 財報季的彙整：Microsoft、Alphabet、Amazon、Meta（連同同業）2026 capex 合計 ≈$725B，方向仍為上修（`ai.hyperscaler_capex`）。

- Microsoft：最新指引來自 2026 Q2 財報季（2026-07 下旬）；本次證據未逐家揭露數字，合計口徑為上修，無下修報導。
- Alphabet：同上，2026 Q2 財報季；報導指其財報後市場對 capex 審視升溫，但未見下修。
- Amazon：同上，2026 Q2 財報季；未見下修。
- Meta：同上，2026 Q2 財報季；未見下修。

目前四家中下修家數為 0。需求側沒有走弱訊號：HBM／DRAM 合約價續升、H200 租金中位 ≈$4.39/hr、供給缺口延至 1H2027（`ai.compute_supply_demand`）；Microsoft 商用 RPO ≈$678B（`ai.customer_concentration_rpo`）。窗口（至 2027-02-08）涵蓋 2026 Q3 財報季與 2026 Q4／FY2027 指引季，具體日期本次證據未提供。

**判讀：** R2 距離很遠——要在兩次財報內出現兩家下修，需要需求斷層（大客戶違約或縮減承諾）或融資條件急劇收緊；Microsoft RPO 約 32% 繫於 OpenAI 是最明確的單點風險，但目前未見任何削減訊號。

### R3 AI 信用事件

AI 基礎設施信用是三條路徑中最有壓力的一條。CoreWeave 5Y CDS 曾擴大至 ≈855bp 後回落、Oracle 5Y CDS ≈215bp，Q2 AI-linked CDS 交易量 ≈$650M（`valuation.ai_credit_schism`，2026-08-03）。CoreWeave 一筆與 Anthropic 合約掛鉤的 $2.6B 貸款被迫調高收益率約 100–125bp 並加入 covenant，Nebius 另有 $775M 融資（`structural.ai_infrastructure_debt`，2026-07-29）。這是典型的「信用端先重定價」訊號：放款人開始要求更高補償與保護條款。

但距 R3 定義（破產申請、逾寬限期付款違約、或完成 distressed exchange）仍有距離：本次證據未見任何付款遲延、covenant waiver、distressed exchange 或 going-concern 字樣；CoreWeave 仍能在市場上完成再融資（只是更貴）。CoreWeave 的總負債規模與近期到期牆本次證據未提供，故無法量化再融資壓力。整體信用環境寬鬆：HY OAS 2.71%、IG OAS 0.78%（2026-08-06，`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 0bp、SOFR99−IORB 8bp、SRF 動用（Standing Repo Facility usage）0（`monetary.repo_stress_srf`）。

**判讀：** R3 是最可能先動的路徑，但目前停在「定價走闊、仍可融資」階段；要在窗口內觸發，需市場關閉 neocloud 再融資管道（例如大型 AI 客戶延遲付款或削減承諾），讓 CoreWeave 級借款人無法展延到期債務。HY 利差仍緊，這一傳導目前沒有跡象。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 曾擴大至 ≈855bp、$2.6B Anthropic 掛鉤貸款被迫加價約 100–125bp 並增設 covenant（2026-07-29／2026-08-03），顯示 AI 基礎設施信用已開始重定價（`valuation.ai_credit_schism`、`structural.ai_infrastructure_debt`）。
- [整體] FINRA 6 月 margin debt $1.502T、YoY +51.5%（2026-07-20），落在 1999／2007／2021 頂部附近常見的槓桿成長區間；一旦下跌易觸發強制去槓桿（`retail.margin_debt`）。
- [R1] Shiller CAPE ≈42.2、trailing P/E ≈29.7（2026-08-07），S&P 500 高於 200 日均線 10.04%（2026-08-07），估值與價格延伸都處於高檔，下跌時幅度可能很大（`valuation.sp500_pe_cape`、`valuation.sp500_trend`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收 ≈$72B vs 年化 capex ≈$725B（分母：top-4＋Oracle；營收組件資料日 2026-06-15），回本壓力巨大（`ai.revenue_capex_gap`）。
- [R2] Microsoft 商用 RPO ≈$678B，約 32% 繫於單一客戶 OpenAI（2026-07-30），backlog 集中度高，若該客戶縮減承諾將同時衝擊 R2 與 R3（`ai.customer_concentration_rpo`）。
- [整體] 美債標售需求（auction tail / bid-to-cover）：5Y 標售連續 14 次 tail、bid-to-cover 為 2022-09 以來最差（2026-07-28），10Y 期限溢價（term premium）0.8681%、trailing 7 日 +3bp（2026-07-31），財政供給壓力可能推高折現率（`monetary.treasury_auctions`、`monetary.term_premium`）。

## 支持 no 的證據

- [R1] NASDAQ-100 最新收盤 29,722.30（2026-08-07）僅距 52 週高點回撤 3.06%，距 R1 門檻 22,995.45 還差約 22.63%（`valuation.ndx_drawdown`）。
- [R2] hyperscaler 2026 capex 合計 ≈$725B 仍在上修（2026-07-28），四家中下修家數為 0，離「兩家下修」很遠（`ai.hyperscaler_capex`）。
- [R3] 整體信用與融資環境寬鬆：HY OAS 2.71%、IG OAS 0.78%（2026-08-06），repo 資金壓力（SOFR−IORB）0bp、SRF 動用 0（2026-08-06／2026-08-07），無傳導至廣義信用市場的跡象（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`）。
- [R2] 算力需求仍強：HBM／DRAM 合約價續升、H200 租金中位 ≈$4.39/hr、供給缺口延至 1H2027（2026-08-01），不支持近期 capex 下修（`ai.compute_supply_demand`）。
- [R1] 波動與廣度未示警：VIX 14.9（2026-08-07）、7 日內 VIX −6.82% 且 S&P 500 +3.58%，co-movement 未觸發；RSP 等權 YTD +15.6% 領先 SPY +13.5%（2026-08-07），漲勢擴散（`structural.vix_spx_comove`、`breadth.rsp_spy`）。
- [整體] 美債基差交易槓桿（Treasury basis-trade leverage）未見平倉：槓桿基金美債期貨淨部位 −7,423,067 口（2026-08-04）、4 週變動 +149,977 口，MOVE 72.03（2026-08-07）較前日回落，國債市場失序（Treasury market dysfunction）前兆不明顯（`structural.treasury_basis_trade`）。

## 與前期比較

前次結論：無前次預測（report-2026-08-06 為舊格式評分報告）

前次為舊格式評分報告，其分數不轉換為 yes／no，本次為新格式下的首個預測，flip_evidence 為 []。自 2026-08-06 以來的主要數據變化：

- S&P 500 由 7,709.96（2026-08-06）升至 7,757.64（2026-08-07），+0.62%；VIX 由 15.15 降至 14.9。
- MOVE 由 76.12 降至 72.03；OFR tri-party repo transaction volume 由 $2,356.8bn 降至 $2,309.0bn（−2.03%）。
- 10Y 殖利率分解：ΔDGS10 0bp、ΔDFII10 0bp、ΔT10YIE −1bp；判讀為 不可判（視窗不一致）——DGS10、DFII10 自前次以來無新觀測（stale_series），T10YIE 已更新，三腿視窗不一致，不推斷 driver。
- 其餘 HY／IG OAS、Fed funds、SOFR 等均無變動。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源檢索完成但無合格當期披露（✗ NOT DISCLOSED），或合格件數為 0：

- `retail.social_sentiment`、`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.pboc`、`ai.token_growth`、`ai.depreciation_life`、`structural.global_leveraged_approvals`：情緒／流動性／會計佐證類，缺漏不會改變答案。
- `monetary.private_credit_liquidity`：30 日內無 BDC 贖回壓力披露。這是 R3 傳導鏈的一環，若實際存在而未披露，可能低估 R3；但 HY OAS 仍緊，現階段不改變答案。
- `ai.openai_anthropic_revenue`：最新 run-rate（Epoch，2026-06-15）屬上一季，非當季披露，故標 NOT DISCLOSED；`ai.revenue_capex_gap` 依 carry-forward 規則沿用該組件並標註資料日。
- `ai.hyperscaler_financing_mix`：quarterly_state 可用（Sage Advisory 2026-07-24：top-5 capex 已超過 FCF、表外 SPV 存量 >$120B、2026 發債規模 ≈$182B），但 30 日 event_scan 無新交易，故整體標 NOT DISCLOSED，不作為本文證據。
- `ai.capital_cycle`：供需增速證據不足，本次不判定週期階段；30 日內無進出場事件。
- `speculation.insider_form4`：篩到的候選交易缺 SEC EDGAR filing URL，不符合合格條件，故記為 0 件且不列名。
- `structural.us_single_stock_etf`：唯一候選（Leverage Shares 新單股槓桿 ETF）的新聞稿 URL 顯示 2026-07-07 發布，早於 30 日窗口，日期不一致，記為 0 件。
- `structural.zero_dte`：最新可得數據為 Cboe 季度披露（資料日 2026-05-31），偏舊，僅作背景，未用作證據。

主要不確定性：

1. CoreWeave 等 neocloud 的總負債與到期牆未取得：若 2026 Q4–2027 Q1 有大額到期且再融資失敗，R3 可能在窗口內觸發，推向 yes。
2. 2026 Q3 財報季（窗口內）：若 Alphabet 或 Meta 因投資人對 ROI 的審視而首度下修 capex，R2 進度會明顯加快，推向 yes；反之續上修則強化 no。
3. 美債標售需求與 10Y 期限溢價：5Y 連續 tail 若演變成更長天期的標售失敗與期限溢價急升，可能透過折現率衝擊高估值科技股（R1），推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 29.7 | https://www.multpl.com/s-p-500-pe-ratio | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE | 42.2 | https://www.multpl.com/shiller-pe | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7757.64 | FRED API (series_id=SP500) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線偏離 %） | 10.04 | FRED API (series_id=SP500) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線偏離 %） | 11.63 | FRED API (series_id=SP500) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29722.3 | FRED API (series_id=NASDAQ100) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-10T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 3.06 | FRED API (series_id=NASDAQ100) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 峰值（回落）／Oracle 5Y CDS | 855bp／215bp | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm | 2026-08-03 | 2026-08-10T09:30:00+08:00 |
| breadth.rsp_spy | RSP 等權 vs SPY YTD 總報酬 | +15.6% vs +13.5% | https://www.benzinga.com/etfs/sector-etfs/26/08/60862370/rsp-etf-is-beating-voo-spy-as-sp-500-equal-weight-fund-nears-100-billion-milestone | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed | 64（Greed） | https://www.cnn.com/markets/fear-and-greed | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-06 月資料）／YoY | $1.502T／+51.5% | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-10T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q1，家計股權佔金融資產 %） | 45.76080873390133（≈45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-10T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標上限） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-09 | 2026-08-10T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標下限） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-09 | 2026-08-10T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.71 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.69 | FRED API (series_id=DGS10) | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.43 | FRED API (series_id=DFII10) | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.25 | FRED API (series_id=T10YIE) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 81.96 | FRED API (series_id=DCOILWTICO) | 2026-08-03 | 2026-08-10T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-08-10T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.28 | FRED API (series_id=T5YIFR) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8681 | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-10T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.65 | FRED API (series_id=SOFR) | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.73 | FRED API (series_id=SOFR99) | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-08-10 | 2026-08-10T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用 transaction volume） | 0.0（$0bn） | FRED API (series_id=RPONTTLD) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| monetary.treasury_auctions | 5Y 標售連續 tail 次數 | 14 | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026 | 2026-07-28 | 2026-08-10T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 9/16 一次動作機率 | 62% | https://growbeansprout.com/tools/fedwatch | 2026-08-10 | 2026-08-10T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6748567.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-05 | 2026-08-10T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5941248.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-31 | 2026-08-10T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-10T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計（2026 Q2 財報季，仍上修） | $725B | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-07-28 | 2026-08-10T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft 商用 RPO／OpenAI 佔比 | $678B／32% | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/ | 2026-07-30 | 2026-08-10T09:30:00+08:00 |
| ai.compute_supply_demand | H200 租金中位 | $4.39/hr | https://jarvislabs.ai/blog/h200-price | 2026-08-01 | 2026-08-10T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 vs 年化 capex（top-4＋Oracle） | $72B vs $725B | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-06-15 | 2026-08-10T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 14.9 | FRED API (series_id=VIXCLS) | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 14.9 | fetch_macro.py 衍生區塊（FRED SP500 + VIX） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日） | -6.82 | fetch_macro.py 衍生區塊（FRED SP500 + VIX） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日） | 3.58 | fetch_macro.py 衍生區塊（FRED SP500 + VIX） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave Anthropic 掛鉤貸款規模 | $2.6B（加價 100–125bp） | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic | 2026-07-29 | 2026-08-10T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2002.4852（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-29 | 2026-08-10T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7423067 | CFTC TFF（cftc_lev_funds） | 2026-08-04 | 2026-08-10T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 149977 | CFTC TFF（cftc_lev_funds） | 2026-08-04 | 2026-08-10T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 72.03 | Yahoo chart ^MOVE（move_index） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2309.0（$2.31T tri-party transaction volume） | OFR STFM REPO-TRIV1_TV_TOT-P（ofr_repo） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation／S&P 500 P/E and Shiller CAPE | multpl.com，WebSearch 主路徑 | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation／Mag 7 weighted P/E and AI leader P/S | SSGA 週評，WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation／Analyst TP upgrade decomposition | 賣方 TP 上調（90 日且同季），WebSearch | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | Valuation／S&P 500 price-trend deviation | fetch_macro.py sp500_trend 區塊（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation／NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown 區塊（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation／AI 信用定價分歧（equity-vs-credit schism） | 14 日信用市場掃描，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth／S&P 500 equal-weight (RSP) vs cap-weight (SPY) | Benzinga，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth／Top-10 concentration in S&P 500 | RBC Wealth Management，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth／Advance/decline ratio, new high/low ratio | StockCharts，WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment／CNN Fear & Greed Index | cnn.com，WebSearch 主路徑 | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment／Margin Debt: FINRA monthly data | FINRA via Advisor Perspectives，WebSearch | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment／Retail survey: AAII Investor Sentiment | aaii.com，WebSearch 主路徑 | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment／Social sentiment proxies | WSB／cashtag，WebSearch（7 日） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment／Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment／NAAIM Exposure Index | naaim.org／YCharts，WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment／BofA Fund Manager Survey and JPM institutional survey | 賣方調查，WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit／Fed funds rate: FRED series DFEDTARU and DFEDTARL | fetch_macro.py（DFEDTARU ok、DFEDTARL ok） | ✓ API |
| monetary.hy_oas | Monetary & Credit／High Yield OAS | fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit／Investment Grade OAS | fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit／10Y Treasury yield | fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit／10Y Treasury real yield / TIPS | fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit／10Y breakeven inflation rate | fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit／WTI crude oil price | fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit／CPI YoY: FRED series CPIAUCSL | fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit／5y5y forward inflation expectation | fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit／10Y 期限溢價（term premium）: FRED series THREEFYTP10 | fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit／repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） | ✓ API |
| monetary.treasury_auctions | Monetary & Credit／美債標售需求（auction tail / bid-to-cover） | 14 日標售回顧，WebSearch | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit／Fed funds rate path expectations | CME FedWatch 摘要，WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit／Fed balance sheet: FRED series WALCL | fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit／Global central bank liquidity cross-check | fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | Monetary & Credit／PBoC aggregate financing | investing／Yicai，WebSearch | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | Monetary & Credit／Private-credit / non-bank fund liquidity stress | BDC 披露（30 日），WebSearch | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals／Hyperscaler capex guidance | 2026 Q2 財報季彙整，WebSearch | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals／AI token volume growth rate | Anthropic／OpenAI／Google 披露，WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals／OpenAI / Anthropic annualized revenue | Epoch／報導，WebSearch；最新為上一季資料 | ✗ NOT DISCLOSED |
| ai.customer_concentration_rpo | AI Fundamentals／Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話會議摘要，WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals／AI compute supply/demand and overcapacity risk | jarvislabs／TrendForce，WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals／Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：Sage Advisory；event_scan：30 日發債掃描，WebSearch | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals／AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露（carry-forward），WebSearch | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals／GPU / 伺服器折舊年限變動 | 10-K／10-Q（30 日），WebSearch | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals／資本週期階段（capital cycle stage） | quarterly_state：供需增速；event_scan：30 日進出場事件，WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior／Search for past 7 days: AI rename / SPAC | Reuters／Benzinga／IPOX 篩選（7 日） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior／IPO market heat | Seeking Alpha／Renaissance 週報，WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior／Microcap thematic moonshots | Finviz／StockAnalysis／StockTitan 漲幅榜（7 日） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior／Upcoming AI IPOs | 具名報導（30 日），WebSearch | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior／Insider selling at AI / market-leadership companies | SEC EDGAR Form 4（14 日）；候選缺 EDGAR URL | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior／Cboe equity-only put/call ratio | YCharts，WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage／US leveraged ETF AUM | cryptobriefing／etf.com，WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage／US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com／GlobeNewswire（30 日） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage／Global leveraged product approvals | KRX／TWSE／JPX／ESMA（7 日），WebSearch | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage／0DTE option volume | Cboe 季度披露，WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage／Options total volume: OCC monthly volume report | theocc.com，WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage／Cross-asset derivatives / correlation checks | Cboe Insights，WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage／VIX / S&P 500 co-movement | fetch_macro.py（VIXCLS ok、vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage／Cross-reference only: FINRA margin debt | 交叉引用 Retail Sentiment margin debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage／AI infrastructure debt financing / vendor-financing loops | 30 日融資掃描，WebSearch | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage／Bank loans to nondepository financial institutions | fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage／美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok；aggregation any）；WebSearch 補充無合格事件 | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E ≈29.7（原定來源 multpl.com） | S&P 500 trailing P/E CAPE August 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE ≈42.2（原定來源 multpl.com） | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 ≈29x vs 指數 ≈25.6x，溢價近十年低 | Magnificent 7 valuation premium lowest decade 2026 | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026 （State Street） | 2026-07-20 | 2026-08-10T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA TP $285→$288，EPS-driven（EPS Δ／目標 PE Δ 未揭露） | Morgan Stanley NVDA target 288 July 2026 AI demand | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044 （Investing.com） | 2026-07-13 | 2026-08-10T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS ≈855bp（回落）、Oracle CDS ≈215bp、AI-linked CDS Q2 ≈$650M | CoreWeave CDS Oracle spread AI credit August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm （Tech Times） | 2026-08-03 | 2026-08-10T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD +15.6% vs SPY +13.5% | RSP vs SPY equal weight YTD August 2026 concentration | https://www.benzinga.com/etfs/sector-etfs/26/08/60862370/rsp-etf-is-beating-voo-spy-as-sp-500-equal-weight-fund-nears-100-billion-milestone （Benzinga） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 ≈37%（36.4%） | S&P 500 top 10 concentration percent August 2026 | https://www.rbcwealthmanagement.com/en-us/insights/the-great-narrowing-sp-500-concentration （RBC） | 2026-07-24 | 2026-08-10T09:30:00+08:00 |
| breadth.advance_decline | ≈64% 成分股在 50DMA 上、A/D 線創高、McClellan 動能轉緩 | S&P 500 breadth percent above 50 day moving average August 2026 | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/ （StockCharts） | 2026-08-03 | 2026-08-10T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed ≈64（Greed） | CNN Fear and Greed Index August 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives；原定來源 FINRA） | 2026-07-20 | 2026-08-10T09:30:00+08:00 |
| retail.aaii | AAII Bull 37.0%／Neutral 25.0%／Bear 38.0% | AAII investor sentiment survey week August 6 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-08-06 | 2026-08-10T09:30:00+08:00 |
| monetary.treasury_auctions | 5Y 連 14 次 tail、BTC 2022-09 以來最差；7Y tail 0.8bp | US Treasury 5 year 7 year auction tail bid to cover July 2026 | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026 （TFTC） | 2026-07-28 | 2026-08-10T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 9/16 會議 ≈62% 一次動作、方向分歧 | CME FedWatch September 2026 probability Fed | https://growbeansprout.com/tools/fedwatch （Beansprout，原定來源 CME FedWatch） | 2026-08-10 | 2026-08-10T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計 ≈$725B、仍上修（2026 Q2 財報季） | hyperscaler capex 2026 725B raised Q2 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-08-10T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO ≈$678B、≈32% 繫於 OpenAI | Microsoft RPO backlog 678 billion OpenAI 2026 | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/ （Benzinga via TradingView） | 2026-07-30 | 2026-08-10T09:30:00+08:00 |
| ai.compute_supply_demand | HBM／DRAM 合約續升、H200 租金 ≈$4.39/hr、缺口延至 1H2027 | H200 GPU rental HBM DRAM 2026 shortage 2027 | https://jarvislabs.ai/blog/h200-price （Jarvislabs） | 2026-08-01 | 2026-08-10T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 超越 FCF、表外存量 >$120B、2026 發債 ≈$182B | hyperscaler capex FCF debt issuance 182 billion off balance sheet SPV 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure （Sage Advisory） | 2026-07-24 | 2026-08-10T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 ≈$72B（Anthropic ≈$47B＋OpenAI ≈$25B）vs 年化 capex ≈$725B（分母 top-4＋Oracle） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-06-15 | 2026-08-10T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收 IPO 篩選，合格 0 件 | AI rename ticker SPAC no revenue IPO August 3-10 2026 | Reuters／Benzinga／IPOX SPAC 篩選 | — | 2026-08-10T09:30:00+08:00 |
| speculation.ipo_heat | 本週 APMD 首日 +56%、JMKE $1B 收平、IOND $3.1B 直接上市 | US IPO pricings week August 2026 Renaissance Apnimed | https://seekingalpha.com/article/4710009-us-ipo-weekly-recap-august-kicks-off-with-one-small-pricing （Seeking Alpha） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| speculation.microcap_moonshots | 單日 ≥100% 且疊加兩個以上題材的 microcap，合格 0 件 | microcap 100% single day quantum fusion nuclear space AI August 2026 | Finviz／StockAnalysis／StockTitan 漲幅榜 | — | 2026-08-10T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 ≈$1T IPO、Anthropic 續進 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground （Benzinga） | 2026-07-28 | 2026-08-10T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 cluster 篩選：候選僅有 StockTitan 二手頁，無 SEC EDGAR filing URL，合格 0 件 | Snowflake Tempus AI Form 4 insider sale July August 2026 SEC | SEC EDGAR、StockTitan 檢查 | — | 2026-08-10T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity-only put/call 0.55（日讀數） | Cboe equity put call ratio August 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio （YCharts） | 2026-08-03 | 2026-08-10T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 記錄高 ≈$198B | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing；原定來源 etf.com） | 2026-07-23 | 2026-08-10T09:30:00+08:00 |
| structural.us_single_stock_etf | 30 日內單股槓桿 ETF 核准／發行，合格 0 件（唯一候選新聞稿 URL 顯示 2026-07-07，早於窗口） | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | SEC EDGAR、ETF.com、GlobeNewswire 檢查 | — | 2026-08-10T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量 ≈65%（Cboe 季度披露） | 0DTE SPX options share Cboe Q2 2026 65% | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641 （Investing.com） | 2026-05-31 | 2026-08-10T09:30:00+08:00 |
| structural.options_volume | OCC 6 月總量 1,603,491,559 口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-08-10T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW ≈140、VIX ≈16 contango、債市波動偏高 | VIX SKEW bond volatility MOVE August 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher （Cboe） | 2026-08-07 | 2026-08-10T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt $1.502T、YoY +51.5%（交叉引用，不重複計入） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-08-10T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B Anthropic 掛鉤貸款加價＋covenant；Nebius $775M | CoreWeave 2.6 billion loan Anthropic covenant July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic （Bloomberg） | 2026-07-29 | 2026-08-10T09:30:00+08:00 |

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

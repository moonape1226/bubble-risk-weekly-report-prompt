> [DRY RUN] this report was not committed to archive.

# 2026-07-20 AI 泡沫破裂預測報告

報告日期：2026-07-20｜ISO 週次：2026-W30｜預測窗口：2026-07-20 → 2027-01-18｜前次基準：report-2026-07-16（4天前）

## 結論

**結論：no**

三條路徑都還遠離解析門檻：NASDAQ-100 自 52 週高點只回撤 6.74%，距 R1 的 25% 門檻仍需再跌約 19.58%；hyperscaler 2026 capex 指引仍在上修，四家中零家下修（`valuation.ndx_drawdown`、`ai.hyperscaler_capex`）。Oracle／CoreWeave CDS 走闊與 Blue Owl 的 gate proration / breach 顯示信用端壓力正在累積，但 HY OAS 2.71%、repo 資金壓力（SOFR−IORB）為 −3bp，尚無傳導至違約或強制去槓桿的證據，不足以推翻「182 天內三條件皆不成立」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 28,592.66（2026-07-17），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 6.74%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45；以最新收盤計，需再下跌約 19.58% 才觸及門檻（若窗口內創新高，門檻會跟著上移）。

近期壓力確實在升溫：2026-07-17 NYSE 下跌家數約為上漲家數的 2 倍、新高 241／新低 166，當日報導主軸為晶片股賣壓擴大（`breadth.advance_decline`）；S&P 500 自前次基準 7,533.77 降至 7,457.69（−1.01%），但仍高於 200 日 MA 6.73%、52 週 MA 8.42%（`valuation.sp500_trend`）。VIX 從 15.03（2026-07-10）升至 18.77（2026-07-17，+24.88%），S&P 500 同窗 −1.55%，屬正常的反向關係，非 crowded-optionality 式同漲（`structural.vix_spx_comove`）。

脆弱度面：Shiller CAPE 41.52、S&P 500 trailing P/E 32.08（`valuation.sp500_pe_cape`），FINRA margin debt $1.416T、YoY +53.7%（2026-05 月資料，`retail.margin_debt`），NAAIM 曝險 95.64（`retail.naaim`）——一旦下跌，槓桿與擁擠部位會放大跌幅。但情緒面並不亢奮：CNN Fear & Greed 37（Fear，`retail.fear_greed`），Cboe equity put/call 0.73（`speculation.equity_put_call`），不是 call-heavy 的末段追價型態。

**判讀：** 距門檻仍遠（6.74% 對 25%）。要在窗口內觸發，需要的不是估值高，而是一個觸發點——例如 hyperscaler 季報下修 capex（R2→R1）、AI 信用事件（R3→R1），或高槓桿部位（margin debt YoY +53.7%）遭強制平倉——把目前的晶片股修正擴大成約 20% 的再跌幅。目前尚未看到這類傳導。

### R2 資本支出收縮

最新官方指引（依彙總報導，2026-05-15）：四大 hyperscaler 2026 capex 合計約 $700B，且仍在上修（`ai.hyperscaler_capex`）。本次 evidence 只提供彙總數字，未取得 Microsoft、Alphabet、Amazon、Meta 個別的指引金額；依該報導，四家方向皆為上修，**目前下修家數為 0／4**（需 2 家）。

需求側仍偏強：TrendForce 預估 3Q26 伺服器 DRAM 合約價 QoQ +13–18%（2026-07-03，`ai.compute_supply_demand`），漲價伴隨的是需求而非庫存去化。Anthropic run-rate 約 $47B、OpenAI 約 $25B（2026-05-15，`ai.openai_anthropic_revenue`）；AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 $72bn（僅 OpenAI＋Anthropic）vs 年化 capex 約 $700bn（分母：該報導的 hyperscaler 合計，是否含 Oracle 未載明；Oracle 因 hyperscaler 融資結構本次無披露未另行加入），缺口極大，但本次無前值組合可判斷擴大或收斂（`ai.revenue_capex_gap`）。

下一輪財報的確切日期本次未取得；依季報節奏，窗口（至 2027-01-18）內應涵蓋 2026 年第二、三季兩輪財報，第四季（通常含次年度 capex 指引）的公布時點可能落在窗口邊界附近。

**判讀：** 遠離門檻。R2 需要兩家在窗口內明確下修指引，而目前方向是全數上修、記憶體合約價仍漲。最可能的觸發路徑是 R1 先發生（股價重挫迫使管理層收斂 capex），或 AI 營收對 capex 缺口在財報會議上被管理層正面承認。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）出現信用端開始重定價的跡象：Oracle 5 年期 CDS 約 198bp，創紀錄；CoreWeave CDS 約 665bp（2026-07-16，`valuation.ai_credit_schism`）。CoreWeave 以 AI 算力為主業，是最可能符合 R3 主體條件的借款人，但其負債規模本次未取得披露數字，是否 ≥ 50 億美元需另行確認；Oracle 主業非 AI 資料中心，即使違約也不直接適用 R3 定義。約 665bp 屬高收益高檔區間，但本次未見付款違約、covenant waiver、distressed exchange 或 going-concern 措辭。

周邊信用：私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）出現實際的 gate proration / breach——Blue Owl OCIC Q2 redemption-request ratio 18.8%，依 5% quarterly redemption cap 比例撥付；報導標題同時指出贖回壓力「略為緩和」（2026-07-02，`monetary.private_credit_liquidity`）。整體信用市場仍緊：HY OAS 2.71%、IG OAS 0.78%（2026-07-16，`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 −3bp，SOFR99−IORB +5bp，SRF 動用（Standing Repo Facility usage）為 0（`monetary.repo_stress_srf`）。

AI 基礎設施債務融資的 30 日事件掃描本次無新披露，近期到期或再融資牆無可引證的數字。

**判讀：** CDS 走闊顯示市場開始為 AI 算力債務的尾端風險定價，是三條路徑中變化最快的一條；但從約 665bp 的 CDS 到破產、違約或 distressed exchange，通常還需要再融資失敗或大客戶合約違約等具體事件，目前沒有這類證據。若 CoreWeave 類發行人 CDS 進入困境區間、或出現 covenant 談判報導，這條路徑才會在窗口內變得可信。

## 支持 yes 的證據

- [R3] Oracle 5 年期 CDS 約 198bp 創紀錄、CoreWeave CDS 約 665bp（2026-07-16），信用端先於股價重定價 AI 算力債務，是典型的後期訊號（`valuation.ai_credit_schism`）。
- [R3] Blue Owl OCIC Q2 redemption-request ratio 18.8%，遠高於 5% quarterly redemption cap，實際發生 gate proration / breach（2026-07-02）；非銀行資金來源收緊，會抬高 AI 基礎設施借款人的再融資難度（`monetary.private_credit_liquidity`）。
- [R1] 槓桿與擁擠部位處於歷史頂部型態：FINRA margin debt $1.416T、YoY +53.7%（2026-05 月資料），NAAIM 曝險 95.64（2026-07-15），一旦修正擴大，有被強制去槓桿放大的風險（`retail.margin_debt`、`retail.naaim`）。
- [R1] 估值極端：Shiller CAPE 41.52、trailing P/E 32.08（2026-07-17），Mag 7 加權 P/E 約 40（`valuation.sp500_pe_cape`、`valuation.mag7_multiples`）；下跌的潛在幅度大。
- [R1] 修正已開始：NASDAQ-100 距 52 週高點回撤 6.74%（2026-07-17）；07-17 晶片股賣壓擴大、NYSE 下跌家數約為上漲的 2 倍；VIX 一週升 24.88% 至 18.77（`valuation.ndx_drawdown`、`breadth.advance_decline`、`structural.vix_spx_comove`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）極大：OpenAI＋Anthropic run-rate 約 $72bn 對比 hyperscaler 年化 capex 約 $700bn，長期終需收斂（`ai.revenue_capex_gap`）。

## 支持 no 的證據

- [整體] 基準率：任一 182 天窗口內同時要求 NASDAQ-100 回撤 25%、兩家 hyperscaler 下修 capex 或 AI 大型借款人違約，三者都屬罕見事件；目前回撤僅 6.74%，距 R1 門檻 22,995.45 仍需再跌約 19.58%（`valuation.ndx_drawdown`）。
- [R2] hyperscaler 2026 capex 合計約 $700B 且仍在上修（2026-05-15），四家中零家下修，距 R2 的「兩家下修」門檻最遠（`ai.hyperscaler_capex`）。
- [R2] 算力需求側仍強：3Q26 伺服器 DRAM 合約價 QoQ +13–18%（2026-07-03），反映需求而非產能過剩或庫存去化（`ai.compute_supply_demand`）。
- [R3] 系統性信用與資金市場平穩：HY OAS 2.71%、IG OAS 0.78%（2026-07-16）；SOFR−IORB −3bp、SRF 動用為 0；美債基差交易槓桿相關的 MOVE 70.88、CFTC 槓桿基金淨部位四週變動 −78,139 口，無失序跡象（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`、`structural.treasury_basis_trade`）。
- [R1] 情緒並非亢奮末段：CNN Fear & Greed 37（Fear，2026-07-17），equity put/call 0.73，代表部分避險已經發生，而非 call-heavy 追價（`retail.fear_greed`、`speculation.equity_put_call`）。
- [整體] 政策緩衝仍在：Fed funds 3.50–3.75%，市場隱含 7/29 維持利率約 86.7%；CPI YoY 3.46%（2026-06）限制寬鬆空間，但未構成被迫緊縮（`monetary.fed_funds`、`monetary.fedwatch`、`monetary.cpi_yoy`）。

## 與前期比較

前次結論：無前次預測（report-2026-07-16 為舊格式評分報告）

前次為舊格式評分報告，不轉換為 yes／no，因此 flip_evidence 為空。2026-07-16 以來的主要變化如下：

- S&P 500 7,533.77 → 7,457.69（−1.01%）；NASDAQ-100 由 29,025.77（07-16）降至 28,592.66（07-17）。
- VIX 16.73 → 18.77；MOVE 68.16 → 70.88。
- 10Y：DGS10 4.57%、ΔDGS10 0bp、ΔDFII10 0bp（stale_series：DGS10、DFII10 無新觀測），ΔT10YIE +2bp；三腿視窗不一致，判讀為 `不可判（視窗不一致）`。T5YIFR +1bp 至 2.21%。
- HY／IG OAS、SOFR、WALCL 自 07-16 起無新觀測（Δ = 0）。
- 新的 AI 信用事件：Oracle／CoreWeave CDS 走闊報導（2026-07-16）與 Anthropic IPO 投資人會議報導（2026-07-15）落在前次前後；兩者皆未改變三條路徑的距離判斷。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源檢索已完成，但視窗內無合格披露，屬 ✗ NOT DISCLOSED：`valuation.analyst_tp_decomposition`、`retail.social_sentiment`、`institutional.bofa_jpm_survey`、`ai.token_growth`、`ai.customer_concentration_rpo`、`ai.hyperscaler_financing_mix`（quarterly_state 與 event_scan 皆無披露）、`ai.depreciation_life`、`ai.capital_cycle`（兩組件皆無披露）、`structural.global_leveraged_approvals`、`structural.ai_infrastructure_debt`。其中 `structural.ai_infrastructure_debt` 與 `ai.hyperscaler_financing_mix` 直接關係 R3：若有未被抓到的大型再融資失敗或 SPV 問題，可能改變 R3 判讀，是本次最主要的盲點。`ai.capital_cycle` 增速證據不足，本次不判定資本週期階段（capital cycle stage）。

其他資料品質註記：

- `speculation.insider_form4` 記為 ✓ SEARCH-VERIFIED（0 件），但 SEC EDGAR 一手 filing URL 因 egress 受限無法取得；本次不引用任何具名內部人賣出，此缺口不影響結論。
- `structural.treasury_basis_trade`：evidence 的檢索紀錄寫 script 三個組件皆 fetch_failed，但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 三塊皆為 `status: ok`；本次依 macro artifact 記為 ✓ API。兩份紀錄的矛盾應在 harness 端確認。
- `structural.zero_dte` 的 0DTE 佔比（約 63%）資料日為 2026-02-28，偏舊，僅作背景。`valuation.mag7_multiples`、`ai.hyperscaler_capex`、`ai.openai_anthropic_revenue` 資料日為 2026-05-15，屬沿用的 stock-of-state。
- R2 只有彙總 capex，缺四家個別指引金額，無法逐家驗證方向。

最大的不確定性：

1. **下一輪 hyperscaler 財報（窗口內）**：若有兩家下修 capex，R2 直接成立，同時可能觸發 R1，會把答案推向 yes；若持續上修，則維持 no。
2. **CoreWeave 類 AI 算力借款人的信用路徑**：CDS 約 665bp 若持續走闊並出現再融資困難或 covenant 談判，R3 會變得可信，推向 yes；負債規模是否達 R3 門檻也尚待確認。
3. **槓桿部位的強制去化**：margin debt YoY +53.7% 搭配 NAAIM 95.64，若晶片股修正演變成 margin call 連鎖，R1 的 19.58% 剩餘距離可能在數週內被吃掉，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7457.69 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日 MA 偏離 %） | 6.73 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週 MA 偏離 %） | 8.42 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（vs 前次基準） | -1.01 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28592.66 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 6.74 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1，家戶股票配置 %） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 2.71 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（IG OAS %） | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（10Y 殖利率 %） | 4.57 | FRED API (series_id=DGS10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（10Y 實質殖利率 %） | 2.35 | FRED API (series_id=DFII10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（10Y breakeven %） | 2.24 | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps（vs 前次基準） | 2.0 | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（WTI 美元） | 79.2 | FRED API (series_id=DCOILWTICO) | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（5y5y %） | 2.21 | FRED API (series_id=T5YIFR) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright 10Y 期限溢價 %） | 0.7788 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（序列自身 trailing 約 7 日） | 4.7 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API (series_id=SOFR99) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.walcl | WALCL latest（Fed 資產負債表） | 6743028.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（ECB 資產） | 5970516.0（€5.97T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（BOJ 資產） | 6395509.0（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 18.77 | FRED API (series_id=VIXCLS) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of） | 18.77 | script block vix_spx_comove（FRED VIXCLS × SP500） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（base 2026-07-10，7 日） | 24.88 | script block vix_spx_comove（FRED VIXCLS × SP500） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（同窗） | -1.55 | script block vix_spx_comove（FRED VIXCLS × SP500） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（銀行對 NBFI 放款） | 2004.0237（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7562874 | CFTC TFF futures-only | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -78139 | CFTC TFF futures-only | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 70.88 | Yahoo Finance chart API (^MOVE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2342.6 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com，WebSearch primary | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | MarketXLS，WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-05-15） |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報摘要，WebSearch primary，90d 且同季 | ✗ NOT DISCLOSED（檢索完成，無合格同季 TP 上調） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導，WebSearch primary，14d | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | ahasignals，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | US News 市場報導，WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | MacroMicro 轉載，WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | Advisor Perspectives（FINRA），WebSearch，月度沿用 | ✓ SEARCH-VERIFIED（2026-05 月資料） |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com，WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag，WebSearch，7d | ✗ NOT DISCLOSED（無顯著討論） |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | ycharts，WebSearch primary | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查，WebSearch | ✗ NOT DISCLOSED（無本月新調查） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直接取得） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | 標售報導，WebSearch primary，14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 轉載，WebSearch primary | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Bloomberg，WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露報導，WebSearch primary，30d | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報彙總報導，WebSearch，stock-of-state 沿用 | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露，WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch AI，WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話會議，WebSearch primary | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce，WebSearch primary | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報 quarterly_state＋30d event_scan，WebSearch primary | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露，WebSearch primary | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q，WebSearch primary，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速 quarterly_state＋30d event_scan，WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | WebSearch，7d | ✓ SEARCH-VERIFIED（1 件改名） |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis.com，WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／Benzinga／StockTitan movers，WebSearch primary | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導，WebSearch，30d | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR primary（egress 受限）＋openinsider 檢索，14d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe daily statistics，WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing，WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF.com，WebSearch，30d | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA，WebSearch，7d | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe insights，WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-02-28，偏舊） |
| structural.options_volume | 結構｜Options total volume: OCC monthly volume report | theocc.com，WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe／AInvest，WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | Advisor Perspectives（FINRA），交叉引用 | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | WebSearch primary，30d | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds／move_index／ofr_repo | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.08（原定來源 multpl.com） | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio（multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 41.52（原定來源 multpl.com） | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 trailing P/E 約 40 | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026（MarketXLS） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS 約 198bp（紀錄）、CoreWeave 約 665bp | Oracle CoreWeave CDS spread widening July 2026 | https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/（Real Investment Advice） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP +10.68% vs SPY +7.47% YTD | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-06-10 | 2026-07-20T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 36.40% | S&P 500 top 10 concentration percent 2026 | https://ahasignals.com/sp500-concentration-risk/（AHA Signals；原定 State Street SPDR 持股） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| breadth.advance_decline | NYSE 下跌約為上漲 2 倍、新高 241／新低 166 | NYSE advance decline breadth July 17 2026 | https://money.usnews.com/investing/news/articles/2026-07-17/wall-st-futures-fall-as-chip-selloff-gathers-pace-netflix-tumbles（US News） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（Fear） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed（MacroMicro；原定 cnn.com） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-05 月資料）$1.416T、YoY +53.7% | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra（Advisor Perspectives；原定 FINRA） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |
| retail.aaii | AAII Bull 44.9% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number（YCharts；原定 naaim.org） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 2.59、小幅 tail | US Treasury 10Y auction July 2026 bid to cover | https://cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/（Crypto Briefing；原定 Reuters／TreasuryDirect） | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 會議維持利率約 86.7% | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch（CryptoRank；原定 CME FedWatch） | 2026-07-18 | 2026-07-20T09:30:00+08:00 |
| monetary.pboc | 人行 6 個月買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance（Bloomberg） | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio 18.8%，依 5% quarterly redemption cap 比例撥付（gate proration / breach） | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://whbl.com/2026/07/02/blue-owl-keeps-withdrawal-limits-even-as-redemption-pressure-modestly-eases/（WHBL／Reuters 轉載） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計約 $700B、仍上修 | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html（Yahoo Finance） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic run-rate 約 $47B、OpenAI 約 $25B | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 QoQ +13–18% | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html（TrendForce） | 2026-07-03 | 2026-07-20T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex 約 $700B vs AI 終端營收約 $72B（OpenAI＋Anthropic） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI）；分母沿用 ai.hyperscaler_capex | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| speculation.ai_rename_spac | EVTV 更名 Azio AI（AZIO） | AI rename ticker change July 2026 Azio EVTV | https://www.businesswire.com/news/home/20260710628386/en/Azio-AI-Holdings-Inc.-Nasdaq-EVTV-to-Begin-Trading-Under-New-Ticker-Symbol-AZIO-Completing-Corporate-Rebrand（Business Wire） | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD 約 200 檔 IPO、募資 $141.2B | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/（StockAnalysis） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot：無 | microcap 100% single day quantum AI moonshot July 2026 | Finviz／Benzinga／StockTitan movers screener | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 投資人會議，估值 $965B，可能 10 月掛牌 | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html（CNBC） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 cluster：無（EDGAR 一手 URL 因 egress 受限無法取得） | insider Form 4 cluster AI leaders July 2026 openinsider | SEC EDGAR／openinsider | — | 2026-07-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.73（日讀數） | Cboe equity put call ratio July 2026 | https://www.cboe.com/markets/us/options/market-statistics/daily/（Cboe） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 約 $198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing；原定 etf.com／ETFGI） | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 推出 6 檔 2x 單一個股 ETF（GOOGL／AMZN／META／AAPL 等） | single-stock leveraged ETF launch July 2026 Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html（GlobeNewswire） | 2026-07-07 | 2026-07-20T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 成交約 63% | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/（Cboe） | 2026-02-28 | 2026-07-20T09:30:00+08:00 |
| structural.options_volume | OCC 6 月總成交 1,603,491,559 口、YoY +45% | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 145.13、VIX 約 16.5 期限結構 contango | VIX term structure SKEW July 2026 | https://www.ainvest.com/news/0dte-volatility-drives-market-strategies-2026-2602/（AInvest） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-05 月資料）$1.416T、YoY +53.7%（交叉確認） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra（Advisor Perspectives） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-07-20",
  "iso_week": "2026-W30",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-01-18",
  "prior_date": "2026-07-16",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 6.74,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

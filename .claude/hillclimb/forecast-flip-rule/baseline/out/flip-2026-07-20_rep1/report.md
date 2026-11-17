> [DRY RUN] this report was not committed to archive.

# 2026-07-20 AI 泡沫破裂預測報告

報告日期：2026-07-20｜ISO 週次：2026-W30｜預測窗口：2026-07-20 → 2027-01-18｜前次基準：report-2026-07-16（4天前）

## 結論

**結論：yes**

維持前次 yes：R3 與 R1 的傳導鏈仍在推進——AI 信用端已出現重定價（Oracle 5yr CDS ≈198bp 創紀錄、CoreWeave ≈665bp，`valuation.ai_credit_schism`），私募信貸出現實際 gate proration / breach（Blue Owl OCIC Q2 redemption-request ratio 18.8%、按 5% quarterly redemption cap 比例撥付，`monetary.private_credit_liquidity`）。前次基準後的新數據（NASDAQ-100 回撤由 3.78% 擴大、7/17 晶片股賣壓、VIX 一週 +24.88%）方向與前次判斷一致，沒有任何一筆新證據把路徑分析推向 no，因此依翻轉紀律維持原答案。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 28,592.66（2026-07-17），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 6.74%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，自最新收盤須再下跌約 5,597 點、≈19.58% 才會觸發。前次基準（2026-07-16）回撤為 3.78%，四天內擴大近 3 個百分點；7/17 NYSE 下跌家數約為上漲家數兩倍、新高 241／新低 166，報導標題為晶片股賣壓擴大（`breadth.advance_decline`）。S&P 500 7,457.69（2026-07-17）仍高於 200 日均線 6.73%、高於 52 週均線 8.42%，較前次基準 −1.01%（`valuation.sp500_trend`）。VIX 18.77（2026-07-17），七日窗口（2026-07-10 → 2026-07-17）VIX +24.88%、S&P 500 −1.55%，屬正常反向變動，非 crowded-optionality 同漲讀數（`structural.vix_spx_comove`）。

**判讀：** R1 距觸發仍遠（尚需再跌≈19.6%），但已由高點回落且賣壓集中於晶片／AI 權重股；在 CAPE 41.52、margin debt YoY +53.7% 的槓桿與估值背景下，若 R3 信用重定價擴散或 Anthropic IPO 等大額供給集中出現，窗口內完成 25% 回撤是可行路徑，而非僅靠估值偏高。

### R2 資本支出收縮

本次可用證據為聚合層級：hyperscaler 2026 年 capex 合計≈$700B，報導指仍在上修（2026-05-15，`ai.hyperscaler_capex`）。逐家（Microsoft、Alphabet、Amazon、Meta）的最新指引數值與日期本次證據未逐一列出；依聚合報導，四家方向均為上修或持平，截至目前下修家數為 0。下一輪季報日期本次證據未載，但至少一輪（多半兩輪）季報會落在 2026-07-20 → 2027-01-18 窗口內。供給側價格仍強：伺服器 DRAM 3Q26 合約價 +13–18% QoQ（2026-07-03，`ai.compute_supply_demand`），顯示需求尚未出現 order digestion。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收（Anthropic ≈$47B、OpenAI ≈$25B run-rate）對年化 capex ≈$700B（分母：top-4 hyperscaler 聚合，未含 Oracle 與 neocloud），缺口巨大（`ai.revenue_capex_gap`、`ai.openai_anthropic_revenue`）。

**判讀：** R2 是三條路徑中最遠的一條——目前零家下修，且指引仍在上修；要在窗口內觸發，需要 R1 回撤或 R3 信用事件先壓迫融資條件，迫使至少兩家在下一兩輪財報中下修指引。

### R3 AI 信用事件

信用端已開始重定價：Oracle 5yr CDS ≈198bp 創紀錄、CoreWeave 5yr CDS ≈665bp（2026-07-16，`valuation.ai_credit_schism`）。CoreWeave 以算力為主業，是 R3 規模門檻的主要候選（其負債總額本次證據未載）；Oracle 主業非 AI 資料中心，其 CDS 是情緒與傳導指標而非 R3 直接標的。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）已具體化：Blue Owl OCIC Q2 redemption-request ratio 18.8%，按 5% quarterly redemption cap 比例撥付，屬實際 gate proration / breach（2026-07-02，`monetary.private_credit_liquidity`）。對照之下，整體信用市場仍平靜：HY OAS 2.71%、IG OAS 0.78%（2026-07-16，`monetary.hy_oas`、`monetary.ig_oas`），repo 資金壓力（SOFR−IORB）−3bp、SRF 動用（Standing Repo Facility usage）0（`monetary.repo_stress_srf`）。過去 30 天未見新的 AI 資料中心／neocloud 債務融資披露，也未見付款違約、covenant waiver 或 distressed exchange 報導。

**判讀：** 尚無違約或 distressed exchange，但 AI 信用定價分歧（equity-vs-credit schism）正以「信貸端先走闊」的後期型態出現，且非銀行資金端已出現贖回比例撥付；若 CoreWeave 類高槓桿借款人在窗口內遭遇再融資受阻或私募信貸資金流進一步惡化，R3 可在窗口內完成，並經由信用傳導觸發 R1。

## 支持 yes 的證據

- [R3] AI 信用端重定價：Oracle 5yr CDS ≈198bp 創紀錄、CoreWeave 5yr CDS ≈665bp（2026-07-16），信貸先於股價走闊，是 AI 信用定價分歧（equity-vs-credit schism）的後期訊號（`valuation.ai_credit_schism`）。
- [R3] 私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）已發生實際 gate proration / breach：Blue Owl OCIC Q2 redemption-request ratio 18.8%，按 5% quarterly redemption cap 比例撥付（2026-07-02），非銀行資金端是 AI infrastructure debt financing / vendor-financing loops 的主要資金來源（`monetary.private_credit_liquidity`）。
- [R1] 回撤在前次基準後加速：NASDAQ-100 距 52 週高點回撤 6.74%（2026-07-17；前次 3.78%），7/17 NYSE 下跌約為上漲兩倍、晶片股賣壓擴大，VIX 七日 +24.88% 至 18.77，CNN Fear & Greed 降至 37（Fear）（`valuation.ndx_drawdown`、`breadth.advance_decline`、`structural.vix_spx_comove`、`retail.fear_greed`）。
- [整體] 脆弱性極高、下跌放大器到位：Shiller CAPE 41.52、trailing P/E 32.08（2026-07-17），FINRA margin debt $1.416T、YoY +53.7%（2026-05 月資料，落在歷史頂部區間 +40–50% 之上），NAAIM 曝險 95.64（2026-07-15），US 槓桿 ETF AUM ≈$198B（`valuation.sp500_pe_cape`、`retail.margin_debt`、`retail.naaim`、`structural.leveraged_etf_aum`）。
- [R1] 窗口內的大額股權供給與投機催化：Anthropic IPO 投資人會議估值 $965B、可能 10 月掛牌（2026-07-15）；2026 YTD ≈200 檔 IPO、募資 $141.2B；EVTV 改名 Azio AI（2026-07-13）；新增 6 檔 2x 單一股票槓桿 ETF（2026-07-07）（`speculation.upcoming_ai_ipos`、`speculation.ipo_heat`、`speculation.ai_rename_spac`、`structural.us_single_stock_etf`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）懸殊：年化 AI 終端營收（Anthropic ≈$47B + OpenAI ≈$25B run-rate）對年化 capex ≈$700B（分母：top-4 hyperscaler 聚合），回本壓力是未來 capex 下修的結構性來源（`ai.revenue_capex_gap`）。

## 支持 no 的證據

- [R1] 距 R1 門檻仍遠：NASDAQ-100 28,592.66 須再跌≈19.58% 才到 22,995.45；S&P 500 仍高於 200 日均線 6.73%（2026-07-17），趨勢尚未破壞（`valuation.ndx_drawdown`、`valuation.sp500_trend`）。
- [R2] capex 仍在上修：hyperscaler 2026 capex 合計≈$700B 且仍上修（2026-05-15），四家下修家數為 0；伺服器 DRAM 3Q26 合約價 +13–18% QoQ（2026-07-03），需求端未見 order digestion（`ai.hyperscaler_capex`、`ai.compute_supply_demand`）。
- [R3] 整體信用與資金市場平靜：HY OAS 2.71%、IG OAS 0.78%（2026-07-16），repo 資金壓力（SOFR−IORB）−3bp、SOFR99−IORB +5bp、SRF 動用 0（2026-07-16／07-17），尚無付款違約或 distressed exchange（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`）。
- [整體] 美債與政策端無失序跡象：MOVE 70.88（2026-07-17）、美債基差交易槓桿（Treasury basis-trade leverage）CFTC 槓桿基金淨空 −7,562,874 口、4 週變動僅 −78,139 口（2026-07-14），10Y 標售 bid-to-cover 2.59 僅小幅 tail（2026-07-08），CME FedWatch 7/29 會議隱含持平≈86.7%（2026-07-18）（`structural.treasury_basis_trade`、`monetary.treasury_auctions`、`monetary.fedwatch`）。
- [整體] 基準率與情緒：任一 182 天窗口內 R1–R3 皆不發生是常態；散戶情緒並非極端狂熱——AAII Bull 44.9%（2026-07-16）、Cboe equity put/call 0.73（2026-07-17），等權重 RSP YTD +10.68% 優於 SPY +7.47%（2026-06-10），廣度未呈現極端集中後的崩解型態（`retail.aaii`、`speculation.equity_put_call`、`breadth.rsp_spy`）。

## 與前期比較

前次結論：yes（report-2026-07-16）

本次結論：維持

- NASDAQ-100 回撤由 3.78% 擴大至 6.74%（2026-07-17，`valuation.ndx_drawdown`）：方向與前次 yes 一致，但距 R1 門檻仍需≈19.58%，不構成改判理由。
- 7/17 晶片股賣壓、VIX 18.77（七日 +24.88%）、CNN Fear & Greed 37（`breadth.advance_decline`、`structural.vix_spx_comove`、`retail.fear_greed`）：風險偏好轉弱，強化而非削弱 R1 路徑。
- CME FedWatch 7/29 隱含持平≈86.7%（2026-07-18，`monetary.fedwatch`）：政策路徑無變化，CPI YoY 3.46%（2026-06 月資料）仍限制降息緩衝空間，對答案中性。
- 10Y 分解：ΔDGS10 0bp、ΔDFII10 0bp（DGS10、DFII10 無新觀測）、ΔT10YIE +2bp，判讀不可判（視窗不一致）；HY／IG OAS、SOFR、WALCL 無新觀測（`monetary.dgs10`、`monetary.t10yie`）。
- 前次基準後沒有任何日期晚於 2026-07-16、且將路徑分析推向 no 的來源（capex 上修與 DRAM 價格均為前次已知資料），依翻轉紀律維持 yes；flip_evidence 為空。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

未披露（✗ NOT DISCLOSED）來源：`valuation.analyst_tp_decomposition`、`retail.social_sentiment`、`institutional.bofa_jpm_survey`、`ai.token_growth`、`ai.customer_concentration_rpo`、`ai.hyperscaler_financing_mix`、`ai.depreciation_life`、`ai.capital_cycle`、`structural.global_leveraged_approvals`、`structural.ai_infrastructure_debt`。其中 `structural.ai_infrastructure_debt` 與 `ai.hyperscaler_financing_mix` 的缺口與 R3 直接相關：若有未被捕捉的大額 neocloud 再融資或 SPV 結構，可能強化 yes；目前缺口不足以改變答案。

資料品質備註：

- `structural.treasury_basis_trade`：搜尋紀錄將三個 script 組件標為 fetch_failed，但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 皆為 status ok；本報告以 deterministic artifact 為準（✓ API），兩者不一致須於正式運行前核查。
- `speculation.insider_form4`：SEC EDGAR egress 受限，0 件係由次要來源篩檢得出，未能逐筆以 EDGAR Form 4 URL 核實；若存在未捕捉的 insider 集中賣出，僅屬情緒佐證，不影響答案。
- `ai.hyperscaler_capex` 僅有聚合層級報導（2026-05-15），缺逐家指引數值；`valuation.mag7_multiples`（2026-05-15）與 `structural.zero_dte`（2026-02-28）資料偏舊。

最大不確定性：

1. 下一輪 hyperscaler 季報（日期本次證據未載，落在窗口內）：若兩家以上下修 capex 指引則直接解析 R2 為 yes；若繼續上修，R2 路徑基本關閉、答案將更依賴 R1／R3。
2. CoreWeave 等以算力為主業借款人的再融資與信用走勢：CDS ≈665bp 若持續走闊並伴隨 covenant／交換要約消息，強力推向 yes；若利差收斂且新融資順利完成，削弱 yes 的主要支柱。
3. Anthropic 可能於 10 月的 IPO：大額股權供給可能成為 R1 催化劑；若順利定價並帶動風險偏好回升，則推向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7457.69 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 6.73 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.42 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28592.66 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 6.74 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1，家庭股權配置 %） | 45.76080873390133（≈45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 2.71 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（IG OAS %） | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（10Y 殖利率 %） | 4.57 | FRED API (series_id=DGS10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（10Y 實質殖利率 %） | 2.35 | FRED API (series_id=DFII10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（10Y breakeven %） | 2.24 | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps（較前次基準 bp） | 2.0 | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（WTI 美元／桶） | 79.2 | FRED API (series_id=DCOILWTICO) | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料，CPI YoY %） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（5y5y forward %） | 2.21 | FRED API (series_id=T5YIFR) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（10Y 期限溢價（term premium）%，Kim-Wright） | 0.7788 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（序列自身 trailing≈7d） | 4.7 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（99th 分位 %） | 3.7 | FRED API (series_id=SOFR99) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用 transaction volume，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps（SOFR−IORB，as_of 2026-07-16） | -3.0 | FRED API (series_id=SOFR, IORB) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.walcl | WALCL latest（Fed 資產負債表） | 6743028.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（ECB 資產） | 5970516.0（€5.97T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（BOJ 資產） | 6395509.0（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 18.77 | FRED API (series_id=VIXCLS) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of 2026-07-17，base 2026-07-10） | 18.77 | FRED API (series_id=SP500, VIX pair) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（七日 %） | 24.88 | FRED API (series_id=SP500, VIX pair) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（七日 %） | -1.55 | FRED API (series_id=SP500, VIX pair) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（銀行對 NBFI 放款） | 2004.0237（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7562874 | CFTC TFF futures-only (cftc_lev_funds) | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -78139 | CFTC TFF futures-only (cftc_lev_funds) | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（MOVE） | 70.88 | Yahoo Finance chart API ^MOVE (move_index) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2342.6 | OFR STFM REPO-TRIV1_TV_TOT-P (ofr_repo) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | MarketXLS 等 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 WebSearch（90d＋同季） | ✗ NOT DISCLOSED（搜尋完成，無同季合格上調） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA／Advisor Perspectives WebSearch（月頻 carry-forward） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag WebSearch（7d） | ✗ NOT DISCLOSED（無顯著討論） |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／ycharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✗ NOT DISCLOSED（無新月份調查） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（DFEDTARU:ok, DFEDTARL:ok） | ✓ API |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直接取得） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（SOFR:ok, SOFR99:ok, IORB:ok, RPONTTLD:ok） | ✓ API |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | Reuters／TreasuryDirect 摘要 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW:ok, JPNASSETS:ok） | ✓ API |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Bloomberg WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]（30d） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報／新聞 WebSearch（季頻 carry-forward） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／The Information WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 [primary: SEARCH] | ✗ NOT DISCLOSED（無合格披露） |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報＋30d 事件 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q [primary: SEARCH]（30d） | ✗ NOT DISCLOSED（30 日內無變動） |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速＋30d 進出場事件 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis／Renaissance WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／Benzinga movers [primary: SEARCH]（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | S-1／具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR [primary]＋openinsider WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com／ETFGI [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com／GlobeNewswire（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED（7 日內無英文披露） |
| structural.zero_dte | 結構｜0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume | OCC 月報 WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe／AInvest WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS:ok, vix_spx_comove:ok） | ✓ API |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 retail.margin_debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]（30d） | ✗ NOT DISCLOSED（30 日內無新披露） |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds:ok, move_index:ok, ofr_repo:ok；any） | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.08（原定來源 multpl.com） | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 41.52（原定來源 multpl.com） | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E ≈40 trailing（MarketXLS） | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026 | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS ≈198bp 創紀錄、CoreWeave ≈665bp（Real Investment Advice） | Oracle CoreWeave CDS spread widening July 2026 | https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/ | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP +10.68% vs SPY +7.47% YTD（247wallst） | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ | 2026-06-10 | 2026-07-20T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 36.40%（ahasignals） | S&P 500 top 10 concentration percent 2026 | https://ahasignals.com/sp500-concentration-risk/ | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| breadth.advance_decline | NYSE 7/17 下跌約為上漲兩倍、新高 241／新低 166（US News／Reuters） | NYSE advance decline breadth July 17 2026 | https://money.usnews.com/investing/news/articles/2026-07-17/wall-st-futures-fall-as-chip-selloff-gathers-pace-netflix-tumbles | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（Fear）（MacroMicro，原定來源 cnn.com） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-05 月資料）$1.416T、YoY +53.7%（Advisor Perspectives，原定來源 FINRA） | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra | 2026-05-31 | 2026-07-20T09:30:00+08:00 |
| retail.aaii | AAII Bull 44.9%（aaii.com） | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64（YCharts） | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 2.59、小幅 tail（CryptoBriefing） | US Treasury 10Y auction July 2026 bid to cover | https://cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/ | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 會議隱含持平≈86.7%（CryptoRank 摘要） | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch | 2026-07-18 | 2026-07-20T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元（Bloomberg） | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio 18.8%，按 5% quarterly redemption cap 比例撥付（gate proration / breach） | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://whbl.com/2026/07/02/blue-owl-keeps-withdrawal-limits-even-as-redemption-pressure-modestly-eases/ | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計≈$700B、仍上修（Yahoo Finance） | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic ≈$47B／OpenAI ≈$25B run-rate（Epoch AI） | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 +13–18% QoQ（TrendForce） | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html | 2026-07-03 | 2026-07-20T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex ≈$700B vs AI 終端營收低百億級（分母：top-4 hyperscaler 聚合；Epoch AI） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| speculation.ai_rename_spac | EVTV 改名 Azio AI（AZIO）（Business Wire） | AI rename ticker change July 2026 Azio EVTV | https://www.businesswire.com/news/home/20260710628386/en/Azio-AI-Holdings-Inc.-Nasdaq-EVTV-to-Begin-Trading-Under-New-Ticker-Symbol-AZIO-Completing-Corporate-Rebrand | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD ≈200 檔 IPO、募資 $141.2B（stockanalysis） | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/ | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| speculation.microcap_moonshots | 7 日內合格 microcap moonshot 0 件 | microcap 100% single day quantum AI moonshot July 2026 | Finviz／Benzinga／StockTitan movers screener | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 投資人會議、估值 $965B、可能 10 月掛牌（CNBC） | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 cluster 0 件（EDGAR egress 受限） | insider Form 4 cluster AI leaders July 2026 openinsider | SEC EDGAR／openinsider | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.73（daily） | Cboe equity put call ratio July 2026 | https://www.cboe.com/markets/us/options/market-statistics/daily/ | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM ≈$198B（CryptoBriefing） | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 新增 6 檔 2x 單一股票槓桿 ETF（GOOGL／AMZN／META／AAPL 等） | single-stock leveraged ETF launch July 2026 Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html | 2026-07-07 | 2026-07-20T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 成交≈63%（Cboe） | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/ | 2026-02-28 | 2026-07-20T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月 1,603,491,559 口、YoY +45% | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 145.13、VIX ≈16.5 contango（AInvest） | VIX term structure SKEW July 2026 | https://www.ainvest.com/news/0dte-volatility-drives-market-strategies-2026-2602/ | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-05 月資料）$1.416T、YoY +53.7%（cross-reference only） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra | 2026-05-31 | 2026-07-20T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-07-20",
  "iso_week": "2026-W30",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "yes",
  "horizon_end": "2027-01-18",
  "prior_date": "2026-07-16",
  "prior_answer": "yes",
  "flip_evidence": [],
  "r1_drawdown_pct": 6.74,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

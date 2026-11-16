> [DRY RUN] this report was not committed to archive.

# 2026-07-20 AI 泡沫破裂預測報告

報告日期：2026-07-20｜ISO 週次：2026-W30｜預測窗口：2026-07-20 → 2027-01-18｜前次基準：report-2026-07-16（4天前）

## 結論

**結論：yes**

維持前次 yes：前次基準（2026-07-16）之後到來的新資料全部指向壓力加深，沒有一筆指向緩解——NASDAQ-100 於 2026-07-17 收盤距 52 週高點回撤 6.74%（前次 r1_drawdown_pct 為 3.78），同日晶片股賣壓、VIX 7 日 +24.88%；同時 R3 端 Oracle 5yr CDS ≈198bp 創紀錄、CoreWeave ≈665bp，私募信貸已出現實際 gate proration / breach。依翻轉紀律，沒有任何晚於前次日期、且把路徑分析推向 no 的新證據，因此不翻轉；R1（股價回撤經信用重定價放大）與 R3 的互動仍是主要路徑。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 28,592.66（2026-07-17），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 6.74%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，自最新收盤再下跌約 19.58% 即觸發；r1_met = false。前次基準時 r1_drawdown_pct 為 3.78，四天內回撤幅度接近翻倍。S&P 500 於 2026-07-17 收 7,457.69，仍高於 200 日均線 6.73%、高於 52 週均線 8.42%（`valuation.sp500_trend`），代表即使回撤擴大，價格相對長期趨勢仍偏延伸。VIX 與 S&P 500 的 7 日共動（2026-07-10 → 2026-07-17）：VIX +24.88%、S&P 500 −1.55%，屬一般的避險上升而非 crowded-optionality 共漲（comove = false）（`structural.vix_spx_comove`）。NYSE 2026-07-17 下跌家數約為上漲的 2 倍，新高 241／新低 166，賣壓集中於晶片股（`breadth.advance_decline`）。估值脆弱性：S&P 500 trailing P/E 32.08、Shiller CAPE 41.52（2026-07-17，`valuation.sp500_pe_cape`）；margin debt $1.416T、YoY +53.7%（2026-05 月資料，`retail.margin_debt`），已高於歷史頂部附近常見的 +40–50% 區間；NAAIM Exposure 95.64（2026-07-15，`retail.naaim`）。

**判讀：** R1 距門檻仍有約 19.58% 的跌幅，屬於遙遠但已開始移動的路徑。窗口內把它推過門檻的情境是：Q2／Q3 財報季的 AI 營收或 capex 敘事失望、R3 端信用重定價擴散到 IG／HY，或高槓桿部位（margin debt YoY +53.7%、槓桿 ETF AUM ≈$198B）的被迫去槓桿造成連鎖下跌。

### R2 資本支出收縮

本次證據只有 hyperscaler 合計層級的指引：2026 年 capex 合計約 $700B，且方向仍是上修（2026-05-15，Q1 財報季後彙整，`ai.hyperscaler_capex`）。Microsoft、Alphabet、Amazon、Meta 各自的最新正式指引數字未逐家出現在本次證據中；依該彙整，四家的方向判讀為上修，下修家數為 0／4。具體下一次財報日期未在本次證據中取得，但 182 天窗口必然涵蓋至少兩輪季報（Q2、Q3）。供給鏈端的需求訊號仍偏強：TrendForce 指 3Q26 伺服器 DRAM 合約價季增 +13–18%（2026-07-03，`ai.compute_supply_demand`），屬需求健康或成本上升的讀數，未見訂單消化或利用率走弱的配對證據。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收 ≈$72B（僅 Anthropic ≈$47B＋OpenAI ≈$25B run-rate）vs 2026 hyperscaler capex ≈$700B（分母：來源所述 hyperscaler 合計，未逐家拆分），缺口約 10 倍；本次無新組件披露，不判斷擴大或收斂（`ai.revenue_capex_gap`、`ai.openai_anthropic_revenue`）。

**判讀：** R2 是三條路徑中離觸發最遠的一條——需要兩家在窗口內下修，而最新方向仍是上修。只有在 R1 大幅回撤或 R3 信用事件使融資成本驟升後，才可能在 Q3 財報季（窗口後段）出現兩家下修；它更可能是 R1／R3 的結果而非起點。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）已開始往信貸端重定價：Oracle 5yr CDS ≈198bp 創紀錄、CoreWeave ≈665bp（2026-07-16，`valuation.ai_credit_schism`）。CoreWeave 這類以 AI 資料中心／算力為主業的 neocloud 是最可能符合 R3 規模門檻（負債 ≥ 50 億美元）的借款人；≈665bp 的 CDS 已是高收益偏弱信用的定價，但不等於違約。本次 30 日內未發現新的 AI infrastructure debt financing / vendor-financing loops 披露，也未發現付款違約、covenant waiver、distressed exchange 或 going-concern 字樣；具體到期牆與再融資需求本次無可用資料。整體信用仍寬鬆：HY OAS 2.71%、IG OAS 0.78%（2026-07-16，`monetary.hy_oas`、`monetary.ig_oas`），代表 AI 特定信用走闊尚未擴散到大盤信用。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）出現實際事件：Blue Owl OCIC Q2 redemption-request ratio 18.8%，以 5% quarterly redemption cap 比例撥付，屬 gate proration / breach（2026-07-02，`monetary.private_credit_liquidity`），但來源同時稱贖回壓力略為緩和。資金面平穩：repo 資金壓力（SOFR−IORB）為 −3bp、SOFR99−IORB 為 +5bp（SOFR／SOFR99／IORB 均為 2026-07-16 觀測），SRF 動用（Standing Repo Facility usage）為 0（2026-07-17）（`monetary.repo_stress_srf`）；銀行對 NBFI 放款 $2.00T（2026-07-08，`structural.nbfi_bank_loans`）。

**判讀：** R3 尚無任何違約或 distressed exchange，但 CDS 已把 CoreWeave 定價在明顯的壓力區，且私募信貸已出現 gate proration。窗口內推過門檻的情境是：AI 股價回撤（R1）收緊 neocloud 的股權與債務再融資管道，疊加私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）擴散到更多基金，迫使高槓桿 neocloud 進行 distressed exchange。

## 支持 yes 的證據

- [R3] Oracle 5yr CDS ≈198bp 創紀錄、CoreWeave ≈665bp（2026-07-16）：AI 信用定價分歧（equity-vs-credit schism）已轉向信貸端重定價，是後期訊號，且 CoreWeave 屬 R3 規模門檻內的主業借款人 `valuation.ai_credit_schism`
- [R1] NASDAQ-100 2026-07-17 收盤 28,592.66，距 52 週高點回撤 6.74%，較前次 r1_drawdown_pct 3.78 明顯擴大；同日 NYSE 下跌家數約為上漲 2 倍、賣壓集中於晶片股 `valuation.ndx_drawdown` `breadth.advance_decline`
- [R1] VIX 7 日由 15.03 升至 18.77（+24.88%，2026-07-10 → 2026-07-17），S&P 500 同期 −1.55%，避險需求快速上升 `structural.vix_spx_comove`
- [整體] 槓桿與估值極端：margin debt $1.416T、YoY +53.7%（2026-05 月資料），Shiller CAPE 41.52、trailing P/E 32.08（2026-07-17），NAAIM 95.64（2026-07-15），回撤一旦啟動易被去槓桿放大 `retail.margin_debt` `valuation.sp500_pe_cape` `retail.naaim`
- [R3] Blue Owl OCIC Q2 redemption-request ratio 18.8%，以 5% quarterly redemption cap 比例撥付，屬實際 gate proration / breach（2026-07-02），非銀行資金鏈已有壓力 `monetary.private_credit_liquidity`
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收 ≈$72B（Anthropic＋OpenAI）vs hyperscaler 2026 capex ≈$700B（2026-05-15），回本壓力是窗口內 capex 敘事反轉的結構前提 `ai.revenue_capex_gap`
- [整體] 投機熱度：Anthropic IPO 投資人會議估值 $965B、可能 10 月掛牌（2026-07-15）；EVTV 改名 Azio AI（AZIO，2026-07-13）；US 槓桿 ETF 總 AUM ≈$198B（2026-07-10） `speculation.upcoming_ai_ipos` `speculation.ai_rename_spac` `structural.leveraged_etf_aum`

## 支持 no 的證據

- [R1] R1 門檻水位 22,995.45，自 2026-07-17 收盤仍需再跌約 19.58%；在任意 182 天窗口內 NASDAQ-100 回撤 25% 本身是罕見事件 `valuation.ndx_drawdown`
- [R2] hyperscaler 2026 capex 合計約 $700B 且仍在上修（2026-05-15），四家中下修家數 0；3Q26 伺服器 DRAM 合約價 +13–18% QoQ（2026-07-03）顯示 AI 供應鏈需求仍強 `ai.hyperscaler_capex` `ai.compute_supply_demand`
- [R3] 大盤信用仍寬鬆：HY OAS 2.71%、IG OAS 0.78%（2026-07-16），AI 特定信用走闊尚未擴散 `monetary.hy_oas` `monetary.ig_oas`
- [R3] 資金面無失序：SOFR−IORB −3bp、SOFR99−IORB +5bp（2026-07-16），SRF 動用 0（2026-07-17），OFR tri-party repo transaction volume $2,342.6bn（2026-07-17） `monetary.repo_stress_srf` `structural.treasury_basis_trade`
- [整體] 情緒已降溫而非亢奮：CNN Fear & Greed 37（Fear，2026-07-17），Cboe equity put/call 0.73（2026-07-17），RSP YTD +10.68% 領先 SPY +7.47%（2026-06-10）代表上漲並非只靠少數巨頭 `retail.fear_greed` `speculation.equity_put_call` `breadth.rsp_spy`
- [整體] Fed 仍有緩衝：fed funds 目標區間 3.50%–3.75%（2026-07-19），CME FedWatch 7/29 會議隱含持平定價 ≈86.7%（2026-07-18），CPI YoY 3.46%（2026-06 月資料）限制降息空間但非緊縮 `monetary.fed_funds` `monetary.fedwatch` `monetary.cpi_yoy`

## 與前期比較

前次結論：yes（report-2026-07-16）

本次結論：維持

- NASDAQ-100 r1_drawdown_pct 由前次 3.78 擴大到 6.74（2026-07-17）：方向強化 R1，不支持翻轉為 no。
- VIX 由前次的 16.73 升至 18.77（2026-07-17），7 日 +24.88%；2026-07-17 晶片股賣壓、NYSE 下跌家數約為上漲 2 倍：皆為前次日期之後的新資料，方向與前次 yes 一致。
- CNN Fear & Greed 37（2026-07-17）與 CME FedWatch 持平定價 ≈86.7%（2026-07-18）是前次之後的新讀數，但前者屬情緒降溫（回撤進行中的同步現象），後者代表近期無降息緩衝，皆不改變 R1／R3 路徑分析。
- DGS10、DFII10、HY OAS、IG OAS、SOFR、WALCL 自前次以來無新觀測（持平）；10Y breakeven（T10YIE）+2bp、5y5y（T5YIFR）+1bp，屬雜訊範圍。
- Oracle／CoreWeave CDS（2026-07-16）與 Blue Owl gate proration（2026-07-02）的日期不晚於前次基準，本次僅延續引用，不作為新證據。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下為 ✗ NOT DISCLOSED（檢索完成但無合格披露）的來源：valuation.analyst_tp_decomposition、retail.social_sentiment、institutional.bofa_jpm_survey、ai.token_growth、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（quarterly_state 與 event_scan 皆無披露）、ai.depreciation_life、ai.capital_cycle（兩組件皆無披露）、structural.global_leveraged_approvals、structural.ai_infrastructure_debt。其中 structural.ai_infrastructure_debt 與 ai.hyperscaler_financing_mix 的缺漏與 R3 最相關：若存在未被搜尋到的 neocloud 再融資困難或 SPV 結構壓力，會把答案進一步推向 yes；反之其缺席不足以支持翻轉。ai.capital_cycle 本次增速證據不足，本次不判定週期階段。

其他資料限制：

- speculation.insider_form4 以 openinsider 等二手來源完成 14 日篩選、0 件合格；SEC EDGAR 一手 filing URL 因 egress 受限無法取得，因此「0 件」的確定性低於正常；即使有 cluster，也只會小幅強化 yes。
- R2 逐家 capex 指引數字未出現在本次證據中，只有 hyperscaler 合計約 $700B 且上修的彙整；四家方向以該彙整判讀。
- structural.treasury_basis_trade：搜尋 outcome 表記錄三個 script 組件為 fetch_failed，但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 三塊均為 status ok，本次以 macro artifact 為準記 ✓ API；槓桿基金美債期貨淨部位 −7,562,874 口（2026-07-14，4 週 Δ −78,139），MOVE 70.88（2026-07-17），無基差平倉事件報導。
- 10Y 分解：ΔDGS10 0bp、ΔDFII10 0bp（兩者無新觀測，stale_series = DGS10, DFII10），ΔT10YIE +2bp，判讀 不可判（視窗不一致）。
- valuation.mag7_multiples（2026-05-15）、structural.zero_dte（2026-02-28）、breadth.rsp_spy（2026-06-10）為較舊的 snapshot，僅作背景。

最大不確定性：

1. Q2 財報季（窗口初段）的 hyperscaler capex 指引與 AI 營收：若指引持續上修且 AI 營收加速，會削弱 R1／R2 路徑、推向 no；若有一家下修，則強化 R2 並可能觸發 R1。
2. CoreWeave 等 neocloud 的再融資：CDS ≈665bp 若持續走闊且伴隨 distressed exchange 傳聞，會直接推向 R3 yes；若成功完成大額再融資，則推向 no。
3. Anthropic 可能於 10 月 IPO（$965B）：成功掛牌會延續 AI 估值敘事（推向 no），失敗或延後會成為 R1 催化劑（推向 yes）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7457.69 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 6.73 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.42 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28592.66 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 6.74 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1，家庭股票配置 %） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 2.71 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（IG OAS %） | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（10Y 殖利率 %，無新觀測） | 4.57 | FRED API (series_id=DGS10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（10Y 實質殖利率 %，無新觀測） | 2.35 | FRED API (series_id=DFII10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（10Y breakeven %） | 2.24 | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps（較前次） | 2.0 | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（WTI 美元/桶） | 79.2 | FRED API (series_id=DCOILWTICO) | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料，CPI YoY %） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（5y5y 遠期通膨 %） | 2.21 | FRED API (series_id=T5YIFR) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（10Y 期限溢價（term premium）%，Kim-Wright） | 0.7788 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（序列自身 trailing 7 日變動） | 4.7 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（99th 分位 %） | 3.7 | FRED API (series_id=SOFR99) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（Fed 隔夜 repo 操作 transaction volume，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps（SOFR 與 IORB 皆為 2026-07-16 觀測） | -3.0 | FRED API repo_stress block | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr99_iorb_bps（兩腿皆為 2026-07-16 觀測） | 5.0 | FRED API repo_stress block | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.walcl | WALCL latest（Fed 資產負債表） | 6,743,028（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（ECB 資產） | 5,970,516（€5.97T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（BOJ 資產） | 6,395,509（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 18.77 | FRED API (series_id=VIXCLS) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of） | 18.77 | FRED API derived block (VIXCLS／SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（base 2026-07-10，window 7 日） | 24.88 | FRED API derived block (VIXCLS／SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（base 2026-07-10，window 7 日；comove=false） | -1.55 | FRED API derived block (VIXCLS／SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（銀行對 NBFI 放款） | 2004.0237（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（槓桿基金六合約淨部位，口） | -7562874 | CFTC TFF futures-only | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -78139 | CFTC TFF futures-only | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（^MOVE） | 70.88 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2342.6 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com，WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | MarketXLS，WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報摘要，WebSearch [primary: SEARCH]（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500，sp500_trend block） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100，ndx_drawdown block） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導，WebSearch [primary: SEARCH]（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | ahasignals／SPDR 持股，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth 報導，WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com／MacroMicro，WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA／Advisor Perspectives，WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com，WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag，WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／ycharts，WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查摘要，WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（DFEDTARU ok、DFEDTARL ok） | ✓ API |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok；repo_stress status ok） | ✓ API |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | 標售報導，WebSearch [primary: SEARCH]（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要，WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Bloomberg，WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC／interval fund 披露，WebSearch [primary: SEARCH]（30d） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報彙整，WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露，WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch AI／The Information，WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話，WebSearch [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce，WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報 quarterly_state＋30d event_scan，WebSearch [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合既有 bullet 披露＋WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q，WebSearch [primary: SEARCH]（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速 quarterly_state＋30d event_scan，WebSearch [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | BusinessWire 等，WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis.com，WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／Benzinga／StockTitan movers，WebSearch [primary: SEARCH]（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導（CNBC），WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR [primary]（egress 受限）＋openinsider，WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe daily market statistics，WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com／cryptobriefing，WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF.com，WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA／ETFGI，WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe insights，WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC monthly volume report | theocc.com，WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe／AInvest，WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS ok、vix_spx_comove block ok） | ✓ API |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 retail.margin_debt 來源，WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | neocloud／資料中心融資報導，WebSearch [primary: SEARCH]（30d） | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok；aggregation any）＋WebSearch 事件掃描 | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.08（原定來源 multpl.com） | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio（multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 41.52（原定來源 multpl.com） | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 trailing P/E ≈40 | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026（MarketXLS） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS ≈198bp 創紀錄、CoreWeave ≈665bp | Oracle CoreWeave CDS spread widening July 2026 | https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/（Real Investment Advice） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP +10.68% vs SPY +7.47% YTD | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-06-10 | 2026-07-20T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 36.40%（原定來源 State Street SPDR 持股） | S&P 500 top 10 concentration percent 2026 | https://ahasignals.com/sp500-concentration-risk/（AHA Signals） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| breadth.advance_decline | NYSE 2026-07-17 下跌約 2 倍於上漲、新高 241／新低 166 | NYSE advance decline breadth July 17 2026 | https://money.usnews.com/investing/news/articles/2026-07-17/wall-st-futures-fall-as-chip-selloff-gathers-pace-netflix-tumbles（U.S. News／Reuters） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（Fear）（原定來源 cnn.com） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed（MacroMicro） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-05 月資料）$1.416T、YoY +53.7% | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra（Advisor Perspectives） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |
| retail.aaii | AAII Bull 44.9% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number（YCharts） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 2.59、小幅 tail | US Treasury 10Y auction July 2026 bid to cover | https://cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/（Crypto Briefing） | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 會議隱含持平 ≈86.7% | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch（CryptoRank） | 2026-07-18 | 2026-07-20T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance（Bloomberg） | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio 18.8%，於 5% quarterly redemption cap 比例撥付 | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://whbl.com/2026/07/02/blue-owl-keeps-withdrawal-limits-even-as-redemption-pressure-modestly-eases/（WHBL／Reuters） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計約 $700B、仍上修（Q1 財報季） | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html（Yahoo Finance） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic ≈$47B／OpenAI ≈$25B 年化 run-rate | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 +13–18% QoQ | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html（TrendForce） | 2026-07-03 | 2026-07-20T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex 約 $700B vs AI 終端營收低百億級 | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| speculation.ai_rename_spac | EVTV 改名 Azio AI Holdings（AZIO）並更換 ticker | AI rename ticker change July 2026 Azio EVTV | https://www.businesswire.com/news/home/20260710628386/en/Azio-AI-Holdings-Inc.-Nasdaq-EVTV-to-Begin-Trading-Under-New-Ticker-Symbol-AZIO-Completing-Corporate-Rebrand（Business Wire） | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD 約 200 檔 IPO、募資 $141.2B | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/（StockAnalysis） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot 0 件 | microcap 100% single day quantum AI moonshot July 2026 | Finviz／Benzinga／StockTitan movers screener | — | 2026-07-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 投資人會議、估值 $965B、可能 10 月掛牌 | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html（CNBC） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 cluster 0 件（EDGAR 一手 URL 因 egress 受限無法取得） | insider Form 4 cluster AI leaders July 2026 openinsider | SEC EDGAR／openinsider | — | 2026-07-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.73（日讀數） | Cboe equity put call ratio July 2026 | https://www.cboe.com/markets/us/options/market-statistics/daily/（Cboe） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM ≈$198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing） | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 推出 6 檔 2x 單一股票 ETF（GOOGL／AMZN／META／AAPL） | single-stock leveraged ETF launch July 2026 Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html（GlobeNewswire） | 2026-07-07 | 2026-07-20T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權成交 ≈63% | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/（Cboe） | 2026-02-28 | 2026-07-20T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月成交 1,603,491,559 口、YoY +45% | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 145.13、VIX ≈16.5 期限結構 contango | VIX term structure SKEW July 2026 | https://www.ainvest.com/news/0dte-volatility-drives-market-strategies-2026-2602/（AInvest） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-05 月資料）$1.416T、YoY +53.7%（交叉確認，不重複計入） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra（Advisor Perspectives） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |

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

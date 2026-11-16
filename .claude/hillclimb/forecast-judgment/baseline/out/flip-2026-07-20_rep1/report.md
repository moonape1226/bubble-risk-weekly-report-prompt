> [DRY RUN] this report was not committed to archive.

# 2026-07-20 AI 泡沫破裂預測報告
報告日期：2026-07-20｜ISO 週次：2026-W30｜預測窗口：2026-07-20 → 2027-01-18｜前次基準：report-2026-07-16（4天前）

## 結論

**結論：yes**

R1 與 R3 的傳導鏈仍在推進：NASDAQ-100 自 2026-06-02 高點的回撤由前次的 3.78% 擴大至 6.74%（2026-07-17），同週 VIX 7 日上升 24.88%、AI 借款人 CDS 創紀錄（Oracle 5yr ≈198bp、CoreWeave ≈665bp），疊加 CAPE 41.52、margin debt YoY +53.7% 與 NAAIM 95.64 的極端部位。2026-07-16 之後的新資料全部指向壓力加深，沒有任何一項削弱前次 yes 的路徑分析，依翻轉紀律維持 yes。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 28,592.66（2026-07-17），252 交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 6.74%；R1 門檻水位 22,995.45，自最新收盤再下跌約 19.58% 即觸發（`valuation.ndx_drawdown`）。前次（report-2026-07-16）記錄的回撤為 3.78%，四天內擴大約 3 個百分點；2026-07-17 NYSE 下跌家數約為上漲家數 2 倍、新聞標題為晶片股賣壓擴大（`breadth.advance_decline`）。S&P 500 7,457.69（2026-07-17），較前次 −1.01%，但仍高於 200 日均線 6.73%、高於 52 週均線 8.42%（`valuation.sp500_trend`），表示均值回歸空間仍大。VIX 18.77（2026-07-17），7 日窗口（2026-07-10 → 2026-07-17）VIX +24.88%、S&P 500 −1.55%，為正常的反向共動、非 crowded-optionality 讀數（`structural.vix_spx_comove`）。脆弱度：S&P 500 trailing P/E 32.08、Shiller CAPE 41.52（2026-07-17，`valuation.sp500_pe_cape`），Mag 7 加權 P/E ≈40（2026-05-15，`valuation.mag7_multiples`），Top-10 集中度 36.40%（`breadth.top10_concentration`）；槓桿部位 margin debt $1.416T、YoY +53.7%（2026-05 月資料，`retail.margin_debt`）落在歷史頂部區間，NAAIM 95.64（2026-07-15，`retail.naaim`），美國槓桿 ETF AUM ≈$198B（`structural.leveraged_etf_aum`）。

**判讀：** 距 R1 仍需約 19.58% 的額外跌幅，尚未接近；但回撤正在擴大，且高槓桿（margin debt YoY +53.7%、NAAIM 95.64、槓桿 ETF AUM ≈$198B）意味一旦跌勢延續將出現強制去槓桿放大。窗口內的推升因素：Q2／Q3 兩次 hyperscaler 財報若對 capex 回報給出負面訊號、AI 信用利差進一步走闊外溢至股權，或 2026 年 10 月可能的 Anthropic IPO 帶來大規模供給。

### R2 資本支出收縮

本次可得的 capex 證據為彙總口徑：hyperscaler 2026 年 capex 合計 ≈$700B，且仍在上修（2026-05-15，Q1 財報季後，`ai.hyperscaler_capex`）。逐家指引如下（carry-forward，stock-of-state）：

- Microsoft：最新正式指引數值未在本次證據逐家列出；彙總口徑方向為上修（Q1 財報季，2026-05-15）。
- Alphabet：同上，彙總口徑方向為上修（Q1 財報季，2026-05-15）。
- Amazon：同上，彙總口徑方向為上修（Q1 財報季，2026-05-15）。
- Meta：同上，彙總口徑方向為上修（Q1 財報季，2026-05-15）。

目前四家中下修家數為 0。下一次財報日期未在本次證據中取得，但 182 天窗口必然涵蓋每家兩次季報（Q2 與 Q3）。需求側仍強：伺服器 DRAM 3Q26 合約價 QoQ +13–18%（2026-07-03，`ai.compute_supply_demand`），Anthropic run-rate ≈$47B、OpenAI ≈$25B（2026-05-15，`ai.openai_anthropic_revenue`）；但年化 capex ≈$700B 對 AI 終端營收僅低百億級（分母：top-4 hyperscaler 彙總，`ai.revenue_capex_gap`），AI 營收對 capex 缺口（revenue-to-capex gap）仍極大。

**判讀：** R2 是三條路徑中最遠的一條——指引方向仍為上修、零家下修。要在窗口內成立，需要兩家在 Q2 或 Q3 財報中主動下修，這通常發生在 R1 股價重挫或 R3 融資管道收縮之後，屬於下游確認而非起點。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）正在往信用端重定價方向移動：Oracle 5yr CDS ≈198bp 創紀錄、CoreWeave CDS ≈665bp（2026-07-16，`valuation.ai_credit_schism`）。CoreWeave 以 AI 算力為主業，是 R3 規模門檻的主要候選；其負債規模、近期到期與再融資時間表未在本次證據中取得。Oracle 雖為 AI 資本支出大戶，但主業並非 AI 資料中心，不直接構成 R3 借款人。非銀行端：私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）已出現實際事件——Blue Owl OCIC Q2 redemption-request ratio 18.8%，在 5% quarterly redemption cap 下發生 gate proration / breach（2026-07-02，`monetary.private_credit_liquidity`）。整體信用仍緊：HY OAS 2.71%、IG OAS 0.78%（2026-07-16，`monetary.hy_oas`、`monetary.ig_oas`），repo 資金壓力（SOFR−IORB）為 −3bp、SRF 動用為 0（`monetary.repo_stress_srf`）。本次 AI infrastructure debt financing / vendor-financing loops 的 30 日掃描無新披露，未見付款違約、covenant waiver 或 distressed exchange 的報導。

**判讀：** 尚無 R3 事件，但 CoreWeave CDS ≈665bp 已是高收益困境邊緣的定價，且私募信貸端出現 gate proration / breach。要在窗口內成立，需要一家 ≥ 50 億美元負債的 AI 算力借款人在再融資受阻後違約或進行 distressed exchange；信用市場的這種走闊若持續，最可能先透過 R1 傳導。

## 支持 yes 的證據

- [R1] NASDAQ-100 回撤由前次 3.78% 擴大至距 52 週高點回撤 6.74%（2026-07-17 收盤 28,592.66 vs 2026-06-02 高點 30,660.60），跌勢在加速而非收斂（`valuation.ndx_drawdown`）。
- [R3] AI 借款人信用端開始重定價：Oracle 5yr CDS ≈198bp 創紀錄、CoreWeave ≈665bp（2026-07-16），股權端仍在高位，屬 equity-vs-credit schism 的後期型態（`valuation.ai_credit_schism`）。
- [整體] 槓桿與部位極端：margin debt $1.416T、YoY +53.7%（2026-05 月資料），達 1999／2007／2021 頂部附近的 YoY 區間；NAAIM 95.64（2026-07-15）；槓桿 ETF AUM ≈$198B（2026-07-10），一旦下跌將放大強制去槓桿（`retail.margin_debt`、`retail.naaim`、`structural.leveraged_etf_aum`）。
- [R3] 私募信貸贖回壓力已有實際 gate proration / breach：Blue Owl OCIC Q2 redemption-request ratio 18.8% 遠超 5% quarterly redemption cap（2026-07-02），非銀行融資管道收縮會傳導至 AI 資料中心融資（`monetary.private_credit_liquidity`）。
- [R1] 估值處於歷史極端：Shiller CAPE 41.52、trailing P/E 32.08（2026-07-17），Mag 7 加權 P/E ≈40；S&P 500 仍高於 200 日均線 6.73%，下行空間大（`valuation.sp500_pe_cape`、`valuation.mag7_multiples`、`valuation.sp500_trend`）。
- [R1] 晶片股賣壓擴散：2026-07-17 NYSE 下跌家數約為上漲 2 倍；VIX 7 日 +24.88% 至 18.77；CNN Fear & Greed 37（Fear，2026-07-17）（`breadth.advance_decline`、`structural.vix_spx_comove`、`retail.fear_greed`）。
- [R2] AI 營收對 capex 缺口極大：年化 capex ≈$700B vs AI 終端營收低百億級（分母：top-4 hyperscaler 彙總），投資回收依賴持續的成長敘事（`ai.revenue_capex_gap`）。

## 支持 no 的證據

- [整體] 基準率：182 天內 NASDAQ-100 回撤 ≥ 25%、兩家 hyperscaler 下修 capex、或大型 AI 算力違約都屬罕見事件；目前距 R1 門檻 22,995.45 仍需再跌約 19.58%（`valuation.ndx_drawdown`）。
- [R2] hyperscaler 2026 capex ≈$700B 且仍在上修（2026-05-15），四家下修家數為 0，R2 最遠（`ai.hyperscaler_capex`）。
- [整體] 廣義信用與資金市場尚無壓力：HY OAS 2.71%、IG OAS 0.78%（2026-07-16）；SOFR−IORB −3bp、SRF 動用 0（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`）。
- [R2] AI 需求側仍強：伺服器 DRAM 3Q26 合約價 QoQ +13–18%（2026-07-03）；Anthropic run-rate ≈$47B、OpenAI ≈$25B（`ai.compute_supply_demand`、`ai.openai_anthropic_revenue`）。
- [整體] 廣度未全面崩壞：RSP YTD +10.68% 優於 SPY +7.47%（2026-06-10），NYSE 新高 241 仍多於新低 166（2026-07-17），顯示資金輪動而非全面撤出（`breadth.rsp_spy`、`breadth.advance_decline`）。
- [R1] 投機指標並非全面狂熱：Cboe equity put/call 0.73（2026-07-17），高於 0.50 的 call-heavy 區間；本週合格 microcap moonshot 0 件（`speculation.equity_put_call`、`speculation.microcap_moonshots`）。

## 與前期比較

前次結論：yes（report-2026-07-16）
本次結論：維持

- NASDAQ-100 回撤由 3.78% 擴大至 6.74%（資料日 2026-07-17，`valuation.ndx_drawdown`）：方向強化 R1 路徑，不構成轉向 no 的依據。
- VIX 由 16.73 升至 18.77、S&P 500 較前次 −1.01%（2026-07-17，`structural.vix_spx_comove`、`valuation.sp500_trend`）：壓力加深，與前次結論一致。
- CNN Fear & Greed 37（Fear，2026-07-17，`retail.fear_greed`）與晶片股賣壓（`breadth.advance_decline`）：情緒轉弱，屬 R1 進行中的訊號，而非緩解。
- CME FedWatch 7/29 會議維持利率的定價 ≈86.7%（2026-07-18，`monetary.fedwatch`）：短期無降息緩衝，不削弱 yes。
- HY OAS、IG OAS、DGS10、SOFR 等於前次以來無新觀測（no_new_obs），信用端的 no 證據沒有新增強化；2026-07-16 之後沒有任何來源改變路徑分析朝向 no，因此 flip_evidence 為空。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

非成功但不影響結論的來源（✗ NOT DISCLOSED）：`valuation.analyst_tp_decomposition`、`retail.social_sentiment`、`institutional.bofa_jpm_survey`、`ai.token_growth`、`ai.customer_concentration_rpo`、`ai.hyperscaler_financing_mix`、`ai.depreciation_life`、`ai.capital_cycle`、`structural.global_leveraged_approvals`、`structural.ai_infrastructure_debt`。其中 `structural.ai_infrastructure_debt` 與 `ai.hyperscaler_financing_mix` 的缺口與 R3 直接相關：若有新的大額 neocloud 融資或 SPV 結構，可能進一步強化 yes；若有大額再融資順利完成則偏向 no。兩者無披露不足以改變答案。

其他註記：`speculation.insider_form4` 的 0 件結果來自 openinsider 篩選，SEC EDGAR 一手 URL 因 egress 受限未能逐筆核對；即使有內部人賣出 cluster，也只屬情緒證據，不會改變答案。evidence 檔對 `structural.treasury_basis_trade` 的描述為三個 script 區塊 fetch_failed，但 macro artifact 顯示 cftc_lev_funds、move_index、ofr_repo 均為 status ok，本報告以 artifact 為準記為 ✓ API。R2 的 capex 證據為彙總口徑，缺逐家正式指引數值。10Y 分解：ΔDGS10 0.0bp、ΔDFII10 0.0bp、ΔT10YIE +2.0bp，判讀為不可判（視窗不一致）；DGS10 與 DFII10 為 stale_series（無新觀測），T10YIE 已更新。

最大不確定性：

1. Q2 hyperscaler 財報（日期未在本次證據中，窗口內必然發生）：若 capex 繼續上修且 AI 營收成長有據，偏向 no；若出現首家下修或 capex 回報質疑，強化 R1／R2 的 yes。
2. CoreWeave 等 AI 算力借款人的再融資：其負債規模與到期時間表本次未取得；CDS ≈665bp 已反映困境風險，若一級市場關閉則 R3 推向 yes，若順利展延則偏向 no。
3. Anthropic IPO（可能 10 月掛牌、估值 $965B，2026-07-15）：大型供給可能在高槓桿環境中壓抑 AI 股價（偏 yes），但若認購強勁也可能延續 AI 敘事（偏 no）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 32.08 | https://www.multpl.com/s-p-500-pe-ratio | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE | 41.52 | https://www.multpl.com/shiller-pe | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 trailing P/E | 40（≈） | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026 | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest | 7457.69 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 6.73 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.42 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較前次 %） | -1.01 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28592.66 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 6.74 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS | 198（≈，bp，創紀錄） | https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/ | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave CDS | 665（≈，bp） | https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/ | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP vs SPY YTD | RSP +10.68% vs SPY +7.47% | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ | 2026-06-10 | 2026-07-20T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 | 36.40% | https://ahasignals.com/sp500-concentration-risk/ | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| breadth.advance_decline | NYSE 新高／新低 | 241 / 166（下跌家數約為上漲 2 倍） | https://money.usnews.com/investing/news/articles/2026-07-17/wall-st-futures-fall-as-chip-selloff-gathers-pace-netflix-tumbles | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed | 37（Fear） | https://en.macromicro.me/charts/50108/cnn-fear-and-greed | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-05 月資料） | $1.416T，YoY +53.7% | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra | 2026-05-31 | 2026-07-20T09:30:00+08:00 |
| retail.aaii | AAII Bullish | 44.9% | https://www.aaii.com/sentimentsurvey | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1） | 45.76（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-20T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index | 95.64 | https://ycharts.com/indicators/naaim_number | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75（%） | FRED API (series_id=DFEDTARU) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5（%） | FRED API (series_id=DFEDTARL) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.71（%） | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.78（%） | FRED API (series_id=BAMLC0A0CM) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.57（%） | FRED API (series_id=DGS10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.35（%） | FRED API (series_id=DFII10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.24（%） | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | 2.0（bp） | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 79.2（USD） | FRED API (series_id=DCOILWTICO) | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46（%） | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.21（%） | FRED API (series_id=T5YIFR) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.7788（%） | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 約 7 日） | 4.7（bp） | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.62（%） | FRED API (series_id=SOFR) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.7（%） | FRED API (series_id=SOFR99) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65（%） | FRED API (series_id=IORB) | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用） | 0.0（十億美元） | FRED API (series_id=RPONTTLD) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover | 2.59（小幅 tail） | https://cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/ | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 維持利率定價 | 86.7%（≈） | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch | 2026-07-18 | 2026-07-20T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,743,028（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,970,516（€5.97T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,395,509（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 | 1.4 兆元 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio | 18.8%（5% quarterly redemption cap 下 gate proration / breach） | https://whbl.com/2026/07/02/blue-owl-keeps-withdrawal-limits-even-as-redemption-pressure-modestly-eases/ | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計（Q1 財報季，仍上修） | 700（≈，十億美元） | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic／OpenAI 年化 run-rate | 47／25（≈，十億美元） | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 QoQ | +13–18% | https://www.trendforce.com/presscenter/news/20260703-13134.html | 2026-07-03 | 2026-07-20T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex vs AI 終端營收（分母：top-4 hyperscaler 彙總） | 700（≈，十億美元）vs 低百億級 | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| speculation.ai_rename_spac | EVTV→Azio AI（AZIO）改名 | 1 件 | https://www.businesswire.com/news/home/20260710628386/en/Azio-AI-Holdings-Inc.-Nasdaq-EVTV-to-Begin-Trading-Under-New-Ticker-Symbol-AZIO-Completing-Corporate-Rebrand | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD US IPO 檔數／募資 | 200（≈）檔，$141.2B | https://stockanalysis.com/ipos/2026/ | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 投資人會議估值 | $965B（可能 10 月掛牌） | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call（日讀數） | 0.73 | https://www.cboe.com/markets/us/options/market-statistics/daily/ | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM | 198（≈，十億美元） | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 新上市 2x 單一個股 ETF（GOOGL/AMZN/META/AAPL） | 6 檔 | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html | 2026-07-07 | 2026-07-20T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權成交 | 63%（≈） | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/ | 2026-02-28 | 2026-07-20T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月總成交口數 | 1,603,491,559（YoY +45%） | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW／VIX 期限結構 | 145.13（VIX 約 16.5，contango） | https://www.ainvest.com/news/0dte-volatility-drives-market-strategies-2026-2602/ | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 18.77 | FRED API (series_id=VIXCLS) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 18.77 | FRED API (series_id=VIXCLS, SP500 共用日) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（2026-07-10 → 2026-07-17） | 24.88 | FRED API (series_id=VIXCLS, SP500 共用日) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（2026-07-10 → 2026-07-17） | -1.55 | FRED API (series_id=VIXCLS, SP500 共用日) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt cross-ref（2026-05 月資料） | $1.416T，YoY +53.7% | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra | 2026-05-31 | 2026-07-20T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2,004.0237（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位） | -7,562,874（口） | CFTC TFF futures-only | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -78,139（口） | CFTC TFF futures-only | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 70.88 | Yahoo Finance chart API (^MOVE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2342.6（十億美元） | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com，WebSearch primary | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | MarketXLS，WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報，WebSearch primary；搜尋完成，無同季度合格上調 | ✗ NOT DISCLOSED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py，FRED SP500 | ✓ API（sp500_trend ok） |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py，FRED NASDAQ100 | ✓ API（ndx_drawdown ok） |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導，WebSearch primary（14 日） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | ahasignals，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | US News 市場報導，WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | MacroMicro 轉載 CNN，WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | Advisor Perspectives／FINRA，WebSearch（月頻 carry-forward） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com，WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag，WebSearch；搜尋完成，無顯著討論 | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py，FRED BOGZ1FL153064486Q | ✓ API（BOGZ1FL153064486Q ok） |
| retail.naaim | 散戶｜NAAIM Exposure Index | ycharts，WebSearch primary | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查，WebSearch；搜尋完成，無當期新調查 | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py，FRED API | ✓ API（DFEDTARU ok／DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py，FRED API | ✓ API（BAMLH0A0HYM2 ok） |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py，FRED API | ✓ API（BAMLC0A0CM ok） |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py，FRED API | ✓ API（DGS10 ok） |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py，FRED API | ✓ API（DFII10 ok） |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py，FRED API（FRED 直取） | ✓ API（T10YIE ok） |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py，FRED API | ✓ API（DCOILWTICO ok） |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py，FRED API（yoy_pct） | ✓ API（CPIAUCSL ok） |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py，FRED API | ✓ API（T5YIFR ok） |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py，FRED API | ✓ API（THREEFYTP10 ok） |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py，FRED API，repo_stress block | ✓ API（SOFR ok／SOFR99 ok／IORB ok／RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | CryptoBriefing／TreasuryDirect，WebSearch primary（14 日） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 轉載，WebSearch primary | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py，FRED API | ✓ API（WALCL ok） |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py，FRED API | ✓ API（ECBASSETSW ok／JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Bloomberg，WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露，WebSearch primary（30 日） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報彙總報導，WebSearch（stock-of-state carry-forward） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露，WebSearch；本季無披露 | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch AI，WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話會議，WebSearch primary；無合格披露 | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce，WebSearch primary | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報＋30 日融資事件掃描，WebSearch primary；兩組件皆無披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露，WebSearch primary（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q，WebSearch primary（30 日）；無變動披露 | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速＋30 日進出場事件，WebSearch；兩組件皆無披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | WebSearch（7 日） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis.com，WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／Benzinga／StockTitan movers，WebSearch primary（7 日） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導（CNBC），WebSearch（30 日） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR primary／openinsider，WebSearch（14 日） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe daily market statistics，WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing，WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF.com，WebSearch（30 日） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA，WebSearch（7 日）；無英文披露 | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe insights，WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume | theocc.com，WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe／AInvest，WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py，FRED VIXCLS＋SP500 | ✓ API（VIXCLS ok／vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | Advisor Perspectives／FINRA 交叉引用，WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | WebSearch primary（30 日）；無新披露 | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py，FRED API | ✓ API（LNFACBW027SBOG ok） |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py 三個非 FRED 區塊 | ✓ API（cftc_lev_funds ok／move_index ok／ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.08（原定來源：multpl.com） | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio（multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 41.52（原定來源：multpl.com） | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 trailing P/E 約 40 | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026（MarketXLS） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS 約 198bp 創紀錄、CoreWeave 約 665bp | Oracle CoreWeave CDS spread widening July 2026 | https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/（RIA） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP +10.68% vs SPY +7.47% YTD | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-06-10 | 2026-07-20T09:30:00+08:00 |
| breadth.top10_concentration | Top-10 集中度 36.40%（原定來源：State Street SPDR 持股） | S&P 500 top 10 concentration percent 2026 | https://ahasignals.com/sp500-concentration-risk/（AHA Signals） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| breadth.advance_decline | NYSE 下跌約為上漲 2 倍、NH 241／NL 166 | NYSE advance decline breadth July 17 2026 | https://money.usnews.com/investing/news/articles/2026-07-17/wall-st-futures-fall-as-chip-selloff-gathers-pace-netflix-tumbles（US News／Reuters） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（原定來源：cnn.com） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed（MacroMicro） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-05 月資料）$1.416T、YoY +53.7%（原定來源：FINRA） | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra（Advisor Perspectives） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |
| retail.aaii | AAII Bullish 44.9% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64（原定來源：naaim.org） | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number（YCharts） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 2.59、小幅 tail（原定來源：TreasuryDirect） | US Treasury 10Y auction July 2026 bid to cover | https://cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/（Crypto Briefing） | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| monetary.fedwatch | 7/29 FOMC 維持利率定價約 86.7%（原定來源：CME FedWatch） | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch（CryptoRank） | 2026-07-18 | 2026-07-20T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance（Bloomberg） | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio 18.8%，5% quarterly redemption cap 下 gate proration / breach | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://whbl.com/2026/07/02/blue-owl-keeps-withdrawal-limits-even-as-redemption-pressure-modestly-eases/（WHBL／Reuters） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計約 $700B、仍上修（Q1 財報季） | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html（Yahoo Finance） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 約 $47B／OpenAI 約 $25B run-rate | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 QoQ +13–18% | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html（TrendForce） | 2026-07-03 | 2026-07-20T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex 約 $700B vs AI 終端營收低百億級 | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| speculation.ai_rename_spac | EVTV→Azio AI（AZIO）改名 | AI rename ticker change July 2026 Azio EVTV | https://www.businesswire.com/news/home/20260710628386/en/Azio-AI-Holdings-Inc.-Nasdaq-EVTV-to-Begin-Trading-Under-New-Ticker-Symbol-AZIO-Completing-Corporate-Rebrand（Business Wire） | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD 約 200 檔 IPO、$141.2B（原定來源：Renaissance） | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/（StockAnalysis） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot 0 件 | microcap 100% single day quantum AI moonshot July 2026 | Finviz／Benzinga／StockTitan movers screener | — | 2026-07-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 投資人會議、估值 $965B、可能 10 月掛牌 | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html（CNBC） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 cluster 0 件（EDGAR 一手 URL 因 egress 受限未能取得） | insider Form 4 cluster AI leaders July 2026 openinsider | SEC EDGAR／openinsider | — | 2026-07-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.73（日讀數） | Cboe equity put call ratio July 2026 | https://www.cboe.com/markets/us/options/market-statistics/daily/（Cboe） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 約 $198B（原定來源：etf.com／ETFGI） | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing） | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x GOOGL/AMZN/META/AAPL 上市 | single-stock leveraged ETF launch July 2026 Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html（GlobeNewswire） | 2026-07-07 | 2026-07-20T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 約 63%（原定來源：Cboe daily statistics） | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/（Cboe） | 2026-02-28 | 2026-07-20T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月 1,603,491,559 口、YoY +45% | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 145.13、VIX 約 16.5 contango | VIX term structure SKEW July 2026 | https://www.ainvest.com/news/0dte-volatility-drives-market-strategies-2026-2602/（AInvest） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-05 月資料）$1.416T、YoY +53.7%（cross-ref retail.margin_debt） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra（Advisor Perspectives） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |

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

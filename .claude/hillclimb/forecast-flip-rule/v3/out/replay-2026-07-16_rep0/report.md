> [DRY RUN] this report was not committed to archive.
# 2026-07-16 AI 泡沫破裂預測報告
報告日期：2026-07-16｜ISO 週次：2026-W29｜預測窗口：2026-07-16 → 2027-01-14｜前次基準：report-2026-07-13（3天前）

## 結論

**結論：no**

三條路徑都沒有已在進行中的證據：NASDAQ-100 距 52 週高點僅回撤 3.78%，還要再跌約 22.06% 才觸及 R1 門檻；hyperscaler 2026 capex 彙總約 $700B 且仍在上修（`ai.hyperscaler_capex`），R2 方向相反。R3 方面雖有 Oracle 5yr CDS 約 198bp 的 AI 信用定價分歧（`valuation.ai_credit_schism`），但 CoreWeave 仍能取得 $8.5B DDTL 新融資（`structural.ai_infrastructure_debt`），沒有付款違約或 distressed exchange 跡象；泡沫程度很高，但 182 天內破裂的觸發與傳導證據不足以推翻基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

FRED `NASDAQ100` 最新收盤 29502.6（2026-07-15）；252 個交易日最高收盤 30660.6（2026-06-02）；距 52 週高點回撤 3.78%（`valuation.ndx_drawdown`）。R1 門檻水位為 22995.45，自最新收盤還需再下跌約 22.06% 才觸及。價格面延伸程度：S&P 500 7572.4（2026-07-15）高於 200 日均線 8.51%、高於 52 週均線 10.25%（`valuation.sp500_trend`）。波動與避險面平靜：VIX 15.67（2026-07-15），7 日窗口（2026-07-08 → 2026-07-15）VIX −7.28%、S&P 500 +1.20%，未出現同漲的 crowded-optionality 讀數（`structural.vix_spx_comove`）；MOVE 68.48（2026-07-15，較 2026-07-13 的 77.77 回落）（`structural.treasury_basis_trade`）。估值高檔：S&P 500 trailing P/E 32.59、Shiller CAPE 42.18（2026-07-15，`valuation.sp500_pe_cape`），代表一旦觸發，下跌幅度可能很大，但本身不構成時點證據。

**判讀：** R1 距離很遠（再跌約 22% 才觸及），目前市場仍接近高點、VIX／MOVE 都在低檔；要在窗口內觸發，需要信用或融資端出現明顯的傳導事件（例如 R3 型違約、hyperscaler 指引轉向，或 repo／美債市場失序引發強制去槓桿），而這些目前都還沒出現。

### R2 資本支出收縮

本次取得的 capex 指引為彙總層級：hyperscaler 2026 年 capex 合計約 $700B，來源描述為仍在上修（2026-05-15，`ai.hyperscaler_capex`）。逐家狀態如下：
- Microsoft：最新正式指引數值本次未逐家取得；依彙總來源，方向為上修，沒有下修報導。
- Alphabet：最新正式指引數值本次未逐家取得；依彙總來源，方向為上修，沒有下修報導。
- Amazon：最新正式指引數值本次未逐家取得；依彙總來源，方向為上修，沒有下修報導。
- Meta：最新正式指引數值本次未逐家取得；依彙總來源，方向為上修，沒有下修報導。

截至目前，四家中下修家數為 0。182 天窗口涵蓋至少兩次季報，但具體日期本次沒有取得來源確認。需求面佐證：伺服器 DRAM 2Q26 合約價季增 58–63%（2026-06-02，`ai.compute_supply_demand`），顯示算力供給仍然吃緊，不是需求消化；Anthropic 年化營收約 $47B、OpenAI 約 $25B（2026-05-15，`ai.openai_anthropic_revenue`）。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 capex 約 $700B，對比來源所述的 AI 終端營收，仍落在低百億級（2026-05-15，`ai.revenue_capex_gap`；分母為來源所述的 hyperscaler 彙總，沒有逐家拆分，Oracle 與 neocloud 本次沒有獨立披露、未納入），缺口極大但沒有新組件披露，本次不判斷擴大或收斂。

**判讀：** R2 目前方向相反（集體上修），而且至少需要兩家在窗口內正式下修。可能推升 R2 的情境是 R1 型大幅回撤或融資成本急升，迫使管理層在下一次季報收縮指引；目前沒有任何一家出現下修前兆。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）：Oracle 5yr CDS 約 198bp，對比 CDX.NA.IG 約 95bp（2026-07-10，`valuation.ai_credit_schism`），信用端對 AI 曝險的定價已明顯寬於投資級基準。不過 Oracle 的主業不是 AI 資料中心／算力，不直接符合 R3 的借款人定義。AI infrastructure debt financing / vendor-financing loops：CoreWeave 取得 $8.5B DDTL，Nvidia 相關循環融資曝險約 $24.9B（2026-07-12，`structural.ai_infrastructure_debt`）。CoreWeave 是最可能符合 R3 規模門檻的借款人，但其負債總額、近期到期與再融資需求本次沒有取得來源佐證（數字未確立）。本次也沒有任何來源提及付款違約、寬限期、covenant waiver、distressed exchange 或 going-concern 字樣。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）：Blue Owl OCIC Q2 redemption-request ratio 18.8%，quarterly redemption cap（5%）出現 gate proration / breach（2026-07-02，`monetary.private_credit_liquidity`），代表非銀行資金端承壓。整體信用：HY OAS 2.72%、IG OAS 0.79%（2026-07-14，`monetary.hy_oas`、`monetary.ig_oas`），仍處於緊縮狀態。

**判讀：** R3 有早期壓力訊號（AI 發債人 CDS 偏寬、私募信貸 gate proration），但最大的候選借款人剛完成新融資，顯示融資市場仍然開放，距離破產、違約或 distressed exchange 還很遠。要在窗口內觸發，需要 neocloud 融資管道關閉並疊加大額到期，或客戶承諾違約；這些本次都沒有取得證據。

## 支持 yes 的證據

- [R3] Oracle 5yr CDS 約 198bp，對比 CDX.NA.IG 約 95bp（2026-07-10），AI 曝險發債人的信用端已開始重定價，與股權端高估值形成 AI 信用定價分歧，屬於後期訊號 `valuation.ai_credit_schism`
- [R3] Blue Owl OCIC Q2 redemption-request ratio 18.8%，quarterly redemption cap 出現 gate proration / breach（2026-07-02），私募信貸贖回壓力已經實際發生，不只是結構存在 `monetary.private_credit_liquidity`
- [R3] CoreWeave $8.5B DDTL 與 Nvidia 循環融資約 $24.9B（2026-07-12），AI infrastructure debt financing / vendor-financing loops 持續擴大，一旦需求鬆動，槓桿會放大損失 `structural.ai_infrastructure_debt`
- [整體] FINRA margin debt $1.416T、YoY +53.7%（2026-05 月資料），槓桿買盤快速累積，下跌時可能引發強制去槓桿 `retail.margin_debt`
- [R1] Shiller CAPE 42.18、S&P 500 trailing P/E 32.59（2026-07-15），估值處於極端水位，觸發後下行空間大 `valuation.sp500_pe_cape`
- [R1] US 槓桿 ETF 總 AUM 約 $198B（2026-07-10），加上首檔美股掛牌 SK hynix 2x 個股槓桿 ETF 上市（2026-07-14），結構性槓桿持續擴張 `structural.leveraged_etf_aum` `structural.us_single_stock_etf`
- [R1] NAAIM Exposure 82.95（2026-07-08），主動經理人部位偏擁擠 `retail.naaim`

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 3.78%（2026-07-15 收盤 29502.6 vs 2026-06-02 高點 30660.6），距 R1 門檻 22995.45 還需再跌約 22.06% `valuation.ndx_drawdown`
- [R2] hyperscaler 2026 capex 合計約 $700B，且仍在上修（2026-05-15），四家中沒有任何一家下修，R2 方向相反 `ai.hyperscaler_capex`
- [R2] 伺服器 DRAM 2Q26 合約價季增 58–63%（2026-06-02），算力供給吃緊，看不到需求消化或產能過剩 `ai.compute_supply_demand`
- [R3] HY OAS 2.72%、IG OAS 0.79%（2026-07-14），整體信用利差仍然緊縮，信用市場沒有系統性重定價 `monetary.hy_oas` `monetary.ig_oas`
- [R3] CoreWeave 仍能取得 $8.5B DDTL（2026-07-12），最大的 R3 候選借款人融資管道暢通，與違約前兆相反 `structural.ai_infrastructure_debt`
- [整體] repo 資金壓力（SOFR−IORB）為 −2bp、SOFR99−IORB 7bp（2026-07-14），SRF 動用僅 $0.102bn（2026-07-15）；MOVE 68.48（2026-07-15），融資與美債波動都沒有失序跡象 `monetary.repo_stress_srf` `structural.treasury_basis_trade`
- [R1] VIX 15.67（2026-07-15），7 日 VIX −7.28%、S&P 500 +1.20%，沒有同漲警訊；CNN Fear & Greed 46（2026-07-15），情緒不是極度貪婪 `structural.vix_spx_comove` `retail.fear_greed`
- [整體] RSP YTD +9.67% 跑贏 SPY +8.38%（2026-06-26），漲勢廣度擴散，不是只靠少數權值股支撐 `breadth.rsp_spy`

## 與前期比較

前次結論：無前次預測（report-2026-07-13 為舊格式評分報告）

前次為舊格式評分報告，不轉換為 yes/no，所以本次沒有翻轉判斷，flip_evidence 為空。自 2026-07-13 以來的主要數據變化：
- MOVE 由 77.77 降至 68.48（2026-07-15），美債波動回落。
- NASDAQ-100 由 29264.1（2026-07-13）回升至 29502.6（2026-07-15）；S&P 500 較前次 +0.76%。
- 10Y 殖利率 −4bp 至 4.58%、DFII10 −3bp、T10YIE −3bp；HY OAS +3bp 至 2.72%，變動有限。
- SRF 動用由 0 增至 $0.102bn（2026-07-15），規模微小，不是失序訊號。

## 資料缺漏與不確定性

FETCH FAILED 來源：
- `speculation.insider_form4`（⛔ FETCH FAILED）：SEC EDGAR 一手 Form 4 URL 因 egress 受限無法取得，因此不能確認「0 件」，也不能當成 0 件篩選結果。內部人賣壓屬於情緒佐證，不在 R1–R3 的傳導主路徑上，這個缺口不太可能改變答案。

✗ NOT DISCLOSED（篩選完成但無合格披露，不作為證據）：`valuation.analyst_tp_decomposition`、`retail.social_sentiment`、`institutional.bofa_jpm_survey`、`ai.token_growth`、`ai.customer_concentration_rpo`、`ai.hyperscaler_financing_mix`、`ai.depreciation_life`、`ai.capital_cycle`、`speculation.upcoming_ai_ipos`、`structural.global_leveraged_approvals`。其中 hyperscaler 融資結構（capex vs FCF / 發債）、backlog 重複計算風險（RPO double-counting）與折舊年限變動（depreciation useful-life change）的缺漏，會讓 R3／R2 的盈餘品質與融資轉變判讀比較不完整；資本週期階段（capital cycle stage）因兩個組件都沒有披露，本次不判定週期階段。

其他資料限制：
- evidence 中 `structural.treasury_basis_trade` 的 WebSearch 列記載 MOVE 77.77（並註記 script 區塊 fetch_failed），但本次 macro artifact 的 `cftc_lev_funds`、`move_index`、`ofr_repo` 三個區塊都是 `status: ok`，而 77.77 正是 artifact 中 2026-07-13 的 prior 值。依協議，本次採用 script 值（MOVE 68.48），搜尋值不作為證據。
- 10Y Δ 分解：ΔDGS10 −4.0bp、ΔDFII10 −3.0bp、ΔT10YIE −3.0bp，判讀為 不可判（視窗不一致）（T10YIE latest_date 為 2026-07-15，與另外兩腿的 2026-07-14 不同）。
- margin debt 對總市值比率本次沒有取得市值分母來源，比率未確立；Mag 7 加權 P/E 約 40 的資料日為 2026-05-15，Top-10 集中度 35.59% 的資料日為 2026-04-30，0DTE 約 63% 的資料日為 2026-02-28，都偏舊。
- R2 只取得彙總層級的 capex 指引，沒有四家逐家的數值與下次財報日期。

最大不確定性：
1. 下一次 hyperscaler 季報（落在窗口內，日期未確認）：若出現兩家下修，會直接推向 yes；目前證據顯示方向相反。
2. CoreWeave 等 neocloud 的負債總額與再融資牆本次未確立：若後續揭露大額近期到期並且融資管道收緊，R3 風險會上升，推向 yes。
3. 私募信貸贖回壓力是否擴散到多檔基金，並形成 net inflow→outflow flip：若擴散，可能經由 AI infrastructure debt financing 傳導到 R3，再透過信用重定價傳導到 R1，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest | 7572.4 | FRED API (series_id=SP500) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 8.51 | FRED API (series_id=SP500) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 10.25 | FRED API (series_id=SP500) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29502.6 | FRED API (series_id=NASDAQ100) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-16T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 3.78 | FRED API (series_id=NASDAQ100) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1 季資料） | 45.76080873390133（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-16T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5 | FRED API (series_id=DFEDTARL) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.72 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.79 | FRED API (series_id=BAMLC0A0CM) | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.58 | FRED API (series_id=DGS10) | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.33 | FRED API (series_id=DFII10) | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.23 | FRED API (series_id=T10YIE) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 79.2 | FRED API (series_id=DCOILWTICO) | 2026-07-13 | 2026-07-16T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-16T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.21 | FRED API (series_id=T5YIFR) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.7788 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-16T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.63 | FRED API (series_id=SOFR) | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.72 | FRED API (series_id=SOFR99) | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-07-16 | 2026-07-16T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用） | 0.102（十億美元） | FRED API (series_id=RPONTTLD) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6735609.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-08 | 2026-07-16T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5970516.0（€5.97T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-10 | 2026-07-16T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6395509.0（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-16T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.67 | FRED API (series_id=VIXCLS) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 15.67 | FRED API (series_id=VIXCLS, SP500) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | -7.28 | FRED API (series_id=VIXCLS) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | 1.2 | FRED API (series_id=SP500) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 1995.0783（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-01 | 2026-07-16T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7573044（口） | CFTC TFF futures-only | 2026-07-07 | 2026-07-16T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 68.48 | Yahoo Finance chart API (^MOVE) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2405.1（十億美元，transaction volume） | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-07-15 | 2026-07-16T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | MarketXLS WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 WebSearch（90d + 同季） | ✗ NOT DISCLOSED（無同季合格 TP 上修） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | S&P DJI factor dashboard WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | McClellan / StockCharts WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH]（MacroMicro 鏡像） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA / Advisor Perspectives WebSearch | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB / cashtag WebSearch（7d） | ✗ NOT DISCLOSED（無顯著 chatter） |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim / ycharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED（無新月份調查） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED DFEDTARU / DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（FRED BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（FRED BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（FRED DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（FRED T10YIE） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（FRED DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED CPIAUCSL | scripts/fetch_macro.py（yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（FRED T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED THREEFYTP10 | scripts/fetch_macro.py | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED SOFR / SOFR99 / IORB / RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | Reuters / TradingView [primary: SEARCH]（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch / MacroMicro [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED WALCL | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Bloomberg WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]（30d） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報 / 財經報導 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic / OpenAI / Google 披露 WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch / The Information WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 [primary: SEARCH] | ✗ NOT DISCLOSED（無合格披露） |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報 + 30d 融資事件 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 [primary: SEARCH]（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K / 10-Q [primary: SEARCH]（30d） | ✗ NOT DISCLOSED（30 日內無變動） |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速 + 30d 進出場事件 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED（1 件：General Fusion SPAC） |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis / Axios WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz / Benzinga / StockTitan [primary: SEARCH]（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | S-1 / 具名報導 WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無 S-1 或具名報導） |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR [primary: SEC EDGAR] + openinsider（14d） | ⛔ FETCH FAILED（EDGAR egress 受限，無法取得一手 Form 4 URL） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe / ycharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com / cryptobriefing [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | SEC / ETF.com / GlobeNewswire WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX / TWSE / JPX / ESMA WebSearch（7d） | ✗ NOT DISCLOSED（7 日內無英文披露） |
| structural.zero_dte | 結構｜0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe / Saxo WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（FRED VIXCLS + vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 Retail margin debt（Advisor Perspectives） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds / move_index / ofr_repo | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.59 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio（multpl） | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.18 | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E 約 40 trailing | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026（MarketXLS） | 2026-05-15 | 2026-07-16T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS 約 198bp vs CDX.NA.IG 約 95bp | Oracle CoreWeave CDS spread vs CDX IG July 2026 | https://www.investing.com/analysis/oracle-and-coreweave-credit-default-swap-spreads-widening-omen-or-jitters-200670506（Investing.com） | 2026-07-10 | 2026-07-16T09:30:00+08:00 |
| breadth.rsp_spy | RSP +9.67% vs SPY +8.38% YTD | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/26/forget-the-magnificent-seven-this-equal-weight-sp-fund-beats-the-mega-caps-for-just-0-20/（24/7 Wall St.） | 2026-06-26 | 2026-07-16T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 35.59% | S&P 500 top 10 concentration percent 2026 | https://www.spglobal.com/spdji/en/documents/performance-reports/dashboard-sp-500-factor.pdf（S&P DJI） | 2026-04-30 | 2026-07-16T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 2008／下跌 2749，A/D 線建設性 | NYSE advance decline breadth July 2026 | https://www.mcoscillator.com/market_breadth_data/（McClellan） | 2026-07-13 | 2026-07-16T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 46（Fear） | CNN Fear and Greed Index today July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed（MacroMicro；原定 cnn.com） | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt $1.416T、+53.7% YoY（2026-05 月資料） | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra（Advisor Perspectives；原定 FINRA） | 2026-05-31 | 2026-07-16T09:30:00+08:00 |
| retail.aaii | AAII Bull 36.3%／Bear 37.2% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-07-09 | 2026-07-16T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 82.95 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number（YCharts；原定 naaim.org） | 2026-07-08 | 2026-07-16T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y bid-to-cover 2.565、30Y bid-to-cover 2.44 | US Treasury 10Y 30Y auction July 2026 bid to cover | https://www.tradingview.com/news/macenews:30b090608094b:0-us-treasury-30-year-bond-auction-high-yield-5-058-bid-cover-ratio-at-2-44/（TradingView / MNI） | 2026-07-09 | 2026-07-16T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 會議約 70% 維持利率 | CME FedWatch rate hold probability July 2026 | https://en.macromicro.me/series/78109/probability-fed-rate-325-350-2026（MacroMicro；原定 CME） | 2026-07-08 | 2026-07-16T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance（Bloomberg） | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio 18.8%，quarterly redemption cap gate proration / breach | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://pitchbook.com/news/articles/private-credit-bdc-redemption-requests-likely-to-peak-in-q2-2026-bofa（PitchBook） | 2026-07-02 | 2026-07-16T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計約 $700B、仍上修 | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html（Yahoo Finance） | 2026-05-15 | 2026-07-16T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 約 $47B／OpenAI 約 $25B 年化營收 | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-05-15 | 2026-07-16T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 2Q26 合約價 +58–63% QoQ | DRAM HBM contract price 2Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260602-13074.html（TrendForce） | 2026-06-02 | 2026-07-16T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex 約 $700B vs AI 終端營收低百億級 | AI revenue to capex gap 2026 | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html（Yahoo Finance） | 2026-05-15 | 2026-07-16T09:30:00+08:00 |
| speculation.ai_rename_spac | General Fusion（GFUZ）SPAC 上市 | AI rename SPAC July 2026 General Fusion | https://www.morningstar.com/news/pr-newswire/20260710ln02448/（Morningstar / PR Newswire） | 2026-07-10 | 2026-07-16T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD 約 200 檔 IPO、募資 $141.2B | US IPO market 2026 YTD count proceeds | https://www.axios.com/2026/07/13/us-ipo-market-record-proceeds（Axios） | 2026-07-13 | 2026-07-16T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot 0 件 | microcap 100% single day quantum AI moonshot July 2026 | Finviz / Benzinga / StockTitan movers screener（已檢查來源） | — | 2026-07-16T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.62（日讀數） | Cboe equity put call ratio July 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio（YCharts；原定 Cboe） | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 約 $198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing；原定 etf.com） | 2026-07-10 | 2026-07-16T09:30:00+08:00 |
| structural.us_single_stock_etf | GraniteShares SK hynix SKUU／SKDD 2x 上市 | single-stock leveraged ETF launch July 2026 SK Hynix Tradr | https://www.globenewswire.com/news-release/2026/07/14/3326857/0/en/GraniteShares-Launches-the-First-U-S-Listed-Leveraged-ETFs-on-SK-hynix.html（GlobeNewswire） | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 成交約 63% | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/（Cboe） | 2026-02-28 | 2026-07-16T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月 1,603,491,559 口、+45% YoY | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-07-16T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 期限結構 contango、Cboe SKEW 149.6 | VIX term structure SKEW July 2026 | https://www.home.saxo/content/articles/options/options-brief---calm-on-top-nervous-underneath---1-july-2026-01072026（Saxo） | 2026-07-01 | 2026-07-16T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt $1.416T、+53.7% YoY（2026-05 月資料，cross-ref） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra（Advisor Perspectives） | 2026-05-31 | 2026-07-16T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $8.5B DDTL、Nvidia 循環融資 $24.9B | AI data center debt CoreWeave Nvidia circular financing July 2026 | https://www.techtimes.com/articles/320239/20260712/nvidia-circular-financing-249b-coreweave-debt-puts-pension-funds-risk.htm（Tech Times） | 2026-07-12 | 2026-07-16T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-07-16",
  "iso_week": "2026-W29",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-01-14",
  "prior_date": "2026-07-13",
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 3.78,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

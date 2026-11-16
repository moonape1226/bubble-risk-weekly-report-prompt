> [DRY RUN] this report was not committed to archive.

# 2026-07-30 AI 泡沫破裂預測報告
報告日期：2026-07-30｜ISO 週次：2026-W31｜預測窗口：2026-07-30 → 2027-01-28｜前次基準：report-2026-07-27（3天前）

## 結論

**結論：no**

三條路徑都還沒走到可在 182 天內完成解析的位置。R1 的 NASDAQ-100 雖已距 52 週高點回撤 11.31%，但還要再跌約 15.43% 才達 25% 門檻，而 HY OAS 284bp、IG OAS 81bp 顯示廣義信用並未失序（`valuation.ndx_drawdown`、`monetary.hy_oas`）。R2 方面，已取得指引的三家 hyperscaler 於 2026-07 季報全部上修 capex（`ai.hyperscaler_capex`），與「兩家下修」的條件方向相反。R3 的信用壓力（CoreWeave 5Y CDS 約 855bp、Oracle 降至 BBB-）是真實的後期訊號，但目前沒有任何違約、寬限期付款違約或 distressed exchange 的證據。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 27192.31（2026-07-29），252 個交易日最高收盤 30660.6（2026-06-02），距 52 週高點回撤 11.31%；R1 門檻水位 22995.45，自最新收盤須再跌約 15.43% 才會觸及（`valuation.ndx_drawdown`）。跌勢在近幾日加速：指數自 2026-07-21 的 29155.18 一路下滑，2026-07-27 → 07-29 兩個交易日即從 28039.21 跌到 27192.31。S&P 500 最新 7316.15（2026-07-29），仍高於 200 日均線 4.29%、高於 52 週均線 5.83%，自前次基準日以來 −1.31%（`valuation.sp500_trend`）。波動率同步升溫：VIX 由 2026-07-22 的 16.64 升至 07-29 的 20.66（+24.16%），同期 S&P 500 −2.44%，屬典型 risk-off 反向走勢，而非 crowded-optionality 的同漲（`structural.vix_spx_comove` comove=false）。估值仍高：S&P 500 trailing P/E 28.6、Shiller CAPE 40.9（2026-07-29，`valuation.sp500_pe_cape`），Top-10 集中度約 38%（`breadth.top10_concentration`）。另一方面，散戶情緒已轉為恐懼——CNN Fear & Greed 37（Fear，2026-07-29，`retail.fear_greed`），AAII Bear 42.3% 對 Bull 29.6%（2026-07-23，`retail.aaii`）——NAAIM 曝險也從 95.64 降至 84.02（2026-07-22，`retail.naaim`），代表部分去槓桿已經發生。

**判讀：** R1 距門檻還有一段（剩約 15.43%）。只有在信用端出現傳導，例如 AI 雲端 CDS 擴散為 HY OAS 明顯走闊，或槓桿部位被迫平倉（margin debt YoY +51.5%、槓桿 ETF AUM 約 $198B 創高），跌勢才會在窗口內延伸到 25%。這條路徑是三者中最近的一條，但目前的速度與廣義信用狀態還不足以支持「更可能完成」。

### R2 資本支出收縮

依 CNBC 2026-07-28 報導（`ai.hyperscaler_capex`），hyperscaler 在 2026-07 季報期間持續上修 2026 年 capex：Amazon 約 $200B（上修）、Alphabet 約 $205B（上修；`ai.hyperscaler_financing_mix` 同日報導其 FY26 capex 上修至約 $205B）、Meta $125–145B（上修），報導中的合計約 $725B。Microsoft 的最新官方指引不在本次取得的證據內，方向列為「未取得」。目前四家中確認下修的家數為 0；確切的下一次財報日期不在本次證據內，但 182 天的窗口預計涵蓋一到兩輪季報。需求端仍緊：伺服器 DRAM 交期 30–40 週，3Q26 合約價續漲 13–18% QoQ（TrendForce 2026-07-03，`ai.compute_supply_demand`），供給仍追不上需求，看不到 order digestion。壓力來自融資端：Alphabet Q2 FCF 轉負（`ai.hyperscaler_financing_mix`），市場對 capex 的審視升高（CNBC 標題稱 Alphabet 財報被看空），而 AI 營收對 capex 缺口（revenue-to-capex gap）仍大：年化 AI 終端營收約 $72B（Anthropic 約 $47B＋OpenAI 約 $25B，Epoch 2026-06-15）對年化 capex 約 $725B（分母：CNBC 報導的 hyperscaler 合計，2026-07-28），約為 10%（`ai.revenue_capex_gap`）。

**判讀：** R2 離解析最遠。最近一輪官方指引是一致上修，要在窗口內出現兩家「相較前次指引下修」，需要先有 R1 級別的市場衝擊或融資受阻迫使管理層轉向。FCF 轉負與股價對 capex 的負面反應是前置壓力，但還不是下修。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）已轉向信用端重新定價：Oracle 遭降至 BBB-，CoreWeave 5Y CDS 約 855bp，同日 Nebius −10%、CoreWeave −9%（247wallst 2026-07-29，`valuation.ai_credit_schism`）。CoreWeave 年初至今以 GPU 擔保募資約 $25B（`structural.ai_infrastructure_debt`），以主業與負債規模而言是最可能符合 R3 規模門檻的借款人。資金面的旁證：私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）已出現 gate proration / breach——BCRED Q2 突破 5% quarterly redemption cap 並比例撥付，redemption-request ratio 升至約 10% NAV（Bloomberg 2026-07-23，`monetary.private_credit_liquidity`）；hyperscaler 2026 年發債累計約 $182B（+1,300% YoY，`ai.hyperscaler_financing_mix`）。本次證據沒有任何 R3 借款人的付款違約、寬限期、covenant waiver、distressed exchange 或 going-concern 揭露，也沒有具名的近期到期牆資料。廣義信用仍緊：HY OAS 2.84%（`monetary.hy_oas`）、IG OAS 0.81%（`monetary.ig_oas`）。

**判讀：** R3 的定價已呈後期特徵（CDS 約 855bp 隱含明顯的違約風險溢酬），但解析條件要求破產、超過寬限期的違約或完成 distressed exchange。CoreWeave 年內仍能募到約 $25B，表示融資管道尚未關閉。要在窗口內轉為 yes，需要融資市場對 neocloud 關門（例如私募信貸贖回壓力擴散到放款端），再加上一個具體的到期或 covenant 觸發點；本次證據兩者都沒有。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 約 855bp、Oracle 遭降至 BBB-，AI 雲端股同日重挫（Nebius −10%、CoreWeave −9%），信用端已先於基本面重新定價（2026-07-29，`valuation.ai_credit_schism`、`structural.ai_infrastructure_debt`）。
- [R1] NASDAQ-100 已距 52 週高點回撤 11.31%，最新 27192.31（2026-07-29）較 2026-07-27 的 28039.21 兩日跌約 3%，同時 VIX 由 16.64 升至 20.66（+24.16%，2026-07-22 → 07-29）（`valuation.ndx_drawdown`、`structural.vix_spx_comove`）。
- [整體] 私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）出現實際 gate proration / breach：BCRED Q2 突破 5% quarterly redemption cap，redemption-request ratio 約 10% NAV（2026-07-23，`monetary.private_credit_liquidity`），可能收緊 AI infrastructure debt financing 的資金來源。
- [R2] Alphabet Q2 FCF 轉負，hyperscaler 2026 年發債累計約 $182B（+1,300% YoY），hyperscaler 融資結構（capex vs FCF / 發債）由現金流轉向舉債（2026-07-16／07-28，`ai.hyperscaler_financing_mix`）；AI 營收對 capex 缺口約 $72B 對 $725B（`ai.revenue_capex_gap`）。
- [R1] 槓桿與估值脆弱度高：FINRA margin debt 6 月 $1.502T、YoY +51.5%（`retail.margin_debt`），US 槓桿 ETF AUM 約 $198B 創高（2026-07-23，`structural.leveraged_etf_aum`），Shiller CAPE 40.9（`valuation.sp500_pe_cape`）；一旦下跌延續，強制去槓桿會放大跌幅。

## 支持 no 的證據

- [R2] 已取得指引的三家 hyperscaler 在 2026-07 季報全部上修 2026 年 capex（Amazon 約 $200B、Alphabet 約 $205B、Meta $125–145B，合計約 $725B，2026-07-28，`ai.hyperscaler_capex`），目前下修家數為 0，與 R2 所需的兩家下修方向相反。
- [整體] 廣義信用與資金市場未失序：HY OAS 2.84%（2026-07-28，`monetary.hy_oas`）、IG OAS 0.81%（`monetary.ig_oas`），SOFR−IORB 0bp、SRF 動用 $0.003bn（`monetary.repo_stress_srf`），MOVE 74.18 自前次的 77.21 回落（`structural.treasury_basis_trade`），AI 信用壓力仍集中在個別 neocloud 名字。
- [R1] 距 R1 門檻水位 22995.45 仍需再跌約 15.43%；S&P 500 仍高於 200 日均線 4.29%（2026-07-29，`valuation.ndx_drawdown`、`valuation.sp500_trend`），而 Fear & Greed 37、AAII Bear 42.3% 顯示恐慌情緒已部分反映（`retail.fear_greed`、`retail.aaii`）。
- [R2] AI 算力需求仍緊：伺服器 DRAM 交期 30–40 週，3Q26 合約價續漲 13–18% QoQ（2026-07-03，`ai.compute_supply_demand`），沒有 order digestion 或過剩產能的證據支持 capex 急轉。
- [R3] 融資管道仍開：CoreWeave 年初至今仍以 GPU 擔保完成約 $25B 募資（2026-07-29，`structural.ai_infrastructure_debt`），本次證據未見任何 R3 規模借款人的付款違約、寬限期或 distressed exchange。

## 與前期比較

前次結論：無前次預測（report-2026-07-27 為舊格式評分報告）

前次為舊格式評分報告，不轉譯為 yes/no；本次為新格式的第一個預測，flip_evidence 為空。自 2026-07-27 以來的主要數據變化如下：
- NASDAQ-100 由 28039.21 降至 27192.31（2026-07-29），回撤擴大至 11.31%。
- S&P 500 −1.31%（7413.18 → 7316.15），VIX 由 18.67 升至 20.66。
- 10Y 殖利率 −4bp 至 4.61%，HY OAS +3bp 至 2.84%，IG OAS 持平 0.81%。
- FOMC 維持 3.50–3.75%（2026-07-29）。
- AI 雲端信用重新定價（CoreWeave CDS 約 855bp，2026-07-29）是本次最重要的新增事件證據。

## 資料缺漏與不確定性

- `structural.zero_dte`（⛔ FETCH FAILED）：本次搜尋只取得 Cboe 2026-02 的「0DTE 佔 SPX 期權量約 56%」紀錄，不是當期快照，不作為證據使用。0DTE 屬投機結構的確認指標，不直接影響 R1–R3 的解析距離，這個缺口不太可能改變結論。
- 其他未取得或無揭露的項目（✗ NOT DISCLOSED，皆為 best-effort）：BofA / JPM 調查、AI token growth、OpenAI / Anthropic 當季營收揭露（最近一筆為 2026-06-15，屬上一季；revenue-to-capex gap 依 carry-forward 規則沿用）、RPO 重複計算、折舊年限變動、資本週期階段、全球槓桿商品核准。其中折舊年限與 RPO 若有新揭露，會影響 R2 的盈餘品質判讀，但不會直接觸發解析。
- 證據內部不一致：social sentiment 那筆的結果 URL 標題指向 Wendy's（WEN），與 BYND 的發現不符；美債標售那筆的 URL 指向 10Y 標售，發現卻是 20Y。這兩筆僅記錄於附錄，不作為證據引用。Microsoft 的最新 capex 指引不在本次證據內。
- 最大不確定性一：CoreWeave 等 neocloud 的再融資。若 CDS 續闊至融資市場關門，R3 可能在窗口內成立並傳導至 R1，推向 yes。
- 最大不確定性二：NASDAQ-100 的跌勢延續性。本週加速下跌加上 margin debt 與槓桿 ETF 的高水位，若引發強制去槓桿，R1 的剩餘 15.43% 可能快速縮短，推向 yes。
- 最大不確定性三：下一輪 hyperscaler 季報（窗口內）。若市場對 FCF 轉負的懲罰持續，指引轉為下修會推向 yes；若維持上修，則支持 no。

## 數據附錄

10Y 分解：ΔDGS10 −4bp、ΔDFII10 −3bp、ΔT10YIE +5bp；判讀：不可判（視窗不一致）（三腿資料更新，freshness=updated）。repo 資金壓力（SOFR−IORB）：as_of 2026-07-28，SOFR−IORB 0bp（IORB 取 2026-07-28）、SOFR99−IORB 9bp（sofr99_date 2026-07-28）。SRF 動用（Standing Repo Facility usage）$0.003bn（2026-07-29）。WALCL $6.75T、ECBASSETSW €5.94T、JPNASSETS ¥639.55T，銀行對 NBFI 放款 $2.01T。margin debt / 股市總市值比率因缺少市值分母，本次未計算。

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7316.15 | FRED API (series_id=SP500) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線） | 4.29（%） | FRED API (series_id=SP500) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線） | 5.83（%） | FRED API (series_id=SP500) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較前次基準） | -1.31（%） | FRED API (series_id=SP500) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 27192.31 | FRED API (series_id=NASDAQ100) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-30T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤） | 11.31（%） | FRED API (series_id=NASDAQ100) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1，家戶股票配置 %） | 45.76080873390133（≈45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-30T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75（%） | FRED API (series_id=DFEDTARU) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5（%） | FRED API (series_id=DFEDTARL) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.84（%，284bp） | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 3.0（bp） | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.81（%，81bp） | FRED API (series_id=BAMLC0A0CM) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.61（%） | FRED API (series_id=DGS10) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | -4.0（bp） | FRED API (series_id=DGS10) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.41（%） | FRED API (series_id=DFII10) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | -3.0（bp） | FRED API (series_id=DFII10) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.26（%） | FRED API (series_id=T10YIE) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | 5.0（bp） | FRED API (series_id=T10YIE) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（no_new_obs，持平） | 84.25（USD） | FRED API (series_id=DCOILWTICO) | 2026-07-27 | 2026-07-30T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46（%） | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-30T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.28（%） | FRED API (series_id=T5YIFR) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8376（%） | FRED API (series_id=THREEFYTP10) | 2026-07-24 | 2026-07-30T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（序列自身 trailing 7d） | 5.9（bp） | FRED API (series_id=THREEFYTP10) | 2026-07-24 | 2026-07-30T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.65（%） | FRED API (series_id=SOFR) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.74（%） | FRED API (series_id=SOFR99) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65（%） | FRED API (series_id=IORB) | 2026-07-30 | 2026-07-30T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用 transaction volume） | 0.003（$bn） | FRED API (series_id=RPONTTLD) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps | 0.0（bp） | FRED API (series_id=SOFR, IORB) repo_stress | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr99_iorb_bps | 9.0（bp） | FRED API (series_id=SOFR99, IORB) repo_stress | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.walcl | WALCL latest（no_new_obs，持平） | 6747378.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-22 | 2026-07-30T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（no_new_obs） | 5944015.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-24 | 2026-07-30T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（no_new_obs） | 6395509.0（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-30T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 20.66 | FRED API (series_id=VIXCLS) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of；base_date 2026-07-22，window_days 7，comove=false） | 20.66 | FRED API (series_id=VIXCLS, SP500) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 24.16（%） | FRED API (series_id=VIXCLS) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -2.44（%） | FRED API (series_id=SP500) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（no_new_obs） | 2012.1032（$2.01T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-15 | 2026-07-30T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位） | -7462516（口） | CFTC TFF futures-only | 2026-07-21 | 2026-07-30T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -45392（口） | CFTC TFF futures-only | 2026-07-21 | 2026-07-30T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 74.18 | Yahoo Finance chart API (^MOVE) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2357.5（$bn） | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl / gurufocus，WebSearch primary | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | CNBC 等財經媒體，WebSearch | ✓ SEARCH-VERIFIED（僅取得 Mag 7 對其餘 493 檔溢價，未取得加權 P/E 與 P/S） |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方 TP 報導，WebSearch primary（90d＋同季） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500 → sp500_trend） | ✓ API（sp500_trend ok） |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100 → ndx_drawdown） | ✓ API（ndx_drawdown ok） |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧 | 信用市場報導，WebSearch primary（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | Forbes，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth 報導，WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com，WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA | FINRA / Advisor Perspectives，WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com，WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB / cashtag，WebSearch（7d） | ✓ SEARCH-VERIFIED（結果 URL 標題與發現不一致，僅記錄不引用） |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API（BOGZ1FL153064486Q ok） |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim / YCharts，WebSearch primary | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查，WebSearch | ✗ NOT DISCLOSED（搜尋完成，窗口內無新調查） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py | ✓ API（BAMLH0A0HYM2 ok） |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py | ✓ API（BAMLC0A0CM ok） |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py | ✓ API（DGS10 ok） |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py | ✓ API（DFII10 ok） |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（FRED 直接取得） | ✓ API（T10YIE ok，FRED 直接取得） |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py | ✓ API（DCOILWTICO ok，no_new_obs） |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（yoy_pct） | ✓ API（CPIAUCSL ok） |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py | ✓ API（T5YIFR ok） |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（Kim-Wright） | ✓ API（THREEFYTP10 ok） |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（repo_stress block） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok；repo_stress ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | 標售報導，WebSearch primary（14d） | ✓ SEARCH-VERIFIED（結果 URL 標題與發現不一致，僅記錄不引用） |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch / CNBC，WebSearch primary | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py | ✓ API（WALCL ok，no_new_obs） |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Bloomberg，WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 揭露，WebSearch primary（30d） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報報導，WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED（Amazon / Alphabet / Meta；Microsoft 未取得） |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic / OpenAI / Google 揭露，WebSearch | ✗ NOT DISCLOSED（當季無揭露） |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch / 媒體報導，WebSearch | ✗ NOT DISCLOSED（最近揭露 2026-06-15 屬上一季，當季無新揭露） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話會議，WebSearch primary | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce，WebSearch primary | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：季報 capex vs FCF；event_scan：30d 發債報導，WebSearch primary | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合揭露（Epoch 分子＋CNBC 分母），carry-forward | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K / 10-Q / 電話會議，WebSearch primary（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | quarterly_state：供需增速；event_scan：30d 進出場事件，WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | Reuters / Benzinga / Boardroom Alpha，WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | Renaissance / emarketer，WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz / Benzinga / StockTwits / Yahoo movers，WebSearch primary（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導，WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe / YCharts，WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com / cryptobriefing，WebSearch primary | ✓ SEARCH-VERIFIED（僅取得總 AUM，個別 ticker 未取得） |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | SEC EDGAR ETF 申報 / 上市 feed，WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX / TWSE / JPX / ESMA，WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe，WebSearch | ⛔ FETCH FAILED（僅取得 2026-02 的舊紀錄，無當期快照） |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com，WebSearch（月頻） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe / Yahoo，WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 retail.margin_debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | 融資報導，WebSearch primary（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py | ✓ API（LNFACBW027SBOG ok，no_new_obs） |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds / move_index / ofr_repo），WebSearch 補充無新事件 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 28.6（原定來源 multpl） | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio（multpl） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 40.9（原定來源 gurufocus） | Shiller CAPE ratio July 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 對其餘 493 檔溢價約 10%（十年來最便宜） | Magnificent 7 valuation premium cheapest decade 2026 | https://www.cnbc.com/2026/07/08/magnificent-seven-stocks-are-the-cheapest-in-a-decade-by-one-measure.html（CNBC） | 2026-07-08 | 2026-07-30T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標價 $288，目標 PE 未擴張（約 22× CY27 EPS），屬 EPS 主導；舊目標價與 EPS Δ 未揭露 | Morgan Stanley NVDA target 288 July 2026 EPS | https://www.gurufocus.com/news/8955458/morgan-stanley-upgrades-nvidia-nvda-with-a-288-target-price（GuruFocus） | 2026-07-13 | 2026-07-30T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 降至 BBB-；CoreWeave 5Y CDS 約 855bp；Nebius −10%、CoreWeave −9% | Oracle BBB- CoreWeave CDS AI credit repricing July 2026 | https://247wallst.com/investing/2026/07/29/nebius-drops-10-coreweave-sinks-9-as-rising-credit-swap-costs-hit-the-ai-cloud-trade/（247wallst） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| breadth.rsp_spy | SPY +9.22% YTD、RSP +14.57% YTD | RSP vs SPY equal weight YTD 2026 | https://247wallst.com/investing/2026/07/26/is-equal-weighting-the-sp-500-worth-it-heres-what-the-data-says/（247wallst） | 2026-07-26 | 2026-07-30T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度約 38% | S&P 500 top 10 concentration percent 2026 | https://www.forbes.com/sites/investor-hub/article/sp-500-weight-mag-7-stocks-diversification-risk/（Forbes） | 2026-07-15 | 2026-07-30T09:30:00+08:00 |
| breadth.advance_decline | NYSE advancers 1.32:1、新高 161、新低 198 | NYSE advance decline new highs new lows July 27 2026 | https://finance.yahoo.com/markets/stocks/articles/stock-market-news-july-27-132000679.html（Yahoo Finance） | 2026-07-27 | 2026-07-30T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（Fear） | CNN Fear and Greed Index July 29 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-06 月資料）$1.502T、YoY +51.5%；URL 路徑日期 2026/06/24 與月資料不一致，以搜尋結果日期為準 | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra（Advisor Perspectives，原定 FINRA） | 2026-07-20 | 2026-07-30T09:30:00+08:00 |
| retail.aaii | AAII Bear 42.3%／Neutral 28.1%／Bull 29.6% | AAII investor sentiment survey July 23 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-07-23 | 2026-07-30T09:30:00+08:00 |
| retail.social_sentiment | BYND 空頭 37%、r/wallstreetbets 軋空、盤前 +10%；結果 URL 標題指向 Wendy's（WEN），與發現不一致，非 AI 標的，不作為證據 | Beyond Meat BYND wallstreetbets short squeeze July 2026 | https://www.asktraders.com/analysis/wendys-nasdaq-wen-stock-turns-meme-darling-amid-short-squeeze-and-activist-buzz/（AskTraders） | 2026-07-23 | 2026-07-30T09:30:00+08:00 |
| retail.naaim | NAAIM 前值 95.64 → 最新 84.02 | NAAIM exposure index July 2026 | https://ycharts.com/indicators/naaim_number（YCharts） | 2026-07-22 | 2026-07-30T09:30:00+08:00 |
| monetary.treasury_auctions | 20Y 標售 dealer takedown 14.67%；結果 URL 標題指向 10Y 標售，與發現不一致，不作為證據 | US Treasury auction July 2026 dealer takedown bid to cover | https://www.cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/（Crypto Briefing） | 2026-07-22 | 2026-07-30T09:30:00+08:00 |
| monetary.fedwatch | FOMC 維持 3.50–3.75%（9-3 票）；CME FedWatch 9 月維持不變約 42% | FOMC July 29 2026 hold FedWatch September | https://www.cnbc.com/2026/07/29/fed-rate-decision-july-2026.html（CNBC，原定 CME FedWatch） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| monetary.pboc | 人行 MLF 五個月最大，淨投放約 ¥100B | PBoC MLF net injection liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-24/pboc-adds-most-liquidity-to-economy-in-five-months-to-aid-growth（Bloomberg） | 2026-07-24 | 2026-07-30T09:30:00+08:00 |
| monetary.private_credit_liquidity | BCRED Q2 突破 5% quarterly redemption cap，gate proration / breach，redemption-request ratio 約 10% NAV | Blackstone BCRED Blue Owl redemption gate 5% cap July 2026 | https://www.bloomberg.com/news/articles/2026-07-02/blue-owl-bdcs-impose-caps-after-facing-19-38-requests-to-exit（Bloomberg） | 2026-07-23 | 2026-07-30T09:30:00+08:00 |
| ai.hyperscaler_capex | 2026 capex 續上修：Amazon 約 $200B、Alphabet 約 $205B、Meta $125–145B，合計約 $725B（2026-07 季報） | hyperscaler capex 2026 725B raised Meta Amazon Alphabet | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 交期 30–40 週；3Q26 合約價續漲 13–18% QoQ | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html（TrendForce） | 2026-07-03 | 2026-07-30T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] Alphabet Q2 FCF 轉負，FY26 capex 上修至約 $205B | Alphabet Q2 2026 capex FCF negative debt | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] hyperscaler 2026 年發債累計約 $182B，+1,300% YoY（公司債發行） | hyperscaler bond issuance 182B 2026 AI credit | https://247wallst.com/investing/2026/07/16/the-ai-revolution-is-reshaping-credit-markets-here-is-what-it-really-says-about-risk/（247wallst） | 2026-07-16 | 2026-07-30T09:30:00+08:00 |
| ai.revenue_capex_gap | 分子：Anthropic 約 $47B＋OpenAI 約 $25B run-rate（Epoch，2026-06-15，carry-forward）；分母：hyperscaler 2026 capex 合計約 $725B（CNBC 2026-07-28） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-06-15 | 2026-07-30T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收 IPO 合格件數 0 | AI rename SPAC no revenue IPO July 23-30 2026 | 已檢查：Reuters / Benzinga / Boardroom Alpha SPAC 螢幕 | — | 2026-07-30T09:30:00+08:00 |
| speculation.ipo_heat | 2026 IPO 募資 $251B、88 檔；Cerebras（CBRS）首日 +68% | US IPO market 2026 Cerebras first day pop | https://www.emarketer.com/content/ipos-test-investor-appetite-unprofitable-ai-giants（eMarketer） | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週 microcap thematic moonshot 合格件數 0 | microcap 100% single day quantum AI fusion moonshot July 2026 | 已檢查：Finviz / Benzinga / StockTwits / Yahoo movers | — | 2026-07-30T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 考慮延至 2027 IPO、目標估值約 $1T；Anthropic 持續推進程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground（Benzinga） | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| speculation.insider_form4 | CRWV 10b5-1 cluster：McBee 交易日 2026-07-20 約 $14.6M；CEO Intrator 交易日 2026-07-21 售 307,692 股約 $24.1M（EDGAR Form 4 filing index） | CoreWeave insider Form 4 July 2026 Intrator McBee SEC | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001769628&type=4（SEC EDGAR） | 2026-07-21 | 2026-07-30T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.66（日讀數） | Cboe equity put call ratio July 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio（YCharts，原定 Cboe） | 2026-07-27 | 2026-07-30T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高約 $198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing，原定 etf.com） | 2026-07-23 | 2026-07-30T09:30:00+08:00 |
| structural.us_single_stock_etf | Kioxia 9 檔美國上市單股槓桿 ETF 申報（首檔日企標的） | single-stock leveraged ETF launch July 2026 Kioxia Tuttle | https://www.tradingkey.com/analysis/stocks/us-stocks/262055692-kioxia-etf-softbank-openai-dram-skhynix-samsung-tradingkey（TradingKey） | 2026-07-26 | 2026-07-30T09:30:00+08:00 |
| structural.options_volume | OCC 6 月總量 16.0 億口，+45% YoY（2026-06 月資料） | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-07-30T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 約 150；VIX 19.99（term structure contango） | VIX SKEW term structure July 29 2026 | https://finance.yahoo.com/quote/%5ESKEW/history/（Yahoo Finance，原定 Cboe） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt $1.502T、+51.5% YoY（交叉引用 retail.margin_debt，不重複計入） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra（Advisor Perspectives） | 2026-07-20 | 2026-07-30T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave 年初至今募資約 $25B（GPU 擔保）；5Y CDS 升至約 855bp | AI data center debt financing CoreWeave CDS July 2026 | https://247wallst.com/investing/2026/07/29/nebius-drops-10-coreweave-sinks-9-as-rising-credit-swap-costs-hit-the-ai-cloud-trade/（247wallst） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-07-30",
  "iso_week": "2026-W31",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-01-28",
  "prior_date": "2026-07-27",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 11.31,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

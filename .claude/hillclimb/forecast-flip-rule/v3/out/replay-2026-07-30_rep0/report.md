> [DRY RUN] this report was not committed to archive.

# 2026-07-30 AI 泡沫破裂預測報告

報告日期：2026-07-30｜ISO 週次：2026-W31｜預測窗口：2026-07-30 → 2027-01-28｜前次基準：report-2026-07-27（3天前）

## 結論

**結論：no**

三條路徑都尚未進入「窗口內大概率完成」的狀態：NASDAQ-100 雖已距 52 週高點回撤 11.31%，但仍需自最新收盤再跌約 15.43% 才觸及 R1；四大 hyperscaler 最新一輪 capex 指引仍在上修（R2 下修家數為 0）。AI 雲端信用確實在重定價（CoreWeave 5Y CDS ≈855bp、Oracle 降至 BBB-），但 HY OAS 2.84%、repo 資金壓力 SOFR−IORB 0bp 顯示整體信用與資金市場尚無傳導，R3 違約事件的證據不足以克服 base rate。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 27,192.31（2026-07-29），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 11.31%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，自最新收盤還需再跌約 15.43% 才會觸及。自前次基準（2026-07-27 收盤 28,039.21）以來指數下跌約 3.0%，下跌在加速。S&P 500 收 7,316.15（2026-07-29），仍高於 200 日均線 4.29%、高於 52 週均線 5.83%，自前次基準下跌 1.31%（`valuation.sp500_trend`）。VIX 由 16.64（2026-07-22）升至 20.66（2026-07-29），7 日內 +24.16%，而同期 S&P 500 −2.44%，屬於正常的「股跌波動升」組合，不是 crowded-optionality 的同漲讀數（`structural.vix_spx_comove`）。情緒已轉向恐懼：CNN Fear & Greed 37（`retail.fear_greed`），AAII Bear 42.3%（`retail.aaii`），NAAIM 由 95.64 降至 84.02（`retail.naaim`）。估值仍高：S&P 500 trailing P/E 28.6、Shiller CAPE 40.9（`valuation.sp500_pe_cape`），margin debt $1.502T、YoY +51.5%（`retail.margin_debt`），因此一旦下跌延續，槓桿去化會放大跌幅。

**判讀：** R1 已走完約四成五的路程（11.31% / 25%），但剩餘的約 15% 跌幅需要新的催化劑，例如 AI 信用事件擴散、下一輪季報 capex 指引轉向或 margin debt 被動去槓桿；目前廣泛信用與資金市場仍平靜，尚不足以判定窗口內大概率完成。

### R2 資本支出收縮

依 CNBC 2026-07-28 的季報彙整，hyperscaler 2026 capex 續上修，四家合計約 $725B（`ai.hyperscaler_capex`）：

- Alphabet：FY26 capex 上修至約 $205B（2026 Q2 季報，2026-07-28），方向「上修」；同期 Q2 FCF 轉負（`ai.hyperscaler_financing_mix`）。
- Amazon：2026 capex 約 $200B（最新一輪季報彙整，2026-07-28），方向「上修」。
- Meta：2026 capex $125–145B（最新一輪季報彙整，2026-07-28），方向「上修」。
- Microsoft：本次證據未單獨列出其 FY 指引數字與方向；彙整報導描述整體續上修，未見任何下修。

目前四家中已下修 0 家。窗口（至 2027-01-28）預計涵蓋下一輪（Q3）季報，並可能涵蓋部分 Q4 季報；各家具體財報日期本次未取得。需求面仍偏緊：伺服器 DRAM 交期 30–40 週、3Q26 合約價續漲 13–18% QoQ（`ai.compute_supply_demand`）；Morgan Stanley 2026-07-13 將 NVDA 目標價設為 $288，目標本益比未擴張（約 22× CY27 EPS），升幅由 EPS 上修主導（`valuation.analyst_tp_decomposition`）。反方向的壓力在融資端：hyperscaler 2026 發債累計約 $182B、YoY +1,300%（`ai.hyperscaler_financing_mix`），AI 營收對 capex 缺口仍大：已披露 AI 終端年化營收約 $72B（Anthropic 約 $47B＋OpenAI 約 $25B）vs 年化 capex 約 $725B（分母：MSFT/GOOGL/AMZN/META 四家合計；Oracle 本次無 capex 數字，未納入）（`ai.revenue_capex_gap`、`ai.openai_anthropic_revenue`）。

**判讀：** R2 距離解析最遠：最新指引全面上修，要在窗口內出現兩家下修，需要季報中出現明確的需求轉弱或融資約束（例如 FCF 轉負迫使節制、信用市場拒絕再融資）。Alphabet FCF 轉負與發債激增是值得追蹤的早期壓力，但尚未轉化為指引下修。

### R3 AI 信用事件

AI 雲端信用正在重定價：Oracle 遭降至 BBB-，CoreWeave 5Y CDS 升至約 855bp，Nebius 單日跌 10%、CoreWeave 跌 9%（247wallst，2026-07-29；`valuation.ai_credit_schism`）。CoreWeave 年初至今募資約 $25B、以 GPU 擔保（`structural.ai_infrastructure_debt`），是本次證據中最可能符合 R3 規模門檻（負債 ≥ 50 億美元、以 AI 算力為主業）的借款人；其精確總負債與近期到期結構本次未取得，因此不在此估算。Oracle 雖遭降評，但其主業並非 AI 資料中心／算力，不直接落入 R3 定義。CoreWeave 內部人在 2026-07-20／07-21 依 10b5-1 計畫出售（McBee 約 $14.6M、CEO Intrator 307,692 股約 $24.1M；`speculation.insider_form4`），屬計畫性賣出，信號有限。周邊非銀行流動性出現 gate proration / breach：BCRED Q2 突破 5% quarterly redemption cap 並比例撥付，redemption-request ratio 升至約 10% NAV（`monetary.private_credit_liquidity`）。但廣泛信用仍緊：HY OAS 2.84%、IG OAS 0.81%（`monetary.hy_oas`、`monetary.ig_oas`），repo 資金壓力（SOFR−IORB）為 0bp、SOFR99−IORB 9bp，SRF 動用僅 $0.003bn（`monetary.repo_stress_srf`）。

**判讀：** CDS 約 855bp 代表市場已為 CoreWeave 定價出顯著違約風險，是三條路徑中最接近「事件」的訊號；但本次證據沒有任何付款違約、covenant waiver、distressed exchange 或 going-concern 文字。若窗口內再融資管道關閉（私募信貸贖回壓力擴散、GPU 擔保品價值下跌）才可能推過門檻，而目前資金市場平靜、需求端價格仍強，不支持大概率發生。

## 支持 yes 的證據

- [R3] AI 雲端信用重定價：CoreWeave 5Y CDS 升至約 855bp、Oracle 降至 BBB-，Nebius／CoreWeave 單日跌 10%／9%（2026-07-29），信貸端領先股價重定價是典型的後期訊號 `valuation.ai_credit_schism`
- [R1] NASDAQ-100 距 52 週高點回撤 11.31%（2026-07-29 收盤 27,192.31），自前次基準 3 個交易日內再跌約 3.0%，跌勢加速 `valuation.ndx_drawdown`
- [R3] CoreWeave 年初至今以 GPU 擔保募資約 $25B（2026-07-29），高槓桿 neocloud 對再融資高度依賴 `structural.ai_infrastructure_debt`
- [整體] 私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）：BCRED Q2 出現 gate proration / breach，redemption-request ratio 升至約 10% NAV（2026-07-23），AI infrastructure debt financing 的主要資金來源正面臨收緊 `monetary.private_credit_liquidity`
- [R2] hyperscaler 融資結構（capex vs FCF / 發債）轉變：Alphabet Q2 FCF 轉負（2026-07-28），hyperscaler 2026 發債 YoY +1,300% 至約 $182B（2026-07-16） `ai.hyperscaler_financing_mix`
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）：已披露 AI 終端年化營收約 $72B vs 四大 hyperscaler 年化 capex 約 $725B，ROI 落差懸殊 `ai.revenue_capex_gap`
- [R1] 槓桿與估值脆弱：margin debt $1.502T、YoY +51.5%（2026-06 月資料），Shiller CAPE 40.9，跌勢延續時易出現被動去槓桿 `retail.margin_debt` `valuation.sp500_pe_cape`
- [R1] VIX 7 日內由 16.64 升至 20.66（+24.16%，2026-07-29），風險偏好明顯降溫 `structural.vix_spx_comove`

## 支持 no 的證據

- [R2] 四大 hyperscaler 最新 capex 指引全面續上修（Alphabet 約 $205B、Amazon 約 $200B、Meta $125–145B，合計約 $725B，2026-07-28），R2 下修家數為 0 `ai.hyperscaler_capex`
- [R1] NASDAQ-100 距 R1 門檻 22,995.45 仍需再跌約 15.43%；S&P 500 仍高於 200 日均線 4.29%（2026-07-29），長期趨勢未破 `valuation.ndx_drawdown` `valuation.sp500_trend`
- [R3] 廣泛信用未傳導：HY OAS 2.84%、IG OAS 0.81%（2026-07-28），AI 雲端的重定價仍侷限於少數 issuer `monetary.hy_oas` `monetary.ig_oas`
- [整體] 資金市場平靜：repo 資金壓力（SOFR−IORB）0bp、SOFR99−IORB 9bp（2026-07-28），SRF 動用 $0.003bn（2026-07-29），MOVE 74.18（2026-07-29），未見國債市場失序（Treasury market dysfunction）前兆 `monetary.repo_stress_srf` `structural.treasury_basis_trade`
- [R2] 算力需求仍緊：伺服器 DRAM 交期 30–40 週、3Q26 合約價 +13–18% QoQ（2026-07-03），尚無利用率下滑或訂單消化證據 `ai.compute_supply_demand`
- [R1] 賣方目標價上修由 EPS 驅動而非本益比擴張（Morgan Stanley NVDA $288、約 22× CY27 EPS，2026-07-13），盈利基本面仍在上修 `valuation.analyst_tp_decomposition`
- [整體] 投機與情緒已降溫而非亢奮：CNN Fear & Greed 37（Fear，2026-07-29）、AAII Bear 42.3%（2026-07-23），+AI 改名／SPAC 與 microcap moonshot 本週皆 0 件，泡沫末期常見的散戶追高訊號減弱 `retail.fear_greed` `retail.aaii`
- [整體] Fed 有緩衝空間但有限：FOMC 維持 3.50–3.75%（2026-07-29），CME FedWatch 9 月持平約 42%；CPI YoY 3.46%（2026-06 月資料）限制大幅降息，但不排除官方市場功能回應（official market-functioning backstop） `monetary.fedwatch` `monetary.cpi_yoy`

## 與前期比較

前次結論：無前次預測（report-2026-07-27 為舊格式評分報告）

前次基準為舊格式評分報告，本次不將其評分換算為 yes/no，`flip_evidence` 為 []。自 2026-07-27 以來的重要變化：

- NASDAQ-100 由 28,039.21 跌至 27,192.31（約 −3.0%），S&P 500 −1.31%，VIX 由 18.67 升至 20.66 `valuation.ndx_drawdown` `structural.vix_spx_comove`
- CoreWeave CDS 走闊至約 855bp、Oracle 降至 BBB-（2026-07-29），AI 信用定價分歧（equity-vs-credit schism）開始朝信用端重定價收斂 `valuation.ai_credit_schism`
- Alphabet Q2 季報（2026-07-28）capex 上修、FCF 轉負 `ai.hyperscaler_financing_mix`
- FOMC 2026-07-29 維持利率不變 `monetary.fedwatch`
- HY OAS 由 2.81% 升至 2.84%，幅度輕微 `monetary.hy_oas`

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `structural.zero_dte`：搜尋僅取得 2026-02 的 Cboe 紀錄（0DTE 佔 SPX 期權量約 56%），無當期數值，標為 FETCH FAILED。0DTE 是短線投機結構指標，不影響三條路徑的判斷，不會改變答案。

其他 ✗ NOT DISCLOSED（非技術失敗，僅供參考）：institutional.bofa_jpm_survey、ai.token_growth、ai.customer_concentration_rpo、ai.depreciation_life、ai.capital_cycle、structural.global_leveraged_approvals。其中 backlog 重複計算風險（RPO double-counting）與折舊年限變動（depreciation useful-life change）缺披露，使 R2 的盈餘品質判讀較薄；資本週期階段（capital cycle stage）因增速證據不足，本次不判定週期階段。

最大的不確定性：

1. CoreWeave 等 neocloud 的實際負債規模與到期結構未確立：若後續證據顯示近期有大額到期且再融資受阻，R3 會明顯靠近，答案可能轉向 yes。
2. 下一輪（Q3）hyperscaler 季報的 capex 指引：若 Alphabet FCF 轉負引發節制、或有兩家轉為下修，R2 會直接解析；目前方向是上修，偏向 no。
3. 私募信貸贖回壓力是否擴散：若多檔基金出現 gate proration / breach 或 net inflow→outflow flip，AI infrastructure debt financing 管道收縮，會同時推升 R3 與 R1，偏向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7316.15 | FRED API (series_id=SP500) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線） | 4.29（%） | FRED API (series_id=SP500) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線） | 5.83（%） | FRED API (series_id=SP500) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較前次基準） | -1.31（%） | FRED API (series_id=SP500) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（NASDAQ-100 最新收盤） | 27192.31 | FRED API (series_id=NASDAQ100) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-30T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點） | 11.31（%） | FRED API (series_id=NASDAQ100) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1） | 45.76（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-30T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75（%） | FRED API (series_id=DFEDTARU) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.50（%） | FRED API (series_id=DFEDTARL) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.84（%） | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.81（%） | FRED API (series_id=BAMLC0A0CM) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.61（%） | FRED API (series_id=DGS10) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.41（%） | FRED API (series_id=DFII10) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.26（%） | FRED API (series_id=T10YIE) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 84.25（美元／桶） | FRED API (series_id=DCOILWTICO) | 2026-07-27 | 2026-07-30T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46（%） | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-30T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.28（%） | FRED API (series_id=T5YIFR) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8376（%） | FRED API (series_id=THREEFYTP10) | 2026-07-24 | 2026-07-30T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.65（%） | FRED API (series_id=SOFR) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.74（%） | FRED API (series_id=SOFR99) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65（%） | FRED API (series_id=IORB) | 2026-07-30 | 2026-07-30T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用 transaction volume） | 0.003（十億美元） | FRED API (series_id=RPONTTLD) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6747378.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-22 | 2026-07-30T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5944015.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-24 | 2026-07-30T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6395509.0（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-30T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 20.66 | FRED API (series_id=VIXCLS) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 20.66 | fetch_macro.py vix_spx_comove（FRED SP500 共同視窗） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日） | 24.16（%） | fetch_macro.py vix_spx_comove（FRED SP500 共同視窗） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日） | -2.44（%） | fetch_macro.py vix_spx_comove（FRED SP500 共同視窗） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2012.1032（$2.01T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-15 | 2026-07-30T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六檔美債期貨槓桿基金淨部位） | -7,462,516（口） | CFTC TFF futures-only (cftc_lev_funds) | 2026-07-21 | 2026-07-30T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 74.18 | Yahoo Finance chart API ^MOVE (move_index) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2357.5（十億美元） | OFR Short-term Funding Monitor (ofr_repo) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |

10Y 分解：ΔDGS10 −4.0bp、ΔDFII10 −3.0bp、ΔT10YIE +5.0bp；判讀：不可判（視窗不一致）。

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation｜S&P 500 P/E and Shiller CAPE | multpl / gurufocus [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation｜Mag 7 weighted P/E and AI leader P/S | CNBC 搜尋 | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation｜Analyst TP upgrade decomposition | 賣方研報摘要 [primary: SEARCH]，90d＋同季 | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | Valuation｜S&P 500 price-trend deviation | fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation｜NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導 [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst 搜尋 | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth｜Top-10 concentration in S&P 500 | Forbes 搜尋 | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth｜Advance/decline ratio, new high/low ratio | Yahoo Finance 市場報導搜尋 | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment｜Margin Debt: FINRA monthly data | Advisor Perspectives／FINRA 搜尋（stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment｜Social sentiment proxies | WSB／cashtag 搜尋，7d | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment｜Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment｜NAAIM Exposure Index | YCharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | Institutional Sentiment｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查搜尋 | ✗ NOT DISCLOSED（搜尋完成，無當月新調查） |
| monetary.fed_funds | Monetary & Credit｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | fetch_macro.py（FRED API） | ✓ API |
| monetary.hy_oas | Monetary & Credit｜High Yield OAS | fetch_macro.py（FRED API） | ✓ API |
| monetary.ig_oas | Monetary & Credit｜Investment Grade OAS | fetch_macro.py（FRED API） | ✓ API |
| monetary.dgs10 | Monetary & Credit｜10Y Treasury yield | fetch_macro.py（FRED API） | ✓ API |
| monetary.dfii10 | Monetary & Credit｜10Y Treasury real yield / TIPS | fetch_macro.py（FRED API） | ✓ API |
| monetary.t10yie | Monetary & Credit｜10Y breakeven inflation rate | fetch_macro.py（FRED API，非 derived） | ✓ API |
| monetary.wti | Monetary & Credit｜WTI crude oil price | fetch_macro.py（FRED API） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit｜CPI YoY: FRED series CPIAUCSL | fetch_macro.py（FRED API，yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit｜5y5y forward inflation expectation | fetch_macro.py（FRED API） | ✓ API |
| monetary.term_premium | Monetary & Credit｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | fetch_macro.py（FRED API，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | fetch_macro.py（FRED API；SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） | ✓ API |
| monetary.treasury_auctions | Monetary & Credit｜美債標售需求（auction tail / bid-to-cover） | 標售報導 [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit｜Fed funds rate path expectations | CME FedWatch／CNBC [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit｜Fed balance sheet: FRED series WALCL | fetch_macro.py（FRED API） | ✓ API |
| monetary.ecb_boj | Monetary & Credit｜Global central bank liquidity cross-check — ECB / BOJ | fetch_macro.py（FRED API；ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | Monetary & Credit｜PBoC aggregate financing / liquidity operations | Bloomberg 搜尋 | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]，30d | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI Fundamentals｜Hyperscaler capex guidance | 季報彙整搜尋（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals｜AI token volume growth rate | Anthropic／OpenAI／Google 披露搜尋 | ✗ NOT DISCLOSED（搜尋完成，無當季披露） |
| ai.openai_anthropic_revenue | AI Fundamentals｜OpenAI / Anthropic annualized revenue | Epoch AI 彙整搜尋 | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話搜尋 [primary: SEARCH] | ✗ NOT DISCLOSED（搜尋完成，無合格披露） |
| ai.compute_supply_demand | AI Fundamentals｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：季報 capex／FCF；event_scan：30d 發債掃描 [primary: SEARCH] | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI Fundamentals｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露（分母：MSFT/GOOGL/AMZN/META） [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q 搜尋，30d | ✗ NOT DISCLOSED（搜尋完成，30 日內無變動） |
| ai.capital_cycle | AI Fundamentals｜資本週期階段（capital cycle stage） | quarterly_state：供需增速；event_scan：30d 進出場事件 [SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior｜Search for past 7 days: AI rename / SPAC | Reuters／Benzinga／Boardroom Alpha 螢幕，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior｜IPO market heat | eMarketer 搜尋，7d | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior｜Microcap thematic moonshots | Finviz／Benzinga／StockTwits／Yahoo movers 螢幕，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior｜Upcoming AI IPOs | 具名報導搜尋，30d | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 [primary: SEC EDGAR]，14d | ✓ SEARCH-VERIFIED |
| speculation.equity_put_call | Speculative Behavior｜Cboe equity-only put/call ratio | YCharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage｜US leveraged ETF AUM | cryptobriefing／etf.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage｜US single-stock leveraged ETF approvals | SEC EDGAR／ETF 新發行搜尋，30d | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | Structural Leverage｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA 搜尋，7d | ✗ NOT DISCLOSED（搜尋完成，7 日內無英文披露） |
| structural.zero_dte | Structural Leverage｜0DTE option volume | Cboe 搜尋 | ⛔ FETCH FAILED（僅取得 2026-02 紀錄，無當期數值） |
| structural.options_volume | Structural Leverage｜Options total volume: OCC monthly volume report | theocc.com 搜尋（stock-of-state） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage｜Cross-asset derivatives / correlation checks | Yahoo Finance（SKEW、VIX term structure）搜尋 | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage｜VIX / S&P 500 co-movement | fetch_macro.py（FRED VIXCLS＋vix_spx_comove） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage｜Cross-reference only: FINRA margin debt | 交叉引用 Retail Sentiment margin debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage｜AI infrastructure debt financing / vendor-financing loops | 信用市場報導 [primary: SEARCH]，30d | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage｜Bank loans to nondepository financial institutions | fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage｜美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok；aggregation any） | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 28.6 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 40.9 | Shiller CAPE ratio July 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio （GuruFocus） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 對其餘 493 檔溢價約 10% | Magnificent 7 valuation premium cheapest decade 2026 | https://www.cnbc.com/2026/07/08/magnificent-seven-stocks-are-the-cheapest-in-a-decade-by-one-measure.html （CNBC） | 2026-07-08 | 2026-07-30T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標價 $288，目標本益比未擴張（約 22× CY27 EPS），EPS 主導 | Morgan Stanley NVDA target 288 July 2026 EPS | https://www.gurufocus.com/news/8955458/morgan-stanley-upgrades-nvidia-nvda-with-a-288-target-price （GuruFocus） | 2026-07-13 | 2026-07-30T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 降至 BBB-、CoreWeave 5Y CDS 約 855bp | Oracle BBB- CoreWeave CDS AI credit repricing July 2026 | https://247wallst.com/investing/2026/07/29/nebius-drops-10-coreweave-sinks-9-as-rising-credit-swap-costs-hit-the-ai-cloud-trade/ （24/7 Wall St.） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| breadth.rsp_spy | SPY +9.22% YTD、RSP +14.57% YTD | RSP vs SPY equal weight YTD 2026 | https://247wallst.com/investing/2026/07/26/is-equal-weighting-the-sp-500-worth-it-heres-what-the-data-says/ （24/7 Wall St.） | 2026-07-26 | 2026-07-30T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度約 38% | S&P 500 top 10 concentration percent 2026 | https://www.forbes.com/sites/investor-hub/article/sp-500-weight-mag-7-stocks-diversification-risk/ （Forbes） | 2026-07-15 | 2026-07-30T09:30:00+08:00 |
| breadth.advance_decline | NYSE advancers 1.32:1、新高 161、新低 198 | NYSE advance decline new highs new lows July 27 2026 | https://finance.yahoo.com/markets/stocks/articles/stock-market-news-july-27-132000679.html （Yahoo Finance） | 2026-07-27 | 2026-07-30T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（Fear） | CNN Fear and Greed Index July 29 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives，原定來源 FINRA） | 2026-07-20 | 2026-07-30T09:30:00+08:00 |
| retail.aaii | AAII Bear 42.3%／Neutral 28.1%／Bull 29.6% | AAII investor sentiment survey July 23 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-23 | 2026-07-30T09:30:00+08:00 |
| retail.social_sentiment | BYND 空頭 37%、r/wallstreetbets 軋空、盤前 +10% | Beyond Meat BYND wallstreetbets short squeeze July 2026 | https://www.asktraders.com/analysis/wendys-nasdaq-wen-stock-turns-meme-darling-amid-short-squeeze-and-activist-buzz/ （AskTraders） | 2026-07-23 | 2026-07-30T09:30:00+08:00 |
| retail.naaim | NAAIM 前值 95.64 → 最新 84.02 | NAAIM exposure index July 2026 | https://ycharts.com/indicators/naaim_number （YCharts） | 2026-07-22 | 2026-07-30T09:30:00+08:00 |
| monetary.treasury_auctions | 20Y 標售 dealer takedown 14.67%（長端需求偏弱） | US Treasury auction July 2026 dealer takedown bid to cover | https://www.cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/ （Crypto Briefing） | 2026-07-22 | 2026-07-30T09:30:00+08:00 |
| monetary.fedwatch | FOMC 維持 3.50–3.75%（9-3 票）、CME FedWatch 9 月持平約 42% | FOMC July 29 2026 hold FedWatch September | https://www.cnbc.com/2026/07/29/fed-rate-decision-july-2026.html （CNBC，原定來源 CME FedWatch） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| monetary.pboc | 人行 MLF 為 5 個月最大、淨投放約 ¥100B | PBoC MLF net injection liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-24/pboc-adds-most-liquidity-to-economy-in-five-months-to-aid-growth （Bloomberg） | 2026-07-24 | 2026-07-30T09:30:00+08:00 |
| monetary.private_credit_liquidity | BCRED Q2 突破 5% quarterly redemption cap、比例撥付（gate proration / breach），redemption-request ratio 升至約 10% NAV | Blackstone BCRED Blue Owl redemption gate 5% cap July 2026 | https://www.bloomberg.com/news/articles/2026-07-02/blue-owl-bdcs-impose-caps-after-facing-19-38-requests-to-exit （Bloomberg） | 2026-07-23 | 2026-07-30T09:30:00+08:00 |
| ai.hyperscaler_capex | 2026 capex 續上修：Amazon $200B、Alphabet $205B、Meta $125–145B、合計約 $725B（2026 Q2 季報） | hyperscaler capex 2026 725B raised Meta Amazon Alphabet | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic run-rate 約 $47B、OpenAI 約 $25B | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-06-15 | 2026-07-30T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 交期 30–40 週、3Q26 合約價 +13–18% QoQ | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html （TrendForce） | 2026-07-03 | 2026-07-30T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] Alphabet Q2 FCF 轉負、FY26 capex 上修至約 $205B | Alphabet Q2 2026 capex FCF negative debt | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] hyperscaler 2026 發債 YoY +1,300% 至累計約 $182B | hyperscaler bond issuance 182B 2026 AI credit | https://247wallst.com/investing/2026/07/16/the-ai-revolution-is-reshaping-credit-markets-here-is-what-it-really-says-about-risk/ （24/7 Wall St.） | 2026-07-16 | 2026-07-30T09:30:00+08:00 |
| ai.revenue_capex_gap | AI 終端年化營收 Anthropic 約 $47B＋OpenAI 約 $25B vs 年化 capex 約 $725B（分母：MSFT/GOOGL/AMZN/META） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI）；分母取自 ai.hyperscaler_capex 列 | 2026-06-15 | 2026-07-30T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收 IPO 合格件數 0 | AI rename SPAC no revenue IPO July 23-30 2026 | Reuters／Benzinga／Boardroom Alpha SPAC 螢幕 | — | 2026-07-30T09:30:00+08:00 |
| speculation.ipo_heat | 2026 IPO 募資 $251B、88 檔、Cerebras（CBRS）首日 +68% | US IPO market 2026 Cerebras first day pop | https://www.emarketer.com/content/ipos-test-investor-appetite-unprofitable-ai-giants （eMarketer） | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週 microcap thematic moonshot 合格 0 件 | microcap 100% single day quantum AI fusion moonshot July 2026 | Finviz／Benzinga／StockTwits／Yahoo movers 螢幕 | — | 2026-07-30T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 考慮延至 2027 IPO、目標估值約 $1T；Anthropic 續進程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground （Benzinga） | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| speculation.insider_form4 | CRWV Form 4（EDGAR 列表日期 2026-07-21）：McBee 交易日 2026-07-20 售約 $14.6M；CEO Intrator 交易日 2026-07-21 售 307,692 股約 $24.1M（10b5-1） | CoreWeave insider Form 4 July 2026 Intrator McBee SEC | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001769628&type=4 （SEC EDGAR） | 2026-07-21 | 2026-07-30T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.66（日讀數） | Cboe equity put call ratio July 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio （YCharts，原定來源 Cboe） | 2026-07-27 | 2026-07-30T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高約 $198B（個別 NVDL／TSLL／CONL／TQQQ／SOXL／SQQQ 未取得） | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing，原定來源 etf.com） | 2026-07-23 | 2026-07-30T09:30:00+08:00 |
| structural.us_single_stock_etf | Kioxia 9 檔美上市單股槓桿 ETF 申報（首檔日企標的） | single-stock leveraged ETF launch July 2026 Kioxia Tuttle | https://www.tradingkey.com/analysis/stocks/us-stocks/262055692-kioxia-etf-softbank-openai-dram-skhynix-samsung-tradingkey （TradingKey） | 2026-07-26 | 2026-07-30T09:30:00+08:00 |
| structural.options_volume | OCC 6 月總量 16.0 億口、+45% YoY | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-07-30T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 約 150、VIX 19.99（term structure contango） | VIX SKEW term structure July 29 2026 | https://finance.yahoo.com/quote/%5ESKEW/history/ （Yahoo Finance） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt $1.502T、+51.5% YoY（交叉引用 retail.margin_debt） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives） | 2026-07-20 | 2026-07-30T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave YTD 募資約 $25B、GPU 擔保；5Y CDS 約 855bp | AI data center debt financing CoreWeave CDS July 2026 | https://247wallst.com/investing/2026/07/29/nebius-drops-10-coreweave-sinks-9-as-rising-credit-swap-costs-hit-the-ai-cloud-trade/ （24/7 Wall St.） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |

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
  "yes_basis": [],
  "r1_drawdown_pct": 11.31,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

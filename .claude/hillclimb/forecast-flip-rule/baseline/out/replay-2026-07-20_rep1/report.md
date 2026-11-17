> [DRY RUN] this report was not committed to archive.
# 2026-07-20 AI 泡沫破裂預測報告
報告日期：2026-07-20｜ISO 週次：2026-W30｜預測窗口：2026-07-20 → 2027-01-18｜前次基準：report-2026-07-16（4天前）

## 結論

**結論：no**

三條路徑都離觸發仍遠：NASDAQ-100 距 52 週高點回撤 6.74%，距 R1 門檻尚需再跌約 19.58%；hyperscaler 2026 capex 合計仍在上修（≈$700B），R2 所需的兩家下修沒有任何跡象；R3 雖見 Oracle／CoreWeave CDS 走闊，但未發現任何違約、寬限期或 distressed exchange 訊號，且 HY OAS 僅 2.71%。估值與槓桿顯示泡沫存在、下檔很大，但目前證據不足以推翻「182 天內三條件皆不成立」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 28,592.66（2026-07-17），252 交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 6.74%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，自最新收盤須再下跌約 19.58% 才觸及。近期走勢偏弱：S&P 500 於 2026-07-17 收 7,457.69，較前次基準日（2026-07-16）跌 1.01%，但仍高於 200 日均線 6.73%、高於 52 週均線 8.42%（`valuation.sp500_trend`）；2026-07-17 NYSE 下跌家數約為上漲的 2 倍，報導主軸為晶片股賣壓（`breadth.advance_decline`）。VIX 由 2026-07-10 的 15.03 升至 2026-07-17 的 18.77（+24.88%），同期 S&P 500 −1.55%，屬正常的股跌波升，非 crowded-optionality 共振（`structural.vix_spx_comove`）。脆弱度高：S&P 500 trailing P/E 32.08、Shiller CAPE 41.52（`valuation.sp500_pe_cape`），FINRA margin debt $1.416T、YoY +53.7%（`retail.margin_debt`），NAAIM 95.64（`retail.naaim`）。

**判讀：** R1 尚遠，目前只是 6.74% 的正常回檔。若要在 2027-01-18 前觸發，需要一個把估值壓縮與去槓桿同時點燃的催化劑——例如 7 月下旬至 8 月初的 hyperscaler 財報季出現 capex／AI 營收失望、或 R3 信用事件外溢；高 margin debt 與 NAAIM 擁擠部位會放大跌幅，但目前未見強制平倉或信用利差急升。

### R2 資本支出收縮

本次取得的 capex 證據為合計層級：2026-05-15 報導 hyperscaler 2026 年 capex 合計約 $700B，且仍在上修（`ai.hyperscaler_capex`，沿用最近一季財報後的指引狀態）。個別公司方向：Microsoft、Alphabet、Amazon、Meta 本次證據只顯示整體上修，未取得逐家指引數字，逐家方向依該合計報導歸為「上修或持平」，四家中目前已下修家數為 0。下一輪財報（各家 2026 Q2 季報，依慣例約於 7 月下旬至 8 月初）落在預測窗口內，2026 Q3 季報（約 10 月下旬至 11 月初）亦在窗口內；本次證據未載明確切日期。需求面目前偏強：TrendForce 2026-07-03 指出伺服器 DRAM 3Q26 合約價 QoQ +13–18%（`ai.compute_supply_demand`），屬需求旺盛而非產能過剩的讀數。AI 營收對 capex 缺口（revenue-to-capex gap）仍大：年化 capex ≈$700B vs AI 終端營收低百億級（分母：top-4 hyperscaler 合計，資料日 2026-05-15，`ai.revenue_capex_gap`）。

**判讀：** R2 是三條路徑中最遠的一條。窗口內雖有兩次財報季，但目前 capex 趨勢仍在上修、記憶體合約價上漲，要在 182 天內出現兩家下修，需要 AI 營收對 capex 缺口急速惡化或 R1 大幅回撤迫使管理層轉向；現階段無證據支持。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）正在擴大：2026-07-16 報導 Oracle 5 年期 CDS 約 198bp、創紀錄，CoreWeave CDS 約 665bp（`valuation.ai_credit_schism`）。CoreWeave 屬以 AI 算力為主業、負債規模可達 R3 門檻的借款人，665bp 的 CDS 反映市場已在定價相當的違約風險；Oracle 雖負債龐大，但主業並非 AI 資料中心，未必落入 R3 定義。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）也已出現：Blue Owl OCIC 2026 Q2 redemption-request ratio 18.8%，於 5% 的 quarterly redemption cap 以比例撥付，屬 gate proration / breach（2026-07-02，`monetary.private_credit_liquidity`）。另一方面，廣義信用仍平靜：HY OAS 2.71%、IG OAS 0.78%（2026-07-16，`monetary.hy_oas`、`monetary.ig_oas`），repo 資金壓力（SOFR−IORB）為 −3bp、SRF 動用（Standing Repo Facility usage）為 0（`monetary.repo_stress_srf`）。本次 30 日 AI infrastructure debt financing / vendor-financing loops 掃描未發現新披露，亦未發現任何缺息、covenant waiver、distressed exchange 或 going-concern 字樣。

**判讀：** R3 是三條路徑中最接近「正在醞釀」的一條——CoreWeave 的 CDS 水位與私募信貸 gate proration 都是後期訊號——但從 CDS 走闊到實際破產／超過寬限期違約／完成 distressed exchange 仍有很長距離，且本次無任何具體到期牆或違約前兆證據。若窗口內出現 neocloud 再融資失敗、主要客戶合約變更或私募信貸贖回潮擴散到多檔基金，R3 會快速升溫。

## 支持 yes 的證據

- [R3] Oracle 5 年期 CDS 約 198bp 創紀錄、CoreWeave CDS 約 665bp（2026-07-16），AI 信用端開始重定價，而 HY OAS 僅 2.71%，信用與股權對 AI 風險的定價分歧擴大 `valuation.ai_credit_schism`
- [R3] Blue Owl OCIC 2026 Q2 redemption-request ratio 18.8%，以 5% quarterly redemption cap 比例撥付，屬實際 gate proration / breach（2026-07-02），非銀行資金端的流動性壓力已具體化 `monetary.private_credit_liquidity`
- [整體] 估值與槓桿處於極端：Shiller CAPE 41.52、trailing P/E 32.08（2026-07-17）；FINRA margin debt $1.416T、YoY +53.7%（2026-05 月資料），落在歷史頂部附近常見的 +40–50% 區間之上 `valuation.sp500_pe_cape` `retail.margin_debt`
- [R1] 部位擁擠：NAAIM Exposure Index 95.64（2026-07-15）、OCC 6 月期權成交 1,603,491,559 口、YoY +45%（2026-07-02），一旦下跌，去槓桿可放大跌幅 `retail.naaim` `structural.options_volume`
- [R1] 晶片股賣壓擴散：2026-07-17 NYSE 下跌家數約為上漲 2 倍、新高 241／新低 166，NASDAQ-100 自 2026-06-02 高點回撤至 6.74%，VIX 一週升 24.88% 至 18.77 `breadth.advance_decline` `valuation.ndx_drawdown` `structural.vix_spx_comove`
- [R2] AI 營收對 capex 缺口巨大：年化 capex ≈$700B vs AI 終端營收低百億級（2026-05-15，分母 top-4 hyperscaler），若財報季營收未跟上，capex 下修壓力會出現 `ai.revenue_capex_gap`

## 支持 no 的證據

- [整體] 基準率：182 天內 NASDAQ-100 回撤 25%、兩家 hyperscaler 同時下修 capex、或數十億美元級 AI 基建違約都屬少見事件；目前 NASDAQ-100 只回撤 6.74%，距 R1 門檻 22,995.45 仍需再跌約 19.58% `valuation.ndx_drawdown`
- [R2] hyperscaler 2026 capex 合計約 $700B 且仍在上修（2026-05-15），四家中無一下修，R2 需要的方向反轉尚未開始 `ai.hyperscaler_capex`
- [R2] AI 算力需求仍強：伺服器 DRAM 3Q26 合約價 QoQ +13–18%（2026-07-03），無產能過剩、訂單消化或庫存上升的證據 `ai.compute_supply_demand`
- [R3] 廣義信用與資金市場平靜：HY OAS 2.71%、IG OAS 0.78%（2026-07-16），SOFR−IORB −3bp、SOFR99−IORB +5bp、SRF 動用 0（2026-07-16／2026-07-17），沒有 credit crunch 或 repo 資金壓力（SOFR−IORB）跡象可把 AI 信用壓力轉成違約 `monetary.hy_oas` `monetary.ig_oas` `monetary.repo_stress_srf`
- [整體] 情緒已降溫而非狂熱：CNN Fear & Greed 37（Fear，2026-07-17）、Cboe equity put/call 0.73（2026-07-17），顯示避險需求正常，不是典型破裂前的極度貪婪 `retail.fear_greed` `speculation.equity_put_call`
- [R1] 政策緩衝仍在：Fed funds 目標區間 3.50%–3.75%（2026-07-19），CME FedWatch 顯示 7/29 會議約 86.7% 持平（2026-07-18），CPI YoY 3.46%（2026-06 資料）限制但未封死降息空間 `monetary.fed_funds` `monetary.fedwatch` `monetary.cpi_yoy`
- [R3] 美債市場無失序跡象：MOVE 70.88（2026-07-17）、CFTC 槓桿基金美債期貨淨部位 −7,562,874 口（2026-07-14，4 週 Δ −78,139），美債基差交易槓桿（Treasury basis-trade leverage）穩定、無平倉事件 `structural.treasury_basis_trade`

## 與前期比較

前次結論：無前次預測（report-2026-07-16 為舊格式評分報告）

本次為新格式首份預測，flip_evidence 為空。自 2026-07-16 以來的主要變化：

- NASDAQ-100 由 29,025.77（2026-07-16）跌至 28,592.66（2026-07-17），回撤擴大至 6.74%；S&P 500 一日 −1.01%。
- VIX 由 16.73 升至 18.77（2026-07-17），MOVE 由 68.16 升至 70.88。
- 10Y 殖利率與實質殖利率無新觀測（DGS10 4.57%、DFII10 2.35%，皆 2026-07-16），10Y breakeven Δ +2bp。
- HY／IG OAS 無新觀測（2.71%／0.78%）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED 來源（檢索完成但無合格當期披露）：valuation.analyst_tp_decomposition、retail.social_sentiment、institutional.bofa_jpm_survey、ai.token_growth、ai.openai_anthropic_revenue（最新 run-rate 披露為 2026-05-15，屬上一季，不計為當期）、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（quarterly_state 與 event_scan 皆無披露）、ai.depreciation_life、ai.capital_cycle（兩組件皆無披露）、structural.global_leveraged_approvals、structural.ai_infrastructure_debt。其中 structural.ai_infrastructure_debt 與 ai.hyperscaler_financing_mix 直接關係 R3：缺少 neocloud 債務到期牆與 hyperscaler 表外融資資料，使 R3 判讀主要依賴 CDS 水位，若補到大額近期到期或再融資困難，可能把 R3 推向 yes。speculation.insider_form4 為 0 件，但 SEC EDGAR 一手連結因 egress 受限未能取得，結果可靠度有限；此缺口不影響 R1–R3 判斷。

主要不確定性：

1. 7 月下旬至 8 月初 hyperscaler Q2 財報：若出現兩家以上 capex 指引下修（R2 直接觸發）或 AI 營收大幅低於預期（壓縮估值，推向 R1），答案會轉向 yes；若續上修則強化 no。
2. CoreWeave 等 neocloud 的再融資狀況：CDS 約 665bp 已反映可觀違約風險，本次缺少到期結構資料；若出現 distressed exchange 或缺息，R3 直接成立。
3. 私募信貸贖回壓力是否擴散：Blue Owl OCIC 18.8% redemption-request ratio 若在 Q3 擴及多檔大型 BDC 並出現 net inflow→outflow flip，資金端緊縮會傳導至 AI infrastructure debt financing，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest | 7457.69 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 6.73 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 8.42 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28592.66 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 6.74 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q1） | 45.76080873390133（≈45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5 | FRED API (series_id=DFEDTARL) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.71 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.57 | FRED API (series_id=DGS10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.35 | FRED API (series_id=DFII10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.24 | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 79.2 | FRED API (series_id=DCOILWTICO) | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.21 | FRED API (series_id=T5YIFR) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest | 0.7788 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.62 | FRED API (series_id=SOFR) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.7 | FRED API (series_id=SOFR99) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest | 0.0 | FRED API (series_id=RPONTTLD) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6743028.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5970516.0（€5.97T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6395509.0（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 18.77 | FRED API (series_id=VIXCLS) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 18.77 | FRED API (series_id=VIXCLS, SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（base 2026-07-10） | 24.88 | FRED API (series_id=VIXCLS) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2004.0237（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7562874 | CFTC TFF futures-only | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 70.88 | Yahoo Finance chart API (^MOVE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2342.6（$2.34T，十億美元） | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |

10Y 分解：ΔDGS10 0.0bp、ΔDFII10 0.0bp、ΔT10YIE +2.0bp；DGS10 與 DFII10 自前次基準日以來無新觀測（freshness partial_stale，stale_series：DGS10、DFII10），T10YIE 視窗不同；判讀：不可判（視窗不一致）。10Y 期限溢價（term premium）0.7788%（Kim-Wright 模型，2026-07-10），序列自身 trailing ≈7d Δ +4.7bp。repo 資金壓力（SOFR−IORB）−3bp、SOFR99−IORB +5bp（皆 2026-07-16），SRF 動用 0（2026-07-17）。

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation｜S&P 500 P/E and Shiller CAPE | multpl.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation｜Mag 7 weighted P/E and AI leader P/S | MarketXLS WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation｜Analyst TP upgrade decomposition | 賣方研報 WebSearch [primary: SEARCH]，90d＋同季 | ✗ NOT DISCLOSED（本季無合格 TP 上修披露） |
| valuation.sp500_trend | Valuation｜S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth｜Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth｜Advance/decline ratio, new high/low ratio | NYSE breadth WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment｜CNN Fear & Greed Index | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment｜Margin Debt: FINRA monthly data | FINRA／Advisor Perspectives WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment｜Retail survey: AAII Investor Sentiment | aaii.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment｜Social sentiment proxies | WSB／cashtag WebSearch，7d | ✗ NOT DISCLOSED（無顯著討論） |
| retail.household_equity_allocation | Retail Sentiment｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment｜NAAIM Exposure Index | ycharts WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | Institutional Sentiment｜BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✗ NOT DISCLOSED（無當期新調查） |
| monetary.fed_funds | Monetary & Credit｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit｜美債標售需求（auction tail / bid-to-cover） | WebSearch [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit｜Fed funds rate path expectations | CME FedWatch WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit｜PBoC aggregate financing / liquidity operations | Bloomberg WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit｜Private-credit / non-bank fund liquidity stress | BDC 披露 WebSearch [primary: SEARCH]，30d | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI Fundamentals｜Hyperscaler capex guidance | 季報 WebSearch（stock-of-state，沿用最近財報季） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals｜AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI Fundamentals｜OpenAI / Anthropic annualized revenue | Epoch／The Information WebSearch | ✗ NOT DISCLOSED（最新為 2026-05-15，非當季） |
| ai.customer_concentration_rpo | AI Fundamentals｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 WebSearch [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals｜AI compute supply/demand and overcapacity risk | TrendForce WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報＋30d 事件 WebSearch [primary: SEARCH]；兩組件皆完成檢索、無披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 WebSearch [primary: SEARCH]（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q WebSearch [primary: SEARCH]，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals｜資本週期階段（capital cycle stage） | 供需增速＋30d 進出場事件 WebSearch [primary: SEARCH]；兩組件皆完成檢索、無披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior｜Search for past 7 days: AI rename / SPAC | WebSearch，7d | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | Speculative Behavior｜IPO market heat | stockanalysis WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior｜Microcap thematic moonshots | Finviz／Benzinga／StockTitan movers WebSearch [primary: SEARCH]，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior｜Upcoming AI IPOs | 具名報導 WebSearch，30d | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior｜Insider selling at AI / market-leadership companies | SEC EDGAR／openinsider WebSearch，14d（EDGAR 一手連結 egress 受限） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior｜Cboe equity-only put/call ratio | Cboe WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage｜US leveraged ETF AUM | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF.com WebSearch，30d | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | Structural Leverage｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch，7d | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage｜0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage｜Options total volume: OCC | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage｜Cross-asset derivatives / correlation checks | Cboe／AInvest WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage｜Cross-reference only: FINRA margin debt | 交叉引用 Retail Sentiment margin debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage｜AI infrastructure debt financing / vendor-financing loops | WebSearch [primary: SEARCH]，30d | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | Structural Leverage｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.08 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 41.52 | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E ≈40 trailing | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026 （MarketXLS） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS ≈198bp 創紀錄、CoreWeave CDS ≈665bp | Oracle CoreWeave CDS spread widening July 2026 | https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/ （RIA） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP +10.68% vs SPY +7.47% YTD | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （247wallst） | 2026-06-10 | 2026-07-20T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 36.40% | S&P 500 top 10 concentration percent 2026 | https://ahasignals.com/sp500-concentration-risk/ （ahasignals） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| breadth.advance_decline | NYSE 下跌約 2×上漲、NH 241／NL 166 | NYSE advance decline breadth July 17 2026 | https://money.usnews.com/investing/news/articles/2026-07-17/wall-st-futures-fall-as-chip-selloff-gathers-pace-netflix-tumbles （US News／Reuters） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（Fear） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed （MacroMicro；原定 cnn.com） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-05 月資料）$1.416T、+53.7% YoY | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives；原定 FINRA） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |
| retail.aaii | AAII Bull 44.9% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number （YCharts；原定 naaim.org） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 BTC 2.59、小幅 tail | US Treasury 10Y auction July 2026 bid to cover | https://cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/ （CryptoBriefing；原定 TreasuryDirect／Reuters） | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 ≈86.7% 持平 | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch （CryptoRank；原定 CME Group） | 2026-07-18 | 2026-07-20T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance （Bloomberg） | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio 18.8%，quarterly redemption cap 5% 比例撥付（gate proration / breach） | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://whbl.com/2026/07/02/blue-owl-keeps-withdrawal-limits-even-as-redemption-pressure-modestly-eases/ （WHBL／Reuters） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計 ≈$700B、仍上修（最近財報季狀態） | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html （Yahoo Finance） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 +13–18% QoQ | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html （TrendForce） | 2026-07-03 | 2026-07-20T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex ≈$700B vs AI 終端營收低百億級（分母：top-4 hyperscaler） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| speculation.ai_rename_spac | EVTV→Azio AI（AZIO）改名 | AI rename ticker change July 2026 Azio EVTV | https://www.businesswire.com/news/home/20260710628386/en/Azio-AI-Holdings-Inc.-Nasdaq-EVTV-to-Begin-Trading-Under-New-Ticker-Symbol-AZIO-Completing-Corporate-Rebrand （Business Wire） | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD ≈200 檔 IPO、$141.2B | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/ （StockAnalysis；原定 Renaissance） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| speculation.microcap_moonshots | 7 日內合格 microcap moonshot 0 件 | microcap 100% single day quantum AI moonshot July 2026 | Finviz／Benzinga／StockTitan movers screener | — | 2026-07-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 投資人會議、估值 $965B、可能 10 月掛牌 | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html （CNBC） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 cluster 0 件（EDGAR 一手 URL egress 受限） | insider Form 4 cluster AI leaders July 2026 openinsider | SEC EDGAR／openinsider | — | 2026-07-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.73（daily） | Cboe equity put call ratio July 2026 | https://www.cboe.com/markets/us/options/market-statistics/daily/ （Cboe） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM ≈$198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （CryptoBriefing；原定 etf.com） | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 推出 6 檔 2x 單一個股 ETF（GOOGL／AMZN／META／AAPL） | single-stock leveraged ETF launch July 2026 Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-07 | 2026-07-20T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 成交 ≈63% | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/ （Cboe） | 2026-02-28 | 2026-07-20T09:30:00+08:00 |
| structural.options_volume | OCC 6 月 1,603,491,559 口、+45% YoY | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 145.13、VIX ≈16.5 contango | VIX term structure SKEW July 2026 | https://www.ainvest.com/news/0dte-volatility-drives-market-strategies-2026-2602/ （AInvest；原定 Cboe） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-05 月資料）$1.416T、+53.7% YoY（交叉引用） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |

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

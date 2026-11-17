> [DRY RUN] this report was not committed to archive.

# 2026-07-20 AI 泡沫破裂預測報告
報告日期：2026-07-20｜ISO 週次：2026-W30｜預測窗口：2026-07-20 → 2027-01-18｜前次基準：report-2026-07-16（4天前）

## 結論

**結論：no**

三條路徑目前都沒有一條已在進行中或可望在 182 天內完成：NASDAQ-100 距 52 週高點回撤 6.74%，仍需再跌約 19.6% 才觸及 R1 門檻；hyperscaler 2026 capex 合計約 $700B 且仍在上修（`ai.hyperscaler_capex`），R2 尚無任何一家下修。R3 端 Oracle／CoreWeave CDS 走闊（`valuation.ai_credit_schism`）屬於重定價而非違約，而且大盤 HY OAS 僅 2.71%（`monetary.hy_oas`），尚未出現信用傳導。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 28,592.66（2026-07-17），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 6.74%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，從最新收盤還需再跌約 19.6% 才會觸及。短線動能轉弱：S&P 500 自前次基準以來 −1.01%，收在 7,457.69（2026-07-17），仍高於 200 日均線 6.73%、高於 52 週均線 8.42%（`valuation.sp500_trend`）；VIX 一週內由 15.03 升至 18.77（+24.88%），同期 S&P 500 −1.55%，屬於正常的反向波動，不是漲勢中避險需求同步被搶高的 co-movement 警訊（`structural.vix_spx_comove`）。2026-07-17 NYSE 下跌家數約為上漲家數 2 倍，新高／新低 241／166（`breadth.advance_decline`）；當日報導為晶片股賣壓擴大。估值脆弱度高：S&P 500 trailing P/E 32.08、Shiller CAPE 41.52（`valuation.sp500_pe_cape`），Mag 7 加權 P/E 約 40（`valuation.mag7_multiples`，資料日 2026-05-15）。

**判讀：** R1 距離門檻還很遠，要觸發需要窗口內 NASDAQ-100 自 6 月高點累計重挫 25%。可能的推力是：晶片股賣壓延續、下一次 hyperscaler 季報指引令人失望、或信用端事件（R3）外溢；目前只看到修正初期，沒有證據顯示急跌已在進行中。

### R2 資本支出收縮

本次取得的最新資料為 2026-05-15 的彙整報導：hyperscaler 2026 年 capex 合計約 $700B，且指引仍在上修（`ai.hyperscaler_capex`，carry-forward 自上一季財報季）。逐家（Microsoft、Alphabet、Amazon、Meta）的指引金額與日期，本次證據只有彙整層級，未逐家建立；該報導未指出任何一家下修，因此本次可確認的下修家數為 0。供給端仍在擴張：TrendForce 指 3Q26 伺服器 DRAM 合約價季增 13–18%（`ai.compute_supply_demand`，2026-07-03），屬需求強勁／成本上升的訊號，而非產能過剩。需求端：Anthropic 年化營收約 $47B、OpenAI 約 $25B（`ai.openai_anthropic_revenue`，2026-05-15），對照年化 capex 約 $700B（分母：top-4 hyperscaler 彙整，未含 Oracle 與 neocloud），AI 營收對 capex 缺口（revenue-to-capex gap）仍大（`ai.revenue_capex_gap`）。182 天窗口預期涵蓋四家接下來的兩到三次季報，但本次證據沒有提供確切的財報日期。

**判讀：** R2 目前完全沒有啟動，整體指引仍在上修。要在窗口內成立，需要兩家在接下來最多三次財報中由上修轉為下修；這通常要先出現 R1 式的市場壓力或 AI 營收落後的明確證據。營收對 capex 缺口是中期壓力來源，但不構成 182 天內的觸發。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）正在往信用重定價方向移動：Oracle 5 年期 CDS 約 198bp、創紀錄，CoreWeave 約 665bp（`valuation.ai_credit_schism`，2026-07-16）。CoreWeave 是符合 R3 主業條件的代表性 neocloud 借款人，但它的總負債本次沒有取得來源，因此是否達到 ≥ 50 億美元的門檻在本報告中未建立。Oracle 不以 AI 資料中心為主業，不構成 R3 主體。本次掃描未取得任何付款違約、covenant waiver、distressed exchange 或 going-concern 披露。大盤信用沒有傳導：HY OAS 2.71%、IG OAS 0.78%（`monetary.hy_oas`、`monetary.ig_oas`，2026-07-16）。非銀行端有局部壓力：Blue Owl OCIC Q2 redemption-request ratio 18.8%，依 quarterly redemption cap 5% 比例撥付，屬 gate proration / breach（`monetary.private_credit_liquidity`，2026-07-02）。報導標題同時指出贖回壓力較前季小幅緩解，而且這只是單一基金，不構成多基金的私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）趨勢。

**判讀：** R3 是三條路徑中最接近警戒的一條。665bp 的 CDS 代表市場正在為 neocloud 違約風險定價，但距離實際違約或 distressed exchange 仍有很大距離。要在窗口內成立，需要融資市場對 neocloud 關門（再融資失敗）或關鍵客戶合約違約，而本次未見到這類訊號。

## 支持 yes 的證據

- [R3] Oracle 5 年期 CDS 約 198bp 創紀錄、CoreWeave 約 665bp（2026-07-16），顯示 AI 基礎設施信用端開始重定價，而股權端仍隱含高成長（`valuation.ai_credit_schism`）。
- [整體] 私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）已有實際 gate proration / breach：Blue Owl OCIC Q2 redemption-request ratio 18.8%，依 5% quarterly redemption cap 比例撥付（2026-07-02，`monetary.private_credit_liquidity`），可能壓縮 AI 基礎設施的非銀行融資管道。
- [R1] 估值與持倉都極度擁擠：Shiller CAPE 41.52、trailing P/E 32.08（2026-07-17，`valuation.sp500_pe_cape`）；NAAIM 曝險 95.64（2026-07-15，`retail.naaim`）；FINRA margin debt $1.416T、年增 +53.7%（2026-05 資料，`retail.margin_debt`）。一旦出現催化劑，下跌幅度可能很大。
- [R1] 短線動能轉弱：2026-07-17 晶片股賣壓擴大，NYSE 下跌家數約為上漲家數 2 倍（`breadth.advance_decline`），VIX 一週升 24.88% 至 18.77（`structural.vix_spx_comove`），CNN Fear & Greed 37（Fear，`retail.fear_greed`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）巨大：年化 capex 約 $700B，對照 Anthropic 約 $47B＋OpenAI 約 $25B 的 run-rate（`ai.revenue_capex_gap`、`ai.openai_anthropic_revenue`），長期回本壓力是 capex 下修的潛在來源。

## 支持 no 的證據

- [R2] Hyperscaler 2026 capex 合計約 $700B 且仍在上修（`ai.hyperscaler_capex`），報導未見任何一家下修。R2 需要兩家反向，目前方向正好相反。
- [R1] NASDAQ-100 距 52 週高點回撤 6.74%（2026-07-17，`valuation.ndx_drawdown`），距 R1 門檻 22,995.45 還需再跌約 19.6%；S&P 500 仍高於 200 日均線 6.73%（`valuation.sp500_trend`）。
- [R3] 大盤信用沒有傳導：HY OAS 2.71%、IG OAS 0.78%（2026-07-16，`monetary.hy_oas`、`monetary.ig_oas`）；銀行對 NBFI 放款 $2.00T 持平（`structural.nbfi_bank_loans`）。本次未見任何 AI 借款人違約或 distressed exchange 披露。
- [整體] 資金面沒有壓力：repo 資金壓力（SOFR−IORB）為 −3bp、SOFR99−IORB 為 +5bp（2026-07-16），SRF 動用（Standing Repo Facility usage）為 0（2026-07-17，`monetary.repo_stress_srf`）；MOVE 70.88（`structural.treasury_basis_trade`）。不存在迫使去槓桿的流動性觸發。
- [R2] AI 算力需求仍強：3Q26 伺服器 DRAM 合約價季增 13–18%（2026-07-03，`ai.compute_supply_demand`）；Anthropic 正以約 $965B 估值進行 IPO 投資人會議（2026-07-15，`speculation.upcoming_ai_ipos`）。股權融資窗口仍開，不支持短期 capex 收縮。

## 與前期比較

前次結論：yes（report-2026-07-16）
本次結論：翻轉
翻轉依據：
- 前次 forecast.json 早於 `yes_basis` 欄位，沒有記錄可逐項檢視的 yes 理由，因此本次依規則重新檢驗 yes 是否成立。R1：NASDAQ-100 距 52 週高點回撤 6.74%（前次為 3.78%），雖擴大，但仍需再跌約 19.6% 才觸及門檻，看不到路徑已在進行中（`valuation.ndx_drawdown`）。
- R2：hyperscaler 2026 capex 合計約 $700B 且仍上修，報導未見任何一家下修（`ai.hyperscaler_capex`），沒有任何一家朝下修移動。
- R3：Oracle／CoreWeave CDS 走闊（2026-07-16，`valuation.ai_credit_schism`）只是違約風險被重新定價，不是違約或 distressed exchange 本身；本次也無 AI 基礎設施債務的新事件披露。
- 傳導：HY OAS 2.71% 持平（`monetary.hy_oas`），大盤信用沒有擴散。重新檢驗後，現有證據不符合「至少一條路徑已在進行中或可望在窗口內完成」的 yes 門檻，因此答案回到 no。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `speculation.insider_form4`：SEC EDGAR egress 受限，一手 Form 4 URL 無法取得，篩選未能依規格完成。內部人賣壓屬情緒面輔助訊號，不在任何解析路徑上，不會改變本次答案。

未披露（✗ NOT DISCLOSED）且與路徑相關的缺口：`structural.ai_infrastructure_debt`（30 日內無新 AI 基礎設施債務事件）、`ai.hyperscaler_financing_mix` 與 `ai.capital_cycle`（兩個組件皆無披露）、`ai.depreciation_life`。缺少這些資料，R3 借款人的負債規模與再融資時程無法量化。

證據落差：`case/evidence.md` 將 `structural.treasury_basis_trade` 的三個組件記為 fetch_failed，但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 的狀態皆為 ok；依 macro 決策分支，本次以 artifact 為準並標 ✓ API。

最大的不確定性：

1. 下一次 hyperscaler 季報（確切日期本次未取得）：若兩家以上 capex 指引轉為下修，會直接推向 yes（R2）；若繼續上修，則加強 no。逐家指引本次只有彙整層級，是 R2 判讀的主要盲點。
2. CoreWeave 等 neocloud 的負債規模與到期牆：CDS 約 665bp 已處於高收益偏弱區，但負債總額與近期到期日本次未建立。若窗口內出現再融資失敗或 distressed exchange，會推向 yes（R3），並可能外溢到 R1。
3. 晶片股賣壓是否延續：7/17 的賣壓若演變為持續性去槓桿（margin debt 年增 +53.7%、NAAIM 95.64 顯示持倉擁擠），回撤可能快速擴大，推向 yes（R1）；若只是技術性修正，則維持 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7457.69 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 6.73 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.42 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（對前次基準 %） | -1.01 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28592.66 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 6.74 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1，家戶股票佔金融資產 %） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上緣 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下緣 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.71 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.57 | FRED API (series_id=DGS10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.35 | FRED API (series_id=DFII10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.24 | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl） | 79.2 | FRED API (series_id=DCOILWTICO) | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料，CPI YoY %） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.21 | FRED API (series_id=T5YIFR) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright 10Y 期限溢價 %） | 0.7788 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API (series_id=SOFR99) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,743,028（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,970,516（€5.97T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,395,509（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 18.77 | FRED API (series_id=VIXCLS) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（7 日窗，comove=false） | 18.77 | FRED API 衍生 (series_id=VIXCLS＋SP500 共同日) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（%，基期 2026-07-10） | 24.88 | FRED API 衍生 (vix_spx_comove block) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（%，基期 2026-07-10） | -1.55 | FRED API 衍生 (vix_spx_comove block) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（十億美元） | 2004.0237（$2.00T） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7,562,874 | CFTC TFF (cftc_lev_funds) | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（^MOVE） | 70.88 | Yahoo chart API (move_index, ^MOVE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2342.6 | OFR STFM (ofr_repo, REPO-TRIV1_TV_TOT-P) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | MarketXLS WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 WebSearch（90d＋同季） | ✗ NOT DISCLOSED（搜尋完成，無合格同季 TP 上調） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧 | 信用市場 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | 集中度 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH]（MacroMicro 鏡像） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA | FINRA／Advisor Perspectives WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag WebSearch（7d） | ✗ NOT DISCLOSED（搜尋完成，無顯著討論） |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／ycharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED（搜尋完成，無當期調查） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | 標售回顧 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Bloomberg WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]（30d） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報彙整 WebSearch（stock-of-state，carry-forward） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch AI WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話 [primary: SEARCH] | ✗ NOT DISCLOSED（無合格披露） |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報＋30 日融資事件 WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K／10-Q [primary: SEARCH]（30d） | ✗ NOT DISCLOSED（30 日內無變動） |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速＋進出場事件 WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／Benzinga／StockTitan [primary: SEARCH] | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR [primary: SEC EDGAR]／openinsider | ⛔ FETCH FAILED（EDGAR egress 受限，一手 Form 4 URL 無法取得） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com／ETFGI [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF.com WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED（7 日內無英文披露） |
| structural.zero_dte | 結構｜0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe／AInvest WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用散戶 margin debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]（30d） | ✗ NOT DISCLOSED（30 日內無新披露） |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo；aggregation any） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.08 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio（multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 41.52 | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E 約 40 trailing | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026（MarketXLS） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS 約 198bp 創紀錄、CoreWeave 約 665bp | Oracle CoreWeave CDS spread widening July 2026 | https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/（Real Investment Advice） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP +10.68% vs SPY +7.47% YTD | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-06-10 | 2026-07-20T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 36.40% | S&P 500 top 10 concentration percent 2026 | https://ahasignals.com/sp500-concentration-risk/（AHA Signals；原定 State Street SPDR 持股） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| breadth.advance_decline | NYSE 07-17 下跌約 2 倍於上漲、NH 241／NL 166 | NYSE advance decline breadth July 17 2026 | https://money.usnews.com/investing/news/articles/2026-07-17/wall-st-futures-fall-as-chip-selloff-gathers-pace-netflix-tumbles（U.S. News／Reuters） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（Fear） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed（MacroMicro；原定 cnn.com） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-05 月資料）$1.416T、+53.7% YoY | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra（Advisor Perspectives；原定 FINRA） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |
| retail.aaii | AAII Bull 44.9% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number（YCharts；原定 naaim.org） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 2.59、小幅 tail | US Treasury 10Y auction July 2026 bid to cover | https://cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/（Crypto Briefing；原定 TreasuryDirect） | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 FOMC 約 86.7% 定價持平 | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch（CryptoRank；原定 CME FedWatch） | 2026-07-18 | 2026-07-20T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance（Bloomberg） | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio 18.8%，依 5% quarterly redemption cap 比例撥付 | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://whbl.com/2026/07/02/blue-owl-keeps-withdrawal-limits-even-as-redemption-pressure-modestly-eases/（WHBL／Reuters） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 約 $700B、仍上修（上一季財報季彙整） | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html（Yahoo Finance） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 約 $47B／OpenAI 約 $25B run-rate | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 +13–18% QoQ | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html（TrendForce） | 2026-07-03 | 2026-07-20T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex 約 $700B vs AI 終端營收低百億級（分母：top-4 hyperscaler 彙整） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| speculation.ai_rename_spac | EVTV 更名 Azio AI（AZIO），2026-07-13 起以新代號交易 | AI rename ticker change July 2026 Azio EVTV | https://www.businesswire.com/news/home/20260710628386/en/Azio-AI-Holdings-Inc.-Nasdaq-EVTV-to-Begin-Trading-Under-New-Ticker-Symbol-AZIO-Completing-Corporate-Rebrand（Business Wire） | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD 約 200 檔 IPO、募資 $141.2B | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/（StockAnalysis；原定 Renaissance） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot 0 件 | microcap 100% single day quantum AI moonshot July 2026 | Finviz／Benzinga／StockTitan movers screener | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 投資人會議、估值約 $965B、可能 10 月掛牌 | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html（CNBC） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.73（日讀數） | Cboe equity put call ratio July 2026 | https://www.cboe.com/markets/us/options/market-statistics/daily/（Cboe） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 約 $198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing；原定 etf.com／ETFGI） | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 推出 6 檔 2x 單一個股 ETF（GOOGL／AMZN／META／AAPL） | single-stock leveraged ETF launch July 2026 Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html（GlobeNewswire） | 2026-07-07 | 2026-07-20T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 成交約 63% | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/（Cboe） | 2026-02-28 | 2026-07-20T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月 1,603,491,559 口、+45% YoY | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 145.13、VIX 約 16.5、期限結構 contango | VIX term structure SKEW July 2026 | https://www.ainvest.com/news/0dte-volatility-drives-market-strategies-2026-2602/（AInvest） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-05 月資料）$1.416T、+53.7% YoY（交叉引用） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra（Advisor Perspectives） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |

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
  "prior_answer": "yes",
  "flip_evidence": ["valuation.ndx_drawdown", "ai.hyperscaler_capex", "valuation.ai_credit_schism", "monetary.hy_oas"],
  "yes_basis": [],
  "r1_drawdown_pct": 6.74,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

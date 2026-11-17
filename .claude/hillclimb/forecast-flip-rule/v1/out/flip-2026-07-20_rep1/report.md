> [DRY RUN] this report was not committed to archive.

# 2026-07-20 AI 泡沫破裂預測報告

報告日期：2026-07-20｜ISO 週次：2026-W30｜預測窗口：2026-07-20 → 2027-01-18｜前次基準：report-2026-07-16（4天前）

## 結論

**結論：no**

三條路徑目前都沒有進入完成軌道：NASDAQ-100 距 52 週高點回撤僅 6.74%，距 R1 門檻仍需再跌約 19.58%（`valuation.ndx_drawdown`）；hyperscaler 2026 capex 指引合計約 $700B 且仍在上修，未見任何一家下修（`ai.hyperscaler_capex`）。AI 信用端雖有 Oracle／CoreWeave CDS 走闊（`valuation.ai_credit_schism`），但 HY OAS 僅 2.71%（`monetary.hy_oas`），尚無違約、distressed exchange 或破產跡象，不足以推翻「182 天內三條件皆不成立」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 28592.66（2026-07-17），252 個交易日最高收盤 30660.6（2026-06-02），距 52 週高點回撤 6.74%（`valuation.ndx_drawdown`）。R1 門檻水位為 22995.45，自最新收盤須再下跌約 19.58% 才會觸及。前次基準（2026-07-16）時回撤為 3.78%，本次擴大，主因 2026-07-17 晶片股賣壓：NYSE 當日下跌家數約為上漲家數 2 倍、新高 241／新低 166（`breadth.advance_decline`）。S&P 500 收 7457.69，較前次 −1.01%，仍高於 200 日均線 6.73%、高於 52 週均線 8.42%（`valuation.sp500_trend`）。VIX 升至 18.77，trailing 7 日（2026-07-10 → 2026-07-17）+24.88%，同期 S&P 500 −1.55%，屬正常的股跌波動升，非 crowded-optionality 共振（`structural.vix_spx_comove`）。估值脆弱性高：S&P 500 trailing P/E 32.08、Shiller CAPE 41.52（`valuation.sp500_pe_cape`），margin debt $1.416T、YoY +53.7%（`retail.margin_debt`），NAAIM 95.64（`retail.naaim`），代表一旦有催化劑，下跌幅度可能很大。

**判讀：** R1 尚遠；需要一個足以讓 NDX 由現水位再跌近兩成的催化劑（例如 AI 信用事件外溢、hyperscaler 財報指引轉弱或強制去槓桿），目前只有晶片股短線賣壓，未見傳導機制啟動。

### R2 資本支出收縮

- Microsoft：最新正式指引為 2026 年 Q1 財報季（彙整來源日期 2026-05-15）；彙整來源未逐家列示金額，方向為上修，未見下修。
- Alphabet：同上，2026 年 Q1 財報季指引，方向為上修，未見下修。
- Amazon：同上，2026 年 Q1 財報季指引，方向為上修，未見下修。
- Meta：同上，2026 年 Q1 財報季指引，方向為上修，未見下修。

彙整來源顯示 hyperscaler 2026 capex 合計約 $700B 且仍在上修（`ai.hyperscaler_capex`），四家中下修家數為 0。窗口內將涵蓋 2026 年 Q2 與 Q3 兩個財報季；本次證據未取得具體財報日期。需求側仍偏緊：TrendForce 指伺服器 DRAM 3Q26 合約價 QoQ +13–18%（`ai.compute_supply_demand`），與 capex 收縮方向相反。AI 營收對 capex 缺口（revenue-to-capex gap）仍大：年化 capex 約 $700B（分母：top-4 hyperscaler 彙整）對 AI 終端營收僅低百億級（`ai.revenue_capex_gap`），其中 Anthropic run-rate 約 $47B、OpenAI 約 $25B（`ai.openai_anthropic_revenue`）；缺口是長期 ROI 壓力，但不是短期內會觸發下修的證據。

**判讀：** R2 距成立最遠——需四家中兩家在接下來兩個財報季正式下修，而目前方向一致上修、記憶體合約價仍漲；只有在 R1 大幅回撤或融資條件急遽收緊時才可能轉向。

### R3 AI 信用事件

符合 R3 規模門檻的主要候選為 CoreWeave（以 AI 算力為主業、負債遠超 50 億美元）；Oracle 負債規模雖大，但主業並非 AI 資料中心，是否計入存疑。AI 信用定價分歧（equity-vs-credit schism）出現信用端先動的跡象：Oracle 5 年 CDS 約 198bp 創紀錄、CoreWeave 約 665bp（2026-07-16，`valuation.ai_credit_schism`），代表信用市場開始為 AI 基礎建設風險重定價。然而整體信用環境仍寬鬆：HY OAS 2.71%（`monetary.hy_oas`）、IG OAS 0.78%（`monetary.ig_oas`），repo 資金壓力（SOFR−IORB）為 −3bp，SOFR99−IORB 為 +5bp，SRF 動用（Standing Repo Facility usage）為 0（`monetary.repo_stress_srf`）。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）有實際事件：Blue Owl OCIC Q2 redemption-request ratio 18.8%，以 5% quarterly redemption cap 比例撥付，屬 gate proration / breach（2026-07-02，`monetary.private_credit_liquidity`），但來源同時指出贖回壓力略為緩和。本次 30 日內未發現新的 AI infrastructure debt financing / vendor-financing loops 披露，也沒有任何付款違約、covenant waiver、distressed exchange 或 going-concern 表述。

**判讀：** R3 是三條路徑中最接近的一條，CoreWeave CDS 約 665bp 已隱含顯著違約風險定價，但從 CDS 走闊到實際違約或 distressed exchange 通常需要再融資牆或流動性斷裂；在本次證據中未見到期牆或違約訊號，須等到出現具體再融資失敗或評等大幅下調才會推向 yes。

## 支持 yes 的證據

- [R3] Oracle 5 年 CDS 約 198bp 創紀錄、CoreWeave CDS 約 665bp（2026-07-16），信用端開始為 AI 基礎建設風險重定價，而股價仍接近高點，符合後期分歧訊號（`valuation.ai_credit_schism`）。
- [整體] Blue Owl OCIC Q2 redemption-request ratio 18.8%，遠超 5% quarterly redemption cap 而被比例撥付（2026-07-02），為私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）的實際 gate proration / breach 事件（`monetary.private_credit_liquidity`）。
- [R1] NASDAQ-100 回撤由前次 3.78% 擴大至 6.74%（2026-07-17），同日 NYSE 下跌家數約為上漲家數 2 倍，晶片股賣壓擴散（`valuation.ndx_drawdown`、`breadth.advance_decline`）。
- [整體] 估值與槓桿處於極端水位：Shiller CAPE 41.52、trailing P/E 32.08（`valuation.sp500_pe_cape`），margin debt $1.416T、YoY +53.7%（2026-05 月資料，`retail.margin_debt`），NAAIM 95.64（`retail.naaim`），一旦破裂幅度可能很大。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 capex 約 $700B（分母：top-4 hyperscaler 彙整）對 AI 終端營收低百億級（`ai.revenue_capex_gap`），長期 ROI 壓力未解。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 6.74%，R1 門檻水位 22995.45，自 28592.66 須再跌約 19.58%；在 182 天窗口內完成這段跌幅屬罕見事件（`valuation.ndx_drawdown`）。
- [R2] hyperscaler 2026 capex 合計約 $700B 且仍在上修（2026-05-15），四家中下修家數為 0（`ai.hyperscaler_capex`）。
- [R3] HY OAS 2.71%、IG OAS 0.78%（2026-07-16），整體信用利差仍極窄，未見 AI 信用壓力外溢（`monetary.hy_oas`、`monetary.ig_oas`）。
- [R3] repo 資金壓力（SOFR−IORB）−3bp、SRF 動用（Standing Repo Facility usage）為 0（`monetary.repo_stress_srf`），資金市場無緊張跡象；MOVE 70.88（`structural.treasury_basis_trade`）亦處低位。
- [R2] 伺服器 DRAM 3Q26 合約價 QoQ +13–18%（2026-07-03），算力需求端仍緊，與 capex 收縮方向相反（`ai.compute_supply_demand`）。
- [整體] 市場資金管道仍暢通：Anthropic 以約 $965B 估值舉行 IPO 投資人會議、可能 10 月掛牌（2026-07-15，`speculation.upcoming_ai_ipos`）；2026 YTD 約 200 檔 IPO、募資 $141.2B（`speculation.ipo_heat`）。

## 與前期比較

前次結論：yes（report-2026-07-16）
本次結論：翻轉
翻轉依據：
- `valuation.ndx_drawdown`：回撤由 3.78% 擴大至 6.74%，但距 R1 門檻仍需約 19.58% 跌幅；在 182 天窗口內這不構成「已在進行或可能完成」的 R1 路徑，前次 yes 在重新檢視下未達 rule 1 的門檻。
- `ai.hyperscaler_capex`：hyperscaler 2026 capex 指引仍在上修，四家中無一下修，R2 不支持 yes。
- `monetary.hy_oas`：HY OAS 2.71% 維持極窄，信用環境未出現足以推動 R1／R3 的系統性重定價。
- `valuation.ai_credit_schism`：Oracle／CoreWeave CDS 走闊是真實警訊，但僅為定價變化，尚無違約、distressed exchange 或再融資失敗，單獨不足以支撐 yes。
- 前次 forecast 未記錄 `yes_basis`，無可逐項延續的決定性理由；本次以現有證據重新判斷，結論為 no。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- speculation.insider_form4（⛔ FETCH FAILED）：SEC EDGAR 一手 Form 4 URL 因 egress 受限無法取得，篩選未能完整執行，故不以 0 件計。內部人賣壓屬情緒／估值輔助訊號，即使有大額 cluster 也不直接觸及 R1–R3，不會改變本次結論。

其他未披露（✗ NOT DISCLOSED）：analyst TP decomposition、social sentiment、BofA／JPM 調查、token growth、customer concentration／RPO、hyperscaler 融資結構、折舊年限變動、資本週期階段、global leveraged approvals、AI infrastructure debt financing。其中 AI infrastructure debt financing 與 hyperscaler 融資結構的空白與 R3 最相關——若有未被搜尋到的大型再融資困難，可能把 R3 推向 yes。

主要不確定性：

1. 2026 年 Q2 hyperscaler 財報季（窗口內）：若有兩家下修 capex 指引即直接觸發 R2；目前方向相反，但這是將答案推向 yes 的最直接節點。
2. CoreWeave 等 neocloud 的再融資與信用評等：CDS 約 665bp 代表市場已在定價壓力，若出現再融資失敗或 distressed exchange，R3 會成立並可能外溢至 R1。
3. 10Y 殖利率分解：ΔDGS10 0bp、ΔDFII10 0bp、ΔT10YIE +2bp，判讀為 `不可判（視窗不一致）`（DGS10、DFII10 無新觀測）；10Y 期限溢價（term premium）0.7788%、trailing 7 日 +4.7bp（`monetary.term_premium`）緩步上行，若財政再定價加速將推升折現率並加大 R1 壓力。

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
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1） | 45.76080873390133（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75（%） | FRED API (series_id=DFEDTARU) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5（%） | FRED API (series_id=DFEDTARL) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.71（%） | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.78（%） | FRED API (series_id=BAMLC0A0CM) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.57（%） | FRED API (series_id=DGS10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.35（%） | FRED API (series_id=DFII10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.24（%） | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 79.2（USD/bbl） | FRED API (series_id=DCOILWTICO) | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46（%） | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.21（%） | FRED API (series_id=T5YIFR) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest | 0.7788（%） | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.62（%） | FRED API (series_id=SOFR) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.7（%） | FRED API (series_id=SOFR99) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65（%） | FRED API (series_id=IORB) | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest | 0.0（$bn） | FRED API (series_id=RPONTTLD) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6743028.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5970516.0（€5.97T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6395509.0（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 18.77 | FRED API (series_id=VIXCLS) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 18.77 | FRED API (series_id=VIXCLS, SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 24.88 | FRED API (series_id=VIXCLS, SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2004.0237（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7562874（口） | CFTC TFF futures-only | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 70.88 | Yahoo Finance chart API (^MOVE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2342.6（$2.34T） | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation｜Mag 7 weighted P/E and AI leader P/S | MarketXLS via WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation｜Analyst TP upgrade decomposition | 賣方研報 WebSearch（90d＋same quarter） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API（sp500_trend ok） |
| valuation.ndx_drawdown | Valuation｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API（ndx_drawdown ok） |
| valuation.ai_credit_schism | Valuation｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst via WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth｜Top-10 concentration in S&P 500 | ahasignals via WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth｜Advance/decline ratio, new high/low ratio | NYSE breadth via WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment｜Margin Debt: FINRA monthly data | FINRA／Advisor Perspectives via WebSearch | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment｜Social sentiment proxies | WSB／cashtag WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API（BOGZ1FL153064486Q ok） |
| retail.naaim | Retail Sentiment｜NAAIM Exposure Index | naaim／ycharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | Institutional Sentiment｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（FRED） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit｜High Yield OAS | scripts/fetch_macro.py（FRED BAMLH0A0HYM2） | ✓ API（BAMLH0A0HYM2 ok） |
| monetary.ig_oas | Monetary & Credit｜Investment Grade OAS | scripts/fetch_macro.py（FRED BAMLC0A0CM） | ✓ API（BAMLC0A0CM ok） |
| monetary.dgs10 | Monetary & Credit｜10Y Treasury yield | scripts/fetch_macro.py（FRED DGS10） | ✓ API（DGS10 ok） |
| monetary.dfii10 | Monetary & Credit｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED DFII10） | ✓ API（DFII10 ok） |
| monetary.t10yie | Monetary & Credit｜10Y breakeven inflation rate | scripts/fetch_macro.py（FRED T10YIE） | ✓ API（T10YIE ok，FRED 直接取得） |
| monetary.wti | Monetary & Credit｜WTI crude oil price | scripts/fetch_macro.py（FRED DCOILWTICO） | ✓ API（DCOILWTICO ok） |
| monetary.cpi_yoy | Monetary & Credit｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（FRED CPIAUCSL yoy_pct） | ✓ API（CPIAUCSL ok） |
| monetary.t5yifr | Monetary & Credit｜5y5y forward inflation expectation | scripts/fetch_macro.py（FRED T5YIFR） | ✓ API（T5YIFR ok） |
| monetary.term_premium | Monetary & Credit｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（FRED THREEFYTP10） | ✓ API（THREEFYTP10 ok） |
| monetary.repo_stress_srf | Monetary & Credit｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（FRED） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit｜美債標售需求（auction tail / bid-to-cover） | auction recap WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（FRED WALCL） | ✓ API（WALCL ok） |
| monetary.ecb_boj | Monetary & Credit｜Global central bank liquidity cross-check — ECB / BOJ balance sheets | scripts/fetch_macro.py（FRED ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit｜PBoC aggregate financing / liquidity operations | Bloomberg via WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]（30d） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI Fundamentals｜Hyperscaler capex guidance | 季報彙整 via WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals｜AI token volume growth rate | Anthropic／OpenAI／Google WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals｜OpenAI / Anthropic annualized revenue | Epoch／The Information via WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報＋30d 融資事件 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q [primary: SEARCH]（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals｜資本週期階段（capital cycle stage） | 供需增速＋30d 進出場事件 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior｜Search for past 7 days: AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | Speculative Behavior｜IPO market heat | stockanalysis／Renaissance via WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior｜Microcap thematic moonshots | Finviz／Benzinga movers [primary: SEARCH]（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior｜Upcoming AI IPOs | S-1／具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 [primary: SEC EDGAR]（14d） | ⛔ FETCH FAILED（EDGAR egress 受限，一手 Form 4 URL 無法取得） |
| speculation.equity_put_call | Speculative Behavior｜Cboe equity-only put/call ratio | Cboe [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage｜US leveraged ETF AUM | etf.com／ETFGI [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage｜US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com launches（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | Structural Leverage｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage｜0DTE option volume | Cboe via WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage｜Options total volume: OCC monthly volume report | theocc.com via WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage｜Cross-asset derivatives / correlation checks | Cboe／AInvest via WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（FRED VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage｜Cross-reference only: FINRA margin debt | 交叉引用 Retail Sentiment margin debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]（30d） | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | Structural Leverage｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API（LNFACBW027SBOG ok） |
| structural.treasury_basis_trade | Structural Leverage｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）＋WebSearch fallback | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.08 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio（multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 41.52 | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E ≈40 trailing | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026（MarketXLS） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS ≈198bp 創紀錄、CoreWeave ≈665bp | Oracle CoreWeave CDS spread widening July 2026 | https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/（RIA） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP +10.68% vs SPY +7.47% YTD | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（247wallst） | 2026-06-10 | 2026-07-20T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 36.40% | S&P 500 top 10 concentration percent 2026 | https://ahasignals.com/sp500-concentration-risk/（ahasignals） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| breadth.advance_decline | NYSE 2026-07-17 下跌約 2×上漲、NH 241／NL 166 | NYSE advance decline breadth July 17 2026 | https://money.usnews.com/investing/news/articles/2026-07-17/wall-st-futures-fall-as-chip-selloff-gathers-pace-netflix-tumbles（US News／Reuters） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（Fear） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed（MacroMicro；原定 cnn.com） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-05 月資料）$1.416T、YoY +53.7% | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra（Advisor Perspectives；原定 FINRA） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |
| retail.aaii | AAII Bull 44.9% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number（YCharts；原定 naaim.org） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 2.59、小幅 tail | US Treasury 10Y auction July 2026 bid to cover | https://cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/（Crypto Briefing；原定 Reuters／TreasuryDirect） | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 會議維持利率 ≈86.7% | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch（CryptoRank；原定 CME FedWatch） | 2026-07-18 | 2026-07-20T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance（Bloomberg） | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio 18.8%，依 5% quarterly redemption cap 比例撥付 | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://whbl.com/2026/07/02/blue-owl-keeps-withdrawal-limits-even-as-redemption-pressure-modestly-eases/（WHBL／Reuters） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計 ≈$700B、仍上修（2026 Q1 財報季指引） | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html（Yahoo Finance） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic ≈$47B／OpenAI ≈$25B run-rate | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 +13–18% QoQ | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html（TrendForce） | 2026-07-03 | 2026-07-20T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex ≈$700B vs AI 終端營收低百億級（分母：top-4 hyperscaler 彙整） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| speculation.ai_rename_spac | EVTV→Azio AI（AZIO）改名，2026-07-13 起以新代號交易 | AI rename ticker change July 2026 Azio EVTV | https://www.businesswire.com/news/home/20260710628386/en/Azio-AI-Holdings-Inc.-Nasdaq-EVTV-to-Begin-Trading-Under-New-Ticker-Symbol-AZIO-Completing-Corporate-Rebrand（Business Wire） | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD ≈200 檔 IPO、募資 $141.2B | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/（StockAnalysis） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot 0 件 | microcap 100% single day quantum AI moonshot July 2026 | Finviz／Benzinga／StockTitan movers screener | — | 2026-07-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 投資人會議、估值 ≈$965B、可能 10 月掛牌 | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html（CNBC） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.73（daily） | Cboe equity put call ratio July 2026 | https://www.cboe.com/markets/us/options/market-statistics/daily/（Cboe） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM ≈$198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing；原定 etf.com／ETFGI） | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x GOOGL／AMZN／META／AAPL 單一個股槓桿 ETF 上市 | single-stock leveraged ETF launch July 2026 Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html（GlobeNewswire） | 2026-07-07 | 2026-07-20T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權成交 ≈63% | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/（Cboe） | 2026-02-28 | 2026-07-20T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月成交 1,603,491,559 口、YoY +45% | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 145.13、VIX ≈16.5 期限結構 contango | VIX term structure SKEW July 2026 | https://www.ainvest.com/news/0dte-volatility-drives-market-strategies-2026-2602/（AInvest；原定 Cboe） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-05 月資料）$1.416T、YoY +53.7%（交叉引用 Retail Sentiment） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra（Advisor Perspectives） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |

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
  "flip_evidence": ["valuation.ndx_drawdown", "ai.hyperscaler_capex", "monetary.hy_oas", "valuation.ai_credit_schism"],
  "yes_basis": [],
  "r1_drawdown_pct": 6.74,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

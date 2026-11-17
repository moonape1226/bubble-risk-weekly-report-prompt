> [DRY RUN] this report was not committed to archive.

# 2026-08-06 AI 泡沫破裂預測報告
報告日期：2026-08-06｜ISO 週次：2026-W32｜預測窗口：2026-08-06 → 2027-02-04｜前次基準：report-2026-08-03（3天前）

## 結論

**結論：no**

三條路徑目前都沒有在 182 天內完成的跡象：NASDAQ-100 只距 52 週高點回撤 3.83%（2026-08-05），還要再跌約 22% 才觸及 R1；四家 hyperscaler 都沒有下修 capex，反而續上修（R2）。R3 的 CoreWeave 信用壓力是真實的，但 HY OAS 已收窄至 2.73%（2026-08-04），尚未擴散成違約或 distressed exchange。估值與槓桿極端，代表泡沫存在且下行空間大，但不足以推翻「窗口內不發生」的基本率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,487.79（2026-08-05），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 3.83%。R1 門檻水位為 22,995.45，須自最新收盤再下跌約 22.0% 才觸及（`valuation.ndx_drawdown`）。前次（2026-08-03）的回撤為 7.78%，距門檻約 18.7%；此後指數反彈，距門檻反而拉遠。同期 S&P 500 收 7,723.55，高於 200 日均線 9.71%、高於 52 週均線 11.32%（`valuation.sp500_trend`）。VIX 為 15.81，近 7 日下跌 23.48%，S&P 500 同期上漲 5.57%，未出現股、波同漲的警戒讀數（`structural.vix_spx_comove`）。估值偏高：trailing P/E 29.74、Shiller CAPE 42.19（`valuation.sp500_pe_cape`）；FINRA margin debt 年增 +51.5%（`retail.margin_debt`）。

**判讀：** R1 距觸發還很遠。要在窗口內成立，需要一次約 22% 的急跌，通常得有外部催化劑，例如 AI 信用事件擴散（R3→R1）、季報季 capex 敘事反轉，或美債標售／期限溢價推動利率急升。高估值與高槓桿會放大下跌幅度，但目前看不到已經啟動的跌勢。

### R2 資本支出收縮

最新季報季（2026 Q2，2026-07 下旬公布）的結果是：hyperscaler 2026 年 capex 續上修，合計約 $725B；Alphabet 再度上修，財報後出現賣壓（`ai.hyperscaler_capex`，CNBC 2026-07-28）。逐家指引方向：Alphabet 上修；Microsoft、Amazon、Meta 在取得的 evidence 中只以合計方式呈現為「續上修」，個別指引數字本次未逐一取得，但沒有任何一家下修的報導。四家中已下修家數為 0。供給面，HBM／DRAM 合約價續升、H200 租金約 $4.39/hr，供給缺口延至 1H2027（`ai.compute_supply_demand`），看不到 order digestion。下一輪（2026 Q3）與再下一輪（2026 Q4）季報都可能落在窗口內（至 2027-02-04），確切日期本次未取得。

**判讀：** R2 距觸發最遠。四家仍在上修，算力仍供不應求。要在窗口內成立，需要兩家在接下來一到兩次季報中由上修轉為下修，前提通常是 R1 式的市場壓力或明確的需求轉弱。Microsoft RPO 約 32% 繫於單一客戶（OpenAI）（`ai.customer_concentration_rpo`），是需求端最可能出現裂縫的地方。

### R3 AI 信用事件

信用定價已經開始分化：CoreWeave 5Y CDS 約 855bp，其一筆 $2.6B 貸款利差擴大 +125bp，放款人要求增加 covenants；Oracle CDS 約 215bp（`valuation.ai_credit_schism`，2026-08-03）。CoreWeave 於 2026-07-29 調高其 $2.6B Anthropic 掛鉤貸款的票息；Nebius 於 2026-07-17 取得 $775M 擔保融資（`structural.ai_infrastructure_debt`）。CoreWeave 是最可能符合 R3 規模門檻的借款人，但其總負債規模不在本次 evidence 中，因此門檻是否成立未以本次資料驗證。Oracle 主業不是 AI 資料中心，不屬 R3 借款人。本次沒有取得付款違約、寬限期、covenant waiver、distressed exchange 或 going-concern 的披露。整體信用市場平靜：HY OAS 2.73%（2026-08-04，較前次收窄 5bp）（`monetary.hy_oas`），IG OAS 0.78%（`monetary.ig_oas`），SOFR−IORB 僅約 1bp、SRF 動用約 $0.001bn（`monetary.repo_stress_srf`）。

**判讀：** R3 是三條路徑中最接近的一條。CoreWeave 的 CDS 水位與貸款重定價，屬於 AI 信用定價分歧（equity-vs-credit schism）中「信貸端開始重定價」的後期訊號；但重定價和違約之間還差一個融資中斷。要在窗口內成立，CoreWeave 這類借款人必須失去再融資管道，進而付款違約或完成 distressed exchange。目前它仍能以較高利差取得資金，大盤信用也沒有傳染。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 約 855bp、$2.6B 貸款利差擴大 +125bp、放款人要求 covenants（2026-08-03），是 AI 借款人信用開始重定價的直接證據，`valuation.ai_credit_schism`
- [R3] CoreWeave 於 2026-07-29 調高 $2.6B Anthropic 掛鉤貸款票息、Nebius 於 2026-07-17 取得 $775M 擔保融資，顯示 neocloud 再融資成本上升，且依賴特定 AI 客戶，`structural.ai_infrastructure_debt`
- [R2] Microsoft RPO 約 $678B，其中約 32% 繫於 OpenAI（2026-07-30）；backlog 重複計算風險（RPO double-counting）與單一客戶集中，是需求端轉弱時 capex 被迫修正的主要通道，`ai.customer_concentration_rpo`
- [整體] 估值與槓桿極端：S&P 500 trailing P/E 29.74、CAPE 42.19（2026-08-05，`valuation.sp500_pe_cape`）；FINRA 6 月 margin debt $1.502T、年增 +51.5%（`retail.margin_debt`）；US 槓桿 ETF AUM 創高約 $198B（`structural.leveraged_etf_aum`）。一旦有催化劑，跌幅會被放大
- [R1] 美債供給壓力：5Y 標售連續 14 次 tail、bid-to-cover 為 2022-09 以來最差、7Y tail 0.8bp（2026-07-28，`monetary.treasury_auctions`）；10Y 期限溢價（term premium）0.8681%，7 日內上升 3bp（2026-07-31，`monetary.term_premium`），為利率衝擊估值的潛在路徑

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 3.83%（2026-08-05），R1 門檻 22,995.45 需再跌約 22%；前次為 7.78%，距離拉大，`valuation.ndx_drawdown`
- [R2] hyperscaler 2026 capex 續上修，合計約 $725B，Alphabet 再上修（2026-07-28），四家中下修家數為 0，`ai.hyperscaler_capex`
- [R3] 大盤信用沒有傳染：HY OAS 2.73%（2026-08-04，收窄 5bp）（`monetary.hy_oas`）、IG OAS 0.78%（`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）約 1bp，SRF 動用接近零（`monetary.repo_stress_srf`）
- [R2] 算力供不應求：HBM／DRAM 合約價續升、H200 租金約 $4.39/hr，缺口延至 1H2027（2026-08-01），與 capex 收縮方向相反，`ai.compute_supply_demand`
- [整體] 風險偏好穩定、尚未失序：VIX 15.81，近 7 日下跌 23.48%，與 S&P 500 同期上漲 5.57% 呈正常反向（`structural.vix_spx_comove`）；MOVE 由 80.48 降至 73.58（`structural.treasury_basis_trade`）；CNN Fear & Greed 約 58（`retail.fear_greed`）；RSP 年初至今 +14.26%，領先 SPY +13.71%，市場廣度擴散（`breadth.rsp_spy`）

## 與前期比較

前次結論：yes（report-2026-08-03）
本次結論：翻轉
翻轉依據：
- `valuation.ndx_drawdown`：NASDAQ-100 回撤由前次的 7.78% 收窄至 3.83%（2026-08-05），觸及 R1 所需跌幅由約 18.7% 擴大至約 22%。R1 由「已在下行途中」變為「仍在高點附近」，最直接的 yes 路徑失去動能。
- `monetary.hy_oas`：HY OAS 由 2.78% 收窄至 2.73%（2026-08-04）。前次判斷的關鍵是 CoreWeave 信用壓力可能外溢；高收益信用在前次之後反而收窄，顯示傳染沒有發生，R3→R1 的傳導鏈證據轉弱。
- `structural.vix_spx_comove`：VIX 15.81（2026-08-05），近 7 日下跌 23.48%，S&P 500 同期上漲 5.57%，未出現股、波同漲；風險偏好回穩，不支持短期失序。
- 未改變的部分：CoreWeave CDS／貸款重定價的資料日為 2026-08-03，與前次同日，不是新證據；R3 仍是最接近的路徑。三條路徑合計仍未達「較可能發生」，因此本次翻轉為 no。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

完成搜尋但無合格披露（✗ NOT DISCLOSED）的來源及其影響：
- `monetary.private_credit_liquidity`：過去 30 日沒有 BDC／interval fund 的 redemption-request ratio、gate proration / breach 或 net inflow→outflow flip 披露。若實際有，會強化 R3 的私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）路徑，是可能改變答案的最大缺口。
- `ai.hyperscaler_financing_mix`（event_scan 無 30 日內事件；quarterly_state 沿用：top-5 capex 已超越 FCF、2026 發債約 $182B、表外 SPV 逾 $120B，2026-07-24）與 `ai.capital_cycle`（兩組件皆無可用披露）：增速證據不足，本次不判定週期階段。
- `ai.openai_anthropic_revenue`：最近披露為 2026-06-15（上一季），不屬本季，因此不作為新證據；`ai.revenue_capex_gap` 只沿用該組件。
- `ai.depreciation_life`、`ai.token_growth`、`retail.naaim`、`institutional.bofa_jpm_survey`、`structural.global_leveraged_approvals`：無合格披露，預期不會改變答案。
- `speculation.insider_form4`：SNOW 的 Form 4 只取得單一日期（2026-07-29），filing 日沒有單獨列出；TEM 的交易沒有取得其自身的 EDGAR URL。兩者都不作為本文證據使用。

最大的不確定性：
1. CoreWeave 的再融資路徑：若放款人拒絕展期，或出現 covenant waiver／distressed exchange，R3 可能直接成立並經 R1 傳導，會把答案推向 yes。CoreWeave 的總負債是否達 R3 門檻，本次沒有以資料驗證。
2. 窗口內的兩輪 hyperscaler 季報（2026 Q3、Q4）：若有兩家下修 capex，R2 成立。目前方向相反，但 Microsoft 的 RPO 高度集中於 OpenAI，一旦 OpenAI 融資受阻，可能迅速翻轉。
3. 利率與財政：美債標售連續 tail、期限溢價上升、FOMC 鷹派持平（CME FedWatch 9 月約 62%，定價分歧）。若長端利率急升，可能觸發 R1 式估值壓縮，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7723.55 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線） | 9.71 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線） | 11.32 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29487.79 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 3.83 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q1） | 45.76080873390133（≈45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.73 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 prior（前次基準日） | 2.78 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.63 | FRED API (series_id=DGS10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.4 | FRED API (series_id=DFII10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.22 | FRED API (series_id=T10YIE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 81.96 | FRED API (series_id=DCOILWTICO) | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-08-06T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.26 | FRED API (series_id=T5YIFR) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8681 | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.66 | FRED API (series_id=SOFR) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.74 | FRED API (series_id=SOFR99) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-08-06 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（transaction volume） | 0.001（十億美元） | FRED API (series_id=RPONTTLD) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,738,190（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,941,248（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,442,957（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.81 | FRED API (series_id=VIXCLS) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of） | 15.81 | scripts/fetch_macro.py vix_spx_comove block | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日） | -23.48 | scripts/fetch_macro.py vix_spx_comove block | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日） | 5.57 | scripts/fetch_macro.py vix_spx_comove block | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2004.9941（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-22 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7,481,041（口） | CFTC TFF (cftc_lev_funds) | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.58 | Yahoo chart ^MOVE (move_index) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index prior（前次基準日） | 80.48 | Yahoo chart ^MOVE (move_index) | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2342.8（十億美元） | OFR STFM REPO-TRIV1_TV_TOT-P (ofr_repo) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | SSGA [SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方 TP 調升掃描 [primary: SEARCH] | ✓ SEARCH-VERIFIED（EPS Δ／PE Δ 未披露，僅標 EPS-driven） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧 | 信用市場 14 日掃描 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | financecharts [SEARCH] | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | P&I [SEARCH] | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | StockCharts [SEARCH] | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA via Advisor Perspectives [SEARCH] | ✓ SEARCH-VERIFIED（2026-06 月資料沿用） |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag [SEARCH] | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py BOGZ1FL153064486Q | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／YCharts [primary: SEARCH] | ✗ NOT DISCLOSED（無本週值） |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 [SEARCH] | ✗ NOT DISCLOSED（無新調查） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | 標售 recap [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | investing.com [SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 30 日掃描 [primary: SEARCH] | ✗ NOT DISCLOSED（30 日內無合格披露） |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 2026 Q2 季報 [SEARCH] | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google [SEARCH] | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／報導 [SEARCH] | ✗ NOT DISCLOSED（最近披露 2026-06-15 屬上一季） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | GPU 租金／HBM 合約 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state 沿用＋event_scan 30 日掃描 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露（沿用各組件） [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K／10-Q 30 日掃描 [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速＋進出場事件 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | Reuters／Benzinga／BusinessWire 螢幕 [SEARCH] | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | Renaissance Capital [SEARCH] | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／StockAnalysis／StockTitan [primary: SEARCH] | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 [SEARCH] | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 [primary: SEC EDGAR] | ✓ SEARCH-VERIFIED |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | YCharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire 發行公告 [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA [SEARCH] | ✗ NOT DISCLOSED（7 日內無英文披露） |
| structural.zero_dte | 結構｜0DTE option volume | Cboe Q2 2026 簡報 [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC monthly volume report | theocc.com [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe insights [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py VIXCLS＋vix_spx_comove | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | FINRA via Advisor Perspectives（交叉引用） [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | 30 日融資掃描 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds／move_index／ofr_repo | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.74 | S&P 500 trailing P/E August 5 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio（multpl；原定 multpl/gurufocus） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.19 | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 約 29x vs 指數約 25.6x，溢價壓縮 | Magnificent 7 valuation premium lowest decade 2026 | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026（SSGA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA TP $285→$288，EPS-driven（EPS Δ／PE Δ 未披露） | Morgan Stanley NVDA target 288 July 2026 AI demand | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044（Investing.com） | 2026-07-13 | 2026-08-06T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 約 855bp、$2.6B 貸款利差 +125bp、Oracle CDS 約 215bp | CoreWeave CDS spread blows out 125 covenants Oracle August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm（Tech Times） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD +14.26% vs SPY +13.71% | RSP vs SPY equal weight total return YTD August 2026 | https://www.financecharts.com/etfs/SPY/performance/total-return（FinanceCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度約 41% | S&P 500 top 10 concentration percent record 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/（P&I） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| breadth.advance_decline | 約 64% 成分股在 50DMA 上、A/D 創高、McClellan 轉負 | S&P 500 breadth percent above 50 day moving average August 2026 McClellan | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/（StockCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 58（Greed） | CNN Fear and Greed Index August 5 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives；原定 FINRA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| retail.aaii | AAII Bull 31.0%／Neutral 26.9%／Bear 42.1% | AAII investor sentiment survey July 30 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| retail.social_sentiment | WSB「Save Wendy's」（WEN）軋空，空頭比重約 44% | Reddit WSB Wendy's WEN short squeeze August 2026 | https://finance.yahoo.com/markets/stocks/articles/reddit-wants-save-wendy-inside-161925726.html（Yahoo Finance） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超越 FCF、2026 發債約 $182B、表外 SPV 逾 $120B | hyperscaler capex FCF debt issuance 182 billion off balance sheet SPV 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure（Sage Advisory） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| monetary.treasury_auctions | 5Y 連續 14 次 tail、bid-to-cover 為 2022-09 以來最差；7Y tail 0.8bp | US Treasury 5 year 7 year auction tail bid to cover July 2026 | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026（TFTC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| monetary.fedwatch | FOMC 7/29 鷹派持平；CME FedWatch 9 月約 62%，定價分歧 | CME FedWatch September 2026 probability FOMC hold | https://growbeansprout.com/tools/fedwatch（Beansprout；原定 CME FedWatch） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.pboc | 人行逆回購約 ¥2.1T、7/24 MLF 淨投放 ¥100B | PBoC reverse repo injection 2.1 trillion yuan late July 2026 | https://www.investing.com/news/economy-news/chinas-pboc-to-conduct-overnight-reverse-repos-inject-a-total-of-21-trillion-yuan-4810853（Investing.com） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_capex | 2026 Q2 季報：hyperscaler 2026 capex 續上修，合計約 $725B；Alphabet 上修 | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO 約 $678B，約 32% 繫於 OpenAI | Microsoft RPO backlog 678 billion single customer OpenAI 2026 | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/（Benzinga via TradingView） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| ai.compute_supply_demand | HBM／DRAM 合約續升、H200 租金約 $4.39/hr、缺口延至 1H2027 | H200 GPU rental price HBM DRAM contract 2026 shortage 2027 | https://jarvislabs.ai/blog/h200-price（JarvisLabs） | 2026-08-01 | 2026-08-06T09:30:00+08:00 |
| ai.revenue_capex_gap | 分子：AI 終端年化營收約 $72B（Anthropic 約 $47B＋OpenAI 約 $25B，沿用） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-06-15 | 2026-08-06T09:30:00+08:00 |
| ai.revenue_capex_gap | 分母：hyperscaler 2026 年化 capex 合計約 $725B（涵蓋公司集合未逐一列出） | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日內 AI 改名／SPAC／無營收 IPO 合格件數 0 | AI rename ticker SPAC no revenue IPO July 30 August 6 2026 | Reuters／Benzinga／BusinessWire SPAC 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.ipo_heat | 約 21 檔跨週定價、無 blowout 首日、YTD 約 $251B／86 檔 | US IPO pricings week August 3 2026 Renaissance | https://www.renaissancecapital.com/IPO-Center/Pricings（Renaissance Capital） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週 microcap thematic moonshot 合格 0 件 | microcap 100% single day quantum fusion space nuclear small cap August 2026 | Finviz／StockAnalysis／StockTitan gainers 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標約 $1T IPO、Anthropic 續進 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground（Benzinga） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| speculation.insider_form4 | SNOW 董事 Dageville 售 50,000 股，約 $14.0M（evidence 僅列單一日期 2026-07-29，filing 日未單獨列出） | Snowflake Dageville Tempus Lefkofsky Form 4 insider sale July 2026 SEC | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1640147&type=4（SEC EDGAR） | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.55（daily 或 5 日平均未標明） | Cboe equity put call ratio August 3 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio（YCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高約 $198B | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing；原定 etf.com） | 2026-07-23 | 2026-08-06T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x 單股槓桿 ETF＋ELOL（TSLA+SpaceX）發行 | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html（GlobeNewswire） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量約 65%（Cboe Q2 2026） | 0DTE SPX options share volume Cboe Q2 2026 65% | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641（Investing.com） | 2026-05-31 | 2026-08-06T09:30:00+08:00 |
| structural.options_volume | OCC 6 月總量 16.0 億口（2026-06 月資料） | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 約 139.96、VIX 約 16.9 contango、TLT 1M skew 創 GFC 以來高 | VIX SKEW term structure bond volatility August 3 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher（Cboe） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.margin_debt_crosscheck | 交叉引用：margin debt（2026-06 月資料）$1.502T、+51.5% YoY | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B Anthropic 掛鉤貸款於 07-29 調高票息；Nebius 於 07-17 取得 $775M 擔保 | CoreWeave 2.6 billion loan Anthropic yield boosted July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic（Bloomberg） | 2026-07-29 | 2026-08-06T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-06",
  "iso_week": "2026-W32",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-04",
  "prior_date": "2026-08-03",
  "prior_answer": "yes",
  "flip_evidence": ["valuation.ndx_drawdown", "monetary.hy_oas", "structural.vix_spx_comove"],
  "r1_drawdown_pct": 3.83,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

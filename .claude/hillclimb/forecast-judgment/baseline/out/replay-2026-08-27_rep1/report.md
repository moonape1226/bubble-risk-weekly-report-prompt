> [DRY RUN] this report was not committed to archive.

# 2026-08-27 AI 泡沫破裂預測報告
報告日期：2026-08-27｜ISO 週次：2026-W35｜預測窗口：2026-08-27 → 2027-02-25｜前次基準：report-2026-08-24（3天前）

## 結論

**結論：no**

三條路徑目前都遠離觸發點：NASDAQ-100 距 52 週高點回撤 4.68%，離 R1 門檻還差約 21.31% 的跌幅；hyperscaler 2026 年 capex 合計仍以 +77% YoY 上行，信用端 HY OAS 2.70%、IG OAS 0.81% 也沒有出現 R3 所需的違約傳導跡象。估值與槓桿偏高說明泡沫存在、下跌空間大，但在 182 天窗口內，本次證據找不到任何已經啟動的觸發催化劑。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,224.52（2026-08-26），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 4.68%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45；以最新收盤計，還需再跌約 6,229 點（約 21.31%）才會觸發。S&P 500 收在 7,675.70（2026-08-26），比 200 日均線高 7.97%、比 52 週均線高 9.40%（`valuation.sp500_trend`），價格偏離均線，但還不到極端水準。波動與避險定價平靜：VIX 15.45（2026-08-25），過去 7 天 VIX −2.46%、S&P 500 −0.19%，沒有出現 crowded-optionality 式的同步上漲（`structural.vix_spx_comove`）；MOVE 69.44（2026-08-26）（`structural.treasury_basis_trade`）。估值脆弱度偏高：Shiller CAPE ≈41.3、trailing P/E ≈26.2（`valuation.sp500_pe_cape`），Mag 7 加權 P/E ≈29.5x（`valuation.mag7_multiples`）。

**判讀：** R1 離觸發還很遠，指數只比高點低不到 5%。要在窗口內跌到 25%，需要一個外生催化劑，例如 R3 信用事件、大型 AI IPO 的股權供給衝擊（Anthropic 目標 10 月 IPO），或財報季 capex 指引轉向。在高估值與高槓桿結構下，一旦啟動，跌幅可能放大，但本次沒有看到已經開始的去槓桿跡象。

### R2 資本支出收縮

本次證據只取得 top-4 合計值：2026 年 hyperscaler capex 合計約 $725bn，+77% YoY（資料日期 2026-08-13，Q2 財報後，`ai.hyperscaler_capex`）。逐家情況如下：

- Microsoft：最新官方指引在本次蒐集的證據中沒有逐家數字；以 Q2 財報季後的合計值看，沒有下修紀錄。
- Alphabet：同上，證據沒有個別指引數字，沒有下修紀錄。
- Amazon：同上，證據沒有個別指引數字，沒有下修紀錄。
- Meta：同上，證據沒有個別指引數字，沒有下修紀錄。

目前四家之中已下修家數為 0。下一次財報日期本次證據未載明；依季報節奏，窗口（至 2027-02-25）內會涵蓋 Q3 與 Q4 兩輪財報，這是 R2 唯一的觸發時點。需求面仍強：GPU 現貨租金超過合約價 2 倍，產能被利用率吸收（2026-08-13，`ai.compute_supply_demand`）；Anthropic run-rate 約 $65B、OpenAI 約 $40B（2026-08-17，`ai.openai_anthropic_revenue`）。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 $105bn，年化 capex 約 $725bn（分母：top-4，未含 Oracle 與 neocloud），缺口很大（`ai.revenue_capex_gap`）。

**判讀：** R2 需要四家中至少兩家下修。合計 capex 仍以 +77% 擴張，且算力供不應求，窗口內兩輪財報同時出現兩家下修的條件尚未形成。可能把 R2 推過門檻的情境是 R1 先發生深度回撤或融資成本急升，迫使管理層收縮 2027 年指引。

### R3 AI 信用事件

規模達門檻（負債 ≥ 50 億美元、以 AI 算力為主業）的主要借款人是 CoreWeave。本次唯一的當期事件：2026-08-10，CoreWeave 完成一筆 $2.6B、以 HPC 基建為擔保的 delayed-draw 定期貸款設施（`structural.ai_infrastructure_debt`）。這筆交易顯示槓桿仍在增加，但融資管道暢通。本次沒有查到任何當期的 AI 發行人債券利差、CDS 或評等動作，也沒有付款違約、covenant waiver、distressed exchange 或 going-concern 措辭。整體信用環境寬鬆：HY OAS 2.70%（2026-08-25，`monetary.hy_oas`），IG OAS 0.81%（`monetary.ig_oas`）。repo 資金壓力（SOFR−IORB）為 1bp，99 分位尾部利差 9bp，SRF 動用（Standing Repo Facility usage）僅 $0.003bn（`monetary.repo_stress_srf`）。

**判讀：** R3 需要大型 AI 算力借款人實際違約或完成 distressed exchange。目前融資市場仍願意提供新的擔保設施，信用利差處於低檔，距離違約事件還有好幾個階段（利差走闊 → 再融資受阻 → 寬限期違約）。窗口內可能的推力是再融資牆與客戶合約集中度風險，但本次沒有可引用的當期證據顯示這些風險已經發酵。

## 支持 yes 的證據

- [整體] 估值處於歷史極端：Shiller CAPE ≈41.3、S&P 500 trailing P/E ≈26.2（2026-08-26，`valuation.sp500_pe_cape`），Mag 7 加權 P/E ≈29.5x（2026-08-26，`valuation.mag7_multiples`）；一旦有催化劑，下跌空間大。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 $105bn，年化 capex 約 $725bn（分母：top-4），營收只覆蓋約七分之一（2026-08-17，`ai.revenue_capex_gap`）；如果回本敘事動搖，capex 指引承壓。
- [R1] 散戶槓桿接近歷史頂部區：FINRA margin debt（2026-07）YoY +38.6%（`retail.margin_debt`），逼近 1999／2007／2021 頂部的 +40–50% 區間；美股槓桿 ETF 總 AUM 創紀錄約 $198bn（2026-08-17，`structural.leveraged_etf_aum`）；SPX 0DTE 佔比創紀錄約 62.4%（2026-08-14，`structural.zero_dte`）。下跌時可能形成被迫去槓桿。
- [R1] 價格延伸與家庭持股飽和：S&P 500 高於 200 日均線 7.97%、高於 52 週均線 9.40%（2026-08-26，`valuation.sp500_trend`）；家庭股票配置佔金融資產 45.76%（2026Q1，`retail.household_equity_allocation`），新增買盤空間有限。
- [R1] 股權供給催化劑落在窗口內：Anthropic 目標 10 月 IPO、估值約 $2T（2026-08-17，`speculation.upcoming_ai_ipos`），可能吸走 AI 股權資金。
- [R3] AI infrastructure debt financing / vendor-financing loops 持續加碼：CoreWeave 2026-08-10 再取得 $2.6B delayed-draw 擔保貸款（`structural.ai_infrastructure_debt`），R3 候選借款人的負債規模繼續上升。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.68%（2026-08-26），離 R1 門檻水位 22,995.45 還需再跌約 21.31%（`valuation.ndx_drawdown`）；基準率上，182 天內從近高點跌 25% 是少見事件。
- [R3] 信用市場沒有任何壓力：HY OAS 2.70%（2026-08-25，`monetary.hy_oas`）、IG OAS 0.81%（`monetary.ig_oas`）；CoreWeave 在 2026-08-10 仍能完成 $2.6B 新設施（`structural.ai_infrastructure_debt`），顯示融資管道暢通，離違約／distressed exchange 很遠。
- [R2] capex 軌跡向上：top-4 2026 年 capex 合計約 $725bn，+77% YoY（2026-08-13，`ai.hyperscaler_capex`）；GPU 現貨租金超過合約價 2 倍，產能被利用率吸收（2026-08-13，`ai.compute_supply_demand`），沒有需求轉弱導致下修的跡象。
- [整體] AI 終端需求快速成長：Anthropic run-rate 約 $65B、OpenAI 約 $40B（2026-08-17，`ai.openai_anthropic_revenue`），Anthropic run-rate 年增約 7 倍（`ai.token_growth`），缺口在收斂方向。
- [整體] 融資與波動市場平靜：repo 資金壓力（SOFR−IORB）1bp、SRF 動用 $0.003bn（`monetary.repo_stress_srf`）；MOVE 69.44，槓桿基金美債期貨淨空單 4 週減少 244,468 口（`structural.treasury_basis_trade`）；VIX 15.45，沒有和指數同步上漲（`structural.vix_spx_comove`）。
- [整體] 情緒並不亢奮：CNN Fear & Greed 55（2026-08-25，`retail.fear_greed`）；AAII 偏多 35.5% 低於偏空 39.9%（2026-08-19，`retail.aaii`）；等權 RSP 領先 SPY 約 1.7pp，領導面擴散（2026-08-23，`breadth.rsp_spy`）。

## 與前期比較

前次結論：無前次預測（report-2026-08-24 為舊格式評分報告）

前次為舊格式六維評分報告，沒有 yes/no 預測可比較，所以 flip_evidence 為空，舊評分也不轉換為答案。自 2026-08-24 以來，主要市場數據變動如下：

- 10Y 殖利率 4.70% → 4.64%（ΔDGS10 −6bp），實質利率 ΔDFII10 −6bp，ΔT10YIE 0bp。T10YIE 的視窗和前兩者不同，所以驅動因素判讀為不可判（視窗不一致）。
- HY OAS 2.69% → 2.70%（+1bp），IG OAS 持平於 0.81%，信用面沒有變化。
- S&P 500 7,652.86 → 7,675.70（+0.30%），MOVE 73.98 → 69.44，波動回落。
- WTI 86.34 → 83.90（−2.83%）；WALCL、ECB、BOJ 資產負債表與銀行對 NBFI 放款都沒有新觀測（持平）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源都已完成檢索但沒有合格的當期披露（✗ NOT DISCLOSED）：valuation.analyst_tp_decomposition、valuation.ai_credit_schism、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.treasury_auctions、monetary.pboc、monetary.private_credit_liquidity、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（quarterly_state 可用、event_scan 30 日內無事件）、ai.depreciation_life、ai.capital_cycle（quarterly_state 可用、event_scan 30 日內無事件）、structural.global_leveraged_approvals。其中最可能影響答案的是 valuation.ai_credit_schism：如果 AI 發行人 CDS 或債券利差已經開始走闊，R3 的距離會比本次判斷更近。不過整體 HY/IG OAS 處於低檔，不太可能存在被遺漏的大幅重定價。monetary.private_credit_liquidity 沒有披露，代表沒有 gate proration / breach 或 net inflow→outflow flip 的當期訊號；這個缺口不太可能改變答案。

R2 的逐家指引缺口：本次證據只有 top-4 合計 capex，沒有 Microsoft／Alphabet／Amazon／Meta 個別的最新指引數字與方向比較。合計值大幅上行，代表兩家同時下修的可能性很低，所以這個缺口不改變答案，但下次應補齊逐家資料。

最大的不確定性：
1. Q3 財報季（窗口內）的 capex 指引：若兩家以上轉向下修，會直接觸發 R2，答案推向 yes。
2. Anthropic 10 月 IPO：定價或上市後表現不佳，可能成為 AI 股權重定價的起點，推向 R1；順利上市則強化 no。
3. AI 算力借款人的再融資條件：CoreWeave 等借款人負債持續增加，若信用利差急速走闊，R3 與 R1 會互相強化；目前證據指向融資管道暢通。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7675.7 | FRED API (series_id=SP500) sp500_trend | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 7.97 | FRED API (series_id=SP500) sp500_trend | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 9.4 | FRED API (series_id=SP500) sp500_trend | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29224.52 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-06-02 | 2026-08-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.68 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1，家庭股票配置 %） | 45.7608 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-27T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.7 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.81 | FRED API (series_id=BAMLC0A0CM) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.64 | FRED API (series_id=DGS10) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（vs 2026-08-24） | -6.0 | FRED API (series_id=DGS10) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.32 | FRED API (series_id=DFII10) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps（vs 2026-08-24） | -6.0 | FRED API (series_id=DFII10) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.32 | FRED API (series_id=T10YIE) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps（vs 2026-08-24） | 0.0 | FRED API (series_id=T10YIE) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl） | 83.9 | FRED API (series_id=DCOILWTICO) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料，%） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-27T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.33 | FRED API (series_id=T5YIFR) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright 10Y 期限溢價，%） | 0.8682 | FRED API (series_id=THREEFYTP10) | 2026-08-21 | 2026-08-27T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（序列自身 trailing 7 日） | 2.9 | FRED API (series_id=THREEFYTP10) | 2026-08-21 | 2026-08-27T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.66 | FRED API (series_id=SOFR) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.74 | FRED API (series_id=SOFR99) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-27 | 2026-08-27T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.003 | FRED API (series_id=RPONTTLD) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,745,699（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-19 | 2026-08-27T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,913,041（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-21 | 2026-08-27T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,442,957（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-27T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.45 | FRED API (series_id=VIXCLS) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of；comove=false） | 15.45 | FRED API 衍生 vix_spx_comove 區塊 | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日，base 2026-08-18） | -2.46 | FRED API 衍生 vix_spx_comove 區塊 | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日，base 2026-08-18） | -0.19 | FRED API 衍生 vix_spx_comove 區塊 | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2026.1422（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-12 | 2026-08-27T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六個 CBT 美債期貨槓桿基金淨部位，口） | -7,218,048 | CFTC TFF futures-only cftc_lev_funds | 2026-08-18 | 2026-08-27T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 244,468 | CFTC TFF futures-only cftc_lev_funds | 2026-08-18 | 2026-08-27T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 69.44 | Yahoo chart API (^MOVE) move_index | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2368.0 | OFR STFM ofr_repo | 2026-08-26 | 2026-08-27T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值 / S&P 500 P/E and Shiller CAPE | multpl / GuruFocus WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值 / Mag 7 weighted P/E and AI leader P/S | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值 / Analyst TP upgrade decomposition | 賣方摘要 WebSearch（90d＋同季） | ✗ NOT DISCLOSED（檢索完成，無同季合格 TP 上修） |
| valuation.sp500_trend | 估值 / S&P 500 price-trend deviation | fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值 / NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值 / AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✗ NOT DISCLOSED（檢索完成，14 日內無合格披露） |
| breadth.rsp_spy | 廣度 / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度 / Top-10 concentration in S&P 500 | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度 / Advance/decline ratio, new high/low ratio | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶 / CNN Fear & Greed Index | CNN WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶 / Margin Debt: FINRA monthly data | FINRA / GuruFocus WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶 / Retail survey: AAII Investor Sentiment | AAII WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶 / Social sentiment proxies | WSB / X WebSearch（7d） | ✗ NOT DISCLOSED（檢索完成，無顯著討論） |
| retail.household_equity_allocation | 散戶 / Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶 / NAAIM Exposure Index | naaim.org WebSearch [primary: SEARCH] | ✗ NOT DISCLOSED（檢索完成，無當週值） |
| institutional.bofa_jpm_survey | 機構 / BofA Fund Manager Survey and JPM institutional survey | BofA / JPM WebSearch | ✗ NOT DISCLOSED（檢索完成，無新調查） |
| monetary.fed_funds | 貨幣與信用 / Fed funds rate: FRED | fetch_macro.py（DFEDTARU ok；DFEDTARL ok） | ✓ API |
| monetary.hy_oas | 貨幣與信用 / High Yield OAS | fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣與信用 / Investment Grade OAS | fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣與信用 / 10Y Treasury yield | fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣與信用 / 10Y Treasury real yield / TIPS | fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣與信用 / 10Y breakeven inflation rate | fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣與信用 / WTI crude oil price | fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣與信用 / CPI YoY: FRED | fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣與信用 / 5y5y forward inflation expectation | fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣與信用 / 10Y 期限溢價（term premium）: FRED | fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣與信用 / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok；repo_stress ok） | ✓ API |
| monetary.treasury_auctions | 貨幣與信用 / 美債標售需求（auction tail / bid-to-cover） | Reuters / TreasuryDirect WebSearch（14d） | ✗ NOT DISCLOSED（檢索完成，14 日內無顯著標售結果） |
| monetary.fedwatch | 貨幣與信用 / Fed funds rate path expectations | CME FedWatch 摘要 WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣與信用 / Fed balance sheet: FRED | fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣與信用 / Global central bank liquidity cross-check | fetch_macro.py（ECBASSETSW ok；JPNASSETS ok） | ✓ API |
| monetary.pboc | 貨幣與信用 / PBoC aggregate financing | PBoC / NBS WebSearch | ✗ NOT DISCLOSED（檢索完成，無英文摘要） |
| monetary.private_credit_liquidity | 貨幣與信用 / Private-credit / non-bank fund liquidity stress | BDC 披露 WebSearch（30d） | ✗ NOT DISCLOSED（檢索完成，30 日內無合格披露） |
| ai.hyperscaler_capex | AI 基本面 / Hyperscaler capex guidance | 財報摘要 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI 基本面 / AI token volume growth rate | 供應商披露 WebSearch | ✓ SEARCH-VERIFIED |
| ai.openai_anthropic_revenue | AI 基本面 / OpenAI / Anthropic annualized revenue | CNBC / Bloomberg WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI 基本面 / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 WebSearch | ✗ NOT DISCLOSED（檢索完成，無合格披露） |
| ai.compute_supply_demand | AI 基本面 / AI compute supply/demand and overcapacity risk | 產業披露 WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI 基本面 / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch：quarterly_state（top-5 capex vs FCF、發債趨勢）＋ event_scan（30d 大額融資）；event_scan 檢索完成無事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI 基本面 / AI 營收對 capex 缺口（revenue-to-capex gap） | 綜合披露 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI 基本面 / GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K / 10-Q WebSearch（30d） | ✗ NOT DISCLOSED（檢索完成，30 日內無變動） |
| ai.capital_cycle | AI 基本面 / 資本週期階段（capital cycle stage） | WebSearch：quarterly_state（供需增速）＋ event_scan（30d 進出場事件）；event_scan 檢索完成無事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機 / Search for past 7 days: AI rename / SPAC | 新聞 / SEC EDGAR WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機 / IPO market heat | stockanalysis / Renaissance WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機 / Microcap thematic moonshots | Finviz / Benzinga / StockTwits WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機 / Upcoming AI IPOs | Bloomberg / CNBC / Yahoo WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機 / Insider selling at AI / market-leadership companies | SEC EDGAR / openinsider WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機 / Cboe equity-only put/call ratio | Cboe / 彙整站 WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構性槓桿 / US leveraged ETF AUM | ETF.com / 新聞 WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構性槓桿 / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com new launches WebSearch（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | 結構性槓桿 / Global leveraged product approvals | KRX / TWSE / JPX / ESMA WebSearch（7d） | ✗ NOT DISCLOSED（檢索完成，7 日內無英文披露） |
| structural.zero_dte | 結構性槓桿 / 0DTE option volume | Cboe insights WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構性槓桿 / Options total volume | OCC 統計 WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構性槓桿 / Cross-asset derivatives / correlation checks | Cboe / 彙整站 WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構性槓桿 / VIX / S&P 500 co-movement | fetch_macro.py（VIXCLS ok；vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | 結構性槓桿 / Cross-reference only: FINRA margin debt | FINRA / GuruFocus WebSearch（交叉檢核） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構性槓桿 / AI infrastructure debt financing / vendor-financing loops | 信用市場 / 公司公告 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構性槓桿 / Bank loans to nondepository financial institutions | fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構性槓桿 / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py（cftc_lev_funds ok；move_index ok；ofr_repo ok）＋ WebSearch 拆倉事件（無合格披露） | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E ≈26.2、Shiller CAPE ≈41.3（原定來源 multpl / GuruFocus） | Shiller CAPE S&P 500 P/E August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio （GuruFocus） | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| valuation.mag7_multiples | Magnificent 7 加權 P/E ≈29.5x（S&P 500 ≈25.6x） | Magnificent Seven weighted PE August 2026 | https://www.nasdaq.com/articles/the-magnificent-seven-market-performance-and-valuations （Nasdaq） | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| breadth.rsp_spy | RSP 領先 SPY，2026 年等權領先 ≈1.7pp（RSP AUM 破 $100B） | RSP equal weight vs SPY 2026 | https://www.cnbc.com/2026/08/23/stocks-market-investing-sp500-spx.html （CNBC） | 2026-08-23 | 2026-08-27T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 top-10 集中度 ≈36.46% | S&P 500 top 10 concentration 2026 | https://finance.yahoo.com/markets/stocks/articles/rsp-vs-spy-does-equal-185007075.html （Yahoo Finance） | 2026-08-23 | 2026-08-27T09:30:00+08:00 |
| breadth.advance_decline | 廣度確認多頭、新高 > 新低、等權領先 ≈1.7pp | market breadth advance decline August 2026 | https://ts2.tech/en/sp-500-equal-weight-leads-by-1-7-points-as-market-breadth-wobbles/ （TS2） | 2026-08-23 | 2026-08-27T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 55（Greed） | CNN Fear and Greed August 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-07 月資料）1,417,225（百萬美元）、YoY +38.6%、MoM −5.7% | FINRA margin debt July 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt （GuruFocus／FINRA） | 2026-07-31 | 2026-08-27T09:30:00+08:00 |
| retail.aaii | AAII 偏多 35.5%、偏空 39.9%（週結 2026-08-19） | AAII investor sentiment August 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-08-19 | 2026-08-27T09:30:00+08:00 |
| monetary.fedwatch | FedWatch：9/16 FOMC 按兵不動定價 ≈68.4% | CME FedWatch September 2026 hold | https://en.macromicro.me/series/1645/probability-fed-rate-decrease （MacroMicro，原定 CME FedWatch） | 2026-08-20 | 2026-08-27T09:30:00+08:00 |
| ai.hyperscaler_capex | top-4（MSFT/GOOGL/AMZN/META）2026 capex 合計 ≈$725bn，+77% YoY（Q2 財報後） | hyperscaler 2026 capex guidance | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-13 | 2026-08-27T09:30:00+08:00 |
| ai.token_growth | Anthropic run-rate 年增 ≈7× | Anthropic token growth 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html （CNBC） | 2026-08-17 | 2026-08-27T09:30:00+08:00 |
| ai.openai_anthropic_revenue | OpenAI ≈$40B、Anthropic ≈$65B run-rate | OpenAI Anthropic annualized revenue 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html （CNBC） | 2026-08-17 | 2026-08-27T09:30:00+08:00 |
| ai.compute_supply_demand | GPU 現貨租金 > 2× 合約價、產能被利用率吸收 | AI GPU rental pricing utilization 2026 | https://www.uncoveralpha.com/p/amazon-google-microsoft-meta-q2-earnings （UncoverAlpha） | 2026-08-13 | 2026-08-27T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex > FCF、2026 發債擴張（背景；event_scan 30 日內無事件） | hyperscaler external financing capex FCF debt 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow （FactSet） | 2026-08-17 | 2026-08-27T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 OpenAI 40＋Anthropic 65 ≈105 vs 年化 capex ≈725（$bn；分母：top-4） | AI revenue to capex gap 2026 | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-17 | 2026-08-27T09:30:00+08:00 |
| ai.capital_cycle | [quarterly_state] 供給側 capex 年增 ≈77%、需求側 token／營收成長並存（背景；event_scan 30 日內無事件） | AI capex growth supply demand 2026 | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-13 | 2026-08-27T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日窗掃描 0 件 | AI rename SPAC ticker change August 2026 | Renaissance Capital / SEC EDGAR / 新聞掃描 | — | 2026-08-27T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD 美股 IPO ≈235 件、無單週無營收 AI IPO 暴衝 | US IPO count August 2026 | https://stockanalysis.com/ipos/2026/ （StockAnalysis） | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot（≥100% 單日、<$1B、2+ 主題、弱基本面）掃描 0 檔 | microcap 100% single day quantum AI August 2026 | Finviz / Benzinga / StockTwits movers | — | 2026-08-27T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 10 月 IPO、估值 ≈$2T | Anthropic OpenAI IPO 2026 | https://finance.yahoo.com/markets/article/spacex-openai-and-anthropic-here-are-the-most-anticipated-ipos-in-2026-114439441.html （Yahoo Finance） | 2026-08-17 | 2026-08-27T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 14 日內合格 Form 4 集中賣出 0 起 | insider Form 4 AI executives August 2026 | SEC EDGAR / openinsider | — | 2026-08-27T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.52 | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/manuals/put-call-ratio （thetrading.tools，原定 Cboe） | 2026-08-19 | 2026-08-27T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美股槓桿 ETF 總 AUM ≈198（$bn）；TQQQ ≈37、SOXL ≈22 | leveraged ETF AUM record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing，原定 etf.com） | 2026-08-17 | 2026-08-27T09:30:00+08:00 |
| structural.us_single_stock_etf | 美單一個股槓桿 ETF 過去 30 日新核准／上市掃描 0 件 | single-stock leveraged ETF launch SEC August 2026 | SEC EDGAR / ETF.com new launches | — | 2026-08-27T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 8 月佔比創紀錄 ≈62.4% | 0DTE SPX volume share August 2026 | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august （Cboe） | 2026-08-14 | 2026-08-27T09:30:00+08:00 |
| structural.options_volume | OCC 2026 YTD 日均 > 71（M 口）（2026-07 月資料） | OCC options volume 2026 | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/historical-volume-statistics （OCC） | 2026-07-31 | 2026-08-27T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 15.45、期限結構 contango、SKEW 偏高 | VIX term structure SKEW August 2026 | https://www.thetrading.tools/vix-term-structure （thetrading.tools，原定 Cboe） | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt／市值交叉檢核（2026-07 月資料，YoY +38.6%） | FINRA margin debt equity market cap ratio 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt （GuruFocus／FINRA） | 2026-07-31 | 2026-08-27T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave：HPC 基建擔保 delayed-draw 定期貸款設施 $2.6B | AI data center debt financing CoreWeave August 2026 | https://investors.coreweave.com/news/news-details/2026/CoreWeave-Closes-2-6-Billion-Loan-Facility-Expanding-Financing-Flexibility-for-AI-Infrastructure/default.aspx （CoreWeave IR） | 2026-08-10 | 2026-08-27T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-27",
  "iso_week": "2026-W35",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-25",
  "prior_date": "2026-08-24",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 4.68,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

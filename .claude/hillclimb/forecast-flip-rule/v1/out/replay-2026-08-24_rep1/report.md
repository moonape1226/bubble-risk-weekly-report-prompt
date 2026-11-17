> [DRY RUN] this report was not committed to archive.

# 2026-08-24 AI 泡沫破裂預測報告
報告日期：2026-08-24｜ISO 週次：2026-W35｜預測窗口：2026-08-24 → 2027-02-22｜前次基準：report-2026-08-20（4天前）

## 結論

**結論：no**

三條路徑目前都沒有進行中的跡象：NASDAQ-100 距 52 週高點只回撤 4.41%，離 R1 門檻還要再跌約 21.54%；hyperscaler top-4 的 2026 capex 合計 ≈$725bn（+77% YoY），本次證據裡沒有任何一家下修。HY OAS 2.75% 處於緊縮水位，也沒有任何 AI 借款人的違約或重組訊號。估值雖然極端（CAPE ≈41.2），但只能說明脆弱度高，不足以推翻「182 天內不破裂」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,308.86（2026-08-21），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 4.41%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，最新收盤還要再跌約 21.54% 才會觸及。S&P 500 收在 7,674.37（2026-08-21），高於 200 日均線 8.15%、高於 52 週均線 9.61%（`valuation.sp500_trend`），價格延伸偏大，回檔空間不小。VIX 與 S&P 500 在 2026-08-13 → 2026-08-20 的 7 日窗內沒有同漲：VIX +9.43%、S&P 500 −2.02%，屬於正常的避險反向走勢，未出現 crowded-optionality 警戒（`structural.vix_spx_comove`）。估值方面，trailing P/E ≈26.2、Shiller CAPE ≈41.2（`valuation.sp500_pe_cape`），Mag 7 加權 P/E ≈29.5x（`valuation.mag7_multiples`）。

**判讀：** R1 離觸發還很遠（目前回撤 4.41%，門檻 25%）。要在窗口內成立，需要一個 R3 式信用衝擊、Fed 轉向升息，或 R2 指引急轉彎，引發 21% 以上的再跌幅；以目前的波動率（VIX 16.01、MOVE 73.4）來看，市場並未定價這種情境。

### R2 資本支出收縮

本次證據只有 top-4（Microsoft、Alphabet、Amazon、Meta）2026 capex 的合計數 ≈$725bn，較前一年 +77%（來源日期 2026-08-13，即 2026 年第二季財報後的彙總，`ai.hyperscaler_capex`）。四家各自的最新指引數字與日期不在本次檢索結果內，因此個別方向無法逐家標示（Microsoft／Alphabet／Amazon／Meta：未提供個別指引數字）；但合計年增 77% 而且本次證據裡沒有任何下修報導，所以已知下修家數為 0／4。下一輪（2026 年第三季）財報預計落在窗口內，但本次證據沒有列出確切日期。需求端支撐仍在：GPU 現貨租金高於合約價 2 倍以上、產能被利用率吸收（`ai.compute_supply_demand`，2026-08-13）。Anthropic 年化營收 ≈$65B、OpenAI ≈$40B（`ai.openai_anthropic_revenue`，2026-08-17）。

**判讀：** R2 目前沒有往觸發的方向走，四家都還在擴張。窗口內有兩輪財報可能改變指引（第三季、以及 2027 年初的第四季／年度指引），但需要兩家同時下修；以目前的利用率與營收成長來看，這需要先出現明顯的需求斷層，或 R1 回撤迫使管理層收手。

### R3 AI 信用事件

本次的 AI 信用定價分歧掃描與 AI infrastructure debt financing / vendor-financing loops 掃描都已完成，但 30 日／14 日窗內沒有合格的新披露。因此本次沒有任何 neocloud／AI 資料中心借款人的利差、CDS、評等動作或付款困難可以引用。大盤信用很緊：HY OAS 2.75%、IG OAS 0.82%（2026-08-20，`monetary.hy_oas`、`monetary.ig_oas`），repo 資金壓力（SOFR−IORB）為 −2bp，SOFR99−IORB 為 +6bp（`monetary.repo_stress_srf`），SRF 動用（Standing Repo Facility usage）為 0（2026-08-21）。hyperscaler 本身的季度狀態顯示 capex 已超過 FCF、開始轉向發債，但 30 日事件掃描無新案（細節見資料缺漏段）。

**判讀：** R3 沒有可見的進行中跡象：沒有違約、寬限期或 distressed exchange 的報導，整體信用利差處於緊縮水位。要在窗口內觸發，需要某家負債 ≥ $5bn 的 neocloud 出現再融資失敗或客戶合約崩解；本次掃描未見再融資牆或困境訊號，但缺少個別發行人的利差資料，是本路徑最大的盲點。

## 支持 yes 的證據

- [整體] 估值處於歷史極端區：S&P 500 Shiller CAPE ≈41.2、trailing P/E ≈26.2（2026-08-20，`valuation.sp500_pe_cape`），Mag 7 加權 P/E ≈29.5x（2026-08-14，`valuation.mag7_multiples`），一旦有觸發事件，下跌幅度會很大。
- [R1] 槓桿與投機部位擁擠：美股槓桿 ETF 總 AUM 創新高 ≈$198bn（TQQQ 31.3、SOXL 17.3，2026-08-17，`structural.leveraged_etf_aum`），SPX 0DTE 佔比在 8 月創紀錄 ≈62.4%（2026-08-14，`structural.zero_dte`），margin debt YoY ≈+38.6%（2026-07 月資料，`retail.margin_debt`），回檔時可能被強制去槓桿放大。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）仍大：年化 AI 終端營收 ≈$105bn（OpenAI 40＋Anthropic 65）vs 年化 capex ≈$725bn（分母：top-4，未含 Oracle），比例約 14.5%（2026-08-17，`ai.revenue_capex_gap`）；如果營收成長放緩，管理層有下修的壓力。
- [R1] 政策緩衝受限：CPI YoY 3.3%（2026-07 月資料，`monetary.cpi_yoy`），FedWatch 顯示 9/16 會議按兵不動 ≈68.4%、尾端情境是升息而非降息（2026-08-20，`monetary.fedwatch`），10Y 期限溢價（term premium）0.8393%、7 日 +1.4bp（2026-08-14，`monetary.term_premium`）。若 AI 股回撤，Fed 降息托底的空間有限。
- [整體] 價格延伸：S&P 500 高於 200 日均線 8.15%（2026-08-21，`valuation.sp500_trend`），均值回歸的空間不小。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.41%（2026-08-21），R1 門檻 22,995.45 需要再跌約 21.54%（`valuation.ndx_drawdown`），離觸發距離很遠。
- [R2] hyperscaler top-4 2026 capex 合計 ≈$725bn、+77% YoY（2026-08-13，`ai.hyperscaler_capex`），本次證據沒有任何一家下修；需求端 GPU 現貨租金高於合約價 2 倍以上、產能被利用率吸收（2026-08-13，`ai.compute_supply_demand`）。
- [R3] 信用市場完全沒有壓力：HY OAS 2.75%、IG OAS 0.82%（2026-08-20，`monetary.hy_oas`、`monetary.ig_oas`），repo 資金壓力（SOFR−IORB）−2bp、SRF 動用 0（`monetary.repo_stress_srf`），沒有 R3 式信用事件的傳導前兆。
- [R2] AI 終端需求仍在加速：Anthropic 年化營收 ≈$65B、OpenAI ≈$40B（2026-08-17，`ai.openai_anthropic_revenue`），Anthropic run-rate 年增 ≈7 倍（`ai.token_growth`），削弱了窗口內兩家 hyperscaler 同時下修的理由。
- [R1] 情緒並非狂熱：CNN Fear & Greed 55（Greed，2026-08-21，`retail.fear_greed`），AAII 偏多 35.5%、偏空 39.9%（2026-08-19，`retail.aaii`），廣度擴散、RSP 領先 SPY YTD ≈5pp（`breadth.rsp_spy`），這些更像健康的輪動，而不是頂部的集中追價。
- [整體] 美債市場平穩：MOVE 73.4（2026-08-21）、槓桿基金美債期貨淨空 −7,218,048 口、4 週淨空減少 244,468 口（2026-08-18，`structural.treasury_basis_trade`），30Y 標售無明顯 tail（2026-08-13，`monetary.treasury_auctions`），美債基差交易槓桿沒有平倉壓力。

## 與前期比較

前次結論：無前次預測（report-2026-08-20 為舊格式評分報告）

- 前次是舊格式評分報告，不轉換成 yes／no；本次 flip_evidence 為空。
- 自 2026-08-20 以來，宏觀序列大多持平：10Y 分解三腿 Δ 皆為 0（無變動；DGS10、DFII10 無新觀測，T10YIE 有新觀測），HY／IG OAS 持平；S&P 500 由 7,641.16 升至 7,674.37（+0.43%）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下為已完成檢索但窗內沒有合格披露（✗ NOT DISCLOSED）的來源，以及它們是否可能改變答案：
- valuation.ai_credit_schism、structural.ai_infrastructure_debt：R3 的核心掃描無新披露，使我們看不到個別 neocloud 的利差與再融資狀態。這是最可能隱藏 R3 風險的缺口；但整體 HY OAS 緊縮，若有大型困境通常會反映在指數利差，因此判斷不太可能翻轉答案。
- ai.hyperscaler_financing_mix、ai.capital_cycle：季度狀態可取得（capex > FCF、轉向發債；供給 capex 年增 ≈77% 與需求成長並存），但 30 日事件掃描無新案，所以兩者整體為 ✗ NOT DISCLOSED，不作正文證據引用。不改變答案。
- monetary.private_credit_liquidity、valuation.analyst_tp_decomposition、ai.depreciation_life、ai.customer_concentration_rpo、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.pboc、structural.global_leveraged_approvals：屬確認性指標，缺漏不改變答案。
- R2 的個別公司指引：本次證據只有 top-4 合計數，沒有各家的指引數字與方向，也沒有下一輪財報日期。若某家的實際指引已經持平甚至收斂，會稍微拉近 R2；但合計 +77% 顯示整體仍在擴張。

最大的不確定性：
1. 2026 年第三季與第四季財報的 capex 指引（窗口內）：若兩家以上轉為下修，會直接推向 yes。
2. Fed 路徑：CPI 3.3%、FedWatch 尾端是升息；若通膨再加速迫使升息，會提高 R1 的風險，推向 yes。
3. Anthropic 10 月 IPO（估值 ≈$2T，`speculation.upcoming_ai_ipos`）：若成功，會延續情緒、推向 no；若發行失敗或大幅折價，可能成為 R1 的觸發點，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7674.37 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 8.15 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 9.61 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29308.86 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.41 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1，家庭股票佔金融資產 %） | 45.76 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（下限 %） | 3.50 | FRED API (series_id=DFEDTARL) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.75 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.82 | FRED API (series_id=BAMLC0A0CM) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.69 | FRED API (series_id=DGS10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.35 | FRED API (series_id=DFII10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.34 | FRED API (series_id=T10YIE) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl） | 86.48 | FRED API (series_id=DCOILWTICO) | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料，%） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.34 | FRED API (series_id=T5YIFR) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 0.8393 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（序列自身 trailing 7 日） | 1.4 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.63 | FRED API (series_id=SOFR) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.71 | FRED API (series_id=SOFR99) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-24 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,745,699（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,927,307（€5.93T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,442,957（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.01 | FRED API (series_id=VIXCLS) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 16.01 | fetch_macro.py 衍生區塊（FRED VIX／SP500 共享時間軸） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日，%） | 9.43 | fetch_macro.py 衍生區塊（FRED VIX／SP500 共享時間軸） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日，%） | -2.02 | fetch_macro.py 衍生區塊（FRED VIX／SP500 共享時間軸） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2,026.1422（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-12 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六檔美債期貨合計，口） | -7,218,048 | CFTC TFF futures-only | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 244,468 | CFTC TFF futures-only | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.4 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2328.6 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值 / S&P 500 P/E and Shiller CAPE | multpl / GuruFocus [SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值 / Mag 7 weighted P/E and AI leader P/S | 市場資料 [SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值 / Analyst TP upgrade decomposition | 賣方摘要 [SEARCH]，90 日且同季 | ✗ NOT DISCLOSED（無同季合格 TP 上修） |
| valuation.sp500_trend | 估值 / S&P 500 price-trend deviation | fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值 / NASDAQ-100 drawdown from 52-week high | fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值 / AI 信用定價分歧（equity-vs-credit schism） | 信用市場 [SEARCH]，14 日 | ✗ NOT DISCLOSED（14 日窗內無合格披露） |
| breadth.rsp_spy | 廣度 / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 市場資料 [SEARCH] | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度 / Top-10 concentration in S&P 500 | 市場資料 [SEARCH] | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度 / Advance/decline ratio, new high/low ratio | 市場資料 [SEARCH] | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶 / CNN Fear & Greed Index | CNN [SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶 / Margin Debt: FINRA monthly data | FINRA / GuruFocus [SEARCH] | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶 / Retail survey: AAII Investor Sentiment | AAII [SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶 / Social sentiment proxies | WSB / X [SEARCH]，7 日 | ✗ NOT DISCLOSED（無顯著討論） |
| retail.household_equity_allocation | 散戶 / Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶 / NAAIM Exposure Index | naaim.org [SEARCH] | ✗ NOT DISCLOSED（無當週值） |
| institutional.bofa_jpm_survey | 機構 / BofA Fund Manager Survey and JPM institutional survey | BofA / JPM [SEARCH] | ✗ NOT DISCLOSED（無新一期調查） |
| monetary.fed_funds | 貨幣 / Fed funds rate: FRED series DFEDTARU and DFEDTARL | fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣 / High Yield OAS | fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣 / Investment Grade OAS | fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣 / 10Y Treasury yield | fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣 / 10Y Treasury real yield / TIPS | fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣 / 10Y breakeven inflation rate | fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣 / WTI crude oil price | fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣 / CPI YoY: FRED series CPIAUCSL | fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣 / 5y5y forward inflation expectation | fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣 / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | 貨幣 / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | fetch_macro.py | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣 / 美債標售需求（auction tail / bid-to-cover） | Reuters / TreasuryDirect [SEARCH]，14 日 | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣 / Fed funds rate path expectations | CME FedWatch [SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣 / Fed balance sheet: FRED series WALCL | fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣 / Global central bank liquidity cross-check — ECB / BOJ | fetch_macro.py | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣 / PBoC aggregate financing / liquidity operations | PBoC / NBS [SEARCH] | ✗ NOT DISCLOSED（無英文摘要） |
| monetary.private_credit_liquidity | 貨幣 / Private-credit / non-bank fund liquidity stress | BDC 披露 [SEARCH]，30 日 | ✗ NOT DISCLOSED（30 日窗內無合格披露） |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | 財報摘要 [SEARCH]，沿用 2026Q2 財報 | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI / AI token volume growth rate | 供應商披露 [SEARCH] | ✓ SEARCH-VERIFIED |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | Bloomberg / CNBC [SEARCH] | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話 [SEARCH] | ✗ NOT DISCLOSED（無合格披露） |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | 產業披露 [SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構（capex vs FCF / 發債） | 財報 / 發債 [SEARCH]；quarterly_state 沿用季度狀態，event_scan 30 日掃描無新案 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口（revenue-to-capex gap） | 綜合披露 [SEARCH] | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動 | 10-K / 10-Q [SEARCH]，30 日 | ✗ NOT DISCLOSED（30 日窗內無變動） |
| ai.capital_cycle | AI / 資本週期階段（capital cycle stage） | 產業披露 [SEARCH]；quarterly_state 沿用，event_scan 30 日掃描無新案 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機 / Search for past 7 days | 新聞 / SEC EDGAR [SEARCH]，7 日 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機 / IPO market heat | stockanalysis / Renaissance [SEARCH] | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機 / Microcap thematic moonshots | Finviz / Benzinga [SEARCH]，7 日 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機 / Upcoming AI IPOs | Bloomberg / CNBC / Yahoo [SEARCH]，30 日 | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機 / Insider selling at AI / market-leadership companies | SEC EDGAR / openinsider [SEARCH]，14 日 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機 / Cboe equity-only put/call ratio | Cboe [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構 / US leveraged ETF AUM | ETF.com [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構 / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com [SEARCH]，30 日 | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | 結構 / Global leveraged product approvals | KRX / TWSE / JPX / ESMA [SEARCH]，7 日 | ✗ NOT DISCLOSED（7 日窗內無英文披露） |
| structural.zero_dte | 結構 / 0DTE option volume | Cboe [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構 / Options total volume | OCC [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構 / Cross-asset derivatives / correlation checks | Cboe / SpotGamma [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構 / VIX / S&P 500 co-movement | fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構 / Cross-reference only: FINRA margin debt | FINRA / GuruFocus [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構 / AI infrastructure debt financing / vendor-financing loops | 信用市場 [SEARCH]，30 日 | ✗ NOT DISCLOSED（30 日窗內無新披露） |
| structural.nbfi_bank_loans | 結構 / Bank loans to nondepository financial institutions | fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構 / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）＋[SEARCH] | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok；WebSearch 無額外平倉事件） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | trailing P/E ≈26.2、Shiller CAPE ≈41.2（原定來源 multpl / GuruFocus） | Shiller CAPE S&P 500 P/E August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio （GuruFocus） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| valuation.mag7_multiples | Magnificent 7 加權 P/E ≈29.5x（S&P 500 ≈25.6x） | Magnificent 7 weighted P/E August 2026 | https://www.fool.com/investing/2026/08/14/the-best-magnificent-seven-stocks-to-buy-in-august/ （Motley Fool） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| breadth.rsp_spy | RSP 領先 SPY YTD ≈5pp | RSP vs SPY YTD 2026 breadth | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 top-10 集中度 ≈36.5% | S&P 500 top 10 concentration 2026 | https://www.ebc.com/forex/rsp-vs-spy （EBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.advance_decline | 領導由 top-100 向 bottom-400 擴散、廣度確認多頭 | market breadth advance decline August 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 55（Greed） | CNN Fear and Greed today August 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）≈1,417,225、YoY ≈+38.6%、MoM −5.7% | FINRA margin debt July 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt （GuruFocus，原定 FINRA） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |
| retail.aaii | AAII 偏多 35.5%、偏空 39.9%（週結 2026-08-19） | AAII investor sentiment August 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 標售無明顯 tail、12.10% allotted at high | US Treasury 30-year auction August 2026 | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2026/R_20260813_3.pdf （TreasuryDirect） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| monetary.fedwatch | 9/16 會議按兵不動 ≈68.4%、尾端為升息（原定 CME FedWatch） | CME FedWatch September 2026 hold probability | https://en.macromicro.me/series/1645/probability-fed-rate-decrease （MacroMicro） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_capex | top-4 2026 capex 合計 ≈725（$bn，+77% YoY），沿用 2026Q2 財報 | hyperscaler 2026 capex guidance Microsoft Google Amazon Meta | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.token_growth | Anthropic run-rate 年增 ≈7 倍、API 佔營收多數 | Anthropic token growth revenue 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html （CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.openai_anthropic_revenue | OpenAI ≈$40B、Anthropic ≈$65B run-rate | OpenAI Anthropic annualized revenue August 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html （CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.compute_supply_demand | GPU 現貨租金 > 2 倍合約價、產能被利用率吸收 | AI GPU rental pricing utilization August 2026 | https://www.uncoveralpha.com/p/amazon-google-microsoft-meta-q2-earnings （UncoverAlpha） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex > FCF、2026 hyperscaler 發債擴張 | hyperscaler external financing capex FCF debt 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow （FactSet） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.revenue_capex_gap | OpenAI 40＋Anthropic 65 → ≈105 vs 年化 capex ≈725（$bn；分母 top-4） | AI revenue to capex gap 2026 | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.capital_cycle | [quarterly_state] 供給側 capex 年增 ≈77%、需求側 token／營收成長並存 | AI capex growth rate supply demand 2026 | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 掃描 0 件（7 日窗） | AI rename SPAC ticker change August 2026 | Renaissance Capital / SEC EDGAR / 新聞掃描（無合格事件） | — | 2026-08-24T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD IPO ≈232 件（截至 2026-08-21）、無單週無營收 AI IPO 暴衝 | US IPO count August 2026 | https://stockanalysis.com/ipos/2026/ （StockAnalysis） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描 0 檔（≥100% 單日、<$1B、2 個以上主題、弱基本面） | microcap 100% single day surge quantum AI August 2026 | Finviz / Benzinga / StockTwits movers 掃描（無合格 ticker） | — | 2026-08-24T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 10 月 IPO、估值 ≈$2T | Anthropic OpenAI IPO 2026 | https://finance.yahoo.com/markets/article/spacex-openai-and-anthropic-here-are-the-most-anticipated-ipos-in-2026-114439441.html （Yahoo Finance） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 14 日內合格 Form 4 集中賣出 0 起 | insider Form 4 AI executives August 2026 | SEC EDGAR / openinsider 掃描（14 日窗內無合格 cluster） | — | 2026-08-24T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.52（daily；9 日均總量 0.85） | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio （thetrading.tools，原定 Cboe） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美股槓桿 ETF 總 AUM ≈198（$bn）創新高；TQQQ 31.3、SOXL 17.3 | leveraged ETF AUM record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing，原定 ETF.com） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| structural.us_single_stock_etf | 單一個股槓桿 ETF 30 日新核准／上市 0 件 | single-stock leveraged ETF launch SEC August 2026 | SEC EDGAR / ETF.com new launches 掃描（30 日窗內無合格核准） | — | 2026-08-24T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 8 月佔比創紀錄 ≈62.4% | 0DTE SPX volume share August 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august （Cboe） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| structural.options_volume | OCC YTD 日均 > 71（百萬口）、量能高檔 | OCC options volume 2026 | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/historical-volume-statistics （OCC） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 16.01、期限結構 contango（IVTS ≈0.82）、SKEW 偏高 | VIX term structure SKEW August 2026 | https://www.thetrading.tools/vix-term-structure （thetrading.tools，原定 Cboe） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-07 月資料）／市值交叉檢核，YoY +38.6%（僅確認，不重複計入） | FINRA margin debt equity market cap ratio 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt （GuruFocus） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-24",
  "iso_week": "2026-W35",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-22",
  "prior_date": "2026-08-20",
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 4.41,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

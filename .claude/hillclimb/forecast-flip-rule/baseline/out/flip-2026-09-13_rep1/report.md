> [DRY RUN] this report was not committed to archive.

# 2026-09-13 AI 泡沫破裂預測報告

報告日期：2026-09-13｜ISO 週次：2026-W37｜預測窗口：2026-09-13 → 2027-03-14｜前次基準：report-2026-09-03（10天前）

## 結論

**結論：yes**

維持前次 yes：R1 是主導路徑——9/16 FOMC 升息定價約 85.5%（`monetary.fedwatch`，2026-09-12），配合 CPI YoY 3.35% 與 WTI $97.26，貨幣緊縮催化劑正落在 Shiller CAPE 約 40.73、前十大權重約 38% 的高度集中市場上（`valuation.sp500_pe_cape`、`breadth.top10_concentration`）。前次以來的新資料（10Y +18bp、實質利率 +13bp、VIX 七日 +24.58%）方向偏向緊縮與避險升溫，沒有任何 2026-09-03 之後的來源削弱 yes 的路徑分析，依翻轉紀律維持原答案。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,368.44（2026-09-11），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 4.21%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，自最新收盤再下跌約 21.70% 才會觸發。前次（2026-09-03）回撤 4.95%，本次略為收斂。

背景條件：S&P 500 收 7,656.98（2026-09-11），高於 200 日均線 6.9%、高於 52 週均線 8.33%，較前次 7,747.71 下跌 1.17%（`valuation.sp500_trend`）。估值偏高：Shiller CAPE 約 40.73（`valuation.sp500_pe_cape`），前十大成分股權重約 38%（`breadth.top10_concentration`），成分股站上 200 日均線比例約 53%（`breadth.advance_decline`），代表指數漲幅集中於少數權值股。催化劑：CME FedWatch 9/16 FOMC 升息 25bp 定價約 85.5%（`monetary.fedwatch`，2026-09-12），目前聯邦基金目標區間 3.50%–3.75%（`monetary.fed_funds`）；CPI YoY 3.35%（2026-08 資料，`monetary.cpi_yoy`）、WTI $97.26（`monetary.wti`）使 Fed 緩衝 AI 主導回撤的空間受限。10Y 殖利率 4.95%（+18bp）、10Y 實質利率 2.55%（+13bp）、10Y breakeven 2.36%（+1bp）（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）；本週 Δ 判讀：不可判（視窗不一致）——T10YIE 最新觀測日（2026-09-11）與 DGS10／DFII10（2026-09-10）不同，三腿不構成同窗恆等式。VIX 17.84，七日 +24.58% 而 S&P 500 同窗 −2.01%，未觸發同漲警戒（`structural.vix_spx_comove`）。

**判讀：** R1 距門檻仍有約 21.70% 的跌幅空間，尚未啟動；要在窗口內成立，需要升息週期重啟（9/16 FOMC 若升息並暗示續升）推動實質利率續升、壓縮高集中度權值股的估值，並經由槓桿與選擇權部位放大下跌。窗口長達 182 天且涵蓋至少一輪完整季報與多次 FOMC，是本次維持 yes 的主導路徑。

### R2 資本支出收縮

本次證據僅取得四大 hyperscaler（Microsoft、Alphabet、Amazon、Meta）2026 年 capex 指引合計約 $725bn（CNBC，2026-07-28，`ai.hyperscaler_capex`），屬 2026-07 財報季的沿用值（stock-of-state）。逐家最新指引金額與相對前次指引方向（上修／持平／下修）在本次取得的證據中未逐家列出；本次證據中四家皆無任何資本支出下修的披露，已下修家數：0 家。同一報導指出市場在 Alphabet 財報後對 capex 審視升高。下一次財報日期本次證據未列出；依季報節奏，窗口內至少涵蓋一輪（2026 年第三季）財報與次年度指引季。

需求面：Anthropic 年化 run-rate 約 $65bn（2026-08-17，`ai.openai_anthropic_revenue`）；AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 $105bn vs 年化 capex 約 $725bn（分母：top-4，Oracle 本次未取得可組合值），缺口仍大（`ai.revenue_capex_gap`）。供給面 H100 中位租金約 $3.38／小時（2026-08-31，`ai.compute_supply_demand`），本次未取得利用率或庫存證據，無法判定缺口是否已現。

**判讀：** R2 目前離成立最遠——尚無任何一家下修。要在窗口內成立，需要兩家在下一輪財報或次年度指引中下修，通常由 R1 回撤或融資成本上升引發；營收對 capex 的大缺口提供動機，但目前沒有一家公司發出收縮訊號。

### R3 AI 信用事件

本次 30 日掃描取得的 AI infrastructure debt financing / vendor-financing loops 事件為 Qualcomm 給予 Amazon 約 $4bn 認股權證的資料中心基礎設施交易（CNBC，2026-09-08，`structural.ai_infrastructure_debt`），屬供應商對客戶的 vendor-financing 型安排，不是困境訊號。AI 發行人個別債券利差／CDS 在本次 14 日窗口內未取得合格報導，因此無法逐一列出符合 R3 規模門檻（負債 ≥ $5bn、以 AI 資料中心／算力為主業）的借款人目前的信用定價或近期到期牆。整體信用市場平靜：HY OAS 2.70%（+5bp）、IG OAS 0.80%（−1bp）（`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 −3bp、SOFR99−IORB 為 +5bp、SRF 動用（Standing Repo Facility usage）0（`monetary.repo_stress_srf`）；銀行對 NBFI 放款 $2.03T 持平（`structural.nbfi_bank_loans`）。本次未見任何付款違約、covenant waiver、distressed exchange 或 going-concern 的披露。

**判讀：** R3 尚無事件，信用利差處於低檔；要在窗口內成立，需要 R1 回撤或利率上行使 neocloud 再融資窗口關閉，進而出現違約或 distressed exchange。這條路徑主要作為 R1 的放大器，而非獨立的觸發點。

## 支持 yes 的證據

- [R1] 9/16 FOMC 升息 25bp 定價約 85.5%（2026-09-12，`monetary.fedwatch`），而現行目標區間 3.50%–3.75%（`monetary.fed_funds`），CPI YoY 3.35%（2026-08，`monetary.cpi_yoy`）、WTI $97.26（2026-09-09，+5.09%，`monetary.wti`）——政策轉向緊縮是窗口內最直接的 R1 催化劑。
- [R1] 估值與集中度偏高：Shiller CAPE 約 40.73（2026-09-01，`valuation.sp500_pe_cape`）、前十大權重約 38%（2026-09-01，`breadth.top10_concentration`）、S&P 500 高於 200 日均線 6.9%（2026-09-11，`valuation.sp500_trend`），下跌時的潛在幅度大。
- [整體] 利率與波動率同步上行：10Y 4.95%（+18bp，`monetary.dgs10`）、10Y 實質利率 2.55%（+13bp，`monetary.dfii10`）、MOVE 82.21（+7.53，2026-09-11，`structural.treasury_basis_trade`）、VIX 17.84（七日 +24.58%，`structural.vix_spx_comove`），call skew 處於第 91 百分位（2026-09-10，`structural.cross_asset_derivatives`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）仍大：年化 AI 終端營收約 $105bn vs top-4 capex 約 $725bn（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`），一旦市場轉向要求回報，capex 下修的壓力會上升。
- [R1] 投機性部位仍高：SPX 0DTE 佔比創紀錄約 62%（2026-08，`structural.zero_dte`）、OCC 8 月總結算量約 14.4 億口（`structural.options_volume`）、margin debt 約 $1.42T（2026-07，`retail.margin_debt`），本週 IPO 定價約 22 檔（2026-09-11，`speculation.ipo_heat`）。
- [R3] vendor-financing loops 仍在擴張：Qualcomm 對 Amazon 約 $4bn 認股權證（2026-09-08，`structural.ai_infrastructure_debt`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤僅 4.21%（2026-09-11），需再跌約 21.70% 才會觸及門檻 22,995.45（`valuation.ndx_drawdown`），且較前次的 4.95% 收斂。
- [R2] 四大 hyperscaler 2026 capex 指引合計約 $725bn（2026-07-28，`ai.hyperscaler_capex`），本次證據中四家皆無下修，R2 需要兩家下修，目前為 0 家。
- [R3] 信用市場平靜：HY OAS 2.70%、IG OAS 0.80%（2026-09-10，`monetary.hy_oas`、`monetary.ig_oas`）；SOFR−IORB −3bp、SRF 動用 0（`monetary.repo_stress_srf`）；槓桿基金美債期貨淨空單四週縮減 387,809 口（2026-09-08，`structural.treasury_basis_trade`），未見平倉壓力。
- [整體] 情緒並非亢奮：CNN Fear & Greed 約 35（恐懼，2026-09-10，`retail.fear_greed`）、AAII 看多約 38.0%（2026-09-10，`retail.aaii`）；單一個股槓桿 ETF 資金流出約 $751m、規模約 $40.74bn（2026-09-08，`structural.leveraged_etf_aum`）；Mag 7 前瞻本益比低於 24（2026-08-03，`valuation.mag7_multiples`），部分去槓桿與估值壓縮已經發生。
- [整體] 基準率：任意 182 天內 NASDAQ-100 回撤 25%、兩家 hyperscaler 同時下修 capex、或大型 AI 基礎設施違約，都屬少見事件；本次三條路徑皆尚未啟動（`valuation.ndx_drawdown`）。

## 與前期比較

前次結論：yes（report-2026-09-03）

本次結論：維持

- NASDAQ-100 回撤由 4.95% 收斂至 4.21%（2026-09-11，`valuation.ndx_drawdown`）：距 R1 門檻的空間只微幅變動（不到 1 個百分點），屬雜訊等級，不改變 R1 的路徑分析。
- 9/16 FOMC 升息定價約 85.5%（2026-09-12，`monetary.fedwatch`）：這是前次以來最重要的新資料，方向強化而非削弱 R1 的緊縮催化劑。
- 10Y 殖利率 +18bp、實質利率 +13bp、MOVE +7.53、VIX 七日 +24.58%（`monetary.dgs10`、`monetary.dfii10`、`structural.treasury_basis_trade`、`structural.vix_spx_comove`）：風險規避與利率壓力升溫，與 yes 的方向一致。
- Fear & Greed 降至約 35、單一個股槓桿 ETF 資金流出約 $751m（`retail.fear_greed`、`structural.leveraged_etf_aum`）：投機溫度降溫，屬偏 no 的資訊，但只代表情緒變化，並未讓任何路徑變得更難成立。
- R2／R3 無新事件：capex 指引仍為 2026-07 的沿用值（`ai.hyperscaler_capex`），信用利差無明顯變化（`monetary.hy_oas`）。沒有任何晚於 2026-09-03 的來源改變 R2／R3 的分析，因此不構成翻轉依據。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下為 ✗ NOT DISCLOSED 的來源（搜尋已完成、窗口內無合格披露）：valuation.analyst_tp_decomposition、valuation.ai_credit_schism、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.private_credit_liquidity、ai.token_growth、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（event_scan 無 30 日事件）、ai.depreciation_life、ai.capital_cycle（兩個組件皆無披露）、speculation.upcoming_ai_ipos、structural.global_leveraged_approvals。其中 AI 信用定價分歧與私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）缺漏對 R3 判讀影響最大：若有 AI 發行人利差走闊或 gate proration / breach 未被捕捉，R3 的距離可能比本次估計更近，會強化 yes；缺漏本身不足以翻轉答案。

資料一致性備註：evidence 記錄中美債基差交易槓桿一列寫「script 三區塊 fetch_failed」，但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 三塊皆為 `status: ok`；本報告以 artifact 為準，並標記為 ✓ API。speculation.insider_form4 唯一的命中（Nvidia 董事出售約 $385m，2026-09-02）只附一個日期，無法區分 Form 4 申報日與交易日，未達具名揭露標準，因此不具名引用，記為 0 件合格。hyperscaler 逐家 capex 指引金額與方向本次未取得，R2 的「0 家下修」是依據證據中沒有任何下修披露。

主要不確定性：
- 9/16 FOMC：若如定價升息並暗示續升，會推升實質利率並壓縮估值，加強 yes；若按兵不動或措辭轉鴿，R1 的催化劑會弱化，偏向 no。
- 2026 年第三季 hyperscaler 財報與次年度 capex 指引：若有任一家下修，R2 啟動，偏向 yes；若全面上修，則 R2 遠離，且 AI 營收對 capex 缺口的敘事會被延後檢驗，偏向 no。
- AI 基礎設施借款人的再融資條件：本次未取得 AI 信用利差資料，若下次掃描出現 neocloud 利差走闊或 distressed exchange 傳聞，R3 會從背景變成主動路徑，偏向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest | 7656.98 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 6.9 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29368.44 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.21 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q2，%） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（%） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（%） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.7 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.8 | FRED API (series_id=BAMLC0A0CM) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.95 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.55 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.36 | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl） | 97.26 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-08 月資料） | 3.35 | FRED API (series_id=CPIAUCSL) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.32 | FRED API (series_id=T5YIFR) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（%，Kim-Wright） | 0.8892 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API (series_id=SOFR99) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-09-13 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6740619.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5912178.0（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6446620.0（¥644.66T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 17.84 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（窗口 2026-09-03 → 2026-09-10） | 17.84 | FRED API (series_id=VIXCLS, SP500) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 24.58 | FRED API (series_id=VIXCLS, SP500) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2027.9777（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約合計，口） | -6863118 | CFTC TFF futures-only | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 82.21 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2271.6 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（multpl / GuruFocus） | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✗ NOT DISCLOSED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch（% above 200-day 作 breadth proxy） | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（月頻沿用） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py BOGZ1FL153064486Q | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py DFEDTARU＋DFEDTARL | ✓ API DFEDTARU ok; DFEDTARL ok |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py BAMLH0A0HYM2 | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py BAMLC0A0CM | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py DGS10 | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | scripts/fetch_macro.py DFII10 | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py T10YIE（FRED 直接取得） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py DCOILWTICO | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | scripts/fetch_macro.py CPIAUCSL yoy_pct | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py T5YIFR | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py THREEFYTP10 | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py SOFR＋SOFR99＋IORB＋RPONTTLD | ✓ API SOFR ok; SOFR99 ok; IORB ok; RPONTTLD ok |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py WALCL | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py ECBASSETSW＋JPNASSETS | ✓ API ECBASSETSW ok; JPNASSETS ok（no_new_obs） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（季頻沿用） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch：quarterly_state 沿用最新季度；event_scan 30d 掃描無事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch＋既有 bullets 組合（分母 top-4） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch：quarterly_state 與 event_scan 30d 皆無合格披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（7d movers） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✗ NOT DISCLOSED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR＋WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py VIXCLS＋vix_spx_comove | ✓ API VIXCLS ok; vix_spx_comove ok |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py LNFACBW027SBOG | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds＋move_index＋ofr_repo | ✓ API cftc_lev_funds ok; move_index ok; ofr_repo ok |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.73（預定來源 multpl / GuruFocus） | S&P 500 Shiller CAPE ratio current September 2026 multpl | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | Magnificent 7 forward P/E valuation September 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html（CNBC） | 2026-08-03 | 2026-09-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 至 7 月止 YTD 報酬約 13% | RSP equal weight vs SPY S&P 500 YTD performance September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度約 38% | S&P 500 top 10 concentration percentage September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 200 日均線之上約 53% | market breadth advance decline new highs lows September 2026 percent stocks above 200-day | https://condoredge.com/stocks/market-breadth（Condor Edge） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 35（恐懼） | CNN Fear and Greed Index today September 2026 reading | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）約 $1.42T | FINRA margin debt August 2026 record year over year | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026（Advisor Perspectives，原始 FINRA） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.0% | AAII sentiment survey results week September 10 2026 bullish bearish neutral | https://www.aaii.com/sentimentsurvey（AAII） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.71 | Treasury auction results September 2026 tail bid-to-cover 10-year | https://thevaultreport.com/treasury-auctions（The Vault Report） | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.fedwatch | 9/16 FOMC 升息 25bp 定價約 85.5%（預定來源 CME FedWatch） | CME FedWatch September 12 2026 probability 25 basis point hike | https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html（Yahoo Finance） | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.pboc | 2026 年 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate financing 2026 total social financing | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm（SteelOrbis） | 2026-08-15 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 指引合計約 $725bn（2026-07 財報季沿用） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 $65bn | OpenAI Anthropic annualized revenue run rate September 2026 | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| ai.compute_supply_demand | H100 中位租金約 $3.38／小時 | GPU rental price HBM DRAM contract price September 2026 utilization | https://www.thundercompute.com/blog/ai-gpu-rental-market-trends（Thunder Compute） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 增額債務佔 capex 約 32%（2026-07 財報季沿用；event_scan 30 日無事件，故整列不作正文證據） | hyperscaler capex vs free cash flow debt issuance 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $105bn（分母沿用 ai.hyperscaler_capex top-4 約 $725bn） | AI revenue vs capex gap 2026 annualized run rate | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement September 7-13 2026 | 檢查來源：SPACInsider、Businesswire SPAC newsroom、Boardroom Alpha（窗內無合格事件） | — | 2026-09-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 22 檔 | IPO priced week September 8 2026 first day return debut | https://www.iposcoop.com/current-year-pricings/（IPOScoop） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描（0 件符合兩個以上主題且基本面弱；Tenon +77%、AEON +35% 皆未達門檻） | biggest stock gainers week September 7 2026 microcap 100% quantum AI | 檢查來源：Finviz、Benzinga、StockTitan、Yahoo movers | — | 2026-09-13T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 14 日掃描（0 件合格：唯一命中僅附單一日期，缺可區分的申報日與交易日，不具名引用） | insider selling Form 4 September 2026 Nvidia AI executives SEC filing | 檢查來源：SEC EDGAR Form 4 全文檢索、財經新聞摘要 | — | 2026-09-13T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 約 0.67（日值或 5 日均值來源未標明） | Cboe equity put call ratio September 2026 reading | https://www.thetrading.tools/put-call-ratio（The Trading Tools） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 $40.74bn，資金流出約 $751m | leveraged ETF assets under management September 2026 record single stock | https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/（ETF Action） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval September 2026 | 檢查來源：SEC EDGAR、ETF.com 新上市 feed（窗內無合格核准或上市） | — | 2026-09-13T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比創紀錄約 62%（2026-08 月資料） | 0DTE options share SPX volume September 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.options_volume | OCC 8 月總結算量約 14.4 億口（2026-08 月資料） | OCC options volume August 2026 monthly report | https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/（Traders Magazine） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 收在 17 以上、call skew 第 91 百分位 | fear gauge VIX hedges September 10 2026 volatility | https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html（CNBC） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率的基數約 $1.42T（2026-07 月資料） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php（Current Market Valuation） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Qualcomm 給予 Amazon 約 $4bn 認股權證（資料中心基礎設施交易，vendor-financing 型安排） | Qualcomm warrants Amazon 4 billion AI infrastructure deal September 2026 | https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html（CNBC） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-09-13",
  "iso_week": "2026-W37",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "yes",
  "horizon_end": "2027-03-14",
  "prior_date": "2026-09-03",
  "prior_answer": "yes",
  "flip_evidence": [],
  "r1_drawdown_pct": 4.21,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

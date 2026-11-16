> [DRY RUN] this report was not committed to archive.
# 2026-08-24 AI 泡沫破裂預測報告
報告日期：2026-08-24｜ISO 週次：2026-W35｜預測窗口：2026-08-24 → 2027-02-22｜前次基準：report-2026-08-20（4天前）

## 結論

**結論：no**

三條路徑都沒有進行中的觸發：NASDAQ-100 距 52 週高點回撤僅 4.41%，距 R1 門檻還需再跌約 21.54%；hyperscaler top-4 的 2026 capex 合計約 $725bn（+77% YoY），本次檢索未見任何一家下修；HY OAS 2.75%、IG OAS 0.82% 仍處窄幅，沒有 AI 信用重定價的跡象。估值與投機槓桿偏高只顯示泡沫的脆弱度，182 天內沒有足以推翻基準率的催化與傳導證據。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,308.86（2026-08-21），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 4.41%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，自最新收盤須再下跌約 6,313 點、約 21.54% 才會觸及。背景：S&P 500 為 7,674.37（2026-08-21），高於 200 日均線 8.15%、高於 52 週均線 9.61%（`valuation.sp500_trend`），價格延伸仍在但非極端；VIX 16.01、VIX 與 S&P 500 在 2026-08-13 → 2026-08-20 窗口內為一升一降（VIX +9.43%、S&P 500 −2.02%），未出現同向上漲的擁擠選擇權讀數（`structural.vix_spx_comove`）。估值端 Shiller CAPE 約 41.2、trailing P/E 約 26.2（`valuation.sp500_pe_cape`），Mag 7 加權本益比約 29.5x（`valuation.mag7_multiples`），代表一旦破裂下檔空間大。

**判讀：** R1 距離解析仍遠（需再跌約 21.54%）；要在窗口內觸發，需要一個把高估值轉化為強制去槓桿的催化——例如 R2 capex 指引反轉、R3 信用事件，或槓桿 ETF／0DTE 部位的集中平倉——目前這些催化都未出現。

### R2 資本支出收縮

本次可得的 hyperscaler capex 證據是 top-4（Microsoft、Alphabet、Amazon、Meta）2026 年度 capex 合計約 $725bn、年增約 77%，資料日 2026-08-13（Q2 財報季後彙整，`ai.hyperscaler_capex`）。逐家數字與方向：

- Microsoft：本次檢索結果未逐家列出最新指引數字；方向相對前次指引在檢索結果中未見下修，無法逐家確認為上修或持平。
- Alphabet：同上，未取得逐家數字；未見下修。
- Amazon：同上，未取得逐家數字；未見下修。
- Meta：同上，未取得逐家數字；未見下修。

目前已下修家數：0（就本次檢索所見）。合計 +77% YoY 的軌跡與「至少兩家下修」方向相反。窗口內依季報節奏應涵蓋兩輪季報（約 10 月下旬的 Q3 與 1 月下旬至 2 月初的 Q4／次年度指引），具體日期本次檢索未取得；次年度（2027）capex 指引通常在 Q4 財報提出，是 R2 最主要的窗口內節點。需求側目前仍支撐 capex：Anthropic run-rate 約 $65B、OpenAI 約 $40B（`ai.openai_anthropic_revenue`），GPU 現貨租金高於合約價 2 倍以上、產能被利用率吸收（`ai.compute_supply_demand`）。

**判讀：** R2 距離解析遠；要在窗口內觸發，需要兩家在 Q3 或 Q4 財報同時下修當年度或 2027 年度指引，前提通常是需求端（AI 營收、GPU 利用率）先出現明顯轉弱或股價先大幅下跌迫使資本紀律，目前兩者都沒有證據。

### R3 AI 信用事件

本次 AI 信用定價分歧與 AI infrastructure debt financing / vendor-financing loops 兩項掃描都完成，但在 14 日／30 日窗口內沒有可引用的合格披露（詳見 `## 資料缺漏與不確定性`），因此無法以發行人層級的債券利差、CDS 或評等動作評估潛在 R3 借款人（大型 neocloud 與資料中心平台）。可用的總體信用讀數全部偏鬆：HY OAS 2.75%、IG OAS 0.82%（2026-08-20，`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 SOFR 3.63% 對 IORB 3.65%（皆為 2026-08-20 對齊觀測）約 −2bp，SOFR99 3.71% 僅高於 IORB 約 6bp，SRF 動用（Standing Repo Facility usage）為 0（2026-08-21，`monetary.repo_stress_srf`）；銀行對 NBFI 放款約 $2.03T、週變動持平（2026-08-12，`structural.nbfi_bank_loans`）。本次檢索未見任何 AI 資料中心／算力借款人的付款違約、寬限期、distressed exchange 或 going-concern 語言。

**判讀：** R3 沒有可觀察的進行中事件；要在窗口內觸發，需要一家負債 ≥ 50 億美元的 AI 算力借款人出現流動性斷裂，而在 HY OAS 2.75% 的環境下再融資管道仍暢通，最可能的觸發路徑是 R1 股權重挫導致 neocloud 再融資關閉，屬二階傳導。

## 支持 yes 的證據

- [整體] 估值處於歷史極端：Shiller CAPE 約 41.2、trailing P/E 約 26.2（2026-08-20），Mag 7 加權本益比約 29.5x（2026-08-14），一旦催化出現 R1 的下檔幅度會很大（`valuation.sp500_pe_cape`、`valuation.mag7_multiples`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）仍大：年化 AI 終端營收約 $105bn（OpenAI 40＋Anthropic 65）vs 年化 capex 約 $725bn（分母：top-4 hyperscaler），資料日 2026-08-17；若營收成長放緩，資本紀律壓力最先出現在 2027 年度指引（`ai.revenue_capex_gap`）。
- [R1] 散戶與結構性槓桿偏高：FINRA margin debt（2026-07 月資料）約 1,417,225、YoY 約 +38.6%，接近歷史頂部常見的 +40–50% 區間（`retail.margin_debt`）；美股槓桿 ETF 總 AUM 約 $198bn 創紀錄、TQQQ 31.3、SOXL 17.3（2026-08-17，`structural.leveraged_etf_aum`）；SPX 0DTE 8 月佔比約 62.4% 創紀錄（2026-08-14，`structural.zero_dte`）。這些部位會放大任何下跌的速度。
- [R1] 投機供給即將上升：Anthropic 目標 10 月 IPO、估值約 $2T（2026-08-17，`speculation.upcoming_ai_ipos`），窗口內的大型 AI IPO 可能吸走流動性並成為情緒高點的標記。
- [整體] 通膨與期限溢價限制 Fed 緩衝空間：CPI YoY 3.3%（2026-07，`monetary.cpi_yoy`）、5y5y 2.34%（`monetary.t5yifr`）、10Y 期限溢價（term premium）0.8393%、trailing 7 日 +1.4bp（2026-08-14，`monetary.term_premium`）；FedWatch 9/16 按兵不動約 68.4%、尾端為升息（2026-08-20，`monetary.fedwatch`），一旦 AI 股重挫，降息托底的空間有限。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤僅 4.41%（2026-08-21 收盤 29,308.86 vs 2026-06-02 高點 30,660.6），距 R1 門檻 22,995.45 仍需再跌約 21.54%（`valuation.ndx_drawdown`）。
- [R2] hyperscaler top-4 的 2026 capex 合計約 $725bn、年增約 77%（2026-08-13），本次檢索未見任何一家下修，與「兩家下修」方向相反（`ai.hyperscaler_capex`）。
- [R3] 信用市場沒有壓力：HY OAS 2.75%、IG OAS 0.82%（2026-08-20），處於窄幅區間（`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）約 −2bp、SRF 動用（Standing Repo Facility usage）為 0（`monetary.repo_stress_srf`）。
- [R2] 需求端仍在吸收供給：Anthropic run-rate 約 $65B、OpenAI 約 $40B（2026-08-17，`ai.openai_anthropic_revenue`），Anthropic run-rate 年增約 7 倍（`ai.token_growth`）；GPU 現貨租金高於合約價 2 倍以上、產能被利用率吸收（2026-08-13，`ai.compute_supply_demand`）。
- [整體] 情緒與廣度不在狂熱區：CNN Fear & Greed 55（2026-08-21，`retail.fear_greed`），AAII 偏多 35.5%、偏空 39.9%（週結 2026-08-19，`retail.aaii`）；RSP 領先 SPY YTD 約 5pp、領導向 bottom-400 擴散（2026-08-17，`breadth.rsp_spy`、`breadth.advance_decline`）；+AI 改名／SPAC 掃描 0 件（`speculation.ai_rename_spac`）、microcap moonshot 掃描 0 檔（`speculation.microcap_moonshots`）。
- [整體] 美債市場平穩：MOVE 73.4（2026-08-21），槓桿基金美債期貨淨空單 −7,218,048 口、4 週回補 244,468 口（2026-08-18，`structural.treasury_basis_trade`）；30Y 美債標售需求（auction tail / bid-to-cover）無明顯 tail（2026-08-13，`monetary.treasury_auctions`），沒有國債市場失序（Treasury market dysfunction）的前兆。

## 與前期比較

前次結論：無前次預測（report-2026-08-20 為舊格式評分報告）

前次基準為舊格式評分報告，不轉換為 yes/no，flip_evidence 為空。自 2026-08-20 以來的主要變化：S&P 500 自 7,641.16 升至 7,674.37（+0.43%），10Y 殖利率 4.69%、HY OAS 2.75%、IG OAS 0.82% 皆無新觀測（Δ = 0）；10Y 拆解為無變動（DGS10、DFII10 無新觀測，T10YIE 已更新但持平）；MOVE 自 73.18 升至 73.4；OFR tri-party repo transaction volume 自 $2,400.4bn 降至 $2,328.6bn（−2.99%）。這些變動都不足以改變三條路徑的判讀。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源完成掃描但無合格的當期披露（✗ NOT DISCLOSED）：valuation.analyst_tp_decomposition、valuation.ai_credit_schism、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.pboc、monetary.private_credit_liquidity、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（quarterly_state 可得、30 日 event_scan 無披露）、ai.depreciation_life、ai.capital_cycle（quarterly_state 可得、30 日 event_scan 無披露）、structural.global_leveraged_approvals、structural.ai_infrastructure_debt。其中 valuation.ai_credit_schism 與 structural.ai_infrastructure_debt 的缺漏對 R3 影響最大：本次無法以發行人層級的利差、CDS 或新融資條款評估大型 neocloud 的信用狀態，只能以 HY／IG OAS 代理；若存在未被檢索到的 AI 借款人重定價，可能低估 R3，但在總體信用全面偏鬆的情況下，單憑此缺漏不太可能把答案翻成 yes。monetary.private_credit_liquidity 無披露代表本次無法確認私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）的 redemption-request ratio 趨勢。

其他資料限制：R2 的 capex 證據只有 top-4 合計約 $725bn，未取得逐家指引數字與相對前次指引的方向，因此「0 家下修」是就本次檢索所見；margin debt 未取得 margin debt / 總市值比率；IPO heat 只取得 YTD 件數，未取得首日報酬與無營收發行人佔比。

最大不確定性：

1. 下一輪 hyperscaler 財報（約 10 月下旬 Q3、1 月下旬至 2 月初 Q4 與 2027 年度指引）：若兩家以上首度給出 2027 capex 下修或明確放緩，會直接把答案推向 yes。
2. 大型 neocloud 的再融資與 AI infrastructure debt financing / vendor-financing loops 的實際條款：本次沒有可用的發行人層級資料，若出現利差急速走闊或評等下調，會把 R3（並經 R1）推向 yes。
3. Anthropic 等大型 AI IPO（目標 10 月）與 Fed 政策路徑：IPO 供給集中加上 FedWatch 尾端的升息風險，可能成為估值回落的催化，偏向 yes；反之若 IPO 順利且需求數據持續強勁，偏向 no。

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
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（家庭股票配置 %，2026Q1） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 2.75 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（IG OAS %） | 0.82 | FRED API (series_id=BAMLC0A0CM) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（10Y 殖利率 %） | 4.69 | FRED API (series_id=DGS10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（10Y 實質殖利率 %） | 2.35 | FRED API (series_id=DFII10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（10Y breakeven %） | 2.34 | FRED API (series_id=T10YIE) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（WTI 美元／桶） | 86.48 | FRED API (series_id=DCOILWTICO) | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（CPI YoY %，2026-07 月資料） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（5y5y %） | 2.34 | FRED API (series_id=T5YIFR) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（10Y 期限溢價 %，Kim-Wright） | 0.8393 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.63 | FRED API (series_id=SOFR) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.71 | FRED API (series_id=SOFR99) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-24 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF／隔夜 repo 操作 transaction volume，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.walcl | WALCL latest（Fed 資產負債表） | 6745699.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（ECB 資產負債表） | 5927307.0（€5.93T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（BOJ 資產負債表） | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest（VIX） | 16.01 | FRED API (series_id=VIXCLS) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（窗口 2026-08-13 → 2026-08-20） | 16.01 | FRED API (series_id=VIXCLS, SP500) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（%） | 9.43 | FRED API (series_id=VIXCLS) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（%） | -2.02 | FRED API (series_id=SP500) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（銀行對 NBFI 放款，十億美元） | 2026.1422（$2.03T） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-12 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（槓桿基金美債期貨淨部位，口） | -7218048 | CFTC TFF futures-only | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（MOVE） | 73.4 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2328.6（$2.33T） | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl / GuruFocus [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | 賣方摘要 [primary: SEARCH]，90d＋同季 | ✗ NOT DISCLOSED（掃描完成，無同季合格上修） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | 信用市場 [primary: SEARCH]，14d | ✗ NOT DISCLOSED（掃描完成，14 日內無合格披露） |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | 市場資料 WebSearch | ✓ SEARCH-VERIFIED（質性廣度敘述，未取得 A/D 數值） |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | CNN [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | FINRA / GuruFocus WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED（市值比率未取得） |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | AAII [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WSB / X WebSearch，7d | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | naaim.org [primary: SEARCH] | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | BofA / JPM WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（repo_stress block） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | Reuters / TreasuryDirect [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | CME FedWatch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check — ECB / BOJ balance sheets | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing / liquidity operations | PBoC / NBS WebSearch | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]，30d | ✗ NOT DISCLOSED（30 日內無合格披露） |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | 財報摘要 WebSearch（stock-of-state，Q2 財報季） | ✓ SEARCH-VERIFIED（僅 top-4 合計，未取得逐家數字） |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | 供應商披露 WebSearch | ✓ SEARCH-VERIFIED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | CNBC 等 WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | 產業披露 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | [primary: SEARCH]；quarterly_state＝top-5 capex vs FCF（FactSet 2026-08-17）；event_scan＝30 日發債掃描，無披露 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | 綜合披露 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K / 10-Q [primary: SEARCH]，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | [primary: SEARCH]；quarterly_state＝capex +77% vs 需求成長；event_scan＝30 日進出場事件掃描，無披露 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | 新聞 WebSearch，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | stockanalysis WebSearch，7d | ✓ SEARCH-VERIFIED（僅 YTD 件數） |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | Finviz / Benzinga [primary: SEARCH]，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | Yahoo Finance 等 WebSearch，30d | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR / openinsider 掃描，14d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | Cboe [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | etf.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com 掃描，30d | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | KRX / TWSE / JPX / ESMA WebSearch，7d | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | OCC WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | Cboe / thetrading.tools WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove block） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | FINRA / GuruFocus WebSearch（交叉檢核） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | 信用市場 [primary: SEARCH]，30d | ✗ NOT DISCLOSED（30 日內無新披露） |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）＋WebSearch 事件掃描 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok；WebSearch 事件掃描無披露） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | trailing P/E 約 26.2、Shiller CAPE 約 41.2 | Shiller CAPE S&P 500 P/E August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus；原定 multpl / GuruFocus） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權本益比約 29.5x（S&P 500 約 25.6x） | Magnificent 7 weighted P/E August 2026 | https://www.fool.com/investing/2026/08/14/the-best-magnificent-seven-stocks-to-buy-in-august/（Motley Fool） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| breadth.rsp_spy | RSP 領先 SPY YTD 約 5pp | RSP vs SPY YTD 2026 breadth | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 top-10 集中度約 36.5% | S&P 500 top 10 concentration 2026 | https://www.ebc.com/forex/rsp-vs-spy（EBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.advance_decline | 領導由 top-100 向 bottom-400 擴散、廣度確認多頭 | market breadth advance decline August 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 55（Greed） | CNN Fear and Greed today August 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-07 月資料）約 1,417,225、YoY 約 +38.6%、MoM −5.7% | FINRA margin debt July 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt（GuruFocus；原定 FINRA） | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| retail.aaii | AAII 偏多 35.5%、偏空 39.9%（週結 2026-08-19） | AAII investor sentiment August 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 標售無明顯 tail、12.10% allotted at high | US Treasury 30-year auction August 2026 | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2026/R_20260813_3.pdf（TreasuryDirect） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| monetary.fedwatch | FedWatch 9/16 按兵不動約 68.4%、尾端為升息 | CME FedWatch September 2026 hold probability | https://en.macromicro.me/series/1645/probability-fed-rate-decrease（MacroMicro；原定 CME FedWatch） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_capex | top-4（MSFT、GOOGL、AMZN、META）2026 capex 合計約 $725bn、+77% YoY | hyperscaler 2026 capex guidance Microsoft Google Amazon Meta | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.token_growth | Anthropic run-rate 年增約 7 倍、API 佔營收多數 | Anthropic token growth revenue 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html（CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.openai_anthropic_revenue | OpenAI 約 $40B、Anthropic 約 $65B run-rate | OpenAI Anthropic annualized revenue August 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html（CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.compute_supply_demand | GPU 現貨租金高於合約價 2 倍以上、產能被利用率吸收 | AI GPU rental pricing utilization August 2026 | https://www.uncoveralpha.com/p/amazon-google-microsoft-meta-q2-earnings（UncoverAlpha） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex > FCF、2026 hyperscaler 發債擴張（capex 由現金流轉向舉債）；背景，非新事件 | hyperscaler external financing capex FCF debt 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow（FactSet） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.capital_cycle | [quarterly_state] 供給側 capex 年增約 77%、需求側 token／營收成長並存 | AI capex growth rate supply demand 2026 | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $105bn（OpenAI 40＋Anthropic 65）vs 年化 capex 約 $725bn（分母：top-4） | AI revenue to capex gap 2026 | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 掃描：7 日內 0 件合格事件 | AI rename SPAC ticker change August 2026 | Renaissance Capital / SEC EDGAR / 新聞掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD IPO 約 232 件（截至 2026-08-21）、無單週無營收 AI IPO 暴衝 | US IPO count August 2026 | https://stockanalysis.com/ipos/2026/（StockAnalysis） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot（單日 ≥100%、市值 <$1B、2+ 主題、弱基本面）掃描：0 檔 | microcap 100% single day surge quantum AI August 2026 | Finviz / Benzinga / StockTwits movers 掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 10 月 IPO、估值約 $2T | Anthropic OpenAI IPO 2026 | https://finance.yahoo.com/markets/article/spacex-openai-and-anthropic-here-are-the-most-anticipated-ipos-in-2026-114439441.html（Yahoo Finance） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 14 日內合格 Form 4 集中賣出：0 起 | insider Form 4 AI executives August 2026 | SEC EDGAR / openinsider 掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.52（日讀數；9 日均總量 0.85） | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio（thetrading.tools；原定 Cboe） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美股槓桿 ETF 總 AUM 約 $198bn 創紀錄；TQQQ 31.3、SOXL 17.3 | leveraged ETF AUM record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing；原定 etf.com） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| structural.us_single_stock_etf | 美單一個股槓桿 ETF 30 日內新核准／上市：0 件 | single-stock leveraged ETF launch SEC August 2026 | SEC EDGAR / ETF.com new launches 掃描 | — | 2026-08-24T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 8 月佔比約 62.4% 創紀錄 | 0DTE SPX volume share August 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| structural.options_volume | OCC YTD 日均 >71（百萬口）、量能高檔（2026-07 月資料） | OCC options volume 2026 | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/historical-volume-statistics（OCC） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 16.01、期限結構 contango（IVTS 約 0.82）、SKEW 偏高 | VIX term structure SKEW August 2026 | https://www.thetrading.tools/vix-term-structure（thetrading.tools；原定 Cboe） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 交叉檢核（同 retail.margin_debt，YoY +38.6%） | FINRA margin debt equity market cap ratio 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt（GuruFocus；原定 FINRA） | 2026-07-01 | 2026-08-24T09:30:00+08:00 |

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
  "r1_drawdown_pct": 4.41,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

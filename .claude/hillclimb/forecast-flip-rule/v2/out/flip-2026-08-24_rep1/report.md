> [DRY RUN] this report was not committed to archive.

# 2026-08-24 AI 泡沫破裂預測報告
報告日期：2026-08-24｜ISO 週次：2026-W35｜預測窗口：2026-08-24 → 2027-02-22｜前次基準：report-2026-08-20（4天前）

## 結論

**結論：no**

三條路徑都沒有已在進行中的跡象：NASDAQ-100 距 52 週高點只有 4.41%，還要再跌約 21.54% 才觸及 R1 門檻（`valuation.ndx_drawdown`）；top-4 hyperscaler 2026 capex 合計約 $725bn、年增約 77%，沒有任何下修（`ai.hyperscaler_capex`）；HY OAS 2.75% 顯示信用市場沒有壓力（`monetary.hy_oas`）。估值偏高與槓桿擴張證明泡沫存在，但不足以推翻「182 天內不破裂」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,308.86（2026-08-21），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 4.41%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，從最新收盤還要再跌約 21.54% 才會觸發。S&P 500 收在 7,674.37（2026-08-21），高於 200 日均線 8.15%、高於 52 週均線 9.61%（`valuation.sp500_trend`），代表價格偏延伸、有均值回歸空間，但目前沒有正在進行的急跌。在 2026-08-13 → 2026-08-20 的窗口內，S&P 500 下跌 2.02%、VIX 上升 9.43%，屬於正常的反向走勢，並非同漲的 crowded-optionality 警戒（`structural.vix_spx_comove`）。估值方面，Shiller CAPE 約 41.2、trailing P/E 約 26.2（`valuation.sp500_pe_cape`），Mag 7 加權 P/E 約 29.5x（`valuation.mag7_multiples`），代表一旦下跌，跌幅可能很大。

**判讀：** R1 離觸發還很遠（回撤 4.41%，門檻 25%）。窗口內要推過門檻，需要一個能讓指數再跌約 21.54% 的觸發因素，例如 R2 capex 下修、R3 信用事件，或通膨迫使 Fed 轉向升息。本次證據裡還沒有看到任何一項正在發生。

### R2 資本支出收縮

本次來源只揭露 top-4（Microsoft、Alphabet、Amazon、Meta）2026 capex 合計約 $725bn、年增約 77%（2026-08-13，Q2 財報後彙整；`ai.hyperscaler_capex`），沒有逐家列出指引數值：

- Microsoft：最新指引為 2026 Q2 財報季，逐家數值與方向本次來源未確立；彙整來源沒有記載任何下修。
- Alphabet：同上，逐家數值未確立，沒有下修紀錄。
- Amazon：同上，逐家數值未確立，沒有下修紀錄。
- Meta：同上，逐家數值未確立，沒有下修紀錄。

依本次來源，四家中已下修的家數為 0。需求面目前仍在吸收產能：GPU 現貨租金超過合約價 2 倍，產能被利用率吸收（`ai.compute_supply_demand`）；Anthropic 年化營收約 $65B、年增約 7×，OpenAI 約 $40B（`ai.openai_anthropic_revenue`、`ai.token_growth`）。缺口仍大：已披露 AI 終端營收約 $105bn，對比年化 capex 約 $725bn（分母：top-4，Oracle 與 neocloud 未納入）（`ai.revenue_capex_gap`）。下兩次季報（2026 Q3、Q4）依季度節奏應落在窗口內，但確切財報日期本次來源未確立。

**判讀：** R2 目前離觸發最遠：指引仍在大幅上修週期，利用率也強。要在窗口內觸發，需要至少兩家在接下來的季報主動下修，通常得先有需求轉弱（GPU 租金崩落、利用率下滑）或融資受阻。本次這兩種訊號都沒有出現。

### R3 AI 信用事件

本次的 AI 信用定價分歧（equity-vs-credit schism）掃描（14 日窗）與 AI infrastructure debt financing / vendor-financing loops 掃描（30 日窗）都順利完成，但沒有找到窗內披露（見 `## 資料缺漏與不確定性`）。因此達到 R3 規模門檻（負債 ≥ USD 5bn、以 AI 資料中心／算力為主業）的借款人名單、各自的債券利差、CDS、評等行動與到期牆，本次都未確立，也沒有看到任何違約、寬限、distressed exchange 或 going-concern 訊號的披露。廣義信用水位：HY OAS 2.75%、IG OAS 0.82%（2026-08-20，`monetary.hy_oas`、`monetary.ig_oas`）。repo 資金壓力（SOFR−IORB）為 −2 bps，SOFR99−IORB 為 6 bps（SOFR 與 IORB 皆為 2026-08-20），SRF 動用（Standing Repo Facility usage）為 0（2026-08-21）（`monetary.repo_stress_srf`）。銀行對 NBFI 放款約 $2.03T（2026-08-12，`structural.nbfi_bank_loans`）。

**判讀：** R3 沒有可觀察到的進行中事件，整體信用利差與資金面也都偏鬆。要在窗口內觸發，需要某家大型 neocloud 或資料中心借款人出現付款違約或 distressed exchange，通常會先看到發行利差急速走闊或融資失敗，而本次沒有這類證據。

## 支持 yes 的證據

- [整體] 估值處於極端水位：Shiller CAPE 約 41.2、trailing P/E 約 26.2（2026-08-20），Mag 7 加權 P/E 約 29.5x（2026-08-14），一旦有觸發因素，下跌幅度可能很大（`valuation.sp500_pe_cape`、`valuation.mag7_multiples`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）很大：已披露年化終端營收約 $105bn，對比年化 capex 約 $725bn（分母：top-4；2026-08-17），投資回收的疑慮是 capex 未來下修的潛在來源（`ai.revenue_capex_gap`）。
- [R1] 槓桿與投機部位偏高：FINRA margin debt（2026-07 月資料）約 1,417,225（百萬美元）、YoY 約 +38.6%；美股槓桿 ETF 總 AUM 創新高約 $198bn（2026-08-17）；SPX 0DTE 佔比創紀錄約 62.4%（2026-08-14），一旦開始下跌，可能放大跌幅（`retail.margin_debt`、`structural.leveraged_etf_aum`、`structural.zero_dte`）。
- [R1] 價格偏延伸：S&P 500 高於 200 日均線 8.15%（2026-08-21）；同時 CPI YoY 3.3%（2026-07 月資料），FedWatch 顯示 9/16 按兵不動約 68.4%、尾端風險為升息（2026-08-20），Fed 在下跌時出手緩衝的空間受限（`valuation.sp500_trend`、`monetary.cpi_yoy`、`monetary.fedwatch`）。
- [R1] 近一週出現風險趨避的苗頭：2026-08-13 → 2026-08-20 間 S&P 500 −2.02%、VIX +9.43%（`structural.vix_spx_comove`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點只有 4.41%（2026-08-21），距 R1 門檻 22,995.45 還要再跌約 21.54%（`valuation.ndx_drawdown`）。
- [R2] top-4 hyperscaler 2026 capex 合計約 $725bn、年增約 77%（2026-08-13），本次來源沒有任何一家下修；GPU 現貨租金超過合約價 2 倍，產能被利用率吸收（`ai.hyperscaler_capex`、`ai.compute_supply_demand`）。
- [R3] 信用與資金面沒有壓力：HY OAS 2.75%、IG OAS 0.82%（2026-08-20）；SOFR−IORB −2 bps、SRF 動用 0（2026-08-21）（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`）。
- [R2] AI 需求端營收仍在快速成長：Anthropic 年化營收約 $65B、年增約 7×，OpenAI 約 $40B（2026-08-17）（`ai.openai_anthropic_revenue`、`ai.token_growth`）。
- [整體] 情緒並不亢奮，廣度也在擴散：CNN Fear & Greed 55（2026-08-21）；AAII 偏空 39.9% 高於偏多 35.5%（2026-08-19）；RSP YTD 領先 SPY 約 5pp，領導股由 top-100 擴散到 bottom-400（2026-08-17）（`retail.fear_greed`、`retail.aaii`、`breadth.rsp_spy`、`breadth.advance_decline`）。
- [整體] 美債市場沒有失序跡象：MOVE 73.4（2026-08-21）；槓桿基金美債期貨淨空單 4 週縮減 244,468 口（2026-08-18）；30Y 標售沒有明顯 tail（2026-08-13）（`structural.treasury_basis_trade`、`monetary.treasury_auctions`）。

## 與前期比較

前次結論：yes（report-2026-08-20）
本次結論：翻轉
前次 forecast.json 沒有 yes_basis 欄位（該檔寫於 yes_basis 欄位存在之前），因此沒有需要逐項回應的前次 yes 理由；yes 每次都必須重新成立，本次的現有證據不足以撐起 yes。
翻轉依據：
- [R1] NASDAQ-100 距 52 週高點只有 4.41%（2026-08-21；前次 r1_drawdown_pct 為 4.03），距 R1 門檻還要再跌約 21.54%，沒有回撤正在進行（`valuation.ndx_drawdown`）。
- [R2] top-4 hyperscaler 2026 capex 合計約 $725bn、年增約 77%（2026-08-13），四家中 0 家下修，R2 沒有起點（`ai.hyperscaler_capex`）。
- [R3] HY OAS 2.75%（2026-08-20）且本次沒有任何 AI 借款人困境披露，R3 沒有可觀察到的傳導路徑（`monetary.hy_oas`）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源的檢索順利完成，但沒有找到合格的窗內披露（✗ NOT DISCLOSED）：`valuation.analyst_tp_decomposition`、`valuation.ai_credit_schism`、`retail.social_sentiment`、`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.pboc`、`monetary.private_credit_liquidity`、`ai.customer_concentration_rpo`、`ai.hyperscaler_financing_mix`（event_scan 無窗內事件）、`ai.depreciation_life`、`ai.capital_cycle`（event_scan 無窗內事件）、`structural.global_leveraged_approvals`、`structural.ai_infrastructure_debt`。其中最可能影響答案的是 `valuation.ai_credit_schism` 與 `structural.ai_infrastructure_debt`：本次無法確認 R3 候選借款人的利差、CDS 與到期牆。不過整體 HY/IG 利差偏緊，也沒有任何違約新聞，因此這個缺口目前不至於把答案推向 yes。`monetary.private_credit_liquidity` 沒有披露，私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）本次無法確認，但不改變判斷。

最大的不確定性：

- 下兩次 hyperscaler 季報（2026 Q3、Q4，確切日期未確立）：若有兩家下修，R2 會直接觸發，答案將推向 yes。目前的軌跡是上修。
- 通膨與 Fed 路徑：CPI YoY 3.3%，加上 FedWatch 的升息尾端風險，若升息成真且估值處於 CAPE 約 41 的水位，可能引發 R1 等級的下修，答案將推向 yes。
- R3 借款人名單與到期牆本次未確立：一旦大型 neocloud 出現再融資失敗，可能經由 R3 傳導到 R1，答案將推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7674.37 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 8.15 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 9.61 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29308.86 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 4.41 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q1，家庭股票配置 %） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.75 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.82 | FRED API (series_id=BAMLC0A0CM) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.69 | FRED API (series_id=DGS10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.35 | FRED API (series_id=DFII10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.34 | FRED API (series_id=T10YIE) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 86.48 | FRED API (series_id=DCOILWTICO) | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.34 | FRED API (series_id=T5YIFR) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8393 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7d） | 1.4 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.63 | FRED API (series_id=SOFR) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.71 | FRED API (series_id=SOFR99) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-08-24 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，$bn） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,745,699（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,927,307（€5.93T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,442,957（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.01 | FRED API (series_id=VIXCLS) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 16.01 | script vix_spx_comove block（FRED） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（2026-08-13 起 7 日） | 9.43 | script vix_spx_comove block（FRED） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（2026-08-13 起 7 日） | -2.02 | script vix_spx_comove block（FRED） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2026.1422（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-12 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7218048 | CFTC TFF futures-only | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 244468 | CFTC TFF futures-only | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.4 | Yahoo Finance chart API (^MOVE) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party transaction volume） | 2328.6 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值 / S&P 500 P/E and Shiller CAPE | multpl / GuruFocus WebSearch | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值 / Mag 7 weighted P/E | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值 / Analyst TP upgrade decomposition | 賣方摘要 WebSearch（90d、同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | 估值 / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值 / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值 / AI 信用定價分歧 | 信用市場 WebSearch（14d） | ✗ NOT DISCLOSED |
| breadth.rsp_spy | 廣度 / S&P 500 equal-weight | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度 / Top-10 concentration | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度 / Advance/decline ratio | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶 / CNN Fear & Greed Index | CNN WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶 / Margin Debt: FINRA | FINRA / GuruFocus WebSearch（月頻沿用） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶 / Retail survey: AAII | AAII WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶 / Social sentiment proxies | WSB / X WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶 / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶 / NAAIM Exposure Index | naaim.org WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | 機構 / BofA Fund Manager Survey | BofA / JPM WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣 / Fed funds rate: FRED | scripts/fetch_macro.py（DFEDTARU ok、DFEDTARL ok） | ✓ API |
| monetary.hy_oas | 貨幣 / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣 / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣 / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣 / 10Y Treasury real yield | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣 / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣 / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣 / CPI YoY: FRED | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣 / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣 / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | 貨幣 / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） | ✓ API |
| monetary.treasury_auctions | 貨幣 / 美債標售需求 | Reuters / TreasuryDirect WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣 / Fed funds rate path expectations | CME FedWatch WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣 / Fed balance sheet: FRED | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣 / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | 貨幣 / PBoC aggregate financing | PBoC / NBS WebSearch | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | 貨幣 / Private-credit / non-bank fund liquidity stress | BDC 披露 WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | 財報摘要 WebSearch（季頻沿用） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI / AI token volume growth rate | 供應商披露 WebSearch | ✓ SEARCH-VERIFIED |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | Bloomberg / CNBC WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration | 財報電話 WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | 產業披露 WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構 | 財報 / 發債 WebSearch；quarterly_state 沿用、event_scan 30d 無事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口 | 綜合披露 WebSearch（季頻沿用） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動 | 10-K / 10-Q WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI / 資本週期階段 | 產業披露 WebSearch；quarterly_state 沿用、event_scan 30d 無事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機 / Search for past 7 days | 新聞 / SEC EDGAR WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機 / IPO market heat | stockanalysis / Renaissance WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機 / Microcap thematic moonshots | Finviz / Benzinga WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機 / Upcoming AI IPOs | Bloomberg / CNBC / Yahoo WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機 / Insider selling at AI | SEC EDGAR / openinsider WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機 / Cboe equity-only put/call ratio | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構 / US leveraged ETF AUM | ETF.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構 / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com WebSearch（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | 結構 / Global leveraged product approvals | KRX / TWSE / JPX / ESMA WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構 / 0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構 / Options total volume | OCC WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構 / Cross-asset derivatives / correlation checks | Cboe / SpotGamma WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構 / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS ok、vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | 結構 / Cross-reference only: FINRA margin debt | FINRA WebSearch（交叉檢核） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構 / AI infrastructure debt financing / vendor-financing loops | 信用市場 WebSearch（30d） | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | 結構 / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構 / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok）＋ WebSearch | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | trailing P/E ≈26.2、Shiller CAPE ≈41.2（原定 multpl / GuruFocus） | Shiller CAPE S&P 500 P/E August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E ≈29.5x（S&P 500 ≈25.6x） | Magnificent 7 weighted P/E August 2026 | https://www.fool.com/investing/2026/08/14/the-best-magnificent-seven-stocks-to-buy-in-august/（Motley Fool） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| breadth.rsp_spy | RSP 領先 SPY YTD ≈5pp | RSP vs SPY YTD 2026 breadth | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 top-10 集中度 ≈36.5% | S&P 500 top 10 concentration 2026 | https://www.ebc.com/forex/rsp-vs-spy（EBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.advance_decline | 領導由 top-100 擴散到 bottom-400，廣度確認多頭 | market breadth advance decline August 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 55（Greed） | CNN Fear and Greed today August 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-07 月資料）≈1,417,225、YoY ≈+38.6%、MoM −5.7% | FINRA margin debt July 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt（GuruFocus，原定 FINRA） | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| retail.aaii | AAII 偏多 35.5%、偏空 39.9%（週結 2026-08-19） | AAII investor sentiment August 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 標售無明顯 tail、12.10% allotted at high | US Treasury 30-year auction August 2026 | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2026/R_20260813_3.pdf（TreasuryDirect） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| monetary.fedwatch | FedWatch 9/16 按兵不動 ≈68.4%，尾端為升息 | CME FedWatch September 2026 hold probability | https://en.macromicro.me/series/1645/probability-fed-rate-decrease（MacroMicro，原定 CME FedWatch） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_capex | top-4 2026 capex 合計 ≈725（$bn，+77% YoY），2026 Q2 財報後彙整 | hyperscaler 2026 capex guidance Microsoft Google Amazon Meta | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.token_growth | Anthropic run-rate 年增 ≈7×、API 佔營收多數 | Anthropic token growth revenue 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html（CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.openai_anthropic_revenue | OpenAI ≈$40B、Anthropic ≈$65B run-rate | OpenAI Anthropic annualized revenue August 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html（CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.compute_supply_demand | GPU 現貨租金 > 2× 合約價，產能被利用率吸收 | AI GPU rental pricing utilization August 2026 | https://www.uncoveralpha.com/p/amazon-google-microsoft-meta-q2-earnings（UncoverAlpha） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex > FCF、2026 hyperscaler 發債擴張（capex 由現金流轉向舉債） | hyperscaler external financing capex FCF debt 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow（FactSet） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.revenue_capex_gap | OpenAI 40 + Anthropic 65 → ≈105 vs 年化 capex ≈725（$bn；分母 top-4） | AI revenue to capex gap 2026 | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.capital_cycle | [quarterly_state] 供給側 capex 年增 ≈77%，需求側 token / 營收成長並存 | AI capex growth rate supply demand 2026 | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描：0 件合格事件 | AI rename SPAC ticker change August 2026 | Renaissance Capital / SEC EDGAR / 新聞掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD IPO ≈232 件（截至 2026-08-21），沒有單週無營收 AI IPO 暴衝 | US IPO count August 2026 | https://stockanalysis.com/ipos/2026/（StockAnalysis） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描（≥100% 單日、<$1B、2+ 主題、弱基本面）：0 檔 | microcap 100% single day surge quantum AI August 2026 | Finviz / Benzinga / StockTwits movers 掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 10 月 IPO、估值 ≈$2T | Anthropic OpenAI IPO 2026 | https://finance.yahoo.com/markets/article/spacex-openai-and-anthropic-here-are-the-most-anticipated-ipos-in-2026-114439441.html（Yahoo Finance） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 14 日內合格 Form 4 集中賣出：0 起 | insider Form 4 AI executives August 2026 | SEC EDGAR / openinsider 掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.52（daily；9 日均總量 0.85） | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio（thetrading.tools，原定 Cboe） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美股槓桿 ETF 總 AUM ≈198（$bn，新高）；TQQQ 31.3、SOXL 17.3 | leveraged ETF AUM record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing，原定 ETF.com） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| structural.us_single_stock_etf | 美股單一個股槓桿 ETF 30 日新核准／上市：0 件 | single-stock leveraged ETF launch SEC August 2026 | SEC EDGAR / ETF.com new launches 掃描 | — | 2026-08-24T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 8 月佔比創紀錄 ≈62.4% | 0DTE SPX volume share August 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| structural.options_volume | OCC YTD 日均 >71（百萬口），量能高檔 | OCC options volume 2026 | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/historical-volume-statistics（OCC） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 16.01、期限結構 contango（IVTS ≈0.82）、SKEW 偏高 | VIX term structure SKEW August 2026 | https://www.thetrading.tools/vix-term-structure（thetrading.tools） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt / 市值交叉檢核（2026-07 月資料，YoY +38.6%；主讀數見 retail.margin_debt） | FINRA margin debt equity market cap ratio 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt（GuruFocus，原定 FINRA） | 2026-07-01 | 2026-08-24T09:30:00+08:00 |

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
  "prior_answer": "yes",
  "flip_evidence": ["valuation.ndx_drawdown", "ai.hyperscaler_capex", "monetary.hy_oas"],
  "yes_basis": [],
  "r1_drawdown_pct": 4.41,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

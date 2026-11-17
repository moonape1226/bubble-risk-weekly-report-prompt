> [DRY RUN] this report was not committed to archive.

# 2026-08-24 AI 泡沫破裂預測報告

報告日期：2026-08-24｜ISO 週次：2026-W35｜預測窗口：2026-08-24 → 2027-02-22｜前次基準：report-2026-08-20（4天前）

## 結論

**結論：no**

三條路徑目前都離觸發門檻很遠：NASDAQ-100 距 52 週高點回撤 4.41%，還要再跌約 21.5% 才觸及 R1；top-4 hyperscaler 2026 capex 合計約 $725bn（+77% YoY），本次證據未見任何一家下修（R2）；HY OAS 2.75%、IG OAS 0.82%，信用市場沒有出現 R3 所需的 AI 借款人違約前兆。估值與槓桿雖然極端，但 182 天內缺少已經啟動的觸發機制。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,308.86（2026-08-21）；252 個交易日最高收盤 30,660.60（2026-06-02）；距 52 週高點回撤 4.41%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，從最新收盤還需再跌約 21.54% 才觸及。同期 S&P 500 為 7,674.37（2026-08-21），高於 200 日 MA 8.15%、高於 52 週 MA 9.61%（`valuation.sp500_trend`），價格延伸程度偏高，有均值回歸壓力，但不在崩跌區。波動面：VIX 16.01（2026-08-20），7 日內 VIX +9.43%、S&P 500 −2.02%，屬於正常的反向變動，不是 crowded-optionality 式的同向上漲（`structural.vix_spx_comove`）。

**判讀：** R1 距離很遠。要在窗口內觸發，需要一個能讓高估值（CAPE 約 41.2、Mag 7 加權 P/E 約 29.5x）在數月內重定價的催化劑，例如 R3 式信用事件、hyperscaler capex 指引轉向，或在通膨黏著（CPI YoY 3.3%）下市場預期轉為升息。目前這些催化劑都還沒出現。

### R2 資本支出收縮

本次證據只有 top-4（Microsoft、Alphabet、Amazon、Meta）2026 capex 合計約 $725bn、+77% YoY（Q2 財報季後彙整，2026-08-13，`ai.hyperscaler_capex`）。逐家的最新指引數字，以及各家相對前次正式指引是上修、持平或下修，都不在本次證據中，因此無法逐家列出方向。本次證據未見任何一家下修，已知下修家數為 0／4。窗口（到 2027-02-22）預計涵蓋兩輪季報，確切日期本次未取得。需求面仍在擴張：Anthropic 年化營收約 $65B、OpenAI 約 $40B（`ai.openai_anthropic_revenue`）；GPU 現貨租金超過合約價 2 倍，新增產能被利用率吸收（`ai.compute_supply_demand`）。

**判讀：** R2 距離很遠。合計 capex 仍在高速成長，需求端也還沒出現 order digestion。要觸發，至少需要兩家在接下來兩輪財報中轉向下修；可能的推力是 R1 式股價重挫、融資成本上升，或 AI 營收對 capex 缺口（約 $105bn vs 約 $725bn，`ai.revenue_capex_gap`）遭到市場懲罰。

### R3 AI 信用事件

本次 14 日內的 AI 信用定價掃描，以及 30 日內的 AI 基礎設施債務融資掃描，都沒有找到合格披露。因此本次沒有個別 AI 基礎設施借款人（負債 ≥ $5bn）的當期利差、CDS、評等或到期資訊可以引用，也沒有看到違約、covenant waiver 或 distressed exchange 的訊號。整體信用環境偏寬鬆：HY OAS 2.75%、IG OAS 0.82%（2026-08-20，`monetary.hy_oas`、`monetary.ig_oas`），週變動 0bp。repo 資金壓力（SOFR−IORB）為 −2bp，SOFR99−IORB 為 +6bp，SRF 動用（Standing Repo Facility usage）為 0（`monetary.repo_stress_srf`）。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）本次也沒有新的 30 日內披露。

**判讀：** 現有資料看不到 R3 的前兆。要在 182 天內完成破產、超過寬限期的違約或 distressed exchange，通常需要先看到利差明顯走闊、評等下調或再融資受阻，而目前的整體利差處於緊縮水位。最大的盲點是個別 neocloud 的信用資料本次沒有取得。

## 支持 yes 的證據

- [R1] 估值極端：Shiller CAPE 約 41.2、S&P 500 trailing P/E 約 26.2（2026-08-20，`valuation.sp500_pe_cape`），Mag 7 加權 P/E 約 29.5x（2026-08-14，`valuation.mag7_multiples`）。一旦出現催化劑，下跌空間會很大。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）：已披露年化 AI 終端營收約 $105bn（OpenAI 40＋Anthropic 65），年化 capex 約 $725bn（分母：top-4，不含 Oracle 與 neocloud）（2026-08-17，`ai.revenue_capex_gap`）。回本壓力是未來 capex 轉向的根源。
- [整體] 散戶與槓桿部位擁擠：FINRA margin debt YoY 約 +38.6%（2026-07 資料，`retail.margin_debt`）；美股槓桿 ETF 總 AUM 創新高，約 $198bn（2026-08-17，`structural.leveraged_etf_aum`）；SPX 0DTE 佔比創紀錄，約 62.4%（2026-08-14，`structural.zero_dte`）。一旦下跌，被迫去槓桿會放大跌幅。
- [R1] Fed 緩衝空間有限：CPI YoY 3.3%（2026-07，`monetary.cpi_yoy`）；FedWatch 顯示 9/16 會議維持利率的機率約 68.4%，另一端是升息而不是降息（2026-08-20，`monetary.fedwatch`）；10Y 期限溢價（term premium）為 0.8393%（2026-08-14，`monetary.term_premium`）。AI 主導的跌勢較難靠降息托底。
- [整體] 大型 AI IPO 供給將至：Anthropic 目標 10 月 IPO，估值約 $2T（2026-08-17，`speculation.upcoming_ai_ipos`）。大額股權供給與估值高點同時出現，是典型的晚期訊號。

## 支持 no 的證據

- [整體] 基礎機率加上路徑距離：NASDAQ-100 距 52 週高點回撤 4.41%，R1 門檻水位 22,995.45，還差約 21.54%（2026-08-21，`valuation.ndx_drawdown`）。任意 182 天窗口內出現這種跌幅並不常見。
- [R2] capex 仍在上修軌道：top-4 2026 capex 合計約 $725bn，+77% YoY（2026-08-13，`ai.hyperscaler_capex`）。本次證據未見任何一家下修。
- [R3] 信用利差緊縮：HY OAS 2.75%（`monetary.hy_oas`）、IG OAS 0.82%（`monetary.ig_oas`）（2026-08-20），週變動 0bp。repo 資金壓力（SOFR−IORB）−2bp、SRF 動用為 0（`monetary.repo_stress_srf`），看不到資金面裂縫。
- [R2] 需求端強勁：Anthropic 年化營收約 $65B、OpenAI 約 $40B（2026-08-17，`ai.openai_anthropic_revenue`），Anthropic run-rate 年增約 7 倍（`ai.token_growth`）；GPU 現貨租金超過合約價 2 倍（2026-08-13，`ai.compute_supply_demand`）。目前沒有過剩產能的證據。
- [R1] 廣度改善、情緒中性：RSP YTD 領先 SPY 約 5pp（`breadth.rsp_spy`），領導股由 top-100 擴散到 bottom-400（`breadth.advance_decline`）；CNN Fear & Greed 55（2026-08-21，`retail.fear_greed`）；AAII 偏多 35.5%、偏空 39.9%（2026-08-19，`retail.aaii`）。這些都不是狂熱頂部的讀數。

## 與前期比較

前次結論：無前次預測（report-2026-08-20 為舊格式評分報告）

前次為舊格式評分報告，本次是第一份 yes/no 預測，flip_evidence 為空。相對 2026-08-20 的主要變化如下：S&P 500 由 7,641.16 升至 7,674.37（+0.43%）；DGS10、DFII10、HY OAS、IG OAS 沒有新觀測，維持不變；10Y 分解三個 Δ 都是 0bp，判讀為無變動（DGS10、DFII10 無新觀測，T10YIE 已更新）；MOVE 由 73.18 升至 73.4；OFR tri-party repo transaction volume 由 $2,400.4bn 降至 $2,328.6bn（−2.99%）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

本次標為 ✗ NOT DISCLOSED 的來源：valuation.analyst_tp_decomposition、valuation.ai_credit_schism、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.pboc、monetary.private_credit_liquidity、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（quarterly_state 有資料，event_scan 30 日內無披露）、ai.depreciation_life、ai.capital_cycle（quarterly_state 有資料，event_scan 30 日內無披露）、structural.global_leveraged_approvals、structural.ai_infrastructure_debt。其中 valuation.ai_credit_schism 與 structural.ai_infrastructure_debt 直接涉及 R3：缺少個別 AI 借款人的利差與融資資料，是本次最大的盲點。若下次掃描出現 neocloud 利差急升或再融資受阻，可能讓 R3 判讀轉向 yes。其餘缺口不太可能改變答案。

最大的不確定性有三項：

1. 下一輪 hyperscaler 財報（窗口內預計兩輪）。只要有兩家轉向下修，R2 就會直接成立，答案會轉向 yes。
2. 通膨與 Fed 路徑。CPI YoY 3.3%，FedWatch 的另一端是升息；如果升息預期成形，高估值的重定價壓力會推向 R1，答案偏向 yes。
3. Anthropic IPO（目標 10 月）。成功上市會鞏固需求敘事，偏向 no；如果定價失利，可能成為情緒轉折點，偏向 yes。

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
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1 家戶股票配置 %） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-24T09:30:00+08:00 |
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
| monetary.term_premium | THREEFYTP10 latest | 0.8393 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 日） | 1.4 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.63 | FRED API (series_id=SOFR) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.71 | FRED API (series_id=SOFR99) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-08-24 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，$bn） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,745,699（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,927,307（€5.93T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,442,957（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.01 | FRED API (series_id=VIXCLS) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of；comove=false） | 16.01 | FRED API (series_id=VIXCLS / SP500 derived block) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日） | 9.43 | FRED API (derived block) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日） | -2.02 | FRED API (derived block) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2026.1422（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-12 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7,218,048 | CFTC TFF futures-only | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 244,468 | CFTC TFF futures-only | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.4 | Yahoo Finance chart API (^MOVE) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2328.6 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值 / S&P 500 P/E and Shiller CAPE | multpl / GuruFocus [SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值 / Mag 7 weighted P/E | 市場資料 [SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值 / Analyst TP upgrade decomposition | 賣方摘要 [SEARCH]，90 日且同季 | ✗ NOT DISCLOSED（無合格同季上修） |
| valuation.sp500_trend | 估值 / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值 / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值 / AI 信用定價分歧 | 信用市場 [SEARCH]，14 日 | ✗ NOT DISCLOSED（14 日內無合格披露） |
| breadth.rsp_spy | 廣度 / S&P 500 equal-weight | 市場資料 [SEARCH] | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度 / Top-10 concentration | 市場資料 [SEARCH] | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度 / Advance/decline ratio | 市場資料 [SEARCH] | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶 / CNN Fear & Greed Index | CNN [SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶 / Margin Debt: FINRA | FINRA / GuruFocus [SEARCH]（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶 / Retail survey: AAII | AAII [SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶 / Social sentiment proxies | WSB / X [SEARCH]，7 日 | ✗ NOT DISCLOSED（無顯著討論） |
| retail.household_equity_allocation | 散戶 / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶 / NAAIM Exposure Index | naaim.org [SEARCH] | ✗ NOT DISCLOSED（無當週值） |
| institutional.bofa_jpm_survey | 機構 / BofA Fund Manager Survey | BofA / JPM [SEARCH] | ✗ NOT DISCLOSED（無新調查） |
| monetary.fed_funds | 貨幣 / Fed funds rate: FRED | scripts/fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok、DFEDTARL ok） |
| monetary.hy_oas | 貨幣 / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣 / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣 / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣 / 10Y Treasury real yield | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣 / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣 / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣 / CPI YoY: FRED | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣 / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣 / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣 / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD） | ✓ API（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣 / 美債標售需求 | Reuters / TreasuryDirect [SEARCH]，14 日 | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣 / Fed funds rate path expectations | CME FedWatch [SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣 / Fed balance sheet: FRED | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣 / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok、JPNASSETS ok） |
| monetary.pboc | 貨幣 / PBoC aggregate financing | PBoC / NBS [SEARCH] | ✗ NOT DISCLOSED（無當期英文摘要） |
| monetary.private_credit_liquidity | 貨幣 / Private-credit / non-bank fund liquidity stress | BDC 披露 [SEARCH]，30 日 | ✗ NOT DISCLOSED（30 日內無合格披露） |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | 財報摘要 [SEARCH]（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI / AI token volume growth rate | 供應商披露 [SEARCH] | ✓ SEARCH-VERIFIED |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | CNBC 等 [SEARCH] | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration | 財報電話 [SEARCH] | ✗ NOT DISCLOSED（無合格披露） |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | 產業披露 [SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構 | 財報 / 發債 [SEARCH]；quarterly_state 沿用最新季、event_scan 30 日 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口 | 綜合披露 [SEARCH]（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動 | 10-K / 10-Q [SEARCH]，30 日 | ✗ NOT DISCLOSED（30 日內無變動） |
| ai.capital_cycle | AI / 資本週期階段 | 產業披露 [SEARCH]；quarterly_state 沿用、event_scan 30 日 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機 / Search for past 7 days | 新聞 / SEC EDGAR [SEARCH]，7 日 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機 / IPO market heat | stockanalysis / Renaissance [SEARCH] | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機 / Microcap thematic moonshots | Finviz / Benzinga [SEARCH]，7 日 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機 / Upcoming AI IPOs | Yahoo Finance 等 [SEARCH]，30 日 | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機 / Insider selling at AI | SEC EDGAR / openinsider [SEARCH]，14 日 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機 / Cboe equity-only put/call ratio | Cboe [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構 / US leveraged ETF AUM | ETF.com [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構 / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com [SEARCH]，30 日 | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | 結構 / Global leveraged product approvals | KRX / TWSE / JPX / ESMA [SEARCH]，7 日 | ✗ NOT DISCLOSED（7 日內無英文披露） |
| structural.zero_dte | 結構 / 0DTE option volume | Cboe [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構 / Options total volume | OCC [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構 / Cross-asset derivatives / correlation checks | Cboe / SpotGamma [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構 / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS、vix_spx_comove） | ✓ API |
| structural.margin_debt_crosscheck | 結構 / Cross-reference only: FINRA margin debt | FINRA / GuruFocus [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構 / AI infrastructure debt financing / vendor-financing loops | 信用市場 [SEARCH]，30 日 | ✗ NOT DISCLOSED（30 日內無合格披露） |
| structural.nbfi_bank_loans | 結構 / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構 / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）＋ [SEARCH] | ✓ API（cftc_lev_funds ok、move_index ok、ofr_repo ok；基差平倉新聞 14 日內無披露） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | trailing P/E 約 26.2、Shiller CAPE 約 41.2（原定來源 multpl / GuruFocus） | Shiller CAPE S&P 500 P/E August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E 約 29.5x（S&P 500 約 25.6x） | Magnificent 7 weighted P/E August 2026 | https://www.fool.com/investing/2026/08/14/the-best-magnificent-seven-stocks-to-buy-in-august/（Motley Fool） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 領先 SPY 約 5pp | RSP vs SPY YTD 2026 breadth | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 top-10 集中度約 36.5% | S&P 500 top 10 concentration 2026 | https://www.ebc.com/forex/rsp-vs-spy（EBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.advance_decline | 領導股由 top-100 擴散到 bottom-400，廣度確認多頭 | market breadth advance decline August 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 55（Greed） | CNN Fear and Greed today August 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-07 月資料）約 1,417,225（百萬美元），YoY 約 +38.6%，MoM −5.7% | FINRA margin debt July 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt（GuruFocus／FINRA） | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| retail.aaii | AAII 偏多 35.5%、偏空 39.9%（週結 2026-08-19） | AAII investor sentiment August 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 標售無明顯 tail，12.10% allotted at high | US Treasury 30-year auction August 2026 | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2026/R_20260813_3.pdf（TreasuryDirect） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| monetary.fedwatch | FedWatch：9/16 會議維持利率約 68.4%，另一端為升息 | CME FedWatch September 2026 hold probability | https://en.macromicro.me/series/1645/probability-fed-rate-decrease（MacroMicro，原定來源 CME FedWatch） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_capex | top-4（MSFT／GOOGL／AMZN／META）2026 capex 合計約 $725bn，+77% YoY（Q2 財報季） | hyperscaler 2026 capex guidance Microsoft Google Amazon Meta | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.token_growth | Anthropic run-rate 年增約 7 倍，API 佔營收多數 | Anthropic token growth revenue 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html（CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.openai_anthropic_revenue | OpenAI 約 $40B、Anthropic 約 $65B run-rate | OpenAI Anthropic annualized revenue August 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html（CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.compute_supply_demand | GPU 現貨租金超過合約價 2 倍，產能被利用率吸收 | AI GPU rental pricing utilization August 2026 | https://www.uncoveralpha.com/p/amazon-google-microsoft-meta-q2-earnings（UncoverAlpha） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 超過 FCF，2026 hyperscaler 發債擴張（capex 由現金流轉向舉債） | hyperscaler external financing capex FCF debt 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow（FactSet） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $105bn（OpenAI 40＋Anthropic 65）vs 年化 capex 約 $725bn（分母：top-4） | AI revenue to capex gap 2026 | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.capital_cycle | [quarterly_state] 供給側 capex 年增約 77%，需求側 token／營收成長並存 | AI capex growth rate supply demand 2026 | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 掃描：7 日內 0 件合格事件 | AI rename SPAC ticker change August 2026 | Renaissance Capital / SEC EDGAR / 新聞掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD IPO 約 232 件（截至 2026-08-21），單週無無營收 AI IPO 暴衝 | US IPO count August 2026 | https://stockanalysis.com/ipos/2026/（StockAnalysis） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot（單日 ≥100%、市值低於 $1B、疊 2 個以上主題、基本面弱）掃描：0 檔 | microcap 100% single day surge quantum AI August 2026 | Finviz / Benzinga / StockTwits movers | — | 2026-08-24T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 10 月 IPO，估值約 $2T | Anthropic OpenAI IPO 2026 | https://finance.yahoo.com/markets/article/spacex-openai-and-anthropic-here-are-the-most-anticipated-ipos-in-2026-114439441.html（Yahoo Finance） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 14 日內合格 Form 4 集中賣出：0 起 | insider Form 4 AI executives August 2026 | SEC EDGAR / openinsider | — | 2026-08-24T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.52（日讀數；9 日均總量 0.85） | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio（thetrading.tools） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美股槓桿 ETF 總 AUM 創新高，約 $198bn；TQQQ 31.3、SOXL 17.3（$bn） | leveraged ETF AUM record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| structural.us_single_stock_etf | 美股單一個股槓桿 ETF 30 日內新核准／上市：0 件 | single-stock leveraged ETF launch SEC August 2026 | SEC EDGAR / ETF.com new launches | — | 2026-08-24T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 8 月佔比創紀錄，約 62.4% | 0DTE SPX volume share August 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| structural.options_volume | OCC YTD 日均超過 71（百萬口），量能在高檔 | OCC options volume 2026 | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/historical-volume-statistics（OCC） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 16.01，期限結構 contango（IVTS 約 0.82），SKEW 偏高 | VIX term structure SKEW August 2026 | https://www.thetrading.tools/vix-term-structure（thetrading.tools） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt／市值交叉檢核（見 retail.margin_debt，YoY +38.6%） | FINRA margin debt equity market cap ratio 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt（GuruFocus／FINRA） | 2026-07-01 | 2026-08-24T09:30:00+08:00 |

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

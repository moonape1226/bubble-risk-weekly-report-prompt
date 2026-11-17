> [DRY RUN] this report was not committed to archive.

# 2026-07-20 AI 泡沫破裂預測報告

報告日期：2026-07-20｜ISO 週次：2026-W30｜預測窗口：2026-07-20 → 2027-01-18｜前次基準：report-2026-07-16（4天前）

## 結論

**結論：no**

三條路徑目前都離解析門檻很遠：NASDAQ-100 距 52 週高點回撤 6.74%，離 R1 的 25% 還差一大段（`valuation.ndx_drawdown`）；hyperscaler 2026 capex 合計 ≈$700B，而且仍在上修，未見任何下修（`ai.hyperscaler_capex`）。Oracle／CoreWeave CDS 走闊與 Blue Owl 的 gate proration / breach 顯示信用端開始承壓，但 HY OAS 只有 2.71%，信用整體仍緊，不足以支撐 182 天內出現 R3 違約或 R1 崩跌的判斷（`valuation.ai_credit_schism`、`monetary.hy_oas`）。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 28,592.66（2026-07-17），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 6.74%（`valuation.ndx_drawdown`）。R1 門檻水位 22,995.45，最新收盤還要再跌約 19.6% 才會觸及。同期 S&P 500 收在 7,457.69（2026-07-17），較前次基準日（7,533.77）下跌 1.01%，但仍高於 200 日均線 6.73%、高於 52 週均線 8.42%（`valuation.sp500_trend`）。VIX 在 2026-07-10 → 2026-07-17 的 7 日窗內由 15.03 升至 18.77（+24.88%），同窗 S&P 500 −1.55%，屬正常的反向走勢，不是 crowded-optionality 式的同向上升（comove=false，`structural.vix_spx_comove`）。2026-07-17 NYSE 跌家約為漲家 2 倍，新高 241／新低 166，晶片股賣壓擴散（`breadth.advance_decline`）。

**判讀：** R1 距門檻還有約 19.6% 的跌幅。估值處於歷史高位（CAPE 41.52、margin debt +53.7% YoY），一旦下跌，幅度可能很大；但目前只是從 6 月高點小幅回落。要在窗口內觸發，需要信用重定價（R3 方向）或 capex 指引轉向（R2 方向）這類催化劑引發強迫去槓桿，本次證據不足以支持這條路徑會在 182 天內走完。

### R2 資本支出收縮

本次來源只提供四家（Microsoft、Alphabet、Amazon、Meta）2026 capex 的合計數：≈$700B，來源描述為「仍上修」（2026-05-15，對應最近一季財報後的指引，carry-forward）（`ai.hyperscaler_capex`）。逐家的最新正式指引金額與上一次指引的比較，本次來源沒有逐一確立，因此四家都只能記為「依合計敘述為上修方向、逐家數值未確立」，沒有任何一家下修的披露。目前下修家數為 0／4，距 R2 要求的 2 家還差 2 家。四家下一次財報日期本次來源未提供，所以無法列出窗口內的具體日期；只能確定窗口（至 2027-01-18）至少涵蓋一次季報週期。伺服器 DRAM 3Q26 合約價季增 +13–18%，顯示 AI 硬體需求仍緊、供給仍吃緊，並非 order digestion（`ai.compute_supply_demand`）。

**判讀：** R2 目前是離門檻最遠的路徑：合計指引仍在上修，供應鏈價格也顯示需求偏強。要在窗口內成立，需要兩家在接下來的季報中同時轉為下修，通常要先有 R1 級的市場壓力或 AI 營收明顯不及預期作為前導，本次證據沒有這類前導訊號。

### R3 AI 信用事件

AI 相關信用定價開始走闊：Oracle 5 年期 CDS ≈198bp，創紀錄；CoreWeave CDS ≈665bp（2026-07-16）（`valuation.ai_credit_schism`）。CoreWeave 以 AI 算力為主業，是最可能落入 R3 範圍的借款人；但它的總負債金額，以及近期到期與再融資需求，本次來源沒有確立，不能據此判斷規模或到期牆。Oracle 的主業並非 AI 資料中心，即使利差走闊也不直接符合 R3 的借款人定義。本次沒有找到任何破產申請、超過寬限期的付款違約、covenant waiver 或 distressed exchange 的報導。非銀行端方面，Blue Owl OCIC Q2 收到的贖回申請達 18.8%，依 5% 的 quarterly redemption cap 比例撥付，屬實際的 gate proration / breach（2026-07-02）（`monetary.private_credit_liquidity`）。整體信用仍緊：HY OAS 2.71%、IG OAS 0.78%（2026-07-16）（`monetary.hy_oas`、`monetary.ig_oas`）。

**判讀：** CoreWeave 665bp 的 CDS 代表市場已為違約風險定價，與 HY 整體的 2.71% 形成 AI 信用定價分歧（equity-vs-credit schism），屬後期訊號，也是三條路徑中最值得追蹤的一條。但 R3 要求實際的違約、破產或 distressed exchange；本次沒有任何事件，也沒有確立的近期到期牆。要在窗口內成立，需要再融資失敗或流動性斷裂，目前只到「定價承壓」，還不到「事件將發生」的程度。

## 支持 yes 的證據

- [R3] CoreWeave CDS ≈665bp、Oracle 5 年期 CDS ≈198bp 創紀錄（2026-07-16），信用端已開始為 AI 基礎設施借款人的風險重新定價，而股價仍接近高點，形成 equity-vs-credit schism（`valuation.ai_credit_schism`）。
- [R3] Blue Owl OCIC Q2 贖回申請 18.8%，依 5% 的 quarterly redemption cap 比例撥付，屬實際的 gate proration / breach（2026-07-02）；私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）可能收緊 AI 基礎設施的融資管道（`monetary.private_credit_liquidity`）。
- [整體] 估值與槓桿處於極端水位：S&P 500 trailing P/E 32.08、Shiller CAPE 41.52（2026-07-17）；FINRA margin debt $1.416T、+53.7% YoY（2026-05 月資料）；NAAIM 95.64（2026-07-15）。一旦有催化劑，下跌幅度可能很大（`valuation.sp500_pe_cape`、`retail.margin_debt`、`retail.naaim`）。
- [R1] 2026-07-17 晶片股賣壓擴散，NYSE 跌家約為漲家 2 倍；VIX 7 日內 +24.88% 至 18.77；CNN Fear & Greed 降至 37（Fear）（`breadth.advance_decline`、`structural.vix_spx_comove`、`retail.fear_greed`）。
- [整體] 投機與槓桿產品熱度高：US 槓桿 ETF 總 AUM ≈$198B 創紀錄（2026-07-10）；OCC 6 月期權成交量 1,603,491,559 口、+45% YoY；2026-07-07 新上市 6 檔 2x 單一個股槓桿 ETF（GOOGL/AMZN/META/AAPL）（`structural.leveraged_etf_aum`、`structural.options_volume`、`structural.us_single_stock_etf`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 6.74%（2026-07-17），R1 門檻水位 22,995.45，還要再跌約 19.6% 才會觸及（`valuation.ndx_drawdown`）。
- [R2] 四家 hyperscaler 2026 capex 合計 ≈$700B，仍在上修，沒有任何一家下修的披露，下修家數 0／4（`ai.hyperscaler_capex`）；伺服器 DRAM 3Q26 合約價季增 +13–18%（2026-07-03），顯示需求端仍緊（`ai.compute_supply_demand`）。
- [R3] 整體信用沒有重定價：HY OAS 2.71%、IG OAS 0.78%（2026-07-16），與前次基準持平；本次沒有任何 AI 借款人違約、破產或 distressed exchange 的報導（`monetary.hy_oas`、`monetary.ig_oas`）。
- [整體] 資金市場平穩：SOFR−IORB −3bp、SOFR99−IORB +5bp（2026-07-16），SRF 動用 0（2026-07-17）；MOVE 70.88（2026-07-17）；美債標售需求 10Y bid-to-cover 2.59、僅小幅 tail（2026-07-08）。沒有國債市場失序（Treasury market dysfunction）的跡象（`monetary.repo_stress_srf`、`structural.treasury_basis_trade`、`monetary.treasury_auctions`）。
- [整體] 基準率：任一 182 天窗口內，R1–R3 都不是常態結果。本次的高估值與投機熱度只能證明脆弱性，無法說明破裂時點；市場廣度也未崩壞，RSP YTD +10.68% 優於 SPY +7.47%（2026-06-10）（`breadth.rsp_spy`、`valuation.sp500_pe_cape`）。

## 與前期比較

前次結論：無前次預測（report-2026-07-16 為舊格式評分報告）

- 前次為舊格式評分報告，沒有 yes/no 預測可比較，flip_evidence 為 []；本次是新格式下的第一份預測，答案 no 完全由本次證據與基準率判定。
- 與前次基準日（2026-07-16）相比：S&P 500 −1.01%；VIX 由 16.73 升至 18.77；T10YIE +2bp、T5YIFR +1bp；HY/IG OAS、SOFR、DGS10、DFII10 無新觀測（持平）。
- 本次的 10Y 分解：ΔDGS10 0bp、ΔDFII10 0bp、ΔT10YIE +2bp，判讀為 不可判（視窗不一致）（DGS10、DFII10 無新觀測，T10YIE 有更新）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

- 未披露（✗ NOT DISCLOSED）的來源：valuation.analyst_tp_decomposition、retail.social_sentiment、institutional.bofa_jpm_survey、ai.token_growth、ai.openai_anthropic_revenue（最近一次為 2026-05-15 的 Q2 數據，不是本季披露）、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（兩組件都無披露）、ai.depreciation_life、ai.capital_cycle（兩組件都無披露）、structural.global_leveraged_approvals、structural.ai_infrastructure_debt。其中 structural.ai_infrastructure_debt 與 ai.hyperscaler_financing_mix 的缺漏與 R3 最直接相關：如果存在未被發現的大額到期或 SPV 融資壓力，可能把判斷推向 yes，但即使如此，也需要實際的違約事件才會改變答案。
- speculation.insider_form4 標為 0 件，但 SEC EDGAR egress 受限，一手 Form 4 URL 無法取得，只能依二手篩選完成；這項缺口不影響本次答案。
- 證據紀錄的差異：搜尋結果表把美債基差交易槓桿的三個 script block 記為 fetch_failed，但 macro artifact（scripts/fetch_macro.py 完整輸出）中 cftc_lev_funds、move_index、ofr_repo 都是 status ok。本報告以 macro artifact 為準，記為 ✓ API。
- 部分 snapshot 資料偏舊：Mag 7 加權 P/E（2026-05-15）、0DTE 佔比（2026-02-28），只作背景，不作決定性證據。
- 最大不確定性 1：CoreWeave 等 neocloud 的再融資能力。CDS 665bp 代表市場已在為違約風險定價，若窗口內出現再融資失敗或 distressed exchange，R3 會直接成立，並可能連帶觸發 R1。這是把答案推向 yes 的首要風險。
- 最大不確定性 2：hyperscaler 下一季財報的 capex 指引（日期本次未確立）。若兩家同時下修，R2 成立；目前合計仍在上修，所以方向偏向 no。
- 最大不確定性 3：私募信貸贖回壓力是否擴散。Blue Owl 的 gate proration / breach 若擴大為多家基金的 net inflow→outflow flip，AI 基礎設施的融資管道會收緊，加大 R3 風險；目前只有單一基金的披露。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7457.69 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 6.73 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.42 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28592.66 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 6.74 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1 家庭股票配置 %） | 45.76080873390133（≈45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.71 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.57 | FRED API (series_id=DGS10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.35 | FRED API (series_id=DFII10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.24 | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 79.2 | FRED API (series_id=DCOILWTICO) | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料，CPI YoY %） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.21 | FRED API (series_id=T5YIFR) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright 10Y 期限溢價） | 0.7788 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.62 | FRED API (series_id=SOFR) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.7 | FRED API (series_id=SOFR99) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,743,028（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,970,516（€5.97T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,395,509（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 18.77 | FRED API (series_id=VIXCLS) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 18.77 | FRED API (series_id=VIXCLS, SP500) vix_spx_comove block | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日窗，base 2026-07-10） | 24.88 | FRED API (series_id=VIXCLS, SP500) vix_spx_comove block | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2004.0237（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（槓桿基金美債期貨淨部位，口數） | -7562874 | CFTC TFF futures-only (cftc_lev_funds) | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 70.88 | Yahoo Finance chart API ^MOVE (move_index) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2342.6 | OFR STFM REPO-TRIV1_TV_TOT-P (ofr_repo) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | MarketXLS WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-05-15，偏舊） |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 WebSearch [primary: SEARCH]，90d＋同季 | ✗ NOT DISCLOSED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧 | 信用市場 WebSearch [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | ahasignals WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth 新聞 WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com／MacroMicro [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA | FINRA／Advisor Perspectives WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag WebSearch，7d | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／ycharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（DFEDTARU ok、DFEDTARL ok） | ✓ API |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） | ✓ API |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | 標售 recap WebSearch [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Bloomberg WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 WebSearch [primary: SEARCH]，30d | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報 WebSearch（stock-of-state carry-forward） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／The Information WebSearch（需本季披露） | ✗ NOT DISCLOSED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 WebSearch [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報 quarterly_state＋30d event_scan WebSearch [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K／10-Q WebSearch，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速 quarterly_state＋30d event_scan WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | WebSearch，7d | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis／Renaissance WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／Benzinga／StockTitan movers [primary: SEARCH]，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | S-1／具名報導 WebSearch，30d | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR／openinsider [primary: SEC EDGAR]，14d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe daily statistics [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com／cryptobriefing [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF.com WebSearch，30d | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch，7d | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe insights WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-02-28，偏舊） |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com WebSearch（月頻） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe／AInvest WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS ok、vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | Advisor Perspectives WebSearch（交叉引用） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | WebSearch [primary: SEARCH]，30d | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok；aggregation any） | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.08 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 41.52 | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E ≈40 trailing | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026 （MarketXLS） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS ≈198bp 創紀錄、CoreWeave CDS ≈665bp | Oracle CoreWeave CDS spread widening July 2026 | https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/ （Real Investment Advice） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP +10.68% vs SPY +7.47% YTD | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St.） | 2026-06-10 | 2026-07-20T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 36.40% | S&P 500 top 10 concentration percent 2026 | https://ahasignals.com/sp500-concentration-risk/ （AHA Signals） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| breadth.advance_decline | NYSE 2026-07-17 跌家約為漲家 2 倍、新高 241／新低 166 | NYSE advance decline breadth July 17 2026 | https://money.usnews.com/investing/news/articles/2026-07-17/wall-st-futures-fall-as-chip-selloff-gathers-pace-netflix-tumbles （US News／Reuters） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（Fear） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed （MacroMicro；原定 cnn.com） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-05 月資料）$1.416T、+53.7% YoY | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives；原定 FINRA） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |
| retail.aaii | AAII Bull 44.9% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number （YCharts；原定 naaim.org） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 2.59、小幅 tail | US Treasury 10Y auction July 2026 bid to cover | https://cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/ （Crypto Briefing；原定 Reuters／TreasuryDirect） | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch：7/29 會議維持利率 ≈86.7% | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch （CryptoRank；原定 CME） | 2026-07-18 | 2026-07-20T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance （Bloomberg） | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 贖回申請 18.8%，依 5% quarterly redemption cap 比例撥付（gate proration / breach） | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://whbl.com/2026/07/02/blue-owl-keeps-withdrawal-limits-even-as-redemption-pressure-modestly-eases/ （WHBL／Reuters） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| ai.hyperscaler_capex | MSFT／GOOGL／AMZN／META 2026 capex 合計 ≈$700B、仍上修 | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html （Yahoo Finance） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 +13–18% QoQ | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html （TrendForce） | 2026-07-03 | 2026-07-20T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex ≈$700B vs AI 終端營收低百億級 | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| speculation.ai_rename_spac | EVTV→Azio AI（AZIO）改名，2026-07-13 起以新代號交易 | AI rename ticker change July 2026 Azio EVTV | https://www.businesswire.com/news/home/20260710628386/en/Azio-AI-Holdings-Inc.-Nasdaq-EVTV-to-Begin-Trading-Under-New-Ticker-Symbol-AZIO-Completing-Corporate-Rebrand （Business Wire） | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD ≈200 檔 IPO、募資 $141.2B | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/ （StockAnalysis） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| speculation.microcap_moonshots | 7 日內合格 microcap moonshot：0 件 | microcap 100% single day quantum AI moonshot July 2026 | Finviz／Benzinga／StockTitan movers screener | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 投資人會議，估值 $965B，可能 10 月掛牌 | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html （CNBC） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 cluster：0 件（EDGAR egress 受限） | insider Form 4 cluster AI leaders July 2026 openinsider | SEC EDGAR／openinsider（一手 URL 無法取得） | — | 2026-07-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.73（日讀數） | Cboe equity put call ratio July 2026 | https://www.cboe.com/markets/us/options/market-statistics/daily/ （Cboe） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM ≈$198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing；原定 etf.com／ETFGI） | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 新上市 6 檔 2x GOOGL／AMZN／META／AAPL 單一個股 ETF | single-stock leveraged ETF launch July 2026 Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-07 | 2026-07-20T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 成交 ≈63% | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/ （Cboe） | 2026-02-28 | 2026-07-20T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月成交 1,603,491,559 口、+45% YoY | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 145.13、VIX ≈16.5 contango | VIX term structure SKEW July 2026 | https://www.ainvest.com/news/0dte-volatility-drives-market-strategies-2026-2602/ （AInvest） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-05 月資料）$1.416T、+53.7% YoY（交叉引用 retail.margin_debt） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |

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
  "yes_basis": [],
  "r1_drawdown_pct": 6.74,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

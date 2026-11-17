> [DRY RUN] this report was not committed to archive.

# 2026-08-06 AI 泡沫破裂預測報告

報告日期：2026-08-06｜ISO 週次：2026-W32｜預測窗口：2026-08-06 → 2027-02-04｜前次基準：report-2026-08-03（3天前）

## 結論

**結論：no**

三條路徑目前都離解析門檻很遠：NASDAQ-100 距 52 週高點回撤 3.83%，還要再跌約 22.02% 才觸及 R1（`valuation.ndx_drawdown`）；四家 hyperscaler 的 2026 capex 指引仍在上修，合計約 $725B，沒有一家下修（`ai.hyperscaler_capex`）。CoreWeave 的信用重定價（5Y CDS 約 855bp）是本次最強的 yes 訊號，但它仍只是利差走闊，不是違約或 distressed exchange；整體 HY OAS 2.73% 與 repo 資金壓力（SOFR−IORB）1bp 也顯示傳導尚未開始。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29487.79（2026-08-05）。252 個交易日內最高收盤為 30660.6（2026-06-02），目前距 52 週高點回撤 3.83%。R1 門檻水位 22995.45（高點 × 0.75），也就是從最新收盤再跌約 22.02% 才會觸發（`valuation.ndx_drawdown`）。同一時間 S&P 500 收 7723.55，高於 200 日均線 9.71%、高於 52 週均線 11.32%（`valuation.sp500_trend`），代表價格仍偏延伸、有均值回歸空間。估值也處於高檔：S&P 500 trailing P/E 29.74，Shiller CAPE 42.19（`valuation.sp500_pe_cape`）。不過波動率正在回落：VIX 15.81，過去 7 日（2026-07-29 → 2026-08-05）下跌 23.48%，同期 S&P 500 上漲 5.57%，comove=false，沒有出現 crowded-optionality 警戒讀數（`structural.vix_spx_comove`）。情緒面也不算亢奮：CNN Fear & Greed 約 58（Greed）（`retail.fear_greed`），AAII 看空 42.1%、看多 31.0%（`retail.aaii`）。

**判讀：** R1 距離很遠。要在 2027-02-04 前觸發，NASDAQ-100 必須從目前水位再跌約 22%，這需要一個本次證據裡還沒出現的強力催化劑，例如 AI 信用事件外溢、hyperscaler 下修 capex，或國債市場失序迫使去槓桿。高估值與價格延伸說明一旦出事跌幅會很大，但不足以證明會在窗口內發生。

### R2 資本支出收縮

CNBC 2026-07-28 報導 hyperscaler 的 2026 capex 指引持續上修，合計約 $725B。其中 Alphabet 在 Q2 財報上修 capex 後股價遭到賣壓，顯示市場對 capex 的檢視變嚴（`ai.hyperscaler_capex`）。逐家情況如下：Alphabet 在 2026 Q2 財報上修；Microsoft、Amazon、Meta 被涵蓋在同一篇「合計續上修」的報導中（2026 Q2 財報季），但本次取得的證據沒有列出三家各自的指引數值，因此三家的方向只能依該報導記為「無下修報導」，不寫具體數字。四家中目前已下修的家數是 0。下一輪財報日期在本次證據中沒有確認；依季度節奏，下一輪（2026 Q3）財報應落在窗口內，但日期本次未取得。需求面方面，HBM／DRAM 合約價續升，H200 租金約 $4.39/hr，供給缺口預期延續到 1H2027（`ai.compute_supply_demand`），目前看不到產能過剩迫使 capex 縮手的證據。反方向的壓力是 AI 營收對 capex 缺口（revenue-to-capex gap）：已披露的年化 AI 終端營收約 $72B（Anthropic 約 $47B＋OpenAI 約 $25B，2026-06-15 資料），對比年化 capex 約 $725B（分母為 CNBC 所稱 hyperscaler 合計，來源未逐一列明涵蓋公司），缺口仍大（`ai.revenue_capex_gap`）。

**判讀：** R2 距離很遠。四家都還在上修或沒有下修報導，要在窗口內出現兩家下修，需要在接下來一到兩次財報中發生急轉。可能的推手包括：股市對 capex 的懲罰（Alphabet 案例）擴大成管理層主動收縮，或 R1／R3 事件迫使預算重估。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）出現實際的重定價：截至 2026-08-03，CoreWeave 5Y CDS 約 855bp，一筆 $2.6B 貸款利差走闊 125bp，投資人開始要求加入 covenants；Oracle CDS 約 215bp（`valuation.ai_credit_schism`）。在 AI infrastructure debt financing / vendor-financing loops 方面，CoreWeave 於 2026-07-29 調高一筆與 Anthropic 合約掛鉤的 $2.6B 貸款收益率；Nebius 在 2026-07-17 有一筆 $775M 擔保融資（`structural.ai_infrastructure_debt`）。營收集中度方面，Microsoft RPO 約 $678B，其中約 32% 繫於單一客戶 OpenAI（`ai.customer_concentration_rpo`），這屬於 backlog 重複計算風險（RPO double-counting）的背景，但本次沒有取得其他供應商對同一 counterparty 的承諾金額，因此無法加總比較。至於規模門檻：CoreWeave 與 Nebius 的總負債是否達到 R3 的 50 億美元，本次來源沒有確立，不做推估。本次證據也沒有任何借款人出現付款違約、寬限期、distressed exchange、going-concern 字樣或破產申請。廣義信用環境仍然很緊：HY OAS 2.73%（`monetary.hy_oas`），IG OAS 0.78%（`monetary.ig_oas`）。

**判讀：** R3 是三條路徑中最接近的一條，但距離解析仍很遠。CDS 約 855bp 代表市場對 CoreWeave 定價了明顯的違約風險，貸款端也開始要求更多保護，屬於信貸端先重定價的後期訊號。然而 R3 需要實際的破產、超過寬限期的付款違約或完成 distressed exchange，目前看到的只是融資成本上升。要在窗口內觸發，需要再融資失敗、主要客戶合約（如 Anthropic／OpenAI 承諾）出問題，或信用市場全面收緊。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 約 855bp，一筆 $2.6B 貸款利差走闊 125bp、貸款人要求 covenants，Oracle CDS 約 215bp（2026-08-03），顯示 AI 信用端已開始重定價，股權端尚未跟上（`valuation.ai_credit_schism`）。
- [R3] CoreWeave 於 2026-07-29 調高與 Anthropic 掛鉤的 $2.6B 貸款收益率，AI 基礎建設借款人的再融資成本正在上升（`structural.ai_infrastructure_debt`）。
- [整體] 估值與價格延伸都在高檔：Shiller CAPE 42.19、trailing P/E 29.74（2026-08-05），S&P 500 高於 200 日均線 9.71%（2026-08-05），一旦出現催化劑，下跌空間很大（`valuation.sp500_pe_cape`、`valuation.sp500_trend`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）約 $72B 對 $725B，加上 Alphabet 上修 capex 後遭賣壓（2026-07-28），市場對 capex 回報的容忍度在下降（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`）。
- [整體] 槓桿偏高：FINRA 2026-06 margin debt $1.502T、YoY +51.5%（`retail.margin_debt`）；US 槓桿 ETF 總 AUM 創新高約 $198B（2026-07-23）（`structural.leveraged_etf_aum`）。下跌時可能放大被動去槓桿。
- [R3] Microsoft RPO 約 $678B，其中約 32% 繫於 OpenAI（2026-07-30），單一客戶集中度高（`ai.customer_concentration_rpo`）。
- [整體] 美債標售需求（auction tail / bid-to-cover）轉弱：5Y 標售連續 14 次 tail，bid-to-cover 為 2022-09 以來最差；7Y tail 0.8bp（2026-07-28）（`monetary.treasury_auctions`）。10Y 期限溢價（term premium）0.8681%，trailing 7 日 +3bp（2026-07-31）（`monetary.term_premium`）。財政供給壓力是潛在的利率衝擊來源。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 3.83%（2026-08-05），R1 門檻水位 22995.45，還需再跌約 22.02%（`valuation.ndx_drawdown`）。
- [R2] hyperscaler 2026 capex 合計約 $725B，仍在上修，四家中下修家數為 0（2026-07-28）（`ai.hyperscaler_capex`）。
- [整體] 信用與資金市場平靜：HY OAS 2.73%、IG OAS 0.78%（2026-08-04）（`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）1bp，SOFR99−IORB 9bp（2026-08-04），SRF 動用 0.001bn（2026-08-05）（`monetary.repo_stress_srf`）。AI 單一名稱的重定價尚未外溢到整體信用市場。
- [R2] 算力需求仍然吃緊：HBM／DRAM 合約價續升，H200 租金約 $4.39/hr，缺口延續到 1H2027（2026-08-01）（`ai.compute_supply_demand`）。這與 capex 下修所需的「產能過剩」情境相反。
- [R1] 波動與避險需求回落：VIX 15.81（2026-08-05），7 日下跌 23.48%，comove=false（`structural.vix_spx_comove`）；MOVE 73.58（2026-08-05），較 2026-08-03 的 80.48 下降（`structural.treasury_basis_trade`）。
- [整體] 市場廣度健康，漲勢不只靠少數權值股：RSP 等權 YTD +14.26%，領先 SPY 的 +13.71%（2026-08-03）（`breadth.rsp_spy`）；約 64% 的成分股站上 50 日均線，A/D 線創新高（2026-08-03）（`breadth.advance_decline`）。
- [整體] 散戶情緒沒有到亢奮：Fear & Greed 約 58（2026-08-05）（`retail.fear_greed`），AAII 看空 42.1%（2026-07-30）（`retail.aaii`）；本週 microcap thematic moonshot 合格件數為 0（`speculation.microcap_moonshots`）。

## 與前期比較

前次結論：無前次預測（report-2026-08-03 為舊格式評分報告）

前次為舊格式六維評分報告，不換算成 yes/no，本次 flip_evidence 為空。相較 2026-08-03 的主要數據變化：NASDAQ-100 由 28776.8 回升至 29487.79；S&P 500 上漲 1.62%；10Y 殖利率 −7bp（ΔDFII10 −3bp、ΔT10YIE −5bp，兩者視窗不一致，判讀：不可判（視窗不一致））；HY OAS −5bp；MOVE 由 80.48 降至 73.58。AI 信用端則有 CoreWeave 利差走闊的報導（2026-08-03）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下 ✗ NOT DISCLOSED 來源是檢索完成但沒有合格披露，不作為證據：
- retail.naaim、institutional.bofa_jpm_survey、monetary.private_credit_liquidity、ai.token_growth、ai.depreciation_life、structural.global_leveraged_approvals：本次窗口內沒有披露。其中私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）的缺漏與 R3 最相關；若實際存在 gate proration / breach，會強化 R3／整體的 yes 證據，但目前沒有資料支持這個方向。
- ai.openai_anthropic_revenue：最新披露為 2026-06-15（Epoch），屬前一季，不是本季的新披露。依規則標示 ✗；其數值只作為 AI 營收對 capex 缺口的沿用組件。
- ai.hyperscaler_financing_mix：quarterly_state 有取得（top-5 capex 已超越 FCF，2026 發債約 $182B），但 30 日內的 event_scan 沒有找到新的融資事件，因此合併狀態為 ✗。
- ai.capital_cycle：兩個組件都沒有可引用的增速對比或進出場事件，增速證據不足，本次不判定資本週期階段。
- speculation.insider_form4：檢索到的 Form 4 相關結果沒有附上 filing-level 細節（個別 filing URL 與申報日），不符合引用標準，依規則記為 0 件，不列名、不列金額。

主要不確定性：
1. CoreWeave 的再融資路徑與負債規模：本次無法確認其負債是否達到 R3 門檻，也沒有取得到期時間表。若出現再融資失敗或 distressed exchange，R3 會直接觸發，並可能連帶引發 R1，會把答案推向 yes。
2. 下一輪（2026 Q3）hyperscaler 財報：日期本次未取得。若有兩家轉為下修，R2 成立；目前方向是上修，偏向 no。
3. 美債標售與期限溢價：若標售需求持續轉弱，演變成國債市場失序（Treasury market dysfunction），可能透過利率衝擊與 NBFI 去槓桿觸發 R1。目前 MOVE 與 repo 指標仍平靜，偏向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest | 7723.55 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | dev200_pct | 9.71 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | dev52w_pct | 11.32 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29487.79 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 3.83 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1 資料，%） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.73 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
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
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.001 | FRED API (series_id=RPONTTLD) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6738190.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5941248.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.81 | FRED API (series_id=VIXCLS) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 15.81 | FRED API (series_id=VIXCLS, SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | -23.48 | FRED API (series_id=VIXCLS, SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2004.9941（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-22 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7481041 | CFTC TFF futures-only | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.58 | Yahoo Finance chart API (^MOVE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2342.8 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | SSGA 市場評論 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報摘要 [primary: SEARCH]（90d＋同季） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導 [primary: SEARCH]（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | financecharts WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | P&I WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | StockCharts WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA via Advisor Perspectives WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | Reddit WSB／cashtag WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim.org／YCharts [primary: SEARCH] | ✗ NOT DISCLOSED（檢索完成，無當週數值） |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED（窗口內無新調查） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED DFEDTARU / DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（FRED BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（FRED BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（FRED DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（FRED T10YIE，FRED-direct） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（FRED DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED CPIAUCSL | scripts/fetch_macro.py（yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（FRED T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED THREEFYTP10 | scripts/fetch_macro.py | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | auction recap [primary: SEARCH]（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED WALCL | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | investing.com WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC／interval fund 披露 [primary: SEARCH]（30d） | ✗ NOT DISCLOSED（30 日內無合格披露） |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報／財經報導 WebSearch（stock-of-state，2026 Q2 財報季） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／報導 WebSearch | ✗ NOT DISCLOSED（最新為 2026-06-15，非本季披露） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話摘要 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | GPU 租金／記憶體價格 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：季報／Sage Advisory 摘要；event_scan：30d 發債／融資事件 WebSearch | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 [primary: SEARCH]（逐組件沿用） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K／10-Q／法說 [primary: SEARCH]（30d） | ✗ NOT DISCLOSED（30 日內無變動披露） |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | quarterly_state：供需增速披露；event_scan：30d 進出場事件 WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC / no-revenue IPO | Reuters／Benzinga／BusinessWire 7d 螢幕 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | Renaissance Capital WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／StockAnalysis／StockTitan gainers 螢幕（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | YCharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com／財經媒體 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF launch feed（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED（7 日內無英文披露） |
| structural.zero_dte | 結構｜0DTE option volume | Cboe 季報投影片 WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC monthly | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe insights WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（FRED VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 Retail margin debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | 融資報導 [primary: SEARCH]（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds／move_index／ofr_repo；WebSearch 補充事件 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok；WebSearch 無合格事件） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.74（原定來源 multpl.com） | S&P 500 trailing P/E August 5 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.19 | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 約 29x vs 指數約 25.6x，溢價壓縮（SSGA） | Magnificent 7 valuation premium lowest decade 2026 | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026 | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA TP $285→$288，EPS-driven；EPS Δ、target PE Δ 未披露 | Morgan Stanley NVDA target 288 July 2026 AI demand | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044 | 2026-07-13 | 2026-08-06T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 約 855bp、$2.6B 貸款利差 +125bp、Oracle CDS 約 215bp | CoreWeave CDS spread blows out 125 covenants Oracle August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD +14.26% vs SPY +13.71%（總報酬） | RSP vs SPY equal weight total return YTD August 2026 | https://www.financecharts.com/etfs/SPY/performance/total-return | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度約 41% | S&P 500 top 10 concentration percent record 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/ | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| breadth.advance_decline | 約 64% 成分股在 50DMA 上、A/D 創高、McClellan 轉負 | S&P 500 breadth percent above 50 day moving average August 2026 McClellan | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/ | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 58（Greed） | CNN Fear and Greed Index August 5 2026 | https://www.cnn.com/markets/fear-and-greed | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| retail.aaii | AAII Bear 42.1%／Neutral 26.9%／Bull 31.0% | AAII investor sentiment survey July 30 2026 | https://www.aaii.com/sentimentsurvey | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| retail.social_sentiment | WSB「Save Wendy's」（WEN）軋空話題，空頭比重約 44% | Reddit WSB Wendy's WEN short squeeze August 2026 | https://finance.yahoo.com/markets/stocks/articles/reddit-wants-save-wendy-inside-161925726.html | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.treasury_auctions | 5Y 連 14 次 tail、BTC 2022-09 以來最差；7Y tail 0.8bp | US Treasury 5 year 7 year auction tail bid to cover July 2026 | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026 | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| monetary.fedwatch | FOMC 7/29 鷹派持平；CME FedWatch 9 月約 62% 定價分歧 | CME FedWatch September 2026 probability FOMC hold | https://growbeansprout.com/tools/fedwatch | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.pboc | 人行 7/29–8/3 逆回購約 ¥2.1T；7/24 MLF 淨投放 ¥100B | PBoC reverse repo injection 2.1 trillion yuan late July 2026 | https://www.investing.com/news/economy-news/chinas-pboc-to-conduct-overnight-reverse-repos-inject-a-total-of-21-trillion-yuan-4810853 | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_capex | 2026 capex 合計約 $725B 續上修；Alphabet Q2 上修後遭賣壓（2026 Q2 財報季） | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO 約 $678B，約 32% 繫單一客戶（OpenAI） | Microsoft RPO backlog 678 billion single customer OpenAI 2026 | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/ | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| ai.compute_supply_demand | HBM／DRAM 合約續升、H200 租金約 $4.39/hr、缺口延至 1H2027 | H200 GPU rental price HBM DRAM contract 2026 shortage 2027 | https://jarvislabs.ai/blog/h200-price | 2026-08-01 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超越 FCF、2026 發債約 $182B、表外 SPV 結構逾 $120B（Sage Advisory 摘要） | hyperscaler capex FCF debt issuance 182 billion off balance sheet SPV 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.revenue_capex_gap | 分子：Anthropic 約 $47B＋OpenAI 約 $25B run-rate（沿用組件） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-06-15 | 2026-08-06T09:30:00+08:00 |
| ai.revenue_capex_gap | 分母：hyperscaler 年化 capex 合計約 $725B（沿用 ai.hyperscaler_capex 組件） | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／no-revenue IPO 合格件數 0 | AI rename ticker SPAC no revenue IPO July 30 August 6 2026 | 已檢查：Reuters、Benzinga、BusinessWire SPAC 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.ipo_heat | 本週約 21 檔跨週定價、無 blowout 首日、YTD 約 $251B／86 檔 | US IPO pricings week August 3 2026 Renaissance | https://www.renaissancecapital.com/IPO-Center/Pricings | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot 合格件數 0 | microcap 100% single day quantum fusion space nuclear small cap August 2026 | 已檢查：Finviz、StockAnalysis、StockTitan gainers 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標約 $1T IPO、Anthropic 續進 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 件數 0（檢索結果缺 filing-level URL／申報日，不合格） | Snowflake Dageville Tempus Lefkofsky Form 4 insider sale July 2026 SEC | 已檢查：SEC EDGAR Form 4 公司索引 | — | 2026-08-06T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.55（日讀數） | Cboe equity put call ratio August 3 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高約 $198B | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-07-23 | 2026-08-06T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x 單股槓桿 ETF＋ELOL（TSLA+SpaceX） | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量約 65%（Cboe Q2 2026） | 0DTE SPX options share volume Cboe Q2 2026 65% | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641 | 2026-05-31 | 2026-08-06T09:30:00+08:00 |
| structural.options_volume | OCC 總量（2026-06 月資料）16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 約 139.96、VIX 約 16.9 contango、TLT 1M skew 創 GFC 以來高 | VIX SKEW term structure bond volatility August 3 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt（2026-06 月資料）$1.502T、+51.5% YoY（交叉引用） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B Anthropic 掛鉤貸款調高收益率 | CoreWeave 2.6 billion loan Anthropic yield boosted July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Nebius $775M 擔保融資（2026-07-17，同篇報導） | CoreWeave 2.6 billion loan Anthropic yield boosted July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic | 2026-07-17 | 2026-08-06T09:30:00+08:00 |

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
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 3.83,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

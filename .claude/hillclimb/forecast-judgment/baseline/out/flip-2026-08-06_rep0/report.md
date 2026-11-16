> [DRY RUN] this report was not committed to archive.

# 2026-08-06 AI 泡沫破裂預測報告
報告日期：2026-08-06｜ISO 週次：2026-W32｜預測窗口：2026-08-06 → 2027-02-04｜前次基準：report-2026-08-03（3天前）

## 結論

**結論：no**

三條路徑在 182 天窗口內都還沒有已啟動的完成軌跡：NASDAQ-100 距 52 週高點回撤 3.83%（2026-08-05），須再跌約 22.02% 才觸及 R1；四家 hyperscaler 的 2026 capex 指引仍在上修，R2 尚無任何一家下修。前次判 yes 之後的新數據（NASDAQ-100 自 7 月底低點反彈、VIX 回落、HY OAS 收窄）顯示 7 月底 Alphabet capex 衝擊並未擴散成跨市場拋售。R3 最大風險 CoreWeave 雖然信用定價已達高壓水位，但在窗口內走到違約或 distressed exchange 的證據仍不足。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29487.79（2026-08-05），252 交易日最高收盤 30660.6（2026-06-02），距 52 週高點回撤 3.83%；R1 門檻水位為 22995.45，自最新收盤須再下跌約 22.02% 才會觸及（`valuation.ndx_drawdown`）。窗口內 7 月下旬曾有一段急跌：指數 2026-07-29 收在 27192.31，之後一週反彈約 8.4%。S&P 500 收 7723.55，高於 200 日均線 9.71%、高於 52 週均線 11.32%（2026-08-05，`valuation.sp500_trend`），價格延伸幅度大，均值回歸的下檔空間不小。估值處於歷史高檔：S&P 500 trailing P/E 29.74、Shiller CAPE 42.19（2026-08-05，`valuation.sp500_pe_cape`）；Top-10 集中度約 41%（`breadth.top10_concentration`）。另一方面，市場內部並沒有呈現擁擠的避險需求：VIX 由 20.66（2026-07-29）降到 15.81（2026-08-05），同期 S&P 500 上漲 5.57%，沒有同漲（`structural.vix_spx_comove`）。等權 RSP YTD +14.26% 領先 SPY +13.71%（`breadth.rsp_spy`），廣度並未只靠少數權值股支撐。

**判讀：** R1 距離門檻還很遠（還差約 22%）。要在窗口內觸發，需要一次 2022 年等級的科技股重估，通常要有信用事件（R3）或 capex 指引轉向（R2）當觸媒，或是利率／期限溢價急升。高 CAPE、margin debt 創高與價格延伸放大了下檔的幅度，但目前沒有已啟動的回撤軌跡。

### R2 資本支出收縮

最新可得資料（CNBC，2026-07-28，`ai.hyperscaler_capex`）顯示，Q2 財報季後 hyperscaler 2026 capex 仍在上修，合計約 $725B；Alphabet 上修 capex，並因此引發股價賣壓。本次證據沒有提供 Microsoft、Amazon、Meta 各自的指引數字，只有「續上修」的合計敘述。逐家方向：Microsoft 上修（依合計敘述，個別數字未取得）／Alphabet 上修／Amazon 上修（依合計敘述，個別數字未取得）／Meta 上修（依合計敘述，個別數字未取得）。目前四家都沒有下修，R2 需要的兩家下修是 0／4。下一輪財報的確切日期不在本次證據中；照季報節奏，窗口（至 2027-02-04）大致涵蓋兩輪季報。需求面的證據仍偏緊：HBM／DRAM 合約價續升，H200 租金約 $4.39/hr，供給缺口預計延到 1H2027（2026-08-01，`ai.compute_supply_demand`）；Microsoft RPO 約 $678B（2026-07-30，`ai.customer_concentration_rpo`）。

**判讀：** R2 是三條路徑裡最遠的一條。市場對 capex 上修的懲罰（Alphabet 賣壓）會給管理層壓力，但從「全面上修」翻到「兩家下修」，通常需要需求明顯轉弱或融資受阻。Microsoft RPO 約 32% 繫於單一客戶 OpenAI（`ai.customer_concentration_rpo`），是集中度上的脆弱點；如果 OpenAI 的支付能力出問題，可能是窗口內 R2 唯一可信的觸發路徑。

### R3 AI 信用事件

CoreWeave 是最符合 R3 規模門檻的 AI 基礎設施借款人。它的 5Y CDS 約 855bp，$2.6B 貸款利差擴大 125bp，貸方要求加入 covenants；Oracle CDS 約 215bp（2026-08-03，`valuation.ai_credit_schism`）。CoreWeave 於 2026-07-29 為一筆與 Anthropic 合約掛鉤的 $2.6B 貸款調高收益率才完成募集，Nebius 在 2026-07-17 有 $775M 的擔保融資（`structural.ai_infrastructure_debt`）。這說明 AI 信用定價分歧（equity-vs-credit schism）正在往信用端重定價的方向發展：借款成本與條款明顯收緊，但市場仍願意放款。本次證據沒有看到 missed payment、covenant waiver、distressed exchange 或 going-concern 字樣。整體信用市場平穩：HY OAS 2.73%、IG OAS 0.78%（2026-08-04，`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 1bp（2026-08-04，`monetary.repo_stress_srf`）。

**判讀：** R3 是三條路徑中最接近的一條：約 855bp 的 CDS 代表市場已為 CoreWeave 定出相當高的違約風險。不過 R3 要的是破產、超過寬限期的違約或完成 distressed exchange，而它仍能以較高成本再融資，因此 182 天內走完這條路徑的可能性仍低於一半。會把它推過門檻的情況包括：再融資市場關閉、主要客戶（OpenAI／Anthropic）的承諾縮減，或 covenant 觸發。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 約 855bp，$2.6B 貸款利差擴大 125bp，貸方要求 covenants（2026-08-03），AI 信用定價分歧開始往信用端重定價（`valuation.ai_credit_schism`）。
- [R3] CoreWeave 2026-07-29 須調高收益率才完成 $2.6B 的 Anthropic 掛鉤貸款，AI infrastructure debt financing 的成本正在上升（`structural.ai_infrastructure_debt`）。
- [整體] FINRA margin debt $1.502T，YoY +51.5%（2026-06 月資料，2026-07-20 發布），已到歷史頂部區間（YoY ≥ +40–50%）（`retail.margin_debt`）。
- [R1] Shiller CAPE 42.19、trailing P/E 29.74（2026-08-05），S&P 500 高於 200 日均線 9.71%（2026-08-05），估值與價格延伸都很極端（`valuation.sp500_pe_cape`、`valuation.sp500_trend`）。
- [整體] 美債標售需求轉弱：5Y 連續 14 次 tail，bid-to-cover 為 2022-09 以來最差，7Y tail 0.8bp（2026-07-28）；10Y 期限溢價（term premium）0.8681%，trailing 7 日 +3bp（2026-07-31）（`monetary.treasury_auctions`、`monetary.term_premium`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 $72B（Anthropic $47B＋OpenAI $25B，2026-06-15）對年化 capex 約 $725B（分母：top-4 hyperscaler 合計，2026-07-28），缺口約 10 倍（`ai.revenue_capex_gap`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 3.83%（2026-08-05），自最新收盤還要再跌約 22.02% 才到 R1 門檻 22995.45（`valuation.ndx_drawdown`）。
- [R2] hyperscaler 2026 capex 持續上修，合計約 $725B（2026-07-28），四家都沒有下修（`ai.hyperscaler_capex`）。
- [R2] AI 算力供不應求：HBM／DRAM 合約價續升，H200 租金約 $4.39/hr，缺口延到 1H2027（2026-08-01），需求端還沒有出現讓 capex 轉向的訊號（`ai.compute_supply_demand`）。
- [R3] 整體信用沒有擴散：HY OAS 2.73%（2026-08-04，較前次 −5bp），IG OAS 0.78%；repo 資金壓力（SOFR−IORB）1bp，SRF 動用 $0.001bn（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`）。
- [R1] VIX 由 20.66 降到 15.81，同期 S&P 500 上漲 5.57%（2026-07-29 → 2026-08-05），沒有 crowded-optionality 的同漲訊號；MOVE 由 80.48 降到 73.58（2026-08-05）（`structural.vix_spx_comove`、`structural.treasury_basis_trade`）。
- [整體] 散戶情緒沒有亢奮：AAII Bear 42.1% 高於 Bull 31.0%（2026-07-30），CNN Fear & Greed 約 58（2026-08-05）；本週 AI 改名／SPAC 合格件數與 microcap thematic moonshot 合格件數都是 0（`retail.aaii`、`retail.fear_greed`、`speculation.ai_rename_spac`、`speculation.microcap_moonshots`）。

## 與前期比較

前次結論：yes（report-2026-08-03）
本次結論：翻轉
翻轉依據：
- `valuation.ndx_drawdown`：前次存檔的 r1_drawdown_pct 為 7.78%（7 月底資料）；本次 2026-08-05 收盤後回撤縮小到 3.83%，達到 R1 門檻所需的跌幅從約 18.7% 擴大到約 22.02%。7 月下旬 Alphabet capex 衝擊引發的急跌（2026-07-29 低點 27192.31）已大致收復，R1 沒有正在進行的回撤軌跡。
- `structural.vix_spx_comove`：2026-08-05 的 VIX 15.81（7 日 −23.48%），S&P 500 同期 +5.57%，避險需求退潮，從股市急跌傳導到持續回撤的通道沒有成形。
- `monetary.hy_oas`：2026-08-04 HY OAS 2.73%，較前次 −5bp；CoreWeave 的信用重定價沒有擴散到整體高收益市場，R3 → R1 的傳導證據沒有增強。
- 說明：本次只讀得到前次的 forecast.json，讀不到前次的論述；上面以前次存檔數值（r1_drawdown_pct）和 2026-08-03 之後的新數據作為翻轉依據。CoreWeave 信用壓力（2026-08-03）不是新證據，本次仍列為最強的 yes 證據，但它單獨不足以撐起 yes。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源為 ✗ NOT DISCLOSED（檢索完成但沒有合格的當期披露），都不會單獨改變答案：NAAIM、BofA／JPM 調查、私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）、token growth、OpenAI／Anthropic 當季營收披露、hyperscaler 融資結構的 30 日事件掃描、折舊年限變動（depreciation useful-life change）、資本週期階段（capital cycle stage）、全球槓桿商品核准。其中私募信貸贖回壓力缺漏影響最大：如果出現 gate proration / breach 或 net inflow→outflow flip，會強化 R3 路徑，但本次沒有披露。內線交易掃描找到兩筆媒體報導的董事出售，但結果缺少 Form 4 申報日與個別申報 URL，依規則不列為具名證據。

最大的不確定性：
1. CoreWeave 再融資：CDS 約 855bp，如果下一筆再融資失敗或 covenant 觸發，R3（並經由 R3 帶動 R1）會快速逼近，答案會往 yes 移動。
2. 窗口內兩輪 hyperscaler 財報：只要有任一家開始下修 capex 指引，就會讓 R2 從 0／4 往門檻移動；目前需求證據偏緊，暫時往 no。
3. 美債供給與期限溢價：5Y 標售連續 tail、期限溢價上升；如果演變成國債市場失序（Treasury market dysfunction），高估值科技股的折現率衝擊可能推動 R1，答案會往 yes 移動。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest | 7723.55 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 9.71 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 11.32 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29487.79 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 3.83 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026-Q1） | 45.76080873390133（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.73 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_abs | -0.05 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.63 | FRED API (series_id=DGS10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.4 | FRED API (series_id=DFII10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.22 | FRED API (series_id=T10YIE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 81.96 | FRED API (series_id=DCOILWTICO) | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-08-06T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.26 | FRED API (series_id=T5YIFR) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest | 0.8681 | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.66 | FRED API (series_id=SOFR) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.74 | FRED API (series_id=SOFR99) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-08-06 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest | 0.001（十億美元） | FRED API (series_id=RPONTTLD) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,738,190（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,941,248（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,442,957（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.81 | FRED API (series_id=VIXCLS) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 15.81 | FRED API (series_id=VIXCLS, SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_base | 20.66 | FRED API (series_id=VIXCLS) | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | -23.48 | FRED API (series_id=VIXCLS) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | 5.57 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2004.9941（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-22 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7481041（口） | CFTC TFF futures-only | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.58 | Yahoo Finance chart API (^MOVE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index prior | 80.48 | Yahoo Finance chart API (^MOVE) | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2342.8（十億美元，transaction volume） | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |

註：10Y Δ 分解 ΔDGS10 −7bp、ΔDFII10 −3bp、ΔT10YIE −5bp；判讀為 不可判（視窗不一致），因為 T10YIE 的視窗與另兩腿不同。repo 資金壓力：SOFR−IORB 1bp、SOFR99−IORB 9bp（兩者 as_of 2026-08-04）；SRF 動用 $0.001bn 的日期是 2026-08-05，與利差日期不同。WALCL、DCOILWTICO、ECBASSETSW、JPNASSETS、LNFACBW027SBOG 自前次以來沒有新觀測（持平）。

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | SSGA [SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方 TP 上修掃描（90d＋同季）[primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 14 日信用市場掃描 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | financecharts [SEARCH] | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | P&I [SEARCH] | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | StockCharts [SEARCH] | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | Advisor Perspectives／FINRA [SEARCH] | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag [SEARCH] | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py BOGZ1FL153064486Q | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／YCharts [primary: SEARCH] | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 [SEARCH] | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py BAMLH0A0HYM2 | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py BAMLC0A0CM | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py DGS10 | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py DFII10 | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py T10YIE（FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py DCOILWTICO | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py CPIAUCSL yoy_pct | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py T5YIFR | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py THREEFYTP10 | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | 14 日標售回顧 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py WALCL | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py ECBASSETSW＋JPNASSETS | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | investing.com [SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | 30 日 BDC 披露掃描 [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報／CNBC [SEARCH] | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 [SEARCH] | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | 報導／Epoch [SEARCH]；僅找到前季（2026-06-15）資料 | ✗ NOT DISCLOSED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話／報導 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce／jarvislabs [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：Sage Advisory 季頻狀態；event_scan：30 日發債／融資掃描 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 carry-forward [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 30 日 10-K／10-Q 掃描 [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | quarterly_state：供需增速；event_scan：30 日進出場事件 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | 7 日螢幕 [SEARCH] | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | Renaissance Capital [SEARCH] | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／StockAnalysis／StockTitan [primary: SEARCH] | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 [SEARCH] | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 [primary: SEC EDGAR] | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | YCharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing／etf.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF 發行 [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA 7 日 [SEARCH] | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC monthly volume report | theocc.com [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe insights [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py VIXCLS＋vix_spx_comove | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用散戶 margin debt [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | 30 日融資掃描 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py LNFACBW027SBOG | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds／move_index／ofr_repo；WebSearch 補充無新披露 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.74 | S&P 500 trailing P/E August 5 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.19 | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 約 29x vs 指數約 25.6x，對指數的溢價壓縮 | Magnificent 7 valuation premium lowest decade 2026 | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026 （SSGA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標價 $285→$288，EPS-driven（EPS 修正主導；EPS／PE Δ 細項未披露） | Morgan Stanley NVDA target 288 July 2026 AI demand | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044 （Investing.com） | 2026-07-13 | 2026-08-06T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 約 855bp、$2.6B 貸款利差 +125bp、貸方要求 covenants；Oracle CDS 約 215bp | CoreWeave CDS spread blows out 125 covenants Oracle August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm （Tech Times） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.rsp_spy | RSP 總報酬 YTD +14.26% vs SPY +13.71% | RSP vs SPY equal weight total return YTD August 2026 | https://www.financecharts.com/etfs/SPY/performance/total-return （FinanceCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度約 41% | S&P 500 top 10 concentration percent record 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/ （P&I） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| breadth.advance_decline | 約 64% 成分股在 50DMA 之上、A/D 線創高、McClellan 轉負 | S&P 500 breadth percent above 50 day moving average August 2026 McClellan | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/ （StockCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 58（Greed） | CNN Fear and Greed Index August 5 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| retail.aaii | AAII Bear 42.1%／Neutral 26.9%／Bull 31.0% | AAII investor sentiment survey July 30 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| retail.social_sentiment | WSB「Save Wendy's」（WEN）軋空，空頭比重約 44%（非 AI 主題） | Reddit WSB Wendy's WEN short squeeze August 2026 | https://finance.yahoo.com/markets/stocks/articles/reddit-wants-save-wendy-inside-161925726.html （Yahoo Finance） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.treasury_auctions | 5Y 連續 14 次 tail、bid-to-cover 為 2022-09 以來最差；7Y tail 0.8bp | US Treasury 5 year 7 year auction tail bid to cover July 2026 | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026 （TFTC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| monetary.fedwatch | FOMC 7/29 鷹派按兵不動；CME FedWatch 9 月定價約 62%，市場分歧 | CME FedWatch September 2026 probability FOMC hold | https://growbeansprout.com/tools/fedwatch （Beansprout／CME FedWatch） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.pboc | 人行 7/29–8/3 逆回購約 ¥2.1T；7/24 MLF 淨投放 ¥100B | PBoC reverse repo injection 2.1 trillion yuan late July 2026 | https://www.investing.com/news/economy-news/chinas-pboc-to-conduct-overnight-reverse-repos-inject-a-total-of-21-trillion-yuan-4810853 （Investing.com） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_capex | 2026 capex 續上修，合計約 $725B；Alphabet 上修並引發賣壓（Q2 2026 財報季） | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO 約 $678B，約 32% 繫於單一客戶（OpenAI） | Microsoft RPO backlog 678 billion single customer OpenAI 2026 | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/ （Benzinga via TradingView） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| ai.compute_supply_demand | HBM／DRAM 合約價續升、H200 租金約 $4.39/hr、缺口延至 1H2027 | H200 GPU rental price HBM DRAM contract 2026 shortage 2027 | https://jarvislabs.ai/blog/h200-price （Jarvislabs） | 2026-08-01 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超越 FCF；2026 發債約 $182B | hyperscaler capex FCF debt issuance 182 billion 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure （Sage Advisory） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $72B（Anthropic 約 $47B＋OpenAI 約 $25B，carry-forward）vs 年化 capex 約 $725B（分母：top-4 hyperscaler） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI）；分母取自 ai.hyperscaler_capex（CNBC 2026-07-28） | 2026-06-15 | 2026-08-06T09:30:00+08:00 |
| speculation.ai_rename_spac | AI 改名／SPAC／無營收投機 IPO：0 件合格 | AI rename ticker SPAC no revenue IPO July 30 August 6 2026 | Reuters／Benzinga／BusinessWire SPAC 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.ipo_heat | 本週約 21 檔跨週定價、沒有 blowout 首日、YTD 約 $251B／86 檔 | US IPO pricings week August 3 2026 Renaissance | https://www.renaissancecapital.com/IPO-Center/Pricings （Renaissance Capital） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot：0 件合格 | microcap 100% single day quantum fusion space nuclear small cap August 2026 | Finviz／StockAnalysis／StockTitan gainers 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標約 $1T IPO、Anthropic 持續推進 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground （Benzinga） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| speculation.insider_form4 | 14 日 Form 4 掃描：0 件具完整申報細節（申報日＋個別申報 URL）的合格交易 | Form 4 insider sale July 2026 SEC AI leadership | SEC EDGAR browse-edgar Form 4 清單；媒體報導 | — | 2026-08-06T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.55（日讀數／5 日均值未標明） | Cboe equity put call ratio August 3 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio （YCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高，約 $198B | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing） | 2026-07-23 | 2026-08-06T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 發行 6 檔 2x 單股槓桿 ETF 與 ELOL（TSLA＋SpaceX） | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權成交量約 65%（Cboe Q2 2026） | 0DTE SPX options share volume Cboe Q2 2026 65% | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641 （Investing.com） | 2026-05-31 | 2026-08-06T09:30:00+08:00 |
| structural.options_volume | OCC 總量（2026-06 月資料）16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 約 139.96、VIX 約 16.9 contango、債市波動轉升（TLT 1M skew 創 GFC 以來高） | VIX SKEW term structure bond volatility August 3 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher （Cboe） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt（2026-06 月資料）$1.502T、+51.5% YoY（交叉確認，不重複計算） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B Anthropic 掛鉤貸款調高收益率（2026-07-29）；Nebius $775M 擔保融資（2026-07-17） | CoreWeave 2.6 billion loan Anthropic yield boosted July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic （Bloomberg） | 2026-07-29 | 2026-08-06T09:30:00+08:00 |

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
  "flip_evidence": ["valuation.ndx_drawdown", "structural.vix_spx_comove", "monetary.hy_oas"],
  "r1_drawdown_pct": 3.83,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

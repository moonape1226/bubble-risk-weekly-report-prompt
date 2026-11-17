> [DRY RUN] this report was not committed to archive.

# 2026-08-06 AI 泡沫破裂預測報告

報告日期：2026-08-06｜ISO 週次：2026-W32｜預測窗口：2026-08-06 → 2027-02-04｜前次基準：report-2026-08-03（3天前）

## 結論

**結論：no**

三條路徑目前都沒有走到可在 182 天內完成的位置：NASDAQ-100 距 52 週高點回撤 3.83%，離 R1 門檻還需再跌約 22%（`valuation.ndx_drawdown`）；四家 hyperscaler 仍在上修 2026 capex，沒有任何一家下修（`ai.hyperscaler_capex`）。CoreWeave 的信用重定價（5Y CDS ≈855bp、貸款利差 +125bp）是最強的 yes 側訊號，但仍屬重定價，不是違約或 distressed exchange（`valuation.ai_credit_schism`），不足以推翻 base rate。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 於 2026-08-05 收在 29487.79；252 個交易日內最高收盤為 30660.6（2026-06-02），距 52 週高點回撤 3.83%。R1 門檻水位為 22995.45，需自最新收盤再下跌約 22.02% 才會觸發（`valuation.ndx_drawdown`）。指數在 2026-07-29 一度跌到 27192.31，之後一週反彈超過 8%；S&P 500 收 7723.55，比 200 日均線高 9.71%、比 52 週均線高 11.32%（`valuation.sp500_trend`）。估值仍然很高：S&P 500 trailing P/E 29.74、Shiller CAPE 42.19（`valuation.sp500_pe_cape`）；FINRA 6 月 margin debt $1.502T，YoY +51.5%（`retail.margin_debt`），已達歷史上 1999／2007／2021 頂部附近常見的 +40–50% 區間。這些都說明一旦下跌，跌幅可能很大，但它們本身不是觸發事件。波動面相當平靜：VIX 15.81，MOVE 73.58（`structural.vix_spx_comove`、`structural.treasury_basis_trade`）。

**判讀：** 距離門檻還很遠（還要再跌約 22%）。要在窗口內觸發 R1，需要一個外部催化劑：R3 型信用事件、R2 型 capex 下修，或利率／期限溢價急升造成的強制去槓桿。目前這三者都還沒有發生。

### R2 資本支出收縮

CNBC 2026-07-28 報導，hyperscaler 在 Q2 2026 財報季繼續上修 2026 capex，合計約 $725B；Alphabet 上修後股價遭賣壓（`ai.hyperscaler_capex`）。各家的方向如下：Alphabet 上修；Microsoft、Amazon、Meta 本次證據只有「整體續上修」的彙總敘述，沒有逐家列出指引數字，但沒有任何一家被報導下修。目前四家中下修家數為 0（R2 需要 2 家）。窗口（到 2027-02-04）涵蓋下兩輪季報週期，確切財報日期本次未取得。需求面仍然吃緊：HBM／DRAM 合約價續漲，H200 租金約 $4.39/hr，供給缺口預期延續到 1H2027（`ai.compute_supply_demand`）。這不支持短期內 capex 被砍。反方向的壓力來自 AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 $72B（Anthropic ≈$47B＋OpenAI ≈$25B，Epoch 2026-06-15），對比年化 capex 約 $725B（分母：CNBC 報導的 hyperscaler 2026 合計，公司集合依該報導，本次未逐家拆分）（`ai.revenue_capex_gap`）。另一個壓力是 Microsoft RPO 約 $678B，其中約 32% 繫於單一客戶 OpenAI，屬 backlog 重複計算風險（RPO double-counting）的集中度面向（`ai.customer_concentration_rpo`）。

**判讀：** 方向與 R2 相反，capex 仍在上修。要在窗口內觸發 R2，需要兩家在下兩輪財報中轉為下修。觸發來源可能是 Alphabet 那種股價懲罰擴大、AI 客戶（OpenAI）付款能力出問題，或融資成本急升。目前證據還看不到轉折。

### R3 AI 信用事件

最接近 R3 的是 CoreWeave（AI 算力為主業；負債規模本次證據未載明）。它的 5Y CDS 約 855bp，一筆 $2.6B 貸款利差擴大 125bp，貸款投資人要求加入 covenants；同一報導中 Oracle CDS 約 215bp（TechTimes 2026-08-03，`valuation.ai_credit_schism`）。Bloomberg 2026-07-29 報導 CoreWeave 為一筆與 Anthropic 掛鉤的 $2.6B 貸款調高票息；Nebius 於 2026-07-17 取得 $775M 擔保融資（`structural.ai_infrastructure_debt`）。這屬於 AI 信用定價分歧（equity-vs-credit schism）中「信貸端開始重定價」的後期訊號。不過證據裡沒有付款違約、寬限期、covenant waiver、distressed exchange 或 going-concern 的字眼，而且 CoreWeave 仍能在市場上完成融資，只是價格更高。整體信用市場仍然很緊：HY OAS 2.73%、IG OAS 0.78%（`monetary.hy_oas`、`monetary.ig_oas`）。repo 資金壓力（SOFR−IORB）只有 1bp，SRF 動用（Standing Repo Facility usage）為 $0.001bn（`monetary.repo_stress_srf`）。

**判讀：** 有局部重定價，但離違約還遠。要在窗口內觸發 R3，CoreWeave 這類借款人必須在融資管道收窄後發生付款違約或完成 distressed exchange。目前它仍能以更高票息再融資，近期到期牆本次證據未載明。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 約 855bp、$2.6B 貸款利差擴大 125bp，投資人要求加 covenants；Oracle CDS 約 215bp（2026-08-03）。AI 借款人的信貸端已開始重定價，股價卻剛反彈到距高點只差 3.83%，equity-vs-credit 分歧正在擴大 `valuation.ai_credit_schism`
- [R3] CoreWeave 於 2026-07-29 為一筆與 Anthropic 掛鉤的 $2.6B 貸款調高票息，AI infrastructure debt financing / vendor-financing loops 的融資成本正在上升 `structural.ai_infrastructure_debt`
- [R2] 年化 AI 終端營收約 $72B（Epoch 2026-06-15），對比 hyperscaler 2026 合計 capex 約 $725B；Microsoft RPO 約 $678B，其中約 32% 繫於 OpenAI（2026-07-30）。回本缺口大、客戶集中，一旦 OpenAI 端出問題，capex 會被迫重估 `ai.revenue_capex_gap` `ai.customer_concentration_rpo`
- [R1] 估值與槓桿處於極端水位：CAPE 42.19、trailing P/E 29.74（2026-08-05）；margin debt $1.502T、YoY +51.5%（2026-06 月資料）。下跌一旦開始，可能被強制去槓桿放大 `valuation.sp500_pe_cape` `retail.margin_debt`
- [整體] 財政／利率端有壓力：5Y 標售連續 14 次 tail、bid-to-cover 為 2022-09 以來最差，7Y tail 0.8bp（2026-07-28）；10Y 期限溢價（term premium）0.8681%（2026-07-31，7 日 +3bp）；TLT 1M skew 創 GFC 以來新高（2026-08-03）。長端利率若上衝，是高估值資產的潛在催化劑 `monetary.treasury_auctions` `monetary.term_premium` `structural.cross_asset_derivatives`

## 支持 no 的證據

- [R1] NASDAQ-100 最新收盤 29487.79（2026-08-05），距 52 週高點回撤 3.83%，比前次的 7.78% 更小；距 R1 門檻 22995.45 還需再跌約 22.02%。S&P 500 高於 200 日均線 9.71% `valuation.ndx_drawdown` `valuation.sp500_trend`
- [R2] hyperscaler 2026 capex 合計約 $725B，仍在上修（2026-07-28），四家中下修 0 家；HBM／DRAM 合約價續漲、H200 租金約 $4.39/hr、供給缺口延到 1H2027（2026-08-01），需求端還沒有出現 digestion `ai.hyperscaler_capex` `ai.compute_supply_demand`
- [R3] 廣義信用與資金市場平穩：HY OAS 2.73%、IG OAS 0.78%（2026-08-04）；SOFR−IORB 1bp、SOFR99−IORB 9bp（2026-08-04）；SRF 動用 $0.001bn（2026-08-05）。CoreWeave 的重定價沒有外溢成系統性信用緊縮 `monetary.hy_oas` `monetary.ig_oas` `monetary.repo_stress_srf`
- [整體] 波動與部位沒有顯示失序：VIX 15.81（2026-08-05），7 日 −23.48%，同期 S&P 500 +5.57%，未出現 co-movement；MOVE 73.58（前次 80.48）；槓桿基金美債期貨淨部位 −7481041 口（2026-07-28），4 週變動 −52919 口，沒有平倉跡象 `structural.vix_spx_comove` `structural.treasury_basis_trade`
- [整體] 市場廣度在擴散，不是收斂：RSP 等權 YTD +14.26%，領先 SPY +13.71%；A/D 線創高（2026-08-03）。情緒未達極端：CNN Fear & Greed 約 58（2026-08-05），AAII bear 42.1%（2026-07-30） `breadth.rsp_spy` `breadth.advance_decline` `retail.fear_greed` `retail.aaii`

## 與前期比較

前次結論：yes（report-2026-08-03）

本次結論：翻轉

翻轉依據：

- 前次 forecast.json 沒有記錄 yes_basis，沒有具名的決定性理由需要逐項延續。依規則，yes 必須每次重新證成；本次以目前證據重新檢視，結果不足以支撐 yes。
- R1：前次 r1_drawdown_pct 為 7.78，本次 NASDAQ-100 回撤收斂到 3.83%（2026-08-05），距門檻還需再跌約 22.02%。市場回撤路徑比前次更遠 `valuation.ndx_drawdown`
- R2：hyperscaler 2026 capex 仍在上修（合計約 $725B，2026-07-28），四家下修 0 家，R2 路徑與觸發方向相反 `ai.hyperscaler_capex`
- R3：CoreWeave 5Y CDS 約 855bp、貸款利差 +125bp（2026-08-03）是真實的重定價，但沒有違約、寬限期或 distressed exchange，且 CoreWeave 仍能完成再融資。重定價不等於 182 天內會完成 R3 事件 `valuation.ai_credit_schism`

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源已完成搜尋，但沒有窗口內的合格披露（✗ NOT DISCLOSED）：NAAIM、BofA／JPM 調查、私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）、AI token 成長、OpenAI／Anthropic 本季營收披露、hyperscaler 融資結構（capex vs FCF / 發債）的 30 日事件掃描、折舊年限變動（depreciation useful-life change）、資本週期階段（capital cycle stage）兩個組件、全球槓桿產品核准。其中可能影響答案的是私募信貸贖回壓力與 hyperscaler 融資結構事件掃描：若在 30 日內出現 gate proration / breach 或 net inflow→outflow flip，或出現大型表外融資的違約條款，就會把 R3 推近。目前沒有披露，所以不改變答案。Insider Form 4 篩選有 2 筆候選，但都缺 filing-level 細節（EDGAR filing URL／申報日），依規則以 0 件處理、不具名。

最大的不確定性：

1. **CoreWeave 的再融資能力。** 5Y CDS 約 855bp，代表市場已在定價顯著的信用風險。如果下一筆融資失敗，或發生 covenant 違反，R3 與 R1 可能同時被推近，答案會往 yes 移動。近期到期牆本次未取得。
2. **下兩輪 hyperscaler 財報。** Alphabet 上修 capex 後遭賣壓，顯示市場開始懲罰 capex。如果股價壓力迫使兩家轉為下修，R2 就會觸發，答案往 yes 移動；如果需求缺口延續到 1H2027，則支持 no。
3. **長端利率與財政供給。** 5Y 標售連續 tail、期限溢價走升、TLT skew 創高。若出現國債市場失序（Treasury market dysfunction）並迫使美債基差交易槓桿（Treasury basis-trade leverage）平倉，可能成為 R1 的催化劑，答案往 yes 移動。目前 MOVE 下降、repo 平穩，暫不支持這個情境。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7723.55 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 9.71 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29487.79 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 3.83 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1） | 45.76080873390133（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-06T09:30:00+08:00 |
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
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（base 2026-07-29） | -23.48 | FRED API (series_id=VIXCLS, SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2004.9941（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-22 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7481041 | CFTC TFF futures-only | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.58 | Yahoo Finance chart API (^MOVE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2342.8 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |

10Y 分解（script `decomposition`）：ΔDGS10 −7bp、ΔDFII10 −3bp、ΔT10YIE −5bp；判讀：不可判（視窗不一致）。repo_stress（as_of 2026-08-04，iorb_date 2026-08-04，sofr99_iorb_date 2026-08-04）：SOFR−IORB 1bp、SOFR99−IORB 9bp；SRF 日期 2026-08-05。

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation｜Mag 7 weighted P/E and AI leader P/S | SSGA 等 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation｜Analyst TP upgrade decomposition | 賣方 TP 調升 WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | Valuation｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | financecharts WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth｜Top-10 concentration in S&P 500 | P&I WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth｜Advance/decline ratio, new high/low ratio | StockCharts WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment｜Margin Debt: FINRA | FINRA／Advisor Perspectives WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment｜Retail survey: AAII | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment｜Social sentiment proxies | Reddit WSB／cashtag WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment｜NAAIM Exposure Index | naaim／YCharts [primary: SEARCH] | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment｜BofA Fund Manager Survey and JPM | 賣方調查 WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit｜Fed funds rate: FRED | scripts/fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit｜CPI YoY: FRED | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit｜10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit｜美債標售需求（auction tail / bid-to-cover） | 標售 recap WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit｜Fed funds rate path expectations | CME FedWatch 摘要 WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit｜Fed balance sheet: FRED | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit｜Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit｜PBoC aggregate financing | investing.com WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit｜Private-credit / non-bank fund liquidity stress | BDC／interval fund 披露 WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals｜Hyperscaler capex guidance | 季報／CNBC WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals｜OpenAI / Anthropic annualized revenue | Epoch／報導 WebSearch（僅 2026-06-15 前季資料，無本季披露） | ✗ NOT DISCLOSED |
| ai.customer_concentration_rpo | AI Fundamentals｜Hyperscaler AI customer concentration | 財報電話 WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals｜AI compute supply/demand and overcapacity risk | TrendForce／jarvislabs WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報／發債 WebSearch；quarterly_state carry＋30d event_scan | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 WebSearch（carry-forward） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals｜GPU / 伺服器折舊年限變動 | 10-K／10-Q WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals｜資本週期階段（capital cycle stage） | 供需增速＋進出場事件 WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior｜Search for past 7 days: AI rename / SPAC | Reuters／Benzinga／BusinessWire WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior｜IPO market heat | Renaissance Capital WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior｜Microcap thematic moonshots | Finviz／StockAnalysis／StockTitan gainers 螢幕（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior｜Upcoming AI IPOs | 具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 篩選（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior｜Cboe equity-only put/call ratio | YCharts WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage｜US leveraged ETF AUM | etf.com／cryptobriefing WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF 發行 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | Structural Leverage｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage｜0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage｜Options total volume | OCC 月報 WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage｜Cross-asset derivatives / correlation checks | Cboe insights WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage｜Cross-reference only: FINRA margin debt | Advisor Perspectives WebSearch（交叉引用） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage｜AI infrastructure debt financing / vendor-financing loops | Bloomberg 等 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）；WebSearch 無新增 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.74 | S&P 500 trailing P/E August 5 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio（multpl；原定 multpl/gurufocus） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.19 | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 ≈29x vs 指數 ≈25.6x，溢價壓縮 | Magnificent 7 valuation premium lowest decade 2026 | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026（SSGA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA TP $285→$288，EPS-driven | Morgan Stanley NVDA target 288 July 2026 AI demand | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044（Investing.com） | 2026-07-13 | 2026-08-06T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS ≈855bp、$2.6B 貸款利差 +125bp、Oracle CDS ≈215bp | CoreWeave CDS spread blows out 125 covenants Oracle August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm（TechTimes） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD +14.26% vs SPY +13.71% | RSP vs SPY equal weight total return YTD August 2026 | https://www.financecharts.com/etfs/SPY/performance/total-return（FinanceCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 ≈41% | S&P 500 top 10 concentration percent record 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/（P&I） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| breadth.advance_decline | ≈64% 成分股在 50DMA 上、A/D 創高、McClellan 轉負 | S&P 500 breadth percent above 50 day moving average August 2026 McClellan | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/（StockCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed ≈58（Greed） | CNN Fear and Greed Index August 5 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives；原定 FINRA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| retail.aaii | AAII Bear 42.1%／Neutral 26.9%／Bull 31.0% | AAII investor sentiment survey July 30 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| retail.social_sentiment | WSB「Save Wendy's」（WEN）軋空，≈44% 空頭 | Reddit WSB Wendy's WEN short squeeze August 2026 | https://finance.yahoo.com/markets/stocks/articles/reddit-wants-save-wendy-inside-161925726.html（Yahoo Finance） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.treasury_auctions | 5Y 連 14 次 tail、BTC 2022-09 以來最差；7Y tail 0.8bp | US Treasury 5 year 7 year auction tail bid to cover July 2026 | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026（TFTC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| monetary.fedwatch | FOMC 7/29 鷹派持平；FedWatch 9 月 ≈62%，定價分歧 | CME FedWatch September 2026 probability FOMC hold | https://growbeansprout.com/tools/fedwatch（Beansprout，原定 CME FedWatch） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.pboc | 人行宣布 7/29–8/3 逆回購合計 ≈¥2.1T；7/24 MLF 淨投放 ¥100B | PBoC reverse repo injection 2.1 trillion yuan late July 2026 | https://www.investing.com/news/economy-news/chinas-pboc-to-conduct-overnight-reverse-repos-inject-a-total-of-21-trillion-yuan-4810853（Investing.com） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 續上修，合計 ≈$725B；Alphabet 上修觸發賣壓（Q2 2026 財報季） | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO ≈$678B，≈32% 繫於 OpenAI | Microsoft RPO backlog 678 billion single customer OpenAI 2026 | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/（Benzinga via TradingView） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| ai.compute_supply_demand | HBM/DRAM 合約續升、H200 租金 ≈$4.39/hr、缺口延至 1H2027 | H200 GPU rental price HBM DRAM contract 2026 shortage 2027 | https://jarvislabs.ai/blog/h200-price（JarvisLabs） | 2026-08-01 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超越 FCF、2026 發債 ≈$182B、>$120B 表外 SPV 結構（季頻狀態，carry） | hyperscaler capex FCF debt issuance 182 billion off balance sheet SPV 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure（Sage Advisory） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 ≈$72B（Anthropic $47B＋OpenAI $25B，carry-forward 2026-06-15） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-06-15 | 2026-08-06T09:30:00+08:00 |
| ai.revenue_capex_gap | 分母：hyperscaler 2026 合計 capex ≈$725B | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收 IPO 合格 0 件 | AI rename ticker SPAC no revenue IPO July 30 August 6 2026 | Reuters／Benzinga／BusinessWire SPAC 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.ipo_heat | ≈21 檔跨週定價、無 blowout 首日、YTD ≈$251B／86 檔 | US IPO pricings week August 3 2026 Renaissance | https://www.renaissancecapital.com/IPO-Center/Pricings（Renaissance Capital） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot 合格 0 件 | microcap 100% single day quantum fusion space nuclear small cap August 2026 | Finviz／StockAnalysis／StockTitan gainers 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 ≈$1T IPO、Anthropic 續進 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground（Benzinga） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| speculation.insider_form4 | 合格 Form 4 叢集 0 件（2 筆候選缺 filing-level URL／申報日，不具名） | Snowflake Dageville Tempus Lefkofsky Form 4 insider sale July 2026 SEC | SEC EDGAR browse-edgar 公司列表 | — | 2026-08-06T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.55（日讀數） | Cboe equity put call ratio August 3 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio（YCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高 ≈$198B | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing；原定 etf.com） | 2026-07-23 | 2026-08-06T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x 單股槓桿 ETF＋ELOL（TSLA+SpaceX）發行 | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html（GlobeNewswire） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量 ≈65%（Cboe Q2 2026 slides） | 0DTE SPX options share volume Cboe Q2 2026 65% | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641（Investing.com） | 2026-05-31 | 2026-08-06T09:30:00+08:00 |
| structural.options_volume | OCC 總量（2026-06 月資料）16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW ≈139.96、VIX ≈16.9 contango、TLT 1M skew 創 GFC 以來高 | VIX SKEW term structure bond volatility August 3 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher（Cboe） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-06 月資料）$1.502T、+51.5% YoY（交叉引用） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B Anthropic 掛鉤貸款調高票息（07-29）；Nebius $775M 擔保融資（07-17） | CoreWeave 2.6 billion loan Anthropic yield boosted July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic（Bloomberg） | 2026-07-29 | 2026-08-06T09:30:00+08:00 |

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
  "flip_evidence": ["valuation.ndx_drawdown", "ai.hyperscaler_capex", "valuation.ai_credit_schism"],
  "yes_basis": [],
  "r1_drawdown_pct": 3.83,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

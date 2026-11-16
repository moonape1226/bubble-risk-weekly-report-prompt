> [DRY RUN] this report was not committed to archive.

# 2026-07-27 AI 泡沫破裂預測報告

報告日期：2026-07-27｜ISO 週次：2026-W31｜預測窗口：2026-07-27 → 2027-01-25｜前次基準：report-2026-07-23（4天前）

## 結論

**結論：no**

三條路徑目前都沒有進入完成段：NASDAQ-100 距 52 週高點回撤 8.26%，距 R1 門檻仍需再跌約 18.25%；hyperscaler capex 指引仍在上修（Alphabet 2026 capex 上修至約 $195–205B），沒有任何一家下修。信用端雖有 AI 發行人利差走闊與 BCRED gate proration / breach 等早期壓力，但 HY OAS 僅 2.77%，R3 規模的 AI 借款人沒有違約或 distressed exchange 跡象，不足以推翻「182 天內三條件皆不成立」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 28,128.34（2026-07-24），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 8.26%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45；自最新收盤還需再下跌約 5,132.89 點、約 18.25% 才會觸發。背景：S&P 500 收 7,411.98（2026-07-24），高於 200 日均線 5.8%、高於 52 週均線 7.4%（`valuation.sp500_trend`），價格延伸幅度溫和；VIX 18.58（2026-07-24），近 7 日 VIX −1.01%、S&P 500 −0.61%，沒有出現股價與波動率同漲的 crowded-optionality 讀數（`structural.vix_spx_comove`）。估值仍高：S&P 500 trailing P/E 28.52、Shiller CAPE 40.46（2026-07-24，`valuation.sp500_pe_cape`），代表一旦有催化劑，下跌空間大。情緒面已偏謹慎：CNN Fear & Greed 39（Fear，2026-07-24，`retail.fear_greed`）、AAII Bear 42.3% 對 Bull 29.6%（2026-07-23，`retail.aaii`）。

**判讀：** 指數已自 6 月高點回落 8.26%，但距 25% 門檻仍有約 18 個百分點；要在窗口內觸發，需要一個信用或盈餘催化劑（例如 hyperscaler 下修 capex、AI 借款人信用事件、或 Fed 升息引發的估值壓縮）疊加高槓桿（margin debt YoY +51.5%）被迫去槓桿。目前沒有這種催化劑正在發生的證據。

### R2 資本支出收縮

- Alphabet：2026 年 capex 指引上修至約 $195–205B（2026-07-22 Q2 財報），方向：上修（`ai.hyperscaler_capex`）。
- Microsoft、Amazon、Meta：本次證據只取得四大 hyperscaler 2026 capex 合計約 $725B+（2026-07-22，`ai.hyperscaler_capex`），沒有逐家最新指引數字，各家方向本次未取得；本次證據中沒有任何一家的下修披露。
- 目前已知下修家數：0／4（需 2／4 才觸發 R2）。下一次財報日期本次證據未提供；182 天窗口一般涵蓋至少兩輪季報，是 R2 唯一的觸發時點。
- 配套：伺服器 DRAM 3Q26 合約價 +13–18% QoQ、交期 30–40+ 週（2026-07-03，`ai.compute_supply_demand`），顯示供給仍緊、需求未消化；Alphabet Q2 FCF 轉負（−$5.9B，2026-07-22，`ai.hyperscaler_financing_mix`），capex 已超過 FCF，hyperscaler 融資結構（capex vs FCF / 發債）轉向舉債。

**判讀：** R2 離觸發最遠——最新一次指引方向是上修，且算力供給仍緊。要在窗口內成立，需在下一兩輪季報中有兩家公司主動下修，通常要先有 AI 營收不及預期或融資成本急升（例如 FCF 轉負後債市胃納轉弱）。目前看不到這種轉向。

### R3 AI 信用事件

- 符合規模的借款人（負債 ≥ USD 5bn、AI 資料中心／算力為主業）：CoreWeave 有 GPU 擔保債務約 $24.9B（2026-07-12，`structural.ai_infrastructure_debt`）；同一來源另列 Broadcom／Anthropic 約 $35B、Oracle 約 $38B＋密州約 $16.3B 的 AI 資料中心融資（Oracle 主業非 AI 算力，不屬 R3 借款人類別，只作為傳導背景）。
- 信用定價：AI 單一發行人利差走闊，而 CDX IG 平穩，hyperscaler 2026 發債約 $182B（2026-07-16，`valuation.ai_credit_schism`）——AI 信用定價分歧（equity-vs-credit schism）開始朝信用端重定價。整體信用仍緊：HY OAS 2.77%、IG OAS 0.79%（2026-07-23，`monetary.hy_oas`、`monetary.ig_oas`）。
- 非銀行端壓力：BCRED Q2 的 redemption-request ratio 約 10% NAV，超過 5% quarterly redemption cap，出現 gate proration / breach（50% 比例撥付），淨流出約 $1.2B（2026-07-23，`monetary.private_credit_liquidity`）——這是私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）的實際事件，不只是結構存在。
- 違約訊號：本次證據中沒有任何 R3 規模借款人出現付款違約、covenant waiver、distressed exchange 或 going-concern 文字。

**判讀：** R3 是三條路徑中惡化最快的一條（AI 發行人利差走闊、BCRED gate proration / breach），但距離「破產／超過寬限期違約／完成 distressed exchange」仍有數個階段。要在窗口內成立，需要 CoreWeave 這類 neocloud 失去再融資管道（例如 AI 發債胃納轉弱、私募信貸贖回擴散到多檔基金），目前尚無此證據。

## 支持 yes 的證據

- [R3] AI 單一發行人利差走闊而 CDX IG 平穩，hyperscaler 2026 發債約 $182B（2026-07-16），顯示信用端開始先於股價重定價 AI 風險 `valuation.ai_credit_schism`
- [R3] BCRED Q2 redemption-request ratio 約 10% NAV、超過 5% quarterly redemption cap，發生 gate proration / breach（50% 撥付），淨流出約 $1.2B（2026-07-23）`monetary.private_credit_liquidity`
- [R1] FINRA margin debt $1.502T、YoY +51.5%（2026-06 月資料，2026-07-20 發布），落在 1999／2007／2021 頂部附近的 +40–50% 區間，回撤時有被迫去槓桿的放大效應 `retail.margin_debt`
- [R2] Alphabet Q2 FCF 轉負（−$5.9B），capex 上修至約 $205B（2026-07-22）；AI 相關 IG 發債累計約 $218–250B（2026-07-08），已在測試投資人胃納，融資一旦受阻將迫使 capex 修正 `ai.hyperscaler_financing_mix`
- [整體] Shiller CAPE 40.46、trailing P/E 28.52（2026-07-24），估值位於歷史極端，下跌空間大 `valuation.sp500_pe_cape`
- [R1] CME FedWatch 顯示 7/29 FOMC 約 38% 升息機率、約 61% 持平（2026-07-25），政策偏鷹；CPI YoY 3.46%（2026-06 月資料）限制 Fed 緩衝空間 `monetary.fedwatch` `monetary.cpi_yoy`
- [R1] NASDAQ-100 已自 2026-06-02 高點回落，距 52 週高點回撤 8.26%（2026-07-24），下跌已經開始 `valuation.ndx_drawdown`

## 支持 no 的證據

- [整體] 基準率：任一 182 天窗口內 R1–R3 皆不成立是常態；目前三條路徑都沒有進入完成段，NASDAQ-100 距 R1 門檻 22,995.45 仍需再跌約 18.25%（2026-07-24）`valuation.ndx_drawdown`
- [R2] Alphabet 2026 capex 指引上修至約 $195–205B（2026-07-22），四大 hyperscaler 合計約 $725B+，四家中已知下修 0 家 `ai.hyperscaler_capex`
- [R2] 伺服器 DRAM 3Q26 合約價 +13–18% QoQ、交期 30–40+ 週（2026-07-03），算力需求未見消化，不支持近期 capex 削減 `ai.compute_supply_demand`
- [R3] HY OAS 2.77%、IG OAS 0.79%（2026-07-23），整體信用利差仍緊，未出現廣泛信用重定價 `monetary.hy_oas` `monetary.ig_oas`
- [整體] repo 資金壓力（SOFR−IORB）為 −1.0bps、SOFR99−IORB 7.0bps（2026-07-23），SRF 動用僅 $0.001bn（2026-07-24），MOVE 76.82（2026-07-24），融資市場平穩 `monetary.repo_stress_srf` `structural.treasury_basis_trade`
- [R1] 情緒已偏恐懼：CNN Fear & Greed 39、AAII Bear 42.3%（2026-07-23/24），不是頂部常見的過度樂觀狀態 `retail.fear_greed` `retail.aaii`
- [R1] 廣度改善：RSP YTD +12.39%、領先 SPY 約 5pp（2026-07-24），NYSE A/D 線創新高（2026-07-21），漲勢不只集中在 AI 權值股 `breadth.rsp_spy` `breadth.advance_decline`

## 與前期比較

前次結論：無前次預測（report-2026-07-23 為舊格式評分報告）

report-2026-07-23 是舊格式（六維度評分）報告，沒有 yes/no 預測可比，因此 flip_evidence 為空。自 2026-07-23 以來的主要證據變化：

- NASDAQ-100 收盤從 28,454.81（2026-07-23）降到 28,128.34（2026-07-24），距 52 週高點回撤 8.26%（`valuation.ndx_drawdown`）。
- BCRED Q2 gate proration / breach 披露（2026-07-23，`monetary.private_credit_liquidity`），是本次新出現的私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）事件。
- 10Y：DGS10、DFII10 沒有新觀測（Δ 0.0bps），T10YIE −2.0bps；三腿視窗不一致，判讀：不可判（視窗不一致）（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。
- MOVE 從 80.08 降到 76.82（`structural.treasury_basis_trade`），債市波動率下降。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `structural.zero_dte`：只找到 Cboe 2026-02 的 0DTE 佔 SPX 約 56% 紀錄，沒有當前 snapshot。0DTE 是投機結構的確認指標，不影響 R1–R3 路徑判讀，因此不會改變答案。

✗ NOT DISCLOSED（搜尋完成、無合格披露）：`institutional.bofa_jpm_survey`、`ai.token_growth`、`ai.openai_anthropic_revenue`（最近披露為 2026-06-15，屬前一季，不視為當季資料）、`ai.customer_concentration_rpo`、`ai.depreciation_life`、`ai.capital_cycle`（季頻狀態與 30 日事件掃描皆無可用披露，增速證據不足，本次不判定週期階段）、`structural.global_leveraged_approvals`。

R2 的逐家缺漏：Microsoft、Amazon、Meta 的最新逐家 capex 指引數字本次未取得，只有合計約 $725B+。若其中任一家實際已下修，R2 距離會比本文判讀更近，這是本次最可能低估 yes 方向的缺口。

主要不確定性：

1. 下一輪 hyperscaler 財報（日期本次未取得）：若 Microsoft／Amazon／Meta 中有兩家下修 capex，R2 直接成立，且可能連帶觸發 R1；推向 yes。
2. 2026-07-29 FOMC：約 38% 升息機率（`monetary.fedwatch`）；若升息並配合高槓桿（margin debt YoY +51.5%），估值壓縮可能加速 R1；推向 yes。若持平，緩解壓力；推向 no。
3. 私募信貸贖回是否擴散：BCRED 的 gate proration / breach 若擴散成多基金 redemption-request ratio 上升或 net inflow→outflow flip，會切斷 neocloud 再融資，增加 R3 可能；推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest | 7411.98 | FRED API (series_id=SP500) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 5.8 | FRED API (series_id=SP500) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 7.4 | FRED API (series_id=SP500) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28128.34 | FRED API (series_id=NASDAQ100) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 8.26 | FRED API (series_id=NASDAQ100) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-27T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-07-26 | 2026-07-27T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5 | FRED API (series_id=DFEDTARL) | 2026-07-26 | 2026-07-27T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.77 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.79 | FRED API (series_id=BAMLC0A0CM) | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.71 | FRED API (series_id=DGS10) | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.43 | FRED API (series_id=DFII10) | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.26 | FRED API (series_id=T10YIE) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 84.38 | FRED API (series_id=DCOILWTICO) | 2026-07-20 | 2026-07-27T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-27T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.28 | FRED API (series_id=T5YIFR) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.7787 | FRED API (series_id=THREEFYTP10) | 2026-07-17 | 2026-07-27T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.64 | FRED API (series_id=SOFR) | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.72 | FRED API (series_id=SOFR99) | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-07-27 | 2026-07-27T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.001 | FRED API (series_id=RPONTTLD) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6747378.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5949077.0（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-17 | 2026-07-27T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6395509.0（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-27T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 18.58 | FRED API (series_id=VIXCLS) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 18.58 | FRED API (series_id=VIXCLS, SP500) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2012.1032（$2.01T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-15 | 2026-07-27T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7462516 | CFTC TFF futures-only | 2026-07-21 | 2026-07-27T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 76.82 | Yahoo Finance chart API (^MOVE) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2304.9 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | CNBC／Morgan Stanley 摘要 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報摘要 [primary: SEARCH]，90d＋同季 | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導 [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | P&I WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | Leuthold NYSE breadth WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH]（MacroMicro 鏡像） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA／Advisor Perspectives WebSearch | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | r/wallstreetbets／cashtag WebSearch，7d | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim.org／YCharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED（搜尋完成，無當月新調查） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | Reuters／investinglive [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Bloomberg WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]，30d | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報摘要 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／報導 WebSearch | ✗ NOT DISCLOSED（僅 2026-06-15 前一季資料） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報／發債報導 [primary: SEARCH]；quarterly_state＝stock_of_state，event_scan＝30d | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 [primary: SEARCH]，carry-forward | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q [primary: SEARCH]，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速＋進出場事件 [primary: SEARCH]；quarterly_state＝stock_of_state，event_scan＝30d | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | WebSearch，7d | ✓ SEARCH-VERIFIED（2 件） |
| speculation.ipo_heat | 投機｜IPO market heat | Renaissance Capital WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／Benzinga／StockTwits／Yahoo movers [primary: SEARCH]，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 WebSearch，30d | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR／openinsider，14d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | YCharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com／新聞 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | 發行商新聞稿／ETF 新發行 WebSearch，30d | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch，7d | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe WebSearch | ⛔ FETCH FAILED（只取得 2026-02 紀錄，無當前 snapshot） |
| structural.options_volume | 結構｜Options total volume: OCC monthly | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Yahoo／Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 retail.margin_debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]，30d | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）＋WebSearch | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok；WebSearch 無合格平倉事件） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 28.52 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio（multpl） | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 40.46 | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 對其餘 493 溢價約 10%、NVDA NTM P/E 約 18.7 | Magnificent 7 valuation premium cheapest decade July 2026 | https://www.cnbc.com/2026/07/08/magnificent-seven-stocks-are-the-cheapest-in-a-decade-by-one-measure.html（CNBC） | 2026-07-08 | 2026-07-27T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標價 $288（約 22× EPS，target PE 未擴張，EPS-driven） | Morgan Stanley NVDA target 288 July 2026 EPS | https://www.gurufocus.com/news/8955458/morgan-stanley-upgrades-nvidia-nvda-with-a-288-target-price（GuruFocus） | 2026-07-13 | 2026-07-27T09:30:00+08:00 |
| valuation.ai_credit_schism | AI 單一發行人利差走闊 vs CDX IG 平穩；hyperscaler 2026 發債約 $182B | AI issuer credit spread CDS widening vs CDX IG July 2026 | https://247wallst.com/investing/2026/07/16/the-ai-revolution-is-reshaping-credit-markets-here-is-what-it-really-says-about-risk/（24/7 Wall St.） | 2026-07-16 | 2026-07-27T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD +12.39%、領先 SPY 約 5pp | RSP vs SPY equal weight YTD 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度約 37% | S&P 500 top 10 concentration percent 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/（Pensions & Investments） | 2026-07-15 | 2026-07-27T09:30:00+08:00 |
| breadth.advance_decline | NYSE A/D 線創新高；新高家數 78 vs 175 轉薄 | NYSE advance decline new highs July 2026 | https://research.leutholdgroup.com/categories/nyse-advancedecline.1440（Leuthold） | 2026-07-21 | 2026-07-27T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 39（Fear） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/series/22748/cnn-fear-and-greed（MacroMicro；原定 cnn.com） | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives；原定 FINRA） | 2026-07-20 | 2026-07-27T09:30:00+08:00 |
| retail.aaii | AAII Bull 29.6%／Bear 42.3% | AAII investor sentiment survey July 23 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| retail.social_sentiment | WEN（Wendy's）r/wallstreetbets 軋空 +25% | WEN Wendys wallstreetbets short squeeze July 2026 | https://altindex.com/wallstreetbets（AltIndex） | 2026-07-25 | 2026-07-27T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 84.02 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number（YCharts；原定 naaim.org） | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| monetary.treasury_auctions | 20Y 標售 high yield 5.163%、tail +0.5bp、dealer takedown 14.67% | US Treasury 20Y auction July 22 2026 tail bid to cover | https://investinglive.com/news/us-treasury-auctions-off-13-billion-of-20-year-bonds-at-a-high-yield-of-5-163（investinglive） | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 約 61% 持平／約 38% 升息 | CME FedWatch July 29 2026 hike hold probability | https://www.cnbc.com/2026/07/13/-a-july-rate-hike-from-the-fed-the-odds-are-rising.html（CNBC；原定 CME FedWatch） | 2026-07-25 | 2026-07-27T09:30:00+08:00 |
| monetary.pboc | 人行 LPR 持穩、MLF 淨投放 ¥100B | PBoC MLF net injection LPR July 2026 | https://www.bloomberg.com/news/articles/2026-07-24/pboc-adds-most-liquidity-to-economy-in-five-months-to-aid-growth（Bloomberg） | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| monetary.private_credit_liquidity | BCRED Q2 redemption-request ratio 約 10% NAV、超過 quarterly redemption cap、gate proration / breach 50% 撥付、淨流出約 $1.2B | Blackstone BCRED Q2 2026 redemption 5% cap breach proration | https://www.benzinga.com/markets/private-markets/26/07/60649546/blackstone-says-bcred-redemptions-have-materially-slowed（Benzinga） | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| ai.hyperscaler_capex | Alphabet 2026 capex 上修至約 $195–205B；四大合計約 $725B+（Q2 財報） | Alphabet raises 2026 capex 205B Q2 hyperscaler | https://mlq.ai/news/alphabet-raises-2026-capex-guidance-to-195-205b-cloud-revenue-surges-82/（MLQ.ai；原定公司季報） | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 +13–18% QoQ、交期 30–40+ 週 | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html（TrendForce） | 2026-07-03 | 2026-07-27T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] Alphabet FY26 capex 上修至約 $205B、Q2 FCF 轉負（−$5.9B） | Alphabet capex 205B Q2 2026 FCF negative debt | https://mlq.ai/news/alphabet-raises-2026-capex-guidance-to-195-205b-cloud-revenue-surges-82/（MLQ.ai） | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] AI 相關 IG 發債累計約 $218–250B（測試投資人胃納） | AI bond issuance 250B July 2026 hyperscaler | https://www.morningstar.com/bonds/bond-issuance-backing-ai-investment-tops-250b-testing-limits-voracious-investor-demand（Morningstar） | 2026-07-08 | 2026-07-27T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex 約 $725B（分母：top-4 hyperscaler，2026-07-22）vs AI 終端營收低百億級（沿用 2026-06-15 組件） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-06-15 | 2026-07-27T09:30:00+08:00 |
| speculation.ai_rename_spac | 2 件合格 SPAC：BRTMU $325M（AI-target）、SCATU $100M | SPAC IPO announcement July 21 2026 AI | https://www.boardroomalpha.com/research/spac-market-update-july-21-2026-cdaq（Boardroom Alpha） | 2026-07-21 | 2026-07-27T09:30:00+08:00 |
| speculation.ipo_heat | Renaissance IPO Index YTD +16.7%、pipeline 建置中 | US IPO market 2026 Renaissance IPO index YTD | https://www.renaissancecapital.com/IPO-Center/Stats（Renaissance Capital） | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| speculation.microcap_moonshots | 7 日內合格 microcap moonshot 0 件 | microcap 100% single day quantum AI fusion moonshot July 2026 | Finviz／Benzinga／StockTwits／Yahoo movers screener | — | 2026-07-27T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 程序（估值 $965B）、OpenAI 傳目標 9 月 | Anthropic OpenAI IPO July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html（CNBC） | 2026-07-15 | 2026-07-27T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 cluster 0 件 | insider Form 4 cluster AI leaders July 2026 openinsider | SEC EDGAR／openinsider | — | 2026-07-27T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.61（日讀數） | Cboe equity put call ratio July 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio（YCharts；原定 Cboe） | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 約 $198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing；原定 etf.com） | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| structural.us_single_stock_etf | Tradr 5 檔 2X 單股、Leverage Shares 6 檔 ±2X 新發行 | single-stock leveraged ETF launch July 2026 Tradr Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html（GlobeNewswire） | 2026-07-07 | 2026-07-27T09:30:00+08:00 |
| structural.options_volume | OCC 6 月月報（2026-06 月資料，7 月待發） | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-07-27T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 150.19、VIX 18.58、期限結構 contango | VIX term structure SKEW July 2026 | https://finance.yahoo.com/quote/%5ESKEW/history/（Yahoo Finance） | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-06 月資料）$1.502T、YoY +51.5%（交叉引用 retail.margin_debt） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives） | 2026-07-20 | 2026-07-27T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Broadcom／Anthropic 約 $35B、Oracle 約 $38B＋密州約 $16.3B、CoreWeave GPU 擔保債務約 $24.9B | AI data center debt financing July 2026 Broadcom Anthropic Oracle CoreWeave | https://www.techtimes.com/articles/320239/20260712/nvidia-circular-financing-249b-coreweave-debt-puts-pension-funds-risk.htm（Tech Times） | 2026-07-12 | 2026-07-27T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-07-27",
  "iso_week": "2026-W31",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-01-25",
  "prior_date": "2026-07-23",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 8.26,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

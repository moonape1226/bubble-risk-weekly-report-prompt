> [DRY RUN] this report was not committed to archive.
# 2026-11-08 AI 泡沫破裂預測報告
報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：report-2026-10-18（21天前）

## 結論

**結論：no**

三條路徑都已明顯升溫但尚未進入完成段：NASDAQ-100 距 52 週高點回撤 13.56%，距 R1 門檻仍需再跌約 13.23%；CoreWeave CDS 突破 1289 bps、債券殖利率升破 16% 屬個別借款人的困境定價，但 HY OAS 僅 3.48%、SOFR−IORB 僅 2 bps、SRF 動用為 0，信用與資金面尚未出現把個別壓力傳導成 R1／R3 的跡象；R2 目前僅 Microsoft 一家（且發生於窗口起點之前）小幅下修。相對於基準率，yes 方證據尚不足以判定任一路徑較可能在 182 天內完成。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

依 `valuation.ndx_drawdown`：NASDAQ-100 最新收盤 26989.99（2026-11-06），252 個交易日最高收盤 31224.69（2026-10-06），距 52 週高點回撤 13.56%。R1 門檻水位為 23418.52，自最新收盤需再下跌約 13.23% 才觸及。回撤在一個月內形成：2026-11-05 收盤 26629.81 為近期低點，11-06 已反彈。S&P 500 方面，`valuation.sp500_trend` 顯示最新 7353.73（2026-11-05），距 200-day MA 偏離僅 +0.42%、距 52-week MA +1.84%，相較 2026-10-16 下跌 3.99%——價格延伸已大致被消化。波動面 `structural.vix_spx_comove` 顯示 VIX 28.18，7 日窗（2026-10-29 → 2026-11-05）VIX +63.84%、S&P 500 −4.75%，屬一般的避險式反向變動而非 crowded-optionality 共振；`structural.cross_asset_derivatives` 另記 SKEW 149.37、隱含相關性 20.93。估值仍偏高：`valuation.sp500_pe_cape` CAPE 38.91、trailing P/E 25.14，`valuation.mag7_multiples` Mag 7 前瞻 P/E 約 28.3。情緒已轉為恐懼：`retail.fear_greed` 22（極度恐懼）、`retail.aaii` 看空 48.4% 對看多 34.1%、`speculation.equity_put_call` 1.05。貨幣面不利於緩衝：`monetary.fedwatch` 顯示 12 月升息 25 bps 的市場隱含機會 76.8%，`monetary.cpi_yoy` CPI YoY 3.72%（2026-09 資料），Fed funds 目標區間 3.75%–4.00%（`monetary.fed_funds`）。

**判讀：** R1 已走完約一半距離，但剩餘約 13% 的跌幅需要新的催化——最可能的是 12 月 FOMC 實際升息疊加 AI 信用事件（R3）或下一輪 hyperscaler 財報 capex 下修（R2）帶來的盈餘預期重估；在情緒已處極度恐懼、價格已回到 200-day MA 附近的情況下，單靠估值偏高不足以推完剩餘跌幅。

### R2 資本支出收縮

依 `ai.hyperscaler_capex`（2026-10-29 季報後）：
- Microsoft：2026 年資本支出指引自約 $175bn 下修至約 $170bn（2026-10-29），方向＝下修。
- Alphabet：本次證據未取得最新指引數值與方向。
- Amazon：本次證據未取得最新指引數值與方向。
- Meta：本次證據未取得最新指引數值與方向。

目前四家中已確認下修者 1 家（Microsoft，幅度約 3%），且該次下修日期 2026-10-29 早於窗口起點 2026-11-08；嚴格按窗口計算，窗口內尚無下修。融資面上 `ai.hyperscaler_financing_mix` 顯示 hyperscaler 今年以來發債約 $296bn，10/29 起一週內 5 筆 AI 相關債券發行合計約 $67bn——capex 仍在以債務融資擴張，而非收縮。`ai.revenue_capex_gap`：年化 AI 終端營收 Anthropic 約 $65bn＋OpenAI 約 $70bn，合計約 $135bn（2026-09-30）vs 年化 capex 約 $170bn（分母：僅 Microsoft；Alphabet／Amazon／Meta／Oracle 本次未取得），缺口方向本次無法判定。

**判讀：** 窗口涵蓋約兩輪季報（具體日期本次證據未取得），R2 需要在這兩輪中出現至少兩家下修。Microsoft 已示範「小幅下修」的可能，若 R1 回撤延續、融資成本隨升息走高，下一輪財報出現第二、三家下修的路徑存在；但目前 hyperscaler 仍在大量發債維持建設，證據不支持兩家以上同步下修已在進行中。

### R3 AI 信用事件

最接近 R3 門檻的借款人是 CoreWeave（以 AI 算力為主業；其負債規模本次證據未載數值，以其發債與 CDS 規模判斷屬可能符合 ≥ USD 5bn 的候選）。依 `valuation.ai_credit_schism`：CoreWeave 債券殖利率升破 16%（2026-11-06），五年期 CDS 突破 1289 bps（2026-11-05），且報導指出在 NASDAQ 反彈時仍持續走闊——信用端已在重定價而股權端反彈，屬 AI 信用定價分歧（equity-vs-credit schism）的後期型態。`structural.ai_infrastructure_debt` 顯示 ING 出售 12 筆資料中心貸款（規模約 500，證據摘錄未標單位，2026-11-06），屬銀行端主動降低 AI infrastructure debt financing / vendor-financing loops 曝險的訊號。本次證據未見任何付款違約、covenant waiver、distressed exchange 或 going-concern 字樣，亦未取得近端到期／再融資牆的具體數字。整體信用面仍平穩：`monetary.hy_oas` HY OAS 3.48%（較前次 +17 bps）、`monetary.ig_oas` IG OAS 0.93%（+8 bps）；`monetary.repo_stress_srf` SOFR−IORB 2 bps、SOFR99−IORB 10 bps、SRF 動用 $0（RPONTTLD 0.0）。

**判讀：** R3 是三條路徑中市場定價最惡化的一條——CDS > 1000 bps 代表市場已為違約定價可觀的權重，但 R3 需要實際的破產申請、超過寬限期違約或完成 distressed exchange；在本次證據未見近端到期或流動性告急、且 hyperscaler 端仍能大規模發債的情況下，182 天內完成信用事件仍非較可能情境。若 CoreWeave 傳出再融資失敗、客戶合約縮減或 exchange offer，判斷應立即重估。

## 支持 yes 的證據

- [R3] CoreWeave 五年期 CDS 突破 1289 bps（2026-11-05）、債券殖利率升破 16%（2026-11-06），且在 NASDAQ 反彈時仍走闊——R3 候選借款人的信用定價已進入困境區間 `valuation.ai_credit_schism`
- [R1] NASDAQ-100 在一個月內自 31224.69（2026-10-06）跌至 26989.99（2026-11-06），距 52 週高點回撤 13.56%，已走完 R1 門檻一半以上距離 `valuation.ndx_drawdown`
- [整體] 12 月升息 25 bps 的市場隱含機會 76.8%（2026-11-06），CPI YoY 3.72%（2026-09 資料）——Fed 在升息而非降息，壓縮緩衝 AI 回撤的空間 `monetary.fedwatch` `monetary.cpi_yoy`
- [R2] Microsoft 將 2026 年資本支出指引自約 $175bn 下修至約 $170bn（2026-10-29），R2 所需兩家中已有一家出現下修先例 `ai.hyperscaler_capex`
- [R3] hyperscaler 今年以來發債約 $296bn，10/29 起一週內 5 筆 AI 相關債券合計約 $67bn（2026-11-06）——capex 融資已由現金流轉向債務，放大信用路徑的槓桿 `ai.hyperscaler_financing_mix`
- [R3] ING 出售 12 筆資料中心貸款（2026-11-06），銀行端開始降低 AI 資料中心放款曝險 `structural.ai_infrastructure_debt`
- [R1] VIX 28.18、SKEW 149.37、隱含相關性創高 20.93（2026-11-06），股票 put/call 1.05（2026-11-05）——尾部避險需求高漲 `structural.cross_asset_derivatives` `speculation.equity_put_call`
- [R1] 估值仍處高檔：CAPE 38.91、trailing P/E 25.14（2026-11-06），Mag 7 前瞻 P/E 約 28.3 `valuation.sp500_pe_cape` `valuation.mag7_multiples`

## 支持 no 的證據

- [整體] 廣義信用與資金面仍平穩：HY OAS 3.48%、IG OAS 0.93%（2026-11-05），SOFR−IORB 2 bps、SOFR99−IORB 10 bps（2026-11-05），SRF 動用 0.0（2026-11-06）——CoreWeave 的個別壓力尚未傳導成系統性信用或 repo 資金壓力（SOFR−IORB） `monetary.hy_oas` `monetary.ig_oas` `monetary.repo_stress_srf`
- [R1] 距 R1 門檻 23418.52 仍需自 26989.99 再跌約 13.23%；S&P 500 距 200-day MA 偏離僅 +0.42%（2026-11-05），價格延伸已大幅消化 `valuation.ndx_drawdown` `valuation.sp500_trend`
- [R1] 情緒已處極度恐懼：Fear & Greed 22（2026-11-06）、AAII 看空 48.4% 對看多 34.1%（2026-11-04）——反向指標下，持續性崩跌通常不從已普遍悲觀的起點開始 `retail.fear_greed` `retail.aaii`
- [R2] hyperscaler 仍以發債維持建設：今年以來發債約 $296bn、一週內 AI 相關債券約 $67bn（2026-11-06），且 Microsoft 下修幅度僅約 3%、發生於窗口之前 `ai.hyperscaler_financing_mix` `ai.hyperscaler_capex`
- [整體] AI 需求端仍在擴張：Anthropic 遞交 S-1、目標估值 1.5 兆至 2 兆美元（2026-10-26），Anthropic 上半年營收 16.3（$bn，2026-10-26），H100 隨選租金中位數 $3.87（2026-11-03） `speculation.upcoming_ai_ipos` `ai.openai_anthropic_revenue` `ai.compute_supply_demand`
- [整體] 美債市場未見失序：MOVE 92.77（2026-11-06，較前次 −8.33），銀行對 NBFI 放款 $2.11T 週增 0.27%（2026-10-28） `structural.treasury_basis_trade` `structural.nbfi_bank_loans`

## 與前期比較

前次結論：無前次預測（report-2026-10-18 為舊格式評分報告）

本次為新版預測格式的第一份 yes/no 判斷，flip_evidence 為 []。自 2026-10-18 以來的主要證據變化：
- NASDAQ-100 自 2026-10-06 高點回撤至 13.56%，S&P 500 較 2026-10-16 下跌 3.99%，VIX 由 19.99 升至 28.18。
- CoreWeave CDS 突破 1289 bps、債券殖利率升破 16%（2026-11-05／06），AI 信用定價分歧明顯化。
- Microsoft 下修 2026 年 capex 指引（2026-10-29），R2 出現首例。
- 10Y 殖利率 −25 bps 至 4.84%，10Y 期限溢價（term premium）0.9089%（2026-10-30），HY OAS +17 bps。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

未成功（✗ NOT DISCLOSED）的來源：NAAIM、BofA／JPM 調查、美債標售需求、私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）、AI token growth、折舊年限變動（depreciation useful-life change）、資本週期階段（capital cycle stage）、全球槓桿產品核准。其中私募信貸贖回壓力本次無 30 日內披露，若存在未披露的 gate proration / breach 或 net inflow→outflow flip，可能加強 R3 路徑；資本週期階段的 event_scan 找到 Microsoft 於 10 月取消 Nscale 英國資料中心交易（規模約 3，2026-11-04），但 quarterly_state 無可用增速證據，整體狀態未成功，故不作為正式證據引用——若取消／延後事件密集化，將支持 R2。另外，前置 evidence 記錄稱美債基差交易槓桿三個 script 區塊 fetch_failed 並以 WebSearch 取得 MOVE 93.88（2026-11-04），但 macro artifact 中 cftc_lev_funds／move_index／ofr_repo 皆為 status ok，本報告以 artifact 值為準（MOVE 92.77，2026-11-06）。R2 部分 Alphabet／Amazon／Meta 最新指引本次證據未取得，這是 R2 判讀的主要缺口：若其中任一家已在 10 月底財報下修，R2 距完成將僅差一家，可能改變答案。10Y 分解：ΔDGS10 −25 bps、ΔDFII10 −14 bps、ΔT10YIE −12 bps，判讀 `不可判（視窗不一致）`。

最大不確定性：
1. 12 月 FOMC：若如市場預期升息 25 bps，疊加 CPI 3.72%，可能把 R1 推向門檻並提高 R3 再融資壓力（推向 yes）；若按兵不動則緩解（推向 no）。
2. CoreWeave 的再融資與流動性：CDS 已 > 1000 bps，任何 exchange offer、covenant waiver 或客戶合約縮減都會直接推向 R3＝yes。
3. 下一輪 hyperscaler 財報（窗口內約兩輪）：Alphabet／Amazon／Meta 任一家下修即使 R2 接近完成（推向 yes）；全部上修或持平則 R2 路徑降溫（推向 no）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest | 7353.73 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 0.42（%） | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 26989.99 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤） | 13.56（%） | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026-Q2 季資料） | 48.2301354474（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 4.0（%） | FRED API (series_id=DFEDTARU) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.75（%） | FRED API (series_id=DFEDTARL) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 3.48（%） | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.93（%） | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.84（%） | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.6（%） | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.23（%） | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 99.64（USD/bbl） | FRED API (series_id=DCOILWTICO) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72（%） | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.17（%） | FRED API (series_id=T5YIFR) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest | 0.9089（%） | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.92（%） | FRED API (series_id=SOFR) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 4.0（%） | FRED API (series_id=SOFR99) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.9（%） | FRED API (series_id=IORB) | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest | 0.0（$bn） | FRED API (series_id=RPONTTLD) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6748145.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5945410.0（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6261882.0（¥626.19T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED API (series_id=VIXCLS) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 28.18 | FRED API (series_id=VIXCLS, SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2111.0042（$2.11T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7249305（口） | CFTC TFF futures-only | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo Finance chart API (^MOVE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2326.9（$bn） | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com 直接頁面 | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED（EPS／PE 分解未披露） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（月資料 carry-forward） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py BOGZ1FL153064486Q | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py DFEDTARU＋DFEDTARL | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py BAMLH0A0HYM2 | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py BAMLC0A0CM | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py DGS10 | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | scripts/fetch_macro.py DFII10 | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py T10YIE | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py DCOILWTICO | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | scripts/fetch_macro.py CPIAUCSL yoy_pct | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py T5YIFR | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py THREEFYTP10 | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py SOFR＋SOFR99＋IORB＋RPONTTLD | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py WALCL | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py ECBASSETSW＋JPNASSETS | ✓ API（ECBASSETSW ok；JPNASSETS ok，無新觀測） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（季報 stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch：quarterly_state stock-of-state＋event_scan 30d | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch（季頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch：quarterly_state stock-of-state＋event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py VIXCLS＋vix_spx_comove | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py LNFACBW027SBOG | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds＋move_index＋ofr_repo | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻 P/E 約 28.3（原定來源：Mag 7 weighted P/E） | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein TSMC 目標價 554 → 600；EPS／目標 PE 分解未披露 | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/ | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html（CNBC） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 五年期 CDS 突破 1289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds（Coinpaper） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | RSP 年初至今報酬約 14.13% | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | 前十大成分股權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 1,474 對下跌 1,252 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 22（極度恐懼；原定來源 cnn.com） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 $1.48T、YoY 約 +31.4%（原定來源 FINRA） | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives（AAII） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔 | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week（Benzinga） | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | 12 月升息 25 bps 市場隱含機會 76.8%（原定來源 CME FedWatch） | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000（摘錄未標單位） | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年 capex 指引約 $175bn → 約 $170bn（下修）；Alphabet／Amazon／Meta 未取得 | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3（$bn） | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html（Yahoo Finance） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle RPO 638（$bn）；同一 counterparty 跨供應商承諾加總未披露 | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/（Motley Fool） | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 $3.87/hr | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 今年以來發債約 $296bn | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 10/29 起一週內 5 筆 AI 相關債券發行合計約 $67bn | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 Anthropic 約 $65bn＋OpenAI 約 $70bn，合計約 $135bn（分母僅 Microsoft） | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html（Yahoo Finance） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] Microsoft 10 月取消 Nscale 英國資料中心交易，規模約 3（摘錄未標單位）；quarterly_state 無可用增速證據 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281（Investing.com／Bloomberg News） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics 完成 SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO 週漲 8% | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears（Renaissance Capital） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描：0 件符合 2+ 主題×弱基本面 | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆美元 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1（Built In） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描：0 件合格 | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe 股票選擇權 put/call 1.05（來源未明示日讀數或 5 日均值） | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide（Seeking Alpha） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭基金 10 月底規模 24.31（$bn）、當月淨流入 7.27（$bn） | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html（Yahoo Finance） | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026（Cboe via PR Newswire） | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 總結算量 1,486,062,415 口（2026-09 月資料） | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report（OCC） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性 20.93 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026（Saxo） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 交叉檢核基數約 $1.48T（2026-09 月資料） | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.ai_infrastructure_debt | ING 出售 12 筆資料中心貸款，規模約 500（摘錄未標單位） | AI data center debt financing private credit November 2026 | https://www.cnbc.com/2026/11/06/ing-ai-data-center-loans-debt.html（CNBC） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-11-08",
  "iso_week": "2026-W45",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-05-09",
  "prior_date": "2026-10-18",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 13.56,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

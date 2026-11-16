> [DRY RUN] this report was not committed to archive.

# 2026-10-18 AI 泡沫破裂預測報告

報告日期：2026-10-18｜ISO 週次：2026-W42｜預測窗口：2026-10-18 → 2027-04-18｜前次基準：report-2026-09-13（35天前）

## 結論

**結論：yes**

主導路徑是 R3 AI 信用事件，並可能經信用重定價傳導到 R1：CoreWeave 5Y CDS 於 2026-10-15 創紀錄的 1,194.5 bps（`valuation.ai_credit_schism`），同期 HY OAS 自 2.65% 走闊至 3.23%（+58 bps，`monetary.hy_oas`），顯示 AI 基礎設施信用端已進入 distress 定價區間。前次（report-2026-09-13）已判 yes，此後的新證據只加深信用壓力，沒有任何新證據讓路徑分析轉向 no，因此維持原判。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,935.59（2026-10-15），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 4.13%（`valuation.ndx_drawdown`）。R1 門檻水位為 23,418.52，自最新收盤須再下跌約 21.77% 才會觸及。S&P 500 收 7,659.44（2026-10-16），高於 200 日均線 7,271.44 約 5.34%、高於 52 週均線 7,173.01 約 6.78%，較前次基準日（2026-09-11，7,656.98）僅 +0.03%（`valuation.sp500_trend`）。估值仍處極端水位：Shiller CAPE 約 40.54（2026-10-16，`valuation.sp500_pe_cape`）；BofA 10 月基金經理人調查顯示科技股淨加碼約 37%，為 2020 年 8 月以來最高（2026-10-13，`institutional.bofa_jpm_survey`）。內部結構已轉弱：2026-10-16 上漲對下跌約 29 對 71（`breadth.advance_decline`），CNN Fear & Greed 約 18、屬極度恐懼（2026-10-16，`retail.fear_greed`），兩週內已有第 4 檔 IPO 撤件或延後（2026-10-16，`speculation.ipo_heat`）。MOVE 自 82.21 升至 101.1（2026-10-16，`structural.treasury_basis_trade`），10Y 殖利率 5.10%、實質殖利率 2.78%（2026-10-15，`monetary.dgs10`、`monetary.dfii10`）。

**判讀：** 指數本身離 R1 還很遠（回撤 4.13%，需再跌約 21.77%），但情緒、廣度、IPO 市場與債市波動都已先行轉弱，且 CAPE 約 40.54、機構科技部位為 2020 年以來最重，若 R3 的信用重定價擴散或 Anthropic 於 11 月中上市帶來大量股票供給，窗口內出現 25% 回撤的條件已經具備；單憑估值不足以觸發，需要信用或盈餘催化。

### R2 資本支出收縮

最新可得的官方指引仍是 2026 年 7 月下旬財報季的組合：四大 hyperscaler（Microsoft、Alphabet、Amazon、Meta）2026 年 capex 合計約 7,250 億美元（CNBC，2026-07-28，`ai.hyperscaler_capex`），同篇報導指出 Alphabet 財報後市場對 capex 的檢視升溫。逐家狀態：

- Microsoft：最新指引為 2026-07 財報季所設，本次證據未提供個別數字；相對前次指引方向本次無法逐家確認，未見下修報導。
- Alphabet：同上，2026-07 財報季（2026-07-28 前後），未見下修報導；市場對其 capex 反應負面。
- Amazon：同上，2026-07 財報季，未見下修報導。
- Meta：同上，2026-07 財報季，未見下修報導。

目前已下修家數：0（就已取得證據而言）。窗口內至少涵蓋兩次財報季（2026 年 10 月下旬至 11 月初的 Q3 財報，與 2027 年 1 月下旬至 2 月初的 Q4 財報及次年度指引），確切日期本次未取得。AI 營收對 capex 缺口（revenue-to-capex gap）：已披露的年化 AI 終端營收僅 Anthropic run-rate 約 650 億美元（2026-08-17），對比年化 capex 約 7,250 億美元（分母：top-4，不含 Oracle 與 neocloud），缺口巨大（`ai.revenue_capex_gap`）。

**判讀：** R2 目前未啟動，且供給端證據（H100 隨選中位租金約 4.20 美元／小時，2026-10-07，`ai.compute_supply_demand`）並未顯示需求崩落。要在窗口內成立，需要兩家在 Q3 或 Q4 財報中主動下修——最可能的情境是 R1/R3 先造成資金成本與股價壓力後，hyperscaler 為保護 FCF 而收縮；在此之前 R2 是三條路徑中最遠的一條。

### R3 AI 信用事件

R3 規模門檻候選中，信用定價最明確的是 CoreWeave：其 5Y CDS 於 2026-10-15 達紀錄高點 1,194.5 bps，報導標題為 AI 信用疑慮推升科技業違約保險至紀錄高位（`valuation.ai_credit_schism`）。約 12% 的年化 CDS 利差已是 distress 定價區間，代表市場對其在數年內違約或進行 distressed exchange 的定價已顯著上升；CoreWeave 的確切負債總額本次證據未載明，但其屬以 AI 算力為主業的大型借款人。neocloud 融資管道仍開放：Lambda 於 2026-10-01 前後取得約 10 億美元的 GPU 擔保融資（`structural.ai_infrastructure_debt`），但以 GPU 為擔保品的結構意味著若 GPU 租金下跌，擔保價值與再融資能力同步受壓。整體高收益信用同步走闊：HY OAS 3.23%（2026-10-15），較前次基準 +58 bps（`monetary.hy_oas`）；IG OAS 0.84%，僅 +4 bps（`monetary.ig_oas`），走闊集中在高收益／AI 敏感段。政策利率在此期間反而上調：Fed funds 目標區間 3.75%–4.00%（2026-10-17，較前次 +25 bps，`monetary.fed_funds`），CPI YoY 3.72%（2026-09 月資料，`monetary.cpi_yoy`），再融資成本上行。本次未取得逾期付款、covenant waiver 或 going-concern 的具體披露。

**判讀：** R3 是最接近成立的路徑。CDS 已在 distress 區間，再融資成本因升息與 10Y 5.10% 而上升，HY 利差一個月內走闊 58 bps；若 neocloud 在窗口內面臨到期或擔保品重估，distressed exchange 是最可能的成立形式。反向力量是融資市場尚未關閉（Lambda 仍能舉債）與 repo 市場無壓力。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 於 2026-10-15 創紀錄的 1,194.5 bps，科技業違約保險整體創高，AI 信用端已進入 distress 定價（`valuation.ai_credit_schism`）。
- [R3] HY OAS 由 2.65%（2026-09-11）走闊至 3.23%（2026-10-15），+58 bps，而 IG OAS 僅 +4 bps 至 0.84%，壓力集中於高收益／AI 敏感段（`monetary.hy_oas`、`monetary.ig_oas`）。
- [整體] 政策緩衝受限：Fed funds 目標區間上調 25 bps 至 3.75%–4.00%（2026-10-17），CPI YoY 3.72%（2026-09 月資料），10Y 殖利率 5.10%、實質殖利率 2.78%（2026-10-15），Fed 難以在 AI 主導的下跌中快速降息（`monetary.fed_funds`、`monetary.cpi_yoy`、`monetary.dgs10`、`monetary.dfii10`）。
- [R1] 風險偏好已轉弱：CNN Fear & Greed 約 18（極度恐懼，2026-10-16）、上漲對下跌約 29 對 71（2026-10-16）、兩週內第 4 檔 IPO 撤件或延後（2026-10-16）（`retail.fear_greed`、`breadth.advance_decline`、`speculation.ipo_heat`）。
- [R1] 部位擁擠與估值極端：BofA 10 月調查科技股淨加碼約 37%，為 2020 年 8 月以來最高（2026-10-13）；Shiller CAPE 約 40.54（2026-10-16）（`institutional.bofa_jpm_survey`、`valuation.sp500_pe_cape`）。
- [R1] 債市波動上升：MOVE 自 82.21（2026-09-11）升至 101.1（2026-10-16），槓桿基金美債期貨淨空部位 4 週擴大 309,307 口至 −6,883,343 口（2026-10-13）（`structural.treasury_basis_trade`）。
- [R1] Anthropic 目標於 11 月中上市（2026-10-05），在情緒轉弱時帶來大型 AI 股權供給（`speculation.upcoming_ai_ipos`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）：已披露年化 AI 終端營收約 650 億美元（Anthropic，2026-08-17）對比年化 capex 約 7,250 億美元（分母：top-4），回本壓力在財報季可能轉為指引壓力（`ai.revenue_capex_gap`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.13%（2026-10-15），52 週高點才於 2026-10-06 創下，距 R1 門檻 23,418.52 仍需再跌約 21.77%；S&P 500 仍高於 200 日均線 5.34%（`valuation.ndx_drawdown`、`valuation.sp500_trend`）。
- [R2] 四大 hyperscaler 2026 年 capex 合計約 7,250 億美元（2026-07-28），已取得證據中無任何一家下修，下修家數為 0（`ai.hyperscaler_capex`）。
- [整體] 短期資金市場無壓力：SOFR−IORB −1 bps、SOFR99−IORB +7 bps（2026-10-15），SRF 動用 0（2026-10-16），OFR tri-party repo 交易量約 $2.26T（2026-10-16），較前次基準 −0.33%（`monetary.repo_stress_srf`、`structural.treasury_basis_trade`）。
- [整體] 美債標售需求（auction tail / bid-to-cover）健康：2026-10-07 10Y 標售 bid-to-cover 約 2.77，報導稱需求強勁（`monetary.treasury_auctions`）。
- [R3] AI 基礎設施融資管道仍開放：Lambda 於 2026-10-01 前後取得約 10 億美元 GPU 擔保融資；H100 隨選中位租金約 4.20 美元／小時（2026-10-07），未見算力需求崩落（`structural.ai_infrastructure_debt`、`ai.compute_supply_demand`）。
- [整體] 股權波動未失控：VIX 16.46（2026-10-15），7 日 VIX/S&P 500 共振為 false（S&P 500 −0.27%、VIX +6.81%）（`structural.vix_spx_comove`）。

## 與前期比較

前次結論：yes（report-2026-09-13）

本次結論：維持

- R3 信用端加劇：CoreWeave 5Y CDS 於 2026-10-15 創紀錄 1,194.5 bps、HY OAS 較 2026-09-11 走闊 58 bps 至 3.23%——強化而非削弱前次 yes 的 R3 主線。
- R1 距離大致不變：NASDAQ-100 回撤由前次 4.21% 變為 4.13%，期間 2026-10-06 創新高；距門檻仍遠，但前次判斷本就不依賴已發生的回撤。
- 政策與利率背景收緊：Fed funds 上調 25 bps 至 3.75%–4.00%，DGS10 +14 bps 至 5.10%、DFII10 +18 bps 至 2.78%（ΔT10YIE −1 bps；判讀：不可判（視窗不一致））——再融資成本上升，屬 yes 方向。
- 情緒轉向極度恐懼（Fear & Greed 約 18）與 IPO 撤件增加，屬風險偏好退潮的早期訊號，未改變答案方向。
- 反向的新資料（repo 無壓力、10Y 標售需求強、Lambda 仍能融資）只說明系統性流動性未斷，並未降低 R3 個別借款人的違約風險，不足以構成翻轉依據。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

未披露（✗ NOT DISCLOSED）的來源：analyst TP 拆解、social sentiment、NAAIM、FedWatch、私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）、token growth、customer concentration／backlog 重複計算風險（RPO double-counting）、hyperscaler 融資結構（capex vs FCF / 發債）的 30 日 event_scan、折舊年限變動（depreciation useful-life change）、資本週期階段（capital cycle stage）兩個組件、Cboe put/call、全球槓桿商品核准。其中私募信貸贖回壓力與 hyperscaler 融資事件掃描若有披露，可能直接影響 R3 判斷；本次空白代表無新證據，不代表風險消失，不會改變答案方向。

資料品質備註：證據檔對 `structural.treasury_basis_trade` 的方法欄記載「script 三區塊 fetch_failed」，但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 三區塊皆為 status ok；本報告以 artifact 為準記 ✓ API。breadth.rsp_spy（2026-07-18）、breadth.top10_concentration（2026-07-31）、valuation.mag7_multiples（2026-09-24，只有 MSFT 單一成員前瞻本益比 24.5）快照偏舊或不完整，只作背景，不影響答案。R2 只取得四家合計 capex 約 7,250 億美元，沒有逐家數字，逐家方向因此無法確認。

最大的不確定性：

1. **2026 年 10 月下旬至 11 月初的 Q3 hyperscaler 財報**：若有兩家下修 capex，R2 直接成立（推向 yes）；若四家全數上修或持平，R2 在 Q4 財報前大致排除，R3 對融資的依賴則會加重。
2. **CoreWeave 等 neocloud 的到期與再融資**：本次未取得具體到期時間表。若窗口內有大額到期且 CDS 維持在 1,000 bps 以上，distressed exchange 機率高（推向 yes）；若 CDS 回落或順利再融資，R3 減弱（推向 no）。
3. **Fed 政策路徑**：本次升息 25 bps、CPI 3.72%。若進一步緊縮，壓力會加劇（推向 yes）；若出現官方市場功能回應（official market-functioning backstop）或轉向降息，可延緩 R1（推向 no）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest | 7659.44 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 5.34 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 6.78 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest | 29935.59 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 4.13 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level | 23418.52 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 4.0 | FRED API (series_id=DFEDTARU) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.75 | FRED API (series_id=DFEDTARL) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 3.23 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.84 | FRED API (series_id=BAMLC0A0CM) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 5.1 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.78 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.35 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 101.91 | FRED API (series_id=DCOILWTICO) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.33 | FRED API (series_id=T5YIFR) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 1.0729 | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.89 | FRED API (series_id=SOFR) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.97 | FRED API (series_id=SOFR99) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.9 | FRED API (series_id=IORB) | 2026-10-18 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6755639.0（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5943911.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6250253.0（¥625.03T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.46 | FRED API (series_id=VIXCLS) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 16.46 | FRED API (series_id=VIXCLS, SP500) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2097.9713（$2.10T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -6883343 | CFTC TFF futures-only | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 101.1 | Yahoo Finance chart API (^MOVE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2264.1 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebSearch | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED（僅 MSFT 單一成員） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py BOGZ1FL153064486Q | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey | WebSearch | ✓ SEARCH-VERIFIED |
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
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch | ✗ NOT DISCLOSED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py WALCL | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py ECBASSETSW＋JPNASSETS | ✓ API（ECBASSETSW ok；JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state，2026-07 財報季） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch：quarterly_state（stock-of-state）＋ event_scan（30d） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch＋既有 bullets 組合（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch：quarterly_state（stock-of-state）＋ event_scan（30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch＋SEC EDGAR 8-K（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch movers screens（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✗ NOT DISCLOSED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py VIXCLS＋vix_spx_comove | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py LNFACBW027SBOG | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds＋move_index＋ofr_repo；WebSearch 補充 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.54 | Shiller PE CAPE ratio current October 2026 multpl | https://www.multpl.com/shiller-pe（multpl；原定來源 multpl.com） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.mag7_multiples | MSFT 前瞻本益比 24.5 | Magnificent 7 forward P/E valuation October 2026 | https://articlegateway.com/?p=146 | 2026-09-24 | 2026-10-18T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 紀錄 1,194.5 bps | AI credit fears tech default insurance record highs October 2026 | https://www.businessday.co.za/world/international-companies/2026-10-15-ai-credit-fears-push-tech-default-insurance-to-record-highs/（BusinessDay） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 報酬約 12.08% | RSP equal weight vs SPY YTD performance 2026 | https://pro.thestreet.com/market-commentary/rsp-vs-spy-does-diversification-require-equal-weight（TheStreet Pro） | 2026-07-18 | 2026-10-18T09:30:00+08:00 |
| breadth.top10_concentration | 前十大集中度約 38.9% | S&P 500 top 10 concentration percent record 2026 | https://walnutinvest.com/stats/market-concentration-statistics | 2026-07-31 | 2026-10-18T09:30:00+08:00 |
| breadth.advance_decline | 上漲約 29 對下跌 71 | market breadth October 16 2026 percent above 200-day advance decline | https://www.thetrading.tools/market-breadth | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 約 18（極度恐懼） | CNN Fear and Greed Index October 16 2026 extreme fear | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/（原定來源 cnn.com） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-08 月資料）約 1.45 兆美元 | FINRA margin debt August 2026 year over year | https://www.thetrading.tools/margin-debt（原定來源 FINRA） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.7% | AAII sentiment survey week ending October 14 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA 10 月 FMS 科技股淨加碼約 37%，2020-08 以來最高 | BofA October 2026 fund manager survey tech overweight cash | https://www.bloomberg.com/news/articles/2026-10-13/bofa-poll-shows-investors-most-exposed-to-tech-stocks-since-2020（Bloomberg） | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.77 | Treasury 10-year note auction October 7 2026 bid-to-cover | https://www.rttnews.com/3697286/ten-year-note-auction-attracts-strong-demand.aspx（RTTNews） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣（2026-07 累計） | PBoC aggregate social financing 2026 total | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm（SteelOrbis） | 2026-08-15 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 7,250 億美元（2026-07 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 650 億美元 | OpenAI Anthropic annualized revenue run rate 2026 | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選中位租金約 4.20 美元／小時 | GPU rental price index HBM DRAM contract price October 2026 | https://uvik.net/blog/gpu-price-index/ | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 2026 年 hyperscaler 發債預估約 1,900 億美元（背景；event_scan 30 日無披露） | hyperscaler bond issuance 2026 capex versus free cash flow | https://www.twentyfouram.com/insights/oracle-clears-the-supply-cloud-with-record-demand（TwentyFour AM） | 2026-02-02 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic run-rate 約 650 億美元；分母：top-4 capex 約 7,250 億美元 | AI revenue versus capex gap 2026 annualized | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement October 2026 | 檢查來源：SEC EDGAR 8-K、SPACInsider、Boardroom Alpha | — | 2026-10-18T09:30:00+08:00 |
| speculation.ipo_heat | 兩週內第 4 檔 IPO 撤件或延後 | IPO market October 16 2026 pulled postponed Firmus Oura | https://www.ipox.com/ipox/the-ipox-update-10162026（IPOX） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（0 件符合 2+ 主題×弱基本面；PFAI 10/7 落在窗外） | biggest stock gainers week October 12-16 2026 microcap 100% | 檢查來源：Tapeboard movers archive、Financial Modeling Prep daily gainers、Yahoo movers | — | 2026-10-18T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 11 月中上市 | Anthropic IPO October 2026 timing valuation S-1 | https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market（CNN） | 2026-10-05 | 2026-10-18T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件合格） | insider selling Form 4 October 2026 Nvidia AI executives SEC | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表（無 filing-level 細節） | — | 2026-10-18T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 400.4 億美元 | single stock leveraged ETF assets October 2026 weekly flows | https://www.etfaction.com/single-stock-traders-pile-into-tsll-and-intw-as-levered-flows-surge/（ETF Action；原定來源 etf.com） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval October 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed | — | 2026-10-18T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 9 月 ADV 創紀錄約 340 萬口 | Cboe September 2026 derivatives volume 0DTE SPX record | https://www.cboe.com/insights/posts/market-metrics-that-matter-derivatives-september-2026-volume-highlights（Cboe） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.options_volume | OCC 9 月總結算量約 1,486,062,415 口（2026-09 月資料） | OCC September 2026 monthly volume data | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report（OCC） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 約 14.84、SKEW 154.34 | VIX term structure SKEW October 2026 options brief | https://www.home.saxo/content/articles/options/the-middle-got-cheaper-the-edge-did-not---options-brief---12-october-2026-12102026（Saxo） | 2026-10-12 | 2026-10-18T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 1.45 兆美元（2026-08 月資料） | margin debt to market cap August 2026 | https://www.thetrading.tools/margin-debt | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Lambda GPU 擔保融資約 10 億美元 | AI data center debt Lambda CoreWeave financing October 2026 | https://valueaddvc.com/pulse/ai-data-center-debt-financing-risk-2026（ValueAdd VC） | 2026-10-01 | 2026-10-18T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-10-18",
  "iso_week": "2026-W42",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "yes",
  "horizon_end": "2027-04-18",
  "prior_date": "2026-09-13",
  "prior_answer": "yes",
  "flip_evidence": [],
  "r1_drawdown_pct": 4.13,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

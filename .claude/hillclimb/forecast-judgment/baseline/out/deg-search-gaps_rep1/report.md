> [DRY RUN] this report was not committed to archive.

# 2026-11-08 AI 泡沫破裂預測報告
報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：report-2026-10-18（21天前）

## 結論

**結論：no**

三條路徑都還沒有一條「已在進行中、且很可能在窗口內完成」：R1 的 NASDAQ-100 距 52 週高點回撤 13.56%，還要再跌約 13.23% 才觸及門檻；R2 目前只取得 Microsoft 一家下修，而且發生在窗口開始前；R3 方面，CoreWeave CDS 1289 bps 已屬 distressed 定價，但還沒有違約、寬限期或 distressed exchange 事件。壓力明顯升溫（VIX 28.18、Fear & Greed 22、12 月升息機率 76.8%），不過依現有證據，任一條件在 182 天內成立的可能性仍低於一半。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

依 `valuation.ndx_drawdown`：NASDAQ-100 最新收盤 26,989.99（2026-11-06），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 13.56%。R1 門檻水位為 23,418.52，從最新收盤還要再跌約 13.23% 才會觸及。這波回撤集中在一個月內：11-05 收盤 26,629.81 為近期低點，11-06 小幅反彈。同期 S&P 500（`valuation.sp500_trend`）收在 7353.73（2026-11-05），較前次基準日下跌 3.99%，距 200-day MA 偏離只剩 +0.42%；`structural.vix_spx_comove` 顯示 7 日窗（2026-10-29 → 2026-11-05）VIX 上升 63.84%、S&P 500 下跌 4.75%，屬正常的股跌波動升，不是 co-movement 警戒讀數。Shiller CAPE 38.91、trailing P/E 25.14（`valuation.sp500_pe_cape`），Mag 7 前瞻本益比約 28.3（`valuation.mag7_multiples`），估值本身仍偏高，下行空間很大。

**判讀：** R1 已走完一半多的距離，市場處於急跌狀態，但還沒到門檻。要在窗口內成立，需要再跌約 13%，觸發因素可能是 Fed 12 月升息落地（`monetary.fedwatch` 76.8%）、AI 信用事件外溢，或下一輪 hyperscaler 財報 capex 再度下修。若沒有新的催化劑，急跌後的回撤常在此區間止穩。

### R2 資本支出收縮

依 `ai.hyperscaler_capex`：Microsoft 將 2026 年資本支出指引自約 175 下調至約 170（2026-10-29 財報，方向：下修）。Alphabet、Amazon、Meta 的最新指引本次搜尋都沒有取得（見 `## 資料缺漏與不確定性`），方向一律記為「未取得」，不會用記憶值補上。目前已確認下修的只有一家，而且下修日 2026-10-29 早於窗口起點 2026-11-08，嚴格依解析條件不計入窗口內。各家下一次財報的確切日期不在本次證據內；依季報節奏，窗口（至 2027-05-09）可能涵蓋兩輪財報。

**判讀：** R2 需要窗口內再出現兩家下修。Microsoft 已率先下修，顯示 capex 擴張開始受到檢視。若 R1 持續惡化，或融資成本因升息上升，下一輪財報出現跟進下修的可能性會提高。不過另外三家的現況未知，本次無法判斷是否已有第二家鬆動。

### R3 AI 信用事件

依 `valuation.ai_credit_schism`：CoreWeave 債券殖利率升破 16%（2026-11-06），五年期 CDS 突破 1289 bps（2026-11-05），已明確進入 distressed 定價區間。股權端 NASDAQ-100 同期反彈，信用端卻沒有跟著修復，AI 信用定價分歧（equity-vs-credit schism）正朝「信貸先重定價」的後期型態發展。CoreWeave 以 AI 算力為主業；其負債是否達 50 億美元門檻，本次證據沒有載明，需以最新申報為準。`structural.ai_infrastructure_debt`：荷蘭國際集團（ING）出售 12 筆資料中心貸款，規模約 500（2026-11-06，單位依來源原文），代表銀行端主動降低 AI infrastructure debt financing 曝險。整體信用市場也略為走闊：HY OAS 3.48%（+17 bps）、IG OAS 0.93%（+8 bps）（`monetary.hy_oas`、`monetary.ig_oas`）。本次證據沒有任何破產申請、付款違約、covenant waiver 或 distressed exchange。

**判讀：** R3 是本次最接近成立的路徑。CDS 已處於 distressed 區間，若 CoreWeave 或同類 neocloud 在窗口內進行 distressed exchange 或錯過付款，就會直接成立，並可能連帶觸發 R1。目前只有價格訊號，沒有事件訊號，到期牆與再融資時程也不在本次證據內，因此還不能判定事件很可能在 182 天內發生。

## 支持 yes 的證據

- [R3] CoreWeave 五年期 CDS 突破 1289 bps（2026-11-05）、債券殖利率升破 16%（2026-11-06），已屬 distressed 定價，信用端在股市反彈時仍持續重定價 `valuation.ai_credit_schism`
- [R1] NASDAQ-100 距 52 週高點回撤 13.56%（2026-11-06），一個月內自 31,224.69 跌至 26,989.99，已走完 R1 門檻一半以上距離 `valuation.ndx_drawdown`
- [整體] 12 月升息 25 bps 機率 76.8%（2026-11-06），CPI YoY 3.72%（2026-09 月資料），Fed 在 AI 主導的跌勢中幾乎沒有降息緩衝空間 `monetary.fedwatch` `monetary.cpi_yoy`
- [R2] Microsoft 將 2026 年 capex 指引自約 175 下調至約 170（2026-10-29），四家中已有一家轉向下修 `ai.hyperscaler_capex`
- [R3] ING 出售 12 筆資料中心貸款，規模約 500（2026-11-06），銀行端降低 AI infrastructure debt financing 曝險 `structural.ai_infrastructure_debt`
- [整體] 波動與避險急升：VIX 28.18、SKEW 149.37、隱含相關性 20.93 創高（2026-11-06），equity put/call 升至 1.05（2026-11-05） `structural.cross_asset_derivatives` `speculation.equity_put_call`
- [整體] 估值脆弱：Shiller CAPE 38.91、trailing P/E 25.14（2026-11-06），前十大成分股權重約 37.9%（2026-11-01） `valuation.sp500_pe_cape` `breadth.top10_concentration`

## 支持 no 的證據

- [整體] 基準率：三個條件在任意 182 天窗口內都屬罕見事件；本次三條路徑都只有價格或單一公司訊號，沒有任一條件已實際成立（`r1_met: false`，R2 窗口內 0 家下修，R3 無違約事件） `valuation.ndx_drawdown` `ai.hyperscaler_capex`
- [R1] R1 門檻水位 23,418.52，從最新收盤 26,989.99 還要再跌約 13.23%；S&P 500 仍高於 200-day MA 0.42%（2026-11-05），廣度並未崩潰：NYSE 上漲 1,474 對下跌 1,252（2026-11-06） `valuation.ndx_drawdown` `valuation.sp500_trend` `breadth.advance_decline`
- [整體] 系統性融資壓力仍低：SOFR−IORB 2 bps、SOFR99−IORB 10 bps（2026-11-05），SRF 動用 0（2026-11-06），HY OAS 僅 3.48%（2026-11-05），尚未出現 repo 資金壓力（SOFR−IORB）或廣義信用失序 `monetary.repo_stress_srf` `monetary.hy_oas`
- [整體] 情緒已轉為極度悲觀：Fear & Greed 22（2026-11-06）、AAII 看空 48.4% 高於看多 34.1%（2026-11-04），反向指標顯示投降式賣壓可能已部分釋放 `retail.fear_greed` `retail.aaii`
- [R3] AI 需求端仍有增長：Anthropic 遞交 S-1、目標估值 1.5 至 2 兆（2026-10-26），年化 AI 終端營收 Anthropic 65＋OpenAI 約 70（2026-09-30），H100 隨選租金中位數 3.87（2026-11-03），沒有利用率崩落的證據 `speculation.upcoming_ai_ipos` `ai.revenue_capex_gap` `ai.compute_supply_demand`
- [整體] 美債基差交易槓桿未見平倉：槓桿基金美債期貨淨空單 -7,249,305 口（2026-11-03，4 週再擴大 489,473 口），MOVE 92.77（2026-11-06）較前次 101.1 回落 `structural.treasury_basis_trade`

## 與前期比較

前次結論：無前次預測（report-2026-10-18 為舊格式評分報告）

前次為舊格式評分報告，不轉換為 yes/no，`flip_evidence` 為空。自 2026-10-18 以來的主要變化：

- NASDAQ-100 自 2026-10-06 高點起回落，截至 2026-11-06 回撤 13.56%；S&P 500 較基準日下跌 3.99%（`valuation.sp500_trend`）。
- AI 信用端顯著惡化：CoreWeave CDS 1289 bps、殖利率升破 16%（`valuation.ai_credit_schism`）。
- Microsoft capex 指引下修（2026-10-29，`ai.hyperscaler_capex`）。
- 利率端：DGS10 4.84%（Δ −25 bps）、DFII10 2.60%（Δ −14 bps）、T10YIE 2.23%（Δ −12 bps，視窗不同）；分解判讀：不可判（視窗不一致）（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。
- HY OAS +17 bps、IG OAS +8 bps，屬溫和走闊（`monetary.hy_oas`、`monetary.ig_oas`）。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `valuation.analyst_tp_decomposition`（⛔ FETCH FAILED，搜尋技術失敗）：只影響估值擴張的歸因，不涉及三條解析路徑，不會改變答案。
- `ai.hyperscaler_financing_mix`（⛔ FETCH FAILED components=quarterly_state:fetch_failed,event_scan:fetch_failed）：無法確認 hyperscaler 融資結構（capex vs FCF / 發債），也無法掃描 30 日內 SPV／表外融資事件。這可能影響 R3 判斷（hyperscaler 支撐的 SPV 違約屬 R3 傳導鏈），屬於有可能改變答案的缺口，但沒有證據顯示方向。

搜尋缺口（非 ⛔，但會影響判斷）：

- `ai.hyperscaler_capex` 只取得 Microsoft 的指引；Alphabet、Amazon、Meta 的最新指引本次搜尋沒有結果。這是 R2 最大的缺口：如果其中任一家在 10 月底財報已下修，就不計入窗口；但若其指引已轉為持平或語氣保守，下一輪財報兩家下修的可能性會上升。本次不補任何數字。
- AI 營收對 capex 缺口（revenue-to-capex gap）的分母目前只有 Microsoft（約 170），其餘三家與 Oracle 都缺，因此不宣稱產業層級缺口：年化 AI 終端營收約 135（Anthropic＋OpenAI）vs 年化 capex 約 170（分母：僅 Microsoft），方向無法判定。
- 資本週期階段（capital cycle stage）為 ✗ NOT DISCLOSED（quarterly_state 未披露、event_scan ok）：event_scan 找到 Microsoft 於 10 月取消 Nscale 英國資料中心交易（規模約 3，2026-11-04），屬取消／延後事件，方向偏 yes；但季度增速證據不足，本次不判定週期階段。
- 以下來源完成搜尋但無合格披露（✗ NOT DISCLOSED）：NAAIM、BofA/JPM 調查、美債標售需求、私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）、token growth、折舊年限變動（depreciation useful-life change）、全球槓桿產品核准。其中私募信貸贖回壓力的缺席讓 R3 的非銀傳導無法驗證。
- 證據註記：case 證據表把美債基差交易槓桿記為「script 三區塊 fetch_failed → WebSearch fallback」，但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 三區塊皆為 `status: ok`。本報告以 artifact 為準（Coverage 記 ✓ API），沒有採用 fallback 搜得的 MOVE 93.88。此外，證據表中多數 finding 只保留數字、沒有單位（如 capex 約 175／170、ING 約 500、Nscale 約 3），本報告照原文保留，未自行補上單位。

最大不確定性：

1. CoreWeave（及同類 neocloud）的再融資時程與負債規模：若在窗口內出現 distressed exchange，R3 直接成立並可能拖動 R1（推向 yes）。
2. 12 月 FOMC 是否升息：升息落地會加重估值壓縮與融資成本，推升 R1／R3（推向 yes）；若數據降溫、升息延後，則推向 no。
3. Alphabet／Amazon／Meta 下一輪財報 capex 指引：任兩家下修即 R2 成立（推向 yes）；維持或上修則推向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest | 7353.73 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 0.42 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（vs 前次基準日） | -3.99 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 26989.99 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 13.56 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level | 23418.52 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q2 季資料） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 4.0 | FRED API (series_id=DFEDTARU) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.75 | FRED API (series_id=DFEDTARL) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 3.48 | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.93 | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.84 | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | -25.0 | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.6 | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | -14.0 | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.23 | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | -12.0 | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 99.64 | FRED API (series_id=DCOILWTICO) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.17 | FRED API (series_id=T5YIFR) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.9089 | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.92 | FRED API (series_id=SOFR) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 4.0 | FRED API (series_id=SOFR99) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.9 | FRED API (series_id=IORB) | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps | 2.0 | fetch_macro.py repo_stress block（FRED） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr99_iorb_bps | 10.0 | fetch_macro.py repo_stress block（FRED） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6748145.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5945410.0（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（no_new_obs，持平） | 6261882.0（¥626.19T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED API (series_id=VIXCLS) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（comove=false） | 28.18 | fetch_macro.py vix_spx_comove block（FRED） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 63.84 | fetch_macro.py vix_spx_comove block（FRED） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -4.75 | fetch_macro.py vix_spx_comove block（FRED） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2111.0042（$2.11T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7249305 | CFTC TFF futures-only（cftc_lev_funds） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -489473 | CFTC TFF futures-only（cftc_lev_funds） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo Finance chart API ^MOVE（move_index） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index delta_abs（vs 2026-10-16 的 101.1） | -8.33 | Yahoo Finance chart API ^MOVE（move_index） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2326.9 | OFR STFM REPO-TRIV1_TV_TOT-P（ofr_repo） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebFetch | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED（僅前瞻 P/E，無 P/S） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch [primary: SEARCH] | ⛔ FETCH FAILED（搜尋技術失敗） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch [primary: SEARCH]，14 日窗 | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail / CNN Fear & Greed Index | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail / Margin Debt: FINRA | WebSearch（月資料 carry-forward） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail / Retail survey: AAII | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail / Social sentiment proxies | WebSearch，7 日窗 | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail / Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail / NAAIM Exposure Index | WebSearch [primary: SEARCH] | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary / Fed funds rate: FRED | fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok、DFEDTARL ok） |
| monetary.hy_oas | Monetary / High Yield OAS | fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary / Investment Grade OAS | fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary / 10Y Treasury yield | fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary / 10Y Treasury real yield | fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary / 10Y breakeven inflation rate | fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary / WTI crude oil price | fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary / CPI YoY: FRED | fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary / 5y5y forward inflation expectation | fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary / 10Y 期限溢價（term premium）: FRED | fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD） | ✓ API（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） |
| monetary.treasury_auctions | Monetary / 美債標售需求 | WebSearch [primary: SEARCH]，14 日窗 | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary / Fed funds rate path expectations | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary / Fed balance sheet: FRED | fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary / Global central bank liquidity cross-check | fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok、JPNASSETS ok） |
| monetary.pboc | Monetary / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary / Private-credit / non-bank fund liquidity stress | WebSearch [primary: SEARCH]，30 日窗 | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED（僅取得 Microsoft；Alphabet／Amazon／Meta 未取得） |
| ai.token_growth | AI / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構 | WebSearch [primary: SEARCH]；quarterly_state 與 30 日 event_scan 皆技術失敗 | ⛔ FETCH FAILED components=quarterly_state:fetch_failed,event_scan:fetch_failed |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口 | WebSearch [primary: SEARCH]（分母僅 Microsoft） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動 | WebSearch [primary: SEARCH]，30 日窗 | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI / 資本週期階段 | WebSearch [primary: SEARCH]；quarterly_state 無披露、event_scan 完成 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculation / Search for past 7 days | WebSearch，7 日窗 | ✓ SEARCH-VERIFIED（1 件 SPAC） |
| speculation.ipo_heat | Speculation / IPO market heat | WebSearch（Renaissance Capital 週報） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculation / Microcap thematic moonshots | WebSearch [primary: SEARCH]，7 日窗 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculation / Upcoming AI IPOs | WebSearch，30 日窗 | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculation / Insider selling at AI | SEC EDGAR Form 4，14 日窗 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculation / Cboe equity-only put/call ratio | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural / US leveraged ETF AUM | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED（僅半導體 3 倍多頭基金） |
| structural.us_single_stock_etf | Structural / US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com feed，30 日窗 | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural / Global leveraged product approvals | WebSearch，7 日窗 | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural / 0DTE option volume | WebSearch（Cboe 月報） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural / VIX / S&P 500 co-movement | fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API |
| structural.margin_debt_crosscheck | Structural / Cross-reference only: FINRA margin debt | WebSearch（confirmation only） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural / AI infrastructure debt financing / vendor-financing loops | WebSearch [primary: SEARCH]，30 日窗 | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural / Bank loans to nondepository financial institutions | fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py（cftc_lev_funds、move_index、ofr_repo） | ✓ API（cftc_lev_funds ok、move_index ok、ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻本益比約 28.3（原定來源：Mag 7 weighted P/E） | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ （Vested Finance） | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html （CNBC） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 五年期 CDS 突破 1289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds （Coinpaper） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | 等權指數（RSP）年初至今報酬約 14.13% | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY （Total Real Returns） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大成分股權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration （Chartrow） | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲家數 1,474 對下跌 1,252 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ （McClellan） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 22（極度恐懼；原定來源 cnn.com） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ （FinHacker） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 1.48 兆美元、YoY 約 31.4% | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt （原定來源 FINRA） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives （AAII） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔 | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week （Benzinga） | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | 12 月升息 25 bps 機率 76.8%（CME FedWatch） | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ （24/7 Wall St.） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000 | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee （BigGo Finance） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年 capex 指引自約 175 下調至約 170（Alphabet／Amazon／Meta 未取得） | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex （Global Data Center Hub） | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3 | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html （Yahoo Finance） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle 剩餘履約義務（RPO）638 | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ （Motley Fool） | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87 | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends （GetDeploying） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 Anthropic 65＋OpenAI 約 70，合計約 135 | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html （Yahoo Finance） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] Microsoft 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 （Investing.com／Bloomberg） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ （Securities.io） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO 週漲 8% | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears （Renaissance Capital） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描：0 件符合 2+ 主題×弱基本面 | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 至 2 兆 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 （Built In） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描：0 件合格 | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call ratio 升至 1.05（daily） | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide （Seeking Alpha） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭基金 10 月底規模 24.31、當月淨流入 7.27 | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html （Yahoo Finance） | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 （Cboe via PR Newswire） | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 9 月總結算量 1,486,062,415 口（2026-09 月資料） | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report （OCC） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性創高 20.93 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 （Saxo） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-09 月資料）交叉檢核基數約 1.48 兆美元 | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt （原定來源 FINRA） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.ai_infrastructure_debt | ING 出售 12 筆資料中心貸款，規模約 500 | AI data center debt financing private credit November 2026 | https://www.cnbc.com/2026/11/06/ing-ai-data-center-loans-debt.html （CNBC） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

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

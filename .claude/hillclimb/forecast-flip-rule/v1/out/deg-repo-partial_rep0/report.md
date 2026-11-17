> [DRY RUN] this report was not committed to archive.

# 2026-11-08 AI 泡沫破裂預測報告
報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：report-2026-10-18（21天前）

## 結論

**結論：no**

三條路徑目前都尚未接近完成：NASDAQ-100 距 52 週高點回撤 13.56%，仍需自最新收盤再跌約 13.2% 才觸及 R1 門檻；R2 目前僅 Microsoft 一家下修 capex 指引（且發生於窗口開始前）；R3 雖見 CoreWeave 債券殖利率破 16%、5 年期 CDS 達 1289 bps 的 distressed 定價，但尚無破產、逾寬限期違約或 distressed exchange 的披露。市場壓力明顯升溫，但相對於 182 天窗口內三項條件皆罕見的 base rate，現有證據尚不足以判斷任一路徑「較可能」完成。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 26,989.99（2026-11-06），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 13.56%；R1 門檻水位 23,418.52，自最新收盤再下跌約 13.2% 即觸及（`valuation.ndx_drawdown`）。整個回撤在一個月內完成，壓力讀數同步惡化：VIX 由 2026-10-29 的 17.2 升至 2026-11-05 的 28.18（+63.84%），同期 S&P 500 −4.75%，屬正常的股跌波動升，非 crowded-optionality 共振（`structural.vix_spx_comove`）；CNN Fear & Greed 22（極度恐懼，2026-11-06，`retail.fear_greed`）；Cboe equity put/call 升至 1.05（2026-11-05，`speculation.equity_put_call`）；SKEW 149.37、隱含相關性 20.93 創高（`structural.cross_asset_derivatives`）。S&P 500 7,353.73 仍僅高於 200 日均線 0.42%（`valuation.sp500_trend`），估值仍高：Shiller CAPE 38.91、trailing P/E 25.14（`valuation.sp500_pe_cape`）。政策端不利於緩衝：CME FedWatch 隱含 12 月升息 25 bps 的定價為 76.8%（2026-11-06，`monetary.fedwatch`），CPI YoY 3.72%（2026-09 月資料，`monetary.cpi_yoy`），Fed funds 目標區間 3.75%–4.00%（`monetary.fed_funds`）。

**判讀：** R1 已走完一半多的距離，但仍需再跌約 13.2%。高估值（CAPE 38.91）＋升息預期＋極度恐懼代表脆弱度高；能在窗口內推過門檻的催化劑是 AI 信用事件外溢（R3→R1）、12 月 FOMC 實際升息、或 hyperscaler 下一輪財報 capex 下修（R2→R1）。目前無證據顯示強迫去槓桿已啟動（廣義 HY OAS 僅 3.48%），故判斷尚未「較可能」完成。

### R2 資本支出收縮

- Microsoft：最新指引 2026 年 capex 由約 175 下修至約 170（十億美元），來源日期 2026-10-29，方向＝下修（`ai.hyperscaler_capex`）。
- Alphabet：本次證據未取得最新指引數值與方向。
- Amazon：本次證據未取得最新指引數值與方向。
- Meta：本次證據未取得最新指引數值與方向。

目前已下修者 1 家（Microsoft），但該下修發生於窗口起點 2026-11-08 之前，依解析條件不計入窗口；窗口內須另有兩家（可含 Microsoft 再次下修）下修。下兩輪季報（約 2027 年 1 月底與 4 月底）預期落在窗口內，具體日期本次證據未涵蓋。融資面：hyperscaler 年初至今發債 296（十億美元），10/29 起一週內 5 筆 AI 相關債券合計 67（十億美元）（`ai.hyperscaler_financing_mix`），顯示 hyperscaler 融資結構（capex vs FCF / 發債）正轉向舉債而非收縮。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收 ≈$135bn（Anthropic 65 ＋ OpenAI ≈70）vs 年化 capex ≈$170bn（分母：僅 Microsoft，其餘三家本次未取得），缺口方向本次無法與前值比較（`ai.revenue_capex_gap`）。

**判讀：** 一家已下修是重要的先行訊號，但 hyperscaler 仍以 $296bn 發債維持擴張，Alphabet／Amazon／Meta 的指引方向本次缺資料。要在窗口內成立，需兩家在 2027 年 1 月或 4 月季報下修；若 R1 回撤加深迫使管理層防守 FCF，機率上升，但目前不構成「較可能」。

### R3 AI 信用事件

符合規模門檻的主要候選為 CoreWeave（AI 算力為主業）。其債券殖利率升破 16%（2026-11-06），5 年期 CDS 突破 1289 bps（2026-11-05），報導指出即使 NASDAQ 反彈時其違約保護成本仍維持 1,000 bps 以上（`valuation.ai_credit_schism`）——AI 信用定價分歧（equity-vs-credit schism）已由「信用與非 AI 無差」轉為信用端先行重定價，屬後期訊號。AI infrastructure debt financing / vendor-financing loops：ING 出售 12 筆資料中心貸款，規模約 500（來源原文數值，2026-11-06，`structural.ai_infrastructure_debt`），顯示銀行端在減少資料中心曝險。對照廣義信用：HY OAS 3.48%（+17 bps vs 前次）、IG OAS 0.93%（+8 bps），擴散有限（`monetary.hy_oas`、`monetary.ig_oas`）。證據中未見任何 AI 基建借款人的付款違約、寬限期、covenant waiver、distressed exchange 或 going-concern 揭露，也未取得 CoreWeave 近期到期牆的資料。

**判讀：** R3 是三條路徑中最接近的一條：1289 bps CDS 是 distressed 區間定價，意味市場已計入顯著的違約可能，但該定價本身仍隱含窗口內多數情境不違約。要成立需在 2027-05-09 前出現實際違約／破產／distressed exchange；觸發點會是再融資失敗、主要客戶承諾縮減或銀行持續出脫曝險導致資金斷鏈。

## 支持 yes 的證據

- [R3] CoreWeave 債券殖利率破 16%（2026-11-06），5 年期 CDS 1289 bps（2026-11-05），信用端已進入 distressed 定價且與股市反彈脫鉤，是窗口內 R3 最具體的候選 `valuation.ai_credit_schism`
- [R1] NASDAQ-100 一個月內自 31,224.69（2026-10-06）跌至 26,989.99（2026-11-06），距 52 週高點回撤 13.56%，已完成觸發門檻一半以上 `valuation.ndx_drawdown`
- [整體] 政策緩衝受限：12 月升息 25 bps 定價 76.8%（2026-11-06），CPI YoY 3.72%（2026-09 月資料），Fed 難以對 AI 主導的回撤降息托底 `monetary.fedwatch` `monetary.cpi_yoy`
- [R2] Microsoft 已將 2026 年 capex 指引由約 175 下修至約 170（十億美元，2026-10-29），四家中首家下修 `ai.hyperscaler_capex`
- [R1] 壓力讀數同步惡化：VIX 28.18、SKEW 149.37、隱含相關性 20.93 創高（2026-11-06），Fear & Greed 22，equity put/call 1.05 `structural.cross_asset_derivatives` `retail.fear_greed` `speculation.equity_put_call`
- [R3] ING 出售 12 筆資料中心貸款（2026-11-06），銀行端減少資料中心曝險，可能收緊 neocloud 再融資管道 `structural.ai_infrastructure_debt`
- [整體] 估值脆弱度高：Shiller CAPE 38.91、trailing P/E 25.14（2026-11-06），一旦催化劑落地，下行空間大 `valuation.sp500_pe_cape`

## 支持 no 的證據

- [R1] 觸及 R1 仍需自 26,989.99 再跌約 13.2% 至 23,418.52；S&P 500 7,353.73 仍高於 200 日均線 0.42%（2026-11-05），尚未進入趨勢性破位 `valuation.ndx_drawdown` `valuation.sp500_trend`
- [R3] 廣義信用未失序：HY OAS 3.48%、IG OAS 0.93%（2026-11-05），僅較前次擴大 17 bps／8 bps，AI 個別信用壓力尚未傳導為系統性利差走闊 `monetary.hy_oas` `monetary.ig_oas`
- [R2] hyperscaler 仍以舉債延續擴張：年初至今發債 296、10/29 起一週 5 筆 AI 相關債券合計 67（十億美元，2026-11-06），資本市場仍願意供資，短期無被迫砍 capex 的資金壓力 `ai.hyperscaler_financing_mix`
- [R2] 窗口內須兩家下修；Microsoft 的下修發生於窗口前，其他三家本次無下修證據 `ai.hyperscaler_capex`
- [整體] 需求端仍在擴張：Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆（2026-10-26），Anthropic 上半年營收 16.3（十億美元）；H100 隨選租金中位數 3.87（2026-11-03）未見崩跌 `speculation.upcoming_ai_ipos` `ai.openai_anthropic_revenue` `ai.compute_supply_demand`
- [整體] 美債市場未見失序：MOVE 92.77（2026-11-06，較前次 −8.33），OFR tri-party repo transaction volume 2,326.9（十億美元）平穩，10Y 殖利率 4.84%（−25 bps） `structural.treasury_basis_trade` `monetary.dgs10`

## 與前期比較

前次結論：無前次預測（report-2026-10-18 為舊格式評分報告）

前次為舊格式評分報告，不轉換為 yes/no。自 2026-10-18 以來的重大變化：

- NASDAQ-100 52 週高點落在 2026-10-06，回撤主要發生在前次之後；S&P 500 較前次 −3.99%（`valuation.sp500_trend`）。
- VIX 由 19.99（2026-10-16）升至 28.18（2026-11-05）（`structural.vix_spx_comove`）。
- HY OAS 由 3.31% 升至 3.48%，10Y 由 5.09% 降至 4.84%，WTI 由 108.21 降至 99.64（`monetary.hy_oas`、`monetary.dgs10`、`monetary.wti`）。
- CoreWeave 信用 distressed 定價（`valuation.ai_credit_schism`）與 Microsoft capex 下修（`ai.hyperscaler_capex`）為新出現的路徑訊號，但均未使任一路徑達到「較可能完成」。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- monetary.repo_stress_srf（必抓）：腳本中 SOFR99 與 RPONTTLD 皆為 fetch_failed，且無 WebSearch fallback，合併狀態依 worst-outcome 為 ⛔ FETCH FAILED。可用腿已保留於 Raw data：SOFR 3.92%（2026-11-05）、IORB 3.90%，`repo_stress` 為 partial、SOFR−IORB 為 2.0 bps（同為 2026-11-05），未見 secured-funding 壓力；缺少 SOFR99 尾部利差與 SRF 動用。此缺口不太可能改變答案：OFR repo 成交量與 MOVE 皆平穩，且 R1–R3 不直接依賴 repo 讀數；但若 SRF 實際大額動用，會提高 R1 的跨資產傳導風險。

其他資料限制（非 FETCH FAILED）：

- ai.hyperscaler_capex 僅取得 Microsoft 指引；Alphabet、Amazon、Meta 的最新指引數值與方向本次證據未涵蓋。這是可能影響 R2 判讀的最大缺口——若其中任一家已在窗口內下修，R2 距離成立只剩一家。另該來源 URL slug 標示「q3-fy2026 / 190b capex」，與發現文字「約 175 → 約 170」不一致，數值以發現文字為準並待下次核實。
- ai.capital_cycle 的 quarterly_state 無可用增速披露，故為 ✗ NOT DISCLOSED；其 event_scan 找到 Microsoft 10 月取消 Nscale 英國資料中心交易（2026-11-04），僅作背景、不作為證據引用。增速證據不足，本次不判定週期階段。
- 腳本 decomposition.driver 為 unknown（ΔT10YIE 視窗與 DGS10／DFII10 不一致）：ΔDGS10 −25 bps、ΔDFII10 −14 bps、ΔT10YIE −12 bps，判讀：不可判（視窗不一致）。
- 證據表將 structural.treasury_basis_trade 描述為「腳本三區塊 fetch_failed → WebSearch fallback」，但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 三塊均為 status ok；本報告以 artifact 為準記 ✓ API，搜尋所得 MOVE 93.88（2026-11-04）僅作交叉核對。
- 分析師 TP 僅取得 Bernstein TSMC 554 → 600，無 EPS／目標 PE 拆解資料。

主要不確定性：

1. CoreWeave 再融資與到期結構（本次未取得）：若出現 distressed exchange 或付款違約，R3 直接成立並很可能經信用外溢觸發 R1，推向 yes。
2. 12 月 FOMC：若如定價升息且 CPI 未降，估值壓縮可能把 NASDAQ-100 推向 R1 門檻，推向 yes；若通膨降溫、升息落空，推向 no。
3. 2027 年 1 月 hyperscaler 季報：若 Alphabet／Amazon／Meta 有兩家下修 capex，R2 成立，推向 yes；若維持上修或持平（配合持續發債），推向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest | 7353.73 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 0.42（%） | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（vs 前次） | -3.99（%） | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 26989.99 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 13.56（%） | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level | 23418.52 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2） | 48.23（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 4.0（%） | FRED API (series_id=DFEDTARU) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.75（%） | FRED API (series_id=DFEDTARL) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 3.48（%） | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.93（%） | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.84（%） | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | -25.0（bps） | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.6（%） | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.23（%） | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 99.64（USD） | FRED API (series_id=DCOILWTICO) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72（%） | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.17（%） | FRED API (series_id=T5YIFR) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.9089（%） | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.92（%） | FRED API (series_id=SOFR) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.9（%） | FRED API (series_id=IORB) | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,748,145（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,945,410（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,261,882（¥626.19T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED API (series_id=VIXCLS) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 28.18 | FRED API derived block (vix_spx_comove) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 63.84（%） | FRED API derived block (vix_spx_comove) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -4.75（%） | FRED API derived block (vix_spx_comove) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2111.0042（$2.11T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7,249,305（口） | CFTC TFF (cftc_lev_funds) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -489,473（口） | CFTC TFF (cftc_lev_funds) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo chart ^MOVE (move_index) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2326.9（十億美元） | OFR STFM REPO-TRIV1_TV_TOT-P (ofr_repo) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebFetch | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch（vestedfinance） | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED（Bernstein TSMC；無 EPS／PE 拆解） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail / CNN Fear & Greed Index | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail / Margin Debt: FINRA | WebSearch（月頻 stock-of-state，2026-09） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail / Retail survey: AAII | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail / Social sentiment proxies | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail / Household equity allocation | scripts/fetch_macro.py BOGZ1FL153064486Q | ✓ API |
| retail.naaim | Retail / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED（無當週值） |
| institutional.bofa_jpm_survey | Institutional / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED（無新月度調查） |
| monetary.fed_funds | Monetary / Fed funds rate: FRED | scripts/fetch_macro.py DFEDTARU＋DFEDTARL | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary / High Yield OAS | scripts/fetch_macro.py BAMLH0A0HYM2 | ✓ API |
| monetary.ig_oas | Monetary / Investment Grade OAS | scripts/fetch_macro.py BAMLC0A0CM | ✓ API |
| monetary.dgs10 | Monetary / 10Y Treasury yield | scripts/fetch_macro.py DGS10 | ✓ API |
| monetary.dfii10 | Monetary / 10Y Treasury real yield | scripts/fetch_macro.py DFII10 | ✓ API |
| monetary.t10yie | Monetary / 10Y breakeven inflation rate | scripts/fetch_macro.py T10YIE（FRED 直取） | ✓ API |
| monetary.wti | Monetary / WTI crude oil price | scripts/fetch_macro.py DCOILWTICO | ✓ API |
| monetary.cpi_yoy | Monetary / CPI YoY: FRED | scripts/fetch_macro.py CPIAUCSL yoy_pct | ✓ API |
| monetary.t5yifr | Monetary / 5y5y forward inflation expectation | scripts/fetch_macro.py T5YIFR | ✓ API |
| monetary.term_premium | Monetary / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py THREEFYTP10 | ✓ API |
| monetary.repo_stress_srf | Monetary / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py SOFR／SOFR99／IORB／RPONTTLD；無 WebSearch fallback | ⛔ FETCH FAILED（SOFR ok；SOFR99 fetch_failed；IORB ok；RPONTTLD fetch_failed） |
| monetary.treasury_auctions | Monetary / 美債標售需求 | WebSearch（14d） | ✗ NOT DISCLOSED（窗內無顯著標售結果） |
| monetary.fedwatch | Monetary / Fed funds rate path expectations | WebSearch（CME FedWatch 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary / Fed balance sheet: FRED | scripts/fetch_macro.py WALCL | ✓ API |
| monetary.ecb_boj | Monetary / Global central bank liquidity cross-check | scripts/fetch_macro.py ECBASSETSW＋JPNASSETS | ✓ API（ECBASSETSW ok；JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED（僅取得 Microsoft） |
| ai.token_growth | AI / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration | WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構 | WebSearch：quarterly_state 承接最新季度；event_scan 30d | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口 | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI / 資本週期階段 | WebSearch：quarterly_state 無增速披露；event_scan 30d 有事件 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculation / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED（1 件 SPAC） |
| speculation.ipo_heat | Speculation / IPO market heat | WebSearch（Renaissance Capital） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculation / Microcap thematic moonshots | WebSearch movers screen（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculation / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculation / Insider selling at AI | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculation / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED（僅半導體 3x 基金） |
| structural.us_single_stock_etf | Structural / US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural / 0DTE option volume | WebSearch（Cboe 月報） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural / VIX / S&P 500 co-movement | scripts/fetch_macro.py VIXCLS＋vix_spx_comove | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural / Cross-reference only: FINRA margin debt | WebSearch（交叉檢核） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural / Bank loans to nondepository financial institutions | scripts/fetch_macro.py LNFACBW027SBOG | ✓ API |
| structural.treasury_basis_trade | Structural / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds／move_index／ofr_repo（any）；MOVE WebSearch 交叉核對 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻 P/E 約 28.3 | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ （Vested Finance；原定 multpl／GuruFocus 類來源） | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein TSMC 目標價 554 → 600 | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/ （StockAnalysis；原定 Reuters／cnyes 摘要） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html （CNBC） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5 年期 CDS 突破 1289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds （Coinpaper） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | RSP 年初至今報酬約 14.13% | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY （Total Real Returns） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration （Chartrow） | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 1,474 對下跌 1,252 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ （McClellan） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 22（極度恐懼） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ （FinHacker；原定 cnn.com） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 $1.48T、YoY 約 +31.4% | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt （原定 FINRA） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives （AAII） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔 | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week （Benzinga） | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | 12 月升息 25 bps 定價 76.8% | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ （24/7 Wall St.；原定 CME FedWatch） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000（來源原文數值） | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee （BigGo Finance） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年 capex 指引約 175 → 約 170（十億美元），下修 | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex （Global Data Center Hub；原定公司財報） | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3（十億美元） | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html （Yahoo Finance） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle RPO 638（十億美元） | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ （Motley Fool） | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87（美元／小時） | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends （GetDeploying） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 年初至今發債 296（十億美元） | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era （404K Research，引 Goldman） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 10/29 起一週 5 筆 AI 相關債券發行合計 67（十億美元） | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era （404K Research，引 Goldman） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 Anthropic 65 ＋ OpenAI 約 70，合計約 135（十億美元） | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html （Yahoo Finance） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] Microsoft 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 （Investing.com，引 Bloomberg） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ （Securities.io） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO 週漲 8% | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears （Renaissance Capital） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描：0 件符合 2+ 主題×弱基本面 | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 （Built In） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描：0 件合格 | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 升至 1.05 | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide （Seeking Alpha） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭基金 10 月底規模 24.31、當月淨流入 7.27（十億美元） | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html （Yahoo Finance；原定 etf.com） | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 （Cboe 新聞稿） | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 2026-09 月總結算量 1,486,062,415 口 | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report （OCC） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性 20.93 創高 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 （Saxo） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 交叉檢核基數約 $1.48T（2026-09 月資料） | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt （原定 FINRA） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.ai_infrastructure_debt | ING 出售 12 筆資料中心貸款，規模約 500（來源原文數值） | AI data center debt financing private credit November 2026 | https://www.cnbc.com/2026/11/06/ing-ai-data-center-loans-debt.html （CNBC） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index 交叉核對：MOVE 93.88（非 primary，artifact 為 92.77） | MOVE index Treasury volatility level November 2026 | https://streetstats.finance/markets/volatility （StreetStats） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |

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
  "yes_basis": [],
  "r1_drawdown_pct": 13.56,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

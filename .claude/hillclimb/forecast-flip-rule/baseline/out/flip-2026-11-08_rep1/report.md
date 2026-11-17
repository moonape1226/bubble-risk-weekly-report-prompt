> [DRY RUN] this report was not committed to archive.

# 2026-11-08 AI 泡沫破裂預測報告
報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：report-2026-10-18（21天前）

## 結論

**結論：yes**

驅動答案的是 R1 與 R3 兩條路徑同時推進：NASDAQ-100 自前次基準以來由 4.13% 回撤擴大到 13.56%，距 R1 門檻只差再跌 13.23%；而 R3 首要候選 CoreWeave 的五年期 CDS 已破 1,289 bps、債券殖利率升破 16%（2026-11-05／11-06），信用端已進入 distressed 定價。同時 FedWatch 隱含 12 月升息 76.8%、CPI YoY 3.72%，政策端缺乏緩衝，使三條路徑在窗口內至少一條成立的可能性高於不成立。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

FRED `NASDAQ100` 最新收盤 26,989.99（2026-11-06），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 13.56%；R1 門檻水位為 23,418.52，自最新收盤再下跌約 13.23% 即觸發（`valuation.ndx_drawdown`）。前次基準（2026-10-18）時 r1_drawdown_pct 為 4.13，三週內回撤擴大逾 9 個百分點。

同步讀數：S&P 500 為 7,353.73（2026-11-05），自前次基準 −3.99%，僅高於 200 日均線 0.42%、52 週均線 1.84%，價格延伸已基本消化（`valuation.sp500_trend`）。VIX 由 2026-10-29 的 17.2 升到 2026-11-05 的 28.18（+63.84%），同窗 S&P 500 −4.75%，屬正常的股跌波動升，非 crowded-optionality 同漲讀數（`structural.vix_spx_comove`）；SKEW 149.37、隱含相關性 20.93 創高（`structural.cross_asset_derivatives`），Cboe 股票賣買權比升至 1.05（`speculation.equity_put_call`），CNN Fear & Greed 22（極度恐懼，`retail.fear_greed`）。估值仍高：Shiller CAPE 38.91、trailing P/E 25.14（`valuation.sp500_pe_cape`），Mag 7 前瞻 P/E 約 28.3（`valuation.mag7_multiples`），前十大權重約 37.9%（`breadth.top10_concentration`）。

利率面：10Y 殖利率 4.84%（2026-11-05，較前次 −25 bps）、實質殖利率 2.60%（−14 bps）、T10YIE 2.23%（2026-11-06，−12 bps）；本週 Δ 分解判讀為 `不可判（視窗不一致）`，因 T10YIE 與 DGS10／DFII10 的視窗不同，不推斷 driver（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。10Y 期限溢價（term premium）0.9089%（Kim-Wright，2026-10-30，trailing 約 7 日 −2.7 bps，`monetary.term_premium`）。

**判讀：** R1 已走完一半以上（13.56% 對 25% 門檻），且是在估值仍高、Fed 傾向升息的環境下發生；窗口內只要再出現一次與 10 月同幅度的修正（例如 AI 信用事件外溢或 12 月 FOMC 升息），R1 即可成立。

### R2 資本支出收縮

- Microsoft：2026 年資本支出指引自約 175 下調至約 170（十億美元，來源日期 2026-10-29）＝下修（`ai.hyperscaler_capex`）。注意該來源 URL 標題提及「$190B capex」且標為 Q3 FY2026，與 2026-10-29 發布日不一致，本次無法核實為何一期財報。
- Alphabet：本次證據未取得最新指引，方向未提供指引。
- Amazon：本次證據未取得最新指引，方向未提供指引。
- Meta：本次證據未取得最新指引，方向未提供指引。

目前可確認下修者 1 家（Microsoft），R2 需 2 家。下一次財報的確切日期本次證據未提供；依季報節奏，2027 年 1 月下旬至 2 月初與 2027 年 4 月下旬兩輪財報皆落在窗口（至 2027-05-09）內。反方向證據：hyperscaler 今年以來發債約 296（十億美元），2026-10-29 起一週內 5 筆 AI 相關債券合計約 67（十億美元），顯示 capex 仍以舉債延續而非收縮（`ai.hyperscaler_financing_mix`）。

**判讀：** R2 距成立尚差 1 家下修；在 R1 持續回撤、融資成本上升（FedWatch 升息預期）的情況下，窗口內兩輪財報給出第二家下修的機會實在，但目前其餘三家無下修證據，R2 單獨成立的把握低於 R1／R3。

### R3 AI 信用事件

- CoreWeave：債券殖利率升破 16%（2026-11-06），五年期 CDS 突破 1,289 bps（2026-11-05），且是在 NASDAQ 反彈日仍走闊（`valuation.ai_credit_schism`）。這是 AI 信用定價分歧（equity-vs-credit schism）由「信用與非 AI 無差」轉為「信用端先重定價」的後期訊號。本次證據未載明 CoreWeave 負債總額與近期到期結構，R3 的 ≥ 50 億美元門檻需另行確認。
- AI infrastructure debt financing / vendor-financing loops：荷蘭國際集團（ING）出售 12 筆資料中心貸款，規模約 500（單位依來源，2026-11-06，`structural.ai_infrastructure_debt`）——銀行端主動降低資料中心曝險。
- 廣義信用尚未失序：HY OAS 3.48%（+17 bps）、IG OAS 0.93%（+8 bps）（`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）2 bps、SOFR99−IORB 10 bps，SRF 動用 0（`monetary.repo_stress_srf`）；銀行對 NBFI 放款 $2.11T（`structural.nbfi_bank_loans`）。
- 本次未發現任何破產申請、付款違約或 distressed exchange 的報導。

**判讀：** R3 尚未發生事件，但首要候選的 CDS 已在 distressed 區間，市場定價的違約風險在六個月窗口內不可忽略；若 CoreWeave 或同類 neocloud 宣布債務交換或錯過付款，R3 即成立並可能經由股市外溢推動 R1。

## 支持 yes 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 13.56%（2026-11-06 收盤 26,989.99 對 2026-10-06 高點 31,224.69），前次基準時僅 4.13，再跌約 13.23% 即達門檻 23,418.52（`valuation.ndx_drawdown`）。
- [R3] CoreWeave 五年期 CDS 突破 1,289 bps（2026-11-05）、債券殖利率升破 16%（2026-11-06），AI 信用端已進入 distressed 定價（`valuation.ai_credit_schism`）。
- [整體] FedWatch 隱含 12 月升息 25 bps 機會 76.8%（2026-11-06，`monetary.fedwatch`），CPI YoY 3.72%（2026-09，`monetary.cpi_yoy`）；政策利率 3.75–4.00%（`monetary.fed_funds`）在通膨未降下難以為 AI 回撤提供緩衝。
- [R2] Microsoft 將 2026 年資本支出指引自約 175 下調至約 170（2026-10-29），四家中已有一家下修（`ai.hyperscaler_capex`）。
- [整體] 壓力讀數同步惡化：VIX 28.18、SKEW 149.37、隱含相關性 20.93 創高（2026-11-06，`structural.cross_asset_derivatives`），Fear & Greed 22（`retail.fear_greed`），賣買權比 1.05（`speculation.equity_put_call`），S&P 500 七日 −4.75% 而 VIX +63.84%（`structural.vix_spx_comove`）。
- [R3] ING 出售 12 筆資料中心貸款（2026-11-06，`structural.ai_infrastructure_debt`），hyperscaler 今年以來發債約 296、一週內 AI 相關債券約 67（十億美元，2026-11-06，`ai.hyperscaler_financing_mix`）——AI 建設已轉入舉債階段，信用端敏感度上升。
- [整體] 估值仍處高檔：Shiller CAPE 38.91（2026-11-06，`valuation.sp500_pe_cape`），Mag 7 前瞻 P/E 約 28.3（`valuation.mag7_multiples`），家戶股票配置 48.23%（2026-Q2，`retail.household_equity_allocation`），下跌空間大。

## 支持 no 的證據

- [整體] 基準率：任一 182 天窗口內 R1–R3 皆不成立是常態；R1 仍需自 26,989.99 再跌約 13.23%，S&P 500 仍高於 200 日均線 0.42%（2026-11-05，`valuation.sp500_trend`），大盤尚未破位（`valuation.ndx_drawdown`）。
- [R3] 廣義信用與資金市場平穩：HY OAS 3.48%、IG OAS 0.93%（2026-11-05，`monetary.hy_oas`、`monetary.ig_oas`），SOFR−IORB 2 bps、SRF 動用 0（`monetary.repo_stress_srf`），MOVE 92.77 較前次 101.1 回落（2026-11-06，`structural.treasury_basis_trade`）——CoreWeave 壓力尚未外溢為系統性信用事件。
- [R2] 目前僅一家下修，hyperscaler 仍大量發債續推 capex（今年以來約 296，`ai.hyperscaler_financing_mix`）；Microsoft 下修幅度僅約 3%，且來源期別標示不一致（`ai.hyperscaler_capex`）。
- [整體] 需求端與資本市場仍開放：Anthropic 年化營收 65、OpenAI 約 70（十億美元，2026-09-30，`ai.revenue_capex_gap`），Anthropic 已遞交 S-1、目標估值 1.5 兆至 2 兆美元（2026-10-26，`speculation.upcoming_ai_ipos`）；H100 隨選租金中位數 3.87（2026-11-03，`ai.compute_supply_demand`）未見崩落。
- [整體] 情緒已轉為恐懼而非狂熱：AAII 看空 48.4%、看多 34.1%（2026-11-04，`retail.aaii`），可能代表部分去槓桿已完成；10Y 殖利率較前次 −25 bps（`monetary.dgs10`）、WTI −7.92%（`monetary.wti`）放鬆金融條件。
- [R1] 市場廣度未全面崩潰：2026-11-06 紐交所上漲 1,474 家對下跌 1,252 家（`breadth.advance_decline`），等權指數 YTD 約 14.13%（`breadth.rsp_spy`）。

## 與前期比較

前次結論：yes（report-2026-10-18）
本次結論：維持

- R1：r1_drawdown_pct 由 4.13 擴大至 13.56（`valuation.ndx_drawdown`），強化 yes，未構成翻轉理由。
- R3：CoreWeave CDS 破 1,289 bps、殖利率破 16%（2026-11-05／11-06，`valuation.ai_credit_schism`），為前次之後的新增信用壓力證據，方向與 yes 一致。
- 政策：FedWatch 12 月升息 76.8%（2026-11-06，`monetary.fedwatch`），政策緩衝縮小，方向與 yes 一致。
- R2：Microsoft 下修 capex 指引（2026-10-29，`ai.hyperscaler_capex`），進度 1／2，方向與 yes 一致但期別待核實。
- 反方向：HY OAS 僅 +17 bps、MOVE 回落（`monetary.hy_oas`、`structural.treasury_basis_trade`），顯示尚未系統性失序；但不足以推翻 R1／R3 的推進，故維持 yes，`flip_evidence` 為空。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

非 ⛔ 但影響判斷的缺漏：monetary.private_credit_liquidity、monetary.treasury_auctions、retail.naaim、institutional.bofa_jpm_survey、ai.token_growth、ai.depreciation_life、structural.global_leveraged_approvals 皆為 ✗ NOT DISCLOSED；ai.capital_cycle 的 quarterly_state 無可用增速證據（增速證據不足，本次不判定週期階段），其 event_scan 雖找到 Microsoft 於 10 月取消 Nscale 英國資料中心交易（2026-11-04 報導），因整體狀態未成功僅列為背景。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）無當期披露，若實際已出現 gate proration / breach 會進一步支持 yes，不會使答案轉向 no。

資料一致性備註：evidence 記錄的 structural.treasury_basis_trade 方法欄稱 script 三區塊 fetch_failed，但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 皆為 `status: ok`，本報告以 artifact 為準記 ✓ API；WebSearch 備援的 MOVE 93.88（2026-11-04）與 artifact 92.77（2026-11-06）日期不同，未採用。

最大不確定性：

1. Alphabet、Amazon、Meta 的最新 capex 指引本次未取得——若其中任一家已於 10 月底財報下修，R2 可能已經成立（推向 yes）；若皆上修，R2 只剩 Microsoft 一家（不改變 yes，因答案主要由 R1／R3 支撐）。Microsoft 來源期別不一致也需下次核實。
2. CoreWeave 負債規模與近期到期／再融資時程本次證據未載明——若其負債與到期結構使 distressed exchange 在窗口內可行，推向 yes；若近期無到期牆，R3 時間點可能落在窗口外（推向 no）。
3. 12 月 FOMC：若如 FedWatch 所示升息，對高估值 AI 股構成直接壓力（推向 yes）；若 Fed 因市場壓力改為暫停或啟動官方市場功能回應（official market-functioning backstop），R1 回撤可能在門檻前止步（推向 no）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7353.73 | FRED API（series_id=SP500，sp500_trend block） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 0.42 | FRED API（series_id=SP500，sp500_trend block） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 1.84 | FRED API（series_id=SP500，sp500_trend block） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較前次基準 %） | -3.99 | FRED API（series_id=SP500，sp500_trend block） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 26989.99 | FRED API（series_id=NASDAQ100，ndx_drawdown block） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API（series_id=NASDAQ100，ndx_drawdown block） | 2026-10-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（回撤 %） | 13.56 | FRED API（series_id=NASDAQ100，ndx_drawdown block） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API（series_id=NASDAQ100，ndx_drawdown block） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026-Q2 季資料，%） | 48.2301354474 | FRED API（series_id=BOGZ1FL153064486Q） | 2026-04-01 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（%） | 4.0 | FRED API（series_id=DFEDTARU） | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（%） | 3.75 | FRED API（series_id=DFEDTARL） | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 3.48 | FRED API（series_id=BAMLH0A0HYM2） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 17.0 | FRED API（series_id=BAMLH0A0HYM2） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.93 | FRED API（series_id=BAMLC0A0CM） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.84 | FRED API（series_id=DGS10） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | -25.0 | FRED API（series_id=DGS10） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.6 | FRED API（series_id=DFII10） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | -14.0 | FRED API（series_id=DFII10） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.23 | FRED API（series_id=T10YIE） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | -12.0 | FRED API（series_id=T10YIE） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（美元／桶） | 99.64 | FRED API（series_id=DCOILWTICO） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO chg_pct | -7.92 | FRED API（series_id=DCOILWTICO） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72 | FRED API（series_id=CPIAUCSL） | 2026-09-01 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.17 | FRED API（series_id=T5YIFR） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR delta_bps | -16.0 | FRED API（series_id=T5YIFR） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（%，Kim-Wright） | 0.9089 | FRED API（series_id=THREEFYTP10） | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 約 7 日） | -2.7 | FRED API（series_id=THREEFYTP10） | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.92 | FRED API（series_id=SOFR） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 4.0 | FRED API（series_id=SOFR99） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.9 | FRED API（series_id=IORB） | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API（series_id=RPONTTLD） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR−IORB（repo_stress sofr_iorb_bps，同日 2026-11-05） | 2.0 | FRED API（SOFR、IORB；repo_stress block） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6748145.0（$6.75T，百萬美元） | FRED API（series_id=WALCL） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5945410.0（€5.95T，百萬歐元） | FRED API（series_id=ECBASSETSW） | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6261882.0（¥626.19T，億日圓） | FRED API（series_id=JPNASSETS） | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED API（series_id=VIXCLS） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of，base_date 2026-10-29，window_days 7，comove false） | 28.18 | FRED API（VIXCLS＋SP500，vix_spx_comove block） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 63.84 | FRED API（vix_spx_comove block） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -4.75 | FRED API（vix_spx_comove block） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2111.0042（$2.11T，十億美元） | FRED API（series_id=LNFACBW027SBOG） | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口數） | -7249305 | CFTC TFF futures-only（cftc_lev_funds block） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口數） | -489473 | CFTC TFF futures-only（cftc_lev_funds block） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo Finance chart API（^MOVE，move_index block） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2326.9 | OFR STFM（REPO-TRIV1_TV_TOT-P，ofr_repo block） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebFetch | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch（vestedfinance） | ✓ SEARCH-VERIFIED（AI leader P/S 對 10 年均值未取得） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d、同季） | ✓ SEARCH-VERIFIED（Bernstein TSM；EPS／PE 拆解未披露） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail / Margin Debt: FINRA | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED（2026-09 月資料；對市值比未取得） |
| retail.aaii | Retail / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail / Social sentiment proxies | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail / Household equity allocation | scripts/fetch_macro.py（BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED（搜尋完成，無當週值） |
| institutional.bofa_jpm_survey | Institutional / BofA Fund Manager Survey and JPM survey | WebSearch | ✗ NOT DISCLOSED（搜尋完成，無當期調查） |
| monetary.fed_funds | Monetary / Fed funds rate: FRED | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary / High Yield OAS | scripts/fetch_macro.py | ✓ API |
| monetary.ig_oas | Monetary / Investment Grade OAS | scripts/fetch_macro.py | ✓ API |
| monetary.dgs10 | Monetary / 10Y Treasury yield | scripts/fetch_macro.py | ✓ API |
| monetary.dfii10 | Monetary / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py | ✓ API |
| monetary.t10yie | Monetary / 10Y breakeven inflation rate | scripts/fetch_macro.py（FRED 直接） | ✓ API |
| monetary.wti | Monetary / WTI crude oil price | scripts/fetch_macro.py | ✓ API |
| monetary.cpi_yoy | Monetary / CPI YoY: FRED | scripts/fetch_macro.py（yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary / 5y5y forward inflation expectation | scripts/fetch_macro.py | ✓ API |
| monetary.term_premium | Monetary / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary / 美債標售需求（auction tail / bid-to-cover） | WebSearch（14d） | ✗ NOT DISCLOSED（搜尋完成，窗內無顯著標售結果） |
| monetary.fedwatch | Monetary / Fed funds rate path expectations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary / Fed balance sheet: FRED | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | Monetary / Global central bank liquidity cross-check | scripts/fetch_macro.py | ✓ API（ECBASSETSW ok；JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED（搜尋完成，30 日內無披露） |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED（僅取得 Microsoft；Alphabet、Amazon、Meta 本次未取得） |
| ai.token_growth | AI / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch；quarterly_state stock-of-state＋event_scan 30d | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI / 資本週期階段（capital cycle stage） | WebSearch；quarterly_state 無增速證據、event_scan 30d 完成 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculation / Search for past 7 days: AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED（1 件合格：Agility Robotics SPAC 合併完成） |
| speculation.ipo_heat | Speculation / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculation / Microcap thematic moonshots | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculation / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculation / Insider selling at AI / market-leadership companies | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculation / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED（僅半導體 3 倍多頭基金；其餘代碼未分列） |
| structural.us_single_stock_etf | Structural / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural / 0DTE option volume | WebSearch（Cboe 月報） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API |
| structural.margin_debt_crosscheck | Structural / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural / Bank loans to nondepository financial institutions | scripts/fetch_macro.py | ✓ API |
| structural.treasury_basis_trade | Structural / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py 三區塊（aggregation any） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻 P/E 約 28.3（原定來源：Mag 7 weighted P/E） | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ （Vested Finance） | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein TSM 目標價 554 → 600；EPS／PE 拆解未披露 | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/ （StockAnalysis） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html （CNBC） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 五年期 CDS 突破 1,289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds （Coinpaper） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | RSP 年初至今報酬約 14.13% | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY （Total Real Returns） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration （Chartrow） | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 1,474 對下跌 1,252 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ （McClellan） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 22（極度恐懼；原定來源 CNN） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ （FinHacker） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 1.48 兆美元、YoY 約 31.4% | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt （thetrading.tools，原定來源 FINRA） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives （AAII） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔（TSLA、AMD、MU 等） | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week （Benzinga） | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 12 月升息 25 bps 機會 76.8% | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ （24/7 Wall St.） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000（單位依來源） | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee （BigGo Finance） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年 capex 指引約 175 → 約 170（下修；URL 標題期別不一致） | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex （Global Data Center Hub） | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3（S-1 相關報導） | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html （Yahoo Finance） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle RPO 638（十億美元） | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ （Motley Fool） | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87 | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends （GetDeploying） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 今年以來發債約 296（十億美元） | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era （404K Research） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 2026-10-29 起一週內 5 筆 AI 相關債券發行合計約 67（十億美元） | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era （404K Research） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic 65＋OpenAI 約 70，合計約 135（十億美元）；分母本次僅 Microsoft 可得，缺口不計算 | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html （Yahoo Finance） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] Microsoft 於 10 月取消 Nscale 英國資料中心交易，規模約 3（單位依來源） | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 （Investing.com／Bloomberg） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件：Agility Robotics 完成 SPAC 合併 | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ （Securities.io） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO 週漲 8% | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears （Renaissance Capital） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | 0 件符合 2+ 熱門主題×弱基本面 | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers（窗內無合格標的） | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆美元 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 （Built In） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描 0 件合格 | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表（窗內無具名申報人、交易日、金額等 filing-level 細節） | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe 股票選擇權賣買權比升至 1.05 | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide （Seeking Alpha） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭基金 10 月底規模 24.31、當月淨流入 7.27（單位依來源） | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html （Yahoo Finance） | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市 0 件 | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿（窗內無合格核准或上市） | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 （Cboe via PR Newswire） | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 總結算量 1,486,062,415 口（2026-09 月資料） | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report （OCC） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性創高 20.93 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 （Saxo） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 交叉檢核基數約 1.48 兆美元（2026-09 月資料） | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt （thetrading.tools） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.ai_infrastructure_debt | ING 出售 12 筆資料中心貸款，規模約 500（單位依來源） | AI data center debt financing private credit November 2026 | https://www.cnbc.com/2026/11/06/ing-ai-data-center-loans-debt.html （CNBC） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-11-08",
  "iso_week": "2026-W45",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "yes",
  "horizon_end": "2027-05-09",
  "prior_date": "2026-10-18",
  "prior_answer": "yes",
  "flip_evidence": [],
  "r1_drawdown_pct": 13.56,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

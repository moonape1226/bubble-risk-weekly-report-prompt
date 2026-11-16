> [DRY RUN] this report was not committed to archive.

# 2026-08-20 AI 泡沫破裂預測報告

報告日期：2026-08-20｜ISO 週次：2026-W34｜預測窗口：2026-08-20 → 2027-02-18｜前次基準：report-2026-08-17（3天前）

## 結論

**結論：no**

三條路徑目前都離觸發很遠：NASDAQ-100 自 52 週高點只回撤 4.03%，還要再跌約 21.85% 才到 R1 門檻；沒有任何 hyperscaler 下修 capex 指引的報導（R2）；HY OAS 2.75%、IG OAS 0.82%，repo 資金壓力（SOFR−IORB）0bp，看不出 R3 需要的信用壓力傳導。估值與擁擠度很高，說明泡沫存在、一旦破裂跌幅會很大，但本次證據裡找不到能讓任一路徑在 182 天內完成的觸發點，因此維持基準率判斷。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,426.02（2026-08-19），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 4.03%。R1 門檻水位為 22,995.45，從最新收盤還要再跌約 21.85% 才會觸及（`valuation.ndx_drawdown`）。

估值與價格延伸都在高檔：S&P 500 trailing P/E 29.8、Shiller CAPE 41.72（`valuation.sp500_pe_cape`，2026-08-19）；S&P 500 7,707.98 高於 200 日均線 8.75%、高於 52 週均線 10.25%（`valuation.sp500_trend`，2026-08-19）；Mag 7 加權 P/E 約 29.5x（`valuation.mag7_multiples`）。擁擠度方面，BofA 8 月 FMS 現金水位 3.5%，最擁擠的交易是做多半導體（53%）（`institutional.bofa_jpm_survey`）；美股槓桿 ETF 總 AUM 創新高約 $198bn（`structural.leveraged_etf_aum`）；SPX 0DTE 佔比創紀錄約 62%（`structural.zero_dte`）。

不過短期市場沒有失序的跡象。VIX 15.84，期限結構維持 contango（`structural.cross_asset_derivatives`）；VIX／S&P 500 同向上漲警訊沒有出現（2026-08-11 → 2026-08-18，VIX +3.66%、S&P 500 −0.47%，comove=false，`structural.vix_spx_comove`）。MOVE 71.26，比前次基準的 75.63 低（`structural.treasury_basis_trade`）。10Y 殖利率 4.71%（ΔDGS10 −1bp，`monetary.dgs10`）、實質殖利率 2.41%（ΔDFII10 −3bp，`monetary.dfii10`）、breakeven 2.30%（ΔT10YIE +2bp，`monetary.t10yie`）。由於三個序列的比較窗口不一致，這次的變動來源判讀為不可判（視窗不一致）。10Y 期限溢價（term premium）0.8393%（Kim-Wright，2026-08-14，trailing 7 日 +1.4bp，`monetary.term_premium`）。CPI YoY 3.3%（2026-07，`monetary.cpi_yoy`），加上 Fed funds 目標區間 3.50%–3.75%（`monetary.fed_funds`），代表萬一 AI 主導的下跌發生，Fed 能緩衝的空間有限。

**判讀：** R1 離門檻還很遠（還要再跌約 21.85%）。窗口內要觸發，大概需要一個外部催化劑：AI 營收或 capex 預期突然重新定價、10 月 Anthropic IPO 大量供給引發 AI 股重新估值，或者信用與資金市場開始傳導壓力。高估值與擁擠部位會放大跌幅，但目前沒有證據顯示這樣的催化劑已經啟動。

### R2 資本支出收縮

本次搜尋只拿到 top-4 hyperscaler 2026 年 capex 合計約 $725bn（valueaddvc，2026-08-13，`ai.hyperscaler_capex`），沒有拆分到各家的指引數值：

- Microsoft：最新指引未在本次證據中個別取得；方向無法個別判定，本次證據中沒有下修報導。
- Alphabet：最新指引未在本次證據中個別取得；方向無法個別判定，本次證據中沒有下修報導。
- Amazon：最新指引未在本次證據中個別取得；方向無法個別判定，本次證據中沒有下修報導。
- Meta：最新指引未在本次證據中個別取得；方向無法個別判定，本次證據中沒有下修報導。

依本次證據，四家中已下修的家數為 0。具體的下次財報日期不在本次證據中；以季報節奏推算，窗口內（到 2027-02-18）會有一到兩次季報可能改變指引。需求面仍然強勁：GPU 現貨租金超過合約價 2 倍，新增產能正在被利用率吸收（`ai.compute_supply_demand`，2026-08-13）；Anthropic 年化營收達 $65B、OpenAI 達 $40B（`ai.openai_anthropic_revenue`，2026-08-17），Anthropic run-rate 年增約 7 倍（`ai.token_growth`）。另一方面，AI 營收對 capex 缺口（revenue-to-capex gap）是年化 AI 終端營收約 $105bn 對年化 capex 約 $725bn（分母：top-4，不含 Oracle 與 neocloud；`ai.revenue_capex_gap`）。這是本次新的組合讀數，沒有更早的組合可比，所以無法判定缺口在擴大還是收斂。

**判讀：** R2 目前沒有往觸發方向移動。需要至少兩家在窗口內的季報中下修指引，而現有證據（GPU 租金、利用率、AI 營收成長）都指向需求仍在吸收供給。最可能改變這點的情況是：R1 大幅下跌或融資成本跳升，迫使管理層收斂 capex。

### R3 AI 信用事件

本次的 AI 信用定價分歧掃描（14 日）與 AI infrastructure debt financing / vendor-financing loops 掃描（30 日）都完成了，但都沒有找到窗口內的披露。因此本次沒有個別 AI 基礎設施借款人的債券殖利率、利差、CDS、評等變動、到期牆或違約徵兆可引用。整體信用與資金市場維持平靜：HY OAS 2.75%（+5bp，`monetary.hy_oas`）、IG OAS 0.82%（+1bp，`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）0.0bp、SOFR99−IORB 7.0bp（同為 2026-08-18），SRF 動用（Standing Repo Facility usage）$0.001bn（2026-08-19，`monetary.repo_stress_srf`）；銀行對 NBFI 放款 $2.02T，持平（2026-08-05，`structural.nbfi_bank_loans`）。槓桿基金美債期貨淨空單 −7,250,927 口，4 週減少 311,947 口（2026-08-11），OFR tri-party repo transaction volume $2,361.6bn（`structural.treasury_basis_trade`），看不出美債基差交易槓桿（Treasury basis-trade leverage）的平倉壓力。

**判讀：** R3 沒有任何可觀察的前兆。要在窗口內成立，需要一家 AI 資料中心／算力為主業的大型借款人進入破產、違約或 distressed exchange，而在那之前通常會先看到利差急速走闊、評等下調或再融資失敗的報導，本次都沒有。最主要的不確定性是本次缺乏個別發行人的信用定價資料（見資料缺漏）。

## 支持 yes 的證據

- [R1] 估值處於歷史極端：Shiller CAPE 41.72、trailing P/E 29.8（2026-08-19，`valuation.sp500_pe_cape`），S&P 500 高於 200 日均線 8.75%（2026-08-19，`valuation.sp500_trend`）。一旦有催化劑，下跌空間很大。
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）很大：年化 AI 終端營收約 $105bn 對年化 capex 約 $725bn（分母：top-4，`ai.revenue_capex_gap`，2026-08-17），回本仰賴營收持續爆發性成長。
- [R1] 部位擁擠：BofA 8 月 FMS 現金 3.5%，最擁擠交易是做多半導體 53%（2026-08-18，`institutional.bofa_jpm_survey`）；槓桿 ETF AUM 創新高約 $198bn，其中 TQQQ $37.3bn、SOXL $17.3bn（2026-08-17，`structural.leveraged_etf_aum`）；SPX 0DTE 佔比創紀錄約 62%（2026-08-14，`structural.zero_dte`）。
- [R1] 窗口內有大型 AI 股權供給事件：Anthropic 目標 10 月 IPO、估值約 $2T（2026-08-17，`speculation.upcoming_ai_ipos`），可能吸走資金或迫使市場重新定價 AI 估值。
- [R1] 槓桿偏高：FINRA margin debt（2026-07）年增約 +38.6%（`retail.margin_debt`），接近歷史頂部常見的 +40–50% 區間；top-10 集中度約 40%（`breadth.top10_concentration`）。
- [整體] Fed 緩衝空間有限：CPI YoY 3.3%（2026-07，`monetary.cpi_yoy`）、10Y 期限溢價（term premium）0.8393%（2026-08-14，`monetary.term_premium`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.03%（2026-08-19），離 R1 門檻 22,995.45 還要再跌約 21.85%（`valuation.ndx_drawdown`）。
- [R3] 信用與資金市場平靜：HY OAS 2.75%、IG OAS 0.82%（2026-08-18，`monetary.hy_oas`、`monetary.ig_oas`）；SOFR−IORB 0.0bp、SRF 動用 $0.001bn（`monetary.repo_stress_srf`）。看不到信用事件需要的壓力傳導。
- [R2] 需求仍在吸收供給：GPU 現貨租金超過合約價 2 倍、產能被利用率吸收（2026-08-13，`ai.compute_supply_demand`）；Anthropic 年化營收 $65B、OpenAI $40B（2026-08-17，`ai.openai_anthropic_revenue`）；Anthropic run-rate 年增約 7 倍（`ai.token_growth`）。本次證據中沒有任何 hyperscaler 下修 capex 的報導，top-4 合計約 $725bn（`ai.hyperscaler_capex`）。
- [整體] 情緒沒有到亢奮：CNN Fear & Greed 56（Greed，2026-08-19，`retail.fear_greed`）；AAII 偏空 37.9% 高於偏多 34.7%（2026-08-12，`retail.aaii`）；equity put/call 0.65（2026-08-17，`speculation.equity_put_call`）；+AI 改名／SPAC 與 microcap moonshot 掃描都是 0 件（`speculation.ai_rename_spac`、`speculation.microcap_moonshots`）。
- [整體] 市場廣度健康：RSP YTD 領先 SPY 約 5pp（`breadth.rsp_spy`）；A/D 線創新高、新高多於新低（2026-08-14，`breadth.advance_decline`）。這不是只靠少數權值股撐盤的末段行情。
- [整體] 波動與債市槓桿沒有警訊：VIX／S&P 500 同向上漲未出現（comove=false，`structural.vix_spx_comove`）；MOVE 71.26，槓桿基金美債期貨淨空單 4 週減少 311,947 口（`structural.treasury_basis_trade`）。

## 與前期比較

前次結論：無前次預測（report-2026-08-17 為舊格式評分報告）

report-2026-08-17 是舊格式的評分報告，它的分數不會被換算成 yes/no，所以本次沒有可比較的前次答案，flip_evidence 為空。和 2026-08-17 相比，市場資料的變動如下：

- S&P 500 由 7,745.06 降到 7,707.98（−0.48%）；NASDAQ-100 由 2026-08-17 的收盤小幅回落，距 52 週高點回撤 4.03%。
- HY OAS +5bp 到 2.75%、IG OAS +1bp 到 0.82%，幅度很小。
- VIX 由 15.19 升到 15.84；MOVE 由 75.63 降到 71.26。
- WALCL、ECB、BOJ 資產負債表與銀行對 NBFI 放款都沒有新觀測（持平）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源的掃描都完成了，但沒有合格的當期披露（✗ NOT DISCLOSED）。它們不會被引用為證據：

- valuation.analyst_tp_decomposition、retail.social_sentiment、retail.naaim、monetary.pboc、ai.customer_concentration_rpo、ai.depreciation_life、structural.global_leveraged_approvals：屬於輔助訊號，即使補上也不太可能改變結論。
- valuation.ai_credit_schism、structural.ai_infrastructure_debt：這兩個是 R3 的核心來源，缺漏可能影響判斷。如果出現個別 neocloud 利差急速走闊或再融資困難的披露，R3 的距離會明顯縮短。目前整體 HY／IG 利差平靜，所以本次不改變答案。
- monetary.private_credit_liquidity：過去 30 日沒有 redemption-request ratio、gate proration / breach 或 net inflow→outflow flip 的披露。
- ai.hyperscaler_financing_mix（quarterly_state 有值：capex 已超過 FCF、2026 年 hyperscaler IG 發債約 $182bn；event_scan 30 日內沒有新事件）與 ai.capital_cycle（quarterly_state 有值：供給側 capex 年增約 77%；event_scan 30 日內沒有取消／延後事件）：依 component_aggregation all 規則，Coverage 為 ✗ NOT DISCLOSED。它們的季度狀態只作背景：hyperscaler 融資結構（capex vs FCF / 發債）正轉向舉債，長期來看會提高 R3 的脆弱度。

最大的不確定性：

1. R2 的各家指引沒有拆分：本次只有 top-4 合計 capex，下一次季報的指引方向是 R2 最關鍵的變數。如果有兩家下修，答案會直接偏向 yes。
2. 10 月 Anthropic IPO：約 $2T 的股權供給加上市場重新定價，可能成為 R1 的催化劑，會把答案推向 yes；如果發行順利，反而可能延續漲勢。
3. 部分搜尋結果的日期有歧義：breadth.rsp_spy 的 URL 路徑顯示 2026-06-10，但結果標示資料日期 2026-08-17；monetary.fedwatch 的 URL 路徑顯示 2026-08-07，但標示 2026-08-19。這兩項都不是決定性證據，不影響答案。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7707.98 | FRED API (series_id=SP500) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線偏離 %） | 8.75 | FRED API (series_id=SP500) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線偏離 %） | 10.25 | FRED API (series_id=SP500) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend prior_spot（前次基準收盤） | 7745.06 | FRED API (series_id=SP500) | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較前次 %） | -0.48 | FRED API (series_id=SP500) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29426.02 | FRED API (series_id=NASDAQ100) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 4.03 | FRED API (series_id=NASDAQ100) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1，家庭股權配置 %） | 45.76080873390133（≈45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.75 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 5.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.82 | FRED API (series_id=BAMLC0A0CM) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM delta_bps | 1.0 | FRED API (series_id=BAMLC0A0CM) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.71 | FRED API (series_id=DGS10) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | -1.0 | FRED API (series_id=DGS10) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.41 | FRED API (series_id=DFII10) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | -3.0 | FRED API (series_id=DFII10) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.3 | FRED API (series_id=T10YIE) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | 2.0 | FRED API (series_id=T10YIE) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（美元／桶） | 86.48 | FRED API (series_id=DCOILWTICO) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-20T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.32 | FRED API (series_id=T5YIFR) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（%，Kim-Wright） | 0.8393 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 日） | 1.4 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.65 | FRED API (series_id=SOFR) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.72 | FRED API (series_id=SOFR99) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-20 | 2026-08-20T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.001 | FRED API (series_id=RPONTTLD) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps | 0.0 | fetch_macro.py repo_stress (FRED-derived) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr99_iorb_bps | 7.0 | fetch_macro.py repo_stress (FRED-derived) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.walcl | WALCL latest（百萬美元） | 6,759,955（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-12 | 2026-08-20T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（百萬歐元） | 5,927,307（€5.93T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-14 | 2026-08-20T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（億日圓） | 6,442,957（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-20T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.84 | FRED API (series_id=VIXCLS) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of；base_date 2026-08-11，comove=false） | 15.84 | fetch_macro.py vix_spx_comove (FRED-derived) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 3.66 | fetch_macro.py vix_spx_comove (FRED-derived) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -0.47 | fetch_macro.py vix_spx_comove (FRED-derived) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（十億美元，持平） | 2016.0821（$2.02T） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-05 | 2026-08-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7,250,927 | CFTC TFF (cftc_lev_funds) | 2026-08-11 | 2026-08-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 311,947 | CFTC TFF (cftc_lev_funds) | 2026-08-11 | 2026-08-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 71.26 | Yahoo chart ^MOVE (move_index) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index prior | 75.63 | Yahoo chart ^MOVE (move_index) | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2361.6 | OFR STFM (ofr_repo) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值 / S&P 500 P/E and Shiller CAPE | multpl / GuruFocus [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值 / Mag 7 weighted P/E and AI leader P/S | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值 / Analyst TP upgrade decomposition | 賣方摘要 WebSearch（90d＋same quarter） | ✗ NOT DISCLOSED（掃描完成，無合格當季 TP 上調） |
| valuation.sp500_trend | 估值 / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500，sp500_trend block） | ✓ API |
| valuation.ndx_drawdown | 估值 / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100，ndx_drawdown block） | ✓ API |
| valuation.ai_credit_schism | 估值 / AI 信用定價分歧 | 信用市場 WebSearch（14d） | ✗ NOT DISCLOSED（掃描完成，14 日內無合格披露） |
| breadth.rsp_spy | 廣度 / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度 / Top-10 concentration in S&P 500 | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度 / Advance/decline ratio, new high/low ratio | StockCharts WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶 / CNN Fear & Greed Index | CNN [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶 / Margin Debt: FINRA monthly data | FINRA / GuruFocus WebSearch | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶 / Retail survey: AAII Investor Sentiment | AAII [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶 / Social sentiment proxies | WSB / X WebSearch（7d） | ✗ NOT DISCLOSED（掃描完成，無顯著討論） |
| retail.household_equity_allocation | 散戶 / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶 / NAAIM Exposure Index | naaim.org [primary: SEARCH] | ✗ NOT DISCLOSED（未找到當週數值） |
| institutional.bofa_jpm_survey | 機構 / BofA Fund Manager Survey and JPM institutional survey | BofA / JPM WebSearch | ✓ SEARCH-VERIFIED（BofA 8 月 FMS；JPM 未找到） |
| monetary.fed_funds | 貨幣 / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣 / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣 / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣 / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣 / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣 / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直接取得） | ✓ API |
| monetary.wti | 貨幣 / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣 / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣 / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣 / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣 / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD；repo_stress block） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣 / 美債標售需求（auction tail / bid-to-cover） | Reuters / TreasuryDirect [primary: SEARCH]（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣 / Fed funds rate path expectations | CME FedWatch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣 / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣 / Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣 / PBoC aggregate financing | PBoC / NBS WebSearch | ✗ NOT DISCLOSED（無當期英文摘要） |
| monetary.private_credit_liquidity | 貨幣 / Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]（30d） | ✗ NOT DISCLOSED（30 日內無合格披露） |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | 財報摘要 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI / AI token volume growth rate | 供應商披露 WebSearch | ✓ SEARCH-VERIFIED |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | CNBC / The Information WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話 [primary: SEARCH] | ✗ NOT DISCLOSED（無合格披露） |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | 產業披露 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構（capex vs FCF / 發債） | 財報 / 發債 [primary: SEARCH]；quarterly_state stock_of_state，event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口（revenue-to-capex gap） | 綜合披露 [primary: SEARCH]（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動 | 10-K / 10-Q [primary: SEARCH]（30d） | ✗ NOT DISCLOSED（30 日內無年限變動） |
| ai.capital_cycle | AI / 資本週期階段（capital cycle stage） | 產業披露 [primary: SEARCH]；quarterly_state stock_of_state，event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機 / Search for past 7 days: AI rename / SPAC / no-revenue IPO | 新聞 WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機 / IPO market heat | Renaissance Capital WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機 / Microcap thematic moonshots | Finviz / Benzinga [primary: SEARCH]（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機 / Upcoming AI IPOs | Bloomberg / CNBC / Yahoo WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機 / Insider selling at AI / market-leadership companies | SEC EDGAR [primary: SEC EDGAR]（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機 / Cboe equity-only put/call ratio | Cboe [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構 / US leveraged ETF AUM | etf.com / ETFGI [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構 / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com WebSearch（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | 結構 / Global leveraged product approvals | KRX / TWSE / JPX / ESMA WebSearch（7d） | ✗ NOT DISCLOSED（7 日內無英文披露） |
| structural.zero_dte | 結構 / 0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構 / Options total volume | OCC WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構 / Cross-asset derivatives / correlation checks | Cboe / SpotGamma WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構 / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove block） | ✓ API |
| structural.margin_debt_crosscheck | 結構 / Cross-reference only: FINRA margin debt | FINRA WebSearch（交叉檢核） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構 / AI infrastructure debt financing / vendor-financing loops | 信用市場 [primary: SEARCH]（30d） | ✗ NOT DISCLOSED（30 日內無新披露） |
| structural.nbfi_bank_loans | 結構 / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構 / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）＋WebSearch | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok；WebSearch 無額外平倉事件） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.8、Shiller CAPE 41.72（原定來源 multpl / GuruFocus） | S&P 500 Shiller CAPE August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio （GuruFocus） | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E 約 29.5x | Magnificent 7 weighted P/E August 2026 | https://www.fool.com/investing/2026/08/14/the-best-magnificent-seven-stocks-to-buy-in-august/ （Motley Fool） | 2026-08-14 | 2026-08-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 領先 SPY 約 5pp（URL 路徑日期 2026-06-10，結果標示資料日期 2026-08-17） | RSP vs SPY YTD 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St.） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 top-10 集中度約 40% | S&P 500 top 10 concentration 2026 | https://www.ebc.com/forex/rsp-vs-spy （EBC） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| breadth.advance_decline | A/D 線創新高、新高多於新低，3 項廣度訊號確認多頭 | NYSE advance decline breadth August 2026 | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/ （StockCharts） | 2026-08-14 | 2026-08-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 56（Greed） | CNN Fear and Greed today August 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-07 月資料）水位約 1,417,225（百萬美元，≈$1.42T）、YoY 約 +38.6% | FINRA margin debt July 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt （GuruFocus，原定 FINRA） | 2026-07-31 | 2026-08-20T09:30:00+08:00 |
| retail.aaii | AAII 偏空 37.9%、偏多 34.7% | AAII investor sentiment August 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-08-12 | 2026-08-20T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA 8 月 FMS：現金 3.5%、最擁擠做多半導體 53% | BofA fund manager survey August 2026 | https://www.hedgefundtips.com/august-2026-bank-of-america-global-fund-manager-survey-results-summary/ （HedgeFundTips 摘要） | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 標售 bid-to-cover 2.39、無明顯 tail | US Treasury 30-year auction August 2026 | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2026/R_20260813_2.pdf （TreasuryDirect） | 2026-08-13 | 2026-08-20T09:30:00+08:00 |
| monetary.fedwatch | FedWatch 9/16 按兵不動約 65.4%（URL 路徑日期 2026-08-07，結果標示資料日期 2026-08-19） | CME FedWatch September 2026 hold probability | https://www.cnbc.com/2026/08/07/odds-the-fed-hikes-in-september-tumble-following-big-july-jobs-miss.html （CNBC） | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| ai.hyperscaler_capex | top-4（MSFT、GOOGL、AMZN、META）2026 capex 合計約 $725bn（未拆分各家） | hyperscaler 2026 capex guidance Microsoft Google Amazon Meta | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-13 | 2026-08-20T09:30:00+08:00 |
| ai.token_growth | Anthropic run-rate 年增約 7 倍、API 佔營收 80% | Anthropic token growth revenue 2026 | https://techcrunch.com/2026/08/17/anthropics-annualized-revenue-surges-to-65b/ （TechCrunch） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| ai.openai_anthropic_revenue | OpenAI $40B、Anthropic $65B 年化營收 | OpenAI Anthropic annualized revenue August 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html （CNBC） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| ai.compute_supply_demand | GPU 現貨租金超過合約價 2 倍、產能被利用率吸收 | AI GPU rental pricing utilization August 2026 | https://www.uncoveralpha.com/p/amazon-google-microsoft-meta-q2-earnings （UncoverAlpha） | 2026-08-13 | 2026-08-20T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] capex 已超過 FCF、2026 hyperscaler IG 發債約 $182bn（+1300%） | hyperscaler external financing capex FCF debt 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow （FactSet） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $105bn（OpenAI 40＋Anthropic 65）vs 年化 capex 約 $725bn（分母：top-4） | AI revenue to capex gap 2026 | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| ai.capital_cycle | [quarterly_state] 供給側 capex 年增約 77%，需求側 token／營收成長並存 | AI capex growth rate supply demand 2026 | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-13 | 2026-08-20T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收投機 IPO 7 日掃描：0 件合格 | AI rename SPAC ticker change August 2026 | Renaissance Capital / SEC EDGAR / 新聞掃描 | — | 2026-08-20T09:30:00+08:00 |
| speculation.ipo_heat | US IPO 週報：pipeline 擴大、Metals Royalty 直接上市；無營收 AI IPO 暴衝 0 起 | US IPO weekly recap August 2026 | https://www.renaissancecapital.com/IPO-Center/News/118238/US-IPO-Weekly-Recap-Pipeline-swells-with-sizable-IPO-filings-as-Metals-Roya （Renaissance Capital） | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot（單日 ≥100%、市值 <$1B、2 個以上主題、弱基本面）7 日掃描：0 檔合格 | microcap 100% single day surge quantum AI August 2026 | Finviz / Benzinga / StockTwits movers 掃描 | — | 2026-08-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 10 月 IPO、估值約 $2T | Anthropic OpenAI IPO 2026 | https://finance.yahoo.com/markets/article/spacex-openai-and-anthropic-here-are-the-most-anticipated-ipos-in-2026-114439441.html （Yahoo Finance） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 14 日內合格 Form 4 集中賣出：0 件 | insider Form 4 AI executives August 2026 | SEC EDGAR / openinsider 掃描 | — | 2026-08-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.65（來源未標明是單日或 5 日均值） | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio （thetrading.tools） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美股槓桿 ETF 總 AUM 創新高約 $198bn；TQQQ $37.3bn、SOXL $17.3bn | leveraged ETF AUM record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| structural.us_single_stock_etf | 美股單一個股槓桿 ETF 30 日新核准／上市：0 件 | single-stock leveraged ETF launch SEC August 2026 | SEC EDGAR / ETF.com new launches 掃描 | — | 2026-08-20T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 8 月佔比創紀錄約 62% | 0DTE SPX volume share August 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august （Cboe） | 2026-08-14 | 2026-08-20T09:30:00+08:00 |
| structural.options_volume | OCC 7 月總量年增 +26%、YTD 日均超過 71M 口（2026-07 月資料） | OCC July 2026 options volume | https://mondovisione.com/media-and-resources/news/occ-july-2026-monthly-volume-data-202686 （Mondo Visione） | 2026-07-31 | 2026-08-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 15.84、期限結構 contango、SKEW 偏高 | VIX term structure SKEW August 2026 | https://www.thetrading.tools/vix-term-structure （thetrading.tools） | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt／市值交叉檢核（2026-07 月資料，YoY +38.6%，主讀數見 retail.margin_debt） | FINRA margin debt equity market cap ratio 2026 | https://kalkine.com/news/financial/finra-margin-debt-hits-record-15-trillion-ratio-climbs-to-340 （Kalkine） | 2026-07-31 | 2026-08-20T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-20",
  "iso_week": "2026-W34",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-18",
  "prior_date": "2026-08-17",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 4.03,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

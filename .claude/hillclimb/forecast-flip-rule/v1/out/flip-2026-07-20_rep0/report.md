> [DRY RUN] this report was not committed to archive.

# 2026-07-20 AI 泡沫破裂預測報告
報告日期：2026-07-20｜ISO 週次：2026-W30｜預測窗口：2026-07-20 → 2027-01-18｜前次基準：report-2026-07-16（4天前）

## 結論

**結論：no**

三條路徑目前都還離觸發很遠：NASDAQ-100 只比 52 週高點低 6.74%，要再跌約 19.58% 才會碰到 R1；四家 hyperscaler 都沒有下修 capex 指引，2026 年合計約 $700B，而且還在上修（R2）。AI 借款人的 CDS 確實走闊（Oracle 約 198bp、CoreWeave 約 665bp），但 HY OAS 2.71%、repo 也很平靜，看不到能在窗口內推到違約或 distressed exchange 的傳導鏈，所以 yes 的舉證門檻沒有達到。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

依 `valuation.ndx_drawdown`：NASDAQ-100 在 2026-07-17 收 28,592.66。252 個交易日內的最高收盤是 2026-06-02 的 30,660.60，距 52 週高點回撤 6.74%。R1 門檻是 22,995.45，從最新收盤還要再跌約 19.58% 才會觸及。前次報告時的回撤是 3.78%，四天內擴大約 3 個百分點，主因是 2026-07-17 的晶片股賣壓：NYSE 下跌家數約為上漲的 2 倍（`breadth.advance_decline`）。S&P 500 從前次的 7,533.77 跌到 7,457.69（−1.01%），但仍比 200 日均線高 6.73%（`valuation.sp500_trend`）。VIX 在 7 日窗口內從 15.03 升到 18.77（+24.88%），同期 S&P 500 −1.55%，屬於正常的反向波動，不是 crowded-optionality 式的同向上漲（`structural.vix_spx_comove`）。

脆弱度方面：CAPE 41.52、trailing P/E 32.08（`valuation.sp500_pe_cape`）；margin debt $1.416T，YoY +53.7%（`retail.margin_debt`），已落在歷史頂部常見的 +40–50% 區間之上；NAAIM 95.64（`retail.naaim`）顯示部位擁擠。一旦下跌啟動，跌幅可能很大。

**判讀：** R1 尚未接近，還差約 19.58%。要在窗口內完成，需要一個能把指數再壓低約兩成的催化：AI 信用事件外溢、capex 指引轉向，或高槓桿部位被迫去化。目前這些催化都看不到已經啟動的證據；本次的回落比較像高估值下的正常修正。

### R2 資本支出收縮

依 `ai.hyperscaler_capex`（沿用最近一季財報後的彙整，資料日 2026-05-15）：Microsoft、Alphabet、Amazon、Meta 合計 2026 capex 約 $700B，最近一次指引的方向是上修。這份彙整沒有逐家列出 FY 指引數字，因此逐家狀態只能這樣寫：

- Microsoft：彙整列入整體上修，沒有下修的報導；逐家 FY 數字本次未取得。
- Alphabet：同上，沒有下修的報導。
- Amazon：同上，沒有下修的報導。
- Meta：同上，沒有下修的報導。

目前四家中下修的家數為 0。需求端也沒有轉弱：伺服器 DRAM 3Q26 合約價 QoQ +13–18%（`ai.compute_supply_demand`），沒有看到 order digestion 或利用率下滑的證據。下一輪季報（2026 年 7 月下旬至 8 月初、以及 10 月下旬至 11 月初）都在窗口內，但本次證據沒有逐家的確切財報日期。

**判讀：** R2 離觸發最遠。要成立，需要兩家在窗口內把 FY 指引改成下修；從上修直接翻成下修，通常要先有 R1 級的股價衝擊或資金成本跳升，本次沒有看到前兆。

### R3 AI 信用事件

依 `valuation.ai_credit_schism`（2026-07-16）：Oracle 5 年期 CDS 約 198bp，創紀錄；CoreWeave CDS 約 665bp。這是 AI 信用定價分歧（equity-vs-credit schism）中「信貸端開始重定價」的後期訊號。CoreWeave 以 AI 算力為主業，負債規模足以符合 R3 門檻，是最可能觸發 R3 的借款人。不過本次沒有取得違約、寬限期付款違約、covenant waiver 或 distressed exchange 的報導。這次 30 日掃描也沒有找到新的 AI infrastructure debt financing / vendor-financing loops 披露，因此沒有可引用的到期牆或再融資事件。外圍信貸沒有出現系統性緊張：HY OAS 2.71%（`monetary.hy_oas`）、IG OAS 0.78%（`monetary.ig_oas`）都很窄；SOFR−IORB 為 −3bp、SOFR99−IORB 為 +5bp、SRF 動用 0（`monetary.repo_stress_srf`）。值得注意的是私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）：Blue Owl OCIC 第二季 redemption-request ratio 為 18.8%，按 5% quarterly redemption cap 比例撥付，屬於 gate proration / breach（`monetary.private_credit_liquidity`，2026-07-02）。

**判讀：** R3 是三條路徑中最接近的一條，但仍然是「定價走闊」，不是「事件發生」。以 665bp 的 CDS 來看，市場隱含的壓力不低；要在窗口內觸發，仍需要再融資失敗或流動性斷裂，最終走到破產、違約或 distressed exchange。目前沒有證據顯示具體到期日或觸發點落在窗口內。

## 支持 yes 的證據

- [R3] Oracle 5 年期 CDS 約 198bp 創紀錄、CoreWeave CDS 約 665bp（2026-07-16）。AI 借款人的信貸端已開始重定價，是 R3 最直接的前兆；CoreWeave 符合 R3 的規模門檻 `valuation.ai_credit_schism`
- [R3] Blue Owl OCIC 2026 Q2 的 redemption-request ratio 為 18.8%，按 5% quarterly redemption cap 比例撥付（gate proration / breach，2026-07-02）。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）已經實際觸發，可能收緊 AI 借款人的私募再融資管道 `monetary.private_credit_liquidity`
- [R1] Margin debt $1.416T、YoY +53.7%（2026-05 月資料），高於歷史頂部常見的 +40–50% 區間；NAAIM 95.64（2026-07-15）。槓桿與部位擁擠會放大任何下跌 `retail.margin_debt` `retail.naaim`
- [R1] CAPE 41.52、trailing P/E 32.08（2026-07-17），估值處於歷史極端，下跌空間大 `valuation.sp500_pe_cape`
- [R1] NASDAQ-100 自 2026-06-02 高點回撤從前次的 3.78% 擴大到 6.74%（2026-07-17）；7/17 晶片股賣壓、NYSE 跌漲比約 2:1；VIX 一週升 24.88% 至 18.77 `valuation.ndx_drawdown` `breadth.advance_decline` `structural.vix_spx_comove`
- [整體] CPI YoY 3.46%（2026-06 月資料）、10Y 期限溢價（term premium）0.7788%（2026-07-10，trailing 7 日 +4.7bp），Fed 用降息緩衝 AI 主導下跌的空間有限；CME FedWatch 顯示 7/29 會議約 86.7% 機率持平 `monetary.cpi_yoy` `monetary.term_premium` `monetary.fedwatch`
- [R1] Anthropic IPO 已進入投資人會議階段，估值約 $965B、可能 10 月掛牌（2026-07-15），窗口內可能出現大規模股權供給 `speculation.upcoming_ai_ipos`

## 支持 no 的證據

- [R1] NASDAQ-100 最新收盤 28,592.66，距 R1 門檻 22,995.45 還要再跌約 19.58%（2026-07-17）。本次回撤只有 R1 門檻的約四分之一 `valuation.ndx_drawdown`
- [R2] 四大 hyperscaler 2026 capex 合計約 $700B，最近一次指引為上修，四家中 0 家下修（2026-05-15 彙整）。R2 需要兩家反轉，離觸發最遠 `ai.hyperscaler_capex`
- [R3] 廣義信貸沒有系統性緊張：HY OAS 2.71%、IG OAS 0.78%（2026-07-16）；SOFR 3.62% 低於 IORB 3.65%、SRF 動用 0（2026-07-17）。AI 個別名稱的 CDS 走闊尚未外溢到市場資金面 `monetary.hy_oas` `monetary.ig_oas` `monetary.repo_stress_srf`
- [R2] 需求端仍然偏緊：伺服器 DRAM 3Q26 合約價 QoQ +13–18%（2026-07-03），沒有 order digestion 或利用率下滑的訊號，不支持 capex 即將下修 `ai.compute_supply_demand`
- [整體] 散戶情緒不再狂熱：CNN Fear & Greed 37（Fear，2026-07-17）、Cboe equity put/call 0.73（2026-07-17），部分泡沫溢價已在消化；市場等寬型 RSP YTD +10.68% 領先 SPY +7.47%（2026-06-10），廣度沒有極端收窄 `retail.fear_greed` `speculation.equity_put_call` `breadth.rsp_spy`
- [整體] 端到端的 AI 營收持續成長：Anthropic 年化約 $47B、OpenAI 約 $25B（2026-05-15）。雖然仍遠低於約 $700B 的年化 capex，但需求曲線還在上升，支撐 hyperscaler 維持支出 `ai.openai_anthropic_revenue` `ai.revenue_capex_gap`
- [整體] 美債市場沒有失序前兆：MOVE 70.88（2026-07-17）、OFR tri-party repo transaction volume $2,342.6bn，美債基差交易槓桿（Treasury basis-trade leverage）沒有平倉跡象 `structural.treasury_basis_trade`

## 與前期比較

前次結論：yes（report-2026-07-16）

本次結論：翻轉

前次 forecast.json 寫於 yes_basis 欄位出現之前，沒有記錄任何決定性理由。依規則，yes 每次都要重新取得。用本次證據重新審視三條路徑後，yes 不成立：

翻轉依據：

- `valuation.ndx_drawdown`：R1 回撤從 3.78% 擴大到 6.74%，但距 R1 門檻仍差約 19.58%。四天的修正幅度不足以把「窗口內再跌約兩成」變成較可能發生的事。
- `ai.hyperscaler_capex`：四家 hyperscaler 的最近指引仍是上修，2026 合計約 $700B，0 家下修。R2 沒有任何進展，重新審視後，前次的 yes 在 R2 上找不到依據。
- `valuation.ai_credit_schism`：Oracle 與 CoreWeave CDS 走闊，是 R3 的重定價訊號，但沒有違約、寬限期付款違約或 distressed exchange 事件。單憑定價走闊，達不到「窗口內較可能完成」的門檻。
- `monetary.hy_oas`：HY OAS 2.71%，與前次持平。廣義信貸沒有重定價，表示 AI 個別名稱的壓力沒有形成跨市場傳導，三條路徑的互相觸發鏈目前並未啟動。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

標為 ✗ NOT DISCLOSED 的來源有：`valuation.analyst_tp_decomposition`、`retail.social_sentiment`、`institutional.bofa_jpm_survey`、`ai.token_growth`、`ai.customer_concentration_rpo`、`ai.hyperscaler_financing_mix`（quarterly_state 與 event_scan 都沒有披露）、`ai.depreciation_life`、`ai.capital_cycle`（兩個組件都沒有披露）、`structural.global_leveraged_approvals`、`structural.ai_infrastructure_debt`。其中與答案最相關的是 `structural.ai_infrastructure_debt` 與 `ai.hyperscaler_financing_mix`：30 日內沒有找到 AI infrastructure debt financing 或 SPV 披露，所以無法評估 R3 借款人的到期牆。若之後發現大額近期到期且再融資受阻，會把答案推向 yes；但目前沒有這方面的證據，缺漏本身不構成 yes 的依據。

其他資料限制：

- `speculation.insider_form4` 標為 0 件，但 SEC EDGAR 一手 egress 受限，篩選只能透過 openinsider 等次級來源完成。
- `ai.hyperscaler_capex` 沿用 2026-05-15 的彙整，沒有逐家的 FY 指引數字。
- `valuation.mag7_multiples`（2026-05-15）與 `structural.zero_dte`（2026-02-28）的資料日期偏舊，只能當背景。
- evidence 紀錄中，`structural.treasury_basis_trade` 的 WebSearch 結果寫的是三個 script 組件失敗；但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 都是 `status: ok`。本報告以 artifact 為準，記為 ✓ API。
- 10Y 分解：DGS10 與 DFII10 都沒有新觀測（stale_series：DGS10、DFII10），ΔT10YIE +2bp 的窗口與另外兩者不一致，判讀為不可判（視窗不一致）。

最大的不確定性：

1. 下一輪 hyperscaler 季報（7 月下旬至 8 月初）。只要有任一家 capex 指引轉為下修，R2 就從 0/4 推進，並可能觸發 R1，推向 yes。
2. CoreWeave 等 neocloud 的再融資狀況。CDS 約 665bp 代表市場已在為事件定價；若出現再融資失敗或 distressed exchange，R3 可直接解析為 yes。
3. 私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）是否擴散到更多基金。若出現多基金的 net inflow→outflow flip，AI 借款人的私募融資管道會收緊，推向 yes；反之，如果 Blue Owl 的 gate proration / breach 只是單一事件，則維持 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7457.69 | FRED API (series_id=SP500) sp500_trend | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 6.73 | FRED API (series_id=SP500) sp500_trend | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.42 | FRED API (series_id=SP500) sp500_trend | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend prior_spot（前次基準日收盤） | 7533.77 | FRED API (series_id=SP500) sp500_trend | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28592.66 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-06-02 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 6.74 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻） | 22995.45 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q1，家庭股票配置 %） | 45.76080873390133（≈45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.71 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%，no_new_obs） | 4.57 | FRED API (series_id=DGS10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%，no_new_obs） | 2.35 | FRED API (series_id=DFII10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.24 | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps（vs 2026-07-16） | 2.0 | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl） | 79.2 | FRED API (series_id=DCOILWTICO) | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料，%） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.21 | FRED API (series_id=T5YIFR) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 0.7788 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 日） | 4.7 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API (series_id=SOFR99) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.walcl | WALCL latest（百萬美元） | 6,743,028（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（百萬歐元） | 5,970,516（€5.97T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（億日圓） | 6,395,509（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 18.77 | FRED API (series_id=VIXCLS) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of） | 18.77 | FRED API vix_spx_comove block | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日窗口 %） | 24.88 | FRED API vix_spx_comove block | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日窗口 %） | -1.55 | FRED API vix_spx_comove block | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（十億美元） | 2004.0237（≈$2.00T） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7562874 | CFTC TFF futures-only cftc_lev_funds | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -78139 | CFTC TFF futures-only cftc_lev_funds | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 70.88 | Yahoo Finance chart API ^MOVE move_index | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2342.6 | OFR STFM REPO-TRIV1_TV_TOT-P ofr_repo | 2026-07-17 | 2026-07-20T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | MarketXLS WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-05-15） |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 WebSearch，90d＋同季 | ✗ NOT DISCLOSED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch，14d | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA／Advisor Perspectives WebSearch，stock-of-state | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag WebSearch，7d | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py FRED BOGZ1FL153064486Q | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／ycharts WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py DFEDTARU＋DFEDTARL | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py BAMLH0A0HYM2 | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py BAMLC0A0CM | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py DGS10 | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py DFII10 | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py T10YIE（FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py DCOILWTICO | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py CPIAUCSL yoy_pct | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py T5YIFR | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py THREEFYTP10 | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series | scripts/fetch_macro.py SOFR、SOFR99、IORB、RPONTTLD | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | Reuters／TreasuryDirect WebSearch，14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py WALCL | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py ECBASSETSW＋JPNASSETS | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing | Bloomberg WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 WebSearch，30d | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報彙整 WebSearch，stock-of-state 沿用 | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／The Information WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話 WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報 quarterly_state＋30d event_scan WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 WebSearch，stock-of-state | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K／10-Q WebSearch，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速 quarterly_state＋30d event_scan WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | WebSearch，7d | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／Benzinga／StockTitan WebSearch，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 WebSearch，30d | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR／openinsider WebSearch，14d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com／cryptobriefing WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF.com WebSearch，30d | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch，7d | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-02-28） |
| structural.options_volume | 結構｜Options total volume | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe／AInvest WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py VIXCLS＋vix_spx_comove | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | Advisor Perspectives WebSearch（交叉引用） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | WebSearch，30d | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py LNFACBW027SBOG | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds＋move_index＋ofr_repo（any） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.08（原定來源 multpl） | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 41.52（原定來源 multpl） | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E ≈40 trailing（原定來源 Mag 7 加權估值） | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026 （MarketXLS） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS ≈198bp 創紀錄、CoreWeave ≈665bp | Oracle CoreWeave CDS spread widening July 2026 | https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/ （RIA） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP +10.68% vs SPY +7.47% YTD | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （247wallst） | 2026-06-10 | 2026-07-20T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 36.40%（原定來源 State Street SPDR 持股） | S&P 500 top 10 concentration percent 2026 | https://ahasignals.com/sp500-concentration-risk/ （AHA Signals） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| breadth.advance_decline | NYSE 07-17 下跌約 2×上漲、NH 241／NL 166 | NYSE advance decline breadth July 17 2026 | https://money.usnews.com/investing/news/articles/2026-07-17/wall-st-futures-fall-as-chip-selloff-gathers-pace-netflix-tumbles （US News／Reuters） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（Fear）（原定來源 cnn.com） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed （MacroMicro） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-05 月資料）$1.416T、+53.7% YoY（原定來源 FINRA） | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |
| retail.aaii | AAII Bull 44.9% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64（原定來源 naaim.org） | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number （YCharts） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 2.59、小幅 tail（原定來源 Reuters／TreasuryDirect） | US Treasury 10Y auction July 2026 bid to cover | https://cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/ （Crypto Briefing） | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 會議持平 ≈86.7% | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch （CryptoRank 轉述 CME） | 2026-07-18 | 2026-07-20T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance （Bloomberg） | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio 18.8%，按 5% quarterly redemption cap 比例撥付（gate proration / breach） | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://whbl.com/2026/07/02/blue-owl-keeps-withdrawal-limits-even-as-redemption-pressure-modestly-eases/ （WHBL／Reuters） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| ai.hyperscaler_capex | MSFT／GOOGL／AMZN／META 2026 capex 合計 ≈$700B、指引仍上修（最近一季財報彙整） | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html （Yahoo Finance） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic ≈$47B／OpenAI ≈$25B 年化 run-rate | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 +13–18% QoQ | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html （TrendForce） | 2026-07-03 | 2026-07-20T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex ≈$700B（分母：MSFT／GOOGL／AMZN／META）vs AI 終端營收低百億級 | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| speculation.ai_rename_spac | EVTV→Azio AI（AZIO）改名、07-13 起以新代號交易 | AI rename ticker change July 2026 Azio EVTV | https://www.businesswire.com/news/home/20260710628386/en/Azio-AI-Holdings-Inc.-Nasdaq-EVTV-to-Begin-Trading-Under-New-Ticker-Symbol-AZIO-Completing-Corporate-Rebrand （Business Wire） | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD ≈200 檔 IPO、募資 $141.2B | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/ （StockAnalysis） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot 0 件 | microcap 100% single day quantum AI moonshot July 2026 | Finviz／Benzinga／StockTitan movers screener | — | 2026-07-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 投資人會議、估值 ≈$965B、可能 10 月掛牌 | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html （CNBC） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 cluster 0 件（SEC EDGAR 一手 egress 受限） | insider Form 4 cluster AI leaders July 2026 openinsider | SEC EDGAR／openinsider | — | 2026-07-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity-only put/call 0.73（日讀數） | Cboe equity put call ratio July 2026 | https://www.cboe.com/markets/us/options/market-statistics/daily/ （Cboe） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM ≈$198B（原定來源 etf.com） | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing） | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 推出 6 檔 2x GOOGL／AMZN／META／AAPL 單一個股槓桿 ETF | single-stock leveraged ETF launch July 2026 Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-07 | 2026-07-20T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權成交 ≈63% | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/ （Cboe） | 2026-02-28 | 2026-07-20T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月成交 1,603,491,559 口、+45% YoY | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 145.13、VIX ≈16.5 期限結構 contango | VIX term structure SKEW July 2026 | https://www.ainvest.com/news/0dte-volatility-drives-market-strategies-2026-2602/ （AInvest） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-05 月資料）$1.416T、+53.7% YoY（交叉引用 Retail Sentiment） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-07-20",
  "iso_week": "2026-W30",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-01-18",
  "prior_date": "2026-07-16",
  "prior_answer": "yes",
  "flip_evidence": ["valuation.ndx_drawdown", "ai.hyperscaler_capex", "valuation.ai_credit_schism", "monetary.hy_oas"],
  "yes_basis": [],
  "r1_drawdown_pct": 6.74,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

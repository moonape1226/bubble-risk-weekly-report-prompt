> [DRY RUN] this report was not committed to archive.

# 2026-10-18 AI 泡沫破裂預測報告

報告日期：2026-10-18｜ISO 週次：2026-W42｜預測窗口：2026-10-18 → 2027-04-18｜前次基準：report-2026-09-13（35天前）

## 結論

**結論：no**

三條路徑目前都還沒有完成到可在 182 天內解析為 yes 的程度：NASDAQ-100 只比 2026-10-06 的高點低 4.13%，還要再跌約 21.77% 才會觸發 R1；本次證據也沒有任何一家 hyperscaler 下修 capex 指引。最強的反向訊號是 CoreWeave 5Y CDS 在 2026-10-15 創下 1,194.5 bps 的紀錄（R3），但目前只有信用重定價，沒有付款違約、破產或 distressed exchange；在 repo 資金與 IG 信用仍然平穩的情況下，這不足以推翻低基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

FRED `NASDAQ100` 最新收盤為 29,935.59（2026-10-15）；過去 252 個交易日的最高收盤為 31,224.69（2026-10-06），距 52 週高點回撤 4.13%（`valuation.ndx_drawdown`）。R1 門檻水位為 23,418.52，也就是要從最新收盤再跌約 21.77% 才會觸發。高點只在 7 個交易日前，代表這是剛從高位回落、而非已在深度修正中。S&P 500 最新為 7,659.44（2026-10-16），仍比 200 日 MA 高 5.34%、比 52 週 MA 高 6.78%，價格延伸尚未消化（`valuation.sp500_trend`）。

脆弱度偏高：Shiller CAPE 約 40.54（`valuation.sp500_pe_cape`）；BofA 2026-10 FMS 的科技股淨加碼約 37%，為 2020 年 8 月以來最高（`institutional.bofa_jpm_survey`）。短線風險偏好已轉弱：2026-10-16 上漲家數約 29、下跌約 71（`breadth.advance_decline`），Fear & Greed 約 18，屬極度恐懼（`retail.fear_greed`），MOVE 由 82.21 升至 101.1（`structural.treasury_basis_trade`）。總經緩衝有限：Fed 目標區間上限由 3.75% 升到 4.0%（`monetary.fed_funds`），10Y 殖利率 5.1%（`monetary.dgs10`），CPI YoY 3.72%（2026-09 資料，`monetary.cpi_yoy`）。窗口內的已知催化劑是 Anthropic 目標 11 月中上市（`speculation.upcoming_ai_ipos`），會測試市場吸收大型 AI 股權供給的能力。

**判讀：** 距離觸發還很遠（約 21.77%）。要在窗口內觸發，需要信用事件（R3）或 capex 指引轉向（R2）帶動 AI 龍頭重新定價，再加上 Fed 因通膨無法降息、反而升息；單靠估值偏高與情緒轉恐懼不足以造成 25% 回撤。

### R2 資本支出收縮

本次證據只有四大 hyperscaler 2026 capex 的合計值，約 725（十億美元）（CNBC，2026-07-28，Q2 財報季；`ai.hyperscaler_capex`）。個別公司的數字與相對前次指引的方向，本次證據沒有逐家揭露：

- Microsoft：最新官方指引來自 Q2 2026 財報季（合計值的一部分）；個別數字與方向未見於本次證據。
- Alphabet：同上，屬 Q2 2026 財報季。CNBC 標題指出 Alphabet 財報後市場對 capex 的審視升高，但沒有下修的紀錄。
- Amazon：同上，屬 Q2 2026 財報季；個別數字與方向未見於本次證據。
- Meta：同上，屬 Q2 2026 財報季；個別數字與方向未見於本次證據。

本次證據中已下修的家數為 0（R2 需要至少 2 家）。窗口內會有 Q3 2026 與 Q4 2026 兩輪財報指引，但確切日期本次證據沒有提供。需求端仍有支撐：H100 隨選中位租金約 4.20（2026-10-07，`ai.compute_supply_demand`），Anthropic 年化 run-rate 約 65（十億美元）（2026-08-17，`ai.openai_anthropic_revenue`）。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 $65bn（僅 Anthropic）vs 年化 capex 約 $725bn（分母：top-4 MSFT／GOOGL／AMZN／META，未含 Oracle 與 neocloud）（`ai.revenue_capex_gap`）。這是第一次組合，沒有前值，所以無法判斷缺口在擴大或收斂。

**判讀：** 尚未啟動。需要窗口內兩輪財報中有兩家明確下修，最可能的觸發是 R1 回撤或 R3 信用事件迫使管理層轉向保守；目前的需求端證據沒有顯示這個方向。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）已轉向信用端重定價：CoreWeave 5Y CDS 在 2026-10-15 創下 1,194.5 bps 的紀錄，報導標題指 AI 信用疑慮把科技業違約保險推到紀錄高點（`valuation.ai_credit_schism`）。CoreWeave 以 AI 算力為主業，是最可能的 R3 候選；但它的負債規模、近期到期與再融資時程本次證據沒有載明，是否達到 ≥ 50 億美元門檻要另外以財報確認。AI infrastructure debt financing / vendor-financing loops：Lambda 在 2026-10-01 前後取得約 1（十億美元）GPU 擔保融資（`structural.ai_infrastructure_debt`），表示 neocloud 仍能進入擔保融資市場。廣義信用方面，HY OAS 為 3.23%，較前次基準擴大 58 bp（`monetary.hy_oas`），IG OAS 為 0.84%（+4 bp，`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 −1 bp、SRF 動用為 0（`monetary.repo_stress_srf`），融資管道沒有失序。本次證據沒有任何付款違約、契約豁免、distressed exchange 或 going-concern 揭露。

**判讀：** 這是三條路徑中最接近的一條：CDS 約 1,195 bps 屬於困境級定價，代表市場認為違約風險不低。但 R3 要求窗口內實際發生破產、超過寬限期的違約或完成 distressed exchange。要觸發，需要出現再融資失敗、主要客戶合約違約，或 HY 利差持續擴大到關閉 neocloud 的融資窗口；目前 Lambda 仍能融資、repo 平穩，觸發條件尚未具備。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 在 2026-10-15 創下 1,194.5 bps 的紀錄，AI 信用定價分歧已由股權端的樂觀轉為信用端重定價（`valuation.ai_credit_schism`）；同期 HY OAS 由 2.65% 擴大到 3.23%（+58 bp，2026-10-15，`monetary.hy_oas`）。
- [整體] 總經緩衝收窄：Fed 目標區間上調到 3.75%–4.0%（2026-10-17，`monetary.fed_funds`），10Y 殖利率 5.1%（+14 bp，`monetary.dgs10`），10Y 實質殖利率 2.78%（+18 bp，`monetary.dfii10`），CPI YoY 3.72%（2026-09，`monetary.cpi_yoy`），WTI 101.91（`monetary.wti`）。AI 帶頭下跌時，Fed 降息緩衝的空間很小。
- [R1] 估值與部位擁擠：Shiller CAPE 約 40.54（2026-10-16，`valuation.sp500_pe_cape`）；BofA 2026-10 FMS 科技股淨加碼約 37%，為 2020 年 8 月以來最高（`institutional.bofa_jpm_survey`）。一旦需要減碼，賣壓會很集中。
- [R1] 風險偏好轉弱：2026-10-16 上漲約 29、下跌約 71（`breadth.advance_decline`）；Fear & Greed 約 18（`retail.fear_greed`）；兩週內第 4 檔 IPO 撤件或延後（2026-10-16，`speculation.ipo_heat`）；MOVE 由 82.21 升至 101.1（`structural.treasury_basis_trade`）。
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）很大：年化 AI 終端營收約 $65bn（僅 Anthropic）vs 年化 capex 約 $725bn（分母：top-4）（`ai.revenue_capex_gap`）。
- [R1] 槓桿與選擇權投機水位高：單一個股槓桿 ETF 規模約 40.04（十億美元）（2026-10-16，`structural.leveraged_etf_aum`）；SPX 0DTE 2026-09 月均量創紀錄，約 3.4 百萬口（`structural.zero_dte`）；margin debt 約 1.45 兆美元（2026-08，`retail.margin_debt`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.13%（2026-10-15 收盤 29,935.59；高點 31,224.69，2026-10-06），要再跌約 21.77% 才會到 R1 門檻 23,418.52（`valuation.ndx_drawdown`）；S&P 500 仍在 200 日 MA 上方 5.34%（`valuation.sp500_trend`）。
- [R2] 本次證據中沒有任何一家 hyperscaler 下修 capex，四家 2026 capex 合計仍約 725（十億美元）（2026-07-28，`ai.hyperscaler_capex`）；需求端 H100 隨選中位租金約 4.20（2026-10-07，`ai.compute_supply_demand`），Anthropic 年化 run-rate 約 65（十億美元）（2026-08-17，`ai.openai_anthropic_revenue`）。
- [整體] 融資市場沒有失序：repo 資金壓力（SOFR−IORB）為 −1 bp，SOFR99−IORB 為 +7 bp，SRF 動用為 0（2026-10-15／16，`monetary.repo_stress_srf`）；IG OAS 只有 0.84%（`monetary.ig_oas`）；10Y 標售 bid-to-cover 約 2.77，需求強勁（2026-10-07，`monetary.treasury_auctions`）。
- [R3] neocloud 仍能取得融資：Lambda 約 1（十億美元）GPU 擔保融資（2026-10-01，`structural.ai_infrastructure_debt`）；本次證據沒有任何 AI 借款人的付款違約或 distressed exchange。
- [整體] 情緒沒有狂熱，波動也沒有擁擠：AAII 看多約 38.7%（2026-10-14，`retail.aaii`）；VIX 16.46，7 日 VIX/S&P 500 同漲訊號未成立（S&P 500 −0.27%，`structural.vix_spx_comove`）；AI 改名／SPAC 7 日掃描為 0 件（`speculation.ai_rename_spac`）。

## 與前期比較

前次結論：無前次預測（report-2026-09-13 為舊格式評分報告）

前次為舊格式評分報告，不轉換成 yes/no；flip_evidence 為空陣列。自 2026-09-13 以來的主要變化：

- Fed 目標區間上限由 3.75% 升到 4.0%（`monetary.fed_funds`），repo 利率同步上移（SOFR 3.62% → 3.89%，`monetary.repo_stress_srf`）。
- HY OAS +58 bp 到 3.23%（`monetary.hy_oas`），MOVE 由 82.21 升至 101.1（`structural.treasury_basis_trade`）：信用與利率波動同步升溫。
- 10Y 殖利率 +14 bp 到 5.1%，10Y 實質殖利率 +18 bp、10Y breakeven −1 bp，分解判讀：不可判（視窗不一致）（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。
- S&P 500 較前次基準幾乎持平（+0.03%，`valuation.sp500_trend`）；NASDAQ-100 在 2026-10-06 創新高後回落 4.13%（`valuation.ndx_drawdown`）。
- 新出現的 CoreWeave CDS 紀錄（2026-10-15，`valuation.ai_credit_schism`）是本次最重要的新增負面證據，但還不構成 R3 事件。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源檢索完成但沒有合格的當期揭露（✗ NOT DISCLOSED），不作為證據引用：`valuation.analyst_tp_decomposition`、`retail.social_sentiment`、`retail.naaim`、`monetary.fedwatch`、`monetary.private_credit_liquidity`、`ai.token_growth`、`ai.customer_concentration_rpo`、`ai.hyperscaler_financing_mix`（quarterly_state 有 2026 年發債預估約 190（十億美元），但 30 日 event_scan 無揭露）、`ai.depreciation_life`、`ai.capital_cycle`（兩個組件都沒有可用揭露，增速證據不足，本次不判定資本週期階段）、`speculation.equity_put_call`、`structural.global_leveraged_approvals`。其中私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）沒有揭露，對 R3 判讀影響最大：若有 gate proration / breach 或 net inflow→outflow flip，會強化 R3 的 yes 方向。其餘缺口不太可能改變結論。

部分成功來源的品質限制：`valuation.mag7_multiples` 只取得 MSFT 前瞻本益比 24.5（2026-09-24），沒有 Mag 7 加權 P/E 或 P/S 對 10 年均值；`breadth.rsp_spy`（2026-07-18）與 `breadth.top10_concentration`（2026-07-31）資料偏舊，只作背景；`ai.hyperscaler_capex` 沒有逐家指引與方向，R2 的逐家判讀因此受限。另外，搜尋結果紀錄把美債基差交易槓桿標為「script 三區塊 fetch_failed」，但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 都是 status ok。本報告以 artifact 為準記為 ✓ API，這項不一致需在正式執行時追查。

最大的不確定性：

1. CoreWeave 的負債規模與近期到期／再融資時程沒有在本次證據中確認。若確認它超過 50 億美元門檻且窗口內有大額到期，R3 的 yes 方向會明顯加強。
2. 窗口內 Q3／Q4 兩輪 hyperscaler 財報的 capex 指引方向：只要兩家下修，R2 就會直接觸發；若持續上修，則支持 no。
3. Fed 在通膨 3.72%、WTI 約 102 的環境下是否繼續升息：進一步緊縮會同時壓縮 AI 估值與 neocloud 的融資窗口，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7659.44 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日 MA 偏離） | 5.34% | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週 MA 偏離） | 6.78% | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較前次基準） | 0.03% | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29935.59 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤） | 4.13% | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2 家戶股票配置 %） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 4.0 | FRED API (series_id=DFEDTARU) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.75 | FRED API (series_id=DFEDTARL) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 3.23 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 58.0 bp | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.84 | FRED API (series_id=BAMLC0A0CM) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 5.1 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | 14.0 bp | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.78 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | 18.0 bp | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%，FRED 直取） | 2.35 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | -1.0 bp | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl） | 101.91 | FRED API (series_id=DCOILWTICO) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72% | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.33 | FRED API (series_id=T5YIFR) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（%，Kim-Wright） | 1.0729 | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（序列自身 trailing 7d） | -1.2 bp | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.89 | FRED API (series_id=SOFR) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.97 | FRED API (series_id=SOFR99) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.9 | FRED API (series_id=IORB) | 2026-10-18 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps（SOFR−IORB，iorb_date 2026-10-15） | -1.0 bp | fetch_macro.py repo_stress block (FRED) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr99_iorb_bps（SOFR99−IORB，sofr99_iorb_date 2026-10-15） | 7.0 bp | fetch_macro.py repo_stress block (FRED) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,755,639（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,943,911（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（no_new_obs，持平） | 6,250,253（¥625.03T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.46 | FRED API (series_id=VIXCLS) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of 2026-10-15，base_date 2026-10-08，window 7 日，comove=false） | 16.46 | fetch_macro.py derived block (FRED SP500 pairing) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 6.81% | fetch_macro.py derived block (FRED SP500 pairing) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -0.27% | fetch_macro.py derived block (FRED SP500 pairing) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2097.9713（$2.10T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG chg_pct | 2.14% | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -6883343 | CFTC TFF futures-only | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -309307 | CFTC TFF futures-only | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 101.1 | Yahoo Finance chart API (^MOVE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2264.1 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebSearch［primary: SEARCH］ | ✓ SEARCH-VERIFIED（取得 CAPE；trailing P/E 未見） |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch | ✓ SEARCH-VERIFIED（僅 MSFT 前瞻 P/E） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch 14 日 | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-07-18，偏舊） |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-07-31，偏舊） |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch［primary: SEARCH］ | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED（2026-08 月資料；ratio／YoY 未見） |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch［primary: SEARCH］ | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch 7 日 | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch［primary: SEARCH］ | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM | WebSearch | ✓ SEARCH-VERIFIED（BofA 2026-10；JPM 未見） |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | fetch_macro.py（FRED API） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | fetch_macro.py（FRED BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | fetch_macro.py（FRED BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | fetch_macro.py（FRED DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | fetch_macro.py（FRED DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | fetch_macro.py（FRED T10YIE 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | fetch_macro.py（FRED DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | fetch_macro.py（FRED CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | fetch_macro.py（FRED T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | fetch_macro.py（FRED THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | fetch_macro.py repo_stress（FRED API） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch 14 日 | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch［primary: SEARCH］ | ✗ NOT DISCLOSED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | fetch_macro.py（FRED WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | fetch_macro.py（FRED ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch 30 日［primary: SEARCH］ | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state，Q2 2026 財報季延續） | ✓ SEARCH-VERIFIED（僅四家合計） |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED（Anthropic；OpenAI 未見） |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險 | WebSearch［primary: SEARCH］ | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch［primary: SEARCH］ | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch：quarterly_state 沿用最新季度；event_scan 30 日無揭露 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch 組合（分子 Anthropic；分母 top-4 capex） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch 30 日 | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch：兩組件均無可用揭露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch＋SEC EDGAR 7 日 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch 7 日 | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch movers 7 日 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch 30 日 | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 14 日 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch［primary: SEARCH］ | ✗ NOT DISCLOSED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch［primary: SEARCH］ | ✓ SEARCH-VERIFIED（單一個股槓桿 ETF 合計；個別 ticker 未見） |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com 30 日 | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch 7 日 | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED（VIX、SKEW；期限結構與股債相關未見） |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | fetch_macro.py（FRED VIXCLS＋vix_spx_comove） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（交叉核對） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch 30 日［primary: SEARCH］ | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py cftc_lev_funds／move_index／ofr_repo（any） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.54（預定來源 multpl／GuruFocus） | Shiller PE CAPE ratio current October 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 成員 MSFT 前瞻本益比 24.5 | Magnificent 7 forward P/E valuation October 2026 | https://articlegateway.com/?p=146（articlegateway） | 2026-09-24 | 2026-10-18T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 紀錄 1,194.5 bps | AI credit fears tech default insurance record highs October 2026 | https://www.businessday.co.za/world/international-companies/2026-10-15-ai-credit-fears-push-tech-default-insurance-to-record-highs/（BusinessDay） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 報酬約 12.08% | RSP equal weight vs SPY YTD performance 2026 | https://pro.thestreet.com/market-commentary/rsp-vs-spy-does-diversification-require-equal-weight（TheStreet Pro） | 2026-07-18 | 2026-10-18T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度約 38.9% | S&P 500 top 10 concentration percent record 2026 | https://walnutinvest.com/stats/market-concentration-statistics（Walnut） | 2026-07-31 | 2026-10-18T09:30:00+08:00 |
| breadth.advance_decline | 上漲家數約 29 對下跌 71 | market breadth October 16 2026 percent above 200-day advance decline | https://www.thetrading.tools/market-breadth（thetrading.tools） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 約 18（極度恐懼；預定來源 CNN） | CNN Fear and Greed Index October 16 2026 extreme fear | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/（finhacker） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-08 月資料）約 1.45 兆美元（預定來源 FINRA） | FINRA margin debt August 2026 year over year | https://www.thetrading.tools/margin-debt（thetrading.tools） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.7%（週截至 2026-10-14） | AAII sentiment survey week ending October 14 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA 2026-10 FMS 科技股淨加碼約 37%，2020 年 8 月以來最高 | BofA October 2026 fund manager survey tech overweight cash | https://www.bloomberg.com/news/articles/2026-10-13/bofa-poll-shows-investors-most-exposed-to-tech-stocks-since-2020（Bloomberg） | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.77（需求強勁） | Treasury 10-year note auction October 7 2026 bid-to-cover | https://www.rttnews.com/3697286/ten-year-note-auction-attracts-strong-demand.aspx（RTTNews） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| monetary.pboc | 2026 年 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate social financing 2026 total | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm（SteelOrbis） | 2026-08-15 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 725（十億美元；Q2 2026 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65（十億美元） | OpenAI Anthropic annualized revenue run rate 2026 | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選中位租金約 4.20 | GPU rental price index HBM DRAM contract price October 2026 | https://uvik.net/blog/gpu-price-index/（Uvik GPU price index） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 2026 年 hyperscaler 發債預估約 190（十億美元） | hyperscaler bond issuance 2026 capex versus free cash flow | https://www.twentyfouram.com/insights/oracle-clears-the-supply-cloud-with-record-demand（TwentyFour AM） | 2026-02-02 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 分子：年化 AI 終端營收，Anthropic run-rate 約 65（十億美元） | AI revenue versus capex gap 2026 annualized | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 分母：top-4 hyperscaler 2026 capex 合計約 725（十億美元；沿用 capex guidance bullet） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描：0 件合格事件 | AI company name change ticker SPAC announcement October 2026 | 檢查來源：SEC EDGAR 8-K、SPACInsider、Boardroom Alpha | — | 2026-10-18T09:30:00+08:00 |
| speculation.ipo_heat | 兩週內第 4 檔 IPO 撤件或延後 | IPO market October 16 2026 pulled postponed Firmus Oura | https://www.ipox.com/ipox/the-ipox-update-10162026（IPOX） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描：0 件符合 2+ 主題×弱基本面（PFAI 2026-10-07 +116.7% 在窗口外） | biggest stock gainers week October 12-16 2026 microcap 100% | 檢查來源：Tapeboard movers archive、Financial Modeling Prep daily gainers、Yahoo movers | — | 2026-10-18T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 11 月中上市 | Anthropic IPO October 2026 timing valuation S-1 | https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market（CNN） | 2026-10-05 | 2026-10-18T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描：0 件合格（NVDA 2026-10-09 有申報，但無 filing-level 申報人／金額細節） | insider selling Form 4 October 2026 Nvidia AI executives SEC | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-10-18T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.04（十億美元），TSLL 等資金流入 | single stock leveraged ETF assets October 2026 weekly flows | https://www.etfaction.com/single-stock-traders-pile-into-tsll-and-intw-as-levered-flows-surge/（ETF Action） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval October 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed | — | 2026-10-18T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 2026-09 月均量創紀錄，約 3.4 百萬口 | Cboe September 2026 derivatives volume 0DTE SPX record | https://www.cboe.com/insights/posts/market-metrics-that-matter-derivatives-september-2026-volume-highlights（Cboe） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.options_volume | OCC 2026-09 總結算量約 1,486,062,415 口 | OCC September 2026 monthly volume data | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report（OCC） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 約 14.84、Cboe SKEW 154.34 | VIX term structure SKEW October 2026 options brief | https://www.home.saxo/content/articles/options/the-middle-got-cheaper-the-edge-did-not---options-brief---12-october-2026-12102026（Saxo） | 2026-10-12 | 2026-10-18T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-08 月資料）約 1.45 兆美元，作 margin debt／股票市值比率基數（比率本身未見） | margin debt to market cap August 2026 | https://www.thetrading.tools/margin-debt（thetrading.tools） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Lambda GPU 擔保融資約 1（十億美元） | AI data center debt Lambda CoreWeave financing October 2026 | https://valueaddvc.com/pulse/ai-data-center-debt-financing-risk-2026（ValueAdd VC） | 2026-10-01 | 2026-10-18T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-10-18",
  "iso_week": "2026-W42",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-04-18",
  "prior_date": "2026-09-13",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 4.13,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

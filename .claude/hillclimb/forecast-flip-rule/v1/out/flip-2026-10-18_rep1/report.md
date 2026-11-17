> [DRY RUN] this report was not committed to archive.

# 2026-10-18 AI 泡沫破裂預測報告
報告日期：2026-10-18｜ISO 週次：2026-W42｜預測窗口：2026-10-18 → 2027-04-18｜前次基準：report-2026-09-13（35天前）

## 結論

**結論：no**

三條路徑都未進入「可能在 182 天內完成」的區段：NASDAQ-100 僅距 52 週高點回撤 4.13%，還需再跌約 21.77% 才觸及 R1 門檻；四大 hyperscaler 最近一次指引仍是 2026 capex 合計約 725（十億美元），本次證據中沒有任何一家下修。CoreWeave 5Y CDS 創紀錄（1,194.5 bps）與 HY OAS 走闊顯示 R3 壓力正在累積，但尚無付款違約、破產或 distressed exchange 跡象，不足以推翻「三者皆不發生」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,935.59（2026-10-15），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 4.13%（`valuation.ndx_drawdown`）。R1 門檻水位為 23,418.52，自最新收盤須再下跌約 21.77% 才觸及。高點僅在 9 個交易日前創下，指數仍貼近頂部。S&P 500 收 7,659.44（2026-10-16），高於 200 日均線 5.34%、高於 52 週均線 6.78%（`valuation.sp500_trend`），屬價格延伸而非破位。VIX 16.46，7 日窗內與 S&P 500 未同向上漲（`structural.vix_spx_comove`，comove=false）。

**判讀：** 距 R1 尚遠。窗口內要觸發，需要一次約 22% 以上的急跌；可能的推手是 R3 信用事件外溢、10 月下旬起的 Q3 財報季讓 AI 敘事失望，或利率（10Y 5.10%、Fed 上調目標區間 25bp）持續壓抑估值。目前價格面沒有出現這種動能。

### R2 資本支出收縮

最近一次可取得的指引是 2026-07-28（Q2 財報季）的四大 hyperscaler 2026 capex 合計約 725（十億美元）（`ai.hyperscaler_capex`）。本次證據只有四家合計數，沒有逐家數字：Microsoft、Alphabet、Amazon、Meta 各自的最新指引數值與相對前次的方向，本次證據都未逐家揭露。報導重點是市場對 Alphabet 加碼 capex 的「審視升高」，不是下修。依本次證據，四家中已下修的家數為 0。下一輪財報落在 2026 年 10 月下旬至 11 月初（Q3）以及 2027 年 1 月下旬至 2 月初（Q4），兩輪都在窗口內，但本次證據未取得確切日期。需求面仍強：H100 隨選中位租金約 $4.20（2026-10-07，`ai.compute_supply_demand`），Anthropic 年化 run-rate 約 65（十億美元）（2026-08-17，`ai.openai_anthropic_revenue`）。

**判讀：** 尚未啟動。要在窗口內成立，四家中至少兩家須在 Q3 或 Q4 財報下修當年度或次年度指引；這通常要等 R1 大幅回撤或融資成本急升之後才會發生。目前的方向是上修或持平，不是收縮。

### R3 AI 信用事件

CoreWeave 5Y CDS 創紀錄的 1,194.5 bps（2026-10-15），報導標題為 AI 信用疑慮把科技股違約保險推升至歷史高點（`valuation.ai_credit_schism`）。這是 AI 信用定價分歧（equity-vs-credit schism）從「信用與非 AI 無差」轉向「信用端開始重定價」的訊號：信用端已經在為違約定價，股權端（NASDAQ-100 回撤僅 4.13%）則沒有跟上。AI infrastructure debt financing / vendor-financing loops 方面，30 日內披露的是 Lambda 約 1（十億美元）的 GPU 擔保融資（2026-10-01，`structural.ai_infrastructure_debt`）。新融資仍然能完成，代表融資管道未關閉。廣義信用方面，HY OAS 由 2.65% 走闊 58bp 至 3.23%（2026-10-15，`monetary.hy_oas`），IG OAS 0.84% 僅 +4bp（`monetary.ig_oas`）。本次證據沒有任何候選借款人出現付款違約、寬限期、covenant waiver、distressed exchange 或 going-concern 語言；CoreWeave 等借款人的負債規模與近期到期牆，本次證據也未提供。

**判讀：** 三條路徑中最接近的一條，但仍在定價壓力階段，不在違約階段。1,194.5 bps 的 CDS 代表市場顯著定價違約風險，換算成 6 個月內實際違約仍明顯低於一半。要在窗口內成立，需要融資窗口關閉（新發行失敗、再融資被拒）並導致付款違約或 distressed exchange，而目前 Lambda 一類的新融資仍在完成。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 於 2026-10-15 創紀錄的 1,194.5 bps，AI 信用疑慮把科技違約保險推升至歷史高點；信用端領先股權端重定價，是典型後期訊號（`valuation.ai_credit_schism`）。
- [整體] 廣義風險溢價走闊：HY OAS 由 2.65% 升至 3.23%（+58bp，2026-10-15）（`monetary.hy_oas`），MOVE 由 82.21 升至 101.1（2026-10-16）（`structural.treasury_basis_trade`）；信用與利率波動率同步上升，對高槓桿 AI 借款人的再融資條件不利。
- [R1] 利率與通膨夾擊估值：10Y 5.10%（+14bp）、10Y 實質利率 2.78%（+18bp，2026-10-15）（`monetary.dgs10`、`monetary.dfii10`），Fed 目標區間上調至 3.75–4.00%（2026-10-17）（`monetary.fed_funds`）；CPI YoY 3.72%（2026-09）（`monetary.cpi_yoy`）、WTI $101.91（`monetary.wti`）限縮 Fed 在 AI 主導的下跌中出手緩衝的空間。
- [R1] 風險偏好轉弱的早期跡象：CNN Fear & Greed 約 18（極度恐懼，2026-10-16）（`retail.fear_greed`），上漲對下跌家數約 29 對 71（2026-10-16）（`breadth.advance_decline`），兩週內第 4 檔 IPO 撤件或延後（2026-10-16）（`speculation.ipo_heat`）。
- [整體] 脆弱性高（解釋泡沫存在與下行幅度，不決定時點）：Shiller CAPE 約 40.54（2026-10-16）（`valuation.sp500_pe_cape`），BofA FMS 科技股淨加碼約 37、為 2020 年 8 月以來最高（2026-10-13）（`institutional.bofa_jpm_survey`），前十大集中度約 38.9%（`breadth.top10_concentration`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.13%（最新收盤 29,935.59，2026-10-15；高點 31,224.69，2026-10-06），距 R1 門檻 23,418.52 還要再跌約 21.77%（`valuation.ndx_drawdown`）；S&P 500 仍高於 200 日均線 5.34%（`valuation.sp500_trend`）。
- [R2] 最近一次指引仍是四大 hyperscaler 2026 capex 合計約 725（十億美元）（2026-07-28），本次證據沒有任何一家下修（`ai.hyperscaler_capex`）；需求側 H100 隨選租金約 $4.20（2026-10-07）（`ai.compute_supply_demand`）、Anthropic run-rate 約 65（十億美元）（`ai.openai_anthropic_revenue`），看不到迫使 capex 收縮的需求崩落。
- [R3] AI 融資管道仍開放：Lambda 約 1（十億美元）GPU 擔保融資於 2026-10-01 完成（`structural.ai_infrastructure_debt`）；IG OAS 0.84% 僅 +4bp（`monetary.ig_oas`）；本次證據中無任何 AI 基礎設施借款人違約、寬限期或 distressed exchange。
- [整體] 系統性融資面平穩：repo 資金壓力（SOFR−IORB）為 −1bp、SOFR99−IORB 7bp（2026-10-15），SRF 動用（Standing Repo Facility usage）為 0（2026-10-16）（`monetary.repo_stress_srf`）；10Y 標售 bid-to-cover 約 2.77、需求強勁（2026-10-07）（`monetary.treasury_auctions`）；VIX 16.46 且未與 S&P 500 同向上漲（`structural.vix_spx_comove`）。
- [整體] 投機與槓桿仍在流入，代表尚未進入強制去槓桿：單一個股槓桿 ETF 規模約 40.04（十億美元）、資金流加速（2026-10-16）（`structural.leveraged_etf_aum`）；Anthropic 目標 11 月中上市（2026-10-05）（`speculation.upcoming_ai_ipos`）。

## 與前期比較

前次結論：yes（report-2026-09-13）
本次結論：翻轉
翻轉依據：
- 前次 forecast.json 早於 `yes_basis` 欄位，沒有記錄任何決定性理由可供逐項延續。`yes` 必須每次重新取得：依規則 1 重新檢驗，本次證據裡沒有任何一條路徑「已在進行或可能在窗口內完成」。
- R1：前次 r1_drawdown_pct 為 4.21，本次 NASDAQ-100 距 52 週高點回撤 4.13%，期間還在 2026-10-06 創新高 31,224.69；距門檻仍需再跌約 21.77%（`valuation.ndx_drawdown`）。市場回撤路徑沒有推進。
- R2：最近一次指引仍是四大合計約 725（十億美元）（2026-07-28），自 prior_date 以來沒有新財報、也沒有下修（`ai.hyperscaler_capex`）。資本支出收縮路徑沒有啟動。
- R3：CoreWeave 5Y CDS 創紀錄的 1,194.5 bps（2026-10-15）是自前次以來最重要的負面新證據（`valuation.ai_credit_schism`），但它屬於定價壓力，不是 R3 定義的違約、破產或 distressed exchange；單憑它不足以讓 R3 在 182 天內「比不發生更可能」。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源為 ✗ NOT DISCLOSED（檢索完成但無合格當期披露）：valuation.analyst_tp_decomposition、retail.social_sentiment、retail.naaim、monetary.fedwatch、monetary.private_credit_liquidity、ai.token_growth、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（event_scan 無 30 日事件；quarterly_state 只沿用 2026-02-02 的 2026 年發債預估約 190 作背景）、ai.depreciation_life、ai.capital_cycle（兩個組件皆無）、speculation.equity_put_call、structural.global_leveraged_approvals。其中 monetary.private_credit_liquidity 與 ai.capital_cycle 的缺漏最可能影響判讀：若私募信貸已出現 redemption-request ratio 上升、gate proration / breach 或 net inflow→outflow flip，或出現密集的資料中心租約取消，R3 與 R2 的距離都會縮短。但這些來源是「完成檢索、無披露」，不是被遮蔽的訊號，因此不改變本次答案。

資料一致性備註：case/evidence.md 的檢索結果表把 structural.treasury_basis_trade 記為「script 三區塊 fetch_failed」，但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 三個區塊都是 status ok。本報告依規則以 macro artifact 為準，記為 ✓ API。

R2 的逐家指引缺口：hyperscaler capex 只取得四家合計數，沒有 Microsoft、Alphabet、Amazon、Meta 的逐家數值與方向。這不影響「目前 0 家下修」的結論，但下一輪財報後必須逐家追蹤。

最大的不確定性：
1. Q3 財報季（10 月下旬至 11 月初，確切日期本次未取得）：若兩家以上下修 2026 或 2027 capex 指引，R2 會直接成立，答案翻向 yes；若持續上修，則強化 no。
2. CoreWeave 等 AI 基礎設施借款人的再融資：CDS 已在 1,194.5 bps，若 HY OAS 持續走闊、融資窗口關閉，可能出現 distressed exchange，答案推向 yes。本次證據沒有這些借款人的到期牆資料。
3. 利率與通膨路徑：10Y 5.10%、CPI 3.72%、WTI 逾 $100、Fed 剛升息。若升息延續，估值壓縮可能把 R1 拉近；若通膨回落、Fed 轉向，則推向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7659.44 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 5.34 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 6.78 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29935.59 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.13 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2 季資料，%） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（%） | 4.0 | FRED API (series_id=DFEDTARU) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（%） | 3.75 | FRED API (series_id=DFEDTARL) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 3.23 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps（vs 2026-09-11） | 58.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.84 | FRED API (series_id=BAMLC0A0CM) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 5.1 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | 14.0 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.78 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | 18.0 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.35 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl） | 101.91 | FRED API (series_id=DCOILWTICO) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料，%） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.33 | FRED API (series_id=T5YIFR) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（%，Kim-Wright） | 1.0729 | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.89 | FRED API (series_id=SOFR) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.97 | FRED API (series_id=SOFR99) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.9 | FRED API (series_id=IORB) | 2026-10-18 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps（同日 2026-10-15） | -1.0 | FRED API (repo_stress block) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,755,639（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,943,911（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,250,253（¥625.03T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.46 | FRED API (series_id=VIXCLS) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（窗 2026-10-08 → 2026-10-15） | 16.46 | FRED API (vix_spx_comove block) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 6.81 | FRED API (vix_spx_comove block) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -0.27 | FRED API (vix_spx_comove block) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2,097.9713（$2.10T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約合計，口） | -6,883,343 | CFTC TFF futures-only | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -309,307 | CFTC TFF futures-only | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 101.1 | Yahoo Finance chart API (^MOVE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party transaction volume） | 2264.1 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebSearch | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch | ✓ SEARCH-VERIFIED（僅 MSFT 前瞻本益比；無加權值） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail / Margin Debt: FINRA monthly data | WebSearch（月度 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail / Retail survey: AAII Investor Sentiment | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail / Household equity allocation | scripts/fetch_macro.py BOGZ1FL153064486Q | ✓ API |
| retail.naaim | Retail / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional / BofA Fund Manager Survey and JPM | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.fed_funds | Monetary / Fed funds rate: FRED DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary / High Yield OAS | scripts/fetch_macro.py | ✓ API |
| monetary.ig_oas | Monetary / Investment Grade OAS | scripts/fetch_macro.py | ✓ API |
| monetary.dgs10 | Monetary / 10Y Treasury yield | scripts/fetch_macro.py | ✓ API |
| monetary.dfii10 | Monetary / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py | ✓ API |
| monetary.t10yie | Monetary / 10Y breakeven inflation rate | scripts/fetch_macro.py（FRED 直取） | ✓ API |
| monetary.wti | Monetary / WTI crude oil price | scripts/fetch_macro.py | ✓ API |
| monetary.cpi_yoy | Monetary / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py | ✓ API |
| monetary.t5yifr | Monetary / 5y5y forward inflation expectation | scripts/fetch_macro.py | ✓ API |
| monetary.term_premium | Monetary / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py | ✓ API |
| monetary.repo_stress_srf | Monetary / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary / 美債標售需求（auction tail / bid-to-cover） | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary / Fed funds rate path expectations | WebSearch | ✗ NOT DISCLOSED |
| monetary.walcl | Monetary / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | Monetary / Global central bank liquidity cross-check | scripts/fetch_macro.py | ✓ API（ECBASSETSW ok；JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | WebSearch（stock-of-state，沿用 Q2 指引） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch：quarterly_state 沿用最近披露；event_scan 30 日掃描 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch＋既有 bullets 組合 | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI / 資本週期階段（capital cycle stage） | WebSearch：quarterly_state 與 event_scan（30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative / Search for past 7 days: AI rename / SPAC | WebSearch＋SEC EDGAR 8-K（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative / IPO market heat | WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative / Microcap thematic moonshots | WebSearch movers 掃描（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative / Insider selling at AI / market-leadership companies | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative / Cboe equity-only put/call ratio | WebSearch | ✗ NOT DISCLOSED |
| structural.leveraged_etf_aum | Structural / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural / VIX / S&P 500 co-movement | scripts/fetch_macro.py VIXCLS＋vix_spx_comove | ✓ API |
| structural.margin_debt_crosscheck | Structural / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural / Bank loans to nondepository financial institutions | scripts/fetch_macro.py | ✓ API |
| structural.treasury_basis_trade | Structural / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds＋move_index＋ofr_repo | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.54 | Shiller PE CAPE ratio current October 2026 multpl | https://www.multpl.com/shiller-pe（multpl；原定來源 multpl.com） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.mag7_multiples | MSFT 前瞻本益比 24.5 | Magnificent 7 forward P/E valuation October 2026 | https://articlegateway.com/?p=146 | 2026-09-24 | 2026-10-18T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 紀錄 1,194.5 bps | AI credit fears tech default insurance record highs October 2026 | https://www.businessday.co.za/world/international-companies/2026-10-15-ai-credit-fears-push-tech-default-insurance-to-record-highs/（BusinessDay） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 報酬約 12.08% | RSP equal weight vs SPY YTD performance 2026 | https://pro.thestreet.com/market-commentary/rsp-vs-spy-does-diversification-require-equal-weight（TheStreet） | 2026-07-18 | 2026-10-18T09:30:00+08:00 |
| breadth.top10_concentration | 前十大集中度約 38.9% | S&P 500 top 10 concentration percent record 2026 | https://walnutinvest.com/stats/market-concentration-statistics | 2026-07-31 | 2026-10-18T09:30:00+08:00 |
| breadth.advance_decline | 上漲約 29 對下跌 71 | market breadth October 16 2026 percent above 200-day advance decline | https://www.thetrading.tools/market-breadth | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 約 18（極度恐懼） | CNN Fear and Greed Index October 16 2026 extreme fear | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/（原定來源 cnn.com） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-08 月資料）約 1.45 兆美元 | FINRA margin debt August 2026 year over year | https://www.thetrading.tools/margin-debt（原定來源 FINRA） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.7% | AAII sentiment survey week ending October 14 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA FMS 科技股淨加碼約 37、2020 年 8 月以來最高 | BofA October 2026 fund manager survey tech overweight cash | https://www.bloomberg.com/news/articles/2026-10-13/bofa-poll-shows-investors-most-exposed-to-tech-stocks-since-2020（Bloomberg） | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.77 | Treasury 10-year note auction October 7 2026 bid-to-cover | https://www.rttnews.com/3697286/ten-year-note-auction-attracts-strong-demand.aspx（RTTNews） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate social financing 2026 total | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm | 2026-08-15 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 725（Q2 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65 | OpenAI Anthropic annualized revenue run rate 2026 | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選中位租金約 $4.20 | GPU rental price index HBM DRAM contract price October 2026 | https://uvik.net/blog/gpu-price-index/ | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 2026 年 hyperscaler 發債預估約 190（背景，沿用） | hyperscaler bond issuance 2026 capex versus free cash flow | https://www.twentyfouram.com/insights/oracle-clears-the-supply-cloud-with-record-demand（TwentyFour AM） | 2026-02-02 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic run-rate 約 65 vs 四大 capex 合計約 725（分母：top-4，未含 Oracle） | AI revenue versus capex gap 2026 annualized | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描：0 件 | AI company name change ticker SPAC announcement October 2026 | 檢查來源：SEC EDGAR 8-K、SPACInsider、Boardroom Alpha | — | 2026-10-18T09:30:00+08:00 |
| speculation.ipo_heat | 兩週內第 4 檔 IPO 撤件或延後 | IPO market October 16 2026 pulled postponed Firmus Oura | https://www.ipox.com/ipox/the-ipox-update-10162026（IPOX） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描：0 件符合 2+ 主題×弱基本面（PFAI 2026-10-07 落在 7 日窗外） | biggest stock gainers week October 12-16 2026 microcap 100% | 檢查來源：Tapeboard movers archive、Financial Modeling Prep daily gainers、Yahoo movers | — | 2026-10-18T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 11 月中上市 | Anthropic IPO October 2026 timing valuation S-1 | https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market（CNN） | 2026-10-05 | 2026-10-18T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描：0 件合格 | insider selling Form 4 October 2026 Nvidia AI executives SEC | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表（無 filing-level 申報人／金額細節） | — | 2026-10-18T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.04 | single stock leveraged ETF assets October 2026 weekly flows | https://www.etfaction.com/single-stock-traders-pile-into-tsll-and-intw-as-levered-flows-surge/（ETF Action） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval October 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed | — | 2026-10-18T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 9 月 ADV 創紀錄約 3.4 百萬口（2026-09 月資料） | Cboe September 2026 derivatives volume 0DTE SPX record | https://www.cboe.com/insights/posts/market-metrics-that-matter-derivatives-september-2026-volume-highlights（Cboe） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.options_volume | OCC 9 月總結算量約 1,486,062,415 口（2026-09 月資料） | OCC September 2026 monthly volume data | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report（OCC） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 約 14.84、SKEW 154.34 | VIX term structure SKEW October 2026 options brief | https://www.home.saxo/content/articles/options/the-middle-got-cheaper-the-edge-did-not---options-brief---12-october-2026-12102026（Saxo） | 2026-10-12 | 2026-10-18T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對市值比率基數約 1.45 兆美元（2026-08 月資料） | margin debt to market cap August 2026 | https://www.thetrading.tools/margin-debt | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Lambda GPU 擔保融資約 1 十億美元 | AI data center debt Lambda CoreWeave financing October 2026 | https://valueaddvc.com/pulse/ai-data-center-debt-financing-risk-2026 | 2026-10-01 | 2026-10-18T09:30:00+08:00 |

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
  "prior_answer": "yes",
  "flip_evidence": ["valuation.ndx_drawdown", "ai.hyperscaler_capex", "valuation.ai_credit_schism"],
  "yes_basis": [],
  "r1_drawdown_pct": 4.13,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

> [DRY RUN] this report was not committed to archive.

# 2026-09-13 AI 泡沫破裂預測報告

報告日期：2026-09-13｜ISO 週次：2026-W37｜預測窗口：2026-09-13 → 2027-03-14｜前次基準：report-2026-09-03（10天前）

## 結論

**結論：no**

三條路徑目前都沒有進行中的觸發：NASDAQ-100 距 52 週高點只回撤 4.21%（`valuation.ndx_drawdown`），離 R1 門檻還差約 21.70% 的跌幅；HY OAS 2.70%、IG OAS 0.80% 仍在偏緊水位（`monetary.hy_oas`、`monetary.ig_oas`），也沒有證據顯示任何 hyperscaler 下修 capex。9/16 FOMC 預期升息、10Y 殖利率升到 4.95% 是真實的利率壓力，但這只是讓市場更脆弱，還不能證明 182 天內必然破裂，所以維持基準率判斷。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,368.44（2026-09-11），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 4.21%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，從最新收盤還要再跌約 21.70% 才會觸及。S&P 500 收在 7,656.98（2026-09-11），比 200 日均線高 6.9%、比 52 週均線高 8.33%，自前次基準以來下跌 1.17%（`valuation.sp500_trend`）。估值偏高：Shiller CAPE 約 40.73（`valuation.sp500_pe_cape`），前十大成分股占 S&P 500 約 38%（`breadth.top10_concentration`）。另一方面，情緒已經轉向謹慎：CNN Fear & Greed 約 35，屬恐懼區（`retail.fear_greed`）；AAII 看多比例約 38.0%（`retail.aaii`）。VIX 從 14.32 升到 17.84（+24.58%），同一個 7 日窗口 S&P 500 下跌 2.01%，屬正常的反向走勢，沒有出現同漲警訊（`structural.vix_spx_comove`）。利率端的壓力在升高：10Y 殖利率 4.95%，自前次基準上升 18 bps（`monetary.dgs10`）；10Y 實質殖利率上升 13 bps（`monetary.dfii10`）；CME FedWatch 顯示 9/16 FOMC 升息 25 bps 的市場隱含機率約 85.5%（`monetary.fedwatch`）；CPI YoY 3.35%（`monetary.cpi_yoy`）；WTI 原油 97.26 美元（`monetary.wti`）。

**判讀：** R1 離觸發還很遠（回撤 4.21% 對門檻 25%）。窗口內要觸發，需要升息循環重啟、長端利率持續上行，加上 AI 獲利或資金面出現衝擊，讓高估值、高集中度的指數再跌約 22%。9/16 FOMC 是最近的催化事件，但目前市場沒有失序跡象。

### R2 資本支出收縮

最新可得的 hyperscaler capex 證據是 2026-07-28 CNBC 的彙整報導：Microsoft、Alphabet、Amazon、Meta 四家 2026 年 capex 合計約 7,250 億美元，報導重點是市場對 capex 的審視變嚴（`ai.hyperscaler_capex`）。本次證據只有四家合計數，沒有逐家的指引數值與前次指引對照，因此 Microsoft、Alphabet、Amazon、Meta 個別的方向（上修／持平／下修）都記為「本次證據未逐家揭露」。就本次證據所見，四家中確認下修的家數為 0。相關基本面：Anthropic 年化 run-rate 約 650 億美元（2026-08-17，`ai.openai_anthropic_revenue`）；AI 營收對 capex 缺口（revenue-to-capex gap）方面，年化 AI 終端營收約 1,050 億美元，對比年化 capex 約 7,250 億美元（分母：top-4 hyperscaler，不含 Oracle，因為 Oracle 季頻數據本次未取得；`ai.revenue_capex_gap`），差距仍大；H100 中位租金約 3.38 美元／小時（2026-08-31，`ai.compute_supply_demand`），本次沒有同時取得利用率轉弱或訂單消化的證據，單看價格無法判定產能過剩。下一輪財報（各家 2026 Q3 財報）依季度節奏會落在窗口內，但具體日期本次證據沒有取得。

**判讀：** R2 目前沒有任何一家確認下修。要在窗口內觸發，需要至少兩家在 Q3 或 Q4 財報下修當年度或次年度指引。營收對 capex 的缺口大，加上市場審視變嚴，代表未來下修壓力存在，但現有證據只看到「審視」，沒有看到「下修」。

### R3 AI 信用事件

本次 14 日窗口內沒有 AI 發行人的利差或 CDS 重定價報導（相關來源見資料缺漏一節）。30 日內查到的 AI infrastructure debt financing / vendor-financing loops 事件是 2026-09-08 Qualcomm 對 Amazon 發行約 40 億美元認股權證，屬於供應商給買方股權誘因的循環型安排，不是債務違約或 distress 訊號（`structural.ai_infrastructure_debt`）。整體信用環境：HY OAS 2.70%（+5 bps）、IG OAS 0.80%（−1 bp）（`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 −3 bps，SOFR99−IORB 為 +5 bps，SRF 動用（Standing Repo Facility usage）為 0（`monetary.repo_stress_srf`）；銀行對 NBFI 放款約 $2.03T，週變動持平（`structural.nbfi_bank_loans`）。本次證據沒有指出任何符合 ≥ 50 億美元門檻、以 AI 算力為主業的借款人出現付款違約、covenant waiver、distressed exchange 或 going-concern 措辭。

**判讀：** R3 沒有進行中的 distress 訊號，信用利差仍緊、資金市場平穩。要在窗口內觸發，需要升息或再融資牆，讓高槓桿的 neocloud／資料中心借款人出現實際付款違約或 distressed exchange。目前沒有證據顯示這個過程已經開始。

## 支持 yes 的證據

- [R1] 利率衝擊正在累積：10Y 殖利率 4.95%（2026-09-10），自 2026-09-03 上升 18 bps；CME FedWatch 顯示 9/16 FOMC 升息機率約 85.5%（2026-09-12）；CPI YoY 3.35%（2026-08），WTI 97.26 美元，壓縮了 Fed 在 AI 主導的跌勢中出手緩衝的空間（`monetary.dgs10`、`monetary.fedwatch`、`monetary.cpi_yoy`、`monetary.wti`）。
- [R1] 估值與集中度處於極端：Shiller CAPE 約 40.73（2026-09-01）；前十大成分股占 S&P 500 約 38%（2026-09-01）；S&P 500 比 200 日均線高 6.9%（2026-09-11），下跌時的空間很大（`valuation.sp500_pe_cape`、`breadth.top10_concentration`、`valuation.sp500_trend`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）很大：年化 AI 終端營收約 1,050 億美元，對比 top-4 hyperscaler 2026 capex 約 7,250 億美元；市場在 2026-07-28 已開始懲罰 capex 擴張（Alphabet 財報遭拋售），日後下修壓力存在（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`）。
- [整體] 波動度與避險需求上升：VIX 從 14.32 升到 17.84（2026-09-10），MOVE 從 74.68 升到 82.21（2026-09-11）；call skew 位於第 91 百分位（2026-09-10）（`structural.vix_spx_comove`、`structural.treasury_basis_trade`、`structural.cross_asset_derivatives`）。
- [R3] AI infrastructure debt financing / vendor-financing loops 仍在擴大：2026-09-08 Qualcomm 對 Amazon 發行約 40 億美元認股權證（`structural.ai_infrastructure_debt`）。

## 支持 no 的證據

- [R1] 回撤離門檻很遠：NASDAQ-100 距 52 週高點回撤 4.21%（2026-09-11），還要再跌約 21.70% 才會碰到 R1 門檻 22,995.45；以 182 天窗口來看，這需要一次重大崩跌（`valuation.ndx_drawdown`）。
- [R3] 信用與資金市場平穩：HY OAS 2.70%、IG OAS 0.80%（2026-09-10）；SOFR−IORB 為 −3 bps、SRF 動用為 0（2026-09-10／2026-09-11），看不到 R3 必經的信用重定價或資金失序（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`）。
- [R2] 沒有任何 hyperscaler 下修 capex 的證據：最新彙整（2026-07-28）顯示四家 2026 capex 合計約 7,250 億美元，仍在擴張，離「兩家下修」差得遠（`ai.hyperscaler_capex`）。
- [整體] 情緒不是狂熱頂部：CNN Fear & Greed 約 35（恐懼，2026-09-10）；AAII 看多約 38.0%（2026-09-10）；本週 0 件 +AI 改名／SPAC、0 件符合條件的 microcap moonshot，顯示投機已降溫，不像破裂前的極端擁擠（`retail.fear_greed`、`retail.aaii`、`speculation.ai_rename_spac`、`speculation.microcap_moonshots`）。
- [整體] 槓桿部位在收縮：單一個股槓桿 ETF 規模約 407.4 億美元，且有約 7.51 億美元淨流出（2026-09-08）；CFTC 槓桿基金美債期貨淨空部位 4 週縮小 387,809 口（2026-09-08），美債基差交易槓桿（Treasury basis-trade leverage）在降而不是在升（`structural.leveraged_etf_aum`、`structural.treasury_basis_trade`）。

## 與前期比較

前次結論：無前次預測（report-2026-09-03 為舊格式評分報告）

本次是第一次以 yes/no 預測格式執行，前次的舊格式評分不轉換成 yes/no，flip_evidence 為空。自 2026-09-03 以來的主要變化：

- 10Y 殖利率上升 18 bps 到 4.95%，10Y 實質殖利率上升 13 bps 到 2.55%；同期 10Y breakeven 只上升 1 bp，但涵蓋的視窗不一致，因此判讀為「不可判（視窗不一致）」（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。
- VIX 從 14.32 升到 17.84，MOVE 從 74.68 升到 82.21；S&P 500 自前次基準下跌 1.17%（`structural.vix_spx_comove`、`structural.treasury_basis_trade`、`valuation.sp500_trend`）。
- WTI 從 92.55 美元升到 97.26 美元（+5.09%）（`monetary.wti`）。
- HY OAS 只擴大 5 bps、IG OAS 收窄 1 bp，信用端沒有跟著股市與利率波動惡化（`monetary.hy_oas`、`monetary.ig_oas`）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

未披露（✗ NOT DISCLOSED）的項目：valuation.analyst_tp_decomposition、valuation.ai_credit_schism、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.private_credit_liquidity、ai.token_growth、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（quarterly_state 有取得，event_scan 30 日內無事件）、ai.depreciation_life、ai.capital_cycle（兩個組件都沒有可用披露）、speculation.upcoming_ai_ipos、structural.global_leveraged_approvals。其中影響最大的是 valuation.ai_credit_schism 與 monetary.private_credit_liquidity：它們是 R3 最早的預警。如果有實際的利差走闊或 gate proration / breach 而本次沒有抓到，答案可能需要往 yes 方向重新評估；但 HY OAS、repo 指標都很平穩，間接降低了這個風險。

資料一致性備註：case/evidence.md 記載美債基差交易槓桿的「script 三區塊 fetch_failed」，但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 三塊都是 status ok，且資料日期都在 14 日窗口內。本報告以 macro artifact 為準，記為 ✓ API。

其他缺漏：hyperscaler capex 只取得四家合計數，沒有逐家指引與前次指引對照，因此 R2 的逐家方向無法判定。如果其中已有一家下修而本次沒有抓到，R2 的距離會比本報告描述的更近。speculation.insider_form4 的 Form 4 證據只有一個日期（2026-09-02），沒有分列申報日與交易日。

最大的不確定性：

- 9/16 FOMC：如果升息並釋出持續緊縮的訊號，長端利率會再上行，這是 R1 與 R3 最直接的推力（往 yes）；如果按兵不動或語氣偏鴿，壓力就會減輕（往 no）。
- 2026 Q3 hyperscaler 財報（日期本次未取得）：如果出現兩家 capex 下修，R2 會直接成立（往 yes）；如果持續上修，就會延續 no。
- 高槓桿 AI 借款人的再融資：本次 14 日內沒有信用定價數據，而利率上行會加大再融資成本；一旦出現 distressed exchange，R3 會成立並可能連帶觸發 R1（往 yes）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7656.98 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 6.9 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29368.44 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 4.21 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q2 季資料，家戶股票占金融資產 %） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.7 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.8 | FRED API (series_id=BAMLC0A0CM) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.95 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.55 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.36 | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（美元／桶） | 97.26 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-08 月資料，YoY %） | 3.35 | FRED API (series_id=CPIAUCSL) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.32 | FRED API (series_id=T5YIFR) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright 10Y 期限溢價 %） | 0.8892 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API (series_id=SOFR99) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-09-13 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6740619.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5912178.0（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6446620.0（¥644.66T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 17.84 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（7 日窗口 2026-09-03 → 2026-09-10，comove=false） | 17.84 | FRED API (series_id=VIXCLS, SP500) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2027.9777（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -6863118 | CFTC TFF futures-only | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 82.21 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2271.6 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl / GuruFocus，WebSearch primary | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch（CNBC 等） | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch，90d＋同季 | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch，14d | ✗ NOT DISCLOSED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch（FINRA 月資料，stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch，7d | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch primary | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py；DFEDTARU ok，DFEDTARL ok | ✓ API |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series | scripts/fetch_macro.py；SOFR ok，SOFR99 ok，IORB ok，RPONTTLD ok | ✓ API |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch，14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py；ECBASSETSW ok，JPNASSETS ok | ✓ API |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing / liquidity operations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch，30d | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（季報指引，stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch；quarterly_state 沿用最近季度，event_scan 30d 無事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch＋既有 bullets 組合 | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動（depreciation useful-life change） | WebSearch，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch；兩個組件都沒有可用披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch，7d | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch，30d | ✗ NOT DISCLOSED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR / WebSearch，14d | ✓ SEARCH-VERIFIED |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com feed，30d | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch，7d | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py；VIXCLS ok，vix_spx_comove ok | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch，30d | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py；cftc_lev_funds ok，move_index ok，ofr_repo ok | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.73（預定來源 multpl / GuruFocus） | S&P 500 Shiller CAPE ratio current September 2026 multpl | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | Magnificent 7 forward P/E valuation September 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html（CNBC） | 2026-08-03 | 2026-09-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 至 7 月止 YTD 報酬約 13% | RSP equal weight vs SPY S&P 500 YTD performance September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度約 38% | S&P 500 top 10 concentration percentage September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 200 日均線之上約 53% | market breadth advance decline new highs lows September 2026 percent stocks above 200-day | https://condoredge.com/stocks/market-breadth（Condor Edge） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 35（恐懼） | CNN Fear and Greed Index today September 2026 reading | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）約 1.42 兆美元 | FINRA margin debt August 2026 record year over year | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026（Advisor Perspectives，FINRA 資料） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.0% | AAII sentiment survey results week September 10 2026 bullish bearish neutral | https://www.aaii.com/sentimentsurvey（AAII） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.71 | Treasury auction results September 2026 tail bid-to-cover 10-year | https://thevaultreport.com/treasury-auctions（The Vault Report） | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.fedwatch | 9/16 FOMC 升息 25 bps 市場隱含機率約 85.5% | CME FedWatch September 12 2026 probability 25 basis point hike | https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html（Yahoo Finance，引 CME FedWatch） | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate financing 2026 total social financing | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm（SteelOrbis） | 2026-08-15 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 7,250 億美元（2026 Q2 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 650 億美元 | OpenAI Anthropic annualized revenue run rate September 2026 | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| ai.compute_supply_demand | H100 中位租金約 3.38 美元／小時 | GPU rental price HBM DRAM contract price September 2026 utilization | https://www.thundercompute.com/blog/ai-gpu-rental-market-trends（Thunder Compute） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 增額債務約占 capex 32%（2026 Q2 財報季） | hyperscaler capex vs free cash flow debt issuance 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 1,050 億美元（分母：top-4 hyperscaler capex 約 7,250 億美元） | AI revenue vs capex gap 2026 annualized run rate | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描：0 件合格事件 | AI company name change ticker SPAC announcement September 7-13 2026 | 檢查來源：SPACInsider、Businesswire SPAC newsroom、Boardroom Alpha | — | 2026-09-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 22 檔 | IPO priced week September 8 2026 first day return debut | https://www.iposcoop.com/current-year-pricings/（IPOScoop） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描：0 件符合 2+ 主題×弱基本面（Tenon +77%、AEON +35% 都未達門檻） | biggest stock gainers week September 7 2026 microcap 100% quantum AI | 檢查來源：Finviz、Benzinga、StockTitan、Yahoo movers | — | 2026-09-13T09:30:00+08:00 |
| speculation.insider_form4 | NVDA 董事 Stevens 出售約 3.85 億美元（Form 4；證據只列一個日期，未分列申報日與交易日） | insider selling Form 4 September 2026 Nvidia AI executives SEC filing | https://www.sec.gov/Archives/edgar/data/0001045810/000119903926000012/wk-form4_1788387031.xml（SEC EDGAR） | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 約 0.67（未標明是單日還是 5 日平均） | Cboe equity put call ratio September 2026 reading | https://www.thetrading.tools/put-call-ratio（thetrading.tools） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 407.4 億美元；標題：Traders pull $751M from single-stock ETFs | leveraged ETF assets under management September 2026 record single stock | https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/（ETF Action） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval September 2026 | 檢查來源：SEC EDGAR、ETF.com 新上市 feed | — | 2026-09-13T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 占成交量比重創紀錄約 62%（2026-08 月資料） | 0DTE options share SPX volume September 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.options_volume | OCC 8 月總結算量約 14.4 億口（2026-08 月資料） | OCC options volume August 2026 monthly report | https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/（Traders Magazine） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 收在 17 以上，call skew 位於第 91 百分位 | fear gauge VIX hedges September 10 2026 volatility | https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html（CNBC） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-07 月資料）對股票市值比率，基數約 1.42 兆美元 | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php（Current Market Valuation） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Qualcomm 對 Amazon 發行認股權證約 40 億美元（vendor-financing loop） | Qualcomm warrants Amazon 4 billion AI infrastructure deal September 2026 | https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html（CNBC） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-09-13",
  "iso_week": "2026-W37",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-03-14",
  "prior_date": "2026-09-03",
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 4.21,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

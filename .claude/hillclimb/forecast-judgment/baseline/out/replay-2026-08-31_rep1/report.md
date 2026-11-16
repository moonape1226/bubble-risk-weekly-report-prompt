> [DRY RUN] this report was not committed to archive.

# 2026-08-31 AI 泡沫破裂預測報告

報告日期：2026-08-31｜ISO 週次：2026-W36｜預測窗口：2026-08-31 → 2027-03-01｜前次基準：report-2026-08-27（4天前）

## 結論

**結論：no**

三條路徑都離觸發很遠：NASDAQ-100 距 52 週高點回撤 4.00%，還要再跌約 21.87% 才達 R1 門檻；檢索到的資料中，四大 hyperscaler 都沒有下修 capex 指引（2026 合計約 725（十億美元））；HY OAS 2.63% 與 CoreWeave 2026-08-10 順利完成 2.6 十億美元融資，顯示 AI 信用端沒有立即的違約壓力。估值與槓桿偏高，說明下跌時幅度會很大，但目前沒有證據顯示破裂會在 182 天內發生。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

依 `valuation.ndx_drawdown`：NASDAQ-100 最新收盤 29,433.43（2026-08-28），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 4.00%。R1 門檻水位為 22,995.45，最新收盤須再下跌約 21.87% 才會觸及。價格趨勢方面，`valuation.sp500_trend` 顯示 S&P 500 為 7,711.76（2026-08-28），高於 200 日均線 8.33%、高於 52 週均線 9.76%，較前次基準日 -0.25%：價格偏離趨勢，有均值回歸空間，但還不是失序下跌。波動面上，`structural.vix_spx_comove` 在 2026-08-20 → 2026-08-27 的 7 日窗口內，VIX 由 16.01 降至 14.51（-9.37%），S&P 500 +1.18%，comove = false，沒有出現「指數漲、避險需求同步被搶高」的擁擠讀數。

**判讀：** R1 距門檻約 21.87%，目前沒有正在進行中的回撤。要在窗口內觸發，需要外部催化劑，例如信用重定價、hyperscaler 下修 capex 指引，或利率衝擊，並引發強制去槓桿（槓桿 ETF 與 0DTE 部位會放大跌幅）。

### R2 資本支出收縮

依 `ai.hyperscaler_capex`（CNBC，2026-07-28），四大 hyperscaler（Microsoft、Alphabet、Amazon、Meta）2026 年 capex 合計約 725（十億美元），報導重點是 Alphabet 財報後市場對 capex 的審視升高，而不是指引下修。本次檢索結果只有四家合計值，沒有逐家拆分：

- Microsoft：最新指引沿用最近一季財報（本次未取得逐家數值），本次證據中未見下修。
- Alphabet：最新指引沿用 2026-07 財報（本次未取得逐家數值）；市場審視升高，但未見下修。
- Amazon：最新指引沿用最近一季財報（本次未取得逐家數值），本次證據中未見下修。
- Meta：最新指引沿用最近一季財報（本次未取得逐家數值），本次證據中未見下修。

目前已下修的家數：本次證據中為 0 家。預測窗口（至 2027-03-01）大致涵蓋兩輪季報（2026 Q3 與 2026 Q4／全年財報），但本次檢索沒有取得確切財報日期。AI 營收對 capex 缺口（revenue-to-capex gap）、資本週期階段（capital cycle stage）與 hyperscaler 融資結構（capex vs FCF / 發債）本次都沒有可用的新披露（見資料缺漏）。

**判讀：** R2 需要四家中兩家正式下修。目前看到的是「投資人審視升高」，還沒有任何一家下修。可能把 R2 推過門檻的情境，是 Q3 或 Q4 財報出現 ROI 壓力，或市場大幅回撤後企業主動收縮 capex（R1 → R2 傳導）。

### R3 AI 信用事件

依 `structural.ai_infrastructure_debt`，CoreWeave 於 2026-08-10 宣布完成 DDTL 5.5 融資，金額 2.6 十億美元，以 GPU 作擔保。這屬於 AI infrastructure debt financing / vendor-financing loops 的新增槓桿，同時也說明融資市場對最主要的 neocloud 借款人仍然開放。本次證據沒有 CoreWeave 的總負債數字，所以不在此認定它是否符合 R3 的 50 億美元門檻。整體信用面，依 `monetary.hy_oas`，HY OAS 為 2.63%（2026-08-27）；依 `monetary.ig_oas`，IG OAS 為 0.79%，都處於偏窄水準。依 `monetary.repo_stress_srf`，repo 資金壓力（SOFR−IORB）為 -1.0 bps、SOFR99−IORB 為 7.0 bps（皆 2026-08-27），SRF 動用僅 0.001（十億美元，2026-08-28），看不到資金市場壓力。AI 信用定價分歧（equity-vs-credit schism）與私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）本次都沒有窗口內的披露。

**判讀：** 本次證據中沒有任何 AI 算力借款人出現付款違約、covenant 豁免、distressed exchange 或 going-concern 語句；新融資能順利完成，信用利差也偏窄。R3 要在窗口內成立，需要融資窗口突然關閉，或租約／客戶合約違約連鎖發生。目前看不到這樣的前兆。

## 支持 yes 的證據

- [整體] 估值處於歷史極端：Shiller CAPE 41.59（2026-08-01），代表一旦出現催化劑，下跌幅度會很大 `valuation.sp500_pe_cape`
- [R1] 槓桿與投機部位集中：槓桿 ETF 總 AUM 198（十億美元），其中 TQQQ 37.3、SOXL 22（2026-08-28）；SPX 0DTE 約佔期權量 60%（2026-08-28），一旦下跌容易被放大 `structural.leveraged_etf_aum` `structural.zero_dte`
- [R1] 散戶槓桿偏高：FINRA margin debt 1.42 兆美元，YoY +38.6%（2026-07 月資料），接近歷史頂部常見的 +40–50% 區間 `retail.margin_debt`
- [R2] 市場開始質疑 capex：CNBC（2026-07-28）報導 Alphabet 財報後，hyperscaler 面臨更高的 capex 審視，四家 2026 capex 合計約 725（十億美元） `ai.hyperscaler_capex`
- [R1] 尾部避險需求偏高：Cboe SKEW 143.9、股債相關性轉正（2026-08-24），代表股債分散效果下降 `structural.cross_asset_derivatives`
- [整體] 集中度高：S&P 500 前十大權重 37.6%（2026-07-31），AI 龍頭若轉弱，指數層級會直接受到衝擊 `breadth.top10_concentration`
- [整體] Fed 緩衝空間有限：CPI YoY 3.3%（2026-07 月資料），10Y 期限溢價（term premium）0.8682%（2026-08-21，7 日 +2.9 bps），一旦 AI 主導下跌，降息救市受到通膨約束 `monetary.cpi_yoy` `monetary.term_premium`

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.00%（2026-08-28 收盤 29,433.43 vs 2026-06-02 高點 30,660.6），距 R1 門檻 22,995.45 還差約 21.87% `valuation.ndx_drawdown`
- [R3] 信用市場沒有壓力：HY OAS 2.63%、IG OAS 0.79%（2026-08-27）；repo 資金壓力（SOFR−IORB）-1.0 bps（2026-08-27） `monetary.hy_oas` `monetary.ig_oas` `monetary.repo_stress_srf`
- [R3] AI 算力借款人融資窗口仍然開放：CoreWeave 2026-08-10 完成 2.6 十億美元 GPU 擔保 DDTL 融資 `structural.ai_infrastructure_debt`
- [R2] 本次證據中四大 hyperscaler 都沒有下修 capex 指引，2026 合計約 725（十億美元）（2026-07-28） `ai.hyperscaler_capex`
- [整體] 情緒不是狂熱：CNN Fear & Greed 為中性 54（2026-08-28）；AAII 看多 32.9%、看空 44.4%（2026-08-26），看空多於看多 `retail.fear_greed` `retail.aaii`
- [R1] 波動面平靜：VIX 14.51（2026-08-27），7 日 -9.37%，與 S&P 500 沒有同漲（comove = false）；MOVE 70.97（2026-08-28） `structural.vix_spx_comove` `structural.treasury_basis_trade`
- [整體] 市場廣度沒有過度集中：equal-weight 與 cap-weight YTD 分別為 9.67% 與 8.38%（2026-08-28），等權重表現優於市值加權 `breadth.rsp_spy`

## 與前期比較

前次結論：無前次預測（report-2026-08-27 為舊格式評分報告）

本次是新格式下的第一份預測，flip_evidence 為空。和 2026-08-27 相比，可觀察到的 macro 變化很小：DGS10、DFII10、HY OAS、IG OAS 都沒有新觀測（Δ = 0，持平）；T10YIE -2.0 bps、T5YIFR -3.0 bps；S&P 500 -0.25%；RPONTTLD 由 0.101 降至 0.001（十億美元）。10Y Δ 分解判讀：不可判（視窗不一致），因為 DGS10、DFII10 沒有新觀測（partial_stale），只有 T10YIE 更新。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED 來源（檢索有完成，但窗口內沒有合格披露）：valuation.analyst_tp_decomposition、valuation.ai_credit_schism、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.treasury_auctions、monetary.pboc、monetary.private_credit_liquidity、ai.token_growth、ai.openai_anthropic_revenue、ai.customer_concentration_rpo、ai.compute_supply_demand、ai.hyperscaler_financing_mix、ai.revenue_capex_gap、ai.depreciation_life、ai.capital_cycle、speculation.upcoming_ai_ipos、structural.global_leveraged_approvals。其中 AI 信用定價分歧（equity-vs-credit schism）與私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）缺少資料，對 R3 判讀影響最大：如果兩者其實出現利差走闊或 gate proration / breach，R3 的距離會被高估。不過 HY OAS 偏窄，加上 CoreWeave 新融資順利完成，兩者是一致的反證，因此這個缺口不太可能改變本次答案。

其他資料注意事項：
- 搜尋紀錄寫著美債基差交易槓桿的 script blocks 為 fetch_failed，但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 都是 status: ok。本次以 artifact 為準（✓ API），WebSearch 補充的交易商資產負債表／平倉新聞則沒有窗口內的披露。
- R2 只取得四家合計 capex，沒有逐家指引與前次指引的比較，也沒有確切的下一次財報日期。如果其中一家其實已在最近一季微幅下修，R2 的距離會比這裡寫的更近。
- S&P 500 P/E 本次沒有取得，只取得 CAPE。
- R3 規模門檻：本次證據沒有 CoreWeave 等 neocloud 的總負債數字，無法列出確定符合 50 億美元門檻的借款人名單。

最大的不確定性：
1. 窗口內的兩輪 hyperscaler 財報（2026 Q3 與 Q4／全年指引）：如果有兩家以上把「審視升高」轉成正式下修，答案會往 yes 移動。
2. AI 算力借款人的再融資：融資市場目前開放；如果利率或期限溢價急升、融資窗口關閉，R3 與 R1 可能連鎖觸發，答案會往 yes 移動。
3. 通膨與 Fed：CPI 3.3%、FedWatch 隱含 9 月維持利率的市場定價為 58.6%（2026-08-25）。Fed 寬鬆空間有限，會讓任何下跌更難被政策緩衝，往 yes 方向；但目前尚無衝擊發生。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7711.76 | FRED API (series_id=SP500) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線偏離 %） | 8.33 | FRED API (series_id=SP500) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線偏離 %） | 9.76 | FRED API (series_id=SP500) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（NASDAQ-100 最新收盤） | 29433.43 | FRED API (series_id=NASDAQ100) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-31T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.0 | FRED API (series_id=NASDAQ100) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（家計股票配置 %，2026 Q1） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-31T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-30 | 2026-08-31T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-30 | 2026-08-31T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 2.63 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（IG OAS %） | 0.79 | FRED API (series_id=BAMLC0A0CM) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（10Y 殖利率 %） | 4.67 | FRED API (series_id=DGS10) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（10Y 實質殖利率 %） | 2.34 | FRED API (series_id=DFII10) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（10Y breakeven %） | 2.31 | FRED API (series_id=T10YIE) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（WTI 美元／桶） | 83.9 | FRED API (series_id=DCOILWTICO) | 2026-08-25 | 2026-08-31T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（CPI YoY %，2026-07 月資料） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-31T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（5y5y 遠期通膨 %） | 2.32 | FRED API (series_id=T5YIFR) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（10Y 期限溢價（term premium）%，Kim-Wright） | 0.8682 | FRED API (series_id=THREEFYTP10) | 2026-08-21 | 2026-08-31T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.64 | FRED API (series_id=SOFR) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.72 | FRED API (series_id=SOFR99) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-31 | 2026-08-31T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.001 | FRED API (series_id=RPONTTLD) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| monetary.walcl | WALCL latest（Fed 資產負債表） | 6730912.0（$6.73T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-26 | 2026-08-31T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（ECB 資產負債表） | 5913041.0（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-21 | 2026-08-31T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（BOJ 資產負債表） | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-31T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest（VIX） | 14.51 | FRED API (series_id=VIXCLS) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（7 日窗口 2026-08-20 → 2026-08-27） | 14.51 | FRED API (series_id=VIXCLS, SP500) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（VIX 7 日變動 %） | -9.37 | FRED API (series_id=VIXCLS) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（銀行對 NBFI 放款，十億美元） | 2026.2859（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-19 | 2026-08-31T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（槓桿基金美債期貨淨部位，口） | -7003041 | CFTC TFF futures-only | 2026-08-25 | 2026-08-31T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（MOVE） | 70.97 | Yahoo Finance chart API (^MOVE) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2355.4 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（gurufocus）[primary: SEARCH] | ✓ SEARCH-VERIFIED（CAPE；P/E 未取得） |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch（CNBC） | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch，90d 且同季 | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch，14d | ✗ NOT DISCLOSED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch（Yahoo Finance） | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch（P&I） | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch（StockCharts） | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch（Advisor Perspectives） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch，7d | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch [primary: SEARCH] | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（FRED 直接取得，非 derived） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch，14d | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing / liquidity operations | WebSearch | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch，30d | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（CNBC），stock-of-state | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✗ NOT DISCLOSED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✗ NOT DISCLOSED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch：quarterly_state stock-of-state＋event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch | ✗ NOT DISCLOSED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch：quarterly_state stock-of-state＋event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（Seeking Alpha） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch，30d | ✗ NOT DISCLOSED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR / WebSearch，14d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com，30d | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch，7d | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch，30d | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）＋WebSearch 補充 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok；WebSearch 補充無窗口內披露） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 41.59（原定來源 multpl / gurufocus） | shiller cape ratio august 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-08-01 | 2026-08-31T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權前瞻本益比 24 | magnificent 7 forward pe august 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html（CNBC） | 2026-08-03 | 2026-08-31T09:30:00+08:00 |
| breadth.rsp_spy | equal-weight vs cap-weight YTD：9.67% vs 8.38% | rsp vs spy ytd 2026 | https://finance.yahoo.com/markets/stocks/articles/rsp-vs-spy-does-equal-185007075.html（Yahoo Finance） | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度 37.6% | sp500 top 10 concentration 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/（Pensions & Investments） | 2026-07-31 | 2026-08-31T09:30:00+08:00 |
| breadth.advance_decline | 成分股站上 50 日均線比率 54% | market breadth advance decline august 2026 | https://articles.stockcharts.com/article/mindfulinvestor-2026-08-weakening-market-breadth-could-signal-trouble-ahead/（StockCharts） | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 中性 54 | cnn fear greed index august 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）1.42 兆美元、YoY +38.6% | finra margin debt july 2026 | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026（Advisor Perspectives，原定 FINRA） | 2026-07-31 | 2026-08-31T09:30:00+08:00 |
| retail.aaii | AAII 看多 32.9% 看空 44.4% | aaii sentiment august 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-08-26 | 2026-08-31T09:30:00+08:00 |
| monetary.fedwatch | FedWatch 9 月維持利率隱含定價 58.6% | cme fedwatch september 2026 | https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html（CME Group） | 2026-08-25 | 2026-08-31T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計 725（十億美元），Alphabet 財報後 capex 審視升高（2026 Q2 財報季） | hyperscaler capex 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-08-31T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 掃描：0 件窗口內符合 | +AI rename SPAC aug 24-31 2026 | 檢查來源：SPACInsider、Boardroom Alpha、Businesswire | — | 2026-08-31T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 39 件、BRVE 首週 +67% | ipo market august 2026 | https://seekingalpha.com/article/4933637-august-kicks-off-with-flurry-of-biotech-ipos（Seeking Alpha） | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描：0 件同時符合 2+ 主題與弱基本面 | microcap moonshot quantum ai aug 24-31 2026 | 檢查來源：Finviz、Benzinga、StockTitan | — | 2026-08-31T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 集中賣出掃描：0 件合格 | insider form 4 nvidia aug 2026 | 檢查來源：SEC EDGAR | — | 2026-08-31T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.52（日讀數），9 日均 0.85 | cboe equity put call ratio august 2026 | https://www.thetrading.tools/put-call-ratio（thetrading.tools） | 2026-08-19 | 2026-08-31T09:30:00+08:00 |
| structural.leveraged_etf_aum | 槓桿 ETF 總 AUM 198（十億美元）；TQQQ 37.3、SOXL 22 | leveraged etf aum record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing） | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件經查證日期 | single stock leveraged etf launch aug 2026 | 檢查來源：SEC EDGAR、ETF.com | — | 2026-08-31T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 約佔期權量 60% | 0dte spx share 2026 | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/（Cboe） | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| structural.options_volume | OCC 月報（2026-07 月資料）ETF 期權 YoY +26%、總日均量 71 | occ july 2026 options volume | https://mondovisione.com/media-and-resources/news/occ-july-2026-monthly-volume-data-202686（Mondo Visione，原定 OCC） | 2026-07-31 | 2026-08-31T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 期限結構 contango、股債相關轉正、SKEW 143.9 | vix term structure skew august 2026 | https://www.thetrading.tools/vix-term-structure（thetrading.tools） | 2026-08-24 | 2026-08-31T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率 confirmation（2026-07 月資料，1.42 兆美元） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php（Current Market Valuation） | 2026-07-31 | 2026-08-31T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave DDTL 5.5 融資完成 2.6 十億美元（GPU 擔保） | coreweave debt facility august 2026 | https://investors.coreweave.com/news/news-details/2026/CoreWeave-Closes-2-6-Billion-Loan-Facility-Expanding-Financing-Flexibility-for-AI-Infrastructure/default.aspx（CoreWeave IR） | 2026-08-10 | 2026-08-31T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-31",
  "iso_week": "2026-W36",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-03-01",
  "prior_date": "2026-08-27",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 4.0,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

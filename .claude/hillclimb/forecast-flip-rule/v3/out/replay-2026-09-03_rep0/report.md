> [DRY RUN] this report was not committed to archive.

# 2026-09-03 AI 泡沫破裂預測報告

報告日期：2026-09-03｜ISO 週次：2026-W36｜預測窗口：2026-09-03 → 2027-03-04｜前次基準：report-2026-08-31（3天前）

## 結論

**結論：no**

三條路徑都還遠離觸發點：NASDAQ-100 距 52 週高點回撤 4.95%，距 R1 門檻仍需再跌約 21.10%（`valuation.ndx_drawdown`）；HY OAS 2.65%、IG OAS 0.81% 仍處緊縮水位（`monetary.hy_oas`、`monetary.ig_oas`），CoreWeave 於 2026-08-10 仍能完成約 26 億美元融資（`structural.ai_infrastructure_debt`），本次證據中沒有任何 hyperscaler 下修 capex 或 AI 借款人違約的訊號。估值極端（CAPE 約 41.6）只說明泡沫存在與下行幅度，不足以推翻 182 天內不破裂的 base rate。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

FRED `NASDAQ100` 最新收盤 29143.33（2026-09-02），252 個交易日最高收盤 30660.6（2026-06-02），距 52 週高點回撤 4.95%（`valuation.ndx_drawdown`）。R1 門檻水位為 22995.45，自最新收盤需再下跌約 21.10% 才會觸發。周邊價格訊號：S&P 500 7666.6（2026-09-02），高於 200 日均線 7.5%、高於 52 週均線 8.89%，較前次基準日 -0.25%（`valuation.sp500_trend`）；VIX 16.34（2026-09-01），trailing 7 日（2026-08-25 → 2026-09-01）VIX +5.76% 而 S&P 500 -0.6%，未構成同漲警戒（comove = false，`structural.vix_spx_comove`）；CNN Fear & Greed 33.8（恐懼，2026-09-02，`retail.fear_greed`）。

**判讀：** R1 距離最遠的一次觸發仍需約 21% 的進一步下跌；只有在信用重定價、AI 獲利預期大幅下修或 hyperscaler capex 轉向等催化劑同時出現時，才可能在窗口內完成，目前價格趨勢仍在長期均線之上，尚無此類催化劑證據。

### R2 資本支出收縮

本次取得的最新 hyperscaler capex 資料為 2026-07-28 CNBC 報導：Microsoft、Alphabet、Amazon、Meta 四家 2026 年 capex 合計約 725（十億美元），屬 2026 年 Q2 財報季（7 月下旬）所設之指引，沿用為 current 值（`ai.hyperscaler_capex`）。本次檢索結果只提供四家合計，未提供逐家最新指引數字與相較前次指引的方向；就已取得的證據，四家中沒有任何一家被報導下修（已下修家數：0／4），但逐家「上修／持平」的方向本次未能確立。下一次財報日期本次未取得來源，故不列具體日期；依季度節奏，窗口（至 2027-03-04）內將涵蓋兩個財報季。需求側對照：Anthropic 年化 run-rate 約 650 億美元（2026-08-17，`ai.openai_anthropic_revenue`）。

**判讀：** R2 需要四家中至少兩家正式下修指引；目前沒有任何一家下修的證據，而需求端營收仍在擴張。要在窗口內觸發，通常需先出現 R1 式的市場重挫或 AI 營收／利用率明顯轉弱，現階段證據不支持。

### R3 AI 信用事件

本次可確認的 AI infrastructure debt financing / vendor-financing loops 事件：CoreWeave 於 2026-08-10 公告完成約 26 億美元融資（SEC EDGAR ex99.1，`structural.ai_infrastructure_debt`），顯示市場仍對該類借款人開放。CoreWeave 為 AI 算力主業借款人，但其總負債規模本次未取得來源確認，因此是否達 R3 的 50 億美元門檻在本報告中未確立。AI 信用定價分歧（equity-vs-credit schism）14 日掃描、hyperscaler 融資結構（capex vs FCF / 發債）與私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）本次皆無合格披露，因此沒有 AI 借款人的利差、CDS、評等行動、即將到期債務或寬限期違約的當期資料。整體信用環境：HY OAS 2.65%（2026-09-01，`monetary.hy_oas`）、IG OAS 0.81%（`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）1.0 bp、SOFR99−IORB 9.0 bp（2026-09-01），SRF 動用（Standing Repo Facility usage）0.0（十億美元，2026-09-02）（`monetary.repo_stress_srf`）。

**判讀：** R3 需要破產申請、逾寬限期付款違約或 distressed exchange；目前沒有任何困境訊號，近期仍有成功融資、整體信用利差緊縮。若窗口內出現 AI 借款人利差急遽走闊、再融資失敗或 covenant 豁免，才會轉向 yes，但本次無此證據。

## 支持 yes 的證據

- [整體] 估值處於極端水位：Shiller CAPE 約 41.6（2026-08-31），代表一旦觸發，下行空間大，`valuation.sp500_pe_cape`。
- [R1] 投機性選擇權活動升溫：SPX 0DTE 佔期權量於 2026 年 8 月創紀錄約 62%（2026-08-31），`structural.zero_dte`；Cboe SKEW 約 148.5、股債相關偏正（2026-08-31），`structural.cross_asset_derivatives`。
- [R1] 短線風險指標轉弱：VIX 7 日 +5.76% 至 16.34 而 S&P 500 -0.6%（2026-09-01），`structural.vix_spx_comove`；MOVE 79.71（2026-09-02），較前次基準日 +4.39，`structural.treasury_basis_trade`；CNN Fear & Greed 33.8（恐懼，2026-09-02），`retail.fear_greed`。
- [整體] Fed 緩衝空間受限：CPI YoY 3.3%（2026-07 資料），`monetary.cpi_yoy`；WTI 91.48 美元（2026-09-01），較前次基準日 +5.11%，`monetary.wti`；10Y 殖利率 4.79%（2026-09-01），`monetary.dgs10`；10Y 期限溢價（term premium）0.8751%（2026-08-28），`monetary.term_premium`。
- [整體] 投機與槓桿行為仍在：Arena Group 更名 Paradium.AI、2026-08-31 起以 PAAI 交易（7 日內 1 件），`speculation.ai_rename_spac`；美國槓桿 ETF 總 AUM 約 198（十億美元，2026-08-15），`structural.leveraged_etf_aum`；FINRA margin debt 約 1.42 兆美元（2026-07 資料），`retail.margin_debt`。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.95%（2026-09-02），距 R1 門檻 22995.45 仍需再跌約 21.10%，`valuation.ndx_drawdown`；S&P 500 仍高於 200 日均線 7.5%，`valuation.sp500_trend`。
- [R3] 信用市場沒有重定價：HY OAS 2.65%、IG OAS 0.81%（2026-09-01），`monetary.hy_oas`、`monetary.ig_oas`；CoreWeave 2026-08-10 完成約 26 億美元融資，市場通道開放，`structural.ai_infrastructure_debt`。
- [R2] hyperscaler capex 指引未見下修：四家 2026 capex 合計約 725（十億美元，2026-07-28），`ai.hyperscaler_capex`；需求端 Anthropic 年化 run-rate 約 650 億美元（2026-08-17），`ai.openai_anthropic_revenue`。
- [整體] 融資市場平穩：repo 資金壓力（SOFR−IORB）1.0 bp、SOFR99−IORB 9.0 bp（2026-09-01），SRF 動用 0.0（2026-09-02），`monetary.repo_stress_srf`；OFR tri-party repo transaction volume 2309.3（十億美元，2026-09-02），`structural.treasury_basis_trade`。
- [整體] Mag 7 估值並非全面失控：Mag 7 前瞻本益比低於 24（2026-08-03），`valuation.mag7_multiples`；散戶情緒偏謹慎，AAII 看多 32.9%（2026-08-28），`retail.aaii`。

## 與前期比較

前次結論：無前次預測（report-2026-08-31 為舊格式評分報告）

- 前次基準日為舊格式評分報告，其評分不轉換為 yes/no；本次 `flip_evidence` 為空。
- 自 2026-08-31 以來的宏觀變化：DGS10 +4.0 bp、DFII10 0.0 bp、T10YIE +3.0 bp；T10YIE 與另兩腿的視窗不同，分解判讀為 不可判（視窗不一致）（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。
- HY OAS +2.0 bp、IG OAS +1.0 bp、WTI +5.11%、MOVE +4.39、S&P 500 -0.25%；WALCL $6.73T 無新觀測（持平）（`monetary.walcl`）。這些幅度都不足以改變任一路徑判讀。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源檢索完成但無合格當期披露（✗ NOT DISCLOSED）：`valuation.analyst_tp_decomposition`、`valuation.ai_credit_schism`、`retail.social_sentiment`、`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.treasury_auctions`、`monetary.fedwatch`、`monetary.private_credit_liquidity`、`ai.token_growth`、`ai.customer_concentration_rpo`、`ai.compute_supply_demand`、`ai.hyperscaler_financing_mix`、`ai.depreciation_life`、`ai.capital_cycle`、`speculation.upcoming_ai_ipos`、`speculation.equity_put_call`、`structural.global_leveraged_approvals`。其中 `valuation.ai_credit_schism`、`ai.hyperscaler_financing_mix` 與 `monetary.private_credit_liquidity` 的缺口最可能影響 R3 判讀：若這些通道其實已有 AI 借款人利差走闊或贖回壓力，R3 會比本報告所見更接近；但目前整體 HY／IG 利差緊縮，缺口翻轉結論的可能性有限。`ai.token_growth` 唯一結果為 2026-05-20（前一季），`speculation.equity_put_call` 唯一讀數為 2026-08-07，皆非當期，不作證據。

其他資料品質註記：

- `breadth.rsp_spy` 唯一結果資料日為 2026-06-10，已非當期，本次不作證據；`breadth.advance_decline` 結果為「成分股在 50 日均線之上約 54%」，是廣度代理而非 A/D 比；`structural.margin_debt_crosscheck` 結果實為 margin debt 水位（約 1.42 兆美元），margin debt／股票市值比率本次未確立；`ai.revenue_capex_gap` 來源所述「缺口約 105」單位與分母未載明，不採用，改以已追蹤組件組合。
- evidence 結果表將美債基差交易槓桿（Treasury basis-trade leverage）記為 script blocks fetch_failed，但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 三塊皆為 `status: ok`；本報告以 macro artifact 為準，記 ✓ API。
- R2 逐家 capex 指引數字與方向本次未取得，僅有四家合計；CoreWeave 等 AI 借款人的總負債規模亦未確立。

最大的不確定性：

1. 窗口內兩個 hyperscaler 財報季（日期本次未確立）：若兩家下修 capex 指引即直接觸發 R2，推向 yes。
2. AI 借款人信用定價資料缺漏：若 AI 信用定價分歧開始以利差走闊呈現，可能是 R3 與 R1 的共同前導，推向 yes。
3. 通膨與油價：CPI 3.3%、WTI 走高壓縮 Fed 緩衝空間，若利率與期限溢價上行加速，可能放大估值回落，推向 yes；反之若緩解則強化 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest | 7666.6 | FRED API (series_id=SP500) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 7.5 | FRED API (series_id=SP500) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 8.89 | FRED API (series_id=SP500) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29143.33 | FRED API (series_id=NASDAQ100) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-09-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 4.95 | FRED API (series_id=NASDAQ100) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-09-03T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5 | FRED API (series_id=DFEDTARL) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.65 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.81 | FRED API (series_id=BAMLC0A0CM) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.79 | FRED API (series_id=DGS10) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.44 | FRED API (series_id=DFII10) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.34 | FRED API (series_id=T10YIE) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 91.48 | FRED API (series_id=DCOILWTICO) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-09-03T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.33 | FRED API (series_id=T5YIFR) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest | 0.8751 | FRED API (series_id=THREEFYTP10) | 2026-08-28 | 2026-09-03T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.66 | FRED API (series_id=SOFR) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.74 | FRED API (series_id=SOFR99) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-09-03 | 2026-09-03T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest | 0.0（十億美元） | FRED API (series_id=RPONTTLD) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6730912.0（$6.73T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-26 | 2026-09-03T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5915343.0（€5.92T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-28 | 2026-09-03T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-09-03T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.34 | FRED API (series_id=VIXCLS) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 16.34 | FRED API (series_id=VIXCLS, SP500) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 5.76 | FRED API (series_id=VIXCLS, SP500) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2026.2859（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-19 | 2026-09-03T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7003041 | CFTC TFF futures-only | 2026-08-25 | 2026-09-03T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 79.71 | Yahoo Finance chart API (^MOVE) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2309.3 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（gurufocus） | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch（CNBC） | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d、同季） | ✗ NOT DISCLOSED（無同季合格 TP 上修） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✗ NOT DISCLOSED（14 日內無合格報導） |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch（247wallst） | ✓ SEARCH-VERIFIED（資料日 2026-06-10，非當期） |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch（P&I） | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch（StockCharts） | ✓ SEARCH-VERIFIED（50 日均線之上占比代理） |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch（CNN） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（Advisor Perspectives） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch（AAII） | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch） | ✗ NOT DISCLOSED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch（gov.cn） | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（CNBC，carry-forward Q2 財報季） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED（唯一結果屬前一季） |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch（TechCrunch） | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✗ NOT DISCLOSED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch（quarterly_state stock_of_state；event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch＋已追蹤組件組合 | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch（quarterly_state stock_of_state；event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED（1 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（Renaissance Capital） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（Finviz、Benzinga、StockTwits、Yahoo） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✗ NOT DISCLOSED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR / WebSearch（14d） | ✓ SEARCH-VERIFIED |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch（YCharts） | ✗ NOT DISCLOSED（唯一讀數 2026-08-07，非當期） |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch（Benzinga） | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（KRX、TWSE、JPX、ESMA，7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC via Mondo Visione） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch（thetrading.tools） | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（currentmarketvaluation） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d，SEC EDGAR） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）；WebSearch 補充 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 41.6（原定來源 multpl / gurufocus） | shiller cape sp500 september 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-08-31 | 2026-09-03T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | magnificent 7 forward pe august 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html（CNBC） | 2026-08-03 | 2026-09-03T09:30:00+08:00 |
| breadth.rsp_spy | RSP 對 SPY YTD 領先幅度約 16.9（非當期） | rsp vs spy ytd 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-06-10 | 2026-09-03T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度約 37.6% | sp500 top 10 concentration 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/（Pensions & Investments） | 2026-07-31 | 2026-09-03T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 50 日均線之上約 54%（A/D 代理） | market breadth advance decline august 2026 | https://articles.stockcharts.com/article/mindfulinvestor-2026-08-weakening-market-breadth-could-signal-trouble-ahead/（StockCharts） | 2026-08-27 | 2026-09-03T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 33.8（恐懼） | cnn fear greed index september 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt 約 1.42 兆美元（2026-07 月資料） | finra margin debt july 2026 | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026（Advisor Perspectives，原定來源 FINRA） | 2026-07-31 | 2026-09-03T09:30:00+08:00 |
| retail.aaii | AAII 看多 32.9% | aaii sentiment august 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-08-28 | 2026-09-03T09:30:00+08:00 |
| monetary.pboc | 社會融資規模約 22.25 兆人民幣（2026-07 資料） | pboc aggregate financing july 2026 | https://english.www.gov.cn/（gov.cn，原定來源 PBoC / NBS） | 2026-08-15 | 2026-09-03T09:30:00+08:00 |
| ai.hyperscaler_capex | MSFT／GOOGL／AMZN／META 2026 capex 合計約 725（十億美元，Q2 財報季） | hyperscaler capex 2026 guidance | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-03T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 650 億美元 | anthropic annualized revenue august 2026 | https://techcrunch.com/2026/08/17/anthropics-annualized-revenue-surges-to-65b/（TechCrunch） | 2026-08-17 | 2026-09-03T09:30:00+08:00 |
| ai.revenue_capex_gap | 分子 Anthropic run-rate 約 650 億美元 vs 分母 top-4 capex 約 7250 億美元（分母：MSFT／GOOGL／AMZN／META，不含 Oracle）；來源所述「缺口約 105」單位未明，不採用 | ai revenue vs capex 2026 | https://techcrunch.com/2026/08/17/anthropics-annualized-revenue-surges-to-65b/（TechCrunch） | 2026-08-17 | 2026-09-03T09:30:00+08:00 |
| speculation.ai_rename_spac | Arena Group 更名 Paradium.AI，2026-08-31 起以 PAAI 交易（1 件） | arena group paradium.ai PAAI ticker august 2026 | https://www.businesswire.com/news/home/20260828769258/en/The-Arena-Group-dba-Paradium.AI-Completes-Name-Change-Will-Trade-Under-New-Stock-Ticker-PAAI-Effective-August-31-2026（Business Wire） | 2026-08-31 | 2026-09-03T09:30:00+08:00 |
| speculation.ipo_heat | 美股 IPO YTD 約 105 件 | ipo market 2026 renaissance capital | https://www.renaissancecapital.com/IPO-Center/Stats（Renaissance Capital） | 2026-08-28 | 2026-09-03T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描：0 件符合 2+ 主題×弱基本面 | microcap moonshot quantum ai aug 27 sep 3 2026 | 檢查來源：Finviz、Benzinga、StockTwits、Yahoo movers（量子族群屬較大市值） | — | 2026-09-03T09:30:00+08:00 |
| speculation.insider_form4 | NVDA 董事 Mark Stevens Form 4 出脫約 3.85 億美元（申報日 2026-09-02；交易日未於檢索結果顯示） | nvidia mark stevens form 4 september 2026 | https://www.sec.gov/Archives/edgar/data/0001045810/000119903926000012/wk-form4_1788387031.xml（SEC EDGAR） | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美國槓桿 ETF 總 AUM 約 198（十億美元） | leveraged etf aum 2026 record | https://www.benzinga.com/etfs/broad-u-s-equity-etfs/26/08/61419951/leveraged-single-stock-etf-closures-went-from-3-to-63-in-a-year-as-money-piles-into-nvidia-bets（Benzinga，原定來源 etf.com / ETFGI） | 2026-08-15 | 2026-09-03T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件（新品為主題型 2x） | single stock leveraged etf launch aug 2026 | 檢查來源：SEC EDGAR、ETF.com（Leverage Shares 新品屬主題 2x） | — | 2026-09-03T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔期權量創紀錄約 62%（2026-08） | spx 0dte share record august 2026 | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-31 | 2026-09-03T09:30:00+08:00 |
| structural.options_volume | OCC 期權日均約 7100 萬口（2026-07 月資料） | occ july 2026 options volume | https://mondovisione.com/media-and-resources/news/occ-july-2026-monthly-volume-data-202686（Mondo Visione，原定來源 OCC） | 2026-07-31 | 2026-09-03T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 期限結構 contango、股債相關偏正、Cboe SKEW 約 148.5 | vix skew term structure august 2026 | https://www.thetrading.tools/skew-index（thetrading.tools） | 2026-08-31 | 2026-09-03T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 約 1.42 兆美元（2026-07 月資料；比率本次未確立） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php（Current Market Valuation） | 2026-07-31 | 2026-09-03T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave 完成約 26 億美元融資 | coreweave 2.6 billion loan covenant august 2026 | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000357/ex991pr.htm（SEC EDGAR） | 2026-08-10 | 2026-09-03T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-09-03",
  "iso_week": "2026-W36",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-03-04",
  "prior_date": "2026-08-31",
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 4.95,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

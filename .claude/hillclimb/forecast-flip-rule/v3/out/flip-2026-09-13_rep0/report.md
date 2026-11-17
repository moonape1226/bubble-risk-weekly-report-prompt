> [DRY RUN] this report was not committed to archive.

# 2026-09-13 AI 泡沫破裂預測報告

報告日期：2026-09-13｜ISO 週次：2026-W37｜預測窗口：2026-09-13 → 2027-03-14｜前次基準：report-2026-09-03（10天前）

## 結論

**結論：no**

三條路徑都沒有已在進行中的證據：NASDAQ-100 距 52 週高點回撤僅 4.21%，距 R1 門檻仍需再跌約 21.70%（`valuation.ndx_drawdown`）；四大 hyperscaler 2026 capex 合計約 725、本次檢索未見任何一家下修（`ai.hyperscaler_capex`）；HY OAS 2.7%、IG OAS 0.8% 仍處緊縮水位，未見 AI 信用事件傳導（`monetary.hy_oas`、`monetary.ig_oas`）。估值與集中度顯示泡沫脆弱度高，但利率上行與 Fed 升息預期這類催化劑尚不足以在 182 天內推翻「三條件皆不成立」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29368.44（2026-09-11），252 個交易日最高收盤 30660.6（2026-06-02），距 52 週高點回撤 4.21%；R1 門檻水位 22995.45，自最新收盤需再下跌約 21.70% 才觸及（`valuation.ndx_drawdown`）。前次（2026-09-03）回撤為 4.95%，本次略為收斂。S&P 500 最新 7656.98（2026-09-11），高於 200 日均線 6.9%、高於 52 週均線 8.33%，較前次 −1.17%（`valuation.sp500_trend`）。近一週波動率上升：VIX 17.84（2026-09-10），trailing 7 日（2026-09-03 → 2026-09-10）VIX +24.58%、S&P 500 −2.01%，屬一般避險反應而非同漲（comove=false）（`structural.vix_spx_comove`）；MOVE 82.21（2026-09-11），較前次 74.68 上升 7.53（`structural.treasury_basis_trade`）。利率端 10Y 殖利率 4.95%（2026-09-10，+18bp），10Y 實質利率 2.55%（+13bp），T10YIE 2.36%（2026-09-11，+1bp）；因 T10YIE 視窗與 DGS10／DFII10 不一致，本次 Δ 分解判讀：不可判（視窗不一致）（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。CME FedWatch 顯示 9/16 FOMC 升息 25bp 機率約 85.5%（2026-09-12）（`monetary.fedwatch`）。

**判讀：** R1 距離門檻仍遠（需再跌約 21.70%）。要在窗口內觸發，需要利率上行／Fed 升息與 AI 盈利預期修正同時發生，或 R3／R2 事件反向傳導至股價；目前僅見波動率回升，未見強制去槓桿或信用重定價。

### R2 資本支出收縮

本次檢索僅取得四大 hyperscaler（Microsoft、Alphabet、Amazon、Meta）2026 capex 合計約 725 的彙總數字（CNBC，2026-07-28，2026 年 7 月財報季後）（`ai.hyperscaler_capex`），未逐家取得最新正式指引數值：

- Microsoft：最新指引隸屬 2026-07 財報季；逐家數值與方向本次未取得，未見下修報導。
- Alphabet：同上；來源標題提及 Alphabet 財報後 capex 受市場質疑，但未載下修。
- Amazon：同上，未見下修報導。
- Meta：同上，未見下修報導。

已確認下修家數：0／4。依季度財報節奏，窗口（至 2027-03-14）內應涵蓋四家各兩次季報（Q3、Q4），但本次檢索未取得確切財報日期。配套觀察：年化 AI 終端營收約 105（Axios，2026-08-17），對照年化 capex 約 725（分母：top-4，不含 Oracle 與 neocloud），缺口顯著，但本次無前次組合值，擴大／收斂方向不可判（`ai.revenue_capex_gap`）；H100 中位租金約 3.38（2026-08-31），單點水位未配合利用率或庫存證據，不構成過剩訊號（`ai.compute_supply_demand`）。

**判讀：** R2 未啟動。窗口內有兩次財報可觸發下修，但目前證據是 capex 仍高位、市場質疑而非公司下修；需至少兩家在 Q3 或 Q4 財報正式下修才會成立。

### R3 AI 信用事件

本次 AI 信用定價掃描（14 日）未取得 AI 發行人債券利差或 CDS 的當期報導，故無法對特定借款人的信用定價作判讀。過去 30 日 AI infrastructure debt financing / vendor-financing loops 掃描僅見 Qualcomm 對 Amazon 約 4 十億美元認股權證的資料中心基礎建設交易（CNBC，2026-09-08）（`structural.ai_infrastructure_debt`），屬供應商對買方的權益誘因安排，不是違約或困境訊號。本次未取得任何符合 R3 門檻（負債 ≥ 50 億美元、以 AI 資料中心／算力為主業）借款人的負債規模、到期牆或評等動作——這些數字本次未建立。整體信用環境：HY OAS 2.7%（2026-09-10，+5bp）、IG OAS 0.8%（−1bp）（`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 −3bp、SOFR99−IORB 為 5bp（2026-09-10），SRF 動用 0（2026-09-11）（`monetary.repo_stress_srf`）；銀行對 NBFI 放款 $2.03T（2026-09-02）持平（`structural.nbfi_bank_loans`）。

**判讀：** R3 無已知困境中的合格借款人，整體信用利差緊、資金市場平穩。要在窗口內成立，需要某家大型 neocloud／資料中心借款人出現付款違約或 distressed exchange，目前沒有任何前兆證據。

## 支持 yes 的證據

- [R1] 利率與政策緊縮催化劑：10Y 殖利率 4.95%（2026-09-10，較 2026-09-03 +18bp），10Y 實質利率 2.55%（+13bp），CME FedWatch 顯示 9/16 FOMC 升息機率約 85.5%（2026-09-12），WTI 97.26（2026-09-09，+5.09%），CPI YoY 3.35%（2026-08 月資料）壓縮 Fed 緩衝空間（`monetary.dgs10`、`monetary.dfii10`、`monetary.fedwatch`、`monetary.wti`、`monetary.cpi_yoy`）
- [整體] 估值與集中度極端：Shiller CAPE 約 40.73（2026-09-01），S&P 500 前十大集中度約 38%（2026-09-01），下跌時的放大效應大（`valuation.sp500_pe_cape`、`breadth.top10_concentration`）
- [R1] 波動率同步上升：VIX 17.84（2026-09-10），trailing 7 日 +24.58%；MOVE 82.21（2026-09-11，+7.53）；VIX call skew 第 91 百分位（2026-09-10）（`structural.vix_spx_comove`、`structural.treasury_basis_trade`、`structural.cross_asset_derivatives`）
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）大：年化 AI 終端營收約 105（2026-08-17）對年化 capex 約 725（分母：top-4），若營收追不上，財報季時有下修壓力（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`）
- [整體] 投機性衍生品活動高：SPX 0DTE 佔比創紀錄約 62%（2026-08 月資料），8 月 OCC 總結算量約 1.44 十億口（`structural.zero_dte`、`structural.options_volume`）
- [R3] vendor-financing loops 持續：Qualcomm 對 Amazon 約 4 十億美元認股權證（2026-09-08），顯示供應商以權益誘因綁定買方（`structural.ai_infrastructure_debt`）

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.21%（2026-09-11），R1 門檻 22995.45 需再跌約 21.70%；回撤較前次 4.95% 收斂（`valuation.ndx_drawdown`）
- [R2] 四大 hyperscaler 2026 capex 合計約 725（2026-07-28），本次檢索未見任何一家下修，已確認下修 0／4（`ai.hyperscaler_capex`）
- [R3] 信用利差仍緊：HY OAS 2.7%、IG OAS 0.8%（2026-09-10），repo 資金壓力（SOFR−IORB）−3bp、SRF 動用 0（2026-09-11），無信用重定價或資金壓力傳導（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`）
- [整體] 情緒並非狂熱：CNN Fear & Greed 約 35（恐懼，2026-09-10），AAII 看多約 38.0%（2026-09-10），equity put/call 約 0.67（2026-09-01），不符合頂部常見的極端貪婪（`retail.fear_greed`、`retail.aaii`、`speculation.equity_put_call`）
- [整體] 基準率：182 天內 R1–R3 任一成立本屬少見事件；S&P 500 高於 200 日均線 6.9%（2026-09-11），延伸程度溫和，Mag 7 前瞻本益比低於 24（2026-08-03）（`valuation.sp500_trend`、`valuation.mag7_multiples`）
- [R1] 市場寬度未崩：S&P 500 成分股在 200 日均線之上約 53%（2026-09-11）（`breadth.advance_decline`）

## 與前期比較

前次結論：yes（report-2026-09-03）

本次結論：翻轉

翻轉依據：

前次 forecast.json 未含 yes_basis 欄位（寫入時尚無此欄位），因此沒有可逐項回應的前次決定性理由；前次的 yes 不能沿用，必須由本次證據重新支持。以下為本次證據不足以支持 yes 的依據：

- `valuation.ndx_drawdown`：R1 回撤由前次 4.95% 收斂至 4.21%（2026-09-11），距門檻仍需再跌約 21.70%，市場回撤路徑沒有在推進。
- `ai.hyperscaler_capex`：最新資料仍為四大 hyperscaler 2026 capex 合計約 725（2026-07-28），本次無任何一家下修，R2 路徑未啟動。
- `monetary.hy_oas`：HY OAS 2.7%（2026-09-10）僅較前次 +5bp，仍處緊縮水位；本次也未取得任何 AI 借款人困境證據，R3 沒有可支持 yes 的依據。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED 來源（掃描完成但無合格當期披露）：valuation.analyst_tp_decomposition、valuation.ai_credit_schism、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.private_credit_liquidity、ai.token_growth、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（quarterly_state 有值、event_scan 無 30 日事件）、ai.depreciation_life、ai.capital_cycle（兩個組件皆無可用證據，增速證據不足，本次不判定週期階段）、speculation.upcoming_ai_ipos、structural.global_leveraged_approvals。其中 AI 信用定價分歧與私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）的缺漏與 R3 最相關：若其中有未被發現的利差走闊或 gate proration / breach，可能使 R3 判讀轉向 yes，但整體 HY／IG OAS 與 repo 數據均未顯示壓力，因此判斷不太可能改變本次答案。

其他註記：

- 證據檔的搜尋結果摘要寫 Treasury basis-trade 的腳本三區塊 fetch_failed，但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 皆為 status ok；本次以 artifact 為準記為 ✓ API。
- speculation.insider_form4：找到一筆 NVDA Form 4（2026-09-02，董事 Stevens 出脫約 385 百萬美元），但檢索結果未顯示交易日期，不符合 filing date＋transaction date 的要求，故不列為具名證據，該篩選記為 0 件。
- R2 四家逐家最新正式指引數值與方向本次未取得，只有合計數。若任一家實際已在 2026-07 下修，R2 距離會比本次判讀更近。

最大不確定性：

1. 9/16 FOMC：若照市場預期升息，或發出更強硬的訊號，利率上行可能壓低高估值科技股，使答案往 yes 推（R1）；若維持不變則往 no。
2. 下一次 hyperscaler 季報（Q3，確切日期本次未取得）：若有兩家 hyperscaler 下修 capex 指引即直接成立 R2，往 yes；若再度上修則強化 no。
3. 大型 AI 基礎建設借款人的負債規模與到期牆本次未建立；若後續揭露再融資困難，R3 風險會上升，往 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7656.98 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 6.9 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.33 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29368.44 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.21 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（家庭股票配置 %，2026Q2 季資料） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（Fed funds 上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（Fed funds 下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 2.7 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（IG OAS %） | 0.8 | FRED API (series_id=BAMLC0A0CM) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（10Y 殖利率 %） | 4.95 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（10Y 實質利率 %） | 2.55 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（10Y breakeven %） | 2.36 | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（WTI 美元／桶） | 97.26 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（CPI YoY %，2026-08 月資料） | 3.35 | FRED API (series_id=CPIAUCSL) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（5y5y forward %） | 2.32 | FRED API (series_id=T5YIFR) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（10Y 期限溢價（term premium），Kim-Wright %） | 0.8892 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API (series_id=SOFR99) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-09-13 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest（Fed 資產負債表） | 6740619.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（ECB 資產） | 5912178.0（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（BOJ 資產） | 6446620.0（¥644.66T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest（VIX） | 17.84 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（trailing 7 日，base 2026-09-03） | 17.84 | FRED API (series_id=VIXCLS, SP500) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（%） | 24.58 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（%） | -2.01 | FRED API (series_id=SP500) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（銀行對 NBFI 放款） | 2027.9777（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（槓桿基金美債期貨淨部位，口） | -6863118 | CFTC TFF futures-only | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（MOVE） | 82.21 | Yahoo Finance chart API (^MOVE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2271.6 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（multpl / GuruFocus） | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch（14d） | ✗ NOT DISCLOSED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API DFEDTARU=ok, DFEDTARL=ok |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（FRED BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（FRED BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（FRED DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（FRED T10YIE） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（FRED DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（FRED T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API SOFR=ok, SOFR99=ok, IORB=ok, RPONTTLD=ok |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py | ✓ API ECBASSETSW=ok, JPNASSETS=ok（no_new_obs） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing / liquidity operations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state，2026-07 財報季） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch：quarterly_state stock-of-state＋event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch（stock-of-state 組合） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch：quarterly_state stock-of-state＋event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✗ NOT DISCLOSED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR / WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API VIXCLS=ok, vix_spx_comove=ok |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds / move_index / ofr_repo（any） | ✓ API cftc_lev_funds=ok, move_index=ok, ofr_repo=ok |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.73（原定來源 multpl / GuruFocus） | S&P 500 Shiller CAPE ratio current September 2026 multpl | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | Magnificent 7 forward P/E valuation September 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html（CNBC） | 2026-08-03 | 2026-09-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 至 7 月止 YTD 報酬約 13% | RSP equal weight vs SPY S&P 500 YTD performance September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.top10_concentration | 前十大集中度約 38% | S&P 500 top 10 concentration percentage September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 200 日均線之上約 53% | market breadth advance decline new highs lows September 2026 percent stocks above 200-day | https://condoredge.com/stocks/market-breadth（Condor Edge） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 約 35（恐懼） | CNN Fear and Greed Index today September 2026 reading | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）約 1.42 兆美元；本次未取得 YoY | FINRA margin debt August 2026 record year over year | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026（Advisor Perspectives，原定來源 FINRA） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.0% | AAII sentiment survey results week September 10 2026 bullish bearish neutral | https://www.aaii.com/sentimentsurvey（AAII） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.71 | Treasury auction results September 2026 tail bid-to-cover 10-year | https://thevaultreport.com/treasury-auctions（The Vault Report） | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.fedwatch | 9/16 FOMC 升息 25bp 機率約 85.5% | CME FedWatch September 12 2026 probability 25 basis point hike | https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html（Yahoo Finance，原定來源 CME FedWatch） | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣（2026-07 月資料） | PBoC aggregate financing 2026 total social financing | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm（SteelOrbis） | 2026-08-15 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 725（2026-07 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65 | OpenAI Anthropic annualized revenue run rate September 2026 | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| ai.compute_supply_demand | H100 中位租金約 3.38 | GPU rental price HBM DRAM contract price September 2026 utilization | https://www.thundercompute.com/blog/ai-gpu-rental-market-trends（Thunder Compute） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 增額債務佔 capex 約 32%（背景；event_scan 30 日無合格事件） | hyperscaler capex vs free cash flow debt issuance 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 105（分子）；分母取 ai.hyperscaler_capex 約 725（top-4） | AI revenue vs capex gap 2026 annualized run rate | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement September 7-13 2026 | 檢查來源：SPACInsider、Businesswire SPAC newsroom、Boardroom Alpha（窗內無合格事件） | — | 2026-09-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 22 檔 | IPO priced week September 8 2026 first day return debut | https://www.iposcoop.com/current-year-pricings/（IPOScoop） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（0 件符合 2+ 主題×弱基本面） | biggest stock gainers week September 7 2026 microcap 100% quantum AI | 檢查來源：Finviz、Benzinga、StockTitan、Yahoo movers（Tenon +77%、AEON +35% 皆未達門檻） | — | 2026-09-13T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 14 日篩選（0 件合格：唯一結果 NVDA 2026-09-02 未顯示交易日期） | insider selling Form 4 September 2026 Nvidia AI executives SEC filing | 檢查來源：SEC EDGAR（https://www.sec.gov/Archives/edgar/data/0001045810/000119903926000012/wk-form4_1788387031.xml） | — | 2026-09-13T09:30:00+08:00 |
| speculation.equity_put_call | equity put/call 約 0.67 | Cboe equity put call ratio September 2026 reading | https://www.thetrading.tools/put-call-ratio（The Trading Tools，原定來源 Cboe） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.74 | leveraged ETF assets under management September 2026 record single stock | https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/（ETF Action） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval September 2026 | 檢查來源：SEC EDGAR、ETF.com 新上市 feed（窗內無合格核准或上市） | — | 2026-09-13T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比創紀錄約 62%（2026-08 月資料） | 0DTE options share SPX volume September 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.options_volume | 8 月 OCC 總結算量約 1.44 十億口（2026-08 月資料） | OCC options volume August 2026 monthly report | https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/（Traders Magazine） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 收在約 17 以上、call skew 第 91 百分位 | fear gauge VIX hedges September 10 2026 volatility | https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html（CNBC） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 1.42 兆美元（2026-07 月資料） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php（Current Market Valuation） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Qualcomm 對 Amazon 認股權證約 4 十億美元（資料中心基礎建設交易） | Qualcomm warrants Amazon 4 billion AI infrastructure deal September 2026 | https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html（CNBC） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |

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
  "prior_answer": "yes",
  "flip_evidence": ["valuation.ndx_drawdown", "ai.hyperscaler_capex", "monetary.hy_oas"],
  "yes_basis": [],
  "r1_drawdown_pct": 4.21,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

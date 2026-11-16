> [DRY RUN] this report was not committed to archive.

# 2026-09-13 AI 泡沫破裂預測報告
報告日期：2026-09-13｜ISO 週次：2026-W37｜預測窗口：2026-09-13 → 2027-03-14｜前次基準：report-2026-09-03（10天前）

## 結論

**結論：yes**

維持前次 yes：驅動路徑是 R1——市場正把 9/16 FOMC 升息約 85.5% 定價進去（`monetary.fedwatch`，2026-09-12），10Y 殖利率一週內上升 18bp 至 4.95%、CPI YoY 3.35%（`monetary.dgs10`、`monetary.cpi_yoy`），而這個緊縮觸媒正落在 Shiller CAPE 約 40.73、前十大權重約 38% 的高脆弱市場上（`valuation.sp500_pe_cape`、`breadth.top10_concentration`）。自 2026-09-03 以來沒有任何新資料削弱這條路徑，新增的利率、波動率讀數反而朝同一方向移動，因此依翻轉紀律不改判。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29368.44（2026-09-11），252 個交易日最高收盤 30660.6（2026-06-02），距 52 週高點回撤 4.21%（`valuation.ndx_drawdown`）。R1 門檻水位為 22995.45，自最新收盤還需再跌約 6,373 點（約 21.70%）才會觸發。S&P 500 收 7656.98（2026-09-11），高於 200 日均線 6.9%、高於 52 週均線 8.33%，自前次基準日以來下跌 1.17%（`valuation.sp500_trend`）。估值與集中度處於極端區：Shiller CAPE 約 40.73（2026-09-01，`valuation.sp500_pe_cape`），前十大權重約 38%（`breadth.top10_concentration`），僅約 53% 成分股在 200 日均線之上（`breadth.advance_decline`）。觸媒端：FedWatch 定價 9/16 FOMC 升息約 85.5%（`monetary.fedwatch`），目前政策利率 3.50%–3.75%（`monetary.fed_funds`）；10Y 4.95%（+18bp）、10Y 實質利率 2.55%（+13bp）（`monetary.dgs10`、`monetary.dfii10`）；WTI 97.26 美元（+5.09%，`monetary.wti`）；CPI YoY 3.35%（2026-08 月資料，`monetary.cpi_yoy`），5y5y 2.32%（`monetary.t5yifr`）——通膨讓 Fed 緩衝 AI 引發回撤的空間有限。VIX 自 14.32 升至 17.84（+24.58%），同期 S&P 500 −2.01%，屬正常的反向變動，不是 crowded-optionality 共振（`structural.vix_spx_comove`）；MOVE 82.21（+7.53，`structural.treasury_basis_trade`）。情緒並不亢奮：CNN Fear & Greed 約 35（恐懼，`retail.fear_greed`）、AAII 看多約 38.0%（`retail.aaii`）。

**判讀：** 距門檻仍約 21.70%，R1 尚未啟動。若要在窗口內成立，需要升息循環重啟並帶動實質利率續升，再疊加 AI 盈利或 capex 敘事失望，使高 CAPE、高集中度的指數在 6 個月內出現 1 次 25% 等級的重估；9/16 FOMC 與之後的季報季是窗口內最可能的推升節點。

### R2 資本支出收縮

本次證據只取得四大 hyperscaler（Microsoft、Alphabet、Amazon、Meta）2026 年 capex 合計約 7,250 億美元，取自 2026-07-28 的季報季報導（`ai.hyperscaler_capex`）；本次證據沒有逐家列出的指引金額，所以四家各自相對前次正式指引的方向（上修／持平／下修）無法逐一確認，在此不推定。報導期間未出現任何一家下修指引的披露，目前已下修家數：0／4。供給側價格訊號：H100 中位租金約 3.38 美元／小時（2026-08-31，`ai.compute_supply_demand`）。只有價格單點，沒有利用率或去化證據，因此無法判定產能過剩。需求側：Anthropic 年化 run-rate 約 650 億美元（2026-08-17，`ai.openai_anthropic_revenue`）；AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 1,050 億美元 vs 年化 capex 約 7,250 億美元（分母：top-4，Oracle 缺當期組件），兩者差距很大（`ai.revenue_capex_gap`）。下一次財報日期未載於本次證據，但窗口（至 2027-03-14）涵蓋兩個季報季。

**判讀：** R2 距成立最遠——目前 0 家下修，而且需要兩家在窗口內正式下修。只有在 R1 式市場重挫或融資成本急升迫使管理層收縮時，下一兩個季報季才可能出現連鎖下修。

### R3 AI 信用事件

本次沒有取得 AI 資料中心／neocloud 個別發行人的債券利差、CDS 或評等動作，AI 信用定價分歧的 14 日掃描也沒有找到合格報導；窗口內沒有任何借款人的付款違約、豁免或 distressed exchange 披露。廣義信用仍極度寬鬆：HY OAS 2.70%（+5bp）、IG OAS 0.80%（−1bp）（`monetary.hy_oas`、`monetary.ig_oas`）。vendor-financing loops：Qualcomm 向 Amazon 發出約 40 億美元認股權證，綁定資料中心基礎設施合作（2026-09-08，`structural.ai_infrastructure_debt`），屬供應商以股權誘因換取客戶採購的循環安排。資金面無壓力：SOFR−IORB −3bp、SOFR99−IORB +5bp、SRF 動用 0（`monetary.repo_stress_srf`）；銀行對 NBFI 放款約 $2.03T（`structural.nbfi_bank_loans`）。

**判讀：** R3 缺少任何已知的困境借款人，信用利差也看不出對 AI 債務的重定價，R3 要在窗口內獨立成立的可能性低；較可能的路徑是 R1 重挫後再融資窗口關閉，才把高槓桿 neocloud 推向違約。

## 支持 yes 的證據

- [R1] 緊縮觸媒正在成形：FedWatch 於 2026-09-12 定價 9/16 FOMC 升息約 85.5%，10Y 殖利率在 2026-09-10 達 4.95%（較 2026-09-03 +18bp），10Y 實質利率 2.55%（+13bp），CPI YoY 3.35%、WTI 97.26 美元，Fed 對股市回撤的緩衝空間受限（`monetary.fedwatch`、`monetary.dgs10`、`monetary.dfii10`、`monetary.cpi_yoy`、`monetary.wti`）。
- [R1] 脆弱性極高：Shiller CAPE 約 40.73（2026-09-01）、前十大權重約 38%（2026-09-01）、僅約 53% 成分股在 200 日均線之上（2026-09-11），漲勢集中，一旦重估，回撤幅度大（`valuation.sp500_pe_cape`、`breadth.top10_concentration`、`breadth.advance_decline`）。
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 1,050 億美元 vs 四大 hyperscaler capex 約 7,250 億美元（分母：top-4），報酬遠落後投入（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`）。
- [R1] 波動率與利率波動同步升溫：VIX 由 14.32 升至 17.84（2026-09-10，+24.58%），MOVE 82.21（2026-09-11，+7.53），同時 call skew 位於第 91 百分位（2026-09-10）（`structural.vix_spx_comove`、`structural.treasury_basis_trade`、`structural.cross_asset_derivatives`）。
- [R3] vendor-financing loops 擴大：Qualcomm 對 Amazon 約 40 億美元認股權證（2026-09-08）（`structural.ai_infrastructure_debt`）。
- [整體] 投機結構仍偏熱：SPX 0DTE 佔比達紀錄約 62%（2026-08 月），單週 IPO 定價約 22 檔（2026-09-11），8 月 OCC 總結算量約 14.4 億口（`structural.zero_dte`、`speculation.ipo_heat`、`structural.options_volume`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.21%（2026-09-11），距 R1 門檻 22995.45 還需再跌約 21.70%；S&P 500 仍高於 200 日均線 6.9%，趨勢未破（`valuation.ndx_drawdown`、`valuation.sp500_trend`）。
- [R3] 信用市場沒有壓力：HY OAS 2.70%、IG OAS 0.80%（2026-09-10），repo 資金壓力（SOFR−IORB）−3bp、SRF 動用 0（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`）。
- [R2] 四大 hyperscaler 2026 年 capex 合計仍約 7,250 億美元（2026-07-28），沒有任何一家下修，需求側 Anthropic run-rate 約 650 億美元（2026-08-17）仍在擴張（`ai.hyperscaler_capex`、`ai.openai_anthropic_revenue`）。
- [整體] 基準率：任一 182 天窗口內 R1–R3 皆不成立是常態；情緒指標顯示恐懼而非狂熱（Fear & Greed 約 35、AAII 看多約 38.0%，2026-09-10），單一個股槓桿 ETF 規模約 407.4 億美元且出現資金撤出（2026-09-08）（`retail.fear_greed`、`retail.aaii`、`structural.leveraged_etf_aum`）。
- [R1] 估值的 AI 核心反而不貴：Mag 7 前瞻本益比低於 24（2026-08-03）（`valuation.mag7_multiples`）。

## 與前期比較

前次結論：yes（report-2026-09-03）
本次結論：維持

- NASDAQ-100 回撤由前次 4.95% 收窄至 4.21%（`valuation.ndx_drawdown`，2026-09-11）：距門檻的距離只小幅變動，不足以改變 R1 分析。
- 利率與政策觸媒朝 yes 方向加強：10Y +18bp 至 4.95%，FedWatch 定價 9/16 升息約 85.5%（`monetary.dgs10`、`monetary.fedwatch`）；這支持前次結論，不構成翻轉理由。
- VIX +24.58%、MOVE +7.53（`structural.vix_spx_comove`、`structural.treasury_basis_trade`）：波動升溫與前次判斷一致。
- 信用面持平：HY OAS 由 2.65% 微升至 2.70%、IG OAS 0.81% → 0.80%（`monetary.hy_oas`、`monetary.ig_oas`）；仍無 R3 壓力，但前次已知此狀態，屬舊資訊。
- 自 2026-09-03 以來沒有任何來源出現削弱 R1／R2／R3 路徑的新證據（沒有 capex 新指引、沒有信用重定價、沒有政策轉鴿），依翻轉紀律保留前次答案，flip_evidence 為空。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下 ✗ NOT DISCLOSED 項目的搜尋已完成，但窗口內沒有合格披露：valuation.analyst_tp_decomposition、valuation.ai_credit_schism、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.private_credit_liquidity、ai.token_growth、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（event_scan 無新事件）、ai.depreciation_life、ai.capital_cycle、speculation.upcoming_ai_ipos、structural.global_leveraged_approvals。其中 AI 信用定價分歧與私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）的空白最可能影響答案：若其實已有未被搜到的 AI 發行人利差走闊或 gate proration / breach，R3 與 R1 的連動會更強，答案仍維持 yes。若兩者都確實平靜，則只削弱 R3，不影響以 R1 為主的判斷。

補充：speculation.insider_form4 的搜尋找到一筆 NVDA 董事 Form 4（2026-09-02），但證據只顯示單一日期，缺少可分辨的交易日，不符合 filing-level 揭露要求，因此不作為具名證據，記為 0 件。structural.treasury_basis_trade 的證據摘要寫「script 三區塊 fetch_failed」，但 macro artifact 顯示 cftc_lev_funds、move_index、ofr_repo 皆為 status ok，本報告以 artifact 為準記為 ✓ API。R2 的逐家指引金額與方向未在本次證據中，無法逐家驗證。

最大不確定性：
1. 9/16 FOMC 結果：若如定價升息且釋出續升訊號，R1 機會上升（推向 yes）；若按兵不動或轉鴿，最主要的觸媒消失（推向 no）。
2. 下一個 hyperscaler 季報季：任一家下修 capex 指引都會同時推進 R2 並衝擊 AI 敘事（推向 yes）；全面上修則削弱 R1、R2 兩條路徑（推向 no）。
3. AI 基礎設施債務的再融資狀況：本次沒有取得個別發行人的定價；若高利率持續，neocloud 再融資壓力浮現會推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7656.98 | FRED API (series_id=SP500) via fetch_macro.py sp500_trend | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 6.9 | FRED API (series_id=SP500) via fetch_macro.py sp500_trend | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.33 | FRED API (series_id=SP500) via fetch_macro.py sp500_trend | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（NASDAQ-100 最新收盤） | 29368.44 | FRED API (series_id=NASDAQ100) via fetch_macro.py ndx_drawdown | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) via fetch_macro.py ndx_drawdown | 2026-06-02 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 4.21 | FRED API (series_id=NASDAQ100) via fetch_macro.py ndx_drawdown | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) via fetch_macro.py ndx_drawdown | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（家庭股票配置 %，2026-Q2 資料） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 2.7 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（IG OAS %） | 0.8 | FRED API (series_id=BAMLC0A0CM) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（10Y 殖利率 %） | 4.95 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（較 2026-09-03） | 18.0 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（10Y 實質利率 %） | 2.55 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps（較 2026-09-03） | 13.0 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（10Y breakeven %） | 2.36 | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（WTI 美元／桶） | 97.26 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（CPI YoY %，2026-08 月資料） | 3.35 | FRED API (series_id=CPIAUCSL) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（5y5y %） | 2.32 | FRED API (series_id=T5YIFR) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（10Y 期限溢價（term premium）%，Kim-Wright） | 0.8892 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API (series_id=SOFR99) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-09-13 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps（同日 2026-09-10 兩腿） | -3.0 | fetch_macro.py repo_stress block (FRED) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest（Fed 資產負債表） | 6740619.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（ECB 資產負債表） | 5912178.0（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（BOJ 資產負債表，no_new_obs） | 6446620.0（¥644.66T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest（VIX） | 17.84 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（共振視窗 VIX） | 17.84 | fetch_macro.py vix_spx_comove block (FRED) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日，base 2026-09-03） | 24.58 | fetch_macro.py vix_spx_comove block (FRED) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日，comove=false） | -2.01 | fetch_macro.py vix_spx_comove block (FRED) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（銀行對 NBFI 放款，十億美元，no_new_obs） | 2027.9777（$2.03T） | FRED API (series_id=LNFACBW027SBOG) | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（槓桿基金美債期貨淨部位，口數） | -6863118 | CFTC TFF via fetch_macro.py cftc_lev_funds | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（4 週變動，口數） | 387809 | CFTC TFF via fetch_macro.py cftc_lev_funds | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（MOVE） | 82.21 | Yahoo chart ^MOVE via fetch_macro.py move_index | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo 交易量，十億美元） | 2271.6 | OFR STFM via fetch_macro.py ofr_repo | 2026-09-11 | 2026-09-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（GuruFocus） | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch（CNBC） | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch 90d 同季掃描 | ✗ NOT DISCLOSED（搜尋完成，窗口內無合格 TP 上修） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch 14d 掃描 | ✗ NOT DISCLOSED（搜尋完成，窗口內無合格報導） |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch（247wallst） | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch（247wallst） | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch（condoredge） | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail / CNN Fear & Greed Index | WebSearch（CNN） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail / Margin Debt: FINRA | WebSearch（Advisor Perspectives，FINRA 7 月資料沿用） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail / Retail survey: AAII | WebSearch（AAII） | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail / Social sentiment proxies | WebSearch 7d | ✗ NOT DISCLOSED（無顯著討論） |
| retail.household_equity_allocation | Retail / Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED（無當期週值） |
| institutional.bofa_jpm_survey | Institutional / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED（無新月調查） |
| monetary.fed_funds | Monetary / Fed funds rate: FRED | fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok、DFEDTARL ok） |
| monetary.hy_oas | Monetary / High Yield OAS | fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary / Investment Grade OAS | fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary / 10Y Treasury yield | fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary / 10Y Treasury real yield | fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary / 10Y breakeven inflation rate | fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary / WTI crude oil price | fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary / CPI YoY: FRED | fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary / 5y5y forward inflation expectation | fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary / 10Y 期限溢價（term premium）: FRED | fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD） | ✓ API（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） |
| monetary.treasury_auctions | Monetary / 美債標售需求 | WebSearch 14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary / Fed funds rate path expectations | WebSearch（Yahoo Finance 引 CME FedWatch） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary / Fed balance sheet: FRED | fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary / Global central bank liquidity cross-check | fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok、JPNASSETS ok） |
| monetary.pboc | Monetary / PBoC aggregate financing | WebSearch（SteelOrbis） | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary / Private-credit / non-bank fund liquidity stress | WebSearch 30d | ✗ NOT DISCLOSED（窗口內無合格披露） |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | WebSearch（CNBC，2026-07 季報季沿用） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | WebSearch（Axios） | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | WebSearch（Thunder Compute） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構 | WebSearch：quarterly_state 沿用 CNBC 2026-07-28；event_scan 30d 無新事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口 | WebSearch（Axios）＋ ai.hyperscaler_capex 分母 | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動 | WebSearch 30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI / 資本週期階段 | WebSearch：quarterly_state 與 event_scan 30d 皆無可用披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculation / Search for past 7 days | WebSearch 7d（SPACInsider、Businesswire、Boardroom Alpha） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculation / IPO market heat | WebSearch（IPOScoop） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculation / Microcap thematic moonshots | WebSearch（Finviz、Benzinga、StockTitan、Yahoo movers） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculation / Upcoming AI IPOs | WebSearch 30d | ✗ NOT DISCLOSED |
| speculation.insider_form4 | Speculation / Insider selling at AI | SEC EDGAR / WebSearch 14d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculation / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural / US leveraged ETF AUM | WebSearch（ETF Action） | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com 30d | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural / Global leveraged product approvals | WebSearch 7d | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural / Options total volume | WebSearch（Traders Magazine 引 OCC） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural / Cross-asset derivatives / correlation checks | WebSearch（CNBC） | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural / VIX / S&P 500 co-movement | fetch_macro.py（VIXCLS、vix_spx_comove） | ✓ API（VIXCLS ok、vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural / Cross-reference only: FINRA margin debt | WebSearch（currentmarketvaluation） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural / AI infrastructure debt financing / vendor-financing loops | WebSearch 30d（CNBC） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural / Bank loans to nondepository financial institutions | fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py（cftc_lev_funds、move_index、ofr_repo） | ✓ API（cftc_lev_funds ok、move_index ok、ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.73（原定來源 multpl / GuruFocus） | S&P 500 Shiller CAPE ratio current September 2026 multpl | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | Magnificent 7 forward P/E valuation September 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html（CNBC） | 2026-08-03 | 2026-09-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 至 7 月止 YTD 報酬約 13% | RSP equal weight vs SPY S&P 500 YTD performance September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度約 38% | S&P 500 top 10 concentration percentage September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 200 日均線之上約 53% | market breadth advance decline new highs lows September 2026 percent stocks above 200-day | https://condoredge.com/stocks/market-breadth（Condor Edge） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 35（恐懼） | CNN Fear and Greed Index today September 2026 reading | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt 約 1.42 兆美元（2026-07 月資料） | FINRA margin debt August 2026 record year over year | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026（Advisor Perspectives） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.0% | AAII sentiment survey results week September 10 2026 bullish bearish neutral | https://www.aaii.com/sentimentsurvey（AAII） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.71 | Treasury auction results September 2026 tail bid-to-cover 10-year | https://thevaultreport.com/treasury-auctions（The Vault Report） | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.fedwatch | 9/16 FOMC 升息 25bp 定價約 85.5%（原定來源 CME FedWatch） | CME FedWatch September 12 2026 probability 25 basis point hike | https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html（Yahoo Finance） | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.pboc | 2026 年 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate financing 2026 total social financing | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm（SteelOrbis） | 2026-08-15 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 7,250 億美元（2026-07 季報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 650 億美元 | OpenAI Anthropic annualized revenue run rate September 2026 | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| ai.compute_supply_demand | H100 中位租金約 3.38 美元／小時 | GPU rental price HBM DRAM contract price September 2026 utilization | https://www.thundercompute.com/blog/ai-gpu-rental-market-trends（Thunder Compute） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 增額債務佔 capex 約 32%（背景沿用） | hyperscaler capex vs free cash flow debt issuance 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 1,050 億美元（分母：top-4 capex 約 7,250 億美元） | AI revenue vs capex gap 2026 annualized run rate | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描：0 件合格事件 | AI company name change ticker SPAC announcement September 7-13 2026 | 檢查來源：SPACInsider、Businesswire SPAC newsroom、Boardroom Alpha | — | 2026-09-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 22 檔 | IPO priced week September 8 2026 first day return debut | https://www.iposcoop.com/current-year-pricings/（IPOScoop） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描：0 件符合 2+ 主題×弱基本面（Tenon +77%、AEON +35% 未達門檻） | biggest stock gainers week September 7 2026 microcap 100% quantum AI | 檢查來源：Finviz、Benzinga、StockTitan、Yahoo movers | — | 2026-09-13T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 14 日掃描：0 件符合 filing-level 要件（唯一結果缺可辨交易日） | insider selling Form 4 September 2026 Nvidia AI executives SEC filing | 檢查來源：SEC EDGAR、WebSearch | — | 2026-09-13T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 約 0.67 | Cboe equity put call ratio September 2026 reading | https://www.thetrading.tools/put-call-ratio（thetrading.tools） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 407.4 億美元，單週撤出約 7.51 億美元 | leveraged ETF assets under management September 2026 record single stock | https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/（ETF Action） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval September 2026 | 檢查來源：SEC EDGAR、ETF.com 新上市 feed | — | 2026-09-13T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比創紀錄約 62%（2026-08 月資料） | 0DTE options share SPX volume September 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.options_volume | OCC 2026-08 月總結算量約 14.4 億口 | OCC options volume August 2026 monthly report | https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/（Traders Magazine） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 收在約 17 以上、call skew 第 91 百分位 | fear gauge VIX hedges September 10 2026 volatility | https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html（CNBC） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 1.42 兆美元（2026-07 月資料） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php（Current Market Valuation） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Qualcomm 對 Amazon 認股權證約 40 億美元（資料中心基礎設施合作，vendor-financing loops） | Qualcomm warrants Amazon 4 billion AI infrastructure deal September 2026 | https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html（CNBC） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-09-13",
  "iso_week": "2026-W37",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "yes",
  "horizon_end": "2027-03-14",
  "prior_date": "2026-09-03",
  "prior_answer": "yes",
  "flip_evidence": [],
  "r1_drawdown_pct": 4.21,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

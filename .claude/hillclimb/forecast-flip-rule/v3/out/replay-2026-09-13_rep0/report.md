> [DRY RUN] this report was not committed to archive.

# 2026-09-13 AI 泡沫破裂預測報告
報告日期：2026-09-13｜ISO 週次：2026-W37｜預測窗口：2026-09-13 → 2027-03-14｜前次基準：report-2026-09-03（10天前）

## 結論

**結論：no**

三條路徑目前都沒有「已在進行中」的證據：NASDAQ-100 距 52 週高點僅回撤 4.21%（R1 門檻需再跌約 21.70%），本次取得的資料中四大 hyperscaler 沒有任何一家下修 capex 指引（R2），也沒有 AI 算力借款人出現違約或 distressed exchange 的跡象（R3）；HY OAS 2.70% 仍處緊縮水位。9/16 FOMC 升息預期、10Y 殖利率上行與 WTI 走高構成值得追蹤的利率衝擊催化劑，但尚不足以推翻 182 天窗口內三項條件皆不成立的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

FRED `NASDAQ100` 最新收盤 29,368.44（2026-09-11），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 4.21%；R1 門檻水位為 22,995.45，自最新收盤須再下跌約 21.70% 才會觸發（`valuation.ndx_drawdown`）。同期 S&P 500 收 7,656.98（2026-09-11），高於 200 日均線 6.9%、高於 52 週均線 8.33%，較前次基準日（2026-09-03）下跌 1.17%（`valuation.sp500_trend`）。估值脆弱度高：Shiller CAPE 約 40.73（2026-09-01，`valuation.sp500_pe_cape`），S&P 500 前十大成分股佔比約 38%（2026-09-01，`breadth.top10_concentration`）。但情緒並未過熱：CNN Fear & Greed 約 35，屬恐懼區（2026-09-10，`retail.fear_greed`），AAII 看多約 38.0%（2026-09-10，`retail.aaii`）。波動端轉趨緊張：VIXCLS 17.84（2026-09-10），7 日窗口（2026-09-03 → 2026-09-10）VIX +24.58%、S&P 500 −2.01%，屬正常反向，co-movement 警戒未觸發（`structural.vix_spx_comove`）。

**判讀：** R1 距門檻仍遠（回撤 4.21% vs 25%）。要在窗口內觸發，需要一次類似利率衝擊或 AI 盈利預期崩落的急跌；9/16 FOMC 若如市場定價升息（`monetary.fedwatch` 約 85.5%），加上 10Y 殖利率 4.95% 與 CAPE 約 40.73 的高估值組合，是最可能的推力，但目前價格行為只是溫和整理，尚無強制去槓桿跡象。

### R2 資本支出收縮

本次取得的 hyperscaler capex 證據為產業合計值：Microsoft、Alphabet、Amazon、Meta 四家 2026 年 capex 指引合計約 $725bn（CNBC，2026-07-28，2026 Q2 財報季；`ai.hyperscaler_capex`），依 stock-of-state 規則沿用為當前值。各公司個別最新指引金額與相對前一次正式指引的方向（上修／持平／下修）本次檢索未逐家取得，不予補填；本次取得的證據中，四家之中已下修者為 0 家（無任何下修披露）。下一輪財報（2026 Q3）與再下一輪（2026 Q4，通常含次年度 capex 指引）預期都落在窗口（至 2027-03-14）內，但確切日期本次未取得。需求端：Anthropic 年化 run-rate 約 $65bn（2026-08-17，`ai.openai_anthropic_revenue`）；年化 AI 終端營收約 $105bn vs 年化 capex 約 $725bn（分母：僅 top-4 hyperscaler，Oracle 無本次可用數字故未納入；`ai.revenue_capex_gap`），本次無前值可比，缺口方向不判定。H100 中位租金約 $3.38/hr（2026-08-31，`ai.compute_supply_demand`），未見配合利用率走弱的證據，不能單獨解讀為產能過剩。

**判讀：** R2 需要四家中兩家下修，目前為 0 家。窗口內有兩次財報機會，若利率衝擊或股價壓力迫使管理層收斂 2027 年 capex 計畫，Q4 財報（2027 年 1–2 月）是最可能的觸發點；但 AI 營收對 capex 缺口（revenue-to-capex gap）雖大（約 $105bn vs 約 $725bn），本次沒有任何公司釋出收斂訊號。

### R3 AI 信用事件

本次 AI 信用定價分歧（equity-vs-credit schism）掃描在 14 日窗口內無合格披露，因此對潛在達到 R3 規模門檻（負債 ≥ 50 億美元、以 AI 資料中心／算力為主業）的借款人（如 CoreWeave 等 neocloud），其當前債券殖利率、利差、CDS 與評等動作本次均未建立；各借款人總負債與近期到期牆亦未由本次來源取得，不予陳述。30 日 AI infrastructure debt financing / vendor-financing loops 掃描僅見一筆：Qualcomm 對 Amazon 發行約 $4bn 認股權證的資料中心基礎設施合作（CNBC，2026-09-08，`structural.ai_infrastructure_debt`），屬供應商與客戶間的 vendor-financing loops 型安排，不是借款人困境訊號。整體信用環境仍寬鬆：HY OAS 2.70%（2026-09-10，較前次 +5bp，`monetary.hy_oas`）、IG OAS 0.80%（`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 −3bp、SOFR99−IORB +5bp、SRF 動用 0（2026-09-10／2026-09-11，`monetary.repo_stress_srf`）。

**判讀：** 沒有任何破產、寬限期後違約或 distressed exchange 的跡象，信用利差也沒有走闊到足以威脅再融資。R3 在窗口內成立需要信用市場先重定價（HY OAS 明顯走闊、neocloud 債券跌價）再演變為違約，目前連第一步都未出現；若 R1 急跌導致資本市場關門，R3 的路徑才會被打開。

## 支持 yes 的證據

- [整體] 利率衝擊催化劑：CME FedWatch 顯示 9/16 FOMC 升息 25bp 的市場定價約 85.5%（2026-09-12，`monetary.fedwatch`），同時 CPI YoY 3.35%（2026-08 資料，`monetary.cpi_yoy`）、WTI 97.26 美元（2026-09-09，較前次 +5.09%，`monetary.wti`），通膨使 Fed 難以在 AI 股回落時緩衝。
- [R1] 長端利率上行壓縮高估值：DGS10 4.95%（2026-09-10，較前次 +18bp，`monetary.dgs10`），DFII10 2.55%（+13bp，`monetary.dfii10`），對 Shiller CAPE 約 40.73（`valuation.sp500_pe_cape`）與前十大集中度約 38%（`breadth.top10_concentration`）的市場構成估值重定價風險。
- [R1] 波動率同步升溫：VIXCLS 17.84（2026-09-10，7 日 +24.58%，`structural.vix_spx_comove`）、MOVE 82.21（2026-09-11，較前次 +7.53，`structural.treasury_basis_trade`），CNBC 報導 call skew 位於第 91 百分位（2026-09-10，`structural.cross_asset_derivatives`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）龐大：年化 AI 終端營收約 $105bn vs top-4 年化 capex 約 $725bn（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`），若回報遲遲未現，Q4 財報下修 2027 指引的壓力會累積。
- [整體] 投機結構仍偏重：SPX 0DTE 佔比 8 月創紀錄約 62%（2026-08-31，`structural.zero_dte`），本週 IPO 定價約 22 檔（2026-09-11，`speculation.ipo_heat`），margin debt 約 $1.42T（2026-07 資料，`retail.margin_debt`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.21%（2026-09-11），距 R1 門檻水位 22,995.45 仍需再跌約 21.70%（`valuation.ndx_drawdown`）；S&P 500 仍高於 200 日均線 6.9%（`valuation.sp500_trend`）。
- [R3] 信用市場無壓力：HY OAS 2.70%（2026-09-10，`monetary.hy_oas`）、IG OAS 0.80%（`monetary.ig_oas`），repo 資金壓力（SOFR−IORB）−3bp 且 SRF 動用 0（`monetary.repo_stress_srf`），沒有任何 AI 算力借款人困境的跡象（`structural.ai_infrastructure_debt` 30 日掃描僅見一筆 Qualcomm–Amazon 合作）。
- [R2] 本次取得的 capex 證據顯示四大 hyperscaler 2026 指引合計約 $725bn（2026-07-28，`ai.hyperscaler_capex`），四家中 0 家下修；需求端 Anthropic 年化 run-rate 約 $65bn（`ai.openai_anthropic_revenue`），H100 中位租金約 $3.38/hr（`ai.compute_supply_demand`），未見需求崩落。
- [整體] 情緒偏恐懼而非亢奮：CNN Fear & Greed 約 35（2026-09-10，`retail.fear_greed`），AAII 看多約 38.0%（`retail.aaii`），equity put/call 約 0.67（2026-09-01，`speculation.equity_put_call`），不符合頂部常見的極度貪婪型態；Mag 7 前瞻本益比低於 24（2026-08-03，`valuation.mag7_multiples`）。
- [整體] 美債市場未見失序：10Y 標售 bid-to-cover 約 2.71（2026-09-09，`monetary.treasury_auctions`）；槓桿基金美債期貨淨空單 −6,863,118 口（2026-09-08），4 週淨空減少 387,809 口，為溫和收斂而非急速平倉（`structural.treasury_basis_trade`）；10Y 期限溢價（term premium）0.8892%（2026-09-04，`monetary.term_premium`）僅小幅變動。

## 與前期比較

前次結論：無前次預測（report-2026-09-03 為舊格式評分報告）

自 2026-09-03 以來的主要證據變化（舊格式評分不轉換為 yes/no，flip_evidence 為空）：

- 10Y 殖利率 4.77% → 4.95%（+18bp），實質利率 +13bp；10Y breakeven 視窗與前兩者不一致（ΔT10YIE +1bp），本次 Δ 分解判讀：不可判（視窗不一致）（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。
- WTI 92.55 → 97.26 美元（+5.09%，`monetary.wti`）；FedWatch 顯示 9/16 升息定價約 85.5%（`monetary.fedwatch`）。
- S&P 500 −1.17%、VIX 14.32 → 17.84、MOVE 74.68 → 82.21（`valuation.sp500_trend`、`structural.vix_spx_comove`、`structural.treasury_basis_trade`）。
- HY OAS 2.65% → 2.70%（+5bp，`monetary.hy_oas`），仍處緊縮水位；這些變化提高了脆弱度，但沒有任何一條路徑進入進行中狀態，因此本次結論為 no。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源檢索完成但無合格披露（✗ NOT DISCLOSED），均不能作為證據引用：

- `valuation.analyst_tp_decomposition`：無同季 TP 上修披露；不影響結論。
- `valuation.ai_credit_schism`：14 日內無 AI 信用重定價報導——這是 R3 的關鍵盲點，若實際上 neocloud 債券已明顯走闊，R3 判讀可能低估風險，但需先有利差走闊再到違約，182 天內轉為 yes 的門檻仍高。
- `retail.social_sentiment`、`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.private_credit_liquidity`、`ai.token_growth`、`ai.customer_concentration_rpo`、`ai.depreciation_life`、`speculation.upcoming_ai_ipos`、`structural.global_leveraged_approvals`：無窗口內合格披露；私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）的缺漏可能低估 R3 傳導風險，其他項目不影響結論。
- `ai.hyperscaler_financing_mix`：quarterly_state 可用（增額債務約佔 capex 32%，2026-07-28），event_scan 30 日內無大型融資事件，故整體為 ✗ NOT DISCLOSED；不影響結論。
- `ai.capital_cycle`：兩個組件均無可用證據，增速證據不足，本次不判定資本週期階段（capital cycle stage）。

部分成功來源的資料限制：`ai.hyperscaler_capex` 只取得四家合計值，各公司個別指引與方向未取得（R2 計數以「無任何下修披露」為依據）；`breadth.rsp_spy` 只取得 RSP 至 7 月止 YTD 約 13%，SPY 對照值缺，等權對市值加權分歧無法計算；`breadth.advance_decline` 只取得「成分股位於 200 日均線之上約 53%」的廣度 proxy，A/D 與新高／新低比未取得；`valuation.mag7_multiples` 未取得 AI 龍頭 P/S 相對 10 年均值；`speculation.insider_form4` 窗內一筆 EDGAR 結果缺交易日期，不符合 filing-level 條件，按 0 件處理。另外，搜尋結果摘要記載 `structural.treasury_basis_trade` 的 script 三區塊為 fetch_failed，但本次 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 均為 status ok，以 artifact 為準記為 ✓ API。

最大的不確定性：

1. 9/16 FOMC 升息與否：若升息並暗示後續再升，利率衝擊可能推動 R1 急跌，偏向 yes；若暫停，壓力緩解，偏向 no。
2. 2026 Q3／Q4 hyperscaler 財報的 capex 指引：只要兩家下修即觸發 R2，偏向 yes；繼續上修則強化 no。
3. neocloud 信用定價未知：本次未取得 AI 借款人利差／CDS，若信用端已在重定價而未被捕捉，R3 與 R1 的連動風險被低估，偏向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7656.98 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 6.9 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.33 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29368.44 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 4.21 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q2 季資料，%） | 48.2301354474（約 48.23%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（%） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（%） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.7 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.8 | FRED API (series_id=BAMLC0A0CM) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.95 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（較 2026-09-03） | 18.0 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.55 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.36 | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（美元／桶） | 97.26 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-08 月資料，%） | 3.35 | FRED API (series_id=CPIAUCSL) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.32 | FRED API (series_id=T5YIFR) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 0.8892 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API (series_id=SOFR99) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-09-13 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6740619.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5912178.0（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6446620.0（¥644.66T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 17.84 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of 2026-09-10，base 2026-09-03） | 17.84 | FRED API (series_id=VIXCLS, SP500) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日 %） | 24.58 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日 %） | -2.01 | FRED API (series_id=SP500) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2027.9777（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -6863118 | CFTC TFF futures-only | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 387809 | CFTC TFF futures-only | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 82.21 | Yahoo Finance chart API (^MOVE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2271.6 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | gurufocus / multpl，WebSearch primary | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch（CNBC）；P/S 未取得 | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch，90d＋同季 | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500，sp500_trend） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100，ndx_drawdown） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch，14d | ✗ NOT DISCLOSED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch（247wallst）；僅 RSP 側 | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch（247wallst） | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch（condoredge），200 日均線廣度 proxy | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch primary（cnn.com） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch（advisorperspectives），月資料沿用 | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | WebSearch primary（aaii.com） | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch，7d | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch primary | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM survey | WebSearch，月度 | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED DFEDTARU / DFEDTARL | scripts/fetch_macro.py（DFEDTARU ok、DFEDTARL ok） | ✓ API |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直接） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） | ✓ API |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch，14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch（steelorbis） | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch，30d | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（CNBC），stock-of-state 沿用 2026 Q2 | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch（Axios） | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch（thundercompute） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch：quarterly_state 沿用 CNBC 2026-07-28；event_scan 30d 無合格事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch（Axios）＋ hyperscaler capex 分母 | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動（depreciation useful-life change） | WebSearch，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch：quarterly_state 與 event_scan 皆無可用披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch 7d screen | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（IPOScoop） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch movers screen 7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch，30d | ✗ NOT DISCLOSED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR / WebSearch，14d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch（etfaction）；個別 ticker 未取得 | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com feed，30d | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch，7d | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe insights） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（Traders Magazine，OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch（CNBC） | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS ok、vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（currentmarketvaluation） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch，30d | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok；aggregation any） | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.73（原定來源 multpl / gurufocus） | S&P 500 Shiller CAPE ratio current September 2026 multpl | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | Magnificent 7 forward P/E valuation September 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html（CNBC） | 2026-08-03 | 2026-09-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 至 7 月止 YTD 報酬約 13%（SPY 對照值未取得） | RSP equal weight vs SPY S&P 500 YTD performance September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度約 38% | S&P 500 top 10 concentration percentage September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.advance_decline | 成分股位於 200 日均線之上約 53%（廣度 proxy） | market breadth advance decline new highs lows September 2026 percent stocks above 200-day | https://condoredge.com/stocks/market-breadth（Condor Edge） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 35（恐懼） | CNN Fear and Greed Index today September 2026 reading | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）約 $1.42T；YoY 與市值比本次未取得 | FINRA margin debt August 2026 record year over year | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026（Advisor Perspectives，原定 FINRA） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.0% | AAII sentiment survey results week September 10 2026 bullish bearish neutral | https://www.aaii.com/sentimentsurvey（AAII） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.71 | Treasury auction results September 2026 tail bid-to-cover 10-year | https://thevaultreport.com/treasury-auctions（The Vault Report） | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.fedwatch | 9/16 FOMC 升息 25bp 定價約 85.5%（原定 CME FedWatch） | CME FedWatch September 12 2026 probability 25 basis point hike | https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html（Yahoo Finance） | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate financing 2026 total social financing | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm（SteelOrbis） | 2026-08-15 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_capex | MSFT／GOOGL／AMZN／META 2026 capex 合計約 $725bn（2026 Q2 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 $65bn | OpenAI Anthropic annualized revenue run rate September 2026 | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| ai.compute_supply_demand | H100 中位租金約 $3.38/hr | GPU rental price HBM DRAM contract price September 2026 utilization | https://www.thundercompute.com/blog/ai-gpu-rental-market-trends（Thunder Compute） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 增額債務約佔 capex 32% | hyperscaler capex vs free cash flow debt issuance 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $105bn（分母取 ai.hyperscaler_capex top-4 約 $725bn） | AI revenue vs capex gap 2026 annualized run rate | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描：0 件合格事件 | AI company name change ticker SPAC announcement September 7-13 2026 | 檢查來源：SPACInsider、Businesswire SPAC newsroom、Boardroom Alpha | — | 2026-09-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 22 檔（首日報酬與無營收發行人佔比未取得） | IPO priced week September 8 2026 first day return debut | https://www.iposcoop.com/current-year-pricings/（IPOScoop） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描：0 件符合 2+ 主題×弱基本面（最大漲幅 +77%、+35% 皆未達門檻） | biggest stock gainers week September 7 2026 microcap 100% quantum AI | 檢查來源：Finviz、Benzinga、StockTitan、Yahoo movers | — | 2026-09-13T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 14 日掃描：0 件具完整 filing-level 細節（唯一 EDGAR 結果缺交易日期，不合格） | insider selling Form 4 September 2026 Nvidia AI executives SEC filing | 檢查來源：SEC EDGAR Form 4 | — | 2026-09-13T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 約 0.67（日值或 5 日均值未標明） | Cboe equity put call ratio September 2026 reading | https://www.thetrading.tools/put-call-ratio（thetrading.tools） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 $40.74bn | leveraged ETF assets under management September 2026 record single stock | https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/（ETF Action） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval September 2026 | 檢查來源：SEC EDGAR、ETF.com 新上市 feed | — | 2026-09-13T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比 8 月創紀錄約 62% | 0DTE options share SPX volume September 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.options_volume | OCC 8 月總結算量約 1.44 十億口 | OCC options volume August 2026 monthly report | https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/（Traders Magazine） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 收在約 17 以上、call skew 第 91 百分位 | fear gauge VIX hedges September 10 2026 volatility | https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html（CNBC） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率的基數約 $1.42T（比率本身未取得） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php（Current Market Valuation） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Qualcomm 對 Amazon 認股權證約 $4bn（資料中心基礎設施合作） | Qualcomm warrants Amazon 4 billion AI infrastructure deal September 2026 | https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html（CNBC） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |

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

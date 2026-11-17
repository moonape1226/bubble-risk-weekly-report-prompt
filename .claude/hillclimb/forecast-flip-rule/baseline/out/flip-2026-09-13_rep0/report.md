> [DRY RUN] this report was not committed to archive.

# 2026-09-13 AI 泡沫破裂預測報告

報告日期：2026-09-13｜ISO 週次：2026-W37｜預測窗口：2026-09-13 → 2027-03-14｜前次基準：report-2026-09-03（10天前）

## 結論

**結論：yes**

維持前次 yes，主驅動是 R1：FedWatch 顯示 2026-09-16 FOMC 升息 25bp 的市場隱含勝算約 85.5%（2026-09-12），10Y 實質利率升至 2.55%（較 2026-09-03 +13bp），而 S&P 500 Shiller CAPE 約 40.73、CPI YoY 3.35% 限制了 Fed 緩衝 AI 主導回檔的空間。自 report-2026-09-03 以來沒有任何新證據削弱這條緊縮催化路徑，依翻轉紀律不翻轉；但 NASDAQ-100 目前距 R1 門檻仍需再跌約 21.70%，R2／R3 亦無進行中的跡象，這個 yes 高度依賴 R1 在窗口內由升息循環觸發。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,368.44（2026-09-11），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 4.21%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45；自最新收盤需再下跌約 21.70% 才會觸及。前次 report-2026-09-03 的回撤為 4.95%，指數自那之後略為收復。

催化面：FedWatch 隱含 2026-09-16 FOMC 升息 25bp 勝算約 85.5%（`monetary.fedwatch`，2026-09-12），現行目標區間 3.50%–3.75%（`monetary.fed_funds`）。10Y 殖利率 4.95%（+18bp）、10Y 實質利率 2.55%（+13bp）、10Y breakeven 2.36%（+1bp），本次 Δ 分解判讀為不可判（視窗不一致）——T10YIE 的最新觀測日（2026-09-11）與 DGS10／DFII10（2026-09-10）不同（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。CPI YoY 3.35%（2026-08 月資料，`monetary.cpi_yoy`）、WTI 97.26 美元（+5.09%，`monetary.wti`）、5y5y 2.32%（`monetary.t5yifr`）。10Y 期限溢價（term premium，Kim-Wright）0.8892%（2026-09-04，trailing 7 日 +1.4bp，`monetary.term_premium`）。

脆弱度：Shiller CAPE 約 40.73（`valuation.sp500_pe_cape`）、S&P 500 前十大集中度約 38%（`breadth.top10_concentration`）、S&P 500 較 200 日均線偏離 +6.9%、較 52 週均線 +8.33%（`valuation.sp500_trend`）、家計股票配置 48.23%（2026-Q2 資料，`retail.household_equity_allocation`）。波動：VIX 17.84（2026-09-10），trailing 7 日 VIX +24.58% 而 S&P 500 −2.01%，未出現同漲（comove false，`structural.vix_spx_comove`）；MOVE 82.21（+7.53，`structural.treasury_basis_trade`）；VIX 收在 17 以上且 call skew 位於第 91 百分位（`structural.cross_asset_derivatives`）。

**判讀：** R1 距門檻仍遠（回撤 4.21%，需再跌約 21.70%），本身不是進行中狀態；把它推過門檻需要的是升息循環確立（9/16 FOMC 升息且後續路徑續升）、實質利率續升壓縮長存續期 AI 權重股評價，並與 10 月底／1 月底財報季的 capex 或營收失望疊加。

### R2 資本支出收縮

最新可得證據為 2026-07-28 的季報彙整：Microsoft、Alphabet、Amazon、Meta 2026 年 capex 合計約 7,250 億美元（`ai.hyperscaler_capex`）。本次證據只有合計值，未逐家揭露各公司指引數值與相對前次指引的方向（上修／持平／下修），因此逐家方向本次不可判；但證據中沒有任何一家下修的披露，已下修家數為 0。下一輪財報（依季報節奏為 10 月底與 1 月底）兩次都落在窗口內，具體日期本次證據未提供。需求側對照：Anthropic 年化 run-rate 約 650 億美元（2026-08-17，`ai.openai_anthropic_revenue`）；H100 中位租金約 3.38 美元／小時（2026-08-31，`ai.compute_supply_demand`），未見價格崩落伴隨利用率下滑的證據。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 1,050 億美元 vs 年化 capex 約 7,250 億美元（分母：top-4 MSFT／GOOGL／AMZN／META，不含 Oracle 與 neocloud）；本次無前值，缺口擴大或收斂無法判定（`ai.revenue_capex_gap`）。

**判讀：** R2 目前離成立最遠——0 家下修、合計指引仍在高檔。窗口內兩輪財報是唯一觸發點，需要至少兩家在 R1 式市場壓力或融資成本上升下主動下修，目前沒有證據顯示這個軌跡已經開始。

### R3 AI 信用事件

本次沒有取得任何符合 R3 規模門檻（負債 ≥ 50 億美元、AI 資料中心／算力為主業）借款人的債券殖利率、利差、CDS 或評等行動；AI 信用定價分歧掃描在 14 日窗內沒有合格披露。可得的相關證據：Qualcomm 對 Amazon 發行約 40 億美元認股權證的資料中心基礎設施交易（2026-09-08，`structural.ai_infrastructure_debt`），屬 vendor-financing loops 型安排而非借款人困境。整體信用背景偏緊：HY OAS 2.70%（+5bp，`monetary.hy_oas`）、IG OAS 0.80%（−1bp，`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 −3bp，SOFR99−IORB +5bp，SRF 動用 0.0（`monetary.repo_stress_srf`）。

**判讀：** 沒有任何違約、寬限期、covenant waiver 或 distressed exchange 的訊號，信用利差處於低檔。R3 要在窗口內成立，需要先出現 R1 式的股權重定價或融資市場關門，讓大型 AI 基礎設施借款人的再融資失敗；目前它最可能作為 R1 的後續傳導，而非獨立先行。

## 支持 yes 的證據

- [R1] FedWatch 隱含 2026-09-16 FOMC 升息 25bp 勝算約 85.5%（2026-09-12），自 3.50%–3.75% 目標區間轉入升息循環，是窗口內對高估值 AI 權重股最直接的折現率催化（`monetary.fedwatch`、`monetary.fed_funds`）。
- [R1] 10Y 殖利率 4.95%（2026-09-10，較 2026-09-03 +18bp）、10Y 實質利率 2.55%（+13bp），實質利率上升直接壓縮長存續期成長股評價（`monetary.dgs10`、`monetary.dfii10`）。
- [R1] 通膨限制 Fed 緩衝：CPI YoY 3.35%（2026-08 月資料）、WTI 97.26 美元（2026-09-09，+5.09%），使 Fed 難以在 AI 主導回檔時迅速轉向寬鬆（`monetary.cpi_yoy`、`monetary.wti`）。
- [R1] 估值與集中度提供大幅下行空間：Shiller CAPE 約 40.73（2026-09-01）、前十大集中度約 38%（2026-09-01）、家計股票配置 48.23%（2026-Q2）（`valuation.sp500_pe_cape`、`breadth.top10_concentration`、`retail.household_equity_allocation`）。
- [R1] 波動開始抬頭：VIX 17.84（2026-09-10，trailing 7 日 +24.58%）、MOVE 82.21（2026-09-11，+7.53）、call skew 第 91 百分位（2026-09-10）（`structural.vix_spx_comove`、`structural.treasury_basis_trade`、`structural.cross_asset_derivatives`）。
- [整體] 投機槓桿結構放大下跌傳導：SPX 0DTE 佔比 8 月創紀錄約 62%、margin debt 約 1.42 兆美元（2026-07 月資料）、單一個股槓桿 ETF 規模約 407.4 億美元（2026-09-08）（`structural.zero_dte`、`retail.margin_debt`、`structural.leveraged_etf_aum`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 1,050 億美元 vs top-4 年化 capex 約 7,250 億美元，回本壓力在財報季可能轉為 capex 紀律要求（`ai.revenue_capex_gap`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.21%（2026-09-11），需再跌約 21.70% 才觸及 22,995.45 的 R1 門檻，且較前次 4.95% 收復（`valuation.ndx_drawdown`）。
- [整體] 基準率：任意 182 日窗口內 R1–R3 皆不成立才是常態；三條路徑目前都沒有進行中的觸發，yes 需仰賴尚未發生的升息循環傳導（`valuation.ndx_drawdown`、`ai.hyperscaler_capex`、`monetary.hy_oas`）。
- [R2] 四大 hyperscaler 2026 capex 合計約 7,250 億美元（2026-07-28），證據中 0 家下修（`ai.hyperscaler_capex`）。
- [R3] 信用利差低檔：HY OAS 2.70%、IG OAS 0.80%（2026-09-10），無 AI 基礎設施借款人違約或 distressed exchange 跡象（`monetary.hy_oas`、`monetary.ig_oas`）。
- [整體] 資金市場平穩：SOFR−IORB −3bp、SOFR99−IORB +5bp（2026-09-10）、SRF 動用 0.0（2026-09-11）、銀行對 NBFI 放款約 2.03 兆美元（2026-09-02，無新觀測，週變動 0）（`monetary.repo_stress_srf`、`structural.nbfi_bank_loans`）。
- [整體] 情緒並不亢奮：CNN Fear & Greed 約 35（恐懼，2026-09-10）、AAII 看多約 38.0%（2026-09-10）、equity put/call 約 0.67（2026-09-01）（`retail.fear_greed`、`retail.aaii`、`speculation.equity_put_call`）。
- [R1] 龍頭估值並非極端：Mag 7 前瞻本益比低於 24（2026-08-03）（`valuation.mag7_multiples`）。
- [R2] 需求側尚未轉弱：Anthropic 年化 run-rate 約 650 億美元（2026-08-17）、H100 中位租金約 3.38 美元／小時（2026-08-31）（`ai.openai_anthropic_revenue`、`ai.compute_supply_demand`）。

## 與前期比較

前次結論：yes（report-2026-09-03）
本次結論：維持

- NASDAQ-100 回撤由 4.95% 收窄至 4.21%（2026-09-11，`valuation.ndx_drawdown`）：方向偏離 R1，但 0.74 個百分點屬日常波動範圍，不足以改變路徑判讀。
- FedWatch 升息勝算約 85.5%（2026-09-12，`monetary.fedwatch`）與 10Y 實質利率 +13bp（`monetary.dfii10`）：是前次之後的新資料，方向強化而非削弱 R1 的緊縮催化。
- VIX trailing 7 日 +24.58%、MOVE +7.53（`structural.vix_spx_comove`、`structural.treasury_basis_trade`）：波動抬頭，同樣不支持翻轉為 no。
- HY OAS +5bp、IG OAS −1bp（`monetary.hy_oas`、`monetary.ig_oas`）：信用面無變化，R3 判讀不變。
- capex 合計約 7,250 億美元的資料日期為 2026-07-28，早於前次基準，前次已可取得，不構成新證據；沒有任何前次之後的來源改變 R2 或 R3 的路徑分析，因此 flip_evidence 為空。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED（檢索完成但無窗內合格披露）：`valuation.analyst_tp_decomposition`、`valuation.ai_credit_schism`、`retail.social_sentiment`、`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.private_credit_liquidity`、`ai.token_growth`、`ai.customer_concentration_rpo`、`ai.hyperscaler_financing_mix`（quarterly_state 可得、event_scan 無披露）、`ai.depreciation_life`、`ai.capital_cycle`、`speculation.upcoming_ai_ipos`、`structural.global_leveraged_approvals`。其中 `valuation.ai_credit_schism` 與 `monetary.private_credit_liquidity` 的缺口最可能改變答案：若出現 AI 基礎設施債利差走闊或 gate proration / breach，會直接提高 R3 與 R1 傳導的可能；目前缺披露只代表未見訊號，不代表確認無壓力。

其他資料註記：`speculation.insider_form4` 的 14 日掃描有一筆 NVIDIA（CIK 1045810）Form 4 命中（2026-09-02），但檢索結果未揭露交易日期，不符合格要件，故依規則列為 0 件且不引用其姓名與金額。`structural.treasury_basis_trade` 的搜尋紀錄寫為「script 三區塊 fetch_failed」，但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 三塊皆為 `status: ok`；本報告以 artifact 為準記 ✓ API。槓桿基金美債期貨淨空單 −6,863,118 口（2026-09-08），4 週淨空減少 387,809 口，屬美債基差交易槓桿（Treasury basis-trade leverage）小幅去化而非失序。R2 證據只有四家合計值，逐家指引方向不可判。

最大不確定性：

1. 2026-09-16 FOMC 是否真的升息、及後續點陣圖是否指向續升——若升息並維持鷹派，推向 yes；若按兵不動或釋出暫停訊號，R1 催化將大幅減弱，推向 no。
2. 10 月底財報季 hyperscaler capex 指引——任兩家下修即直接觸發 R2（yes）；若持續上修，則支撐 AI 權重股並壓低 R1 可能（no）。
3. 大型 AI 基礎設施借款人的再融資條件——本次無信用定價資料；若利差在升息環境中快速走闊，R3 與 R1 會相互強化（yes），若融資市場維持開放則推向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7656.98 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 6.9 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.33 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29368.44 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點 %） | 4.21 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026-Q2 資料） | 48.2301354474（約 48.23%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5 | FRED API (series_id=DFEDTARL) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.7 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.8 | FRED API (series_id=BAMLC0A0CM) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.95 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | 18.0 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.55 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | 13.0 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.36 | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 97.26 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO chg_pct | 5.09 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-08 月資料） | 3.35 | FRED API (series_id=CPIAUCSL) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.32 | FRED API (series_id=T5YIFR) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8892 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.62 | FRED API (series_id=SOFR) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.7 | FRED API (series_id=SOFR99) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-09-13 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,740,619（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,912,178（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,446,620（¥644.66T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 17.84 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 17.84 | fetch_macro.py 派生區塊（FRED API） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（trailing 7 日） | 24.58 | fetch_macro.py 派生區塊（FRED API） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（trailing 7 日） | -2.01 | fetch_macro.py 派生區塊（FRED API） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2027.9777（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約合計，口） | -6863118 | CFTC TFF futures-only | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 387809 | CFTC TFF futures-only | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 82.21 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index delta_abs | 7.53 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2271.6 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl／GuruFocus，WebSearch primary | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch（CNBC 等） | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch，90 日且同季 | ✗ NOT DISCLOSED（窗內無合格同季 TP 上調） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch，14 日 | ✗ NOT DISCLOSED（14 日窗內無合格披露） |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight vs cap-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail / CNN Fear & Greed Index | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail / Margin Debt: FINRA | WebSearch（FINRA 月資料，stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail / Retail survey: AAII | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail / Social sentiment proxies | WebSearch，7 日 | ✗ NOT DISCLOSED（無顯著討論） |
| retail.household_equity_allocation | Retail / Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail / NAAIM Exposure Index | WebSearch primary | ✗ NOT DISCLOSED（無當週值） |
| institutional.bofa_jpm_survey | Institutional / BofA Fund Manager Survey and JPM | WebSearch | ✗ NOT DISCLOSED（無新調查） |
| monetary.fed_funds | Monetary / Fed funds rate: FRED | fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary / High Yield OAS | fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary / Investment Grade OAS | fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary / 10Y Treasury yield | fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary / 10Y Treasury real yield | fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary / 10Y breakeven inflation rate | fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary / WTI crude oil price | fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary / CPI YoY: FRED | fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary / 5y5y forward inflation expectation | fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary / 10Y 期限溢價（term premium）: FRED | fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary / 美債標售需求 | WebSearch primary，14 日 | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary / Fed funds rate path expectations | WebSearch primary（CME FedWatch 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary / Fed balance sheet: FRED | fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary / Global central bank liquidity cross-check | fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok，無新觀測） |
| monetary.pboc | Monetary / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary / Private-credit / non-bank fund liquidity stress | WebSearch primary，30 日 | ✗ NOT DISCLOSED（30 日窗內無合格披露） |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | WebSearch（季報彙整，stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration | WebSearch primary | ✗ NOT DISCLOSED（無合格披露） |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | WebSearch primary | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構 | WebSearch primary；quarterly_state 沿用最新季、event_scan 30 日 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口 | WebSearch primary（分子 Axios 彙整；分母 top-4 capex） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動 | WebSearch primary，30 日 | ✗ NOT DISCLOSED（30 日窗內無變動披露） |
| ai.capital_cycle | AI / 資本週期階段 | WebSearch primary；quarterly_state 與 event_scan 30 日 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculation / Search for past 7 days | WebSearch，7 日 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculation / IPO market heat | WebSearch，7 日 | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculation / Microcap thematic moonshots | WebSearch primary，7 日 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculation / Upcoming AI IPOs | WebSearch，30 日 | ✗ NOT DISCLOSED（無 30 日內 S-1 或具名來源） |
| speculation.insider_form4 | Speculation / Insider selling at AI / market-leadership companies | SEC EDGAR＋WebSearch，14 日 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculation / Cboe equity-only put/call ratio | WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural / US leveraged ETF AUM | WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed，30 日 | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural / Global leveraged product approvals | WebSearch，7 日 | ✗ NOT DISCLOSED（7 日窗內無英文披露） |
| structural.zero_dte | Structural / 0DTE option volume | WebSearch（Cboe insights） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural / VIX / S&P 500 co-movement | fetch_macro.py（VIXCLS＋vix_spx_comove 區塊） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural / Cross-reference only: FINRA margin debt | WebSearch（confirmation only） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural / AI infrastructure debt financing / vendor-financing loops | WebSearch primary，30 日 | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural / Bank loans to nondepository financial institutions | fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）；WebSearch 補充 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.73（原定來源 multpl／GuruFocus） | S&P 500 Shiller CAPE ratio current September 2026 multpl | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio （GuruFocus） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | Magnificent 7 forward P/E valuation September 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html （CNBC） | 2026-08-03 | 2026-09-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 至 7 月止 YTD 報酬約 13% | RSP equal weight vs SPY S&P 500 YTD performance September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/ （24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度約 38% | S&P 500 top 10 concentration percentage September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/ （24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 200 日均線之上約 53% | market breadth advance decline new highs lows September 2026 percent stocks above 200-day | https://condoredge.com/stocks/market-breadth （Condor Edge） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 35（恐懼） | CNN Fear and Greed Index today September 2026 reading | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）約 1.42 兆美元 | FINRA margin debt August 2026 record year over year | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026 （Advisor Perspectives，原定來源 FINRA） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.0% | AAII sentiment survey results week September 10 2026 bullish bearish neutral | https://www.aaii.com/sentimentsurvey （AAII） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.71 | Treasury auction results September 2026 tail bid-to-cover 10-year | https://thevaultreport.com/treasury-auctions （The Vault Report） | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.fedwatch | 2026-09-16 FOMC 升息 25bp 勝算約 85.5% | CME FedWatch September 12 2026 probability 25 basis point hike | https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html （Yahoo Finance，原定來源 CME FedWatch） | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.pboc | 2026 年 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate financing 2026 total social financing | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm （SteelOrbis） | 2026-08-15 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_capex | MSFT／GOOGL／AMZN／META 2026 capex 合計約 7,250 億美元（2026 Q2 季報） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 650 億美元 | OpenAI Anthropic annualized revenue run rate September 2026 | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| ai.compute_supply_demand | H100 中位租金約 3.38 美元／小時 | GPU rental price HBM DRAM contract price September 2026 utilization | https://www.thundercompute.com/blog/ai-gpu-rental-market-trends （Thunder Compute） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 增額債務佔 capex 約 32% | hyperscaler capex vs free cash flow debt issuance 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 1,050 億美元（分母另取 top-4 capex 約 7,250 億美元） | AI revenue vs capex gap 2026 annualized run rate | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描：0 件合格事件 | AI company name change ticker SPAC announcement September 7-13 2026 | 檢查來源：SPACInsider、Businesswire SPAC newsroom、Boardroom Alpha | — | 2026-09-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 22 檔 | IPO priced week September 8 2026 first day return debut | https://www.iposcoop.com/current-year-pricings/ （IPOScoop） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描：0 件符合 2+ 主題×弱基本面（Tenon +77%、AEON +35% 皆未達門檻） | biggest stock gainers week September 7 2026 microcap 100% quantum AI | 檢查來源：Finviz、Benzinga、StockTitan、Yahoo movers | — | 2026-09-13T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 14 日掃描：0 件合格（唯一命中未揭露交易日期，排除） | insider selling Form 4 September 2026 Nvidia AI executives SEC filing | 檢查來源：SEC EDGAR、WebSearch | — | 2026-09-13T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 約 0.67（日讀數） | Cboe equity put call ratio September 2026 reading | https://www.thetrading.tools/put-call-ratio （thetrading.tools，原定來源 Cboe） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 407.4 億美元 | leveraged ETF assets under management September 2026 record single stock | https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/ （ETF Action） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval September 2026 | 檢查來源：SEC EDGAR、ETF.com 新上市 feed | — | 2026-09-13T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比 8 月創紀錄約 62% | 0DTE options share SPX volume September 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august （Cboe） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.options_volume | OCC 8 月總結算量約 14.4 億口（2026-08 月資料） | OCC options volume August 2026 monthly report | https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/ （Traders Magazine，原定來源 OCC） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 收在約 17 以上、call skew 第 91 百分位 | fear gauge VIX hedges September 10 2026 volatility | https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html （CNBC） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 1.42 兆美元（2026-07 月資料） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php （Current Market Valuation） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Qualcomm 對 Amazon 認股權證約 40 億美元（vendor-financing loops） | Qualcomm warrants Amazon 4 billion AI infrastructure deal September 2026 | https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html （CNBC） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |

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

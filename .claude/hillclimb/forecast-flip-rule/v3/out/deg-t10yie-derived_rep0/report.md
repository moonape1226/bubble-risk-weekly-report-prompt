> [DRY RUN] this report was not committed to archive.

# 2026-09-13 AI 泡沫破裂預測報告
報告日期：2026-09-13｜ISO 週次：2026-W37｜預測窗口：2026-09-13 → 2027-03-14｜前次基準：report-2026-09-03（10天前）

## 結論

**結論：no**

三條路徑都還離觸發很遠。NASDAQ-100 距 52 週高點回撤 4.21%，還要再跌約 21.70% 才到 R1 門檻；HY OAS 只有 2.70%，repo 資金壓力（SOFR−IORB）為 −3bps，信用與資金市場都沒有 R3 式壓力。升息預期與實質利率上行是真實的時點催化劑，但目前還不足以推翻「182 天內三項條件皆不成立」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,368.44（2026-09-11），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 4.21%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，需從最新收盤再下跌約 6,372.99 點（約 21.70%）才會觸發。前次基準日（2026-09-03）收盤為 29,482.32，這 10 天指數小幅走低。

脆弱度面：S&P 500 為 7,656.98（2026-09-11），高於 200 日均線 6.9%、高於 52 週均線 8.33%（`valuation.sp500_trend`）；Shiller CAPE 約 40.73（2026-09-01，`valuation.sp500_pe_cape`）；S&P 500 前十大集中度約 38%（2026-09-01，`breadth.top10_concentration`）。時點催化劑：10Y 殖利率 4.95%（2026-09-10），較前次 +18bps，主要來自實質利率（DFII10 +13bps；T10YIE 為 derived，+5bps），判讀為 real-rate 驅動（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。CME FedWatch 顯示 9/16 FOMC 升息 25bp 的機率約 85.5%（2026-09-12，`monetary.fedwatch`）。VIX 在 7 日窗（2026-09-03 → 2026-09-10）上升 24.58% 至 17.84，同期 S&P 500 下跌 2.01%，兩者未同向上漲（comove=false，`structural.vix_spx_comove`），屬正常的避險反應，不是 crowded-optionality 讀數。

**判讀：** R1 距門檻還很遠（4.21% vs 25%）。窗口內要觸發，需要一次持續性的大幅下跌，例如升息週期重啟加上實質利率續升，導致長存續期 AI 權益資產重新定價，或由 R3 信用事件傳導；目前證據顯示壓力在累積，但沒有出現加速下跌的跡象。

### R2 資本支出收縮

本次 `ai.hyperscaler_capex` 只取得 CNBC 2026-07-28 報導中四大 hyperscaler 2026 capex 合計約 725（摘錄未逐字標示單位，依報導脈絡為十億美元級），沒有逐家數據：

- Microsoft：最新官方指引數值與方向本次未逐家取得（沿用 2026-07 財報季合計值）。
- Alphabet：同上；該報導標題指出 Alphabet 財報後市場對 capex 的審視升高，但沒有顯示指引下修。
- Amazon：同上，本次未逐家取得。
- Meta：同上，本次未逐家取得。

依本次證據，四家中已確認下修的家數為 0。下一次財報日期本次沒有取得可引證的日期，但下一輪季報應落在窗口內（2026-09-13 → 2027-03-14），可能有一到兩輪指引更新。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 105 vs 年化 capex 約 725（分母：top-4，Oracle 本次無可用 capex 數據故未納入），缺口很大（`ai.revenue_capex_gap`）；這是本次首次組合，沒有前值，因此無法判斷缺口在擴大還是收斂。

**判讀：** R2 目前沒有任何一家確認下修。要在窗口內觸發，需要至少兩家在未來的季報或法說會正式下修；在需求面證據（Anthropic run-rate 約 65，2026-08-17，`ai.openai_anthropic_revenue`）仍在成長的情況下，主動下修的誘因有限，除非 R1 式股價下跌或融資條件惡化迫使公司收縮。

### R3 AI 信用事件

本次沒有任何來源確立哪一家 AI 資料中心／算力借款人的負債規模達到 R3 的 50 億美元門檻，因此不列舉、也不估計個別借款人的負債。過去 14 日的 AI 信用定價掃描（債券利差、CDS、評等動作）沒有找到窗內披露，也沒有任何違約、寬限期、distressed exchange 或 going-concern 字樣的報導。過去 30 日唯一的 AI infrastructure debt financing / vendor-financing loops 事件是 Qualcomm 向 Amazon 發行約 40 億美元認股權證的資料中心基礎設施交易（2026-09-08，`structural.ai_infrastructure_debt`）。這屬於供應商以權益換取採購承諾的循環安排，不是債務困境訊號。整體信用環境：HY OAS 2.70%（+5bps）、IG OAS 0.80%（−1bp）（`monetary.hy_oas`、`monetary.ig_oas`），都處於偏緊水位。

**判讀：** R3 沒有任何已知借款人處於困境邊緣。窗口內要觸發，需要高槓桿 neocloud 或資料中心借款人出現再融資失敗、利差急遽走闊或付款違約；本次資料缺口較大（信用定價與私募信貸都無窗內披露），但已取得的利差數據不支持近期違約。

## 支持 yes 的證據

- [整體] CME FedWatch 顯示 2026-09-16 FOMC 升息 25bp 的機率約 85.5%（2026-09-12），同時 CPI YoY 3.35%（2026-08 資料）、WTI 97.26（2026-09-09，較前次 +5.09%），Fed 沒有空間為 AI 主導的下跌提供緩衝，是窗口內最明確的緊縮催化劑（`monetary.fedwatch`、`monetary.cpi_yoy`、`monetary.wti`）。
- [R1] 10Y 殖利率 4.95%（2026-09-10）較前次 +18bps，其中 DFII10 +13bps、T10YIE +5bps（derived），為實質利率驅動的折現率上升，直接壓迫長存續期 AI 權益估值（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。
- [R1] 估值與集中度處於高位：Shiller CAPE 約 40.73（2026-09-01）、前十大集中度約 38%（2026-09-01）、S&P 500 高於 200 日均線 6.9%（2026-09-11），一旦下跌開始，跌幅可能很大（`valuation.sp500_pe_cape`、`breadth.top10_concentration`、`valuation.sp500_trend`）。
- [R1] 波動度同步升溫：VIX 17.84（2026-09-10），7 日上升 24.58%；MOVE 82.21（2026-09-11），前次為 74.68；CNBC 報導 call skew 位於第 91 百分位（2026-09-10）（`structural.vix_spx_comove`、`structural.treasury_basis_trade`、`structural.cross_asset_derivatives`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）很大：年化 AI 終端營收約 105 vs top-4 年化 capex 約 725；CNBC 2026-07-28 報導 Alphabet 財報後 hyperscaler capex 受到更嚴格審視（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`）。
- [R3] AI infrastructure debt financing / vendor-financing loops 持續擴張：Qualcomm 向 Amazon 發行約 40 億美元認股權證（2026-09-08），供應商以權益換採購的循環結構增加了系統的相互依存（`structural.ai_infrastructure_debt`）。
- [整體] 投機槓桿結構仍高：SPX 0DTE 佔比在 8 月創紀錄約 62%（2026-08-31）；單一個股槓桿 ETF 規模約 40.74（2026-09-08）（`structural.zero_dte`、`structural.leveraged_etf_aum`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.21%（2026-09-11），門檻水位 22,995.45，需再下跌約 21.70%；182 天內從近高點跌到 25% 回撤是罕見事件（`valuation.ndx_drawdown`）。
- [R3] 信用市場沒有壓力：HY OAS 2.70%、IG OAS 0.80%（2026-09-10），前次以來僅 +5bps／−1bp，與違約或 distressed exchange 臨近的狀態不符（`monetary.hy_oas`、`monetary.ig_oas`）。
- [整體] 資金與槓桿管道平穩：SOFR−IORB −3bps、SOFR99−IORB +5bps（2026-09-10）、SRF 動用（Standing Repo Facility usage）0.0（2026-09-11）；銀行對 NBFI 放款 2,027.98bn（≈$2.03T，2026-09-02，持平）；槓桿基金美債期貨淨空單 −6,863,118 口（2026-09-08），4 週內縮減 387,809 口，沒有被迫去槓桿的跡象（`monetary.repo_stress_srf`、`structural.nbfi_bank_loans`、`structural.treasury_basis_trade`）。
- [R2] 依本次證據四大 hyperscaler 沒有一家下修 capex 指引，2026 合計約 725（2026-07-28）；需求端 Anthropic 年化 run-rate 約 65（2026-08-17），H100 中位租金約 3.38（2026-08-31），沒有出現供給過剩的證據（`ai.hyperscaler_capex`、`ai.openai_anthropic_revenue`、`ai.compute_supply_demand`）。
- [整體] 情緒並不狂熱：CNN Fear & Greed 約 35（恐懼，2026-09-10）、AAII 看多約 38.0%（2026-09-10）、equity put/call 約 0.67（2026-09-01）、約 53% 成分股在 200 日均線之上（2026-09-11）；CNBC 報導 Mag 7 前瞻本益比低於 24（2026-08-03）。這些都不是頂部式的追高狀態（`retail.fear_greed`、`retail.aaii`、`speculation.equity_put_call`、`breadth.advance_decline`、`valuation.mag7_multiples`）。

## 與前期比較

前次結論：無前次預測（report-2026-09-03 為舊格式評分報告）

本次結論：no。前次為舊格式評分報告，不轉譯為 yes/no，flip_evidence 為空。自 2026-09-03 以來的主要變化：

- 10Y 殖利率 4.77% → 4.95%（+18bps），由實質利率驅動（`monetary.dgs10`）。
- VIX 14.32 → 17.84，MOVE 74.68 → 82.21，波動度同步升溫（`structural.vix_spx_comove`、`structural.treasury_basis_trade`）。
- S&P 500 7,747.71 → 7,656.98（−1.17%）；NASDAQ-100 29,482.32 → 29,368.44（`valuation.sp500_trend`、`valuation.ndx_drawdown`）。
- HY OAS 2.65% → 2.70%，仍處偏緊水位（`monetary.hy_oas`）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

已完成檢索但沒有窗內合格披露（✗ NOT DISCLOSED）：valuation.analyst_tp_decomposition、valuation.ai_credit_schism、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.private_credit_liquidity、ai.token_growth、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（quarterly_state 有值、event_scan 無 30 日事件）、ai.depreciation_life、ai.capital_cycle（兩組件皆無披露，增速證據不足，本次不判定資本週期階段）、speculation.upcoming_ai_ipos、structural.global_leveraged_approvals。其中 AI 信用定價分歧與私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）是 R3 的主要早期訊號；這兩個缺口若實際存在未被捕捉的壓力，可能讓 R3 比本次判讀更接近觸發，是本次最可能改變答案的缺口。

其他資料品質說明：

- speculation.insider_form4 記為 0 件：搜尋找到一筆 NVDA Form 4 結果（EDGAR，日期 2026-09-02），但沒有交易日與完整 filing-level 細節，不符合合格要求，因此不列名、不作為證據。
- case/evidence.md 描述美債基差交易槓桿的 script 三區塊為 fetch_failed，但本次 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 皆為 status ok；本報告以 macro artifact 為準，記為 ✓ API。
- 多個搜尋摘錄值（hyperscaler capex 約 725、AI 終端營收約 105、Anthropic 約 65、H100 租金約 3.38、槓桿 ETF 約 40.74）在摘錄中沒有逐字標示單位，本報告不推定精確單位。
- R2 只有四家合計值，沒有逐家指引與方向，下一次財報日期也未取得。
- R3 沒有任何借款人的負債規模經本次來源確立。

最大的不確定性：

1. 2026-09-16 FOMC：若如 FedWatch 所示升息，且引發實質利率續升，會把答案推向 yes（R1）；若按兵不動或釋出鴿派訊號，會強化 no。
2. 下一輪 hyperscaler 季報（落在窗口內，日期未確立）：若有兩家下修 capex，R2 直接觸發；若持續上修，強化 no。
3. AI 基礎設施借款人的再融資狀態未知：本次沒有信用定價數據，若出現利差急遽走闊或再融資失敗，會推向 yes（R3，並可能傳導至 R1）。

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
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（家庭股票配置 %，2026Q2 季資料，FRED 以季初日標記） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.7 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.8 | FRED API (series_id=BAMLC0A0CM) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.95 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（較 2026-09-03） | 18.0 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.55 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps（較 2026-09-03） | 13.0 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%，derived＝DGS10 − DFII10） | 2.4 | derived: FRED API (series_id=DGS10) − FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（美元/桶） | 97.26 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO chg_pct（較 2026-09-03） | 5.09 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-08 月資料） | 3.35 | FRED API (series_id=CPIAUCSL) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.32 | FRED API (series_id=T5YIFR) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（%，Kim-Wright） | 0.8892 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API (series_id=SOFR99) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-09-13 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,740,619（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,912,178（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,446,620（¥644.66T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 17.84 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（7 日窗 2026-09-03 → 2026-09-10，comove=false） | 17.84 | FRED API (series_id=VIXCLS ＋ SP500 共同日序) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 24.58 | FRED API (series_id=VIXCLS ＋ SP500 共同日序) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -2.01 | FRED API (series_id=VIXCLS ＋ SP500 共同日序) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（十億美元） | 2027.9777（≈$2.03T） | FRED API (series_id=LNFACBW027SBOG) | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六個 CBT 美債期貨合約槓桿基金淨部位，口） | -6863118 | CFTC TFF futures-only | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 387809 | CFTC TFF futures-only | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 82.21 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2271.6 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（gurufocus / multpl） | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch（CNBC） | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d ＋ same quarter） | ✗ NOT DISCLOSED（無同季合格 TP 上修） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch（14d） | ✗ NOT DISCLOSED（14 日內無合格披露） |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch（247wallst） | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch（247wallst） | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch（condoredge） | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch（CNN） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch（Advisor Perspectives，2026-07 月資料 carry-forward） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | WebSearch（AAII） | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED（無顯著討論） |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED（無當週值） |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✗ NOT DISCLOSED（無新調查） |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（DFEDTARU ok；DFEDTARL ok） | ✓ API |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE 由 DGS10 − DFII10 計算） | derived（DGS10 − DFII10） |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） | ✓ API |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW ok；JPNASSETS ok） | ✓ API |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無合格披露） |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（2026-07 財報季 carry-forward） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED（無當季披露） |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch（Axios） | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | WebSearch | ✗ NOT DISCLOSED（無合格披露） |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch（GPU 租金） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch；quarterly_state 沿用 2026-07-28 CNBC；event_scan 30 日無事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch ＋ 既有 bullets 組合（分母 top-4） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動（depreciation useful-life change） | WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無變動披露） |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch；兩組件皆無可用披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（IPOScoop） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（Finviz / Benzinga / StockTitan / Yahoo movers） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無 S-1 或具名來源報導） |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR ＋ WebSearch（14d，需 filing-level 細節） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch（etfaction） | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR ＋ ETF.com 新上市 feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d，KRX / TWSE / JPX / ESMA / ETFGI） | ✗ NOT DISCLOSED（7 日內無英文披露） |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe insights） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報摘要） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch（CNBC） | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS ok；vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（currentmarketvaluation） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds ok；move_index ok；ofr_repo ok）；aggregation any | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.73（原定 multpl / gurufocus） | S&P 500 Shiller CAPE ratio current September 2026 multpl | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | Magnificent 7 forward P/E valuation September 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html（CNBC） | 2026-08-03 | 2026-09-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 至 7 月止 YTD 報酬約 13% | RSP equal weight vs SPY S&P 500 YTD performance September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度約 38% | S&P 500 top 10 concentration percentage September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 200 日均線之上約 53% | market breadth advance decline new highs lows September 2026 percent stocks above 200-day | https://condoredge.com/stocks/market-breadth（CondorEdge） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 約 35（恐懼） | CNN Fear and Greed Index today September 2026 reading | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）約 1.42 兆美元 | FINRA margin debt August 2026 record year over year | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026（Advisor Perspectives，原定 FINRA） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.0% | AAII sentiment survey results week September 10 2026 bullish bearish neutral | https://www.aaii.com/sentimentsurvey（AAII） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.71 | Treasury auction results September 2026 tail bid-to-cover 10-year | https://thevaultreport.com/treasury-auctions（The Vault Report） | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.fedwatch | 9/16 FOMC 升息 25bp 機率約 85.5%（原定 CME FedWatch） | CME FedWatch September 12 2026 probability 25 basis point hike | https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html（Yahoo Finance） | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate financing 2026 total social financing | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm（SteelOrbis） | 2026-08-15 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 725（2026-07 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65 | OpenAI Anthropic annualized revenue run rate September 2026 | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| ai.compute_supply_demand | H100 中位租金約 3.38 | GPU rental price HBM DRAM contract price September 2026 utilization | https://www.thundercompute.com/blog/ai-gpu-rental-market-trends（Thunder Compute） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 增額債務佔 capex 約 32%（背景，2026-07 財報季） | hyperscaler capex vs free cash flow debt issuance 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 105（分母 top-4 capex 約 725） | AI revenue vs capex gap 2026 annualized run rate | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement September 7-13 2026 | 檢查來源：SPACInsider、Businesswire SPAC newsroom、Boardroom Alpha（窗內無合格事件） | — | 2026-09-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 22 檔 | IPO priced week September 8 2026 first day return debut | https://www.iposcoop.com/current-year-pricings/（IPOScoop） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（0 件符合 2+ 主題×弱基本面） | biggest stock gainers week September 7 2026 microcap 100% quantum AI | 檢查來源：Finviz、Benzinga、StockTitan、Yahoo movers（Tenon +77%、AEON +35% 皆未達門檻） | — | 2026-09-13T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 14 日掃描（0 件合格：唯一結果缺交易日等 filing-level 細節） | insider selling Form 4 September 2026 Nvidia AI executives SEC filing | 檢查來源：SEC EDGAR Form 4 搜尋結果（未達合格要求） | — | 2026-09-13T09:30:00+08:00 |
| speculation.equity_put_call | equity put/call 約 0.67（讀數類型未標示） | Cboe equity put call ratio September 2026 reading | https://www.thetrading.tools/put-call-ratio（thetrading.tools） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.74 | leveraged ETF assets under management September 2026 record single stock | https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/（ETF Action） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval September 2026 | 檢查來源：SEC EDGAR、ETF.com 新上市 feed（窗內無合格核准或上市） | — | 2026-09-13T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比創紀錄約 62%（8 月） | 0DTE options share SPX volume September 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.options_volume | OCC 8 月總結算量約 1.44 十億口（2026-08 月資料） | OCC options volume August 2026 monthly report | https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/（Traders Magazine） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 收在約 17 以上、call skew 第 91 百分位 | fear gauge VIX hedges September 10 2026 volatility | https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html（CNBC） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率，基數約 1.42 兆美元（2026-07 月資料） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php（Current Market Valuation） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Qualcomm 對 Amazon 認股權證約 40 億美元（資料中心基礎設施交易） | Qualcomm warrants Amazon 4 billion AI infrastructure deal September 2026 | https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html（CNBC） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |

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

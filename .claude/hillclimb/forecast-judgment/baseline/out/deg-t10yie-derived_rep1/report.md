> [DRY RUN] this report was not committed to archive.

# 2026-09-13 AI 泡沫破裂預測報告

報告日期：2026-09-13｜ISO 週次：2026-W37｜預測窗口：2026-09-13 → 2027-03-14｜前次基準：report-2026-09-03（10天前）

## 結論

**結論：no**

三條路徑目前都沒有進入完成階段：NASDAQ-100 自 52 週高點僅回撤 4.21%，離 R1 門檻還需再跌約 21.70%（`valuation.ndx_drawdown`）；HY OAS 2.70%、IG OAS 0.80% 顯示信用市場尚未替 AI 借款人重定價（`monetary.hy_oas`、`monetary.ig_oas`），本次證據也沒有任何 hyperscaler 下修 capex 指引（`ai.hyperscaler_capex`）。9/16 FOMC 升息預期與實質利率上行是真實的催化劑，但單憑它不足以推翻 182 天窗口內三條路徑皆不完成的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,368.44（2026-09-11），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 4.21%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，從最新收盤需再下跌約 21.70% 才觸及。同期 S&P 500 收 7,656.98（2026-09-11），較前次基準日（2026-09-03）的 7,747.71 下跌 1.17%，仍高於 200 日均線 6.9%、高於 52 週均線 8.33%（`valuation.sp500_trend`）。估值面 Shiller CAPE 約 40.73（2026-09-01，`valuation.sp500_pe_cape`），前十大成分股佔 S&P 500 約 38%（`breadth.top10_concentration`），代表一旦下跌，幅度可能很大。但 Mag 7 前瞻本益比已低於 24（2026-08-03，`valuation.mag7_multiples`），市場情緒偏恐懼而非亢奮：CNN Fear & Greed 約 35（2026-09-10，`retail.fear_greed`），AAII 看多約 38.0%（`retail.aaii`）。VIX 在 2026-09-03 → 2026-09-10 的 7 日視窗由 14.32 升到 17.84（+24.58%），同期 S&P 500 跌 2.01%，屬正常的避險反向關係，並非 crowded-optionality 的同漲讀數（`structural.vix_spx_comove`）；MOVE 由 74.68 升至 82.21（`structural.treasury_basis_trade`）。

**判讀：** 距 R1 還很遠（還需約 21.70% 的跌幅）。窗口內要觸發，需要一個把 NASDAQ-100 打掉逾五分之一的衝擊，例如 Fed 升息後實質利率持續上行，疊加 AI 財報或 capex 敘事破裂，或 R3 信用事件外溢。目前波動率的上升屬於溫和避險，不是失序。

### R2 資本支出收縮

本次取得的最新官方指引來自 2026 年 7 月下旬的財報季：Microsoft、Alphabet、Amazon、Meta 四家 2026 年 capex 合計約 725（十億美元）（2026-07-28，`ai.hyperscaler_capex`）。各家個別數字與「相對前一次正式指引的方向」未在本次證據中分列，因此逐家只能記為：Microsoft 未分列、Alphabet 未分列（報導指 Alphabet 財報後市場對 capex 的檢視轉嚴）、Amazon 未分列、Meta 未分列；本次證據中沒有任何一家下修，已下修家數為 0／4。前次基準日以來沒有新財報。下一輪財報的確切日期本次未取得；窗口一路延伸至 2027-03-14，涵蓋 10 月下旬（Q3）與 1–2 月（Q4 及 2027 全年指引）兩個財報季，是 R2 最可能出現變化的節點。需求端：Anthropic 年化 run-rate 約 65（十億美元）（2026-08-17，`ai.openai_anthropic_revenue`）；H100 中位租金約 3.38 美元／小時（2026-08-31，`ai.compute_supply_demand`），本次沒有配套的利用率惡化證據。產業層級 AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 105 vs 年化 capex 約 725（十億美元；分母：top-4 hyperscaler，Oracle 本次無可用 capex 數字未納入），缺口仍大（`ai.revenue_capex_gap`）。

**判讀：** R2 尚未起步（0／4 下修）。要在窗口內成立，至少兩家必須在 Q3（10 月）或 Q4（1–2 月）財報下修 2026 或 2027 年指引；以目前「指引持續上修、市場只是檢視轉嚴」的狀態，這需要先出現 R1 式股價壓力或明確的需求降溫證據。

### R3 AI 信用事件

本次沒有取得任何單一 AI 基礎設施借款人（負債 ≥ 50 億美元、以 AI 資料中心／算力為主業）的當期債券殖利率、利差、CDS 或評等動作；AI 信用定價分歧（equity-vs-credit schism）的 14 日掃描未找到合格報導，故無法逐家列出近期到期或再融資牆。30 日窗口內唯一的 AI infrastructure debt financing / vendor-financing loops 事件是 Qualcomm 對 Amazon 發出約 40 億美元的認股權證，作為資料中心基礎設施合作的一部分（2026-09-08，`structural.ai_infrastructure_debt`）：這是賣方給買方股權誘因的循環式安排，屬於結構性脆弱性，不是違約訊號。整體信用環境仍緊：HY OAS 2.70%（較前次 +5bp）、IG OAS 0.80%（`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 −3bp、SOFR99−IORB 為 +5bp，SRF 動用（Standing Repo Facility usage）為 0（`monetary.repo_stress_srf`）；銀行對 NBFI 放款約 $2.03T（2026-09-02，無新觀測，`structural.nbfi_bank_loans`）。本次沒有任何違約、寬限期、distressed exchange 或 going-concern 揭露。

**判讀：** R3 沒有可見的前兆。要在窗口內成立，需要一家大型 neocloud 或 AI 資料中心借款人實際破產、違約或完成 distressed exchange；目前利差極窄、資金市場平穩，最可能的路徑是 R1／R2 先發生、切斷再融資，而不是 R3 自發先爆。

## 支持 yes 的證據

- [整體] 貨幣條件正在收緊：CME FedWatch 顯示 9/16 FOMC 升息 25bp 的機率約 85.5%（2026-09-12，`monetary.fedwatch`）；CPI 年增 3.35%（2026-08 月資料，`monetary.cpi_yoy`）；WTI 97.26（2026-09-09，較前次 +5.09%，`monetary.wti`）；10Y 殖利率一週上升 18bp 至 4.95%，其中實質利率 DFII10 貢獻 +13bp、breakeven 僅 +5bp（driver：real-rate，`monetary.dgs10`、`monetary.dfii10`）。對高估值的長存續期 AI 股而言，實質利率上行是最直接的折現率衝擊。
- [R1] 估值與集中度處於歷史極端：Shiller CAPE 約 40.73（2026-09-01，`valuation.sp500_pe_cape`），前十大成分股佔 S&P 500 約 38%（2026-09-01，`breadth.top10_concentration`），S&P 500 仍高於 200 日均線 6.9%（`valuation.sp500_trend`）。一旦出現催化劑，下跌幅度會被放大。
- [R1] 槓桿與短天期投機仍高：SPX 0DTE 佔比在 8 月創紀錄約 62%（`structural.zero_dte`），OCC 8 月總結算量約 14.4 億口（`structural.options_volume`），單一個股槓桿 ETF 規模約 40.74（十億美元）（2026-09-08，`structural.leveraged_etf_aum`），margin debt 約 1.42 兆美元（2026-07 月資料，`retail.margin_debt`）。這類部位在下跌時會形成被迫去槓桿。
- [R1] 避險需求升溫：VIX 7 日內由 14.32 升至 17.84（+24.58%，`structural.vix_spx_comove`），call skew 位於第 91 百分位（2026-09-10，`structural.cross_asset_derivatives`），MOVE 由 74.68 升至 82.21（`structural.treasury_basis_trade`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）仍大：年化 AI 終端營收約 105 vs top-4 capex 約 725（十億美元）（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`），且報導指市場在 Alphabet 財報後對 capex 的檢視轉嚴（2026-07-28，`ai.hyperscaler_capex`）。這是 Q3／Q4 財報季指引下修的潛在壓力。
- [R3] AI infrastructure debt financing / vendor-financing loops 持續出現：Qualcomm 對 Amazon 發出約 40 億美元認股權證（2026-09-08，`structural.ai_infrastructure_debt`），顯示供應商以股權誘因綁定買方的循環結構仍在擴大。

## 支持 no 的證據

- [R1] NASDAQ-100 自 52 週高點只回撤 4.21%（2026-09-11），R1 門檻 22,995.45 需要從 29,368.44 再跌約 21.70%（`valuation.ndx_drawdown`）。在 182 天內從這個距離完成 25% 回撤，需要一次大型衝擊，不屬基準情境。
- [R3] 信用市場沒有重定價：HY OAS 2.70%、IG OAS 0.80%（2026-09-10，`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）−3bp、SRF 動用 0（`monetary.repo_stress_srf`）；CFTC 槓桿基金美債期貨淨空單 4 週縮小 387,809 口至 -6,863,118 口（2026-09-08，`structural.treasury_basis_trade`）。R3 需要的違約或 distressed exchange 沒有任何前兆。
- [R2] 本次證據中四大 hyperscaler 沒有任何一家下修 capex，2026 年合計指引約 725（十億美元）（2026-07-28，`ai.hyperscaler_capex`）；需求端 Anthropic 年化 run-rate 約 65（十億美元）（2026-08-17，`ai.openai_anthropic_revenue`），H100 中位租金約 3.38 美元／小時（2026-08-31，`ai.compute_supply_demand`），看不到需求崩落。
- [整體] 情緒並不亢奮，反而偏防禦：CNN Fear & Greed 約 35（恐懼，2026-09-10，`retail.fear_greed`），AAII 看多約 38.0%（2026-09-10，`retail.aaii`），equity put/call 約 0.67（2026-09-01，`speculation.equity_put_call`），Mag 7 前瞻本益比低於 24（2026-08-03，`valuation.mag7_multiples`），約 53% 成分股在 200 日均線之上（2026-09-11，`breadth.advance_decline`）。泡沫頂部常見的群眾亢奮與極度一致性在此看不到。
- [整體] 投機篩檢偏冷：+AI 改名／SPAC 7 日掃描 0 件（`speculation.ai_rename_spac`），microcap 主題 moonshot 0 件（`speculation.microcap_moonshots`），美國單一個股槓桿 ETF 30 日核准／上市 0 件（`structural.us_single_stock_etf`）；資金另一面是單一個股 ETF 遭贖回約 7.51 億美元（2026-09-08，`structural.leveraged_etf_aum`）。
- [整體] 5y5y 通膨預期 2.32% 持平偏降（`monetary.t5yifr`）、10Y 期限溢價（term premium）0.8892%，trailing ≈7d 僅 +1.4bp（`monetary.term_premium`），長端並未出現財政再定價式失序，Fed 不至於在通膨預期失錨下被迫連續大幅升息。

## 與前期比較

前次結論：無前次預測（report-2026-09-03 為舊格式評分報告）

前次為舊格式評分報告，其分數不轉換為 yes／no，flip discipline 不適用。自 2026-09-03 以來的主要變化：

- 10Y 殖利率 +18bp 至 4.95%，以實質利率為主（DFII10 +13bp，breakeven +5bp，三腿皆有新觀測），9/16 FOMC 升息預期升至約 85.5%（`monetary.dgs10`、`monetary.fedwatch`）。
- S&P 500 由 7,747.71 跌至 7,656.98（−1.17%），VIX 由 14.32 升至 17.84，MOVE 由 74.68 升至 82.21（`valuation.sp500_trend`、`structural.vix_spx_comove`、`structural.treasury_basis_trade`）。
- WTI 由 92.55 升至 97.26（+5.09%，`monetary.wti`）。
- HY OAS 由 2.65% 微升至 2.70%，IG OAS 由 0.81% 降至 0.80%，信用端幾乎不動（`monetary.hy_oas`、`monetary.ig_oas`）。
- 上述變化提高了 R1 的催化劑強度，但沒有任何路徑接近完成，本次結論為 no。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED 的 optional 來源（檢索完成、無合格當期揭露）：valuation.analyst_tp_decomposition、valuation.ai_credit_schism、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.private_credit_liquidity、ai.token_growth、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（quarterly_state 有值、30 日 event_scan 無合格事件）、ai.depreciation_life、ai.capital_cycle（兩組件皆無揭露，本次不判定週期階段）、speculation.upcoming_ai_ipos、structural.global_leveraged_approvals。其中最可能改變答案的是 valuation.ai_credit_schism：R3 的逐家信用定價（CoreWeave 等 neocloud 債券／CDS）在本次完全空白；若這些發行人利差已明顯走闊而 HY 指數未反映，R3 的距離會被低估。不過在指數利差 2.70% 的環境下，單一大型借款人在 182 天內違約仍需要大量額外證據，因此這個缺口目前不足以翻轉結論。

其他資料說明：

- ai.hyperscaler_capex 只取得四家合計值約 725（十億美元），沒有逐家指引與方向；R2 的「0／4 下修」是依據本次證據未見下修，而非逐家驗證。若某家在 7 月已小幅下修而未被捕捉，R2 的距離會更近（偏向 yes）。
- speculation.insider_form4：EDGAR 檢索找到一筆 CIK 0001045810 的 Form 4（日期 2026-09-02），但證據沒有分列 filing date 與 transaction date，不符合 filing-level 必要欄位，因此不列為合格事件，記為 0 件。
- structural.treasury_basis_trade：搜尋紀錄寫的是腳本三區塊 fetch_failed，但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 皆為 status: ok；本報告以 macro artifact 為準，記為 ✓ API，WebSearch 補充（basis-trade 平倉新聞）無合格揭露。
- monetary.t10yie 為 derived（DGS10 − DFII10），10Y 分解恆等式依構造成立，只能確認歸因，不是獨立交叉驗證。
- JPNASSETS（2026-08-01）與 LNFACBW027SBOG（2026-09-02）自前次以來無新觀測，以持平處理；BOGZ1FL153064486Q 沿用 2026 Q2 季值。

最大的不確定性：

1. 9/16 FOMC 若實際升息並釋出鷹派路徑，實質利率可能繼續上行，壓縮 AI 股估值（偏向 yes，主要經由 R1）。
2. 10 月下旬及 1–2 月的 hyperscaler 財報：若兩家以上下修 2027 年 capex，R2 直接成立（偏向 yes）；若持續上修，R2 在窗口內幾乎不可能成立（偏向 no）。
3. Neocloud 再融資：本次沒有逐家到期資料，一旦股市修正使股權融資窗口關閉，R3 可能在窗口後段加速（偏向 yes）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7656.98 | FRED API (series_id=SP500)，script sp500_trend block | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 6.9 | FRED API (series_id=SP500)，script sp500_trend block | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.33 | FRED API (series_id=SP500)，script sp500_trend block | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較前次基準 %） | -1.17 | FRED API (series_id=SP500)，script sp500_trend block | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29368.44 | FRED API (series_id=NASDAQ100)，script ndx_drawdown block | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100)，script ndx_drawdown block | 2026-06-02 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（自高點回撤 %） | 4.21 | FRED API (series_id=NASDAQ100)，script ndx_drawdown block | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100)，script ndx_drawdown block | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（家庭股票配置 %，2026 Q2 季值） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.7 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps（較前次） | 5.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.8 | FRED API (series_id=BAMLC0A0CM) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.95 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（較前次） | 18.0 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.55 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps（較前次） | 13.0 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%，derived = DGS10 − DFII10） | 2.4 | script derived (series_id=T10YIE) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（美元／桶） | 97.26 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO chg_pct（較前次 %） | 5.09 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-08 月資料） | 3.35 | FRED API (series_id=CPIAUCSL) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.32 | FRED API (series_id=T5YIFR) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（%，Kim-Wright） | 0.8892 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing ≈7d） | 1.4 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API (series_id=SOFR99) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-09-13 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps（SOFR − IORB，兩腿皆 2026-09-10） | -3.0 | script repo_stress block (SOFR, IORB) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest（百萬美元） | 6,740,619（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（百萬歐元） | 5,912,178（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（億日圓，無新觀測） | 6,446,620（¥644.66T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 17.84 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of，視窗 7 日，base 2026-09-03） | 17.84 | FRED SP500 與 VIX 日序，script vix_spx_comove block | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 24.58 | FRED SP500 與 VIX 日序，script vix_spx_comove block | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（comove: false） | -2.01 | FRED SP500 與 VIX 日序，script vix_spx_comove block | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（十億美元，無新觀測） | 2027.9777（$2.03T） | FRED API (series_id=LNFACBW027SBOG) | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -6,863,118 | CFTC TFF，script cftc_lev_funds block | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 387,809 | CFTC TFF，script cftc_lev_funds block | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 82.21 | Yahoo chart ^MOVE，script move_index block | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2271.6 | OFR STFM，script ofr_repo block | 2026-09-11 | 2026-09-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（multpl／gurufocus） | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED（無同季合格 TP 上修） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch（14d） | ✗ NOT DISCLOSED（14 日內無合格報導） |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch | ✓ SEARCH-VERIFIED（以 200 日均線之上比例代理） |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch（FINRA 月資料，carry forward） | ✓ SEARCH-VERIFIED（2026-07 月資料） |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE；script fallback derived） | derived（DGS10 − DFII10，2026-09-10） |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（repo_stress block） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok；repo_stress status ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok，無新觀測） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（最近財報季，carry forward） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch（quarterly_state stock_of_state；event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch＋既有 bullets 組合 | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動（depreciation useful-life change） | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch（quarterly_state stock_of_state；event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✗ NOT DISCLOSED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR＋WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove block） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）＋WebSearch 補充 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok；WebSearch 補充無合格揭露） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.73（原定來源 multpl／gurufocus） | S&P 500 Shiller CAPE ratio current September 2026 multpl | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | Magnificent 7 forward P/E valuation September 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html（CNBC） | 2026-08-03 | 2026-09-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 至 7 月止 YTD 報酬約 13% | RSP equal weight vs SPY S&P 500 YTD performance September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.top10_concentration | 前十大集中度約 38% | S&P 500 top 10 concentration percentage September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 200 日均線之上約 53% | market breadth advance decline new highs lows September 2026 percent stocks above 200-day | https://condoredge.com/stocks/market-breadth（Condor Edge） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 35（恐懼） | CNN Fear and Greed Index today September 2026 reading | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）約 1.42 兆美元 | FINRA margin debt August 2026 record year over year | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026（Advisor Perspectives，原定 FINRA） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.0% | AAII sentiment survey results week September 10 2026 bullish bearish neutral | https://www.aaii.com/sentimentsurvey（AAII） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.71 | Treasury auction results September 2026 tail bid-to-cover 10-year | https://thevaultreport.com/treasury-auctions（The Vault Report） | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.fedwatch | 9/16 FOMC 升息 25bp 機率約 85.5%（原定 CME FedWatch） | CME FedWatch September 12 2026 probability 25 basis point hike | https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html（Yahoo Finance） | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模增量約 22.25 兆人民幣（2026-07 月資料） | PBoC aggregate financing 2026 total social financing | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm（SteelOrbis） | 2026-08-15 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 725（十億美元，2026 Q2 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65（十億美元） | OpenAI Anthropic annualized revenue run rate September 2026 | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| ai.compute_supply_demand | H100 中位租金約 3.38 美元／小時 | GPU rental price HBM DRAM contract price September 2026 utilization | https://www.thundercompute.com/blog/ai-gpu-rental-market-trends（Thunder Compute） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 增額債務佔 capex 約 32%（2026 Q2 財報季） | hyperscaler capex vs free cash flow debt issuance 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 105（十億美元；分母沿用 ai.hyperscaler_capex top-4 約 725） | AI revenue vs capex gap 2026 annualized run rate | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描：0 件合格事件 | AI company name change ticker SPAC announcement September 7-13 2026 | 檢查來源：SPACInsider、Businesswire SPAC newsroom、Boardroom Alpha | — | 2026-09-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 22 檔 | IPO priced week September 8 2026 first day return debut | https://www.iposcoop.com/current-year-pricings/（IPOScoop） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描：0 件符合 2+ 主題×弱基本面（Tenon +77%、AEON +35% 未達門檻） | biggest stock gainers week September 7 2026 microcap 100% quantum AI | 檢查來源：Finviz、Benzinga、StockTitan、Yahoo movers | — | 2026-09-13T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 14 日掃描：0 件具完整 filing date＋transaction date 的合格事件 | insider selling Form 4 September 2026 Nvidia AI executives SEC filing | 檢查來源：SEC EDGAR（https://www.sec.gov/Archives/edgar/data/0001045810/000119903926000012/wk-form4_1788387031.xml 缺分列的 transaction date，未列入） | — | 2026-09-13T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 約 0.67（daily reading） | Cboe equity put call ratio September 2026 reading | https://www.thetrading.tools/put-call-ratio（The Trading Tools） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.74（十億美元），單一個股 ETF 遭贖回約 7.51 億美元 | leveraged ETF assets under management September 2026 record single stock | https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/（ETF Action） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval September 2026 | 檢查來源：SEC EDGAR、ETF.com 新上市 feed | — | 2026-09-13T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比創紀錄約 62%（2026-08 月資料） | 0DTE options share SPX volume September 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.options_volume | OCC 8 月總結算量約 1.44 十億口（2026-08 月資料） | OCC options volume August 2026 monthly report | https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/（Traders Magazine） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 收在約 17 以上、call skew 第 91 百分位 | fear gauge VIX hedges September 10 2026 volatility | https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html（CNBC） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 1.42 兆美元（2026-07 月資料，僅交叉檢查） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php（Current Market Valuation） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Qualcomm 對 Amazon 認股權證約 40 億美元（資料中心基礎設施合作） | Qualcomm warrants Amazon 4 billion AI infrastructure deal September 2026 | https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html（CNBC） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |

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
  "r1_drawdown_pct": 4.21,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

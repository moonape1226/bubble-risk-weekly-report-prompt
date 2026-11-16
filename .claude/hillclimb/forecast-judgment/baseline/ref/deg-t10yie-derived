> [DRY RUN] this report was not committed to archive.

# 2026-09-13 AI 泡沫破裂預測報告
報告日期：2026-09-13｜ISO 週次：2026-W37｜預測窗口：2026-09-13 → 2027-03-14｜前次基準：report-2026-09-03（10天前）

## 結論

**結論：no**

三條路徑目前都離解析門檻很遠：NASDAQ-100 距 52 週高點回撤 4.21%，還要再跌約 21.70% 才觸及 R1；信用端 HY OAS 2.70%、IG OAS 0.80% 仍處緊縮水位，本次證據也沒有任何 hyperscaler 下修 capex 或 AI 借款人違約的跡象。本次最強的 yes 因素是利率衝擊：10Y 殖利率 +18bp 由實質利率驅動，市場預期 9/16 FOMC 升息（`monetary.fedwatch`）。但目前看來這是會拉高估值脆弱度的催化劑，還沒形成能在 182 天內走完 R1–R3 的傳導鏈。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,368.44（2026-09-11），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 4.21%。R1 門檻水位為 22,995.45，要從最新收盤再跌約 21.70% 才會觸及（`valuation.ndx_drawdown`）。同期 S&P 500 為 7,656.98（2026-09-11），比 200 日均線 7,162.55 高 6.9%、比 52 週均線高 8.33%，較前次基準日下跌 1.17%（`valuation.sp500_trend`）。VIX 升至 17.84（2026-09-10），7 日窗口內 VIX +24.58%、S&P 500 −2.01%，屬正常的股跌波動升，並非同漲的 crowded-optionality 讀數（`structural.vix_spx_comove`）。情緒偏恐懼：CNN Fear & Greed 約 35（`retail.fear_greed`），AAII 看多約 38.0%（`retail.aaii`）。估值仍高，Shiller CAPE 約 40.73（`valuation.sp500_pe_cape`），但 Mag 7 前瞻本益比已降至 24 以下（`valuation.mag7_multiples`，2026-08-03）。

**判讀：** R1 距門檻還有約 21.70% 的跌幅空間，目前不在進行中的崩跌路徑上。窗口內能推過門檻的情境是：9/16 FOMC 升息後實質利率繼續大幅上行，疊加下一輪財報 AI 營收或 capex 敘事失望，使長存續期科技股出現估值壓縮；若再加上信用事件（R3）引發強制去槓桿，才可能在半年內完成 25% 回撤。

### R2 資本支出收縮

本次證據只有四大 hyperscaler 2026 年 capex 合計約 725（十億美元），出自 2026-07-28 的 CNBC 季報後報導（`ai.hyperscaler_capex`，Q2 2026 財報季，carry-forward 為 current）。Microsoft、Alphabet、Amazon、Meta 的逐家指引數字及其相對前次指引的方向（上修／持平／下修），本次證據都沒有提供，所以逐家方向列為「未取得」，不自行補值。目前的證據中沒有任何一家下修指引的報導，已下修家數按已知證據為 0 家。下一輪（Q3）與再下一輪（Q4）季報都會落在窗口內，但具體日期本次沒有取得。旁證：Anthropic 年化 run-rate 約 650 億美元（`ai.openai_anthropic_revenue`，2026-08-17）；AI 營收對 capex 缺口（revenue-to-capex gap）為年化 AI 終端營收約 1,050 億美元對 2026 capex 約 7,250 億美元（分母：top-4，不含 Oracle，因為 Oracle 的季頻組件本次沒有披露）（`ai.revenue_capex_gap`）；H100 中位租金約 3.38 美元／小時（`ai.compute_supply_demand`，2026-08-31），單看價格無法判斷產能缺口。

**判讀：** R2 需要四家中兩家正式下修，本次沒有任何下修證據，路徑尚未啟動。窗口內兩輪季報是唯一的觸發節點；可能推動的情境是 R1 式股價重挫，或融資成本上升迫使管理層在 Q4 財報（次年度指引）時收斂，但目前 AI 營收對 capex 的缺口雖大，需求端 run-rate 仍在成長。

### R3 AI 信用事件

本次沒有取得負債 ≥ 50 億美元的 AI 資料中心／算力借款人的個別信用定價：AI 信用定價分歧（equity-vs-credit schism）的 14 日掃描沒有窗內披露，也沒有觀察到違約、寬限期、distressed exchange 或 going-concern 字樣。30 日窗內唯一的 AI infrastructure debt financing / vendor-financing loops 事件，是 Qualcomm 對 Amazon 發出約 40 億美元的認股權證（`structural.ai_infrastructure_debt`，2026-09-08）。這屬於供應商對買方的股權誘因型循環安排，而非借款人壓力。整體信用水位仍緊：HY OAS 2.70%（+5bp，2026-09-10）（`monetary.hy_oas`）、IG OAS 0.80%（`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 −3bp、SOFR99−IORB 為 +5bp（均為 2026-09-10），SRF 動用（Standing Repo Facility usage）為 0（2026-09-11）（`monetary.repo_stress_srf`）；銀行對 NBFI 放款約 $2.03T，週變動 0%（`structural.nbfi_bank_loans`）。

**判讀：** R3 沒有任何可識別的進行中壓力訊號，信用市場整體也沒有重定價。窗口內要觸發，需要某家大型 neocloud 或資料中心借款人遭遇再融資失敗或客戶合約違約；在利率上行、MOVE 走升的環境下尾部風險提高，但目前沒有證據指向特定借款人。

## 支持 yes 的證據

- [整體] 市場預期 9/16 FOMC 升息，CME FedWatch 升息 25bp 機率約 85.5%（2026-09-12），政策利率目前 3.50%–3.75%，代表 Fed 在 AI 主導的回檔中難以提供降息緩衝（`monetary.fedwatch`、`monetary.fed_funds`）。
- [R1] 10Y 殖利率 4.95%（2026-09-10），比前次基準日 +18bp，分解為 ΔDFII10 +13bp、ΔT10YIE +5bp，由實質利率驅動；10Y 實質殖利率 2.55%，直接壓縮長存續期科技股估值（`monetary.dgs10`、`monetary.dfii10`）。
- [整體] 通膨壓力限制政策空間：CPI YoY 3.35%（2026-08 月資料），WTI 97.26 美元（2026-09-09），較前次基準日 +5.09%（`monetary.cpi_yoy`、`monetary.wti`）。
- [R1] 估值與集中度仍是泡沫級：Shiller CAPE 約 40.73（2026-09-01），S&P 500 前十大集中度約 38%（2026-09-01），一旦觸發，下行幅度會被放大（`valuation.sp500_pe_cape`、`breadth.top10_concentration`）。
- [R1] 波動與債市波動同步升溫：VIX 17.84（2026-09-10），7 日 +24.58%；MOVE 82.21（2026-09-11），比 74.68 升 7.53（`structural.vix_spx_comove`、`structural.treasury_basis_trade`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）仍大：年化 AI 終端營收約 1,050 億美元，對比 top-4 hyperscaler 2026 capex 約 7,250 億美元（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`）。
- [R1] 投機與槓桿部位仍高：SPX 0DTE 佔比創紀錄約 62%（2026-08），單一個股槓桿 ETF 規模約 407.4 億美元（2026-09-08），margin debt 約 1.42 兆美元（2026-07 月資料）（`structural.zero_dte`、`structural.leveraged_etf_aum`、`retail.margin_debt`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.21%（2026-09-11 收盤 29,368.44 vs 2026-06-02 高點 30,660.60），距 R1 門檻 22,995.45 還差約 21.70%，基準率上半年內完成這種跌幅屬少見事件（`valuation.ndx_drawdown`）。
- [R3] 信用市場沒有重定價：HY OAS 2.70%、IG OAS 0.80%（2026-09-10），均為緊縮水位，週變動僅 +5bp／−1bp（`monetary.hy_oas`、`monetary.ig_oas`）。
- [R3] 資金市場平穩：SOFR−IORB −3bp、SOFR99−IORB +5bp（2026-09-10），SRF 動用為 0（2026-09-11），OFR tri-party repo transaction volume 約 2.27 兆美元（2026-09-11，較前次 −1.78%），沒有國債市場失序（Treasury market dysfunction）跡象（`monetary.repo_stress_srf`、`structural.treasury_basis_trade`）。
- [R2] 本次證據中沒有任何 hyperscaler 下修 capex 指引，四家 2026 capex 合計約 7,250 億美元仍是擴張水位（2026-07-28）（`ai.hyperscaler_capex`）。
- [R2] 需求端仍在成長：Anthropic 年化 run-rate 約 650 億美元（2026-08-17）（`ai.openai_anthropic_revenue`）。
- [R1] 情緒已偏恐懼而非亢奮：CNN Fear & Greed 約 35（2026-09-10）、AAII 看多約 38.0%（2026-09-10）、equity put/call 約 0.67（2026-09-01），代表部位並未極端擁擠（`retail.fear_greed`、`retail.aaii`、`speculation.equity_put_call`）。
- [R1] 本次週篩選沒有找到合格的 +AI 改名／SPAC 事件，也沒有找到合格的 microcap 多主題 moonshot（各 0 件），投機狂熱沒有新增訊號（`speculation.ai_rename_spac`、`speculation.microcap_moonshots`）。
- [整體] 美債基差交易槓桿（Treasury basis-trade leverage）在收斂：CFTC 槓桿基金美債期貨淨部位 −6,863,118 口（2026-09-08），4 週淨空減少 387,809 口，降低被迫平倉的放大效應（`structural.treasury_basis_trade`）。

## 與前期比較

前次結論：無前次預測（report-2026-09-03 為舊格式評分報告）

前次為舊格式評分報告，不轉譯為 yes/no；flip_evidence 為空。自 2026-09-03 以來的主要變化：

- 10Y 殖利率由 4.77% 升至 4.95%（+18bp），實質利率驅動；FedWatch 轉為高度預期 9/16 升息。
- S&P 500 由 7,747.71 跌至 7,656.98（−1.17%），VIX 由 14.32 升至 17.84，MOVE 由 74.68 升至 82.21。
- HY OAS 由 2.65% 升至 2.70%，IG OAS 由 0.81% 降至 0.80%，信用端大致持平。
- SRF 動用由 0.033 降至 0，repo 資金壓力（SOFR−IORB）維持負值。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下 optional 來源完成檢索，但窗內沒有合格披露（✗ NOT DISCLOSED）：analyst TP 拆解、AI 信用定價分歧、social sentiment、NAAIM、BofA／JPM survey、私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）、token growth、backlog 重複計算風險（RPO double-counting）、hyperscaler 融資結構（capex vs FCF / 發債）的 30 日 event_scan、折舊年限變動（depreciation useful-life change）、資本週期階段（capital cycle stage）兩個組件、upcoming AI IPOs、全球槓桿產品核准。其中 AI 信用定價分歧與私募信貸贖回壓力兩項的缺口最可能影響 R3 判讀；但 HY／IG OAS 與 repo 指標都沒有出現壓力，所以目前不足以改變答案。

其他資料限制：

- R2 逐家指引缺失：本次只取得四家合計值，無法逐家判斷方向。若某兩家在上一輪財報其實已下修，答案會轉向 yes，但目前沒有任何證據指向這點。
- 內部 Form 4：EDGAR 檢索有一筆 2026-09-02 的結果，但缺少獨立的交易日欄位，未達 filing-level 要件，因此依規則以 0 件處理，不列出姓名與金額。
- 美債基差交易槓桿的 evidence 摘要寫 script 三個區塊為 fetch_failed，但 macro artifact 顯示 cftc_lev_funds、move_index、ofr_repo 三塊皆為 `ok`。本報告以 artifact 為準（✓ API）。

最大的不確定性：

1. 9/16 FOMC 升息幅度與後續路徑：若升息後 10Y 實質利率續升並突破前高，長存續期 AI 股估值壓縮會加速，推向 R1（偏 yes）；若只是一次性升息、實質利率回落，則偏 no。
2. 下一輪（Q3）hyperscaler 財報的 capex 指引：任何兩家下修即直接解析 R2（偏 yes）；續上修則偏 no。
3. 大型 neocloud／資料中心借款人的再融資：本次沒有個別信用定價可用，利率上行環境中若有借款人出現再融資困難，R3 與 R1 會同時被觸發（偏 yes）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7656.98 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線偏離 %） | 6.9 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線偏離 %） | 8.33 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（NASDAQ-100 最新收盤） | 29368.44 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 4.21 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（家庭股票配置 %，2026Q2 季資料，FRED 以季初日期標記） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.7 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 5.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.8 | FRED API (series_id=BAMLC0A0CM) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.95 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | 18.0 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.55 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | 13.0 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%，derived = DGS10 − DFII10） | 2.4 | derived from FRED API DGS10 / DFII10 | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（美元／桶） | 97.26 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO chg_pct | 5.09 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-08 月資料） | 3.35 | FRED API (series_id=CPIAUCSL) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.32 | FRED API (series_id=T5YIFR) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（%，Kim-Wright） | 0.8892 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7d） | 1.4 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API (series_id=SOFR99) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-09-13 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6740619.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5912178.0（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6446620.0（¥644.66T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 17.84 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（comove=false） | 17.84 | script vix_spx_comove block（VIXCLS × SP500） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日） | 24.58 | script vix_spx_comove block（FRED SP500 共同日期對） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日） | -2.01 | script vix_spx_comove block（FRED SP500 共同日期對） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2027.9777（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -6863118 | CFTC TFF futures-only（cftc_lev_funds） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 387809 | CFTC TFF futures-only（cftc_lev_funds） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 82.21 | Yahoo Finance chart API ^MOVE（move_index） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2271.6 | OFR STFM REPO-TRIV1_TV_TOT-P（ofr_repo） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（multpl / GuruFocus） | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED（窗內無合格 TP 上修拆解） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✗ NOT DISCLOSED（14 日窗內無合格披露） |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight vs cap-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED（窗內無顯著討論） |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED（無當期週值） |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM | WebSearch | ✗ NOT DISCLOSED（無新一期 survey） |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（FRED T10YIE；fallback 推導） | derived（DGS10 − DFII10，FRED T10YIE 未直接取得） |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED（30 日窗內無合格披露） |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state，carry Q2 2026） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED（無當季披露） |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✗ NOT DISCLOSED（無合格披露） |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch；quarterly_state 為 stock-of-state carry，event_scan 為 30 日掃描（無窗內融資事件） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch＋組合既有 bullets（分母 top-4） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED（30 日窗內無變動） |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch；兩組件皆無可用披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（7d movers 篩選） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✗ NOT DISCLOSED（30 日窗內無 S-1 或具名報導） |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR／WebSearch（14d，需 filing-level 要件） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d，KRX／TWSE／JPX／ESMA） | ✗ NOT DISCLOSED（7 日窗內無英文披露） |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe insights） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo），WebSearch 補充 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.73 | S&P 500 Shiller CAPE ratio current September 2026 multpl | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio （GuruFocus；原定 multpl／GuruFocus） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | Magnificent 7 forward P/E valuation September 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html （CNBC） | 2026-08-03 | 2026-09-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 至 7 月止 YTD 報酬約 13% | RSP equal weight vs SPY S&P 500 YTD performance September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/ （24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度約 38% | S&P 500 top 10 concentration percentage September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/ （24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.advance_decline | 成分股位於 200 日均線之上約 53% | market breadth advance decline new highs lows September 2026 percent stocks above 200-day | https://condoredge.com/stocks/market-breadth （Condor Edge） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 35（恐懼） | CNN Fear and Greed Index today September 2026 reading | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）約 1.42 兆美元 | FINRA margin debt August 2026 record year over year | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026 （Advisor Perspectives；原定 FINRA） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.0% | AAII sentiment survey results week September 10 2026 bullish bearish neutral | https://www.aaii.com/sentimentsurvey （AAII） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.71 | Treasury auction results September 2026 tail bid-to-cover 10-year | https://thevaultreport.com/treasury-auctions （The Vault Report） | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.fedwatch | 9/16 FOMC 升息 25bp 機率約 85.5% | CME FedWatch September 12 2026 probability 25 basis point hike | https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html （Yahoo Finance；原定 CME FedWatch） | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.pboc | 2026 年 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate financing 2026 total social financing | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm （SteelOrbis） | 2026-08-15 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 725（十億美元），Q2 2026 財報季 | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65（十億美元） | OpenAI Anthropic annualized revenue run rate September 2026 | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| ai.compute_supply_demand | H100 中位租金約 3.38 美元／小時 | GPU rental price HBM DRAM contract price September 2026 utilization | https://www.thundercompute.com/blog/ai-gpu-rental-market-trends （Thunder Compute） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 增額債務佔 capex 約 32%（Q2 2026 財報季） | hyperscaler capex vs free cash flow debt issuance 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 105（十億美元）；分母取 ai.hyperscaler_capex 的 top-4 合計 | AI revenue vs capex gap 2026 annualized run rate | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描：0 件合格事件 | AI company name change ticker SPAC announcement September 7-13 2026 | 檢查來源：SPACInsider、Businesswire SPAC newsroom、Boardroom Alpha | — | 2026-09-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 22 檔 | IPO priced week September 8 2026 first day return debut | https://www.iposcoop.com/current-year-pricings/ （IPOScoop） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描：0 件符合 2+ 主題 × 弱基本面（最大漲幅 +77%、+35% 皆未達門檻） | biggest stock gainers week September 7 2026 microcap 100% quantum AI | 檢查來源：Finviz、Benzinga、StockTitan、Yahoo movers | — | 2026-09-13T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 14 日掃描：0 件符合 filing-level 要件（唯一 EDGAR 結果缺少獨立交易日欄位） | insider selling Form 4 September 2026 Nvidia AI executives SEC filing | 檢查來源：SEC EDGAR（https://www.sec.gov/Archives/edgar/data/0001045810/000119903926000012/wk-form4_1788387031.xml ） | — | 2026-09-13T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 約 0.67（日讀數） | Cboe equity put call ratio September 2026 reading | https://www.thetrading.tools/put-call-ratio （thetrading.tools；原定 Cboe） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.74（十億美元） | leveraged ETF assets under management September 2026 record single stock | https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/ （ETF Action） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval September 2026 | 檢查來源：SEC EDGAR、ETF.com 新上市 feed | — | 2026-09-13T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比創紀錄約 62%（2026-08） | 0DTE options share SPX volume September 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august （Cboe） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.options_volume | OCC 8 月總結算量約 1.44 十億口 | OCC options volume August 2026 monthly report | https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/ （Traders Magazine；原定 OCC） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 收在約 17 以上、call skew 第 91 百分位 | fear gauge VIX hedges September 10 2026 volatility | https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html （CNBC） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 1.42 兆美元（2026-07 月資料，僅交叉確認） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php （Current Market Valuation） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Qualcomm 對 Amazon 認股權證約 4（十億美元），供應商對買方的循環安排 | Qualcomm warrants Amazon 4 billion AI infrastructure deal September 2026 | https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html （CNBC） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |

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

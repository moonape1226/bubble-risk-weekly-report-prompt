> [DRY RUN] this report was not committed to archive.

# 2026-09-13 AI 泡沫破裂預測報告

報告日期：2026-09-13｜ISO 週次：2026-W37｜預測窗口：2026-09-13 → 2027-03-14｜前次基準：report-2026-09-03（10天前）

## 結論

**結論：no**

三條路徑目前都離觸發很遠：NASDAQ-100 距 52 週高點回撤 4.21%，還需再跌約 21.70% 才觸及 R1；四大 hyperscaler 2026 capex 合計約 725（USD bn）且檢索結果未見任何下修，HY OAS 2.70% 也未顯示 AI 信用壓力。9/16 FOMC 升息預期（FedWatch 約 85.5%）與殖利率上行是最主要的 yes 側催化劑，但目前證據不足以把任一路徑推過門檻。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29368.44（2026-09-11），252 個交易日最高收盤 30660.6（2026-06-02），距 52 週高點回撤 4.21%（`valuation.ndx_drawdown`）。R1 門檻水位為 22995.45，自最新收盤須再下跌約 21.70% 才會觸及。背景脆弱度偏高：Shiller CAPE 約 40.73（`valuation.sp500_pe_cape`），S&P 500 前十大權重約 38%（`breadth.top10_concentration`），S&P 500 收在 7656.98、高於 200 日均線 6.9%、高於 52 週均線 8.33%（`valuation.sp500_trend`）。催化面：10Y 殖利率 4.95%（自 2026-09-03 起 +18 bps）、10Y 實質殖利率 2.55%（+13 bps）（`monetary.dgs10`、`monetary.dfii10`）；10Y breakeven 2.36%（+1 bp，但 T10YIE 視窗與另兩腿不一致，判讀：不可判（視窗不一致））（`monetary.t10yie`）；CME FedWatch 顯示 9/16 FOMC 升息 25 bps 的市場隱含機會約 85.5%（`monetary.fedwatch`），而 CPI YoY 3.35%（2026-08 月資料）（`monetary.cpi_yoy`）限制了 Fed 緩衝 AI 主導下跌的空間。VIX 由 14.32 升至 17.84（+24.58%），同期 S&P 500 −2.01%，兩者反向，未出現 crowded-optionality 共振（`structural.vix_spx_comove`，視窗 2026-09-03 → 2026-09-10）。

**判讀：** R1 距門檻仍有約 21.70% 的下跌空間，屬遠端；在 182 天窗口內要觸發，需要升息循環重啟加上獲利或 capex 敘事破裂的雙重衝擊，目前只見前者的苗頭（升息預期、殖利率上行），未見後者。

### R2 資本支出收縮

本次檢索到的最新資料為 2026-07-28 CNBC 報導：Microsoft、Alphabet、Amazon、Meta 四家 2026 年 capex 合計約 725（USD bn），報導標題指 Alphabet 財報後 capex 受到更嚴格檢視（`ai.hyperscaler_capex`）。檢索結果只給出合計值，未逐家揭露各公司最新正式指引數值及其相對前次指引的方向，因此四家個別方向本次皆無法逐一確認（未提供逐家指引）；檢索結果中亦無任何一家下修的報導，已下修家數就現有證據為 0。下一輪財報日期未見於本次證據；依季度財報節奏，窗口（至 2027-03-14）內預期至少涵蓋兩次財報季，但確切日期未經來源確認。需求側支撐：Anthropic 年化 run-rate 約 65（USD bn，2026-08-17）（`ai.openai_anthropic_revenue`）；AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 105（USD bn）vs 年化 capex 約 725（USD bn）（分母：top-4，Oracle 未納入），本次無前值可判斷缺口擴大或收斂（`ai.revenue_capex_gap`）。H100 中位租金約 3.38 USD/hr（2026-08-31），但缺利用率證據，無法判讀產能過剩（`ai.compute_supply_demand`）。

**判讀：** R2 目前未見任何一家下修，要在窗口內成立需兩家在接下來的財報中下修指引；營收對 capex 缺口（約 105 vs 約 725）是長期壓力，但沒有證據顯示管理層已轉向收縮，屬遠端。

### R3 AI 信用事件

本次 AI 信用定價分歧掃描（14 日窗）未找到 AI 發行人債券利差、CDS 或評等動作的窗內報導，因此無法逐一列出符合 R3 規模門檻（負債 ≥ 50 億美元、AI 資料中心／算力主業）的借款人目前的信用定價或到期牆；這是本路徑的主要資料缺口。可用的相關證據：2026-09-08 Qualcomm 對 Amazon 發出約 4（USD bn）的認股權證，屬供應商對客戶的 vendor-financing-like 安排，列入 AI infrastructure debt financing / vendor-financing loops 的循環融資追蹤，並非違約或 distressed 訊號（`structural.ai_infrastructure_debt`）。整體信用環境：HY OAS 2.70%（+5 bps）、IG OAS 0.80%（−1 bp）（`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 −3 bps、SOFR99 較 IORB 高 5 bps、SRF 動用（Standing Repo Facility usage）為 0（`monetary.repo_stress_srf`）；銀行對 NBFI 放款 2027.9777（USD bn，約 $2.03T，2026-09-02，無新觀測）（`structural.nbfi_bank_loans`）。

**判讀：** 現有證據中沒有任何破產、付款違約或 distressed exchange 的跡象，整體信用利差處於緊縮水位；R3 在窗口內成立需先出現 AI 借款人利差顯著走闊或再融資失敗，目前未觀察到，屬遠端，但因 AI 信用定價資料缺席，本路徑的不確定性最高。

## 支持 yes 的證據

- [整體] CME FedWatch（2026-09-12）顯示 9/16 FOMC 升息 25 bps 的隱含機會約 85.5%，Fed funds 目前 3.50%–3.75%，CPI YoY 3.35%（2026-08 月資料）——在高估值下重啟緊縮是 R1 最直接的催化劑，也壓縮 Fed 對 AI 下跌的緩衝空間（`monetary.fedwatch`、`monetary.fed_funds`、`monetary.cpi_yoy`）。
- [R1] 10Y 殖利率 4.95%（2026-09-10，自 2026-09-03 起 +18 bps），10Y 實質殖利率 2.55%（+13 bps），10Y 期限溢價（term premium）0.8892%（2026-09-04，Kim-Wright）——折現率上行直接衝擊長存續期的 AI 股權估值（`monetary.dgs10`、`monetary.dfii10`、`monetary.term_premium`）。
- [R1] 估值與集中度極端：Shiller CAPE 約 40.73（2026-09-01），S&P 500 前十大權重約 38%（2026-09-01），S&P 500 高於 200 日均線 6.9%（2026-09-11）——下跌一旦啟動，幅度可能很大（`valuation.sp500_pe_cape`、`breadth.top10_concentration`、`valuation.sp500_trend`）。
- [R1] 避險需求升溫：VIX 17.84（2026-09-10，7 日 +24.58%），MOVE 82.21（2026-09-11，較 2026-09-03 +7.53），call skew 在第 91 百分位（2026-09-10）；WTI 97.26 美元（2026-09-09，+5.09%）加重通膨壓力（`structural.vix_spx_comove`、`structural.treasury_basis_trade`、`structural.cross_asset_derivatives`、`monetary.wti`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 105（USD bn，2026-08-17）vs 四大 hyperscaler 2026 capex 合計約 725（USD bn，2026-07-28，分母：top-4）；CNBC 2026-07-28 報導 Alphabet 財報後 capex 受更嚴格檢視——ROI 壓力是 R2 的潛在推力（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`）。
- [整體] 投機結構槓桿高：SPX 0DTE 佔比 8 月創紀錄約 62%（2026-08-31），單一個股槓桿 ETF 規模約 40.74（2026-09-08），8 月 OCC 總結算量約 1.44 十億口——下跌時可能放大賣壓（`structural.zero_dte`、`structural.leveraged_etf_aum`、`structural.options_volume`）。
- [R3] Qualcomm 對 Amazon 發出約 4（USD bn）認股權證（2026-09-08），屬供應商與客戶之間的 vendor-financing-like 循環安排，顯示 AI 基礎設施融資循環仍在擴大（`structural.ai_infrastructure_debt`）。

## 支持 no 的證據

- [R1] NASDAQ-100 最新收盤 29368.44（2026-09-11），距 52 週高點回撤 4.21%，R1 門檻水位 22995.45，需再跌約 21.70%——在基準率下 182 天內完成這種幅度的下跌並不常見（`valuation.ndx_drawdown`）。
- [R3] 信用市場未定價壓力：HY OAS 2.70%、IG OAS 0.80%（2026-09-10）；repo 資金壓力（SOFR−IORB）−3 bps、SRF 動用 0（2026-09-10／2026-09-11）——沒有 R3 前導的融資緊縮或利差走闊（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`）。
- [R2] 四大 hyperscaler 2026 capex 合計約 725（USD bn，2026-07-28），檢索結果無任何一家下修；Anthropic 年化 run-rate 約 65（USD bn，2026-08-17）顯示終端需求仍在成長——R2 需要兩家轉向，目前零家（`ai.hyperscaler_capex`、`ai.openai_anthropic_revenue`）。
- [整體] 情緒並非亢奮：CNN Fear & Greed 約 35（恐懼，2026-09-10），AAII 看多約 38.0%（2026-09-10），成分股在 200 日均線之上約 53%（2026-09-11），Mag 7 前瞻本益比低於 24（2026-08-03），equity put/call 約 0.67（2026-09-01）——缺少典型頂部的過度樂觀（`retail.fear_greed`、`retail.aaii`、`breadth.advance_decline`、`valuation.mag7_multiples`、`speculation.equity_put_call`）。
- [整體] 美債基差交易槓桿（Treasury basis-trade leverage）在漸進去化而非被迫平倉：CFTC 槓桿基金美債期貨淨部位 −6,863,118 口（2026-09-08），4 週淨空單縮減 387,809 口；10Y 標售 bid-to-cover 約 2.71（2026-09-09）；OFR tri-party repo transaction volume 2271.6（USD bn，2026-09-11）——未見國債市場失序（Treasury market dysfunction）的前兆（`structural.treasury_basis_trade`、`monetary.treasury_auctions`）。
- [整體] 投機篩查冷卻：+AI 改名／SPAC 7 日掃描 0 件、microcap moonshot 掃描 0 件、美國單一個股槓桿 ETF 30 日核准／上市 0 件（`speculation.ai_rename_spac`、`speculation.microcap_moonshots`、`structural.us_single_stock_etf`）。

## 與前期比較

前次結論：無前次預測（report-2026-09-03 為舊格式評分報告）

本次為新格式首份 yes/no 預測；舊格式評分不轉譯為 yes/no，flip_evidence 為 []。自 2026-09-03 以來的主要變化：

- 10Y 殖利率 +18 bps 至 4.95%、實質殖利率 +13 bps 至 2.55%（`monetary.dgs10`、`monetary.dfii10`）。
- S&P 500 較 2026-09-03 −1.17% 至 7656.98，VIX 由 14.32 升至 17.84（`valuation.sp500_trend`、`structural.vix_spx_comove`）。
- WTI 由 92.55 升至 97.26 美元（+5.09%）（`monetary.wti`）。
- SRF 動用由 0.033（USD bn）降至 0，repo 資金壓力未升溫（`monetary.repo_stress_srf`）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下 optional 來源為 ✗ NOT DISCLOSED（檢索完成但無合格窗內披露）：valuation.analyst_tp_decomposition、valuation.ai_credit_schism、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.private_credit_liquidity、ai.token_growth、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（quarterly_state 有 2026-07-28 背景值：增額債務佔 capex 約 32%，但 30 日 event_scan 無披露）、ai.depreciation_life、ai.capital_cycle、speculation.upcoming_ai_ipos、structural.global_leveraged_approvals。其中 valuation.ai_credit_schism 的缺席最可能影響結論：若 AI 借款人利差實際已顯著走闊，R3 路徑會比本次評估更近，答案可能轉向 yes。

其他說明：

- speculation.insider_form4 搜尋出一筆 Nvidia 相關 SEC EDGAR Form 4 結果（2026-09-02），但檢索結果未分別揭露交易日，未達「申報日＋交易日＋金額」的合格門檻，故按規則記為 0 件、不引用具名或金額。
- structural.treasury_basis_trade：搜尋結果紀錄註明 script 三區塊失敗，但本次 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 皆為 status ok，本報告以 artifact 為準並記 ✓ API；WebSearch 補充掃描無窗內基差平倉事件。
- ai.hyperscaler_capex 只取得四家合計值，逐家指引與方向缺失，R2 的逐家判讀因此不完整。

最大不確定性：

1. 9/16 FOMC：若如市場預期升息且釋出持續緊縮訊號，殖利率與估值壓力將推向 yes（R1）；若按兵不動或鴿派，則強化 no。
2. 下一輪 hyperscaler 財報：任何兩家下修 capex 指引即直接觸發 R2；若再度上修，則 R2 更遠，結論維持 no。
3. AI 基礎設施借款人的再融資：AI 信用定價資料缺席，若 neocloud 出現利差急升或再融資失敗，R3（並經傳導至 R1）將推向 yes。

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
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2 季資料，FRED 日期標記） | 48.2301354474（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限） | 3.75（%） | FRED API (series_id=DFEDTARU) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限） | 3.5（%） | FRED API (series_id=DFEDTARL) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.7（%） | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.8（%） | FRED API (series_id=BAMLC0A0CM) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.95（%） | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（較 2026-09-03） | 18.0（bps） | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.55（%） | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps（較 2026-09-03） | 13.0（bps） | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.36（%） | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 97.26（USD/bbl） | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO chg_pct（較 2026-09-03） | 5.09（%） | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-08 月資料） | 3.35（%） | FRED API (series_id=CPIAUCSL) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.32（%） | FRED API (series_id=T5YIFR) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8892（%） | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.62（%） | FRED API (series_id=SOFR) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.7（%） | FRED API (series_id=SOFR99) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65（%） | FRED API (series_id=IORB) | 2026-09-13 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用 transaction volume） | 0.0（USD bn） | FRED API (series_id=RPONTTLD) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6740619.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5912178.0（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（無新觀測） | 6446620.0（¥644.66T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 17.84 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（window 2026-09-03 → 2026-09-10） | 17.84 | FRED API (VIXCLS／SP500 共同時序) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 24.58（%） | FRED API (VIXCLS／SP500 共同時序) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -2.01（%） | FRED API (VIXCLS／SP500 共同時序) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（無新觀測） | 2027.9777（約 $2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六個 CBT 美債合約合計） | -6863118（口） | CFTC TFF (cftc_lev_funds) | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | 387809（口） | CFTC TFF (cftc_lev_funds) | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 82.21 | Yahoo chart API (move_index, ^MOVE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2271.6（USD bn） | OFR STFM (ofr_repo, REPO-TRIV1_TV_TOT-P) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（multpl / GuruFocus） | ✓ SEARCH-VERIFIED（CAPE；P/E 未見於結果） |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch（CNBC） | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED（無同季合格 TP 上修） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API（sp500_trend ok） |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API（ndx_drawdown ok） |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✗ NOT DISCLOSED（無窗內 AI 信用定價報導） |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch（24/7 Wall St） | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch（24/7 Wall St） | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch（condoredge，200 日均線之上比例） | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch（CNN） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（Advisor Perspectives，2026-07 月資料沿用） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch（AAII） | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API（BOGZ1FL153064486Q ok） |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok，無新觀測） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch（SteelOrbis 引 PBoC 數據） | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（CNBC，2026-07-28 財報季沿用） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch（Axios） | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch（Thunder Compute） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch（quarterly_state 沿用 2026-07-28；event_scan 30d 無披露） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch（Axios）＋ hyperscaler capex 分母 | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch（quarterly_state 與 30d event_scan 皆無披露） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch（7d 改名／SPAC 篩查） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（IPOScoop） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（Finviz、Benzinga、StockTitan、Yahoo movers） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d S-1／具名來源） | ✗ NOT DISCLOSED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR／WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch（ETF Action） | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR、ETF.com 新上市 feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d，KRX／TWSE／JPX／ESMA） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe insights） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（Traders Magazine 引 OCC） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch（CNBC） | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok，comove false） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（currentmarketvaluation） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API（無新觀測） |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py 三區塊＋WebSearch 補充掃描 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.73（原定來源 multpl / GuruFocus） | S&P 500 Shiller CAPE ratio current September 2026 multpl | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio （GuruFocus） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | Magnificent 7 forward P/E valuation September 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html （CNBC） | 2026-08-03 | 2026-09-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 至 7 月止 YTD 報酬約 13% | RSP equal weight vs SPY S&P 500 YTD performance September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/ （24/7 Wall St） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度約 38% | S&P 500 top 10 concentration percentage September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/ （24/7 Wall St） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 200 日均線之上約 53% | market breadth advance decline new highs lows September 2026 percent stocks above 200-day | https://condoredge.com/stocks/market-breadth （condoredge） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 35（恐懼） | CNN Fear and Greed Index today September 2026 reading | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）約 1.42 兆美元 | FINRA margin debt August 2026 record year over year | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026 （Advisor Perspectives，引 FINRA） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.0% | AAII sentiment survey results week September 10 2026 bullish bearish neutral | https://www.aaii.com/sentimentsurvey （AAII） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.71 | Treasury auction results September 2026 tail bid-to-cover 10-year | https://thevaultreport.com/treasury-auctions （The Vault Report） | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.fedwatch | 9/16 FOMC 升息 25 bps 隱含機會約 85.5%（原定來源 CME FedWatch） | CME FedWatch September 12 2026 probability 25 basis point hike | https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html （Yahoo Finance） | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.pboc | 2026 年 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate financing 2026 total social financing | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm （SteelOrbis） | 2026-08-15 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_capex | MSFT／GOOGL／AMZN／META 2026 capex 合計約 725（USD bn），2026-07 財報季 | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65（USD bn） | OpenAI Anthropic annualized revenue run rate September 2026 | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| ai.compute_supply_demand | H100 中位租金約 3.38 USD/hr | GPU rental price HBM DRAM contract price September 2026 utilization | https://www.thundercompute.com/blog/ai-gpu-rental-market-trends （Thunder Compute） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 增額債務佔 capex 約 32% | hyperscaler capex vs free cash flow debt issuance 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 105（USD bn；分母取 ai.hyperscaler_capex top-4 約 725） | AI revenue vs capex gap 2026 annualized run rate | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement September 7-13 2026 | 檢查來源：SPACInsider、Businesswire SPAC newsroom、Boardroom Alpha | — | 2026-09-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 22 檔 | IPO priced week September 8 2026 first day return debut | https://www.iposcoop.com/current-year-pricings/ （IPOScoop） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（0 件；Tenon +77%、AEON +35% 未達門檻） | biggest stock gainers week September 7 2026 microcap 100% quantum AI | 檢查來源：Finviz、Benzinga、StockTitan、Yahoo movers | — | 2026-09-13T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 14 日篩查（0 件合格：唯一結果缺分列交易日） | insider selling Form 4 September 2026 Nvidia AI executives SEC filing | 檢查來源：SEC EDGAR Form 4 搜尋結果 | — | 2026-09-13T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 約 0.67（日值或 5 日均值未標明） | Cboe equity put call ratio September 2026 reading | https://www.thetrading.tools/put-call-ratio （thetrading.tools） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.74 | leveraged ETF assets under management September 2026 record single stock | https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/ （ETF Action） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval September 2026 | 檢查來源：SEC EDGAR、ETF.com 新上市 feed | — | 2026-09-13T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比 8 月創紀錄約 62% | 0DTE options share SPX volume September 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august （Cboe） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.options_volume | OCC 8 月總結算量約 1.44 十億口 | OCC options volume August 2026 monthly report | https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/ （Traders Magazine） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 收在約 17 以上、call skew 第 91 百分位 | fear gauge VIX hedges September 10 2026 volatility | https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html （CNBC） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 1.42 兆美元（2026-07 月資料） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php （Current Market Valuation） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Qualcomm 對 Amazon 認股權證約 4（USD bn），vendor-financing-like 循環安排 | Qualcomm warrants Amazon 4 billion AI infrastructure deal September 2026 | https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html （CNBC） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |

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

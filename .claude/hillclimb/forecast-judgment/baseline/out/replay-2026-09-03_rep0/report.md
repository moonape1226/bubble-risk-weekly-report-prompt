> [DRY RUN] this report was not committed to archive.

# 2026-09-03 AI 泡沫破裂預測報告

報告日期：2026-09-03｜ISO 週次：2026-W36｜預測窗口：2026-09-03 → 2027-03-04｜前次基準：report-2026-08-31（3天前）

## 結論

**結論：no**

三條路徑目前都離觸發很遠：NASDAQ-100 距 52 週高點回撤 4.95%，還需再跌約 21.10% 才觸及 R1 門檻（`valuation.ndx_drawdown`）；HY OAS 2.65%、IG OAS 0.81% 與 repo 資金壓力（SOFR−IORB）1bp 顯示信用與資金面尚無 R3 所需的傳導（`monetary.hy_oas`、`monetary.repo_stress_srf`）。估值與槓桿顯示泡沫存在、下檔空間大，但本次證據中沒有足以在 182 天內完成任一路徑的催化劑。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,143.33（2026-09-02），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 4.95%；R1 門檻水位為 22,995.45，自最新收盤須再下跌約 21.10% 才會觸及（`valuation.ndx_drawdown`）。S&P 500 收 7,666.6（2026-09-02），高於 200 日均線 7.5%、高於 52 週均線 8.89%，自 2026-08-31 以來 −0.25%（`valuation.sp500_trend`）。VIX 由 2026-08-25 的 15.45 升至 2026-09-01 的 16.34（+5.76%），同期 S&P 500 −0.6%，屬一般的股跌波動升，不是 crowded-optionality 的同漲讀數（`structural.vix_spx_comove`）。估值端 Shiller CAPE 約 41.6（2026-08-31，`valuation.sp500_pe_cape`），家庭股票配置 45.76%（2026Q1，`retail.household_equity_allocation`），SPX 0DTE 占比 8 月創紀錄約 62%（`structural.zero_dte`）——脆弱度高，但這些是泡沫存在的證據，不是時點證據。

**判讀：** R1 距離遙遠（回撤僅 4.95%，門檻需再跌約 21%）。要在窗口內觸發，需要一個外生衝擊或 R3／R2 傳導（例如 AI 信用重定價或 hyperscaler 下修 capex 引發的集中度高的大型股拋售），本次證據中未見已啟動的此類催化劑。

### R2 資本支出收縮

本次取得的 capex 證據僅為四家合計：CNBC 2026-07-28 報導四大 hyperscaler 2026 capex 合計約 725（十億美元），文章脈絡為 Alphabet 財報後市場對 capex 的審視升溫（`ai.hyperscaler_capex`）。逐家狀態：

- Microsoft：本次證據未含個別最新指引數值與方向（未提供指引——本次未取得）。
- Alphabet：本次證據未含個別最新指引數值與方向（未提供指引——本次未取得）。
- Amazon：本次證據未含個別最新指引數值與方向（未提供指引——本次未取得）。
- Meta：本次證據未含個別最新指引數值與方向（未提供指引——本次未取得）。

已下修家數：本次證據中 0 家有可引證的下修。窗口（至 2027-03-04）涵蓋兩輪季報週期（日曆 Q3 與 Q4 財報），但具體財報日期不在本次證據內。需求側：Anthropic 年化 run-rate 約 $65bn（TechCrunch 2026-08-17，`ai.openai_anthropic_revenue`）；AI 營收對 capex 缺口（revenue-to-capex gap）以已追蹤組件組合為年化 AI 終端營收 ≈$65bn（分子：僅 Anthropic）vs 2026 capex ≈$725bn（分母：top-4，Oracle 未取得），缺口巨大但無前次組合值可判斷擴大或收斂（`ai.revenue_capex_gap`）。

**判讀：** R2 需要四家中兩家正式下修，這是季報事件驅動的路徑。本次沒有任何一家下修的證據，合計指引仍處於高位；要在窗口內觸發，需要 R1 式的股價壓力或融資成本上升迫使至少兩家在接下來兩輪財報中轉向。逐家指引缺漏是本路徑最大的資料不確定性。

### R3 AI 信用事件

候選借款人：本次證據中唯一出現的 AI 算力主業借款人是 CoreWeave，其 SEC 8-K 附件（2026-08-10）揭露完成約 $2.6bn 融資（`structural.ai_infrastructure_debt`）；其總負債規模、近期到期與再融資牆不在本次證據內，因此無法在此確認其是否落在 R3 的 ≥ 50 億美元門檻（僅能列為最可能的候選）。本次 AI 信用定價分歧（equity-vs-credit schism）掃描未找到 14 日內的 AI 發行人利差或 CDS 報導，hyperscaler 融資結構（capex vs FCF / 發債）的季頻狀態與 30 日事件掃描皆無披露，私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）亦無 30 日內披露——這些缺口記於資料缺漏段。廣義信用面：HY OAS 2.65%（2026-09-01，較 2026-08-31 +2bp，`monetary.hy_oas`）、IG OAS 0.81%（+1bp，`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）1bp、SOFR99−IORB 9bp、SRF 動用（Standing Repo Facility usage）0（SOFR／IORB／SOFR99 皆 2026-09-01，RPONTTLD 2026-09-02，`monetary.repo_stress_srf`）；銀行對 NBFI 放款約 $2.03T（2026-08-19，無新觀測，`structural.nbfi_bank_loans`）。

**判讀：** R3 目前沒有任何違約、寬限期、distressed exchange 或 going-concern 訊號；CoreWeave 仍能完成新融資，代表市場准入暢通。信用利差處於緊縮水位，需要先出現 AI 發行人利差明顯走闊或融資失敗，才可能在窗口內走到 R3。

## 支持 yes 的證據

- [整體] 估值與配置極端：Shiller CAPE 約 41.6（2026-08-31，`valuation.sp500_pe_cape`），S&P 500 高於 200 日均線 7.5%（2026-09-02，`valuation.sp500_trend`），家庭股票配置 45.76%（2026Q1，`retail.household_equity_allocation`）——一旦開始下跌，跌幅潛在很大。
- [R1] 槓桿與投機結構偏熱：SPX 0DTE 占比 8 月創紀錄約 62%（2026-08-31，`structural.zero_dte`），margin debt 約 $1.42T（2026-07 月資料，`retail.margin_debt`），Cboe SKEW 約 148.5 且股債相關偏正（2026-08-31，`structural.cross_asset_derivatives`），Arena Group 更名 Paradium.AI、2026-08-31 起以 PAAI 交易（`speculation.ai_rename_spac`）——放大下跌的機制存在。
- [R2] AI 營收對 capex 缺口巨大：已追蹤組件下年化 AI 終端營收 ≈$65bn（僅 Anthropic）對 2026 capex ≈$725bn（top-4）（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`），CNBC 2026-07-28 報導 Alphabet 財報後 capex 受到更高審視，回本壓力是 R2 的長期動因。
- [R1] 通膨與利率限制 Fed 緩衝空間：CPI YoY 3.3%（2026-07 月資料，`monetary.cpi_yoy`），WTI 91.48 美元、較 2026-08-31 +5.11%（2026-09-01，`monetary.wti`），10Y 殖利率 4.79%（+4bp，`monetary.dgs10`），10Y 期限溢價（term premium）0.8751%（2026-08-28，`monetary.term_premium`）——若 AI 帶頭回檔，降息托底的空間有限。
- [R3] AI 算力借款人持續加槓桿：CoreWeave 於 2026-08-10 揭露完成約 $2.6bn 融資（`structural.ai_infrastructure_debt`），AI infrastructure debt financing / vendor-financing loops 仍在累積。
- [整體] 波動率開始抬頭：VIX 7 日 +5.76% 至 16.34（2026-09-01，`structural.vix_spx_comove`），MOVE 由 75.32 升至 79.71（2026-09-02，`structural.treasury_basis_trade`）。

## 支持 no 的證據

- [R1] 距門檻極遠：NASDAQ-100 收 29,143.33（2026-09-02），距 52 週高點回撤 4.95%，須再跌約 21.10% 至 22,995.45 才觸發 R1（`valuation.ndx_drawdown`）。
- [R3] 信用面平靜：HY OAS 2.65%、IG OAS 0.81%（2026-09-01，`monetary.hy_oas`、`monetary.ig_oas`），CoreWeave 2026-08-10 仍完成約 $2.6bn 融資（`structural.ai_infrastructure_debt`），沒有任何違約或 distressed exchange 證據。
- [整體] 資金管線無壓力：repo 資金壓力（SOFR−IORB）1bp、SOFR99−IORB 9bp、SRF 動用 0（`monetary.repo_stress_srf`）；槓桿基金美債期貨淨空單由 2026-07-07 的 −7,573,044 口縮至 2026-08-25 的 −7,003,041 口（`structural.treasury_basis_trade`），OFR tri-party repo transaction volume 約 $2.31T 平穩，未見美債基差交易槓桿（Treasury basis-trade leverage）的失序式平倉。
- [R2] capex 沒有下修證據：四大 hyperscaler 2026 capex 合計約 725（十億美元，2026-07-28，`ai.hyperscaler_capex`），需求側 Anthropic 年化 run-rate 約 $65bn（2026-08-17，`ai.openai_anthropic_revenue`）仍在快速成長。
- [整體] 情緒並不亢奮：CNN Fear & Greed 33.8（恐懼，2026-09-02，`retail.fear_greed`），AAII 看多 32.9%（2026-08-28，`retail.aaii`），Mag 7 前瞻本益比低於 24（2026-08-03，`valuation.mag7_multiples`）——頂部常見的狂熱尚未出現。
- [整體] 基準率：任一 182 天窗口內 R1–R3 皆屬罕見事件，而本次證據沒有顯示任何路徑已經啟動（`valuation.ndx_drawdown`）。

## 與前期比較

前次結論：無前次預測（report-2026-08-31 為舊格式評分報告）

本次為新格式首次預測，flip_evidence 為空。自 2026-08-31 以來的 macro 變化（皆取自 macro artifact）：

- 10Y 殖利率 4.75% → 4.79%（ΔDGS10 +4bp，ΔDFII10 0bp，ΔT10YIE +3bp；判讀：不可判（視窗不一致），T10YIE 最新觀測為 2026-09-02，DGS10／DFII10 為 2026-09-01）（`monetary.dgs10`）。
- HY OAS 2.63% → 2.65%、IG OAS 0.80% → 0.81%（`monetary.hy_oas`、`monetary.ig_oas`）。
- WTI 87.03 → 91.48 美元（+5.11%，`monetary.wti`）；VIX 14.92 → 16.34（`structural.vix_spx_comove`）。
- S&P 500 7,686.14 → 7,666.6（−0.25%，`valuation.sp500_trend`）；WALCL、ECB、BOJ 資產負債表與銀行對 NBFI 放款皆無新觀測。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- breadth.rsp_spy：唯一搜尋結果為 2026-06-10 的 YTD 對比，非當期 snapshot，且此為 required 來源，故列 ⛔ FETCH FAILED。等權對市值權重的落差只影響廣度判讀，不涉及 R1–R3 任何解析條件，不會改變本次答案。

其他缺漏（✗ NOT DISCLOSED，非技術失敗）：AI 信用定價分歧（equity-vs-credit schism）、hyperscaler 融資結構兩個組件、私募信貸贖回壓力、資本週期階段、折舊年限變動、backlog 重複計算風險、AI compute 供需、美債標售需求、FedWatch、analyst TP 拆解、NAAIM、BofA／JPM 調查、社群情緒、全球槓桿產品核准、upcoming AI IPO、PBoC（搜尋僅指向 gov.cn 入口首頁，無可追溯的文章）、AI token growth（唯一結果為 2026-05-20，屬前一季）、equity put/call（唯一值為 2026-08-07，非當期）。R3 相關的兩個缺口（信用定價分歧與融資結構）是本次最可能遮蔽訊號的缺漏；若後續揭露 AI 發行人利差大幅走闊，會把答案推向 yes。insider Form 4 掃描中有一筆候選申報缺交易日欄位，依規則不納入，記為 0 件。另外：事前 evidence 表記載 basis-trade 三個 script block 失敗，但 macro artifact 顯示 cftc_lev_funds、move_index、ofr_repo 皆 status ok，本次以 artifact 為準記為 ✓ API。

主要不確定性：

1. R2 逐家 capex 指引缺漏：本次只有四家合計值，無法確認各家相較前次指引的方向；若下一輪財報出現兩家下修，答案直接轉為 yes。
2. R3 候選借款人的負債規模與再融資牆：CoreWeave 等 AI 算力借款人的總負債與到期分布不在本次證據內；若出現融資失敗或利差急升，會推向 yes。
3. 油價與利率衝擊：WTI 三天內 +5.11%、CPI 3.3%，若通膨再加速推高長端利率，可能成為 R1 的外生催化劑，推向 yes；反之若油價回落則維持 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7666.6 | FRED API (series_id=SP500) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 7.5 | FRED API (series_id=SP500) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.89 | FRED API (series_id=SP500) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29143.33 | FRED API (series_id=NASDAQ100) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-09-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.95 | FRED API (series_id=NASDAQ100) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1，% of financial assets） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-09-03T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（%） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（%） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.65 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.81 | FRED API (series_id=BAMLC0A0CM) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.79 | FRED API (series_id=DGS10) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.44 | FRED API (series_id=DFII10) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.34 | FRED API (series_id=T10YIE) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（美元/桶） | 91.48 | FRED API (series_id=DCOILWTICO) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料，%） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-09-03T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.33 | FRED API (series_id=T5YIFR) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 0.8751 | FRED API (series_id=THREEFYTP10) | 2026-08-28 | 2026-09-03T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.66 | FRED API (series_id=SOFR) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.74 | FRED API (series_id=SOFR99) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-09-03 | 2026-09-03T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,730,912（$6.73T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-26 | 2026-09-03T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,915,343（€5.92T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-28 | 2026-09-03T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,442,957（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-09-03T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.34 | FRED API (series_id=VIXCLS) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of；base_date 2026-08-25） | 16.34 | FRED fetch_macro block | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日 %） | 5.76 | FRED fetch_macro block | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日 %） | -0.6 | FRED fetch_macro block | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2026.2859（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-19 | 2026-09-03T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約合計，口） | -7003041 | CFTC TFF futures-only | 2026-08-25 | 2026-09-03T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 478000 | CFTC TFF futures-only | 2026-08-25 | 2026-09-03T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 79.71 | Yahoo chart API (^MOVE, unofficial) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2309.3（$2.31T） | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch → gurufocus（僅取得 CAPE，P/E 未取得） | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch → CNBC（前瞻 P/E；AI leader P/S 未取得） | ✓ SEARCH-VERIFIED（資料日 2026-08-03） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED（搜尋完成，無合格同季上調） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch（14d） | ✗ NOT DISCLOSED（搜尋完成，14 日內無合格報導） |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ⛔ FETCH FAILED（唯一結果為 2026-06-10 舊值，無當期 snapshot） |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch → Pensions & Investments | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch → StockCharts（以 50 日均線上方成分股比例為替代） | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch → CNN | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch → Advisor Perspectives（FINRA 7 月） | ✓ SEARCH-VERIFIED（YoY 與市值比未取得） |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch → AAII | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直接取得） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok；repo_stress status ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch | ✗ NOT DISCLOSED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✗ NOT DISCLOSED（結果僅為 gov.cn 入口首頁，無可追溯摘要） |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch → CNBC（僅四家合計，逐家未取得） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED（唯一結果 2026-05-20 屬前一季） |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch → TechCrunch（Anthropic；OpenAI 未取得） | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✗ NOT DISCLOSED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch：quarterly_state（stock_of_state）＋event_scan（30d），兩者皆無披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | 由已追蹤組件組合（Anthropic run-rate ÷ top-4 capex） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch：quarterly_state（stock_of_state）＋event_scan（30d），兩者皆無披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED（1 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch → Renaissance Capital | ✓ SEARCH-VERIFIED（僅 YTD 件數） |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（Finviz、Benzinga、StockTwits、Yahoo movers） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✗ NOT DISCLOSED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR / WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✗ NOT DISCLOSED（唯一值 2026-08-07，非當期） |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch → Benzinga（逐檔 AUM 未取得） | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR、ETF.com（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch → Cboe Insights | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch → OCC 月報（Mondo Visione） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch → thetrading.tools | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove block） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch → currentmarketvaluation（僅水位確認，比率未取得） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch → SEC EDGAR（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 41.6（原定來源 multpl / gurufocus） | shiller cape sp500 september 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio （GuruFocus） | 2026-08-31 | 2026-09-03T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24（原定來源 Mag 7 weighted P/E） | magnificent 7 forward pe august 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html （CNBC） | 2026-08-03 | 2026-09-03T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度約 37.6% | sp500 top 10 concentration 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/ （Pensions & Investments） | 2026-07-31 | 2026-09-03T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 50 日均線之上約 54%（A/D 替代；A/D ratio 與新高新低比未取得） | market breadth advance decline august 2026 | https://articles.stockcharts.com/article/mindfulinvestor-2026-08-weakening-market-breadth-could-signal-trouble-ahead/ （StockCharts） | 2026-08-27 | 2026-09-03T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 33.8（恐懼） | cnn fear greed index september 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）約 $1.42T | finra margin debt july 2026 | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026 （Advisor Perspectives，FINRA） | 2026-07-31 | 2026-09-03T09:30:00+08:00 |
| retail.aaii | AAII 看多 32.9% | aaii sentiment august 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-08-28 | 2026-09-03T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler（MSFT、GOOGL、AMZN、META）2026 capex 合計約 725（十億美元）；逐家指引未取得 | hyperscaler capex 2026 guidance | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-09-03T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 $65bn | anthropic annualized revenue august 2026 | https://techcrunch.com/2026/08/17/anthropics-annualized-revenue-surges-to-65b/ （TechCrunch） | 2026-08-17 | 2026-09-03T09:30:00+08:00 |
| ai.revenue_capex_gap | 組合值：分子 Anthropic ≈$65bn vs 分母 top-4 capex ≈$725bn（Oracle 未取得）；搜尋摘要中的「缺口約 105」無法由組件重現，未採用 | ai revenue vs capex 2026 | https://techcrunch.com/2026/08/17/anthropics-annualized-revenue-surges-to-65b/ （TechCrunch）＋ https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-08-17 | 2026-09-03T09:30:00+08:00 |
| speculation.ai_rename_spac | The Arena Group 更名 Paradium.AI，2026-08-31 起以 PAAI 交易（1 件） | arena group paradium.ai PAAI ticker august 2026 | https://www.businesswire.com/news/home/20260828769258/en/The-Arena-Group-dba-Paradium.AI-Completes-Name-Change-Will-Trade-Under-New-Stock-Ticker-PAAI-Effective-August-31-2026 （Business Wire） | 2026-08-31 | 2026-09-03T09:30:00+08:00 |
| speculation.ipo_heat | 美國 IPO YTD 約 105 件（週件數、首日報酬、無營收占比未取得） | ipo market 2026 renaissance capital | https://www.renaissancecapital.com/IPO-Center/Stats （Renaissance Capital） | 2026-08-28 | 2026-09-03T09:30:00+08:00 |
| speculation.microcap_moonshots | 7 日 microcap moonshot 掃描：0 件符合「2+ 主題×弱基本面」 | microcap moonshot quantum ai aug 27 sep 3 2026 | 檢查來源：Finviz、Benzinga、StockTwits、Yahoo movers（量子族群屬較大市值） | — | 2026-09-03T09:30:00+08:00 |
| speculation.insider_form4 | 14 日 Form 4 掃描：0 件合格（1 筆候選缺交易日欄位，依規則不納入） | nvidia mark stevens form 4 september 2026 | 檢查來源：SEC EDGAR Form 4、WebSearch | — | 2026-09-03T09:30:00+08:00 |
| structural.leveraged_etf_aum | 槓桿 ETF 總 AUM 約 198（原文數值；NVDL、TSLL、CONL、TQQQ、SOXL、SQQQ 逐檔未取得） | leveraged etf aum 2026 record | https://www.benzinga.com/etfs/broad-u-s-equity-etfs/26/08/61419951/leveraged-single-stock-etf-closures-went-from-3-to-63-in-a-year-as-money-piles-into-nvidia-bets （Benzinga） | 2026-08-15 | 2026-09-03T09:30:00+08:00 |
| structural.us_single_stock_etf | 30 日美國單一個股槓桿 ETF 核准／上市：0 件（新品為主題型 2x） | single stock leveraged etf launch aug 2026 | 檢查來源：SEC EDGAR、ETF.com（Leverage Shares 新品屬主題 2x） | — | 2026-09-03T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 占比 8 月創紀錄約 62% | spx 0dte share record august 2026 | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august （Cboe） | 2026-08-31 | 2026-09-03T09:30:00+08:00 |
| structural.options_volume | OCC 2026-07 期權日均約 71 百萬口 | occ july 2026 options volume | https://mondovisione.com/media-and-resources/news/occ-july-2026-monthly-volume-data-202686 （Mondo Visione，OCC） | 2026-07-31 | 2026-09-03T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 約 148.5；VIX 期限結構 contango；股債相關偏正 | vix skew term structure august 2026 | https://www.thetrading.tools/skew-index （thetrading.tools） | 2026-08-31 | 2026-09-03T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 水位約 $1.42T（交叉確認；市值比未取得） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php （Current Market Valuation） | 2026-07-31 | 2026-09-03T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave 完成約 $2.6bn 融資（SEC 8-K Ex. 99.1） | coreweave 2.6 billion loan covenant august 2026 | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000357/ex991pr.htm （SEC EDGAR） | 2026-08-10 | 2026-09-03T09:30:00+08:00 |

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
  "r1_drawdown_pct": 4.95,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

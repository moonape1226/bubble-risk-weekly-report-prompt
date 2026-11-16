> [DRY RUN] this report was not committed to archive.

# 2026-07-23 AI 泡沫破裂預測報告

報告日期：2026-07-23｜ISO 週次：2026-W30｜預測窗口：2026-07-23 → 2027-01-21｜前次基準：report-2026-07-20（3天前）

## 結論

**結論：no**

三條路徑目前都沒有進入完成段：NASDAQ-100 距 R1 門檻仍需再跌 20.70%，而 Alphabet 剛於 2026-07-22 將 FY26 capex 上修至約 $205B，R2 方向相反（`valuation.ndx_drawdown`、`ai.hyperscaler_capex`）。R3 方面，Oracle／CoreWeave CDS 走闊與 Blue Owl OCIC 的 gate proration / breach 是真實的後期壓力，但 HY OAS 2.69%、repo 資金面平靜、AI 資料中心垃圾債市場仍開放，窗口內出現 ≥ 50 億美元 AI 借款人違約的證據不足（`valuation.ai_credit_schism`、`monetary.hy_oas`）。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 28,998.1（2026-07-22），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 5.42%。R1 門檻水位 `r1_threshold_level` = 22,995.45；自最新收盤再下跌約 20.70% 才會觸及（`valuation.ndx_drawdown`）。同期 S&P 500 7,498.96（2026-07-22）仍高於 200 日均線 7.14%、高於 52 週均線 8.8%（`valuation.sp500_trend`）。脆弱度高：trailing P/E 28.85、Shiller CAPE 40.94（2026-07-22，`valuation.sp500_pe_cape`），FINRA margin debt $1.416T、YoY +53.7%（2026-05 月資料，`retail.margin_debt`），NAAIM 95.64（2026-07-15，`retail.naaim`）顯示部位擁擠。但短線情緒已冷卻而非亢奮：CNN Fear & Greed 41（Fear，2026-07-21，`retail.fear_greed`），VIX 16.64、MOVE 76.31 皆屬低波動區（`structural.vix_spx_comove`、`structural.treasury_basis_trade`），VIX／S&P 500 同漲訊號未觸發（7 日窗 S&P 500 −0.97%、VIX +6.19%，comove=false）。廣度偏弱：07-22 A/D 轉弱、新低多於新高（`breadth.advance_decline`），Top-10 集中度 36.40%（`breadth.top10_concentration`），但 RSP YTD +11.8% 領先 SPY +9.4%（`breadth.rsp_spy`），代表資金並非只擠在龍頭。

**判讀：** 距門檻仍有約 20.70% 的空間，屬遠端。要在窗口內完成，需要 R3 型信用事件或 hyperscaler 財報讓 capex／營收敘事急轉，觸發槓桿（margin debt YoY +53.7%、槓桿 ETF AUM 約 $198B，2026-07-10，`structural.leveraged_etf_aum`）被迫去化；單靠高估值不足以在 182 天內推過門檻。

### R2 資本支出收縮

- Alphabet：2026-07-22 Q2 財報將 FY26 capex 上修至約 $205B（上修），CNBC 彙整的 hyperscaler 2026 capex 合計約 $725B+（`ai.hyperscaler_capex`）。
- Microsoft、Amazon、Meta：本次證據未載明各自最新官方指引數值、日期與方向，記為「未提供指引」；不以記憶或估計補值。
- Amazon 於 2026-07-07 啟動 ≥ $25B 八檔期公司債用於 AI 基建（`ai.hyperscaler_financing_mix`），屬加碼而非收縮訊號；伺服器 DRAM 3Q26 合約價 +13–18% QoQ（2026-07-09，`ai.compute_supply_demand`）顯示供給端仍緊。
- 目前四家中已下修家數：0。下一輪財報日期本次證據未含；窗口（至 2027-01-21）涵蓋後續季度財報。

**判讀：** R2 距成立最遠——唯一有新資料的 Alphabet 是上修，且 hyperscaler 正以發債延續投資（hyperscaler 融資結構由 FCF 轉向發債）。需至少兩家在窗口內財報下修，通常要先有 R1 型市場衝擊或 AI 營收對 capex 缺口（約 $72B run-rate vs 約 $725B+ capex，`ai.revenue_capex_gap`）被市場懲罰才會出現。

### R3 AI 信用事件

- 信用定價：Oracle 5Y CDS 約 198bp 創紀錄、CoreWeave 5Y CDS 約 665bp（2026-07-20，`valuation.ai_credit_schism`）。CoreWeave 的利差水位已屬高收益／壓力區，AI 信用定價分歧（equity-vs-credit schism）正朝信貸端重定價方向發展。
- 新融資：Galaxy Digital 為 CoreWeave 承租的資料中心推出約 $3.5B 首發垃圾債（2026-07-22，`structural.ai_infrastructure_debt`），顯示市場仍願意承接 AI infrastructure debt financing，但融資品質下移到高收益級。
- 非銀行流動性：Blue Owl OCIC Q2 redemption-request ratio 18.8%，以 5% quarterly redemption cap 比例撥付（gate proration / breach，2026-07-02，`monetary.private_credit_liquidity`），報導亦指申請較前季緩和。
- 系統面：HY OAS 2.69%、IG OAS 0.78%（2026-07-21，持平，`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）−4bp、SOFR99−IORB +4bp、SRF 動用 0（`monetary.repo_stress_srf`）；銀行對 NBFI 放款約 $2.00T（2026-07-08，`structural.nbfi_bank_loans`）。
- 本次證據未見任何符合規模門檻借款人的付款違約、寬限期、covenant waiver、distressed exchange 或 going-concern 披露；近期到期牆資料本次未取得。

**判讀：** R3 是三條路徑中最接近的一條——CoreWeave CDS 約 665bp 與 OCIC 贖回壓力說明市場已開始為 AI 借款人違約定價，但「定價走闊」與「破產／違約／distressed exchange 完成」之間仍有距離：新垃圾債仍能發出、整體 HY 利差極窄、資金市場無失序。要推過門檻，需看到 CoreWeave 級借款人再融資失敗、主要客戶合約縮減，或高收益市場關門。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 約 665bp、Oracle 5Y CDS 約 198bp 創紀錄（2026-07-20），AI 借款人信用端已先於股權重定價 `valuation.ai_credit_schism`
- [R3] Blue Owl OCIC Q2 redemption-request ratio 18.8% 遠超 5% quarterly redemption cap，實際 gate proration / breach（2026-07-02） `monetary.private_credit_liquidity`
- [R3] CoreWeave 承租資料中心以約 $3.5B 垃圾債融資（2026-07-22），AI infrastructure debt financing 品質下移至高收益級，再融資依賴市場持續開放 `structural.ai_infrastructure_debt`
- [R1] FINRA margin debt $1.416T、YoY +53.7%（2026-05 月資料），高於歷史頂部附近的 +40–50% 區間；NAAIM 95.64（2026-07-15）部位擁擠 `retail.margin_debt` `retail.naaim`
- [R1] Shiller CAPE 40.94、trailing P/E 28.85（2026-07-22），S&P 500 仍高於 200 日均線 7.14%，下行空間大 `valuation.sp500_pe_cape` `valuation.sp500_trend`
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）：Anthropic 約 $47B＋OpenAI 約 $25B run-rate（2026-05-15 披露，沿用）對 hyperscaler 2026 capex 約 $725B+（分母：CNBC 彙整的 hyperscaler 合計，未單獨含 Oracle），缺口巨大 `ai.revenue_capex_gap`

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 5.42%（2026-07-22），需再跌約 20.70% 才觸及 R1 門檻 22,995.45 `valuation.ndx_drawdown`
- [R2] Alphabet 於 2026-07-22 將 FY26 capex 上修至約 $205B，hyperscaler 合計約 $725B+；四家中已下修 0 家 `ai.hyperscaler_capex`
- [R3] HY OAS 2.69%、IG OAS 0.78%（2026-07-21），信用市場整體未定價系統性違約，高收益市場仍能消化 AI 資料中心新債 `monetary.hy_oas` `monetary.ig_oas`
- [整體] repo 資金壓力（SOFR−IORB）−4bp、SOFR99−IORB +4bp、SRF 動用 0（2026-07-21／07-22），MOVE 76.31（2026-07-22），無國債市場失序跡象 `monetary.repo_stress_srf` `structural.treasury_basis_trade`
- [R2] Amazon 2026-07-07 發行 ≥ $25B 公司債支應 AI 基建，伺服器 DRAM 3Q26 合約 +13–18% QoQ（2026-07-09），供給鏈訊號仍為擴張而非消化 `ai.hyperscaler_financing_mix` `ai.compute_supply_demand`
- [R1] CNN Fear & Greed 41（Fear，2026-07-21）、VIX 16.64 且 VIX／S&P 500 同漲未觸發，情緒已部分降溫而非極端亢奮 `retail.fear_greed` `structural.vix_spx_comove`

## 與前期比較

前次結論：無前次預測（report-2026-07-20 為舊格式評分報告）

前次為舊格式六維評分報告，不轉譯為 yes/no；flip_evidence 為 []。自 2026-07-20 以來的主要變化：

- Alphabet Q2 財報（2026-07-22）capex 上修至約 $205B，R2 路徑更遠。
- Galaxy Digital 約 $3.5B CoreWeave 資料中心垃圾債（2026-07-22）：AI 融資仍可取得，但信用品質下移。
- NASDAQ-100 自 28,604.23（07-20）回升至 28,998.1（07-22）；S&P 500 +0.75%；VIX 由 18.65 降至 16.64，MOVE 由 72.66 升至 76.31。
- 10Y 殖利率 +3bp 至 4.63%，HY／IG OAS 持平。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED 來源（檢索完成、無合格當期披露）：retail.social_sentiment、institutional.bofa_jpm_survey、ai.token_growth、ai.openai_anthropic_revenue（最近披露為 2026-05-15，屬前一季，僅作背景）、ai.customer_concentration_rpo、ai.depreciation_life、ai.capital_cycle（quarterly_state 與 event_scan 皆無可引證資料）、structural.global_leveraged_approvals。其中 backlog 重複計算風險（RPO double-counting）與資本週期階段的缺漏若補上可能加強 R2／R3 的 yes 論證，但在 R1／R2 距門檻甚遠的情況下不足以單獨改變結論。

資料品質注意：valuation.mag7_multiples（Mag 7 加權 P/E 約 40，資料日 2026-05-15）與 structural.zero_dte（0DTE 佔 SPX 約 63%，2026-02-28）為本次能取得的最近 snapshot，日期偏舊，僅作背景、未作關鍵證據。speculation.insider_form4 的 EDGAR 一手 URL 無法取得，依規則以 0 件處理，不引用任何具名內部人交易。10Y Δ 分解：ΔDGS10 +3bp、ΔDFII10 +2bp、ΔT10YIE +3bp，判讀 `不可判（視窗不一致）`。

最大不確定性：

1. CoreWeave 等 AI 資料中心借款人的再融資路徑：CDS 約 665bp 已屬壓力區，若高收益市場對 AI 資料中心債關門或主要客戶承諾縮減，R3 可能在窗口內完成並連帶觸發 R1——此項會把答案推向 yes。
2. Microsoft、Amazon、Meta 的下一次 capex 指引：本次證據未含其最新數值與財報日期；若兩家在窗口內下修，R2 直接成立（推向 yes），若延續上修則強化 no。
3. 私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）是否擴散：OCIC 已出現 gate proration / breach，若多基金 redemption-request ratio 同步上升或出現 net inflow→outflow flip，將壓縮 AI 借款人的非銀行融資管道（推向 yes）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7498.96 | FRED API (series_id=SP500) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 7.14 | FRED API (series_id=SP500) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.8 | FRED API (series_id=SP500) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28998.1 | FRED API (series_id=NASDAQ100) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-23T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 5.42 | FRED API (series_id=NASDAQ100) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1，家庭股票佔金融資產 %） | 45.76 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-23T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.69 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.63 | FRED API (series_id=DGS10) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（vs 2026-07-20） | 3.0 | FRED API (series_id=DGS10) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.37 | FRED API (series_id=DFII10) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.28 | FRED API (series_id=T10YIE) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD／桶） | 84.38 | FRED API (series_id=DCOILWTICO) | 2026-07-20 | 2026-07-23T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料，%） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-23T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.26 | FRED API (series_id=T5YIFR) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 0.7787 | FRED API (series_id=THREEFYTP10) | 2026-07-17 | 2026-07-23T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.61 | FRED API (series_id=SOFR) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.69 | FRED API (series_id=SOFR99) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-07-23 | 2026-07-23T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,743,028（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-15 | 2026-07-23T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,949,077（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-17 | 2026-07-23T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,395,509（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-23T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.64 | FRED API (series_id=VIXCLS) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of，base_date 2026-07-15，window_days 7，comove=false） | 16.64 | FRED API (series_id=VIXCLS, SP500) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（%） | 6.19 | FRED API (series_id=VIXCLS) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（%） | −0.97 | FRED API (series_id=SP500) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2004.0237（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-08 | 2026-07-23T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7562874 | CFTC TFF futures-only | 2026-07-14 | 2026-07-23T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -78139 | CFTC TFF futures-only | 2026-07-14 | 2026-07-23T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 76.31 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2334.5 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | MarketXLS WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-05-15，偏舊，僅背景） |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方 TP 調整 WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | portfolioslab WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | MacroMicro WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA／Advisor Perspectives WebSearch（月頻沿用） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／MacroMicro [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok、DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | RTTNews WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要 WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok、JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Xinhua WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報／CNBC WebSearch | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／The Information WebSearch | ✗ NOT DISCLOSED（無當季披露；最近為 2026-05-15） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話 WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報 quarterly_state＋30d 發債 event_scan WebSearch | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 WebSearch（季頻沿用） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K／10-Q WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速 quarterly_state＋30d 進出場 event_scan WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | Businesswire／StockTitan WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／Benzinga／StockTwits WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR／openinsider（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | YCharts WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com／新聞 WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF.com WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-02-28，偏舊，僅背景） |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe／Velox WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok、vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用散戶 margin debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo） | ✓ API（cftc_lev_funds ok、move_index ok、ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 28.85（原定來源 multpl） | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 40.94（原定來源 multpl） | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E 約 40 trailing | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026 （MarketXLS） | 2026-05-15 | 2026-07-23T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標 $288（約 22× EPS，target PE 未擴張，EPS 主導；舊 TP 未披露） | Morgan Stanley NVDA target 288 July 2026 EPS | https://www.gurufocus.com/news/8955458/morgan-stanley-upgrades-nvidia-nvda-with-a-288-target-price （GuruFocus） | 2026-07-13 | 2026-07-23T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5Y CDS 約 198bp 創紀錄、CoreWeave 約 665bp | Oracle CoreWeave CDS spread record July 2026 | https://bondblox.com/news/oracles-5y-cds-spread-hits-all-time-highs （BondbloX） | 2026-07-20 | 2026-07-23T09:30:00+08:00 |
| breadth.rsp_spy | RSP +11.8% vs SPY +9.4% YTD | RSP vs SPY equal weight YTD 2026 | https://portfolioslab.com/tools/stock-comparison/RSP/SPY （PortfoliosLab） | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 36.40% | S&P 500 top 10 concentration percent 2026 | https://en.macromicro.me/collections/34/us-stock-relative/123442/us-sp-500-top-10-companies-total-market-cap-and-share （MacroMicro） | 2026-07-02 | 2026-07-23T09:30:00+08:00 |
| breadth.advance_decline | 07-22 A/D 轉弱、新低多於新高 | NYSE breadth advance decline July 22 2026 | https://ts2.tech/en/nasdaq-ends-flat-as-market-breadth-remains-thin-ahead-of-big-tech-earnings/ （TS2） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 41（Fear）（原定來源 cnn.com） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/series/22748/cnn-fear-and-greed （MacroMicro） | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt $1.416T、YoY +53.7%（2026-05 月資料，沿用） | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives） | 2026-05-31 | 2026-07-23T09:30:00+08:00 |
| retail.aaii | AAII Bull 44.9% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-15 | 2026-07-23T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64 | NAAIM exposure index latest July 2026 | https://en.macromicro.me/series/20540/naaim-exposure-index （MacroMicro） | 2026-07-15 | 2026-07-23T09:30:00+08:00 |
| monetary.treasury_auctions | 20Y 標售 bid-to-cover 2.64、小幅 tail | US Treasury 20Y auction July 2026 bid to cover | https://www.rttnews.com/3669412/twenty-year-bond-auction-attracts-average-demand.aspx （RTTNews） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 FOMC 約 83.4% 持平 | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch （CryptoRank 轉述 CME） | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://english.news.cn/20260714/2d460c4227c244f1bf930993be469262/c.html （Xinhua） | 2026-07-14 | 2026-07-23T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio 18.8%，5% quarterly redemption cap 比例撥付 | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://www.investing.com/news/stock-market-news/blue-owl-keeps-5-redemption-caps-as-ocic-requests-ease-from-prior-quarter-4773280 （Investing.com） | 2026-07-02 | 2026-07-23T09:30:00+08:00 |
| ai.hyperscaler_capex | Alphabet FY26 capex 上修至約 $205B；hyperscaler 2026 capex 合計約 $725B+ | hyperscaler capex 2026 Alphabet raised 205B Q2 | https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html （CNBC） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 +13–18% QoQ | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260709-13140.html （TrendForce） | 2026-07-09 | 2026-07-23T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] Alphabet FY26 capex 上修至約 $205B、發債佔比上升 | Alphabet capex 205B Q2 2026 debt financing | https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html （CNBC） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] Amazon 啟動 ≥ $25B 八檔期公司債（AI 基建，資產負債表內發債） | Amazon 25 billion bond offering AI data center July 2026 | https://finance.yahoo.com/technology/ai/articles/bond-issuance-backing-ai-investment-135635215.html （Yahoo Finance） | 2026-07-07 | 2026-07-23T09:30:00+08:00 |
| ai.revenue_capex_gap | 分子：Anthropic 約 $47B＋OpenAI 約 $25B run-rate（沿用） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-05-15 | 2026-07-23T09:30:00+08:00 |
| ai.revenue_capex_gap | 分母：hyperscaler 2026 capex 合計約 $725B+（取自 capex guidance bullet） | hyperscaler capex 2026 Alphabet raised 205B Q2 | https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html （CNBC） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| speculation.ai_rename_spac | 2026-07-16 至 07-23 合格 +AI 改名／SPAC 件數 0 | AI rename ticker change SPAC July 16-23 2026 | Businesswire／StockTitan movers screener | — | 2026-07-23T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD 約 203 檔 IPO、募資 $141.2B | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/ （StockAnalysis） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot 件數 0 | microcap 100% single day quantum AI fusion moonshot July 2026 | Finviz／Benzinga／StockTwits movers screener | — | 2026-07-23T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 程序，估值 $965B，可能 10 月掛牌 | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html （CNBC） | 2026-07-15 | 2026-07-23T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 cluster 件數 0（EDGAR 一手 filing URL 無法取得，不引用具名交易） | insider Form 4 cluster AI leaders July 2026 openinsider | SEC EDGAR／openinsider | — | 2026-07-23T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.65（日讀數） | Cboe equity put call ratio July 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio （YCharts） | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 約 $198B（個別 NVDL／TSLL／CONL／TQQQ／SOXL／SQQQ 未拆分） | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing） | 2026-07-10 | 2026-07-23T09:30:00+08:00 |
| structural.us_single_stock_etf | GraniteShares 推出首檔美掛 SK hynix 2x 多／空 ETF | single-stock leveraged ETF launch July 2026 GraniteShares SK hynix | https://www.globenewswire.com/news-release/2026/07/14/3326857/0/en/GraniteShares-Launches-the-First-U-S-Listed-Leveraged-ETFs-on-SK-hynix.html （GlobeNewswire） | 2026-07-14 | 2026-07-23T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 成交約 63% | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/volatility-insights-evaluating-the-market-impact-of-spx-0-dte-options/ （Cboe） | 2026-02-28 | 2026-07-23T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月 1,603,491,559 口、YoY +45% | OCC monthly options volume June 2026 | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/monthly-weekly-volume-statistics （OCC） | 2026-07-02 | 2026-07-23T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 146.05、VIX 約 18.7 contango | VIX term structure SKEW July 2026 | https://veloxmacro.com/how-to-read-the-vix-week-ending-july-20-2026/ （Velox Macro） | 2026-07-20 | 2026-07-23T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt $1.416T、YoY +53.7%（2026-05 月資料，交叉引用散戶 margin debt） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives） | 2026-05-31 | 2026-07-23T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Galaxy Digital 約 $3.5B CoreWeave 承租資料中心首發垃圾債 | Galaxy Digital 3.5 billion junk bond CoreWeave data center July 2026 | https://www.bloomberg.com/news/articles/2026-07-22/coreweave-backed-data-center-plans-3-5-billion-junk-bond-sale （Bloomberg） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-07-23",
  "iso_week": "2026-W30",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-01-21",
  "prior_date": "2026-07-20",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 5.42,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

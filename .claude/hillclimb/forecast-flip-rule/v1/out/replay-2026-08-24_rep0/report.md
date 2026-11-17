> [DRY RUN] this report was not committed to archive.

# 2026-08-24 AI 泡沫破裂預測報告

報告日期：2026-08-24｜ISO 週次：2026-W35｜預測窗口：2026-08-24 → 2027-02-22｜前次基準：report-2026-08-20（4天前）

## 結論

**結論：no**

三條路徑都離解析門檻很遠：NASDAQ-100 距 52 週高點回撤 4.41%，還需再跌約 21.54% 才觸及 R1；hyperscaler 2026 capex 合計 ≈$725bn、年增 ≈77%，本次未見任何一家下修（R2）；HY OAS 2.75%、IG OAS 0.82% 等信用指標仍緊，且無 AI 借款人違約或 distressed exchange 跡象（R3）。估值與槓桿顯示泡沫存在、下行空間大，但窗口內缺少已啟動的觸發與傳導證據，因此不足以推翻「182 天內不破裂」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,308.86（2026-08-21），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 4.41%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，自最新收盤還需再跌約 21.54% 才觸及。S&P 500 最新 7,674.37（2026-08-21），較前次基準日（2026-08-20）+0.43%，高於 200 日 MA 8.15%、高於 52 週 MA 9.61%（`valuation.sp500_trend`），顯示價格延伸偏高但無崩跌動能。VIX 16.01（2026-08-20），trailing 7 日（2026-08-13 → 2026-08-20）VIX +9.43%、S&P 500 −2.02%，屬正常的反向變動，未觸發 crowded-optionality 同漲讀數（`structural.vix_spx_comove`）。估值端 Shiller CAPE ≈41.2、trailing P/E ≈26.2（2026-08-20，`valuation.sp500_pe_cape`），Mag 7 加權 P/E ≈29.5x（2026-08-14，`valuation.mag7_multiples`）。

**判讀：** R1 距門檻仍有約 21.54% 的跌幅空間，現況不在進行中；要在窗口內成立，需要一個能引發 AI 權值股集中拋售的催化劑，例如 hyperscaler 財報季 capex 意外轉向、Anthropic 預計 10 月的大型 IPO 帶來的供給衝擊、或信用／利率端急速重定價，並經高槓桿 ETF 與 0DTE 部位放大。

### R2 資本支出收縮

本次取得的 `ai.hyperscaler_capex` 證據為 2026 Q2 財報季後的彙整：Microsoft、Alphabet、Amazon、Meta 四家 2026 capex 合計 ≈$725bn、年增 ≈77%（2026-08-13）。這份證據沒有逐家列出最新指引數字，因此四家各自相對前次正式指引的方向（上修／持平／下修）本次無法逐家引證；但證據中未見任何一家下修的披露，已下修家數按本次證據計為 0 家（R2 需要至少 2 家）。需求端仍強：OpenAI run-rate ≈$40B、Anthropic ≈$65B（2026-08-17，`ai.openai_anthropic_revenue`），GPU 現貨租金高於合約價 2 倍以上、產能被利用率吸收（2026-08-13，`ai.compute_supply_demand`）。下一輪（2026 Q3）與再下一輪（2026 Q4）財報都落在窗口內，確切日期本次未取得。

**判讀：** R2 目前沒有任何下修跡象；在需求與定價仍強、合計 capex 仍以 ≈77% 年增的情況下，窗口內出現兩家下修需要需求端明顯轉弱（利用率下滑、GPU 租金崩落）或 R1 式股價重挫迫使管理層收手，現有證據都不支持這種轉折。

### R3 AI 信用事件

本次 AI 信用定價分歧（equity-vs-credit schism）與 AI infrastructure debt financing / vendor-financing loops 的 14／30 日掃描都完成，但沒有找到合格的當期披露（未見 AI 發行人利差／CDS 走闊、也未見新的 neocloud 融資或困境事件），因此無法對符合 R3 規模門檻的個別借款人給出當期信用定價、到期牆或困境訊號。可用的整體信用水位：HY OAS 2.75%、IG OAS 0.82%（2026-08-20，`monetary.hy_oas`、`monetary.ig_oas`），處於極緊水準；repo 資金壓力（SOFR−IORB）為 −2bp、SOFR99−IORB 為 +6bp（SOFR／SOFR99／IORB 皆取 2026-08-20），SRF 動用（Standing Repo Facility usage）0（2026-08-21，`monetary.repo_stress_srf`）；銀行對 NBFI 放款 $2.03T（2026-08-12，`structural.nbfi_bank_loans`）。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）的 30 日掃描也無合格披露。

**判讀：** R3 沒有任何正在進行的違約、寬限期或 distressed exchange 訊號，整體信用利差緊、短端資金無壓力；要在窗口內成立，需要某家高負債 neocloud／AI 資料中心借款人出現客戶合約流失或再融資失敗，而本次缺少個別發行人層級的資料，這是 R3 判讀最大的盲點。

## 支持 yes 的證據

- [整體] 估值處於極端區：Shiller CAPE ≈41.2、trailing P/E ≈26.2（2026-08-20，`valuation.sp500_pe_cape`），Mag 7 加權 P/E ≈29.5x（2026-08-14，`valuation.mag7_multiples`），一旦催化劑出現，下跌空間大。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）大：已披露年化 AI 終端營收 ≈$105bn（OpenAI ≈40＋Anthropic ≈65）vs 年化 capex ≈$725bn（分母：top-4 hyperscaler，Oracle 本次無可組合數字），營收僅約 capex 的 14%（2026-08-17，`ai.revenue_capex_gap`）；若回本預期鬆動，capex 指引有下修壓力。
- [R1] 槓桿與投機部位擁擠：美股槓桿 ETF 總 AUM ≈$198bn 創紀錄、TQQQ ≈$31.3bn、SOXL ≈$17.3bn（2026-08-17，`structural.leveraged_etf_aum`）；SPX 0DTE 佔比 ≈62.4% 創紀錄（2026-08-14，`structural.zero_dte`）；margin debt（2026-07）YoY ≈+38.6%（`retail.margin_debt`），接近歷史頂部常見的 +40–50% 區間；這些部位會放大任何回撤。
- [R1] 大型 AI IPO 的供給衝擊：Anthropic 目標 10 月 IPO、估值 ≈$2T（2026-08-17，`speculation.upcoming_ai_ipos`），落在窗口內，可能吸走 AI 權值股資金。
- [整體] 利率端對 Fed 緩衝不利：CPI YoY 3.3%（2026-07，`monetary.cpi_yoy`），FedWatch 9/16 按兵不動 ≈68.4%、尾端定價為升息（2026-08-20，`monetary.fedwatch`），10Y 期限溢價（term premium）0.8393%、trailing 7 日 +1.4bp（2026-08-14，`monetary.term_premium`）；若 AI 股回撤，貨幣政策託底空間有限。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.41%（2026-08-21），R1 門檻水位 22,995.45，仍需再跌約 21.54%（`valuation.ndx_drawdown`）；S&P 500 仍高於 200 日 MA 8.15%（`valuation.sp500_trend`）。
- [R2] hyperscaler capex 仍在擴張：top-4 2026 capex 合計 ≈$725bn、年增 ≈77%，本次證據未見任何一家下修（2026-08-13，`ai.hyperscaler_capex`）；需求端 GPU 現貨租金 > 2× 合約價、產能被利用率吸收（`ai.compute_supply_demand`），OpenAI ≈$40B、Anthropic ≈$65B run-rate（`ai.openai_anthropic_revenue`）。
- [R3] 信用市場沒有壓力：HY OAS 2.75%（`monetary.hy_oas`）、IG OAS 0.82%（`monetary.ig_oas`），皆為 2026-08-20；SOFR−IORB −2bp、SRF 動用 0（`monetary.repo_stress_srf`）；MOVE 73.4（2026-08-21），CFTC 槓桿基金美債期貨淨空單 4 週縮減 244,468 口（`structural.treasury_basis_trade`）。
- [整體] 情緒未達狂熱：CNN Fear & Greed 55（Greed，2026-08-21，`retail.fear_greed`），AAII 偏多 35.5%、偏空 39.9%（`retail.aaii`），Cboe equity put/call 0.52（`speculation.equity_put_call`）；廣度改善，RSP 領先 SPY YTD ≈5pp（`breadth.rsp_spy`）；margin debt MoM −5.7%（`retail.margin_debt`）。
- [整體] 投機篩選全數落空：+AI 改名／SPAC（`speculation.ai_rename_spac`）、microcap moonshot（`speculation.microcap_moonshots`）、14 日內 Form 4 集中賣出（`speculation.insider_form4`）皆 0 件；2026 YTD IPO ≈232 件且無單週無營收 AI IPO 暴衝（2026-08-21，`speculation.ipo_heat`）。

## 與前期比較

前次結論：無前次預測（report-2026-08-20 為舊格式評分報告）

前次為舊格式評分報告，不轉譯為 yes／no；flip_evidence 為 []。與 2026-08-20 相比的主要數據變化：

- S&P 500 由 7,641.16 升至 7,674.37（+0.43%）；NASDAQ-100 收盤 29,308.86，距 52 週高點回撤 4.41%。
- 10Y 分解無變動：ΔDGS10、ΔDFII10、ΔT10YIE 皆 0bp；DGS10、DFII10 無新觀測（partial stale），T10YIE 已更新。HY／IG OAS、SOFR、VIX 也無新觀測，讀為持平。
- 新出現的事件型證據：Anthropic ≈$65B run-rate 披露與 10 月 IPO 目標（≈$2T 估值，2026-08-17），都屬需求強勁的方向，不構成路徑啟動證據。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源檢索完成但無合格當期披露（✗ NOT DISCLOSED），僅說明缺口影響：

- `valuation.ai_credit_schism`、`structural.ai_infrastructure_debt`：R3 的個別發行人信用定價與新融資事件缺席，是最可能改變答案的缺口；若存在未被捕捉的 neocloud 利差急升或再融資困難，R3 會比本次判讀更近。
- `ai.hyperscaler_financing_mix`、`ai.capital_cycle`：季度狀態可用（capex > FCF、發債擴張；供給 capex +77%），但 30 日事件掃描無披露；`ai.depreciation_life`、`ai.customer_concentration_rpo` 無披露，影響盈餘品質判讀，短期不太可能改變答案。
- `ai.token_growth`：唯一取得的結果為 Anthropic run-rate 年增 ≈7×，屬營收而非 token 用量指標，故未採用。
- `monetary.private_credit_liquidity`、`retail.naaim`、`retail.social_sentiment`、`institutional.bofa_jpm_survey`、`monetary.pboc`、`valuation.analyst_tp_decomposition`、`structural.global_leveraged_approvals`：輔助性來源，缺席不太可能翻轉答案。

主要不確定性：

1. 2026 Q3 hyperscaler 財報（窗口內）：若兩家以上 capex 指引轉為下修，R2 直接成立並可能連動 R1，會推向 yes；目前資料指向持續上修。
2. Anthropic 10 月 IPO（≈$2T 估值）：若定價／首日表現失利，可能觸發 AI 權值股重定價，推向 yes；若順利則強化 no。
3. 通膨與 Fed 路徑：CPI 3.3%、FedWatch 尾端為升息；若升息定價擴大，估值壓縮加上槓桿部位平倉可能放大 R1，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7674.37 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日 MA） | 8.15（%） | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週 MA） | 9.61（%） | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較前次基準） | 0.43（%） | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（NASDAQ-100 收盤） | 29308.86 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤） | 4.41（%） | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1 季資料） | 45.76080873390133（≈45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75（%） | FRED API (series_id=DFEDTARU) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5（%） | FRED API (series_id=DFEDTARL) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.75（%） | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.82（%） | FRED API (series_id=BAMLC0A0CM) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.69（%） | FRED API (series_id=DGS10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.35（%） | FRED API (series_id=DFII10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.34（%） | FRED API (series_id=T10YIE) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 86.48（USD） | FRED API (series_id=DCOILWTICO) | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料） | 3.3（%） | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.34（%） | FRED API (series_id=T5YIFR) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8393（%） | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 日） | 1.4（bp） | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.63（%） | FRED API (series_id=SOFR) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.71（%） | FRED API (series_id=SOFR99) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65（%） | FRED API (series_id=IORB) | 2026-08-24 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用） | 0.0（十億美元） | FRED API (series_id=RPONTTLD) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6745699.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5927307.0（€5.93T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.01 | FRED API (series_id=VIXCLS) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 16.01 | fetch_macro.py 衍生區塊（FRED 波動率×SP500） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（trailing 7 日） | 9.43（%） | fetch_macro.py 衍生區塊（FRED 波動率×SP500） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（trailing 7 日） | -2.02（%） | fetch_macro.py 衍生區塊（FRED 波動率×SP500） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2026.1422（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-12 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位） | -7218048（口） | CFTC TFF futures-only | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | 244468（口） | CFTC TFF futures-only | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.4 | Yahoo Finance chart API (^MOVE) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2328.6（十億美元） | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值 / S&P 500 P/E and Shiller CAPE | multpl / GuruFocus，WebSearch 主路徑 | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值 / Mag 7 weighted P/E and AI leader P/S | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值 / Analyst TP upgrade decomposition | 賣方摘要 WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | 估值 / S&P 500 price-trend deviation | fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值 / NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值 / AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✗ NOT DISCLOSED |
| breadth.rsp_spy | 廣度 / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度 / Top-10 concentration in S&P 500 | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度 / Advance/decline ratio, new high/low ratio | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶 / CNN Fear & Greed Index | CNN，WebSearch 主路徑 | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶 / Margin Debt: FINRA monthly data | FINRA / GuruFocus WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶 / Retail survey: AAII Investor Sentiment | AAII，WebSearch 主路徑 | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶 / Social sentiment proxies | WSB / X WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶 / Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶 / NAAIM Exposure Index | naaim.org WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | 機構 / BofA Fund Manager Survey and JPM institutional survey | BofA / JPM WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣 / Fed funds rate: FRED series DFEDTARU and DFEDTARL | fetch_macro.py（FRED API） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣 / High Yield OAS | fetch_macro.py（FRED API） | ✓ API |
| monetary.ig_oas | 貨幣 / Investment Grade OAS | fetch_macro.py（FRED API） | ✓ API |
| monetary.dgs10 | 貨幣 / 10Y Treasury yield | fetch_macro.py（FRED API） | ✓ API |
| monetary.dfii10 | 貨幣 / 10Y Treasury real yield / TIPS | fetch_macro.py（FRED API） | ✓ API |
| monetary.t10yie | 貨幣 / 10Y breakeven inflation rate | fetch_macro.py（FRED API 直接取得） | ✓ API |
| monetary.wti | 貨幣 / WTI crude oil price | fetch_macro.py（FRED API） | ✓ API |
| monetary.cpi_yoy | 貨幣 / CPI YoY: FRED series CPIAUCSL | fetch_macro.py（FRED API，yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣 / 5y5y forward inflation expectation | fetch_macro.py（FRED API） | ✓ API |
| monetary.term_premium | 貨幣 / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | fetch_macro.py（FRED API） | ✓ API |
| monetary.repo_stress_srf | 貨幣 / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | fetch_macro.py repo_stress（FRED API） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣 / 美債標售需求（auction tail / bid-to-cover） | TreasuryDirect / Reuters WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣 / Fed funds rate path expectations | CME FedWatch 摘要 WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣 / Fed balance sheet: FRED series WALCL | fetch_macro.py（FRED API） | ✓ API |
| monetary.ecb_boj | 貨幣 / Global central bank liquidity cross-check — ECB / BOJ | fetch_macro.py（FRED API） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣 / PBoC aggregate financing / liquidity operations | PBoC / NBS WebSearch | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | 貨幣 / Private-credit / non-bank fund liquidity stress | BDC／interval fund 披露 WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | 財報摘要 WebSearch（stock-of-state，沿用 Q2 財報季） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI / AI token volume growth rate | 供應商披露 WebSearch（僅得營收 run-rate，無 token 用量指標） | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | CNBC 等 WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | 產業披露 WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch；quarterly_state 沿用最新季、event_scan 30 日掃描無披露 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口（revenue-to-capex gap） | 綜合披露 WebSearch（分母 top-4） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K / 10-Q WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI / 資本週期階段（capital cycle stage） | WebSearch；quarterly_state 沿用、event_scan 30 日掃描無披露 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機 / Search for past 7 days: AI rename / SPAC | 新聞／SEC EDGAR WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機 / IPO market heat | stockanalysis WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機 / Microcap thematic moonshots | Finviz / Benzinga / StockTwits WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機 / Upcoming AI IPOs | 新聞 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機 / Insider selling at AI / market-leadership companies | SEC EDGAR / openinsider（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機 / Cboe equity-only put/call ratio | Cboe 統計 WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構 / US leveraged ETF AUM | etf.com 等 WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構 / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com new launches（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | 結構 / Global leveraged product approvals | KRX / TWSE / JPX / ESMA WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構 / 0DTE option volume | Cboe insights WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構 / Options total volume | OCC 統計 WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構 / Cross-asset derivatives / correlation checks | VIX term structure / SKEW WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構 / VIX / S&P 500 co-movement | fetch_macro.py（FRED VIXCLS＋vix_spx_comove） | ✓ API |
| structural.margin_debt_crosscheck | 結構 / Cross-reference only: FINRA margin debt | FINRA / GuruFocus WebSearch（交叉檢核） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構 / AI infrastructure debt financing / vendor-financing loops | 信用市場 WebSearch（30d） | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | 結構 / Bank loans to nondepository financial institutions | fetch_macro.py（FRED API） | ✓ API |
| structural.treasury_basis_trade | 結構 / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py cftc_lev_funds / move_index / ofr_repo；WebSearch 補充無新披露 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E ≈26.2、Shiller CAPE ≈41.2 | Shiller CAPE S&P 500 P/E August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus；原定 multpl / GuruFocus） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E ≈29.5x（S&P 500 ≈25.6x） | Magnificent 7 weighted P/E August 2026 | https://www.fool.com/investing/2026/08/14/the-best-magnificent-seven-stocks-to-buy-in-august/（Motley Fool） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| breadth.rsp_spy | RSP 領先 SPY YTD ≈5pp | RSP vs SPY YTD 2026 breadth | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 top-10 集中度 ≈36.5% | S&P 500 top 10 concentration 2026 | https://www.ebc.com/forex/rsp-vs-spy（EBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.advance_decline | 領導由 top-100 向 bottom-400 擴散、廣度確認多頭（無數值 A/D ratio） | market breadth advance decline August 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 55（Greed） | CNN Fear and Greed today August 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-07 月資料）≈1,417,225、YoY ≈+38.6%、MoM −5.7% | FINRA margin debt July 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt（GuruFocus；原定 FINRA） | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| retail.aaii | AAII 偏多 35.5%、偏空 39.9%（週結 2026-08-19） | AAII investor sentiment August 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 標售無明顯 tail、12.10% allotted at high | US Treasury 30-year auction August 2026 | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2026/R_20260813_3.pdf（TreasuryDirect） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| monetary.fedwatch | FedWatch 9/16 按兵不動 ≈68.4%、尾端為升息 | CME FedWatch September 2026 hold probability | https://en.macromicro.me/series/1645/probability-fed-rate-decrease（MacroMicro；原定 CME FedWatch） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_capex | top-4 hyperscaler 2026 capex 合計 ≈$725bn（+77% YoY，Q2 財報季彙整） | hyperscaler 2026 capex guidance Microsoft Google Amazon Meta | https://valueaddvc.com/ai-spending（ValueAdd VC；原定各家財報） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.openai_anthropic_revenue | OpenAI ≈$40B、Anthropic ≈$65B run-rate | OpenAI Anthropic annualized revenue August 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html（CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.compute_supply_demand | GPU 現貨租金 > 2× 合約價、產能被利用率吸收 | AI GPU rental pricing utilization August 2026 | https://www.uncoveralpha.com/p/amazon-google-microsoft-meta-q2-earnings（UncoverAlpha） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex > FCF、2026 hyperscaler 發債擴張（capex 由現金流轉向舉債） | hyperscaler external financing capex FCF debt 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow（FactSet） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 ≈$105bn（OpenAI 40＋Anthropic 65）vs 年化 capex ≈$725bn（分母：top-4） | AI revenue to capex gap 2026 | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.capital_cycle | [quarterly_state] 供給側 capex 年增 ≈77%、需求側 token／營收成長並存 | AI capex growth rate supply demand 2026 | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描 0 件 | AI rename SPAC ticker change August 2026 | Renaissance Capital / SEC EDGAR / 新聞掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD IPO ≈232 件（截至 2026-08-21）、無單週無營收 AI IPO 暴衝 | US IPO count August 2026 | https://stockanalysis.com/ipos/2026/（StockAnalysis） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot（單日 ≥100%、市值 < $1B、2+ 主題、弱基本面）7 日掃描 0 檔 | microcap 100% single day surge quantum AI August 2026 | Finviz / Benzinga / StockTwits movers 掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 10 月 IPO、估值 ≈$2T | Anthropic OpenAI IPO 2026 | https://finance.yahoo.com/markets/article/spacex-openai-and-anthropic-here-are-the-most-anticipated-ipos-in-2026-114439441.html（Yahoo Finance） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 14 日內合格 Form 4 集中賣出 0 起 | insider Form 4 AI executives August 2026 | SEC EDGAR / openinsider 掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.52（9 日均總量 0.85） | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio（原定 Cboe） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美股槓桿 ETF 總 AUM ≈$198bn 創紀錄；TQQQ 31.3、SOXL 17.3（$bn） | leveraged ETF AUM record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing；原定 etf.com） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| structural.us_single_stock_etf | 美單一個股槓桿 ETF 30 日新核准／上市 0 件 | single-stock leveraged ETF launch SEC August 2026 | SEC EDGAR / ETF.com new launches 掃描 | — | 2026-08-24T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 8 月佔比 ≈62.4% 創紀錄 | 0DTE SPX volume share August 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| structural.options_volume | OCC YTD 日均 > 71M 口、量能高檔 | OCC options volume 2026 | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/historical-volume-statistics（OCC） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 16.01、期限結構 contango（IVTS ≈0.82）、SKEW 偏高 | VIX term structure SKEW August 2026 | https://www.thetrading.tools/vix-term-structure（原定 Cboe / SpotGamma） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt / 市值交叉檢核（2026-07 月資料，YoY +38.6%） | FINRA margin debt equity market cap ratio 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt（GuruFocus；原定 FINRA） | 2026-07-01 | 2026-08-24T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-24",
  "iso_week": "2026-W35",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-22",
  "prior_date": "2026-08-20",
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 4.41,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

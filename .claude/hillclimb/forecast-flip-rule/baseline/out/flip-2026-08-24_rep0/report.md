> [DRY RUN] this report was not committed to archive.

# 2026-08-24 AI 泡沫破裂預測報告

報告日期：2026-08-24｜ISO 週次：2026-W35｜預測窗口：2026-08-24 → 2027-02-22｜前次基準：report-2026-08-20（4天前）

## 結論

**結論：yes**

依翻轉紀律維持前次 yes：自 report-2026-08-20 以來，日期晚於前次且觸及路徑的新數據只有 R1 一項——NASDAQ-100 距 52 週高點回撤 4.41%（前次 4.03%，`valuation.ndx_drawdown`），方向不支持改判 no；R2 與 R3 本次沒有任何日期晚於 2026-08-20 的新證據。支持 no 的主要證據（top-4 capex 合計 ≈$725bn、+77% YoY，`ai.hyperscaler_capex`；HY OAS 2.75%，`monetary.hy_oas`）在前次基準日前已公布，不構成翻轉依據。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,308.86（2026-08-21），252 交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 4.41%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45；自最新收盤再下跌約 21.54% 才會觸及。前次基準日（2026-08-20）的回撤為 4.03%，本次略為擴大。同期 S&P 500 收 7,674.37（2026-08-21），較 200 日 MA 高 8.15%、較 52 週 MA 高 9.61%（`valuation.sp500_trend`），價格仍明顯偏離趨勢、具均值回歸空間；VIX 16.01（2026-08-20），trailing 7 日 VIX +9.43%、S&P 500 −2.02%，屬正常的反向變動、未出現 crowded-optionality 同漲讀數（`structural.vix_spx_comove`）。估值端 Shiller CAPE ≈41.2、trailing P/E ≈26.2（2026-08-20，`valuation.sp500_pe_cape`），Mag 7 加權 P/E ≈29.5x（`valuation.mag7_multiples`）。

**判讀：** R1 距門檻仍有約 21.54% 的跌幅，屬遠端；高估值與趨勢偏離代表下跌空間大，但要在 182 天內完成需要明確催化劑，例如 Anthropic 10 月 IPO 估值重定價、Q3 季報 capex 或營收不及預期，或 9/16 FOMC 意外轉鷹而引發去槓桿。

### R2 資本支出收縮

本次證據只有 top-4（Microsoft、Alphabet、Amazon、Meta）2026 capex 合計 ≈$725bn、+77% YoY（2026-08-13，`ai.hyperscaler_capex`），出自 2026 Q2 季報後的彙整；各家的指引數字與相對前次正式指引的方向（上修／持平／下修）未在本次證據中逐家揭露：

- Microsoft：未逐家揭露（合計口徑內，未見下修披露）
- Alphabet：未逐家揭露（合計口徑內，未見下修披露）
- Amazon：未逐家揭露（合計口徑內，未見下修披露）
- Meta：未逐家揭露（合計口徑內，未見下修披露）

已知下修家數：0／4。窗口內會有兩輪季報（Q3 與 Q4），但確切財報日期不在本次證據中。需求端：Anthropic run-rate ≈$65B、OpenAI ≈$40B（2026-08-17，`ai.openai_anthropic_revenue`）；GPU 現貨租金高於合約價 2 倍以上，產能已被利用率吸收（2026-08-13，`ai.compute_supply_demand`）。

**判讀：** R2 目前離成立最遠。合計 capex 仍在加速、需求端利用率偏緊，兩家同時下修需要需求突然轉弱或資金成本急升；在本次證據下，窗口內兩輪季報出現兩家下修的跡象不明顯。

### R3 AI 信用事件

本次的 AI 信用定價分歧（equity-vs-credit schism）掃描與 AI infrastructure debt financing / vendor-financing loops 掃描都已完成，但 14／30 日窗內沒有合格披露。因此本次沒有關於可能達到 R3 門檻（負債 ≥ USD 5bn、以 AI 資料中心／算力為主業）的借款人的當期債券殖利率、利差、CDS 或評等資料，也沒有違約、豁免、distressed exchange 或 going-concern 訊號的披露。廣義信用環境寬鬆：HY OAS 2.75%、IG OAS 0.82%（2026-08-20，`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 −2bp，SRF 動用（Standing Repo Facility usage）為 0（`monetary.repo_stress_srf`）。

**判讀：** 現有數據沒有任何 R3 事件正在進行的跡象。要在窗口內成立，需要某家大型 neocloud 在再融資時失敗；以 HY OAS 2.75% 的資金環境，短期出現的可能性低。不過本次缺乏借款人層級的定價，所以這個判讀的覆蓋面有限。

## 支持 yes 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.41%（2026-08-21），較前次的 4.03% 擴大；S&P 500 較 200 日 MA 高 8.15%（`valuation.ndx_drawdown`、`valuation.sp500_trend`）。
- [整體] 估值極端：Shiller CAPE ≈41.2、trailing P/E ≈26.2（2026-08-20，`valuation.sp500_pe_cape`）；Mag 7 加權 P/E ≈29.5x，高於 S&P 500 的 ≈25.6x（2026-08-14，`valuation.mag7_multiples`）。
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收 ≈$105bn（OpenAI ≈40＋Anthropic ≈65）對年化 capex ≈$725bn（分母：top-4，不含 Oracle 與 neocloud），缺口仍大（2026-08-17，`ai.revenue_capex_gap`）。
- [R1] 槓桿與投機部位處於高位：FINRA margin debt（2026-07）YoY ≈+38.6%，接近歷史頂部常見的 +40–50% 區間（`retail.margin_debt`）；美股槓桿 ETF 總 AUM 創 ≈$198bn 紀錄（2026-08-17，`structural.leveraged_etf_aum`）；SPX 0DTE 佔比創 ≈62.4% 紀錄（2026-08-14，`structural.zero_dte`）。
- [R1] 窗口內有估值重定價催化劑：Anthropic 目標 10 月 IPO、估值 ≈$2T（2026-08-17，`speculation.upcoming_ai_ipos`）；FedWatch 對 9/16 會議的定價為按兵不動 ≈68.4%，尾端為升息（2026-08-20，`monetary.fedwatch`）；CPI YoY 3.3%（2026-07，`monetary.cpi_yoy`）限制了 Fed 緩衝 AI 主導下跌的空間。

## 支持 no 的證據

- [R2] top-4 hyperscaler 2026 capex 合計 ≈$725bn、+77% YoY，未見任何一家下修（2026-08-13，`ai.hyperscaler_capex`）；GPU 現貨租金高於合約價 2 倍以上，產能已被利用率吸收（`ai.compute_supply_demand`）。
- [R1] R1 門檻 22,995.45 距最新收盤 29,308.86 尚有約 21.54% 的跌幅（`valuation.ndx_drawdown`）；在任意 182 天窗口內出現 25% 回撤本身就不常見。
- [R3] 信用與資金市場寬鬆：HY OAS 2.75%、IG OAS 0.82%（2026-08-20，`monetary.hy_oas`、`monetary.ig_oas`）；SOFR−IORB −2bp、SRF 動用 0（`monetary.repo_stress_srf`）；MOVE 73.4（2026-08-21，`structural.treasury_basis_trade`）。
- [R2] 需求端仍在快速成長：Anthropic run-rate ≈$65B、年增 ≈7×（2026-08-17，`ai.token_growth`、`ai.openai_anthropic_revenue`）。
- [整體] 情緒未達亢奮、廣度擴散：CNN Fear & Greed 55（2026-08-21，`retail.fear_greed`）；AAII 偏空 39.9% 高於偏多 35.5%（`retail.aaii`）；RSP YTD 領先 SPY ≈5pp（`breadth.rsp_spy`）；VIX 16.01 且期限結構呈 contango（`structural.cross_asset_derivatives`）。

## 與前期比較

前次結論：yes（report-2026-08-20）

本次結論：維持

- R1：距 52 週高點回撤 4.41%（2026-08-21），前次 4.03%，略為擴大，方向與前次 yes 一致，不支持翻轉（`valuation.ndx_drawdown`）。
- 日期晚於 2026-08-20 的其他新數據都沒有改變路徑分析：CNN Fear & Greed 55（2026-08-21，`retail.fear_greed`）、IPO YTD ≈232 件且無單週無營收 AI IPO 暴衝（2026-08-21，`speculation.ipo_heat`）、MOVE 73.4（`structural.treasury_basis_trade`）、SRF 動用 0（`monetary.repo_stress_srf`），全屬持平或雜訊級變動。
- 宏觀序列大多沒有新觀測：DGS10、DFII10、HY OAS、IG OAS 的最新觀測仍是 2026-08-20；10Y Δ 分解為 `無變動`（stale_series：DGS10、DFII10），因此沒有 R3 方向的新資訊。
- 支持 no 的主要證據——top-4 capex 合計 ≈$725bn（2026-08-13）、OpenAI／Anthropic run-rate（2026-08-17）、GPU 租金與利用率（2026-08-13）——發布日都早於 2026-08-20，依翻轉紀律不得作為翻轉依據。這裡如實揭露：若不考慮前次結論、只看本次全部證據，no 一側的證據較強；但本次沒有日期晚於前次、且足以改變任何路徑分析的來源，所以維持 yes。
- R2 與 R3 本次沒有晚於前次的新披露；AI 信用定價分歧與 AI infrastructure debt financing 掃描在窗內都沒有合格事件。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源的檢索已完成，但窗內無合格披露（✗ NOT DISCLOSED），其中幾項缺口可能影響結論：

- valuation.ai_credit_schism、structural.ai_infrastructure_debt：R3 的直接證據來源。缺少借款人層級的利差、CDS 與再融資資料，是本次最大的盲點；若下一次出現 neocloud 利差顯著走闊或再融資困難，會強化 yes。
- ai.hyperscaler_financing_mix（quarterly_state ok：top-5 capex 已超過 FCF、2026 年發債擴張，2026-08-17；event_scan 30 日窗內無合格事件）與 ai.capital_cycle（event_scan 無取消／延後事件）：沒有新的融資或取消事件，對結論是中性。
- monetary.private_credit_liquidity：30 日窗內沒有贖回壓力披露。若出現多檔基金 redemption-request ratio 上升或 gate proration / breach，會推向 yes（經由 R3 再傳導至 R1）。
- valuation.analyst_tp_decomposition、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.pboc、ai.customer_concentration_rpo、ai.depreciation_life、structural.global_leveraged_approvals：屬輔助訊號，缺漏不太可能改變結論。

最大的不確定性：

1. 前次 yes 的依據：本次維持 yes 是依翻轉紀律，而非由本次證據獨立推導。如果下一次出現日期晚於本次、且偏向 no 的新路徑證據（例如 Q3 季報 capex 再上修、信用持續寬鬆），應依紀律翻轉為 no。
2. Q3 季報（窗口內）：只要兩家 hyperscaler 下修 capex 指引就直接觸發 R2；季報結果也會左右 R1 的估值重定價。
3. Anthropic 10 月 IPO（估值 ≈$2T）與 9/16 FOMC 的升息尾端：若定價失利或貨幣緊縮，可能成為 R1 的催化劑，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7674.37 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日 MA %） | 8.15 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週 MA %） | 9.61 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（NASDAQ-100 收盤） | 29308.86 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.41 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1 家庭股票配置 %） | 45.76080873390133（≈45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上緣 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下緣 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.75 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.82 | FRED API (series_id=BAMLC0A0CM) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.69 | FRED API (series_id=DGS10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.35 | FRED API (series_id=DFII10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.34 | FRED API (series_id=T10YIE) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl） | 86.48 | FRED API (series_id=DCOILWTICO) | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料，%） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.34 | FRED API (series_id=T5YIFR) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright 10Y 期限溢價，%） | 0.8393 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 日） | 1.4 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.63 | FRED API (series_id=SOFR) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.71 | FRED API (series_id=SOFR99) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-24 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR−IORB 利差（repo_stress sofr_iorb_bps） | -2.0 | FRED API (series_id=SOFR, IORB) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.walcl | WALCL latest（百萬美元） | 6745699.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（百萬歐元） | 5927307.0（€5.93T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（億日圓） | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.01 | FRED API (series_id=VIXCLS) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of 2026-08-20，base 2026-08-13，7 日窗） | 16.01 | FRED API (series_id=VIXCLS, SP500) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 9.43 | FRED API (series_id=VIXCLS, SP500) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -2.02 | FRED API (series_id=VIXCLS, SP500) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（十億美元） | 2026.1422（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-12 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7218048 | CFTC TFF (cftc_lev_funds) | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.4 | Yahoo chart ^MOVE (move_index) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2328.6 | OFR STFM REPO-TRIV1_TV_TOT-P (ofr_repo) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl / GuruFocus WebSearch | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | 賣方摘要 WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | 信用市場 WebSearch（14d） | ✗ NOT DISCLOSED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | CNN WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | FINRA / GuruFocus WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | AAII WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WSB / X WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | naaim.org WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey | BofA / JPM WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API DFEDTARU ok；DFEDTARL ok |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD） | ✓ API SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | Reuters / TreasuryDirect WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | CME FedWatch WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API ECBASSETSW ok；JPNASSETS ok |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | PBoC / NBS WebSearch | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | BDC 披露 WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | 財報摘要 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | 供應商披露 WebSearch | ✓ SEARCH-VERIFIED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | Bloomberg / CNBC WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | 財報電話 WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | 產業披露 WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | 財報／發債 WebSearch；quarterly_state 沿用最近季度，event_scan 30d 無合格事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | 綜合披露 WebSearch（分母 top-4） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | 10-K / 10-Q WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | 產業披露 WebSearch；quarterly_state 沿用，event_scan 30d 無合格事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | 新聞／SEC EDGAR WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | stockanalysis / Renaissance WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | Finviz / Benzinga WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | Bloomberg / CNBC / Yahoo WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR / openinsider WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | ETF.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com WebSearch（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | KRX / TWSE / JPX / ESMA WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | OCC WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | Cboe / SpotGamma WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API VIXCLS ok；vix_spx_comove ok |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | FINRA / GuruFocus WebSearch（交叉檢核） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | 信用市場 WebSearch（30d） | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）＋WebSearch 平倉新聞（無合格事件） | ✓ API cftc_lev_funds ok；move_index ok；ofr_repo ok |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | trailing P/E ≈26.2、Shiller CAPE ≈41.2（原定 multpl / GuruFocus） | Shiller CAPE S&P 500 P/E August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio （GuruFocus） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E ≈29.5x（S&P 500 ≈25.6x） | Magnificent 7 weighted P/E August 2026 | https://www.fool.com/investing/2026/08/14/the-best-magnificent-seven-stocks-to-buy-in-august/ （Motley Fool） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| breadth.rsp_spy | RSP 領先 SPY YTD ≈5pp | RSP vs SPY YTD 2026 breadth | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 top-10 集中度 ≈36.5% | S&P 500 top 10 concentration 2026 | https://www.ebc.com/forex/rsp-vs-spy （EBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.advance_decline | 領導由 top-100 擴散至 bottom-400，廣度確認多頭 | market breadth advance decline August 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 55（Greed） | CNN Fear and Greed today August 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-07 月資料）≈1,417,225、YoY ≈+38.6%、MoM −5.7% | FINRA margin debt July 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt （GuruFocus，原定 FINRA） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |
| retail.aaii | AAII 偏多 35.5%、偏空 39.9%（週結 2026-08-19） | AAII investor sentiment August 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 標售無明顯 tail、12.10% allotted at high | US Treasury 30-year auction August 2026 | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2026/R_20260813_3.pdf （TreasuryDirect） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| monetary.fedwatch | 9/16 FOMC 按兵不動定價 ≈68.4%，尾端為升息 | CME FedWatch September 2026 hold probability | https://en.macromicro.me/series/1645/probability-fed-rate-decrease （MacroMicro，原定 CME FedWatch） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_capex | top-4 2026 capex 合計 ≈$725bn、+77% YoY（Q2 季報後彙整） | hyperscaler 2026 capex guidance Microsoft Google Amazon Meta | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.token_growth | Anthropic run-rate 年增 ≈7×、API 佔營收多數 | Anthropic token growth revenue 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html （CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.openai_anthropic_revenue | OpenAI ≈$40B、Anthropic ≈$65B run-rate | OpenAI Anthropic annualized revenue August 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html （CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.compute_supply_demand | GPU 現貨租金 > 2× 合約價，產能已被利用率吸收 | AI GPU rental pricing utilization August 2026 | https://www.uncoveralpha.com/p/amazon-google-microsoft-meta-q2-earnings （UncoverAlpha） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex > FCF、2026 hyperscaler 發債擴張（capex 由現金流轉向舉債） | hyperscaler external financing capex FCF debt 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow （FactSet） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.revenue_capex_gap | OpenAI 40＋Anthropic 65 → ≈105 vs 年化 capex ≈725（$bn；分母 top-4） | AI revenue to capex gap 2026 | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.capital_cycle | [quarterly_state] 供給側 capex 年增 ≈77%、需求側 token／營收成長並存 | AI capex growth rate supply demand 2026 | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 掃描：7 日窗內 0 件合格事件 | AI rename SPAC ticker change August 2026 | Renaissance Capital / SEC EDGAR / 新聞掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD IPO ≈232 件（截至 2026-08-21），無單週無營收 AI IPO 暴衝 | US IPO count August 2026 | https://stockanalysis.com/ipos/2026/ （StockAnalysis） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（≥100% 單日、<$1B、2+ 主題、弱基本面）：0 檔 | microcap 100% single day surge quantum AI August 2026 | Finviz / Benzinga / StockTwits movers 掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 10 月 IPO、估值 ≈$2T | Anthropic OpenAI IPO 2026 | https://finance.yahoo.com/markets/article/spacex-openai-and-anthropic-here-are-the-most-anticipated-ipos-in-2026-114439441.html （Yahoo Finance） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 14 日窗內合格 Form 4 集中賣出：0 起 | insider Form 4 AI executives August 2026 | SEC EDGAR / openinsider 掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.52（9 日均總量 0.85） | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio （thetrading.tools，原定 Cboe） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美股槓桿 ETF 總 AUM ≈$198bn 創紀錄；TQQQ 31.3、SOXL 17.3（$bn） | leveraged ETF AUM record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing，原定 etf.com） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| structural.us_single_stock_etf | 單一個股槓桿 ETF 30 日窗內新核准／上市：0 件 | single-stock leveraged ETF launch SEC August 2026 | SEC EDGAR / ETF.com new launches 掃描 | — | 2026-08-24T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 8 月佔比創紀錄 ≈62.4% | 0DTE SPX volume share August 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august （Cboe） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| structural.options_volume | OCC YTD 日均 >71M 口，量能處高檔 | OCC options volume 2026 | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/historical-volume-statistics （OCC） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 16.01、期限結構 contango（IVTS ≈0.82）、SKEW 偏高 | VIX term structure SKEW August 2026 | https://www.thetrading.tools/vix-term-structure （thetrading.tools） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt／市值交叉檢核（2026-07 月資料，YoY +38.6%，見 retail.margin_debt） | FINRA margin debt equity market cap ratio 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt （GuruFocus） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-24",
  "iso_week": "2026-W35",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "yes",
  "horizon_end": "2027-02-22",
  "prior_date": "2026-08-20",
  "prior_answer": "yes",
  "flip_evidence": [],
  "r1_drawdown_pct": 4.41,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

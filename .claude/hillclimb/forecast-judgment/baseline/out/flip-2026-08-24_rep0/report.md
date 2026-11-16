> [DRY RUN] this report was not committed to archive.

# 2026-08-24 AI 泡沫破裂預測報告

報告日期：2026-08-24｜ISO 週次：2026-W35｜預測窗口：2026-08-24 → 2027-02-22｜前次基準：report-2026-08-20（4天前）

## 結論

**結論：yes**

依翻轉紀律維持前次 yes：日期晚於 2026-08-20 的新資料（NASDAQ-100 2026-08-21 收盤、MOVE、SRF 動用、CNN Fear & Greed、IPO heat）只延續既有格局，沒有任何一項改變 R1–R3 的路徑分析，因此不構成翻轉依據。須明確指出：就證據本身而言，支持 no 的一側較強（HY OAS 2.75%、hyperscaler capex 仍在擴張、R1 尚需自最新收盤再跌約 21.54%），維持 yes 的理由是前次結論加上 R1 的高脆弱度（CAPE ≈41.2、margin debt YoY ≈+38.6%、槓桿 ETF AUM 創紀錄），而非本次出現新的破裂觸發。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,308.86（2026-08-21），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 4.41%（前次 report-2026-08-20 為 4.03%，略為擴大）。R1 門檻水位 22,995.45，自最新收盤須再跌約 21.54% 才會觸及（`valuation.ndx_drawdown`）。S&P 500 收 7,674.37（2026-08-21），高於 200 日均線 8.15%、高於 52 週均線 9.61%，價格延伸仍明顯（`valuation.sp500_trend`）。2026-08-13 → 2026-08-20 共享窗口內 S&P 500 −2.02%、VIX +9.43%（16.01），屬正常負相關、未出現同漲的 crowded-optionality 警戒（`structural.vix_spx_comove`）。脆弱度面：Shiller CAPE ≈41.2、trailing P/E ≈26.2（`valuation.sp500_pe_cape`），Mag 7 加權 P/E ≈29.5x（`valuation.mag7_multiples`），FINRA margin debt 2026-07 YoY ≈+38.6%（`retail.margin_debt`），美股槓桿 ETF AUM ≈$198bn 創紀錄（`structural.leveraged_etf_aum`），SPX 0DTE 佔比 ≈62.4%（`structural.zero_dte`）。

**判讀：** 距門檻仍遠（須再跌約 21.54%），目前沒有已啟動的回撤；但估值與槓桿使一旦出現觸發（hyperscaler 季報失望、利率再上行、2026-10 Anthropic IPO 帶來的大量股權供給），窗口內走完 25% 回撤的放大條件存在。推過門檻需要信用或資金面出現傳導，目前未見。

### R2 資本支出收縮

本次可得證據為 top-4（Microsoft、Alphabet、Amazon、Meta）2026 capex 合計 ≈$725bn、年增 ≈77%（2026-08-13，2026Q2 財報季後彙整；`ai.hyperscaler_capex`）。各公司個別指引數值與相對前次正式指引的方向（上修／持平／下修）未在本次證據中逐家列出，因此不逐家填寫；就合計口徑與可得報導，四家中已下修家數為 0。需求面支撐：GPU 現貨租金 > 2× 合約價、產能被利用率吸收（2026-08-13；`ai.compute_supply_demand`）；Anthropic run-rate ≈$65B、OpenAI ≈$40B（2026-08-17；`ai.openai_anthropic_revenue`）。下一輪財報季（2026Q3，約 10 月下旬）與 2027-01/02 的 2026Q4 財報季都落在窗口內，確切日期未在本次證據中。

**判讀：** R2 離成立最遠——capex 仍在大幅上修期且算力需求吃緊；要在窗口內成立需兩家在 10 月或 1–2 月財報下修指引，目前沒有任何證據指向這個方向。

### R3 AI 信用事件

本次 AI 信用定價分歧與 AI infrastructure debt financing / vendor-financing loops 兩項掃描都未取得窗口內披露（詳見資料缺漏），因此沒有可引用的 AI 借款人個別債券利差、CDS、評等動作或到期牆資料。整體信用環境：HY OAS 2.75%、IG OAS 0.82%（2026-08-20，與前次無新觀測；`monetary.hy_oas`、`monetary.ig_oas`），處於歷史緊縮區間；銀行對 NBFI 放款 $2.03T（2026-08-12；`structural.nbfi_bank_loans`）。資金面：repo 資金壓力（SOFR−IORB）為 −2.0 bps、SOFR99−IORB +6.0 bps（皆 2026-08-20），SRF 動用（Standing Repo Facility usage）為 0（2026-08-21；`monetary.repo_stress_srf`）；MOVE 73.4（2026-08-21；`structural.treasury_basis_trade`）。

**判讀：** 沒有任何 R3 規模借款人出現違約、寬限期、distressed exchange 或 going-concern 的證據，信用利差也未重定價；R3 要在窗口內成立需先看到 neocloud 類借款人利差急遽走闊或再融資失敗，目前完全未見。

## 支持 yes 的證據

- [R1] 估值與槓桿處於極端水位：Shiller CAPE ≈41.2、trailing P/E ≈26.2（2026-08-20，`valuation.sp500_pe_cape`），FINRA margin debt 2026-07 YoY ≈+38.6% 接近歷史頂部常見的 +40–50% 區間（`retail.margin_debt`），美股槓桿 ETF AUM ≈$198bn 創紀錄（2026-08-17，`structural.leveraged_etf_aum`），SPX 0DTE 佔比 ≈62.4%（2026-08-14，`structural.zero_dte`）——一旦觸發，回撤會被強制去槓桿放大。
- [R1] NASDAQ-100 距 52 週高點回撤 4.41%（2026-08-21），較前次 4.03% 擴大，且 S&P 500 仍高於 200 日均線 8.15%，均值回歸空間大（`valuation.ndx_drawdown`、`valuation.sp500_trend`）。
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）：已披露年化 AI 終端營收 ≈$105bn（OpenAI ≈$40B＋Anthropic ≈$65B）vs 年化 capex ≈$725bn（分母：top-4 MSFT／GOOGL／AMZN／META，Oracle 無當期披露未納入），營收僅約分母的 14%（2026-08-17，`ai.revenue_capex_gap`）。
- [R1] Anthropic 目標 2026-10 IPO、估值 ≈$2T（2026-08-17，`speculation.upcoming_ai_ipos`），窗口內的大型股權供給可能成為情緒轉折點。
- [整體] 利率端對 Fed 緩衝的限制：10Y 殖利率 4.69%（`monetary.dgs10`）、10Y 期限溢價（term premium）0.8393%、trailing ≈7 日 +1.4 bps（`monetary.term_premium`）、CPI YoY 3.3%（2026-07，`monetary.cpi_yoy`），FedWatch 9/16 按兵不動 ≈68.4% 且尾端為升息（2026-08-20，`monetary.fedwatch`）——回撤時降息救市空間有限。

## 支持 no 的證據

- [R3] 信用市場完全未重定價：HY OAS 2.75%、IG OAS 0.82%（2026-08-20，`monetary.hy_oas`、`monetary.ig_oas`），repo 資金壓力（SOFR−IORB）−2.0 bps、SRF 動用 0（`monetary.repo_stress_srf`），沒有任何 AI 規模借款人的違約或 distressed exchange 證據。
- [R2] hyperscaler capex 仍在擴張：top-4 2026 合計 ≈$725bn、年增 ≈77%（2026-08-13，`ai.hyperscaler_capex`），GPU 現貨租金 > 2× 合約價、產能被利用率吸收（`ai.compute_supply_demand`），四家中下修家數為 0。
- [R1] 距 R1 門檻仍遠：NASDAQ-100 最新收盤 29,308.86 須再跌約 21.54% 至 22,995.45 才觸及門檻（`valuation.ndx_drawdown`）；在任意 182 天窗口內這是少見事件。
- [整體] AI 需求端仍在加速：Anthropic run-rate ≈$65B、年增 ≈7×，OpenAI ≈$40B（2026-08-17，`ai.openai_anthropic_revenue`、`ai.token_growth`）。
- [整體] 情緒與廣度非狂熱：CNN Fear & Greed 55（2026-08-21，`retail.fear_greed`），AAII 偏多 35.5%／偏空 39.9%（`retail.aaii`），RSP 領先 SPY YTD ≈5pp、領導向 bottom-400 擴散（`breadth.rsp_spy`、`breadth.advance_decline`），microcap moonshot 與 +AI 改名掃描皆 0 件（`speculation.microcap_moonshots`、`speculation.ai_rename_spac`）。
- [整體] 債市波動與美債基差交易槓桿未見壓力：MOVE 73.4（2026-08-21），CFTC 槓桿基金美債期貨淨空單 4 週回補 244,468 口（2026-08-18，`structural.treasury_basis_trade`）；30Y 標售無明顯 tail（2026-08-13，`monetary.treasury_auctions`）。

## 與前期比較

前次結論：yes（report-2026-08-20）

本次結論：維持

- NASDAQ-100 最新收盤 29,308.86（2026-08-21），距 52 週高點回撤 4.41%，前次為 4.03%：R1 距離小幅縮短，方向不支持翻轉為 no，幅度也不足以改變路徑分析（`valuation.ndx_drawdown`）。
- MOVE 73.4（2026-08-21，較前一日 +0.22）、SRF 動用 0（2026-08-21）：資金與債市波動延續平靜，只是確認既有格局，沒有改變 R3 路徑（`structural.treasury_basis_trade`、`monetary.repo_stress_srf`）。
- CNN Fear & Greed 55（2026-08-21）與 2026 YTD IPO ≈232 件、無單週無營收 AI IPO 暴衝（2026-08-21）：情緒中性，未提供新的觸發或排除證據（`retail.fear_greed`、`speculation.ipo_heat`）。
- HY／IG OAS、DGS10、DFII10 均無 2026-08-20 之後的新觀測；10Y Δ 分解：DGS10、DFII10、T10YIE 三者 Δ 均為 0，判讀為無變動，其中 DGS10、DFII10 無新觀測（freshness 為 partial_stale），T10YIE 有更新但同樣持平（`monetary.dgs10`、`monetary.t10yie`）。
- 支撐 no 的主要證據（capex ≈$725bn、Anthropic ≈$65B run-rate、HY OAS 2.75%）日期皆不晚於 2026-08-20，前次已可取得，依翻轉紀律不能作為翻轉依據；結論維持 yes。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED（掃描完成、窗口內無合格披露）的來源：valuation.analyst_tp_decomposition、valuation.ai_credit_schism、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.pboc、monetary.private_credit_liquidity、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（quarterly_state 可得：top-5 capex > FCF、2026 發債擴張，2026-08-17；event_scan 30 日內無新融資事件）、ai.depreciation_life、ai.capital_cycle（quarterly_state 可得：供給側 capex 年增 ≈77%，需求側 token／營收成長並存；event_scan 30 日內無取消／延後事件）、structural.global_leveraged_approvals、structural.ai_infrastructure_debt。其中對答案影響最大的是 valuation.ai_credit_schism 與 structural.ai_infrastructure_debt：R3 的個別借款人利差、到期牆與違約訊號完全來自這兩項，本次缺漏使 R3 只能以整體 HY／IG OAS 判讀；若其實存在未被搜尋到的 neocloud 利差走闊，會強化 yes。monetary.private_credit_liquidity 缺漏同理，但目前整體信用利差緊縮，顯示未被捕捉的壓力不大。

最大的不確定性：

1. 翻轉紀律與證據強弱的落差：本次證據整體支持 no（R1 須再跌約 21.54%、R2 下修家數 0、R3 無信用重定價），yes 僅因缺少日期晚於 2026-08-20 的新證據而維持。下次若出現確認此格局的新資料（如新一期 HY OAS 仍緊、新一期 hyperscaler 指引上修），即構成翻轉為 no 的依據。
2. 2026Q3 hyperscaler 財報季（約 10 月下旬，落在窗口內）：若兩家以上下修 2026／2027 capex 指引，R2 直接成立並可能連帶觸發 R1；若持續上修，則強化 no。
3. 2026-10 Anthropic IPO（估值 ≈$2T）與利率路徑：大型股權供給加上 FedWatch 尾端升息風險，是 R1 在窗口內最可能的觸發組合，推向 yes；若 IPO 順利、利率持平，則推向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7674.37 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 8.15 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 9.61 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29308.86 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.41 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1 家戶股票配置 %） | 45.76（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.75 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.82 | FRED API (series_id=BAMLC0A0CM) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.69 | FRED API (series_id=DGS10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.35 | FRED API (series_id=DFII10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.34 | FRED API (series_id=T10YIE) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（美元／桶） | 86.48 | FRED API (series_id=DCOILWTICO) | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料，%） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.34 | FRED API (series_id=T5YIFR) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 0.8393 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing ≈7 日） | 1.4 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.63 | FRED API (series_id=SOFR) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.71 | FRED API (series_id=SOFR99) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-24 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6745699.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5927307.0（€5.93T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.01 | FRED API (series_id=VIXCLS) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of 2026-08-20，base 2026-08-13，7 日窗） | 16.01 | FRED API (series_id=VIXCLS + SP500) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 9.43 | FRED API (series_id=VIXCLS + SP500) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -2.02 | FRED API (series_id=VIXCLS + SP500) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2026.1422（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-12 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7218048 | CFTC TFF futures-only | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 244468 | CFTC TFF futures-only | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.4 | Yahoo Finance chart API (^MOVE) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index delta_abs | 0.22 | Yahoo Finance chart API (^MOVE) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2328.6 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值 / S&P 500 P/E and Shiller CAPE | multpl / GuruFocus [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值 / Mag 7 weighted P/E and AI leader P/S | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值 / Analyst TP upgrade decomposition | 賣方摘要 WebSearch（90d＋同季） | ✗ NOT DISCLOSED（無同季合格 TP 上修） |
| valuation.sp500_trend | 估值 / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500，sp500_trend） | ✓ API |
| valuation.ndx_drawdown | 估值 / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100，ndx_drawdown） | ✓ API |
| valuation.ai_credit_schism | 估值 / AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✗ NOT DISCLOSED（14 日內無合格報導） |
| breadth.rsp_spy | 廣度 / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度 / Top-10 concentration in S&P 500 | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度 / Advance/decline ratio, new high/low ratio | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶 / CNN Fear & Greed Index | CNN [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶 / Margin Debt: FINRA monthly data | FINRA / GuruFocus WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶 / Retail survey: AAII Investor Sentiment | AAII [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶 / Social sentiment proxies | WSB / X WebSearch（7d） | ✗ NOT DISCLOSED（無顯著討論） |
| retail.household_equity_allocation | 散戶 / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶 / NAAIM Exposure Index | naaim.org [primary: SEARCH] | ✗ NOT DISCLOSED（無當週數值） |
| institutional.bofa_jpm_survey | 機構 / BofA Fund Manager Survey and JPM institutional survey | BofA / JPM WebSearch | ✗ NOT DISCLOSED（無新一期調查） |
| monetary.fed_funds | 貨幣 / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（DFEDTARU ok、DFEDTARL ok） | ✓ API |
| monetary.hy_oas | 貨幣 / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣 / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣 / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣 / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣 / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直接取得） | ✓ API |
| monetary.wti | 貨幣 / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣 / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣 / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣 / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣 / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok；repo_stress ok） | ✓ API |
| monetary.treasury_auctions | 貨幣 / 美債標售需求（auction tail / bid-to-cover） | Reuters / TreasuryDirect [primary: SEARCH]（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣 / Fed funds rate path expectations | CME FedWatch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣 / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣 / Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | 貨幣 / PBoC aggregate financing / liquidity operations | PBoC / NBS WebSearch | ✗ NOT DISCLOSED（無當期英文摘要） |
| monetary.private_credit_liquidity | 貨幣 / Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]（30d） | ✗ NOT DISCLOSED（30 日內無合格披露） |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | 財報摘要 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI / AI token volume growth rate | 供應商披露 WebSearch | ✓ SEARCH-VERIFIED |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | CNBC / 媒體 WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 [primary: SEARCH] | ✗ NOT DISCLOSED（無當期合格披露） |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | 產業披露 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構（capex vs FCF / 發債） | 財報／發債 [primary: SEARCH]；quarterly_state 沿用最新季、event_scan 30 日掃描無新事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口（revenue-to-capex gap） | 綜合披露 [primary: SEARCH]（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q [primary: SEARCH]（30d） | ✗ NOT DISCLOSED（30 日內無變動披露） |
| ai.capital_cycle | AI / 資本週期階段（capital cycle stage） | 產業披露 [primary: SEARCH]；quarterly_state 沿用、event_scan 30 日掃描無新事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機 / Search for past 7 days: AI rename / SPAC | 新聞／EDGAR WebSearch（7d，zero-result eligible） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機 / IPO market heat | stockanalysis / Renaissance WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機 / Microcap thematic moonshots | Finviz / Benzinga [primary: SEARCH]（7d，zero-result eligible） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機 / Upcoming AI IPOs | 媒體 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機 / Insider selling at AI / market-leadership companies | SEC EDGAR / openinsider（14d，zero-result eligible） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機 / Cboe equity-only put/call ratio | Cboe [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構 / US leveraged ETF AUM | ETF.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構 / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com（30d，zero-result eligible） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | 結構 / Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED（7 日內無英文披露） |
| structural.zero_dte | 結構 / 0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構 / Options total volume | OCC WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構 / Cross-asset derivatives / correlation checks | Cboe / SpotGamma WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構 / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS ok、vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | 結構 / Cross-reference only: FINRA margin debt | FINRA / GuruFocus WebSearch（交叉檢核） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構 / AI infrastructure debt financing / vendor-financing loops | 信用市場 [primary: SEARCH]（30d） | ✗ NOT DISCLOSED（30 日內無新披露） |
| structural.nbfi_bank_loans | 結構 / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構 / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok）；WebSearch 補充無合格事件 | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | trailing P/E ≈26.2、Shiller CAPE ≈41.2 | Shiller CAPE S&P 500 P/E August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus；原定 multpl / GuruFocus） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E ≈29.5x（S&P 500 ≈25.6x） | Magnificent 7 weighted P/E August 2026 | https://www.fool.com/investing/2026/08/14/the-best-magnificent-seven-stocks-to-buy-in-august/（Motley Fool） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| breadth.rsp_spy | RSP 領先 SPY YTD ≈5pp | RSP vs SPY YTD 2026 breadth | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 top-10 集中度 ≈36.5% | S&P 500 top 10 concentration 2026 | https://www.ebc.com/forex/rsp-vs-spy（EBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.advance_decline | 領導由 top-100 向 bottom-400 擴散、廣度確認多頭 | market breadth advance decline August 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 55（Greed） | CNN Fear and Greed today August 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-07 月資料）≈1,417,225（百萬美元）、YoY ≈+38.6%、MoM −5.7% | FINRA margin debt July 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt（GuruFocus；原定 FINRA） | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| retail.aaii | AAII 偏多 35.5%、偏空 39.9%（週結 2026-08-19） | AAII investor sentiment August 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 標售無明顯 tail、12.10% allotted at high | US Treasury 30-year auction August 2026 | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2026/R_20260813_3.pdf（TreasuryDirect） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| monetary.fedwatch | FedWatch 9/16 按兵不動 ≈68.4%、尾端為升息 | CME FedWatch September 2026 hold probability | https://en.macromicro.me/series/1645/probability-fed-rate-decrease（MacroMicro；原定 CME FedWatch） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_capex | top-4 2026 capex 合計 ≈$725bn、+77% YoY（2026Q2 財報季後） | hyperscaler 2026 capex guidance Microsoft Google Amazon Meta | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.token_growth | Anthropic run-rate 年增 ≈7×、API 佔營收多數 | Anthropic token growth revenue 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html（CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.openai_anthropic_revenue | OpenAI ≈$40B、Anthropic ≈$65B run-rate | OpenAI Anthropic annualized revenue August 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html（CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.compute_supply_demand | GPU 現貨租金 > 2× 合約價、產能被利用率吸收 | AI GPU rental pricing utilization August 2026 | https://www.uncoveralpha.com/p/amazon-google-microsoft-meta-q2-earnings（Uncover Alpha） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex > FCF、2026 hyperscaler 發債擴張（capex 由現金流轉向舉債） | hyperscaler external financing capex FCF debt 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow（FactSet） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 ≈$105bn（OpenAI 40＋Anthropic 65）vs 年化 capex ≈$725bn（分母：top-4） | AI revenue to capex gap 2026 | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.capital_cycle | [quarterly_state] 供給側 capex 年增 ≈77%、需求側 token／營收成長並存 | AI capex growth rate supply demand 2026 | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 掃描：0 件合格事件（7 日窗） | AI rename SPAC ticker change August 2026 | Renaissance Capital / SEC EDGAR / 新聞掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD IPO ≈232 件（截至 2026-08-21）、無單週無營收 AI IPO 暴衝 | US IPO count August 2026 | https://stockanalysis.com/ipos/2026/（StockAnalysis） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot（≥100% 單日、<$1B、2+ 主題、弱基本面）：0 檔 | microcap 100% single day surge quantum AI August 2026 | Finviz / Benzinga / StockTwits movers 掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 10 月 IPO、估值 ≈$2T | Anthropic OpenAI IPO 2026 | https://finance.yahoo.com/markets/article/spacex-openai-and-anthropic-here-are-the-most-anticipated-ipos-in-2026-114439441.html（Yahoo Finance） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 14 日內合格 Form 4 集中賣出：0 起 | insider Form 4 AI executives August 2026 | SEC EDGAR / openinsider 掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.52（daily；9 日均總量 0.85） | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio（The Trading Tools；原定 Cboe） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美股槓桿 ETF 總 AUM ≈$198bn 創紀錄；TQQQ 31.3、SOXL 17.3（$bn） | leveraged ETF AUM record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing；原定 etf.com） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| structural.us_single_stock_etf | 單一個股槓桿 ETF 30 日內新核准／上市：0 件 | single-stock leveraged ETF launch SEC August 2026 | SEC EDGAR / ETF.com new launches 掃描 | — | 2026-08-24T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 8 月佔比 ≈62.4% 創紀錄 | 0DTE SPX volume share August 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| structural.options_volume | OCC YTD 日均 > 71M 口、量能高檔 | OCC options volume 2026 | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/historical-volume-statistics（OCC） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 16.01、期限結構 contango（IVTS ≈0.82）、SKEW 偏高 | VIX term structure SKEW August 2026 | https://www.thetrading.tools/vix-term-structure（The Trading Tools；原定 Cboe） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt / 市值交叉檢核（見 retail.margin_debt，YoY +38.6%） | FINRA margin debt equity market cap ratio 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt（GuruFocus） | 2026-07-01 | 2026-08-24T09:30:00+08:00 |

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

> [DRY RUN] this report was not committed to archive.

# 2026-08-20 AI 泡沫破裂預測報告

報告日期：2026-08-20｜ISO 週次：2026-W34｜預測窗口：2026-08-20 → 2027-02-18｜前次基準：report-2026-08-17（3天前）

## 結論

**結論：no**

三條路徑都沒有已啟動的觸發跡象：NASDAQ-100 僅距 52 週高點回撤 4.03%，距 R1 門檻仍需再跌約 21.85%（`valuation.ndx_drawdown`）；hyperscaler top-4 的 2026 capex 合計仍在 ≈$725bn 高位、未見下修（`ai.hyperscaler_capex`），而 HY OAS 2.75%、SOFR−IORB 0bp 顯示信用與資金市場尚無 R3 所需的壓力傳導（`monetary.hy_oas`、`monetary.repo_stress_srf`）。估值與槓桿雖顯示泡沫存在，但 182 天內破裂所需的催化與傳導證據不足以推翻低基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,426.02（2026-08-19），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 4.03%；R1 門檻水位 22,995.45，自最新收盤須再下跌約 21.85% 才會觸及（`valuation.ndx_drawdown`）。同期 S&P 500 收 7,707.98（2026-08-19），高於 200 日均線 8.75%、高於 52 週均線 10.25%，自前次基準日（2026-08-17）以來 −0.48%（`valuation.sp500_trend`）。脆弱度面：Shiller CAPE 41.72、trailing P/E 29.8（`valuation.sp500_pe_cape`），Mag 7 加權本益比 ≈29.5x（`valuation.mag7_multiples`），FINRA margin debt（2026-07 月資料）YoY ≈+38.6%（`retail.margin_debt`），美股槓桿 ETF 總 AUM ≈$198bn 創紀錄（`structural.leveraged_etf_aum`），SPX 0DTE 佔比 ≈62% 創紀錄（`structural.zero_dte`）——下跌一旦啟動，槓桿與選擇權部位會放大跌幅。抑制面：A/D 線創新高、新高多於新低（`breadth.advance_decline`），RSP 領先 SPY YTD ≈5pp（`breadth.rsp_spy`），VIX 15.84（2026-08-18）、7 日窗口內 VIX +3.66% 而 S&P 500 −0.47%，未出現股波同漲（`structural.vix_spx_comove`）；CNN Fear & Greed 56（`retail.fear_greed`）、AAII 偏空 37.9% 高於偏多 34.7%（`retail.aaii`），情緒並非極端亢奮。

**判讀：** R1 距門檻尚遠（回撤 4.03% vs 25%），廣度與波動率結構都不支持近期急跌；要在窗口內觸發，需要一個外生催化（R2 指引下修、R3 信用事件、或通膨／利率衝擊）引發槓桿部位被迫平倉，目前尚未看到這類觸發。

### R2 資本支出收縮

本次取得的 capex 證據為 top-4 合計值：Microsoft、Alphabet、Amazon、Meta 的 2026 capex 合計 ≈$725bn（資料日 2026-08-13，最新一季即 2026 Q2 財報後的彙整；`ai.hyperscaler_capex`）。逐家而言：Microsoft——最新指引含於上述 2026 Q2 財報後合計，個別數值與相較前次指引的方向未於本次證據拆分；Alphabet——同上；Amazon——同上；Meta——同上。本次證據中四家皆無下修披露，已下修家數為 0/4。需求面同步走強：Anthropic 年化營收 $65B、OpenAI $40B（`ai.openai_anthropic_revenue`），Anthropic run-rate 年增 ≈7×、API 佔營收 80%（`ai.token_growth`）；GPU 現貨租金高於合約價 2 倍以上、產能被利用率吸收（`ai.compute_supply_demand`）。風險面：年化 AI 終端營收 ≈$105bn（OpenAI＋Anthropic）vs 年化 capex ≈$725bn（分母：top-4），缺口仍大（`ai.revenue_capex_gap`）。窗口（至 2027-02-18）內四家各還有兩次季報（9 月季與 12 月季），具體日期未在本次證據中取得。

**判讀：** R2 目前 0/4，且需求端（營收、token、GPU 租金）同步走強，短期沒有下修壓力；要在窗口內觸發，需至少兩家在接下來兩輪季報中主動下修——通常以需求放緩或資金成本驟升為前提，目前證據指向相反方向。

### R3 AI 信用事件

本次 AI 信用定價分歧與 AI infrastructure debt financing / vendor-financing loops 的 14／30 日掃描均已完成但無合格披露，因此沒有個別 AI 資料中心借款人（CoreWeave、neocloud 等）的當期債券殖利率、CDS、評等動作或到期牆可引用，也沒有違約、豁免、distressed exchange 或 going-concern 語句的報導。可用的整體信用讀數：HY OAS 2.75%（2026-08-18，自前次基準 +5bp；`monetary.hy_oas`），IG OAS 0.82%（+1bp；`monetary.ig_oas`），兩者皆處於歷史偏窄區；repo 資金壓力（SOFR−IORB）為 0bp、SOFR99−IORB 7bp（皆 2026-08-18），SRF 動用（Standing Repo Facility usage）僅 $0.001bn（2026-08-19，與利差腿相差一日）（`monetary.repo_stress_srf`）；MOVE 71.26（2026-08-19，較 2026-08-17 −4.37），槓桿基金美債期貨淨空 −7,250,927 口（2026-08-11，4 週淨空減少 311,947 口）（`structural.treasury_basis_trade`）；銀行對 NBFI 放款 $2.02T（2026-08-05，無新觀測）（`structural.nbfi_bank_loans`）。

**判讀：** R3 沒有任何可辨識的接近跡象——整體信用利差偏窄、資金市場平穩；要在窗口內觸發，需要一個大型 AI 算力借款人出現再融資失敗或客戶合約違約，並先在信用利差／CDS 上顯現，目前這兩個前導訊號都不存在（但借款人層級的定價本次無資料，見缺漏段）。

## 支持 yes 的證據

- [整體] 估值處於歷史極端：Shiller CAPE 41.72、S&P 500 trailing P/E 29.8（2026-08-19），Mag 7 加權本益比 ≈29.5x（2026-08-14），代表若有催化，下行空間很大（`valuation.sp500_pe_cape`、`valuation.mag7_multiples`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）巨大：年化 AI 終端營收 ≈$105bn（OpenAI＋Anthropic）vs 年化 capex ≈$725bn（分母：top-4），資料日 2026-08-17；若營收成長放緩，資本回收壓力會直接轉為 capex 指引壓力（`ai.revenue_capex_gap`）。
- [R1] 槓桿與投機部位偏高：FINRA margin debt（2026-07 月資料）YoY ≈+38.6%，逼近歷史頂部常見的 +40–50% 區；美股槓桿 ETF 總 AUM ≈$198bn 創紀錄（TQQQ $37.3bn、SOXL $17.3bn，2026-08-17）；SPX 0DTE 佔比 ≈62% 創紀錄（2026-08-14），一旦下跌易被放大（`retail.margin_debt`、`structural.leveraged_etf_aum`、`structural.zero_dte`）。
- [R1] 機構部位擁擠：BofA 8 月 FMS 現金水位 3.5%，最擁擠交易為做多半導體（53%），2026-08-18（`institutional.bofa_jpm_survey`）。
- [R1] 價格延伸：S&P 500 高於 200 日均線 8.75%、高於 52 週均線 10.25%（2026-08-19），均值回歸風險偏高（`valuation.sp500_trend`）。
- [整體] Fed 緩衝空間受限：CPI YoY 3.3%（2026-07 月資料），5y5y 通膨預期 2.32%（2026-08-19），10Y 期限溢價（term premium）0.8393%（2026-08-14，trailing 7 日 +1.4bp），10Y 殖利率 4.71%——若 AI 領跌，降息托底的空間有限（`monetary.cpi_yoy`、`monetary.t5yifr`、`monetary.term_premium`、`monetary.dgs10`）。
- [R1] 巨型 AI IPO 供給：Anthropic 目標 10 月 IPO、估值 ≈$2T（2026-08-17），落在窗口內，可能成為情緒頂點或吸走流動性（`speculation.upcoming_ai_ipos`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.03%（2026-08-19 收盤 29,426.02 vs 2026-06-02 高點 30,660.6），距 R1 門檻 22,995.45 仍需再跌約 21.85%（`valuation.ndx_drawdown`）。
- [R2] hyperscaler top-4 2026 capex 合計 ≈$725bn（2026-08-13），本次證據中四家皆無下修，已下修 0/4（`ai.hyperscaler_capex`）。
- [R2] 需求端同步加速：Anthropic 年化營收 $65B、OpenAI $40B（2026-08-17），Anthropic run-rate 年增 ≈7×；GPU 現貨租金 > 2× 合約價、產能被利用率吸收（2026-08-13），與產能過剩相反（`ai.openai_anthropic_revenue`、`ai.token_growth`、`ai.compute_supply_demand`）。
- [R3] 信用與資金市場平穩：HY OAS 2.75%、IG OAS 0.82%（2026-08-18）；SOFR−IORB 0bp、SOFR99−IORB 7bp（2026-08-18）、SRF 動用 $0.001bn（2026-08-19）；MOVE 71.26 下滑（2026-08-19），無 R3 所需的信用重定價前導訊號（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`、`structural.treasury_basis_trade`）。
- [R1] 廣度健康、波動率平靜：A/D 線創新高、新高多於新低（2026-08-14），RSP 領先 SPY YTD ≈5pp；VIX 15.84、7 日窗口未出現股波同漲（comove false，2026-08-11 → 2026-08-18）（`breadth.advance_decline`、`breadth.rsp_spy`、`structural.vix_spx_comove`）。
- [整體] 散戶情緒未達亢奮：CNN Fear & Greed 56（2026-08-19）、AAII 偏空 37.9% > 偏多 34.7%（2026-08-12）；投機篩選本週 0 件 +AI 改名／SPAC、0 檔 microcap moonshot，IPO 週報無無營收 AI IPO 暴衝（`retail.fear_greed`、`retail.aaii`、`speculation.ai_rename_spac`、`speculation.microcap_moonshots`、`speculation.ipo_heat`）。

## 與前期比較

前次結論：無前次預測（report-2026-08-17 為舊格式評分報告）

report-2026-08-17 為改版前的舊格式評分報告，其分數不轉譯為 yes/no，因此本次為新格式下的第一個預測，flip_evidence 為空。自 2026-08-17 以來的主要變化：NASDAQ-100 由 29,995.38 回落至 29,426.02；S&P 500 −0.48%；HY OAS +5bp 至 2.75%；10Y 殖利率 −1bp 至 4.71%（ΔDFII10 −3bp、ΔT10YIE +2bp，視窗不一致，判讀：不可判（視窗不一致））；MOVE 由 75.63 降至 71.26。這些變化幅度都小，未改變三條路徑的距離判斷。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下 optional 來源完成檢索但無合格當期披露（✗ NOT DISCLOSED），及其對結論的影響：

- `valuation.ai_credit_schism`、`structural.ai_infrastructure_debt`：R3 最直接的兩個借款人層級來源皆無 14／30 日內披露，R3 只能以整體 HY／IG OAS 與 repo 讀數間接判斷。若存在未被報導的大型 neocloud 利差急升，可能改變 R3 判讀，但目前整體信用利差沒有任何外溢跡象，判斷此缺口不太可能翻轉結論。
- `ai.hyperscaler_financing_mix`（quarterly_state 可用：FactSet 2026-08-17 顯示 capex > FCF、2026 hyperscaler IG 發債 ≈$182bn、+1300%；event_scan 30 日無新案）與 `ai.capital_cycle`（quarterly_state 可用：供給側 capex 年增 ≈77%；event_scan 30 日無取消／延後事件）：組合狀態為 ✗ NOT DISCLOSED，故不作為正文證據；季頻背景顯示 hyperscaler 已轉向舉債融資 capex，是中期 R3／R2 脆弱度來源，但窗口內未見事件。
- `valuation.analyst_tp_decomposition`、`retail.social_sentiment`、`retail.naaim`、`monetary.pboc`、`monetary.private_credit_liquidity`、`ai.customer_concentration_rpo`、`ai.depreciation_life`、`structural.global_leveraged_approvals`：皆無合格當期披露；其中私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）與 backlog 重複計算風險（RPO double-counting）若出現負面披露會偏向 yes，但目前沒有證據，不改變結論。
- R2 逐家指引：本次 `ai.hyperscaler_capex` 證據只有 top-4 合計值，未拆分到逐家指引數值與方向；若其中有一家已在 Q2 財報小幅下修而合計被其他三家上修掩蓋，R2 距離會比本報告描述的更近，但仍需第二家下修才會觸發。

最大不確定性：

1. 未來兩輪 hyperscaler 季報（窗口內，日期未取得）：若需求放緩導致兩家下修，R2 會直接觸發並可能拖動 R1——偏向 yes。
2. Anthropic 10 月 IPO（估值 ≈$2T）：成功定價會延續情緒（偏 no）；若定價失敗或延後，可能成為 R1 催化——偏 yes。
3. 通膨與利率：CPI 3.3%、期限溢價走升，若長端利率急升壓縮估值，是 R1 的外生觸發路徑——偏 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 41.72 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 29.8 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權本益比 | ≈29.5x | https://www.fool.com/investing/2026/08/14/the-best-magnificent-seven-stocks-to-buy-in-august/ | 2026-08-14 | 2026-08-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7707.98 | FRED API (series_id=SP500) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 8.75 | FRED API (series_id=SP500) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 10.25 | FRED API (series_id=SP500) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較 2026-08-17 %） | -0.48 | FRED API (series_id=SP500) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29426.02 | FRED API (series_id=NASDAQ100) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.03 | FRED API (series_id=NASDAQ100) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP 領先 SPY YTD | ≈5pp | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 top-10 集中度 | ≈40% | https://www.ebc.com/forex/rsp-vs-spy | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed | 56（Greed） | https://www.cnn.com/markets/fear-and-greed | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）YoY | ≈+38.6% | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt | 2026-07-01 | 2026-08-20T09:30:00+08:00 |
| retail.aaii | AAII 偏空 / 偏多 | 37.9% / 34.7% | https://www.aaii.com/sentimentsurvey | 2026-08-12 | 2026-08-20T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q1，家庭股票佔金融資產 %） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-20T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA 8 月 FMS 現金水位 / 做多半導體擁擠度 | 3.5% / 53% | https://www.hedgefundtips.com/august-2026-bank-of-america-global-fund-manager-survey-results-summary/ | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（上限） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（下限） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.75 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.82 | FRED API (series_id=BAMLC0A0CM) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.71 | FRED API (series_id=DGS10) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（vs 2026-08-17） | -1.0 | FRED API (series_id=DGS10) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.41 | FRED API (series_id=DFII10) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps（vs 2026-08-17） | -3.0 | FRED API (series_id=DFII10) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.3 | FRED API (series_id=T10YIE) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps（vs 2026-08-17） | 2.0 | FRED API (series_id=T10YIE) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 86.48 | FRED API (series_id=DCOILWTICO) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-20T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.32 | FRED API (series_id=T5YIFR) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8393 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.65 | FRED API (series_id=SOFR) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.72 | FRED API (series_id=SOFR99) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-08-20 | 2026-08-20T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.001 | FRED API (series_id=RPONTTLD) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps（SOFR−IORB，as_of） | 0.0 | FRED API (series_id=SOFR, IORB) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 標售 bid-to-cover | 2.39 | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2026/R_20260813_2.pdf | 2026-08-13 | 2026-08-20T09:30:00+08:00 |
| monetary.fedwatch | FedWatch 9/16 按兵不動 | ≈65.4% | https://www.cnbc.com/2026/08/07/odds-the-fed-hikes-in-september-tumble-following-big-july-jobs-miss.html | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,759,955（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-12 | 2026-08-20T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,927,307（€5.93T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-14 | 2026-08-20T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,442,957（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-20T09:30:00+08:00 |
| ai.hyperscaler_capex | top-4 2026 capex 合計（$bn） | ≈725 | https://valueaddvc.com/ai-spending | 2026-08-13 | 2026-08-20T09:30:00+08:00 |
| ai.token_growth | Anthropic run-rate 年增 / API 佔營收 | ≈7× / 80% | https://techcrunch.com/2026/08/17/anthropics-annualized-revenue-surges-to-65b/ | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic / OpenAI 年化營收（$B） | 65 / 40 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| ai.compute_supply_demand | GPU 現貨租金 / 合約價 | > 2× | https://www.uncoveralpha.com/p/amazon-google-microsoft-meta-q2-earnings | 2026-08-13 | 2026-08-20T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 vs 年化 capex（$bn，分母 top-4） | ≈105 vs ≈725 | https://valueaddvc.com/ai-spending | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 目標估值 | ≈$2T（目標 10 月） | https://finance.yahoo.com/markets/article/spacex-openai-and-anthropic-here-are-the-most-anticipated-ipos-in-2026-114439441.html | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call | 0.65 | https://www.thetrading.tools/put-call-ratio | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美股槓桿 ETF 總 AUM / TQQQ / SOXL（$bn） | ≈198 / 37.3 / 17.3 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比 | ≈62% | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august | 2026-08-14 | 2026-08-20T09:30:00+08:00 |
| structural.options_volume | OCC 7 月總量 YoY | +26% | https://mondovisione.com/media-and-resources/news/occ-july-2026-monthly-volume-data-202686 | 2026-07-31 | 2026-08-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX（期限結構 contango、SKEW 偏高） | 15.84 | https://www.thetrading.tools/vix-term-structure | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.84 | FRED API (series_id=VIXCLS) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of；comove false） | 15.84 | FRED API 衍生（vix_spx_comove） | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日窗口，base 2026-08-11） | 3.66 | FRED API 衍生（vix_spx_comove） | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日窗口，base 2026-08-11） | -0.47 | FRED API 衍生（vix_spx_comove） | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt / 市值 交叉檢核 YoY | +38.6% | https://kalkine.com/news/financial/finra-margin-debt-hits-record-15-trillion-ratio-climbs-to-340 | 2026-07-01 | 2026-08-20T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2016.0821（$2.02T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-05 | 2026-08-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7,250,927 | CFTC TFF (cftc_lev_funds) | 2026-08-11 | 2026-08-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 311,947 | CFTC TFF (cftc_lev_funds) | 2026-08-11 | 2026-08-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 71.26 | Yahoo Finance chart API ^MOVE (move_index) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2361.6 | OFR STFM REPO-TRIV1_TV_TOT-P (ofr_repo) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值 / S&P 500 P/E and Shiller CAPE | multpl / GuruFocus，WebSearch primary | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值 / Mag 7 weighted P/E and AI leader P/S | 市場資料，WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值 / Analyst TP upgrade decomposition | 賣方 TP 摘要，WebSearch（90d＋同季） | ✗ NOT DISCLOSED（無合格同季上調） |
| valuation.sp500_trend | 估值 / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500，sp500_trend） | ✓ API |
| valuation.ndx_drawdown | 估值 / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100，ndx_drawdown） | ✓ API |
| valuation.ai_credit_schism | 估值 / AI 信用定價分歧 | 信用市場報導，WebSearch（14d） | ✗ NOT DISCLOSED（14 日內無合格報導） |
| breadth.rsp_spy | 廣度 / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 市場資料，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度 / Top-10 concentration in S&P 500 | 市場資料，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度 / Advance/decline ratio, new high/low ratio | StockCharts，WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶 / CNN Fear & Greed Index | CNN，WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶 / Margin Debt: FINRA monthly data | FINRA / GuruFocus，WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶 / Retail survey: AAII Investor Sentiment | AAII，WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶 / Social sentiment proxies | WSB / X，WebSearch（7d） | ✗ NOT DISCLOSED（無顯著討論） |
| retail.household_equity_allocation | 散戶 / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶 / NAAIM Exposure Index | naaim.org，WebSearch | ✗ NOT DISCLOSED（無當週值） |
| institutional.bofa_jpm_survey | 機構 / BofA Fund Manager Survey and JPM institutional survey | BofA / JPM，WebSearch | ✓ SEARCH-VERIFIED |
| monetary.fed_funds | 貨幣 / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（FRED API） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣 / High Yield OAS | scripts/fetch_macro.py（FRED BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣 / Investment Grade OAS | scripts/fetch_macro.py（FRED BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣 / 10Y Treasury yield | scripts/fetch_macro.py（FRED DGS10） | ✓ API |
| monetary.dfii10 | 貨幣 / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED DFII10） | ✓ API |
| monetary.t10yie | 貨幣 / 10Y breakeven inflation rate | scripts/fetch_macro.py（FRED T10YIE，FRED-direct） | ✓ API |
| monetary.wti | 貨幣 / WTI crude oil price | scripts/fetch_macro.py（FRED DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣 / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（FRED CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣 / 5y5y forward inflation expectation | scripts/fetch_macro.py（FRED T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣 / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（FRED THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣 / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（FRED API，repo_stress） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣 / 美債標售需求（auction tail / bid-to-cover） | TreasuryDirect / Reuters，WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣 / Fed funds rate path expectations | CME FedWatch 摘要，WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣 / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（FRED WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣 / Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（FRED ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣 / PBoC aggregate financing / liquidity operations | PBoC / NBS 英文摘要，WebSearch | ✗ NOT DISCLOSED（無當期英文摘要） |
| monetary.private_credit_liquidity | 貨幣 / Private-credit / non-bank fund liquidity stress | BDC / interval fund 披露，WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無合格披露） |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | 財報摘要，WebSearch（stock-of-state，沿用 2026 Q2 財報） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI / AI token volume growth rate | 供應商披露，WebSearch | ✓ SEARCH-VERIFIED |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | CNBC / The Information，WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話會，WebSearch | ✗ NOT DISCLOSED（無合格披露） |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | 產業披露，WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：FactSet 季頻；event_scan：30 日發債／私募信貸／SPV 掃描，WebSearch | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口（revenue-to-capex gap） | 綜合披露，WebSearch（分母 top-4） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動 | 10-K / 10-Q / 法說會，WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無變動） |
| ai.capital_cycle | AI / 資本週期階段（capital cycle stage） | quarterly_state：供需增速披露；event_scan：30 日進出場事件掃描，WebSearch | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機 / Search for past 7 days: AI rename / SPAC | 新聞 / SEC EDGAR，WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機 / IPO market heat | Renaissance Capital，WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機 / Microcap thematic moonshots | Finviz / Benzinga / StockTwits，WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機 / Upcoming AI IPOs | Yahoo Finance / Bloomberg，WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機 / Insider selling at AI / market-leadership companies | SEC EDGAR / openinsider，WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機 / Cboe equity-only put/call ratio | Cboe / thetrading.tools，WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構 / US leveraged ETF AUM | ETF.com，WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構 / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com，WebSearch（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | 結構 / Global leveraged product approvals | KRX / TWSE / JPX / ESMA，WebSearch（7d） | ✗ NOT DISCLOSED（7 日內無英文披露） |
| structural.zero_dte | 結構 / 0DTE option volume | Cboe，WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構 / Options total volume | OCC 月報，WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構 / Cross-asset derivatives / correlation checks | Cboe / thetrading.tools，WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構 / VIX / S&P 500 co-movement | scripts/fetch_macro.py（FRED VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構 / Cross-reference only: FINRA margin debt | FINRA / Kalkine，WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構 / AI infrastructure debt financing / vendor-financing loops | 信用市場報導，WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無新披露） |
| structural.nbfi_bank_loans | 結構 / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構 / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）＋ WebSearch | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok；WebSearch 無額外合格披露） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | trailing P/E 29.8、Shiller CAPE 41.72（原定來源：multpl / GuruFocus） | S&P 500 Shiller CAPE August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.mag7_multiples | Magnificent 7 加權本益比 ≈29.5x | Magnificent 7 weighted P/E August 2026 | https://www.fool.com/investing/2026/08/14/the-best-magnificent-seven-stocks-to-buy-in-august/（The Motley Fool） | 2026-08-14 | 2026-08-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP 領先 SPY YTD ≈5pp | RSP vs SPY YTD 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 top-10 集中度 ≈40% | S&P 500 top 10 concentration 2026 | https://www.ebc.com/forex/rsp-vs-spy（EBC） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| breadth.advance_decline | A/D 線創新高、新高 > 新低，3 項廣度訊號確認多頭 | NYSE advance decline breadth August 2026 | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/（StockCharts） | 2026-08-14 | 2026-08-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 56（Greed） | CNN Fear and Greed today August 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-07 月資料）YoY ≈+38.6%，水位 ≈1,417,225（原定來源：FINRA） | FINRA margin debt July 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt（GuruFocus） | 2026-07-01 | 2026-08-20T09:30:00+08:00 |
| retail.aaii | AAII 偏空 37.9%、偏多 34.7% | AAII investor sentiment August 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-08-12 | 2026-08-20T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA 8 月 FMS：現金 3.5%、最擁擠做多半導體 53% | BofA fund manager survey August 2026 | https://www.hedgefundtips.com/august-2026-bank-of-america-global-fund-manager-survey-results-summary/（HedgeFundTips） | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 標售 bid-to-cover 2.39、無明顯 tail | US Treasury 30-year auction August 2026 | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2026/R_20260813_2.pdf（TreasuryDirect） | 2026-08-13 | 2026-08-20T09:30:00+08:00 |
| monetary.fedwatch | FedWatch 9/16 按兵不動 ≈65.4%（原定來源：CME FedWatch） | CME FedWatch September 2026 hold probability | https://www.cnbc.com/2026/08/07/odds-the-fed-hikes-in-september-tumble-following-big-july-jobs-miss.html（CNBC） | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| ai.hyperscaler_capex | top-4（MSFT／GOOGL／AMZN／META）2026 capex 合計 ≈$725bn | hyperscaler 2026 capex guidance Microsoft Google Amazon Meta | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-13 | 2026-08-20T09:30:00+08:00 |
| ai.token_growth | Anthropic run-rate 年增 ≈7×、API 佔營收 80% | Anthropic token growth revenue 2026 | https://techcrunch.com/2026/08/17/anthropics-annualized-revenue-surges-to-65b/（TechCrunch） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| ai.openai_anthropic_revenue | OpenAI $40B、Anthropic $65B run-rate | OpenAI Anthropic annualized revenue August 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html（CNBC） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| ai.compute_supply_demand | GPU 現貨租金 > 2× 合約價、產能被利用率吸收 | AI GPU rental pricing utilization August 2026 | https://www.uncoveralpha.com/p/amazon-google-microsoft-meta-q2-earnings（UncoverAlpha） | 2026-08-13 | 2026-08-20T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] capex > FCF、2026 hyperscaler IG 發債 ≈$182bn（+1300%） | hyperscaler external financing capex FCF debt 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow（FactSet） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| ai.revenue_capex_gap | OpenAI 40＋Anthropic 65 → ≈$105bn vs 年化 capex ≈$725bn（分母：top-4） | AI revenue to capex gap 2026 | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| ai.capital_cycle | [quarterly_state] 供給側 capex 年增 ≈77%、需求側 token／營收成長並存 | AI capex growth rate supply demand 2026 | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-13 | 2026-08-20T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描：0 件合格 | AI rename SPAC ticker change August 2026 | Renaissance Capital / SEC EDGAR / 新聞掃描 | — | 2026-08-20T09:30:00+08:00 |
| speculation.ipo_heat | US IPO 週報：pipeline 擴大、Metals Royalty 直接上市；無營收 AI IPO 暴衝 0 起 | US IPO weekly recap August 2026 | https://www.renaissancecapital.com/IPO-Center/News/118238/US-IPO-Weekly-Recap-Pipeline-swells-with-sizable-IPO-filings-as-Metals-Roya（Renaissance Capital） | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot（≥100% 單日、<$1B、2+ 主題、弱基本面）7 日掃描：0 檔 | microcap 100% single day surge quantum AI August 2026 | Finviz / Benzinga / StockTwits movers 掃描 | — | 2026-08-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 10 月 IPO、估值 ≈$2T | Anthropic OpenAI IPO 2026 | https://finance.yahoo.com/markets/article/spacex-openai-and-anthropic-here-are-the-most-anticipated-ipos-in-2026-114439441.html（Yahoo Finance） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 14 日內合格 Form 4 集中賣出：0 起 | insider Form 4 AI executives August 2026 | SEC EDGAR / openinsider 掃描 | — | 2026-08-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.65 | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio（thetrading.tools） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美股槓桿 ETF 總 AUM ≈$198bn 創紀錄；TQQQ 37.3、SOXL 17.3（$bn）（原定來源：etf.com） | leveraged ETF AUM record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| structural.us_single_stock_etf | 美單一個股槓桿 ETF 30 日新核准／上市掃描：0 件 | single-stock leveraged ETF launch SEC August 2026 | SEC EDGAR / ETF.com new launches 掃描 | — | 2026-08-20T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 8 月創紀錄 ≈62% 佔比 | 0DTE SPX volume share August 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-14 | 2026-08-20T09:30:00+08:00 |
| structural.options_volume | OCC 7 月總量 +26% YoY、YTD 日均 > 71M 口 | OCC July 2026 options volume | https://mondovisione.com/media-and-resources/news/occ-july-2026-monthly-volume-data-202686（Mondo Visione） | 2026-07-31 | 2026-08-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 15.84、期限結構 contango、SKEW 偏高 | VIX term structure SKEW August 2026 | https://www.thetrading.tools/vix-term-structure（thetrading.tools） | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt / 市值 交叉檢核（YoY +38.6%，見 retail.margin_debt） | FINRA margin debt equity market cap ratio 2026 | https://kalkine.com/news/financial/finra-margin-debt-hits-record-15-trillion-ratio-climbs-to-340（Kalkine） | 2026-07-01 | 2026-08-20T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-20",
  "iso_week": "2026-W34",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-18",
  "prior_date": "2026-08-17",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 4.03,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

> [DRY RUN] this report was not committed to archive.

# 2026-08-27 AI 泡沫破裂預測報告
報告日期：2026-08-27｜ISO 週次：2026-W35｜預測窗口：2026-08-27 → 2027-02-25｜前次基準：report-2026-08-24（3天前）

## 結論

**結論：no**

三條路徑都沒有已在進行中的跡象：NASDAQ-100 距 52 週高點回撤 4.68%，離 R1 門檻還差約 21% 的跌幅；top-4 hyperscaler 2026 capex 合計 ≈$725bn（+77% YoY），本次來源沒有任何一家下修指引（R2）。信用端 HY OAS 2.70%、repo 資金壓力（SOFR−IORB）僅 1bp，看不到 R3 所需的傳導。高估值與槓桿只說明泡沫存在且下行空間大，還不足以推翻「182 天內不破裂」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,224.52（2026-08-26），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 4.68%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，需自最新收盤再跌 ≈21.31% 才會觸及。S&P 500 收 7,675.7（2026-08-26），高於 200 日均線 7.97%、高於 52 週均線 9.4%（`valuation.sp500_trend`），價格延伸偏高但並非極端。VIX 15.45（2026-08-25），近 7 日 VIX −2.46%、S&P 500 −0.19%，沒有出現「股價與波動同漲」的 crowded-optionality 讀數（`structural.vix_spx_comove`）；MOVE 69.44（2026-08-26），較前次基準的 73.98 回落（`structural.treasury_basis_trade`）。

**判讀：** R1 距門檻還很遠。窗口內要觸發，需要一個能讓 NASDAQ-100 自高點再跌兩成以上的催化劑，例如信用重定價、hyperscaler 財報引發 capex 回收疑慮，或大型 AI IPO 帶來的股票供給衝擊，而且必須與估值壓縮同時發生。目前的波動與信用讀數都沒有顯示這種情境正在醞釀。

### R2 資本支出收縮

本次取得的 hyperscaler capex 資料是彙總數：top-4（MSFT、GOOGL、AMZN、META）2026 capex 合計 ≈$725bn，年增 +77%，資料日期 2026-08-13，對應各家 2026 年 7–8 月的 Q2 財報期（`ai.hyperscaler_capex`）。來源沒有逐家列出最新指引數字和相對前次指引的方向，因此 Microsoft、Alphabet、Amazon、Meta 各自是上修、持平或下修，本次無法逐一確認；但來源中也沒有任何一家下修的披露，目前已知下修家數為 0 家。下一輪財報日期本次來源沒有提供；依季報節奏，Q3 與 Q4 兩次財報都落在窗口內，但具體日期未在來源中確認。需求面上，GPU 現貨租金仍高於合約價 2 倍以上，產能被利用率吸收（`ai.compute_supply_demand`）。

**判讀：** R2 目前沒有起步。四家合計仍以 +77% 擴張，GPU 租金也未見產能過剩。要在窗口內成立，需要兩家以上在 Q3 或 Q4 財報中下修指引，這通常要先出現 R1 式的市場衝擊或明確的需求轉弱，現在都看不到。

### R3 AI 信用事件

本次唯一在窗口內的 AI infrastructure debt financing / vendor-financing loops 事件，是 CoreWeave 於 2026-08-10 完成一筆 $2.6B 的 delayed-draw 定期貸款設施，以 HPC 基礎設施為擔保（`structural.ai_infrastructure_debt`）。能取得新融資本身說明信用市場仍向其開放，不是困境訊號。CoreWeave 的總負債是否達到 R3 的 ≥ 50 億美元門檻，本次來源沒有提供，屬未確立數字。AI 信用定價分歧（equity-vs-credit schism）這一項，本次在 14 日窗內沒有找到 AI 發行人債券利差、CDS 或評等動作的合格披露，因此沒有 AI 專屬的信用定價讀數。整體信用環境方面，HY OAS 2.70%（`monetary.hy_oas`）、IG OAS 0.81%（`monetary.ig_oas`），都在偏緊水位；repo 資金壓力（SOFR−IORB）1bp，SRF 動用（Standing Repo Facility usage）僅 $0.003bn（`monetary.repo_stress_srf`）。

**判讀：** R3 沒有任何違約、展延或 distressed exchange 的訊號，借款人仍在順利新增融資。要在窗口內成立，需要某個規模夠大的 AI 資料中心借款人在再融資時碰壁，而且前提是信用利差先明顯走闊。目前 HY OAS 處於低檔，這條路徑最遠。

## 支持 yes 的證據

- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）仍大：已披露的年化 AI 終端營收 ≈$105bn（OpenAI ≈$40bn＋Anthropic ≈$65bn），對比年化 capex ≈$725bn（分母：top-4，未含 Oracle 與 neocloud），缺口顯示回本仰賴未來成長（`ai.revenue_capex_gap`，2026-08-17；`ai.openai_anthropic_revenue`，2026-08-17）。
- [R1] 估值偏高、延伸幅度大：Shiller CAPE ≈41.3、trailing P/E ≈26.2（`valuation.sp500_pe_cape`，2026-08-26）；Mag 7 加權本益比 ≈29.5x（`valuation.mag7_multiples`，2026-08-26）；S&P 500 高於 200 日均線 7.97%（`valuation.sp500_trend`，2026-08-26）。這些說明一旦下跌，跌幅可能很大。
- [R1] 散戶槓桿與投機性選擇權部位偏高：FINRA margin debt 1,417,225（2026-07 月資料），YoY +38.6%（`retail.margin_debt`）；SPX 0DTE 占比 8 月創紀錄 ≈62.4%（`structural.zero_dte`，2026-08-14）；美股槓桿 ETF 總 AUM ≈$198bn，其中 TQQQ ≈$37bn、SOXL ≈$22bn（`structural.leveraged_etf_aum`，2026-08-17）。被迫去槓桿時會放大 R1 跌幅。
- [R1] 窗口內有潛在的股票供給衝擊：報導指 Anthropic 目標 10 月 IPO、估值 ≈$2T（`speculation.upcoming_ai_ipos`，2026-08-17），可能從現有 AI 持股抽走資金。
- [R3] AI 基建持續以債務擴張：CoreWeave 於 2026-08-10 完成 $2.6B delayed-draw 定期貸款設施（`structural.ai_infrastructure_debt`），反映 AI infrastructure debt financing / vendor-financing loops 的槓桿仍在累積。
- [整體] 財政與期限端有壓力：10Y 期限溢價（term premium）0.8682%（2026-08-21，trailing 7 日 +2.9bp）（`monetary.term_premium`）；CPI YoY 3.3%（2026-07）（`monetary.cpi_yoy`），限制了 Fed 在 AI 主導的下跌中出手緩衝的空間。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.68%（2026-08-26），距 R1 門檻 22,995.45 還差 ≈21.31% 的跌幅（`valuation.ndx_drawdown`）。
- [R2] top-4 hyperscaler 2026 capex 合計 ≈$725bn、+77% YoY，本次來源沒有任何一家下修（`ai.hyperscaler_capex`，2026-08-13）；GPU 現貨租金高於合約價 2 倍以上、產能被利用率吸收，看不到過剩（`ai.compute_supply_demand`，2026-08-13）。
- [R3] 信用與資金市場平穩：HY OAS 2.70%（`monetary.hy_oas`，2026-08-25）、IG OAS 0.81%（`monetary.ig_oas`，2026-08-25）；repo 資金壓力（SOFR−IORB）1bp、SOFR99−IORB 9bp、SRF 動用 $0.003bn（`monetary.repo_stress_srf`）；銀行對 NBFI 放款 $2.03T 持平（`structural.nbfi_bank_loans`，2026-08-12）。
- [整體] 避險與波動指標沒有警訊：VIX 15.45，近 7 日沒有股價與波動同漲（`structural.vix_spx_comove`，2026-08-25）；MOVE 69.44，前次基準為 73.98（`structural.treasury_basis_trade`，2026-08-26）；槓桿基金美債期貨淨空部位 4 週縮減 244,468 口（`structural.treasury_basis_trade`，2026-08-18）。
- [整體] 情緒不在極端狂熱區：CNN Fear & Greed 55（Greed）（`retail.fear_greed`，2026-08-25）；AAII 偏多 35.5%、偏空 39.9%（`retail.aaii`，2026-08-19）；等權 RSP 領先 SPY ≈1.7pp、新高多於新低（`breadth.rsp_spy`；`breadth.advance_decline`，2026-08-23），漲勢擴散、並非只靠少數龍頭。
- [整體] 投機篩選沒有發現熱點：7 日窗內 +AI 改名／SPAC 0 件（`speculation.ai_rename_spac`）、microcap moonshot 0 檔（`speculation.microcap_moonshots`）、14 日內 AI 領導股合格 Form 4 集中賣出 0 起（`speculation.insider_form4`）；2026 YTD IPO ≈235 件，沒有出現單週無營收 AI IPO 暴衝（`speculation.ipo_heat`，2026-08-26）。

## 與前期比較

前次結論：無前次預測（report-2026-08-24 為舊格式評分報告）

前次是舊格式評分報告，不轉換成 yes/no；本次 `flip_evidence` 為空。自 2026-08-24 以來的主要變化：

- DGS10 −6bp 至 4.64%、DFII10 −6bp 至 2.32%（`monetary.dgs10`；`monetary.dfii10`）；T10YIE 持平於 2.32%，但其觀測視窗與前兩者不同，Δ 分解判讀為 不可判（視窗不一致）（`monetary.t10yie`）。
- HY OAS +1bp 至 2.70%，IG OAS 持平（`monetary.hy_oas`；`monetary.ig_oas`）。
- MOVE 自 73.98 降至 69.44；OFR tri-party repo transaction volume $2,368.0bn，+0.62%（`structural.treasury_basis_trade`）。
- S&P 500 +0.3%；WTI 自 86.34 降至 83.9，−2.83%（`valuation.sp500_trend`；`monetary.wti`）。
- WALCL、ECB/BOJ 資產負債表與銀行對 NBFI 放款都沒有新觀測（`monetary.walcl`；`monetary.ecb_boj`；`structural.nbfi_bank_loans`）。

以上變化都不足以讓任何一條路徑轉為進行中。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下項目的檢索都正常完成，但沒有合格披露（✗ NOT DISCLOSED），均不影響本次答案：
- valuation.analyst_tp_decomposition、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.treasury_auctions、monetary.pboc、ai.customer_concentration_rpo、ai.depreciation_life、structural.global_leveraged_approvals：都屬輔助訊號，不影響路徑判讀。
- valuation.ai_credit_schism：缺少 AI 專屬的債券利差／CDS 讀數，是 R3 判讀最大的資訊缺口。若補到的資料顯示 AI 發行人利差明顯走闊，會削弱 no 的信心，但單憑利差走闊還不足以構成 R3。
- monetary.private_credit_liquidity：30 日內沒有找到私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）的合格披露，因此無法確認 redemption-request ratio 的趨勢。
- ai.token_growth：唯一找到的是 Anthropic 營收 run-rate 年增 ≈7×，不是 token volume 指標，判定為未披露。
- ai.hyperscaler_financing_mix 與 ai.capital_cycle：quarterly_state 可用（top-5 capex 已超過 FCF、2026 發債擴張；供給側 capex 年增 ≈77%），但 30 日 event_scan 沒有新事件，依 component_aggregation: all 判為 ✗ NOT DISCLOSED，不作為主證據。

最大的不確定性：
1. 窗口內的 Q3 與 Q4 hyperscaler 財報：若兩家以上下修 capex 指引，R2 會直接成立，答案會轉向 yes；目前合計 +77% 的擴張不支持這個情境。
2. AI 大型 IPO（報導中 Anthropic 目標 10 月）帶來的股票供給，以及 IPO 後的定價表現：若引發 AI 板塊重新定價，會推動 R1 往 yes 方向移動。
3. AI 基建借款人的總負債與再融資時程沒有建立：CoreWeave 等借款人是否超過 50 億美元門檻，以及近期到期債務，本次都沒有資料。若信用利差走闊、再融資受阻，R3 風險會上升。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7675.7 | FRED API (series_id=SP500) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 7.97 | FRED API (series_id=SP500) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 9.4 | FRED API (series_id=SP500) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（NASDAQ-100 最新收盤） | 29224.52 | FRED API (series_id=NASDAQ100) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.68 | FRED API (series_id=NASDAQ100) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026-Q1，家庭股票配置 %） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-27T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.7 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.81 | FRED API (series_id=BAMLC0A0CM) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.64 | FRED API (series_id=DGS10) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | -6.0 | FRED API (series_id=DGS10) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.32 | FRED API (series_id=DFII10) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | -6.0 | FRED API (series_id=DFII10) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.32 | FRED API (series_id=T10YIE) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 83.9 | FRED API (series_id=DCOILWTICO) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-27T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.33 | FRED API (series_id=T5YIFR) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8682 | FRED API (series_id=THREEFYTP10) | 2026-08-21 | 2026-08-27T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.66 | FRED API (series_id=SOFR) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.74 | FRED API (series_id=SOFR99) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-08-27 | 2026-08-27T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，transaction volume） | 0.003（$bn） | FRED API (series_id=RPONTTLD) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps（as_of 2026-08-25，兩腿同日） | 1.0 | FRED API (scripts/fetch_macro.py repo_stress block) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr99_iorb_bps（as_of 2026-08-25） | 9.0 | FRED API (scripts/fetch_macro.py repo_stress block) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,745,699（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-19 | 2026-08-27T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,913,041（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-21 | 2026-08-27T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,442,957（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-27T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.45 | FRED API (series_id=VIXCLS) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of；base_date 2026-08-18，window 7 日，comove=false） | 15.45 | scripts/fetch_macro.py (FRED shared timeline) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | -2.46 | scripts/fetch_macro.py (FRED shared timeline) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -0.19 | scripts/fetch_macro.py (FRED shared timeline) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2026.1422（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-12 | 2026-08-27T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口數） | -7,218,048 | CFTC TFF futures-only | 2026-08-18 | 2026-08-27T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | 244,468 | CFTC TFF futures-only | 2026-08-18 | 2026-08-27T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 69.44 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index prior | 73.98 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-08-24 | 2026-08-27T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2368.0 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl / GuruFocus [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | 賣方摘要 WebSearch（90d＋same quarter） | ✗ NOT DISCLOSED（搜尋完成，無同季合格上調） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✗ NOT DISCLOSED（14 日窗無合格披露） |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | CNN [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | FINRA / GuruFocus WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | AAII [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WSB / X WebSearch（7d） | ✗ NOT DISCLOSED（無顯著討論） |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | naaim.org [primary: SEARCH] | ✗ NOT DISCLOSED（無當週值） |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | BofA / JPM WebSearch | ✗ NOT DISCLOSED（無新一期調查） |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | Reuters / TreasuryDirect WebSearch（14d） | ✗ NOT DISCLOSED（14 日窗無顯著標售結果） |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | CME FedWatch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | PBoC / NBS WebSearch | ✗ NOT DISCLOSED（無當期英文摘要） |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]（30d） | ✗ NOT DISCLOSED（30 日窗無合格披露） |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | 財報摘要 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | 供應商披露 WebSearch | ✗ NOT DISCLOSED（僅找到營收 run-rate 成長，非 token volume） |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | CNBC 等 WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 [primary: SEARCH] | ✗ NOT DISCLOSED（無合格披露） |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | 產業披露 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | [primary: SEARCH]；quarterly_state 沿用 FactSet 季度狀態；event_scan 30 日掃描無事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | 綜合披露 [primary: SEARCH]（分母 top-4） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K / 10-Q [primary: SEARCH]（30d） | ✗ NOT DISCLOSED（30 日窗無變動） |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | [primary: SEARCH]；quarterly_state 沿用 capex 增速披露；event_scan 30 日掃描無事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | 新聞 / SEC EDGAR WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | stockanalysis / Renaissance WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | Finviz / Benzinga [primary: SEARCH]（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | Yahoo Finance 等 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR / openinsider（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | Cboe [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | etf.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | KRX / TWSE / JPX / ESMA WebSearch（7d） | ✗ NOT DISCLOSED（7 日窗無英文披露） |
| structural.zero_dte | Structural Leverage / 0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | OCC WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | FINRA / GuruFocus WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | 信用市場 [primary: SEARCH]（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）＋WebSearch | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok；WebSearch 無額外披露） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | trailing P/E ≈26.2、Shiller CAPE ≈41.3（原定來源 multpl / GuruFocus） | Shiller CAPE S&P 500 P/E August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio （GuruFocus） | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權本益比 ≈29.5x（S&P 500 ≈25.6x） | Magnificent Seven weighted PE August 2026 | https://www.nasdaq.com/articles/the-magnificent-seven-market-performance-and-valuations （Nasdaq） | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| breadth.rsp_spy | RSP 領先 SPY，2026 等權領先 ≈1.7pp | RSP equal weight vs SPY 2026 | https://www.cnbc.com/2026/08/23/stocks-market-investing-sp500-spx.html （CNBC） | 2026-08-23 | 2026-08-27T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 top-10 集中度 ≈36.46% | S&P 500 top 10 concentration 2026 | https://finance.yahoo.com/markets/stocks/articles/rsp-vs-spy-does-equal-185007075.html （Yahoo Finance） | 2026-08-23 | 2026-08-27T09:30:00+08:00 |
| breadth.advance_decline | 廣度確認多頭、新高多於新低 | market breadth advance decline August 2026 | https://ts2.tech/en/sp-500-equal-weight-leads-by-1-7-points-as-market-breadth-wobbles/ （TS2） | 2026-08-23 | 2026-08-27T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 55（Greed） | CNN Fear and Greed August 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-07 月資料）1,417,225，YoY +38.6%，MoM −5.7% | FINRA margin debt July 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt （GuruFocus，原定 FINRA） | 2026-07-31 | 2026-08-27T09:30:00+08:00 |
| retail.aaii | AAII 偏多 35.5%、偏空 39.9%（週結 2026-08-19） | AAII investor sentiment August 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-08-19 | 2026-08-27T09:30:00+08:00 |
| monetary.fedwatch | FedWatch 隱含 9/16 會議按兵不動 ≈68.4% | CME FedWatch September 2026 hold | https://en.macromicro.me/series/1645/probability-fed-rate-decrease （MacroMicro，原定 CME FedWatch） | 2026-08-20 | 2026-08-27T09:30:00+08:00 |
| ai.hyperscaler_capex | top-4 hyperscaler 2026 capex ≈$725bn（+77% YoY），Q2 財報期 | hyperscaler 2026 capex guidance | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-13 | 2026-08-27T09:30:00+08:00 |
| ai.openai_anthropic_revenue | OpenAI ≈$40bn、Anthropic ≈$65bn run-rate | OpenAI Anthropic annualized revenue 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html （CNBC） | 2026-08-17 | 2026-08-27T09:30:00+08:00 |
| ai.compute_supply_demand | GPU 現貨租金 > 2× 合約價、產能被利用率吸收 | AI GPU rental pricing utilization 2026 | https://www.uncoveralpha.com/p/amazon-google-microsoft-meta-q2-earnings （UncoverAlpha） | 2026-08-13 | 2026-08-27T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex > FCF、2026 發債擴張（30 日 event_scan 無事件，另計） | hyperscaler external financing capex FCF debt 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow （FactSet） | 2026-08-17 | 2026-08-27T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 ≈$105bn（OpenAI 40＋Anthropic 65）vs 年化 capex ≈$725bn（分母：top-4） | AI revenue to capex gap 2026 | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-17 | 2026-08-27T09:30:00+08:00 |
| ai.capital_cycle | [quarterly_state] 供給側 capex 年增 ≈77%、需求側 token／營收成長並存（30 日 event_scan 無事件，另計） | AI capex growth supply demand 2026 | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-13 | 2026-08-27T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日窗掃描 0 件 | AI rename SPAC ticker change August 2026 | Renaissance Capital / SEC EDGAR / 新聞掃描 | — | 2026-08-27T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD IPO ≈235 件，無單週無營收 AI IPO 暴衝 | US IPO count August 2026 | https://stockanalysis.com/ipos/2026/ （StockAnalysis） | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot（≥100% 單日、<$1B、2+ 主題、弱基本面）7 日窗掃描 0 檔 | microcap 100% single day quantum AI August 2026 | Finviz / Benzinga / StockTwits movers | — | 2026-08-27T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 10 月 IPO、估值 ≈$2T | Anthropic OpenAI IPO 2026 | https://finance.yahoo.com/markets/article/spacex-openai-and-anthropic-here-are-the-most-anticipated-ipos-in-2026-114439441.html （Yahoo Finance） | 2026-08-17 | 2026-08-27T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 14 日內合格 Form 4 集中賣出 0 起 | insider Form 4 AI executives August 2026 | SEC EDGAR / openinsider | — | 2026-08-27T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.52 | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/manuals/put-call-ratio （TheTrading.tools，原定 Cboe） | 2026-08-19 | 2026-08-27T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美股槓桿 ETF 總 AUM ≈$198bn；TQQQ ≈$37bn、SOXL ≈$22bn | leveraged ETF AUM record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing，原定 etf.com） | 2026-08-17 | 2026-08-27T09:30:00+08:00 |
| structural.us_single_stock_etf | 美單一個股槓桿 ETF 30 日窗新核准／上市 0 件 | single-stock leveraged ETF launch SEC August 2026 | SEC EDGAR / ETF.com new launches | — | 2026-08-27T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 8 月占比創紀錄 ≈62.4% | 0DTE SPX volume share August 2026 | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august （Cboe） | 2026-08-14 | 2026-08-27T09:30:00+08:00 |
| structural.options_volume | OCC 2026 YTD 日均 >71M 口 | OCC options volume 2026 | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/historical-volume-statistics （OCC） | 2026-07-31 | 2026-08-27T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 15.45、期限結構 contango、SKEW 偏高 | VIX term structure SKEW August 2026 | https://www.thetrading.tools/vix-term-structure （TheTrading.tools） | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 交叉檢核（2026-07 月資料，YoY +38.6%）；margin debt／市值比本次未確立 | FINRA margin debt equity market cap ratio 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt （GuruFocus） | 2026-07-31 | 2026-08-27T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave HPC 基建擔保 delayed-draw 定期貸款設施 $2.6B | AI data center debt financing CoreWeave August 2026 | https://investors.coreweave.com/news/news-details/2026/CoreWeave-Closes-2-6-Billion-Loan-Facility-Expanding-Financing-Flexibility-for-AI-Infrastructure/default.aspx （CoreWeave IR） | 2026-08-10 | 2026-08-27T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-27",
  "iso_week": "2026-W35",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-25",
  "prior_date": "2026-08-24",
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 4.68,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

> [DRY RUN] this report was not committed to archive.

# 2026-08-06 AI 泡沫破裂預測報告

報告日期：2026-08-06｜ISO 週次：2026-W32｜預測窗口：2026-08-06 → 2027-02-04｜前次基準：report-2026-08-03（3天前）

## 結論

**結論：no**

三條路徑都沒有已在進行中的觸發：NASDAQ-100 距 52 週高點回撤 3.83%，離 R1 門檻還差 22.02%（`valuation.ndx_drawdown`）；四家 hyperscaler 2026 capex 指引仍在上修、零家下修（`ai.hyperscaler_capex`）。最強的 yes 側訊號是 CoreWeave 信用重定價（5Y CDS ≈855bp、貸款利差 +125bp，`valuation.ai_credit_schism`），但目前只有定價壓力，沒有違約、寬限期外未付款或 distressed exchange，而且整體 HY OAS 仍只有 2.73%（`monetary.hy_oas`），信用壓力還沒擴散。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,487.79（2026-08-05），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 3.83%（`valuation.ndx_drawdown`）。R1 門檻為 22,995.45；從最新收盤還要再跌 22.02% 才會觸及。本次窗口內曾出現的最低收盤是 27,192.31（2026-07-29），之後已反彈約 8.4%。

脆弱度確實高：S&P 500 trailing P/E 29.74、Shiller CAPE 42.19（2026-08-05，`valuation.sp500_pe_cape`）；S&P 500 高於 200 日均線 9.71%、高於 52 週均線 11.32%（2026-08-05，`valuation.sp500_trend`）；FINRA 2026-06 margin debt $1.502T，YoY +51.5%（`retail.margin_debt`）；美國槓桿 ETF AUM 創高至 ≈$198B（`structural.leveraged_etf_aum`）。另外，CNBC 2026-07-28 報導 Alphabet 上修 capex 後股價遭拋售（`ai.hyperscaler_capex`），可見市場已開始懲罰 capex 擴張。不過目前沒有恐慌或強迫去槓桿的跡象：VIX 15.81（2026-08-05），截至 2026-08-05 的 7 日內 VIX −23.48%、S&P 500 +5.57%，未出現同漲警戒（`structural.vix_spx_comove`）；CNN Fear & Greed ≈58（Greed，`retail.fear_greed`）；AAII Bear 42.1% 高於 Bull 31.0%（2026-07-30，`retail.aaii`），散戶情緒偏謹慎而非亢奮。

**判讀：** R1 距門檻很遠（還差 22.02%）。窗口內要觸發，需要一個具傳導力的催化劑，例如 AI 信用事件擴散（R3→R1）、hyperscaler capex 指引轉向或財報大幅失望，或長端利率／期限溢價急升引發估值重定價。單靠高估值，不足以在 182 天內造成 25% 回撤。

### R2 資本支出收縮

CNBC 2026-07-28 報導 hyperscaler 2026 capex 續上修，合計 ≈$725B，其中 Alphabet 在 Q2 財報上修指引（`ai.hyperscaler_capex`）。逐家狀態如下：

- Alphabet：Q2 2026 財報（2026-07 下旬）上修。
- Microsoft、Amazon、Meta：本次來源只提供「合計續上修」的敘述，沒有逐家列出最新指引數值。本次證據中沒有任何一家下修，但三家各自的指引金額與方向本次未逐一確立。

目前已下修家數為 0/4。下一次財報日期本次證據未載明；窗口長 182 天，按季報節奏應會涵蓋後續兩個財報季，但具體日期未確立。需求面仍偏緊：HBM／DRAM 合約價續升，H200 租金 ≈$4.39/hr，供給缺口預估延續到 1H2027（2026-08-01，`ai.compute_supply_demand`）。這種狀態下，四家沒有立即下修 capex 的營運理由。

**判讀：** R2 目前是最遠的一條路徑：四家仍在上修，需求端報告為供不應求。要在窗口內觸發，需要至少兩家在接下來的財報季同步轉向，最可能的情境是 R1 大幅回撤或 AI 營收不及預期迫使紀律化。本次沒有任何證據顯示這個轉向已經開始。

### R3 AI 信用事件

CoreWeave 是本次最接近 R3 的借款人：5Y CDS ≈855bp，其 $2.6B 貸款利差擴大 125bp，貸款投資人開始要求 covenants；同一報導中 Oracle CDS ≈215bp（2026-08-03，`valuation.ai_credit_schism`）。CoreWeave 在 2026-07-29 調高一筆與 Anthropic 掛鉤的 $2.6B 貸款票息；Nebius 於 2026-07-17 完成 $775M 擔保融資（`structural.ai_infrastructure_debt`）。客戶集中度方面，Microsoft RPO ≈$678B，其中 ≈32% 繫於單一客戶 OpenAI（2026-07-30，`ai.customer_concentration_rpo`），AI 基礎設施的償債能力最終取決於少數 AI 實驗室的付款能力。

CoreWeave 的總負債規模是否達到 R3 的 50 億美元門檻，本次來源沒有確立（不引用記憶中的數字）。本次也沒有找到任何 AI 基礎設施借款人的近期到期牆、未付款、covenant waiver、distressed exchange 或 going-concern 文字。整體信用市場仍然平靜：HY OAS 2.73%（較 2026-08-03 收窄 5bp，`monetary.hy_oas`），IG OAS 0.78%（`monetary.ig_oas`）。

**判讀：** R3 是三條路徑中壓力最明顯的一條。CDS ≈855bp 加上貸款被迫加價，代表市場已在定價顯著的違約風險，但從「重定價」走到「破產／寬限期外違約／distressed exchange」還需要融資中斷，例如再融資失敗、主要客戶付款能力受質疑，或信用利差全面走闊。本次證據顯示 CoreWeave 仍能取得融資（只是成本更高），所以 R3 在窗口內完成不是目前的主情境。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS ≈855bp，$2.6B 貸款利差擴大 125bp，投資人要求 covenants；Oracle CDS ≈215bp（2026-08-03）——AI 基礎設施信用端已開始重定價（`valuation.ai_credit_schism`）
- [R3] CoreWeave 於 2026-07-29 被迫調高一筆與 Anthropic 掛鉤的 $2.6B 貸款票息，顯示 AI 基礎設施融資成本上升（`structural.ai_infrastructure_debt`）
- [整體] 估值與槓桿處於極端：Shiller CAPE 42.19、trailing P/E 29.74（2026-08-05，`valuation.sp500_pe_cape`）；margin debt $1.502T、YoY +51.5%（2026-06 月資料，`retail.margin_debt`）；槓桿 ETF AUM ≈$198B 創高（`structural.leveraged_etf_aum`）——一旦有催化劑，下跌幅度會被放大
- [R1] 市場已開始懲罰 capex 擴張：Alphabet 上修 capex 後股價遭拋售（2026-07-28，`ai.hyperscaler_capex`）；NASDAQ-100 曾在 2026-07-29 收在 27,192.31（`valuation.ndx_drawdown`）
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收 ≈$72B（Anthropic ≈$47B＋OpenAI ≈$25B）vs hyperscaler 2026 年化 capex ≈$725B（分母：CNBC 報導的 hyperscaler 合計），缺口約 10 倍（`ai.revenue_capex_gap`）；Microsoft RPO ≈32% 繫於 OpenAI（`ai.customer_concentration_rpo`）
- [整體] 美債標售需求（auction tail / bid-to-cover）轉弱：5Y 連 14 次 tail、bid-to-cover 為 2022-09 以來最差，7Y tail 0.8bp（2026-07-28，`monetary.treasury_auctions`）；10Y 期限溢價（term premium）0.8681%，trailing 7 日 +3bp（2026-07-31，`monetary.term_premium`）——長端利率是估值重定價的潛在催化劑

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 3.83%（2026-08-05），R1 門檻 22,995.45，還要再跌 22.02%（`valuation.ndx_drawdown`）
- [R2] hyperscaler 2026 capex 合計 ≈$725B 續上修，Alphabet 上修，四家零家下修（2026-07-28，`ai.hyperscaler_capex`）；HBM／DRAM 合約續升、H200 租金 ≈$4.39/hr、缺口延至 1H2027（2026-08-01，`ai.compute_supply_demand`）
- [R3] 整體信用沒有壓力：HY OAS 2.73%（2026-08-04，較前次 −5bp，`monetary.hy_oas`），IG OAS 0.78%（`monetary.ig_oas`）；CoreWeave 仍能取得 $2.6B 融資，Nebius 07-17 完成 $775M 擔保（`structural.ai_infrastructure_debt`），融資管道沒有中斷
- [整體] 資金市場平穩：SOFR 3.66% vs IORB 3.65%，SOFR−IORB 1bp、SOFR99−IORB 9bp（2026-08-04），SRF 動用 $0.001bn（2026-08-05，`monetary.repo_stress_srf`）；MOVE 73.58，較 08-03 的 80.48 回落（`structural.treasury_basis_trade`）
- [整體] 情緒沒有亢奮：AAII Bear 42.1% > Bull 31.0%（2026-07-30，`retail.aaii`）；CNN Fear & Greed ≈58（`retail.fear_greed`）；VIX 7 日 −23.48%、S&P 500 +5.57%，未出現同漲（`structural.vix_spx_comove`）；RSP 等權 YTD +14.26% 領先 SPY +13.71%，廣度並未惡化（2026-08-03，`breadth.rsp_spy`）
- [整體] 基準率：任意 182 天窗口內，R1–R3 都不發生是常態；本次三條路徑都沒有已在進行中的觸發，`yes` 的舉證門檻未達（`valuation.ndx_drawdown`、`ai.hyperscaler_capex`、`valuation.ai_credit_schism`）

## 與前期比較

前次結論：無前次預測（report-2026-08-03 為舊格式評分報告）

前次為舊格式評分報告，不把其評分轉譯為 yes/no；`flip_evidence` 為 `[]`。自 2026-08-03 以來的主要變化：

- NASDAQ-100 由 2026-08-03 的 28,776.80 升至 2026-08-05 的 29,487.79，R1 距離進一步拉大（`valuation.ndx_drawdown`）。
- HY OAS 由 2.78% 收窄至 2.73%，DGS10 由 4.70% 降至 4.63%（`monetary.hy_oas`、`monetary.dgs10`）。
- MOVE 由 80.48 回落至 73.58（`structural.treasury_basis_trade`）。
- CoreWeave 信用重定價（2026-08-03 報導）是新出現的 R3 壓力訊號，但尚未達到解析條件（`valuation.ai_credit_schism`）。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `structural.zero_dte`（⛔ FETCH FAILED）：找到的「Cboe Q2 2026 slides，0DTE 佔 SPX 期權量 ≈65%」標示的資料日期是 2026-05-31，早於 Q2 結束，日期互相矛盾，也不是當期快照，因此不採用。0DTE 只是投機強度的確認指標，這個缺口不會改變答案。

✗ NOT DISCLOSED（搜尋完成、無合格當期披露）：`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.pboc`（找到的報導發布日 2026-07-24 卻含 7/29–8/3 的操作數字，日期矛盾，不採用）、`monetary.private_credit_liquidity`（30 日內沒有 redemption-request ratio、gate proration / breach 或 net inflow→outflow flip 的披露）、`ai.token_growth`、`ai.hyperscaler_financing_mix`（quarterly_state 有：top-5 capex 已超越 FCF、2026 發債 ≈$182B；但 30 日 event_scan 無新融資事件）、`ai.depreciation_life`、`ai.capital_cycle`（增速證據不足，本次不判定週期階段）、`structural.global_leveraged_approvals`。以上都是 best-effort 來源，private-credit 與 capital-cycle 的空白會降低本次對 R3 傳導的能見度，但不足以把答案推向 yes。

零件數篩檢（✓ SEARCH-VERIFIED（0 件））：`speculation.ai_rename_spac`、`speculation.microcap_moonshots`、`speculation.insider_form4`（搜到 SNOW、TEM 內部人賣股報導，但缺少 Form 4 申報日／個別申報 URL 等 filing-level 欄位，依規則不列出姓名與金額）、`structural.us_single_stock_etf`（找到的 Leverage Shares 發行新聞，URL 日期 2026-07-07 與搜尋結果日期 2026-07-30 互相矛盾，日期不明確，只作背景）。

主要不確定性：

1. **CoreWeave 的負債規模與再融資路徑**：本次未確立其總負債是否 ≥ 50 億美元，也不知道近期到期分布。若後續確認規模達標，且出現再融資失敗或 distressed exchange，R3 可以直接觸發，並可能傳導到 R1——這會把答案推向 yes。
2. **下一個 hyperscaler 財報季**：日期本次未確立，但會落在窗口內。若兩家以上同步下修 capex，R2 成立；目前證據方向相反（續上修），維持 no。
3. **長端利率／美債標售需求**：5Y 連續 tail 加上期限溢價上行，如果演變成國債市場失序（Treasury market dysfunction），可能成為 R1 的估值重定價催化劑，會把答案推向 yes；目前 MOVE 回落、repo 平穩，尚未出現。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7723.55 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線偏離） | 9.71% | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線偏離） | 11.32% | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29487.79 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤） | 3.83% | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（家庭股票配置，2026Q1） | 45.76080873390133（≈45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限） | 3.75% | FRED API (series_id=DFEDTARU) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限） | 3.5% | FRED API (series_id=DFEDTARL) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.73% | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.78% | FRED API (series_id=BAMLC0A0CM) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.63% | FRED API (series_id=DGS10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.4% | FRED API (series_id=DFII10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.22% | FRED API (series_id=T10YIE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 81.96（USD/bbl） | FRED API (series_id=DCOILWTICO) | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46% | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-08-06T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.26% | FRED API (series_id=T5YIFR) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8681% | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.66% | FRED API (series_id=SOFR) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.74% | FRED API (series_id=SOFR99) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65% | FRED API (series_id=IORB) | 2026-08-06 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用） | 0.001（$bn） | FRED API (series_id=RPONTTLD) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,738,190（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,941,248（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,442,957（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.81 | FRED API (series_id=VIXCLS) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 15.81 | FRED API 衍生（vix_spx_comove，base_date 2026-07-29） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日） | -23.48% | FRED API 衍生（vix_spx_comove） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日） | 5.57% | FRED API 衍生（vix_spx_comove） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2004.9941（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-22 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7,481,041（口） | CFTC TFF（cftc_lev_funds） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.58 | Yahoo Finance chart API ^MOVE（move_index） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2342.8（$bn，tri-party transaction volume） | OFR STFM REPO-TRIV1_TV_TOT-P（ofr_repo） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation｜S&P 500 P/E and Shiller CAPE | multpl.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation｜Mag 7 weighted P/E and AI leader P/S | SSGA WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation｜Analyst TP upgrade decomposition | 賣方研報 WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | Valuation｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | financecharts WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth｜Top-10 concentration in S&P 500 | P&I WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth｜Advance/decline ratio, new high/low ratio | StockCharts WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment｜CNN Fear & Greed Index | cnn.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment｜Margin Debt: FINRA monthly data | FINRA／Advisor Perspectives WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment｜Retail survey: AAII Investor Sentiment | aaii.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment｜Social sentiment proxies | WSB／cashtag WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment｜NAAIM Exposure Index | naaim／YCharts WebSearch [primary: SEARCH] | ✗ NOT DISCLOSED（無當期週值） |
| institutional.bofa_jpm_survey | Institutional Sentiment｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED（無新調查） |
| monetary.fed_funds | Monetary & Credit｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit｜美債標售需求（auction tail / bid-to-cover） | auction recap WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit｜Fed funds rate path expectations | CME FedWatch WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit｜PBoC aggregate financing / liquidity operations | investing.com WebSearch | ✗ NOT DISCLOSED（結果日期矛盾，無可用當期披露） |
| monetary.private_credit_liquidity | Monetary & Credit｜Private-credit / non-bank fund liquidity stress | BDC 披露 WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無合格披露） |
| ai.hyperscaler_capex | AI Fundamentals｜Hyperscaler capex guidance | 季報／CNBC WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals｜AI token volume growth rate | Anthropic／OpenAI／Google WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI Fundamentals｜OpenAI / Anthropic annualized revenue | Epoch AI WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals｜Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話／Benzinga WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals｜AI compute supply/demand and overcapacity risk | TrendForce／jarvislabs WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：Sage Advisory WebSearch；event_scan：30 日發債／融資 WebSearch | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals｜GPU / 伺服器折舊年限變動 | 10-K／10-Q WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無變動） |
| ai.capital_cycle | AI Fundamentals｜資本週期階段（capital cycle stage） | quarterly_state：供需增速 WebSearch；event_scan：30 日進出場事件 WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior｜Search for past 7 days: AI rename / SPAC | Reuters／Benzinga／BusinessWire WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior｜IPO market heat | Renaissance Capital WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior｜Microcap thematic moonshots | Finviz／StockAnalysis／StockTitan WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior｜Upcoming AI IPOs | 具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 篩檢（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior｜Cboe equity-only put/call ratio | YCharts WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage｜US leveraged ETF AUM | cryptobriefing／etf.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage｜US single-stock leveraged ETF approvals | SEC EDGAR／GlobeNewswire 篩檢（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED（7 日內無英文披露） |
| structural.zero_dte | Structural Leverage｜0DTE option volume | Cboe WebSearch | ⛔ FETCH FAILED（結果資料日期矛盾，無可用當期快照） |
| structural.options_volume | Structural Leverage｜Options total volume: OCC monthly volume report | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage｜Cross-asset derivatives / correlation checks | Cboe insights WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage｜Cross-reference only: FINRA margin debt | 交叉引用 Retail Sentiment margin debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage｜AI infrastructure debt financing / vendor-financing loops | Bloomberg WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）；WebSearch 補充掃描無合格披露 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.74 | S&P 500 trailing P/E August 5 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio（multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.19 | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 forward P/E ≈29x vs 指數 ≈25.6x，溢價壓縮（AI leader P/S vs 10 年均值未披露） | Magnificent 7 valuation premium lowest decade 2026 | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026（SSGA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA TP $285→$288，EPS-revision 主導（EPS／PE Δ 數值未披露） | Morgan Stanley NVDA target 288 July 2026 AI demand | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044（Investing.com） | 2026-07-13 | 2026-08-06T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS ≈855bp、$2.6B 貸款利差 +125bp、Oracle CDS ≈215bp | CoreWeave CDS spread blows out 125 covenants Oracle August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm（Tech Times） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD +14.26% vs SPY +13.71%（總報酬） | RSP vs SPY equal weight total return YTD August 2026 | https://www.financecharts.com/etfs/SPY/performance/total-return（FinanceCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 ≈41% | S&P 500 top 10 concentration percent record 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/（Pensions & Investments） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| breadth.advance_decline | ≈64% 成分股在 50DMA 上、A/D 線創高、McClellan 轉負 | S&P 500 breadth percent above 50 day moving average August 2026 McClellan | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/（StockCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed ≈58（Greed） | CNN Fear and Greed Index August 5 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-06 月資料）$1.502T、YoY +51.5%（margin debt／市值比本次未確立） | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| retail.aaii | AAII Bear 42.1%／Neutral 26.9%／Bull 31.0% | AAII investor sentiment survey July 30 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| retail.social_sentiment | WSB「Save Wendy's」WEN 軋空，空頭比重 ≈44%（非 AI 題材） | Reddit WSB Wendy's WEN short squeeze August 2026 | https://finance.yahoo.com/markets/stocks/articles/reddit-wants-save-wendy-inside-161925726.html（Yahoo Finance） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.treasury_auctions | 5Y 連 14 次 tail、bid-to-cover 為 2022-09 以來最差；7Y tail 0.8bp | US Treasury 5 year 7 year auction tail bid to cover July 2026 | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026（TFTC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| monetary.fedwatch | FOMC 7/29 鷹派持平；FedWatch 9 月 ≈62%，定價分歧 | CME FedWatch September 2026 probability FOMC hold | https://growbeansprout.com/tools/fedwatch（Beansprout／CME FedWatch） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計 ≈$725B 續上修；Alphabet Q2 上修觸發賣壓 | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic run-rate ≈$47B、OpenAI ≈$25B | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-06-15 | 2026-08-06T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO ≈$678B，≈32% 繫於單一客戶 OpenAI | Microsoft RPO backlog 678 billion single customer OpenAI 2026 | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/（Benzinga via TradingView） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| ai.compute_supply_demand | HBM／DRAM 合約續升、H200 租金 ≈$4.39/hr、缺口延至 1H2027 | H200 GPU rental price HBM DRAM contract 2026 shortage 2027 | https://jarvislabs.ai/blog/h200-price（JarvisLabs） | 2026-08-01 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超越 FCF、2026 發債 ≈$182B、>$120B 表外結構 | hyperscaler capex FCF debt issuance 182 billion off balance sheet SPV 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure（Sage Advisory） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 ≈$72B（Anthropic $47B＋OpenAI $25B，2026-06-15）vs hyperscaler 2026 年化 capex ≈$725B（CNBC 2026-07-28；分母：CNBC 報導的 hyperscaler 合計） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI）；https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-06-15 | 2026-08-06T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收投機 IPO：合格 0 件 | AI rename ticker SPAC no revenue IPO July 30 August 6 2026 | Reuters／Benzinga／BusinessWire SPAC 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.ipo_heat | 跨週 ≈21 檔定價、無 blowout 首日、YTD ≈$251B／86 檔 | US IPO pricings week August 3 2026 Renaissance | https://www.renaissancecapital.com/IPO-Center/Pricings（Renaissance Capital） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot：合格 0 件 | microcap 100% single day quantum fusion space nuclear small cap August 2026 | Finviz／StockAnalysis／StockTitan gainers 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 ≈$1T IPO、Anthropic 續進 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground（Benzinga） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| speculation.insider_form4 | 14 日 Form 4 篩檢：具完整 filing-level 欄位的合格申報 0 件（SNOW／TEM 報導缺申報日或個別申報 URL，未採用） | Snowflake Dageville Tempus Lefkofsky Form 4 insider sale July 2026 SEC | SEC EDGAR Form 4（CIK=1640147 公司申報索引）、新聞報導 | — | 2026-08-06T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.55（未載明單日或 5 日均值） | Cboe equity put call ratio August 3 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio（YCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高 ≈$198B（個別 NVDL／TSLL／CONL／TQQQ／SOXL／SQQQ 未逐檔披露） | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing） | 2026-07-23 | 2026-08-06T09:30:00+08:00 |
| structural.us_single_stock_etf | 30 日單股槓桿 ETF 核准／發行：日期明確的合格事件 0 件（Leverage Shares 新聞 URL 日期 2026-07-07 與結果日期 2026-07-30 矛盾，僅作背景） | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | SEC EDGAR ETF filings、ETF.com launches、GlobeNewswire | — | 2026-08-06T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月總量 16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW ≈139.96、VIX ≈16.9 contango、TLT 1M skew 創 GFC 以來高 | VIX SKEW term structure bond volatility August 3 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher（Cboe） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-06 月資料）$1.502T、YoY +51.5%（僅交叉確認，不重複計入） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B Anthropic 掛鉤貸款調高票息 | CoreWeave 2.6 billion loan Anthropic yield boosted July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic（Bloomberg） | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Nebius $775M 擔保融資 | CoreWeave 2.6 billion loan Anthropic yield boosted July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic（Bloomberg） | 2026-07-17 | 2026-08-06T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-06",
  "iso_week": "2026-W32",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-04",
  "prior_date": "2026-08-03",
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 3.83,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

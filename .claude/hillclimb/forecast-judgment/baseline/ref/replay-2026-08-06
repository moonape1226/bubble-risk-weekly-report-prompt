> [DRY RUN] this report was not committed to archive.

# 2026-08-06 AI 泡沫破裂預測報告
報告日期：2026-08-06｜ISO 週次：2026-W32｜預測窗口：2026-08-06 → 2027-02-04｜前次基準：report-2026-08-03（3天前）

## 結論

**結論：no**

三條路徑都還離觸發很遠：NASDAQ-100 距 52 週高點回撤 3.83%，距 R1 門檻仍需再跌約 22.02%；四大 hyperscaler 的 2026 capex 指引仍在上修、尚無一家下修（`ai.hyperscaler_capex`）。最強的反向訊號是 CoreWeave 信用定價明顯走闊（5Y CDS ≈855bp，`valuation.ai_credit_schism`），但目前沒有付款違約、破產或 distressed exchange 的證據，HY OAS 也只有 2.73%（`monetary.hy_oas`），不足以推翻「182 天內三條路徑皆不成立」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,487.79（2026-08-05），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 3.83%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，從最新收盤還要再跌約 22.02% 才會觸及。7 月下旬曾回落到 27,192.31（2026-07-29），之後一週內反彈約 8%。

脆弱度方面：S&P 500 為 7,723.55（2026-08-05），高於 200 日均線 9.71%、高於 52 週均線 11.32%（`valuation.sp500_trend`）；S&P 500 trailing P/E 29.74、Shiller CAPE 42.19（2026-08-05，`valuation.sp500_pe_cape`）；margin debt $1.502T，YoY +51.5%（2026-06 資料，`retail.margin_debt`），已落在歷史頂部附近常見的 YoY +40–50% 區間之上。不過觸發條件目前沒有出現：VIX 15.81（2026-08-05），過去 7 天 VIX −23.48%、S&P 500 +5.57%，未呈現同漲（`structural.vix_spx_comove`）；CNN Fear & Greed ≈58（Greed，`retail.fear_greed`），沒有到極端貪婪。

**判讀：** R1 離觸發很遠。要在窗口內觸發，需要一次接近 1987／2000／2022 級別的科技股重挫，而且要在約 6 個月內完成。可能的推手包括 10–11 月與 1–2 月 hyperscaler 財報上 capex 回報被重新質疑、AI 信用事件外溢，或利率與通膨再次衝擊（CPI YoY 3.46%，壓縮 Fed 托底空間）。

### R2 資本支出收縮

- 合計：Microsoft、Alphabet、Amazon、Meta 2026 capex 指引合計約 $725B，報導描述為「續上修」；Alphabet 在 Q2 財報（2026-07 下旬）再次上修，反而引來賣壓（CNBC，2026-07-28，`ai.hyperscaler_capex`）。
- Alphabet：上修（相較前次正式指引）。
- Microsoft、Amazon、Meta：本次證據只有合計「續上修」的敘述，沒有逐家列出數值或方向；三家都沒有下修的報導。
- 已下修家數：0／4。
- 窗口內的下一輪財報：依慣例約在 2026-10 下旬（Q3）與 2027-01 下旬至 02 初（Q4）兩輪，都落在窗口內；確切日期本次未取得。

需求面目前仍支持 capex：HBM／DRAM 合約價續升，H200 租金約 $4.39/hr，供給缺口延至 1H2027（2026-08-01，`ai.compute_supply_demand`）。Microsoft RPO 約 $678B，其中約 32% 繫於單一客戶 OpenAI（2026-07-30，`ai.customer_concentration_rpo`），這是 backlog 重複計算風險（RPO double-counting）與客戶集中風險的來源，但本次沒有可加總的跨供應商同一 counterparty 承諾金額，因此不計算重複計算比例。

**判讀：** R2 離觸發最遠。四家仍在上修，加上需求端短缺，在窗口內的兩輪財報中出現「兩家下修」的機率很低。要翻轉，需要 R1 式的股價大跌或 AI 營收對 capex 缺口（revenue-to-capex gap）引發的股東壓力，迫使至少兩家在 10 月或 1 月財報同時下修。

### R3 AI 信用事件

- CoreWeave：最可能符合 R3 規模門檻的 AI 算力借款人（本次證據未載其負債總額，僅依其公開發債規模判斷可能符合）。5Y CDS 約 855bp；與 Anthropic 掛鉤的 $2.6B 貸款利差擴大 125bp，投資人要求加上 covenants（2026-08-03，`valuation.ai_credit_schism`）。CoreWeave 已在 2026-07-29 調高這筆貸款的票息（Bloomberg，`structural.ai_infrastructure_debt`）。
- Oracle：CDS 約 215bp（2026-08-03，`valuation.ai_credit_schism`）。Oracle 主業不是 AI 資料中心，不屬 R3 定義的借款人，只作外溢指標。
- Nebius：2026-07-17 取得 $775M 擔保融資（`structural.ai_infrastructure_debt`），屬持續融資，不是困境訊號。
- 困境證據：本次未發現付款違約、寬限期、covenant waiver、distressed exchange 或 going-concern 文字。
- 近期到期與再融資：本次未取得具體的到期日或再融資金額。

整體信用環境仍寬鬆：HY OAS 2.73%、IG OAS 0.78%（2026-08-04，`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 +1bp，SOFR99−IORB 為 +9bp（2026-08-04），SRF 動用（Standing Repo Facility usage）只有 $0.001bn（2026-08-05，`monetary.repo_stress_srf`）。

**判讀：** R3 是三條路徑中「方向最差」的一條。AI 信用定價分歧（equity-vs-credit schism）正從「與非 AI 信用無差」轉向單一 neocloud 被重新定價，屬後期訊號。但從 CDS 走闊到 182 天內真的發生破產、付款違約或 distressed exchange，中間還隔著現金消耗、客戶合約與再融資能力；本次也沒有任何事件層級的困境證據。要觸發 R3，需要 CoreWeave 或同類借款人失去關鍵客戶、再融資失敗，或在信用市場整體轉弱時被迫做 distressed exchange。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 約 855bp，與 Anthropic 掛鉤的 $2.6B 貸款利差擴大 125bp，投資人要求加上 covenants，Oracle CDS 約 215bp（2026-08-03）；CoreWeave 已在 2026-07-29 調高這筆貸款的票息。這是 AI 信用端開始重定價、而股價未跟上的後期訊號（`valuation.ai_credit_schism`、`structural.ai_infrastructure_debt`）。
- [R1] 估值與槓桿都處在極端水位：Shiller CAPE 42.19、trailing P/E 29.74（2026-08-05）；margin debt $1.502T、YoY +51.5%（2026-06 資料）；美國槓桿 ETF AUM 創高，約 $198B（2026-07-23）。一旦出現觸發事件，跌幅可能放大（`valuation.sp500_pe_cape`、`retail.margin_debt`、`structural.leveraged_etf_aum`）。
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）極大：已披露的年化 AI 終端營收約 $72B（Anthropic ≈$47B＋OpenAI ≈$25B，2026-06-15），對比年化 capex 約 $725B（分母僅 top-4：MSFT／GOOGL／AMZN／META，2026-07-28），約 10 倍。Alphabet 上修 capex 引發賣壓，顯示市場開始懲罰 capex 擴張（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`）。
- [R2] Microsoft RPO 約 $678B，其中約 32% 繫於單一客戶 OpenAI（2026-07-30）。若單一 AI 客戶的支付能力出問題，backlog 與 capex 計畫可能同時被重估（`ai.customer_concentration_rpo`）。
- [整體] 利率端有財政供給壓力：5Y 標售連續 14 次 tail，bid-to-cover 為 2022-09 以來最差，7Y tail 0.8bp（2026-07-28）；10Y 期限溢價（term premium）0.8681%（2026-07-31，trailing 7d +3bp）；CPI YoY 3.46%（2026-06）。這限制 Fed 在 AI 引發的下跌中托底的空間（`monetary.treasury_auctions`、`monetary.term_premium`、`monetary.cpi_yoy`）。
- [R1] 股價延伸偏高：S&P 500 高於 200 日均線 9.71%（2026-08-05）；Top-10 集中度約 41%（2026-07-02）（`valuation.sp500_trend`、`breadth.top10_concentration`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 3.83%（2026-08-05），收盤 29,487.79，R1 門檻 22,995.45，還需再跌約 22.02%；在 182 天內完成這種跌幅屬罕見事件（`valuation.ndx_drawdown`）。
- [R2] 四大 hyperscaler 2026 capex 合計約 $725B 且續上修，Alphabet 在 Q2 再上修（2026-07-28）；四家中下修 0 家，離 R2 的「兩家下修」最遠（`ai.hyperscaler_capex`）。
- [R2] 算力需求端仍短缺：HBM／DRAM 合約價續升，H200 租金約 $4.39/hr，缺口延至 1H2027（2026-08-01）。沒有產能過剩或利用率轉弱的證據，不支持短期內 capex 收縮（`ai.compute_supply_demand`）。
- [R3] 整體信用與資金市場平穩：HY OAS 2.73%（2026-08-04，較前次 −5bp）、IG OAS 0.78%；SOFR−IORB +1bp、SOFR99−IORB +9bp（2026-08-04）、SRF 動用 $0.001bn（2026-08-05）；MOVE 73.58（2026-08-05，較前次 −6.9）。單一 neocloud 走闊沒有擴散成系統性信用壓力（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`、`structural.treasury_basis_trade`）。
- [整體] 情緒與廣度沒有到極端：RSP 等權 YTD +14.26%，領先 SPY +13.71%（2026-08-03）；約 64% S&P 500 成分股在 50DMA 之上，A/D 線創高（2026-08-03）；AAII Bear 42.1%、Bull 31.0%（2026-07-30）；Fear & Greed 約 58（2026-08-05）；VIX 與 S&P 500 過去 7 天反向變動，未同漲（2026-08-05）。漲勢由廣度支撐而非極少數權值股撐起，散戶情緒偏謹慎（`breadth.rsp_spy`、`breadth.advance_decline`、`retail.aaii`、`retail.fear_greed`、`structural.vix_spx_comove`）。
- [R1] 新股市場沒有狂熱：本週約 21 檔 IPO 跨週定價，無 blowout 首日（2026-08-04）；+AI 改名／SPAC 與 microcap moonshot 兩項篩選皆為 0 件（`speculation.ipo_heat`）。

## 與前期比較

前次結論：無前次預測（report-2026-08-03 為舊格式評分報告）

前次為舊格式評分報告，不轉換為 yes／no，flip_evidence 為 []。自 2026-08-03 以來的主要變化：

- NASDAQ-100 從 28,776.80（2026-08-03）升至 29,487.79（2026-08-05），R1 距離拉開；S&P 500 同期 +1.62%。
- 10Y 殖利率 −7bp 至 4.63%、TIPS 實質殖利率 −3bp、T10YIE −5bp。三者視窗不一致，判讀：不可判（視窗不一致）。
- HY OAS −5bp 至 2.73%，IG OAS 持平 0.78%；MOVE 由 80.48 降至 73.58。
- CoreWeave 信用定價走闊的報導（2026-08-03）與貸款票息調高（2026-07-29）落在前次報告前後，是本次 R3 最主要的追蹤點。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED 來源（檢索已完成但沒有合格的當期披露）：retail.naaim、institutional.bofa_jpm_survey、monetary.private_credit_liquidity、ai.token_growth、ai.openai_anthropic_revenue（最新披露為 2026-06-15，屬前一季，不視為當期；只作為 AI 營收對 capex 缺口的沿用分子組件）、ai.hyperscaler_financing_mix（quarterly_state 可用：top-5 capex 已超越 FCF、2026 發債約 $182B；但 30 日 event_scan 無新融資事件）、ai.depreciation_life、ai.capital_cycle（增速證據不足，本次不判定週期階段）、structural.global_leveraged_approvals。其中私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）與 hyperscaler 融資事件的缺漏與 R3 最相關：如果其實已有 gate proration / breach 或大型 SPV 融資困難而未被檢索到，可能低估 R3 的進度。但 HY OAS 與 repo 指標都沒有顯示壓力，判斷改變答案的可能性低。

其他資料限制：

- speculation.insider_form4 為 0 件。候選交易缺 filing-level 的 EDGAR URL 或申報日，未列入合格。
- structural.zero_dte 最新可得資料為 Cboe Q2 2026（標示 2026-05-31），偏舊。
- R2 的逐家 capex 數值（MSFT／AMZN／META）本次只取得合計敘述。

最大的不確定性：

1. CoreWeave 等 neocloud 的再融資能力與客戶集中度。若信用利差持續走闊並出現 covenant 或交換要約，R3 會加速，並可能經由信用外溢觸發 R1，推向 yes。
2. 2026-10 下旬與 2027-01 下旬的 hyperscaler 財報。若市場持續懲罰 capex 上修，管理層可能轉向；兩家同時下修會直接觸發 R2，推向 yes。目前軌跡推向 no。
3. 利率與財政供給：5Y 標售連續 tail、CPI 3.46%、FedWatch 對 9 月定價分歧。若長端殖利率急升而 Fed 無法降息，估值壓縮可能加速 R1，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7723.55 | FRED API (series_id=SP500) sp500_trend | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 9.71 | FRED API (series_id=SP500) sp500_trend | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 11.32 | FRED API (series_id=SP500) sp500_trend | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29487.79 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-06-02 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 3.83 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（家庭股票配置 %，2026Q1） | 45.76080873390133（≈45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（上限） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（下限） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.73 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.63 | FRED API (series_id=DGS10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.4 | FRED API (series_id=DFII10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.22 | FRED API (series_id=T10YIE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 81.96 | FRED API (series_id=DCOILWTICO) | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-08-06T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.26 | FRED API (series_id=T5YIFR) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8681 | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.66 | FRED API (series_id=SOFR) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.74 | FRED API (series_id=SOFR99) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-08-06 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用） | 0.001（十億美元） | FRED API (series_id=RPONTTLD) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,738,190（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,941,248（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,442,957（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.81 | FRED API (series_id=VIXCLS) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 15.81 | FRED API vix_spx_comove（VIX／SP500 共同視窗） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日） | -23.48 | FRED API vix_spx_comove（VIX／SP500 共同視窗） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日） | 5.57 | FRED API vix_spx_comove（VIX／SP500 共同視窗） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2004.9941（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-22 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（槓桿基金美債期貨淨部位，口） | -7,481,041 | CFTC TFF futures-only cftc_lev_funds | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.58 | Yahoo Finance chart API (^MOVE) move_index | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2342.8 | OFR STFM (REPO-TRIV1_TV_TOT-P) ofr_repo | 2026-08-05 | 2026-08-06T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | SSGA 研究摘要 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方 TP 上修 WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | financecharts WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | P&I WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | StockCharts WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA／Advisor Perspectives WebSearch | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／YCharts [primary: SEARCH] | ✗ NOT DISCLOSED 檢索完成，無當期週值 |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED 檢索完成，無當期新調查 |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API DFEDTARU ok；DFEDTARL ok |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | 標售 recap WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要 WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API ECBASSETSW ok；JPNASSETS ok |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | investing.com WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC／interval fund 披露 WebSearch（30d） | ✗ NOT DISCLOSED 檢索完成，30 日內無合格披露 |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報／CNBC WebSearch | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 WebSearch | ✗ NOT DISCLOSED 本季無披露 |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／報導 WebSearch | ✗ NOT DISCLOSED 最新為 2026-06-15 前一季披露 |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話摘要 WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | jarvislabs／TrendForce WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：季報／Sage Advisory；event_scan：30d 發債掃描 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露（分子 Epoch、分母 hyperscaler capex） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q WebSearch（30d） | ✗ NOT DISCLOSED 30 日內無變動披露 |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速＋進出場事件 WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | Reuters／Benzinga／BusinessWire 篩選 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | Renaissance Capital WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／StockAnalysis／StockTitan 篩選 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | YCharts WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com／cryptobriefing WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF 發行 feed（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED 7 日內無英文披露 |
| structural.zero_dte | 結構｜0DTE option volume | Cboe 季報摘要 WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC monthly volume report | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe insights WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API VIXCLS ok；vix_spx_comove ok |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | Advisor Perspectives 交叉引用 | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | Bloomberg 等 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）＋WebSearch | ✓ API cftc_lev_funds ok；move_index ok；ofr_repo ok；WebSearch 無合格事件 |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.74（原定 multpl／gurufocus） | S&P 500 trailing P/E August 5 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.19 | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 forward P/E ≈29x vs 指數 ≈25.6x，溢價壓縮 | Magnificent 7 valuation premium lowest decade 2026 | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026 （SSGA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA TP $285→$288，EPS-driven（EPS Δ、target PE Δ 未披露） | Morgan Stanley NVDA target 288 July 2026 AI demand | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044 （Investing.com） | 2026-07-13 | 2026-08-06T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS ≈855bp、$2.6B 貸款利差 +125bp、Oracle CDS ≈215bp | CoreWeave CDS spread blows out 125 covenants Oracle August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm （Tech Times） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD +14.26% vs SPY +13.71%（總報酬） | RSP vs SPY equal weight total return YTD August 2026 | https://www.financecharts.com/etfs/SPY/performance/total-return （FinanceCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 ≈41% | S&P 500 top 10 concentration percent record 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/ （Pensions & Investments） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| breadth.advance_decline | ≈64% 成分股在 50DMA 上、A/D 創高、McClellan 轉負 | S&P 500 breadth percent above 50 day moving average August 2026 McClellan | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/ （StockCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed ≈58（Greed） | CNN Fear and Greed Index August 5 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives，原定 FINRA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| retail.aaii | AAII Bear 42.1%／Neutral 26.9%／Bull 31.0% | AAII investor sentiment survey July 30 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| retail.social_sentiment | WSB「Save Wendy's」WEN 軋空，空頭比重 ≈44%（非 AI 主題） | Reddit WSB Wendy's WEN short squeeze August 2026 | https://finance.yahoo.com/markets/stocks/articles/reddit-wants-save-wendy-inside-161925726.html （Yahoo Finance） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.treasury_auctions | 5Y 連 14 次 tail、BTC 2022-09 以來最差；7Y tail 0.8bp | US Treasury 5 year 7 year auction tail bid to cover July 2026 | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026 （TFTC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| monetary.fedwatch | FOMC 7/29 鷹派持平；CME FedWatch 9 月 ≈62% 定價分歧 | CME FedWatch September 2026 probability FOMC hold | https://growbeansprout.com/tools/fedwatch （Beansprout，原定 CME FedWatch） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.pboc | 人行逆回購 ≈¥2.1T、MLF 淨投放 ¥100B | PBoC reverse repo injection 2.1 trillion yuan late July 2026 | https://www.investing.com/news/economy-news/chinas-pboc-to-conduct-overnight-reverse-repos-inject-a-total-of-21-trillion-yuan-4810853 （Investing.com） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計 ≈$725B 續上修；Alphabet Q2 上修 | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO ≈$678B、≈32% 繫單一客戶 OpenAI | Microsoft RPO backlog 678 billion single customer OpenAI 2026 | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/ （Benzinga via TradingView） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| ai.compute_supply_demand | HBM／DRAM 合約續升、H200 租金 ≈$4.39/hr、缺口延至 1H2027 | H200 GPU rental price HBM DRAM contract 2026 shortage 2027 | https://jarvislabs.ai/blog/h200-price （Jarvislabs） | 2026-08-01 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超越 FCF、2026 發債 ≈$182B | hyperscaler capex FCF debt issuance 182 billion off balance sheet SPV 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure （Sage Advisory） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.revenue_capex_gap | 分子：年化 AI 終端營收 ≈$72B（Anthropic ≈$47B＋OpenAI ≈$25B，沿用組件） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-06-15 | 2026-08-06T09:30:00+08:00 |
| ai.revenue_capex_gap | 分母：年化 capex ≈$725B（top-4：MSFT／GOOGL／AMZN／META） | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收 IPO 篩選：合格 0 件 | AI rename ticker SPAC no revenue IPO July 30 August 6 2026 | Reuters、Benzinga、BusinessWire（已檢查） | — | 2026-08-06T09:30:00+08:00 |
| speculation.ipo_heat | 本週 ≈21 檔跨週定價、無 blowout 首日、YTD ≈$251B／86 檔 | US IPO pricings week August 3 2026 Renaissance | https://www.renaissancecapital.com/IPO-Center/Pricings （Renaissance Capital） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot 篩選：合格 0 件 | microcap 100% single day quantum fusion space nuclear small cap August 2026 | Finviz、StockAnalysis、StockTitan gainers（已檢查） | — | 2026-08-06T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 ≈$1T IPO、Anthropic 續推 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground （Benzinga） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 篩選：具完整 filing-level 欄位的合格交易 0 件 | Form 4 insider sale AI leadership July 2026 SEC | SEC EDGAR Form 4 browse、財經新聞（已檢查） | — | 2026-08-06T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.55（YCharts 日頻指標） | Cboe equity put call ratio August 3 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio （YCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高 ≈$198B（個別 NVDL／TSLL 等未分列） | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing，原定 etf.com） | 2026-07-23 | 2026-08-06T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x 單股槓桿 ETF＋ELOL（TSLA+SpaceX）發行 | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量 ≈65%（Cboe Q2 2026） | 0DTE SPX options share volume Cboe Q2 2026 65% | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641 （Investing.com） | 2026-05-31 | 2026-08-06T09:30:00+08:00 |
| structural.options_volume | OCC 總量（2026-06 月資料）16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW ≈139.96、VIX ≈16.9 contango、TLT 1M skew 創 GFC 以來高 | VIX SKEW term structure bond volatility August 3 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher （Cboe） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-06 月資料）$1.502T、+51.5% YoY（交叉確認） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B Anthropic 掛鉤貸款調高票息 | CoreWeave 2.6 billion loan Anthropic yield boosted July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic （Bloomberg） | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Nebius $775M 擔保融資 | CoreWeave 2.6 billion loan Anthropic yield boosted July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic （Bloomberg） | 2026-07-17 | 2026-08-06T09:30:00+08:00 |

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
  "r1_drawdown_pct": 3.83,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

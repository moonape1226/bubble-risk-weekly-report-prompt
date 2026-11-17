> [DRY RUN] this report was not committed to archive.

# 2026-08-06 AI 泡沫破裂預測報告
報告日期：2026-08-06｜ISO 週次：2026-W32｜預測窗口：2026-08-06 → 2027-02-04｜前次基準：report-2026-08-03（3天前）

## 結論

**結論：no**

三條路徑都沒有已在進行、且可望在窗口內完成的跡象：NASDAQ-100 距 52 週高點回撤 3.83%，離 R1 門檻還要再跌約 22%（`valuation.ndx_drawdown`）；hyperscaler 2026 capex 指引仍在上修，合計約 $725B，R2 方向相反（`ai.hyperscaler_capex`）。CoreWeave 信用重定價（5Y CDS 約 855bp）是本次最強的 yes 證據（`valuation.ai_credit_schism`），但它是壓力訊號，不是 R3 事件，而且在 HY OAS 2.73% 的寬鬆信用環境下，尚不足以推翻「182 天內 R1–R3 皆不發生」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,487.79（2026-08-05），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 3.83%。R1 門檻水位為 22,995.45，需自最新收盤再跌約 22.02% 才會觸發（`valuation.ndx_drawdown`）。前次存檔回撤值為 7.78%，三天內指數明顯回升。同步讀數：S&P 500 為 7,723.55（2026-08-05），高於 200 日均線 9.71%、高於 52 週均線 11.32%；以 2026-07-29 → 2026-08-05 的共同 7 日窗口計，S&P 500 上漲 5.57%、VIX 下跌 23.48% 至 15.81，`comove: false`，沒有出現「指數上漲、避險需求同步升溫」的擁擠讀數（`valuation.sp500_trend`、`structural.vix_spx_comove`）。估值偏高（trailing P/E 29.74、Shiller CAPE 42.19，`valuation.sp500_pe_cape`），融資餘額年增 51.5%（`retail.margin_debt`），下跌一旦啟動，跌幅可能很大；但 R1 要成立需要催化劑。

**判讀：** 距 R1 很遠。窗口內要再跌 22% 以上，需要一個傳導事件，例如 AI 信用事件外溢、hyperscaler 法說會集體下修，或國債市場失序（Treasury market dysfunction）引發的強制去槓桿；目前這些都還沒有啟動。

### R2 資本支出收縮

本次取得的 hyperscaler capex 證據是產業層級：CNBC（2026-07-28）報導 2026 年 hyperscaler capex 續上修，合計約 $725B，Alphabet 第二季上修 capex 後股價反而遭拋售，市場檢視轉嚴（`ai.hyperscaler_capex`）。四家逐家結果如下：
- Alphabet：Q2 2026 財報（2026-07 下旬）上修，方向為上修。
- Microsoft、Amazon、Meta：本次來源只有「合計續上修」的敘述，沒有逐家的指引數字與日期；逐家方向本次無法確立，但沒有任何來源顯示有人下修。
- 已下修家數：0／4。下一輪財報約落在 2026-10 下旬（Q3）與 2027-01 下旬至 02 初（Q4），都在窗口內；本次來源未提供確切日期。

需求端仍偏緊：HBM／DRAM 合約價續升，H200 租金約 $4.39/hr，供給缺口延至 1H2027（`ai.compute_supply_demand`）。這不利於 capex 在半年內轉為下修。

**判讀：** R2 目前朝相反方向走。要在窗口內成立，需兩家在 Q3 或 Q4 法說會下修指引，通常要先有 R1 型股價壓力或 AI 需求明顯降溫；Alphabet 上修遭拋售顯示市場對 capex 的容忍度正在下降，這是值得追蹤的早期壓力，但還不是指引下修。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）正在信貸端出現：TechTimes（2026-08-03）報導 CoreWeave 5Y CDS 約 855bp，一筆 $2.6B 貸款利差走闊 125bp，貸款人開始要求加入 covenants；Oracle CDS 約 215bp（`valuation.ai_credit_schism`）。AI infrastructure debt financing / vendor-financing loops 方面，Bloomberg（2026-07-29）報導 CoreWeave 為一筆與 Anthropic 合約掛鉤的 $2.6B 貸款調高收益率；Nebius 另有一筆 $775M 擔保融資（2026-07-17）（`structural.ai_infrastructure_debt`）。客戶集中度也是 backlog 重複計算風險（RPO double-counting）的背景：Microsoft RPO 約 $678B，其中約 32% 繫於單一客戶 OpenAI（`ai.customer_concentration_rpo`）。

R3 規模門檻：本次來源沒有提供 CoreWeave 或其他 AI 資料中心借款人的總負債，因此「負債 ≥ 50 億美元」本次無法確立（單筆 $2.6B 貸款本身低於門檻）。本次來源也沒有任何借款人出現付款違約、寬限期、distressed exchange 或 going-concern 文字。

**判讀：** R3 是三條路徑中最接近的一條，信貸端已開始為 AI 風險重新定價，但從利差走闊到破產、違約或 distressed exchange 通常還有距離。窗口內可能推過門檻的因素：CoreWeave 類借款人再融資失敗、主要客戶合約（OpenAI／Anthropic）付款能力出現疑慮、或 covenant 觸發。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 約 855bp，$2.6B 貸款利差走闊 125bp，貸款人要求加入 covenants，Oracle CDS 約 215bp（2026-08-03）；信貸端已先於股價為 AI 信用風險重新定價（`valuation.ai_credit_schism`）。
- [R3] CoreWeave 為與 Anthropic 掛鉤的 $2.6B 貸款調高收益率（2026-07-29），顯示 neocloud 融資成本上升，貸款依賴單一 AI 客戶合約（`structural.ai_infrastructure_debt`）。
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）：已披露的 AI 終端年化營收約 $72B（Anthropic 約 $47B＋OpenAI 約 $25B，2026-06-15），對比 hyperscaler 2026 capex 約 $725B（分母：CNBC 報導的 hyperscaler 合計，本次未逐家拆分），缺口約 10 倍（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`）。
- [R2] Alphabet 上修 capex 後股價遭拋售，市場對 capex 的檢視轉嚴（2026-07-28）；投資人對 capex 的容忍度若轉為懲罰，未來法說會下修 capex 的壓力會上升（`ai.hyperscaler_capex`）。
- [R1] 估值與槓桿處於高位：S&P 500 trailing P/E 29.74、CAPE 42.19（2026-08-05），FINRA 6 月融資餘額 $1.502T、年增 51.5%，S&P 500 高於 200 日均線 9.71%，一旦下跌，跌幅可能很大（`valuation.sp500_pe_cape`、`retail.margin_debt`、`valuation.sp500_trend`）。
- [整體] 財政與美債端有壓力：5Y 標售連續 14 次 tail、bid-to-cover 為 2022-09 以來最差，7Y tail 0.8bp（2026-07-28）；10Y 期限溢價（term premium）0.8681%（2026-07-31），7 日內上升 3bp（`monetary.treasury_auctions`、`monetary.term_premium`）。
- [整體] Microsoft RPO 約 $678B，約 32% 繫於 OpenAI（2026-07-30），單一 counterparty 的付款能力是 backlog 品質的集中風險（`ai.customer_concentration_rpo`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 3.83%（2026-08-05），R1 門檻 22,995.45，需再跌約 22%；前次存檔回撤值為 7.78%，距離正在拉大（`valuation.ndx_drawdown`）。
- [R2] hyperscaler 2026 capex 指引仍在上修，合計約 $725B（2026-07-28），四家中沒有任何一家下修（`ai.hyperscaler_capex`）。
- [整體] 整體信用環境沒有傳導：HY OAS 2.73%（2026-08-04，較前次收窄 5bp），IG OAS 0.78% 持平，AI 信貸壓力目前集中在單一發行人，沒有擴散到整體信用市場（`monetary.hy_oas`、`monetary.ig_oas`）。
- [R2] AI 算力供給仍緊：HBM／DRAM 合約價續升，H200 租金約 $4.39/hr，缺口延至 1H2027（2026-08-01），需求端目前不支持半年內下修 capex（`ai.compute_supply_demand`）。
- [整體] 資金與波動指標平穩：SOFR−IORB 1bp、SOFR99−IORB 9bp（2026-08-04），SRF 動用 $0.001bn（2026-08-05）；MOVE 由 80.48 降至 73.58，VIX 15.81；VIX 與 S&P 500 沒有同步上升（`monetary.repo_stress_srf`、`structural.treasury_basis_trade`、`structural.vix_spx_comove`）。
- [整體] 情緒未達極端：CNN Fear & Greed 約 58（Greed，2026-08-05）；AAII 看空 42.1% 高於看多 31.0%（2026-07-30）；RSP 等權 YTD +14.26% 領先 SPY +13.71%，漲勢並未只靠少數權值股（`retail.fear_greed`、`retail.aaii`、`breadth.rsp_spy`）。

## 與前期比較

前次結論：yes（report-2026-08-03）
本次結論：翻轉
前次 forecast.json 沒有 `yes_basis` 欄位（在該欄位建立前寫入），沒有可逐項回應的既有 yes 理由，因此依目前證據重新檢視三條路徑：
翻轉依據：
- R1 退後：NASDAQ-100 回撤由前次存檔的 7.78% 收斂到 3.83%（2026-08-05），需再跌約 22% 才觸及門檻 22,995.45；沒有證據顯示 R1 已在進行（`valuation.ndx_drawdown`）。
- R2 方向相反：hyperscaler 2026 capex 合計約 $725B，仍在上修（2026-07-28），已下修家數 0／4；在 Q3 法說會之前，R2 沒有成立的路徑（`ai.hyperscaler_capex`）。
- R3 未達門檻：CoreWeave CDS 約 855bp 與貸款利差走闊（2026-08-03）是真實的壓力訊號，但本次來源沒有違約、寬限期或 distressed exchange，借款人負債是否 ≥ 50 億美元也無法確立；這屬於脆弱性，還不是在窗口內完成 R3 的證據。重新檢視後，前次 yes 不符合規則 1 的門檻（`valuation.ai_credit_schism`）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下為 ✗ NOT DISCLOSED（檢索完成但沒有合格的當期披露）：retail.naaim、institutional.bofa_jpm_survey、monetary.private_credit_liquidity、ai.token_growth、ai.hyperscaler_financing_mix（quarterly_state 有資料：top-5 capex 已超過 FCF、2026 發債約 $182B、表外 SPV 超過 $120B，2026-07-24；但 30 日 event_scan 沒有新的融資事件）、ai.depreciation_life、ai.capital_cycle（兩個組件都沒有可用披露，本次不判定週期階段）、structural.global_leveraged_approvals。其中私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）沒有披露，是 R3 傳導鏈上的缺口：若出現 gate proration / breach 或 net inflow→outflow flip，會強化 yes 方向，但目前沒有證據。

其他資料限制：
- R2 逐家指引：本次只取得產業合計與 Alphabet 方向，Microsoft／Amazon／Meta 的逐家指引數字未確立。不過沒有來源顯示有人下修，不影響本次 no 的判斷。
- R3 規模門檻：CoreWeave 總負債本次未確立，所以無法確認它是否符合 R3 借款人資格；即使符合，目前也沒有違約事件。
- 10Y 分解：ΔDGS10 −7bp、ΔDFII10 −3bp、ΔT10YIE −5bp；T10YIE 的視窗與另外兩條不同，判讀為不可判（視窗不一致）。
- `speculation.insider_form4` 篩選找到兩筆候選，但缺少 filing-level 要件（filing 日期、逐筆 filing URL，其中一筆沒有金額），依規則列為 0 件，不列名。
- `structural.zero_dte` 的 65% 為 Cboe Q2 2026 資料（2026-05-31），屬較舊的快照。

最大不確定性：
1. CoreWeave 再融資與 covenant 談判：若出現付款違約或 distressed exchange，而且負債超過 50 億美元，R3 會直接成立，並可能透過 AI 信用定價分歧外溢到 R1。這是讓答案轉為 yes 的主要路徑。
2. 2026-10 下旬的 Q3 hyperscaler 法說會：Alphabet 上修遭拋售後，若市場壓力迫使兩家下修 capex，R2 會成立；目前證據指向繼續上修。
3. 美債標售需求（auction tail / bid-to-cover）持續轉弱，加上 10Y 期限溢價（term premium）上升：若演變成國債市場失序（Treasury market dysfunction），可能引發跨資產去槓桿，推升 R1 的可能性；目前 MOVE 回落、repo 資金壓力（SOFR−IORB）平穩。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7723.55 | FRED API (series_id=SP500) sp500_trend | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 9.71 | FRED API (series_id=SP500) sp500_trend | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 11.32 | FRED API (series_id=SP500) sp500_trend | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29487.79 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-06-02 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（回撤 %） | 3.83 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1，FRED 觀測日） | 45.76（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.50 | FRED API (series_id=DFEDTARL) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.73 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.63 | FRED API (series_id=DGS10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.40 | FRED API (series_id=DFII10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.22 | FRED API (series_id=T10YIE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 81.96 | FRED API (series_id=DCOILWTICO) | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-08-06T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.26 | FRED API (series_id=T5YIFR) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8681 | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.66 | FRED API (series_id=SOFR) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.74 | FRED API (series_id=SOFR99) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-08-06 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，transaction volume） | 0.001（十億美元） | FRED API (series_id=RPONTTLD) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,738,190（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,941,248（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,442,957（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.81 | FRED API (series_id=VIXCLS) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of；base 2026-07-29，7 日窗） | 15.81 | scripts/fetch_macro.py vix_spx_comove block | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | -23.48（%） | scripts/fetch_macro.py vix_spx_comove block | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | 5.57（%） | scripts/fetch_macro.py vix_spx_comove block | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2,004.9941（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-22 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7,481,041 | CFTC TFF futures-only cftc_lev_funds | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -52,919 | CFTC TFF futures-only cftc_lev_funds | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.58 | Yahoo Finance chart API ^MOVE move_index | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2342.8 | OFR STFM REPO-TRIV1_TV_TOT-P ofr_repo | 2026-08-05 | 2026-08-06T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | SSGA insight WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方 TP 調升 WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場新聞 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | financecharts WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | P&I chart WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | StockCharts breadth WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly | Advisor Perspectives／FINRA WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／YCharts WebSearch | ✗ NOT DISCLOSED（無當週值） |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM | 賣方調查 WebSearch | ✗ NOT DISCLOSED（無新調查） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED DFEDTARU/DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直接） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED CPIAUCSL | scripts/fetch_macro.py（yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED THREEFYTP10 | scripts/fetch_macro.py | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | auction recap WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要 WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED WALCL | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | investing.com WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC／interval fund 披露 WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無合格披露） |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報／財經媒體 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch AI WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話／新聞 WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | jarvislabs／TrendForce WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：Sage Advisory WebSearch；event_scan：30d 發債／私募信貸掃描，無新事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K／10-Q WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無變動） |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速＋進出場事件 WebSearch；兩組件皆無可用披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days +AI rename / SPAC | Reuters／Benzinga／BusinessWire 螢幕 WebSearch | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | Renaissance Capital WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／StockAnalysis／StockTitan gainers 螢幕 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 篩選（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | YCharts WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing／etf.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF launch feed WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED（7 日內無英文披露） |
| structural.zero_dte | 結構｜0DTE option volume | Cboe Q2 slides WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe insights WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 retail.margin_debt 來源 | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | Bloomberg／新聞 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds／move_index／ofr_repo；WebSearch 無額外事件 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.74 | S&P 500 trailing P/E August 5 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.19 | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 約 29x vs 指數約 25.6x，溢價壓縮；AI leader P/S 對 10 年均值本次未披露 | Magnificent 7 valuation premium lowest decade 2026 | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026 （SSGA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA TP $285→$288，EPS 驅動；EPS Δ 與目標 PE Δ 未披露 | Morgan Stanley NVDA target 288 July 2026 AI demand | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044 （Investing.com） | 2026-07-13 | 2026-08-06T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 約 855bp、$2.6B 貸款利差 +125bp、要求 covenants；Oracle CDS 約 215bp | CoreWeave CDS spread blows out 125 covenants Oracle August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm （TechTimes） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 總報酬 +14.26% vs SPY +13.71% | RSP vs SPY equal weight total return YTD August 2026 | https://www.financecharts.com/etfs/SPY/performance/total-return （FinanceCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度約 41% | S&P 500 top 10 concentration percent record 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/ （Pensions & Investments） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| breadth.advance_decline | 約 64% 成分股在 50DMA 之上、A/D 線創高、McClellan 轉負 | S&P 500 breadth percent above 50 day moving average August 2026 McClellan | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/ （StockCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 58（Greed） | CNN Fear and Greed Index August 5 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-06 月資料）$1.502T、YoY +51.5%；margin debt／市值比本次未計算（無市值來源） | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives／FINRA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| retail.aaii | AAII Bear 42.1%／Neutral 26.9%／Bull 31.0% | AAII investor sentiment survey July 30 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| retail.social_sentiment | WSB「Save Wendy's」WEN 軋空討論，空頭部位約 44%（非 AI 標的） | Reddit WSB Wendy's WEN short squeeze August 2026 | https://finance.yahoo.com/markets/stocks/articles/reddit-wants-save-wendy-inside-161925726.html （Yahoo Finance） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.treasury_auctions | 5Y 連續 14 次 tail、bid-to-cover 為 2022-09 以來最差；7Y tail 0.8bp | US Treasury 5 year 7 year auction tail bid to cover July 2026 | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026 （TFTC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| monetary.fedwatch | FOMC 7/29 鷹派按兵不動；CME FedWatch 9 月約 62%，定價分歧 | CME FedWatch September 2026 probability FOMC hold | https://growbeansprout.com/tools/fedwatch （Beansprout／CME FedWatch） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.pboc | 人行逆回購約 ¥2.1T（7/29–8/3）、7/24 MLF 淨投放 ¥100B（來源標示日期 2026-07-24） | PBoC reverse repo injection 2.1 trillion yuan late July 2026 | https://www.investing.com/news/economy-news/chinas-pboc-to-conduct-overnight-reverse-repos-inject-a-total-of-21-trillion-yuan-4810853 （Investing.com） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 續上修，合計約 $725B；Alphabet 上修後遭拋售 | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic run-rate 約 $47B、OpenAI 約 $25B | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-06-15 | 2026-08-06T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO 約 $678B，約 32% 繫於單一客戶（OpenAI） | Microsoft RPO backlog 678 billion single customer OpenAI 2026 | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/ （Benzinga via TradingView） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| ai.compute_supply_demand | HBM／DRAM 合約價續升、H200 租金約 $4.39/hr、缺口延至 1H2027 | H200 GPU rental price HBM DRAM contract 2026 shortage 2027 | https://jarvislabs.ai/blog/h200-price （Jarvis Labs） | 2026-08-01 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超過 FCF、2026 發債約 $182B、表外結構超過 $120B | hyperscaler capex FCF debt issuance 182 billion off balance sheet SPV 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure （Sage Advisory） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.revenue_capex_gap | AI 終端年化營收約 $72B（Anthropic $47B＋OpenAI $25B）vs 2026 capex 約 $725B（分母：CNBC hyperscaler 合計） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI）；分母 https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-06-15 | 2026-08-06T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收 IPO 合格事件 0 件 | AI rename ticker SPAC no revenue IPO July 30 August 6 2026 | Reuters／Benzinga／BusinessWire SPAC 螢幕 | 2026-08-06 | 2026-08-06T09:30:00+08:00 |
| speculation.ipo_heat | 本週約 21 檔定價、無 blowout 首日；YTD 約 $251B／86 檔 | US IPO pricings week August 3 2026 Renaissance | https://www.renaissancecapital.com/IPO-Center/Pricings （Renaissance Capital） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot 合格 0 件 | microcap 100% single day quantum fusion space nuclear small cap August 2026 | Finviz／StockAnalysis／StockTitan gainers 螢幕 | 2026-08-06 | 2026-08-06T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標約 $1T IPO，Anthropic 持續推進 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground （Benzinga） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 合格 0 件（2 筆候選缺 filing 日期／逐筆 filing URL／金額，未達 filing-level 要件） | Snowflake Dageville Tempus Lefkofsky Form 4 insider sale July 2026 SEC | SEC EDGAR Form 4 company browse | — | 2026-08-06T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.55（日讀數） | Cboe equity put call ratio August 3 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio （YCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高約 $198B（NVDL／TSLL／CONL／TQQQ／SOXL／SQQQ 個別 AUM 未披露） | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing） | 2026-07-23 | 2026-08-06T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x 單股槓桿 ETF＋ELOL（TSLA＋SpaceX）發行（URL 路徑顯示 2026-07-07，兩個日期皆在 30 日窗內） | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量約 65%（Cboe Q2 2026） | 0DTE SPX options share volume Cboe Q2 2026 65% | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641 （Investing.com） | 2026-05-31 | 2026-08-06T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 總成交量 16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 約 139.96、VIX 約 16.9 contango、TLT 1M skew 創 GFC 以來高 | VIX SKEW term structure bond volatility August 3 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher （Cboe） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt $1.502T、YoY +51.5%（交叉引用，不重複計入） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave 與 Anthropic 掛鉤 $2.6B 貸款調高收益率（2026-07-29）；Nebius $775M 擔保融資（2026-07-17） | CoreWeave 2.6 billion loan Anthropic yield boosted July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic （Bloomberg） | 2026-07-29 | 2026-08-06T09:30:00+08:00 |

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
  "prior_answer": "yes",
  "flip_evidence": ["valuation.ndx_drawdown", "ai.hyperscaler_capex", "valuation.ai_credit_schism"],
  "yes_basis": [],
  "r1_drawdown_pct": 3.83,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

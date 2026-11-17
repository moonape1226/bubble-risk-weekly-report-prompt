> [DRY RUN] this report was not committed to archive.

# 2026-08-06 AI 泡沫破裂預測報告

報告日期：2026-08-06｜ISO 週次：2026-W32｜預測窗口：2026-08-06 → 2027-02-04｜前次基準：report-2026-08-03（3天前）

## 結論

**結論：no**

三條路徑都沒有已在進行、可望於窗口內完成的跡象。NASDAQ-100 距 52 週高點回撤 3.83%，離 R1 門檻還差約 22%（`valuation.ndx_drawdown`）；hyperscaler 2026 capex 指引仍在上修，合計約 $725B（`ai.hyperscaler_capex`）。CoreWeave 信用利差急遽走闊（`valuation.ai_credit_schism`）是目前最強的 yes 方向訊號，但僅止於重定價，尚無付款違約或 distressed exchange。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,487.79（2026-08-05），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 3.83%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，從最新收盤還需再跌 6,492.34 點，即約 22.0%，才會觸發。S&P 500 收在 7,723.55，比 200 日均線高 9.71%、比 52 週均線高 11.32%（`valuation.sp500_trend`），價格延伸幅度大，均值回歸的空間不小。不過 VIX 在 7 日窗口（2026-07-29 → 2026-08-05）內下跌 23.48%，同期 S&P 500 上漲 5.57%，沒有出現指數與 VIX 同步上升的擁擠選擇權訊號（`structural.vix_spx_comove`）。估值方面，S&P 500 trailing P/E 29.74、Shiller CAPE 42.19（`valuation.sp500_pe_cape`），市場明顯偏貴。但 HY OAS 只有 2.73%（`monetary.hy_oas`），信用面還沒有開始向股市傳導壓力。

**判讀：** 距 R1 門檻約 22%，目前尚無正在進行的回撤。窗口內要觸發，需要 R3 信用事件外溢、hyperscaler 在財報季意外下修指引，或利率／期限溢價急升引發估值重定價。高 CAPE 加上 margin debt YoY +51.5%，代表一旦開始下跌，跌幅可能很深，但這是脆弱性，不是時點證據。

### R2 資本支出收縮

- Alphabet：在 2026 Q2 財報（2026-07-28 報導）**上修** 2026 capex 指引，市場對此反應負面，出現賣壓（`ai.hyperscaler_capex`）。
- Microsoft、Amazon、Meta：同一報導（2026-07-28）描述 hyperscaler 2026 capex 合計約 $725B 且「續上修」，但本次證據沒有逐家列出各公司的指引數字。三家都沒有任何**下修**披露，方向記為上修或持平（`ai.hyperscaler_capex`）。
- 四家之中目前**下修家數：0**。本次證據沒有載明下一次財報的具體日期；依季度節奏，2026 Q3（約 2026-10 下旬）與 2026 Q4（約 2027-01 下旬至 2 月初）兩輪財報都落在窗口內。
- 需求端仍偏緊：HBM／DRAM 合約價續升，H200 租金約 $4.39/hr，供給缺口延至 1H2027（`ai.compute_supply_demand`）。Microsoft RPO 約 $678B，其中約 32% 來自單一客戶 OpenAI（`ai.customer_concentration_rpo`）。這是集中度風險，但短期內反而支撐 capex 承諾。
- AI 營收對 capex 缺口（revenue-to-capex gap）：已披露的 AI 年化終端營收約 $72B（Anthropic 約 $47B＋OpenAI 約 $25B，資料日 2026-06-15），對比年化 capex 約 $725B。分母依 CNBC 報導的 hyperscaler 合計口徑，本次未逐家拆分，Oracle 也未單獨納入。缺口約 10 倍；因無可比前值，本次不判定方向（`ai.revenue_capex_gap`）。

**判讀：** R2 離觸發很遠。指引方向仍是上修，供給缺口預期延至 2027 上半年，兩輪財報內要有兩家由上修轉為下修，需要需求急遽崩落或融資受阻（例如 R3 或 R1 先發生），目前沒有證據指向這一點。

### R3 AI 信用事件

- CoreWeave：5Y CDS 約 855bp，$2.6B 貸款利差擴大 125bp，貸款投資人開始要求加強 covenants（2026-08-03，`valuation.ai_credit_schism`）。2026-07-29 CoreWeave 為 $2.6B 與 Anthropic 掛鉤的貸款調高票息（`structural.ai_infrastructure_debt`）。CoreWeave 以 AI 算力為主業，是最可能達到 R3 規模門檻的借款人，但本次證據沒有載明其總負債金額，未獨立驗證。
- Oracle：CDS 約 215bp（2026-08-03，`valuation.ai_credit_schism`）。不過 Oracle 的主業不是 AI 資料中心，不屬於 R3 定義的借款人。
- Nebius：2026-07-17 取得 $775M 擔保融資（`structural.ai_infrastructure_debt`），屬於持續融資，不是困境訊號。
- 本次證據中沒有任何 R3 合格借款人出現付款違約、covenant waiver、distressed exchange 或 going-concern 語句；近期到期與再融資時程也沒有披露。
- 整體信用環境：HY OAS 2.73%（−5bp）、IG OAS 0.78%（持平）（`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）1bp（`monetary.repo_stress_srf`）。系統性資金壓力不明顯。

**判讀：** AI 信用定價分歧（equity-vs-credit schism）已經在 CoreWeave 身上明顯浮現：信貸端開始重定價，屬於後期訊號。但從 855bp 的 CDS 走到超過寬限期的違約或 distressed exchange，中間還要經過流動性耗盡、再融資失敗等步驟。窗口內要觸發，需要 Anthropic／OpenAI 等核心客戶合約轉弱，或貸款市場關門。目前只看到重定價，看不到違約。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 約 855bp，$2.6B 貸款利差 +125bp，投資人要求 covenants，Oracle CDS 約 215bp（2026-08-03）。AI 信貸端已開始重定價，是三條路徑中最接近「進行中」的訊號 `valuation.ai_credit_schism`
- [R3] CoreWeave 2026-07-29 為 $2.6B 與 Anthropic 掛鉤的貸款調高收益率，顯示 AI 基礎設施的邊際融資成本正在上升 `structural.ai_infrastructure_debt`
- [R1] FINRA 6 月 margin debt $1.502T，YoY +51.5%（2026-07-20），已達歷史頂部附近的 +40–50% 區間，一旦下跌，被動去槓桿會放大回撤 `retail.margin_debt`
- [R1] S&P 500 trailing P/E 29.74、Shiller CAPE 42.19（2026-08-05）；S&P 500 比 200 日均線高 9.71%（2026-08-05），估值與價格延伸都偏高 `valuation.sp500_pe_cape` `valuation.sp500_trend`
- [R2] AI 年化終端營收約 $72B，對比 hyperscaler 年化 capex 約 $725B，缺口約 10 倍；Alphabet 上修 capex 後遭市場拋售（2026-07-28），代表投資人對 ROI 的容忍度在下降 `ai.revenue_capex_gap` `ai.hyperscaler_capex`
- [整體] 5Y 美債標售連續 14 次 tail，bid-to-cover 為 2022-09 以來最差（2026-07-28）；10Y 期限溢價（term premium）0.8681%（2026-07-31，trailing 7 日 +3bp），財政供給壓力可能推升折現率 `monetary.treasury_auctions` `monetary.term_premium`

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 3.83%（2026-08-05），距 R1 門檻水位 22,995.45 還差約 22%，且最新收盤接近高點 `valuation.ndx_drawdown`
- [R2] hyperscaler 2026 capex 合計約 $725B 且續上修，Alphabet 2026-07-28 上修指引；四家無一下修 `ai.hyperscaler_capex`
- [R2] HBM／DRAM 合約價續升，H200 租金約 $4.39/hr，供給缺口延至 1H2027（2026-08-01），目前看不到產能過剩或訂單消化 `ai.compute_supply_demand`
- [R3] HY OAS 2.73%（2026-08-04，−5bp）、IG OAS 0.78%（持平），整體信用利差仍處低檔，CoreWeave 的壓力尚未擴散 `monetary.hy_oas` `monetary.ig_oas`
- [整體] repo 資金壓力（SOFR−IORB）1bp、SOFR99−IORB 9bp（2026-08-04），SRF 動用 $0.001bn（2026-08-05）；MOVE 由 80.48 降至 73.58（2026-08-05），看不到國債市場失序（Treasury market dysfunction）的前兆 `monetary.repo_stress_srf` `structural.treasury_basis_trade`
- [整體] 7 日窗口（2026-07-29 → 2026-08-05）內 S&P 500 +5.57%、VIX −23.48%，沒有同步上升；CNN Fear & Greed 約 58（Greed，2026-08-05），AAII Bear 42.1%（2026-07-30），情緒並非極端狂熱 `structural.vix_spx_comove` `retail.fear_greed` `retail.aaii`

## 與前期比較

前次結論：無前次預測（report-2026-08-03 為舊格式評分報告）

上一份報告是舊格式評分報告，其分數不轉換成 yes/no，因此 flip_evidence 為 []。自 2026-08-03 以來的主要變化：

- S&P 500 自 prior-run 日起上漲 1.62%（2026-08-05：7,723.55），NASDAQ-100 回撤收斂至 3.83%（`valuation.sp500_trend`、`valuation.ndx_drawdown`）。
- 10Y 殖利率 −7bp（DGS10 4.63%）、實質殖利率 −3bp（DFII10 2.4%）、breakeven −5bp（T10YIE 2.22%）。因 ΔT10YIE 的視窗與另外兩腿不一致，本次 Δ 分解的驅動判讀為「不可判（視窗不一致）」（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。
- MOVE 由 80.48 降至 73.58，HY OAS −5bp，跨資產壓力下降（`structural.treasury_basis_trade`、`monetary.hy_oas`）。
- CoreWeave 信用重定價（2026-07-29 貸款收益率上調、2026-08-03 CDS 約 855bp）是本次新增最重要的負面訊號，但尚未構成 R3 事件（`valuation.ai_credit_schism`）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED（搜尋完成但無合格披露）：retail.naaim、institutional.bofa_jpm_survey、monetary.private_credit_liquidity、ai.token_growth、ai.hyperscaler_financing_mix（quarterly_state 有資料，但 30 日 event_scan 無新融資事件）、ai.depreciation_life、ai.capital_cycle（兩個組件都無可用披露）、structural.global_leveraged_approvals。這些缺漏中最可能影響結論的是私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）與 hyperscaler 融資結構（capex vs FCF / 發債）的事件掃描：若有未被捕捉的 gate proration / breach 或大型困境融資，會強化 R3 路徑。但兩者目前都只是「無披露」，不是反向證據，不足以翻轉結論。其餘缺漏屬於情緒與確認類輸入，不影響三條路徑的判讀。

另外，OpenAI／Anthropic 營收資料日期是 2026-06-15（上一季），以 stock-of-state 方式沿用；內部人賣股篩選僅列入有 EDGAR filing URL 的 SNOW 一筆，TEM 因缺少 filing URL 未具名引用。

最大的不確定性：

1. **CoreWeave 再融資與客戶合約**：如果貸款市場持續要求更高利差或 covenants，而 Anthropic 掛鉤的合約條件轉弱，R3 可能在窗口內由重定價演變成 distressed exchange，會把結論推向 yes。
2. **2026 Q3 財報季（約 2026-10 下旬）**：若兩家以上 hyperscaler 因 ROI 壓力由上修轉為下修，R2 即觸發；目前證據指向繼續上修，偏向 no。
3. **利率與期限溢價**：5Y 標售連續 tail、10Y 期限溢價（term premium）上行；若演變成標售失利或國債市場失序（Treasury market dysfunction），可能壓縮高估值股票的倍數，推升 R1 風險，偏向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7723.55 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 9.71 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 11.32 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較 prior-run 日 %） | 1.62 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29487.79 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 3.83 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1 季資料，家庭股票配置 %） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上緣 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下緣 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.73 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.63 | FRED API (series_id=DGS10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.4 | FRED API (series_id=DFII10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.22 | FRED API (series_id=T10YIE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD／桶，no_new_obs） | 81.96 | FRED API (series_id=DCOILWTICO) | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料，YoY %） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-08-06T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.26 | FRED API (series_id=T5YIFR) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright 10Y 期限溢價 %） | 0.8681 | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.66 | FRED API (series_id=SOFR) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.74 | FRED API (series_id=SOFR99) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-06 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（Fed 隔夜 repo transaction volume，十億美元） | 0.001 | FRED API (series_id=RPONTTLD) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.walcl | WALCL latest（百萬美元，no_new_obs） | 6738190.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（百萬歐元，no_new_obs） | 5941248.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（億日圓，no_new_obs） | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.81 | FRED API (series_id=VIXCLS) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of；base 2026-07-29，window 7 日，comove=false） | 15.81 | FRED API (series_id=VIXCLS, SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日 %） | -23.48 | FRED API (series_id=VIXCLS) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日 %） | 5.57 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（十億美元，no_new_obs） | 2004.9941（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-22 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口；delta_4w −52,919） | -7481041 | CFTC TFF futures-only | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（^MOVE；prior 80.48） | 73.58 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2342.8 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | SSGA／advisorperspectives WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報摘要 [primary: SEARCH]，90d＋同季 | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導 [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | financecharts WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | P&I WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | StockCharts WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA／Advisor Perspectives WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag WebSearch，7d | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／YCharts [primary: SEARCH] | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED DFEDTARU / DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（FRED BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（FRED BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（FRED DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（FRED T10YIE，FRED-direct） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（FRED DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（FRED CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（FRED T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（FRED THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（FRED SOFR／SOFR99／IORB／RPONTTLD） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | 標售 recap [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（FRED WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（FRED ECBASSETSW／JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | investing.com WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC／interval fund 披露 [primary: SEARCH]，30d | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報／財經報導 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／報導 WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話摘要 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce／jarvislabs [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：top-5 季頻 stock-of-state；event_scan：30d 發債／私募／hybrid 掃描 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 [primary: SEARCH]（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K／10-Q／法說 [primary: SEARCH]，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | quarterly_state：供需增速對比；event_scan：30d 進出場事件 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | Reuters／Benzinga／BusinessWire WebSearch，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | Renaissance Capital WebSearch，7d | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／StockAnalysis／StockTitan [primary: SEARCH]，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 WebSearch，30d | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 [primary: SEC EDGAR]，14d | ✓ SEARCH-VERIFIED |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | YCharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com／cryptobriefing [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF launches WebSearch，30d | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch，7d | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe insights WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（FRED VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | Advisor Perspectives WebSearch（交叉引用） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | Bloomberg 等 [primary: SEARCH]，30d | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds／move_index／ofr_repo（aggregation any） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.74 | S&P 500 trailing P/E August 5 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio（multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.19 | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 對指數溢價壓縮：Mag 7 約 29x vs 指數約 25.6x | Magnificent 7 valuation premium lowest decade 2026 | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026（SSGA；原定 SSGA／advisorperspectives） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標價 $285→$288，EPS-driven（EPS 修正主導，target PE 變動未披露） | Morgan Stanley NVDA target 288 July 2026 AI demand | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044（Investing.com） | 2026-07-13 | 2026-08-06T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 約 855bp、$2.6B 貸款利差 +125bp、Oracle CDS 約 215bp | CoreWeave CDS spread blows out 125 covenants Oracle August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm（Tech Times） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.rsp_spy | RSP 等權總報酬 YTD +14.26% 領先 SPY +13.71% | RSP vs SPY equal weight total return YTD August 2026 | https://www.financecharts.com/etfs/SPY/performance/total-return（FinanceCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度約 41% | S&P 500 top 10 concentration percent record 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/（Pensions & Investments） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| breadth.advance_decline | 約 64% S&P 500 成分股在 50DMA 上、A/D 創高、McClellan 轉負 | S&P 500 breadth percent above 50 day moving average August 2026 McClellan | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/（StockCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 58（Greed） | CNN Fear and Greed Index August 5 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives；原定 FINRA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| retail.aaii | AAII Bear 42.1%／Neutral 26.9%／Bull 31.0% | AAII investor sentiment survey July 30 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| retail.social_sentiment | Wendy's（WEN）「Save Wendy's」WSB 軋空、空頭部位約 44%（非 AI 標的） | Reddit WSB Wendy's WEN short squeeze August 2026 | https://finance.yahoo.com/markets/stocks/articles/reddit-wants-save-wendy-inside-161925726.html（Yahoo Finance） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.treasury_auctions | 5Y 標售連續 14 次 tail、bid-to-cover 為 2022-09 以來最差；7Y tail 0.8bp | US Treasury 5 year 7 year auction tail bid to cover July 2026 | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026（TFTC；原定 Reuters／Bloomberg recap） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| monetary.fedwatch | FOMC 7/29 鷹派持平；CME FedWatch 9 月定價約 62%，定價分歧 | CME FedWatch September 2026 probability FOMC hold | https://growbeansprout.com/tools/fedwatch（Beansprout；原定 CME FedWatch） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.pboc | 人行 7/29–8/3 逆回購約 ¥2.1T、7/24 MLF 淨投放 ¥100B | PBoC reverse repo injection 2.1 trillion yuan late July 2026 | https://www.investing.com/news/economy-news/chinas-pboc-to-conduct-overnight-reverse-repos-inject-a-total-of-21-trillion-yuan-4810853（Investing.com） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 續上修，合計約 $725B；Alphabet Q2 上修觸發賣壓 | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC；原定各家季報） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic run-rate 約 $47B、OpenAI 約 $25B | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-06-15 | 2026-08-06T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO 約 $678B，約 32% 繫於單一客戶（OpenAI） | Microsoft RPO backlog 678 billion single customer OpenAI 2026 | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/（Benzinga via TradingView） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| ai.compute_supply_demand | HBM／DRAM 合約續升、H200 租金約 $4.39/hr、缺口延至 1H2027 | H200 GPU rental price HBM DRAM contract 2026 shortage 2027 | https://jarvislabs.ai/blog/h200-price（JarvisLabs；原定 TrendForce） | 2026-08-01 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超越 FCF、2026 發債約 $182B、>$120B 表外 SPV 結構（季頻 stock-of-state；30d event_scan 無新事件） | hyperscaler capex FCF debt issuance 182 billion off balance sheet SPV 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure（Sage Advisory） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.revenue_capex_gap | AI 終端年化營收約 $72B（Anthropic $47B＋OpenAI $25B，2026-06-15）vs 年化 capex 約 $725B（CNBC hyperscaler 合計，2026-07-28） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI）；分母見 ai.hyperscaler_capex 列 | 2026-06-15 | 2026-08-06T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收投機 IPO 合格件數 0（7 日窗 2026-07-30 → 2026-08-06） | AI rename ticker SPAC no revenue IPO July 30 August 6 2026 | 檢查來源：Reuters、Benzinga、BusinessWire SPAC 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.ipo_heat | 本週約 21 檔跨週定價、無 blowout 首日；YTD 約 $251B／86 檔 | US IPO pricings week August 3 2026 Renaissance | https://www.renaissancecapital.com/IPO-Center/Pricings（Renaissance Capital） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週 microcap thematic moonshot 合格 0 件 | microcap 100% single day quantum fusion space nuclear small cap August 2026 | 檢查來源：Finviz、StockAnalysis、StockTitan gainers 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標約 $1T IPO；Anthropic 續進 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground（Benzinga） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| speculation.insider_form4 | SNOW 董事 Dageville：Form 4 filing／交易日 2026-07-29，售出 50,000 股約 $14.0M（TEM 一筆因缺 filing URL 未具名引用） | Snowflake Dageville Tempus Lefkofsky Form 4 insider sale July 2026 SEC | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1640147&type=4（SEC EDGAR） | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.55（日讀數） | Cboe equity put call ratio August 3 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio（YCharts；原定 Cboe） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高約 $198B | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing；原定 etf.com） | 2026-07-23 | 2026-08-06T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x 單股槓桿 ETF＋ELOL（TSLA+SpaceX）發行 | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html（GlobeNewswire） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量約 65%（Cboe Q2 2026） | 0DTE SPX options share volume Cboe Q2 2026 65% | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641（Investing.com；原定 Cboe） | 2026-05-31 | 2026-08-06T09:30:00+08:00 |
| structural.options_volume | OCC 6 月總量 16.0 億口（2026-06 月資料） | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 約 139.96、VIX 約 16.9 contango、TLT 1M skew 創 GFC 以來高 | VIX SKEW term structure bond volatility August 3 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher（Cboe） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt（2026-06 月資料）$1.502T、+51.5% YoY（交叉引用，不重複計入） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B 與 Anthropic 掛鉤貸款 2026-07-29 調高收益率；Nebius $775M 擔保融資 2026-07-17 | CoreWeave 2.6 billion loan Anthropic yield boosted July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic（Bloomberg） | 2026-07-29 | 2026-08-06T09:30:00+08:00 |

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

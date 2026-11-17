> [DRY RUN] this report was not committed to archive.

# 2026-08-06 AI 泡沫破裂預測報告
報告日期：2026-08-06｜ISO 週次：2026-W32｜預測窗口：2026-08-06 → 2027-02-04｜前次基準：report-2026-08-03（3天前）

## 結論

**結論：no**

三條路徑目前都離解析門檻很遠：NASDAQ-100 截至 2026-08-05 距 52 週高點回撤 3.83%，還要再跌約 22.02% 才觸及 R1；四家 hyperscaler 在 2026 年 7 月財報季是集體上修 capex，R2 所需的下修為 0 家。CoreWeave 信用利差走闊是最強的 yes 訊號，但截至 2026-08-06 未見任何付款違約或 distressed exchange，而 2026-08-04 HY OAS 收窄、2026-08-05 MOVE 回落，顯示壓力尚未向外傳導。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,487.79（2026-08-05），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 3.83%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，需自最新收盤再跌約 22.02% 才觸及。指數在 2026-07-29 收 27,192.31 的低點後已反彈。S&P 500 收 7,723.55（2026-08-05），高於 200 日均線 9.71%、高於 52 週均線 11.32%（`valuation.sp500_trend`），代表價格延伸程度偏高，有均值回歸空間。估值處於高檔：S&P 500 trailing P/E 29.74、Shiller CAPE 42.19（2026-08-05，`valuation.sp500_pe_cape`）。另一方面，VIX 由 20.66（2026-07-29）降至 15.81（2026-08-05），同期 S&P 500 上漲 5.57%，未出現同漲的 crowded-optionality 讀數（`structural.vix_spx_comove`）。槓桿部位偏高：FINRA margin debt $1.502T、YoY +51.5%（2026-06 月資料，`retail.margin_debt`），US 槓桿 ETF AUM 約 $198B 創新高（`structural.leveraged_etf_aum`）。一旦出現下跌催化劑，這些部位會放大跌幅。

**判讀：** R1 距離門檻約 22.02%，比前次基準時更遠。若要在窗口內觸發，需出現一次類似 2000 或 2022 年的估值重定價，通常要有信用事件（R3）或 capex 轉向（R2）作為催化劑，再經 margin debt 與槓桿 ETF 去槓桿放大。目前看不到已啟動的觸發鏈。

### R2 資本支出收縮

截至 2026-07-28，hyperscaler 2026 年 capex 指引合計約 $725B，且延續上修趨勢（`ai.hyperscaler_capex`）：

- Alphabet：2026 年第二季財報（2026-07 下旬）上修 2026 capex 指引，較前次指引為上修；財報後股價因 capex 增加而遭賣壓。
- Microsoft、Amazon、Meta：本次證據（CNBC 2026-07-28）只寫到四家合計約 $725B、整體續上修，沒有列出個別公司的數字。三家均無下修報導，方向依合計敘述列為上修或持平，未見下修。

目前四家中下修家數為 0。下一輪財報（2026 年第三季，約在 2026 年 10 月下旬）以及 2026 年第四季財報（約 2027 年 1 月下旬至 2 月初）都可能落在窗口內，具體日期本次證據未載。需求面仍偏緊：HBM／DRAM 合約價續升、H200 租金約 $4.39/hr、供給缺口延至 1H2027（2026-08-01，`ai.compute_supply_demand`）。財務面的壓力來自 AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 $72B（Anthropic 約 $47B＋OpenAI 約 $25B，沿用 2026-06-15 披露），對比年化 capex 約 $725B（分母：top-4 hyperscaler 合計），缺口仍大（`ai.revenue_capex_gap`）。

**判讀：** R2 目前朝反方向發展，上修多於下修。要在窗口內觸發，至少兩家必須在 2026 年第三或第四季財報中由上修轉為下修。這通常需要先出現 R1 等級的股價懲罰，或需求端轉弱（GPU 租金連同利用率下滑）。本次證據顯示算力仍短缺，因此近期觸發的可能性低。

### R3 AI 信用事件

最可能達到 R3 規模門檻的借款人是 CoreWeave（具體負債規模本次證據未載）。其 5Y CDS 約 855bp，一筆 $2.6B 貸款利差擴大 125bp，貸方開始要求 covenant；Oracle CDS 約 215bp（2026-08-03，`valuation.ai_credit_schism`）。CoreWeave 在 2026-07-29 調高一筆與 Anthropic 掛鉤、規模 $2.6B 貸款的票息；Nebius 於 2026-07-17 完成 $775M 擔保融資（`structural.ai_infrastructure_debt`）。這屬於 AI 信用定價分歧（equity-vs-credit schism）中「信貸端開始重定價」的後期型訊號。不過融資仍能完成，只是成本升高，截至 2026-08-06 未見付款違約、寬限期、破產申請或 distressed exchange。客戶集中度方面，Microsoft RPO 約 $678B，其中約 32% 繫於單一客戶 OpenAI（2026-07-30，`ai.customer_concentration_rpo`），屬於 backlog 重複計算風險（RPO double-counting）的結構性脆弱點。整體信用市場平靜：HY OAS 2.73%（2026-08-04，較前次 −5bp，`monetary.hy_oas`），IG OAS 0.78%（`monetary.ig_oas`），repo 資金壓力（SOFR−IORB）約 1bp（`monetary.repo_stress_srf`）。

**判讀：** R3 是三條路徑中最接近觸發的一條。CoreWeave 的 CDS 與貸款利差已在為違約風險定價，但仍有借新還舊的能力。要在窗口內觸發，需要一筆再融資失敗、主要客戶合約違約，或流動性斷裂而導致付款違約或 distressed exchange。目前證據停在「成本上升」，尚未到「市場關門」。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 約 855bp，$2.6B 貸款利差擴大 125bp，貸方要求 covenant；Oracle CDS 約 215bp（2026-08-03）。AI 借款人的信用端已開始重定價，而 NASDAQ-100 仍接近高點，兩者分歧未解（`valuation.ai_credit_schism`）
- [R3] CoreWeave 於 2026-07-29 調高與 Anthropic 掛鉤的 $2.6B 貸款票息，顯示 AI infrastructure debt financing / vendor-financing loops 的融資成本正在上升（`structural.ai_infrastructure_debt`）
- [R1] 槓桿與估值處於極端水位：margin debt $1.502T、YoY +51.5%（2026-06 月資料，`retail.margin_debt`）；Shiller CAPE 42.19（2026-08-05，`valuation.sp500_pe_cape`）；S&P 500 高於 200 日均線 9.71%（2026-08-05，`valuation.sp500_trend`）。一旦出現催化劑，下跌幅度可能很大
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 $72B，對比年化 capex 約 $725B（分母：top-4 hyperscaler），回本壓力大（`ai.revenue_capex_gap`）；Microsoft RPO 約 32% 繫於 OpenAI 單一客戶（2026-07-30，`ai.customer_concentration_rpo`）
- [整體] 美債標售需求（auction tail / bid-to-cover）轉弱：5Y 標售連續 14 次出現 tail，bid-to-cover 為 2022-09 以來最差，7Y tail 0.8bp（2026-07-28，`monetary.treasury_auctions`）；10Y 期限溢價（term premium）0.8681%，trailing 7 日 +3bp（2026-07-31，`monetary.term_premium`）。若長端利率再走高，可能壓縮估值

## 支持 no 的證據

- [R2] Hyperscaler 2026 capex 合計約 $725B 且持續上修，Alphabet 第二季上修（2026-07-28），四家下修家數為 0（`ai.hyperscaler_capex`）
- [R1] NASDAQ-100 距 52 週高點回撤 3.83%（2026-08-05），距 R1 門檻水位 22,995.45 約 22.02%，較前次基準時更遠（`valuation.ndx_drawdown`）
- [R3] 信用市場沒有向外傳導：HY OAS 2.73%（2026-08-04，−5bp，`monetary.hy_oas`），IG OAS 0.78% 持平（`monetary.ig_oas`），SOFR−IORB 約 1bp、SRF 動用約 $0.001bn（`monetary.repo_stress_srf`）
- [R2] 算力供給仍緊：HBM／DRAM 合約價上升，H200 租金約 $4.39/hr，供需缺口延至 1H2027（2026-08-01，`ai.compute_supply_demand`）。需求面目前沒有支持 capex 下修的證據
- [整體] 波動與情緒並不亢奮：VIX 15.81，較 7 日前下跌 23.48%（2026-08-05，`structural.vix_spx_comove`）；MOVE 由 80.48 降至 73.58（2026-08-05，`structural.treasury_basis_trade`）；AAII Bear 42.1%（2026-07-30，`retail.aaii`）；CNN Fear & Greed 約 58（2026-08-05，`retail.fear_greed`）

## 與前期比較

前次結論：yes（report-2026-08-03）
本次結論：翻轉
翻轉依據：
- `valuation.ndx_drawdown`（2026-08-05）：前次 forecast 記錄的 r1_drawdown_pct 為 7.78，本次為 3.83。觸及 R1 所需的再跌幅由約 18.67% 擴大到約 22.02%，07-29 的低點已被收復，R1 路徑明顯遠離。
- `monetary.hy_oas`（2026-08-04）：HY OAS 由 2.78% 收窄至 2.73%。CoreWeave 的個別信用壓力沒有擴散到整體高收益市場，R3 → R1 的傳導鏈未成形。
- `structural.treasury_basis_trade`（2026-08-05）：MOVE 由 80.48 回落至 73.58，CFTC 槓桿基金美債期貨淨部位 −7,481,041 口（2026-07-28），4 週變動僅 −52,919。債市波動降溫，美債基差交易槓桿被迫平倉的觸發風險下降。
- 未改變的部分：CoreWeave CDS 約 855bp（2026-08-03 資料，不晚於前次基準日，不作為翻轉依據）仍是最強的 yes 訊號，但本次結論回到 base rate。前次的 yes 缺乏「路徑已啟動」的證據，而 2026-08-03 之後的新資料一致指向壓力消退。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED（篩檢完成但無合格披露）：`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.private_credit_liquidity`、`ai.token_growth`、`ai.openai_anthropic_revenue`（最近披露為 2026-06-15，屬上一季，不視為本季新證據）、`ai.hyperscaler_financing_mix`（quarterly_state 可用：top-5 capex 已超過 FCF、2026 年發債約 $182B，2026-07-24；但 30 日內 event_scan 無新融資事件）、`ai.depreciation_life`、`ai.capital_cycle`（增速證據不足，本次不判定週期階段）、`structural.global_leveraged_approvals`。其中 `monetary.private_credit_liquidity` 與 `ai.hyperscaler_financing_mix` 的事件掃描缺漏最可能影響 R3 判讀：若有未被抓到的私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）或 hyperscaler 大額表外融資事件，R3 的距離可能被低估。不過整體 HY OAS 與 repo 數據沒有顯示對應壓力，因此不足以改變結論。

`speculation.insider_form4` 記為 0 件：搜尋找到 SNOW 與 TEM 的 insider 賣出，但缺少完整的 Form 4 申報日與 EDGAR filing URL，不符合 filing-level 要求，因此不列入證據。

10Y 殖利率分解：ΔDGS10 −7bp、ΔDFII10 −3bp、ΔT10YIE −5bp；T10YIE 與另兩腿的觀測視窗不一致，判讀為 不可判（視窗不一致）。

主要不確定性：
1. CoreWeave 的再融資與流動性路徑。若 2026 年下半年出現再融資失敗或客戶合約違約，R3 可能直接觸發並帶動 R1，結論會推向 yes。
2. 2026 年第三季 hyperscaler 財報（約 2026 年 10 月下旬）。若 Alphabet 因股價懲罰而轉為保守，並有第二家跟進，R2 會推向 yes；延續上修則強化 no。
3. 美債供給壓力。5Y 連續 tail 加上期限溢價上升，若演變成國債市場失序（Treasury market dysfunction），在高估值、高 margin debt 的環境下可能觸發 R1 等級的去槓桿，結論會推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7723.55 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 9.71 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 11.32 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29487.79 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 3.83 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026-Q1，家庭股票配置 %） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 2.73 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps（較前次 bps） | -5.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（IG OAS %） | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（10Y 殖利率 %） | 4.63 | FRED API (series_id=DGS10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（10Y 實質殖利率 %） | 2.4 | FRED API (series_id=DFII10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（10Y breakeven %） | 2.22 | FRED API (series_id=T10YIE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（WTI 美元／桶，無新觀測） | 81.96 | FRED API (series_id=DCOILWTICO) | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料 CPI YoY %） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-08-06T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（5y5y forward %） | 2.26 | FRED API (series_id=T5YIFR) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（10Y 期限溢價 %，Kim-Wright） | 0.8681 | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.66 | FRED API (series_id=SOFR) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（99th 分位 %） | 3.74 | FRED API (series_id=SOFR99) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-06 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用 transaction volume，十億美元） | 0.001 | FRED API (series_id=RPONTTLD) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.walcl | WALCL latest（Fed 資產負債表） | 6738190.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（ECB 資產負債表） | 5941248.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（BOJ 資產負債表） | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.81 | FRED API (series_id=VIXCLS) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of 值，comove=false） | 15.81 | fetch_macro.py 衍生區塊（FRED 波動率與指數日序） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日 %） | -23.48 | fetch_macro.py 衍生區塊（FRED 波動率與指數日序） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日 %） | 5.57 | fetch_macro.py 衍生區塊（FRED 波動率與指數日序） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（銀行對 NBFI 放款） | 2004.9941（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-22 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（槓桿基金美債期貨淨部位，口） | -7481041 | CFTC TFF futures-only | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（4 週變動，口） | -52919 | CFTC TFF futures-only | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（MOVE） | 73.58 | Yahoo Finance chart API (^MOVE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index prior（前次基準 MOVE） | 80.48 | Yahoo Finance chart API (^MOVE) | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2342.8 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation｜S&P 500 P/E and Shiller CAPE | multpl.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation｜Mag 7 weighted P/E and AI leader P/S | SSGA 研究 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation｜Analyst TP upgrade decomposition | 賣方 TP 報導 WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | Valuation｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | financecharts WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth｜Top-10 concentration in S&P 500 | P&I WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth｜Advance/decline ratio, new high/low ratio | StockCharts WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment｜CNN Fear & Greed Index | cnn.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment｜Margin Debt: FINRA monthly data | FINRA via Advisor Perspectives WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment｜Retail survey: AAII Investor Sentiment | aaii.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment｜Social sentiment proxies | Reddit WSB／cashtag WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment｜NAAIM Exposure Index | naaim.org／YCharts WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（FRED DFEDTARU、DFEDTARL） | ✓ API |
| monetary.hy_oas | Monetary & Credit｜High Yield OAS | scripts/fetch_macro.py（FRED BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit｜Investment Grade OAS | scripts/fetch_macro.py（FRED BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit｜10Y Treasury yield | scripts/fetch_macro.py（FRED DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit｜10Y breakeven inflation rate | scripts/fetch_macro.py（FRED T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit｜WTI crude oil price | scripts/fetch_macro.py（FRED DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（FRED CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit｜5y5y forward inflation expectation | scripts/fetch_macro.py（FRED T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（FRED THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（SOFR ok／SOFR99 ok／IORB ok／RPONTTLD ok） | ✓ API |
| monetary.treasury_auctions | Monetary & Credit｜美債標售需求（auction tail / bid-to-cover） | 標售 recap WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit｜Fed funds rate path expectations | CME FedWatch 摘要 WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（FRED WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit｜Global central bank liquidity cross-check — ECB / BOJ balance sheets | scripts/fetch_macro.py（ECBASSETSW ok／JPNASSETS ok） | ✓ API |
| monetary.pboc | Monetary & Credit｜PBoC aggregate financing / liquidity operations | investing.com WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit｜Private-credit / non-bank fund liquidity stress | BDC／interval fund 披露 WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals｜Hyperscaler capex guidance | 季報報導 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals｜OpenAI / Anthropic annualized revenue | Epoch／媒體 WebSearch（本季無新披露） | ✗ NOT DISCLOSED |
| ai.customer_concentration_rpo | AI Fundamentals｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話會報導 WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals｜AI compute supply/demand and overcapacity risk | GPU 租金／記憶體報價 WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：季報／研究 WebSearch；event_scan：30d 發債與融資掃描 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 WebSearch（stock-of-state，沿用最近組件） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals｜資本週期階段（capital cycle stage） | quarterly_state：供需增速 WebSearch；event_scan：30d 進出場事件掃描 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior｜Search for past 7 days: "AI rename" / SPAC | Reuters／Benzinga／BusinessWire WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior｜IPO market heat | Renaissance Capital WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior｜Microcap thematic moonshots | Finviz／StockAnalysis／StockTitan gainers WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior｜Upcoming AI IPOs | 具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior｜Cboe equity-only put/call ratio | YCharts WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage｜US leveraged ETF AUM | etf.com／媒體 WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage｜US single-stock leveraged ETF approvals | GlobeNewswire／發行商 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | Structural Leverage｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage｜0DTE option volume | Cboe 季報摘要 WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage｜Options total volume | OCC 月報 WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage｜Cross-asset derivatives / correlation checks | Cboe insights WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS ok／vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage｜Cross-reference only: FINRA margin debt | FINRA via Advisor Perspectives WebSearch（交叉引用） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage｜AI infrastructure debt financing / vendor-financing loops | Bloomberg 等 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds ok／move_index ok／ofr_repo ok） | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.74（原定 multpl） | S&P 500 trailing P/E August 5 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.19（原定 multpl） | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 約 29x vs 指數約 25.6x，溢價壓縮 | Magnificent 7 valuation premium lowest decade 2026 | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026 （SSGA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA TP $285→$288，EPS-driven（EPS Δ 與 target PE Δ 未披露） | Morgan Stanley NVDA target 288 July 2026 AI demand | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044 （Investing.com） | 2026-07-13 | 2026-08-06T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 約 855bp、$2.6B 貸款利差 +125bp、Oracle CDS 約 215bp | CoreWeave CDS spread blows out 125 covenants Oracle August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm （TechTimes） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD +14.26% vs SPY +13.71%（總報酬） | RSP vs SPY equal weight total return YTD August 2026 | https://www.financecharts.com/etfs/SPY/performance/total-return （FinanceCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度約 41% | S&P 500 top 10 concentration percent record 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/ （P&I） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| breadth.advance_decline | 約 64% 成分股在 50DMA 上、A/D 創高、McClellan 轉負 | S&P 500 breadth percent above 50 day moving average August 2026 McClellan | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/ （StockCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 58（Greed） | CNN Fear and Greed Index August 5 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives／FINRA） | 2026-06-30 | 2026-08-06T09:30:00+08:00 |
| retail.aaii | AAII Bear 42.1%／Neutral 26.9%／Bull 31.0% | AAII investor sentiment survey July 30 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| retail.social_sentiment | WSB「Save Wendy's」WEN 軋空題材、空頭比率約 44% | Reddit WSB Wendy's WEN short squeeze August 2026 | https://finance.yahoo.com/markets/stocks/articles/reddit-wants-save-wendy-inside-161925726.html （Yahoo Finance） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.treasury_auctions | 5Y 連續 14 次 tail、bid-to-cover 為 2022-09 以來最差；7Y tail 0.8bp | US Treasury 5 year 7 year auction tail bid to cover July 2026 | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026 （TFTC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| monetary.fedwatch | FOMC 7/29 鷹派按兵不動；CME FedWatch 9 月約 62%，定價分歧 | CME FedWatch September 2026 probability FOMC hold | https://growbeansprout.com/tools/fedwatch （Beansprout／CME FedWatch） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.pboc | 人行逆回購約 ¥2.1T、7/24 MLF 淨投放 ¥100B | PBoC reverse repo injection 2.1 trillion yuan late July 2026 | https://www.investing.com/news/economy-news/chinas-pboc-to-conduct-overnight-reverse-repos-inject-a-total-of-21-trillion-yuan-4810853 （Investing.com） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_capex | 2026 capex 合計約 $725B 續上修；Alphabet Q2 上修 | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO 約 $678B、約 32% 繫於 OpenAI | Microsoft RPO backlog 678 billion single customer OpenAI 2026 | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/ （Benzinga via TradingView） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| ai.compute_supply_demand | HBM／DRAM 合約續升、H200 租金約 $4.39/hr、缺口延至 1H2027 | H200 GPU rental price HBM DRAM contract 2026 shortage 2027 | https://jarvislabs.ai/blog/h200-price （JarvisLabs） | 2026-08-01 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超過 FCF；2026 年發債約 $182B | hyperscaler capex FCF debt issuance 182 billion 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure （Sage Advisory） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $72B（Anthropic $47B＋OpenAI $25B）vs 年化 capex 約 $725B（分母：top-4） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-06-15 | 2026-08-06T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收 IPO 合格件數 0 | AI rename ticker SPAC no revenue IPO July 30 August 6 2026 | Reuters／Benzinga／BusinessWire SPAC 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.ipo_heat | 約 21 檔跨週定價、無 blowout 首日、YTD 約 $251B／86 檔 | US IPO pricings week August 3 2026 Renaissance | https://www.renaissancecapital.com/IPO-Center/Pricings （Renaissance Capital） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot 合格件數 0 | microcap 100% single day quantum fusion space nuclear small cap August 2026 | Finviz／StockAnalysis／StockTitan gainers 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標約 $1T IPO、Anthropic 持續推進 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground （Benzinga） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| speculation.insider_form4 | 符合 filing-level 要求（申報日＋交易日＋EDGAR filing URL）的 Form 4 件數 0 | Snowflake Dageville Tempus Lefkofsky Form 4 insider sale July 2026 SEC | SEC EDGAR Form 4 搜尋（CIK 1640147 等） | — | 2026-08-06T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.55（日讀數） | Cboe equity put call ratio August 3 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio （YCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 約 $198B 創新高 | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing） | 2026-07-23 | 2026-08-06T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x 單股槓桿 ETF＋ELOL（TSLA+SpaceX）發行 | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權成交量約 65%（Cboe Q2 2026） | 0DTE SPX options share volume Cboe Q2 2026 65% | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641 （Investing.com） | 2026-05-31 | 2026-08-06T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月總量 16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 約 139.96、VIX 約 16.9 contango、TLT 1M skew 創 GFC 以來高 | VIX SKEW term structure bond volatility August 3 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher （Cboe） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-06 月資料）$1.502T、+51.5% YoY（交叉引用 Retail Sentiment） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B Anthropic 掛鉤貸款 07-29 調高票息；Nebius $775M 擔保 07-17 | CoreWeave 2.6 billion loan Anthropic yield boosted July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic （Bloomberg） | 2026-07-29 | 2026-08-06T09:30:00+08:00 |

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
  "flip_evidence": [
    "valuation.ndx_drawdown",
    "monetary.hy_oas",
    "structural.treasury_basis_trade"
  ],
  "r1_drawdown_pct": 3.83,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

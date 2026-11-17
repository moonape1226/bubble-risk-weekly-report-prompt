> [DRY RUN] this report was not committed to archive.

# 2026-08-06 AI 泡沫破裂預測報告

報告日期：2026-08-06｜ISO 週次：2026-W32｜預測窗口：2026-08-06 → 2027-02-04｜前次基準：report-2026-08-03（3天前）

## 結論

**結論：no**

三條路徑都沒有在窗口內完成的跡象：NASDAQ-100 距 R1 門檻仍需再跌約 22.02%（`valuation.ndx_drawdown`），hyperscaler 2026 capex 指引仍在上修、四家中尚無一家下修（`ai.hyperscaler_capex`）。CoreWeave 信用利差急遽走闊是本次最強的 yes 側訊號（`valuation.ai_credit_schism`），但它仍能完成新融資，且未出現付款違約或 distressed exchange，不足以把 R3 推過「多於不發生」的門檻。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,487.79（2026-08-05），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 3.83%（`valuation.ndx_drawdown`）。R1 門檻為 22,995.45，從最新收盤還需再跌約 22.02% 才會觸發。7 月底曾有一段明顯回落，2026-07-29 收盤 27,192.31（比高點低約 11.31%），之後一週反彈約 8%。S&P 500 收在 7,723.55（2026-08-05），高於 200 日均線 9.71%、高於 52 週均線 11.32%（`valuation.sp500_trend`），代表價格拉伸偏高，回檔空間大，但這是脆弱度訊號，本身不是觸發因子。估值偏高：S&P 500 trailing P/E 29.74、Shiller CAPE 42.19（`valuation.sp500_pe_cape`）。VIX 15.81，過去 7 日下跌 23.48%，S&P 500 同期上漲 5.57%，comove = false（`structural.vix_spx_comove`）；HY OAS 2.73%（`monetary.hy_oas`），信用市場整體沒有替股市定價下跌。

**判讀：** R1 離解析還很遠；在 182 天內要達成，需要由信用事件（R3）或 capex 撤退（R2）引發一次約 22% 以上的續跌。7 月底已證明 AI 權重股對 capex 消息的反應很劇烈，但目前缺少能帶動這種規模下跌的傳導機制（利差、資金面、強制去槓桿）。

### R2 資本支出收縮

CNBC 2026-07-28 報導：hyperscaler 2026 capex 合計約 $725B，且持續上修；Alphabet Q2 再度上修 capex，股價因此遭賣壓（`ai.hyperscaler_capex`）。本次取得的證據只逐家確立了 Alphabet 的方向（上修）。Microsoft、Amazon、Meta 的具體指引金額沒有逐家取得；報導的整體敘述是「續上修」，三家都沒有下修的證據。目前下修家數：0／4。下一次財報的具體日期本次未取得；窗口到 2027-02-04，應涵蓋後續的季報週期。需求面仍然吃緊：HBM／DRAM 合約價續升，H200 租金約 $4.39/hr，供給缺口據稱延續到 1H2027（`ai.compute_supply_demand`）。營收品質方面，Microsoft RPO 約 $678B，其中約 32% 繫於單一客戶（OpenAI）（`ai.customer_concentration_rpo`），屬 backlog 重複計算風險（RPO double-counting）的集中曝險。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 $72B（僅 Anthropic 約 $47B 加 OpenAI 約 $25B，取自 2026-06-15 的披露）對比年化 capex 約 $725B（分母為 CNBC 報導的 hyperscaler 合計，逐家涵蓋範圍未確立），缺口很大（`ai.revenue_capex_gap`）。

**判讀：** R2 離解析最遠。四家仍在上修，需求面證據也指向供給短缺而非過剩。窗口內要有兩家下修，需要急劇的需求斷裂，或由市場／信用壓力迫使 capex 紀律收緊（例如由 R1 或 R3 引發）。市場懲罰 Alphabet 上修是「投資人開始質疑 capex」的早期跡象，但指引方向還沒有轉變。

### R3 AI 信用事件

本次可確認的 AI 基礎設施借款人訊號：CoreWeave 5Y CDS 約 855bp，其 $2.6B 貸款利差擴大 125bp，貸款投資人要求加入 covenants；Oracle CDS 約 215bp（TechTimes，2026-08-03，`valuation.ai_credit_schism`）。CoreWeave 在 2026-07-29 調高一筆與 Anthropic 合約掛鉤、規模 $2.6B 的貸款票息；Nebius 於 2026-07-17 完成 $775M 擔保融資（`structural.ai_infrastructure_debt`）。這構成 AI 信用定價分歧（equity-vs-credit schism）的後期型態：信貸端開始重定價，而 NASDAQ-100 仍接近高點。但本次證據沒有出現付款違約、covenant waiver、distressed exchange 或 going-concern 措辭。CoreWeave 的總負債金額與近期到期結構，本次沒有取得可引用的來源，因此其是否達到 R3 的 50 億美元門檻「未確立」（不以記憶補數）。

**判讀：** R3 是三條路徑中最接近的，但仍有一段距離。約 855bp 的 CDS 反映市場要求很高的信用溢價，然而借款人仍能完成再融資（雖然代價更高），表示融資市場尚未關閉。窗口內要推過門檻，需要融資管道斷裂（新債無法發行或重大客戶合約違約），並演變成實際的付款違約或 distressed exchange。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 約 855bp，$2.6B 貸款利差擴大 125bp，投資人要求加入 covenants（2026-08-03），且 CoreWeave 在 2026-07-29 被迫調高同筆貸款的票息：AI 基礎設施信用正在重定價，股市卻仍接近高點，是典型的後期分歧（`valuation.ai_credit_schism`、`structural.ai_infrastructure_debt`）。
- [R1] 7 月底 NASDAQ-100 曾從 30,660.6 跌到 27,192.31（2026-07-29），Alphabet 上修 capex 反而遭賣壓（2026-07-28）：市場對 AI capex 的容忍度在下降，已證明有快速下跌的能力（`valuation.ndx_drawdown`、`ai.hyperscaler_capex`）。
- [整體] 美債標售需求（auction tail / bid-to-cover）轉弱：5Y 標售連續 14 次 tail，bid-to-cover 為 2022-09 以來最差，7Y tail 0.8bp（2026-07-28）；10Y 期限溢價（term premium）0.8681%，trailing 約 7 日上升 3bp（2026-07-31）。財政供給壓力會推高折現率，衝擊高估值成長股（`monetary.treasury_auctions`、`monetary.term_premium`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）：年化終端營收約 $72B 對比年化 capex 約 $725B；Microsoft RPO 約 $678B 中約 32% 繫於 OpenAI 單一客戶。一旦單一客戶的支付能力出現疑慮，capex 合理性會受衝擊（`ai.revenue_capex_gap`、`ai.customer_concentration_rpo`）。
- [整體] 估值與槓桿處於極端水位：Shiller CAPE 42.19、trailing P/E 29.74（2026-08-05）；FINRA 6 月 margin debt $1.502T，YoY +51.5%；美國槓桿 ETF 總 AUM 創高約 $198B（2026-07-23）。這些代表下跌一旦啟動，放大效應會很大（`valuation.sp500_pe_cape`、`retail.margin_debt`、`structural.leveraged_etf_aum`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 3.83%（2026-08-05），距 R1 門檻 22,995.45 還需再跌約 22.02%；且比前次存檔的 7.78% 更接近高點（`valuation.ndx_drawdown`）。
- [R2] hyperscaler 2026 capex 合計約 $725B 且續上修，Alphabet Q2 再上修（2026-07-28），四家下修數為 0；HBM／DRAM 合約價續升，H200 租金約 $4.39/hr，供給缺口延至 1H2027（2026-08-01）。需求面不支持窗口內出現兩家下修（`ai.hyperscaler_capex`、`ai.compute_supply_demand`）。
- [整體] 信用與資金面平靜：HY OAS 2.73%（較前次 −5bp）、IG OAS 0.78%（2026-08-04）；repo 資金壓力（SOFR−IORB）1bp，SOFR99−IORB 9bp，SRF 動用（Standing Repo Facility usage）0.001 十億美元，沒有可推動強制去槓桿的系統性壓力（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`）。
- [R3] AI 基礎設施借款人仍能取得融資：CoreWeave 完成 $2.6B 貸款（雖然調高票息，2026-07-29），Nebius 完成 $775M 擔保融資（2026-07-17）。融資管道開放時，短期內走到付款違約或 distressed exchange 的機率有限（`structural.ai_infrastructure_debt`）。
- [整體] 波動與情緒沒有出現 crowded-optionality 或狂熱：VIX 15.81，7 日跌 23.48%，與 S&P 500 沒有同漲（2026-08-05）；MOVE 73.58，較前次 −6.9（2026-08-05）；CNN Fear & Greed 約 58（2026-08-05）；AAII 看空 42.1% 高於看多 31.0%（2026-07-30）；RSP 等權 YTD +14.26% 領先 SPY +13.71%，漲勢並非只集中在少數股（`structural.vix_spx_comove`、`structural.treasury_basis_trade`、`retail.fear_greed`、`retail.aaii`、`breadth.rsp_spy`）。

## 與前期比較

前次結論：yes（report-2026-08-03）
本次結論：翻轉
前次存檔未記錄 yes_basis（該欄位存在之前寫入的預測），沒有逐項可回應的決定性理由；依規則 yes 必須每次重新取得，以下是本次在各路徑重新檢視後不再支持 yes 的依據：
翻轉依據：
- R1：NASDAQ-100 距 52 週高點回撤 3.83%（2026-08-05），前次存檔 r1_drawdown_pct 為 7.78，指數已反彈回接近高點，距門檻還需再跌約 22.02%（`valuation.ndx_drawdown`）。
- R2：hyperscaler 2026 capex 指引續上修至合計約 $725B（2026-07-28），四家下修數 0，沒有任何 R2 進行中的證據（`ai.hyperscaler_capex`）。
- R3：CoreWeave 利差走闊（CDS 約 855bp，2026-08-03）是真實的壓力訊號，但同期仍完成 $2.6B 貸款，Nebius 也完成 $775M 擔保融資；沒有違約、waiver 或 distressed exchange，且其負債規模在本次未確立（`valuation.ai_credit_schism`、`structural.ai_infrastructure_debt`）。
- 傳導：HY OAS 2.73%，較前次收窄 5bp；VIX 15.81，7 日下跌 23.48%，沒有從信用或波動端把 R3 傳導到 R1 的跡象（`monetary.hy_oas`、`structural.vix_spx_comove`）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源檢索完成但沒有合格的當期披露（✗ NOT DISCLOSED），依規則不得引用為證據：retail.naaim、institutional.bofa_jpm_survey、monetary.private_credit_liquidity、ai.token_growth、ai.openai_anthropic_revenue（最近一次披露是 2026-06-15，不屬當季，只作為 revenue-to-capex gap 的 carry-forward 組件）、ai.hyperscaler_financing_mix（quarterly_state 可用：top-5 capex 已超越 FCF，2026 發債約 $182B，表外 SPV 超過 $120B，日期 2026-07-24；但 30 日 event_scan 沒有新的融資事件，因此整列為 NOT DISCLOSED）、ai.depreciation_life、ai.capital_cycle（兩個組件皆無可用披露，本次不判定資本週期階段）、structural.global_leveraged_approvals。其中私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）與 hyperscaler 融資事件掃描的缺口最可能影響 R3 判讀：若實際上有未被搜尋到的 gate proration / breach 或 net inflow→outflow flip，R3 的傳導風險會被低估，但僅憑缺口不足以翻轉答案。

其他資料品質註記：speculation.insider_form4 找到 2 筆候選（SNOW、TEM），但缺 Form 4 申報日，TEM 也缺個別申報 URL 與金額，不符合 filing-level 標準，因此記為 0 件且不具名引用。structural.zero_dte 的 0DTE 佔比資料日期為 2026-05-31，較舊，只作背景。monetary.pboc 的搜尋結果中，逆回購區間（7/29–8/3）晚於發布日 2026-07-24，自相矛盾，只採用 7/24 MLF 數據。structural.us_single_stock_etf 的 GlobeNewswire 新聞稿 URL 日期為 2026-07-07（30 日窗邊界），搜尋表另列 2026-07-30，本次以較早的 2026-07-07 記錄。10Y 分解：ΔDGS10 −7bp、ΔDFII10 −3bp、ΔT10YIE −5bp，判讀為不可判（視窗不一致）。

最大的不確定性：
1. CoreWeave 的再融資路徑與負債總額（本次未確立）：如果下一筆融資失敗，或出現 covenant 違約，R3 會快速升溫，並可能經由信用重定價傳導到 R1，把答案推向 yes。
2. 下一輪 hyperscaler 財報（具體日期本次未取得）：任何一家明確下修 capex 都會讓 R2 與 R1 同時升溫，推向 yes；若持續上修，則強化 no。
3. 美債標售需求（auction tail / bid-to-cover）與 10Y 期限溢價（term premium）：若標售持續轉弱，帶動長端利率急升，估值壓縮可能加速 R1，推向 yes；CPI YoY 3.46% 也限制 Fed 降息緩衝的空間。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7,723.55 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 9.71 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 11.32 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29,487.79 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30,660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 3.83 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻） | 22,995.45 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1 家庭股票配置 %） | 45.76080873390133（約 45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.73 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | -5.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.63 | FRED API (series_id=DGS10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | -7.0 | FRED API (series_id=DGS10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.4 | FRED API (series_id=DFII10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | -3.0 | FRED API (series_id=DFII10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.22 | FRED API (series_id=T10YIE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | -5.0 | FRED API (series_id=T10YIE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl） | 81.96 | FRED API (series_id=DCOILWTICO) | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-08-06T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.26 | FRED API (series_id=T5YIFR) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR delta_bps | -5.0 | FRED API (series_id=T5YIFR) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 0.8681 | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 約 7 日） | 3.0 | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.66 | FRED API (series_id=SOFR) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.74 | FRED API (series_id=SOFR99) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-06 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.001（十億美元） | FRED API (series_id=RPONTTLD) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps（SOFR−IORB，IORB 取 2026-08-04） | 1.0 | FRED API (series_id=SOFR, IORB) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr99_iorb_bps（SOFR99−IORB，IORB 取 2026-08-04） | 9.0 | FRED API (series_id=SOFR99, IORB) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,738,190（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,941,248（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,442,957（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.81 | FRED API (series_id=VIXCLS) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（base 2026-07-29，window 7 日） | 15.81 | FRED API (vix_spx_comove block) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | -23.48 | FRED API (vix_spx_comove block) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | 5.57 | FRED API (vix_spx_comove block) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2,004.9941（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-22 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7,481,041 | CFTC TFF futures-only (cftc_lev_funds) | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -52,919 | CFTC TFF futures-only (cftc_lev_funds) | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.58 | Yahoo Finance chart API (^MOVE, move_index) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index delta_abs | -6.9 | Yahoo Finance chart API (^MOVE, move_index) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2,342.8 | OFR STFM (REPO-TRIV1_TV_TOT-P, ofr_repo) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | SSGA WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報摘要 WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | financecharts WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | P&I WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | StockCharts WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA／Advisor Perspectives WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／YCharts WebSearch | ✗ NOT DISCLOSED（無當週值） |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED（無新調查） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API DFEDTARU ok；DFEDTARL ok |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（FRED BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（FRED BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（FRED DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（FRED T10YIE 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（FRED DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（FRED T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | 標售 recap WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要 WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py | ✓ API ECBASSETSW ok；JPNASSETS ok |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | investing.com WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC／interval fund 披露 WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無合格披露） |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報報導 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／報導 WebSearch | ✗ NOT DISCLOSED（最新為 2026-06-15，非當季） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話報導 WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce／jarvislabs WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：Sage Advisory WebSearch；event_scan：30 日發債／SPV 掃描完成無新事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組件 carry-forward（Epoch 2026-06-15＋CNBC 2026-07-28） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無變動） |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速＋進出場事件 WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | Reuters／Benzinga／BusinessWire 螢幕（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | Renaissance Capital WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／StockAnalysis／StockTitan gainers 螢幕（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 篩選（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | YCharts WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing／etf.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF 發行 feed（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED（7 日內無英文披露） |
| structural.zero_dte | 結構｜0DTE option volume | Cboe 報導 WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe insights WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API VIXCLS ok；vix_spx_comove ok |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | Advisor Perspectives 交叉引用 | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | Bloomberg 等 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds／move_index／ofr_repo；WebSearch 補充無合格事件 | ✓ API cftc_lev_funds ok；move_index ok；ofr_repo ok |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.74 | S&P 500 trailing P/E August 5 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.19 | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 約 29x vs 指數約 25.6x，溢價壓縮 | Magnificent 7 valuation premium lowest decade 2026 | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026 （SSGA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA TP $285→$288，EPS-driven（EPS Δ／target PE Δ 未披露） | Morgan Stanley NVDA target 288 July 2026 AI demand | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044 （Investing.com） | 2026-07-13 | 2026-08-06T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 約 855bp；$2.6B 貸款利差 +125bp；Oracle CDS 約 215bp | CoreWeave CDS spread blows out 125 covenants Oracle August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm （TechTimes） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD +14.26% vs SPY +13.71%（總報酬） | RSP vs SPY equal weight total return YTD August 2026 | https://www.financecharts.com/etfs/SPY/performance/total-return （FinanceCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度約 41% | S&P 500 top 10 concentration percent record 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/ （P&I） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| breadth.advance_decline | 約 64% 成分股在 50DMA 上；A/D 創高；McClellan 轉負 | S&P 500 breadth percent above 50 day moving average August 2026 McClellan | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/ （StockCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 58（Greed） | CNN Fear and Greed Index August 5 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-06 月資料）$1.502T，YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives／FINRA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| retail.aaii | AAII Bear 42.1%／Neutral 26.9%／Bull 31.0% | AAII investor sentiment survey July 30 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| retail.social_sentiment | WSB「Save Wendy's」WEN 軋空，空頭比重約 44% | Reddit WSB Wendy's WEN short squeeze August 2026 | https://finance.yahoo.com/markets/stocks/articles/reddit-wants-save-wendy-inside-161925726.html （Yahoo Finance） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.treasury_auctions | 5Y 連 14 次 tail，bid-to-cover 為 2022-09 以來最差；7Y tail 0.8bp | US Treasury 5 year 7 year auction tail bid to cover July 2026 | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026 （TFTC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| monetary.fedwatch | FOMC 7/29 鷹派按兵不動；FedWatch 9 月約 62%，定價分歧 | CME FedWatch September 2026 probability FOMC hold | https://growbeansprout.com/tools/fedwatch （CME FedWatch 摘要） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.pboc | 人行 7/24 MLF 淨投放 ¥100B（同結果所列 7/29–8/3 逆回購晚於發布日，不採用） | PBoC reverse repo injection 2.1 trillion yuan late July 2026 | https://www.investing.com/news/economy-news/chinas-pboc-to-conduct-overnight-reverse-repos-inject-a-total-of-21-trillion-yuan-4810853 （Investing.com） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計約 $725B 續上修；Alphabet Q2 上修觸發賣壓 | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO 約 $678B，約 32% 繫單一客戶（OpenAI） | Microsoft RPO backlog 678 billion single customer OpenAI 2026 | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/ （Benzinga via TradingView） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| ai.compute_supply_demand | HBM／DRAM 合約續升；H200 租金約 $4.39/hr；缺口延至 1H2027 | H200 GPU rental price HBM DRAM contract 2026 shortage 2027 | https://jarvislabs.ai/blog/h200-price （JarvisLabs） | 2026-08-01 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超越 FCF；2026 發債約 $182B；表外結構逾 $120B | hyperscaler capex FCF debt issuance 182 billion off balance sheet SPV 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure （Sage Advisory） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $72B（Anthropic $47B＋OpenAI $25B）vs 年化 capex 約 $725B | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI；分母取自 CNBC 2026-07-28） | 2026-06-15 | 2026-08-06T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收 IPO 合格事件 0 件 | AI rename ticker SPAC no revenue IPO July 30 August 6 2026 | Reuters／Benzinga／BusinessWire SPAC 螢幕 | 2026-08-06 | 2026-08-06T09:30:00+08:00 |
| speculation.ipo_heat | 本週約 21 檔跨週定價，無 blowout 首日；YTD 約 $251B／86 檔 | US IPO pricings week August 3 2026 Renaissance | https://www.renaissancecapital.com/IPO-Center/Pricings （Renaissance Capital） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot 合格 0 件 | microcap 100% single day quantum fusion space nuclear small cap August 2026 | Finviz／StockAnalysis／StockTitan gainers 螢幕 | 2026-08-06 | 2026-08-06T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標約 $1T IPO；Anthropic 續進 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground （Benzinga） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| speculation.insider_form4 | 合格 Form 4 群聚 0 件（2 筆候選缺申報日／個別申報 URL，不合格） | Snowflake Dageville Tempus Lefkofsky Form 4 insider sale July 2026 SEC | SEC EDGAR Form 4 browse（CIK 1640147）、財經報導 | — | 2026-08-06T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.55（日讀數） | Cboe equity put call ratio August 3 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio （YCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高約 $198B | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing） | 2026-07-23 | 2026-08-06T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x 單股槓桿 ETF＋ELOL（TSLA+SpaceX）發行 | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-07 | 2026-08-06T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量約 65%（Cboe Q2 2026 簡報） | 0DTE SPX options share volume Cboe Q2 2026 65% | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641 （Investing.com） | 2026-05-31 | 2026-08-06T09:30:00+08:00 |
| structural.options_volume | OCC 總量（2026-06 月資料）16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 約 139.96；VIX 約 16.9 contango；TLT 1M skew 創 GFC 以來高 | VIX SKEW term structure bond volatility August 3 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher （Cboe） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt（2026-06 月資料）$1.502T，+51.5% YoY（交叉引用） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B Anthropic 掛鉤貸款調高票息（07-29）；Nebius $775M 擔保融資（07-17） | CoreWeave 2.6 billion loan Anthropic yield boosted July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic （Bloomberg） | 2026-07-29 | 2026-08-06T09:30:00+08:00 |

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
  "flip_evidence": ["valuation.ndx_drawdown", "ai.hyperscaler_capex", "valuation.ai_credit_schism", "structural.ai_infrastructure_debt", "monetary.hy_oas", "structural.vix_spx_comove"],
  "yes_basis": [],
  "r1_drawdown_pct": 3.83,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

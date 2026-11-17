> [DRY RUN] this report was not committed to archive.

# 2026-08-06 AI 泡沫破裂預測報告

報告日期：2026-08-06｜ISO 週次：2026-W32｜預測窗口：2026-08-06 → 2027-02-04｜前次基準：report-2026-08-03（3天前）

## 結論

**結論：no**

三條路徑目前都離解析門檻很遠：NASDAQ-100 只比 252 日高點低 3.83%，還需再跌約 22% 才觸及 R1；hyperscaler 2026 capex 仍在上修（合計 ≈$725B），沒有任何一家下修，R2 不成立。最可能先動的是 R3：CoreWeave 5Y CDS ≈855bp，貸款利差擴大 125bp，屬於明確的信用重定價，但目前沒有違約、寬限期外未付款或 distressed exchange 的跡象；HY OAS 只有 2.73%，代表信用壓力尚未擴散。在這種情況下，基準率仍站在 no 這一邊。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,487.79（2026-08-05），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 3.83%。R1 門檻水位為 22,995.45；從最新收盤算起還要再跌約 22.02% 才會觸發（`valuation.ndx_drawdown`）。2026-07-29 指數一度收在 27,192.31，比高點低約 11.3%，隨後一週反彈。同時 S&P 500 報 7,723.55，高於 200 日均線 9.71%、高於 52 週均線 11.32%，自前次基準以來上漲 1.62%（`valuation.sp500_trend`）。估值依然偏高：Shiller CAPE 42.19，trailing P/E 29.74（`valuation.sp500_pe_cape`）；margin debt 年增 +51.5%，落在歷史頂部附近的區間（`retail.margin_debt`）。另一方面，VIX 從 20.66 降到 15.81（−23.48%），同一窗口 S&P 500 上漲 5.57%，並未出現「股價與波動率同步上升」的 crowded-optionality 警訊（`structural.vix_spx_comove`）。

**判讀：** R1 距離門檻還很遠，需要在 182 天內從目前水位再跌約 22%。只有估值收縮與一個硬性催化劑同時出現才可能做到，例如 R3 信用事件外溢、hyperscaler 財報下修 capex，或國債市場失序（Treasury market dysfunction）迫使去槓桿。目前這些催化劑都還沒有發生。

### R2 資本支出收縮

- Alphabet：在 2026 Q2 財報（CNBC 2026-07-28 報導）**上修** 2026 capex 指引，市場對此以賣壓回應（`ai.hyperscaler_capex`）。
- Microsoft、Amazon、Meta：本次取得的資料只有 CNBC 2026-07-28 的合計敘述，即 hyperscaler 2026 capex 合計 ≈$725B 且「續上修」，沒有逐家列出指引金額與方向。三家都沒有找到下修報導，但各自相對前次指引的方向無法逐家確認（`ai.hyperscaler_capex`）。
- 目前已下修的家數：0／4（就已取得的資料而言）。下一輪 Q3 2026 財報與 Q4 2026 財報都落在窗口（→ 2027-02-04）內，確切日期本次未取得。
- 需求端支撐：HBM／DRAM 合約價持續上漲，H200 租金 ≈$4.39/hr，供需缺口預計延續到 1H2027（`ai.compute_supply_demand`，2026-08-01）。Microsoft RPO ≈$678B，其中約 32% 來自單一客戶 OpenAI（`ai.customer_concentration_rpo`，2026-07-30）。這顯示 backlog 高度集中，但本次只取得單一供應商的披露，無法加總計算 backlog 重複計算風險（RPO double-counting）。
- AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收 ≈$72B（Anthropic ≈$47B＋OpenAI ≈$25B，Epoch 2026-06-15 沿用值），對比年化 capex ≈$725B（分母：CNBC 報導的 hyperscaler 2026 capex 合計，涵蓋公司集合以該報導為準），缺口非常大。兩個組件自前次基準以來都沒有新披露，因此不視為新證據（`ai.revenue_capex_gap`）。

**判讀：** R2 目前完全不成立，方向甚至相反（capex 仍在上修）。要在窗口內成立，必須在 Q3 或 Q4 財報中有兩家正式下修。可能促成下修的情境是 R1 大幅回撤使市場懲罰 capex，或 AI 營收對 capex 缺口迫使管理層收縮。但算力供給仍緊、合約價還在上漲，短期內出現兩家同時下修的可能性不大。

### R3 AI 信用事件

- CoreWeave：5Y CDS ≈855bp；一筆與 Anthropic 合約掛鉤的 $2.6B 貸款利差擴大 125bp，貸方開始要求加上 covenants（`valuation.ai_credit_schism`，2026-08-03）。Bloomberg 2026-07-29 報導 CoreWeave 為這筆 $2.6B 貸款調高收益率（`structural.ai_infrastructure_debt`）。CoreWeave 是最可能符合 R3 規模門檻的 AI 基礎設施借款人，但它的負債總額不在本次 evidence 中，這裡只就定價做判讀。
- Oracle：5Y CDS ≈215bp（`valuation.ai_credit_schism`）。Oracle 並非以 AI 資料中心為主業，不符合 R3 借款人定義，只作為 AI 信用定價分歧（equity-vs-credit schism）的參照。
- Nebius：2026-07-17 完成 $775M 擔保融資（`structural.ai_infrastructure_debt`），顯示市場仍在承接 AI infrastructure debt financing / vendor-financing loops。
- 本次資料沒有任何 AI 基礎設施借款人出現未付款、covenant waiver、distressed exchange 或 going-concern 字樣，也沒有取得近期到期牆的具體金額。
- 整體信用環境仍然寬鬆：HY OAS 2.73%（−5bp，`monetary.hy_oas`），IG OAS 0.78%（持平，`monetary.ig_oas`）。

**判讀：** R3 是三條路徑中最接近觸發的一條。信貸端已經開始對 CoreWeave 重定價（利差走闊、要求 covenants），但同期 NASDAQ-100 仍接近高點，屬於後期分歧訊號。不過 855bp 的 CDS 反映的是「壓力定價」，而不是「已違約」。要在 182 天內完成破產、寬限期外違約或 distressed exchange，還需要發生再融資失敗或主要客戶合約斷裂；目前沒有證據顯示已經走到這一步。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS ≈855bp，$2.6B 貸款利差擴大 125bp，貸方要求加上 covenants（2026-08-03）；Oracle CDS ≈215bp。AI 信用定價已開始走闊，而股價尚未跟上，這是典型的後期分歧（`valuation.ai_credit_schism`）。
- [R3] CoreWeave 於 2026-07-29 為與 Anthropic 掛鉤的 $2.6B 貸款調高收益率，顯示 AI infrastructure debt financing 的邊際融資成本正在上升（`structural.ai_infrastructure_debt`）。
- [整體] 美債標售需求（auction tail / bid-to-cover）轉弱：5Y 連續 14 次 tail，bid-to-cover 為 2022-09 以來最差，7Y tail 0.8bp（2026-07-28）。若財政供給壓力外溢成長端利率上升，會壓縮 AI 高估值（`monetary.treasury_auctions`）。
- [R1] 估值與槓桿都處於極端水位：Shiller CAPE 42.19、trailing P/E 29.74（2026-08-05，`valuation.sp500_pe_cape`）；FINRA margin debt $1.502T，YoY +51.5%（2026-06 月資料，`retail.margin_debt`）；US 槓桿 ETF AUM 創新高 ≈$198B（`structural.leveraged_etf_aum`）。這代表一旦開始回撤，下跌幅度可能很大。
- [R1] NASDAQ-100 在 2026-07-29 一度收在 27,192.31，比高點低約 11.3%，顯示指數對 Alphabet capex 上修這類消息相當敏感（`valuation.ndx_drawdown`）；同一份報導記錄了市場對 capex 上修的負面反應（`ai.hyperscaler_capex`）。
- [整體] 債市波動出現升溫跡象：Cboe 2026-08-03 週報指出 TLT 1M skew 創 GFC 以來新高，SKEW ≈139.96（`structural.cross_asset_derivatives`）；10Y 期限溢價（term premium）0.8681%，trailing 7 天 +3bp（2026-07-31，`monetary.term_premium`）。

## 支持 no 的證據

- [R1] NASDAQ-100 最新收盤 29,487.79，只比 252 日高點 30,660.6 低 3.83%，離 R1 門檻 22,995.45 還差約 22.02%（2026-08-05，`valuation.ndx_drawdown`）；S&P 500 自前次基準以來上漲 1.62%（`valuation.sp500_trend`）。
- [R2] hyperscaler 2026 capex 合計 ≈$725B 且仍在上修，Alphabet 剛上修，四家中沒有任何一家下修（2026-07-28，`ai.hyperscaler_capex`）。
- [R2] 算力仍然短缺：HBM／DRAM 合約價持續上漲，H200 租金 ≈$4.39/hr，缺口延續到 1H2027（2026-08-01，`ai.compute_supply_demand`）。需求端不支持短期 capex 收縮。
- [R3] 信用壓力沒有擴散：HY OAS 2.73%（2026-08-04，`monetary.hy_oas`），IG OAS 0.78%（`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）只有 +1bp，SOFR99−IORB +9bp，SRF 動用（Standing Repo Facility usage）僅 $0.001bn（`monetary.repo_stress_srf`）。
- [整體] 美債基差交易槓桿（Treasury basis-trade leverage）沒有平倉跡象：CFTC 槓桿基金淨部位 −7,481,041 口（2026-07-28），4 週變化 −52,919 口，大致持平；MOVE 從 80.48 降到 73.58（2026-08-05），OFR 三方 repo 交易量 $2,342.8bn（`structural.treasury_basis_trade`）。
- [R1] 情緒沒有到亢奮：CNN Fear & Greed ≈58（`retail.fear_greed`）；AAII Bear 42.1% 高於 Bull 31.0%（2026-07-30，`retail.aaii`）；RSP 年初至今 +14.26%，領先 SPY 的 +13.71%，市場廣度在擴散而不是收窄（`breadth.rsp_spy`）。
- [R3] Nebius 於 2026-07-17 完成 $775M 擔保融資，AI 基礎設施借款人仍能進入資本市場（`structural.ai_infrastructure_debt`）。

## 與前期比較

前次結論：無前次預測（report-2026-08-03 為舊格式評分報告）

report-2026-08-03 是舊格式評分報告，沒有 yes/no 預測可以比較，flip_evidence 為 []。自 2026-08-03 以來的主要變化如下：

- NASDAQ-100 從 28,776.80 回升到 29,487.79；S&P 500 上漲 1.62%；VIX 從 15.86 降到 15.81；MOVE 從 80.48 降到 73.58。
- 10Y 殖利率 −7bp（4.70% → 4.63%），10Y 實質利率 −3bp，10Y breakeven −5bp。分解判讀為不可判（視窗不一致）。
- HY OAS −5bp，降到 2.73%；IG OAS 持平在 0.78%。
- CoreWeave 信用重定價的報導（2026-08-03）與前次基準同日，可以視為本次判讀 R3 的主要新增資訊，但還沒有達到違約事件的程度。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源完成了檢索，但沒有合格的當期披露（✗ NOT DISCLOSED）或為 0 件：

- retail.naaim、institutional.bofa_jpm_survey、monetary.private_credit_liquidity、ai.token_growth、ai.depreciation_life、structural.global_leveraged_approvals：沒有找到窗口內的披露。其中最可能影響結論的是 monetary.private_credit_liquidity：如果之後出現多檔基金 redemption-request ratio 同步上升、gate proration / breach，或 net inflow→outflow flip，就會強化 R3 路徑。本次沒有這類證據，不改變答案。
- ai.openai_anthropic_revenue：最新可得數字（Epoch 2026-06-15：Anthropic ≈$47B、OpenAI ≈$25B）屬於上一季，沒有本季披露，因此標為 ✗ NOT DISCLOSED；ai.revenue_capex_gap 依 stock-of-state 規則沿用這些組件。
- ai.hyperscaler_financing_mix：quarterly_state 有資料（Sage Advisory 2026-07-24：top-5 capex 已超過 FCF，2026 發債 ≈$182B，另有 >$120B 的表外 SPV），但 30 日 event_scan 沒有找到 hyperscaler 新的大額融資事件，依 component_aggregation: all 標為 ✗ NOT DISCLOSED，在正文不作為證據引用。這份 hyperscaler 融資結構（capex vs FCF / 發債）的背景屬於 R3 的長期脆弱性，不屬於窗口內的觸發事件。
- ai.capital_cycle：兩個組件都沒有可用證據，本次不判定資本週期階段（capital cycle stage）。
- speculation.insider_form4：搜尋結果有兩筆 Form 4 相關報導，但都缺少 Form 4 filing date 與具體的 SEC EDGAR filing URL，不符合 filing-level 引用條件，依規則記為 0 件且不列出姓名或金額。
- speculation.ai_rename_spac、speculation.microcap_moonshots：7 日螢幕篩選結果皆為 0 件合格事件。

最大的三個不確定性：

1. CoreWeave 的再融資路徑：負債總額與近期到期金額本次都沒有取得。如果利差持續走闊並出現 covenant waiver 或 distressed exchange，R3 可能在窗口內成立，並經由 AI 信用定價分歧外溢到 R1，答案會往 yes 移動。
2. Q3 2026 與 Q4 2026 hyperscaler 財報（都在窗口內）：只要有兩家下修 capex，R2 就成立。以目前上修的趨勢來看，這件事會讓答案往 yes 移動，但目前可能性偏低。
3. 美債供給與期限溢價：標售 tail 持續、10Y 期限溢價（term premium）上升。如果演變成國債市場失序（Treasury market dysfunction）並引發去槓桿，可能觸發 R1，答案會往 yes 移動；目前 MOVE 回落、repo 資金壓力（SOFR−IORB）偏低，這個路徑仍屬尾部風險。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7723.55 | FRED API (series_id=SP500), sp500_trend | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 9.71 | FRED API (series_id=SP500), sp500_trend | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 11.32 | FRED API (series_id=SP500), sp500_trend | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（自前次基準 %） | 1.62 | FRED API (series_id=SP500), sp500_trend | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29487.79 | FRED API (series_id=NASDAQ100), ndx_drawdown | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100), ndx_drawdown | 2026-06-02 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（%） | 3.83 | FRED API (series_id=NASDAQ100), ndx_drawdown | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100), ndx_drawdown | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q1，%） | 45.7608 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（%） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（%） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
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
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料，%） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-08-06T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.26 | FRED API (series_id=T5YIFR) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（%，Kim-Wright） | 0.8681 | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 天） | 3.0 | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.66 | FRED API (series_id=SOFR) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.74 | FRED API (series_id=SOFR99) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-06 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.001 | FRED API (series_id=RPONTTLD) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,738,190（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,941,248（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,442,957（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.81 | FRED API (series_id=VIXCLS) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of） | 15.81 | macro block vix_spx_comove（FRED VIXCLS＋SP500） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日窗，base 2026-07-29） | -23.48 | macro block vix_spx_comove（FRED VIXCLS＋SP500） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日窗） | 5.57 | macro block vix_spx_comove（FRED VIXCLS＋SP500） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2004.9941（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-22 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（口） | -7481041 | CFTC TFF futures-only, cftc_lev_funds | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -52919 | CFTC TFF futures-only, cftc_lev_funds | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.58 | Yahoo chart ^MOVE, move_index | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo 交易量） | 2342.8 | OFR STFM REPO-TRIV1_TV_TOT-P, ofr_repo | 2026-08-05 | 2026-08-06T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | SSGA 等 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報摘要 WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | financecharts WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | P&I WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | StockCharts WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA / Advisor Perspectives WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB / cashtag WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | 散戶｜Household equity allocation: FRED BOGZ1FL153064486Q | scripts/fetch_macro.py | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim / YCharts WebSearch [primary: SEARCH] | ✗ NOT DISCLOSED 無當週值 |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED 無新月度調查 |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED DFEDTARU / DFEDTARL | scripts/fetch_macro.py | ✓ API DFEDTARU ok; DFEDTARL ok |
| monetary.hy_oas | 貨幣｜High Yield OAS: FRED BAMLH0A0HYM2 | scripts/fetch_macro.py | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS: FRED BAMLC0A0CM | scripts/fetch_macro.py | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield: FRED DGS10 | scripts/fetch_macro.py | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS: FRED DFII10 | scripts/fetch_macro.py | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate: FRED T10YIE | scripts/fetch_macro.py（FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price: FRED DCOILWTICO | scripts/fetch_macro.py | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED CPIAUCSL | scripts/fetch_macro.py（yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation: FRED T5YIFR | scripts/fetch_macro.py | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED THREEFYTP10 | scripts/fetch_macro.py（Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED SOFR / SOFR99 / IORB / RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API SOFR ok; SOFR99 ok; IORB ok; RPONTTLD ok |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | Reuters / Bloomberg recap WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED WALCL | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py | ✓ API ECBASSETSW ok; JPNASSETS ok |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | investing.com WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC / interval fund 披露 WebSearch（30d） | ✗ NOT DISCLOSED 30 日內無合格披露 |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報報導 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic / OpenAI / Google 披露 WebSearch | ✗ NOT DISCLOSED 本季無披露 |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch / 報導 WebSearch | ✗ NOT DISCLOSED 最新值為上一季（2026-06-15） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話報導 WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce / jarvislabs WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state 季報彙整 WebSearch；event_scan 30 日發債掃描 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組件沿用（Epoch＋CNBC）WebSearch | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K / 10-Q WebSearch（30d） | ✗ NOT DISCLOSED 30 日內無變動 |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速＋進出場事件 WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | Reuters / Benzinga / BusinessWire WebSearch | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | Renaissance Capital WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz / StockAnalysis / StockTitan WebSearch | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | YCharts WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing / etf.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire / ETF launches WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX / TWSE / JPX / ESMA WebSearch（7d） | ✗ NOT DISCLOSED 7 日內無英文披露 |
| structural.zero_dte | 結構｜0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC monthly | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe insights WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API VIXCLS ok; vix_spx_comove ok |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 retail.margin_debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | Bloomberg 等 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions: FRED LNFACBW027SBOG | scripts/fetch_macro.py | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds / move_index / ofr_repo；WebSearch 無新增事件 | ✓ API cftc_lev_funds ok; move_index ok; ofr_repo ok |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.74 | S&P 500 trailing P/E August 5 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio（multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.19 | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 ≈29x vs 指數 ≈25.6x，溢價壓縮 | Magnificent 7 valuation premium lowest decade 2026 | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026（SSGA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA TP $285 → $288，EPS-driven（EPS Δ／target PE Δ 未披露） | Morgan Stanley NVDA target 288 July 2026 AI demand | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044（Investing.com） | 2026-07-13 | 2026-08-06T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS ≈855bp、$2.6B 貸款利差 +125bp、Oracle CDS ≈215bp | CoreWeave CDS spread blows out 125 covenants Oracle August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm（Tech Times） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD +14.26% vs SPY +13.71% | RSP vs SPY equal weight total return YTD August 2026 | https://www.financecharts.com/etfs/SPY/performance/total-return（FinanceCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 ≈41% | S&P 500 top 10 concentration percent record 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/（P&I） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| breadth.advance_decline | ≈64% 成分股在 50DMA 上、A/D 創高、McClellan 轉負 | S&P 500 breadth percent above 50 day moving average August 2026 McClellan | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/（StockCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed ≈58（Greed） | CNN Fear and Greed Index August 5 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| retail.aaii | AAII Bear 42.1%／Neutral 26.9%／Bull 31.0% | AAII investor sentiment survey July 30 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| retail.social_sentiment | WSB「Save Wendy's」WEN 軋空討論，≈44% 空頭部位 | Reddit WSB Wendy's WEN short squeeze August 2026 | https://finance.yahoo.com/markets/stocks/articles/reddit-wants-save-wendy-inside-161925726.html（Yahoo Finance） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.treasury_auctions | 5Y 連 14 次 tail、bid-to-cover 為 2022-09 以來最差；7Y tail 0.8bp | US Treasury 5 year 7 year auction tail bid to cover July 2026 | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026（TFTC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| monetary.fedwatch | FOMC 7/29 鷹派按兵不動；CME FedWatch 9 月會議 ≈62%，定價分歧 | CME FedWatch September 2026 probability FOMC hold | https://growbeansprout.com/tools/fedwatch（Beansprout FedWatch） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.pboc | 人行公告 7/29–8/3 逆回購合計 ≈¥2.1T、7/24 MLF 淨投放 ¥100B | PBoC reverse repo injection 2.1 trillion yuan late July 2026 | https://www.investing.com/news/economy-news/chinas-pboc-to-conduct-overnight-reverse-repos-inject-a-total-of-21-trillion-yuan-4810853（Investing.com） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計 ≈$725B 續上修；Alphabet Q2 上修觸發賣壓 | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO ≈$678B，≈32% 繫於單一客戶 OpenAI | Microsoft RPO backlog 678 billion single customer OpenAI 2026 | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/（Benzinga via TradingView） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| ai.compute_supply_demand | HBM/DRAM 合約續升、H200 租金 ≈$4.39/hr、缺口延至 1H2027 | H200 GPU rental price HBM DRAM contract 2026 shortage 2027 | https://jarvislabs.ai/blog/h200-price（Jarvislabs） | 2026-08-01 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超越 FCF、2026 發債 ≈$182B、>$120B 表外結構 | hyperscaler capex FCF debt issuance 182 billion off balance sheet SPV 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure（Sage Advisory） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.revenue_capex_gap | 分子：Anthropic ≈$47B＋OpenAI ≈$25B ≈$72B（沿用） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-06-15 | 2026-08-06T09:30:00+08:00 |
| ai.revenue_capex_gap | 分母：hyperscaler 2026 capex 合計 ≈$725B | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收投機 IPO 合格事件 0 件 | AI rename ticker SPAC no revenue IPO July 30 August 6 2026 | Reuters / Benzinga / BusinessWire SPAC 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.ipo_heat | 本週 ≈21 檔跨週定價、無 blowout 首日、YTD ≈$251B／86 檔 | US IPO pricings week August 3 2026 Renaissance | https://www.renaissancecapital.com/IPO-Center/Pricings（Renaissance Capital） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot 合格 0 件 | microcap 100% single day quantum fusion space nuclear small cap August 2026 | Finviz / StockAnalysis / StockTitan gainers 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 ≈$1T IPO、Anthropic 續進 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground（Benzinga） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4（具 filing date＋filing URL）0 件；搜尋結果缺 filing-level 欄位 | Snowflake Dageville Tempus Lefkofsky Form 4 insider sale July 2026 SEC | SEC EDGAR company browse（Form 4 清單）、新聞摘要 | — | 2026-08-06T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.55（日讀數） | Cboe equity put call ratio August 3 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio（YCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高 ≈$198B | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing） | 2026-07-23 | 2026-08-06T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x 單股槓桿 ETF＋ELOL（TSLA＋SpaceX）發行 | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html（GlobeNewswire；URL 路徑 2026-07-07，亦在 30 日窗內） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量 ≈65%（Cboe Q2 2026） | 0DTE SPX options share volume Cboe Q2 2026 65% | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641（Investing.com） | 2026-05-31 | 2026-08-06T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月總量 16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW ≈139.96、VIX ≈16.9 contango、TLT 1M skew 創 GFC 以來高 | VIX SKEW term structure bond volatility August 3 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher（Cboe） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-06 月資料）$1.502T、YoY +51.5%（交叉引用） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B Anthropic 掛鉤貸款調高收益率 | CoreWeave 2.6 billion loan Anthropic yield boosted July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic（Bloomberg） | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Nebius $775M 擔保融資（2026-07-17） | CoreWeave 2.6 billion loan Anthropic yield boosted July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic（Bloomberg 同篇） | 2026-07-17 | 2026-08-06T09:30:00+08:00 |

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

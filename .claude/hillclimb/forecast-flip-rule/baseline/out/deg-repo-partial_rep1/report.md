> [DRY RUN] this report was not committed to archive.
# 2026-11-08 AI 泡沫破裂預測報告
報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：report-2026-10-18（21天前）

## 結論

**結論：yes**

三條路徑同時在推進，且信用端已出現具體壓力：CoreWeave 五年期 CDS 於 2026-11-05 突破 1289 bps、債券殖利率於 2026-11-06 升破 16%（`valuation.ai_credit_schism`），NASDAQ-100 已距 52 週高點回撤 13.56%（`valuation.ndx_drawdown`），而 Microsoft 已於 2026-10-29 將 capex 指引下修（`ai.hyperscaler_capex`）。在 CPI YoY 3.72% 與市場定價 12 月升息 76.8%（`monetary.fedwatch`）之下，Fed 緩衝空間受限，R3→R1→R2 的傳導鏈在 182 天內完成至少一條的可能性高於不完成。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 26989.99（2026-11-06），252 個交易日最高收盤 31224.69（2026-10-06），距 52 週高點回撤 13.56%（`valuation.ndx_drawdown`）。R1 門檻水位為 23418.52，自最新收盤再下跌約 13.23% 即觸發。回撤集中於一個月內：2026-11-05 收盤 26629.81 為近期低點，2026-11-06 小幅反彈。同期 S&P 500 收 7353.73（2026-11-05），僅高於 200 日均線 0.42%、高於 52 週均線 1.84%，自前次基準（2026-10-16 的 7659.44）下跌 3.99%（`valuation.sp500_trend`）。VIX 於 2026-11-05 升至 28.18，7 日內（基準 2026-10-29 的 17.2）上升 63.84%，同窗 S&P 500 下跌 4.75%，屬正常的股跌—波動升關係，非 crowded-optionality 共振（comove=false，`structural.vix_spx_comove`）。估值仍高：Shiller CAPE 38.91、trailing P/E 25.14（2026-11-06，`valuation.sp500_pe_cape`），下修空間大。

**判讀：** 已走完通往 R1 門檻約一半的距離；若 R3 信用事件落地或 12 月 FOMC 升息確認並引發再一輪 AI 估值壓縮，窗口內再跌約 13.23% 屬可達範圍，但目前尚未觸發。

### R2 資本支出收縮

- Microsoft：2026 年資本支出指引自約 175 下調至約 170（2026-10-29 季報，方向：下修）（`ai.hyperscaler_capex`）。
- Alphabet：本次證據未取得最新指引數值，方向無法判定。
- Amazon：本次證據未取得最新指引數值，方向無法判定。
- Meta：本次證據未取得最新指引數值，方向無法判定。

目前已確認下修者 1 家（Microsoft），尚需四家中再一家下修。四家下一次季報日期本次證據未載，但依季報節奏，下一輪財報應落在窗口內（2027 年初）。融資面，hyperscaler 今年以來發債 296、10/29 起一週內 5 筆 AI 相關債券發行合計 67（2026-11-06，`ai.hyperscaler_financing_mix`），顯示 hyperscaler 融資結構（capex vs FCF / 發債）正由現金流轉向舉債。

**判讀：** 1/4 已下修；若 R1 回撤延續或 R3 信用壓力推高融資成本，下一輪季報再有一家下修即觸發 R2，這是窗口內可見的排程催化劑。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）已轉為信貸端先行重定價：CoreWeave 五年期 CDS 突破 1289 bps（2026-11-05），報導指出此時 Nasdaq 仍在反彈；CoreWeave 債券殖利率升破 16%（2026-11-06）（`valuation.ai_credit_schism`）。AI infrastructure debt financing / vendor-financing loops 端，ING 出售 12 筆資料中心貸款、規模約 500（2026-11-06，`structural.ai_infrastructure_debt`），顯示銀行端開始降低 AI 資料中心曝險。CoreWeave 的總負債規模、近期到期與再融資日程本次證據未載，無法在報告內直接核實其是否超過 R3 50 億美元門檻；本次證據亦未見付款違約、covenant waiver 或 going-concern 字樣。整體信用市場尚未擴散：HY OAS 3.48%（+17 bps）、IG OAS 0.93%（+8 bps）（2026-11-05，`monetary.hy_oas`、`monetary.ig_oas`）。

**判讀：** CDS 逾 1000 bps 屬典型困境定價區間，市場已在為 distressed exchange 或違約定價；若窗口內出現交換要約、寬限期違約或再融資失敗，即觸發 R3，並可能連鎖推動 R1。

## 支持 yes 的證據

- [R3] CoreWeave 五年期 CDS 於 2026-11-05 突破 1289 bps、債券殖利率於 2026-11-06 升破 16%，信貸端先於股權重定價，屬後期訊號（`valuation.ai_credit_schism`）
- [R1] NASDAQ-100 於 2026-11-06 距 52 週高點回撤 13.56%，距 R1 門檻 23418.52 僅需再跌約 13.23%；VIX 7 日內上升 63.84% 至 28.18（`valuation.ndx_drawdown`、`structural.vix_spx_comove`）
- [R2] Microsoft 於 2026-10-29 將 2026 年資本支出指引自約 175 下調至約 170，R2 已完成 1/2（`ai.hyperscaler_capex`）
- [整體] CME FedWatch 於 2026-11-06 定價 12 月升息 25 bps 機會 76.8%，CPI YoY 3.72%（2026-09 月資料），Fed 難以在 AI 回撤時降息托底（`monetary.fedwatch`、`monetary.cpi_yoy`）
- [R3] ING 於 2026-11-06 出售 12 筆資料中心貸款、規模約 500；hyperscaler 今年以來發債 296，10/29 起一週 AI 相關發債 67，AI 融資鏈槓桿快速上升（`structural.ai_infrastructure_debt`、`ai.hyperscaler_financing_mix`）
- [整體] Shiller CAPE 38.91、trailing P/E 25.14（2026-11-06），下跌時估值緩衝薄（`valuation.sp500_pe_cape`）

## 支持 no 的證據

- [整體] 基準率：任意 182 天窗口內 R1–R3 皆屬少見事件；廣義信用尚未擴散，HY OAS 3.48%、IG OAS 0.93%（2026-11-05）仍屬低位（`monetary.hy_oas`、`monetary.ig_oas`）
- [R2] 四家中目前僅 Microsoft 1 家下修，且其指引仍約 170 的高水位；hyperscaler 今年以來發債 296 顯示債市仍對其敞開（`ai.hyperscaler_capex`、`ai.hyperscaler_financing_mix`）
- [R1] S&P 500 於 2026-11-05 仍高於 200 日均線 0.42%，NASDAQ-100 於 2026-11-06 已自 26629.81 反彈至 26989.99（`valuation.sp500_trend`、`valuation.ndx_drawdown`）
- [整體] 情緒已洗至極端：CNN Fear & Greed 22（極度恐懼，2026-11-06）、AAII 看空 48.4%（2026-11-04）、Cboe 股票賣買權比 1.05（2026-11-05），逆向指標顯示部分去槓桿已完成（`retail.fear_greed`、`retail.aaii`、`speculation.equity_put_call`）
- [整體] 美債市場未見失序：10Y 殖利率較前次下行 25 bps 至 4.84%（2026-11-05），MOVE 降至 92.77（2026-11-06，較前次 -8.33）（`monetary.dgs10`、`structural.treasury_basis_trade`）
- [R3] Anthropic 於 2026-10-26 遞交 S-1、目標估值 1.5 兆至 2 兆，AI 生態系股權融資管道仍暢通（`speculation.upcoming_ai_ipos`）

## 與前期比較

前次結論：無前次預測（report-2026-10-18 為舊格式評分報告）

前次為舊格式評分報告，不轉換為 yes/no；flip_evidence 為空。自 2026-10-18 以來的主要變化：

- NASDAQ-100 自 2026-10-06 高點 31224.69 回落至 26989.99，回撤 13.56%（`valuation.ndx_drawdown`）
- CoreWeave CDS 突破 1289 bps、債券殖利率升破 16%（`valuation.ai_credit_schism`）
- Microsoft 2026-10-29 下修 capex 指引（`ai.hyperscaler_capex`）
- 10Y 殖利率 -25 bps、HY OAS +17 bps，ΔDGS10 −25 bps、ΔDFII10 −14 bps、ΔT10YIE −12 bps，判讀：不可判（視窗不一致）（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `monetary.repo_stress_srf`：SOFR（3.92%，2026-11-05，FRED series_id=SOFR）與 IORB（3.9%，FRED series_id=IORB）取得，SOFR−IORB 為 2.0 bps（repo_stress status: partial，as_of 2026-11-05）；SOFR99 與 RPONTTLD 腳本 fetch_failed 且無 fallback 值，因此缺 99th 分位尾部利差與 SRF 動用讀數。核心利差僅 2 bps，顯示 repo 資金壓力（SOFR−IORB）不大；缺漏腿若顯示 SRF 大量動用，會強化 yes，但不太可能翻轉結論。

其他未取得或無披露（不作為證據）：NAAIM、BofA/JPM 調查、美債標售需求、私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）、token growth、折舊年限變動（depreciation useful-life change）、全球槓桿商品核准均為無合格披露；資本週期階段（capital cycle stage）缺 quarterly_state 增速證據，本次不判定週期階段（其 event_scan 雖找到 Microsoft 取消 Nscale 英國資料中心交易的報導，但因整體狀態未成功而不引用為證據）。另外，搜尋結果描述 Treasury basis-trade 三個 script 區塊為 fetch_failed，但 macro artifact 顯示三塊均為 ok，本報告以 artifact 為準（MOVE 92.77），搜尋 fallback 值 93.88 僅作背景。

最大的不確定性：

1. CoreWeave 負債規模與到期日程未在本次證據中披露：若其負債未達 50 億美元門檻或近期無到期，R3 路徑會變弱、推向 no；若有大額到期並出現交換要約，則強力推向 yes。
2. Microsoft 指引資料的一致性：結果標題提及「190b capex」，與摘錄的約 175→約 170 不完全一致；若下修不成立，R2 進度歸零，推向 no。
3. 12 月 FOMC：若升息落地並伴隨鷹派指引，推升 R1；若市場壓力迫使 Fed 按兵不動，則降低 R1 速度，推向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest | 7353.73 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 0.42 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest | 26989.99 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 13.56 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026-Q2） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 4.0 | FRED API (series_id=DFEDTARU) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.75 | FRED API (series_id=DFEDTARL) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 3.48 | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.93 | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.84 | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.6 | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.23 | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 99.64 | FRED API (series_id=DCOILWTICO) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.17 | FRED API (series_id=T5YIFR) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest | 0.9089 | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.92 | FRED API (series_id=SOFR) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.9 | FRED API (series_id=IORB) | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,748,145（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,945,410（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,261,882（¥626.19T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED API (series_id=VIXCLS) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 28.18 | FRED API (series_id=VIXCLS, SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 63.84 | FRED API (series_id=VIXCLS, SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2111.0042（$2.11T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7249305 | CFTC TFF futures-only | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo Finance chart API (^MOVE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2326.9 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebFetch | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED（EPS／PE 拆解未披露） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | fetch_macro.py sp500_trend | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | fetch_macro.py BOGZ1FL153064486Q | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | fetch_macro.py DFEDTARU＋DFEDTARL | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | fetch_macro.py BAMLH0A0HYM2 | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | fetch_macro.py BAMLC0A0CM | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | fetch_macro.py DGS10 | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | fetch_macro.py DFII10 | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | fetch_macro.py T10YIE（FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | fetch_macro.py DCOILWTICO | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | fetch_macro.py CPIAUCSL yoy_pct | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | fetch_macro.py T5YIFR | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | fetch_macro.py THREEFYTP10 | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py SOFR＋SOFR99＋IORB＋RPONTTLD | ⛔ FETCH FAILED（SOFR ok；IORB ok；SOFR99 fetch_failed；RPONTTLD fetch_failed，無 fallback 值） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | fetch_macro.py WALCL | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | fetch_macro.py ECBASSETSW＋JPNASSETS | ✓ API（ECBASSETSW ok；JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch：quarterly_state stock-of-state＋event_scan 30d | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch：quarterly_state stock-of-state＋event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（月頻） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | fetch_macro.py VIXCLS＋vix_spx_comove | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | fetch_macro.py LNFACBW027SBOG | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py cftc_lev_funds＋move_index＋ofr_repo（any） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻本益比約 28.3 | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein TSMC 目標價 554 → 600（EPS／PE 拆解未披露） | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/ | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 五年期 CDS 突破 1289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | RSP 年初至今報酬約 14.13% | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | 前十大成分股權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 1,474 對下跌 1,252 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 22（極度恐懼） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 1.48 兆美元、YoY 約 31.4% | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔 | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | 12 月升息 25 bps 定價 76.8% | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000 | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年 capex 指引約 175 → 約 170（下修） | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3 | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle RPO 638 | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87 | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 今年以來發債 296 | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 10/29 起一週內 5 筆 AI 相關債券發行合計 67 | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic 65 ＋ OpenAI 約 70，合計約 135（分母僅 Microsoft 可得，缺口不完整） | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] Microsoft 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics 完成 SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO 週漲 8% | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描：0 件符合 2+ 主題×弱基本面 | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描：0 件合格 | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe 股票選擇權賣買權比 1.05 | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭基金 10 月底規模 24.31、當月淨流入 7.27 | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 9 月總結算量 1,486,062,415（2026-09 月資料） | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性 20.93 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 交叉檢核基數約 1.48（2026-09 月資料） | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.ai_infrastructure_debt | ING 出售 12 筆資料中心貸款，規模約 500 | AI data center debt financing private credit November 2026 | https://www.cnbc.com/2026/11/06/ing-ai-data-center-loans-debt.html | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-11-08",
  "iso_week": "2026-W45",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "yes",
  "horizon_end": "2027-05-09",
  "prior_date": "2026-10-18",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 13.56,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

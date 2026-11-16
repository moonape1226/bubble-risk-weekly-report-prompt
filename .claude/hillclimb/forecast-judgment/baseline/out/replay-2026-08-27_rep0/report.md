> [DRY RUN] this report was not committed to archive.

# 2026-08-27 AI 泡沫破裂預測報告
報告日期：2026-08-27｜ISO 週次：2026-W35｜預測窗口：2026-08-27 → 2027-02-25｜前次基準：report-2026-08-24（3天前）

## 結論

**結論：no**

三條路徑都沒有已在進行中的觸發：NASDAQ-100 距 52 週高點回撤 4.68%，還要再跌約 21.31% 才到 R1 門檻；hyperscaler 2026 capex 仍以 top-4 合計約 $725bn（+77% YoY）擴張，看不到 R2 所需的兩家下修；HY OAS 2.70%、IG OAS 0.81% 與 repo 資金壓力（SOFR−IORB）1bp 都顯示信用與資金市場平穩，CoreWeave 仍能取得新融資，R3 違約事件缺乏近期傳導跡象。估值與槓桿雖極端，但它們只證明泡沫存在、下行幅度大，不足以推翻「182 天內三條件皆不成立」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,224.52（2026-08-26），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 4.68%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，自最新收盤須再下跌約 21.31% 才會觸及；`r1_met` 為 false。輔助讀數：S&P 500 7,675.7（2026-08-26），高於 200 日均線 7.97%、高於 52 週均線 9.40%，自前次基準（2026-08-24）以來 +0.3%（`valuation.sp500_trend`）；VIX 15.45、期限結構 contango（`structural.cross_asset_derivatives`），VIX 與 S&P 500 的 7 日同向讀數為否（VIX −2.46%、S&P 500 −0.19%，2026-08-18 → 2026-08-25，`structural.vix_spx_comove`）；MOVE 69.44，較 2026-08-24 的 73.98 回落（`structural.treasury_basis_trade`）。價格延伸（S&P 500 高於 200 日均線近 8%）提高均值回歸的幅度，但目前的波動與信用市場沒有呈現壓力。

**判讀：** R1 距離觸發還很遠：指數離高點不到 5%，波動率偏低。要在窗口內完成約 21% 的再下跌，需要明確的催化劑，例如 AI 信用事件（R3）外溢、hyperscaler capex 指引轉弱（R2），或國債市場失序（Treasury market dysfunction）引發的被迫去槓桿；本次證據中都還看不到這些催化劑。

### R2 資本支出收縮

本次取得的 hyperscaler capex 證據是彙總值：Microsoft、Alphabet、Amazon、Meta 四家 2026 年 capex 合計約 $725bn，年增約 77%（2026-08-13，Q2 財報季後彙整，`ai.hyperscaler_capex`）。四家各自的最新正式指引數字，以及各自相對前一次指引的方向（上修／持平／下修／未提供指引），本次證據沒有逐家載明，因此不能逐家判定方向；但本次檢索沒有發現任何一家下修 capex 指引的披露，目前已下修家數記為 0／4。需求面的旁證：OpenAI run-rate 約 $40B、Anthropic 約 $65B（2026-08-17，`ai.openai_anthropic_revenue`）；GPU 現貨租金高於合約價 2 倍以上，新增產能被利用率吸收（2026-08-13，`ai.compute_supply_demand`）。預測窗口（至 2027-02-25）涵蓋兩輪季報週期（日曆 Q3 與 Q4 財報，Q4 財報通常同時給出次年度指引），本次證據沒有載明具體財報日期。

**判讀：** R2 處於相反方向：capex 仍在擴張，算力需求訊號偏緊。要成立，四家之中須有兩家在窗口內兩輪財報下修指引。這通常需要 R1 式的股價重挫或 AI 營收急凍作為前導，本次沒有看到這樣的前導。

### R3 AI 信用事件

在可追蹤的 AI 基建借款人中，CoreWeave 是最可能接近 R3 規模門檻的名字。本次證據只顯示它於 2026-08-10 完成一筆以 HPC 基建擔保的 delayed-draw 定期貸款設施，規模 $2.6B（`structural.ai_infrastructure_debt`）；其總負債、債券殖利率、CDS 與評級動作本次證據未載，因此無法用本次資料驗證它是否達到 ≥ 50 億美元的門檻，也無法讀出它目前的信用定價。AI 發行人的利差或 CDS 重定價訊號（AI 信用定價分歧）在 14 日窗內沒有合格披露。本次也沒有發現付款違約、covenant waiver、distressed exchange 或 going-concern 語言。整體信用環境方面：HY OAS 2.70%（較 2026-08-24 +1bp，`monetary.hy_oas`）、IG OAS 0.81%（持平，`monetary.ig_oas`），repo 資金壓力（SOFR−IORB）1bp、SOFR99−IORB 9bp、SRF 動用 $0.003bn（`monetary.repo_stress_srf`），都沒有信用緊縮的跡象。

**判讀：** R3 目前沒有觸發中的事件：借款人仍能取得新的擔保融資，代表融資管道暢通，而非已經走到違約邊緣。不過槓桿持續累積，若窗口內出現大型 AI 基建借款人再融資失敗、利差急速走闊或主要客戶合約違約，可能在數月內完成 distressed exchange；本次證據中沒有這類前導。

## 支持 yes 的證據

- [整體] 估值處於歷史極端：S&P 500 Shiller CAPE 約 41.3、trailing P/E 約 26.2（2026-08-26，`valuation.sp500_pe_cape`），Mag 7 加權本益比約 29.5x（2026-08-26，`valuation.mag7_multiples`），代表一旦出現催化劑，下跌幅度可能很大。
- [R1] AI 營收對 capex 缺口（revenue-to-capex gap）很大：已披露的 AI 年化終端營收約 $105bn（OpenAI 40＋Anthropic 65），對比年化 capex 約 $725bn（分母：top-4，未含 Oracle 與 neocloud），2026-08-17（`ai.revenue_capex_gap`）；如果營收追不上，可能先打擊股價，再壓縮 capex。
- [R1] 槓桿與投機部位偏高：FINRA margin debt 2026-07 為 $1.42T，YoY +38.6%，接近歷史上頂部常見的 +40–50% 區間（`retail.margin_debt`）；美股槓桿 ETF 總 AUM 約 $198bn，創新高（2026-08-17，`structural.leveraged_etf_aum`）；SPX 0DTE 佔比在 8 月創紀錄的約 62.4%（2026-08-14，`structural.zero_dte`）。一旦開始下跌，這些部位可能放大跌勢。
- [R3] AI infrastructure debt financing / vendor-financing loops 持續擴大：CoreWeave 於 2026-08-10 再取得 $2.6B HPC 基建擔保 delayed-draw 定期貸款（`structural.ai_infrastructure_debt`），顯示 AI 算力擴張越來越依賴債務。
- [R1] 價格延伸：S&P 500 高於 200 日均線 7.97%、高於 52 週均線 9.40%（2026-08-26，`valuation.sp500_trend`），均值回歸的空間不小。
- [整體] 大型 AI 股權供給即將到來：Anthropic 據報目標 10 月 IPO、估值約 $2T（2026-08-17，`speculation.upcoming_ai_ipos`），這種規模的新股供給可能考驗市場的承接力。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.68%（2026-08-26），距 R1 門檻 22,995.45 還要再跌約 21.31%（`valuation.ndx_drawdown`）；VIX 15.45 且 7 日沒有與 S&P 500 同向上升（`structural.vix_spx_comove`），市場不在壓力狀態。
- [R2] hyperscaler 2026 capex top-4 合計約 $725bn、年增 +77%（2026-08-13，`ai.hyperscaler_capex`），本次檢索沒有任何下修披露；要在兩輪財報內出現兩家下修，需要大幅逆轉。
- [R3] 信用市場平靜：HY OAS 2.70%（`monetary.hy_oas`）、IG OAS 0.81%（`monetary.ig_oas`）處於低位；repo 資金壓力（SOFR−IORB）1bp、SRF 動用 $0.003bn（`monetary.repo_stress_srf`），沒有融資緊縮傳導。
- [R2] 需求端仍強：Anthropic run-rate 約 $65B、OpenAI 約 $40B（2026-08-17，`ai.openai_anthropic_revenue`）；GPU 現貨租金高於合約價 2 倍以上，產能被利用率吸收（2026-08-13，`ai.compute_supply_demand`），沒有產能過剩的跡象。
- [整體] 情緒沒有到狂熱：CNN Fear & Greed 55（Greed，2026-08-25，`retail.fear_greed`），AAII 偏多 35.5%、偏空 39.9%（2026-08-19，`retail.aaii`），Cboe equity put/call 0.52（2026-08-19，`speculation.equity_put_call`），整體偏中性，不是一般頂部常見的極度貪婪。
- [整體] 市場廣度擴散：RSP 年初至今領先 SPY 約 1.7pp（2026-08-23，`breadth.rsp_spy`），新高多於新低（`breadth.advance_decline`），漲勢不只集中在少數 AI 股。
- [整體] 美債基差交易槓桿（Treasury basis-trade leverage）有所降低：CFTC 槓桿基金美債期貨淨空 −7,218,048 口，4 週回補 244,468 口（2026-08-18）；MOVE 69.44（2026-08-26）；OFR tri-party repo transaction volume $2,368bn（`structural.treasury_basis_trade`），國債市場失序（Treasury market dysfunction）的放大管道目前偏靜。

## 與前期比較

前次結論：無前次預測（report-2026-08-24 為舊格式評分報告）

前次為舊格式評分報告，不轉換成 yes/no，flip_evidence 為空。自 2026-08-24 以來的主要變化如下：

- DGS10 −6bp 至 4.64%、DFII10 −6bp 至 2.32%；T10YIE 的變動視窗與前兩者不一致，判讀為不可判（視窗不一致）（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。
- HY OAS +1bp 至 2.70%，IG OAS 持平 0.81%（`monetary.hy_oas`、`monetary.ig_oas`）。
- MOVE 自 73.98 降至 69.44；S&P 500 +0.3%（`structural.treasury_basis_trade`、`valuation.sp500_trend`）。
- WTI 自 86.34 降至 83.9（−2.83%，`monetary.wti`）；WALCL、ECBASSETSW、JPNASSETS、LNFACBW027SBOG 沒有新觀測，視為持平。

以上變化都很小，不改變三條路徑的距離判斷。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

未揭露（✗ NOT DISCLOSED）的項目都是 best-effort 來源：analyst TP 拆解、AI 信用定價分歧、社群情緒、NAAIM、BofA／JPM 調查、美債標售需求、PBoC、私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）、AI token volume（本次只找到 Anthropic run-rate 營收年增約 7 倍，屬營收而非 token 指標，因此不計入）、backlog 重複計算風險（RPO double-counting）、折舊年限變動（depreciation useful-life change）、全球槓桿產品核准，以及兩個 composite 來源（hyperscaler 融資結構（capex vs FCF / 發債）與資本週期階段（capital cycle stage））。後兩者的 quarterly_state 仍有效（top-5 capex 已超過 FCF、2026 發債擴張；供給側 capex 年增約 77% 與需求側成長並存），但 30 日 event_scan 沒有新事件。其中可能影響結論的是 AI 信用定價分歧與私募信貸贖回壓力：如果其實存在未被抓到的 AI 發行人利差急速走闊或 BDC gate proration / breach，R3 的距離會被低估。不過 HY／IG OAS 與 repo 讀數都平穩，這個缺口推翻 no 的可能性低。

最大的不確定性：

- 日曆 Q3／Q4 hyperscaler 財報（窗口內兩輪）：如果有兩家下修次年度 capex 指引，R2 直接成立，並可能拖累 R1。這會把答案推向 yes。
- CoreWeave 等 AI 基建借款人的總負債與再融資時程本次未知：若窗口內有大額到期且利差急速走闊，R3 風險會上升，推向 yes。
- Anthropic 據報的 10 月 IPO 與 margin debt 接近 +40% YoY：若 IPO 定價失利引發 AI 股重估，加上槓桿部位被迫平倉，R1 的再下跌幅度可能被放大，推向 yes；反之若 IPO 順利，則強化 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7675.7 | FRED API (series_id=SP500) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線） | 7.97（%） | FRED API (series_id=SP500) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線） | 9.4（%） | FRED API (series_id=SP500) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較前次基準） | 0.3（%） | FRED API (series_id=SP500) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29224.52 | FRED API (series_id=NASDAQ100) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤） | 4.68（%） | FRED API (series_id=NASDAQ100) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1） | 45.76080873390133（%，約 45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-27T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75（%） | FRED API (series_id=DFEDTARU) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5（%） | FRED API (series_id=DFEDTARL) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.7（%） | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 1.0（bp） | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.81（%） | FRED API (series_id=BAMLC0A0CM) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.64（%） | FRED API (series_id=DGS10) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | -6.0（bp） | FRED API (series_id=DGS10) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.32（%） | FRED API (series_id=DFII10) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | -6.0（bp） | FRED API (series_id=DFII10) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.32（%） | FRED API (series_id=T10YIE) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | 0.0（bp） | FRED API (series_id=T10YIE) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 83.9（USD） | FRED API (series_id=DCOILWTICO) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.wti | DCOILWTICO chg_pct | -2.83（%） | FRED API (series_id=DCOILWTICO) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料） | 3.3（%） | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-27T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.33（%） | FRED API (series_id=T5YIFR) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR delta_bps | 1.0（bp） | FRED API (series_id=T5YIFR) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest | 0.8682（%） | FRED API (series_id=THREEFYTP10) | 2026-08-21 | 2026-08-27T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（序列自身 trailing 7 日） | 2.9（bp） | FRED API (series_id=THREEFYTP10) | 2026-08-21 | 2026-08-27T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.66（%） | FRED API (series_id=SOFR) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.74（%） | FRED API (series_id=SOFR99) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65（%） | FRED API (series_id=IORB) | 2026-08-27 | 2026-08-27T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用 transaction volume） | 0.003（$bn） | FRED API (series_id=RPONTTLD) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6745699.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-19 | 2026-08-27T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5913041.0（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-21 | 2026-08-27T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-27T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.45 | FRED API (series_id=VIXCLS) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of） | 15.45 | FRED API (series_id=VIXCLS, SP500 derived) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日，base 2026-08-18） | -2.46（%） | FRED API (series_id=VIXCLS, SP500 derived) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日，base 2026-08-18） | -0.19（%） | FRED API (series_id=VIXCLS, SP500 derived) | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2026.1422（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-12 | 2026-08-27T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位） | -7218048（口） | CFTC TFF futures-only | 2026-08-18 | 2026-08-27T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | 244468（口） | CFTC TFF futures-only | 2026-08-18 | 2026-08-27T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 69.44 | Yahoo Finance chart API (^MOVE) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index delta_abs（較 2026-08-24） | -4.54 | Yahoo Finance chart API (^MOVE) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2368.0（$bn） | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-08-26 | 2026-08-27T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值 / S&P 500 P/E and Shiller CAPE | multpl / GuruFocus [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值 / Mag 7 weighted P/E and AI leader P/S | 市場資料 WebSearch（Nasdaq） | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值 / Analyst TP upgrade decomposition | 賣方摘要 WebSearch（90d＋同季） | ✗ NOT DISCLOSED（無同季合格 TP 上修） |
| valuation.sp500_trend | 估值 / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500，sp500_trend block） | ✓ API |
| valuation.ndx_drawdown | 估值 / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100，ndx_drawdown block） | ✓ API |
| valuation.ai_credit_schism | 估值 / AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✗ NOT DISCLOSED（14 日窗無合格披露） |
| breadth.rsp_spy | 廣度 / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 市場資料 WebSearch（CNBC） | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度 / Top-10 concentration in S&P 500 | 市場資料 WebSearch（Yahoo Finance） | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度 / Advance/decline ratio, new high/low ratio | 市場資料 WebSearch（ts2.tech） | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶 / CNN Fear & Greed Index | CNN [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶 / Margin Debt: FINRA monthly data | FINRA / GuruFocus WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶 / Retail survey: AAII Investor Sentiment | AAII [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶 / Social sentiment proxies | WSB / X WebSearch（7d） | ✗ NOT DISCLOSED（無顯著討論） |
| retail.household_equity_allocation | 散戶 / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶 / NAAIM Exposure Index | naaim.org [primary: SEARCH] | ✗ NOT DISCLOSED（無當週值） |
| institutional.bofa_jpm_survey | 機構 / BofA Fund Manager Survey and JPM institutional survey | BofA / JPM WebSearch | ✗ NOT DISCLOSED（無新調查） |
| monetary.fed_funds | 貨幣 / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（FRED） | ✓ API（DFEDTARU ok／DFEDTARL ok） |
| monetary.hy_oas | 貨幣 / High Yield OAS | scripts/fetch_macro.py（FRED BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣 / Investment Grade OAS | scripts/fetch_macro.py（FRED BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣 / 10Y Treasury yield | scripts/fetch_macro.py（FRED DGS10） | ✓ API |
| monetary.dfii10 | 貨幣 / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED DFII10） | ✓ API |
| monetary.t10yie | 貨幣 / 10Y breakeven inflation rate | scripts/fetch_macro.py（FRED T10YIE，直接取得） | ✓ API |
| monetary.wti | 貨幣 / WTI crude oil price | scripts/fetch_macro.py（FRED DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣 / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（FRED CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣 / 5y5y forward inflation expectation | scripts/fetch_macro.py（FRED T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣 / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣 / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（repo_stress block） | ✓ API（SOFR ok／SOFR99 ok／IORB ok／RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣 / 美債標售需求（auction tail / bid-to-cover） | Reuters / TreasuryDirect WebSearch（14d） | ✗ NOT DISCLOSED（14 日窗無顯著標售結果） |
| monetary.fedwatch | 貨幣 / Fed funds rate path expectations | CME FedWatch [primary: SEARCH]（MacroMicro 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣 / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（FRED WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣 / Global central bank liquidity cross-check | scripts/fetch_macro.py（FRED ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok／JPNASSETS ok） |
| monetary.pboc | 貨幣 / PBoC aggregate financing / liquidity operations | PBoC / NBS WebSearch | ✗ NOT DISCLOSED（無當期英文摘要） |
| monetary.private_credit_liquidity | 貨幣 / Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]（30d） | ✗ NOT DISCLOSED（30 日窗無合格披露） |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | 財報摘要 WebSearch（stock-of-state，Q2 財報季） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI / AI token volume growth rate | 供應商披露 WebSearch | ✗ NOT DISCLOSED（只找到 run-rate 營收成長，無 token volume 指標） |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | CNBC WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 [primary: SEARCH] | ✗ NOT DISCLOSED（無合格披露） |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | 產業披露 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：FactSet 財報彙整；event_scan：30 日發債／私募信貸掃描 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口（revenue-to-capex gap） | 綜合披露 [primary: SEARCH]（分母 top-4） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K / 10-Q [primary: SEARCH]（30d） | ✗ NOT DISCLOSED（30 日窗無變動） |
| ai.capital_cycle | AI / 資本週期階段（capital cycle stage） | quarterly_state：供需增速披露；event_scan：30 日進出場事件掃描 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機 / Search for past 7 days: AI rename / SPAC | 新聞 WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機 / IPO market heat | stockanalysis WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機 / Microcap thematic moonshots | Finviz / Benzinga [primary: SEARCH]（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機 / Upcoming AI IPOs | Bloomberg / CNBC / Yahoo WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機 / Insider selling at AI / market-leadership companies | SEC EDGAR [primary: SEC EDGAR]（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機 / Cboe equity-only put/call ratio | Cboe [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構 / US leveraged ETF AUM | etf.com / ETFGI [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構 / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com WebSearch（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | 結構 / Global leveraged product approvals | KRX / TWSE / JPX / ESMA WebSearch（7d） | ✗ NOT DISCLOSED（7 日窗無英文披露） |
| structural.zero_dte | 結構 / 0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構 / Options total volume | OCC WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構 / Cross-asset derivatives / correlation checks | Cboe / SpotGamma WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構 / VIX / S&P 500 co-movement | scripts/fetch_macro.py（FRED VIXCLS＋vix_spx_comove block） | ✓ API（VIXCLS ok／vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構 / Cross-reference only: FINRA margin debt | FINRA / GuruFocus WebSearch（交叉檢核） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構 / AI infrastructure debt financing / vendor-financing loops | 信用市場 [primary: SEARCH]（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構 / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構 / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）＋WebSearch 補充 | ✓ API（cftc_lev_funds ok／move_index ok／ofr_repo ok；WebSearch 補充無合格事件） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 約 26.2、Shiller CAPE 約 41.3（原定來源 multpl / GuruFocus） | Shiller CAPE S&P 500 P/E August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio （GuruFocus） | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權本益比約 29.5x（S&P 500 約 25.6x） | Magnificent Seven weighted PE August 2026 | https://www.nasdaq.com/articles/the-magnificent-seven-market-performance-and-valuations （Nasdaq） | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| breadth.rsp_spy | RSP 年初至今領先 SPY 約 1.7pp；RSP AUM 破 $100B | RSP equal weight vs SPY 2026 | https://www.cnbc.com/2026/08/23/stocks-market-investing-sp500-spx.html （CNBC） | 2026-08-23 | 2026-08-27T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 top-10 集中度約 36.46% | S&P 500 top 10 concentration 2026 | https://finance.yahoo.com/markets/stocks/articles/rsp-vs-spy-does-equal-185007075.html （Yahoo Finance） | 2026-08-23 | 2026-08-27T09:30:00+08:00 |
| breadth.advance_decline | 廣度確認多頭、新高多於新低，等權領先約 1.7 個百分點 | market breadth advance decline August 2026 | https://ts2.tech/en/sp-500-equal-weight-leads-by-1-7-points-as-market-breadth-wobbles/ （ts2.tech） | 2026-08-23 | 2026-08-27T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 55（Greed） | CNN Fear and Greed August 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-07 月資料）1,417,225（$M，約 $1.42T），YoY +38.6%、MoM −5.7% | FINRA margin debt July 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt （GuruFocus／FINRA） | 2026-07-31 | 2026-08-27T09:30:00+08:00 |
| retail.aaii | AAII 偏多 35.5%、偏空 39.9%（週結 2026-08-19） | AAII investor sentiment August 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-08-19 | 2026-08-27T09:30:00+08:00 |
| monetary.fedwatch | FedWatch：2026-09-16 FOMC 按兵不動隱含機率約 68.4% | CME FedWatch September 2026 hold | https://en.macromicro.me/series/1645/probability-fed-rate-decrease （MacroMicro，原定來源 CME FedWatch） | 2026-08-20 | 2026-08-27T09:30:00+08:00 |
| ai.hyperscaler_capex | MSFT／GOOGL／AMZN／META 2026 capex 合計約 $725bn（+77% YoY），Q2 財報季彙整 | hyperscaler 2026 capex guidance | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-13 | 2026-08-27T09:30:00+08:00 |
| ai.openai_anthropic_revenue | OpenAI run-rate 約 $40B、Anthropic run-rate 約 $65B（7 月） | OpenAI Anthropic annualized revenue 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html （CNBC） | 2026-08-17 | 2026-08-27T09:30:00+08:00 |
| ai.compute_supply_demand | GPU 現貨租金高於合約價 2 倍以上，產能被利用率吸收 | AI GPU rental pricing utilization 2026 | https://www.uncoveralpha.com/p/amazon-google-microsoft-meta-q2-earnings （UncoverAlpha） | 2026-08-13 | 2026-08-27T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 超過 FCF，2026 發債擴張（背景；event_scan 30 日無新事件） | hyperscaler external financing capex FCF debt 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow （FactSet） | 2026-08-17 | 2026-08-27T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $105bn（OpenAI 40＋Anthropic 65）vs 年化 capex 約 $725bn（分母：top-4） | AI revenue to capex gap 2026 | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-17 | 2026-08-27T09:30:00+08:00 |
| ai.capital_cycle | [quarterly_state] 供給側 capex 年增約 77%，需求側 token／營收成長並存（背景；event_scan 30 日無新事件） | AI capex growth supply demand 2026 | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-13 | 2026-08-27T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收投機 IPO 7 日窗掃描：0 件合格事件 | AI rename SPAC ticker change August 2026 | Renaissance Capital／SEC EDGAR／新聞掃描（7 日窗無合格事件） | — | 2026-08-27T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD 美股 IPO 約 235 件，沒有單週無營收 AI IPO 暴衝 | US IPO count August 2026 | https://stockanalysis.com/ipos/2026/ （StockAnalysis） | 2026-08-26 | 2026-08-27T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot（單日 ≥100%、市值 <$1B、2 個以上主題、弱基本面）7 日窗掃描：0 檔 | microcap 100% single day quantum AI August 2026 | Finviz／Benzinga／StockTwits movers（7 日窗無合格 ticker） | — | 2026-08-27T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 10 月 IPO，估值約 $2T | Anthropic OpenAI IPO 2026 | https://finance.yahoo.com/markets/article/spacex-openai-and-anthropic-here-are-the-most-anticipated-ipos-in-2026-114439441.html （Yahoo Finance） | 2026-08-17 | 2026-08-27T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 14 日窗內合格 Form 4 集中賣出：0 起 | insider Form 4 AI executives August 2026 | SEC EDGAR／openinsider（14 日窗無合格 cluster） | — | 2026-08-27T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.52（來源未標明為日值或 5 日均值） | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/manuals/put-call-ratio （thetrading.tools） | 2026-08-19 | 2026-08-27T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美股槓桿 ETF 總 AUM 約 $198bn（創新高）；TQQQ 約 $37bn、SOXL 約 $22bn | leveraged ETF AUM record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing） | 2026-08-17 | 2026-08-27T09:30:00+08:00 |
| structural.us_single_stock_etf | 美股單一個股槓桿 ETF 30 日窗新核准／上市掃描：0 件 | single-stock leveraged ETF launch SEC August 2026 | SEC EDGAR／ETF.com new launches（30 日窗無合格核准） | — | 2026-08-27T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比在 8 月創紀錄，約 62.4% | 0DTE SPX volume share August 2026 | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august （Cboe） | 2026-08-14 | 2026-08-27T09:30:00+08:00 |
| structural.options_volume | OCC YTD 日均成交量超過 71M 口（2026-07 月資料） | OCC options volume 2026 | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/historical-volume-statistics （OCC） | 2026-07-31 | 2026-08-27T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 15.45、期限結構 contango、SKEW 偏高 | VIX term structure SKEW August 2026 | https://www.thetrading.tools/vix-term-structure （thetrading.tools） | 2026-08-25 | 2026-08-27T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 交叉檢核（2026-07 月資料）：YoY +38.6%；margin debt／市值比率本次未取得 | FINRA margin debt equity market cap ratio 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt （GuruFocus／FINRA） | 2026-07-31 | 2026-08-27T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave 以 HPC 基建擔保的 delayed-draw 定期貸款設施，規模 $2.6B | AI data center debt financing CoreWeave August 2026 | https://investors.coreweave.com/news/news-details/2026/CoreWeave-Closes-2-6-Billion-Loan-Facility-Expanding-Financing-Flexibility-for-AI-Infrastructure/default.aspx （CoreWeave IR） | 2026-08-10 | 2026-08-27T09:30:00+08:00 |

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
  "r1_drawdown_pct": 4.68,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

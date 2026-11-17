> [DRY RUN] this report was not committed to archive.

# 2026-11-08 AI 泡沫破裂預測報告
報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：report-2026-10-18（21天前）

## 結論

**結論：no**

三條路徑都已出現壓力，但沒有一條已接近完成：R1 的 NASDAQ-100 距 52 週高點回撤 13.56%，距 25% 門檻仍需再跌 13.23%；R3 的 CoreWeave 債券殖利率破 16%、5 年期 CDS 破 1289 bps，是目前最強的 yes 訊號，但本次沒有任何破產、付款違約或 distressed exchange 的披露，且其負債規模本次未取得來源佐證。R2 目前只有 Microsoft 一家下修（2026-10-29，在窗口開始前），而廣義信用利差（HY OAS 3.48%）仍屬偏緊，因此判斷 182 天內任一條件成立的可能性低於一半。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 26989.99（2026-11-06），252 個交易日最高收盤 31224.69（2026-10-06），距 52 週高點回撤 13.56%。R1 門檻水位為 23418.52，自最新收盤須再下跌 3571.47 點（約 13.23%）才會觸發（`valuation.ndx_drawdown`）。回撤是在一個月內形成的：S&P 500 自前次基準日 7659.44（2026-10-16）跌至 7353.73（2026-11-05，−3.99%），仍僅高於 200 日均線 0.42%（`valuation.sp500_trend`）；同一 7 日窗口 VIX 由 17.2 升至 28.18（+63.84%）而 S&P 500 −4.75%，屬一般的避險式反向變動而非 crowded-optionality 同漲（`structural.vix_spx_comove`）。Cboe SKEW 149.37、隱含相關性創高 20.93（`structural.cross_asset_derivatives`），equity put/call 1.05（`speculation.equity_put_call`），CNN Fear & Greed 22（極度恐懼，`retail.fear_greed`）。估值仍高：Shiller CAPE 38.91、trailing P/E 25.14（`valuation.sp500_pe_cape`），Mag 7 前瞻本益比約 28.3（`valuation.mag7_multiples`），前十大權重約 37.9%（`breadth.top10_concentration`），代表若下跌延續，下檔空間大。

**判讀：** R1 已走完約一半距離，是三條路徑中距離最可量化的一條；要在窗口內觸發，需要再一次與一個月前同等量級以上的下殺，可能推手是 R3 信用事件外溢、或 12 月升息定價落實（FedWatch 12 月升息 25 bps 機率 76.8%，`monetary.fedwatch`）壓縮估值。情緒已在極度恐懼區，反向而言短期進一步殺跌需要新催化劑。

### R2 資本支出收縮

- Microsoft：2026-10-29 財報後將 2026 年資本支出指引自約 175 下調至約 170（來源摘要未標單位），方向＝下修（`ai.hyperscaler_capex`）。
- Alphabet：本次檢索未取得其最新正式指引，方向不可判。
- Amazon：本次檢索未取得其最新正式指引，方向不可判。
- Meta：本次檢索未取得其最新正式指引，方向不可判。

目前四家中已確認下修者 1 家（Microsoft），且該下修發生在預測窗口開始（2026-11-08）之前；依解析條件，窗口內須有兩家下修。下一次財報日期本次未取得來源；182 天窗口（至 2027-05-09）跨越 2026Q4 與 2027Q1 兩個季末。反向證據：hyperscaler 今年以來發債約 $296bn，10/29 起一週內 5 筆 AI 相關債券發行合計約 $67bn（`ai.hyperscaler_financing_mix`），顯示建設仍以舉債延續，而非收縮。

**判讀：** R2 有一個起點（Microsoft 小幅下修），但其他三家狀態本次未建立；要在窗口內成立，需要至少兩家在接下來的季度財報中正式下修——最可能的路徑是 R1 回撤加深或融資成本上升迫使指引轉向。目前證據不足以判斷這已在發生。

### R3 AI 信用事件

AI 基礎設施借款人中，本次唯一有當期信用定價資料的是 CoreWeave：債券殖利率升破 16%（2026-11-06），5 年期 CDS 突破 1289 bps（2026-11-05），且是在 NASDAQ 反彈時仍走闊（`valuation.ai_credit_schism`）。這是明確的 AI 信用定價分歧（equity-vs-credit schism）後期訊號：信貸端先行重定價。CoreWeave 的總負債與近期到期牆本次未取得來源佐證，是否達 R3 的 50 億美元門檻在本報告中不予斷言（not established）。銀行端出現風險轉移：荷蘭國際集團出售 12 筆資料中心貸款，規模約 500（摘要未標單位，2026-11-06，`structural.ai_infrastructure_debt`）。本次未見任何破產申請、超過寬限期的付款違約、covenant waiver、distressed exchange 或 going-concern 語句的披露。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）30 日窗內無合格披露。廣義信用仍偏緊：HY OAS 3.48%（+17 bps vs 前次基準，`monetary.hy_oas`）、IG OAS 0.93%（`monetary.ig_oas`）。

**判讀：** R3 是三條路徑中市場定價最接近事件的一條——1289 bps 的 CDS 代表市場對違約風險的定價已屬高收益困境區間——但解析需要實際的破產、違約或 distressed exchange，本次無此類披露，且借款人規模門檻未被來源確認。推進因素是再融資失敗、客戶合約（如 Microsoft 收緊 neocloud 專案監督）轉弱或銀行加速出清貸款；這也是最可能觸發 R1 的傳導鏈。

## 支持 yes 的證據

- [R3] CoreWeave 債券殖利率升破 16%（2026-11-06），5 年期 CDS 突破 1289 bps（2026-11-05），且在 NASDAQ 反彈期間仍走闊，是 AI 信用定價分歧中信貸端先行重定價的後期訊號 `valuation.ai_credit_schism`。
- [R1] NASDAQ-100 自 2026-10-06 高點 31224.69 跌至 26989.99（2026-11-06），距 52 週高點回撤 13.56%，一個月內走完門檻的一半以上；同期 VIX 7 日升 63.84% 至 28.18 `valuation.ndx_drawdown` `structural.vix_spx_comove`。
- [整體] 貨幣政策緩衝受限：FedWatch 12 月升息 25 bps 機率 76.8%（2026-11-06），CPI YoY 3.72%（2026-09 月資料），Fed funds 目標區間 3.75%–4.00%，Fed 無法如過往以降息緩衝 AI 主導的下跌 `monetary.fedwatch` `monetary.cpi_yoy` `monetary.fed_funds`。
- [R2] Microsoft 於 2026-10-29 將 2026 年資本支出指引自約 175 下調至約 170，是四家 hyperscaler 中第一個正式下修，顯示指引軌跡可能轉向 `ai.hyperscaler_capex`。
- [R3] hyperscaler 融資結構（capex vs FCF / 發債）轉向舉債：今年以來發債約 $296bn，10/29 起一週內 5 筆 AI 相關債券合計約 $67bn（2026-11-06）；同時銀行端出售 12 筆資料中心貸款（2026-11-06），信用風險正在擴散與轉手 `ai.hyperscaler_financing_mix` `structural.ai_infrastructure_debt`。
- [整體] 泡沫脆弱性仍高：Shiller CAPE 38.91、Mag 7 前瞻本益比約 28.3、前十大權重約 37.9%、margin debt 約 1.48 兆美元年增約 31.4%（2026-09 月資料），一旦觸發下檔空間大 `valuation.sp500_pe_cape` `valuation.mag7_multiples` `breadth.top10_concentration` `retail.margin_debt`。

## 支持 no 的證據

- [整體] 基礎率與剩餘距離：任意 182 天窗口內 R1–R3 皆不成立才是常態；R1 仍需自 26989.99 再跌約 13.23% 至 23418.52 才觸發，相當於再來一次比一個月前更大的下殺 `valuation.ndx_drawdown`。
- [R3] 廣義信用未失序：HY OAS 3.48%、IG OAS 0.93%（2026-11-05），僅較前次基準分別 +17 bps、+8 bps；CoreWeave 的壓力尚未擴散成全面信用重定價，且本次無任何 AI 借款人違約或 distressed exchange 披露 `monetary.hy_oas` `monetary.ig_oas`。
- [R2] 目前僅 Microsoft 一家下修，且發生於窗口開始前；R2 需窗口內兩家下修，而 hyperscaler 今年以來仍發債約 $296bn 支撐建設，顯示資本承諾未退 `ai.hyperscaler_capex` `ai.hyperscaler_financing_mix`。
- [整體] 情緒已大幅清洗、反向指標偏向反彈：CNN Fear & Greed 22（極度恐懼）、AAII 看空 48.4% 對看多 34.1%（2026-11-04）、equity put/call 1.05；同時半導體 3 倍多頭基金 10 月淨流入 7.27，逢低買盤仍在 `retail.fear_greed` `retail.aaii` `speculation.equity_put_call` `structural.leveraged_etf_aum`。
- [R2] AI 終端需求訊號仍在擴張：Anthropic 遞交 S-1、目標估值 1.5 兆至 2 兆（2026-10-26），上半年營收 16.3；H100 隨選租金中位數 3.87（2026-11-03）未見崩跌 `speculation.upcoming_ai_ipos` `ai.openai_anthropic_revenue` `ai.compute_supply_demand`。
- [整體] 美債市場未見失序：MOVE 92.77（2026-11-06，前次基準 101.1），10Y 殖利率降 25 bps 至 4.84%，10Y 期限溢價（term premium）0.9089%（2026-10-30，7 日 −2.7 bps），國債市場失序（Treasury market dysfunction）傳導至 AI 資產的通道暫未啟動 `structural.treasury_basis_trade` `monetary.dgs10` `monetary.term_premium`。

## 與前期比較

前次結論：無前次預測（report-2026-10-18 為舊格式評分報告）

本次結論：no（首次以 yes/no 預測格式產出，舊格式評分不轉譯為 yes/no；flip_evidence 為空）

- 自 2026-10-18 以來最大的變化是市場端：NASDAQ-100 自 2026-10-06 高點回落 13.56%，S&P 500 自 7659.44 跌至 7353.73，VIX 由 19.99 升至 28.18（`valuation.ndx_drawdown`、`valuation.sp500_trend`）。
- 信用端：HY OAS 由 3.31% 升至 3.48%，IG OAS 由 0.85% 升至 0.93%（`monetary.hy_oas`、`monetary.ig_oas`）；CoreWeave CDS 破 1289 bps 是新出現的 R3 壓力點（`valuation.ai_credit_schism`）。
- 利率端：10Y 由 5.09% 降至 4.84%，WTI 由 108.21 降至 99.64（`monetary.dgs10`、`monetary.wti`），但 12 月升息定價升至 76.8%（`monetary.fedwatch`）。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `monetary.repo_stress_srf`（⛔ FETCH FAILED）：四個必要序列中 SOFR99 與 RPONTTLD 腳本 fetch_failed，本次無 WebSearch fallback 結果。可用腿仍保留：`repo_stress` 為 partial，SOFR−IORB = 2.0 bps（SOFR 3.92%、IORB 3.9%，as_of 2026-11-05），未見 secured-funding 壓力；缺 SOFR99 尾部利差與 SRF 動用量。此缺口不太可能改變答案：MOVE、OFR repo 成交量與 SOFR−IORB 都顯示資金面平穩，而 R1–R3 的判斷不依賴 repo 尾部讀數。

其他缺漏與資料問題（不構成 FETCH FAILED）：

- R2 的 Alphabet、Amazon、Meta 最新指引本次未取得；若其中一家已在窗口前下修，或在下一次財報下修，R2 的距離會比本報告描述得更近——這是最可能把答案推向 yes 的資料缺口。
- Microsoft capex 數值來源摘要未標單位，且結果 URL 路徑寫作 Q3 FY2026／190b，與摘要的「2026 年 175 → 170」不一致；方向（下修）明確，但絕對水位以來源原文為準，AI 營收對 capex 缺口（分母僅 Microsoft）因此只作背景、不作判斷依據。
- `ai.capital_cycle` 為 ✗ NOT DISCLOSED（quarterly_state 無可引證增速，本次不判定週期階段）；其 event_scan 有一筆：Microsoft 10 月取消 Nscale 英國資料中心交易（規模約 3，2026-11-04），並收緊 neocloud 專案監督——方向偏 R3／R2 負面，但組合狀態不成立，不作主證據。
- 美債基差交易槓桿：evidence 檔案註記腳本三區塊 fetch_failed 並以 WebSearch 取得 MOVE 93.88（2026-11-04），但 macro artifact 顯示 `cftc_lev_funds`、`move_index`、`ofr_repo` 皆為 status ok（MOVE 92.77，2026-11-06）；依協議以 artifact 為準記 ✓ API，搜尋值不使用。
- 10Y Δ 分解：ΔDGS10 −25.0 bps、ΔDFII10 −14.0 bps、ΔT10YIE −12.0 bps；判讀 `不可判（視窗不一致）`（T10YIE 最新日 2026-11-06 與其他兩腿 2026-11-05 不同窗）。
- 私募信貸贖回壓力、美債標售需求、折舊年限變動（depreciation useful-life change）、token growth、NAAIM、BofA/JPM 調查、全球槓桿產品核准：皆為 ✗ NOT DISCLOSED（選擇性來源，搜尋完成但窗內無合格披露）。

最大的不確定性：

1. CoreWeave 的負債規模、到期牆與再融資進度——若來源確認其負債 ≥ 50 億美元且出現 distressed exchange 或付款違約，R3 會直接成立並可能連動 R1，推向 yes。
2. 12 月 FOMC 是否升息——升息落實會在估值高位壓縮倍數、加重高槓桿 AI 借款人成本，推向 yes；若通膨降溫（5y5y 已降至 2.17%）使升息延後，推向 no。
3. 下一輪 hyperscaler 財報的 capex 指引——第二家下修即讓 R2 成立在望（推向 yes）；維持或上修則 R2 幾乎排除（推向 no）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest | 7353.73 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 0.42（%） | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 1.84（%） | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend prior_spot | 7659.44 | FRED API (series_id=SP500) | 2026-10-16 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct | -3.99（%） | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 26989.99 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤） | 13.56（%） | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2 季資料） | 48.2301354474（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 4.0（%） | FRED API (series_id=DFEDTARU) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.75（%） | FRED API (series_id=DFEDTARL) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 3.48（%） | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 prior | 3.31（%） | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-16 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.93（%） | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM prior | 0.85（%） | FRED API (series_id=BAMLC0A0CM) | 2026-10-16 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.84（%） | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | -25.0（bps） | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 prior | 5.09（%） | FRED API (series_id=DGS10) | 2026-10-16 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.6（%） | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | -14.0（bps） | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.23（%） | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | -12.0（bps） | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 99.64（USD） | FRED API (series_id=DCOILWTICO) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO prior | 108.21（USD） | FRED API (series_id=DCOILWTICO) | 2026-10-16 | 2026-11-08T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72（%） | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.17（%） | FRED API (series_id=T5YIFR) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.9089（%） | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7d） | -2.7（bps） | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.92（%） | FRED API (series_id=SOFR) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.9（%） | FRED API (series_id=IORB) | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6748145.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5945410.0（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6261882.0（¥626.19T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED API (series_id=VIXCLS) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS prior | 19.99 | FRED API (series_id=VIXCLS) | 2026-10-16 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 28.18 | FRED API (VIXCLS / SP500 共同日序，script 區塊) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_base | 17.2 | FRED API (VIXCLS / SP500 共同日序，script 區塊) | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 63.84（%） | FRED API (VIXCLS / SP500 共同日序，script 區塊) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -4.75（%，comove=false） | FRED API (VIXCLS / SP500 共同日序，script 區塊) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2111.0042（$2.11T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7249305（口） | CFTC TFF futures-only | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -489473（口） | CFTC TFF futures-only | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo Finance chart API (^MOVE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index delta_abs（vs 2026-10-16） | -8.33 | Yahoo Finance chart API (^MOVE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2326.9（十億美元，transaction volume） | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation：S&P 500 P/E and Shiller CAPE | multpl.com WebFetch | ✓ DIRECT |
| valuation.mag7_multiples | Valuation：Mag 7 weighted P/E and AI leader P/S | WebSearch（P/S vs 10 年均值未取得） | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation：Analyst TP upgrade decomposition | WebSearch（90d＋同季；EPS／PE 分拆未披露） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | Valuation：S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend | ✓ API |
| valuation.ndx_drawdown | Valuation：NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown | ✓ API |
| valuation.ai_credit_schism | Valuation：AI 信用定價分歧（equity-vs-credit schism） | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth：S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth：Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth：Advance/decline ratio, new high/low ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment：CNN Fear & Greed Index | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment：Margin Debt: FINRA monthly data | WebSearch（stock-of-state，2026-09 月資料） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment：Retail survey: AAII Investor Sentiment | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment：Social sentiment proxies | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment：Household equity allocation | scripts/fetch_macro.py BOGZ1FL153064486Q | ✓ API |
| retail.naaim | Retail Sentiment：NAAIM Exposure Index | WebSearch primary | ✗ NOT DISCLOSED（無當期週值） |
| institutional.bofa_jpm_survey | Institutional Sentiment：BofA Fund Manager Survey and JPM | WebSearch | ✗ NOT DISCLOSED（窗內無新調查） |
| monetary.fed_funds | Monetary & Credit：Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit：High Yield OAS | scripts/fetch_macro.py BAMLH0A0HYM2 | ✓ API |
| monetary.ig_oas | Monetary & Credit：Investment Grade OAS | scripts/fetch_macro.py BAMLC0A0CM | ✓ API |
| monetary.dgs10 | Monetary & Credit：10Y Treasury yield | scripts/fetch_macro.py DGS10 | ✓ API |
| monetary.dfii10 | Monetary & Credit：10Y Treasury real yield / TIPS | scripts/fetch_macro.py DFII10 | ✓ API |
| monetary.t10yie | Monetary & Credit：10Y breakeven inflation rate | scripts/fetch_macro.py T10YIE（FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit：WTI crude oil price | scripts/fetch_macro.py DCOILWTICO | ✓ API |
| monetary.cpi_yoy | Monetary & Credit：CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py CPIAUCSL yoy_pct | ✓ API |
| monetary.t5yifr | Monetary & Credit：5y5y forward inflation expectation | scripts/fetch_macro.py T5YIFR | ✓ API |
| monetary.term_premium | Monetary & Credit：10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py THREEFYTP10 | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit：repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py；SOFR99／RPONTTLD 無 fallback 結果 | ⛔ FETCH FAILED（SOFR ok；IORB ok；SOFR99 fetch_failed；RPONTTLD fetch_failed） |
| monetary.treasury_auctions | Monetary & Credit：美債標售需求（auction tail / bid-to-cover） | WebSearch（14d） | ✗ NOT DISCLOSED（窗內無顯著標售結果） |
| monetary.fedwatch | Monetary & Credit：Fed funds rate path expectations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit：Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py WALCL | ✓ API |
| monetary.ecb_boj | Monetary & Credit：Global central bank liquidity cross-check | scripts/fetch_macro.py ECBASSETSW＋JPNASSETS | ✓ API（ECBASSETSW ok；JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary & Credit：PBoC aggregate financing / liquidity operations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit：Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED（30 日窗內無合格披露） |
| ai.hyperscaler_capex | AI Fundamentals：Hyperscaler capex guidance | WebSearch（stock-of-state；僅取得 Microsoft） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals：AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI Fundamentals：OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals：Hyperscaler AI customer concentration 與 backlog 重複計算風險 | WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals：AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals：Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch；quarterly_state stock-of-state＋event_scan 30d | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI Fundamentals：AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch（分子組件）；分母僅 Microsoft | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals：GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED（30 日窗內無變動） |
| ai.capital_cycle | AI Fundamentals：資本週期階段（capital cycle stage） | WebSearch；quarterly_state 無可引證增速，event_scan 30d 有事件 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculative Behavior：Search for past 7 days AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | Speculative Behavior：IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior：Microcap thematic moonshots | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior：Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior：Insider selling at AI / market-leadership companies | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior：Cboe equity-only put/call ratio | WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage：US leveraged ETF AUM | WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage：US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage：Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED（7 日窗內無英文披露） |
| structural.zero_dte | Structural Leverage：0DTE option volume | WebSearch（Cboe 月報） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage：Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage：Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage：VIX / S&P 500 co-movement | scripts/fetch_macro.py VIXCLS＋vix_spx_comove | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage：Cross-reference only: FINRA margin debt | WebSearch（confirmation only） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage：AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage：Bank loans to nondepository financial institutions | scripts/fetch_macro.py LNFACBW027SBOG | ✓ API |
| structural.treasury_basis_trade | Structural Leverage：美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds＋move_index＋ofr_repo | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻本益比約 28.3（原定 multpl／GuruFocus／FactSet） | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein TSM 目標價 554 → 600（EPS／PE 分拆未披露） | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/ | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5 年期 CDS 突破 1289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | RSP 年初至今報酬約 14.13%（SPY 對照值摘要未載） | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 1,474 對下跌 1,252 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 22（極度恐懼；原定 cnn.com） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 1.48 兆美元、年增約 31.4%（原定 FINRA） | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔（TSLA、AMD、MU 等） | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 12 月升息 25 bps 機率 76.8% | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000（摘要未標單位） | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年 capex 指引約 175 → 約 170（下修；其餘三家未取得） | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3 | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle RPO 638 | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87 | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 今年以來發債約 $296bn | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 10/29 起一週內 5 筆 AI 相關債券發行合計約 $67bn | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic 65＋OpenAI 約 70，合計約 135（分母僅 Microsoft） | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] Microsoft 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics 完成 SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO 週漲 8% | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描：0 件符合 2+ 主題×弱基本面 | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描：0 件合格 | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 升至 1.05（日讀數） | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭基金 10 月底規模 24.31、當月淨流入 7.27 | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 9 月總結算量 1,486,062,415 口（2026-09 月資料） | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性創高 20.93 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 交叉檢核基數（2026-09 月資料）約 1.48 兆美元 | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.ai_infrastructure_debt | 荷蘭國際集團出售 12 筆資料中心貸款，規模約 500（摘要未標單位） | AI data center debt financing private credit November 2026 | https://www.cnbc.com/2026/11/06/ing-ai-data-center-loans-debt.html | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-11-08",
  "iso_week": "2026-W45",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-05-09",
  "prior_date": "2026-10-18",
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 13.56,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

> [DRY RUN] this report was not committed to archive.

# 2026-07-27 AI 泡沫破裂預測報告
報告日期：2026-07-27｜ISO 週次：2026-W31｜預測窗口：2026-07-27 → 2027-01-25｜前次基準：report-2026-07-23（4天前）

## 結論

**結論：no**

三條路徑都沒有已經在進行、且可望在 182 天內完成的跡象：NASDAQ-100 距 52 週高點只回撤 8.26%，要再跌約 18.25% 才觸及 R1（`valuation.ndx_drawdown`）；四家 hyperscaler 中唯一有新指引的 Alphabet 在 2026-07-22 是上修 capex，沒有任何一家下修（`ai.hyperscaler_capex`）。BCRED 的 gate proration / breach 與 AI 單一發行人利差走闊都是真實的 R3 前兆，但 HY OAS 仍在 2.77%，且本次沒有找到任何 R3 規模借款人的違約或困境訊號，還不足以推翻基礎機率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 28,128.34（2026-07-24），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 8.26%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，從最新收盤還要再跌約 18.25% 才會觸及。同類指標：S&P 500 為 7,411.98，高於 200 日均線 5.8%、高於 52 週均線 7.4%（`valuation.sp500_trend`）；VIX 18.58，過去 7 天 S&P 500 −0.61%、VIX −1.01%，沒有出現股價與波動率同漲（`structural.vix_spx_comove`）。估值偏高：Shiller CAPE 40.46、trailing P/E 28.52（`valuation.sp500_pe_cape`）；槓桿偏高：FINRA margin debt $1.502T，年增 51.5%（`retail.margin_debt`）。但情緒反而偏謹慎：CNN Fear & Greed 39（`retail.fear_greed`），AAII 看空 42.3%（`retail.aaii`）。

**判讀：** 距離觸發還遠。要在窗口內觸發，需要一個從現在起 18% 以上的跌幅，例如 7/29 FOMC 意外升息（`monetary.fedwatch` 顯示升息機率約 38%），再加上 AI 信用重定價或 hyperscaler 下修 capex 引發的去槓桿（margin debt 年增 51.5% 會放大下跌）。目前波動率與信用利差都沒有顯示這個過程已經開始。

### R2 資本支出收縮

- Alphabet：2026-07-22 Q2 財報把 2026 capex 指引上修到約 $195–205B，方向為上修（`ai.hyperscaler_capex`）。
- Microsoft、Amazon、Meta：本次取得的來源只給出 hyperscaler 2026 capex 合計約 $725B+，沒有逐家列出最新指引與日期。三家的方向無法由本次來源確認，按本次資料記為未提供指引。
- 已確認下修家數：0／4。下一次財報日期本次來源沒有列出，無法確認；三家的下一次季報都會落在窗口內（窗口涵蓋兩個季報季）。

需求面的旁證：伺服器 DRAM 3Q26 合約價季增 13–18%，交期 30–40 週以上（`ai.compute_supply_demand`，2026-07-03），顯示算力需求仍偏緊，看不到砍單或去化庫存。

**判讀：** 距離觸發很遠。窗口內需要至少兩家在接下來的財報中下修，但唯一的新指引是上修，供應鏈價格與交期也指向需求持續。可能讓 R2 成立的路徑是：R1 式的大跌或信用市場關閉，迫使 capex 已超過 FCF 的公司（Alphabet Q2 FCF −$5.9B，`ai.hyperscaler_financing_mix`）收縮。

### R3 AI 信用事件

- 符合規模門檻的借款人：CoreWeave 有已披露的 GPU 擔保債務 $24.9B（`structural.ai_infrastructure_debt`，2026-07-12），主業為 AI 算力，符合負債 ≥ 50 億美元。同一來源還列出 Broadcom/Anthropic $35B 與 Oracle $38B＋密州 $16.3B 的融資；但 Oracle 與 Anthropic 的主業不是 AI 資料中心／算力，密州案的借款主體本次未確認，因此不列為 R3 主體。
- 信用定價：AI 單一發行人利差走闊，CDX IG 持平；hyperscaler 2026 發債約 $182B（`valuation.ai_credit_schism`，2026-07-16），屬於 AI 信用定價分歧（equity-vs-credit schism）中信用端先動的型態。整體 HY OAS 2.77%、IG OAS 0.79%，仍很緊（`monetary.hy_oas`、`monetary.ig_oas`）。
- 鄰近壓力：私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）出現實際事件：BCRED Q2 突破 quarterly redemption cap，贖回約 10% NAV，以 50% 比例撥付（gate proration / breach），並出現 net inflow→outflow flip，淨流出約 $1.2B（`monetary.private_credit_liquidity`，2026-07-23）。
- 困境訊號：本次來源沒有發現 CoreWeave 或其他 R3 規模借款人有付款違約、covenant waiver、distressed exchange 或 going-concern 字句。近期到期與再融資需求本次未確認。

**判讀：** 前兆存在但距離事件仍遠。R3 需要的是實際的破產、超過寬限期的違約或 distressed exchange，目前只看到利差走闊和私募信貸資金端開始流出。要在窗口內觸發，需要私募信貸贖回壓力擴散到多支基金、AI 信用利差大幅走闊，再加上某個 neocloud 再融資失敗；這些條件本次都還沒有出現。

## 支持 yes 的證據

- [R3] 私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）出現實際的 gate proration / breach：BCRED Q2 贖回約 10% NAV，突破 quarterly redemption cap，以 50% 比例撥付，淨流出約 $1.2B，即 net inflow→outflow flip（2026-07-23，`monetary.private_credit_liquidity`）。這是 AI infrastructure debt financing 的主要資金來源之一開始收縮。
- [R3] AI 信用定價分歧（equity-vs-credit schism）中信用端先動：AI 單一發行人利差走闊，CDX IG 持平，hyperscaler 2026 發債約 $182B（2026-07-16，`valuation.ai_credit_schism`）。
- [R3] AI infrastructure debt financing / vendor-financing loops 規模大：CoreWeave GPU 擔保債務 $24.9B，Oracle $38B＋密州 $16.3B，Broadcom/Anthropic $35B（2026-07-12，`structural.ai_infrastructure_debt`）。高度依賴 GPU 擔保品價值，一旦再融資出問題可直接觸發 R3。
- [整體] hyperscaler 融資結構（capex vs FCF / 發債）轉向舉債：Alphabet FY26 capex 上修至約 $205B，Q2 FCF 轉負 −$5.9B（2026-07-22）；AI 相關 IG 發債累計約 $218–250B，已在測試投資人胃納（2026-07-08）（`ai.hyperscaler_financing_mix`）。
- [R1] 估值與槓桿高，下跌時會被放大：Shiller CAPE 40.46、trailing P/E 28.52（2026-07-24，`valuation.sp500_pe_cape`）；margin debt $1.502T，年增 51.5%（2026-06 月資料，`retail.margin_debt`）；NAAIM 84.02（2026-07-22，`retail.naaim`）。
- [R1] 利率端可能成為觸發點：CME FedWatch 顯示 7/29 FOMC 升息機率約 38%、持平約 61%（2026-07-25，`monetary.fedwatch`）；CPI YoY 3.46%（2026-06，`monetary.cpi_yoy`）；20Y 美債標售需求（auction tail / bid-to-cover）出現 tail +0.5bp，dealer takedown 14.67%（2026-07-22，`monetary.treasury_auctions`）。
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 capex 約 $725B，對比 AI 終端營收僅在低百億美元級（分母為來源所稱 hyperscaler 合計，本次未逐家拆分；營收端沿用 2026-06-15 的資料，`ai.revenue_capex_gap`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 8.26%，最新收盤 28,128.34，距 R1 門檻 22,995.45 還差約 18.25%（2026-07-24，`valuation.ndx_drawdown`）；VIX 18.58，股價與波動率沒有同漲（`structural.vix_spx_comove`）；MOVE 76.82，較前次下降 3.26（`structural.treasury_basis_trade`）。
- [R2] 四家中沒有任何一家下修：Alphabet 2026-07-22 把 capex 上修到約 $195–205B（`ai.hyperscaler_capex`）；伺服器 DRAM 3Q26 合約價季增 13–18%，交期 30–40 週以上，需求仍偏緊（2026-07-03，`ai.compute_supply_demand`）。
- [R3] 整體信用市場平靜：HY OAS 2.77%、IG OAS 0.79%（2026-07-23，`monetary.hy_oas`、`monetary.ig_oas`）；本次沒有任何 R3 規模借款人的違約或困境訊號。
- [整體] 資金與美債市場運作正常：repo 資金壓力（SOFR−IORB）為 −1bp，SOFR99−IORB +7bp，SRF 動用（Standing Repo Facility usage）僅 $0.001bn（`monetary.repo_stress_srf`）；美債基差交易槓桿（Treasury basis-trade leverage）方面，槓桿基金淨部位 −7,462,516 口，4 週變動 −45,392 口，沒有平倉跡象（2026-07-21，`structural.treasury_basis_trade`）。
- [整體] 情緒偏謹慎，市場廣度擴散：CNN Fear & Greed 39（`retail.fear_greed`）；AAII 看空 42.3%、看多 29.6%（`retail.aaii`）；RSP 年初至今 +12.39%，領先 SPY 約 5pp（`breadth.rsp_spy`）。這與泡沫頂部常見的一致狂熱不同。
- [R1] AI 龍頭估值沒有極端擴張：Mag 7 對其餘 493 檔的溢價約 10%，NVDA NTM P/E 約 18.7（2026-07-08，`valuation.mag7_multiples`）；Morgan Stanley 把 NVDA 目標價定在 $288，約 22× EPS，由 EPS 推動，target PE 沒有擴張（2026-07-13，`valuation.analyst_tp_decomposition`）。
- [整體] AI 公司仍能取得資本：Anthropic IPO 程序估值 $965B，OpenAI 傳出目標 9 月（2026-07-15，`speculation.upcoming_ai_ipos`）。

## 與前期比較

前次結論：無前次預測（report-2026-07-23 為舊格式評分報告）

本次結論為 no。前次為舊格式評分報告，不轉換成 yes/no，因此 flip_evidence 為空。

- 宏觀數據相較 2026-07-23：DGS10、DFII10、HY OAS、IG OAS、SOFR、SOFR99、WALCL、WTI 都沒有新觀測（Δ = 0，持平）。T10YIE 下降 2bp，T5YIFR 上升 1bp。10Y Δ 分解：ΔDGS10 0bp、ΔDFII10 0bp、ΔT10YIE −2bp，判讀為 `不可判（視窗不一致）`；freshness 為 partial_stale，stale_series 為 DGS10、DFII10。
- 波動率回落：VIX 從 18.70 降至 18.58，MOVE 從 80.08 降至 76.82（`structural.treasury_basis_trade`）。
- 前次之後的新事件：BCRED 的 gate proration / breach（2026-07-23）與 Alphabet 上修 capex（2026-07-22）。前者讓 R3 前兆變強，後者讓 R2 更遠。兩者都沒有讓任何路徑變成已在進行中。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `structural.zero_dte`：只找到 2026-02 的 Cboe 0DTE 佔比紀錄，沒有當期快照。這是投機結構的確認指標，不影響三條路徑的判讀，不會改變答案。
- `structural.options_volume`：只確認 OCC 6 月月報已發布，沒有取得成交量數值。同屬確認指標，不會改變答案。

其他缺口：`ai.openai_anthropic_revenue` 最新的 run-rate（Anthropic 約 $47B／OpenAI 約 $25B）發布於 2026-06-15，屬於上一季，按規則記為 ✗ NOT DISCLOSED，只作背景。`ai.capital_cycle`、`ai.depreciation_life`、`ai.customer_concentration_rpo`、`ai.token_growth`、`institutional.bofa_jpm_survey`、`structural.global_leveraged_approvals` 都沒有當期披露。Microsoft／Amazon／Meta 的逐家 capex 指引本次未取得，這是 R2 判讀最大的缺口；但因為 Alphabet 上修，且合計規模仍在擴大，補齊這三家的資料不太可能改出兩家下修。

主要不確定性：

1. Microsoft、Amazon、Meta 的下一次財報（日期本次未確認）：若有兩家下修，R2 會直接成立，答案轉向 yes。
2. 7/29 FOMC：若意外升息，再加上 CPI 3.46%，會壓縮 Fed 緩衝 AI 主導下跌的空間，R1 機率上升，答案傾向 yes。
3. 私募信貸贖回壓力是否擴散：若 BCRED 之外有多支基金出現 gate proration / breach，並傳導到 CoreWeave 等 neocloud 的再融資，R3 與 R1 會一起升溫；若下一季贖回放緩，則支持 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7411.98 | FRED API (series_id=SP500)；sp500_trend | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 5.8 | FRED API (series_id=SP500)；sp500_trend | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 7.4 | FRED API (series_id=SP500)；sp500_trend | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28128.34 | FRED API (series_id=NASDAQ100)；ndx_drawdown | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100)；ndx_drawdown | 2026-06-02 | 2026-07-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 8.26 | FRED API (series_id=NASDAQ100)；ndx_drawdown | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100)；ndx_drawdown | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1 家庭股票配置 %） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-27T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-07-26 | 2026-07-27T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-07-26 | 2026-07-27T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.77 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.79 | FRED API (series_id=BAMLC0A0CM) | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.71 | FRED API (series_id=DGS10) | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.43 | FRED API (series_id=DFII10) | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.26 | FRED API (series_id=T10YIE) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps（vs 2026-07-23） | −2.0 | FRED API (series_id=T10YIE) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD） | 84.38 | FRED API (series_id=DCOILWTICO) | 2026-07-20 | 2026-07-27T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-27T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.28 | FRED API (series_id=T5YIFR) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 0.7787 | FRED API (series_id=THREEFYTP10) | 2026-07-17 | 2026-07-27T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.64 | FRED API (series_id=SOFR) | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.72 | FRED API (series_id=SOFR99) | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-07-27 | 2026-07-27T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.001 | FRED API (series_id=RPONTTLD) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,747,378（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,949,077（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-17 | 2026-07-27T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,395,509（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-27T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 18.58 | FRED API (series_id=VIXCLS) | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of；base_date 2026-07-17、window_days 7、comove=false） | 18.58 | FRED API 共同日序（SP500 與 VIX 對齊）；vix_spx_comove block | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | −1.01 | FRED API 共同日序（SP500 與 VIX 對齊）；vix_spx_comove block | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | −0.61 | FRED API 共同日序（SP500 與 VIX 對齊）；vix_spx_comove block | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2012.1032（$2.01T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-15 | 2026-07-27T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | −7,462,516 | CFTC TFF futures-only；cftc_lev_funds | 2026-07-21 | 2026-07-27T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | −45,392 | CFTC TFF futures-only；cftc_lev_funds | 2026-07-21 | 2026-07-27T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 76.82 | Yahoo Finance chart API (^MOVE)；move_index | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2304.9 | OFR STFM REPO-TRIV1_TV_TOT-P；ofr_repo | 2026-07-24 | 2026-07-27T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | CNBC / Morgan Stanley 摘要 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報摘要 [primary: SEARCH]，90d＋同季 | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導 [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst / portfolioslab WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | P&I / RBC WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth（Leuthold）WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH]，MacroMicro 鏡像 | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA / Advisor Perspectives WebSearch | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | r/wallstreetbets / cashtag WebSearch，7d | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim / YCharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED（無當期新調查） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（DFEDTARU ok、DFEDTARL ok） | ✓ API |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok；repo_stress status ok） | ✓ API |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | auction recap [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Bloomberg / fxstreet WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]，30d | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報摘要 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic / OpenAI / Google 披露 WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch / 報導 WebSearch | ✗ NOT DISCLOSED（最新為 2026-06-15，非當季） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話摘要 [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報＋發債 [primary: SEARCH]；quarterly_state stock-of-state、event_scan 30d | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 [primary: SEARCH]，carry-forward | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K / 10-Q [primary: SEARCH]，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速＋進出場事件 [primary: SEARCH]；quarterly_state stock-of-state、event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC / no-revenue IPO | WebSearch，7d | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | 投機｜IPO market heat | Renaissance Capital WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz / Benzinga / StockTwits / Yahoo movers [primary: SEARCH]，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 WebSearch，30d | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR / openinsider，14d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe / YCharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com / cryptobriefing [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | 發行商新聞稿 / ETF 上市 feed，30d | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX / TWSE / JPX / ESMA WebSearch，7d | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe WebSearch | ⛔ FETCH FAILED（只取得 2026-02 舊紀錄，無當期快照） |
| structural.options_volume | 結構｜Options total volume: OCC monthly | theocc.com WebSearch | ⛔ FETCH FAILED（未取得月報數值） |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe / Yahoo WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS ok、vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | Advisor Perspectives WebSearch（交叉引用） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]，30d | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok）；WebSearch 無額外披露 | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 28.52（原定來源 multpl） | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 40.46（原定來源 multpl） | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 對其餘 493 溢價約 10%、NVDA NTM 約 18.7 | Magnificent 7 valuation premium cheapest decade July 2026 | https://www.cnbc.com/2026/07/08/magnificent-seven-stocks-are-the-cheapest-in-a-decade-by-one-measure.html （CNBC） | 2026-07-08 | 2026-07-27T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標 $288（約 22× EPS；舊目標價與 EPS Δ 未披露；target PE 未擴張，EPS 主導） | Morgan Stanley NVDA target 288 July 2026 EPS | https://www.gurufocus.com/news/8955458/morgan-stanley-upgrades-nvidia-nvda-with-a-288-target-price （GuruFocus） | 2026-07-13 | 2026-07-27T09:30:00+08:00 |
| valuation.ai_credit_schism | AI 單一發行人利差走闊 vs CDX IG 平穩；hyperscaler 2026 發債約 $182B | AI issuer credit spread CDS widening vs CDX IG July 2026 | https://247wallst.com/investing/2026/07/16/the-ai-revolution-is-reshaping-credit-markets-here-is-what-it-really-says-about-risk/ （24/7 Wall St.） | 2026-07-16 | 2026-07-27T09:30:00+08:00 |
| breadth.rsp_spy | RSP 年初至今 +12.39%，領先 SPY 約 5pp | RSP vs SPY equal weight YTD 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St.） | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度約 37% | S&P 500 top 10 concentration percent 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/ （P&I） | 2026-07-15 | 2026-07-27T09:30:00+08:00 |
| breadth.advance_decline | NYSE A/D 線 12 月新高；新高家數轉薄 78 vs 175 | NYSE advance decline new highs July 2026 | https://research.leutholdgroup.com/categories/nyse-advancedecline.1440 （Leuthold） | 2026-07-21 | 2026-07-27T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 39（Fear）（原定來源 cnn.com） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/series/22748/cnn-fear-and-greed （MacroMicro） | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt $1.502T，年增 51.5%（2026-06 月資料） | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-07-27T09:30:00+08:00 |
| retail.aaii | AAII Bull 29.6%／Bear 42.3% | AAII investor sentiment survey July 23 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| retail.social_sentiment | WEN（Wendy's）r/wallstreetbets 軋空 +25% | WEN Wendys wallstreetbets short squeeze July 2026 | https://altindex.com/wallstreetbets （AltIndex） | 2026-07-25 | 2026-07-27T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 84.02 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number （YCharts） | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| monetary.treasury_auctions | 20Y 標售 high yield 5.163%、tail +0.5bp、dealer takedown 14.67%、評級 D+ | US Treasury 20Y auction July 22 2026 tail bid to cover | https://investinglive.com/news/us-treasury-auctions-off-13-billion-of-20-year-bonds-at-a-high-yield-of-5-163 （investingLive） | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29：持平約 61%、升息約 38% | CME FedWatch July 29 2026 hike hold probability | https://www.cnbc.com/2026/07/13/-a-july-rate-hike-from-the-fed-the-odds-are-rising.html （CNBC） | 2026-07-25 | 2026-07-27T09:30:00+08:00 |
| monetary.pboc | 人行 LPR 持穩、MLF 淨投放 ¥100B | PBoC MLF net injection LPR July 2026 | https://www.bloomberg.com/news/articles/2026-07-24/pboc-adds-most-liquidity-to-economy-in-five-months-to-aid-growth （Bloomberg） | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| monetary.private_credit_liquidity | BCRED Q2 突破 quarterly redemption cap，贖回約 10% NAV，50% 比例撥付，淨流出約 $1.2B | Blackstone BCRED Q2 2026 redemption 5% cap breach proration | https://www.benzinga.com/markets/private-markets/26/07/60649546/blackstone-says-bcred-redemptions-have-materially-slowed （Benzinga） | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| ai.hyperscaler_capex | Alphabet 2026 capex 上修至約 $195–205B（Q2 財報）；hyperscaler 合計約 $725B+ | Alphabet raises 2026 capex 205B Q2 hyperscaler | https://mlq.ai/news/alphabet-raises-2026-capex-guidance-to-195-205b-cloud-revenue-surges-82/ （MLQ.ai） | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 +13–18% QoQ，交期 30–40 週以上 | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html （TrendForce） | 2026-07-03 | 2026-07-27T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] Alphabet FY26 capex 上修至約 $205B，Q2 FCF −$5.9B（capex 已超過 FCF） | Alphabet capex 205B Q2 2026 FCF negative debt | https://mlq.ai/news/alphabet-raises-2026-capex-guidance-to-195-205b-cloud-revenue-surges-82/ （MLQ.ai） | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] AI 相關 IG 發債累計約 $218–250B（測試投資人胃納） | AI bond issuance 250B July 2026 hyperscaler | https://www.morningstar.com/bonds/bond-issuance-backing-ai-investment-tops-250b-testing-limits-voracious-investor-demand （Morningstar） | 2026-07-08 | 2026-07-27T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex 約 $725B vs AI 終端營收低百億美元級（分母：來源所稱 hyperscaler 合計；carry-forward） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-06-15 | 2026-07-27T09:30:00+08:00 |
| speculation.ai_rename_spac | 2 件合格 SPAC：BRTMU $325M（AI 標的）、SCATU $100M | SPAC IPO announcement July 21 2026 AI | https://www.boardroomalpha.com/research/spac-market-update-july-21-2026-cdaq （Boardroom Alpha） | 2026-07-21 | 2026-07-27T09:30:00+08:00 |
| speculation.ipo_heat | Renaissance IPO Index 年初至今 +16.7%，pipeline 建置中 | US IPO market 2026 Renaissance IPO index YTD | https://www.renaissancecapital.com/IPO-Center/Stats （Renaissance Capital） | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot 0 件 | microcap 100% single day quantum AI fusion moonshot July 2026 | 檢查來源：Finviz、Benzinga、StockTwits、Yahoo movers | 2026-07-27 | 2026-07-27T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 程序估值 $965B；OpenAI 傳目標 9 月 | Anthropic OpenAI IPO July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html （CNBC） | 2026-07-15 | 2026-07-27T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 cluster 0 件（無一手 EDGAR URL 的零星申報不列名） | insider Form 4 cluster AI leaders July 2026 openinsider | 檢查來源：SEC EDGAR、openinsider | 2026-07-27 | 2026-07-27T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.61（日讀數） | Cboe equity put call ratio July 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio （YCharts） | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 約 $198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing） | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| structural.us_single_stock_etf | Tradr 5 檔 2X 單股；Leverage Shares 6 檔 ±2X | single-stock leveraged ETF launch July 2026 Tradr Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-07 | 2026-07-27T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 150.19；VIX 18.58 contango | VIX term structure SKEW July 2026 | https://finance.yahoo.com/quote/%5ESKEW/history/ （Yahoo Finance） | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt $1.502T，年增 51.5%（交叉引用 retail.margin_debt，僅確認） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-07-27T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Broadcom/Anthropic $35B；Oracle $38B＋密州 $16.3B；CoreWeave GPU 擔保 $24.9B | AI data center debt financing July 2026 Broadcom Anthropic Oracle CoreWeave | https://www.techtimes.com/articles/320239/20260712/nvidia-circular-financing-249b-coreweave-debt-puts-pension-funds-risk.htm （Tech Times） | 2026-07-12 | 2026-07-27T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-07-27",
  "iso_week": "2026-W31",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-01-25",
  "prior_date": "2026-07-23",
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 8.26,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

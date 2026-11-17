> [DRY RUN] this report was not committed to archive.

# 2026-08-06 AI 泡沫破裂預測報告

報告日期：2026-08-06｜ISO 週次：2026-W32｜預測窗口：2026-08-06 → 2027-02-04｜前次基準：report-2026-08-03（3天前）

## 結論

**結論：no**

三條路徑目前都沒有走到「已啟動或很可能在窗口內完成」的程度。R1：NASDAQ-100 只比 52 週高點低 3.83%，要再跌約 22.02% 才觸發（`valuation.ndx_drawdown`）。R2：hyperscaler 2026 capex 指引仍在上修，合計約 $725B（`ai.hyperscaler_capex`）。R3 方面，CoreWeave 的信用確實在重定價，但目前只反映在利差和 covenant 要求上，沒有任何付款違約或 distressed exchange（`valuation.ai_credit_schism`）。估值與槓桿都在極端水位，泡沫本身存在，但這些證據不足以推翻「182 天內不破裂」的 base rate。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

- NASDAQ-100 最新收盤 29,487.79（2026-08-05）。252 個交易日內最高收盤為 30,660.6（2026-06-02），目前距 52 週高點回撤 3.83%（`valuation.ndx_drawdown`）。
- R1 門檻為 22,995.45（`r1_threshold_level`），從最新收盤再跌約 22.02% 才會觸及。`r1_met` = false。
- 前次報告記錄的 `r1_drawdown_pct` 為 7.78，對應 2026-07-31 的收盤 28,274.2。此後三個交易日指數反彈，回撤幅度縮小約一半。
- 價格延伸：S&P 500 為 7,723.55（2026-08-05），高於 200 日 MA 9.71%、高於 52 週 MA 11.32%，自前次以來上漲 1.62%（`valuation.sp500_trend`）。指數處於明顯延伸狀態，均值回歸的空間大，但這是脆弱度的證據，不是時點的證據。
- 波動／情緒：VIX 15.81（2026-08-05）。7/29→8/5 視窗內 VIX −23.48%、S&P 500 +5.57%，comove = false，沒有出現「指數漲、避險需求也同時被搶」的 crowded-optionality 讀數（`structural.vix_spx_comove`）。CNN Fear & Greed 約 58（Greed，2026-08-05，`retail.fear_greed`），AAII 空方 42.1%（2026-07-30，`retail.aaii`），情緒不在狂熱區。
- 可能的催化劑：Alphabet 7 月底財報後，capex 上修引發了賣壓（`ai.hyperscaler_capex`），代表市場對「capex 增加但回報未證實」已開始敏感；債市波動上升（`structural.cross_asset_derivatives`）；以及 FOMC 路徑分歧（`monetary.fedwatch`）。

**判讀：** R1 距門檻還很遠（再跌約 22.02%），而且回撤幅度比前次縮小。若要在窗口內觸發，大概需要信用事件（R3）或 capex 大幅反轉（R2）引發的系統性去槓桿。槓桿 ETF、margin debt 與 0DTE 部位會放大跌幅，但目前看不到啟動這一連串效應的觸發點。

### R2 資本支出收縮

- 根據 2026-07-28 的 CNBC 報導，hyperscaler 2026 capex 仍在上修，合計約 $725B。Alphabet 在 Q2 財報上修 capex 後股價遭到賣壓（`ai.hyperscaler_capex`）。
- 逐家方向（最近一次財報：2026 Q2，2026 年 7 月下旬公布）：Alphabet 上修。Microsoft、Amazon、Meta 的個別數值本次證據沒有逐家列出，只有「合計續上修」的敘述，因此個別方向判為「未下修（無下修證據）」，不寫成具體數字。
- 目前下修家數：0／4。窗口（至 2027-02-04）內會有兩輪季報（Q3 與 Q4），具體日期本次證據未載。
- 需求端：H200 租金約 $4.39/hr，HBM／DRAM 合約價持續上升，供給缺口延伸到 1H2027（2026-08-01，`ai.compute_supply_demand`）。目前沒有利用率下滑或訂單消化的證據。
- 營收端：Microsoft RPO 約 $678B，其中約 32% 綁定單一客戶 OpenAI（2026-07-30，`ai.customer_concentration_rpo`）。年化 AI 終端營收約 $72B，對比年化 capex 約 $725B（分母為 CNBC 報導的 hyperscaler 合計；分子為 Anthropic 加 OpenAI，沿用 2026-06-15 的披露，`ai.revenue_capex_gap`）。這個缺口很大，但同一來源的增速資料不足，無法判斷缺口是在擴大還是收斂。

**判讀：** R2 正朝相反方向移動，四家都沒有下修，指引還在上修。要在窗口內觸發，至少兩家必須在下一兩輪季報中反轉指引；目前算力供不應求的證據不支持這種情況在短期內發生。下修比較可能出現在 R1／R3 衝擊之後，作為二階反應。

### R3 AI 信用事件

- 主要候選借款人是 CoreWeave（AI 算力為主業）。5Y CDS 約 855bp，一筆 $2.6B 貸款利差擴大 125bp，貸款投資人要求加入 covenants（2026-08-03，`valuation.ai_credit_schism`）。2026-07-29，這筆與 Anthropic 掛鉤的 $2.6B 貸款調高了票息（`structural.ai_infrastructure_debt`）。CoreWeave 的總負債規模本次證據未載數值，R3 的規模門檻需以其財報確認。
- 其他：Oracle CDS 約 215bp（`valuation.ai_credit_schism`）；Nebius 2026-07-17 有一筆 $775M 擔保融資（`structural.ai_infrastructure_debt`）。
- 違約／困境訊號：本次證據中，沒有任何 AI 基礎設施借款人出現付款違約、covenant waiver、distressed exchange 或 going-concern 字樣。
- 整體信用環境仍然寬鬆：HY OAS 2.73%（2026-08-04，Δ −5bp，`monetary.hy_oas`），IG OAS 0.78%（Δ 0，`monetary.ig_oas`）。repo 資金壓力（SOFR−IORB）為 1bp，SOFR99−IORB 為 9bp（2026-08-04），SRF 動用 $0.001bn（2026-08-05）（`monetary.repo_stress_srf`）。

**判讀：** R3 是三條路徑中最接近的一條：AI 信用定價分歧（equity-vs-credit schism）已經從「與非 AI 無差」轉為 CoreWeave 單名利差走闊、貸方要求 covenants，這屬於後期訊號。不過，R3 需要的是實際的破產、超過寬限期的違約或 distressed exchange，而 855bp 的利差反映的是重定價，還不是困境交換的水位。若窗口內 CoreWeave 的再融資受阻、關鍵客戶合約出問題，或利差急升到困境區，此判斷就需要重新檢視。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 約 855bp，$2.6B 貸款利差擴大 125bp，投資人要求 covenants（2026-08-03）。7/29 該筆 Anthropic 掛鉤貸款被迫調高票息，顯示 AI 基礎設施債的信用端正在重定價（`valuation.ai_credit_schism`、`structural.ai_infrastructure_debt`）。
- [整體] 估值與槓桿處於極端水位：S&P 500 Shiller CAPE 42.19、trailing P/E 29.74（2026-08-05，`valuation.sp500_pe_cape`）；FINRA margin debt $1.502T，YoY +51.5%，已達歷史頂部區間的 +40–50%（2026-06 月資料，`retail.margin_debt`）；美國槓桿 ETF AUM 創新高，約 $198B（`structural.leveraged_etf_aum`）。一旦開始回撤，這些因素會放大跌幅。
- [R2] 營收對 capex 的落差與集中度：年化 AI 終端營收約 $72B，對比年化 capex 約 $725B（`ai.revenue_capex_gap`）；Microsoft RPO 約 $678B，其中約 32% 綁定 OpenAI（2026-07-30，`ai.customer_concentration_rpo`）。單一客戶的支付能力一旦出問題，會同時打擊多家供應商的 backlog。
- [R1] 市場對 capex 的容忍度在下降：Alphabet 上修 capex 後股價遭到賣壓（2026-07-28，`ai.hyperscaler_capex`）。S&P 500 高於 200 日 MA 9.71%（`valuation.sp500_trend`），Top-10 集中度約 41%（`breadth.top10_concentration`）。
- [整體] 財政／債市壓力升溫：5Y 標售連續 14 次 tail，bid-to-cover 為 2022-09 以來最差，7Y tail 0.8bp（2026-07-28，`monetary.treasury_auctions`）；10Y 期限溢價（term premium）0.8681%，trailing 7d 上升 3bp（2026-07-31，`monetary.term_premium`）；TLT 1M skew 創 GFC 以來新高（2026-08-03，`structural.cross_asset_derivatives`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 3.83%（2026-08-05），距 R1 門檻 22,995.45 還要再跌約 22.02%，且回撤幅度比前次的 7.78 縮小（`valuation.ndx_drawdown`）。
- [R2] 四家 hyperscaler 沒有一家下修，2026 capex 合計續上修到約 $725B（2026-07-28，`ai.hyperscaler_capex`）。算力需求仍然吃緊：H200 租金約 $4.39/hr，HBM／DRAM 合約價續升，缺口延伸到 1H2027（2026-08-01，`ai.compute_supply_demand`）。
- [R3] 廣義信用與資金市場沒有傳導跡象：HY OAS 2.73%（`monetary.hy_oas`），IG OAS 0.78%（`monetary.ig_oas`），SOFR−IORB 1bp，SRF 動用約為零（`monetary.repo_stress_srf`），MOVE 由 80.48 降到 73.58（`structural.treasury_basis_trade`）。單名重定價還沒有擴散成系統性的融資壓力。
- [整體] 情緒不在狂熱區：VIX 15.81，與 S&P 500 沒有同漲（comove false，`structural.vix_spx_comove`）；Fear & Greed 約 58（`retail.fear_greed`）；AAII 空方 42.1% 多於多方 31.0%（`retail.aaii`）。廣度在擴散：RSP YTD +14.26% 領先 SPY 的 +13.71%（`breadth.rsp_spy`）。這不是典型的頂部前窄幅領漲格局。
- [整體] 投機篩選偏冷：本週 +AI 改名／SPAC 合格事件 0 件（`speculation.ai_rename_spac`），microcap thematic moonshot 合格 0 件（`speculation.microcap_moonshots`），IPO 本週約 21 檔、沒有 blowout 首日（`speculation.ipo_heat`）。
- [整體] Base rate：任意 182 天窗口內，R1–R3 都不發生才是常態。本次 yes 方的證據集中在「泡沫存在、下行時會很深」，屬於脆弱度；能說明時點的證據只有 R3 單一借款人的利差走闊（`valuation.ai_credit_schism`），尚未見到違約或交換。

## 與前期比較

前次結論：yes（report-2026-08-03）
本次結論：翻轉
前次 forecast 沒有記錄 yes_basis（舊版欄位），沒有可逐項回應的決定性理由。重新檢視後，前次的 yes 依現有證據不符合 rule 1：沒有任何一條路徑已啟動或很可能在窗口內完成。
翻轉依據：
- `valuation.ndx_drawdown`：R1 回撤由前次記錄的 7.78 縮小到 3.83%（2026-08-05），離 25% 門檻更遠（還要再跌約 22.02%），R1 沒有在推進。
- `ai.hyperscaler_capex`：hyperscaler 2026 capex 合計續上修到約 $725B（2026-07-28），0／4 家下修，R2 朝反方向移動。
- `valuation.ai_credit_schism`、`structural.ai_infrastructure_debt`：CoreWeave 的壓力停留在利差走闊（CDS 約 855bp、貸款利差 +125bp）與票息上調，沒有破產、超過寬限期的違約或 distressed exchange，不符合 R3 的解析事件定義。
- `monetary.hy_oas`：HY OAS 2.73%（2026-08-04，Δ −5bp），廣義信用沒有傳導 AI 單名壓力，R3 擴散成 R1 的鏈條還沒有形成。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源為 ✗ NOT DISCLOSED（篩選已完成，但窗口內沒有合格披露），逐項評估是否可能改變答案：

- `retail.naaim`、`institutional.bofa_jpm_survey`：屬於部位與情緒的交叉確認，缺漏不影響答案。
- `monetary.private_credit_liquidity`：30 日內沒有 BDC 的 redemption-request ratio、gate proration / breach 或 net inflow→outflow flip 披露。若有，會強化 R3 的傳導判斷，是最可能改變答案的缺口之一，但目前沒有證據顯示有此類事件。
- `ai.token_growth`、`ai.openai_anthropic_revenue`：本季（Q3）沒有新披露。OpenAI／Anthropic run-rate 的最近資料為 2026-06-15，只作為 `ai.revenue_capex_gap` 的沿用組件，不當成新證據。
- `ai.hyperscaler_financing_mix`：quarterly_state 有取得（2026-07-24：top-5 capex 已超過 FCF，2026 發債約 $182B，表外 SPV 超過 $120B），但 30 日 event_scan 沒有新的融資事件，因此合併狀態為 NOT DISCLOSED，不在正文當作證據引用。表外結構規模大，是 R3 的背景風險。
- `ai.depreciation_life`、`ai.capital_cycle`：30 日內沒有折舊年限變動，資本週期的增速對比證據也不足，本次不判定週期階段。
- `structural.global_leveraged_approvals`：7 日內沒有英文披露，不影響答案。
- 其他資料限制：`speculation.insider_form4` 只有 SNOW 一筆可對應 EDGAR 的紀錄（Dageville 2026-07-29 售出 50,000 股，約 $14.0M）。證據只列出單一日期，所附的 EDGAR 連結是公司 Form 4 清單頁，不是單一 filing 頁。另一筆 TEM（Lefkofsky）沒有自己的 EDGAR URL，依規則不列為具名證據。`retail.margin_debt` 的 margin debt / 市值比率，本次證據沒有可用的分母，未計算。`valuation.analyst_tp_decomposition` 只有「EPS-driven」的定性拆解，沒有 EPS Δ 與 target PE Δ 的數值。

最大的不確定性：

1. **Q3 季報（窗口內）的 capex 指引**：若兩家以上轉為下修，R2 直接成立；目前方向是上修，這項不確定性偏向維持 no。
2. **CoreWeave 的再融資與 covenants 談判**：若利差進一步升到困境區、出現 waiver 或交換要約，R3 會快速升溫，並可能經由 AI 信用定價分歧傳導到 R1，是最可能把答案推向 yes 的節點。
3. **美債供給／期限溢價與 FOMC 路徑**：5Y 標售連續 tail、TLT skew 創高、9 月降息定價分歧（約 62%）。若國債市場失序（Treasury market dysfunction）迫使去槓桿，會從估值端推動 R1；目前 MOVE 回落、SOFR−IORB 平穩，這項偏中性。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7723.55 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日 MA） | 9.71（%） | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週 MA） | 11.32（%） | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（自前次） | 1.62（%） | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29487.79 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 3.83（%） | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1 季資料） | 45.7608（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75（%） | FRED API (series_id=DFEDTARU) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.50（%） | FRED API (series_id=DFEDTARL) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.73（%） | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | -5.0（bp） | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.78（%） | FRED API (series_id=BAMLC0A0CM) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.63（%） | FRED API (series_id=DGS10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | -7.0（bp） | FRED API (series_id=DGS10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.40（%） | FRED API (series_id=DFII10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | -3.0（bp） | FRED API (series_id=DFII10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.22（%） | FRED API (series_id=T10YIE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | -5.0（bp） | FRED API (series_id=T10YIE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（no_new_obs） | 81.96（USD） | FRED API (series_id=DCOILWTICO) | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46（%） | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-08-06T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.26（%） | FRED API (series_id=T5YIFR) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8681（%） | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7d） | 3.0（bp） | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.66（%） | FRED API (series_id=SOFR) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.74（%） | FRED API (series_id=SOFR99) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65（%） | FRED API (series_id=IORB) | 2026-08-06 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用） | 0.001（$bn） | FRED API (series_id=RPONTTLD) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR−IORB（repo_stress sofr_iorb_bps） | 1.0（bp） | FRED API (series_id=SOFR, IORB) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99−IORB（repo_stress sofr99_iorb_bps） | 9.0（bp） | FRED API (series_id=SOFR99, IORB) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.walcl | WALCL latest（no_new_obs） | 6,738,190（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（no_new_obs） | 5,941,248（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（no_new_obs） | 6,442,957（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.81 | FRED API (series_id=VIXCLS) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（comove false） | 15.81 | scripts/fetch_macro.py vix_spx_comove block（FRED） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7/29→8/5） | -23.48（%） | scripts/fetch_macro.py vix_spx_comove block（FRED） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7/29→8/5） | 5.57（%） | scripts/fetch_macro.py vix_spx_comove block（FRED） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（no_new_obs） | 2004.9941（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-22 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約合計） | -7,481,041（口） | CFTC TFF futures-only | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -52,919（口） | CFTC TFF futures-only | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.58 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index prior | 80.48 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party transaction volume） | 2342.8（$2.34T） | OFR STFM REPO-TRIV1_TV_TOT-P | 2026-08-05 | 2026-08-06T09:30:00+08:00 |

10Y 分解：ΔDGS10 −7bp、ΔDFII10 −3bp、ΔT10YIE −5bp；decomposition.driver = unknown（T10YIE 視窗至 2026-08-05，與 DGS10／DFII10 的 2026-08-04 不一致），判讀：不可判（視窗不一致）。

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation／S&P 500 P/E and Shiller CAPE | multpl.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation／Mag 7 weighted P/E and AI leader P/S | SSGA／advisorperspectives WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation／Analyst TP upgrade decomposition | 賣方 TP 報導 WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED（僅 EPS-driven 定性拆解） |
| valuation.sp500_trend | Valuation／S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API（sp500_trend ok） |
| valuation.ndx_drawdown | Valuation／NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API（ndx_drawdown ok） |
| valuation.ai_credit_schism | Valuation／AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth／S&P 500 equal-weight (RSP) vs cap-weight (SPY) | financecharts WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth／Top-10 concentration in S&P 500 | P&I WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth／Advance/decline ratio, new high/low ratio | StockCharts WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail／CNN Fear & Greed Index | cnn.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail／Margin Debt: FINRA monthly data | FINRA via Advisor Perspectives WebSearch | ✓ SEARCH-VERIFIED（2026-06 月資料） |
| retail.aaii | Retail／Retail survey: AAII Investor Sentiment | aaii.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail／Social sentiment proxies | WSB／cashtag WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail／Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API（2026Q1） |
| retail.naaim | Retail／NAAIM Exposure Index | naaim／YCharts WebSearch | ✗ NOT DISCLOSED（無當週值） |
| institutional.bofa_jpm_survey | Institutional／BofA Fund Manager Survey and JPM | 賣方調查 WebSearch | ✗ NOT DISCLOSED（無新調查） |
| monetary.fed_funds | Monetary／Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok、DFEDTARL ok） |
| monetary.hy_oas | Monetary／High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary／Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary／10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary／10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary／10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary／WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API（no_new_obs） |
| monetary.cpi_yoy | Monetary／CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（yoy_pct） | ✓ API（2026-06） |
| monetary.t5yifr | Monetary／5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary／10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary／repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） |
| monetary.treasury_auctions | Monetary／美債標售需求（auction tail / bid-to-cover） | auction recap WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary／Fed funds rate path expectations | CME FedWatch 摘要 WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary／Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py | ✓ API（no_new_obs） |
| monetary.ecb_boj | Monetary／Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok、JPNASSETS ok） |
| monetary.pboc | Monetary／PBoC aggregate financing / liquidity operations | investing.com WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary／Private-credit / non-bank fund liquidity stress | BDC 披露 WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無合格披露） |
| ai.hyperscaler_capex | AI／Hyperscaler capex guidance | 季報報導 WebSearch（stock-of-state，2026 Q2） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI／AI token volume growth rate | Anthropic／OpenAI／Google WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI／OpenAI / Anthropic annualized revenue | Epoch／報導 WebSearch | ✗ NOT DISCLOSED（最近披露 2026-06-15，非本季） |
| ai.customer_concentration_rpo | AI／Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話報導 WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI／AI compute supply/demand and overcapacity risk | jarvislabs／TrendForce WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI／Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：Sage Advisory WebSearch；event_scan：30d 發債／SPV 掃描，無事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI／AI 營收對 capex 缺口（revenue-to-capex gap） | 組合既有披露（沿用組件） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI／GPU / 伺服器折舊年限變動 | 10-K／10-Q WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無變動） |
| ai.capital_cycle | AI／資本週期階段（capital cycle stage） | 供需增速＋進出場事件 WebSearch；兩組件皆無合格披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative／Search for past 7 days: AI rename / SPAC | Reuters／Benzinga／BusinessWire 篩選 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative／IPO market heat | Renaissance Capital WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative／Microcap thematic moonshots | Finviz／StockAnalysis／StockTitan gainers 篩選 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative／Upcoming AI IPOs | 具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative／Insider selling at AI / market-leadership companies | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（SNOW 一筆） |
| speculation.equity_put_call | Speculative／Cboe equity-only put/call ratio | YCharts WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural／US leveraged ETF AUM | cryptobriefing／etf.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural／US single-stock leveraged ETF approvals | GlobeNewswire／ETF 發行 feed（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | Structural／Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED（7 日內無英文披露） |
| structural.zero_dte | Structural／0DTE option volume | Cboe Q2 2026 簡報 WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural／Options total volume: OCC | theocc.com WebSearch | ✓ SEARCH-VERIFIED（2026-06 月資料） |
| structural.cross_asset_derivatives | Structural／Cross-asset derivatives / correlation checks | Cboe insights WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural／VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok、vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural／Cross-reference only: FINRA margin debt | 交叉引用 retail.margin_debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural／AI infrastructure debt financing / vendor-financing loops | Bloomberg 等 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural／Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API（no_new_obs） |
| structural.treasury_basis_trade | Structural／美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds／move_index／ofr_repo；WebSearch 無 14 日內平倉事件 | ✓ API（cftc_lev_funds ok、move_index ok、ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.74 | S&P 500 trailing P/E August 5 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.19 | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 約 29x vs 指數約 25.6x，溢價壓縮 | Magnificent 7 valuation premium lowest decade 2026 | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026 （SSGA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA TP $285→$288，EPS-driven | Morgan Stanley NVDA target 288 July 2026 AI demand | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044 （Investing.com） | 2026-07-13 | 2026-08-06T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 約 855bp、$2.6B 貸款利差 +125bp、Oracle CDS 約 215bp | CoreWeave CDS spread blows out 125 covenants Oracle August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm （Tech Times） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD +14.26% vs SPY +13.71% | RSP vs SPY equal weight total return YTD August 2026 | https://www.financecharts.com/etfs/SPY/performance/total-return （FinanceCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度約 41% | S&P 500 top 10 concentration percent record 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/ （P&I） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| breadth.advance_decline | 約 64% 成分股在 50DMA 上、A/D 線創高、McClellan 轉負 | S&P 500 breadth percent above 50 day moving average August 2026 McClellan | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/ （StockCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 58（Greed） | CNN Fear and Greed Index August 5 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives／FINRA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| retail.aaii | AAII Bear 42.1%／Neutral 26.9%／Bull 31.0% | AAII investor sentiment survey July 30 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| retail.social_sentiment | WEN「Save Wendy's」WSB 軋空，空頭比例約 44% | Reddit WSB Wendy's WEN short squeeze August 2026 | https://finance.yahoo.com/markets/stocks/articles/reddit-wants-save-wendy-inside-161925726.html （Yahoo Finance） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.treasury_auctions | 5Y 連 14 次 tail、bid-to-cover 為 2022-09 以來最差；7Y tail 0.8bp | US Treasury 5 year 7 year auction tail bid to cover July 2026 | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026 （TFTC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| monetary.fedwatch | FOMC 7/29 鷹派按兵不動；CME FedWatch 9 月定價約 62%，分歧 | CME FedWatch September 2026 probability FOMC hold | https://growbeansprout.com/tools/fedwatch （CME FedWatch 摘要） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.pboc | 人行逆回購合計約 ¥2.1T、7/24 MLF 淨投放 ¥100B | PBoC reverse repo injection 2.1 trillion yuan late July 2026 | https://www.investing.com/news/economy-news/chinas-pboc-to-conduct-overnight-reverse-repos-inject-a-total-of-21-trillion-yuan-4810853 （Investing.com） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_capex | 2026 capex 合計約 $725B，續上修；Alphabet Q2 上修後股價承壓 | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO 約 $678B，約 32% 繫於單一客戶（OpenAI） | Microsoft RPO backlog 678 billion single customer OpenAI 2026 | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/ （Benzinga via TradingView） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| ai.compute_supply_demand | HBM／DRAM 合約價續升、H200 租金約 $4.39/hr、缺口延至 1H2027 | H200 GPU rental price HBM DRAM contract 2026 shortage 2027 | https://jarvislabs.ai/blog/h200-price （Jarvislabs） | 2026-08-01 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超過 FCF、2026 發債約 $182B、表外 SPV 超過 $120B | hyperscaler capex FCF debt issuance 182 billion off balance sheet SPV 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure （Sage Advisory） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $72B（Anthropic 約 $47B＋OpenAI 約 $25B，沿用 2026-06-15 組件）vs 年化 capex 約 $725B（分母：CNBC hyperscaler 合計） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI）；分母 https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-06-15 | 2026-08-06T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收 IPO 合格事件 0 件（7 日窗） | AI rename ticker SPAC no revenue IPO July 30 August 6 2026 | Reuters／Benzinga／BusinessWire SPAC 篩選 | — | 2026-08-06T09:30:00+08:00 |
| speculation.ipo_heat | 本週約 21 檔定價、沒有 blowout 首日、YTD 約 $251B／86 檔 | US IPO pricings week August 3 2026 Renaissance | https://www.renaissancecapital.com/IPO-Center/Pricings （Renaissance Capital） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot 合格 0 件（7 日窗） | microcap 100% single day quantum fusion space nuclear small cap August 2026 | Finviz／StockAnalysis／StockTitan gainers 篩選 | — | 2026-08-06T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標約 $1T IPO、Anthropic 續推 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground （Benzinga） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| speculation.insider_form4 | SNOW Dageville 售 50,000 股約 $14.0M（Form 4／交易日 2026-07-29；證據僅列單一日期） | Snowflake Dageville Tempus Lefkofsky Form 4 insider sale July 2026 SEC | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1640147&type=4 （SEC EDGAR） | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.55（日讀數） | Cboe equity put call ratio August 3 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio （YCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創新高，約 $198B | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing） | 2026-07-23 | 2026-08-06T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x 單股槓桿 ETF＋ELOL（TSLA＋SpaceX）（URL 路徑顯示 2026-07-07 新聞稿，亦在 30 日窗內） | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量約 65%（Cboe Q2 2026） | 0DTE SPX options share volume Cboe Q2 2026 65% | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641 （Investing.com） | 2026-05-31 | 2026-08-06T09:30:00+08:00 |
| structural.options_volume | OCC 總量（2026-06 月資料）16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 約 139.96、VIX 約 16.9 contango、TLT 1M skew 創 GFC 以來新高 | VIX SKEW term structure bond volatility August 3 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher （Cboe） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-06 月資料）$1.502T、YoY +51.5%（交叉確認，不重複計入） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B Anthropic 掛鉤貸款 7/29 調高票息；Nebius $775M 擔保融資 7/17 | CoreWeave 2.6 billion loan Anthropic yield boosted July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic （Bloomberg） | 2026-07-29 | 2026-08-06T09:30:00+08:00 |

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
  "flip_evidence": ["valuation.ndx_drawdown", "ai.hyperscaler_capex", "valuation.ai_credit_schism", "structural.ai_infrastructure_debt", "monetary.hy_oas"],
  "yes_basis": [],
  "r1_drawdown_pct": 3.83,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

> [DRY RUN] this report was not committed to archive.

# 2026-08-13 AI 泡沫破裂預測報告
報告日期：2026-08-13｜ISO 週次：2026-W33｜預測窗口：2026-08-13 → 2027-02-11｜前次基準：report-2026-08-10（3天前）

## 結論

**結論：no**

三條路徑目前都離觸發很遠：NASDAQ-100 距 52 週高點僅回撤 2.99%（R1 門檻需再跌約 22.69%），四大 hyperscaler 在 Q2 季報後合計 2026 capex 仍上修至約 $725B、無一家下修（R2）。R3 雖出現 CoreWeave 貸款利差被迫調高 100–125bp、Oracle CDS 升至 7 年高的信用重定價，但尚無任何付款違約或 distressed exchange，HY OAS 僅 2.72%，不足以在 182 天內推翻低基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,742.6（2026-08-12），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 2.99%；R1 門檻水位為 22,995.45，自最新收盤須再下跌約 22.69% 才會觸發（`valuation.ndx_drawdown`）。估值與部位面的脆弱度偏高：S&P 500 trailing P/E 29.85、Shiller CAPE 42.34（`valuation.sp500_pe_cape`，2026-08-12）；S&P 500 高於 200 日均線 9.67%、高於 52 週均線 11.23%（`valuation.sp500_trend`，2026-08-12）；FINRA margin debt $1.502T、YoY +51.5%（`retail.margin_debt`，2026-06 月資料），落在歷史上 1999／2007／2021 頂部附近的 YoY 區間。但即時壓力讀數平靜：VIX 15.28，2026-08-04 → 2026-08-11 這 7 日窗 VIX −7.39%、S&P 500 −0.11%，未出現 crowded-optionality 同向上漲（`structural.vix_spx_comove`）；CNN Fear & Greed 約 61（Greed，非極端；`retail.fear_greed`）；AAII Bear 38.0% 高於 Bull 37.0%（`retail.aaii`）。另一方面 CME FedWatch 顯示 9/16 會議約 45% 升息定價、無降息定價（`monetary.fedwatch`），CPI YoY 3.3%（2026-07；`monetary.cpi_yoy`），意味 Fed 緩衝 AI 主導回撤的空間有限。

**判讀：** R1 距離很遠（只回撤 2.99%，需再跌約 22.69%）。窗口內要觸發，需要一個外生催化劑——例如 9 月 FOMC 意外升息觸發的估值壓縮、R3 信用事件外溢，或 Q3／Q4 季報出現 capex 指引下修——在高 margin debt 與高 CAPE 的槓桿結構上引發強制去槓桿；目前尚無此類催化劑正在發生的證據。

### R2 資本支出收縮

彙總來源顯示，Microsoft、Alphabet、Amazon、Meta 在 2026 年 7 月下旬的 Q2 季報後，2026 年 capex 合計約 $725B，方向為「仍上修」（CNBC 2026-07-28；`ai.hyperscaler_capex`）。本次證據為四家合計數，未逐家列出各自的指引數值；但彙總來源描述的是整體上修，沒有任何一家相對前次正式指引下修——目前四家中已下修的家數為 0。融資面已顯示壓力：top-5 hyperscaler capex 已超越 FCF（Alphabet Q2 FCF 轉負），2026 年發債預估約 $182B（`ai.hyperscaler_financing_mix`，2026-07-24），Meta El Paso 資料中心另以 BlackRock 主導、超過 $12B 的表外債券融資（2026-07-20）。年化 AI 終端營收約 $72B，對比年化 capex 約 $725B（分母：top-4＋Oracle；`ai.revenue_capex_gap`，沿用 2026-06-15 組合值，非新證據）。需求端尚未鬆動：Blackwell 售罄、H200 租金中位約 $3.99/hr、HBM 合約價約 +40%（`ai.compute_supply_demand`，2026-08-01）。依季報週期，窗口內（至 2027-02-11）預期還有兩輪季報（約 10 月下旬的 Q3 與 2027 年 1 月下旬至 2 月初的 Q4），確切日期本次證據未列出。

**判讀：** R2 目前 0／4，方向仍是上修。要在窗口內觸發，需要兩家在 Q3 或 Q4 季報中下修——可能的推力是 FCF 轉負後的發債成本上升、AI 營收對 capex 缺口持續擴大，或 R1 回撤迫使管理層收手；但在算力仍供不應求的當下，兩家同時下修不是基準情境。

### R3 AI 信用事件

信用面是三條路徑中變化最明顯的一條：CoreWeave 的 $2.6B 貸款被迫將利差調高 100–125bp 並加上 covenant（2026-07-29；`structural.ai_infrastructure_debt`）；同一波報導指出 Oracle 5Y CDS 約 75bp、為 7 年高點，Fitch／Moody's 發出預警（2026-08-03；`valuation.ai_credit_schism`）。這屬於 AI 信用定價分歧（equity-vs-credit schism）中「信貸端開始重定價、股價未跟上」的後期型態。不過：（1）CoreWeave 是最可能接近 R3 規模門檻（負債 ≥ 50 億美元、AI 算力為主業）的借款人，但其總負債與近期到期牆本次證據未提供，無法逐一核對；Oracle 主業非 AI 資料中心，不符 R3 借款人定義。（2）本次證據中沒有任何付款違約、covenant waiver、distressed exchange 或 going-concern 字眼——CoreWeave 仍能以更高成本完成 $2.6B 融資，代表市場仍在放款。（3）廣義信用利差仍緊：HY OAS 2.72%（+2bp）、IG OAS 0.79%（+1bp，2026-08-11；`monetary.hy_oas`、`monetary.ig_oas`）。（4）融資管道沒有失序：repo 資金壓力（SOFR−IORB）為 −1bp、SOFR99−IORB 為 +8bp（2026-08-11），SRF 動用（Standing Repo Facility usage）為 0（2026-08-12；`monetary.repo_stress_srf`）。

**判讀：** R3 已從「無訊號」進入「定價開始反映風險」，但距離真正的違約或 distressed exchange 仍有好幾步。窗口內若觸發，路徑大致是：利差持續走闊 → 再融資失敗或 covenant 觸發 → 大型 neocloud 進入 distressed exchange；Meta El Paso 這類表外 SPV 結構若出現承租方問題也會直接牽動 R3。目前每一步都尚未發生。

## 支持 yes 的證據

- [R3] CoreWeave $2.6B 貸款被迫將利差調高 100–125bp 並加上 covenant（2026-07-29），Oracle 5Y CDS 約 75bp、為 7 年高，Fitch／Moody's 發出預警（2026-08-03）——信貸端已先於股價重定價（`structural.ai_infrastructure_debt`、`valuation.ai_credit_schism`）。
- [R2] top-5 hyperscaler capex 已超越 FCF（Alphabet Q2 FCF 轉負），2026 年發債預估約 $182B，Meta El Paso 另有超過 $12B 的表外債券融資（`ai.hyperscaler_financing_mix`，2026-07-24／2026-07-20）；年化 AI 終端營收約 $72B 對比年化 capex 約 $725B（分母：top-4＋Oracle，2026-06-15 組合值；`ai.revenue_capex_gap`）——回本缺口大，融資成本上升時下修誘因增加。
- [R1] 估值與槓桿處於極端區：Shiller CAPE 42.34、trailing P/E 29.85（2026-08-12；`valuation.sp500_pe_cape`），FINRA margin debt $1.502T、YoY +51.5%（2026-06 月資料；`retail.margin_debt`），US 槓桿 ETF 總 AUM 創記錄高約 $198B（2026-07-23；`structural.leveraged_etf_aum`）——一旦有催化劑，下跌幅度會被放大。
- [R1] 貨幣政策沒有緩衝：CME FedWatch 顯示 9/16 會議約 45% 升息定價、無降息定價（2026-08-12；`monetary.fedwatch`），CPI YoY 3.3%（2026-07；`monetary.cpi_yoy`）。
- [R2] Microsoft 商用 RPO 約 $678B，其中約 32% 繫於單一客戶 OpenAI（2026-07-30；`ai.customer_concentration_rpo`）——單一 counterparty 的付款能力若出問題，backlog 會同時在多家供應商端縮水。
- [整體] 投機熱度高：IPO 市場 2026-08-12／08-13 每日約 12 檔定價、平均首日報酬約 18%（`speculation.ipo_heat`），2026-08-11 新發 6 檔單股 2x 槓桿 ETF（`structural.us_single_stock_etf`），OpenAI 目標 9 月上市、估值約 $730–850B（2026-07-28；`speculation.upcoming_ai_ipos`）。

## 支持 no 的證據

- [R1] NASDAQ-100 最新收盤 29,742.6（2026-08-12），距 52 週高點回撤 2.99%，要觸及 R1 門檻 22,995.45 還需再跌約 22.69%（`valuation.ndx_drawdown`）。
- [R2] 四大 hyperscaler 在 Q2 季報後 2026 年 capex 合計約 $725B、仍在上修，四家中下修家數為 0（2026-07-28；`ai.hyperscaler_capex`）；R2 需要窗口內兩家反轉。
- [R2] 算力需求仍緊：Blackwell 售罄、H200 租金中位約 $3.99/hr、HBM 合約價約 +40%（2026-08-01；`ai.compute_supply_demand`）——沒有產能過剩或訂單消化的跡象，削弱短期 capex 下修的理由。
- [R3] 廣義信用與融資市場平靜：HY OAS 2.72%、IG OAS 0.79%（2026-08-11；`monetary.hy_oas`、`monetary.ig_oas`）；SOFR−IORB −1bp、SRF 動用 0（`monetary.repo_stress_srf`）；MOVE 72.09（2026-08-12，−3.37）、CFTC 槓桿基金美債期貨淨空單 4 週減少 149,977 口（2026-08-04；`structural.treasury_basis_trade`）——沒有正在擴散的信用或美債基差交易槓桿（Treasury basis-trade leverage）壓力。
- [R3] CoreWeave 雖然付出更高利差，仍成功完成 $2.6B 融資（2026-07-29；`structural.ai_infrastructure_debt`）——市場仍在放款，與違約或 distressed exchange 相距甚遠。
- [整體] 情緒與波動未出現頂部型極端：VIX 15.28 且 7 日窗內與 S&P 500 未同向上漲（`structural.vix_spx_comove`），CNN Fear & Greed 約 61（`retail.fear_greed`），AAII Bear 38.0% 略高於 Bull 37.0%（`retail.aaii`），過去 14 日 AI／領導股無合格 Form 4 賣壓 cluster（`speculation.insider_form4`）。
- [整體] 基準率：任一 182 天窗口內 R1–R3 任一成立都屬少見事件；目前只有 R3 顯示早期定價訊號，而 R1（回撤 2.99%；`valuation.ndx_drawdown`）與 R2（capex 仍上修；`ai.hyperscaler_capex`）的當前讀數都指向相反方向。

## 與前期比較

前次結論：無前次預測（report-2026-08-10 為舊格式評分報告）

本次為新格式下的第一份 yes/no 預測；report-2026-08-10 的舊格式評分不轉譯為 yes/no，flip_evidence 為空。與 2026-08-10 相比的 macro 變動很小：DGS10 −2bp 至 4.70%、DFII10 持平於 2.43%、T10YIE −3bp 至 2.26%（ΔT10YIE 視窗與 DGS10／DFII10 不同，分解判讀：不可判（視窗不一致））；HY OAS +2bp 至 2.72%；MOVE 由 75.46 降至 72.09；S&P 500 較前次 −0.06%。WALCL（$6.75T）、ECB（€5.92T）、BOJ（¥644.30T）與銀行對 NBFI 放款（$2.00T）均無新觀測、持平（`monetary.walcl`、`monetary.ecb_boj`、`structural.nbfi_bank_loans`）。

## 資料缺漏與不確定性

**FETCH FAILED 來源：**

- `breadth.rsp_spy`（required）：搜尋只取得 2026-06-10 的 RSP vs SPY YTD 數據（+9.67% vs +8.38%），已落後約兩個月，不能當作本次的 current snapshot；沒有取得 current 值。不會改變答案——廣度只影響脆弱度判斷，不影響 R1–R3 的時點；Top-10 集中度約 37% 與 50DMA 廣度約 71.6% 仍提供了替代讀數。

**✗ NOT DISCLOSED（非證據，僅列示）：** `valuation.analyst_tp_decomposition`（唯一結果為 Susquehanna 2026-07-16 TSMC 目標價 $575→$600，不屬於 bullet 指定的 top-tier 券商，且只有「EPS-driven」敘述、缺 EPS Δ／目標 PE Δ，無法分解）、`retail.social_sentiment`、`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.pboc`、`monetary.private_credit_liquidity`、`ai.token_growth`、`ai.openai_anthropic_revenue`（唯一結果為 2026-05-29 的上一季資料，且頁面標題寫 $30B run-rate、摘錄卻是 $47B，前後不一致，不採為本季證據）、`ai.depreciation_life`、`ai.capital_cycle`（兩個組件皆無披露：增速證據不足，本次不判定資本週期階段）、`structural.global_leveraged_approvals`。其中最可能影響 R3 的是 `monetary.private_credit_liquidity`：過去 30 日沒有 BDC redemption-request ratio、gate proration / breach 或 net inflow→outflow flip 的披露——這是缺訊號，不是反證。

**最大的不確定性：**

1. **CoreWeave 的資產負債表與到期牆**：本次證據沒有它的總負債與近期到期資料，所以無法確認它是否達到 R3 規模門檻，也無法估計再融資壓力。若後續披露顯示大額到期集中在窗口內、利差再走闊，R3（以及經由 R3 外溢的 R1）的距離會明顯縮短，推向 yes。
2. **9/16 FOMC**：約 45% 的升息定價意味著意外升息不是尾端事件。升息會同時壓縮估值（R1）並推高 AI 發債成本（R2／R3），推向 yes；維持不動則推向 no。
3. **Q3 季報（約 10 月下旬）的 capex 指引**：只要兩家下修就直接觸發 R2。FCF 轉負與發債放大推向 yes；算力售罄與 HBM 漲價推向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7748.5 | FRED API (series_id=SP500), sp500_trend | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 9.67 | FRED API (series_id=SP500), sp500_trend | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 11.23 | FRED API (series_id=SP500), sp500_trend | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29742.6 | FRED API (series_id=NASDAQ100), ndx_drawdown | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100), ndx_drawdown | 2026-06-02 | 2026-08-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（回撤 %） | 2.99 | FRED API (series_id=NASDAQ100), ndx_drawdown | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100), ndx_drawdown | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1，家庭股票配置 %） | 45.76 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.72 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.79 | FRED API (series_id=BAMLC0A0CM) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.7 | FRED API (series_id=DGS10) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.43 | FRED API (series_id=DFII10) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.26 | FRED API (series_id=T10YIE) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl） | 84.77 | FRED API (series_id=DCOILWTICO) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料，YoY %） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.28 | FRED API (series_id=T5YIFR) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 0.8257 | FRED API (series_id=THREEFYTP10) | 2026-08-07 | 2026-08-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.64 | FRED API (series_id=SOFR) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.73 | FRED API (series_id=SOFR99) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-13 | 2026-08-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6748567.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-05 | 2026-08-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5923023.0（€5.92T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-07 | 2026-08-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.28 | FRED API (series_id=VIXCLS) | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（7 日窗終點） | 15.28 | FRED API 派生區塊 vix_spx_comove | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日窗 %） | -7.39 | FRED API 派生區塊 vix_spx_comove | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日窗 %） | -0.11 | FRED API 派生區塊 vix_spx_comove | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2002.4852（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-29 | 2026-08-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約淨部位，口） | -7423067 | CFTC TFF futures-only, cftc_lev_funds | 2026-08-04 | 2026-08-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 149977 | CFTC TFF futures-only, cftc_lev_funds | 2026-08-04 | 2026-08-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 72.09 | Yahoo Finance chart API (^MOVE), move_index | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party transaction volume） | 2385.3 | OFR STFM (REPO-TRIV1_TV_TOT-P), ofr_repo | 2026-08-12 | 2026-08-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | Fool research 彙總 [SEARCH] | ✓ SEARCH-VERIFIED（取得 Mag 7 P/E vs 指數；AI leader P/S vs 10 年均值未取得） |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報摘要 [primary: SEARCH]，90d＋同季 | ✗ NOT DISCLOSED（無 top-tier 券商可分解的同季上調） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧 | 信用市場報導 [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 財經媒體 [SEARCH] | ⛔ FETCH FAILED（僅取得 2026-06-10 舊值，無 current snapshot） |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | RBC Wealth Management [SEARCH] | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | Investing.com breadth [SEARCH] | ✓ SEARCH-VERIFIED（以 >50DMA 比例作廣度讀數；A/D 與 NH/NL 比未直接取得） |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA | FINRA 經 Advisor Perspectives [SEARCH]，stock-of-state | ✓ SEARCH-VERIFIED（2026-06 月資料沿用） |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com 經 Seeking Alpha [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag [SEARCH]，7d | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／YCharts [primary: SEARCH] | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 [SEARCH] | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（repo_stress block） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | Reuters／RTTNews recap [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | investing／Yicai [SEARCH] | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]，30d | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報彙總 [SEARCH]，stock-of-state | ✓ SEARCH-VERIFIED（Q2 2026 季報） |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 [SEARCH] | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | 具名報導 [SEARCH] | ✗ NOT DISCLOSED（僅有上一季 2026-05-29 資料） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話摘要 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | GPU 租金／HBM 報價 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：季報／發債彙總（stock-of-state）；event_scan：30d 融資事件 [primary: SEARCH] | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 [primary: SEARCH]，stock-of-state | ✓ SEARCH-VERIFIED（沿用 2026-06-15 組合值） |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K／10-Q [primary: SEARCH]，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | quarterly_state：供需增速；event_scan：30d 進出場事件 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: +AI rename / SPAC | Reuters／Benzinga／SEC 螢幕 [SEARCH]，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | IPOScoop [SEARCH]，7d | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／StockAnalysis gainers [primary: SEARCH]，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | S-1／具名報導 [SEARCH]，30d | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR／openinsider／secform4 [primary: SEC EDGAR]，14d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | thetrading.tools [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | 財經媒體／etf.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（總 AUM；個別 ticker 未分列） |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire 新發公告 [SEARCH]，30d | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA [SEARCH]，7d | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe Q2 2026 簡報 [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com 月報 [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe insights [SEARCH] | ✓ SEARCH-VERIFIED（SKEW／VIX／MOVE；VIX term structure 與股債相關未取得） |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用散戶 margin debt [SEARCH] | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | 融資公告 [primary: SEARCH]，30d | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）；WebSearch 無新增事件 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.85（原定來源 multpl／gurufocus） | S&P 500 trailing P/E CAPE August 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.34 | S&P 500 trailing P/E CAPE August 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E 約 29x vs 指數約 25.6x、佔市值約 33.9% | Magnificent 7 weighted PE vs S&P 500 August 2026 | https://www.fool.com/research/magnificent-seven-sp-500/ （Motley Fool） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 貸款利差 +100–125bp；Oracle 5Y CDS 約 75bp（7 年高）；Fitch／Moody's 預警 | CoreWeave Oracle CDS spread AI credit widening August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm （Tech Times） | 2026-08-03 | 2026-08-13T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度約 37% | S&P 500 top 10 concentration percent 2026 | https://www.rbcwealthmanagement.com/en-us/insights/the-great-narrowing-sp-500-concentration （RBC Wealth Management） | 2026-07-24 | 2026-08-13T09:30:00+08:00 |
| breadth.advance_decline | S&P 500 成分股高於 50DMA 比例約 71.6% | S&P 500 percent above 50 day moving average August 2026 | https://www.investing.com/indices/s-p-500-stocks-above-50-day-average （Investing.com） | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 61（Greed） | CNN Fear and Greed Index August 12 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives，原定來源 FINRA） | 2026-07-20 | 2026-08-13T09:30:00+08:00 |
| retail.aaii | AAII Bull 37.0%／Neutral 25.0%／Bear 38.0%（週結束 2026-08-05） | AAII investor sentiment survey week August 5 2026 | https://seekingalpha.com/article/4932187-aaii-sentiment-survey-optimism-jumps （Seeking Alpha，原定來源 aaii.com） | 2026-08-06 | 2026-08-13T09:30:00+08:00 |
| monetary.treasury_auctions | 3Y 2026-08-11 bid-to-cover 2.71、tail −0.5bp；10Y 2026-08-12 bid-to-cover 2.58、需求略高於均值 | US Treasury 3 year 10 year auction bid to cover August 2026 | https://www.rttnews.com/3679611/ten-year-note-auction-attracts-modestly-above-average-demand.aspx （RTTNews） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 9/16 會議升息約 45%、無降息定價 | CME FedWatch September 2026 rate hike probability | https://cryptobriefing.com/traders-45-percent-chance-september-fed-rate-hike/ （Crypto Briefing，原定來源 CME FedWatch） | 2026-08-12 | 2026-08-13T09:30:00+08:00 |
| ai.hyperscaler_capex | MSFT／GOOGL／AMZN／META 2026 capex 合計約 $725B（Q2 2026 季報後，仍上修） | hyperscaler capex 2026 725 billion raised Q2 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-08-13T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft 商用 RPO 約 $678B、約 32% 繫於 OpenAI | Microsoft RPO backlog 678 billion OpenAI 2026 | https://www.benzinga.com/trading-ideas/long-ideas/26/07/60816147/microsofts-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer （Benzinga） | 2026-07-30 | 2026-08-13T09:30:00+08:00 |
| ai.compute_supply_demand | H200 租金中位約 $3.99/hr、HBM 合約約 +40%、Blackwell 售罄 | H200 GPU rental HBM DRAM 2026 shortage Blackwell | https://jarvislabs.ai/blog/h200-price （Jarvislabs） | 2026-08-01 | 2026-08-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 超越 FCF（Alphabet Q2 FCF 轉負）、2026 發債約 $182B | hyperscaler capex FCF debt issuance 182 billion 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure （Sage Advisory） | 2026-07-24 | 2026-08-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan][spv_deal] Meta El Paso 資料中心 BlackRock 主導 >$12B 債券（triple-net lease 表外結構） sponsor_equity_split=undisclosed;residual_value_guarantee=undisclosed;lease_term=20-30yr;debt_tenor=undisclosed;lead_lenders=BlackRock/JPMorgan/MS; | hyperscaler capex vs free cash flow debt 2026 | https://www.landgate.com/news/blackrock-s-12-billion-bond-sale-signals-a-new-financing-playbook-for-data-center-developers （Landgate） | 2026-07-20 | 2026-08-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $72B vs 年化 capex 約 $725B（分母：top-4＋Oracle；沿用組合值） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-06-15 | 2026-08-13T09:30:00+08:00 |
| speculation.ai_rename_spac | 過去 7 日 +AI 改名／SPAC／無營收投機 IPO 合格事件 0 件 | AI rename ticker SPAC no revenue IPO August 6-13 2026 | 已檢查 Reuters、Benzinga、SEC EDGAR 螢幕 | — | 2026-08-13T09:30:00+08:00 |
| speculation.ipo_heat | 2026-08-12／08-13 每日約 12 檔定價、平均首日報酬約 18% | US IPO pricings week August 2026 IPOScoop | https://www.iposcoop.com/current-year-pricings/ （IPOScoop） | 2026-08-13 | 2026-08-13T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週 microcap thematic moonshot 合格 0 件 | microcap 100% single day quantum fusion nuclear AI August 2026 | 已檢查 Finviz、StockAnalysis gainers 螢幕 | — | 2026-08-13T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 9 月上市、估值約 $730–850B；Anthropic 持續推進 | OpenAI Anthropic IPO timing valuation 2026 | https://cryptobriefing.com/openai-ipo-filing-trillion-valuation/ （Crypto Briefing） | 2026-07-28 | 2026-08-13T09:30:00+08:00 |
| speculation.insider_form4 | 過去 14 日 AI／領導股合格 Form 4 賣壓 cluster 0 件 | AI leadership insider Form 4 sale July 30 August 13 2026 SEC | 已檢查 openinsider、secform4、SEC EDGAR | — | 2026-08-13T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity-only put/call 0.54（來源未標明 daily 或 5-day） | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio （thetrading.tools，原定來源 Cboe） | 2026-08-07 | 2026-08-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 記錄高約 $198B | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing，原定來源 etf.com） | 2026-07-23 | 2026-08-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 2026-08-11 新發 6 檔單股 2x 槓桿 ETF（Leverage Shares／Tradr） | single-stock leveraged ETF launch August 11 2026 Leverage Shares Tradr | https://www.globenewswire.com/news-release/2026/08/11/3342794/0/en/leverage-shares-by-themes-launches-three-new-2x-etfs-targeting-ai-infrastructure-and-connectivity-leaders.html （GlobeNewswire） | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量約 65%（Cboe Q2 2026） | 0DTE SPX options share Cboe Q2 2026 65% | https://ca.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4768656 （Investing.com） | 2026-07-31 | 2026-08-13T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月總量 1,603,491,559 口（約 16.0 億口） | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-08-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 135.59／VIX 15.28／MOVE 74.67 | VIX SKEW MOVE bond volatility August 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-10-2026-spx-skew-collapses-on-upside-chasing （Cboe） | 2026-08-11 | 2026-08-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt $1.502T、YoY +51.5%（僅交叉確認，不重複計入） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-08-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B 貸款，利差調高 +100–125bp＋covenant | CoreWeave 2.6 billion loan spread covenant August 2026 | https://www.stocktitan.net/news/CRWV/core-weave-closes-2-6-billion-loan-facility-expanding-financing-gwhngwnf0jt5.html （StockTitan） | 2026-07-29 | 2026-08-13T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-13",
  "iso_week": "2026-W33",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-11",
  "prior_date": "2026-08-10",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 2.99,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

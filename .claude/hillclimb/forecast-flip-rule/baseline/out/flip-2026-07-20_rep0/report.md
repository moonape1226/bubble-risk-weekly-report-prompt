> [DRY RUN] this report was not committed to archive.

# 2026-07-20 AI 泡沫破裂預測報告
報告日期：2026-07-20｜ISO 週次：2026-W30｜預測窗口：2026-07-20 → 2027-01-18｜前次基準：report-2026-07-16（4天前）

## 結論

**結論：yes**

維持前次判斷：R3 信用端已開始重定價（Oracle 5yr CDS ≈198bp 創紀錄、CoreWeave ≈665bp，2026-07-16），且 R1 回撤自前次 3.78% 擴大至 6.74%，私募信貸贖回壓力已出現實際 gate proration / breach；前次基準日後的新資料沒有任何一項削弱這條 R3→R1 傳導路徑，依翻轉紀律不翻轉。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 28,592.66（2026-07-17），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 6.74%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45；自最新收盤再下跌約 19.58% 才會觸及。前次基準日（2026-07-16）的回撤為 3.78%，四天內擴大約 2.96 個百分點。同期 S&P 500 收 7,457.69（2026-07-17），較前次 7,533.77 下跌 1.01%，仍高於 200 日均線 6.73%、高於 52 週均線 8.42%（`valuation.sp500_trend`）。VIX 升至 18.77（2026-07-17），較 7 日前的 15.03 上升 24.88%，同期 S&P 500 下跌 1.55%，屬於正常的反向走勢，並非 crowded-optionality 共振（`structural.vix_spx_comove`）。2026-07-17 NYSE 下跌家數約為上漲家數的 2 倍，晶片股賣壓擴大（`breadth.advance_decline`）。估值仍處高檔：Shiller CAPE 41.52、trailing P/E 32.08（2026-07-17，`valuation.sp500_pe_cape`）。

**判讀：** R1 距門檻仍約 19.58%，目前只是初期回撤。要在窗口內成立，需要信用或資金面的觸發事件（R3 違約、hyperscaler 下修 capex、或財政／通膨迫使利率上行）把高估值、高槓桿的部位推向強制去槓桿；margin debt YoY +53.7% 與 NAAIM 95.64 顯示一旦下跌，放大機制已經就位。

### R2 資本支出收縮

最新可得的官方指引來自 1Q26 財報季。彙總報導（2026-05-15）指出 Microsoft、Alphabet、Amazon、Meta 等 hyperscaler 2026 年 capex 合計約 $700B，且仍在上修（`ai.hyperscaler_capex`）。本次證據沒有逐家的指引數值，因此逐家方向只能依彙總報導判讀：Microsoft、Alphabet、Amazon、Meta 皆未見下修（彙總為上修）。四家中已下修家數：0。供給端需求訊號仍強：TrendForce 預估伺服器 DRAM 3Q26 合約價季增 13–18%（2026-07-03，`ai.compute_supply_demand`）。AI 營收對 capex 缺口（revenue-to-capex gap）仍大：年化 capex 約 $700B，AI 終端營收僅在低百億美元級（分母：top-4 hyperscaler 彙總；2026-05-15 組合值沿用，`ai.revenue_capex_gap`）。下一次四家財報（2Q26）將落在窗口內，但本次證據未取得具體日期。

**判讀：** R2 目前最遠，四家中沒有任何一家下修，需求端價格訊號仍偏強。要在窗口內成立，需要至少兩家在 2Q26 或 3Q26 財報中下修，通常要以 R1 大幅回撤或融資條件急遽收緊為前提；營收與 capex 的巨大缺口是中期壓力，但單靠它不足以在 182 天內迫使兩家下修。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）已轉向信貸端重定價：Oracle 5yr CDS 約 198bp、創紀錄，CoreWeave CDS 約 665bp（2026-07-16，`valuation.ai_credit_schism`）。以 AI 算力為主業的借款人中，CoreWeave 是最直接的 R3 候選；不過本次證據沒有載明其負債總額、近期到期或再融資時程，因此無法逐項確認它已達 R3 的 50 億美元門檻。Oracle 的主業不是 AI 資料中心，不屬於 R3 主體，但其 CDS 走闊是 AI 信用壓力的領先指標。非銀行端的私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）：Blue Owl OCIC 2Q26 的 redemption-request ratio 為 18.8%，遠高於 5% quarterly redemption cap，已實際發生 gate proration / breach（2026-07-02，`monetary.private_credit_liquidity`）。整體信用市場仍平靜：HY OAS 2.71%、IG OAS 0.78%（2026-07-16，`monetary.hy_oas`、`monetary.ig_oas`）。近 30 日 AI infrastructure debt financing / vendor-financing loops 掃描沒有新的合格披露，也沒有看到付款違約、covenant waiver、distressed exchange 或 going-concern 字樣。

**判讀：** R3 是最可能率先成立的路徑：單一 AI 算力借款人的 CDS 已到高收益困境區，但違約、破產或 distressed exchange 都還沒發生，且整體 HY 利差仍緊。要在窗口內成立，需要 CoreWeave 這類高槓桿 neocloud 遇上再融資受阻或客戶合約延後，私募信貸贖回壓力也同時限制其再融資管道；一旦發生，將經由信用傳導觸發 R1。

## 支持 yes 的證據

- [R3] AI 信用端已重定價：Oracle 5yr CDS 約 198bp 創紀錄、CoreWeave CDS 約 665bp（2026-07-16），而 HY OAS 僅 2.71%，AI 借款人與整體信用市場明顯脫鉤，屬於後期訊號（`valuation.ai_credit_schism`）。
- [R1] 回撤擴大且波動上升：NASDAQ-100 距 52 週高點回撤 6.74%（2026-07-17，前次 3.78%），VIX 18.77、7 日上升 24.88%，2026-07-17 下跌家數約為上漲家數的 2 倍，晶片股賣壓擴大（`valuation.ndx_drawdown`、`structural.vix_spx_comove`、`breadth.advance_decline`）。
- [R3] 私募信貸贖回壓力：Blue Owl OCIC 2Q26 redemption-request ratio 18.8%，高於 5% quarterly redemption cap，實際 gate proration / breach（2026-07-02），非銀行資金端已開始限制流動性（`monetary.private_credit_liquidity`）。
- [整體] 槓桿與部位擁擠：margin debt $1.416T、YoY +53.7%（2026-05 月資料，超過歷史頂部附近的 +40–50% 區間），NAAIM 95.64（2026-07-15），US 槓桿 ETF 總 AUM 約 $198B（2026-07-10），OCC 6 月選擇權成交 1,603,491,559 口、YoY +45%（`retail.margin_debt`、`retail.naaim`、`structural.leveraged_etf_aum`、`structural.options_volume`）。
- [整體] 估值與集中度極端：Shiller CAPE 41.52、trailing P/E 32.08（2026-07-17），S&P 500 Top-10 集中度 36.40%（2026-07-02），代表一旦破裂下檔空間很大（`valuation.sp500_pe_cape`、`breadth.top10_concentration`）。
- [R1] 政策緩衝有限：CPI YoY 3.46%（2026-06 月資料）、5y5y 2.21%，Fed 目標區間 3.50–3.75%，FedWatch 顯示 7/29 會議維持利率約 86.7%（2026-07-18），10Y 期限溢價（term premium）0.7788%（2026-07-10），Fed 難以搶先降息承接 AI 主導的下跌（`monetary.cpi_yoy`、`monetary.fed_funds`、`monetary.fedwatch`、`monetary.term_premium`）。
- [整體] 股權供給與投機催化：Anthropic 以約 $965B 估值舉行 IPO 投資人會議、可能 10 月掛牌（2026-07-15），2026 YTD 約 200 檔 IPO、募資 $141.2B（2026-07-16），EVTV 更名為 Azio AI（AZIO，2026-07-13）（`speculation.upcoming_ai_ipos`、`speculation.ipo_heat`、`speculation.ai_rename_spac`）。

## 支持 no 的證據

- [整體] 基準率與距離：182 天內 R1–R3 任一成立都不是常態；NASDAQ-100 最新收盤 28,592.66，距 R1 門檻 22,995.45 仍需再跌約 19.58%（`valuation.ndx_drawdown`）。
- [R2] capex 仍在上修：hyperscaler 2026 年 capex 合計約 $700B 且仍上修（2026-05-15），四家中 0 家下修；伺服器 DRAM 3Q26 合約價季增 13–18%（2026-07-03），顯示算力需求並未消化（`ai.hyperscaler_capex`、`ai.compute_supply_demand`）。
- [R3] 整體信用市場平靜：HY OAS 2.71%、IG OAS 0.78%（2026-07-16），銀行對 NBFI 放款 2004.0237 十億美元（約 $2.00T，2026-07-08）週變動 0%，沒有廣泛信用緊縮（`monetary.hy_oas`、`monetary.ig_oas`、`structural.nbfi_bank_loans`）。
- [整體] 資金管道無壓力：repo 資金壓力（SOFR−IORB）為 −3bp、SOFR99−IORB +5bp（2026-07-16），SRF 動用（Standing Repo Facility usage）0（2026-07-17），MOVE 70.88（2026-07-17），美債基差交易槓桿（Treasury basis-trade leverage）4 週變動僅 −78,139 口（2026-07-14）（`monetary.repo_stress_srf`、`structural.treasury_basis_trade`）。
- [整體] 散戶情緒未見狂熱：CNN Fear & Greed 37（Fear，2026-07-17），Cboe equity put/call 0.73（2026-07-17）不低，RSP YTD +10.68% 優於 SPY +7.47%（2026-06-10），漲勢有所擴散（`retail.fear_greed`、`speculation.equity_put_call`、`breadth.rsp_spy`）。

## 與前期比較

前次結論：yes（report-2026-07-16）

本次結論：維持

- NASDAQ-100 回撤由前次 3.78% 擴大到 6.74%（2026-07-17）。方向朝 R1，不支持翻轉為 no。
- VIX 由 16.73（2026-07-16）升至 18.77（2026-07-17），CNN Fear & Greed 落在 37（Fear，2026-07-17），2026-07-17 市場廣度轉弱。這些都是風險升溫的訊號，不削弱 yes。
- FedWatch（2026-07-18）顯示 7/29 會議大致維持利率，沒有出現新的政策緩衝。
- HY OAS、IG OAS、DGS10、DFII10、SOFR 在前次基準日後沒有新觀測（Δ = 0），信用與利率水位持平。
- AI 信用定價分歧（Oracle／CoreWeave CDS）的資料日為 2026-07-16，與前次基準日同日。前次基準日後沒有任何來源顯示信用端修復或 capex 轉弱的反證，因此缺乏翻轉依據，維持 yes。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下為 `✗ NOT DISCLOSED`（搜尋完成但無合格當期披露，皆為 best-effort 來源）：`valuation.analyst_tp_decomposition`、`retail.social_sentiment`、`institutional.bofa_jpm_survey`、`ai.token_growth`、`ai.openai_anthropic_revenue`（最新 run-rate 披露為 2026-05-15，不在執行日所屬的 3Q26，依規則不當作當季證據）、`ai.customer_concentration_rpo`、`ai.hyperscaler_financing_mix`（兩個 component 皆無披露）、`ai.depreciation_life`、`ai.capital_cycle`（兩個 component 皆無披露）、`structural.global_leveraged_approvals`、`structural.ai_infrastructure_debt`。其中 `structural.ai_infrastructure_debt` 與 `ai.hyperscaler_financing_mix` 的缺漏可能影響結論：R3 判讀缺少 CoreWeave 等借款人的負債規模與到期牆，如果補到的資料顯示近期有大額到期且再融資受阻，會強化 yes；若顯示融資順暢，則削弱 R3。其餘缺漏不太可能改變結論。

其他資料品質註記：
- `speculation.insider_form4` 記為 0 件，但 SEC EDGAR 一手連線受限，篩檢只能透過 openinsider 等二手來源；不影響結論。
- 快照偏舊：`valuation.mag7_multiples`（2026-05-15）、`structural.zero_dte`（2026-02-28）、`breadth.rsp_spy`（2026-06-10）都是最新可得的快照，僅作背景參考。
- 外部證據摘要中，`structural.treasury_basis_trade` 的搜尋結果列記三個 script component 為 fetch_failed，但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 皆為 status ok。本報告以 artifact 為準記為 ✓ API，此不一致應於正式執行時追查。
- 10Y 分解：DGS10／DFII10 在前次基準日後沒有新觀測（stale_series：DGS10、DFII10），ΔT10YIE +2bp 涵蓋不同視窗，driver 判讀：不可判（視窗不一致）。

最大的不確定性：
1. 2Q26 hyperscaler 財報（落在窗口內，日期未取得）：若有兩家下修 capex 即直接成立 R2，並可能連帶觸發 R1 → 推向 yes；若四家再度上修，則削弱 R2 並緩和 AI 信用端壓力 → 推向 no。
2. CoreWeave 等 neocloud 的再融資與到期結構（本次未取得）：若出現再融資失敗、covenant waiver 或 distressed exchange，R3 會直接成立 → 推向 yes；若順利展延，R3 時程延後 → 推向 no。
3. Anthropic IPO 時點（可能 10 月）與 7/29 FOMC：大型 IPO 帶來的股權供給，加上通膨 3.46% 使 Fed 不易降息 → 推向 yes；若 IPO 順利且市場吸收良好，代表風險偏好仍強 → 推向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7457.69 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 6.73 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.42 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend prior_spot（前次基準日收盤） | 7533.77 | FRED API (series_id=SP500) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較前次 %） | -1.01 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28592.66 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（回撤 %） | 6.74 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（家庭股票配置 %，2026Q1） | 45.76080873390133（≈45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 2.71 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（IG OAS %） | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（10Y 殖利率 %） | 4.57 | FRED API (series_id=DGS10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（10Y 實質殖利率 %） | 2.35 | FRED API (series_id=DFII10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（10Y breakeven %） | 2.24 | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（WTI 美元／桶） | 79.2 | FRED API (series_id=DCOILWTICO) | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（CPI YoY %，2026-06 月資料） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（5y5y forward %） | 2.21 | FRED API (series_id=T5YIFR) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（10Y 期限溢價（term premium）%，Kim-Wright） | 0.7788 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（序列自身 trailing 7 日變動） | 4.7 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（99th 分位 %） | 3.7 | FRED API (series_id=SOFR99) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（Fed 隔夜 repo 操作 transaction volume，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.walcl | WALCL latest（Fed 資產） | 6743028.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（ECB 資產） | 5970516.0（€5.97T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（BOJ 資產） | 6395509.0（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 18.77 | FRED API (series_id=VIXCLS) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of） | 18.77 | FRED-derived (vix_spx_comove) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日 %） | 24.88 | FRED-derived (vix_spx_comove) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日 %） | -1.55 | FRED-derived (vix_spx_comove) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_base（base_date） | 15.03 | FRED-derived (vix_spx_comove) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（銀行對 NBFI 放款） | 2004.0237（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（槓桿基金美債期貨淨部位，口） | -7562874 | CFTC TFF futures-only (cftc_lev_funds) | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（4 週變動，口） | -78139 | CFTC TFF futures-only (cftc_lev_funds) | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（MOVE） | 70.88 | Yahoo Finance chart API ^MOVE (move_index) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2342.6 | OFR STFM REPO-TRIV1_TV_TOT-P (ofr_repo) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH]，WebSearch | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | MarketXLS 儀表板，WebSearch | ✓ SEARCH-VERIFIED（最新可得快照 2026-05-15） |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報摘要 [primary: SEARCH]，90 日且同季 | ✗ NOT DISCLOSED（搜尋完成，無合格 TP 上調） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py → FRED API (series_id=SP500) sp500_trend | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py → FRED API (series_id=NASDAQ100) ndx_drawdown | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導 [primary: SEARCH]，14 日 | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst，WebSearch | ✓ SEARCH-VERIFIED（快照 2026-06-10） |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | ahasignals，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth 報導，WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH]，MacroMicro 鏡像 | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA | FINRA／Advisor Perspectives，WebSearch | ✓ SEARCH-VERIFIED（2026-05 月資料沿用） |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag，WebSearch | ✗ NOT DISCLOSED（7 日內無顯著討論） |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py → FRED API (series_id=BOGZ1FL153064486Q) | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | ycharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查，WebSearch | ✗ NOT DISCLOSED（無當期調查） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py → FRED API | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py → FRED API (series_id=BAMLH0A0HYM2) | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py → FRED API (series_id=BAMLC0A0CM) | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py → FRED API (series_id=DGS10) | ✓ API（no_new_obs） |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py → FRED API (series_id=DFII10) | ✓ API（no_new_obs） |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py → FRED API (series_id=T10YIE) | ✓ API（FRED 直取） |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py → FRED API (series_id=DCOILWTICO) | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py → FRED API，yoy_pct | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py → FRED API (series_id=T5YIFR) | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py → FRED API (series_id=THREEFYTP10) | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py → FRED API，repo_stress block | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | 標售報導 [primary: SEARCH]，14 日 | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py → FRED API (series_id=WALCL) | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py → FRED API (ECBASSETSW, JPNASSETS) | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Bloomberg，WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]，30 日 | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報彙總，WebSearch（沿用 1Q26 指引） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露，WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／The Information，WebSearch | ✗ NOT DISCLOSED（無 3Q26 當季披露） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報＋30 日融資事件掃描 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 [primary: SEARCH]，沿用最近組合值 | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q [primary: SEARCH]，30 日 | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速＋30 日進出場事件 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | WebSearch，7 日 | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis，WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／Benzinga／StockTitan movers [primary: SEARCH]，7 日 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導，WebSearch，30 日 | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR [primary]／openinsider，14 日（EDGAR 一手連線受限） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe daily statistics [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF.com，30 日 | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA，7 日 | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe insights，WebSearch | ✓ SEARCH-VERIFIED（快照 2026-02-28） |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com，WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe／AInvest，WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py → FRED API (series_id=VIXCLS) + vix_spx_comove block | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | Advisor Perspectives 交叉引用 | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]，30 日 | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py → FRED API (series_id=LNFACBW027SBOG) | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py：cftc_lev_funds、move_index、ofr_repo | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.08 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 41.52 | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 trailing P/E 約 40 | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026 （MarketXLS） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS 約 198bp 創紀錄、CoreWeave CDS 約 665bp | Oracle CoreWeave CDS spread widening July 2026 | https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/ （RIA） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP +10.68% vs SPY +7.47% YTD | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St.） | 2026-06-10 | 2026-07-20T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 36.40% | S&P 500 top 10 concentration percent 2026 | https://ahasignals.com/sp500-concentration-risk/ （AHA Signals；原定 State Street SPDR 持股） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| breadth.advance_decline | NYSE 下跌家數約為上漲 2 倍、新高 241／新低 166 | NYSE advance decline breadth July 17 2026 | https://money.usnews.com/investing/news/articles/2026-07-17/wall-st-futures-fall-as-chip-selloff-gathers-pace-netflix-tumbles （US News／Reuters） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（Fear） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed （MacroMicro；原定 cnn.com） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-05 月資料）$1.416T、YoY +53.7% | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives；原定 FINRA） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |
| retail.aaii | AAII Bull 44.9% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number （YCharts；原定 naaim.org） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 2.59、小幅 tail | US Treasury 10Y auction July 2026 bid to cover | https://cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/ （Crypto Briefing；原定 TreasuryDirect） | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch：7/29 維持利率約 86.7% | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch （CryptoRank；原定 CME FedWatch） | 2026-07-18 | 2026-07-20T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance （Bloomberg） | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC 2Q26 redemption-request ratio 18.8%，5% quarterly redemption cap 下 gate proration / breach | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://whbl.com/2026/07/02/blue-owl-keeps-withdrawal-limits-even-as-redemption-pressure-modestly-eases/ （WHBL／Reuters） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計約 $700B、仍上修（1Q26 財報季） | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html （Yahoo Finance） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 +13–18% QoQ | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html （TrendForce） | 2026-07-03 | 2026-07-20T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex 約 $700B vs AI 終端營收低百億美元級（組合值沿用） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| speculation.ai_rename_spac | EVTV 更名為 Azio AI（AZIO） | AI rename ticker change July 2026 Azio EVTV | https://www.businesswire.com/news/home/20260710628386/en/Azio-AI-Holdings-Inc.-Nasdaq-EVTV-to-Begin-Trading-Under-New-Ticker-Symbol-AZIO-Completing-Corporate-Rebrand （Business Wire） | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD 約 200 檔 IPO、募資 $141.2B | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/ （StockAnalysis） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| speculation.microcap_moonshots | 7 日內合格 microcap moonshot 0 件 | microcap 100% single day quantum AI moonshot July 2026 | Finviz／Benzinga／StockTitan movers screener | — | 2026-07-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 投資人會議，估值約 $965B，可能 10 月掛牌 | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html （CNBC） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 cluster 0 件（EDGAR 一手 URL 無法取得） | insider Form 4 cluster AI leaders July 2026 openinsider | SEC EDGAR／openinsider | — | 2026-07-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.73（日讀數） | Cboe equity put call ratio July 2026 | https://www.cboe.com/markets/us/options/market-statistics/daily/ （Cboe） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 約 $198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing；原定 etf.com） | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 推出 6 檔 2x 單一個股 ETF（GOOGL／AMZN／META／AAPL） | single-stock leveraged ETF launch July 2026 Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-07 | 2026-07-20T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 成交約 63% | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/ （Cboe） | 2026-02-28 | 2026-07-20T09:30:00+08:00 |
| structural.options_volume | OCC 選擇權成交（2026-06 月資料）1,603,491,559 口、YoY +45% | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 145.13、VIX 約 16.5、期限結構 contango | VIX term structure SKEW July 2026 | https://www.ainvest.com/news/0dte-volatility-drives-market-strategies-2026-2602/ （AInvest） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-05 月資料）$1.416T、YoY +53.7%（交叉引用） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-07-20",
  "iso_week": "2026-W30",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "yes",
  "horizon_end": "2027-01-18",
  "prior_date": "2026-07-16",
  "prior_answer": "yes",
  "flip_evidence": [],
  "r1_drawdown_pct": 6.74,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

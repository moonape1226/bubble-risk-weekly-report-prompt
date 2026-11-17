> [DRY RUN] this report was not committed to archive.

# 2026-09-13 AI 泡沫破裂預測報告

報告日期：2026-09-13｜ISO 週次：2026-W37｜預測窗口：2026-09-13 → 2027-03-14｜前次基準：report-2026-09-03（10天前）

## 結論

**結論：no**

三條路徑目前都離解析門檻很遠：NASDAQ-100 距 52 週高點回撤僅 4.21%，還需再跌約 21.70% 才觸及 R1；本次證據中四大 hyperscaler 2026 capex 合計仍約 $725bn，未見任何一家下修（R2）；HY OAS 2.70% 仍處緊縮水位，且未發現任何 R3 規模借款人的違約或困境訊號。升息預期、長端利率與波動率同步走升是真實的壓力來源，但尚不足以讓任一路徑在 182 天內「較可能完成」。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

`valuation.ndx_drawdown`：NASDAQ-100 最新收盤 29,368.44（2026-09-11），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 4.21%。R1 門檻水位為 22,995.45，自最新收盤須再下跌約 21.70% 才會觸及。

背景：S&P 500 收 7,656.98（2026-09-11），較前次基準日 −1.17%，仍高於 200 日均線 6.9%、高於 52 週均線 8.33%（`valuation.sp500_trend`）；VIX 由 14.32 升至 17.84（+24.58%），同期 S&P 500 −2.01%，屬正常的避險反向走勢、非 crowded-optionality 式同漲（`structural.vix_spx_comove`）。估值端 Shiller CAPE 約 40.73（`valuation.sp500_pe_cape`）、前十大成分股集中度約 38%（`breadth.top10_concentration`），顯示一旦下跌其幅度可能很大。

催化劑：CME FedWatch 顯示 2026-09-16 FOMC 升息 25bp 的市場隱含機率約 85.5%（`monetary.fedwatch`，2026-09-12），10Y 殖利率 4.95%、本次 +18.0bp（`monetary.dgs10`），實質利率 2.55%、+13.0bp（`monetary.dfii10`）。

**判讀：** R1 尚遠，距門檻約 21.70% 的再下跌；要在窗口內觸發需要一次由升息／長端利率衝擊加上 AI 獲利或信用事件共同引發的快速去槓桿，目前資金與信用指標尚未顯示這種傳導已啟動。

### R2 資本支出收縮

`ai.hyperscaler_capex`：本次取得的最新正式資料為 2026-07-28 的季報後彙整（2026 Q2 財報季），四大 hyperscaler 2026 年 capex 指引合計約 $725bn。

- Microsoft：個別指引數值與方向本次證據未載；未見下修。
- Alphabet：個別指引數值與方向本次證據未載；同篇報導指出其財報後市場對 capex 審視升高，但未見下修。
- Amazon：個別指引數值與方向本次證據未載；未見下修。
- Meta：個別指引數值與方向本次證據未載；未見下修。

已知下修家數：0／4。依季報節奏，窗口（至 2027-03-14）內預計涵蓋兩輪季報（2026 Q3 與 Q4），但確切財報日期本次證據未載。需求側對照：Anthropic 年化 run-rate 約 $65bn（`ai.openai_anthropic_revenue`，2026-08-17）；已披露年化 AI 終端營收約 $105bn vs 年化 capex 約 $725bn（分母：top-4，MSFT／GOOGL／AMZN／META；Oracle 本次無可用季頻資料，未納入），AI 營收對 capex 缺口（revenue-to-capex gap）約 $620bn（`ai.revenue_capex_gap`）。H100 中位租金約 $3.38／小時（`ai.compute_supply_demand`，2026-08-31），本次未見利用率下滑或訂單消化的配對證據。

**判讀：** R2 尚未啟動；要在窗口內成立需兩家在 Q3 或 Q4 財報下修 capex，這通常需要 R1 式股價壓力或 AI 需求明顯放緩先出現，而目前證據顯示需求端仍在擴張。

### R3 AI 信用事件

`structural.ai_infrastructure_debt`：30 日掃描僅取得 2026-09-08 Qualcomm 對 Amazon 發行約 $4bn 認股權證的 AI 資料中心基礎設施協議，屬供應商對買方的 vendor-financing loops 類安排，並非 R3 規模借款人的債務壓力事件。本次 AI 信用定價分歧（equity-vs-credit schism）的 14 日掃描未找到合格的 neocloud／AI 基礎設施發債人利差或 CDS 資料，因此無法直接評估 CoreWeave 等潛在 R3 借款人的當前信用定價、到期牆或評等動作。

廣義信用：HY OAS 2.70%（+5bp，`monetary.hy_oas`）、IG OAS 0.80%（−1bp，`monetary.ig_oas`），皆在緊縮水位；repo 資金壓力（SOFR−IORB）為 −3bp、SOFR99−IORB 為 +5bp（2026-09-10），SRF 動用（Standing Repo Facility usage）為 0（2026-09-11），未見資金面失序（`monetary.repo_stress_srf`）。

**判讀：** 本次無任何 R3 規模借款人出現違約、寬限期或 distressed exchange 的跡象，且整體信用利差緊；要在窗口內成立，需要升息與長端利率上行把 neocloud 再融資成本推高到無法展延，目前缺乏直接的發債人層級證據，這是最大的資料缺口。

## 支持 yes 的證據

- [整體] 2026-09-16 FOMC 升息 25bp 的市場隱含機率約 85.5%（2026-09-12，`monetary.fedwatch`），CPI YoY 3.35%（2026-08 月資料，`monetary.cpi_yoy`）、WTI $97.26（+5.09%，`monetary.wti`）限制了 Fed 緩衝 AI 主導回檔的空間。
- [R1] 長端利率與債市波動同步上升：10Y 4.95%（+18.0bp，`monetary.dgs10`）、10Y 實質利率 2.55%（+13.0bp，`monetary.dfii10`）、MOVE 82.21（+7.53，`structural.treasury_basis_trade`），對高估值長存續期 AI 股的折現率壓力上升。
- [R1] 估值與集中度處極端水位：Shiller CAPE 約 40.73（2026-09-01，`valuation.sp500_pe_cape`），S&P 500 前十大集中度約 38%（2026-09-01，`breadth.top10_concentration`），一旦觸發下跌幅度可能很大。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）：已披露年化 AI 終端營收約 $105bn vs top-4 年化 capex 約 $725bn（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`），回本壓力為 capex 下修提供基本面動機。
- [R3] AI infrastructure debt financing / vendor-financing loops 持續：Qualcomm 對 Amazon 發行約 $4bn 認股權證以綁定資料中心合作（2026-09-08，`structural.ai_infrastructure_debt`），顯示供應鏈以權益誘因換取需求的循環安排仍在擴大。
- [R1] 風險情緒轉弱：CNN Fear & Greed 約 35（恐懼，2026-09-10，`retail.fear_greed`），VIX 17.84（+24.58%，`structural.vix_spx_comove`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點僅 4.21% 回撤，須再跌約 21.70% 才觸及門檻 22,995.45（2026-09-11，`valuation.ndx_drawdown`）；基準率上 182 天內出現 25% 回撤本身就不常見。
- [R3] 信用市場未見重定價：HY OAS 2.70%（`monetary.hy_oas`）、IG OAS 0.80%（`monetary.ig_oas`），repo 資金壓力（SOFR−IORB）−3bp、SRF 動用 0（`monetary.repo_stress_srf`），沒有信用事件前常見的利差走闊或資金緊縮。
- [R2] 四大 hyperscaler 2026 capex 指引合計仍約 $725bn，本次證據未見任何一家下修（2026-07-28，`ai.hyperscaler_capex`）。
- [R2] AI 需求端仍在擴張：Anthropic 年化 run-rate 約 $65bn（2026-08-17，`ai.openai_anthropic_revenue`），H100 中位租金約 $3.38／小時（2026-08-31，`ai.compute_supply_demand`），未見利用率崩落配對證據。
- [R1] S&P 500 僅較前次基準日 −1.17%，仍高於 200 日均線 6.9%（`valuation.sp500_trend`），趨勢未破；VIX 與 S&P 500 為正常反向走勢、非同漲警戒（`structural.vix_spx_comove`）。
- [整體] 投機狂熱訊號未現：7 日 +AI 改名／SPAC 掃描 0 件（`speculation.ai_rename_spac`）、microcap moonshot 0 件（`speculation.microcap_moonshots`），AAII 看多約 38.0%（`retail.aaii`），不似末段狂熱。

## 與前期比較

前次結論：無前次預測（report-2026-09-03 為舊格式評分報告）

自 2026-09-03 以來的主要變化（僅供參考，不構成翻轉判定）：
- 10Y 殖利率 +18.0bp 至 4.95%、實質利率 +13.0bp，MOVE +7.53 至 82.21，債市波動上升。
- VIX 由 14.32 升至 17.84，S&P 500 −1.17%，NASDAQ-100 回撤擴至 4.21%。
- 9/16 FOMC 升息預期升至約 85.5%，WTI +5.09% 至 $97.26。
- 信用利差大致持平（HY +5bp、IG −1bp），資金面無壓力。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

非成功但可能影響判斷的來源（✗ NOT DISCLOSED）：
- valuation.ai_credit_schism：14 日內無 AI 發債人利差／CDS 資料，是 R3 評估最大缺口；若有 neocloud 利差急遽走闊的資料，會把答案推向 yes，但目前無證據顯示如此。
- ai.capital_cycle（兩組件皆無披露）與 ai.hyperscaler_financing_mix 的 30 日 event_scan 無新事件：無法判定資本週期階段，也無法確認 hyperscaler 新發債動態。
- monetary.private_credit_liquidity、ai.depreciation_life、ai.customer_concentration_rpo、ai.token_growth、speculation.upcoming_ai_ipos、valuation.analyst_tp_decomposition、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、structural.global_leveraged_approvals：本次掃描完成但無合格披露，個別不太可能改變答案。
- speculation.insider_form4 以 0 件計：EDGAR 檢索有一筆命中，但僅顯示單一日期、無法分辨 filing date 與 transaction date，不符合合格條件，因此不列名、不列金額。
- ai.hyperscaler_capex 只取得四家合計，未取得個別公司指引與方向，R2 的逐家判讀因此不完整；若其中有一家其實已下修，R2 距門檻會比本文所述更近。
- 部分 snapshot 資料偏舊：breadth.rsp_spy 為至 2026-07 的 YTD 數字、valuation.mag7_multiples 資料日 2026-08-03，未作為主要論據。
- 證據紀錄中 structural.treasury_basis_trade 註記為「script 三區塊 fetch_failed」，但 macro artifact 中 cftc_lev_funds／move_index／ofr_repo 三區塊皆為 ok；本報告以 artifact 為準記 ✓ API。

最大的不確定性：
1. 2026-09-16 FOMC：若如預期升息且釋出進一步緊縮訊號，長端利率與 AI 估值可能同步重定價，推向 yes（R1）；若按兵不動或措辭偏鴿，則支持 no。
2. 2026 Q3／Q4 hyperscaler 財報：任兩家 capex 下修即直接觸發 R2，推向 yes；續上修則支持 no。
3. neocloud 再融資：缺乏發債人層級信用資料；若利率上行導致再融資受阻，R3 風險會被低估。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7656.98 | FRED API (series_id=SP500)，sp500_trend 區塊 | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 6.9 | FRED API (series_id=SP500)，sp500_trend 區塊 | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.33 | FRED API (series_id=SP500)，sp500_trend 區塊 | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較前次基準 %） | -1.17 | FRED API (series_id=SP500)，sp500_trend 區塊 | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29368.44 | FRED API (series_id=NASDAQ100)，ndx_drawdown 區塊 | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100)，ndx_drawdown 區塊 | 2026-06-02 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 4.21 | FRED API (series_id=NASDAQ100)，ndx_drawdown 區塊 | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100)，ndx_drawdown 區塊 | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2 季資料，%） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.7 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.8 | FRED API (series_id=BAMLC0A0CM) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.95 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（較 2026-09-03） | 18.0 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.55 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps（較 2026-09-03） | 13.0 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.36 | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps（較 2026-09-03） | 1.0 | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（美元／桶） | 97.26 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO chg_pct（較前次 %） | 5.09 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-08 月資料，%） | 3.35 | FRED API (series_id=CPIAUCSL) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.32 | FRED API (series_id=T5YIFR) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 0.8892 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7d） | 1.4 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API (series_id=SOFR99) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-09-13 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,740,619（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,912,178（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（無新觀測） | 6,446,620（¥644.66T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 17.84 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of，base 2026-09-03，7 日窗） | 17.84 | FRED API（SP500 對齊），fetch_macro.py vix_spx_comove 區塊 | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（%） | 24.58 | FRED API（SP500 對齊），fetch_macro.py vix_spx_comove 區塊 | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（%，comove=false） | -2.01 | FRED API（SP500 對齊），fetch_macro.py vix_spx_comove 區塊 | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（無新觀測） | 2027.9777（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -6,863,118 | CFTC TFF futures-only，cftc_lev_funds 區塊 | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 387,809 | CFTC TFF futures-only，cftc_lev_funds 區塊 | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 82.21 | Yahoo Finance chart API (^MOVE)，move_index 區塊 | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index delta_abs（較 2026-09-03） | 7.53 | Yahoo Finance chart API (^MOVE)，move_index 區塊 | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2271.6 | OFR STFM (REPO-TRIV1_TV_TOT-P)，ofr_repo 區塊 | 2026-09-11 | 2026-09-13T09:30:00+08:00 |

10Y 分解（`decomposition`）：ΔDGS10 +18.0bp、ΔDFII10 +13.0bp、ΔT10YIE +1.0bp；T10YIE 最新觀測 2026-09-11 與另兩腿 2026-09-10 視窗不一致，判讀：不可判（視窗不一致）。repo 利差：SOFR−IORB −3bp、SOFR99−IORB +5bp（兩腿皆 2026-09-10）。

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（multpl / gurufocus） | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-08-03，偏舊） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED（掃描完成，無合格同季 TP 上修） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✗ NOT DISCLOSED（掃描完成，無窗內合格資料） |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED（至 2026-07 YTD，偏舊） |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED（以 % above 200-day 代理） |
| retail.fear_greed | Retail / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail / Margin Debt: FINRA | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED（2026-07 月資料） |
| retail.aaii | Retail / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail / Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary / Fed funds rate: FRED | fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok、DFEDTARL ok） |
| monetary.hy_oas | Monetary / High Yield OAS | fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary / Investment Grade OAS | fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary / 10Y Treasury yield | fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary / 10Y Treasury real yield | fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary / 10Y breakeven inflation rate | fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary / WTI crude oil price | fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary / CPI YoY: FRED | fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary / 5y5y forward inflation expectation | fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary / 10Y 期限溢價（term premium）: FRED | fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD） | ✓ API（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） |
| monetary.treasury_auctions | Monetary / 美債標售需求 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary / Fed funds rate path expectations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary / Fed balance sheet: FRED | fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary / Global central bank liquidity cross-check | fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok、JPNASSETS ok） |
| monetary.pboc | Monetary / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | WebSearch（stock-of-state，沿用 2026 Q2 財報季） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構 | WebSearch（quarterly_state 沿用季頻；event_scan 30d 掃描完成無新事件） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口 | WebSearch＋組合既有 bullets（分母 top-4） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI / 資本週期階段 | WebSearch（兩組件皆掃描完成無披露） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculation / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculation / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculation / Microcap thematic moonshots | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculation / Upcoming AI IPOs | WebSearch（30d） | ✗ NOT DISCLOSED |
| speculation.insider_form4 | Speculation / Insider selling at AI | SEC EDGAR＋WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculation / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural / VIX / S&P 500 co-movement | fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API |
| structural.margin_debt_crosscheck | Structural / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural / Bank loans to nondepository financial institutions | fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py（cftc_lev_funds、move_index、ofr_repo，aggregation any） | ✓ API（cftc_lev_funds ok、move_index ok、ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.73（原定來源 multpl / gurufocus） | S&P 500 Shiller CAPE ratio current September 2026 multpl | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | Magnificent 7 forward P/E valuation September 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html（CNBC） | 2026-08-03 | 2026-09-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 至 2026-07 YTD 報酬約 13%（文章發布 2026-09-01） | RSP equal weight vs SPY S&P 500 YTD performance September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度約 38% | S&P 500 top 10 concentration percentage September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 200 日均線之上約 53% | market breadth advance decline new highs lows September 2026 percent stocks above 200-day | https://condoredge.com/stocks/market-breadth（Condor Edge） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 約 35（恐懼） | CNN Fear and Greed Index today September 2026 reading | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）約 $1.42T | FINRA margin debt August 2026 record year over year | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026（Advisor Perspectives，原定來源 FINRA） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.0% | AAII sentiment survey results week September 10 2026 bullish bearish neutral | https://www.aaii.com/sentimentsurvey（AAII） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.71 | Treasury auction results September 2026 tail bid-to-cover 10-year | https://thevaultreport.com/treasury-auctions（The Vault Report） | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.fedwatch | 2026-09-16 FOMC 升息 25bp 市場隱含機率約 85.5%（原定來源 CME FedWatch） | CME FedWatch September 12 2026 probability 25 basis point hike | https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html（Yahoo Finance） | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.pboc | 2026 年 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate financing 2026 total social financing | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm（SteelOrbis） | 2026-08-15 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 指引合計約 $725bn（2026 Q2 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 $65bn | OpenAI Anthropic annualized revenue run rate September 2026 | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| ai.compute_supply_demand | H100 中位租金約 $3.38／小時 | GPU rental price HBM DRAM contract price September 2026 utilization | https://www.thundercompute.com/blog/ai-gpu-rental-market-trends（Thunder Compute） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 增額債務佔 capex 約 32% | hyperscaler capex vs free cash flow debt issuance 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $105bn（分母 top-4 capex 約 $725bn） | AI revenue vs capex gap 2026 annualized run rate | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement September 7-13 2026 | 檢查來源：SPACInsider、Businesswire SPAC newsroom、Boardroom Alpha（窗內無合格事件） | — | 2026-09-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 22 檔 | IPO priced week September 8 2026 first day return debut | https://www.iposcoop.com/current-year-pricings/（IPOScoop） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（0 件符合 2+ 主題×弱基本面） | biggest stock gainers week September 7 2026 microcap 100% quantum AI | 檢查來源：Finviz、Benzinga、StockTitan、Yahoo movers（Tenon +77%、AEON +35% 皆未達門檻） | — | 2026-09-13T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 14 日掃描（0 件合格：唯一命中缺獨立 transaction date） | insider selling Form 4 September 2026 Nvidia AI executives SEC filing | 檢查來源：SEC EDGAR Form 4、WebSearch（無同時具 filing date 與 transaction date 的合格紀錄） | — | 2026-09-13T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 約 0.67 | Cboe equity put call ratio September 2026 reading | https://www.thetrading.tools/put-call-ratio（thetrading.tools） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 $40.74bn | leveraged ETF assets under management September 2026 record single stock | https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/（ETF Action） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval September 2026 | 檢查來源：SEC EDGAR、ETF.com 新上市 feed（窗內無合格核准或上市） | — | 2026-09-13T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比創紀錄約 62%（2026-08） | 0DTE options share SPX volume September 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.options_volume | OCC 2026-08 總結算量約 1.44 十億口 | OCC options volume August 2026 monthly report | https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/（Traders Magazine） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 收在約 17 以上、call skew 第 91 百分位 | fear gauge VIX hedges September 10 2026 volatility | https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html（CNBC） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-07 月資料）對股票市值比率，基數約 $1.42T | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php（Current Market Valuation） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Qualcomm 對 Amazon 發行約 $4bn 認股權證（資料中心基礎設施合作，vendor-financing loops） | Qualcomm warrants Amazon 4 billion AI infrastructure deal September 2026 | https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html（CNBC） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-09-13",
  "iso_week": "2026-W37",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-03-14",
  "prior_date": "2026-09-03",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 4.21,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

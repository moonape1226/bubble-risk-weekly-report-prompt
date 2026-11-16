> [DRY RUN] this report was not committed to archive.

# 2026-09-13 AI 泡沫破裂預測報告
報告日期：2026-09-13｜ISO 週次：2026-W37｜預測窗口：2026-09-13 → 2027-03-14｜前次基準：report-2026-09-03（10天前）

## 結論

**結論：no**

三條路徑都離觸發點很遠：NASDAQ-100 只比 52 週高點低 4.21%，還要從最新收盤再跌約 21.70% 才會碰到 R1（`valuation.ndx_drawdown`）；HY OAS 2.70%、IG OAS 0.80% 仍非常緊（`monetary.hy_oas`、`monetary.ig_oas`），證據中也沒有任何 hyperscaler 下修 capex 指引（`ai.hyperscaler_capex`）。最明確的反向催化劑是 9/16 FOMC 升息定價約 85.5%（`monetary.fedwatch`），再加上殖利率與油價走高。這些因素提高了下跌風險，但目前還不足以讓 182 天內觸發的可能性高過基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,368.44（2026-09-11），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 4.21%。R1 門檻為 22,995.45，從最新收盤還要再跌約 21.70% 才會觸及（`valuation.ndx_drawdown`）。S&P 500 收在 7,656.98（2026-09-11），比 200 日均線 7,162.55 高 6.9%、比 52 週均線高 8.33%。自前次基準（2026-09-03）以來下跌 1.17%（`valuation.sp500_trend`）。

最近一週風險偏好轉弱：VIXCLS 從 14.32 升到 17.84（+24.58%），同期 S&P 500 下跌 2.01%（視窗 2026-09-03 → 2026-09-10）。這是典型的 risk-off 反向走勢，不是 crowded-optionality 共振，`comove` 為 false（`structural.vix_spx_comove`）。MOVE 從 74.68 升到 82.21（`structural.treasury_basis_trade`）。

估值與集中度仍偏高：Shiller CAPE 約 40.73（`valuation.sp500_pe_cape`），前十大成分股約佔 38%（`breadth.top10_concentration`）。不過 Mag 7 前瞻本益比低於 24（`valuation.mag7_multiples`），Fear & Greed 約 35、處於恐懼區（`retail.fear_greed`），AAII 看多比例約 38.0%（`retail.aaii`），情緒並不亢奮。

**判讀：** R1 離門檻很遠，還差約 21.70% 的跌幅。窗口內要觸發，需要一次熊市等級的重估，例如 Fed 升息後接著殖利率與油價再衝高、AI 龍頭財報讓市場失望，或信用端出現傳導。現有證據顯示的是脆弱度上升，還沒看到正在進行中的崩跌。

### R2 資本支出收縮

最近一次可取得的 hyperscaler capex 資料：CNBC 2026-07-28（2026 年第二季財報季）報導，Microsoft、Alphabet、Amazon、Meta 四家 2026 年 capex 合計約 $725bn，並指出 Alphabet 財報後市場對 capex 的檢視變嚴（`ai.hyperscaler_capex`）。本次檢索證據沒有提供四家各自的指引數值，也沒有提供各家相對前一次正式指引的方向（上修／持平／下修）。因此本次沒辦法逐家確認方向，但證據中沒有任何一家下修 capex 指引的報導，目前已知下修家數為 0。下一輪（2026 年第三季）財報依季報節奏會落在窗口內，具體日期不在本次證據中。

需求面：Anthropic 年化 run-rate 約 $65bn（2026-08-17，`ai.openai_anthropic_revenue`）。H100 中位租金約 $3.38/hr（2026-08-31，`ai.compute_supply_demand`），單一價格點不足以判斷產能缺口。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 $105bn，對比年化 capex 約 $725bn（分母只含 top-4，不含 Oracle，因為 Oracle 季度資料本次未取得）（`ai.revenue_capex_gap`）。這次沒有前一組可比組合，所以無法判斷缺口是在擴大還是收斂。

**判讀：** R2 目前看不到正在形成的跡象。要在窗口內觸發，至少兩家須在接下來的季報中正式下修 capex 指引。比較可能的觸發順序是先出現 R1 等級的股價重挫或融資條件收緊，再迫使 hyperscaler 削減支出。目前營收對 capex 的落差很大，代表長期回本壓力存在，但還沒轉成下修行動。

### R3 AI 信用事件

本次證據沒有涵蓋任何符合 R3 規模門檻（以 AI 資料中心／算力為主業、負債 ≥ 50 億美元）的借款人當期的債券殖利率、利差、CDS、評等動作、到期牆，或違約／寬限／distressed exchange 訊號。AI 信用定價分歧與私募信貸贖回壓力的掃描都已完成，但 14／30 日窗口內沒有合格披露，詳見資料缺漏一節。

AI infrastructure debt financing / vendor-financing loops 這部分，窗口內有一筆紀錄：Qualcomm 與 Amazon 的 data-center 基礎設施交易，Qualcomm 給 Amazon 約 $4bn 認股權證（2026-09-08，`structural.ai_infrastructure_debt`）。這屬於「供應商給買方股權誘因」的循環結構，不是違約訊號。整體信用環境依然寬鬆：HY OAS 2.70%（比前次 +5bp，`monetary.hy_oas`），IG OAS 0.80%（`monetary.ig_oas`）。repo 資金壓力（SOFR−IORB）為 −3bp，SOFR99−IORB 為 +5bp（2026-09-10），SRF 動用（Standing Repo Facility usage）為 0（2026-09-11，`monetary.repo_stress_srf`）。

**判讀：** R3 離觸發最遠。破產、超過寬限期的違約或 distressed exchange，通常要先經過利差大幅走闊、融資窗口關閉和再融資失敗，現在三個條件都沒有出現。要在窗口內觸發，需要升息與殖利率上行把高槓桿 neocloud 類借款人的再融資成本推到臨界點，而本次證據中看不到這個前兆。

## 支持 yes 的證據

- [整體] 9/16 FOMC 升息定價約 85.5%（2026-09-12，`monetary.fedwatch`），目前 fed funds 目標區間 3.50%–3.75%（`monetary.fed_funds`）。同時 CPI YoY 3.35%（2026-08 月資料，`monetary.cpi_yoy`），WTI 漲到 $97.26（比前次 +5.09%，`monetary.wti`）。在高估值下轉向緊縮，是 R1 最直接的催化劑，也壓縮 Fed 在跌勢中出手緩衝的空間。
- [R1] 10Y 殖利率升到 4.95%（比前次 +18bp，`monetary.dgs10`），實質殖利率 2.55%（+13bp，`monetary.dfii10`）。10Y 期限溢價（term premium）為 0.8892%（2026-09-04，`monetary.term_premium`）。實質利率走高直接壓低長存續期 AI 股的折現價值。
- [R1] 估值與集中度仍處極端：Shiller CAPE 約 40.73（2026-09-01，`valuation.sp500_pe_cape`），前十大成分股約佔 S&P 500 的 38%（2026-09-01，`breadth.top10_concentration`）。一旦出現催化劑，指數跌幅會被集中度放大。
- [R1] 波動率同步上升：VIX 7 日 +24.58% 到 17.84、S&P 500 −2.01%（2026-09-10，`structural.vix_spx_comove`），MOVE 從 74.68 升到 82.21（2026-09-11，`structural.treasury_basis_trade`），call skew 在第 91 百分位（2026-09-10，`structural.cross_asset_derivatives`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）很大：年化 AI 終端營收約 $105bn，年化 capex 約 $725bn（分母只含 top-4）（`ai.revenue_capex_gap`）。CNBC 報導 Alphabet 財報後 capex 受到更嚴格的檢視（2026-07-28，`ai.hyperscaler_capex`），回本壓力是 R2 的長期來源。
- [R3] AI infrastructure debt financing / vendor-financing loops 仍在擴大：Qualcomm 給 Amazon 約 $4bn 認股權證（2026-09-08，`structural.ai_infrastructure_debt`），顯示供應鏈靠股權誘因綁定需求的循環結構。
- [整體] 投機性籌碼仍然很大：SPX 0DTE 佔比創紀錄約 62%（2026-08，`structural.zero_dte`），單一個股槓桿 ETF 規模約 $40.74bn（2026-09-08，`structural.leveraged_etf_aum`），margin debt 約 $1.42T（2026-07，`retail.margin_debt`）。一旦下跌，可能引發被迫去槓桿。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.21%（2026-09-11），R1 門檻 22,995.45 還需要再跌約 21.70%（`valuation.ndx_drawdown`）。S&P 500 仍比 200 日均線高 6.9%（`valuation.sp500_trend`），趨勢還沒破。
- [R3] 信用市場沒有壓力：HY OAS 2.70%（比前次 +5bp，`monetary.hy_oas`），IG OAS 0.80%（−1bp，`monetary.ig_oas`）。窗口內的 AI 信用事件通常會先看到利差大幅走闊，但目前還沒有這個前兆。
- [整體] 融資市場運作正常：SOFR−IORB −3bp、SOFR99−IORB +5bp、SRF 動用為 0（`monetary.repo_stress_srf`）。銀行對 NBFI 放款 $2.03T 持平（`structural.nbfi_bank_loans`）。美債標售需求方面，10Y bid-to-cover 約 2.71（2026-09-09，`monetary.treasury_auctions`），沒有失序跡象。
- [R2] 證據中沒有任何 hyperscaler 下修 capex 指引，四家 2026 年 capex 合計約 $725bn（`ai.hyperscaler_capex`）。終端需求仍在成長：Anthropic 年化 run-rate 約 $65bn（2026-08-17，`ai.openai_anthropic_revenue`）。
- [R1] 情緒沒有過熱，已經消化一部分風險：Fear & Greed 約 35、處於恐懼區（2026-09-10，`retail.fear_greed`），AAII 看多比例約 38.0%（`retail.aaii`），equity put/call 約 0.67（`speculation.equity_put_call`）。Mag 7 前瞻本益比低於 24（`valuation.mag7_multiples`）。
- [整體] 基準率：任意 182 天窗口內，NASDAQ-100 回撤 25%、兩家 hyperscaler 下修 capex、或大型 AI 基礎設施違約都屬少見事件。本次投機篩檢中，+AI 改名／SPAC 與 microcap moonshot 都是 0 件（`speculation.ai_rename_spac`、`speculation.microcap_moonshots`），看不到末期狂熱的典型訊號。

## 與前期比較

前次結論：無前次預測（report-2026-09-03 為舊格式評分報告）

前次是舊格式評分報告，沒有 yes/no 預測可以比較，所以 flip_evidence 為空。自 2026-09-03 以來的主要變化：10Y 殖利率 +18bp 到 4.95%（`monetary.dgs10`），WTI +5.09%（`monetary.wti`），VIX 從 14.32 升到 17.84（`structural.vix_spx_comove`），S&P 500 −1.17%（`valuation.sp500_trend`），HY OAS +5bp（`monetary.hy_oas`）。10Y 本次 Δ 分解：ΔDGS10 +18bp、ΔDFII10 +13bp、ΔT10YIE +1bp，判讀為不可判（視窗不一致）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源檢索已完成，但窗口內沒有合格披露（✗ NOT DISCLOSED）：valuation.analyst_tp_decomposition、valuation.ai_credit_schism、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.private_credit_liquidity、ai.token_growth、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（quarterly_state 有資料，增額債務約佔 capex 32%，但 30 日 event_scan 沒有新事件）、ai.depreciation_life、ai.capital_cycle（增速證據不足，本次不判定週期階段）、speculation.upcoming_ai_ipos、structural.global_leveraged_approvals。其中 valuation.ai_credit_schism 與 monetary.private_credit_liquidity 的空白對 R3 影響最大：如果實際上 AI 發行人利差已經走闊，或已有基金出現 gate proration / breach，R3 與 R1 的時序判斷可能會往 yes 移動。不過大盤 HY／IG OAS 仍緊，代表這個盲點不太可能掩蓋正在進行中的信用事件。

speculation.insider_form4 檢索到一筆 2026-09-02 的 SEC EDGAR Form 4 結果，但無法同時確認 filing date 與 transaction date 等完整 filing-level 欄位，依規則不列為合格事件，記為 0 件。這不影響結論。

ai.hyperscaler_capex 只取得四家合計約 $725bn，沒有逐家指引與方向，所以 R2 的「已下修家數」是根據「證據中沒有下修報導」推得。如果有某家已經悄悄下修，R2 會比本文所述更接近觸發，但要兩家才成立，結論仍不會因此改變。

最大的三項不確定性：
- 9/16 FOMC：若照市場定價升息，並搭配鷹派指引，殖利率與實質利率可能再升，把 R1 推向 yes。若意外按兵不動，則偏 no。
- 2026 年第三季 hyperscaler 財報（窗口內）：只要有兩家下修 capex 就直接觸發 R2。若指引維持或上修，R2 在窗口內基本可以排除。
- 油價與通膨：WTI 已到 $97.26，CPI YoY 3.35%。若通膨再加速，會壓縮 Fed 在 AI 領跌時出手護盤的空間，提高 R1 尾部風險。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7656.98 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 6.9 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.33 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較前次 %） | -1.17 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29368.44 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.21 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2 季資料，FRED 觀測日） | 48.2301354474（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75（%） | FRED API (series_id=DFEDTARU) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5（%） | FRED API (series_id=DFEDTARL) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.7（%） | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 5.0（bp） | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.8（%） | FRED API (series_id=BAMLC0A0CM) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM delta_bps | -1.0（bp） | FRED API (series_id=BAMLC0A0CM) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.95（%） | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | 18.0（bp） | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.55（%） | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | 13.0（bp） | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.36（%） | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | 1.0（bp） | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 97.26（美元） | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO chg_pct | 5.09（%） | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-08 月資料） | 3.35（%） | FRED API (series_id=CPIAUCSL) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.32（%） | FRED API (series_id=T5YIFR) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8892（%） | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（序列自身 trailing 7d） | 1.4（bp） | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.62（%） | FRED API (series_id=SOFR) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.7（%） | FRED API (series_id=SOFR99) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65（%） | FRED API (series_id=IORB) | 2026-09-13 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用 transaction volume） | 0.0（十億美元） | FRED API (series_id=RPONTTLD) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps（iorb_date 2026-09-10） | -3.0（bp） | FRED API (repo_stress block) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr99_iorb_bps（sofr99_iorb_date 2026-09-10） | 5.0（bp） | FRED API (repo_stress block) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,740,619（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,912,178（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（no_new_obs） | 6,446,620（¥644.66T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 17.84 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（base_date 2026-09-03，window 7d） | 17.84 | FRED API (comove block) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 24.58（%） | FRED API (comove block) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -2.01（%） | FRED API (comove block) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（no_new_obs） | 2027.9777（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位） | -6,863,118（口） | CFTC TFF futures-only | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | 387,809（口） | CFTC TFF futures-only | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 82.21 | Yahoo Finance chart API (^MOVE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index prior | 74.68 | Yahoo Finance chart API (^MOVE) | 2026-09-03 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2271.6（十億美元） | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（multpl / GuruFocus） | ✓ SEARCH-VERIFIED（CAPE；P/E 未見於結果） |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch（CNBC） | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch（14d） | ✗ NOT DISCLOSED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch（247wallst） | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch（247wallst） | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch（condoredge market breadth） | ✓ SEARCH-VERIFIED（以 % above 200DMA 代理） |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch（cnn.com） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch（Advisor Perspectives，FINRA 2026-07 月資料 carry-forward） | ✓ SEARCH-VERIFIED（YoY 與市值比未見於結果） |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | WebSearch（aaii.com） | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（DFEDTARU ok、DFEDTARL ok） | ✓ API |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直接取得） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok；repo_stress status ok） | ✓ API |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch（SteelOrbis 引述 PBoC） | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（CNBC，2026Q2 財報季 carry-forward） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch（Axios） | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險 | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch（Thunder Compute GPU rental） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch：quarterly_state（CNBC 2026-07-28）＋ 30d event_scan（無新事件） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch（Axios）＋ hyperscaler capex 分母 | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch：quarterly_state ＋ 30d event_scan（皆無可用披露） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（IPOScoop） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（Finviz / Benzinga / StockTitan / Yahoo movers） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✗ NOT DISCLOSED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR ＋ WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch（etfaction） | ✓ SEARCH-VERIFIED（僅單一個股槓桿 ETF 合計） |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR ＋ ETF.com 新上市 feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（KRX / TWSE / JPX / ESMA，7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe insights） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（Traders Magazine 引述 OCC） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch（CNBC） | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS ok、vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（currentmarketvaluation） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok；aggregation any） | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.73（原定 multpl / GuruFocus） | S&P 500 Shiller CAPE ratio current September 2026 multpl | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | Magnificent 7 forward P/E valuation September 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html（CNBC） | 2026-08-03 | 2026-09-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 至 7 月止 YTD 報酬約 13% | RSP equal weight vs SPY S&P 500 YTD performance September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.top10_concentration | 前十大集中度約 38% | S&P 500 top 10 concentration percentage September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 200 日均線之上約 53% | market breadth advance decline new highs lows September 2026 percent stocks above 200-day | https://condoredge.com/stocks/market-breadth（Condor Edge） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 約 35（恐懼；原定 CNN） | CNN Fear and Greed Index today September 2026 reading | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| retail.margin_debt | margin debt 約 $1.42T（2026-07 月資料；原定 FINRA） | FINRA margin debt August 2026 record year over year | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026（Advisor Perspectives） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.0% | AAII sentiment survey results week September 10 2026 bullish bearish neutral | https://www.aaii.com/sentimentsurvey（AAII） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.71 | Treasury auction results September 2026 tail bid-to-cover 10-year | https://thevaultreport.com/treasury-auctions（The Vault Report） | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.fedwatch | 9/16 FOMC 升息 25bp 定價約 85.5%（原定 CME FedWatch） | CME FedWatch September 12 2026 probability 25 basis point hike | https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html（Yahoo Finance） | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate financing 2026 total social financing | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm（SteelOrbis） | 2026-08-15 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_capex | MSFT / GOOGL / AMZN / META 2026 capex 合計約 $725bn（2026Q2 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 $65bn | OpenAI Anthropic annualized revenue run rate September 2026 | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| ai.compute_supply_demand | H100 中位租金約 $3.38/hr | GPU rental price HBM DRAM contract price September 2026 utilization | https://www.thundercompute.com/blog/ai-gpu-rental-market-trends（Thunder Compute） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 增額債務約佔 capex 32%（2026Q2） | hyperscaler capex vs free cash flow debt issuance 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $105bn（分母：top-4 capex 約 $725bn） | AI revenue vs capex gap 2026 annualized run rate | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement September 7-13 2026 | 檢查來源：SPACInsider、Businesswire SPAC newsroom、Boardroom Alpha（窗內無合格事件） | — | 2026-09-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 22 檔 | IPO priced week September 8 2026 first day return debut | https://www.iposcoop.com/current-year-pricings/（IPOScoop） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（0 件符合 2+ 主題×弱基本面） | biggest stock gainers week September 7 2026 microcap 100% quantum AI | 檢查來源：Finviz、Benzinga、StockTitan、Yahoo movers（Tenon +77%、AEON +35% 皆未達門檻） | — | 2026-09-13T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 14 日篩檢（0 件；唯一候選缺完整 filing／transaction 日期欄位） | insider selling Form 4 September 2026 Nvidia AI executives SEC filing | 檢查來源：SEC EDGAR、WebSearch（無符合完整欄位要求的 filing） | — | 2026-09-13T09:30:00+08:00 |
| speculation.equity_put_call | equity put/call 約 0.67（日值或 5 日均值未標明） | Cboe equity put call ratio September 2026 reading | https://www.thetrading.tools/put-call-ratio（The Trading Tools） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 $40.74bn | leveraged ETF assets under management September 2026 record single stock | https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/（ETF Action） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval September 2026 | 檢查來源：SEC EDGAR、ETF.com 新上市 feed（窗內無合格核准或上市） | — | 2026-09-13T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比創紀錄約 62%（2026-08） | 0DTE options share SPX volume September 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.options_volume | 8 月 OCC 總結算量約 1.44 十億口（2026-08） | OCC options volume August 2026 monthly report | https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/（Traders Magazine） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 收在約 17 以上、call skew 第 91 百分位 | fear gauge VIX hedges September 10 2026 volatility | https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html（CNBC） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對市值比率基數約 $1.42T（2026-07 月資料） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php（Current Market Valuation） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Qualcomm 對 Amazon 認股權證約 $4bn（data-center 基礎設施交易） | Qualcomm warrants Amazon 4 billion AI infrastructure deal September 2026 | https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html（CNBC） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |

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

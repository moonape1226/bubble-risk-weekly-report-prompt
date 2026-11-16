> [DRY RUN] this report was not committed to archive.

# 2026-09-13 AI 泡沫破裂預測報告

報告日期：2026-09-13｜ISO 週次：2026-W37｜預測窗口：2026-09-13 → 2027-03-14｜前次基準：report-2026-09-03（10天前）

## 結論

**結論：no**

三條路徑都離解析門檻很遠：NASDAQ-100 距 52 週高點回撤 4.21%，還要再跌約 21.70% 才觸及 R1；現有證據中沒有任何 hyperscaler 下修 capex 指引，High Yield OAS 只有 2.70%，也看不到 AI 借款人違約的跡象。估值極高（CAPE 約 40.73），9/16 FOMC 也有升息風險，這些顯示泡沫脆弱，但不足以說明它會在 182 天內破裂。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29368.44（2026-09-11），252 個交易日最高收盤 30660.6（2026-06-02），距 52 週高點回撤 4.21%（`valuation.ndx_drawdown`）。R1 門檻水位為 22995.45，指數要從最新收盤再跌約 21.70% 才會觸及。可能的催化劑：CME FedWatch 顯示 9/16 FOMC 升息 25bp 的機率約 85.5%（`monetary.fedwatch`，2026-09-12），聯邦基金目標區間目前為 3.50%–3.75%（`monetary.fed_funds`）；8 月 CPI YoY 3.35%（`monetary.cpi_yoy`），WTI 漲到 97.26 美元（2026-09-09，自前次基準 +5.09%，`monetary.wti`），10Y 殖利率升到 4.95%（+18.0bp，`monetary.dgs10`）。波動度開始上升：MOVE 從 74.68 升到 82.21（`structural.treasury_basis_trade`），CNBC 2026-09-10 報導 VIX 收在約 17 以上、call skew 位於第 91 百分位（`structural.cross_asset_derivatives`）。估值面，Shiller CAPE 約 40.73（`valuation.sp500_pe_cape`），前十大成分股約占 S&P 500 的 38%（`breadth.top10_concentration`），一旦修正，下跌空間很大。另一方面，市場情緒已偏恐懼（Fear & Greed 約 35，`retail.fear_greed`），代表追價情緒沒有過熱到極端。S&P 500 的 200 日／52 週趨勢偏離本次無法取得。

**判讀：** R1 距門檻很遠：4.21% 的回撤要擴大到 25%，必須在半年內出現類似 2022 年的大幅下跌。可能把它推過門檻的情境是：升息落地，加上利率與油價持續上行，觸發高集中度大型股的估值重定價，再疊加 AI 信用事件的傳導。目前這些條件都還沒同時出現。

### R2 資本支出收縮

CNBC 2026-07-28 報導，Microsoft、Alphabet、Amazon、Meta 四家 2026 年 capex 合計約 7,250 億美元（`ai.hyperscaler_capex`，沿用 2026 年 7 月財報季的指引）。本次證據沒有逐家拆分的指引數字與前次指引值，因此四家各自的方向無法逐一確認：Microsoft、Alphabet、Amazon、Meta 的逐家指引在本次證據中都是「未提供逐家數字」。可確認的是，報導重點是市場對 capex 規模加強審視，不是任何一家下修。下修家數：現有證據中 0 家。下一輪季報預計落在窗口內，但本次證據沒有具體日期。需求面：Anthropic 年化 run-rate 約 650 億美元（`ai.openai_anthropic_revenue`，2026-08-17）；H100 中位租金約每小時 3.38 美元（`ai.compute_supply_demand`，2026-08-31），沒有伴隨利用率疲弱或訂單消化的證據。AI 營收對 capex 缺口：年化 AI 終端營收約 1,050 億美元，對比年化 capex 約 7,250 億美元（分母：僅 top-4，Oracle 本次無可組合的披露；`ai.revenue_capex_gap`）。本次沒有前次組合值，無法判斷缺口擴大還是收斂。

**判讀：** R2 需要四家中至少兩家正式下修，目前沒有任何一家下修的證據。窗口內會有一到兩輪季報；要觸發 R2，通常需要先出現 R1 等級的股價壓力，或 AI 需求明顯降溫（租金與利用率同步下滑）。這兩者目前都沒有。

### R3 AI 信用事件

本次證據沒有 AI 基礎設施借款人的債券利差、CDS、評等動作或到期牆資料，因此無法逐一確認哪些借款人已達 R3 的 50 億美元負債門檻，也無法確認其信用定價。唯一的窗內融資事件：CNBC 2026-09-08 報導 Qualcomm 與 Amazon 的資料中心基礎設施交易，Amazon 取得約 40 億美元的 Qualcomm 認股權證（`structural.ai_infrastructure_debt`），屬於 AI infrastructure debt financing / vendor-financing loops 中「供應商以股權誘因綁定買方」的型態，不是違約或困境訊號。整體信用環境仍然寬鬆：High Yield OAS 2.70%（+5bp，`monetary.hy_oas`），Investment Grade OAS 0.80%（`monetary.ig_oas`）。repo 資金壓力（SOFR−IORB）為 −3bp，SOFR99−IORB +5bp，SRF 動用 0（`monetary.repo_stress_srf`），沒有融資市場失序的跡象。

**判讀：** R3 需要大型 AI 算力借款人實際違約、破產或完成 distressed exchange；在 HY OAS 2.70% 的寬鬆環境下，再融資管道暢通，目前沒有任何困境訊號。要觸發 R3，需要先出現信用利差大幅走闊或融資市場關閉，再傳導到高槓桿 neocloud。窗口內可能的觸發路徑是升息與長端利率上行推高再融資成本，但目前沒有證據顯示這條路徑已經啟動。

## 支持 yes 的證據

- [R1] CME FedWatch 顯示 9/16 FOMC 升息 25bp 的機率約 85.5%（2026-09-12），目標區間目前為 3.50%–3.75%；在 CAPE 約 40.73 的高估值下轉向緊縮，是典型的泡沫轉折催化劑（`monetary.fedwatch`、`monetary.fed_funds`、`valuation.sp500_pe_cape`）。
- [整體] 利率與通膨壓力同步上升：10Y 殖利率 4.95%（2026-09-10，+18.0bp），10Y 實質利率 2.55%（+13.0bp），8 月 CPI YoY 3.35%，WTI 97.26 美元（+5.09%），壓縮了 Fed 緩衝 AI 主導下跌的空間（`monetary.dgs10`、`monetary.dfii10`、`monetary.cpi_yoy`、`monetary.wti`）。
- [R1] 波動度開始上升：MOVE 自 74.68（2026-09-03）升到 82.21（2026-09-11）；CNBC 報導 VIX 收在約 17 以上、call skew 位於第 91 百分位（2026-09-10）（`structural.treasury_basis_trade`、`structural.cross_asset_derivatives`）。
- [R2] AI 營收對 capex 缺口巨大：年化 AI 終端營收約 1,050 億美元，對比 top-4 年化 capex 約 7,250 億美元（2026-08-17／2026-07-28），市場已開始加強審視 capex（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`）。
- [R1] 投機與集中度仍處高檔：前十大成分股約占 S&P 500 的 38%（2026-09-01），SPX 0DTE 占比創紀錄約 62%（2026-08 月資料），margin debt 約 1.42 兆美元（2026-07 月資料）（`breadth.top10_concentration`、`structural.zero_dte`、`retail.margin_debt`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.21%（2026-09-11 收盤 29368.44，高點 30660.6），距 R1 門檻水位 22995.45 還要再跌約 21.70%；在 182 天窗口內出現這種幅度的下跌並不常見（`valuation.ndx_drawdown`）。
- [R3] 信用市場沒有壓力：High Yield OAS 2.70%、Investment Grade OAS 0.80%（2026-09-10），AI 相關借款人的再融資管道仍然暢通（`monetary.hy_oas`、`monetary.ig_oas`）。
- [R2] 四大 hyperscaler 2026 年 capex 合計約 7,250 億美元（2026-07-28），現有證據中沒有任何一家下修，距 R2 要求的兩家下修還很遠（`ai.hyperscaler_capex`）。
- [整體] 融資市場平穩：SOFR−IORB −3bp、SOFR99−IORB +5bp（2026-09-10），SRF 動用 0（2026-09-11）；OFR tri-party repo transaction volume 2271.6 十億美元（`monetary.repo_stress_srf`、`structural.treasury_basis_trade`）。
- [R2] AI 需求面仍然穩健：Anthropic 年化 run-rate 約 650 億美元（2026-08-17），H100 中位租金約每小時 3.38 美元（2026-08-31），沒有算力過剩的證據（`ai.openai_anthropic_revenue`、`ai.compute_supply_demand`）。
- [R1] 情緒偏謹慎而非亢奮：CNN Fear & Greed 約 35（恐懼，2026-09-10），AAII 看多約 38.0%（2026-09-10），單一個股槓桿 ETF 本週淨流出 7.51 億美元，規模約 407.4 億美元（2026-09-08）（`retail.fear_greed`、`retail.aaii`、`structural.leveraged_etf_aum`）。

## 與前期比較

前次結論：無前次預測（report-2026-09-03 為舊格式評分報告）

前次為舊格式評分報告，沒有 yes/no 結論可以比較，flip_evidence 為空。自 2026-09-03 以來的主要變化：10Y 殖利率 +18.0bp 到 4.95%；WTI +5.09% 到 97.26 美元；MOVE 自 74.68 升到 82.21；FRED VIXCLS 自 14.32 升到 17.84（僅作背景）；High Yield OAS +5bp 到 2.70%；NASDAQ-100 回撤維持在 4.21% 的低檔。10Y 本次 Δ 分解：ΔDGS10 +18.0bp、ΔDFII10 +13.0bp、ΔT10YIE +1.0bp，判讀為 `不可判（視窗不一致）`。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `valuation.sp500_trend`：腳本的 `sp500_trend` 區塊 fetch_failed，本次證據也沒有 S&P 500 現價的搜尋結果，因此現價與趨勢偏離都不可用，本週趨勢偏離不可用——無日序資料。這只影響估值延伸程度的輔助判讀；R1 以 NASDAQ-100 回撤直接量測，而且 4.21% 的回撤離門檻很遠，這個缺口不會改變結論。
- `structural.vix_spx_comove`：受 `sp500_trend` 失敗影響，`vix_spx_comove` 區塊為 unavailable（comove=false，沒有可重現的共同視窗）。FRED VIXCLS 本身已取得（17.84，2026-09-10），只是沒有 S&P 500 的對應腿，無法判讀共動。這屬於擁擠選擇權的確認訊號，不會改變結論。

最大的不確定性：

1. 9/16 FOMC：若照市場預期升息，而且長端利率繼續上行，R1 的估值重定價風險會升高，推向 yes；若暫停升息，推向 no。
2. 下一輪 hyperscaler 季報（落在窗口內，具體日期未在本次證據中）：若兩家以上下修 capex，會直接觸發 R2，而且本次證據缺少逐家指引，這是 R2 判讀的主要盲點。
3. AI 信用定價：AI 信用定價分歧、私募信貸贖回壓力、hyperscaler 融資結構 event scan 本次都沒有窗內披露；若 AI 借款人利差開始走闊，R3 與 R1 的傳導風險會上升，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29368.44 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 4.21 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2，%） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（%） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（%） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.7 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 5.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.8 | FRED API (series_id=BAMLC0A0CM) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.95 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | 18.0 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.55 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | 13.0 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.36 | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | 1.0 | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（美元） | 97.26 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO chg_pct | 5.09 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-08 月資料） | 3.35 | FRED API (series_id=CPIAUCSL) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.32 | FRED API (series_id=T5YIFR) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（%，Kim-Wright） | 0.8892 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7d） | 1.4 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API (series_id=SOFR99) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-09-13 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（十億美元，SRF 動用） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,740,619（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,912,178（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,446,620（¥644.66T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest（共動區塊 unavailable，僅水位） | 17.84 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2027.9777（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -6863118 | CFTC TFF futures-only | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 387809 | CFTC TFF futures-only | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 82.21 | Yahoo Finance chart API (^MOVE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index prior | 74.68 | Yahoo Finance chart API (^MOVE) | 2026-09-03 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2271.6 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（multpl / GuruFocus） | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED（搜尋完成，無同季合格上修） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500 日序） | ⛔ FETCH FAILED（sp500_trend fetch_failed；本次無 S&P 500 現價搜尋結果） |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✗ NOT DISCLOSED（搜尋完成，無窗內披露） |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight vs cap-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED（無顯著討論） |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED（無當期週值） |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM | WebSearch | ✗ NOT DISCLOSED（無新一期調查） |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED（無窗內披露） |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（沿用最近一季指引） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✗ NOT DISCLOSED（無合格披露） |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch（quarterly_state 沿用；event_scan 30d 搜尋完成，無窗內事件） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch＋既有 bullets 組合（分母 top-4） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED（無窗內變動） |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch（兩組件皆搜尋完成，無可用披露） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days（AI rename / SPAC） | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✗ NOT DISCLOSED（無窗內 S-1 或具名報導） |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR＋WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED（窗內無英文披露） |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ⛔ FETCH FAILED（VIXCLS ok；vix_spx_comove unavailable，sp500_trend 失敗） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo；artifact 三區塊皆 ok） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.73（原定 multpl / GuruFocus） | S&P 500 Shiller CAPE ratio current September 2026 multpl | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | Magnificent 7 forward P/E valuation September 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html（CNBC） | 2026-08-03 | 2026-09-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 至 7 月止 YTD 報酬約 13% | RSP equal weight vs SPY S&P 500 YTD performance September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.top10_concentration | 前十大集中度約 38% | S&P 500 top 10 concentration percentage September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 200 日均線之上約 53% | market breadth advance decline new highs lows September 2026 percent stocks above 200-day | https://condoredge.com/stocks/market-breadth（Condor Edge） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 35（恐懼） | CNN Fear and Greed Index today September 2026 reading | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）約 1.42 兆美元 | FINRA margin debt August 2026 record year over year | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026（Advisor Perspectives，原定 FINRA） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.0% | AAII sentiment survey results week September 10 2026 bullish bearish neutral | https://www.aaii.com/sentimentsurvey（AAII） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.71 | Treasury auction results September 2026 tail bid-to-cover 10-year | https://thevaultreport.com/treasury-auctions（The Vault Report） | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.fedwatch | 9/16 FOMC 升息 25bp 機率約 85.5% | CME FedWatch September 12 2026 probability 25 basis point hike | https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html（Yahoo Finance，原定 CME FedWatch） | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate financing 2026 total social financing | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm（SteelOrbis） | 2026-08-15 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 7,250 億美元（2026 年 7 月財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 650 億美元 | OpenAI Anthropic annualized revenue run rate September 2026 | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| ai.compute_supply_demand | H100 中位租金約每小時 3.38 美元 | GPU rental price HBM DRAM contract price September 2026 utilization | https://www.thundercompute.com/blog/ai-gpu-rental-market-trends（Thunder Compute） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 增額債務占 capex 約 32%（沿用最近一季，背景） | hyperscaler capex vs free cash flow debt issuance 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 1,050 億美元（分母 top-4 capex 約 7,250 億美元） | AI revenue vs capex gap 2026 annualized run rate | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement September 7-13 2026 | 檢查來源：SPACInsider、Businesswire SPAC newsroom、Boardroom Alpha（窗內無合格事件） | — | 2026-09-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 22 檔 | IPO priced week September 8 2026 first day return debut | https://www.iposcoop.com/current-year-pricings/（IPOScoop） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（0 件，兩個以上主題疊加弱基本面的條件皆未達） | biggest stock gainers week September 7 2026 microcap 100% quantum AI | 檢查來源：Finviz、Benzinga、StockTitan、Yahoo movers（Tenon +77%、AEON +35% 皆未達門檻） | — | 2026-09-13T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 14 日掃描（0 件合格：唯一 EDGAR 結果沒有可確認的交易日與申報日組合，不計入） | insider selling Form 4 September 2026 Nvidia AI executives SEC filing | 檢查來源：SEC EDGAR Form 4、WebSearch | — | 2026-09-13T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 約 0.67 | Cboe equity put call ratio September 2026 reading | https://www.thetrading.tools/put-call-ratio（thetrading.tools，原定 Cboe） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 407.4 億美元（淨流出 7.51 億美元） | leveraged ETF assets under management September 2026 record single stock | https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/（ETF Action） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval September 2026 | 檢查來源：SEC EDGAR、ETF.com 新上市 feed（窗內無合格核准或上市） | — | 2026-09-13T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 占比創紀錄約 62%（2026-08 月資料） | 0DTE options share SPX volume September 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.options_volume | OCC 8 月總結算量約 14.4 億口（2026-08 月資料） | OCC options volume August 2026 monthly report | https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/（Traders Magazine） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 收在約 17 以上、call skew 位於第 91 百分位 | fear gauge VIX hedges September 10 2026 volatility | https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html（CNBC） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率的分子約 1.42 兆美元（2026-07 月資料，僅交叉確認） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php（Current Market Valuation） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Qualcomm 給 Amazon 約 40 億美元認股權證（資料中心基礎設施交易） | Qualcomm warrants Amazon 4 billion AI infrastructure deal September 2026 | https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html（CNBC） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |

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

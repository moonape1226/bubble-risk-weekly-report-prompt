> [DRY RUN] this report was not committed to archive.
# 2026-09-03 AI 泡沫破裂預測報告
報告日期：2026-09-03｜ISO 週次：2026-W36｜預測窗口：2026-09-03 → 2027-03-04｜前次基準：report-2026-08-31（3天前）

## 結論

**結論：no**

三條路徑都離觸發條件很遠：NASDAQ-100 距 52 週高點回撤 4.95%，還需再跌約 21.10% 才達 R1 門檻（`valuation.ndx_drawdown`）；HY OAS 2.65%、IG OAS 0.81% 仍屬緊縮水位（`monetary.hy_oas`、`monetary.ig_oas`），且 CoreWeave 於 2026-08-10 仍完成約 2.6 十億美元融資（`structural.ai_infrastructure_debt`），R2 也沒有任何一家 hyperscaler 下修 capex 的證據。高估值與偏恐懼情緒顯示泡沫脆弱度高，但本次沒有看到能在 182 天內把任一路徑推過門檻的觸發與傳導證據。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,143.33（2026-09-02），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 4.95%。R1 門檻水位為 22,995.45，自最新收盤須再下跌約 21.10% 才會觸發（`valuation.ndx_drawdown`）。同期 S&P 500 收 7,666.6（2026-09-02），高於 200 日均線 7.5%、高於 52 週均線 8.89%，自前次基準日（2026-08-31，7,686.14）小跌 0.25%（`valuation.sp500_trend`）。估值仍處極端區：Shiller CAPE 約 41.6（2026-08-31，`valuation.sp500_pe_cape`）。但市場情緒已先行降溫：CNN Fear & Greed 33.8（恐懼，2026-09-02，`retail.fear_greed`），AAII 看多 32.9%（2026-08-28，`retail.aaii`），S&P 500 成分股站上 50 日均線比例約 54%（2026-08-27，`breadth.advance_decline`）。VIX 16.34（2026-09-01），7 日窗口（2026-08-25 → 2026-09-01）VIX +5.76%、S&P 500 −0.6%，未出現股價與波動同漲的 crowded-optionality 讀數（`structural.vix_spx_comove`）。

**判讀：** R1 距門檻仍有約 21% 的跌幅空間，在無信用或資金面傳導的情況下，182 天內完成 25% 回撤需要一次明確的衝擊（例如 Q3 財報季 capex 敘事轉向、利率再度急升或 AI 信用事件外溢）；目前位置偏離 200 日均線 7.5% 只代表回檔風險，不代表破裂已在進行。

### R2 資本支出收縮

最新可得的 hyperscaler capex 證據為 CNBC 2026-07-28 報導：Microsoft、Alphabet、Amazon、Meta 四家 2026 年 capex 合計約 725（十億美元）（`ai.hyperscaler_capex`，2026 Q2 財報季）。該來源只給合計，未逐家列出指引數值，因此四家各自的最新指引數值與相較前次指引的方向本次無法逐家確認：Microsoft —（方向未能確認）、Alphabet —（方向未能確認）、Amazon —（方向未能確認）、Meta —（方向未能確認）。已取得的證據中沒有任何一家下修，目前已下修家數為 0。同篇報導標題指出 Alphabet 財報後 hyperscaler capex 受到更高審視。需求側：Anthropic 年化 run-rate 約 650 億美元（2026-08-17，`ai.openai_anthropic_revenue`）。下一次正式指引節點為 2026 年 Q3 財報季，落在預測窗口內，確切日期本次證據未載。

**判讀：** R2 需要四家中兩家在窗口內正式下修指引，目前零家下修，且終端 AI 營收仍在成長；唯一可能推動 R2 的是 Q3／Q4 財報季的投資人壓力（capex scrutiny）轉為公司主動縮減，本次沒有證據顯示這已開始。

### R3 AI 信用事件

符合 R3 規模門檻（負債 ≥ 50 億美元、以 AI 資料中心／算力為主業）的借款人中，本次唯一有當期證據的是 CoreWeave：2026-08-10 SEC 8-K 附件新聞稿顯示其完成約 2.6 十億美元的融資（`structural.ai_infrastructure_debt`），代表其仍可進入債務市場，並無付款違約、寬限期或 distressed exchange 的訊號。廣義信用定價仍緊：HY OAS 2.65%（2026-09-01，較前次 +2 bps，`monetary.hy_oas`），IG OAS 0.81%（`monetary.ig_oas`）。銀行對 NBFI 放款 2,026.2859 十億美元（$2.03T，2026-08-19，`structural.nbfi_bank_loans`）。repo 資金壓力（SOFR−IORB）為 1 bp、SOFR99−IORB 9 bps，SRF 動用（Standing Repo Facility usage）0（2026-09-01／2026-09-02，`monetary.repo_stress_srf`），資金市場沒有壓力。AI 發行人個別利差／CDS 與私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）本次均無當期披露（見資料缺漏）。

**判讀：** R3 需要一家大型 AI 基礎設施借款人在窗口內破產、違約或完成 distressed exchange；目前最大的 neocloud 借款人仍在成功融資、整體信用利差緊縮，近期再融資壓力與違約訊號均未出現，R3 是三條路徑中最遠的一條。

## 支持 yes 的證據

- [整體] 估值處於歷史極端：Shiller CAPE 約 41.6（2026-08-31），若觸發事件出現，下行幅度可能很大（`valuation.sp500_pe_cape`）。
- [R1] 投機性槓桿與短天期選擇權擁擠：SPX 0DTE 佔期權量於 2026 年 8 月創紀錄約 62%（2026-08-31，`structural.zero_dte`），Cboe SKEW 約 148.5、股債相關偏正（2026-08-31，`structural.cross_asset_derivatives`），一旦下跌容易被放大。
- [R1] 通膨與利率限制 Fed 緩衝空間：CPI YoY 3.3%（2026-07 月資料，`monetary.cpi_yoy`），WTI 由 87.03 升至 91.48 美元（+5.11%，2026-09-01，`monetary.wti`），10Y 殖利率 4.79%（2026-09-01，較前次 +4 bps，`monetary.dgs10`），10Y 期限溢價（term premium）0.8751%（2026-08-28，`monetary.term_premium`）。
- [R1] 情緒與市場廣度轉弱：CNN Fear & Greed 33.8（恐懼，2026-09-02，`retail.fear_greed`），成分股站上 50 日均線比例約 54%（2026-08-27，`breadth.advance_decline`），前十大集中度約 37.6%（2026-07-31，`breadth.top10_concentration`）。
- [R2] capex 審視升溫：CNBC 2026-07-28 報導 Alphabet 財報後 hyperscaler capex 受到更高審視，四家 2026 capex 合計約 725（十億美元）（`ai.hyperscaler_capex`）。
- [整體] 債市波動上升：MOVE 由 75.32 升至 79.71（2026-09-02，`structural.treasury_basis_trade`）。

## 支持 no 的證據

- [整體] 基準率：任一 182 天窗口內 R1–R3 均不發生是常態，而 NASDAQ-100 距 52 週高點回撤 4.95%，距 R1 門檻 22,995.45 還差約 21.10%（2026-09-02，`valuation.ndx_drawdown`）。
- [R3] 信用市場沒有重定價：HY OAS 2.65%、IG OAS 0.81%（2026-09-01，`monetary.hy_oas`、`monetary.ig_oas`），CoreWeave 於 2026-08-10 仍完成約 2.6 十億美元融資（`structural.ai_infrastructure_debt`）。
- [R2] 終端需求仍在擴張：Anthropic 年化 run-rate 約 650 億美元（2026-08-17，`ai.openai_anthropic_revenue`），已取得證據中四大 hyperscaler 沒有任何一家下修 capex 指引（`ai.hyperscaler_capex`）。
- [整體] 資金市場平穩：SOFR−IORB 1 bp、SRF 動用 0（2026-09-01／2026-09-02，`monetary.repo_stress_srf`），OFR tri-party repo transaction volume 2,309.3 十億美元（2026-09-02，`structural.treasury_basis_trade`）。
- [R1] 情緒已非亢奮：Fear & Greed 33.8 與 AAII 看多 32.9%（`retail.fear_greed`、`retail.aaii`）顯示部位已部分降溫；Mag 7 前瞻本益比低於 24（2026-08-03，`valuation.mag7_multiples`），龍頭估值並未同步極端化。

## 與前期比較

前次結論：無前次預測（report-2026-08-31 為舊格式評分報告）

前次為舊格式評分報告，不轉換為 yes/no，`flip_evidence` 為空。自 2026-08-31 以來的主要變化：10Y 殖利率 +4 bps 至 4.79%，WTI +5.11% 至 91.48 美元，MOVE 由 75.32 升至 79.71，HY OAS +2 bps 至 2.65%，S&P 500 自 7,686.14 小跌 0.25%。10Y 變動分解：ΔDGS10 +4 bps、ΔDFII10 0 bps、ΔT10YIE +3 bps，判讀為 `不可判（視窗不一致）`（T10YIE 窗口與另兩腿不同）。這些變化方向偏向風險上升，但幅度不足以改變三條路徑的距離。

## 資料缺漏與不確定性

⛔ FETCH FAILED 來源：

- breadth.rsp_spy：搜尋只取得 2026-06-10 的 RSP 對 SPY YTD 數據，不是當期快照，因此視為未取得當期值。此缺口不影響結論：市場廣度已有前十大集中度與 50 日均線比例兩項替代讀數，且 R1 判斷取決於 NASDAQ-100 的實際回撤距離。

其他未披露項目（✗ NOT DISCLOSED，不作為證據引用）：AI 信用定價分歧（equity-vs-credit schism）、私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）、hyperscaler 融資結構（capex vs FCF / 發債）、資本週期階段（capital cycle stage）、backlog 重複計算風險（RPO double-counting）、折舊年限變動（depreciation useful-life change）、美債標售需求（auction tail / bid-to-cover）、FedWatch、AI token volume（僅有 2026-05-20 舊季資料）等。其中 AI 發行人利差／CDS 與私募信貸贖回訊號是 R3 最直接的領先指標，缺漏使 R3 判讀主要依賴廣義 OAS 與 CoreWeave 融資事件；若這些來源出現明顯走闊或 gate proration / breach，會把答案推向 yes。insider Form 4 掃描結果為 0 件：一筆搜尋結果未載交易日，不符資格要求，不予引用。

主要不確定性：

1. 2026 Q3 財報季（窗口內）：若兩家以上 hyperscaler 在審視壓力下轉為下修 capex，R2 會直接成立並可能拖動 R1，推向 yes。
2. 利率與油價：WTI 升至 91.48 美元、CPI 3.3%，若通膨再加速迫使長端殖利率急升，估值壓縮可能放大 R1 下跌，推向 yes。
3. AI 基礎設施信用：缺少個別 AI 發行人利差數據，若 neocloud 再融資條件惡化而未被本次搜尋捕捉，R3 風險可能被低估，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7666.6 | FRED API (series_id=SP500) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 7.5 | FRED API (series_id=SP500) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.89 | FRED API (series_id=SP500) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（NASDAQ-100 最新收盤） | 29143.33 | FRED API (series_id=NASDAQ100) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-09-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.95 | FRED API (series_id=NASDAQ100) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q1 家戶股票配置 %） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-09-03T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.65 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.81 | FRED API (series_id=BAMLC0A0CM) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.79 | FRED API (series_id=DGS10) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.44 | FRED API (series_id=DFII10) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.34 | FRED API (series_id=T10YIE) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（美元／桶） | 91.48 | FRED API (series_id=DCOILWTICO) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.wti | DCOILWTICO chg_pct（較前次 %） | 5.11 | FRED API (series_id=DCOILWTICO) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料，%） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-09-03T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.33 | FRED API (series_id=T5YIFR) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 0.8751 | FRED API (series_id=THREEFYTP10) | 2026-08-28 | 2026-09-03T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.66 | FRED API (series_id=SOFR) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.74 | FRED API (series_id=SOFR99) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-09-03 | 2026-09-03T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,730,912（$6.73T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-26 | 2026-09-03T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,915,343（€5.92T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-28 | 2026-09-03T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,442,957（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-09-03T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.34 | FRED API (series_id=VIXCLS) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（7 日窗口終點） | 16.34 | FRED API (series_id=SP500 paired) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 5.76 | FRED API (series_id=SP500 paired) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -0.6 | FRED API (series_id=SP500 paired) | 2026-09-01 | 2026-09-03T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2026.2859（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-19 | 2026-09-03T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六個 UST 期貨合約槓桿基金淨部位，口） | -7,003,041 | CFTC TFF futures-only | 2026-08-25 | 2026-09-03T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 478,000 | CFTC TFF futures-only | 2026-08-25 | 2026-09-03T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 79.71 | Yahoo Finance chart API (^MOVE) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index prior | 75.32 | Yahoo Finance chart API (^MOVE) | 2026-08-31 | 2026-09-03T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2309.3 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-09-02 | 2026-09-03T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（gurufocus） | ✓ SEARCH-VERIFIED（僅 CAPE；P/E 未取得） |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch（CNBC） | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED（無同季合格 TP 上調） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✗ NOT DISCLOSED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ⛔ FETCH FAILED（僅得 2026-06-10 舊資料，無當期快照） |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch（P&I） | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch（StockCharts，50 日均線比例代理） | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch（CNN） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（Advisor Perspectives） | ✓ SEARCH-VERIFIED（2026-07 月資料沿用） |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch（AAII） | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py（DFEDTARU＋DFEDTARL） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch | ✗ NOT DISCLOSED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW＋JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（CNBC，Q2 財報季沿用） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED（僅 2026-05-20 前季資料） |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch（TechCrunch） | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✗ NOT DISCLOSED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch：quarterly_state（stock_of_state）＋event_scan（30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch（TechCrunch）＋既有 bullets 組合 | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch：quarterly_state（stock_of_state）＋event_scan（30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（Renaissance Capital） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（Finviz、Benzinga、StockTwits、Yahoo movers） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✗ NOT DISCLOSED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch（YCharts） | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch（Benzinga） | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報摘要） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（currentmarketvaluation） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（SEC EDGAR 8-K，30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）＋WebSearch 事件掃描 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok；WebSearch 無合格事件） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 41.6 | shiller cape sp500 september 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus；預定來源 multpl / GuruFocus） | 2026-08-31 | 2026-09-03T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | magnificent 7 forward pe august 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html（CNBC） | 2026-08-03 | 2026-09-03T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度約 37.6% | sp500 top 10 concentration 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/（Pensions & Investments） | 2026-07-31 | 2026-09-03T09:30:00+08:00 |
| breadth.advance_decline | 成分股站上 50 日均線比例約 54% | market breadth advance decline august 2026 | https://articles.stockcharts.com/article/mindfulinvestor-2026-08-weakening-market-breadth-could-signal-trouble-ahead/（StockCharts） | 2026-08-27 | 2026-09-03T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 33.8（恐懼） | cnn fear greed index september 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-09-02 | 2026-09-03T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-07 月資料）約 1.42 兆美元 | finra margin debt july 2026 | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026（Advisor Perspectives；預定來源 FINRA） | 2026-07-31 | 2026-09-03T09:30:00+08:00 |
| retail.aaii | AAII 看多 32.9% | aaii sentiment august 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-08-28 | 2026-09-03T09:30:00+08:00 |
| monetary.pboc | 社會融資規模約 22.25 兆人民幣（2026-07 資料） | pboc aggregate financing july 2026 | https://english.www.gov.cn/（中國政府網英文版） | 2026-08-15 | 2026-09-03T09:30:00+08:00 |
| ai.hyperscaler_capex | MSFT＋GOOGL＋AMZN＋META 2026 capex 合計約 725（十億美元），2026 Q2 財報季 | hyperscaler capex 2026 guidance | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-03T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 650 億美元 | anthropic annualized revenue august 2026 | https://techcrunch.com/2026/08/17/anthropics-annualized-revenue-surges-to-65b/（TechCrunch） | 2026-08-17 | 2026-09-03T09:30:00+08:00 |
| ai.revenue_capex_gap | 來源所載缺口約 105（單位未載明，不作量化引用）；可組合分子 Anthropic 約 65bn，分母 top-4 capex 約 725bn | ai revenue vs capex 2026 | https://techcrunch.com/2026/08/17/anthropics-annualized-revenue-surges-to-65b/（TechCrunch） | 2026-08-17 | 2026-09-03T09:30:00+08:00 |
| speculation.ai_rename_spac | The Arena Group 更名 Paradium.AI，新代號 PAAI（7 日內 1 件） | arena group paradium.ai PAAI ticker august 2026 | https://www.businesswire.com/news/home/20260828769258/en/The-Arena-Group-dba-Paradium.AI-Completes-Name-Change-Will-Trade-Under-New-Stock-Ticker-PAAI-Effective-August-31-2026（Business Wire） | 2026-08-31 | 2026-09-03T09:30:00+08:00 |
| speculation.ipo_heat | 美股 IPO YTD 約 105 件 | ipo market 2026 renaissance capital | https://www.renaissancecapital.com/IPO-Center/Stats（Renaissance Capital） | 2026-08-28 | 2026-09-03T09:30:00+08:00 |
| speculation.microcap_moonshots | 0 件符合（2+ 主題疊加且弱基本面） | microcap moonshot quantum ai aug 27 sep 3 2026 | 檢查來源：Finviz、Benzinga、StockTwits、Yahoo movers（量子族群屬較大市值） | — | 2026-09-03T09:30:00+08:00 |
| speculation.insider_form4 | 0 件合格（唯一結果未載交易日，不符資格要求） | nvidia mark stevens form 4 september 2026 | 檢查來源：SEC EDGAR Form 4 | — | 2026-09-03T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 約 0.54（日讀數） | cboe equity put call ratio august 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio（YCharts） | 2026-08-07 | 2026-09-03T09:30:00+08:00 |
| structural.leveraged_etf_aum | 槓桿 ETF 總 AUM 約 198（來源未載明單位） | leveraged etf aum 2026 record | https://www.benzinga.com/etfs/broad-u-s-equity-etfs/26/08/61419951/leveraged-single-stock-etf-closures-went-from-3-to-63-in-a-year-as-money-piles-into-nvidia-bets（Benzinga；預定來源 etf.com / ETFGI） | 2026-08-15 | 2026-09-03T09:30:00+08:00 |
| structural.us_single_stock_etf | 0 件（30 日內新品為主題型 2x，非單一個股） | single stock leveraged etf launch aug 2026 | 檢查來源：SEC EDGAR、ETF.com | — | 2026-09-03T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔期權量 2026 年 8 月創紀錄約 62% | spx 0dte share record august 2026 | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-31 | 2026-09-03T09:30:00+08:00 |
| structural.options_volume | OCC 2026-07 期權日均量約 71 百萬口 | occ july 2026 options volume | https://mondovisione.com/media-and-resources/news/occ-july-2026-monthly-volume-data-202686（Mondo Visione；預定來源 OCC） | 2026-07-31 | 2026-09-03T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 期限結構 contango、股債相關偏正、SKEW 約 148.5 | vix skew term structure august 2026 | https://www.thetrading.tools/skew-index（thetrading.tools；預定來源 Cboe） | 2026-08-31 | 2026-09-03T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-07 月資料）約 1.42 兆美元；對市值比率未取得 | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php（Current Market Valuation） | 2026-07-31 | 2026-09-03T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave 完成約 2.6 十億美元融資 | coreweave 2.6 billion loan covenant august 2026 | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000357/ex991pr.htm（SEC EDGAR 8-K 附件） | 2026-08-10 | 2026-09-03T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-09-03",
  "iso_week": "2026-W36",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-03-04",
  "prior_date": "2026-08-31",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 4.95,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

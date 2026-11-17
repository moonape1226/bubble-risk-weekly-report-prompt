> [DRY RUN] this report was not committed to archive.

# 2026-09-13 AI 泡沫破裂預測報告
報告日期：2026-09-13｜ISO 週次：2026-W37｜預測窗口：2026-09-13 → 2027-03-14｜前次基準：report-2026-09-03（10天前）

## 結論

**結論：no**

三條路徑都沒有已在進行中的證據：NASDAQ-100 距 52 週高點回撤僅 4.21%，距 R1 門檻仍需再跌約 21.70%（`valuation.ndx_drawdown`）；HY OAS 2.70%、IG OAS 0.80% 顯示信用市場未重定價（`monetary.hy_oas`、`monetary.ig_oas`），本次也沒有取得任何 hyperscaler 下修 capex 指引或 AI 基建借款人違約的證據。9/16 FOMC 升息預期（CME FedWatch 約 85.5%）與殖利率、油價上行是值得追蹤的催化劑，但尚不足以推翻「182 天內 R1–R3 均不發生」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

FRED `NASDAQ100` 最新收盤 29,368.44（2026-09-11）；252 個交易日最高收盤 30,660.60（2026-06-02）；距 52 週高點回撤 4.21%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，自最新收盤須再下跌約 21.70% 才會觸及。

催化劑與傳導：CME FedWatch 顯示 9/16 FOMC 升息 25bp 的市場隱含機率約 85.5%（2026-09-12，`monetary.fedwatch`），目前 Fed funds 目標區間 3.50%–3.75%（`monetary.fed_funds`）；CPI YoY 3.35%（2026-08 資料，`monetary.cpi_yoy`）、WTI 97.26 美元（2026-09-09，較前次 +5.09%，`monetary.wti`）限制了 Fed 以降息緩衝股市修正的空間。10Y 殖利率 4.95%（較前次 +18bp，`monetary.dgs10`），其中 10Y 實質殖利率 +13bp（`monetary.dfii10`）、10Y breakeven +1bp（`monetary.t10yie`）；因 T10YIE 與 DGS10/DFII10 視窗不一致，本次 Δ 分解判讀：不可判（視窗不一致）。估值面 Shiller CAPE 約 40.73（2026-09-01，`valuation.sp500_pe_cape`）、前十大成分股佔 S&P 500 約 38%（`breadth.top10_concentration`），代表若出現修正，跌幅可能放大。S&P 500 價格趨勢偏離：本週趨勢偏離不可用——無日序資料。

情緒面並非過熱：CNN Fear & Greed 約 35（恐懼區，2026-09-10，`retail.fear_greed`）、AAII 看多約 38.0%（2026-09-10，`retail.aaii`），VIX 收在約 17 以上、call skew 位於第 91 百分位（2026-09-10，`structural.cross_asset_derivatives`）——上檔選擇權需求仍高，但整體不是恐慌性去槓桿。

**判讀：** R1 距門檻尚遠（回撤 4.21% vs 25%），需要在 182 天內出現由升息衝擊、信用重定價或 AI 獲利預期崩落觸發的再跌約 21.70%；目前利率與油價上行是逆風，但沒有看到強制去槓桿或信用傳導的證據。

### R2 資本支出收縮

本次取得的最新資料為 2026-07-28 的 Q2 財報季彙總：Microsoft、Alphabet、Amazon、Meta 四家 2026 年 capex 指引合計約 725（摘錄數值，依語境為十億美元；`ai.hyperscaler_capex`），且報導焦點是市場對高 capex 的審視加嚴，而非公司下修指引。本次證據未提供逐家指引數值與相對前次指引的方向，因此逐家狀態如下：

- Microsoft：最新指引見 2026-07 財報季彙總；逐家方向本次未確立（未見下修證據）。
- Alphabet：最新指引見 2026-07 財報季彙總；逐家方向本次未確立（報導稱其財報遭市場負評，但未見下修指引證據）。
- Amazon：最新指引見 2026-07 財報季彙總；逐家方向本次未確立（未見下修證據）。
- Meta：最新指引見 2026-07 財報季彙總；逐家方向本次未確立（未見下修證據）。

已確認下修家數：0。窗口內（至 2027-03-14）預計包含下一輪 Q3（約 10 月底）與 Q4（約 1 月底至 2 月初）財報，具體日期本次未取得。需求端：Anthropic 年化 run-rate 約 65（2026-08-17，`ai.openai_anthropic_revenue`）；已披露年化 AI 終端營收約 105 vs 年化 capex 約 725（分母：top-4 hyperscaler，未含 Oracle 與 neocloud；`ai.revenue_capex_gap`），缺口仍大。供需面 H100 中位租金約 3.38 美元／小時（2026-08-31，`ai.compute_supply_demand`），本次未取得同步的利用率或庫存證據，無法判定為產能過剩。

**判讀：** R2 目前 0／4 已下修，需在窗口內兩輪財報中有兩家下修；AI 營收對 capex 缺口（revenue-to-capex gap）擴大與市場審視加嚴是壓力來源，但沒有任何一家已表態縮減，若 R1 先發生大幅回撤才較可能誘發下修。

### R3 AI 信用事件

本次 30 日掃描取得的 AI infrastructure debt financing / vendor-financing loops 事件為 Qualcomm 授予 Amazon 約 40 億美元認股權證的資料中心基建交易（2026-09-08，`structural.ai_infrastructure_debt`），屬於供應商與客戶間的 vendor-financing 型安排，而非借款人困境訊號。AI 信用定價分歧（equity-vs-credit schism）在 14 日窗內無合格報導；本次未取得任何符合 R3 規模門檻（負債 ≥ 50 億美元、以 AI 資料中心／算力為主業）之借款人的債券利差、CDS、評等行動、到期牆或困境訊號，相關借款人的總負債數字本次亦未確立。廣義信用環境：HY OAS 2.70%（+5bp，`monetary.hy_oas`）、IG OAS 0.80%（`monetary.ig_oas`），repo 資金壓力（SOFR−IORB）為 −3bp、SOFR99−IORB 5bp、SRF 動用 0（2026-09-10／09-11，`monetary.repo_stress_srf`），銀行對 NBFI 放款 $2.03T（2026-09-02，`structural.nbfi_bank_loans`）。

**判讀：** R3 無任何進行中的困境證據，信用利差處於緊縮水位；要在窗口內成立，需出現大型 neocloud／資料中心借款人的付款違約、破產或 distressed exchange，而目前連利差走闊的前導訊號都未取得。

## 支持 yes 的證據

- [R1] CME FedWatch 顯示 9/16 FOMC 升息 25bp 的市場隱含機率約 85.5%（2026-09-12），在 CPI YoY 3.35%（2026-08）與 WTI 97.26 美元（2026-09-09，+5.09%）下，Fed 緩衝股市修正的空間受限 `monetary.fedwatch` `monetary.cpi_yoy` `monetary.wti`
- [R1] 10Y 殖利率 4.95%（2026-09-10，較 2026-09-03 +18bp），10Y 實質殖利率 2.55%（+13bp），長端利率上行壓縮高估值成長股的折現空間 `monetary.dgs10` `monetary.dfii10`
- [整體] 估值與集中度處於高位：Shiller CAPE 約 40.73（2026-09-01）、前十大成分股約佔 S&P 500 38%（2026-09-01），一旦修正可能被放大 `valuation.sp500_pe_cape` `breadth.top10_concentration`
- [R2] 年化 AI 終端營收約 105 vs top-4 hyperscaler 2026 年 capex 約 725（2026-07-28／2026-08-17），AI 營收對 capex 缺口（revenue-to-capex gap）仍大，市場對 capex 的審視加嚴 `ai.revenue_capex_gap` `ai.hyperscaler_capex`
- [整體] 波動率與避險需求升溫：MOVE 82.21（2026-09-11，較前次 +7.53）、VIX 收在約 17 以上且 call skew 位於第 91 百分位（2026-09-10） `structural.treasury_basis_trade` `structural.cross_asset_derivatives`

## 支持 no 的證據

- [R1] NASDAQ-100 最新收盤 29,368.44（2026-09-11）距 52 週高點回撤僅 4.21%，距 R1 門檻 22,995.45 仍需再跌約 21.70% `valuation.ndx_drawdown`
- [R3] 信用市場未重定價：HY OAS 2.70%、IG OAS 0.80%（2026-09-10），repo 資金壓力（SOFR−IORB）−3bp、SRF 動用 0（2026-09-10／09-11） `monetary.hy_oas` `monetary.ig_oas` `monetary.repo_stress_srf`
- [R2] 四大 hyperscaler 2026 年 capex 指引合計約 725（2026-07-28 財報季），本次未見任何一家下修，已確認下修家數為 0 `ai.hyperscaler_capex`
- [整體] 情緒偏謹慎而非亢奮：CNN Fear & Greed 約 35（2026-09-10，恐懼）、AAII 看多約 38.0%（2026-09-10），不是典型頂部的狂熱讀數 `retail.fear_greed` `retail.aaii`
- [R3] AI 需求端持續擴張：Anthropic 年化 run-rate 約 65（2026-08-17），H100 中位租金約 3.38 美元／小時（2026-08-31），未見利用率崩落證據 `ai.openai_anthropic_revenue` `ai.compute_supply_demand`

## 與前期比較

前次結論：無前次預測（report-2026-09-03 為舊格式評分報告）

自 2026-09-03 以來的主要變化（僅供參考，不轉換舊格式評分）：

- 10Y 殖利率 4.77% → 4.95%（+18bp），實質殖利率 +13bp（`monetary.dgs10`、`monetary.dfii10`）。
- MOVE 74.68 → 82.21（`structural.treasury_basis_trade`）；HY OAS 2.65% → 2.70%（`monetary.hy_oas`）。
- WTI 92.55 → 97.26 美元（+5.09%，`monetary.wti`）。
- NASDAQ-100 回撤維持在 4.21% 的低位（`valuation.ndx_drawdown`）。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `valuation.sp500_trend`：`scripts/fetch_macro.py` 的 `sp500_trend` 區塊 fetch_failed，WebSearch 亦未取得 S&P 500 現貨水位；本週趨勢偏離不可用——無日序資料。此為估值／延伸度的輔助訊號，R1 由 NASDAQ-100 回撤直接量測，缺口不會改變結論。
- `structural.vix_spx_comove`：VIXCLS 本身取得，但 `vix_spx_comove` 區塊因 `sp500_trend` 缺失而 unavailable，無法判讀 VIX／S&P 500 同向上漲的 crowded-optionality 警戒；VIX 水位已由交叉資產來源覆蓋，缺口不太可能改變結論。

其他說明：搜尋紀錄稱美債基差交易槓桿的腳本三區塊 fetch_failed，但本次 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 皆為 `status: ok`，以 artifact 為準記為 `✓ API`。Insider Form 4 掃描找到一筆 2026-09-02 的 Form 4 結果，但僅顯示單一日期、未能分別確立申報日與交易日，不符合合格條件，故記為 0 件且不列名。逐家 hyperscaler capex 指引數值與方向、R3 規模門檻借款人的負債與信用定價本次均未確立。

最大不確定性：

1. 9/16 FOMC：若如市場預期升息且釋出更鷹派路徑，配合油價與殖利率上行，可能加速 R1 回撤（推向 yes）；若按兵不動或措辭溫和則推向 no。
2. Q3 財報季（約 10 月底）hyperscaler capex 指引：若有兩家下修即直接觸發 R2（推向 yes）；續上修則強化 no。
3. AI 基建借款人信用定價：本次 AI 信用定價分歧與私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）均無合格揭露，若後續出現利差走闊或 gate proration / breach，將提高 R3 與 R1 的連動風險（推向 yes）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.ndx_drawdown | ndx_drawdown latest（NASDAQ-100 最新收盤） | 29368.44 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.21 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（家庭股票配置 %，2026Q2 觀測） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5 | FRED API (series_id=DFEDTARL) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.7 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.8 | FRED API (series_id=BAMLC0A0CM) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.95 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | 18.0 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.55 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | 13.0 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.36 | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | 1.0 | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 97.26 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO chg_pct | 5.09 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-08 月資料） | 3.35 | FRED API (series_id=CPIAUCSL) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.32 | FRED API (series_id=T5YIFR) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright 10Y 期限溢價（term premium）） | 0.8892 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.62 | FRED API (series_id=SOFR) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.7 | FRED API (series_id=SOFR99) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-09-13 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6740619.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5912178.0（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6446620.0（¥644.66T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest（component 取得；vix_spx_comove 區塊 unavailable，不作證據） | 17.84 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2027.9777（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口數） | -6863118 | CFTC TFF futures-only | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 82.21 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2271.6（$2.27T） | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（gurufocus）[primary: SEARCH] | ✓ SEARCH-VERIFIED（CAPE；P/E 未取得） |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch（CNBC） | ✓ SEARCH-VERIFIED（前瞻 P/E；P/S 未取得） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500）＋WebSearch 現貨 fallback | ⛔ FETCH FAILED（sp500_trend fetch_failed；WebSearch 未取得現貨） |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✗ NOT DISCLOSED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight vs cap-weight | WebSearch（247wallst） | ✓ SEARCH-VERIFIED（RSP；SPY 未取得） |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch（247wallst） | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch（condoredge） | ✓ SEARCH-VERIFIED（% above 200-day 代理） |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（Advisor Perspectives） | ✓ SEARCH-VERIFIED（2026-07 月資料） |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch [primary: SEARCH] | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok、DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD） | ✓ API（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch [primary: SEARCH]（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok、JPNASSETS ok） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch [primary: SEARCH]（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（CNBC，Q2 財報季 carry-forward） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch（Axios） | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch [primary: SEARCH]；quarterly_state carry＋event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch [primary: SEARCH]＋capex bullet 分母 | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch [primary: SEARCH]（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch [primary: SEARCH]；quarterly_state carry＋event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days（AI rename / SPAC） | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（IPOScoop） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch [primary: SEARCH]（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✗ NOT DISCLOSED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR / WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch [primary: SEARCH]（etfaction） | ✓ SEARCH-VERIFIED（單一個股槓桿 ETF 合計；逐檔未取得） |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe insights） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC via Traders Magazine） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch（CNBC） | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove 區塊） | ⛔ FETCH FAILED（VIXCLS ok；vix_spx_comove unavailable，因 sp500_trend fetch_failed） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（currentmarketvaluation） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch [primary: SEARCH]（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo） | ✓ API（cftc_lev_funds ok、move_index ok、ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.73（原定來源 multpl / gurufocus） | S&P 500 Shiller CAPE ratio current September 2026 multpl | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | Magnificent 7 forward P/E valuation September 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html（CNBC） | 2026-08-03 | 2026-09-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 至 7 月止 YTD 報酬約 13% | RSP equal weight vs SPY S&P 500 YTD performance September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.top10_concentration | 前十大集中度約 38% | S&P 500 top 10 concentration percentage September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 200 日均線之上約 53% | market breadth advance decline new highs lows September 2026 percent stocks above 200-day | https://condoredge.com/stocks/market-breadth（Condor Edge） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 35（恐懼） | CNN Fear and Greed Index today September 2026 reading | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）約 1.42 兆美元 | FINRA margin debt August 2026 record year over year | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026（Advisor Perspectives／FINRA） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.0% | AAII sentiment survey results week September 10 2026 bullish bearish neutral | https://www.aaii.com/sentimentsurvey（AAII） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.71 | Treasury auction results September 2026 tail bid-to-cover 10-year | https://thevaultreport.com/treasury-auctions（The Vault Report） | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.fedwatch | 9/16 FOMC 升息 25bp 市場隱含機率約 85.5%（原定來源 CME FedWatch） | CME FedWatch September 12 2026 probability 25 basis point hike | https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html（Yahoo Finance） | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣（2026-07 累計） | PBoC aggregate financing 2026 total social financing | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm（SteelOrbis） | 2026-08-15 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 指引合計約 725（Q2 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65 | OpenAI Anthropic annualized revenue run rate September 2026 | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| ai.compute_supply_demand | H100 中位租金約 3.38 美元／小時 | GPU rental price HBM DRAM contract price September 2026 utilization | https://www.thundercompute.com/blog/ai-gpu-rental-market-trends（Thunder Compute） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 增額債務佔 capex 約 32%（背景；event_scan 30 日無揭露） | hyperscaler capex vs free cash flow debt issuance 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 105（分母取 ai.hyperscaler_capex top-4 約 725） | AI revenue vs capex gap 2026 annualized run rate | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement September 7-13 2026 | 檢查來源：SPACInsider、Businesswire SPAC newsroom、Boardroom Alpha（窗內無合格事件） | — | 2026-09-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 22 檔 | IPO priced week September 8 2026 first day return debut | https://www.iposcoop.com/current-year-pricings/（IPOScoop） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描（0 件符合 2+ 主題×弱基本面） | biggest stock gainers week September 7 2026 microcap 100% quantum AI | 檢查來源：Finviz、Benzinga、StockTitan、Yahoo movers（最大漲幅標的皆未達門檻） | — | 2026-09-13T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 14 日掃描（0 件合格：唯一結果未能分別確立申報日與交易日） | insider selling Form 4 September 2026 Nvidia AI executives SEC filing | 檢查來源：SEC EDGAR Form 4 檔案、WebSearch | — | 2026-09-13T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 約 0.67（日讀數或 5 日均值未標示） | Cboe equity put call ratio September 2026 reading | https://www.thetrading.tools/put-call-ratio（The Trading Tools） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.74（十億美元） | leveraged ETF assets under management September 2026 record single stock | https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/（ETF Action） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval September 2026 | 檢查來源：SEC EDGAR、ETF.com 新上市 feed（窗內無合格核准或上市） | — | 2026-09-13T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比約 62%（2026-08 月資料，創紀錄） | 0DTE options share SPX volume September 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.options_volume | OCC 總結算量約 1.44 十億口（2026-08 月資料） | OCC options volume August 2026 monthly report | https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/（Traders Magazine／OCC） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 收在約 17 以上、call skew 第 91 百分位 | fear gauge VIX hedges September 10 2026 volatility | https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html（CNBC） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 1.42 兆美元（2026-07 月資料；比率本身未取得） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php（Current Market Valuation） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Qualcomm 對 Amazon 認股權證約 40 億美元（vendor-financing 型安排） | Qualcomm warrants Amazon 4 billion AI infrastructure deal September 2026 | https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html（CNBC） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |

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
  "yes_basis": [],
  "r1_drawdown_pct": 4.21,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

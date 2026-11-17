> [DRY RUN] this report was not committed to archive.

# 2026-09-13 AI 泡沫破裂預測報告
報告日期：2026-09-13｜ISO 週次：2026-W37｜預測窗口：2026-09-13 → 2027-03-14｜前次基準：report-2026-09-03（10天前）

## 結論

**結論：no**

三條路徑都沒有已在進行中的跡象：NASDAQ-100 距 52 週高點回撤 4.21%，距 R1 門檻仍需再跌約 21.70%；四大 hyperscaler 2026 capex 合計約 725（十億美元）且本次證據未見任何下修。HY OAS 僅 2.70%，也沒有 AI 基建借款人出現困境訊號。利率上行與 9/16 FOMC 升息預期是真實的催化劑，但目前只顯示脆弱度，不足以證明 182 天內會完成破裂。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,368.44（2026-09-11），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 4.21%（前次 report-2026-09-03 為 4.95%，回撤反而收窄）。R1 門檻水位為 22,995.45，需自最新收盤再跌約 21.70% 才觸及（`valuation.ndx_drawdown`）。

同期背景：S&P 500 為 7,656.98（2026-09-11），高於 200 日均線 6.9%、高於 52 週均線 8.33%，自前次基準日起跌 1.17%（`valuation.sp500_trend`）。VIX 由 14.32 升至 17.84（+24.58%），同窗 S&P 500 跌 2.01%，屬於正常的股跌波動升，不是 crowded-optionality 的同漲讀數（`structural.vix_spx_comove`）。估值偏高：Shiller CAPE 約 40.73（`valuation.sp500_pe_cape`），前十大成分股佔 S&P 500 約 38%（`breadth.top10_concentration`）。情緒並不亢奮：CNN Fear & Greed 約 35，屬恐懼區（`retail.fear_greed`）；AAII 看多約 38.0%（`retail.aaii`）。

利率是主要的潛在催化劑：10Y 殖利率 4.95%，自前次 +18bp；實質殖利率 DFII10 2.55%，+13bp（`monetary.dgs10`、`monetary.dfii10`）；T10YIE 2.36%，+1bp（`monetary.t10yie`）。本次 Δ 分解判讀：不可判（視窗不一致），因 T10YIE 最新觀測日 2026-09-11 與 DGS10／DFII10 的 2026-09-10 不同。CME FedWatch 顯示市場對 9/16 FOMC 升息 25bp 的定價約 85.5%（`monetary.fedwatch`），而 CPI YoY 為 3.35%（2026-08 月資料，`monetary.cpi_yoy`），WTI 為 97.26 美元，自前次 +5.09%（`monetary.wti`）。通膨壓力限制了 Fed 緩衝 AI 主導回撤的空間。

**判讀：** R1 離觸發很遠（回撤 4.21% vs 門檻 25%）。窗口內要推過門檻，需要一次升息週期擴大（9/16 FOMC 起）引發的實質利率衝擊、AI 獲利或 capex 敘事破裂，或 R3 信用事件外溢的連鎖反應；目前證據顯示壓力在累積，但尚未轉為趨勢性拋售。

### R2 資本支出收縮

本次檢索到的最新 hyperscaler capex 狀態為 CNBC 2026-07-28 的季報後彙整：Microsoft、Alphabet、Amazon、Meta 四家 2026 年 capex 合計約 725（十億美元），報導重點是市場對 capex 的檢視升溫（Alphabet 財報遭市場負評），而非指引下修（`ai.hyperscaler_capex`）。檢索結果沒有提供各公司個別的指引金額與相對前次指引的方向，因此本報告不逐家填寫上修／持平；在本次證據中，四家之中已下修者為 0 家。下一輪（Q3）季報預期落在窗口內，但確切日期未在本次證據中取得。

需求側仍在擴張：Anthropic 年化 run-rate 約 65（十億美元，2026-08-17，`ai.openai_anthropic_revenue`）。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 105（十億美元）vs 年化 capex 約 725（十億美元）（分母：top-4，Microsoft／Alphabet／Amazon／Meta；未含 Oracle 與 neocloud），缺口巨大，本次無新組件披露可判斷擴大或收斂（`ai.revenue_capex_gap`）。GPU 租金方面，H100 中位租金約 3.38 美元／小時（2026-08-31，`ai.compute_supply_demand`），單一價格點不構成利用率轉弱證據。

**判讀：** R2 未啟動。要在窗口內成立，需要兩家在 Q3 或 Q4 財報中把 2026／2027 capex 指引調低；營收對 capex 的巨大缺口是長期壓力，但目前披露仍是擴張，沒有任何一家已下修。

### R3 AI 信用事件

本次 30 日掃描到的 AI infrastructure debt financing / vendor-financing loops 事件：Qualcomm 對 Amazon 發行約 4（十億美元）認股權證，屬資料中心基礎設施合作（2026-09-08，`structural.ai_infrastructure_debt`）。這是供應商對客戶的股權誘因安排，屬循環融資型的結構風險，不是借款人困境。廣義信用仍很鬆：HY OAS 2.70%（+5bp），IG OAS 0.80%（−1bp）（`monetary.hy_oas`、`monetary.ig_oas`）。repo 資金壓力（SOFR−IORB）為 −3bp，SOFR99−IORB 為 +5bp（皆為 2026-09-10 同日觀測），SRF 動用（Standing Repo Facility usage）為 0.0（2026-09-11）（`monetary.repo_stress_srf`），沒有融資市場緊縮訊號。本次 AI 信用定價分歧掃描與私募信貸贖回壓力掃描均無窗內披露，因此沒有任何符合 R3 規模門檻（負債 ≥ 50 億美元）的 AI 基建借款人出現利差急升、違約、寬限期或 distressed exchange 的證據。

**判讀：** R3 未啟動。要在窗口內成立，需有大型 neocloud 或 AI 資料中心借款人出現再融資失敗或付款違約；目前信用利差與資金面都不支持這條路徑在近期完成，但信用端資訊缺口（見資料缺漏）使這條路徑最難排除。

## 支持 yes 的證據

- [R1] 利率與政策衝擊正在形成：10Y 殖利率 4.95%（+18bp）、實質殖利率 2.55%（+13bp，2026-09-10），CME FedWatch 對 9/16 升息定價約 85.5%（2026-09-12），在 CAPE 約 40.73 的估值下，貼現率上升是 R1 的最直接催化劑（`monetary.dgs10`、`monetary.dfii10`、`monetary.fedwatch`、`valuation.sp500_pe_cape`）。
- [整體] 通膨限制 Fed 緩衝空間：CPI YoY 3.35%（2026-08 月資料）、WTI 97.26 美元（+5.09%，2026-09-09），一旦 AI 股回撤，Fed 難以快速轉鬆（`monetary.cpi_yoy`、`monetary.wti`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）極大：年化 AI 終端營收約 105 vs 四大 hyperscaler capex 約 725（十億美元），且 2026-07-28 起市場對 capex 的檢視已升溫，是 R2 的結構性壓力來源（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`）。
- [R1] 市場集中度與波動上升：前十大佔 S&P 500 約 38%（2026-09-01），VIX 7 日升 24.58% 至 17.84、call skew 位於第 91 百分位（2026-09-10），MOVE 由 74.68 升至 82.21（2026-09-11），集中部位對衝擊更敏感（`breadth.top10_concentration`、`structural.vix_spx_comove`、`structural.cross_asset_derivatives`、`structural.treasury_basis_trade`）。
- [R3] 循環融資結構持續擴大：Qualcomm 對 Amazon 約 4（十億美元）認股權證（2026-09-08），供應商與客戶的資本糾纏增加日後信用傳導的路徑（`structural.ai_infrastructure_debt`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.21%（2026-09-11），較前次的 4.95% 收窄，距 25% 門檻仍需再跌約 21.70%；基準率下 182 天內出現 25% 回撤本就少見（`valuation.ndx_drawdown`）。
- [R3] 信用市場沒有重定價：HY OAS 2.70%、IG OAS 0.80%（2026-09-10），repo 資金壓力（SOFR−IORB）−3bp、SRF 動用 0.0，沒有任何資金或信用面的傳導跡象（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`）。
- [R2] 四大 hyperscaler 2026 capex 合計約 725（十億美元，2026-07-28），本次證據未見任何一家下修；需求端 Anthropic run-rate 約 65（十億美元，2026-08-17）仍在擴張（`ai.hyperscaler_capex`、`ai.openai_anthropic_revenue`）。
- [整體] 情緒並非亢奮頂部：CNN Fear & Greed 約 35（恐懼，2026-09-10）、AAII 看多約 38.0%（2026-09-10）、equity put/call 約 0.67（2026-09-01），未見典型泡沫末段的追高（`retail.fear_greed`、`retail.aaii`、`speculation.equity_put_call`）。
- [整體] 投機活動降溫：單一個股槓桿 ETF 資金流出（規模約 40.74，2026-09-08），7 日內 +AI 改名／SPAC 與 microcap moonshot 掃描皆 0 件，30 日內美國單一個股槓桿 ETF 核准／上市 0 件（`structural.leveraged_etf_aum`、`speculation.ai_rename_spac`、`speculation.microcap_moonshots`、`structural.us_single_stock_etf`）。

## 與前期比較

前次結論：yes（report-2026-09-03）
本次結論：翻轉
前次 forecast.json 沒有 `yes_basis` 欄位（在該欄位存在之前寫成），沒有可逐項延續的決定性理由；依規則，yes 每次都要重新證成。以下逐路徑說明為何本次不再支持 yes。
翻轉依據：
- R1：NASDAQ-100 回撤由前次的 4.95% 收窄為 4.21%，距 R1 門檻仍需再跌約 21.70%，市場路徑沒有朝觸發方向前進（`valuation.ndx_drawdown`）。
- R2：最新 capex 狀態（2026-07-28）為四家合計約 725（十億美元），本次證據未見任何一家下修，R2 需要的「兩家下修」毫無進展（`ai.hyperscaler_capex`）。
- R3／傳導：HY OAS 2.70%（2026-09-10）仍處於緊縮水位，信用端沒有開始重定價，因此 R1／R3 的傳導鏈在本次證據中不存在（`monetary.hy_oas`）。
- R3：30 日掃描僅見 Qualcomm 對 Amazon 的約 4（十億美元）認股權證安排（2026-09-08），沒有任何 AI 基建借款人困境、違約或 distressed exchange（`structural.ai_infrastructure_debt`）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

未取得窗內披露（✗ NOT DISCLOSED）的來源中，與答案最相關的是 valuation.ai_credit_schism 與 monetary.private_credit_liquidity：若真有 AI 發行人利差急升或私募信貸 gate proration / breach 而未被檢索到，R3 路徑的評估可能偏樂觀，這是可能改變答案的缺口。ai.hyperscaler_financing_mix 的 event_scan 與 ai.capital_cycle 兩個組件無窗內披露，不影響本次答案。

來源不一致註記：本次 WebSearch 紀錄將美債基差交易槓桿標為「script 三區塊 fetch_failed」，但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 三塊皆為 status ok。本報告以 deterministic macro artifact 為準，記為 ✓ API。

內線申報：檢索到 NVDA（CIK 0001045810）Form 4，申報日 2026-09-02，出售約 385 百萬美元；但檢索結果未揭露交易日，不符合具名引用要求，因此不在正文作為證據使用。

最大不確定性：
1. 9/16 FOMC 若升息且釋出更鷹派的路徑，實質殖利率持續上行可能觸發估值重定價，推向 yes（R1）。
2. 窗口內的 Q3（10 月下旬）與 Q4 hyperscaler 季報：若兩家以上下修 2026／2027 capex 指引，R2 直接成立，推向 yes；若持續上修，則強化 no。
3. 本次未取得的 AI 信用定價與私募信貸贖回資料：若後續出現大型 neocloud 再融資困難，R3 可能在窗口內啟動並外溢至 R1，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest | 7656.98 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 6.9 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 8.33 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct | -1.17 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest | 29368.44 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 4.21 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2 季資料） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5 | FRED API (series_id=DFEDTARL) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.7 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.8 | FRED API (series_id=BAMLC0A0CM) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.95 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | 18.0 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.55 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | 13.0 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.36 | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 97.26 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-08 月資料） | 3.35 | FRED API (series_id=CPIAUCSL) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.32 | FRED API (series_id=T5YIFR) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest | 0.8892 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.62 | FRED API (series_id=SOFR) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.7 | FRED API (series_id=SOFR99) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-09-13 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6740619.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5912178.0（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6446620.0（¥644.66T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 17.84 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 17.84 | FRED API (VIXCLS／SP500 共同時間軸) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 24.58 | FRED API (VIXCLS／SP500 共同時間軸) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -2.01 | FRED API (VIXCLS／SP500 共同時間軸) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2027.9777（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -6863118 | CFTC TFF futures-only | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | 387809 | CFTC TFF futures-only | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 82.21 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2271.6 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（multpl / gurufocus） | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED（無同季合格上調） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✗ NOT DISCLOSED（窗內無合格報導） |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（月頻 carry-forward） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED（無顯著討論） |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED（無當週值） |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED（無新一期調查） |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直接取得） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED（窗內無披露） |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（季頻 carry-forward） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✗ NOT DISCLOSED（無合格披露） |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch（quarterly_state carry；event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch（組合 carry-forward） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED（窗內無變動） |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch（quarterly_state carry；event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✗ NOT DISCLOSED（無 S-1 或具名來源） |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR／WebSearch（14d） | ✓ SEARCH-VERIFIED |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED（窗內無英文披露） |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS、vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.73（原定來源：multpl / gurufocus） | S&P 500 Shiller CAPE ratio current September 2026 multpl | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | Magnificent 7 forward P/E valuation September 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html（CNBC） | 2026-08-03 | 2026-09-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 至 7 月止 YTD 報酬約 13% | RSP equal weight vs SPY S&P 500 YTD performance September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.top10_concentration | 前十大集中度約 38% | S&P 500 top 10 concentration percentage September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 200 日均線之上約 53% | market breadth advance decline new highs lows September 2026 percent stocks above 200-day | https://condoredge.com/stocks/market-breadth（CondorEdge） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 35（恐懼） | CNN Fear and Greed Index today September 2026 reading | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）約 1.42 兆美元 | FINRA margin debt August 2026 record year over year | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026（Advisor Perspectives，原定來源 FINRA） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.0% | AAII sentiment survey results week September 10 2026 bullish bearish neutral | https://www.aaii.com/sentimentsurvey（AAII） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.71 | Treasury auction results September 2026 tail bid-to-cover 10-year | https://thevaultreport.com/treasury-auctions（The Vault Report） | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.fedwatch | 9/16 FOMC 升息 25bp 定價約 85.5% | CME FedWatch September 12 2026 probability 25 basis point hike | https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html（Yahoo Finance，原定來源 CME FedWatch） | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate financing 2026 total social financing | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm（SteelOrbis） | 2026-08-15 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 725（十億美元，Q2 季報後） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65（十億美元） | OpenAI Anthropic annualized revenue run rate September 2026 | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| ai.compute_supply_demand | H100 中位租金約 3.38 美元／小時 | GPU rental price HBM DRAM contract price September 2026 utilization | https://www.thundercompute.com/blog/ai-gpu-rental-market-trends（Thunder Compute） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 增額債務佔 capex 約 32% | hyperscaler capex vs free cash flow debt issuance 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 105（十億美元）；分母沿用 ai.hyperscaler_capex top-4 約 725 | AI revenue vs capex gap 2026 annualized run rate | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描：0 件合格事件 | AI company name change ticker SPAC announcement September 7-13 2026 | 檢查來源：SPACInsider、Businesswire SPAC newsroom、Boardroom Alpha | — | 2026-09-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 22 檔 | IPO priced week September 8 2026 first day return debut | https://www.iposcoop.com/current-year-pricings/（IPOScoop） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描：0 件符合 2+ 主題×弱基本面（Tenon +77%、AEON +35% 未達門檻） | biggest stock gainers week September 7 2026 microcap 100% quantum AI | 檢查來源：Finviz、Benzinga、StockTitan、Yahoo movers | — | 2026-09-13T09:30:00+08:00 |
| speculation.insider_form4 | NVDA Form 4 董事出售約 385 百萬美元（申報日 2026-09-02；交易日檢索結果未揭露） | insider selling Form 4 September 2026 Nvidia AI executives SEC filing | https://www.sec.gov/Archives/edgar/data/0001045810/000119903926000012/wk-form4_1788387031.xml（SEC EDGAR） | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 約 0.67（日讀數） | Cboe equity put call ratio September 2026 reading | https://www.thetrading.tools/put-call-ratio（thetrading.tools，原定來源 Cboe） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.74（來源標題：資金流出單一個股 ETF） | leveraged ETF assets under management September 2026 record single stock | https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/（ETF Action） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval September 2026 | 檢查來源：SEC EDGAR、ETF.com 新上市 feed | — | 2026-09-13T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比創紀錄約 62%（2026-08 月資料） | 0DTE options share SPX volume September 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.options_volume | OCC 總結算量約 1.44 十億口（2026-08 月資料） | OCC options volume August 2026 monthly report | https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/（Traders Magazine，原定來源 OCC） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 收在約 17 以上、call skew 第 91 百分位 | fear gauge VIX hedges September 10 2026 volatility | https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html（CNBC） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 1.42 兆美元（2026-07 月資料） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php（Current Market Valuation） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Qualcomm 對 Amazon 認股權證約 4（十億美元），資料中心基礎設施合作 | Qualcomm warrants Amazon 4 billion AI infrastructure deal September 2026 | https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html（CNBC） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |

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
  "prior_answer": "yes",
  "flip_evidence": ["valuation.ndx_drawdown", "ai.hyperscaler_capex", "monetary.hy_oas", "structural.ai_infrastructure_debt"],
  "yes_basis": [],
  "r1_drawdown_pct": 4.21,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

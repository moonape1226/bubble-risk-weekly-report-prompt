> [DRY RUN] this report was not committed to archive.

# 2026-09-13 AI 泡沫破裂預測報告

報告日期：2026-09-13｜ISO 週次：2026-W37｜預測窗口：2026-09-13 → 2027-03-14｜前次基準：report-2026-09-03（10天前）

## 結論

**結論：no**

三條路徑目前都沒有「已在進行中」的證據：NASDAQ-100 距 52 週高點回撤 4.21%，距 R1 門檻仍需再跌約 21.70%；四大 hyperscaler 2026 capex 合計指引約 $725bn、本次證據中未見任何一家下修（R2 為 0/4）；HY OAS 2.70%、IG OAS 0.80% 仍處緊縮水位，R3 規模門檻內無任何違約／distressed exchange 跡象。Fed 9/16 升息定價（FedWatch 約 85.5%）、油價與長端利率上行是真實的時序催化劑，但目前只見於波動率與利率，尚未傳導到信用或 capex，不足以推翻 182 天窗口的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,368.44（2026-09-11），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 4.21%；R1 門檻水位 22,995.45，自最新收盤還需再下跌約 21.70% 才觸及（`valuation.ndx_drawdown`）。S&P 500 收 7,656.98（2026-09-11），仍高於 200 日均線 6.90%、高於 52 週均線 8.33%，較前次基準 2026-09-03 下跌 1.17%（`valuation.sp500_trend`）。估值脆弱度高：Shiller CAPE 約 40.73（2026-09-01，`valuation.sp500_pe_cape`），前十大成分股佔 S&P 500 約 38%（`breadth.top10_concentration`），SPX 0DTE 佔比 8 月創紀錄約 62%（`structural.zero_dte`）。但短線情緒已偏謹慎而非亢奮：CNN Fear & Greed 約 35（恐懼，2026-09-10，`retail.fear_greed`），AAII 看多約 38.0%（2026-09-10，`retail.aaii`），equity put/call 約 0.67（2026-09-01，`speculation.equity_put_call`），單一個股槓桿 ETF 規模約 $40.74bn 且出現資金流出（2026-09-08，`structural.leveraged_etf_aum`）。VIX 在 7 天內由 14.32 升至 17.84（+24.58%），同期 S&P 500 −2.01%，屬正常的股跌波動升，非 crowded-optionality 共振（`structural.vix_spx_comove`）。

**判讀：** R1 距門檻還很遠（需再跌約 21.70%），且目前 NDX 的回撤幅度小。能在窗口內推過門檻的路徑是：Fed 9/16 若升息並釋出續升訊號、10Y 實質利率續升（本次 DFII10 已 +13bp 至 2.55%），對高 CAPE、高集中度的 AI 權值股做估值壓縮；或 R3／R2 事件反向觸發。目前沒有證據顯示這個過程已開始。

### R2 資本支出收縮

最新可得的官方指引是 2026-07 下旬 Q2 財報季：四大 hyperscaler（Microsoft、Alphabet、Amazon、Meta）2026 capex 合計約 $725bn（CNBC 2026-07-28，`ai.hyperscaler_capex`）。本次取得的證據為四家合計值，未逐家列出各自的指引數字與相對前次指引的方向；在 Microsoft、Alphabet、Amazon、Meta 任何一家，本次證據都沒有下修紀錄。已下修家數：0/4。同篇報導指出 Alphabet 財報後市場對 capex 審視升高，屬投資人壓力，不是公司下修。需求面仍在擴張：Anthropic 年化 run-rate 約 $65bn（Axios 2026-08-17，`ai.openai_anthropic_revenue`），H100 中位租金約 $3.38/小時（2026-08-31，`ai.compute_supply_demand`），未見租金崩落搭配利用率轉弱的組合。產業 AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 $105bn vs 年化 capex 約 $725bn（分母：top-4，Oracle 本次無可組合的季頻數字故不納入）（`ai.revenue_capex_gap`）。缺口巨大，是 R2 的中期壓力來源，但不是窗口內的下修訊號。窗口（至 2027-03-14）涵蓋兩輪季報（2026 年 Q3 與 Q4 財報季）；確切財報日期未在本次證據中確認。

**判讀：** R2 需要四家中兩家正式下修，目前為 0；最可能的觸發點是 Q4 財報季（2027 年 1–2 月）給出 2027 年指引時，若 R1 回撤已發生或融資成本顯著上升，才可能出現下修。現階段證據指向持續上修或持平，而非收縮。

### R3 AI 信用事件

本次 30 日窗內唯一的 AI infrastructure debt financing / vendor-financing loops 事件是 Qualcomm 對 Amazon 發行約 $4bn 認股權證、綁定資料中心基礎設施合作（CNBC 2026-09-08，`structural.ai_infrastructure_debt`），屬供應商以股權工具換取採購承諾的 vendor-financing 型安排，是循環融資的累積訊號，而非信用壓力。整體信用定價仍寬鬆：HY OAS 2.70%（+5bp，2026-09-10，`monetary.hy_oas`）、IG OAS 0.80%（−1bp，`monetary.ig_oas`）。repo 資金壓力（SOFR−IORB）為 −3bp、SOFR99−IORB +5bp（2026-09-10），SRF 動用（Standing Repo Facility usage）為 0（2026-09-11）（`monetary.repo_stress_srf`），融資市場沒有緊繃。本次 14 日掃描沒有找到 AI 發行人債券利差／CDS 的當期報導，30 日掃描也沒有找到私募信貸贖回事件或 hyperscaler 自身的新融資事件（見資料缺漏一節），因此無法對符合 R3 規模門檻（≥ USD 5bn 負債、以 AI 資料中心／算力為主業）的 neocloud 借款人給出當期利差或到期牆數字；本次證據中沒有任何此類借款人出現付款違約、covenant waiver、distressed exchange 或 going-concern 字樣。

**判讀：** R3 目前沒有任何前兆事件；HY OAS 處緊縮水位代表信用市場尚未替 AI 基建借款人重定價。推向 yes 需要：利率上行（10Y 4.95%）疊加 GPU 租金下滑造成 neocloud 再融資失敗，或大型 AI 客戶承諾落空導致現金流斷裂；這些在窗口內可能發生，但目前沒有可引證的跡象。

## 支持 yes 的證據

- [整體] 貨幣政策正轉向緊縮：CME FedWatch 顯示 9/16 FOMC 升息 25bp 的定價約 85.5%（2026-09-12），而 CPI YoY 3.35%（2026-08 月資料）、WTI $97.26（2026-09-09，較前次 +5.09%），代表 Fed 緩衝 AI 主導回撤的空間有限，是 R1 估值壓縮的最直接時序催化劑（`monetary.fedwatch`、`monetary.cpi_yoy`、`monetary.wti`）。
- [R1] 長端利率與債市波動同步上行：10Y 殖利率 4.95%（+18bp）、10Y 實質利率 2.55%（+13bp，2026-09-10），MOVE 由 74.68 升至 82.21（2026-09-11），VIX 7 日 +24.58% 至 17.84；高實質利率直接壓縮長存續期的 AI 權值股估值（`monetary.dgs10`、`monetary.dfii10`、`structural.treasury_basis_trade`、`structural.vix_spx_comove`）。
- [R1] 估值與集中度處極端水位，一旦下跌幅度會很大：Shiller CAPE 約 40.73（2026-09-01）、前十大成分股佔 S&P 500 約 38%（2026-09-01）、SPX 0DTE 佔比創紀錄約 62%（2026-08），S&P 500 仍高於 200 日均線 6.90%（`valuation.sp500_pe_cape`、`breadth.top10_concentration`、`structural.zero_dte`、`valuation.sp500_trend`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）巨大：年化 AI 終端營收約 $105bn vs 四大 hyperscaler 2026 capex 合計約 $725bn（分母：top-4），且 Alphabet 財報後市場對 capex 的審視升高，若回報遲遲不現，下修壓力會在 2027 年指引中浮現（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`）。
- [R3] vendor-financing 循環持續擴大：Qualcomm 對 Amazon 發行約 $4bn 認股權證以綁定資料中心合作（2026-09-08），這類以股權工具換取採購承諾的安排在循環中堆疊，週期反轉時會放大信用衝擊（`structural.ai_infrastructure_debt`）。

## 支持 no 的證據

- [整體] 基準率與距離：任意 182 天窗口內 R1–R3 都屬罕見事件；NASDAQ-100 距 52 週高點回撤 4.21%（2026-09-11），距 R1 門檻 22,995.45 還需再跌約 21.70%，目前沒有任何一條路徑已在進行中（`valuation.ndx_drawdown`）。
- [R3] 信用市場完全沒有重定價：HY OAS 2.70%、IG OAS 0.80%（2026-09-10），repo 資金壓力（SOFR−IORB）−3bp、SRF 動用為 0（2026-09-11），R3 所需的信用傳導目前不存在（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`）。
- [R2] capex 指引仍在高位擴張：四大 hyperscaler 2026 capex 合計約 $725bn（2026-07-28），本次證據中 0/4 下修；需求端 Anthropic 年化 run-rate 約 $65bn（2026-08-17）、H100 中位租金約 $3.38（2026-08-31），未見利用率崩落（`ai.hyperscaler_capex`、`ai.openai_anthropic_revenue`、`ai.compute_supply_demand`）。
- [R1] 情緒已偏恐懼、槓桿部位在減：CNN Fear & Greed 約 35（2026-09-10）、AAII 看多約 38.0%（2026-09-10）、equity put/call 約 0.67（2026-09-01），單一個股槓桿 ETF 出現資金流出、規模約 $40.74bn（2026-09-08）；缺乏亢奮頂部常見的單邊追價，降低了窗口內崩跌式回撤的條件（`retail.fear_greed`、`retail.aaii`、`speculation.equity_put_call`、`structural.leveraged_etf_aum`）。
- [整體] 投機行為篩檢本週無合格事件：+AI 改名／SPAC 7 日掃描 0 件、microcap thematic moonshot 0 件、美國單一個股槓桿 ETF 30 日核准／上市 0 件，與 1999／2021 頂部前的投機狂熱型態不符（`speculation.ai_rename_spac`、`speculation.microcap_moonshots`、`structural.us_single_stock_etf`）。

## 與前期比較

前次結論：無前次預測（report-2026-09-03 為舊格式評分報告）

本次為新格式下的第一次 yes/no 預測，`flip_evidence` 為 `[]`。自 2026-09-03 以來的主要證據變化：

- 利率與波動上行：10Y 殖利率 +18bp 至 4.95%、10Y 實質利率 +13bp 至 2.55%，MOVE +7.53 至 82.21，VIX 由 14.32 升至 17.84。10Y 分解：ΔDGS10 +18bp、ΔDFII10 +13bp、ΔT10YIE +1bp，判讀為不可判（視窗不一致）（T10YIE 最新觀測為 2026-09-11，與 DGS10／DFII10 的 2026-09-10 不同窗）。
- 市場小幅回落：S&P 500 −1.17%，NDX 回撤 4.21%。
- 信用持平：HY OAS +5bp、IG OAS −1bp，未出現擴大。
- 新增 Fed 升息定價（9/16 FOMC 約 85.5%）與 WTI +5.09%，是本次最重要的新增 yes 側催化劑，但尚未傳導到信用或 capex。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源檢索完成但無合格當期披露（✗ NOT DISCLOSED），對結論的影響：

- `valuation.ai_credit_schism`（14 日內無 AI 發行人利差／CDS 報導）：這是 R3 最直接的前導指標；若實際已有 neocloud 利差顯著走闊而未被搜尋到，可能低估 R3 風險。HY OAS 緊縮使這個可能性偏低，但這是本次最大的資料缺口。
- `monetary.private_credit_liquidity`（30 日內無贖回事件披露）：私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）若在季末（9 月底 tender）浮現，會是 R3 的傳導通道；目前無法判讀。
- `ai.hyperscaler_financing_mix`（quarterly_state 可得：增額債務約佔 capex 32%，2026-07-28；30 日 event_scan 無新融資事件）、`ai.capital_cycle`（兩組件皆無合格披露）、`ai.customer_concentration_rpo`、`ai.depreciation_life`、`ai.token_growth`：影響 R2 中期判讀，但不改變窗口內 0/4 下修的事實。
- `valuation.analyst_tp_decomposition`、`retail.social_sentiment`、`retail.naaim`、`institutional.bofa_jpm_survey`、`speculation.upcoming_ai_ipos`、`structural.global_leveraged_approvals`：情緒／投機佐證，缺漏不會改變結論。
- `speculation.insider_form4` 以 0 件計：搜尋命中 1 筆 SEC EDGAR Form 4（NVIDIA，2026-09-02），但證據中只有單一日期，未分列 filing date 與 transaction date，不符合可引用條件，故不引用具名內部人或金額。
- 證據紀錄與 macro artifact 有一處不一致：搜尋紀錄稱美債基差交易槓桿的三個 script 區塊 fetch_failed，但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 皆為 `status: ok`；本報告以 artifact 為準（✓ API）。
- 市場廣度資料不完整：RSP YTD 約 13% 為截至 7 月的數字，未附 SPY 對照；advance/decline 以「成分股在 200 日均線之上約 53%」作代理。

最大的不確定性：

1. 9/16 FOMC：若升息並釋出續升路徑，10Y 實質利率續升，會推動 R1 往 yes 方向；若僅一次性升息、市場解讀為控通膨，影響有限。
2. 油價與通膨：WTI $97.26、CPI 3.35% 若持續，壓縮 Fed 在 AI 回撤時的救市空間，往 yes 推。
3. Q4 財報季（2027 年 1–2 月）的 2027 年 capex 指引：是 R2 唯一在窗口內的主要決策點；若 R1 回撤先發生，下修機會上升，往 yes 推。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7656.98 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線） | 6.9 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線） | 8.33 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較前次基準） | -1.17 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29368.44 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.21 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2 季資料） | 48.2301354474（≈48.23%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-09-13T09:30:00+08:00 |
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
| monetary.wti | DCOILWTICO chg_pct | 5.09 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-08 月資料） | 3.35 | FRED API (series_id=CPIAUCSL) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.32 | FRED API (series_id=T5YIFR) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest | 0.8892 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.62 | FRED API (series_id=SOFR) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.7 | FRED API (series_id=SOFR99) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-09-13 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,740,619（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,912,178（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,446,620（¥644.66T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 17.84 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 17.84 | FRED API 衍生區塊 (VIXCLS／SP500 共同日序) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日） | 24.58 | FRED API 衍生區塊 (SP500 共同日序) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日） | -2.01 | FRED API 衍生區塊 (SP500 共同日序) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2027.9777（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約合計，口數） | -6863118 | CFTC TFF futures-only (UST 2Y/5Y/10Y/Ultra-10Y/Bond/Ultra-Bond) | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | 387809 | CFTC TFF futures-only | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 82.21 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index prior | 74.68 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-09-03 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo 交易量） | 2271.6 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（gurufocus / multpl） | ✓ SEARCH-VERIFIED（CAPE 取得；trailing P/E 未於結果中出現） |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch（CNBC） | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch（14d） | ✗ NOT DISCLOSED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch（247wallst） | ✓ SEARCH-VERIFIED（僅 RSP 至 7 月 YTD） |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch（247wallst） | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch（condoredge，200 日均線之上比例代理） | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch（cnn.com） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch（Advisor Perspectives，2026-07 月資料沿用） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | WebSearch（aaii.com） | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直接取得） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（repo_stress 區塊） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok，無新觀測） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing / liquidity operations | WebSearch（steelorbis） | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（Q2 財報季指引沿用） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch（Axios） | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch（thundercompute） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch（quarterly_state 沿用 CNBC 2026-07-28；event_scan 30d 無新融資事件） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch（Axios）＋capex guidance 組件 | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch（quarterly_state 與 30d event_scan 皆無合格披露） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch（SPACInsider、Businesswire、Boardroom Alpha） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（IPOScoop） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（Finviz、Benzinga、StockTitan、Yahoo movers） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✗ NOT DISCLOSED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR / WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch（etfaction） | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com 新上市 feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（KRX / TWSE / JPX / ESMA，7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe insights） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（Traders Magazine / OCC） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch（CNBC） | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove 區塊） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（currentmarketvaluation） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.73（原定來源 multpl / gurufocus） | S&P 500 Shiller CAPE ratio current September 2026 multpl | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | Magnificent 7 forward P/E valuation September 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html（CNBC） | 2026-08-03 | 2026-09-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 至 7 月止 YTD 報酬約 13% | RSP equal weight vs SPY S&P 500 YTD performance September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.top10_concentration | 前十大集中度約 38% | S&P 500 top 10 concentration percentage September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 200 日均線之上約 53%（A/D 代理） | market breadth advance decline new highs lows September 2026 percent stocks above 200-day | https://condoredge.com/stocks/market-breadth（Condor Edge） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 35（恐懼） | CNN Fear and Greed Index today September 2026 reading | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| retail.margin_debt | margin debt 約 1.42 兆美元（2026-07 月資料） | FINRA margin debt August 2026 record year over year | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026（Advisor Perspectives，原定來源 FINRA） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.0% | AAII sentiment survey results week September 10 2026 bullish bearish neutral | https://www.aaii.com/sentimentsurvey（AAII） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.71 | Treasury auction results September 2026 tail bid-to-cover 10-year | https://thevaultreport.com/treasury-auctions（The Vault Report） | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.fedwatch | 9/16 FOMC 升息 25bp 定價約 85.5% | CME FedWatch September 12 2026 probability 25 basis point hike | https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html（Yahoo Finance，原定來源 CME FedWatch） | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate financing 2026 total social financing | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm（SteelOrbis） | 2026-08-15 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 725（十億美元，Q2 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65（十億美元） | OpenAI Anthropic annualized revenue run rate September 2026 | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| ai.compute_supply_demand | H100 中位租金約 3.38（美元／小時） | GPU rental price HBM DRAM contract price September 2026 utilization | https://www.thundercompute.com/blog/ai-gpu-rental-market-trends（Thunder Compute） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 增額債務佔 capex 約 32% | hyperscaler capex vs free cash flow debt issuance 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 105（十億美元）；分母沿用 ai.hyperscaler_capex top-4 合計 | AI revenue vs capex gap 2026 annualized run rate | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描：0 件合格事件 | AI company name change ticker SPAC announcement September 7-13 2026 | 檢查來源：SPACInsider、Businesswire SPAC newsroom、Boardroom Alpha | — | 2026-09-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 22 檔 | IPO priced week September 8 2026 first day return debut | https://www.iposcoop.com/current-year-pricings/（IPOScoop） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描：0 件符合 2+ 主題×弱基本面（最大漲幅 Tenon +77%、AEON +35% 未達門檻） | biggest stock gainers week September 7 2026 microcap 100% quantum AI | 檢查來源：Finviz、Benzinga、StockTitan、Yahoo movers | — | 2026-09-13T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 14 日掃描：0 件合格（1 筆 EDGAR 命中未分列 filing／transaction date，不符引用條件） | insider selling Form 4 September 2026 Nvidia AI executives SEC filing | 檢查來源：SEC EDGAR（https://www.sec.gov/Archives/edgar/data/0001045810/000119903926000012/wk-form4_1788387031.xml） | — | 2026-09-13T09:30:00+08:00 |
| speculation.equity_put_call | equity put/call 約 0.67（日讀數） | Cboe equity put call ratio September 2026 reading | https://www.thetrading.tools/put-call-ratio（原定來源 Cboe） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.74（十億美元），資金流出約 $751m | leveraged ETF assets under management September 2026 record single stock | https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/（ETF Action） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval September 2026 | 檢查來源：SEC EDGAR、ETF.com 新上市 feed | — | 2026-09-13T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比創紀錄約 62%（2026-08） | 0DTE options share SPX volume September 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.options_volume | 8 月 OCC 總結算量約 1.44 十億口 | OCC options volume August 2026 monthly report | https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/（Traders Magazine，原定來源 OCC） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 收在約 17 以上、call skew 第 91 百分位 | fear gauge VIX hedges September 10 2026 volatility | https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html（CNBC） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 1.42 兆美元（2026-07 月資料） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php（Current Market Valuation） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Qualcomm 對 Amazon 認股權證約 4（十億美元），資料中心基礎設施合作（vendor-financing 型） | Qualcomm warrants Amazon 4 billion AI infrastructure deal September 2026 | https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html（CNBC） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |

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

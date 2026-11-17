> [DRY RUN] this report was not committed to archive.

# 2026-11-08 AI 泡沫破裂預測報告

報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：report-2026-10-18（21天前）

## 結論

**結論：no**

壓力自前次明顯升高，但三條路徑都還沒走到「窗口內大概率完成」：R1 NASDAQ-100 距 52 週高點回撤 13.56%，離 25% 門檻還要再跌約 13.23%；R2 目前只有 Microsoft 一家下修 capex 指引（約 175 → 約 170），還差一家，其餘三家本次沒有下修證據。R3 方面 CoreWeave 信用已進入困境定價（CDS 1289 bps、殖利率破 16%），但沒有違約、寬限期或 distressed exchange 跡象；同時 HY OAS 3.48% 顯示整體信用市場並未失序，所以本次不足以推翻「窗口內無事件」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 26,989.99（2026-11-06）。252 個交易日最高收盤是 31,224.69（2026-10-06），距 52 週高點回撤 13.56%。R1 門檻水位為 23,418.52，從最新收盤還要再跌約 13.23% 才會觸及（`valuation.ndx_drawdown`）。整個回落集中在一個月內：S&P 500 自前次基準（2026-10-16 收 7,659.44）至 2026-11-05 跌 3.99% 到 7,353.73，只比 200 日均線高 0.42%（`valuation.sp500_trend`）。VIX 升到 28.18（2026-11-05），前次為 19.99；過去 7 日 VIX 漲 63.84%、S&P 500 跌 4.75%，屬典型避險型下跌，不是 co-movement 警戒（comove=false）（`structural.vix_spx_comove`）。情緒已在恐慌區：CNN Fear & Greed 22（極度恐懼，2026-11-06）（`retail.fear_greed`），AAII 看空 48.4% 對看多 34.1%（2026-11-04）（`retail.aaii`），Cboe 股票賣買權比 1.05（2026-11-05）（`speculation.equity_put_call`）。估值仍高：Shiller CAPE 38.91、trailing P/E 25.14（2026-11-06）（`valuation.sp500_pe_cape`）。政策緩衝有限：FedWatch 隱含 12 月升息 25 bps 的定價約 76.8%（2026-11-06）（`monetary.fedwatch`），CPI YoY 3.72%（2026-09 月資料）（`monetary.cpi_yoy`）。

**判讀：** R1 已走了一半多一點，但剩下約 13% 的跌幅需要新催化劑才會完成，例如 12 月升息落地加上 AI 信用事件擴散，或下一輪 hyperscaler 財報讓 capex 敘事破裂。目前情緒已極度悲觀、put/call 偏高，短線反而常是反彈條件；窗口內觸及 R1 有可能，但本次證據不足以判斷大於一半。

### R2 資本支出收縮

- Microsoft：Q3 財報（2026-10-29）把 2026 年 capex 指引由約 175 下調到約 170（摘錄未標單位），屬下修（`ai.hyperscaler_capex`）。
- Alphabet：本次檢索沒有取得最新正式指引，方向不可判。
- Amazon：本次檢索沒有取得最新正式指引，方向不可判。
- Meta：本次檢索沒有取得最新正式指引，方向不可判。

目前四家中確認下修的只有一家（Microsoft），R2 還需要再一家。下一輪財報日期本次資料沒有確立；依季報節奏，窗口（至 2027-05-09）大致會涵蓋一到兩輪財報，但這是推估，不是已取得的日期。反方向證據是 hyperscaler 仍在大量發債：今年以來發債 296 billion，10/29 起一週內 5 筆 AI 相關債券合計 67 billion（2026-11-06）（`ai.hyperscaler_financing_mix`）。hyperscaler 融資結構（capex vs FCF / 發債）正轉向借債支撐 capex，而不是收縮 capex。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收 Anthropic 65 ＋ OpenAI 約 70，合計約 135（2026-09-30），分母本次只有 Microsoft 約 170（分母：僅 Microsoft，非全產業）。缺口方向本次無法判斷（`ai.revenue_capex_gap`）。

**判讀：** R2 已完成一半（1/2），是三條路徑中最接近的。但 Microsoft 的下修幅度很小（約 3%），其餘三家本次沒有任何下修證據，hyperscaler 仍在以債融資擴張。若下一輪財報再有一家下修就會解析為 yes；本次無法判斷這件事大於一半。

### R3 AI 信用事件

CoreWeave 是本次唯一有信用定價證據的 AI 基礎設施借款人：債券殖利率升破 16%（2026-11-06），五年期 CDS 突破 1289 bps（2026-11-05）（`valuation.ai_credit_schism`）。AI 信用定價分歧（equity-vs-credit schism）已從「信用與非 AI 無差」轉向信用端重定價。CoreWeave 的總負債本次沒有任何來源可確立，所以它是否滿足「負債 ≥ 50 億美元」的門檻本次不予斷言。AI infrastructure debt financing / vendor-financing loops 方面，ING 出售 12 筆資料中心貸款（規模約 500，摘錄未標單位，2026-11-06）（`structural.ai_infrastructure_debt`），顯示銀行在減少資料中心放款曝險。本次沒有任何借款人出現漏付、寬限期、covenant waiver、distressed exchange 或 going-concern 揭露。整體信用市場：HY OAS 3.48%（前次 3.31%，+17 bps）、IG OAS 0.93%（+8 bps）（`monetary.hy_oas`、`monetary.ig_oas`）。repo 資金壓力（SOFR−IORB）僅 2 bps，SOFR99−IORB 10 bps，SRF 動用（Standing Repo Facility usage）0（`monetary.repo_stress_srf`），沒有融資市場失序跡象。

**判讀：** CoreWeave 的困境級定價是本次最強的 yes 方向訊號，但 R3 需要的是破產、超過寬限期的違約或已完成的 distressed exchange，不只是寬利差。目前沒有到期牆或付款問題的已取得證據，負債規模門檻也未確立。窗口內若 CoreWeave 進行債務交換或重組就會觸發，本次證據不足以判斷大於一半。

## 支持 yes 的證據

- [R2] Microsoft 於 2026-10-29 Q3 財報把 2026 年 capex 指引由約 175 下調到約 170，R2 的兩家門檻已完成一家（`ai.hyperscaler_capex`）。
- [R3] CoreWeave 五年期 CDS 突破 1289 bps（2026-11-05）、債券殖利率升破 16%（2026-11-06），AI 信用端已進入困境定價（`valuation.ai_credit_schism`）。
- [R1] NASDAQ-100 距 52 週高點回撤 13.56%（2026-11-06），前次 forecast 時為 4.13%；一個月內回撤擴大三倍（`valuation.ndx_drawdown`）。
- [整體] Fed 緩衝受限：FedWatch 隱含 12 月升息 25 bps 定價約 76.8%（2026-11-06），CPI YoY 3.72%（2026-09 月資料），下跌中央行不太可能降息托底（`monetary.fedwatch`、`monetary.cpi_yoy`）。
- [R3] ING 出售 12 筆資料中心貸款（規模約 500，2026-11-06），銀行端正在減少 AI 資料中心放款曝險（`structural.ai_infrastructure_debt`）。
- [R1] 波動與避險急升：VIX 28.18（2026-11-05，前次 19.99），Cboe 偏斜指數 149.37、隱含相關性 20.93 創高（2026-11-06）（`structural.cross_asset_derivatives`、`structural.vix_spx_comove`）。
- [整體] 估值仍在極端區：Shiller CAPE 38.91、trailing P/E 25.14（2026-11-06），融資餘額約 1.48 兆美元、年增約 31.4%（2026-09 月資料）（`valuation.sp500_pe_cape`、`retail.margin_debt`）。

## 支持 no 的證據

- [整體] 基準率：任一 182 日窗口內 R1–R3 都不是常態；本次三條路徑都還沒完成，也沒有任何一條有「窗口內大概率完成」的具體證據。R1 還差約 13.23% 跌幅（門檻 23,418.52）（`valuation.ndx_drawdown`）。
- [R3] 整體信用沒有失序：HY OAS 3.48%、IG OAS 0.93%（2026-11-05），只溫和走闊 17 / 8 bps；repo 資金壓力（SOFR−IORB）2 bps、SRF 動用 0（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`）。
- [R2] hyperscaler 正以發債而不是砍 capex 應對：今年以來發債 296 billion，10/29 起一週 5 筆 AI 相關債券合計 67 billion（2026-11-06），市場仍在為擴張融資（`ai.hyperscaler_financing_mix`）。
- [R2] Microsoft 的下修幅度僅約 3%（約 175 → 約 170），其餘三家本次沒有下修證據；R2 還需要第二家（`ai.hyperscaler_capex`）。
- [R3] CoreWeave 雖然信用定價困境，但本次沒有漏付、寬限期、distressed exchange 或破產揭露；R3 要求實際信用事件（`valuation.ai_credit_schism`）。
- [R1] 情緒已在極度恐懼：Fear & Greed 22（2026-11-06）、AAII 看空 48.4%（2026-11-04）、股票 put/call 1.05（2026-11-05），屬反向指標中的超賣區，不是亢奮頂部（`retail.fear_greed`、`retail.aaii`、`speculation.equity_put_call`）。
- [整體] AI 需求端仍在擴張：Anthropic 遞交 S-1、目標估值 1.5 兆至 2 兆（2026-10-26），H100 隨選租金中位數 3.87（2026-11-03）（`speculation.upcoming_ai_ipos`、`ai.compute_supply_demand`）。

## 與前期比較

前次結論：yes（report-2026-10-18）

本次結論：翻轉

前次 forecast.json 沒有 `yes_basis` 欄位（寫於該欄位存在之前），所以沒有逐項必須回應的前次 yes 理由。依規則 yes 每次重新取得、不能沿用；本次自己的權衡未達 yes 的舉證門檻。

翻轉依據：

- `valuation.ndx_drawdown`：回撤由前次 4.13% 擴大到 13.56%，方向偏 yes，但仍只走了 25% 門檻的一半多一點，還需要約 13.23% 跌幅；它本身不能證明窗口內大概率完成。
- `ai.hyperscaler_capex`：R2 只有 Microsoft 一家小幅下修（約 175 → 約 170），其餘三家無下修證據，未達兩家門檻，也看不出第二家在窗口內大概率出現。
- `valuation.ai_credit_schism`：CoreWeave 定價已進入困境區，但 R3 要求實際破產／違約／distressed exchange，本次沒有任何這類跡象，借款人負債規模門檻也未在本次資料中確立。
- `monetary.hy_oas`：HY OAS 3.48% 只溫和走闊，沒有出現 R3 擴散到整體信用的傳導證據。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED（檢索完成、窗口內無合格揭露）：`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.treasury_auctions`、`monetary.private_credit_liquidity`、`ai.token_growth`、`ai.depreciation_life`、`ai.capital_cycle`（quarterly_state 無揭露；event_scan 取得微軟 10 月取消 Nscale 英國資料中心交易，規模約 3，2026-11-04，但複合狀態不成功，未作為正文證據）、`structural.global_leveraged_approvals`。其中私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）與美債標售需求（auction tail / bid-to-cover）若出現 gate proration / breach 或明顯 tail，會強化 R3／R1 傳導，但本次沒有揭露，不改變答案。

資料一致性備註：evidence 紀錄寫美債基差交易槓桿三個 script 區塊 fetch_failed、改走 WebSearch（MOVE 93.88，2026-11-04）；但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 皆為 status ok（MOVE 92.77，2026-11-06）。本報告以 macro artifact 為準，記為 ✓ API，WebSearch 值未採用。

`ai.hyperscaler_capex` 只取得 Microsoft 的指引；Alphabet、Amazon、Meta 的最新指引與方向本次未取得。這是可能改變答案的最大缺口：若其中任一家已在最近財報下修，R2 即已成立（答案會轉 yes）。下一輪 production run 必須優先補齊。

最大不確定性：

1. Alphabet／Amazon／Meta 的 capex 指引方向與下一輪財報日期：任一家下修就直接解析 R2 為 yes，偏向 yes。
2. CoreWeave 的負債規模、到期與再融資需求：本次沒有取得；若確認負債 ≥ 50 億美元且有近期到期牆，R3 會大幅接近，偏向 yes；若再融資順利，偏向 no。
3. 12 月 FOMC：升息落地加上 CPI 3.72% 會削弱政策托底，增加 R1 完成的可能，偏向 yes；若市場隱含升息定價回落，偏向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest | 7353.73 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 0.42 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 1.84 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（vs 前次基準） | -3.99 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 26989.99 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 13.56 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level | 23418.52 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026-Q2） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 4.0 | FRED API (series_id=DFEDTARU) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.75 | FRED API (series_id=DFEDTARL) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 3.48 | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 17.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.93 | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM delta_bps | 8.0 | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.84 | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | -25.0 | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.6 | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | -14.0 | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.23 | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | -12.0 | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 99.64 | FRED API (series_id=DCOILWTICO) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.17 | FRED API (series_id=T5YIFR) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.9089 | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.92 | FRED API (series_id=SOFR) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 4.0 | FRED API (series_id=SOFR99) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.9 | FRED API (series_id=IORB) | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6748145.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5945410.0（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6261882.0（¥626.19T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED API (series_id=VIXCLS) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（comove=false） | 28.18 | FRED API (series_id=VIXCLS, SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日窗，base 2026-10-29） | 63.84 | FRED API (series_id=VIXCLS, SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -4.75 | FRED API (series_id=VIXCLS, SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2111.0042（$2.11T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約合計） | -7249305 | CFTC TFF futures-only | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -489473 | CFTC TFF futures-only | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo Finance chart API (^MOVE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2326.9 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebFetch | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED（EPS／PE 拆解未揭露） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail / Margin Debt: FINRA | WebSearch（月頻 carry-forward） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail / Social sentiment proxies | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary / Fed funds rate: FRED | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary / High Yield OAS | scripts/fetch_macro.py | ✓ API |
| monetary.ig_oas | Monetary / Investment Grade OAS | scripts/fetch_macro.py | ✓ API |
| monetary.dgs10 | Monetary / 10Y Treasury yield | scripts/fetch_macro.py | ✓ API |
| monetary.dfii10 | Monetary / 10Y Treasury real yield | scripts/fetch_macro.py | ✓ API |
| monetary.t10yie | Monetary / 10Y breakeven inflation rate | scripts/fetch_macro.py（FRED 直取） | ✓ API |
| monetary.wti | Monetary / WTI crude oil price | scripts/fetch_macro.py | ✓ API |
| monetary.cpi_yoy | Monetary / CPI YoY: FRED | scripts/fetch_macro.py | ✓ API |
| monetary.t5yifr | Monetary / 5y5y forward inflation expectation | scripts/fetch_macro.py | ✓ API |
| monetary.term_premium | Monetary / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py | ✓ API |
| monetary.repo_stress_srf | Monetary / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary / 美債標售需求 | WebSearch（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary / Fed funds rate path expectations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary / Fed balance sheet: FRED | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | Monetary / Global central bank liquidity cross-check | scripts/fetch_macro.py | ✓ API（ECBASSETSW ok；JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED（僅取得 Microsoft） |
| ai.token_growth | AI / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration | WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構 | WebSearch（quarterly_state stock-of-state＋event_scan 30d） | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口 | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI / 資本週期階段 | WebSearch（quarterly_state stock-of-state＋event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculation / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | Speculation / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculation / Microcap thematic moonshots | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculation / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculation / Insider selling at AI | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculation / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural / 0DTE option volume | WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural / VIX / S&P 500 co-movement | scripts/fetch_macro.py | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural / Bank loans to nondepository financial institutions | scripts/fetch_macro.py | ✓ API |
| structural.treasury_basis_trade | Structural / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py 三區塊（aggregation any） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻本益比約 28.3 | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein TSMC 目標價 554 → 600（EPS／PE 拆解未揭露） | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/ | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 五年期 CDS 突破 1289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | 等權指數年初至今報酬約 14.13% | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | 前十大成分股權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 1,474 對下跌 1,252 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 22（極度恐懼） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 1.48 兆美元、年增約 31.4% | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔 | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | 12 月升息 25 bps 隱含定價 76.8% | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000 | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 capex 指引約 175 → 約 170（Q3 財報） | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3 | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle RPO 638（backlog 重複計算風險背景） | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87 | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 今年以來發債 296 billion | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 10/29 起一週 5 筆 AI 相關債券發行合計 67 billion | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 Anthropic 65 ＋ OpenAI 約 70，合計約 135（分母僅 Microsoft） | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] 微軟 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics 完成 SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO 週漲 8% | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描：0 件符合 2+ 主題×弱基本面 | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描：0 件合格 | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe 股票選擇權賣買權比 1.05 | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭基金 10 月底規模 24.31、當月淨流入 7.27 | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 9 月總結算量 1,486,062,415（2026-09 月資料） | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性創高 20.93 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 交叉檢核基數約 1.48 兆美元（2026-09 月資料） | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.ai_infrastructure_debt | ING 出售 12 筆資料中心貸款，規模約 500 | AI data center debt financing private credit November 2026 | https://www.cnbc.com/2026/11/06/ing-ai-data-center-loans-debt.html | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-11-08",
  "iso_week": "2026-W45",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-05-09",
  "prior_date": "2026-10-18",
  "prior_answer": "yes",
  "flip_evidence": ["valuation.ndx_drawdown", "ai.hyperscaler_capex", "valuation.ai_credit_schism", "monetary.hy_oas"],
  "yes_basis": [],
  "r1_drawdown_pct": 13.56,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

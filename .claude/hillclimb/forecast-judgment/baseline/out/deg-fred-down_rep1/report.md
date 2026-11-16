> [DRY RUN] this report was not committed to archive.
# 2026-11-08 AI 泡沫破裂預測報告
報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：report-2026-10-18（21天前）

## 結論

**結論：no**

三條路徑目前都沒有走到解析門檻：R2 只有 Microsoft 一家下修 capex 指引（約 175 → 約 170，`ai.hyperscaler_capex`），還需要第二家；R3 雖有 CoreWeave CDS 突破 1289 bps、債券殖利率升破 16% 的重定價（`valuation.ai_credit_schism`），但目前沒有付款違約、破產或 distressed exchange 的證據。R1 本次因 NASDAQ100 日序資料取得失敗而無法量測，這個缺口限制了判斷力，但不足以單獨支持 yes。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

R1 回撤不可用——腳本未取得 NASDAQ100 日序資料。由於 FRED API key 不存在，NASDAQ100 與 SP500 日序都未取得，本次無法計算距 52 週高點的距離，也無法算出 R1 門檻水位。間接的市場壓力讀數有：CNN Fear & Greed 為 22（極度恐懼，2026-11-06，`retail.fear_greed`）；Cboe 股票選擇權 put/call ratio 升至 1.05（2026-11-05，`speculation.equity_put_call`）；VIX 28.18、SKEW 149.37、隱含相關性 20.93 創高（2026-11-06，`structural.cross_asset_derivatives`）；AAII 看空 48.4% 高於看多 34.1%（2026-11-04，`retail.aaii`）。估值仍偏高：Shiller CAPE 38.91、trailing P/E 25.14（2026-11-06，`valuation.sp500_pe_cape`），Mag 7 前瞻 P/E 約 28.3（2026-10-13，`valuation.mag7_multiples`）。CME FedWatch 顯示 12 月升息 25 bps 的市場隱含機會為 76.8%（2026-11-06，`monetary.fedwatch`），10Y 殖利率 4.86%（2026-11-06，`monetary.dgs10`），WTI 95.97 美元（`monetary.wti`），對高估值科技股構成貼現率壓力。

**判讀：** 回撤距離未知。情緒與避險讀數顯示市場已處於壓力狀態，但沒有量化回撤就無法判斷離 25% 門檻有多近。要推過門檻，需要升息落地或 AI 信用事件外溢，在已偏高的估值上引發持續拋售。

### R2 資本支出收縮

- Microsoft：2026 年 capex 指引由約 175 下調至約 170（2026-10-29 季報，下修）（`ai.hyperscaler_capex`）。
- Alphabet：本次證據未載最新指引與方向，列為未提供指引。
- Amazon：本次證據未載最新指引與方向，列為未提供指引。
- Meta：本次證據未載最新指引與方向，列為未提供指引。

目前四家中已下修 1 家，還差 1 家。下一輪四家季報的確切日期未在本次證據中，但依季報節奏應落在窗口內（2027 年初）。融資面上，hyperscaler 今年以來發債約 296，10/29 起一週內 5 筆 AI 相關債券發行合計約 67（2026-11-06，`ai.hyperscaler_financing_mix`），顯示 capex 已轉向債務融資。AI 終端營收方面，Anthropic＋OpenAI 年化約 135（2026-09-30，`ai.revenue_capex_gap`），對照分母僅能涵蓋 Microsoft 的約 170 指引（分母：僅 Microsoft；其餘三家與 Oracle 本次無可用指引）。

**判讀：** 1/4 已下修，是本次最接近門檻的路徑。窗口內的下一輪季報只要再有一家正式下修就成立。目前可見的是 Microsoft 本身的收縮與融資轉向債務，其餘三家方向不明，所以還不能推定第二家會跟進。

### R3 AI 信用事件

可能符合規模門檻的借款人以 CoreWeave 為主：其債券殖利率升破 16%（2026-11-06），五年期 CDS 突破 1289 bps（2026-11-05）（`valuation.ai_credit_schism`）。本次證據未載其確切負債額，但它是主要的 AI 算力借款人。這是明確的信貸端重定價：信用市場正在對 AI 基建償債能力打折，標題也指出這發生在 Nasdaq 反彈之際，屬於 AI 信用定價分歧（equity-vs-credit schism）中「信貸先動」的後期型態。AI infrastructure debt financing / vendor-financing loops 方面，ING 出售 12 筆資料中心貸款，規模約 500（2026-11-06，`structural.ai_infrastructure_debt`），顯示銀行在降低 AI 資料中心曝險。本次證據沒有付款違約、寬限期、covenant waiver、distressed exchange 或 going-concern 字樣，也沒有具名的近期到期牆。

**判讀：** 信用定價已到困境區間，但尚未發生事件。要成立，需要 CoreWeave 或同級借款人在窗口內出現付款違約、破產申請或完成 distressed exchange；若再融資窗口關閉（升息、銀行出售曝險）就可能加速。目前仍是定價訊號，不是事件。

## 支持 yes 的證據

- [R3] CoreWeave 五年期 CDS 突破 1289 bps（2026-11-05），債券殖利率升破 16%（2026-11-06），信用市場已把 AI 算力借款人定價在困境區間 `valuation.ai_credit_schism`
- [R2] Microsoft 將 2026 年 capex 指引由約 175 下調至約 170（2026-10-29），R2 四家中已有一家下修，只差一家 `ai.hyperscaler_capex`
- [整體] 12 月升息 25 bps 的 CME FedWatch 隱含機會為 76.8%（2026-11-06），在 CAPE 38.91 的估值上施加貼現率與再融資壓力 `monetary.fedwatch` `valuation.sp500_pe_cape`
- [R3] ING 出售 12 筆資料中心貸款，規模約 500（2026-11-06），銀行端在縮減 AI 資料中心曝險，可能收緊 neocloud 再融資管道 `structural.ai_infrastructure_debt`
- [R1] 恐懼讀數集中：Fear & Greed 22（2026-11-06）、put/call 1.05（2026-11-05）、VIX 28.18 且隱含相關性 20.93 創高（2026-11-06） `retail.fear_greed` `speculation.equity_put_call` `structural.cross_asset_derivatives`
- [整體] hyperscaler 今年以來發債約 296、10/29 起一週 5 筆 AI 債券合計約 67（2026-11-06），capex 融資由現金流轉向債務，提高對信貸條件的敏感度 `ai.hyperscaler_financing_mix`

## 支持 no 的證據

- [整體] 基準率：任意 182 天窗口內 R1–R3 都不成立是常態；本次三條路徑都未達門檻（R2 只有 1/4，R3 無事件），R1 也沒有已觸發的證據 `ai.hyperscaler_capex` `valuation.ai_credit_schism`
- [R3] CDS 與殖利率是定價而非事件：本次證據中無付款違約、破產申請或 distressed exchange，信用重定價到實際違約通常需要再融資失敗 `valuation.ai_credit_schism` `structural.ai_infrastructure_debt`
- [R2] AI 需求面仍在擴張：Anthropic 上半年營收 16.3（2026-10-26），並遞交 S-1、目標估值 1.5 兆至 2 兆（2026-10-26），Anthropic＋OpenAI 年化終端營收約 135（2026-09-30），不利 hyperscaler 集體大幅縮手 `ai.openai_anthropic_revenue` `speculation.upcoming_ai_ipos` `ai.revenue_capex_gap`
- [R2] Microsoft 的下修幅度小（約 175 → 約 170，2026-10-29），屬微調而非撤退；Oracle RPO 仍有 638（2026-08-31），backlog 支撐產能需求 `ai.hyperscaler_capex` `ai.customer_concentration_rpo`
- [R1] 10Y 殖利率較前次基準下降 23 bps 至 4.86%（2026-11-06），其中 breakeven 貢獻 12 bps、實質利率 11 bps；MOVE 由 101.1 降至 92.77（2026-11-06），債市壓力在緩解 `monetary.dgs10` `monetary.dfii10` `structural.treasury_basis_trade`
- [整體] 情緒已處極度恐懼（Fear & Greed 22、AAII 看空 48.4%），歷史上多為反向訊號，不是泡沫頂部的狂熱型態 `retail.fear_greed` `retail.aaii`

## 與前期比較

前次結論：無前次預測（report-2026-10-18 為舊格式評分報告）

本次為新格式下的第一份預測，flip_evidence 為空。自 2026-10-18 以來的主要證據變化：10Y 殖利率由 5.09% 降至 4.86%（driver：breakeven）；WTI 由 99.93 降至 95.97；MOVE 由 101.1 降至 92.77；CFTC 槓桿基金美債期貨淨空單由 -6,796,358（2026-10-20）擴大至 -7,249,305（2026-11-03）；Microsoft 在 2026-10-29 下修 capex 指引；CoreWeave 信用定價在 2026-11 初急遽走闊。

## 資料缺漏與不確定性

⛔ FETCH FAILED 來源（FRED API key 不存在，導致下列 FRED 序列與衍生區塊全部失敗，本次證據中沒有 WebSearch 備援值）：

- `valuation.sp500_trend`：S&P 500 本週趨勢偏離不可用——無日序資料。屬估值延伸的輔助讀數，單獨不會改變答案。
- `valuation.ndx_drawdown`：R1 回撤距離不可用。**這是最大缺口，可能改變答案**：若 NASDAQ-100 實際已接近 25% 回撤，R1 可能已在門檻附近，答案應轉向 yes。在極度恐懼與 put/call 1.05 的背景下，不能排除回撤已相當大。
- `retail.household_equity_allocation`：季頻結構性背景，不會改變答案。
- `monetary.fed_funds`：政策利率水位缺失；路徑預期由 FedWatch 補足，不會改變答案。
- `monetary.hy_oas`、`monetary.ig_oas`：廣義信用利差缺失，無法確認 CoreWeave 的重定價是否已擴散到整體 HY。若 HY OAS 大幅走闊，會強化 R3／R1 的 yes 方向，**可能影響答案**。
- `monetary.cpi_yoy`、`monetary.t5yifr`、`monetary.term_premium`：通膨與期限溢價水位缺失，影響對 Fed 緩衝空間的判讀，屬間接影響。
- `monetary.repo_stress_srf`：SOFR、SOFR99、IORB、RPONTTLD 全部失敗，repo_stress 為 unavailable；OFR tri-party repo 成交量 2,326.9 可作部分替代，不太會改變答案。
- `monetary.walcl`、`monetary.ecb_boj`：央行資產負債表水位缺失，屬背景，不會改變答案。
- `structural.vix_spx_comove`：VIXCLS 與 sp500_trend 皆不可用，共振讀數不可用；VIX 水位由 Saxo 檢索補足，不會改變答案。
- `structural.nbfi_bank_loans`：銀行對 NBFI 放款缺失，屬確認性指標，不會改變答案。

其他註記：證據檔記錄美債基差交易槓桿 bullet 為「script 三區塊 fetch_failed → WebSearch fallback」，但 macro artifact 顯示 `cftc_lev_funds`、`move_index`、`ofr_repo` 三塊皆為 status ok。本報告以 artifact 為準，記為 ✓ API；檢索所得 MOVE 93.88（2026-11-04）未採用。

最大不確定性：

1. NASDAQ-100 實際回撤深度未知（R1）：若已深，答案會轉向 yes。
2. 2027 年初 Alphabet／Amazon／Meta 的 capex 指引（R2）：任一家正式下修即解析 yes。三家目前方向未知，是推向 yes 的主要風險。
3. CoreWeave 等 AI 算力借款人的再融資（R3）：CDS 1289 bps 下若再融資受阻或進行 distressed exchange 即成立。12 月升息若落地，會推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.86（%，較 2026-10-16 -23.0 bps） | US Treasury（BC_10YEAR，series_id=DGS10 fallback） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.63（%，較 2026-10-16 -11.0 bps） | US Treasury（TC_10YEAR，series_id=DFII10 fallback） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.23（%，derived DGS10 − DFII10） | derived（DGS10 − DFII10） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 95.97（美元／桶，較 2026-10-16 -3.96%） | EIA (RWTC)，series_id=DCOILWTICO fallback | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7249305（口，六個 CBT 美債期貨合計；delta_4w -489473） | CFTC TFF futures-only | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77（前次 2026-10-16 為 101.1） | Yahoo Finance chart API (^MOVE, unofficial) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2326.9（十億美元，tri-party repo transaction volume；+2.77%） | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebFetch | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED（EPS／PE 拆解未披露） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ⛔ FETCH FAILED（FRED key 不存在） |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ⛔ FETCH FAILED（FRED key 不存在） |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py BOGZ1FL153064486Q | ⛔ FETCH FAILED（FRED key 不存在，無 WebSearch 值） |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py DFEDTARU、DFEDTARL | ⛔ FETCH FAILED（DFEDTARU fetch_failed；DFEDTARL fetch_failed） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py BAMLH0A0HYM2 | ⛔ FETCH FAILED |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py BAMLC0A0CM | ⛔ FETCH FAILED |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py DGS10（US Treasury fallback） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | scripts/fetch_macro.py DFII10（US Treasury fallback） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py T10YIE | derived（DGS10 − DFII10） |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py DCOILWTICO（EIA RWTC fallback） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | scripts/fetch_macro.py CPIAUCSL | ⛔ FETCH FAILED |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py T5YIFR | ⛔ FETCH FAILED |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py THREEFYTP10 | ⛔ FETCH FAILED |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py SOFR、SOFR99、IORB、RPONTTLD | ⛔ FETCH FAILED（SOFR fetch_failed；SOFR99 fetch_failed；IORB fetch_failed；RPONTTLD fetch_failed） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py WALCL | ⛔ FETCH FAILED |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py ECBASSETSW、JPNASSETS | ⛔ FETCH FAILED（ECBASSETSW fetch_failed；JPNASSETS fetch_failed） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch（quarterly_state stock-of-state＋event_scan 30d） | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch（quarterly_state stock-of-state＋event_scan 30d；quarterly_state 無增速披露） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py VIXCLS＋vix_spx_comove | ⛔ FETCH FAILED（VIXCLS fetch_failed；vix_spx_comove unavailable） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py LNFACBW027SBOG | ⛔ FETCH FAILED |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds、move_index、ofr_repo（any） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 前瞻 P/E 約 28.3 | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein TSMC 目標價 554 → 600（EPS／PE 拆解未披露） | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/ | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 五年期 CDS 突破 1289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | RSP 年初至今報酬約 14.13% | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 1,474／下跌 1,252 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 22（極度恐懼） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 1.48 兆美元、YoY 約 31.4% | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔 | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | 12 月升息 25 bps 隱含機會 76.8% | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000 | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 capex 指引約 175 → 約 170（下修） | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3 | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle RPO 638 | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87 | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 今年以來發債 296 | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 10/29 起一週內 5 筆 AI 相關債券發行合計 67 | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 Anthropic 65＋OpenAI 約 70，合計約 135（分母：僅 Microsoft 約 170） | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] Microsoft 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics 完成 SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO 週漲 8% | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（0 件符合 2+ 主題×弱基本面） | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件合格） | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call ratio 1.05（日讀數） | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭基金 10 月底規模 24.31、當月淨流入 7.27 | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 總結算量 1,486,062,415（2026-09 月資料） | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性 20.93 創高 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
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
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": null,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

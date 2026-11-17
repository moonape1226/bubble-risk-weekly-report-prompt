> [DRY RUN] this report was not committed to archive.

# 2026-11-08 AI 泡沫破裂預測報告

報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：report-2026-10-18（21天前）

## 結論

**結論：no**

三條路徑都還沒走到「窗口內更可能完成」的程度。R3 的 CoreWeave 信用定價已是困境水準（債券殖利率破 16%、5 年 CDS 1289 bps），但本次未取得任何付款違約、破產或 distressed exchange 的證據。R2 目前只有 Microsoft 一家下修（需要兩家）。R1 因 NASDAQ100 日序資料取得失敗，本次無法量測回撤距離。依 base rate，本次判斷為 no。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

R1 回撤不可用——腳本未取得 NASDAQ100 日序資料。本次沒有 52 週高點、最新收盤，也沒有 R1 門檻水位，不從搜尋片段自行推算回撤。S&P 500 的 200 日／52 週趨勢偏離同樣因 FRED 日序資料失敗而不可用（本週趨勢偏離不可用——無日序資料）。

間接的市場壓力讀數（不能代替回撤量測）如下：CNN Fear & Greed 為 22（極度恐懼，2026-11-06，`retail.fear_greed`）；VIX 28.18、SKEW 149.37、隱含相關性 20.93 創高（2026-11-06，`structural.cross_asset_derivatives`）；Cboe 股票選擇權 put/call ratio 升至 1.05（2026-11-05，`speculation.equity_put_call`）；AAII 看空 48.4% 高於看多 34.1%（2026-11-04，`retail.aaii`）。另一方面，估值仍高：Shiller CAPE 38.91、trailing P/E 25.14（2026-11-06，`valuation.sp500_pe_cape`），Mag 7 前瞻本益比約 28.3（2026-10-13，`valuation.mag7_multiples`），前十大權重約 37.9%（2026-11-01，`breadth.top10_concentration`）。若要回撤 25%，從這個起點出發，下跌空間很大。

**判讀：** 情緒與波動率顯示市場已在明顯修正中，但沒有 NASDAQ-100 回撤數字，就無法判斷距 25% 門檻還有多遠。要在窗口內觸發，需要 R3 信用事件或 R2 指引連鎖下修帶動估值重定價；12 月升息定價（`monetary.fedwatch`）是窗口內可能的加速因子。

### R2 資本支出收縮

- **Microsoft：** 2026 年資本支出指引自約 175 下修至約 170（來源摘錄數值，單位依來源；2026-10-29 財報，`ai.hyperscaler_capex`）。方向為**下修**，相較前一次正式指引。
- **Alphabet：** 本次未取得最新指引及其方向。
- **Amazon：** 本次未取得最新指引及其方向。
- **Meta：** 本次未取得最新指引及其方向。

目前確認下修的有 1 家（Microsoft），R2 需要 2 家。本次證據沒有給出下一次財報日期，不自行推定；依季報節奏，窗口（至 2027-05-09）通常涵蓋各家兩次季報，但具體日期未經本次來源確認。融資面上，hyperscaler 今年以來發債約 296（2026-11-06），10/29 起一週內就有 5 筆 AI 相關債券發行、合計約 67（`ai.hyperscaler_financing_mix`），代表 capex 正持續轉向舉債融資，而不是收縮。

**判讀：** R2 已有一家下修，是三條路徑中最具體的一步，但還需要 Alphabet、Amazon、Meta 之中再有一家正式下修。本次未取得這三家的指引狀態，因此無法確認方向。下一輪財報若再出現一家下修，即觸發 R2；市場持續修正，或 R3 信用收緊抬高融資成本，都會增加這個可能。

### R3 AI 信用事件

- **CoreWeave：** 債券殖利率升破 16%（2026-11-06，`valuation.ai_credit_schism`）；5 年 CDS 突破 1289 bps（2026-11-05，`valuation.ai_credit_schism`）。這是困境區間的信用定價，顯示 AI 信用定價分歧（equity-vs-credit schism）中，信貸端已大幅重定價。CoreWeave 的總負債規模本次未經來源確認，因此是否達到 R3 的 50 億美元門檻本次未建立。本次未取得近期到期日或再融資需求的資料。
- **AI infrastructure debt financing / vendor-financing loops：** ING 出售 12 筆資料中心貸款，規模約 500（來源摘錄數值，單位依來源；2026-11-06，`structural.ai_infrastructure_debt`），顯示銀行正在降低 AI 資料中心授信曝險。
- 本次證據中**未見**任何付款違約、covenant waiver、distressed exchange、破產申請或 going-concern 語句。

**判讀：** R3 的定價已經進入困境區，是窗口內最可能率先觸發的路徑。但 R3 要求違約、破產或完成 distressed exchange 實際發生，目前只有市場定價，沒有事件。若窗口內 CoreWeave 或同類 neocloud 宣布債務交換、錯過付款，或銀行持續撤出導致再融資失敗，R3 即可能成立，並可能透過 R1 傳導。

## 支持 yes 的證據

- [R3] CoreWeave 5 年 CDS 突破 1289 bps（2026-11-05）、債券殖利率升破 16%（2026-11-06），AI 基建借款人的信用定價已進入困境區間 `valuation.ai_credit_schism`
- [R2] Microsoft 於 2026-10-29 將 2026 年資本支出指引自約 175 下修至約 170，R2 所需的兩家已有一家 `ai.hyperscaler_capex`
- [R3] ING 出售 12 筆資料中心貸款，規模約 500（2026-11-06），顯示銀行端開始降低 AI 資料中心曝險，可能壓縮 neocloud 再融資管道 `structural.ai_infrastructure_debt`
- [整體] 市場已轉為避險：Fear & Greed 22（2026-11-06）、VIX 28.18 與隱含相關性 20.93 創高（2026-11-06）、equity put/call 1.05（2026-11-05） `retail.fear_greed` `structural.cross_asset_derivatives` `speculation.equity_put_call`
- [整體] CME FedWatch 顯示 12 月升息 25 bps 的定價約 76.8%（2026-11-06）。在 CAPE 38.91 的高估值下（2026-11-06），貨幣緊縮會削弱市場緩衝 `monetary.fedwatch` `valuation.sp500_pe_cape`
- [R3] hyperscaler 今年以來發債約 296，10/29 起一週內 5 筆 AI 債券合計約 67（2026-11-06），AI capex 對債市的依賴快速上升 `ai.hyperscaler_financing_mix`

## 支持 no 的證據

- [整體] Base rate：任一 182 天窗口內，R1–R3 都不成立才是常態。本次證據中沒有任何 R3 實際違約或交換事件，R2 只有 1 家下修，未達門檻 `ai.hyperscaler_capex` `valuation.ai_credit_schism`
- [R2] capex 仍在以債務融資擴張，不是在收縮：hyperscaler 今年以來發債約 296，近一週 5 筆 AI 債券合計約 67（2026-11-06） `ai.hyperscaler_financing_mix`
- [R1] 10Y 殖利率自 5.09% 降至 4.86%（Δ −23 bps，主要由 breakeven −12 bps 驅動，實質利率 −11 bps），WTI 自 99.93 降至 95.97（2026-11-06），利率與油價壓力在前次基準後已緩解 `monetary.dgs10` `monetary.t10yie` `monetary.dfii10` `monetary.wti`
- [整體] AI 需求面仍有支撐：Anthropic 上半年營收 16.3、並已遞交 S-1（2026-10-26）；年化 AI 終端營收 Anthropic 65＋OpenAI 約 70（2026-09-30）；H100 隨選租金中位數 3.87（2026-11-03），本次未見利用率崩落的證據 `ai.openai_anthropic_revenue` `speculation.upcoming_ai_ipos` `ai.revenue_capex_gap` `ai.compute_supply_demand`
- [R1] 散戶與投機情緒已經降溫，不是繼續追高：AAII 看空 48.4%（2026-11-04）、本週唯一定價的 IPO 週漲 8%（2026-11-06）、microcap moonshot 與 Form 4 掃描皆 0 件，降低窗口內踩踏式崩跌的條件 `retail.aaii` `speculation.ipo_heat` `speculation.microcap_moonshots`
- [R1] 美債市場未見失序：CFTC 槓桿基金美債期貨淨空 −7,249,305 口（2026-11-03），MOVE 自 101.1 降至 92.77（2026-11-06），OFR tri-party repo transaction volume 2,326.9bn 平穩 `structural.treasury_basis_trade`

## 與前期比較

前次結論：無前次預測（report-2026-10-18 為舊格式評分報告）

- 自 2026-10-18 以來的主要變化：Microsoft 下修 capex 指引（2026-10-29）；CoreWeave CDS 突破 1289 bps、殖利率破 16%（2026-11-05／06）；市場轉入極度恐懼（Fear & Greed 22）；10Y 殖利率下降 23 bps。
- 這是本次首份 yes/no 預測。舊格式評分不轉換為 yes/no，因此 flip_evidence 為空。

## 資料缺漏與不確定性

本次 FRED API 金鑰缺失（fred_key_present: false），因此多數 FRED 序列 fetch_failed，且本次證據中沒有這些序列的 WebSearch 後備值。以下來源為 ⛔ FETCH FAILED：

- `valuation.sp500_trend`：S&P 500 趨勢偏離不可用。屬估值延伸的輔助讀數，不太可能單獨改變答案。
- `valuation.ndx_drawdown`：**R1 距離完全不可用，是本次最大的缺漏。** 如果 NASDAQ-100 實際已接近 25% 回撤，答案可能改變。
- `retail.household_equity_allocation`：季頻背景讀數，不影響答案。
- `monetary.fed_funds`：目前政策利率水位不可用；升息路徑以 FedWatch 代替。影響有限。
- `monetary.hy_oas`、`monetary.ig_oas`：**整體信用利差不可用**，無法判斷 CoreWeave 的壓力是否已擴散到一般高收益債。若 HY OAS 已大幅走闊，R3 與 R1 的傳導會更強，可能推向 yes。
- `monetary.cpi_yoy`、`monetary.t5yifr`、`monetary.term_premium`：通膨與 10Y 期限溢價（term premium）讀數不可用，只影響 Fed 緩衝空間的判讀，不太可能單獨改變答案。
- `monetary.repo_stress_srf`：SOFR、SOFR99、IORB、RPONTTLD 四腿全部失敗，repo_stress 為 unavailable；repo 資金壓力（SOFR−IORB）與 SRF 動用（Standing Repo Facility usage）不可讀。OFR repo transaction volume 有部分補充。
- `monetary.walcl`、`monetary.ecb_boj`：央行資產負債表不可用，屬背景流動性讀數，影響有限。
- `structural.vix_spx_comove`：VIXCLS 與 sp500_trend 皆失敗，co-movement 無法判讀；VIX 水位改由搜尋取得。
- `structural.nbfi_bank_loans`：銀行對 NBFI 放款不可用，屬確認性讀數。

✗ NOT DISCLOSED（不可作為證據）：retail.naaim、institutional.bofa_jpm_survey、monetary.treasury_auctions、monetary.private_credit_liquidity、ai.token_growth、ai.depreciation_life、structural.global_leveraged_approvals；ai.capital_cycle 的 quarterly_state 未取得可引證的增速對比，因此不判定資本週期階段（capital cycle stage）。不過其 event_scan 找到 Microsoft 於 10 月取消 Nscale 英國資料中心交易（2026-11-04 報導），列為背景訊號。

來源不一致註記：evidence 記錄美債基差交易槓桿為「script 三區塊 fetch_failed → WebSearch fallback」（MOVE 93.88，2026-11-04），但本次 macro artifact 中 cftc_lev_funds／move_index／ofr_repo 三區塊皆為 ok。本報告以 artifact 值（MOVE 92.77，2026-11-06）為準，Coverage 記 ✓ API。

最大的不確定性：

1. **CoreWeave 的負債規模與近期到期**：本次未確認是否達到 50 億美元門檻，也未取得到期牆資料。若確認達標且有窗口內到期或交換談判，會強力推向 yes。
2. **Alphabet／Amazon／Meta 的下一次 capex 指引**：任一家下修即觸發 R2，會推向 yes；三家都上修或持平，則支持 no。
3. **NASDAQ-100 實際回撤深度與 12 月 FOMC**：回撤數據缺失。若 12 月升息落地，且市場已大幅修正，R1 窗口內觸發的可能會明顯上升，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.86 | US Treasury（BC_10YEAR fallback，series_id=DGS10） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.63 | US Treasury（TC_10YEAR fallback，series_id=DFII10） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（derived DGS10 − DFII10） | 2.23 | derived：DGS10 − DFII10（series_id=T10YIE） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 95.97 | EIA (RWTC)（series_id=DCOILWTICO） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7249305 | CFTC TFF futures-only（cftc_lev_funds） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo Finance chart API（^MOVE，move_index） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2326.9 | OFR Short-term Funding Monitor（REPO-TRIV1_TV_TOT-P，ofr_repo） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebFetch | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋same quarter） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ⛔ FETCH FAILED（sp500_trend fetch_failed；無日序資料） |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ⛔ FETCH FAILED（ndx_drawdown fetch_failed） |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight vs cap-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（BOGZ1FL153064486Q） | ⛔ FETCH FAILED（BOGZ1FL153064486Q fetch_failed；無 WebSearch 後備值） |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ⛔ FETCH FAILED（DFEDTARU fetch_failed；DFEDTARL fetch_failed） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ⛔ FETCH FAILED（BAMLH0A0HYM2 fetch_failed） |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ⛔ FETCH FAILED（BAMLC0A0CM fetch_failed） |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10，US Treasury fallback） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10，US Treasury fallback） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE） | derived（DGS10 − DFII10） |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO，EIA RWTC fallback） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL） | ⛔ FETCH FAILED（CPIAUCSL fetch_failed） |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ⛔ FETCH FAILED（T5YIFR fetch_failed） |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10） | ⛔ FETCH FAILED（THREEFYTP10 fetch_failed） |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py（SOFR, SOFR99, IORB, RPONTTLD） | ⛔ FETCH FAILED（SOFR fetch_failed；SOFR99 fetch_failed；IORB fetch_failed；RPONTTLD fetch_failed；repo_stress unavailable） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch summaries） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED WALCL | scripts/fetch_macro.py（WALCL） | ⛔ FETCH FAILED（WALCL fetch_failed） |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW, JPNASSETS） | ⛔ FETCH FAILED（ECBASSETSW fetch_failed；JPNASSETS fetch_failed） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch（quarterly_state stock-of-state；event_scan 30d） | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch（quarterly_state stock-of-state；event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR ETF filings＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ⛔ FETCH FAILED（VIXCLS fetch_failed；vix_spx_comove unavailable） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ⛔ FETCH FAILED（LNFACBW027SBOG fetch_failed） |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds, move_index, ofr_repo；aggregation any） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻本益比約 28.3（原定來源：Mag 7 weighted P/E） | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein TSMC 目標價 554 → 600（EPS／PE 拆解未披露） | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/ | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html（CNBC） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5 年 CDS 突破 1289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds（Coinpaper） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | RSP 等權年初至今報酬約 14.13% | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 1,474／下跌 1,252 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 22（極度恐懼） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/（原定來源：cnn.com） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 1.48 兆美元、年增約 31.4% | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt（原定來源：FINRA） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔 | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | 12 月升息 25 bps 機率 76.8% | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/（原定來源：CME FedWatch） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000 | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年 capex 指引約 175 → 約 170（下修；Q3 財報） | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3 | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle RPO 638 | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87 | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 今年以來發債 296 | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 10/29 起一週內 5 筆 AI 相關債券發行合計 67 | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 Anthropic 65＋OpenAI 約 70，合計約 135（分母僅 Microsoft 指引可得，不計缺口） | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] Microsoft 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO 週漲 8% | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（0 件符合 2+ 主題×弱基本面） | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件合格） | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call ratio 1.05（daily） | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭基金 10 月底規模 24.31、當月淨流入 7.27 | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 總結算量 1,486,062,415（2026-09 月資料） | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性 20.93 創高 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 交叉檢核基數約 1.48 兆美元（2026-09 月資料） | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.ai_infrastructure_debt | ING 出售 12 筆資料中心貸款，規模約 500 | AI data center debt financing private credit November 2026 | https://www.cnbc.com/2026/11/06/ing-ai-data-center-loans-debt.html（CNBC） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

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
  "yes_basis": [],
  "r1_drawdown_pct": null,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

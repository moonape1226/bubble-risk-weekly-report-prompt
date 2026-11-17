> [DRY RUN] this report was not committed to archive.

# 2026-11-08 AI 泡沫破裂預測報告
報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：無（基準）

## 結論

**結論：no**

三條路徑都已出現壓力，但沒有一條在 182 天內完成的可能性高於不完成：NASDAQ-100 距 R1 門檻仍需再跌約 13.23%（`valuation.ndx_drawdown`），R2 目前僅 Microsoft 一家下修 capex 指引（`ai.hyperscaler_capex`），R3 雖有 CoreWeave CDS 1289 bps 的 distressed 定價（`valuation.ai_credit_schism`），但尚無付款違約或重組事件，且整體 HY OAS 3.48%、repo 資金壓力（SOFR−IORB）2 bps 顯示信用與資金市場尚未傳導（`monetary.hy_oas`、`monetary.repo_stress_srf`）。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 26,989.99（2026-11-06），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 13.56%；R1 門檻水位 23,418.52，自最新收盤須再下跌約 13.23% 才會觸發（`valuation.ndx_drawdown`）。這段回撤在一個月內完成：2026-11-05 收盤 26,629.81 為近期低點，11-06 反彈。同期 S&P 500 於 2026-11-05 收在 7,353.73，僅高於 200 日均線 0.42%、高於 52 週均線 1.84%（`valuation.sp500_trend`）；VIX 由 17.2（2026-10-29）升至 28.18（2026-11-05），7 日 +63.84%，S&P 500 同窗 −4.75%，屬正常的股跌波動升（comove=false），不是 crowded-optionality 讀數（`structural.vix_spx_comove`）。情緒面已進入恐慌區：CNN Fear & Greed 22（極度恐懼，`retail.fear_greed`）、AAII 看空 48.4% 對看多 34.1%（`retail.aaii`）、Cboe 股票賣買權比 1.05（`speculation.equity_put_call`）。估值仍高：Shiller CAPE 38.91、trailing P/E 25.14（`valuation.sp500_pe_cape`），Mag 7 前瞻 P/E 約 28.3（`valuation.mag7_multiples`）。貨幣面沒有立即的 Fed 緩衝：CME FedWatch 隱含 12 月升息 25 bps 機率 76.8%（`monetary.fedwatch`），CPI YoY 3.72%（2026-09，`monetary.cpi_yoy`），10Y 殖利率 4.84%（`monetary.dgs10`），WTI 99.64 美元（`monetary.wti`）。

**判讀：** 已完成門檻距離的一半以上，但剩下的 13.23% 需要新的催化劑——最可能是 R3 方向的信用事件或 12 月升息確認後的再一輪去槓桿；以目前廣義信用利差仍緊、指數已出現反彈來看，窗口內觸發 R1 是實質但低於一半的情境。

### R2 資本支出收縮

- Microsoft：最新指引將 2026 年 capex 自約 175 下調至約 170（十億美元，2026-10-29 財報季披露），方向為**下修**（`ai.hyperscaler_capex`）。注意來源 URL 標題寫作「190B capex」，與摘錄數字不一致，詳見資料缺漏。
- Alphabet：本次證據未取得最新正式指引，方向**未提供指引**。
- Amazon：本次證據未取得最新正式指引，方向**未提供指引**。
- Meta：本次證據未取得最新正式指引，方向**未提供指引**。

目前四家中已下修 1 家（Microsoft，幅度約 3%）。下一輪財報的確切日期本次證據未載；依季度財報節奏，窗口（至 2027-05-09）可涵蓋兩輪 hyperscaler 財報。反向訊號是 hyperscaler 融資結構（capex vs FCF / 發債）：今年以來 hyperscaler 發債約 296（十億美元），2026-10-29 起一週內 5 筆 AI 相關債券合計約 67（十億美元）（`ai.hyperscaler_financing_mix`），代表它們正以債務維持支出而非收縮。

**判讀：** 需再有一家在窗口內下修；目前只有 Microsoft 的小幅下修，其餘三家本次無指引資料，而債市仍大量供給資金給 capex。R2 最可能經 R1 傳導（股價大跌後的支出紀律）而觸發，單獨觸發的證據不足。

### R3 AI 信用事件

具代表性的 AI 算力借款人是 CoreWeave：債券殖利率升破 16%（2026-11-06），五年期 CDS 突破 1289 bps（2026-11-05），已屬 distressed 定價區間，且在 NASDAQ 反彈時仍維持高檔（`valuation.ai_credit_schism`）。這是 AI 信用定價分歧（equity-vs-credit schism）中「信貸端開始重定價」的後期訊號。融資端，ING 正出售 12 筆資料中心貸款，規模約 500（來源摘錄未標明單位），顯示銀行在減少 AI infrastructure debt financing / vendor-financing loops 的曝險（`structural.ai_infrastructure_debt`）。CoreWeave 的負債總額、近期到期與再融資時程不在本次證據內，因此無法確認其是否已符合 R3 的 50 億美元門檻（需另行核實），也沒有任何付款違約、寬限期、covenant waiver、distressed exchange 或 going-concern 措辭的報導。廣義信用市場平靜：HY OAS 3.48%（`monetary.hy_oas`）、IG OAS 0.93%（`monetary.ig_oas`）。

**判讀：** 定價已反映高度壓力，但 R3 需要的是實際違約、破產或 distressed exchange；在沒有到期牆或流動性缺口證據的情況下，窗口內完成仍屬少數情境。若 CoreWeave 等借款人出現再融資失敗或交換要約，將同時推動 R1。

## 支持 yes 的證據

- [R3] CoreWeave 五年期 CDS 突破 1289 bps（2026-11-05）、債券殖利率升破 16%（2026-11-06），信用市場已以 distressed 水準定價 AI 算力借款人，且在股價反彈期間未收斂（`valuation.ai_credit_schism`）。
- [R1] NASDAQ-100 於 2026-10-06 高點後一個月內回撤 13.56%，VIX 7 日上升 63.84% 至 28.18，回撤動能明顯（`valuation.ndx_drawdown`、`structural.vix_spx_comove`）。
- [R1] Fed 沒有緩衝空間：FedWatch 隱含 12 月升息 25 bps 機率 76.8%（2026-11-06），CPI YoY 3.72%（2026-09），WTI 99.64 美元（2026-11-03），10Y 殖利率 4.84%（`monetary.fedwatch`、`monetary.cpi_yoy`、`monetary.wti`、`monetary.dgs10`）。
- [R2] Microsoft 已將 2026 年 capex 指引自約 175 下調至約 170（十億美元，2026-10-29），R2 所需兩家中已有一家（`ai.hyperscaler_capex`）。
- [R3] ING 出售 12 筆資料中心貸款（2026-11-06），銀行開始降低 AI 資料中心放款曝險，可能抬高 neocloud 再融資成本（`structural.ai_infrastructure_debt`）。
- [整體] 估值與槓桿使下跌幅度可能放大：Shiller CAPE 38.91（2026-11-06）、前十大成分股權重約 37.9%、半導體 3 倍多頭 ETF 10 月淨流入 7.27（十億美元），融資餘額約 1.48 兆美元、年增約 31.4%（`valuation.sp500_pe_cape`、`breadth.top10_concentration`、`structural.leveraged_etf_aum`、`retail.margin_debt`）。

## 支持 no 的證據

- [整體] 基準率：在任意 182 天窗口內，NASDAQ-100 回撤 25%、兩家 hyperscaler 同時下修 capex、或大型 AI 借款人違約都屬罕見；R1 仍需自 26,989.99 再跌約 13.23% 至 23,418.52（`valuation.ndx_drawdown`）。
- [R3] 廣義信用與資金市場未傳導：HY OAS 3.48%、IG OAS 0.93%（2026-11-05），SOFR−IORB 2 bps、SOFR99−IORB 10 bps、SRF 動用 0（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`）。
- [R2] hyperscaler 仍有充分的債市融資管道：今年以來發債約 296（十億美元），10/29 起一週內 AI 相關債券合計約 67（十億美元），資金取得不是 capex 收縮的限制（`ai.hyperscaler_financing_mix`）。
- [R2] AI 終端需求仍在擴張：Anthropic 年化營收約 65、OpenAI 約 70（十億美元，2026-09-30），Anthropic 已遞交 S-1、目標估值 1.5 兆至 2 兆美元（`ai.revenue_capex_gap`、`speculation.upcoming_ai_ipos`）。
- [R1] 回撤尚未擴散到市場廣度：S&P 500 仍高於 200 日均線 0.42%，RSP 年初至今約 +14.13%，紐交所上漲 1,474 家對下跌 1,252 家（2026-11-06）（`valuation.sp500_trend`、`breadth.rsp_spy`、`breadth.advance_decline`）。
- [R1] 恐慌讀數已偏極端，常伴隨短期反彈：Fear & Greed 22、AAII 看空 48.4%、股票賣買權比 1.05（`retail.fear_greed`、`retail.aaii`、`speculation.equity_put_call`）。

## 與前期比較

前次結論：無前次（基準）

本次為基準執行，無前次預測可比較，`flip_evidence` 為空陣列。下次執行應優先追蹤：CoreWeave 信用定價是否續惡化、Alphabet／Amazon／Meta 的最新 capex 指引，以及 12 月 FOMC 決議。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED 來源（搜尋完成但窗口內無合格披露）：`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.treasury_auctions`、`monetary.private_credit_liquidity`、`ai.token_growth`、`ai.depreciation_life`、`ai.capital_cycle`、`structural.global_leveraged_approvals`。其中 `monetary.private_credit_liquidity` 缺漏最可能影響判斷：若私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）正在累積，R3 的傳導速度會更快；本次無證據顯示 gate proration / breach。`ai.capital_cycle` 的 event_scan 找到微軟 10 月取消 Nscale 英國資料中心交易（規模約 3），但 quarterly_state 未取得，因此整體狀態為 ✗ NOT DISCLOSED，不作為正式證據；若後續出現密集的取消／延後事件，會推向 yes。

資料一致性備註：
- `ai.hyperscaler_capex`：Microsoft 指引數字（約 175 → 約 170）取自搜尋摘錄，但來源 URL 標題寫作「190B capex」，且標示「Q3 FY2026」與 2026-10-29 的發布日不一致；Alphabet、Amazon、Meta 本次沒有指引資料。若 Microsoft 實際上並未下修，R2 計數將為 0/4，會更支持 no。
- `structural.treasury_basis_trade`：搜尋紀錄寫 script 三區塊 fetch_failed 並以 WebSearch 取得 MOVE 93.88（2026-11-04），但 macro artifact 顯示 cftc_lev_funds、move_index、ofr_repo 皆為 ok（MOVE 92.77，2026-11-06）。本報告以 artifact 為準（✓ API），未使用 93.88。
- `structural.ai_infrastructure_debt`：ING 貸款組合規模「約 500」未標單位；CoreWeave 負債總額不在證據內，因此 R3 規模門檻未核實。
- 10Y 分解：本次為基準執行（decomposition status baseline_no_prior），沒有前次比較，故不提供 Δ 分解。

主要不確定性：
1. 12 月 FOMC：若照市場定價升息，在 CPI 3.72% 與油價 99.64 美元的組合下，高估值科技股的再定價可能延續，推向 yes（R1）。
2. CoreWeave 等 neocloud 的再融資：一旦出現交換要約或付款延遲，R3 與 R1 會同時觸發，推向 yes；若重新取得融資，CDS 回落，推向 no。
3. 下一輪 hyperscaler 財報：若 Alphabet、Amazon、Meta 任一家下修 capex（且 Microsoft 的下修經確認），R2 即成立；若維持或上修，推向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest | 7353.73 | FRED API (series_id=SP500) sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend ma200 | 7322.74 | FRED API (series_id=SP500) sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 0.42 | FRED API (series_id=SP500) sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 1.84 | FRED API (series_id=SP500) sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 26989.99 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 13.56 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level | 23418.52 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026-Q2 季資料） | 48.2301354474（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 4.0（%） | FRED API (series_id=DFEDTARU) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.75（%） | FRED API (series_id=DFEDTARL) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 3.48（%） | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.93（%） | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.84（%） | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.6（%） | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.23（%） | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 99.64（美元／桶） | FRED API (series_id=DCOILWTICO) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72（%） | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.17（%） | FRED API (series_id=T5YIFR) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest | 0.9089（%，Kim-Wright） | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（序列自身 trailing 7 日） | -2.7（bps） | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.92（%） | FRED API (series_id=SOFR) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 4.0（%） | FRED API (series_id=SOFR99) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.9（%） | FRED API (series_id=IORB) | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用） | 0.0（十億美元） | FRED API (series_id=RPONTTLD) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,748,145（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,945,410（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,261,882（¥626.19T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED API (series_id=VIXCLS) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 28.18 | FRED API vix_spx_comove block | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日窗） | 63.84（%） | FRED API vix_spx_comove block | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日窗） | -4.75（%） | FRED API vix_spx_comove block | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2111.0042（$2.11T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7249305（口） | CFTC TFF futures-only cftc_lev_funds | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -489473（口） | CFTC TFF futures-only cftc_lev_funds | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo Finance chart API (^MOVE) move_index | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2326.9（十億美元，transaction volume） | OFR STFM REPO-TRIV1_TV_TOT-P ofr_repo | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebFetch | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED（EPS／PE 拆解未披露） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py BOGZ1FL153064486Q | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py DFEDTARU＋DFEDTARL | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py BAMLH0A0HYM2 | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py BAMLC0A0CM | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py DGS10 | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | scripts/fetch_macro.py DFII10 | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py T10YIE（FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py DCOILWTICO | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | scripts/fetch_macro.py CPIAUCSL yoy_pct | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py T5YIFR | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py THREEFYTP10 | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py SOFR、SOFR99、IORB、RPONTTLD | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py WALCL | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py ECBASSETSW＋JPNASSETS | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED（僅 Microsoft 取得最新指引） |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch：quarterly_state（stock-of-state）＋event_scan（30d） | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch：quarterly_state（stock-of-state）＋event_scan（30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe 月報） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py VIXCLS＋vix_spx_comove | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py LNFACBW027SBOG | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds、move_index、ofr_repo（any） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻 P/E 約 28.3 | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ （Vested Finance；原定來源 Mag 7 P/E 彙整） | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein TSMC 目標價 554 → 600（EPS／PE 拆解未披露） | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/ （StockAnalysis；原定來源 Bernstein 研究摘要） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html （CNBC） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 五年期 CDS 突破 1289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds （Coinpaper） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | RSP 年初至今報酬約 14.13% | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY （Total Real Returns） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration （Chartrow） | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | 紐交所上漲 1,474 對下跌 1,252 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ （McClellan） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 22（極度恐懼） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ （FinHacker；原定來源 cnn.com/markets/fear-and-greed） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 1.48 兆美元、年增約 31.4% | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt （原定來源 FINRA 月報） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives （AAII） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔 | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week （Benzinga） | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | 12 月升息 25 bps 機率 76.8% | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ （24/7 Wall St.；原定來源 CME FedWatch） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000（來源未標單位） | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee （BigGo Finance） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年 capex 指引約 175 → 約 170（十億美元） | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex （Global Data Center Hub；URL 標題數字與摘錄不一致） | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3（十億美元） | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html （Yahoo Finance） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle RPO 638（十億美元） | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ （Motley Fool） | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87（美元／小時） | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends （GetDeploying） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 今年以來發債約 296（十億美元） | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era （404K Research 引 Goldman） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 2026-10-29 起一週內 5 筆 AI 相關債券發行合計約 67（十億美元） | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era （404K Research 引 Goldman） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 Anthropic 65＋OpenAI 約 70，合計約 135（十億美元）；分母本次僅 Microsoft 約 170 | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html （Yahoo Finance） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] 微軟 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 （Investing.com 引 Bloomberg） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics 完成 SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ （Securities.io） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO 週漲 8% | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears （Renaissance Capital） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描：0 件符合 2+ 主題×弱基本面 | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆美元 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 （Built In） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描：0 件合格 | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe 股票選擇權賣買權比 1.05（daily） | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide （Seeking Alpha） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭 ETF 10 月底規模 24.31、當月淨流入 7.27（十億美元） | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html （Yahoo Finance） | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 （Cboe 新聞稿） | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 9 月總結算量 1,486,062,415 口（2026-09 月資料） | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report （OCC） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性 20.93（創高） | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 （Saxo） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-09 月資料）交叉檢核基數約 1.48 兆美元 | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt （原定來源 FINRA 月報） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.ai_infrastructure_debt | ING 出售 12 筆資料中心貸款，規模約 500（來源未標單位） | AI data center debt financing private credit November 2026 | https://www.cnbc.com/2026/11/06/ing-ai-data-center-loans-debt.html （CNBC） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

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
  "prior_date": null,
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 13.56,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

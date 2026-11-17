> [DRY RUN] this report was not committed to archive.

# 2026-11-08 AI 泡沫破裂預測報告

報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：report-2026-10-18（21天前）

## 結論

**結論：no**

三條路徑都已升溫但尚無一條完成或接近完成：NASDAQ-100 距 52 週高點回撤 13.56%，仍需自最新收盤再跌約 13.23% 才觸及 R1；R2 目前僅 Microsoft 一家下修 capex 指引（需兩家）；R3 方面 CoreWeave 5 年期 CDS 已達 1289 bps、債券殖利率破 16%，屬 distressed 定價，但 evidence 中沒有付款違約、破產申請或 distressed exchange。相對於 182 天窗口的低基準率，現有證據顯示脆弱性與壓力在上升，但仍不足以判定任一條件「較可能成立」。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 26989.99（2026-11-06），252 個交易日最高收盤 31224.69（2026-10-06），距 52 週高點回撤 13.56%；R1 門檻水位 23418.52，自最新收盤需再下跌約 13.23% 才觸及（`valuation.ndx_drawdown`）。回撤在一個月內由高點快速展開：S&P 500 於 2026-11-05 收 7353.73，較前次基準日（2026-10-16 收 7659.44）下跌 3.99%，距 200 日均線僅 +0.42%、距 52 週均線 +1.84%，延伸幅度已大致消化（`valuation.sp500_trend`）。壓力讀數明顯升高：VIXCLS 2026-11-05 為 28.18，7 日內 VIX 上升 63.84% 而 S&P 500 下跌 4.75%，屬一般的避險型反向走勢而非 crowded-optionality 同漲（`structural.vix_spx_comove`）；CNN Fear & Greed 22（極度恐懼，2026-11-06，`retail.fear_greed`）；Cboe equity put/call 升至 1.05（2026-11-05，`speculation.equity_put_call`）；Cboe SKEW 149.37、隱含相關性創高 20.93（2026-11-06，`structural.cross_asset_derivatives`）。估值仍高：Shiller CAPE 38.91、trailing P/E 25.14（2026-11-06，`valuation.sp500_pe_cape`），Mag 7 前瞻本益比約 28.3（2026-10-13，`valuation.mag7_multiples`）。貨幣面不利於護盤：CME FedWatch 顯示 12 月升息 25 bps 機率 76.8%（2026-11-06，`monetary.fedwatch`），CPI YoY 3.72%（2026-09 月資料，`monetary.cpi_yoy`）。

**判讀：** R1 距門檻仍有約 13% 的跌幅空間，高估值與已出現的恐慌讀數讓剩餘跌幅並非不可能；若 Fed 於 12 月升息、AI 信用壓力（R3 路徑）外溢或下一輪季報出現第二家 capex 下修，可能在窗口內把回撤推過 25%，但目前市場廣度與信用利差尚未呈現失序。

### R2 資本支出收縮

- Microsoft：2026 年資本支出指引由約 175 下調至約 170（十億美元，2026-10-29 財報季），方向為 **下修**（`ai.hyperscaler_capex`）。
- Alphabet：本次 evidence 未取得最新官方指引，方向無法判定。
- Amazon：本次 evidence 未取得最新官方指引，方向無法判定。
- Meta：本次 evidence 未取得最新官方指引，方向無法判定。

四家中目前已知 1 家下修。其餘三家的具體下次財報日期未在 evidence 中，但 182 天窗口涵蓋兩個季報季（年初與春季），因此至少還有兩次正式指引機會。融資面已由現金流轉向舉債：hyperscaler 今年以來發債 296（十億美元），10/29 起一週內 5 筆 AI 相關債券合計 67（十億美元）（2026-11-06，`ai.hyperscaler_financing_mix`）——舉債能力尚在，短期內反而降低被迫砍 capex 的壓力。需求端 Anthropic 上半年營收 16.3（2026-10-26，`ai.openai_anthropic_revenue`），年化 AI 終端營收 Anthropic 65 ＋ OpenAI 約 70，合計約 135（2026-09-30，`ai.revenue_capex_gap`）。

**判讀：** R2 已完成一半（1/2），但 Microsoft 的下修幅度僅約 3%，且其他三家方向未知；要在窗口內成立，需要再一家在下一或下下季報中正式下修。若 R1 路徑的股價回撤擴大或融資成本上升，下修壓力會增加；目前債市仍願意大額承接 hyperscaler 發行，是反向力量。

### R3 AI 信用事件

候選借款人：CoreWeave 是 evidence 中唯一出現明顯信用壓力的 AI 算力主業借款人。其 5 年期 CDS 突破 1289 bps（2026-11-05）、債券殖利率升破 16%（2026-11-06）（`valuation.ai_credit_schism`）——即使 NASDAQ 反彈，違約保護成本仍維持在 1,000 bps 以上，是 AI 信用定價分歧（equity-vs-credit schism）中「信貸端先重定價」的後期訊號。銀行端亦在降低曝險：ING 出售 12 筆資料中心貸款，規模約 500（2026-11-06，`structural.ai_infrastructure_debt`）。廣義信用仍平穩：HY OAS 3.48%（+17 bps vs 2026-10-16，`monetary.hy_oas`）、IG OAS 0.93%（+8 bps，`monetary.ig_oas`）。evidence 未披露 CoreWeave 的負債總額、近期到期日、評等動作，也沒有任何付款違約、covenant waiver、distressed exchange 或 going-concern 文字。

**判讀：** R3 是最接近「事件型」觸發的路徑：CDS 處於 distressed 區間代表市場正在為違約／債務重組定價，但 R3 需要實際的破產、超過寬限期違約或完成 distressed exchange；若 CoreWeave 或同類 neocloud 在窗口內面臨再融資失敗或啟動交換要約，R3 可能成立並同時觸發 R1。目前 evidence 不足以判定該事件較可能在 182 天內發生。

## 支持 yes 的證據

- [R3] CoreWeave 5 年期 CDS 突破 1289 bps（2026-11-05）、債券殖利率升破 16%（2026-11-06），已屬 distressed 定價，信貸端先於股權重定價 `valuation.ai_credit_schism`
- [R2] Microsoft 將 2026 年資本支出指引自約 175 下調至約 170（2026-10-29），R2 所需兩家中已有一家下修 `ai.hyperscaler_capex`
- [R1] NASDAQ-100 2026-11-06 收 26989.99，距 52 週高點回撤 13.56%，一個月內自 2026-10-06 高點 31224.69 快速下跌 `valuation.ndx_drawdown`
- [整體] 市場壓力讀數同步升高：VIXCLS 28.18（2026-11-05，7 日 +63.84%）、CNN Fear & Greed 22、equity put/call 1.05 `structural.vix_spx_comove` `retail.fear_greed` `speculation.equity_put_call`
- [整體] 貨幣緩衝有限：12 月升息 25 bps 機率 76.8%（2026-11-06）、CPI YoY 3.72%（2026-09），Fed 難以在 AI 主導的回撤中降息護盤 `monetary.fedwatch` `monetary.cpi_yoy`
- [R3] 銀行端降低 AI 資料中心曝險：ING 出售 12 筆資料中心貸款，規模約 500（2026-11-06） `structural.ai_infrastructure_debt`
- [整體] 估值與舉債雙高：Shiller CAPE 38.91（2026-11-06）、hyperscaler 今年以來發債 296（十億美元，2026-11-06） `valuation.sp500_pe_cape` `ai.hyperscaler_financing_mix`

## 支持 no 的證據

- [整體] 基準率：182 天內 R1–R3 任一成立本屬少見；目前 R1 仍需自 26989.99 再跌約 13.23% 至 23418.52 才觸及門檻 `valuation.ndx_drawdown`
- [R3] 廣義信用未失序：HY OAS 3.48%、IG OAS 0.93%（2026-11-05），自前次基準日僅分別擴大 17 bps 與 8 bps，AI 信用壓力尚未擴散成系統性重定價 `monetary.hy_oas` `monetary.ig_oas`
- [R2] 債市仍大規模承接 hyperscaler 融資：10/29 起一週 5 筆 AI 相關債券合計 67（十億美元，2026-11-06），融資管道暢通降低被迫下修 capex 的壓力 `ai.hyperscaler_financing_mix`
- [R2] AI 終端需求仍在成長：Anthropic 上半年營收 16.3（2026-10-26），年化 AI 終端營收 Anthropic 65 ＋ OpenAI 約 70 合計約 135（2026-09-30） `ai.openai_anthropic_revenue` `ai.revenue_capex_gap`
- [R1] S&P 500 已回到 200 日均線附近（2026-11-05 偏離 +0.42%），價格延伸已大幅消化，VIX 與股價為一般反向關係而非同漲 `valuation.sp500_trend` `structural.vix_spx_comove`
- [R2] 賣方仍在上調 AI 半導體目標價：Bernstein 將 TSMC 目標價由 554 上調至 600（2026-11-03） `valuation.analyst_tp_decomposition`

## 與前期比較

前次結論：無前次預測（report-2026-10-18 為舊格式評分報告）

前次基準為舊格式評分報告，不轉換為 yes／no，flip_evidence 為空。自 2026-10-18 以來的主要變化：

- NASDAQ-100 在 2026-10-06 創 252 日高點 31224.69 後回撤至 13.56%（2026-11-06）`valuation.ndx_drawdown`
- Microsoft 於 2026-10-29 下修 2026 年 capex 指引，R2 首家下修出現 `ai.hyperscaler_capex`
- CoreWeave CDS 突破 1289 bps（2026-11-05）`valuation.ai_credit_schism`
- VIXCLS 由 19.99（2026-10-16）升至 28.18（2026-11-05）；10Y 殖利率由 5.09% 降至 4.84%（ΔDGS10 −25 bps、ΔDFII10 −14 bps、ΔT10YIE −12 bps，判讀：不可判（視窗不一致））`monetary.dgs10` `monetary.dfii10` `monetary.t10yie`

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `monetary.repo_stress_srf`：SOFR99 與 RPONTTLD 腳本 `fetch_failed`，本次無 fallback 值，因此 99th 分位尾部利差與 SRF 動用（Standing Repo Facility usage）不可用。可用的核心腿：SOFR 3.92%、IORB 3.90%（皆 2026-11-05），repo 資金壓力（SOFR−IORB）為 2 bps（`repo_stress.status: partial`）。此缺口不太可能改變結論：R1–R3 的主要訊號來自股權回撤、capex 指引與 AI 發行人信用，且 SOFR−IORB 與 OFR tri-party repo transaction volume 均未顯示資金失序；但若 SRF 動用實際大幅上升，會強化 yes 側的系統性壓力敘事。

其他註記：

- 美債基差交易槓桿（Treasury basis-trade leverage）：evidence 的 WebSearch fallback（MOVE 93.88，2026-11-04）是在假設腳本三區塊失敗下執行，但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 均為 `status: ok`；依規則以腳本值為準（MOVE 92.77，2026-11-06），fallback 值不作為證據。
- R2 只取得 Microsoft 指引；Alphabet、Amazon、Meta 的最新官方指引不在 evidence 中，這是本次判斷最大的資料缺口——若其中任一家已在本季下修，R2 可能已經成立，答案會轉為 yes。
- 資本週期階段（capital cycle stage）的 quarterly_state 未取得；30 日事件掃描見到 Microsoft 取消 Nscale 英國資料中心交易（2026-11-04），因組件聚合為 all，該來源整體為 ✗ NOT DISCLOSED，不作為證據引用。

最大的不確定性：

1. CoreWeave 等 neocloud 的再融資與到期結構（evidence 未披露）：若出現交換要約或寬限期違約，R3 成立並可能帶動 R1，答案推向 yes。
2. 12 月 FOMC 是否升息：升息會壓縮估值並提高 AI 發行人融資成本，推向 yes；若維持不變，緩和 R1 壓力，推向 no。
3. 下一輪 hyperscaler 季報的 capex 指引：再有一家下修即 R2 成立（yes）；若 Alphabet／Amazon／Meta 維持或上修，R2 在窗口內成立的空間縮小（no）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7353.73 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 0.42 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 1.84 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 26989.99 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 13.56 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
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
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.9089（%） | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.92（%） | FRED API (series_id=SOFR) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.9（%） | FRED API (series_id=IORB) | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,748,145（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,945,410（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,261,882（¥626.19T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED API (series_id=VIXCLS) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（base 2026-10-29，window 7 日） | 28.18 | FRED API (series_id=VIXCLS + SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 63.84 | FRED API (series_id=VIXCLS + SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -4.75 | FRED API (series_id=VIXCLS + SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2111.0042（$2.11T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位） | -7249305 | CFTC TFF futures-only | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo Finance chart API (^MOVE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2326.9 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com 直接抓取 | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED（EPS／PE 拆解未披露） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch（stock-of-state，2026-09 月資料） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py BOGZ1FL153064486Q | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py DFEDTARU＋DFEDTARL | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py BAMLH0A0HYM2 | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py BAMLC0A0CM | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py DGS10 | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py DFII10 | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py T10YIE（FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py DCOILWTICO | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | scripts/fetch_macro.py CPIAUCSL yoy_pct | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py T5YIFR | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py THREEFYTP10 | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py SOFR／SOFR99／IORB／RPONTTLD；無 WebSearch fallback 結果 | ⛔ FETCH FAILED（SOFR ok；SOFR99 fetch_failed；IORB ok；RPONTTLD fetch_failed） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py WALCL | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py ECBASSETSW＋JPNASSETS | ✓ API（ECBASSETSW ok；JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED（僅取得 MSFT；GOOGL／AMZN／META 未取得） |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch：quarterly_state（stock-of-state）＋event_scan（30d） | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch：quarterly_state（stock-of-state）＋event_scan（30d）；quarterly_state 無可用披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED（1 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（Renaissance Capital weekly recap） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（7d movers 掃描） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR ETF 申報＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe 月度量報告） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py VIXCLS＋vix_spx_comove | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py LNFACBW027SBOG | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds＋move_index＋ofr_repo（aggregation any） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻本益比約 28.3 | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein TSMC 目標價 554 → 600（EPS Δ／目標 PE Δ 未披露） | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/ | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5 年期 CDS 突破 1289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | 等權指數（RSP）年初至今報酬約 14.13 | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | 前十大成分股權重約 37.9 | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 1,474 對下跌 1,252 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 22（極度恐懼） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 1.48 兆美元、年增約 31.4% | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1、看空 48.4 | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔 | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | 12 月升息 25 bps 機率 76.8% | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000（單位依來源原文） | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年 capex 指引約 175 → 約 170（下修） | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3 | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle 剩餘履約義務（RPO）638 | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87 | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 今年以來發債 296（十億美元） | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 10/29 起一週內 5 筆 AI 相關債券發行合計 67（十億美元） | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic 65 ＋ OpenAI 約 70，合計約 135；分母僅 MSFT 指引約 170 可用，缺口方向不判定 | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] Microsoft 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics 完成 SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO 週漲 8% | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | 0 件符合 2+ 主題×弱基本面 | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描 0 件合格 | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 升至 1.05（S&P 500 下跌 4.4% 期間） | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭基金 10 月底規模 24.31、當月淨流入 7.27 | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市 0 件 | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 9 月總結算量 1,486,062,415（2026-09 月資料） | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性創高 20.93 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-09 月資料）交叉檢核基數約 1.48 兆美元 | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
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
  "r1_drawdown_pct": 13.56,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

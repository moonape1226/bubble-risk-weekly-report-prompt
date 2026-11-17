> [DRY RUN] this report was not committed to archive.

# 2026-11-08 AI 泡沫破裂預測報告
報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：無（基準）

## 結論

**結論：no**

三條路徑都已出現壓力，但都還沒有走到終點：R1 尚需自最新收盤再跌約 13.23%，R2 目前僅 Microsoft 一家（且來源有歧義）下修，R3 的 CoreWeave 雖已被定價為高違約風險，卻無付款違約或 distressed exchange 的證據。決定性的反證是融資市場仍完全敞開——hyperscaler 今年以來發債約 296、單週 AI 相關發債約 67、HY OAS 僅 3.48%——在資金可得的情況下，182 天內完成 R2 第二家下修或 R3 實際違約的門檻仍高於本次證據所能支撐的程度。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 26,989.99（2026-11-06），252 交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 13.56%；R1 門檻水位為 23,418.52，自最新收盤須再下跌約 13.23% 才會觸發（`valuation.ndx_drawdown`）。高點僅在一個月前，故整個預測窗口內 31,224.69 都仍在 252 日回溯期內，門檻水位不會因高點滾出而下移。同期波動已急升：VIX 28.18（2026-11-05），trailing 7 日 VIX +63.84%、S&P 500 −4.75%，屬典型的「股跌波動升」而非 crowded-optionality 的同漲（`structural.vix_spx_comove`）；S&P 500 7,353.73 僅高於 200 日均線 0.42%（`valuation.sp500_trend`）。情緒端已在極度恐懼區：CNN Fear & Greed 22（2026-11-06，`retail.fear_greed`），AAII 看空 48.4% 對看多 34.1%（2026-11-04，`retail.aaii`），Cboe 股票賣買權比 1.05（2026-11-05，`speculation.equity_put_call`）。宏觀緩衝有限：CPI YoY 3.72%（2026-09）、WTI 99.64（`monetary.cpi_yoy`、`monetary.wti`），市場隱含 12 月升息 25 bps 的機會約 76.8%（`monetary.fedwatch`），Fed 難以在跌勢中降息托底。估值仍高：Shiller CAPE 38.91、trailing P/E 25.14（`valuation.sp500_pe_cape`）。

**判讀：** R1 已走了一半以上（13.56% / 25%），而且是在升息預期、油價近 100 美元與 VIX 28 的環境下發生；要在窗口內觸發，需要再一次與 10 月同等級的去槓桿，典型觸發者是 R3 信用事件外溢或 R2 第二家下修。情緒已極度悲觀、槓桿 ETF 仍有逢低買盤，短期反彈與續跌都可能，單靠目前證據不足以判定再跌 13% 會在 182 天內完成。

### R2 資本支出收縮

- Microsoft：依 2026-10-29 來源，2026 年資本支出指引自約 175 下調至約 170（來源原文數值），方向為下修（`ai.hyperscaler_capex`）。注意同一來源的網址標題提及「190B capex」，與內文數值不一致，且未明示是否為公司正式指引（vs 分析師口徑），本次將其計為「可能的第一家下修」，但存在歧義。
- Alphabet：本次證據未取得其最新正式指引（未提供指引資料）。
- Amazon：本次證據未取得其最新正式指引（未提供指引資料）。
- Meta：本次證據未取得其最新正式指引（未提供指引資料）。

目前四家中至多一家下修。旁證：Microsoft 在 2026-11-04 被報導收緊對 neocloud 資料中心專案的監督並取消一筆英國資料中心交易（僅作背景，該來源的 Coverage 整體非成功狀態）。反向證據是融資端仍暢通：hyperscaler 今年以來發債約 296、2026-10-29 起一週內 5 筆 AI 相關債券發行合計約 67（`ai.hyperscaler_financing_mix`）。下一輪財報（約 2027 年 1 月底）與再下一輪（約 2027 年 4 月底）依季報節奏都落在窗口內，具體日期本次證據未取得。

**判讀：** R2 只差一家，是三條路徑中「結構上最接近」的一條；但 Microsoft 的下修幅度僅約 3%，且資料有歧義，其餘三家沒有任何下修證據，同時發債管道大開代表 capex 尚無被迫收縮的資金約束。推過門檻需要 1 月財報季出現第二家明確下修，最可能的觸發是 R1 續跌壓縮股價或 AI 營收對 capex 缺口（revenue-to-capex gap）被市場懲罰。

### R3 AI 信用事件

最接近 R3 門檻的借款人是 CoreWeave（主業為 AI 算力；其負債是否 ≥ 50 億美元本次證據未直接取得）。AI 信用定價分歧（equity-vs-credit schism）已明顯轉向信貸端重定價：CoreWeave 債券殖利率升破 16%（2026-11-06），五年期 CDS 突破 1,289 bps（2026-11-05），且發生在 NASDAQ 反彈之際（`valuation.ai_credit_schism`）。AI infrastructure debt financing / vendor-financing loops 方面，ING 出售 12 筆資料中心貸款、規模約 500（2026-11-06，`structural.ai_infrastructure_debt`），顯示銀行在降低曝險，但次級市場仍有承接。廣義信用並未失序：HY OAS 3.48%、IG OAS 0.93%（2026-11-05，`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）僅 2 bps、SOFR99−IORB 10 bps，SRF 動用 0（`monetary.repo_stress_srf`）。本次證據未見任何付款違約、covenant waiver、distressed exchange 或 going-concern 字樣，也未取得具體到期牆資料。

**判讀：** 信貸市場已把 CoreWeave 定價為高風險，屬後期訊號；但從 CDS 高企到實際違約或 distressed exchange 通常需要流動性真正耗盡，而目前 AI 相關發債與貸款轉售都還能成交。推過門檻需要：融資窗口關閉（例如 HY 大幅走闊）、主要客戶承諾縮減，或一次拒絕再融資。

## 支持 yes 的證據

- [R1] NASDAQ-100 一個月內自 31,224.69 跌至 26,989.99，距 52 週高點回撤 13.56%，距 R1 門檻只差約 13.23%，且 VIX 已達 28.18、trailing 7 日 +63.84%（`valuation.ndx_drawdown`、`structural.vix_spx_comove`）。
- [R3] CoreWeave 債券殖利率升破 16%（2026-11-06）、五年期 CDS 突破 1,289 bps（2026-11-05），信貸端已先於股價重定價（`valuation.ai_credit_schism`）。
- [R2] Microsoft 2026 年資本支出指引據報自約 175 下調至約 170（2026-10-29），若屬正式指引，R2 只差第二家（`ai.hyperscaler_capex`）。
- [整體] Fed 的緩衝空間受限：CPI YoY 3.72%（2026-09）、WTI 99.64（2026-11-03）、市場隱含 12 月升息 25 bps 的機會約 76.8%，10Y 殖利率 4.84%（`monetary.cpi_yoy`、`monetary.wti`、`monetary.fedwatch`、`monetary.dgs10`）。
- [R3] AI 融資高度依賴債市：hyperscaler 今年以來發債約 296，單週 AI 相關發債約 67；ING 出售 12 筆資料中心貸款約 500，銀行端開始降曝險（`ai.hyperscaler_financing_mix`、`structural.ai_infrastructure_debt`）。
- [整體] 估值與槓桿仍在高檔：Shiller CAPE 38.91、margin debt 約 1.48 兆美元且年增約 31.4%（2026-09）、半導體 3 倍多頭基金 10 月淨流入 7.27（`valuation.sp500_pe_cape`、`retail.margin_debt`、`structural.leveraged_etf_aum`）。

## 支持 no 的證據

- [R3] 廣義信用與資金市場平靜：HY OAS 3.48%、IG OAS 0.93%（2026-11-05），SOFR−IORB 2 bps、SRF 動用 0（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`）。
- [R2] 融資窗口完全敞開：hyperscaler 今年以來發債約 296、2026-10-29 起一週 5 筆 AI 相關債券合計約 67，沒有迫使 capex 收縮的資金約束（`ai.hyperscaler_financing_mix`）。
- [整體] AI 資本市場仍在擴張：Anthropic 已遞交 S-1，目標估值 1.5 兆至 2 兆（2026-10-26）；Bernstein 於 2026-11-03 將 TSMC 目標價自 554 上調至 600（`speculation.upcoming_ai_ipos`、`valuation.analyst_tp_decomposition`）。
- [R2] 除 Microsoft 外，Alphabet、Amazon、Meta 本次均無下修證據，且 Microsoft 的下調幅度僅約 3%、資料存在歧義（`ai.hyperscaler_capex`）。
- [R1] 情緒已極度悲觀，常見於階段性低點附近：Fear & Greed 22、AAII 看空 48.4%、股票賣買權比 1.05（`retail.fear_greed`、`retail.aaii`、`speculation.equity_put_call`）。
- [整體] 需求端仍有成長：Anthropic 與 OpenAI 年化營收合計約 135（2026-09-30），H100 隨選租金中位數 3.87（2026-11-03）未見崩跌（`ai.revenue_capex_gap`、`ai.compute_supply_demand`）。

## 與前期比較

前次結論：無前次（基準）

這是新格式的第一次預測，無前次預測可比較，flip_evidence 為空。10Y 拆解為 baseline_no_prior（無前次比較日），非資料缺失。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源檢索完成但無窗口內合格披露（✗ NOT DISCLOSED），不作為證據引用：retail.naaim、institutional.bofa_jpm_survey、monetary.treasury_auctions、monetary.private_credit_liquidity、ai.token_growth、ai.depreciation_life、ai.capital_cycle（quarterly_state 無供需增速披露；event_scan 有 Microsoft 取消 Nscale 英國資料中心交易一事，但組合狀態非成功）、structural.global_leveraged_approvals。其中私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）與美債標售需求（auction tail / bid-to-cover）的缺漏最可能影響 R3 判讀：若存在未被抓到的 gate proration / breach，R3 傳導會比本文假設更快。

資料一致性註記：case 證據表把美債基差交易槓桿（Treasury basis-trade leverage）標為「script 三區塊 fetch_failed → WebSearch fallback」，但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 三區塊皆為 status ok；本次以 artifact 為準記 ✓ API（MOVE 92.77），WebSearch 所得 MOVE 93.88（2026-11-04）僅列為 traceability 交叉核對。

最大不確定性：

- Microsoft 資本支出下修的性質：來源數值（約 175 → 約 170）與網址標題（190B capex）不一致，若證實為正式指引下修，R2 只差一家，答案更接近翻向 yes；若為誤讀，R2 距離更遠。
- CoreWeave 的負債規模與到期結構未取得：若確認負債 ≥ 50 億美元且窗口內有大額再融資，R3 會成為最可能的 yes 路徑。
- 2027 年 1 月底的 hyperscaler 財報季與 12 月 FOMC：若升息落地且 NASDAQ 續跌，R1 與 R2 可能同時推進，會把答案推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest | 7353.73 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 0.42 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 1.84 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 26989.99 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 13.56 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level | 23418.52 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2） | 48.23 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 4.0 | FRED API (series_id=DFEDTARU) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.75 | FRED API (series_id=DFEDTARL) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 3.48 | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.93 | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.84 | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.6 | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.23 | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 99.64 | FRED API (series_id=DCOILWTICO) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.17 | FRED API (series_id=T5YIFR) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.9089 | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 日） | -2.7 | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.92 | FRED API (series_id=SOFR) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 4.0 | FRED API (series_id=SOFR99) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.9 | FRED API (series_id=IORB) | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,748,145（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,945,410（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,261,882（¥626.19T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED API (series_id=VIXCLS) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 28.18 | FRED API derived block vix_spx_comove | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 63.84 | FRED API derived block vix_spx_comove | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -4.75 | FRED API derived block vix_spx_comove | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2111.0042（$2.11T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7249305 | CFTC TFF futures-only (block cftc_lev_funds) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -489473 | CFTC TFF futures-only (block cftc_lev_funds) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo Finance chart API ^MOVE (block move_index) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2326.9 | OFR STFM REPO-TRIV1_TV_TOT-P (block ofr_repo) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebFetch | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED（僅群體前瞻 P/E；P/S 對 10 年均值未取得） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED（EPS／PE 拆解未披露） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED（new high/low 未取得） |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（stock-of-state，2026-09 月資料） | ✓ SEARCH-VERIFIED（對市值比率未取得） |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch primary | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
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
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch primary（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch primary | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch primary（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED（僅 Microsoft；Alphabet／Amazon／Meta 未取得） |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch primary | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch primary | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch primary（quarterly_state stock-of-state；event_scan 30d） | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch primary（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch primary（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch primary（quarterly_state stock-of-state；event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch primary（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch primary | ✓ SEARCH-VERIFIED（僅半導體 3 倍多頭基金） |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe 月報） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（confirmation only） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch primary（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）；WebSearch 交叉核對 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻本益比約 28.3 | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein TSMC 目標價 554 → 600（EPS／PE 拆解未披露） | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/ | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 五年期 CDS 突破 1,289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | 等權指數（RSP）年初至今報酬約 14.13%（SPY 對照未載於結果） | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 1,474 對下跌 1,252 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 22（極度恐懼） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 1.48 兆美元、年增約 31.4% | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔 | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | 12 月升息 25 bps 市場隱含機會 76.8% | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000 | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年資本支出指引約 175 → 約 170（下修；網址標題提及 190B，存歧義） | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3 | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle RPO 638（同一 counterparty 跨供應商加總未披露） | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87 | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 今年以來發債約 296 | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 2026-10-29 起一週內 5 筆 AI 相關債券發行合計約 67 | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic 65＋OpenAI 約 70，合計約 135（分母僅 Microsoft 約 170） | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] Microsoft 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
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
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性 20.93 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 交叉檢核基數約 1.48 兆美元（2026-09 月資料） | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.ai_infrastructure_debt | ING 出售 12 筆資料中心貸款，規模約 500 | AI data center debt financing private credit November 2026 | https://www.cnbc.com/2026/11/06/ing-ai-data-center-loans-debt.html | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index 交叉核對：MOVE 93.88（artifact 值 92.77 為準） | MOVE index Treasury volatility level November 2026 | https://streetstats.finance/markets/volatility | 2026-11-04 | 2026-11-08T09:30:00+08:00 |

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
  "r1_drawdown_pct": 13.56,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

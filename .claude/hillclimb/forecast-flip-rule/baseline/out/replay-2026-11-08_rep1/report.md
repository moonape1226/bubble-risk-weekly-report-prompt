> [DRY RUN] this report was not committed to archive.

# 2026-11-08 AI 泡沫破裂預測報告

報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：report-2026-10-18（21天前）

## 結論

**結論：no**

三條路徑都已出現壓力，但沒有一條已走過一半並取得廣義信用或資金面確認：NASDAQ-100 距 R1 門檻仍需再跌約 13.23%（`valuation.ndx_drawdown`）；R2 目前只確認 Microsoft 一家下修（`ai.hyperscaler_capex`）；R3 方面 CoreWeave 信用定價已達困境水準（`valuation.ai_credit_schism`），但本次證據沒有付款違約、破產或 distressed exchange。同時 HY OAS 3.48%、SOFR−IORB 僅 2 bps（`monetary.hy_oas`、`monetary.repo_stress_srf`），傳導尚未擴散，因此相對基準率仍判斷為 no。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 26,989.99（2026-11-06）；252 個交易日最高收盤 31,224.69（2026-10-06）；距 52 週高點回撤 13.56%。R1 門檻水位 23,418.52，需自最新收盤再下跌約 13.23% 才會觸發（`valuation.ndx_drawdown`）。這次回撤集中在一個月內：同期 S&P 500 自 2026-10-16 的 7,659.44 跌至 2026-11-05 的 7,353.73（−3.99%），但仍高於 200 日均線 0.42%、高於 52 週均線 1.84%（`valuation.sp500_trend`）。波動與情緒已明顯轉向避險：VIX 28.18（2026-11-05），7 日內 +63.84%，同窗 S&P 500 −4.75%，屬正常的股跌波動升，非 crowded-optionality 共振（`structural.vix_spx_comove`）；CNN Fear & Greed 22，處於極度恐懼（`retail.fear_greed`）；Cboe 股票選擇權 put/call 升至 1.05（`speculation.equity_put_call`）；SKEW 149.37、隱含相關性 20.93 創高（`structural.cross_asset_derivatives`）。另一方面，CME FedWatch 顯示 12 月升息 25 bps 的市場隱含機會為 76.8%（`monetary.fedwatch`），CPI YoY 3.72%（2026-09，`monetary.cpi_yoy`），Fed 緩衝跌勢的空間有限。

**判讀：** R1 已走了一半以上的距離，但剩下的 13.23% 需要新的催化劑。窗口內可能的推力包括：12 月 FOMC 真的升息、AI 信用重定價擴散至 IG／HY 指數，或下一輪 hyperscaler 財報出現 capex 下修。若 VIX 持續高於 28 且 HY OAS 明顯走闊，此路徑會成為最可能觸發的一條。

### R2 資本支出收縮

- Microsoft：最新指引將 2026 年資本支出自約 175 下調至約 170（2026-10-29 季報後），方向為**下修**（`ai.hyperscaler_capex`）。來源摘錄未標單位，且 URL slug 另含「190b」字樣，兩者口徑本次未能核對。
- Alphabet：本次證據未取得最新正式指引，方向無法判定。
- Amazon：本次證據未取得最新正式指引，方向無法判定。
- Meta：本次證據未取得最新正式指引，方向無法判定。

已確認下修：1／4 家（Microsoft）。下一輪財報日期本次證據未載；窗口（至 2027-05-09）通常涵蓋兩輪季報。背景：hyperscaler 今年以來發債約 296（2026-11-06），10/29 起一週內 5 筆 AI 相關債券合計約 67（`ai.hyperscaler_financing_mix`），代表 capex 越來越依賴舉債，資本市場收緊時容易被迫刪減。

**判讀：** R2 只差一家，是三條路徑中「步數」最少的一條，但其他三家的指引方向本次未取得，無法確認是否已有第二家下修。若窗口內任一家在財報中下修指引，R2 即成立；Microsoft 的下修幅度約 3%，屬微調而非收縮，目前不足以推斷其他三家跟進。

### R3 AI 信用事件

最接近的候選是 CoreWeave：債券殖利率升破 16%（2026-11-06），五年期 CDS 突破 1,289 bps（2026-11-05）（`valuation.ai_credit_schism`）。這已是困境級信用定價，與 AI 股權仍隱含高成長的狀態形成 AI 信用定價分歧（equity-vs-credit schism），且是信貸端先行重定價的後期訊號。另外 ING 出售 12 筆資料中心貸款，規模約 500（2026-11-06）（`structural.ai_infrastructure_debt`），顯示銀行開始降低 AI infrastructure debt financing 曝險。本次證據未載 CoreWeave 的負債總額、近期到期日或再融資需求，也沒有付款違約、covenant waiver、distressed exchange 或 going-concern 語句。

**判讀：** 信用定價已把 R3 推到可見範圍，但 R3 需要實際違約、破產或完成 distressed exchange，而非只是利差走闊。若窗口內 CoreWeave 或同類 neocloud 在再融資時被迫進行債務交換，或流動性斷裂，R3 成立並可能反向觸發 R1。

## 支持 yes 的證據

- [R3] CoreWeave 五年期 CDS 突破 1,289 bps（2026-11-05）、債券殖利率升破 16%（2026-11-06），信用市場已按困境水準定價，是 R3 最直接的前導訊號（`valuation.ai_credit_schism`）。
- [R1] NASDAQ-100 2026-11-06 收盤 26,989.99，距 52 週高點回撤 13.56%，約一個月內完成，已過 R1 門檻一半以上（`valuation.ndx_drawdown`）。
- [R2] Microsoft 2026-10-29 將 2026 年 capex 指引自約 175 下修至約 170，R2 已有 1／4 家（`ai.hyperscaler_capex`）。
- [整體] 市場已轉入恐慌：Fear & Greed 22（2026-11-06），VIX 28.18（2026-11-05），put/call 1.05（2026-11-05），SKEW 149.37（2026-11-06）（`retail.fear_greed`、`structural.vix_spx_comove`、`speculation.equity_put_call`、`structural.cross_asset_derivatives`）。
- [整體] 貨幣條件反向收緊：FedWatch 12 月升息隱含機會 76.8%（2026-11-06），CPI YoY 3.72%（2026-09），Fed 在 AI 主導的跌勢中缺乏降息緩衝（`monetary.fedwatch`、`monetary.cpi_yoy`）。
- [R3] ING 出售 12 筆資料中心貸款（2026-11-06），且 hyperscaler 今年以來發債約 296（2026-11-06），AI 建設融資轉向債務、銀行端開始減碼（`structural.ai_infrastructure_debt`、`ai.hyperscaler_financing_mix`）。
- [整體] 估值仍高，下行空間大：Shiller CAPE 38.91、S&P 500 trailing P/E 25.14（2026-11-06），Mag 7 前瞻 P/E 約 28.3（`valuation.sp500_pe_cape`、`valuation.mag7_multiples`）。

## 支持 no 的證據

- [整體] 基準率：任一 182 天窗口內三條路徑皆不成立是常態；目前三條路徑都未取得實際觸發，R1 仍需再跌約 13.23%，R2 只確認 1／4 家，R3 無違約事件（`valuation.ndx_drawdown`、`ai.hyperscaler_capex`）。
- [R3] 廣義信用尚未確認 AI 信用壓力：HY OAS 3.48%、IG OAS 0.93%（2026-11-05），自 2026-10-16 僅分別走闊 17 bps 與 8 bps，仍屬偏緊水位（`monetary.hy_oas`、`monetary.ig_oas`）。
- [整體] 資金市場平靜：SOFR 3.92% 對 IORB 3.90% 僅 2 bps，SOFR99 4.00%（2026-11-05），SRF 動用（RPONTTLD）0（2026-11-06）；MOVE 自 101.1 降至 92.77（2026-11-06），沒有國債市場失序跡象（`monetary.repo_stress_srf`、`structural.treasury_basis_trade`）。
- [R1] S&P 500 7,353.73（2026-11-05）仍高於 200 日均線 0.42%，廣義指數尚未跌破長期趨勢，跌勢集中於 AI 權重股（`valuation.sp500_trend`）。
- [R2] AI 終端需求仍在擴張：Anthropic 已遞交 S-1，目標估值 1.5 兆至 2 兆（2026-10-26），上半年營收 16.3；年化 AI 終端營收 Anthropic 65＋OpenAI 約 70，合計約 135（2026-09-30），降低 hyperscaler 集體刪減 capex 的誘因（`speculation.upcoming_ai_ipos`、`ai.openai_anthropic_revenue`、`ai.revenue_capex_gap`）。
- [整體] 10 年期利率下行緩和估值壓力：DGS10 4.84%（2026-11-05），自 2026-10-16 下降 25 bps（`monetary.dgs10`）。

## 與前期比較

前次結論：無前次預測（report-2026-10-18 為舊格式評分報告）

前次為舊格式評分報告，不轉換為 yes／no；以下為自 2026-10-18 以來的主要證據變化：

- NASDAQ-100 自 2026-10-06 高點 31,224.69 回落至 26,989.99（2026-11-06），回撤擴大至 13.56%；S&P 500 自 2026-10-16 下跌 3.99%。
- VIX 自 19.99（2026-10-16）升至 28.18（2026-11-05）；HY OAS 走闊 17 bps 至 3.48%，IG OAS 走闊 8 bps 至 0.93%。
- 10Y 殖利率 −25 bps、實質殖利率 −14 bps、breakeven −12 bps；T10YIE 與另兩腿視窗不一致，本次 10Y Δ 分解判讀為不可判（視窗不一致）。
- CoreWeave 信用定價跳升至困境水準（CDS 1,289 bps），Microsoft 下修 capex 指引，ING 出售資料中心貸款，均為前次之後的新事件。
- 市場 12 月升息預期升至 76.8%，WTI 自 108.21 降至 99.64（−7.92%）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源檢索完成但無合格當期披露（✗ NOT DISCLOSED），不作為證據引用：`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.treasury_auctions`、`monetary.private_credit_liquidity`、`ai.token_growth`、`ai.depreciation_life`、`structural.global_leveraged_approvals`，以及 `ai.capital_cycle`（quarterly_state 無可用增速披露；event_scan 有 Microsoft 取消 Nscale 英國資料中心交易一筆，但複合狀態仍為 ✗ NOT DISCLOSED）。其中 `monetary.private_credit_liquidity` 的缺漏最可能影響答案：若私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）已出現 gate proration / breach，R3 傳導會更快，但本次 30 日內無披露。

資料品質注意：
- `ai.hyperscaler_capex` 雖標為 ✓ SEARCH-VERIFIED，實際僅取得 Microsoft 一家；Alphabet、Amazon、Meta 的最新指引本次未取得。這是對 R2 判讀影響最大的缺口：若其中一家已下修，R2 已經成立。
- `structural.treasury_basis_trade`：搜尋記錄顯示 script 三區塊 fetch_failed 並走 WebSearch fallback（MOVE 93.88，2026-11-04），但本次 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 皆為 status ok；依 artifact 為準記 ✓ API，fallback 值不採用。
- Microsoft capex 數值未標單位，且來源 URL slug 含「190b」，數值口徑未能核對。

最大不確定性：
1. 其他三家 hyperscaler 的下一次 capex 指引（日期本次未載）：任一家下修即可使 R2 成立，會把答案推向 yes。
2. CoreWeave 的負債規模、到期結構與再融資進度（本次證據未載）：若出現 distressed exchange 或付款違約，R3 成立並可能帶動 R1，推向 yes。
3. 12 月 FOMC：若照市場預期升息，股市估值與 AI 融資成本同時承壓，推向 yes；若暫停，則支持 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7353.73 | FRED API (series_id=SP500) sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 0.42 | FRED API (series_id=SP500) sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 1.84 | FRED API (series_id=SP500) sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 26989.99 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 13.56 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026-Q2 季資料，%） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（%） | 4.00 | FRED API (series_id=DFEDTARU) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（%） | 3.75 | FRED API (series_id=DFEDTARL) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 3.48 | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.93 | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.84 | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.60 | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.23 | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD／桶） | 99.64 | FRED API (series_id=DCOILWTICO) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料，%） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.17 | FRED API (series_id=T5YIFR) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（%，Kim-Wright） | 0.9089 | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.92 | FRED API (series_id=SOFR) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 4.00 | FRED API (series_id=SOFR99) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.90 | FRED API (series_id=IORB) | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,748,145（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,945,410（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,261,882（¥626.19T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED API (series_id=VIXCLS) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of；base_date 2026-10-29，window_days 7） | 28.18 | FRED API vix_spx_comove block | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 63.84 | FRED API vix_spx_comove block | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -4.75 | FRED API vix_spx_comove block | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2111.0042（$2.11T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六檔 UST 期貨槓桿基金淨部位，口） | -7249305 | CFTC TFF futures-only cftc_lev_funds | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -489473 | CFTC TFF futures-only cftc_lev_funds | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo Finance chart API (^MOVE) move_index | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2326.9 | OFR STFM (REPO-TRIV1_TV_TOT-P) ofr_repo | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebFetch | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED（EPS／PE 分解未披露） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（季頻 stock-of-state） | ✓ SEARCH-VERIFIED（僅取得 Microsoft；Alphabet、Amazon、Meta 未取得） |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch（quarterly_state stock-of-state＋event_scan 30d） | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch（季頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch（quarterly_state stock-of-state＋event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED（僅取得半導體 3 倍多頭基金） |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py（cftc_lev_funds、move_index、ofr_repo） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻本益比約 28.3 | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein 將 TSMC 目標價由 554 上調至 600（EPS／PE 分解未披露） | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/ | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 五年期 CDS 突破 1,289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | RSP 等權指數年初至今報酬約 14.13 | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大成分股權重約 37.9 | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲家數 1,474 對下跌 1,252 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 22（極度恐懼） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 1.48 兆美元、年增約 31.4 | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1、看空 48.4 | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔 | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | 12 月升息 25 bps 隱含機會 76.8 | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000 | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年 capex 指引自約 175 下調至約 170 | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3 | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle 剩餘履約義務（RPO）638 | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87 | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 今年以來發債 296 | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 10/29 起一週內 5 筆 AI 相關債券發行合計 67 | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic 65＋OpenAI 約 70，合計約 135 | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] Microsoft 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO 週漲 8 | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描（0 件符合 2＋主題×弱基本面） | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件合格） | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe 股票選擇權 put/call 升至 1.05 | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭基金 10 月底規模 24.31、當月淨流入 7.27 | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 2026-09 月總結算量 1,486,062,415 | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
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

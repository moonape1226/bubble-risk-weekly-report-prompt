> [DRY RUN] this report was not committed to archive.

# 2026-11-08 AI 泡沫破裂預測報告

報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：report-2026-10-18（21天前）

## 結論

**結論：no**

三條路徑都已出現壓力，但沒有一條被證據顯示會在 2027-05-09 前完成：R1 NASDAQ-100 距 52 週高點回撤 13.56%，仍需自最新收盤再跌約 13.23% 才觸線；R2 目前僅 Microsoft 一家被報導下修 capex 指引（且來源口徑有疑義），其餘三家本次未取得指引；R3 的 CoreWeave CDS 1289 bps、債券殖利率逾 16% 屬困境定價，但未見付款違約或 distressed exchange，且其負債規模本次未經來源確認，而 HY OAS 3.48% 顯示整體信用尚未傳導。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

`valuation.ndx_drawdown`：NASDAQ-100 最新收盤 26,989.99（2026-11-06），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 13.56%；R1 門檻水位 23,418.52，自最新收盤再下跌約 13.23% 即觸線。回撤在一個月內形成，2026-11-05 收盤曾低至 26,629.81。同期 S&P 500 為 7,353.73（2026-11-05），僅高於 200 日均線 0.42%、高於 52 週均線 1.84%，較前次基準日下跌 3.99%（`valuation.sp500_trend`）。VIX 於 2026-11-05 升至 28.18，7 日內 +63.84%，S&P 500 同窗 −4.75%，屬正常的股跌波動升，不是 crowded-optionality 共振（`structural.vix_spx_comove`）。情緒端 CNN Fear & Greed 22（極度恐懼，2026-11-06，`retail.fear_greed`）、AAII 看空 48.4%（2026-11-04，`retail.aaii`）、Cboe 股票賣買權比 1.05（2026-11-05，`speculation.equity_put_call`），顯示去槓桿與避險已在進行。估值仍高：Shiller CAPE 38.91、trailing P/E 25.14（2026-11-06，`valuation.sp500_pe_cape`）。宏觀面 CME FedWatch 顯示 12 月升息 25 bps 的市場隱含勝算 76.8%（2026-11-06，`monetary.fedwatch`），CPI YoY 3.72%（2026-09，`monetary.cpi_yoy`），Fed 緩衝下跌的空間有限。

**判讀：** 已走完約一半距離（13.56% / 25%），但仍需再跌約 13.23%。窗口內可推動觸線的催化劑包括 12 月 FOMC 升息、下一輪 hyperscaler 財報對 capex 的再下修，以及 R3 信用事件外溢；若無這些催化，情緒已在極度恐懼區，反彈與觸線同樣可能，目前證據不足以判定觸線較可能發生。

### R2 資本支出收縮

`ai.hyperscaler_capex`：本次取得的指引只有 Microsoft——2026 年 capex 指引自約 175 下調至約 170（2026-10-29 報導，方向：下修）。注意該來源 URL 標題寫「Q3 FY2026」與「190b capex」，與摘錄的 175 → 170 口徑不一致，本次無法確認下修所對應的財年與單位。Alphabet、Amazon、Meta 的最新指引與方向本次未取得（未提供指引／未確認），故目前已下修家數為 1（待確認）/ 4，R2 需 2 家。下一次財報日期本次未經來源確認；以季度節奏推估窗口內至少還有一輪財報，但不列為已證實的日期。旁證：hyperscaler 今年以來發債約 296（2026-11-06），10/29 起一週內 5 筆 AI 相關債券合計約 67（`ai.hyperscaler_financing_mix`），顯示融資仍暢通、capex 以發債支撐而非被迫收縮；Oracle RPO 638（2026-08-31，`ai.customer_concentration_rpo`）顯示 backlog 仍大，但同一 counterparty 重複計算本次無法量化。

**判讀：** R2 距離解析最近的是「再一家下修」。若 Microsoft 的下修屬實，只需 Alphabet、Amazon、Meta 任一家在窗口內的財報下修即成立；但其餘三家目前方向不明、融資市場仍大量吸納 hyperscaler 債券，本次證據不支持「第二家下修較可能發生」。

### R3 AI 信用事件

`valuation.ai_credit_schism`：CoreWeave 五年期 CDS 突破 1289 bps（2026-11-05），債券殖利率升破 16%（2026-11-06）；報導同時提到 NASDAQ 反彈而 CDS 仍在 1,000 bps 以上，屬「信貸先重定價、股價未跟上」的後期訊號。CoreWeave 以 AI 算力為主業，但其總負債是否 ≥ 50 億美元本次未經來源確認，近期到期與再融資需求也未取得。`structural.ai_infrastructure_debt`：ING 出售 12 筆資料中心貸款，規模約 500（2026-11-06），顯示銀行端開始降低 AI 資料中心曝險。本次未見任何借款人的破產申請、寬限期後付款違約、covenant waiver 或 distressed exchange 報導。整體信用尚未傳導：HY OAS 3.48%（+17 bps vs 2026-10-16，`monetary.hy_oas`）、IG OAS 0.93%（`monetary.ig_oas`），repo 資金壓力（SOFR−IORB）僅 2 bps、SRF 動用 0（`monetary.repo_stress_srf`）。

**判讀：** R3 的定價訊號是三條路徑中最強的，但解析需要實際的破產、超過寬限期的違約或完成 distressed exchange；CDS 1289 bps 反映市場對中期違約的高度擔憂，並不等於 182 天內必然違約。若窗口內出現 CoreWeave 或同類 neocloud 錯過付息、啟動債務交換、或再融資失敗，R3 即可能成立並同時推動 R1。

## 支持 yes 的證據

- [R3] CoreWeave 五年期 CDS 突破 1289 bps（2026-11-05）、債券殖利率升破 16%（2026-11-06），AI 信用已出現困境級定價，且股價反彈未帶動 CDS 回落 `valuation.ai_credit_schism`
- [R1] NASDAQ-100 一個月內自 31,224.69（2026-10-06）跌至 26,989.99（2026-11-06），距 52 週高點回撤 13.56%，已走完 R1 門檻約一半 `valuation.ndx_drawdown`
- [R2] Microsoft 2026 年 capex 指引自約 175 下調至約 170（2026-10-29 報導），R2 所需兩家中已可能有一家 `ai.hyperscaler_capex`
- [整體] CME FedWatch 顯示 12 月升息 25 bps 的市場隱含勝算 76.8%（2026-11-06），CPI YoY 3.72%（2026-09），貨幣政策朝收緊方向，削弱 Fed 對 AI 主導下跌的緩衝 `monetary.fedwatch` `monetary.cpi_yoy`
- [R3] ING 出售 12 筆資料中心貸款，規模約 500（2026-11-06），銀行開始卸下 AI 資料中心曝險 `structural.ai_infrastructure_debt`
- [R1] VIX 7 日內 +63.84% 至 28.18（2026-11-05）、隱含相關性 20.93 創高、SKEW 149.37（2026-11-06），避險需求與系統性連動同步升高 `structural.vix_spx_comove` `structural.cross_asset_derivatives`
- [整體] 估值仍處高位：Shiller CAPE 38.91、trailing P/E 25.14（2026-11-06），前十大成分股權重約 37.9%（2026-11-01），融資餘額約 1.48 兆美元、年增約 31.4%（2026-09），下跌時的放大空間大 `valuation.sp500_pe_cape` `breadth.top10_concentration` `retail.margin_debt`

## 支持 no 的證據

- [整體] 基準率：三個解析條件在任意 182 天窗口內都不常見；本次沒有任何一條路徑已有完成中的事件（無違約、僅一家可能下修、回撤距門檻仍約 13.23%） `valuation.ndx_drawdown` `ai.hyperscaler_capex`
- [R3] 整體信用未傳導：HY OAS 3.48%、IG OAS 0.93%（2026-11-05），repo 資金壓力（SOFR−IORB）2 bps、SRF 動用 0（2026-11-05／2026-11-06） `monetary.hy_oas` `monetary.ig_oas` `monetary.repo_stress_srf`
- [R2] hyperscaler 融資仍暢通：今年以來發債約 296、10/29 起一週內 5 筆 AI 相關債券合計約 67（2026-11-06），capex 仍有資金來源，不需被迫收縮 `ai.hyperscaler_financing_mix`
- [R1] 情緒已極度悲觀：Fear & Greed 22（2026-11-06）、AAII 看空 48.4%（2026-11-04）、股票賣買權比 1.05（2026-11-05），反向指標顯示短期拋壓已大量釋放 `retail.fear_greed` `retail.aaii` `speculation.equity_put_call`
- [R1] 寬度未崩：S&P 500 仍高於 200 日均線 0.42%（2026-11-05），等權指數年初至今約 +14.13%（2026-11-06），紐交所上漲 1,474 對下跌 1,252（2026-11-06） `valuation.sp500_trend` `breadth.rsp_spy` `breadth.advance_decline`
- [整體] AI 需求與資本市場仍在擴張：Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆（2026-10-26），上半年營收 16.3；年化 AI 終端營收（Anthropic＋OpenAI）約 135（2026-09-30） `speculation.upcoming_ai_ipos` `ai.openai_anthropic_revenue` `ai.revenue_capex_gap`
- [整體] 美債市場未見失序：MOVE 92.77（2026-11-06，較 2026-10-16 下降 8.33），OFR tri-party repo transaction volume 2,326.9（十億美元，2026-11-06） `structural.treasury_basis_trade`

## 與前期比較

前次結論：無前次預測（report-2026-10-18 為舊格式評分報告）

前次為 2026-11 改版前的舊格式評分報告，其分數不轉譯為 yes/no，flip_evidence 為空。自 2026-10-18 以來的主要變化：

- NASDAQ-100 自 2026-10-06 高點回撤至 13.56%；S&P 500 較 2026-10-16 下跌 3.99%（`valuation.ndx_drawdown`、`valuation.sp500_trend`）。
- AI 信用定價急劇惡化：CoreWeave CDS 突破 1289 bps、殖利率逾 16%（`valuation.ai_credit_schism`）。
- 10Y 殖利率 −25 bps 至 4.84%、HY OAS +17 bps 至 3.48%、WTI −7.92% 至 99.64（`monetary.dgs10`、`monetary.hy_oas`、`monetary.wti`）。
- Microsoft capex 指引被報導下修（`ai.hyperscaler_capex`）；市場轉為定價 12 月升息（`monetary.fedwatch`）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED（搜尋完成但窗口內無合格披露）：NAAIM、BofA／JPM 調查、美債標售需求、私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）、AI token growth、折舊年限變動（depreciation useful-life change）、全球槓桿商品核准，以及資本週期階段（capital cycle stage；quarterly_state 未取得增速證據，event_scan 有 Microsoft 取消 Nscale 英國資料中心交易的 2026-11-04 報導，但依 aggregation all 整體不成立，故不作為正式證據）。其中私募信貸贖回壓力若出現 gate proration / breach 或 net inflow→outflow flip，會強化 R3；本次缺漏可能低估 R3 壓力，但不足以單獨改變答案。

資料一致性註記：

- 案例檢索紀錄把美債基差交易槓桿標為「script 三區塊 fetch_failed → WebSearch fallback」（MOVE 93.88，2026-11-04），但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 三塊皆為 `status: ok`；本報告以 artifact 為準（MOVE 92.77，2026-11-06），未採用 fallback 數值。
- Microsoft capex 下修的來源 URL 標題（Q3 FY2026、190b）與摘錄數值（175 → 170）口徑不符，R2 的「1 家」需以 Microsoft 正式文件確認。
- 10Y 分解：ΔDGS10 −25 bps、ΔDFII10 −14 bps、ΔT10YIE −12 bps，T10YIE 視窗與另兩腿不同，判讀為不可判（視窗不一致）。

最大的不確定性：

1. Alphabet、Amazon、Meta 的最新 capex 指引方向本次未取得——若其中任一家已下修或在窗口內財報下修（且 Microsoft 下修屬實），R2 即成立，答案會轉向 yes。
2. CoreWeave 的負債規模、近期到期與再融資安排未經確認——若確認負債 ≥ 50 億美元且有窗口內的大額到期或付息壓力，R3 的完成可能性會顯著上升，推向 yes。
3. 12 月 FOMC 是否真的升息——升息將加重高估值資產的折現壓力並可能推動 R1；若改為按兵不動，則支持 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7353.73 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 0.42 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 1.84 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較前次基準 %） | -3.99 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 26989.99 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 13.56 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2 季資料，%） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（%） | 4.0 | FRED API (series_id=DFEDTARU) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（%） | 3.75 | FRED API (series_id=DFEDTARL) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 3.48 | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 17.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.93 | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.84 | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | -25.0 | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.6 | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | -14.0 | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.23 | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | -12.0 | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（美元／桶） | 99.64 | FRED API (series_id=DCOILWTICO) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO chg_pct | -7.92 | FRED API (series_id=DCOILWTICO) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料，%） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.17 | FRED API (series_id=T5YIFR) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（%，Kim-Wright） | 0.9089 | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7d） | -2.7 | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.92 | FRED API (series_id=SOFR) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 4.0 | FRED API (series_id=SOFR99) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.9 | FRED API (series_id=IORB) | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,748,145（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,945,410（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,261,882（¥626.19T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED API (series_id=VIXCLS) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（7 日窗，base 2026-10-29） | 28.18 | FRED API（fetch_macro 區塊） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 63.84 | FRED API（fetch_macro 區塊） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -4.75 | FRED API（fetch_macro 區塊） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2111.0042（$2.11T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7249305 | CFTC TFF futures-only | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -489473 | CFTC TFF futures-only | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo Finance chart API (^MOVE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2326.9 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebFetch | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED（EPS／PE 分解未披露） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | fetch_macro.py sp500_trend | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED（new high/low 未取得） |
| retail.fear_greed | Retail / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail / Margin Debt: FINRA | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED（margin debt／市值比未取得） |
| retail.aaii | Retail / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail / Social sentiment proxies | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail / Household equity allocation | fetch_macro.py BOGZ1FL153064486Q | ✓ API |
| retail.naaim | Retail / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary / Fed funds rate: FRED | fetch_macro.py DFEDTARU＋DFEDTARL | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary / High Yield OAS | fetch_macro.py BAMLH0A0HYM2 | ✓ API |
| monetary.ig_oas | Monetary / Investment Grade OAS | fetch_macro.py BAMLC0A0CM | ✓ API |
| monetary.dgs10 | Monetary / 10Y Treasury yield | fetch_macro.py DGS10 | ✓ API |
| monetary.dfii10 | Monetary / 10Y Treasury real yield | fetch_macro.py DFII10 | ✓ API |
| monetary.t10yie | Monetary / 10Y breakeven inflation rate | fetch_macro.py T10YIE（FRED 直接取得） | ✓ API |
| monetary.wti | Monetary / WTI crude oil price | fetch_macro.py DCOILWTICO | ✓ API |
| monetary.cpi_yoy | Monetary / CPI YoY: FRED | fetch_macro.py CPIAUCSL yoy_pct | ✓ API |
| monetary.t5yifr | Monetary / 5y5y forward inflation expectation | fetch_macro.py T5YIFR | ✓ API |
| monetary.term_premium | Monetary / 10Y 期限溢價（term premium）: FRED | fetch_macro.py THREEFYTP10 | ✓ API |
| monetary.repo_stress_srf | Monetary / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py SOFR／SOFR99／IORB／RPONTTLD | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary / 美債標售需求 | WebSearch（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary / Fed funds rate path expectations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary / Fed balance sheet: FRED | fetch_macro.py WALCL | ✓ API |
| monetary.ecb_boj | Monetary / Global central bank liquidity cross-check | fetch_macro.py ECBASSETSW＋JPNASSETS | ✓ API（ECBASSETSW ok；JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED（僅 Microsoft；GOOGL／AMZN／META 未取得） |
| ai.token_growth | AI / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration | WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構 | WebSearch：quarterly_state stock-of-state；event_scan 30d | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口 | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI / 資本週期階段 | WebSearch：quarterly_state stock-of-state（無增速證據）；event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculation / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED（1 件） |
| speculation.ipo_heat | Speculation / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculation / Microcap thematic moonshots | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculation / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculation / Insider selling at AI | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculation / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED（僅半導體 3 倍多頭） |
| structural.us_single_stock_etf | Structural / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural / 0DTE option volume | WebSearch（Cboe 月報） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural / VIX / S&P 500 co-movement | fetch_macro.py VIXCLS＋vix_spx_comove | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural / Bank loans to nondepository financial institutions | fetch_macro.py LNFACBW027SBOG | ✓ API |
| structural.treasury_basis_trade | Structural / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py cftc_lev_funds／move_index／ofr_repo（artifact 三塊皆 ok） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻本益比約 28.3 | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/（Vested Finance；原定來源 Mag 7 weighted P/E） | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein TSMC 目標價 554 → 600（EPS／PE 分解未披露） | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/（StockAnalysis） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html（CNBC） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 五年期 CDS 突破 1289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds（Coinpaper） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | 等權指數（RSP）年初至今報酬約 14.13% | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY（Total Real Returns） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大成分股權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration（Chartrow） | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | 紐交所上漲 1,474 對下跌 1,252 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/（McClellan） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 22（極度恐懼） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/（Finhacker；原定來源 cnn.com） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 1.48 兆美元、年增約 31.4% | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt（原定來源 FINRA） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives（AAII） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔 | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week（Benzinga） | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | 12 月升息 25 bps 隱含勝算 76.8% | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/（24/7 Wall St.；原定來源 CME FedWatch） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000 | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee（BigGo Finance） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年 capex 指引自約 175 下調至約 170（URL 標題口徑 190b，待確認） | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex（Global Data Center Hub） | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3 | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html（Yahoo Finance） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle RPO 638 | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/（Motley Fool） | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87 | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends（GetDeploying） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 今年以來發債約 296 | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era（404K Research，引 Goldman） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 10/29 起一週內 5 筆 AI 相關債券發行合計約 67 | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era（404K Research，引 Goldman） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 Anthropic 65＋OpenAI 約 70，合計約 135（分母僅 Microsoft capex 約 170 可用） | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html（Yahoo Finance） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] Microsoft 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281（Investing.com，引 Bloomberg） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics 完成 SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/（Securities.io） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO 週漲 8 | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears（Renaissance Capital） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描（0 件符合 2+ 主題×弱基本面） | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1（Built In） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件合格） | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe 股票選擇權賣買權比升至 1.05（日讀數／5 日均值未標明） | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide（Seeking Alpha） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭基金 10 月底規模 24.31、當月淨流入 7.27 | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html（Yahoo Finance） | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026（Cboe via PR Newswire） | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 總結算量（2026-09 月資料）1,486,062,415 | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report（OCC） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性創高 20.93 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026（Saxo） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.margin_debt_crosscheck | 融資餘額交叉檢核基數約 1.48 兆美元（2026-09 月資料） | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt（原定來源 FINRA） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
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
  "r1_drawdown_pct": 13.56,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

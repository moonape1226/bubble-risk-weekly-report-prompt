> [DRY RUN] this report was not committed to archive.

# 2026-11-08 AI 泡沫破裂預測報告

報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：report-2026-10-18（21天前）

## 結論

**結論：yes**

三條路徑同時已啟動而非僅停留在估值偏高：R2 已有一家（Microsoft，2026-10-29 將 2026 年 capex 指引自約 175 下修至約 170）下修，只差一家即成立；R3 端 CoreWeave 5 年 CDS 突破 1289 bps、債券殖利率升破 16%（2026-11-05／11-06），屬困境定價。市場同時定價 12 月升息（FedWatch 76.8%）、CPI YoY 3.72%，Fed 緩衝空間有限，使 R1（NASDAQ-100 已回撤 13.56%）與 R2／R3 相互傳導的路徑在 182 天內完成的可能性高於不完成。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

依 `valuation.ndx_drawdown`：NASDAQ-100 最新收盤 26,989.99（2026-11-06），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 13.56%。R1 門檻水位 23,418.52；自最新收盤再下跌約 13.23%（約 3,571 點）即觸發 R1。高點距今僅一個月，回撤速度快。同期 S&P 500 收 7,353.73（2026-11-05），較 2026-10-16 的 7,659.44 下跌 3.99%，距 200 日均線僅 +0.42%、距 52 週均線 +1.84%（`valuation.sp500_trend`），趨勢延伸已大致消化。VIX 7 日由 17.2 升至 28.18（+63.84%），S&P 500 同窗 −4.75%，屬一般 risk-off 而非 crowded-optionality 同向上漲（comove=false，`structural.vix_spx_comove`）。情緒端 CNN Fear & Greed 22（極度恐懼，`retail.fear_greed`）、AAII 看空 48.4%（`retail.aaii`）、Cboe 股票賣買權比 1.05（`speculation.equity_put_call`）。

**判讀：** R1 已走完約一半距離（13.56% / 25%），需要再跌約 13.23%。若 R3 信用事件或第二家 hyperscaler 下修 capex 在窗口內出現，加上 Fed 因通膨無法降息托底，這段跌幅在 6 個月內完成並不罕見；反之若升息落地後市場消化、信用未擴散，指數可能在現水位築底。

### R2 資本支出收縮

依 `ai.hyperscaler_capex`（2026-10-29）：

- Microsoft：2026 年 capex 指引自約 175 下修至約 170（Q3 財報週期，2026-10-29）——**下修**。
- Alphabet：本次證據未取得其最新指引——未提供指引（本次未取得）。
- Amazon：本次證據未取得其最新指引——未提供指引（本次未取得）。
- Meta：本次證據未取得其最新指引——未提供指引（本次未取得）。

截至目前四家中已有 1 家下修。下一輪財報日期本次未取得；依季報節奏，窗口（至 2027-05-09）預期涵蓋下兩輪 hyperscaler 季報。相關訊號：hyperscaler 今年以來發債 296、10/29 起一週內 5 筆 AI 相關債券合計 67（`ai.hyperscaler_financing_mix`，2026-11-06），融資結構正從現金流轉向發債；年化 AI 終端營收約 135（Anthropic 65 ＋ OpenAI 約 70，2026-09-30）對年化 capex 約 170（分母：僅 Microsoft，其餘三家與 Oracle 本次未取得），缺口方向因無前次組合值本次不判定（`ai.revenue_capex_gap`）。

**判讀：** R2 只差一家。Microsoft 已下修且收緊 neocloud 專案監管，若 Alphabet／Amazon／Meta 任一家在窗口內兩輪財報之一跟進下修（尤其在 R1 回撤加深、發債成本上升的情境下），R2 即成立；反向風險是 Microsoft 的下修幅度僅約 3%，另三家可能維持或上修。

### R3 AI 信用事件

依 `valuation.ai_credit_schism`：CoreWeave 債券殖利率升破 16%（2026-11-06，CNBC），5 年 CDS 突破 1289 bps（2026-11-05）——同期整體 HY OAS 僅 3.48%（+17 bps，`monetary.hy_oas`）、IG OAS 0.93%（`monetary.ig_oas`），AI 信用定價分歧明顯：AI 基建信用已重定價、廣義信用尚未跟進。依 `structural.ai_infrastructure_debt`：ING 出售 12 筆資料中心貸款、規模約 500（2026-11-06），銀行正在降低 AI 資料中心曝險。CoreWeave 的負債規模、近期到期與再融資時程本次證據未載明，是否達 R3 的 50 億美元門檻需以其財報確認；本次未見付款違約、covenant waiver、distressed exchange 或 going-concern 字眼。

**判讀：** CDS 逾 1000 bps 屬困境定價，但 R3 需要實際破產、超過寬限期違約或完成 distressed exchange。若 Microsoft 對 neocloud 的收縮延續到 CoreWeave 類借款人的合約或再融資，且銀行持續出售資料中心貸款，窗口內出現 distressed exchange 的路徑是可信的；目前仍屬「定價先行、事件未到」。

## 支持 yes 的證據

- [R2] Microsoft 於 2026-10-29 將 2026 年 capex 指引自約 175 下修至約 170，R2 所需兩家已有一家完成，`ai.hyperscaler_capex`。
- [R3] CoreWeave 5 年 CDS 突破 1289 bps（2026-11-05）、債券殖利率升破 16%（2026-11-06），AI 基建信用已進入困境定價區，`valuation.ai_credit_schism`。
- [R1] NASDAQ-100 一個月內距 52 週高點回撤 13.56%（高點 2026-10-06，最新 2026-11-06），已走完 R1 約一半距離，`valuation.ndx_drawdown`。
- [整體] 市場定價 12 月升息 25 bps 達 76.8%（2026-11-06），CPI YoY 3.72%（2026-09），Fed 無法以降息緩衝 AI 主導的下跌，`monetary.fedwatch`、`monetary.cpi_yoy`、`monetary.fed_funds`。
- [R3] ING 出售 12 筆資料中心貸款、規模約 500（2026-11-06），銀行端開始降低 AI 資料中心曝險，`structural.ai_infrastructure_debt`。
- [R1] VIX 7 日由 17.2 升至 28.18（+63.84%）、Fear & Greed 22（極度恐懼）、股票賣買權比 1.05（2026-11-05/06），風險偏好快速反轉，`structural.vix_spx_comove`、`retail.fear_greed`、`speculation.equity_put_call`。
- [R2] hyperscaler 今年以來發債 296、10/29 起一週 5 筆 AI 相關債券合計 67（2026-11-06），capex 越來越依賴舉債而非 FCF，`ai.hyperscaler_financing_mix`。

## 支持 no 的證據

- [整體] 基準率：任意 182 天窗口內 R1–R3 皆不成立是常態；R2 仍差一家、R3 尚無任何實際違約或 distressed exchange，`ai.hyperscaler_capex`、`valuation.ai_credit_schism`。
- [R3] 廣義信用與資金市場平穩：HY OAS 3.48%、IG OAS 0.93%（2026-11-05），SOFR−IORB 2 bps、SOFR99−IORB 10 bps、SRF 動用 0（2026-11-05/06），尚無系統性傳導，`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`。
- [R2] hyperscaler 債市通道仍暢通：一週內 5 筆 AI 相關債券合計 67 順利發行（2026-11-06），融資能力未受限，`ai.hyperscaler_financing_mix`。
- [R1] S&P 500 仍高於 200 日均線 0.42%、52 週均線 1.84%（2026-11-05），NASDAQ-100 尚需再跌約 13.23% 才達 R1，`valuation.sp500_trend`、`valuation.ndx_drawdown`。
- [整體] 資本市場仍願意為 AI 定高價：Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆（2026-10-26）；半導體 3 倍多頭 ETF 10 月淨流入 7.27、規模 24.31（2026-10-31），逢低買盤仍在，`speculation.upcoming_ai_ipos`、`structural.leveraged_etf_aum`。
- [R2] Microsoft 下修幅度僅約 3%（約 175 → 約 170），H100 隨選租金中位數 3.87（2026-11-03）未見崩跌，需求端未出現明確利用率塌陷，`ai.hyperscaler_capex`、`ai.compute_supply_demand`。

## 與前期比較

前次結論：無前次預測（report-2026-10-18 為舊格式評分報告）

前次為 2026-11 改版前的舊格式評分報告，其分數不轉換為 yes/no，本次為首份 yes/no 預測；flip_evidence 為空。自 2026-10-18 以來的主要變化：

- NASDAQ-100 自 2026-10-06 高點回撤至 13.56%；S&P 500 自 2026-10-16 起下跌 3.99%。
- 10Y 殖利率 −25 bps 至 4.84%、10Y 實質殖利率 −14 bps、10Y breakeven −12 bps（視窗不一致，driver 不可判（視窗不一致））。
- HY OAS +17 bps、IG OAS +8 bps；VIX 由 19.99（2026-10-16）升至 28.18。
- Microsoft 2026-10-29 下修 capex 指引；CoreWeave CDS 突破 1289 bps。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED（檢索完成但無合格當期披露）：`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.treasury_auctions`、`monetary.private_credit_liquidity`、`ai.token_growth`、`ai.depreciation_life`、`ai.capital_cycle`（quarterly_state 無可用增速披露；event_scan 有一筆：Microsoft 10 月取消 Nscale 英國資料中心交易、規模約 3，2026-11-04，指向週期轉折，但因 composite 規則整體不得作為證據引用）、`structural.global_leveraged_approvals`。其中私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）缺當期披露最可能影響判斷：若出現 gate proration / breach 或 net inflow→outflow flip，R3 傳導會更快，強化 yes。

資料品質註記：

- `ai.hyperscaler_capex` 僅取得 Microsoft；Alphabet／Amazon／Meta 最新指引本次未取得。另該結果 URL 字串含「190b」，與摘錄數值（約 175 → 約 170）不一致、單位未標。若 Microsoft 的「下修」判讀有誤，R2 回到 0/4，yes 的最強支柱會消失——這是本次判斷最大的資料風險。
- 證據檔將美債基差交易槓桿標為「script 三區塊 fetch_failed → WebSearch fallback」（MOVE 93.88，2026-11-04），但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 三塊皆為 `status: ok`；依決策分支以 artifact 為準（MOVE 92.77，2026-11-06），未採用該搜尋值。
- `ai.customer_concentration_rpo` 的 Oracle RPO 638 資料日 2026-08-31，但結果 URL 路徑日期為 2026-07-02，日期歸屬有疑義，僅作背景。多家供應商對同一 counterparty 的承諾金額本次未取得，backlog 重複計算風險（RPO double-counting）無法量化。
- 多項摘錄數值（hyperscaler 發債、AI 營收、ING 貸款規模）來源未標單位。

最大不確定性：

1. 下兩輪 hyperscaler 財報（日期本次未取得）：Alphabet／Amazon／Meta 任一家下修即解析 R2 為 yes；三家皆維持或上修會削弱 yes。
2. CoreWeave 的負債規模與再融資時程未取得：若其到期牆落在窗口內且 CDS 維持 1000 bps 以上，R3 走向 yes；若完成再融資，R3 路徑大幅降溫。
3. 12 月 FOMC：若如市場定價升息，對高估值 AI 股是 R1 的加速器；若通膨回落、Fed 按兵不動，則支持 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7353.73 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線偏離） | 0.42% | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線偏離） | 1.84% | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較前次基準） | -3.99% | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 26989.99 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤） | 13.56% | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2 季資料，家計股票配置 %） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 4.0 | FRED API (series_id=DFEDTARU) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.75 | FRED API (series_id=DFEDTARL) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 3.48 | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | +17.0 bps | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.93 | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM delta_bps | +8.0 bps | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.84 | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | -25.0 bps | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.6 | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | -14.0 bps | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.23 | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | -12.0 bps | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 99.64 | FRED API (series_id=DCOILWTICO) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO chg_pct | -7.92% | FRED API (series_id=DCOILWTICO) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72% | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.17 | FRED API (series_id=T5YIFR) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR delta_bps | -16.0 bps | FRED API (series_id=T5YIFR) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.9089 | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（序列自身 trailing 7 日） | -2.7 bps | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.92 | FRED API (series_id=SOFR) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 4.0 | FRED API (series_id=SOFR99) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.9 | FRED API (series_id=IORB) | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps（SOFR−IORB，IORB 取 2026-11-05） | 2.0 bps | fetch_macro.py repo_stress（FRED SOFR／IORB） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr99_iorb_bps（SOFR99−IORB，IORB 取 2026-11-05） | 10.0 bps | fetch_macro.py repo_stress（FRED SOFR99／IORB） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,748,145（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,945,410（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,261,882（¥626.19T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED API (series_id=VIXCLS) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of，base_date 2026-10-29，window 7 日） | 28.18 | fetch_macro.py vix_spx_comove 區塊（FRED 衍生） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | +63.84% | fetch_macro.py vix_spx_comove 區塊（FRED 衍生） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（comove=false） | -4.75% | fetch_macro.py vix_spx_comove 區塊（FRED 衍生） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2111.0042（$2.11T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG chg_pct | +0.27% | FRED API (series_id=LNFACBW027SBOG) | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7,249,305 | CFTC TFF futures-only | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -489,473 | CFTC TFF futures-only | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2326.9（$2.33T） | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebFetch（[primary: SEARCH]，direct fetch 成功） | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch（vestedfinance） | ✓ SEARCH-VERIFIED（僅取得群體前瞻 P/E；AI leader P/S vs 10 年均值未取得） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch，90d＋同季 | ✓ SEARCH-VERIFIED（EPS／PE 拆解未披露） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch，14d | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch | ✓ SEARCH-VERIFIED（new high/low 未取得） |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch（[primary: SEARCH]） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch，stock-of-state（2026-09 月資料） | ✓ SEARCH-VERIFIED（市值比未計算） |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch（[primary: SEARCH]） | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch，7d | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED（無當週數值） |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM | WebSearch | ✗ NOT DISCLOSED（無當期調查） |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED DFEDTARU / DFEDTARL | fetch_macro.py（FRED API） | ✓ API DFEDTARU ok；DFEDTARL ok |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | fetch_macro.py（FRED BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | fetch_macro.py（FRED BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | fetch_macro.py（FRED DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | fetch_macro.py（FRED DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | fetch_macro.py（FRED T10YIE，非衍生） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | fetch_macro.py（FRED DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED CPIAUCSL | fetch_macro.py（FRED CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | fetch_macro.py（FRED T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED THREEFYTP10 | fetch_macro.py（FRED THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py（FRED SOFR、SOFR99、IORB、RPONTTLD；repo_stress status ok） | ✓ API SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch，14d | ✗ NOT DISCLOSED（窗內無值得記錄的標售結果） |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED WALCL | fetch_macro.py（FRED WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | fetch_macro.py（FRED ECBASSETSW、JPNASSETS） | ✓ API ECBASSETSW ok；JPNASSETS ok（no_new_obs） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch，30d | ✗ NOT DISCLOSED（30 日內無合格披露） |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch，stock-of-state | ✓ SEARCH-VERIFIED（僅取得 Microsoft） |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch；quarterly_state stock-of-state＋event_scan 30d | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch＋既有 bullets 組合 | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動（depreciation useful-life change） | WebSearch，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch；quarterly_state stock-of-state＋event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch，7d | ✓ SEARCH-VERIFIED（1 件合格 SPAC 事件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（Renaissance Capital weekly recap） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch movers 掃描，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch，30d | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR Form 4，14d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch（[primary: SEARCH]） | ✓ SEARCH-VERIFIED（僅取得半導體 3 倍多頭基金） |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR ETF 申報＋ETF.com feed，30d | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch，7d | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe 月度量報告） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC monthly） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | fetch_macro.py（FRED VIXCLS＋vix_spx_comove 區塊） | ✓ API VIXCLS ok；vix_spx_comove ok |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（僅交叉檢核） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch，30d | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py cftc_lev_funds、move_index、ofr_repo（皆 status ok） | ✓ API cftc_lev_funds ok；move_index ok；ofr_repo ok |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻 P/E 約 28.3 | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ （Vested Finance；原定 Mag 7 加權 P/E 來源） | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein TSMC 目標價 554 → 600（EPS／PE 拆解未披露） | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/ （StockAnalysis；原定 sell-side TP 摘要） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html （CNBC） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5 年 CDS 突破 1289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds （Coinpaper） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | RSP 等權年初至今報酬約 14.13% | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY （Total Real Returns） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration （Chartrow） | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 1,474／下跌 1,252 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ （McClellan） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 22（極度恐懼） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ （FinHacker；原定 cnn.com） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-09 月資料）約 1.48 兆美元、YoY 約 31.4% | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt （原定 FINRA） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives （AAII） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔 | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week （Benzinga） | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | 12 月升息 25 bps 機率 76.8% | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ （24/7 Wall St.；原定 CME FedWatch） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000 | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee （BigGo Finance） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年 capex 指引約 175 → 約 170（下修；URL 字串含 190b，單位未標） | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex （Global Data Center Hub） | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3 | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html （Yahoo Finance） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle RPO 638（URL 路徑日期 2026-07-02，與資料日不一致） | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ （Motley Fool） | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87 | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends （GetDeploying） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 今年以來發債 296 | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era （404K Research，引 Goldman） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 10/29 起一週內 5 筆 AI 相關債券發行合計 67（發行人未逐一披露） | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era （404K Research，引 Goldman） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 Anthropic 65 ＋ OpenAI 約 70，合計約 135；分母僅 Microsoft capex 約 170 | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html （Yahoo Finance） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] Microsoft 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 （Investing.com，引 Bloomberg） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics 完成 SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ （Securities.io） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO 週漲 8% | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears （Renaissance Capital） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描，0 件符合 2+ 主題×弱基本面 | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 （Built In） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描，0 件合格 | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表（窗內無 filing-level 細節） | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe 股票選擇權賣買權比 1.05（日／5 日均未標） | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide （Seeking Alpha；原定 Cboe） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭基金 10 月底規模 24.31、當月淨流入 7.27 | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html （Yahoo Finance；原定 etf.com） | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市，0 件 | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 （Cboe 新聞稿） | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 9 月總結算量 1,486,062,415 口（2026-09 月資料） | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report （OCC） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性創高 20.93 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 （Saxo） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.margin_debt_crosscheck | 融資餘額交叉檢核基數約 1.48 兆美元（2026-09 月資料） | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt （原定 FINRA） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.ai_infrastructure_debt | ING 出售 12 筆資料中心貸款，規模約 500 | AI data center debt financing private credit November 2026 | https://www.cnbc.com/2026/11/06/ing-ai-data-center-loans-debt.html （CNBC） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-11-08",
  "iso_week": "2026-W45",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "yes",
  "horizon_end": "2027-05-09",
  "prior_date": "2026-10-18",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 13.56,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

> [DRY RUN] this report was not committed to archive.

# 2026-07-20 AI 泡沫破裂預測報告

報告日期：2026-07-20｜ISO 週次：2026-W30｜預測窗口：2026-07-20 → 2027-01-18｜前次基準：report-2026-07-16（4天前）

## 結論

**結論：no**

三條路徑都還沒有實際走起來：NASDAQ-100 距 52 週高點回撤 6.74%，離 R1 門檻還要再跌約 19.58%（`valuation.ndx_drawdown`）；hyperscaler 2026 capex 指引約 $700B，仍在上修，R2 沒有任何一家下修（`ai.hyperscaler_capex`）。Oracle／CoreWeave CDS 走闊（`valuation.ai_credit_schism`）說明 R3 方向的壓力在累積，但 HY OAS 2.71%（`monetary.hy_oas`）顯示整體信用市場還沒傳導；在 182 天的基準率下，這些證據不足以判定「多半會發生」。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 28592.66（2026-07-17），252 個交易日最高收盤 30660.6（2026-06-02），距 52 週高點回撤 6.74%（`valuation.ndx_drawdown`）。R1 門檻水位 22995.45，從最新收盤還要再跌約 19.58% 才會觸及。前次基準（report-2026-07-16）當時的回撤是 3.78%，四天內擴大約 3 個百分點，起因是 07-17 的晶片股賣壓：當天 NYSE 下跌家數約為上漲的 2 倍，新高 241／新低 166（`breadth.advance_decline`）。VIX 在 2026-07-10 → 2026-07-17 的 7 日窗口內從 15.03 升到 18.77（+24.88%），同期 S&P 500 -1.55%，co-movement 為 false：這是正常的跌勢避險，不是「指數上漲時避險需求同步被搶高」的擁擠訊號（`structural.vix_spx_comove`）。S&P 500 收在 7457.69，仍高於 200 日均線 6.73%、52 週均線 8.42%（`valuation.sp500_trend`），趨勢還沒有破壞。

估值脆弱度很高：S&P 500 trailing P/E 32.08、Shiller CAPE 41.52（`valuation.sp500_pe_cape`）；margin debt $1.416T，YoY +53.7%（2026-05 月資料，`retail.margin_debt`）；NAAIM 95.64（`retail.naaim`）。這些數字說明一旦破裂，跌幅可能很大，但本身不代表破裂時點落在窗口內。

**判讀：** 距 R1 還有約 19.58% 的跌幅，目前只是由晶片股帶動的一般修正。要在窗口內觸及門檻，需要信用端（R3 方向）或 capex 端（R2 方向）出現具體催化，把修正放大成去槓桿式的賣壓；以目前證據看還沒到那一步。

### R2 資本支出收縮

本次取得的 capex 來源（2026-05-15，對應最近一季財報）只給出 hyperscaler 2026 年合計 capex 約 $700B、方向「仍上修」（`ai.hyperscaler_capex`）。Microsoft、Alphabet、Amazon、Meta 各自的指引金額與日期，本次檢索結果沒有分列，因此本次無法確立個別公司數字；就整體方向而言，四家目前都沒有下修，已下修家數為 0。下一次財報日期本次來源沒有提供，不另作推定；照季報節奏，窗口內預計會有兩輪財報可以修改指引。需求端沒有轉弱跡象：TrendForce 指 3Q26 伺服器 DRAM 合約價 QoQ +13–18%（`ai.compute_supply_demand`）。AI 營收對 capex 缺口（revenue-to-capex gap）仍大：年化 capex 約 $700B，AI 終端營收在「低百億級」（Anthropic 約 $47B、OpenAI 約 $25B run-rate；分母為 top-4 hyperscaler 合計，`ai.revenue_capex_gap`、`ai.openai_anthropic_revenue`）。

**判讀：** R2 離成立最遠：需要四家裡至少兩家在接下來兩輪財報中下修，但目前方向仍是上修。只有 R1 的回撤擴大到逼使管理層調整預算，或 AI 營收對 capex 缺口開始壓到 hyperscaler 的融資能力，才可能在窗口內出現。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）出現信用端重新定價：Oracle 5 年期 CDS 約 198bp，創紀錄；CoreWeave 約 665bp（2026-07-16，`valuation.ai_credit_schism`）。這兩檔是窗口內最可能達到 R3 規模門檻的 AI 基礎設施信用名字，但本次來源沒有給出各自的總負債、近期到期或再融資金額，因此負債規模是否 ≥ 50 億美元、以及到期牆，本次都無法確立。本次也沒有看到付款違約、covenant waiver、distressed exchange 或 going-concern 的披露。過去 30 日內 AI 基礎設施的新債務融資事件與 hyperscaler 融資結構事件，本次掃描都沒有找到合格披露。整體信用環境仍然寬鬆：HY OAS 2.71%、IG OAS 0.78%（`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 -3bp，SRF 動用 0（`monetary.repo_stress_srf`）。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）出現一例：Blue Owl OCIC Q2 的 redemption-request ratio 為 18.8%，依 5% quarterly redemption cap 按比例撥付，屬 gate proration / breach（2026-07-02，`monetary.private_credit_liquidity`），不過來源也說贖回壓力略有緩和。

**判讀：** CoreWeave CDS 約 665bp 代表市場已經在為違約風險定價，這是三條路徑中變化最明顯的一條，但距離「破產申請、超過寬限期的付款違約或完成 distressed exchange」還隔著再融資失敗這一步，而本次沒有可引用的到期或流動性缺口資料。若窗口內出現 neocloud 再融資受阻、評等大幅下調或 distressed exchange 談判的報導，R3 會快速接近成立，也可能連帶觸發 R1。

## 支持 yes 的證據

- [R3] Oracle 5 年期 CDS 約 198bp 創紀錄、CoreWeave 約 665bp（2026-07-16），信用端已開始為 AI 基礎設施借款人重新定價，股權端則還沒完全跟上（`valuation.ai_credit_schism`）。
- [R1] NASDAQ-100 距 52 週高點回撤 6.74%（2026-07-17 收盤 28592.66），前次基準時為 3.78%，四天內明顯擴大；07-17 晶片股賣壓下 NYSE 下跌家數約為上漲的 2 倍（`valuation.ndx_drawdown`、`breadth.advance_decline`）。
- [整體] 私募信貸贖回壓力：Blue Owl OCIC Q2 redemption-request ratio 18.8%，依 5% quarterly redemption cap 按比例撥付（gate proration / breach，2026-07-02），非銀行資金端出現實際受限事件（`monetary.private_credit_liquidity`）。
- [整體] 脆弱度處於高檔：Shiller CAPE 41.52、trailing P/E 32.08（2026-07-17）；margin debt $1.416T、YoY +53.7%（2026-05）；NAAIM 95.64（2026-07-15），一旦有催化，下跌會被槓桿放大（`valuation.sp500_pe_cape`、`retail.margin_debt`、`retail.naaim`）。
- [R2] AI 營收對 capex 缺口：年化 capex 約 $700B，AI 終端營收在低百億級（分母為 top-4 hyperscaler，2026-05-15），長期回本壓力是 capex 下修的潛在來源（`ai.revenue_capex_gap`）。

## 支持 no 的證據

- [R1] 回撤只有 6.74%，R1 門檻水位 22995.45，從 28592.66 還要再跌約 19.58%；S&P 500 仍高於 200 日均線 6.73%（2026-07-17），趨勢沒有破壞（`valuation.ndx_drawdown`、`valuation.sp500_trend`）。
- [R2] hyperscaler 2026 capex 合計約 $700B，方向仍是上修（2026-05-15），四家已下修家數為 0；3Q26 伺服器 DRAM 合約價 QoQ +13–18%（2026-07-03）顯示需求仍強（`ai.hyperscaler_capex`、`ai.compute_supply_demand`）。
- [R3] 整體信用市場沒有傳導：HY OAS 2.71%、IG OAS 0.78%（2026-07-16）；SOFR−IORB -3bp、SRF 動用 0（2026-07-16／07-17），資金市場沒有壓力（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`）。
- [整體] 資本市場窗口仍開著：Anthropic IPO 投資人會議以約 $965B 估值進行，可能 10 月掛牌（2026-07-15）；2026 YTD 約 200 檔 IPO、募資 $141.2B（2026-07-16），AI 企業的股權融資管道暢通，降低窗口內出現流動性違約的機率（`speculation.upcoming_ai_ipos`、`speculation.ipo_heat`）。
- [整體] 政策端沒有收緊：Fed funds 目標區間 3.50%–3.75%（2026-07-19），CME FedWatch 顯示 7/29 會議約 86.7% 機率按兵不動（2026-07-18）；情緒已經降到 CNN Fear & Greed 37（Fear，2026-07-17），沒有處在極端亢奮（`monetary.fed_funds`、`monetary.fedwatch`、`retail.fear_greed`）。

## 與前期比較

前次結論：yes（report-2026-07-16）
本次結論：翻轉
翻轉依據：
- 前次的 yes 沒有記錄 yes_basis，所以沒有可以逐項檢驗的決定性理由；本次依規則 1 重新檢查，任何一條路徑都還沒有達到「已在進行或多半會在窗口內完成」的門檻。R1：回撤雖由 3.78% 擴大到 6.74%，離門檻仍需再跌約 19.58%（`valuation.ndx_drawdown`）。
- R2：capex 方向仍是上修，四家都沒有下修（`ai.hyperscaler_capex`），這條路徑沒有任何進展。
- R3：Oracle／CoreWeave CDS 走闊（`valuation.ai_credit_schism`）是唯一明顯惡化的訊號，但本次沒有違約、distressed exchange 或再融資失敗的證據，也無法確立借款人的負債規模與到期牆。
- 整體信用面：HY OAS 2.71%（`monetary.hy_oas`）沒有顯示 AI 信用壓力已擴散到廣義信用市場，因此 yes 方的證據只能證明脆弱度高，不能證明窗口內會破裂。

## 資料缺漏與不確定性

- ⛔ FETCH FAILED：`speculation.insider_form4`。搜尋有執行，但 SEC EDGAR 一手 Form 4 URL 因 egress 受限無法取得，無法完成規定的 EDGAR 篩檢，因此不能標為 0 件成功。內部人賣壓屬於投機熱度的輔助證據，不直接對應 R1–R3 任一條件，這個缺口不會改變本次結論。
- ✗ NOT DISCLOSED（非證據，僅列示）：`valuation.analyst_tp_decomposition`、`retail.social_sentiment`、`institutional.bofa_jpm_survey`、`ai.token_growth`、`ai.customer_concentration_rpo`、`ai.hyperscaler_financing_mix`、`ai.depreciation_life`、`ai.capital_cycle`、`structural.global_leveraged_approvals`、`structural.ai_infrastructure_debt`。其中 `structural.ai_infrastructure_debt` 與 `ai.hyperscaler_financing_mix` 沒有披露，讓 R3 缺少再融資與表外結構的事件證據，是最可能影響判斷的缺口；如果實際存在大額受困融資，結論可能偏向 yes。
- 證據檔與 macro artifact 不一致：搜尋紀錄寫 `structural.treasury_basis_trade` 的三個腳本區塊均 fetch_failed，但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 都是 `status: ok`。本報告以 artifact 為準（✓ API）：槓桿基金淨部位 -7562874 口（2026-07-14，4 週 Δ -78139），MOVE 70.88（2026-07-17），OFR tri-party repo transaction volume $2342.6bn（2026-07-17）。美債基差交易槓桿沒有失序跡象。
- 10Y 分解：ΔDGS10 0bp、ΔDFII10 0bp、ΔT10YIE +2bp，判讀為 `不可判（視窗不一致）`；DGS10、DFII10 自前次以來沒有新觀測（stale_series），T10YIE 有更新。10Y 期限溢價（term premium）0.7788%（2026-07-10，trailing 7 日 +4.7bp，Kim-Wright）。
- 部分 snapshot 來源日期偏舊：`structural.zero_dte`（0DTE 佔 SPX 約 63%，2026-02-28）、`valuation.mag7_multiples`（2026-05-15）、`breadth.rsp_spy`（2026-06-10），只作背景參考，不影響結論。
- 最大的不確定性：（1）下一輪 hyperscaler 財報（日期本次未確立）若有兩家下修 capex，R2 會直接成立，推向 yes；（2）CoreWeave 等 neocloud 的再融資結果與負債規模本次無法確立，若出現 distressed exchange 談判，R3 與 R1 會同時推向 yes；（3）CPI YoY 3.46%（2026-06）限制了 Fed 緩衝 AI 主導下跌的空間，若通膨讓降息預期落空，回撤可能被放大。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7457.69 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 6.73 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.42 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28592.66 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 6.74 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026-Q1 季資料，家計股票配置 %） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 2.71 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（IG OAS %） | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（10Y 殖利率 %） | 4.57 | FRED API (series_id=DGS10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（10Y 實質殖利率 %） | 2.35 | FRED API (series_id=DFII10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（10Y breakeven %） | 2.24 | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（WTI 美元／桶） | 79.2 | FRED API (series_id=DCOILWTICO) | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料，CPI YoY %） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（5y5y forward %） | 2.21 | FRED API (series_id=T5YIFR) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（10Y 期限溢價（term premium）%，Kim-Wright） | 0.7788 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 日） | 4.7 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API (series_id=SOFR99) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.walcl | WALCL latest（Fed 資產負債表） | 6743028.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（ECB 資產） | 5970516.0（€5.97T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（BOJ 資產） | 6395509.0（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest（VIX） | 18.77 | FRED API (series_id=VIXCLS) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（窗口終點 VIX） | 18.77 | FRED API (series_id=VIXCLS, SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_base（窗口起點 VIX） | 15.03 | FRED API (series_id=VIXCLS) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日 %） | 24.88 | FRED API (series_id=VIXCLS) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日 %） | -1.55 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（銀行對 NBFI 放款） | 2004.0237（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（槓桿基金美債期貨淨部位，口） | -7562874 | CFTC TFF futures-only | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -78139 | CFTC TFF futures-only | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（MOVE） | 70.88 | Yahoo Finance chart API (^MOVE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2342.6 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | MarketXLS WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧 | 信用市場 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | WebSearch（集中度追蹤頁） | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | WebSearch [primary: SEARCH]（MacroMicro 轉載） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA | FINRA／Advisor Perspectives WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII | aaii.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | ycharts WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM | 賣方調查 WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED DFEDTARU／DFEDTARL | scripts/fetch_macro.py（DFEDTARU ok、DFEDTARL ok） | ✓ API |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED SOFR／SOFR99／IORB／RPONTTLD | scripts/fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） | ✓ API |
| monetary.treasury_auctions | 貨幣｜美債標售需求 | Auction recap WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Bloomberg WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報 WebSearch（stock-of-state，沿用最近一季） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch AI WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報 quarterly_state＋30d event_scan WebSearch；兩組件皆無合格披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K／10-Q WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速 quarterly_state＋30d 進出場 event_scan WebSearch；兩組件皆無合格披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／Benzinga／StockTitan movers WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 [primary: SEC EDGAR]；EDGAR egress 受限，一手 URL 無法取得 | ⛔ FETCH FAILED |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe daily statistics WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF.com WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe insights WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe／AInvest WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS ok、vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | Advisor Perspectives WebSearch（交叉核對） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok；aggregation any） | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.08 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl；原定來源 multpl.com） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 41.52 | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe （multpl；原定來源 multpl.com） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E 約 40（trailing） | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026 （MarketXLS） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS 約 198bp 創紀錄、CoreWeave 約 665bp | Oracle CoreWeave CDS spread widening July 2026 | https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/ （Real Investment Advice） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP +10.68% vs SPY +7.47% YTD | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St.） | 2026-06-10 | 2026-07-20T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 36.40% | S&P 500 top 10 concentration percent 2026 | https://ahasignals.com/sp500-concentration-risk/ （AHA Signals；原定 State Street SPDR 持股） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| breadth.advance_decline | NYSE 07-17 下跌約為上漲 2 倍、新高 241／新低 166 | NYSE advance decline breadth July 17 2026 | https://money.usnews.com/investing/news/articles/2026-07-17/wall-st-futures-fall-as-chip-selloff-gathers-pace-netflix-tumbles （U.S. News／Reuters） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（Fear） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed （MacroMicro；原定 cnn.com） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-05 月資料）$1.416T、YoY +53.7% | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives；原定 FINRA） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |
| retail.aaii | AAII Bull 44.9% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number （YCharts；原定 naaim.org） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 2.59、小幅 tail | US Treasury 10Y auction July 2026 bid to cover | https://cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/ （Crypto Briefing；原定 TreasuryDirect／Reuters） | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 會議約 86.7% 持平 | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch （CryptoRank；原定 CME FedWatch） | 2026-07-18 | 2026-07-20T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance （Bloomberg） | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio 18.8%，依 5% quarterly redemption cap 按比例撥付 | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://whbl.com/2026/07/02/blue-owl-keeps-withdrawal-limits-even-as-redemption-pressure-modestly-eases/ （WHBL／Reuters） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計約 $700B、仍上修（最近一季財報） | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html （Yahoo Finance） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 約 $47B／OpenAI 約 $25B run-rate | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 QoQ +13–18% | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html （TrendForce） | 2026-07-03 | 2026-07-20T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex 約 $700B vs AI 終端營收低百億級（分母：top-4 hyperscaler） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| speculation.ai_rename_spac | EVTV → Azio AI（AZIO）改名 | AI rename ticker change July 2026 Azio EVTV | https://www.businesswire.com/news/home/20260710628386/en/Azio-AI-Holdings-Inc.-Nasdaq-EVTV-to-Begin-Trading-Under-New-Ticker-Symbol-AZIO-Completing-Corporate-Rebrand （Business Wire） | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD 約 200 檔 IPO、募資 $141.2B | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/ （StockAnalysis；原定 Renaissance） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| speculation.microcap_moonshots | 7 日內合格 microcap moonshot 0 件 | microcap 100% single day quantum AI moonshot July 2026 | 已檢查：Finviz biggest gainers、Benzinga movers、StockTitan movers | — | 2026-07-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 投資人會議，估值約 $965B，可能 10 月掛牌 | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html （CNBC） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.73（daily） | Cboe equity put call ratio July 2026 | https://www.cboe.com/markets/us/options/market-statistics/daily/ （Cboe） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 約 $198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing；原定 etf.com／ETFGI） | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 推出 6 檔 2x 單一個股 ETF（GOOGL／AMZN／META／AAPL 等） | single-stock leveraged ETF launch July 2026 Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-07 | 2026-07-20T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 成交約 63% | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/ （Cboe） | 2026-02-28 | 2026-07-20T09:30:00+08:00 |
| structural.options_volume | OCC 6 月總成交 1,603,491,559 口、YoY +45%（2026-06 月資料） | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 145.13、VIX 約 16.5、期限結構 contango | VIX term structure SKEW July 2026 | https://www.ainvest.com/news/0dte-volatility-drives-market-strategies-2026-2602/ （AInvest；原定 Cboe） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-05 月資料）$1.416T、YoY +53.7%（交叉核對） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-07-20",
  "iso_week": "2026-W30",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-01-18",
  "prior_date": "2026-07-16",
  "prior_answer": "yes",
  "flip_evidence": ["valuation.ndx_drawdown", "ai.hyperscaler_capex", "valuation.ai_credit_schism", "monetary.hy_oas"],
  "yes_basis": [],
  "r1_drawdown_pct": 6.74,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

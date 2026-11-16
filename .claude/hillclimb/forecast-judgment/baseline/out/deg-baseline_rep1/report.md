> [DRY RUN] this report was not committed to archive.

# 2026-11-08 AI 泡沫破裂預測報告
報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：無（基準）

## 結論

**結論：yes**

三條路徑同時已在推進：NASDAQ-100 已距 52 週高點回撤 13.56%，只需再跌約 13.23% 即觸發 R1；Microsoft 已於 2026-10-29 下修資本支出指引（R2 四家中已有一家），而 CoreWeave 五年期 CDS 突破 1289 bps、債券殖利率升破 16%（R3 的 distressed 定價）。在 FedWatch 隱含 12 月升息、CPI YoY 3.72% 限制 Fed 緩衝空間的背景下，判斷窗口內至少一條路徑完成的可能性高於不完成。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 26,989.99（2026-11-06），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 13.56%。R1 門檻水位為 23,418.52，自最新收盤再下跌約 13.23% 即觸發（`valuation.ndx_drawdown`）。這段回撤在一個月內完成：2026-11-05 單日收在 26,629.81，次日僅小幅反彈。同期 S&P 500 為 7,353.73（2026-11-05），仍高於 200 日均線 0.42%、高於 52 週均線 1.84%（`valuation.sp500_trend`），代表跌勢集中在 AI／科技權重，尚未全面擴散。波動面：VIX 28.18、SKEW 149.37、隱含相關性 20.93（2026-11-06，`structural.cross_asset_derivatives`）；VIX 在 2026-10-29 → 2026-11-05 的 7 日窗內 +63.84%，同期 S&P 500 −4.75%，屬典型避險型反向走勢而非 crowded-optionality 同漲（`structural.vix_spx_comove`）。估值仍高：Shiller CAPE 38.91、trailing P/E 25.14（2026-11-06，`valuation.sp500_pe_cape`），Mag 7 前瞻 P/E 約 28.3（`valuation.mag7_multiples`），前十大權重約 37.9%（`breadth.top10_concentration`），一旦獲利預期下修，下行空間大。政策緩衝有限：Fed funds 目標區間 3.75%–4.00%（`monetary.fed_funds`），FedWatch 隱含 12 月升息 25 bps 約 76.8%（2026-11-06，`monetary.fedwatch`），CPI YoY 3.72%（2026-09，`monetary.cpi_yoy`），WTI 99.64 美元（`monetary.wti`）。

**判讀：** R1 已走完門檻距離的一半以上；在 Fed 偏向升息、通膨與油價偏高、AI 信用端已出現 distressed 定價的組合下，再跌約 13% 於 6 個月內發生並非尾部情境。推過門檻的觸發點包括 12 月 FOMC 升息落地、CoreWeave 等 AI 借款人信用事件外溢，以及下一輪 hyperscaler 財報的 capex／指引訊號。反向力量是情緒已極度恐懼（逆勢反彈常見）且廣義信用利差仍窄。

### R2 資本支出收縮

- Microsoft：將 2026 年資本支出指引自約 175 下調至約 170（2026-10-29 財報季），方向：下修（`ai.hyperscaler_capex`）。
- Alphabet：本次未取得最新正式指引，方向無法判定。
- Amazon：本次未取得最新正式指引，方向無法判定。
- Meta：本次未取得最新正式指引，方向無法判定。

依已取得資料，四家中已有一家下修。窗口（至 2027-05-09）涵蓋接下來兩輪季報週期，具體財報日期本次未取得。融資面：hyperscaler 今年以來發債約 296，10/29 起一週內 5 筆 AI 相關債券合計約 67（`ai.hyperscaler_financing_mix`），顯示 capex 仍以發債延續而非收縮；產業 AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 135（Anthropic 65＋OpenAI 約 70）vs 年化 capex 約 170（分母：僅 Microsoft，其餘三家與 Oracle 本次未取得），單一 Microsoft 的 capex 已超過兩家領先模型公司的合計年化營收（`ai.revenue_capex_gap`）。

**判讀：** R2 已完成一半門檻（1/4 家下修），只需 Alphabet、Amazon、Meta 任一家在下兩輪財報中將當年度或次年度指引相對前次下修即成立；在信用成本上升（CoreWeave 殖利率逾 16%）與股價回撤壓力下，管理層小幅修剪指引的門檻很低。反向力量是三家仍在大量發債擴建，且首次給出的次年度指引不構成「下修」。另需注意：Microsoft 下修的數字僅來自單一搜尋結果，其來源標題提及 190B，與 175→170 的關係本次未能交叉核實。

### R3 AI 信用事件

符合 R3 規模門檻（負債 ≥ 50 億美元、以 AI 資料中心／算力為主業）的借款人中，本次取得當期定價的是 CoreWeave：五年期 CDS 突破 1289 bps（2026-11-05），債券殖利率升破 16%（2026-11-06），兩者都是 distressed 等級的定價（`valuation.ai_credit_schism`）。這是 AI 信用定價分歧（equity-vs-credit schism）從「信用與非 AI 無差」轉為「信用端先行重定價」的訊號。AI infrastructure debt financing / vendor-financing loops 方面，ING 出售 12 筆資料中心貸款、規模約 500（2026-11-06，`structural.ai_infrastructure_debt`），顯示銀行端開始降低資料中心貸款曝險。本次未取得任何 AI 借款人的實際付款違約、寬限期、covenant waiver、distressed exchange 或 going-concern 披露，也未取得具體到期牆資料。廣義信用仍平靜：HY OAS 3.48%、IG OAS 0.93%（2026-11-05，`monetary.hy_oas`、`monetary.ig_oas`）。

**判讀：** R3 尚未發生，但 CoreWeave 的 CDS 與殖利率已進入通常伴隨再融資困難或 distressed exchange 的區間；推過門檻需要一次實際的付款違約、破產申請或完成 distressed exchange。在 Fed 可能升息、銀行出售資料中心貸款的環境下，再融資窗口收窄是可信的傳導路徑，且 R3 事件幾乎必然觸發 R1 的進一步下跌。

## 支持 yes 的證據

- [R1] NASDAQ-100 收盤 26,989.99（2026-11-06），距 52 週高點回撤 13.56%，離 R1 門檻 23,418.52 只差約 13.23%，且回撤在一個月內形成 `valuation.ndx_drawdown`
- [R3] CoreWeave 五年期 CDS 突破 1289 bps（2026-11-05）、債券殖利率升破 16%（2026-11-06），AI 信用定價分歧（equity-vs-credit schism）轉為信用端先行重定價 `valuation.ai_credit_schism`
- [R2] Microsoft 於 2026-10-29 將 2026 年資本支出指引自約 175 下調至約 170，R2 所需兩家中已有一家 `ai.hyperscaler_capex`
- [整體] Fed 緩衝空間受限：FedWatch 隱含 12 月升息 25 bps 約 76.8%（2026-11-06），CPI YoY 3.72%（2026-09），WTI 99.64 美元（2026-11-03），10Y 殖利率 4.84%（2026-11-05） `monetary.fedwatch` `monetary.cpi_yoy` `monetary.wti` `monetary.dgs10`
- [R3] ING 出售 12 筆資料中心貸款、規模約 500（2026-11-06），AI infrastructure debt financing / vendor-financing loops 的銀行端資金開始撤退 `structural.ai_infrastructure_debt`
- [R1] 避險需求急升：VIX 28.18、SKEW 149.37、隱含相關性創高 20.93（2026-11-06）；VIX 7 日 +63.84% 而 S&P 500 −4.75%（2026-11-05） `structural.cross_asset_derivatives` `structural.vix_spx_comove`
- [R2] hyperscaler 融資結構（capex vs FCF / 發債）轉向債務：今年以來發債約 296，10/29 起一週 5 筆 AI 債券合計約 67（2026-11-06），capex 越來越依賴融資市場，信用收緊時削減指引的壓力上升 `ai.hyperscaler_financing_mix`
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 135（Anthropic＋OpenAI，2026-09-30）低於單一 Microsoft 的年化 capex 約 170（分母僅 Microsoft） `ai.revenue_capex_gap`
- [整體] 估值與集中度仍處高位：Shiller CAPE 38.91（2026-11-06）、Mag 7 前瞻 P/E 約 28.3（2026-10-13）、前十大權重約 37.9%（2026-11-01），下行幅度空間大 `valuation.sp500_pe_cape` `valuation.mag7_multiples` `breadth.top10_concentration`
- [R1] 槓桿部位仍重：margin debt 約 1.48 兆美元、YoY 約 +31.4%（2026-09）；半導體 3 倍多頭基金 10 月底規模 24.31、當月淨流入 7.27（逢低加碼） `retail.margin_debt` `structural.leveraged_etf_aum`
- [整體] 美債基差交易槓桿（Treasury basis-trade leverage）持續累積：槓桿基金美債期貨淨部位 −7,249,305 口（2026-11-03），4 週變動 −489,473 口；MOVE 92.77（2026-11-06） `structural.treasury_basis_trade`

## 支持 no 的證據

- [R3] 廣義信用利差仍窄：HY OAS 3.48%、IG OAS 0.93%（2026-11-05），信用市場尚未把 AI 壓力定價為系統性事件 `monetary.hy_oas` `monetary.ig_oas`
- [整體] 資金市場無壓力：repo 資金壓力（SOFR−IORB）2.0 bps、SOFR99−IORB 10.0 bps（2026-11-05），SRF 動用（Standing Repo Facility usage）0.0（2026-11-06）；銀行對 NBFI 放款 $2.11T（2026-10-28）未見收縮 `monetary.repo_stress_srf` `structural.nbfi_bank_loans`
- [R1] 跌勢尚未擴散：S&P 500 7,353.73 仍高於 200 日均線 0.42%（2026-11-05）；RSP 年初至今約 +14.13%（2026-11-06）；NYSE 上漲 1,474 家對下跌 1,252 家（2026-11-06） `valuation.sp500_trend` `breadth.rsp_spy` `breadth.advance_decline`
- [R1] 情緒已極度悲觀，逆勢反彈條件成熟：Fear & Greed 22（2026-11-06）、AAII 看空 48.4%（2026-11-04）、Cboe 股票賣買權比 1.05（2026-11-05） `retail.fear_greed` `retail.aaii` `speculation.equity_put_call`
- [R2] AI 需求面尚未轉弱：Anthropic 上半年營收 16.3（2026-10-26）並遞交 S-1、目標估值 1.5–2 兆；H100 隨選租金中位數 3.87（2026-11-03）未見崩跌 `ai.openai_anthropic_revenue` `speculation.upcoming_ai_ipos` `ai.compute_supply_demand`
- [R2] Microsoft 的下修幅度僅約 3%（175→170），hyperscaler 一週內仍發行約 67 的 AI 相關債券（2026-11-06），擴建意願未見逆轉 `ai.hyperscaler_capex` `ai.hyperscaler_financing_mix`
- [整體] 長端利率壓力回落：10Y 殖利率由 2026-10-05 的 5.31% 降至 2026-11-05 的 4.84%；10Y 期限溢價（term premium）0.9089%（2026-10-30），7 日 −2.7 bps `monetary.dgs10` `monetary.term_premium`
- [整體] 基準率：任一 182 天窗口內 R1–R3 都不發生才是常態，且目前三條路徑都尚未有任何一條真正完成；R3 的 Oracle backlog 仍高達 638（2026-08-31）代表合約承諾尚在 `ai.customer_concentration_rpo`

## 與前期比較

前次結論：無前次（基準）

這是基準執行：archive 中沒有可用的前次資料夾，fetcher 以 `none` 執行，10Y Δ 分解為 baseline_no_prior（無前次比較，不適用 Δ 分解）。flip_evidence 為空陣列。下次執行起，將以本次的 yes 為前次結論並套用翻轉紀律。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源檢索完成但無合格當期披露（✗ NOT DISCLOSED），均為 best-effort：`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.treasury_auctions`、`monetary.private_credit_liquidity`、`ai.token_growth`、`ai.depreciation_life`、`ai.capital_cycle`（quarterly_state 無可用增速對比，故「增速證據不足，本次不判定週期階段」；其 event_scan 取得微軟 10 月取消 Nscale 英國資料中心交易、規模約 3 的事件，2026-11-04）、`structural.global_leveraged_approvals`。其中 `monetary.private_credit_liquidity` 與 `monetary.treasury_auctions` 若有披露，可能強化 R3 或 Fed 緩衝判斷，但目前缺口不改變答案。

資料一致性注意：evidence 記錄稱美債基差交易槓桿的三個 script 區塊 fetch_failed 並以 WebSearch 取得 MOVE 93.88（2026-11-04），但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 皆為 status ok（MOVE 92.77，2026-11-06）。依 macro-fetch decision branch，以 artifact 為準記 ✓ API，未使用 93.88 的搜尋值。

最大不確定性：

1. Alphabet、Amazon、Meta 的最新正式 capex 指引本次未取得（`ai.hyperscaler_capex` 僅涵蓋 Microsoft）。若三家近期已上修，R2 的推進力道較弱，答案偏向 no；若其中一家已下修，R2 可能已成立，答案將更確定為 yes。Microsoft 175→170 本身也僅單一來源，且來源標題提及 190B，若此下修不成立，R2 退回 0/4，削弱 yes 的論據。
2. CoreWeave 的到期牆與再融資時程本次未取得。若窗口內有大額到期且市場維持 16% 以上殖利率，distressed exchange 可能性上升（推向 yes）；若取得新融資或 hyperscaler 提供 capacity backstop，R3 路徑降溫（推向 no）。
3. 12 月 FOMC：若如 FedWatch 定價升息，R1 下行與 AI 借款人再融資壓力同步加劇（推向 yes）；若 Fed 按兵不動且通膨回落，極度恐懼情緒下的反彈可能使 NASDAQ-100 遠離 R1 門檻（推向 no）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7353.73 | FRED API (series_id=SP500)，fetch_macro.py sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend ma200 | 7322.74 | FRED API (series_id=SP500)，fetch_macro.py sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 0.42 | FRED API (series_id=SP500)，fetch_macro.py sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 1.84 | FRED API (series_id=SP500)，fetch_macro.py sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 26989.99 | FRED API (series_id=NASDAQ100)，fetch_macro.py ndx_drawdown | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100)，fetch_macro.py ndx_drawdown | 2026-10-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 13.56 | FRED API (series_id=NASDAQ100)，fetch_macro.py ndx_drawdown | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API (series_id=NASDAQ100)，fetch_macro.py ndx_drawdown | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2 季資料，FRED 觀測日 2026-04-01，%） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 4.0 | FRED API (series_id=DFEDTARU) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.75 | FRED API (series_id=DFEDTARL) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 3.48 | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.93 | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.84 | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.6 | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.23 | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（美元／桶） | 99.64 | FRED API (series_id=DCOILWTICO) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料，FRED 觀測日 2026-09-01） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.17 | FRED API (series_id=T5YIFR) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 0.9089 | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 日） | -2.7 | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.92 | FRED API (series_id=SOFR) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 4.0 | FRED API (series_id=SOFR99) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.9 | FRED API (series_id=IORB) | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用 transaction volume，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,748,145（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,945,410（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,261,882（¥626.19T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED API (series_id=VIXCLS) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of，base_date 2026-10-29，window 7 日） | 28.18 | FRED API，fetch_macro.py vix_spx_comove block | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 63.84 | FRED API，fetch_macro.py vix_spx_comove block | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -4.75 | FRED API，fetch_macro.py vix_spx_comove block | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2111.0042（$2.11T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7,249,305 | CFTC TFF futures-only，fetch_macro.py cftc_lev_funds | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -489,473 | CFTC TFF futures-only，fetch_macro.py cftc_lev_funds | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo Finance chart API (^MOVE)，fetch_macro.py move_index | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2326.9 | OFR STFM (REPO-TRIV1_TV_TOT-P)，fetch_macro.py ofr_repo | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebFetch（primary SEARCH，direct 成功） | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch（vestedfinance） | ✓ SEARCH-VERIFIED（僅前瞻 P/E；P/S vs 10 年均值未取得） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（stockanalysis.com） | ✓ SEARCH-VERIFIED（Bernstein TSM TP 554→600；EPS／PE 分解未披露） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API（sp500_trend ok） |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API（ndx_drawdown ok） |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch 14 日窗（CNBC、coinpaper） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch（totalrealreturns） | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch（chartrow） | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch（mcoscillator） | ✓ SEARCH-VERIFIED（A/D 取得；new high/low 未取得） |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch（primary SEARCH） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch（FINRA 月資料彙整） | ✓ SEARCH-VERIFIED（2026-09 月資料 carry-forward） |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | WebSearch（AAII insights） | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch 7 日窗（Benzinga） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API（BOGZ1FL153064486Q ok） |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch（primary SEARCH） | ✗ NOT DISCLOSED（無當期週值） |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✗ NOT DISCLOSED（無窗內新調查） |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（FRED API） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（FRED API） | ✓ API（BAMLH0A0HYM2 ok） |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（FRED API） | ✓ API（BAMLC0A0CM ok） |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（FRED API） | ✓ API（DGS10 ok） |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED API） | ✓ API（DFII10 ok） |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（FRED API，非 derived） | ✓ API（T10YIE ok） |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（FRED API） | ✓ API（DCOILWTICO ok） |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（FRED API，yoy_pct） | ✓ API（CPIAUCSL ok） |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（FRED API） | ✓ API（T5YIFR ok） |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（FRED API，Kim-Wright） | ✓ API（THREEFYTP10 ok） |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（FRED API，repo_stress block） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok；repo_stress status ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch 14 日窗 | ✗ NOT DISCLOSED（窗內無顯著標售結果） |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（FRED API） | ✓ API（WALCL ok） |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（FRED API） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing / liquidity operations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch 30 日窗（primary SEARCH） | ✗ NOT DISCLOSED（窗內無合格披露） |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（最新季報指引） | ✓ SEARCH-VERIFIED（僅 Microsoft；Alphabet／Amazon／Meta 本次未取得） |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | WebSearch（primary SEARCH） | ✓ SEARCH-VERIFIED（Oracle RPO；同一 counterparty 跨供應商加總未披露） |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch（primary SEARCH） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch：quarterly_state 發債趨勢 + event_scan 30 日窗 | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch + 既有 bullets 組合（分母僅 Microsoft） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動（depreciation useful-life change） | WebSearch 30 日窗 | ✗ NOT DISCLOSED（窗內無變動披露） |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch：quarterly_state 增速對比 + event_scan 30 日窗 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch 7 日窗 | ✓ SEARCH-VERIFIED（1 件合格 SPAC 事件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（Renaissance Capital weekly recap） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch 7 日窗（movers screeners） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch 30 日窗 | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 14 日窗 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch（primary SEARCH） | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch（primary SEARCH） | ✓ SEARCH-VERIFIED（僅半導體 3 倍多頭基金；其餘標的 AUM 未取得） |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR ETF 申報 + ETF.com feed 30 日窗 | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch 7 日窗（KRX／TWSE／JPX／ESMA／ETFGI） | ✗ NOT DISCLOSED（窗內無英文披露） |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe 月度量報告） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch（Saxo options brief） | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（FRED VIXCLS + vix_spx_comove block） | ✓ API（VIXCLS ok；vix_spx_comove ok，comove false） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（FINRA 月資料彙整） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch 30 日窗（primary SEARCH） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED API） | ✓ API（LNFACBW027SBOG ok） |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py 三區塊（CFTC TFF、Yahoo ^MOVE、OFR STFM） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻 P/E 約 28.3（原定來源：Mag 7 weighted P/E） | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ （Vested Finance） | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein 將 TSMC 目標價由 554 上調至 600；EPS／PE 分解未披露 | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/ （StockAnalysis） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html （CNBC） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 五年期 CDS 突破 1289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds （Coinpaper） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | RSP 年初至今報酬約 14.13% | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY （Total Real Returns） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大成分股權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration （Chartrow） | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 1,474 家對下跌 1,252 家 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ （McClellan） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 22（極度恐懼）；原定來源 cnn.com | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ （Finhacker） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 1.48 兆美元、YoY 約 +31.4% | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt （FINRA 資料彙整） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives （AAII） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔 | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week （Benzinga） | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | 12 月升息 25 bps 隱含定價約 76.8% | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ （24/7 Wall St.） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000 | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee （BigGo Finance） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年 capex 指引自約 175 下調至約 170 | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex （Global Data Center Hub） | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3 | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html （Yahoo Finance） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle 剩餘履約義務（RPO）638 | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ （Motley Fool） | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87 | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends （GetDeploying） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 今年以來發債約 296 | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era （404K Research，引 Goldman） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 10/29 起一週內 5 筆 AI 相關債券發行合計約 67 | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era （404K Research，引 Goldman） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 Anthropic 65＋OpenAI 約 70，合計約 135；分母 Microsoft capex 約 170（取自 ai.hyperscaler_capex） | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html （Yahoo Finance） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] 微軟 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 （Investing.com，引 Bloomberg） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics 完成 SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ （Securities.io） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO，週漲 8% | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears （Renaissance Capital） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描：無合格標的（2+ 主題×弱基本面） | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 （Built In） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描：無合格 filing-level 申報 | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe 股票選擇權賣買權比升至 1.05（日讀數） | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide （Seeking Alpha） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭基金 10 月底規模 24.31、當月淨流入 7.27 | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html （Yahoo Finance） | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：無合格事件 | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 （Cboe via PR Newswire） | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 9 月總結算量 1,486,062,415 口（2026-09 月資料） | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report （OCC） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性創高 20.93 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 （Saxo） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 交叉檢核基數約 1.48 兆美元（2026-09 月資料） | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt （FINRA 資料彙整） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
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
  "prior_date": null,
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 13.56,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

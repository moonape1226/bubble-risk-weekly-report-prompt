> [DRY RUN] this report was not committed to archive.

# 2026-11-08 AI 泡沫破裂預測報告

報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：無（基準）

## 結論

**結論：no**

三條路徑目前都還沒走完：NASDAQ-100 雖已距 52 週高點回撤 13.56%，但仍需再跌約 13.23% 才觸及 R1 門檻；R2 目前四家中只有 Microsoft 小幅下修（且發生於窗口開始前）；R3 的 CoreWeave 信用已呈 distressed 定價（五年 CDS 1289 bps、債券殖利率破 16%），但尚無違約或 distressed exchange。廣義信用（HY OAS 3.48%）與 repo 資金市場（SOFR−IORB 2 bps、SRF 動用 0）仍未出現傳導，相對於 182 天窗口的低基準率，yes 方證據尚不足以過半。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 26,989.99（2026-11-06），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 13.56%。R1 門檻水位為 23,418.52，自最新收盤再下跌約 13.23% 即觸及（`valuation.ndx_drawdown`）。回撤是在一個月內形成：S&P 500 最新 7,353.73（2026-11-05），僅高於 200 日均線 0.42%、高於 52 週均線 1.84%，價格延伸已幾乎歸零（`valuation.sp500_trend`）。波動急升：VIX 由 17.2（2026-10-29）升至 28.18（2026-11-05），7 日 +63.84%，同期 S&P 500 −4.75%，屬正常的股跌波升而非 crowded-optionality 共漲（`structural.vix_spx_comove`）；SKEW 149.37、隱含相關性 20.93 創高（`structural.cross_asset_derivatives`）。貨幣面沒有緩衝：CME FedWatch 隱含 12 月升息 25 bps 機率 76.8%（`monetary.fedwatch`），CPI YoY 3.72%（2026-09，`monetary.cpi_yoy`），WTI 99.64 美元（`monetary.wti`），10Y 殖利率 4.84%（`monetary.dgs10`）。情緒已極度悲觀：Fear & Greed 22（`retail.fear_greed`）、AAII 看空 48.4%（`retail.aaii`）、Cboe 股票選擇權 put/call 1.05（`speculation.equity_put_call`）。

**判讀：** R1 已走完約一半路程（13.56% / 25%）。要在窗口內觸發，需要一個新的負面催化劑把跌幅再擴大約 13%，最可能的組合是 Fed 12 月實際升息並維持鷹派、疊加 R3 信用事件或 hyperscaler 下修 capex 的傳導。目前情緒與 put/call 已處極端，短線反彈與續跌皆有可能；在沒有信用／資金面傳導下，再跌 13% 尚非較可能情境。

### R2 資本支出收縮

- Microsoft：2026 年 capex 指引自約 $175bn 下修至約 $170bn（2026-10-29 財報季，下修約 3%）（`ai.hyperscaler_capex`）。
- Alphabet：本次證據未取得最新正式指引與方向（未提供指引）。
- Amazon：本次證據未取得最新正式指引與方向（未提供指引）。
- Meta：本次證據未取得最新正式指引與方向（未提供指引）。

目前四家中已確認下修者 1 家（Microsoft），但該次下修發生於 2026-10-29，早於窗口起點 2026-11-08，依解析條件不計入窗口內；窗口內仍需至少兩家新的下修。具體下次財報日期本次證據未載，按季報節奏，窗口（至 2027-05-09）預計涵蓋兩輪季報。融資面上 hyperscaler 仍大量發債：今年以來發債約 $296bn，10/29 起一週內 5 筆 AI 相關債券發行合計約 $67bn（`ai.hyperscaler_financing_mix`），顯示 capex 的資金管道仍暢通；年化 AI 終端營收約 $135bn（Anthropic $65bn ＋ OpenAI 約 $70bn）對照分母僅含 Microsoft 2026 capex 指引約 $170bn（`ai.revenue_capex_gap`），分母涵蓋不完整，無法判定全產業缺口方向。

**判讀：** R2 距觸發仍遠：窗口內需兩家新下修，而目前只有一家小幅修正且不計入。可能推過門檻的情境是 R1 回撤加深或債市融資成本急升，迫使 Alphabet／Amazon／Meta 在 2027 年初的財報中給出低於前次的指引；在債券市場仍吸收 $67bn 單週發行的情況下，此情境尚非主流。

### R3 AI 信用事件

主要候選借款人為 CoreWeave（AI 算力為主業；其負債總額本次證據未載，是否達 50 億美元門檻需另行確認）。信用定價已明顯惡化：CoreWeave 債券殖利率升破 16%（2026-11-06），五年期 CDS 突破 1289 bps（2026-11-05），屬 distressed 級別定價，且出現在 NASDAQ 反彈期間——信貸端重定價領先股權端，是 AI 信用定價分歧（equity-vs-credit schism）的後期訊號（`valuation.ai_credit_schism`）。AI infrastructure debt financing / vendor-financing loops 方面，荷蘭國際集團（ING）出售 12 筆資料中心貸款、規模約 500（2026-11-06，單位依來源原文），顯示銀行開始減持資料中心信用曝險（`structural.ai_infrastructure_debt`）。本次證據中未見任何 AI 基建借款人的付款違約、寬限期、covenant waiver 或 distressed exchange 公告；近期到期與再融資需求亦未在證據中披露。廣義信用仍平穩：HY OAS 3.48%（`monetary.hy_oas`）、IG OAS 0.93%（`monetary.ig_oas`）。

**判讀：** R3 是三條路徑中最接近「進行中」的一條：CDS 1289 bps 代表市場已為 CoreWeave 定價出相當高的違約風險。但 R3 需要實際的破產、逾寬限期違約或完成 distressed exchange，且借款人負債須達門檻；目前沒有任何事件層級證據。推過門檻的情境是再融資窗口關閉（殖利率持續 16% 以上無法展延）或大客戶承諾縮減，導致 distressed exchange——這需要觀察後續數月的到期表與融資公告。

## 支持 yes 的證據

- [R3] CoreWeave 五年期 CDS 突破 1289 bps（2026-11-05）、債券殖利率升破 16%（2026-11-06），在 NASDAQ 反彈期間仍走闊，信貸端已先行以 distressed 水準定價 AI 算力借款人（`valuation.ai_credit_schism`）。
- [R1] NASDAQ-100 一個月內自 31,224.69（2026-10-06）跌至 26,989.99（2026-11-06），距 52 週高點回撤 13.56%，R1 路程已過半（`valuation.ndx_drawdown`）。
- [整體] Fed 無法托底：12 月升息 25 bps 隱含機率 76.8%（2026-11-06，`monetary.fedwatch`），CPI YoY 3.72%（2026-09，`monetary.cpi_yoy`），WTI 99.64 美元（2026-11-03，`monetary.wti`），10Y 4.84%（`monetary.dgs10`）——下跌若擴大，政策緩衝空間有限。
- [R1] 波動急升：VIX 7 日 +63.84% 至 28.18（2026-11-05，`structural.vix_spx_comove`），SKEW 149.37、隱含相關性 20.93 創高（2026-11-06，`structural.cross_asset_derivatives`），尾部避險需求擴大。
- [R3] ING 出售 12 筆資料中心貸款、規模約 500（2026-11-06），銀行端主動減持 AI 資料中心信用曝險（`structural.ai_infrastructure_debt`）。
- [R1] 槓桿部位仍在加碼：半導體 3 倍多頭 ETF 10 月底規模 $24.31bn、當月淨流入 $7.27bn（`structural.leveraged_etf_aum`）；融資餘額約 $1.48T、年增約 31.4%（2026-09，`retail.margin_debt`），回撤加深時有強制去槓桿放大風險。
- [整體] 估值仍高：Shiller CAPE 38.91、S&P 500 trailing P/E 25.14（2026-11-06，`valuation.sp500_pe_cape`），Mag 7 前瞻本益比約 28.3（`valuation.mag7_multiples`），前十大權重約 37.9%（`breadth.top10_concentration`）。
- [R2] Microsoft 已將 2026 年 capex 指引自約 $175bn 下修至約 $170bn（2026-10-29，`ai.hyperscaler_capex`），四家中首家出現下修方向。

## 支持 no 的證據

- [整體] 基準率：任意 182 天窗口內 R1–R3 皆非常態；目前三條路徑沒有任何一條已觸發——R1 距門檻 23,418.52 仍需再跌約 13.23%（`valuation.ndx_drawdown`），R2 窗口內新下修為 0 家（`ai.hyperscaler_capex`）。
- [R3] 廣義信用未傳導：HY OAS 3.48%、IG OAS 0.93%（2026-11-05，`monetary.hy_oas`、`monetary.ig_oas`），CoreWeave 的壓力尚屬個別信用，未擴散為 AI 產業或高收益市場的系統性重定價。
- [整體] 資金市場無壓力：repo 資金壓力（SOFR−IORB）僅 2 bps、SOFR99−IORB 10 bps（2026-11-05），SRF 動用（Standing Repo Facility usage）為 0（2026-11-06）（`monetary.repo_stress_srf`）；OFR tri-party repo transaction volume $2,326.9bn（2026-11-06，`structural.treasury_basis_trade`），未見強制去槓桿的資金面觸發。
- [R2] hyperscaler 融資管道暢通：今年以來發債約 $296bn，10/29 起一週內 5 筆 AI 相關債券合計約 $67bn（2026-11-06，`ai.hyperscaler_financing_mix`），債市仍願意為 capex 融資，降低短期被迫砍 capex 的壓力。
- [R2] Microsoft 下修幅度僅約 3%（$175bn → $170bn），且發生在窗口起點之前，不計入 R2（`ai.hyperscaler_capex`）。
- [R1] 情緒已極度悲觀，屬逆向指標：Fear & Greed 22（2026-11-06，`retail.fear_greed`）、AAII 看空 48.4%（2026-11-04，`retail.aaii`）、put/call 1.05（2026-11-05，`speculation.equity_put_call`）；S&P 500 僅高於 200 日均線 0.42%（`valuation.sp500_trend`），價格延伸已大幅消化。
- [整體] AI 需求面仍有成長訊號：Anthropic 已遞交 S-1、目標估值 1.5 兆至 2 兆美元（2026-10-26，`speculation.upcoming_ai_ipos`），年化 AI 終端營收約 $135bn（`ai.revenue_capex_gap`），Bernstein 將 TSMC 目標價由 554 上調至 600（2026-11-03，`valuation.analyst_tp_decomposition`）。
- [整體] 投機熱度降溫而非過熱：本週唯一定價 IPO（`speculation.ipo_heat`），microcap moonshot 掃描 0 件（`speculation.microcap_moonshots`），顯示投機擴張期已過，下跌更像修正而非瘋狂頂部後的崩跌起點。

## 與前期比較

前次結論：無前次（基準）

本次為基準執行，無前次預測可比較；flip_evidence 為空。下次執行應重點追蹤：CoreWeave CDS／債券殖利率是否續升、NASDAQ-100 回撤是否擴大、Fed 12 月決議，以及 hyperscaler 指引。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下為 `✗ NOT DISCLOSED`（搜尋完成但無窗內合格披露）：retail.naaim、institutional.bofa_jpm_survey、monetary.treasury_auctions、monetary.private_credit_liquidity、ai.token_growth、ai.depreciation_life、ai.capital_cycle（quarterly_state 無可引證增速披露；event_scan 有 1 筆事件：Microsoft 10 月取消 Nscale 英國資料中心交易、規模約 3（2026-11-04），因組件聚合規則為 all，整體列為 ✗ NOT DISCLOSED，不作正文證據）、structural.global_leveraged_approvals。其中可能影響答案的是 monetary.private_credit_liquidity（若出現 gate proration / breach 或 net inflow→outflow flip，將強化 R3 傳導）與 monetary.treasury_auctions（標售轉弱會推升長端利率、加重 R1 壓力）；其餘缺口不太可能改變答案。

資料一致性注意：case/evidence.md 記載美債基差交易槓桿三個 script 區塊 fetch_failed 並改走 WebSearch（MOVE 93.88，2026-11-04），但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 三區塊皆為 status ok（MOVE 92.77，2026-11-06）。本次以 macro artifact 為準（✓ API），未使用該搜尋值。另 ai.hyperscaler_capex 僅取得 Microsoft 指引，Alphabet／Amazon／Meta 最新指引未在證據中出現，R2 計數因此可能低估或高估其他三家的方向。

最大不確定性：

1. CoreWeave 負債規模與再融資時程：若其負債達 50 億美元門檻且近期有到期，CDS 1289 bps 的定價意味 distressed exchange 在窗口內並非低可能事件，會把答案推向 yes。
2. Fed 12 月決議：實際升息並釋出續升訊號，會在高估值下推動 R1 再跌，推向 yes；若暫停或轉鴿，推向 no。
3. 2027 年初 hyperscaler 財報指引：Alphabet／Amazon／Meta 任兩家下修即觸發 R2；目前缺三家最新指引，是 R2 判斷的最大盲點。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest | 7353.73 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend ma200 | 7322.74 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 0.42（%） | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 1.84（%） | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 26989.99 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤） | 13.56（%） | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2 季資料） | 48.2301354474（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-11-08T09:30:00+08:00 |
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
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7d） | −2.7（bps） | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.92（%） | FRED API (series_id=SOFR) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 4.0（%） | FRED API (series_id=SOFR99) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.9（%） | FRED API (series_id=IORB) | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用） | 0.0（十億美元） | FRED API (series_id=RPONTTLD) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps（SOFR−IORB，兩腿皆 2026-11-05） | 2.0（bps） | FRED API (series_id=SOFR, IORB) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,748,145（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,945,410（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,261,882（¥626.19T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED API (series_id=VIXCLS) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of 2026-11-05，base 2026-10-29，window 7d，comove=false） | 28.18 | FRED API (series_id=VIXCLS, SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 63.84（%） | FRED API (series_id=VIXCLS) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | −4.75（%） | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2111.0042（$2.11T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位） | −7,249,305（口） | CFTC TFF futures-only | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | −489,473（口） | CFTC TFF futures-only | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo Finance chart API (^MOVE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party transaction volume） | 2326.9（十億美元） | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebFetch | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED（AI leader P/S vs 10 年均值未取得） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED（EPS／PE 拆解未披露） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
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
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED（僅取得 Microsoft） |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch：quarterly_state（stock-of-state）＋ event_scan（30d） | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch：quarterly_state（stock-of-state）＋ event_scan（30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED（1 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（7d movers screen） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED（僅取得半導體 3 倍多頭） |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe 月報） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻本益比約 28.3 | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein TSMC 目標價 554 → 600（EPS／PE 拆解未披露） | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/ | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 五年期 CDS 突破 1289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | RSP 年初至今報酬約 14.13%（SPY 對照值來源未列） | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 1,474 對下跌 1,252 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 22（極度恐懼） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 $1.48T、YoY 約 +31.4% | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔（TSLA、AMD、MU 等） | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 12 月升息 25 bps 隱含機率 76.8% | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000（原文單位） | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年 capex 指引約 $175bn → 約 $170bn（下修；Q3 2026 財報季） | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3（$bn） | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle RPO 638（$bn），單一 counterparty 拆分未披露 | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 $3.87／小時（利用率未披露） | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 今年以來發債約 $296bn | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 10/29 起一週內 5 筆 AI 相關債券發行合計約 $67bn | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 Anthropic $65bn ＋ OpenAI 約 $70bn ≈ $135bn（分母僅 Microsoft capex 指引） | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] Microsoft 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics 完成 SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO，週漲 8% | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描：0 件符合 2+ 主題×弱基本面 | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆美元 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描：0 件合格 | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe 股票選擇權 put/call 升至 1.05（日讀數） | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭 ETF 10 月底規模 $24.31bn、當月淨流入 $7.27bn | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 總結算量 1,486,062,415 口（2026-09 月資料） | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性 20.93 創高 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-09 月資料）交叉檢核基數約 $1.48T | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.ai_infrastructure_debt | ING 出售 12 筆資料中心貸款，規模約 500（原文單位） | AI data center debt financing private credit November 2026 | https://www.cnbc.com/2026/11/06/ing-ai-data-center-loans-debt.html | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

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

> [DRY RUN] this report was not committed to archive.

# 2026-11-08 AI 泡沫破裂預測報告

報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：無（基準）

## 結論

**結論：no**

R1 距門檻仍需自最新收盤再跌約 13.23%，而 HY／IG OAS（3.48%／0.93%）與 repo 資金壓力（SOFR−IORB 2 bps、SRF 動用 0）顯示壓力仍侷限在 AI 股權與 CoreWeave 等個別 AI 信用，尚未擴散為整體信用或融資失序；hyperscaler 單週仍能完成約 67（十億美元）AI 相關發債，R2 需窗口內兩家新下修、R3 需實際違約／distressed exchange，目前皆無已發生的觸發事件。最強的反方證據是 CoreWeave 5 年期 CDS 約 1289 bps、債券殖利率破 16%，加上 12 月升息定價，若 CoreWeave 走向 distressed exchange 將同時觸發 R3 並拖動 R1，這是本次結論最可能被推翻的路徑。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 26,989.99（2026-11-06），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 13.56%（`valuation.ndx_drawdown`）。R1 門檻水位為 23,418.52，需自最新收盤再下跌約 13.23% 才觸及。回撤在一個月內由高點形成，速度快：同期 S&P 500 在 2026-10-29 → 2026-11-05 的 7 日間跌 4.75%、VIXCLS 同期升 63.84% 至 28.18（`structural.vix_spx_comove`，屬正常的股跌波升，非 crowded-optionality 共振）；S&P 500 僅高於 200 日均線 0.42%、高於 52 週均線 1.84%（`valuation.sp500_trend`），趨勢延伸已大致消化。估值仍高：Shiller CAPE 38.91、trailing P/E 25.14（2026-11-06，`valuation.sp500_pe_cape`），Mag 7 前瞻 P/E 約 28.3（2026-10-13，`valuation.mag7_multiples`），前十大權重約 37.9%（`breadth.top10_concentration`），代表若有催化劑，下行空間足以達到 R1。情緒端已進入極度恐懼：CNN Fear & Greed 22（2026-11-06，`retail.fear_greed`）、AAII 看空 48.4% 對看多 34.1%（2026-11-04，`retail.aaii`）、Cboe equity put/call 1.05（2026-11-05，`speculation.equity_put_call`），短線拋售已相當擁擠。

**判讀：** R1 已走完一半路程，但剩餘 13% 以上的跌幅需要新的催化劑（AI 信用事件、12 月升息後的利率衝擊、或下一輪季報 capex 下修）；在 HY 利差仍緊、情緒已極度悲觀的條件下，單靠估值回歸不足以在窗口內完成，若 CoreWeave 信用惡化擴散或 Fed 升息引發利率再走高，則可能推過門檻。

### R2 資本支出收縮

- Microsoft：2026 年 capex 指引自約 175 下調至約 170（十億美元，依來源語境；2026-10-29 季報），方向：下修（`ai.hyperscaler_capex`）。
- Alphabet：本次證據未取得最新指引，方向不可判。
- Amazon：本次證據未取得最新指引，方向不可判。
- Meta：本次證據未取得最新指引，方向不可判。

R2 只計窗口內（2026-11-08 起）的下修；Microsoft 的 2026-10-29 下修早於窗口起點，不計入，因此窗口內已下修家數為 0 / 4。窗口內預計涵蓋下一輪（2027 年 1 月下旬前後）與再下一輪（2027 年 4 月下旬前後）季報，但本次證據未提供具體財報日期。融資面：hyperscaler 年初至今發債約 296、2026-10-29 起一週內 5 筆 AI 相關債券合計約 67（十億美元，`ai.hyperscaler_financing_mix`），顯示 capex 正從現金流轉向債務融資，債市目前仍願意承接。AI 營收對 capex 缺口（revenue-to-capex gap）：Anthropic 約 65 ＋ OpenAI 約 70，年化 AI 終端營收合計約 135（2026-09-30，`ai.revenue_capex_gap`），對照年化 capex 約 170（分母：僅 Microsoft，其餘三家與 Oracle 本次未取得），單一公司 capex 已高於兩大 AI 實驗室的合計 run-rate。

**判讀：** Microsoft 已率先下修，是方向訊號，但 R2 需要窗口內兩家新的正式下修；在債市仍暢通、AI 實驗室營收仍在成長的情況下，下一輪季報出現兩家同時下修並非基準情境，除非 R1 / R3 先發生而迫使 capex 收縮。

### R3 AI 信用事件

符合規模門檻的 AI 算力借款人中，CoreWeave 是信用定價最差者：債券殖利率升破 16%（2026-11-06），5 年期 CDS 突破 1289 bps（2026-11-05）（`valuation.ai_credit_schism`）——這已是 distressed 區間的定價，且發生在 NASDAQ 反彈期間，屬典型的「信用先於股權重定價」後期訊號。AI infrastructure debt financing / vendor-financing loops 方面，ING 出售 12 筆資料中心貸款、規模約 500（2026-11-06，`structural.ai_infrastructure_debt`），顯示銀行開始降低資料中心授信曝險。Oracle 剩餘履約義務約 638（2026-08-31，`ai.customer_concentration_rpo`）凸顯 AI 承諾高度集中於少數終端客戶，但本次無可量化的 backlog 重複計算風險（RPO double-counting）加總。本次證據未見任何 AI 借款人發生付款違約、寬限期、covenant waiver、distressed exchange 或 going-concern 語句，亦未取得 CoreWeave 具體債務到期時程。

**判讀：** CoreWeave 的 CDS／殖利率已把 R3 從遠端尾部拉近為可見風險，但 R3 要求已發生的破產、超過寬限期違約或完成 distressed exchange；在無到期牆與流動性缺口證據的情況下，六個月內完成信用事件仍非多數情境，若出現 covenant 違反、融資失敗或交換要約公告即會迅速推向 yes。

## 支持 yes 的證據

- [R3] CoreWeave 5 年期 CDS 突破 1289 bps（2026-11-05）、債券殖利率升破 16%（2026-11-06），信用端已按 distressed 定價，是 R3 最直接、且可透過拋售傳導至 R1 的路徑（`valuation.ai_credit_schism`）。
- [R1] NASDAQ-100 自 2026-10-06 高點 31,224.69 跌至 26,989.99（2026-11-06），距 52 週高點回撤 13.56%，一個月內已完成門檻一半以上的距離（`valuation.ndx_drawdown`）。
- [整體] 12 月升息 25 bps 的市場定價約 76.8%（2026-11-06，`monetary.fedwatch`），而 CPI YoY 3.72%（2026-09，`monetary.cpi_yoy`）、WTI 99.64（2026-11-03，`monetary.wti`），Fed 在 AI 主導的下跌中難以提供寬鬆緩衝。
- [R2] Microsoft 於 2026-10-29 將 2026 年 capex 指引自約 175 下修至約 170，四家中已有一家轉向（`ai.hyperscaler_capex`）；同時 hyperscaler 年初至今發債約 296，capex 依賴債務融資的程度上升（`ai.hyperscaler_financing_mix`）。
- [R3] ING 出售 12 筆資料中心貸款、規模約 500（2026-11-06），銀行端開始撤出 AI 資料中心授信（`structural.ai_infrastructure_debt`）。
- [R1] 估值仍處高位：Shiller CAPE 38.91、trailing P/E 25.14（2026-11-06，`valuation.sp500_pe_cape`），前十大權重約 37.9%（`breadth.top10_concentration`），下行空間足以達到 R1。
- [整體] 10Y 殖利率 4.84%（`monetary.dgs10`）、實質殖利率 2.6%（`monetary.dfii10`），高折現率對長存續期 AI 股估值不利。

## 支持 no 的證據

- [整體] 基準比率：任一 182 天窗口內 R1–R3 均非常態；目前 R1 尚需再跌約 13.23%（門檻 23,418.52，`valuation.ndx_drawdown`），R2 窗口內下修家數為 0，R3 尚無任何違約或交換事件。
- [R3] 整體信用未失序：HY OAS 3.48%（`monetary.hy_oas`）、IG OAS 0.93%（`monetary.ig_oas`）（2026-11-05），AI 信用壓力仍是個別發行人問題，未擴散為廣泛信用重定價。
- [整體] 資金市場平靜：SOFR 3.92% 對 IORB 3.9%、SOFR−IORB 2 bps，SOFR99 4.0%，SRF 動用 0（`monetary.repo_stress_srf`）；CFTC 槓桿基金美債期貨淨部位 -7,249,305 口（2026-11-03）、MOVE 92.77（2026-11-06，`structural.treasury_basis_trade`），未見國債市場失序（Treasury market dysfunction）。
- [R2] hyperscaler 債市通道暢通：2026-10-29 起一週內 5 筆 AI 相關債券合計約 67（`ai.hyperscaler_financing_mix`），融資能力未受限，降低被迫砍 capex 的壓力。
- [R1] 情緒已極度悲觀，短線拋售擁擠：Fear & Greed 22（`retail.fear_greed`）、AAII 看空 48.4%（`retail.aaii`）、equity put/call 1.05（`speculation.equity_put_call`）；S&P 500 僅高於 200 日均線 0.42%（`valuation.sp500_trend`），延伸已消化。
- [R2] AI 需求端仍在擴張：Anthropic ＋ OpenAI 年化營收合計約 135（`ai.revenue_capex_gap`），Anthropic 已遞交 S-1、目標估值 1.5 兆至 2 兆（2026-10-26，`speculation.upcoming_ai_ipos`），資本市場仍願意為 AI 定價。
- [R1] 市場廣度未崩：2026-11-06 紐交所上漲 1,474 家對下跌 1,252 家（`breadth.advance_decline`），等權指數年初至今約 +14.13%（`breadth.rsp_spy`）。

## 與前期比較

前次結論：無前次（基準）

本次為基準執行，無前次預測可比較，`flip_evidence` 為空陣列；10Y Δ 分解為 baseline_no_prior（無前次比較日），不適用週變動判讀。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

未揭露（✗ NOT DISCLOSED）來源：`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.treasury_auctions`、`monetary.private_credit_liquidity`、`ai.token_growth`、`ai.depreciation_life`、`ai.capital_cycle`、`structural.global_leveraged_approvals`。其中可能影響結論者：
- `monetary.private_credit_liquidity`：若私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）出現 gate proration / breach，將強化 R3 與 R1 傳導；本次搜尋完成但 30 日內無揭露，不改變結論。
- `ai.capital_cycle`：event_scan 找到 Microsoft 於 2026-11-04 報導收緊 neocloud 專案、取消 Nscale 英國資料中心交易（規模約 3），但 quarterly_state 無可用增速對比，依 component_aggregation all 判為未揭露，不作為正式證據；該事件方向偏 yes（資本週期轉折訊號）。
- `monetary.treasury_auctions`：無窗口內標售數據，無法排除財政供給壓力，但 MOVE 與 repo 數據未顯示異常。

部分取得（狀態為成功但涵蓋不完整）：
- `ai.hyperscaler_capex` 僅取得 Microsoft；Alphabet、Amazon、Meta 最新指引未在證據中出現。這是最可能改變判讀的缺口：若其中已有公司在最近季報下修，代表 R2 的方向動能比本次判讀更強（雖然窗口前的下修不計入 R2）。
- `breadth.rsp_spy` 僅有 RSP 年初至今約 +14.13%，SPY 同期數值未取得，等權對市值加權的落差無法計算。
- `retail.margin_debt` 僅取得融資餘額約 1.48 兆美元、年增約 31.4%（2026-09），margin debt / 市值比未計算。
- `structural.leveraged_etf_aum` 僅取得半導體 3 倍多頭基金規模 24.31、10 月淨流入 7.27，未逐檔涵蓋 NVDL、TSLL、CONL、TQQQ、SOXL、SQQQ。
- `structural.cross_asset_derivatives` 未取得滾動股債相關係數。
- `valuation.analyst_tp_decomposition` 僅取得 Bernstein 將 TSMC 目標價由 554 上調至 600（2026-11-03），EPS 與目標 PE 的分解未揭露，無法判定主導成分。
- 多數搜尋摘錄未標註金額單位；報告中依語境標示（如 capex、發債以十億美元理解），未能確認者保留原值。
- 證據檔將 `structural.treasury_basis_trade` 描述為「script 三區塊 fetch_failed → WebSearch fallback」（MOVE 搜尋值 93.88，2026-11-04），但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 三塊皆為 ok；本報告以 macro artifact 為準，記 ✓ API，不使用 fallback 值。

最大不確定性：
1. CoreWeave 的債務到期與流動性：CDS 1289 bps 已屬 distressed 定價，若出現交換要約或融資失敗，R3 與 R1 可能同時成立，推向 yes。
2. 12 月 FOMC 升息與通膨路徑：若升息後 10Y 與期限溢價再走高，估值壓縮可能把 NASDAQ-100 推向門檻，推向 yes；若通膨降溫、升息落空，推向 no。
3. 下一輪 hyperscaler 季報（約 2027 年 1 月下旬）：若 Alphabet／Amazon／Meta 中有兩家跟進 Microsoft 下修，R2 直接成立，推向 yes；若維持或上修，推向 no。

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
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（回撤 %） | 13.56 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2 資料，家戶股票占金融資產 %） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 4.0 | FRED API (series_id=DFEDTARU) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.75 | FRED API (series_id=DFEDTARL) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 3.48 | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.93 | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.84 | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.6 | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.23 | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（美元／桶） | 99.64 | FRED API (series_id=DCOILWTICO) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料，YoY %） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.17 | FRED API (series_id=T5YIFR) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright 10Y 期限溢價 %） | 0.9089 | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（序列自身 trailing 7 日變動） | -2.7 | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.92 | FRED API (series_id=SOFR) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（99th 分位 %） | 4.0 | FRED API (series_id=SOFR99) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.9 | FRED API (series_id=IORB) | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用 transaction volume，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,748,145（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,945,410（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,261,882（¥626.19T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED API (series_id=VIXCLS) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of） | 28.18 | FRED API 衍生區塊 vix_spx_comove（window 7 日，base 2026-10-29） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日 %） | 63.84 | FRED API 衍生區塊 vix_spx_comove | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日 %） | -4.75 | FRED API 衍生區塊 vix_spx_comove | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2111.0042（$2.11T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7,249,305 | CFTC TFF futures-only | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -489,473 | CFTC TFF futures-only | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo Finance chart API (^MOVE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2326.9 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebFetch | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED（AI leader P/S vs 10 年均值未取得） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d、同季） | ✓ SEARCH-VERIFIED（分解成分未揭露） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED（僅 RSP，SPY 未取得） |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED（新高／新低比未取得） |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（stock-of-state，2026-09 月資料） | ✓ SEARCH-VERIFIED（市值比未計算） |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py BOGZ1FL153064486Q | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch primary | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py DFEDTARU + DFEDTARL | ✓ API（DFEDTARU ok；DFEDTARL ok） |
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
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch primary（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch primary | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py WALCL | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py ECBASSETSW + JPNASSETS | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch primary（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state，最新季報） | ✓ SEARCH-VERIFIED（僅 Microsoft；GOOGL／AMZN／META 未取得） |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch primary | ✓ SEARCH-VERIFIED（RPO double-counting 無可量化加總） |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch primary | ✓ SEARCH-VERIFIED（僅價格，無利用率） |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch primary：quarterly_state 承接最新發債趨勢、event_scan 30d | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch primary（分母僅 Microsoft） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch primary（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch primary：quarterly_state 無增速對比、event_scan 30d 有事件 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch primary（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch primary | ✓ SEARCH-VERIFIED（未逐檔涵蓋） |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe 月報） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED（股債相關係數未取得） |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py VIXCLS + vix_spx_comove | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（交叉檢核） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch primary（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py LNFACBW027SBOG | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds、move_index、ofr_repo | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻 P/E 約 28.3 | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein 將 TSMC 目標價由 554 上調至 600（EPS／PE 分解未揭露） | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/ | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5 年期 CDS 突破 1289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | RSP 年初至今報酬約 14.13% | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | 紐交所上漲 1,474 對下跌 1,252 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 22（極度恐懼） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 1.48 兆美元、YoY 約 31.4% | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔 | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 12 月升息 25 bps 定價 76.8% | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000 | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年 capex 指引自約 175 下調至約 170 | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3 | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle 剩餘履約義務 638 | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87 | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 年初至今發債 296 | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 2026-10-29 起一週內 5 筆 AI 相關債券發行合計 67 | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic 65 ＋ OpenAI 約 70，合計約 135 | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] Microsoft 收緊 neocloud 資料中心專案、10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics 完成 SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO 週漲 8 | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描：0 件符合 2+ 主題 × 弱基本面 | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描：0 件合格 | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 升至 1.05（日讀數） | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭基金 10 月底規模 24.31、當月淨流入 7.27 | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 9 月總結算量 1,486,062,415 口（2026-09 月資料） | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性創高 20.93 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 交叉檢核（2026-09 月資料）約 1.48 兆美元 | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
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
  "prior_date": null,
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 13.56,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

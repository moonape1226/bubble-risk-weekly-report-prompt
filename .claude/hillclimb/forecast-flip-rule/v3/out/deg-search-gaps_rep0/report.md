> [DRY RUN] this report was not committed to archive.

# 2026-11-08 AI 泡沫破裂預測報告

報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：report-2026-10-18（21天前）

## 結論

**結論：no**

三條路徑都已出現壓力，但沒有一條在現有證據下「更可能完成」：R1 的 NASDAQ-100 距 52 週高點回撤 13.56%，仍需自最新收盤再跌約 13.23% 才觸及門檻，而 HY OAS 3.48%、SOFR−IORB 2 bps 顯示廣義信用與資金市場尚未傳導；R2 目前僅 Microsoft 一家下修（需兩家）；R3 最受壓的 CoreWeave 雖債券殖利率逾 16%、CDS 1289 bps，但本次未見任何違約／交換事件，且其負債是否達 50 億美元門檻本次來源未能確立。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

FRED `NASDAQ100` 最新收盤 26,989.99（2026-11-06），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 13.56%。R1 門檻水位為 23,418.52，自最新收盤還需再跌 3,571.47 點（約 13.23%）才會觸發（`valuation.ndx_drawdown`）。壓力訊號同步升高：VIX 2026-11-05 收 28.18，在 2026-10-29 → 2026-11-05 的 7 日共同窗口內上升 63.84%，同期 S&P 500 下跌 4.75%，屬典型的股跌波動升（非 crowded-optionality 的同漲型態，`comove: false`）（`structural.vix_spx_comove`）。S&P 500 2026-11-05 為 7,353.73，仍高於 200 日均線 0.42%、高於 52 週均線 1.84%，自前次基準日（2026-10-16 觀測）下跌 3.99%（`valuation.sp500_trend`）。Cboe 股票賣買權比 1.05（2026-11-05）、CNN Fear & Greed 22（極度恐懼，2026-11-06）（`speculation.equity_put_call`、`retail.fear_greed`）。估值仍高：Shiller CAPE 38.91、S&P 500 trailing P/E 25.14（2026-11-06，`valuation.sp500_pe_cape`），Mag 7 群體前瞻本益比約 28.3（`valuation.mag7_multiples`）。

**判讀：** R1 已走完約一半的距離，回撤在一個月內從高點展開，速度不慢；但要在窗口內再跌約 13% 需要一個額外催化劑——例如 12 月 FOMC 意外升息落地、R3 方向的信用事件引爆，或 R2 第二家 hyperscaler 下修造成 AI 敘事重估。在廣義信用利差與資金市場仍平穩的情況下，現有證據不足以判定此跌勢更可能延伸至 25%。

### R2 資本支出收縮

- Microsoft：2026-10-29 披露將 2026 年資本支出指引自約 175 下調至約 170（來源摘錄未標單位），方向為**下修**（`ai.hyperscaler_capex`）。來源網址字串標示「q3-fy2026」「190b」，與摘錄數字及披露日期不一致，該筆指引所屬季度與確切數字存在不確定性。
- Alphabet：本次來源未取得最新正式指引，方向不可判定。
- Amazon：本次來源未取得最新正式指引，方向不可判定。
- Meta：本次來源未取得最新正式指引，方向不可判定。

目前四家中已確認下修 1 家（Microsoft），R2 需要 2 家。下一次財報的具體日期本次來源未取得；依季報節奏，2026 年第四季與 2027 年第一季兩輪財報季均落在窗口（至 2027-05-09）之內，等於 R2 在窗口內有兩次觸發機會。需求側對照：年化 AI 終端營收 Anthropic 65 ＋ OpenAI 約 70，合計約 135（2026-09-30 資料，摘錄未標單位）vs 年化 capex 約 170（分母：僅 Microsoft；Alphabet／Amazon／Meta 指引與 Oracle 季頻資料本次均未取得），因無前次可比組合，缺口方向本次不判定（`ai.revenue_capex_gap`）。Anthropic 上半年營收 16.3（2026-10-26 報導，`ai.openai_anthropic_revenue`）。H100 隨選租金中位數 3.87（2026-11-03，`ai.compute_supply_demand`）——僅單點價格，無利用率配對，不構成產能過剩證據。

**判讀：** R2 已有一家下修，是三條路徑中「進度」最具體的一條；但其餘三家的指引本次完全沒有取得，無法判斷是否有第二家正在轉向。若 2026 Q4 財報季（窗口內）Alphabet、Amazon 或 Meta 任一家下修，R2 即成立；R1 繼續下跌會提高這個可能性。在缺乏三家現況的情況下，不能把 1/4 外推成「更可能達到 2/4」。

### R3 AI 信用事件

- CoreWeave：債券殖利率升破 16%（2026-11-06）、五年期 CDS 突破 1289 bps（2026-11-05），AI 信用定價已明顯脫離一般高收益信用（`valuation.ai_credit_schism`）；同期 HY OAS 僅 3.48%（2026-11-05，較 2026-10-16 走闊 17 bps，`monetary.hy_oas`）。這是 AI 信用定價分歧（equity-vs-credit schism）中「信貸端開始重定價」的後期訊號。
- CoreWeave 的總負債、近期到期與再融資時間表，本次來源均未取得，是否達 R3「負債 ≥ 50 億美元」門檻本次無法確立（不以記憶數字補齊）。
- AI infrastructure debt financing / vendor-financing loops：ING 出售 12 筆資料中心貸款，規模約 500（2026-11-06，摘錄未標單位），顯示銀行端在轉移 AI 資料中心信用曝險（`structural.ai_infrastructure_debt`）。
- 本次來源中未見任何 AI 基礎設施借款人的破產申請、超過寬限期的付款違約、covenant waiver、distressed exchange 或 going-concern 文字。

**判讀：** R3 的市場定價已到 distressed 區間，是三條路徑中尾部風險最高的一條；但 R3 需要實際的違約／破產／完成 distressed exchange 事件，而本次既無事件、也無法確立最受壓借款人的規模與到期牆。若窗口內出現 CoreWeave 或同類借款人的付款違約或交換要約，R3 會直接觸發並可能帶動 R1；目前證據只支持「風險升高」，不支持「更可能完成」。

## 支持 yes 的證據

- [R3] CoreWeave 債券殖利率升破 16%（2026-11-06）、五年期 CDS 突破 1289 bps（2026-11-05），AI 信用已進入 distressed 定價，是窗口內信用事件最直接的前兆（`valuation.ai_credit_schism`）。
- [R2] Microsoft 2026-10-29 將 2026 年資本支出指引自約 175 下調至約 170，R2 所需的兩家下修已出現一家，2026 Q4 與 2027 Q1 兩輪財報季都在窗口內（`ai.hyperscaler_capex`）。
- [R1] NASDAQ-100 自 2026-10-06 高點 31,224.69 跌至 2026-11-06 的 26,989.99，距 52 週高點回撤 13.56%，一個月內走完 R1 一半路程（`valuation.ndx_drawdown`）；VIX 2026-11-05 為 28.18、7 日上升 63.84%（`structural.vix_spx_comove`）。
- [整體] Fed 緩衝空間受限：CME FedWatch 顯示 12 月升息 25 bps 機率 76.8%（2026-11-06，`monetary.fedwatch`），CPI YoY 3.72%（2026-09 月資料，`monetary.cpi_yoy`），聯邦基金目標區間 3.75%–4.00%（2026-11-07，`monetary.fed_funds`）——跌勢中央行降息托底的可能性低，反而有緊縮催化劑。
- [整體] 脆弱性高：Shiller CAPE 38.91、trailing P/E 25.14（2026-11-06，`valuation.sp500_pe_cape`）；融資餘額約 1.48 兆美元、年增約 31.4%（2026-09 月資料，`retail.margin_debt`）；前十大成分股權重約 37.9%（2026-11-01，`breadth.top10_concentration`）——下跌一旦延續，去槓桿放大空間大。
- [整體] 選擇權避險需求急升：Cboe 股票賣買權比 1.05（2026-11-05，`speculation.equity_put_call`）；SKEW 149.37、隱含相關性創高 20.93（2026-11-06，`structural.cross_asset_derivatives`）；0DTE 佔 SPX 選擇權量約 65%（2026-10 資料，`structural.zero_dte`）。
- [R3] ING 出售 12 筆資料中心貸款、規模約 500（2026-11-06），銀行端主動轉移 AI 資料中心信用曝險（`structural.ai_infrastructure_debt`）。

## 支持 no 的證據

- [R1] R1 仍需自 26,989.99 再跌 3,571.47 點（約 13.23%）至 23,418.52 才觸發；S&P 500 仍高於 200 日均線 0.42%、高於 52 週均線 1.84%（2026-11-05），大盤並未進入趨勢性破位（`valuation.ndx_drawdown`、`valuation.sp500_trend`）。
- [整體] 廣義信用尚未傳導：HY OAS 3.48%、IG OAS 0.93%（2026-11-05），自 2026-10-16 僅分別走闊 17 bps 與 8 bps，AI 信用壓力仍侷限於個別發行人（`monetary.hy_oas`、`monetary.ig_oas`）。
- [整體] 資金與美債市場平穩：SOFR−IORB 2 bps、SOFR99−IORB 10 bps（2026-11-05），SRF 動用 0（RPONTTLD 2026-11-06）（`monetary.repo_stress_srf`）；MOVE 92.77（2026-11-06），較 2026-10-16 下降 8.33（`structural.treasury_basis_trade`）；10Y 殖利率 4.84%（2026-11-05），自 2026-10-16 下降 25 bps，金融條件反而放鬆（`monetary.dgs10`）。
- [R2] 四家中僅一家下修，Microsoft 下修後的指引水位（約 170）仍屬高位；AI 終端需求仍在擴張：Anthropic 年化營收 65 ＋ OpenAI 約 70（2026-09-30，`ai.revenue_capex_gap`），Anthropic 已遞交 S-1、目標估值 1.5 兆至 2 兆（2026-10-26，`speculation.upcoming_ai_ipos`），股權市場仍對 AI 開放。
- [R3] 本次所有 AI 信用證據都是「定價」而非「事件」：CoreWeave 殖利率與 CDS 走闊，但來源未載任何付款違約、寬限期、交換要約或破產申請（`valuation.ai_credit_schism`）；銀行對 NBFI 放款 2026-10-28 為 2111.0042 十億美元（$2.11T），自 2026-10-14 再增 0.27%，信用供給未收縮（`structural.nbfi_bank_loans`）。
- [整體] 散戶情緒已大幅退潮、逢低買盤仍在：AAII 看多 34.1%、看空 48.4%（2026-11-04，`retail.aaii`）；半導體 3 倍多頭基金 10 月淨流入 7.27、月底規模 24.31（2026-10-31，`structural.leveraged_etf_aum`）——恐慌已部分反映在價格與部位中，非全面去槓桿。
- [整體] 基準率：任一 182 天窗口內 NASDAQ-100 回撤 25%、兩家 hyperscaler 同時下修、或 50 億美元以上 AI 基礎設施違約，都是少見事件；本次三條路徑各自都缺一個「已發生的關鍵步驟」（R1 缺後半段跌幅、R2 缺第二家、R3 缺實際違約事件）（`valuation.ndx_drawdown`、`ai.hyperscaler_capex`）。

## 與前期比較

前次結論：無前次預測（report-2026-10-18 為舊格式評分報告）

舊格式評分不轉譯為 yes/no；本次為新格式下的第一份預測，flip_evidence 為空。自 2026-10-18 以來的主要變化：

- NASDAQ-100 自 2026-10-06 高點起回撤擴大至 13.56%（`valuation.ndx_drawdown`），VIX 由 2026-10-16 的 19.99 升至 2026-11-05 的 28.18（`structural.vix_spx_comove`）。
- Microsoft 於 2026-10-29 下修資本支出指引，R2 出現第一家（`ai.hyperscaler_capex`）。
- CoreWeave 信用定價在 2026-11-05／06 進入 distressed 區間（`valuation.ai_credit_schism`）。
- 12 月升息定價升至 76.8%（`monetary.fedwatch`），而 10Y 殖利率同期下降 25 bps（`monetary.dgs10`）。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `valuation.analyst_tp_decomposition`（⛔ FETCH FAILED，搜尋技術失敗）：屬估值敘事的輔助拆解，不涉 R1–R3 觸發條件，不會改變結論。
- `ai.hyperscaler_financing_mix`（⛔ FETCH FAILED，兩組件皆技術失敗）：缺 top-5 的 capex vs FCF 季頻狀態與 30 日 hyperscaler 發債／SPV 事件掃描，也使 AI 營收對 capex 缺口的分母缺 Oracle。若 hyperscaler 正以大規模發債或表外結構支撐 capex，會提高 R2（被迫削減）與 R3 的尾部風險；此缺口有可能改變判斷的強度，但單憑缺口不足以翻成 yes。

✗ NOT DISCLOSED（選填來源，搜尋完成但無合格披露）：`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.treasury_auctions`、`monetary.private_credit_liquidity`、`ai.token_growth`、`ai.customer_concentration_rpo`、`ai.depreciation_life`、`ai.capital_cycle`、`structural.global_leveraged_approvals`。其中 `ai.customer_concentration_rpo` 的唯一結果（Oracle RPO 638）網址日期為 2026-07-02、資料日卻標 2026-08-31，日期互相矛盾且未涉客戶集中度或跨供應商重複計算，因此不作證據；`ai.capital_cycle` 的 event_scan 找到微軟 10 月取消 Nscale 英國資料中心交易（規模約 3，2026-11-04 報導），但 quarterly_state 無增速披露，依 all 聚合為 ✗ NOT DISCLOSED，該事件僅作背景——它與 R2 方向一致，值得下次追蹤。

其他資料問題：

- `structural.treasury_basis_trade` 的搜尋紀錄寫「script 三區塊 fetch_failed → WebSearch fallback」，但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 皆為 `status: ok`；本報告以 artifact 為準（✓ API，MOVE 92.77），搜尋所得 MOVE 93.88（2026-11-04）不採用。
- 10Y Δ 分解：ΔDGS10 −25 bps、ΔDFII10 −14 bps、ΔT10YIE −12 bps，但 T10YIE 視窗（至 2026-11-06）與另兩腿（至 2026-11-05）不一致，driver 判讀：不可判（視窗不一致）。
- Microsoft 指引摘錄未標單位，且來源網址字串（q3-fy2026、190b）與摘錄不一致。

最大的不確定性：

1. **Alphabet／Amazon／Meta 的資本支出指引現況（R2）**：本次完全未取得。若其中任一家在最近一次財報已下修，R2 即已成立，答案應為 yes；若三家皆上修，R2 距離更遠。此項推向 yes 的潛在力道最大。
2. **CoreWeave 的負債規模與到期牆（R3）**：若可確立負債 ≥ 50 億美元且近月有大額到期或再融資受阻，R3 在窗口內完成的可能性將顯著上升，推向 yes。
3. **12 月 FOMC（R1）**：76.8% 的升息定價若落地並伴隨更鷹派指引，會成為 R1 後半段跌幅的催化劑（推向 yes）；若暫停升息，則壓力緩解（推向 no）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7353.73 | FRED API（series_id=SP500）→ sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 0.42 | FRED API（series_id=SP500）→ sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 1.84 | FRED API（series_id=SP500）→ sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較前次基準 %） | −3.99 | FRED API（series_id=SP500）→ sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 26989.99 | FRED API（series_id=NASDAQ100）→ ndx_drawdown | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API（series_id=NASDAQ100）→ ndx_drawdown | 2026-10-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 13.56 | FRED API（series_id=NASDAQ100）→ ndx_drawdown | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API（series_id=NASDAQ100）→ ndx_drawdown | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2 季資料） | 48.2301354474（%） | FRED API（series_id=BOGZ1FL153064486Q） | 2026-04-01 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標上限） | 4.0（%） | FRED API（series_id=DFEDTARU） | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標下限） | 3.75（%） | FRED API（series_id=DFEDTARL） | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 3.48（%） | FRED API（series_id=BAMLH0A0HYM2） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 17.0（bps，vs 2026-10-16） | FRED API（series_id=BAMLH0A0HYM2） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.93（%） | FRED API（series_id=BAMLC0A0CM） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM delta_bps | 8.0（bps，vs 2026-10-16） | FRED API（series_id=BAMLC0A0CM） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.84（%） | FRED API（series_id=DGS10） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | −25.0（bps，vs 2026-10-16） | FRED API（series_id=DGS10） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.6（%） | FRED API（series_id=DFII10） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | −14.0（bps，vs 2026-10-16） | FRED API（series_id=DFII10） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.23（%） | FRED API（series_id=T10YIE） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | −12.0（bps，vs 2026-10-16） | FRED API（series_id=T10YIE） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 99.64（USD/bbl） | FRED API（series_id=DCOILWTICO） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO chg_pct | −7.92（%，vs 2026-10-16） | FRED API（series_id=DCOILWTICO） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72（%） | FRED API（series_id=CPIAUCSL） | 2026-09-01 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.17（%） | FRED API（series_id=T5YIFR） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.9089（%） | FRED API（series_id=THREEFYTP10） | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7d） | −2.7（bps） | FRED API（series_id=THREEFYTP10） | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.92（%） | FRED API（series_id=SOFR） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 4.0（%） | FRED API（series_id=SOFR99） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.9（%） | FRED API（series_id=IORB） | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用 transaction volume） | 0.0（十億美元） | FRED API（series_id=RPONTTLD） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps（SOFR−IORB，兩腿皆 2026-11-05） | 2.0（bps） | FRED API（SOFR、IORB）→ repo_stress | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr99_iorb_bps（SOFR99−IORB，兩腿皆 2026-11-05） | 10.0（bps） | FRED API（SOFR99、IORB）→ repo_stress | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,748,145（$6.75T，百萬美元） | FRED API（series_id=WALCL） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,945,410（€5.95T，百萬歐元） | FRED API（series_id=ECBASSETSW） | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（無新觀測） | 6,261,882（¥626.19T，億日圓） | FRED API（series_id=JPNASSETS） | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED API（series_id=VIXCLS） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（共同窗口終點） | 28.18 | scripts/fetch_macro.py vix_spx_comove（FRED SP500 對齊） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（base 2026-10-29） | 63.84（%） | scripts/fetch_macro.py vix_spx_comove（FRED SP500 對齊） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（base 2026-10-29） | −4.75（%） | scripts/fetch_macro.py vix_spx_comove（FRED SP500 對齊） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2111.0042（$2.11T，十億美元） | FRED API（series_id=LNFACBW027SBOG） | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG chg_pct | 0.27（%，vs 2026-10-14） | FRED API（series_id=LNFACBW027SBOG） | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位） | −7,249,305（口） | CFTC TFF futures-only → cftc_lev_funds | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | −489,473（口） | CFTC TFF futures-only → cftc_lev_funds | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo Finance chart API（^MOVE）→ move_index | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index delta_abs（vs 2026-10-16） | −8.33 | Yahoo Finance chart API（^MOVE）→ move_index | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party transaction volume） | 2326.9（十億美元） | OFR STFM（REPO-TRIV1_TV_TOT-P）→ ofr_repo | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebFetch | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ⛔ FETCH FAILED（搜尋技術失敗） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py BOGZ1FL153064486Q | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED（無當週數值） |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED（無窗內新調查） |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py DFEDTARU＋DFEDTARL | ✓ API（DFEDTARU ok、DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py BAMLH0A0HYM2 | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py BAMLC0A0CM | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py DGS10 | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | scripts/fetch_macro.py DFII10 | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py T10YIE（FRED 直接取得） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py DCOILWTICO | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | scripts/fetch_macro.py CPIAUCSL yoy_pct | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py T5YIFR | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py THREEFYTP10 | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py SOFR＋SOFR99＋IORB＋RPONTTLD | ✓ API（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok；repo_stress status ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✗ NOT DISCLOSED（窗內無值得記錄的標售結果） |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py WALCL | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py ECBASSETSW＋JPNASSETS | ✓ API（ECBASSETSW ok、JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無合格披露） |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED（僅取得 Microsoft；Alphabet、Amazon、Meta 本次未取得） |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✗ NOT DISCLOSED（唯一結果日期矛盾且無客戶集中度內容） |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch：quarterly_state（stock-of-state）＋event_scan（30d），兩組件皆技術失敗 | ⛔ FETCH FAILED components=quarterly_state:fetch_failed,event_scan:fetch_failed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch＋既有 bullets 組合（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無變動披露） |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch：quarterly_state 無增速披露；event_scan（30d）取得取消事件 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED（1 件 SPAC 完成合併） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED（7 日內無英文披露） |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe 月報） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py VIXCLS＋vix_spx_comove | ✓ API（VIXCLS ok、vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（僅交叉檢核） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py LNFACBW027SBOG | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds＋move_index＋ofr_repo（artifact 三塊皆 ok；搜尋紀錄所稱 fallback 不採用） | ✓ API（cftc_lev_funds ok、move_index ok、ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻本益比約 28.3 | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html（CNBC） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 五年期 CDS 突破 1289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds（Coinpaper） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | RSP 等權指數年初至今報酬約 14.13% | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大成分股權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 1,474 家對下跌 1,252 家 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 22（極度恐懼） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/（原定來源 cnn.com） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 1.48 兆美元、年增約 31.4% | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt（原定來源 FINRA） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔 | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week（Benzinga） | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | 12 月升息 25 bps 機率 76.8% | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/（原定來源 CME FedWatch） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000 | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年資本支出指引自約 175 下調至約 170（Alphabet、Amazon、Meta 未取得） | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3 | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87 | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 Anthropic 65 ＋ OpenAI 約 70，合計約 135（分母僅 Microsoft 約 170，取自 ai.hyperscaler_capex） | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] 微軟 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics 完成 SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO 週漲 8% | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描：0 件符合 2+ 主題×弱基本面 | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描：0 件合格 | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe 股票選擇權賣買權比 1.05 | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭基金 10 月底規模 24.31、當月淨流入 7.27 | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 9 月總結算量 1,486,062,415 口（2026-09 月資料） | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性創高 20.93 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 交叉檢核基數約 1.48 兆美元（2026-09 月資料） | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
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

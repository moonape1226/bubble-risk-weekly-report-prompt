> [DRY RUN] this report was not committed to archive.

# 2026-08-03 AI 泡沫破裂預測報告

報告日期：2026-08-03｜ISO 週次：2026-W32｜預測窗口：2026-08-03 → 2027-02-01｜前次基準：report-2026-07-30（4天前）

## 結論

**結論：no**

三條路徑目前都離觸發點很遠。NASDAQ-100 距 52 週高點回撤 7.78%，還要再跌約 18.67% 才觸及 R1。hyperscaler 2026 capex 指引仍在上修（合計 ≈$725B），R2 沒有任何下修。R3 雖有 CoreWeave 5Y CDS ≈675bp 的信用重定價，但 HY OAS 2.84%、IG OAS 0.80% 顯示整體信用市場沒有傳導，也沒有任何付款違約或 distressed exchange 的跡象，不足以推翻 182 天內「不破裂」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

- NASDAQ-100 最新收盤 28,274.20（2026-07-31），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 7.78%。R1 門檻水位為 22,995.45，自最新收盤還要再跌約 18.67% 才觸及（`valuation.ndx_drawdown`）。
- 價格延伸：S&P 500 為 7,489.72（2026-07-31），距 200 日均線 +6.63%、距 52 週均線 +8.20%，相對 2026-07-30 +0.70%（`valuation.sp500_trend`）。估值偏高：S&P 500 trailing P/E 28.84、Shiller CAPE 40.91（2026-07-31，`valuation.sp500_pe_cape`）。融資餘額偏高：FINRA 6 月 margin debt $1.502T，YoY +51.5%，已在歷史頂部常見的 +40–50% 區間之上（`retail.margin_debt`）。
- 情緒與波動沒有亢奮：CNN Fear & Greed ≈39（Fear，2026-07-31，`retail.fear_greed`）；AAII Bear 42.1% / Bull 31.0%（2026-07-30，`retail.aaii`）；VIX 15.99（2026-07-31），7 日內 VIX −13.94%、S&P 500 +1.05%，未出現 crowded-optionality 同向上漲（`structural.vix_spx_comove`）。
- 廣度偏弱：Nasdaq-100 只有 48.0% 成分股站上 50DMA，10 日淨新高 ≈0.1%（2026-07-29，`breadth.advance_decline`）。

**判讀：** R1 距門檻還有約 18.67% 的跌幅，在 182 天窗口內需要一次接近 2022 年等級的科技股重挫。高 CAPE、創高的 margin debt YoY 與偏弱的廣度代表一旦下跌，跌幅會被放大。但目前缺乏觸發因子：信用利差緊、repo 資金壓力（SOFR−IORB）為 0bp、情緒已偏恐懼而非亢奮。可能把 R1 推過門檻的路徑是 R3 信用事件外溢，或 Q3 財報季 AI 營收不及預期引發估值重評。

### R2 資本支出收縮

- hyperscaler 2026 capex 指引在 Q2 2026 財報後仍被上修，四家（Microsoft、Alphabet、Amazon、Meta）合計 ≈$725B（+77% YoY，2026-07-28，`ai.hyperscaler_capex`）。這份彙總報導描述的方向是「續上修」。本次證據沒有逐家列出最新指引數字，所以各家方向只能依報導整體寫為上修，不寫出個別金額。
- 目前四家中下修指引的家數：0。下一輪正式指引會在 2026 Q3 財報（確切日期本次未取得），預期落在窗口內；2026 Q4 財報（含 2027 年度指引）也可能落在窗口尾端。
- 需求側沒有降溫：伺服器 DRAM 交期 30–40 週，3Q26 合約價續漲 +13–18% QoQ（2026-07-03，`ai.compute_supply_demand`），這是 capacity 吃緊的訊號，不是 order digestion。
- 回本壓力：年化 AI 終端營收 ≈$72B（Anthropic ≈$47B＋OpenAI ≈$25B，2026-06-15）對年化 capex ≈$725B（分母：top-4，Microsoft／Alphabet／Amazon／Meta，2026-07-28），比值約 10%（`ai.revenue_capex_gap`）。本次沒有可比較的前次組合值，缺口擴大或收斂無法判定。

**判讀：** R2 要在窗口內成立，需要兩家在接下來一到兩次財報中下修指引；目前四家剛上修，方向完全相反。AI 營收對 capex 缺口（revenue-to-capex gap）很大，是中長期下修的根源，但在 182 天內，真正會讓指引轉向的應該是 R1 式股價重挫或融資成本急升，而這兩者目前都不存在。

### R3 AI 信用事件

- AI 信用定價分歧（equity-vs-credit schism）已轉為信用端重定價：Oracle 5Y CDS ≈200bp、CoreWeave 5Y CDS ≈675bp，hyperscaler 債利差 ≈78bp（2026-07-30，`valuation.ai_credit_schism`）；該報導標題以「50% default odds」描述 CoreWeave CDS。CoreWeave 屬於最可能符合 R3「AI 資料中心／算力為主業」條件的借款人類型，但其負債總額與近期到期結構本次證據沒有載明。
- AI infrastructure debt financing / vendor-financing loops：Nebius 於 2026-07-17 完成首筆 $775M 擔保債務融資，以 GPU 基建作擔保（`structural.ai_infrastructure_debt`）。這顯示 neocloud 仍能進入擔保融資市場，再融資管道沒有關閉。
- 整體信用環境：HY OAS 2.84%、IG OAS 0.80%（2026-07-30，`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）0bp，SOFR99−IORB 8bp，SRF 動用（Standing Repo Facility usage）$0.0bn（`monetary.repo_stress_srf`）。
- 本次證據中沒有任何 R3 借款人出現付款違約、covenant waiver、distressed exchange 或 going-concern 文字。

**判讀：** R3 是三條路徑中最接近的一條：CoreWeave CDS ≈675bp 代表市場已為其信用風險定出高價。但 R3 需要實際的破產申請、超過寬限期的付款違約或完成 distressed exchange，CDS 走闊本身不構成解析。可能推過門檻的是：CoreWeave 類借款人在窗口內遇到大額再融資而市場關閉、主要客戶承諾縮減，或股價重挫使 equity-funded 融資中斷。目前 neocloud 擔保融資仍能完成，整體利差也緊，尚不足以判定 182 天內會發生違約。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS ≈675bp、Oracle 5Y CDS ≈200bp（2026-07-30），AI 信用端已明顯重定價，是三條路徑中最直接的壓力訊號（`valuation.ai_credit_schism`）。
- [R1] FINRA 6 月 margin debt $1.502T，YoY +51.5%（2026-07-20 發布），超過歷史頂部常見的 +40–50% 區間；一旦下跌，被迫去槓桿會放大跌幅（`retail.margin_debt`）。
- [R1] Shiller CAPE 40.91、S&P 500 trailing P/E 28.84（2026-07-31），估值脆弱度高（`valuation.sp500_pe_cape`）。
- [R2] 年化 AI 終端營收 ≈$72B 對年化 capex ≈$725B（分母：top-4），比值約 10%，capex 回本壓力是日後下修的根源（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`）。
- [R1] Nasdaq-100 只有 48.0% 成分股站上 50DMA、10 日淨新高 ≈0.1%（2026-07-29），指數接近高點但內部廣度轉弱（`breadth.advance_decline`）。
- [整體] US 槓桿 ETF 總 AUM 創高 ≈$198B（2026-07-23），且 2026-07-30 仍有新的單股 2x 槓桿 ETF 發行，結構性槓桿持續累積（`structural.leveraged_etf_aum`、`structural.us_single_stock_etf`）。
- [整體] 10Y 期限溢價（term premium）0.8376%，7 日 +5.9bp（2026-07-24），MOVE 83.02，單日 +5.93（2026-07-31），利率端波動略升（`monetary.term_premium`、`structural.treasury_basis_trade`）。

## 支持 no 的證據

- [R2] hyperscaler 2026 capex 指引在 Q2 財報後續上修，合計 ≈$725B（+77% YoY，2026-07-28），四家中下修家數為 0，與 R2 所需方向相反（`ai.hyperscaler_capex`）。
- [R1] NASDAQ-100 距 52 週高點回撤 7.78%（2026-07-31），距 R1 門檻 22,995.45 還要再跌約 18.67%（`valuation.ndx_drawdown`）。
- [R3] HY OAS 2.84%、IG OAS 0.80%（2026-07-30），整體信用市場沒有出現 AI 信用重定價的傳導（`monetary.hy_oas`、`monetary.ig_oas`）。
- [R3] Nebius 2026-07-17 完成 $775M 擔保債務融資，neocloud 融資管道仍開放，近期被迫違約的機會較低（`structural.ai_infrastructure_debt`）。
- [整體] repo 資金壓力（SOFR−IORB）0bp、SRF 動用 $0.0bn（2026-07-30／07-31），銀行對 NBFI 放款 $2.00T 持平（2026-07-22），融資市場沒有失序（`monetary.repo_stress_srf`、`structural.nbfi_bank_loans`）。
- [R2] 伺服器 DRAM 交期 30–40 週、3Q26 合約價 +13–18% QoQ（2026-07-03），算力需求仍吃緊，不支持短期 capex 收縮（`ai.compute_supply_demand`）。
- [R1] CNN Fear & Greed ≈39（Fear）、AAII Bear 42.1%、NAAIM 由 84.02 降至 79.70，情緒已部分出清，不是亢奮頂部的形態（`retail.fear_greed`、`retail.aaii`、`retail.naaim`）。
- [整體] 本週 +AI 改名／SPAC 與 microcap thematic moonshot 螢幕皆為 0 件，投機狂熱的尾部訊號沒有出現（`speculation.ai_rename_spac`、`speculation.microcap_moonshots`）。

## 與前期比較

前次結論：無前次預測（report-2026-07-30 為舊格式評分報告）

report-2026-07-30 是舊格式評分報告，不轉換為 yes/no，所以 flip_evidence 為空，本次為新格式下的第一個預測。自 2026-07-30 以來可量測的變化：

- S&P 500 由 7,437.63 升至 7,489.72（+0.70%），VIX 由 17.09 降至 15.99。
- MOVE 由 77.09 升至 83.02；OFR tri-party repo transaction volume 由 $2,414.0bn 降至 $2,293.2bn（−5.0%）。
- DGS10、DFII10、HY OAS、IG OAS 均無新觀測（Δ 0）；T10YIE +1.0bp。10Y 分解判讀：不可判（視窗不一致）。stale_series 為 DGS10、DFII10，其餘有 Δ 的序列都有新觀測。
- CoreWeave／Oracle CDS 報導（2026-07-30）與前次基準同日，是本次 R3 判讀的主要信用證據。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源的檢索完成但沒有合格的當期披露（✗ NOT DISCLOSED），以及 0 件螢幕，對結論的影響：

- `retail.social_sentiment`、`institutional.bofa_jpm_survey`、`monetary.treasury_auctions`、`structural.global_leveraged_approvals`：屬情緒或供給面的確認指標，補上也不會改變 R1–R3 的距離判斷。
- `monetary.private_credit_liquidity`：30 日內沒有 redemption-request ratio、gate proration / breach 或 net inflow→outflow flip 的披露。若有，會提高 R3／R1 的傳導風險，是可能改變結論的缺口之一。
- `ai.hyperscaler_financing_mix`：quarterly_state 可用（FactSet 2026-07-24：top-5 capex 已超過 FCF、持續依賴外部融資、Amazon 遭 S&P 降至 BBB-；五大 2026 發債 ≈$159B，+47% YoY，2026-07-22）。但 30 日 event_scan 沒有找到具名的單筆 hyperscaler 發債或融資事件，依 component_aggregation: all 判為 ✗ NOT DISCLOSED，本次不作為正文證據引用。這個 quarterly_state 顯示 hyperscaler 融資結構正從現金流轉向舉債，屬於 R2 下修的中期壓力，但不改變 182 天判斷。
- `ai.capital_cycle`：兩個組件都沒有可用證據，增速證據不足，本次不判定週期階段。
- `ai.openai_anthropic_revenue`：最近一次 run-rate 披露（2026-06-15）屬上一季，沒有當季披露，所以標為 ✗ NOT DISCLOSED。`ai.revenue_capex_gap` 依 stock-of-state 規則沿用該組件並標註其日期，不作為新證據。
- `ai.token_growth`、`ai.customer_concentration_rpo`、`ai.depreciation_life`：沒有當期披露。backlog 重複計算風險（RPO double-counting）與折舊年限變動若出現，會是 R2 的盈餘品質訊號，本次無法評估。
- `speculation.insider_form4`：唯一候選（一筆 AI 基建公司 2026-07-21 的內部人賣出）缺 Form 4 filing date 與 filing-level EDGAR URL，不符合 qualifying 條件，依規則記為 0 件，不列名。
- 非宏觀 snapshot 的時效：`breadth.rsp_spy`（2026-06-10）與 `structural.zero_dte`（2026-05-31）的資料日期偏舊，只作背景，不影響結論。

主要不確定性：

1. CoreWeave 類借款人的負債規模與近期到期結構本次沒有取得。若窗口內有大額到期且再融資失敗，R3 可能成立，並經由 R1 外溢，會把結論推向 yes。
2. 2026 Q3 hyperscaler 財報（預期落在窗口內，確切日期未取得）。若兩家同時轉為下修，R2 直接成立，會推向 yes；若續上修，會強化 no。
3. 利率端：10Y 期限溢價（term premium）走升、MOVE 上升、CME FedWatch 9 月路徑分歧（≈63%，FOMC 7/29 以 9-3 持平）。若財政或通膨壓力迫使利率急升，會壓縮高估值科技股，提高 R1 的可能性。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7489.72 | FRED API (series_id=SP500) sp500_trend | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線） | 6.63（%） | FRED API (series_id=SP500) sp500_trend | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線） | 8.20（%） | FRED API (series_id=SP500) sp500_trend | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（NASDAQ-100 最新收盤） | 28274.2 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-06-02 | 2026-08-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤） | 7.78（%） | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q1 季資料） | 45.76（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-03T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75（%） | FRED API (series_id=DFEDTARU) | 2026-08-02 | 2026-08-03T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5（%） | FRED API (series_id=DFEDTARL) | 2026-08-02 | 2026-08-03T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.84（%） | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.8（%） | FRED API (series_id=BAMLC0A0CM) | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.68（%） | FRED API (series_id=DGS10) | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.41（%） | FRED API (series_id=DFII10) | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.28（%） | FRED API (series_id=T10YIE) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 84.25（USD/bbl） | FRED API (series_id=DCOILWTICO) | 2026-07-27 | 2026-08-03T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46（%） | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-08-03T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.3（%） | FRED API (series_id=T5YIFR) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8376（%） | FRED API (series_id=THREEFYTP10) | 2026-07-24 | 2026-08-03T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 日） | 5.9（bp） | FRED API (series_id=THREEFYTP10) | 2026-07-24 | 2026-08-03T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.65（%） | FRED API (series_id=SOFR) | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.73（%） | FRED API (series_id=SOFR99) | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65（%） | FRED API (series_id=IORB) | 2026-08-03 | 2026-08-03T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用） | 0.0（十億美元） | FRED API (series_id=RPONTTLD) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,738,190（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-29 | 2026-08-03T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,944,015（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-24 | 2026-08-03T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,395,509（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-08-03T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.99 | FRED API (series_id=VIXCLS) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of；base_date 2026-07-24，window_days 7，comove false） | 15.99 | FRED API derived block vix_spx_comove | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | −13.94（%） | FRED API derived block vix_spx_comove | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | 1.05（%） | FRED API derived block vix_spx_comove | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2004.9941（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-22 | 2026-08-03T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位） | −7,481,041（口） | CFTC TFF futures-only cftc_lev_funds | 2026-07-28 | 2026-08-03T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | −52,919（口） | CFTC TFF futures-only cftc_lev_funds | 2026-07-28 | 2026-08-03T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 83.02 | Yahoo Finance chart API ^MOVE move_index | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index delta_abs | 5.93 | Yahoo Finance chart API ^MOVE move_index | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2293.2（十億美元） | OFR STFM REPO-TRIV1_TV_TOT-P ofr_repo | 2026-07-31 | 2026-08-03T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | Advisor Perspectives，WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報摘要 [primary: SEARCH]（90d＋同季） | ✓ SEARCH-VERIFIED（2026-07-13，Q3；舊 TP／EPS Δ 未披露） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500 → sp500_trend） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100 → ndx_drawdown） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導 [primary: SEARCH]（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst，WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-06-10，偏舊） |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | Pensions & Investments，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | streetstats NQ100 breadth proxy，WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA／Advisor Perspectives，WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag，WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／YCharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查，WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（DFEDTARU ok、DFEDTARL ok） | ✓ API |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok；repo_stress ok） | ✓ API |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | Reuters／Bloomberg recap [primary: SEARCH]（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Bloomberg，WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC／interval fund 披露 [primary: SEARCH]（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報彙總，WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露，WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／具名報導，WebSearch（最近披露 2026-06-15 屬上一季） | ✗ NOT DISCLOSED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話會議 [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：FactSet／cryptobriefing；event_scan：30d 具名發債／融資事件 [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露（分子 Anthropic＋OpenAI；分母 top-4）[primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q／法說 [primary: SEARCH]（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速＋進出場事件，WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: "AI rename" / SPAC | Reuters／Benzinga／Boardroom Alpha，WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | valueaddvc／Renaissance，WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／Benzinga／StockTwits／Yahoo movers [primary: SEARCH]（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導，WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 [primary: SEC EDGAR]（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe／YCharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com／cryptobriefing [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | Leverage Shares／GlobeNewswire，WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA，WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe 投資人簡報，WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-05-31，偏舊） |
| structural.options_volume | 結構｜Options total volume: OCC monthly volume report | theocc.com，WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Saxo options brief／Cboe，WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS ok、vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 retail.margin_debt，WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | 公司新聞稿 [primary: SEARCH]（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok；aggregation any） | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 28.84（原定來源 multpl.com） | S&P 500 trailing P/E August 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 40.91（原定來源 multpl.com） | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 對其餘 493 檔估值溢價 ≈10% | Magnificent 7 valuation premium compressed 2026 | https://www.advisorperspectives.com/articles/2026/07/09/magnificent-sevens-weakness-become-problem-wall-street （Advisor Perspectives） | 2026-07-09 | 2026-08-03T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標價 $288；目標 PE 未擴張，EPS-driven（舊 TP、EPS Δ 未披露） | Morgan Stanley NVDA target 288 July 2026 EPS | https://www.gurufocus.com/news/8955458/morgan-stanley-upgrades-nvidia-nvda-with-a-288-target-price （GuruFocus） | 2026-07-13 | 2026-08-03T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5Y CDS ≈200bp、CoreWeave 5Y CDS ≈675bp、hyperscaler 債利差 ≈78bp | Oracle CoreWeave CDS AI credit repricing hyperscaler spread August 2026 | https://www.techtimes.com/articles/322222/20260730/coreweave-cds-hits-50-default-odds-bond-market-calls-time-gpu-debt-spiral.htm （Tech Times） | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD +9.67% vs SPY YTD +8.38% | RSP vs SPY equal weight YTD 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St.） | 2026-06-10 | 2026-08-03T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 ≈40% | S&P 500 top 10 concentration percent 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/ （Pensions & Investments） | 2026-07-02 | 2026-08-03T09:30:00+08:00 |
| breadth.advance_decline | Nasdaq-100 48.0% >50DMA、63.7% >200DMA、10 日淨新高 ≈0.1% | Nasdaq 100 breadth percent above 50 day 200 day July 2026 | https://streetstats.finance/markets/breadth-momentum/NQ100 （streetstats） | 2026-07-29 | 2026-08-03T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed ≈39（Fear） | CNN Fear and Greed Index July 31 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives／FINRA） | 2026-07-20 | 2026-08-03T09:30:00+08:00 |
| retail.aaii | AAII Bear 42.1%／Neutral 26.9%／Bull 31.0% | AAII investor sentiment survey July 30 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| retail.naaim | NAAIM 前值 84.02 → 最新 79.70 | NAAIM exposure index July 2026 | https://ycharts.com/indicators/naaim_number （YCharts） | 2026-07-29 | 2026-08-03T09:30:00+08:00 |
| monetary.fedwatch | FOMC 7/29 持平（9-3）；CME FedWatch 9 月路徑分歧 ≈63% | FOMC July 29 2026 hold FedWatch September cut probability | https://growbeansprout.com/tools/fedwatch （FedWatch 摘要） | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.pboc | 人行 7/24 MLF 淨投放 ≈¥100B（5 個月最大） | PBoC MLF net injection liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-24/pboc-adds-most-liquidity-to-economy-in-five-months-to-aid-growth （Bloomberg） | 2026-07-24 | 2026-08-03T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 續上修，合計 ≈$725B（+77% YoY），Q2 2026 財報 | hyperscaler capex 2026 725B raised Meta Amazon Alphabet Microsoft | https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion （Tom's Hardware） | 2026-07-28 | 2026-08-03T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 交期 30–40 週、3Q26 合約價 +13–18% QoQ | DRAM contract price 3Q26 TrendForce lead time | https://www.trendforce.com/presscenter/news/20260703-13134.html （TrendForce） | 2026-07-03 | 2026-08-03T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超過 FCF、續靠外部融資、Amazon 遭 S&P 降至 BBB- | hyperscaler capex FCF debt Amazon downgrade BBB- 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow （FactSet） | 2026-07-24 | 2026-08-03T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 五大 2026 發債 ≈$159B（+47% YoY） | hyperscaler bond issuance 159B 2026 AI credit | https://cryptobriefing.com/tech-giants-record-159b-bonds-ai/ （Crypto Briefing） | 2026-07-22 | 2026-08-03T09:30:00+08:00 |
| ai.revenue_capex_gap | 分子：AI 終端年化營收 ≈$72B（Anthropic ≈$47B＋OpenAI ≈$25B） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-06-15 | 2026-08-03T09:30:00+08:00 |
| ai.revenue_capex_gap | 分母：年化 capex ≈$725B（top-4，取自 ai.hyperscaler_capex） | hyperscaler capex 2026 725B raised Meta Amazon Alphabet Microsoft | https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion （Tom's Hardware） | 2026-07-28 | 2026-08-03T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收 IPO 螢幕：合格件數為零 | AI rename SPAC no revenue IPO July 27 August 3 2026 | Reuters／Benzinga／Boardroom Alpha SPAC 螢幕 | — | 2026-08-03T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD 86 檔、募資 ≈$251B；JMKE 首日收平、aftermarket 轉弱 | US IPO market 2026 Jersey Mike's Cerebras aftermarket | https://valueaddvc.com/blog/ipo-market-2026-which-companies-are-going-public-and-what-the-window-looks-like （valueaddvc） | 2026-08-01 | 2026-08-03T09:30:00+08:00 |
| speculation.microcap_moonshots | 市值 < $1B、單日 ≥100% 且疊加多主題的 moonshot：合格件數為零 | microcap 100% single day quantum AI fusion moonshot July August 2026 | Finviz／Benzinga／StockTwits／Yahoo movers 螢幕 | — | 2026-08-03T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 ≈$1T IPO、Anthropic 續進 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground （Benzinga） | 2026-07-28 | 2026-08-03T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內 AI 龍頭內部人 Form 4 cluster：合格件數為零（唯一候選缺 filing date 與 filing-level URL） | CoreWeave insider Form 4 July 2026 SEC | SEC EDGAR company Form 4 listing；Form 4 新聞摘要 | — | 2026-08-03T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.63（daily） | Cboe equity put call ratio July 31 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio （YCharts） | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高 ≈$198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing） | 2026-07-23 | 2026-08-03T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x 單股槓桿 ETF＋ELOL（TSLA＋SpaceX）發行 | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | https://www.manilatimes.net/2026/07/30/tmt-newswire/globenewswire/two-industry-leaders-one-ticker-leverage-shares-by-themes-launches-elol/2395125 （GlobeNewswire via Manila Times） | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量 ≈65%（Cboe Q2 2026 簡報） | 0DTE SPX options share volume Cboe Q2 2026 | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641 （Investing.com） | 2026-05-31 | 2026-08-03T09:30:00+08:00 |
| structural.options_volume | OCC 6 月總量 16.0 億口（2026-06 月資料） | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-08-03T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW ≈139.9、VIX 17.09（term structure contango） | VIX SKEW term structure July 31 2026 | https://www.home.saxo/content/articles/options/index-up-average-stock-down---options-brief---31-july-2026-31072026 （Saxo） | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt（2026-06 月資料）$1.502T、+51.5% YoY（交叉引用 retail.margin_debt） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-08-03T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Nebius 2026-07-17 完成首筆 $775M 擔保債務融資（GPU 基建擔保） | AI data center debt financing Nebius secured facility July 2026 | https://nebius.com/newsroom/nebius-raises-775-million-in-first-secured-debt-financing-to-accelerate-global-buildout （Nebius） | 2026-07-17 | 2026-08-03T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-03",
  "iso_week": "2026-W32",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-01",
  "prior_date": "2026-07-30",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 7.78,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

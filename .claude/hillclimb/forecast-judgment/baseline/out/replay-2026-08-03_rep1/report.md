> [DRY RUN] this report was not committed to archive.

# 2026-08-03 AI 泡沫破裂預測報告

報告日期：2026-08-03｜ISO 週次：2026-W32｜預測窗口：2026-08-03 → 2027-02-01｜前次基準：report-2026-07-30（4天前）

## 結論

**結論：no**

三條路徑目前都離觸發有明顯距離：NASDAQ-100 距 52 週高點回撤 7.78%，仍需再跌約 18.67% 才觸及 R1；四家 hyperscaler 2026 capex 合計仍在上修（≈$725B，+77% YoY），R2 尚無一家下修。AI 信用定價分歧（equity-vs-credit schism）已在 CoreWeave CDS ≈675bp 浮現，是最值得追蹤的 R3 → R1 傳導鏈，但 HY OAS 2.84% 與 repo 資金壓力（SOFR−IORB）0bp 顯示尚無系統性信用／融資壓力，不足以推翻低基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 28274.2（2026-07-31），252 個交易日最高收盤 30660.6（2026-06-02），距 52 週高點回撤 7.78%；R1 門檻水位 22995.45，自最新收盤需再下跌約 18.67% 才會觸及（`valuation.ndx_drawdown`）。7 月下旬曾在 2026-07-29 收 27192.31，之後兩日反彈。

估值脆弱度高：S&P 500 trailing P/E 28.84、Shiller CAPE 40.91（multpl，2026-07-31，`valuation.sp500_pe_cape`）；S&P 500 7489.72 高於 200 日均線 7024.11 達 6.63%、高於 52 週均線 8.2%（`valuation.sp500_trend`）。槓桿面：FINRA 6 月 margin debt $1.502T、YoY +51.5%，落在歷史頂部常見的 +40–50% 區間之上（`retail.margin_debt`）；US 槓桿 ETF AUM ≈$198B 創高（`structural.leveraged_etf_aum`）。但情緒並不亢奮：CNN Fear & Greed ≈39（Fear，`retail.fear_greed`）、AAII Bear 42.1%（`retail.aaii`）、Cboe equity put/call 0.63（`speculation.equity_put_call`）。

政策緩衝有限：Fed funds 目標區間 3.50%–3.75%（`monetary.fed_funds`），FOMC 2026-07-29 以 9-3 鷹派持平、FedWatch 9 月路徑分歧（`monetary.fedwatch`）；CPI YoY 3.46%（2026-06，`monetary.cpi_yoy`）、5y5y 2.3%（`monetary.t5yifr`），通膨仍高於目標，Fed 對 AI 主導回檔的緩衝空間受限。債券波動上升：MOVE 由 77.09（2026-07-30）升至 83.02（2026-07-31）（`structural.treasury_basis_trade`）；VIX 15.99（2026-07-31），近 7 日 VIX −13.94%、S&P 500 +1.05%，未出現 crowded-optionality 同漲（`structural.vix_spx_comove`）。

**判讀：** R1 尚遠，需要再 18.67% 的下跌；在窗口內推過門檻需要一個傳導型催化劑，例如 R3 方向的 AI 信用重定價擴散到 hyperscaler，或 Q3／Q4 財報季的 capex 指引轉向（R2），在高估值與高 margin debt 下放大跌幅。

### R2 資本支出收縮

最新季報（2026-07 下旬財報季）後，Microsoft、Alphabet、Amazon、Meta 2026 capex 指引合計 ≈$725B、YoY +77%，報導描述為四家「續上修」（Tom's Hardware，2026-07-28，`ai.hyperscaler_capex`）。本次取得的來源只提供合計數，未逐家列出指引金額；依該報導，四家方向皆為上修，無一家下修，目前 0／4 下修。下一個逐家檢驗點是 Q3 財報季（按季報節奏約在 10 月下旬）與 Q4 財報季（約在 2027-01 下旬），兩者都落在窗口內；確切日期本次未取得。

需求側證據仍偏緊：伺服器 DRAM 交期 30–40 週、3Q26 合約價 QoQ +13–18%（TrendForce，2026-07-03，`ai.compute_supply_demand`），屬價格上漲與交期拉長並存，不是供過於求的訊號。但 hyperscaler 融資結構（capex vs FCF / 發債）顯示 top-5 capex 已超越 FCF、續靠外部融資，S&P 將 Amazon 降至 BBB-（FactSet，2026-07-24），五大 2026 發債 ≈$159B、+47% YoY（2026-07-22）（`ai.hyperscaler_financing_mix`）；AI 營收對 capex 缺口（revenue-to-capex gap）約為年化 AI 終端營收 ≈$72B（Anthropic ≈$47B＋OpenAI ≈$25B，2026-06-15 披露）vs 年化 capex ≈$725B（分母：MSFT／GOOGL／AMZN／META 四家；Oracle 本次無 capex 披露，未納入）（`ai.revenue_capex_gap`），本次無前次組合值可比，缺口方向不判定。

**判讀：** R2 距離最遠；剛結束的財報季是集體上修，要在窗口內出現兩家下修，需要在 Q3 或 Q4 財報季發生急轉，較可能的觸發是信用成本上升（評等下調、發債利差走闊）迫使融資受限，或 R1 大幅回撤後的防禦性下修。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）已轉為信貸端先重定價：CoreWeave 5Y CDS ≈675bp、Oracle 5Y CDS ≈200bp、hyperscaler 債利差 ≈78bp（Tech Times，2026-07-30，`valuation.ai_credit_schism`）。CoreWeave 是最接近 R3 規模門檻的 AI 算力主業借款人，但本次證據未提供其總負債、近期到期或寬限期資訊；Oracle 主業非 AI 資料中心，不屬 R3 借款人類別。AI infrastructure debt financing / vendor-financing loops 方面，Nebius 於 2026-07-17 完成首筆 $775M 擔保債務融資，以 GPU 基建為擔保（`structural.ai_infrastructure_debt`），顯示 neocloud 仍能進入擔保債市場。全市場信用仍緊：HY OAS 2.84%、IG OAS 0.80%（2026-07-30，`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）0bp、SOFR99−IORB 8bp、SRF 動用（Standing Repo Facility usage）0（2026-07-30／2026-07-31，`monetary.repo_stress_srf`）；銀行對 NBFI 放款 $2.00T（2026-07-22，`structural.nbfi_bank_loans`）。本次未取得任何違約、寬限期、covenant waiver 或 distressed exchange 證據。

**判讀：** R3 是三條中最接近的路徑：CoreWeave CDS ≈675bp 已是市場明確定價違約風險的水位，但從 CDS 走闊到實際破產申請／付款違約／distressed exchange 通常需要再融資失敗或流動性耗盡；若窗口內出現 CoreWeave 等大型 neocloud 的再融資受阻、評等降至 distressed 或 exchange offer，R3 會直接觸發並可能經 AI 股權重定價帶動 R1。

## 支持 yes 的證據

- [R3] AI 信用定價分歧（equity-vs-credit schism）轉為信貸端先走闊：CoreWeave 5Y CDS ≈675bp、Oracle 5Y CDS ≈200bp（2026-07-30），是 AI 算力借款人違約風險被明確定價的後期訊號 `valuation.ai_credit_schism`
- [R3] hyperscaler 融資結構（capex vs FCF / 發債）由現金流轉向舉債：top-5 capex 已超越 FCF、Amazon 遭 S&P 降至 BBB-（2026-07-24），五大 2026 發債 ≈$159B、+47% YoY（2026-07-22） `ai.hyperscaler_financing_mix`
- [整體] AI 營收對 capex 缺口（revenue-to-capex gap）約 10 倍：年化 AI 終端營收 ≈$72B vs 年化 capex ≈$725B（分母：四家 hyperscaler） `ai.revenue_capex_gap`
- [R1] 槓桿極端：FINRA 6 月 margin debt $1.502T、YoY +51.5%（2026-07-20 發布），US 槓桿 ETF AUM ≈$198B 創高（2026-07-23） `retail.margin_debt` `structural.leveraged_etf_aum`
- [R1] 估值與價格延伸偏高：Shiller CAPE 40.91、trailing P/E 28.84（2026-07-31），S&P 500 高於 200 日均線 6.63%（2026-07-31） `valuation.sp500_pe_cape` `valuation.sp500_trend`
- [R1] 政策緩衝受限：FOMC 2026-07-29 以 9-3 鷹派持平，CPI YoY 3.46%（2026-06），Fed funds 3.50%–3.75% `monetary.fedwatch` `monetary.cpi_yoy` `monetary.fed_funds`
- [R1] 廣度轉弱：Nasdaq-100 僅 48.0% 成分股高於 50DMA、10 日淨新高 ≈0.1%（2026-07-29）；MOVE 由 77.09 升至 83.02（2026-07-31） `breadth.advance_decline` `structural.treasury_basis_trade`
- [整體] 單股槓桿產品仍在擴張：Leverage Shares 發行 6 檔 2x 單股槓桿 ETF 與 ELOL（2026-07-30） `structural.us_single_stock_etf`

## 支持 no 的證據

- [R2] 四家 hyperscaler 2026 capex 合計 ≈$725B、YoY +77%，最新財報季續上修，0／4 下修（2026-07-28） `ai.hyperscaler_capex`
- [R1] NASDAQ-100 距 52 週高點回撤 7.78%（2026-07-31），距 R1 門檻 22995.45 仍需再跌約 18.67% `valuation.ndx_drawdown`
- [R3] 全市場信用與融資未見壓力：HY OAS 2.84%、IG OAS 0.80%（2026-07-30），SOFR−IORB 0bp、SRF 動用 0（2026-07-31） `monetary.hy_oas` `monetary.ig_oas` `monetary.repo_stress_srf`
- [R2] 算力需求仍緊：伺服器 DRAM 交期 30–40 週、3Q26 合約價 QoQ +13–18%（2026-07-03） `ai.compute_supply_demand`
- [R3] AI 基建借款人仍可進入擔保債市場：Nebius 2026-07-17 完成 $775M 擔保債務融資 `structural.ai_infrastructure_debt`
- [整體] 情緒偏恐懼而非亢奮：CNN Fear & Greed ≈39（2026-07-31）、AAII Bear 42.1%（2026-07-30）、equity put/call 0.63（2026-07-31）、NAAIM 由 84.02 降至 79.70（2026-07-29） `retail.fear_greed` `retail.aaii` `speculation.equity_put_call` `retail.naaim`
- [整體] 投機篩選無合格事件：+AI 改名／SPAC 0 件、microcap thematic moonshot 0 件（2026-08-03），IPO aftermarket 轉弱（2026-08-01） `speculation.ai_rename_spac` `speculation.microcap_moonshots` `speculation.ipo_heat`
- [整體] 賣方目標價上修以 EPS 驅動而非估值擴張：Morgan Stanley NVDA 目標價 $288，目標 PE 未擴張（2026-07-13） `valuation.analyst_tp_decomposition`

## 與前期比較

前次結論：無前次預測（report-2026-07-30 為舊格式評分報告）

本次為新格式首次預測，`flip_evidence` 為空。自 2026-07-30 以來的主要變化：

- S&P 500 由 7437.63 升至 7489.72（+0.7%），NASDAQ-100 由 28106.35 升至 28274.2，R1 距離小幅拉開。
- MOVE 由 77.09 升至 83.02（+5.93），債券波動上升；VIX 由 17.09 降至 15.99。
- 10Y 分解：ΔDGS10 0bp、ΔDFII10 0bp、ΔT10YIE +1bp，判讀：不可判（視窗不一致）；stale_series 為 DGS10、DFII10（最新觀測仍為 2026-07-30），T10YIE 已更新至 2026-07-31。
- OFR tri-party repo transaction volume 由 2414.0bn 降至 2293.2bn（−5.0%），RPONTTLD 由 0.008bn 降至 0.0。
- 10Y 期限溢價（term premium）0.8376%（2026-07-24，Kim-Wright），序列自身 trailing 7 日 +5.9bp。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源完成檢索但無合格當期披露（✗ NOT DISCLOSED），均為 best-effort：`retail.social_sentiment`、`institutional.bofa_jpm_survey`、`monetary.treasury_auctions`、`monetary.private_credit_liquidity`、`ai.token_growth`、`ai.openai_anthropic_revenue`（最近披露為 2026-06-15，屬上一季，不符 current-quarter 要求；僅在 AI 營收對 capex 缺口中以 carry-forward 組件使用）、`ai.customer_concentration_rpo`、`ai.depreciation_life`、`ai.capital_cycle`、`structural.global_leveraged_approvals`。其中私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）與 backlog 重複計算風險（RPO double-counting）的缺漏與 R3 最相關：若存在未被捕捉的 gate proration / breach 或同一 counterparty 承諾被多家重複計入，可能提高 R3 的近端風險，但目前沒有證據顯示其已發生，不改變答案。資本週期階段（capital cycle stage）兩個組件皆無披露，本次不判定週期階段。insider Form 4 篩選有 1 筆候選缺 Form 4 filing date 與 filing-level EDGAR URL，依規則記為 0 件。

時效性提醒：`breadth.rsp_spy`（2026-06-10）、`breadth.top10_concentration`（2026-07-02）、`structural.zero_dte`（2026-05-31）、`valuation.mag7_multiples`（2026-07-09）的 snapshot 資料日期偏舊，本次只作背景、未用於判斷。

最大不確定性：

1. CoreWeave 等大型 neocloud 的負債規模與再融資時程（本次未取得）：若窗口內出現再融資失敗或 distressed exchange，R3 直接觸發，並推向 yes。
2. Q3（約 10 月下旬）與 Q4（約 2027-01 下旬）hyperscaler 財報：若兩家以上因融資成本或 ROI 壓力下修 capex，R2 觸發推向 yes；繼續上修則強化 no。
3. 鷹派 Fed 與 3.46% CPI：若通膨迫使 Fed 進一步收緊、10Y 與期限溢價續升，高估值下的估值壓縮可能把 R1 推近門檻；若 9 月轉向降息，推向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest | 7489.72 | FRED API (series_id=SP500) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 6.63 | FRED API (series_id=SP500) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28274.2 | FRED API (series_id=NASDAQ100) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-03T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 7.78 | FRED API (series_id=NASDAQ100) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-03T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-02 | 2026-08-03T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-02 | 2026-08-03T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.84 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.8 | FRED API (series_id=BAMLC0A0CM) | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.68 | FRED API (series_id=DGS10) | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.41 | FRED API (series_id=DFII10) | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.28 | FRED API (series_id=T10YIE) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 84.25 | FRED API (series_id=DCOILWTICO) | 2026-07-27 | 2026-08-03T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-08-03T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.3 | FRED API (series_id=T5YIFR) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest | 0.8376 | FRED API (series_id=THREEFYTP10) | 2026-07-24 | 2026-08-03T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.65 | FRED API (series_id=SOFR) | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.73 | FRED API (series_id=SOFR99) | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-08-03 | 2026-08-03T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest | 0.0 | FRED API (series_id=RPONTTLD) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6738190.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-29 | 2026-08-03T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5944015.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-24 | 2026-08-03T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6395509.0（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-08-03T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.99 | FRED API (series_id=VIXCLS) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 15.99 | FRED API (series_id=VIXCLS, SP500) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | -13.94 | FRED API (series_id=VIXCLS, SP500) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2004.9941（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-22 | 2026-08-03T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7481041 | CFTC TFF futures-only | 2026-07-28 | 2026-08-03T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 83.02 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2293.2 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-07-31 | 2026-08-03T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation｜S&P 500 P/E and Shiller CAPE | multpl.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation｜Mag 7 weighted P/E and AI leader P/S | Advisor Perspectives WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation｜Analyst TP upgrade decomposition | 賣方研報摘要 WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | Valuation｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth｜Top-10 concentration in S&P 500 | Pensions & Investments WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth｜Advance/decline ratio, new high/low ratio | streetstats NQ100 breadth WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment｜CNN Fear & Greed Index | cnn.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment｜Margin Debt: FINRA monthly data | FINRA／Advisor Perspectives WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment｜Retail survey: AAII Investor Sentiment | aaii.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment｜Social sentiment proxies | WSB／cashtag WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment｜NAAIM Exposure Index | YCharts WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | Institutional Sentiment｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（FRED DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit｜High Yield OAS | scripts/fetch_macro.py（FRED BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit｜Investment Grade OAS | scripts/fetch_macro.py（FRED BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit｜10Y Treasury yield | scripts/fetch_macro.py（FRED DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit｜10Y breakeven inflation rate | scripts/fetch_macro.py（FRED T10YIE） | ✓ API |
| monetary.wti | Monetary & Credit｜WTI crude oil price | scripts/fetch_macro.py（FRED DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（FRED CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit｜5y5y forward inflation expectation | scripts/fetch_macro.py（FRED T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（FRED THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（FRED SOFR、SOFR99、IORB、RPONTTLD） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit｜美債標售需求（auction tail / bid-to-cover） | Reuters／Bloomberg auction recap WebSearch（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary & Credit｜Fed funds rate path expectations | CME FedWatch 摘要 WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（FRED WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit｜Global central bank liquidity cross-check — ECB / BOJ balance sheets | scripts/fetch_macro.py（FRED ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit｜PBoC aggregate financing / liquidity operations | Bloomberg WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit｜Private-credit / non-bank fund liquidity stress | BDC／interval fund 披露 WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals｜Hyperscaler capex guidance | 季報／財經媒體 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals｜OpenAI / Anthropic annualized revenue | Epoch／具名報導 WebSearch（current quarter） | ✗ NOT DISCLOSED |
| ai.customer_concentration_rpo | AI Fundamentals｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals｜AI compute supply/demand and overcapacity risk | TrendForce WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals｜Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch：quarterly_state＝FactSet top-5 capex vs FCF；event_scan＝30d 發債掃描 | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI Fundamentals｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 WebSearch（stock-of-state carry-forward） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals｜GPU / 伺服器折舊年限變動 | 10-K／10-Q／earnings call WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals｜資本週期階段（capital cycle stage） | WebSearch：quarterly_state＝供需增速；event_scan＝30d 進出場事件 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior｜Search for past 7 days: AI rename / SPAC / no-revenue IPO | Reuters／Benzinga／Boardroom Alpha WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior｜IPO market heat | valueaddvc／Renaissance WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior｜Microcap thematic moonshots | Finviz／Benzinga／StockTwits／Yahoo movers WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior｜Upcoming AI IPOs | S-1／具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 篩選（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior｜Cboe equity-only put/call ratio | YCharts WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage｜US leveraged ETF AUM | etf.com／財經媒體 WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage｜US single-stock leveraged ETF approvals | ETF launch feed／GlobeNewswire WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | Structural Leverage｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA／ETFGI WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage｜0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage｜Options total volume: OCC monthly volume report | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage｜Cross-asset derivatives / correlation checks | Saxo options brief WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（FRED VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage｜Cross-reference only: FINRA margin debt | Advisor Perspectives WebSearch（交叉引用） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage｜AI infrastructure debt financing / vendor-financing loops | 公司新聞稿 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）；WebSearch 無 14d 內披露 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 28.84 | S&P 500 trailing P/E August 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio（multpl；原定來源 multpl／gurufocus） | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 40.91 | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe（multpl） | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 對其餘 493 檔溢價 ≈10% | Magnificent 7 valuation premium compressed 2026 | https://www.advisorperspectives.com/articles/2026/07/09/magnificent-sevens-weakness-become-problem-wall-street（Advisor Perspectives） | 2026-07-09 | 2026-08-03T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標價 $288；目標 PE 未擴張，EPS 驅動（舊 TP、EPS Δ 未披露） | Morgan Stanley NVDA target 288 July 2026 EPS | https://www.gurufocus.com/news/8955458/morgan-stanley-upgrades-nvidia-nvda-with-a-288-target-price（GuruFocus） | 2026-07-13 | 2026-08-03T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5Y CDS ≈200bp、CoreWeave 5Y CDS ≈675bp、hyperscaler 債利差 ≈78bp | Oracle CoreWeave CDS AI credit repricing hyperscaler spread August 2026 | https://www.techtimes.com/articles/322222/20260730/coreweave-cds-hits-50-default-odds-bond-market-calls-time-gpu-debt-spiral.htm（Tech Times） | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| breadth.rsp_spy | RSP 等權 YTD +9.67% vs SPY +8.38% | RSP vs SPY equal weight YTD 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（247wallst） | 2026-06-10 | 2026-08-03T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 ≈40% | S&P 500 top 10 concentration percent 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/（Pensions & Investments） | 2026-07-02 | 2026-08-03T09:30:00+08:00 |
| breadth.advance_decline | Nasdaq-100：48.0% >50DMA、63.7% >200DMA、10 日淨新高 ≈0.1% | Nasdaq 100 breadth percent above 50 day 200 day July 2026 | https://streetstats.finance/markets/breadth-momentum/NQ100（streetstats） | 2026-07-29 | 2026-08-03T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed ≈39（Fear） | CNN Fear and Greed Index July 31 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives；原定來源 FINRA） | 2026-07-20 | 2026-08-03T09:30:00+08:00 |
| retail.aaii | AAII Bear 42.1%／Neutral 26.9%／Bull 31.0% | AAII investor sentiment survey July 30 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| retail.naaim | NAAIM 前值 84.02 → 最新 79.70 | NAAIM exposure index July 2026 | https://ycharts.com/indicators/naaim_number（YCharts；原定來源 naaim.org） | 2026-07-29 | 2026-08-03T09:30:00+08:00 |
| monetary.fedwatch | FOMC 7/29 鷹派持平（9-3）；FedWatch 9 月路徑分歧 ≈63% | FOMC July 29 2026 hold FedWatch September cut probability | https://growbeansprout.com/tools/fedwatch（原定來源 CME FedWatch） | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| monetary.pboc | 人行 7/24 MLF 淨投放 ≈¥100B（5 個月最大） | PBoC MLF net injection liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-24/pboc-adds-most-liquidity-to-economy-in-five-months-to-aid-growth（Bloomberg） | 2026-07-24 | 2026-08-03T09:30:00+08:00 |
| ai.hyperscaler_capex | 四家 hyperscaler 2026 capex 續上修，合計 ≈$725B（+77% YoY） | hyperscaler capex 2026 725B raised Meta Amazon Alphabet Microsoft | https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion（Tom's Hardware；原定來源 季報） | 2026-07-28 | 2026-08-03T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 交期 30–40 週、3Q26 合約價 QoQ +13–18% | DRAM contract price 3Q26 TrendForce lead time | https://www.trendforce.com/presscenter/news/20260703-13134.html（TrendForce） | 2026-07-03 | 2026-08-03T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超越 FCF、續靠外部融資；S&P 將 Amazon 降至 BBB- | hyperscaler capex FCF debt Amazon downgrade BBB- 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow（FactSet） | 2026-07-24 | 2026-08-03T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 五大 hyperscaler 2026 發債 ≈$159B（+47% YoY），公司債 | hyperscaler bond issuance 159B 2026 AI credit | https://cryptobriefing.com/tech-giants-record-159b-bonds-ai/（Crypto Briefing） | 2026-07-22 | 2026-08-03T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 ≈$72B（Anthropic ≈$47B＋OpenAI ≈$25B）vs 年化 capex ≈$725B（分母：MSFT／GOOGL／AMZN／META） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI；分母取自 ai.hyperscaler_capex 2026-07-28） | 2026-06-15 | 2026-08-03T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收 IPO 合格 0 件 | AI rename SPAC no revenue IPO July 27 August 3 2026 | 檢查來源：Reuters、Benzinga、Boardroom Alpha SPAC 螢幕 | — | 2026-08-03T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD 86 檔 IPO、募資 ≈$251B；JMKE 首日收平、aftermarket 轉弱 | US IPO market 2026 Jersey Mike's Cerebras aftermarket | https://valueaddvc.com/blog/ipo-market-2026-which-companies-are-going-public-and-what-the-window-looks-like（valueaddvc） | 2026-08-01 | 2026-08-03T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot 合格 0 件 | microcap 100% single day quantum AI fusion moonshot July August 2026 | 檢查來源：Finviz、Benzinga、StockTwits、Yahoo Finance movers | — | 2026-08-03T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 ≈$1T IPO、Anthropic 續進 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground（Benzinga） | 2026-07-28 | 2026-08-03T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內具 filing-level 細節的合格 Form 4 cluster 0 件（1 筆候選缺 filing date 與 filing URL，未計入） | CoreWeave insider Form 4 July 2026 SEC | 檢查來源：SEC EDGAR Form 4 公司申報清單 | — | 2026-08-03T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.63（未標明單日或 5 日均值） | Cboe equity put call ratio July 31 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio（YCharts；原定來源 Cboe） | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高 ≈$198B（個別 NVDL／TSLL／CONL／TQQQ／SOXL／SQQQ 未拆分） | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing；原定來源 etf.com／ETFGI） | 2026-07-23 | 2026-08-03T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x 單股槓桿 ETF＋ELOL（TSLA＋SpaceX）發行 | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | https://www.manilatimes.net/2026/07/30/tmt-newswire/globenewswire/two-industry-leaders-one-ticker-leverage-shares-by-themes-launches-elol/2395125（GlobeNewswire via Manila Times） | 2026-07-30 | 2026-08-03T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量 ≈65%（Cboe Q2 2026 slides） | 0DTE SPX options share volume Cboe Q2 2026 | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641（Investing.com；原定來源 Cboe） | 2026-05-31 | 2026-08-03T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月總量 16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-08-03T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW ≈139.9、VIX 17.09（term structure contango；與 FRED VIXCLS 2026-07-30 收盤一致） | VIX SKEW term structure July 31 2026 | https://www.home.saxo/content/articles/options/index-up-average-stock-down---options-brief---31-july-2026-31072026（Saxo） | 2026-07-31 | 2026-08-03T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-06 月資料）$1.502T、+51.5% YoY（交叉引用 retail.margin_debt） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives） | 2026-07-20 | 2026-08-03T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Nebius 完成首筆 $775M 擔保債務融資（GPU 基建擔保，用於全球擴建） | AI data center debt financing Nebius secured facility July 2026 | https://nebius.com/newsroom/nebius-raises-775-million-in-first-secured-debt-financing-to-accelerate-global-buildout（Nebius） | 2026-07-17 | 2026-08-03T09:30:00+08:00 |

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

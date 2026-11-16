> [DRY RUN] this report was not committed to archive.

# 2026-07-30 AI 泡沫破裂預測報告

報告日期：2026-07-30｜ISO 週次：2026-W31｜預測窗口：2026-07-30 → 2027-01-28｜前次基準：report-2026-07-27（3天前）

## 結論

**結論：no**

三條路徑都還沒走到能在 182 天內完成的程度。R1 方面，NASDAQ-100 雖已距 52 週高點回撤 11.31%，但仍需再跌 15.43% 才觸及門檻（`valuation.ndx_drawdown`）。R2 方面，四大 hyperscaler 的 2026 capex 指引仍在上修（`ai.hyperscaler_capex`）。R3 方面，CoreWeave 5Y CDS ≈855bp 顯示 AI 信用正在重定價，但目前沒有任何違約、寬限期付款違約或 distressed exchange 跡象，而且 HY OAS 僅 2.84%，整體信用並未傳導（`valuation.ai_credit_schism`、`monetary.hy_oas`）。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 於 2026-07-29 收在 27192.31。252 個交易日內的最高收盤為 2026-06-02 的 30660.6，距 52 週高點回撤 11.31%（`valuation.ndx_drawdown`）。R1 門檻水位是 22995.45，從最新收盤起算還要再跌約 15.43% 才會觸及；`r1_met` 為 false。短線壓力正在升溫：截至 2026-07-29 的 7 日窗口（基準日 2026-07-22），VIX 由 16.64 升到 20.66（+24.16%），S&P 500 則由 7498.96 跌到 7316.15（−2.44%）。兩者呈正常的反向走勢，不是 crowded-optionality 共漲讀數（`structural.vix_spx_comove`）。S&P 500 仍高於 200 日均線 4.29%、高於 52 週均線 5.83%，自前次基準以來變動 −1.31%（`valuation.sp500_trend`）。估值仍屬極端：trailing P/E 28.6、Shiller CAPE 40.9（`valuation.sp500_pe_cape`）。槓桿面，FINRA margin debt 6 月為 $1.502T，YoY +51.5%（`retail.margin_debt`），已落在歷史頂部常見的 +40–50% 區間之上，代表一旦下跌，被迫去槓桿的放大效應會很大。不過，散戶情緒已經轉向恐懼：CNN Fear & Greed 為 37（`retail.fear_greed`），AAII Bear 達 42.3%（`retail.aaii`），NAAIM 由 95.64 降到 84.02（`retail.naaim`），部位擁擠度正在消化中，而不是處於過熱狀態。

**判讀：** 回撤已過門檻的一半，但還差約 15%。要在窗口內觸發 R1，需要一個能讓 margin debt 被迫平倉的催化劑，例如 AI 信用事件擴散（R3→R1）、下一輪財報中 capex 回收疑慮升級，或利率端 10Y 期限溢價（term premium）再度上行。依目前證據，這屬於可能但非主要情境。

### R2 資本支出收縮

根據 CNBC 2026-07-28 的 Q2 財報季整理（`ai.hyperscaler_capex`），hyperscaler 2026 capex 指引仍在上修，合計約 $725B：

- Alphabet：FY26 上修到 ≈$205B，方向為「上修」。
- Amazon：$200B，報導歸為續上修，方向為「上修」。
- Meta：$125–145B，報導歸為續上修，方向為「上修」。
- Microsoft：本次蒐集到的證據沒有個別數字或方向，記為「未提供指引（未取得個別數字）」；報導只把它算進合計的續上修敘述。

四家中目前有 0 家下修，距離 R2 要求的兩家還差兩家。同一篇報導也指出，Alphabet 財報後市場對 capex 的審視升高。供給端沒有出現過剩：伺服器 DRAM 交期 30–40 週，3Q26 合約價預估 QoQ +13–18%（`ai.compute_supply_demand`），反映需求仍然吃緊，沒有 order digestion 跡象。產業層級的 AI 營收對 capex 缺口（revenue-to-capex gap）仍大：已披露的年化 AI 終端營收約 $72B（Anthropic ≈$47B＋OpenAI ≈$25B，Epoch 2026-06-15 沿用值），年化 capex 約 $725B（分母為 CNBC 所列 hyperscaler 合計，未含 Oracle 與 neocloud）（`ai.revenue_capex_gap`）。因為沒有前次組合值，本次無法判定缺口是在擴大還是收斂。

**判讀：** R2 是三條路徑中離觸發最遠的一條，目前方向完全相反。窗口內通常還會有兩輪季報（約 10 月下旬的 Q3，以及約 1 月下旬、接近窗口末端的 Q4；本次證據未載明確切日期）。要觸發 R2，必須有兩家在這兩輪內由上修轉為下修。這通常要先發生 R1 級回撤或融資受阻，才會逼出下修。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）正在往信用端重定價的方向發展。2026-07-29 的報導指出，Oracle 遭降評至 BBB-，AI 雲端信用正在重定價，CoreWeave 5Y CDS 升到約 855bp，Nebius 與 CoreWeave 股價同日大跌（`valuation.ai_credit_schism`）。在符合 R3 規模門檻的借款人中，CoreWeave 今年以來以 GPU 擔保募資約 $25B（`structural.ai_infrastructure_debt`），以 AI 算力為主業，可以合理視為 R3 候選。Oracle 雖遭降評，但主業不是 AI 資料中心，不符合 R3 借款人定義，只能作為傳導背景。對照組是整體信用仍緊：HY OAS 2.84%（較前次 +3bp，`monetary.hy_oas`），IG OAS 0.81%（持平，`monetary.ig_oas`）。換言之，AI 單一名稱的信用風險被大幅加價，整體信用市場卻沒有跟進。資金面也看不到壓力：repo 資金壓力（SOFR−IORB）為 0bp，SOFR99−IORB 為 9bp（皆為 2026-07-28），SRF 動用（Standing Repo Facility usage）僅 $0.003bn（2026-07-29）（`monetary.repo_stress_srf`）。本次證據中沒有任何 R3 借款人出現付款違約、covenant waiver、distressed exchange 或 going-concern 字樣，也沒有取得近期到期牆的具體資料。

**判讀：** R3 是三條路徑中動能最強的一條。CDS 已在 distressed 邊緣，但從 CDS 走闊到真正完成違約或 distressed exchange，通常需要再融資失敗或流動性耗盡，在 182 天內完成仍屬少數情境。若 CoreWeave 類借款人出現再融資受阻、評等降至 CCC 區間，或私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）出現可追溯的 gate proration / breach，R3 就會明顯逼近，並可能經 margin debt 去槓桿帶動 R1。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 於 2026-07-29 升到約 855bp，Oracle 降評至 BBB-，AI 雲端信用開始重定價（`valuation.ai_credit_schism`）。CoreWeave 今年以來以 GPU 擔保募資約 $25B，是最接近 R3 規模門檻的借款人（`structural.ai_infrastructure_debt`）。
- [R1] NASDAQ-100 自 2026-06-02 高點 30660.6 回撤到 2026-07-29 的 27192.31，距 52 週高點回撤 11.31%，已走完 R1 門檻的一半（`valuation.ndx_drawdown`）。同期 VIX 7 日上升 24.16% 到 20.66（`structural.vix_spx_comove`）。
- [整體] 槓桿與估值偏高，放大下跌的能量：FINRA margin debt $1.502T，YoY +51.5%（`retail.margin_debt`），超過歷史頂部的 +40–50% 區間；Shiller CAPE 40.9（`valuation.sp500_pe_cape`）；US 槓桿 ETF 總 AUM 創高至約 $198B（`structural.leveraged_etf_aum`）。
- [整體] Fed 緩衝空間受限：CPI YoY 3.46%（2026-06 資料，`monetary.cpi_yoy`），FOMC 於 2026-07-29 以 9-3 維持 3.50–3.75%，CME FedWatch 9 月持平機率約 42%（`monetary.fedwatch`）。10Y 期限溢價（term premium）0.8376%，trailing 7 日 +5.9bp（`monetary.term_premium`）。AI 主導的回檔較難期待快速降息承接。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）約 $72B 對 $725B（分母為 CNBC 所列 hyperscaler 合計，未含 Oracle）（`ai.revenue_capex_gap`）。CNBC 2026-07-28 指出，Alphabet 財報後 capex 審視升高（`ai.hyperscaler_capex`）。這是日後被迫下修的結構性壓力來源。

## 支持 no 的證據

- [整體] 基準率：在任意 182 天窗口內，R1–R3 三者都不發生才是常態。目前沒有任何一條路徑已經觸發（`r1_met` 為 false，`valuation.ndx_drawdown`）。R1 還差約 15.43%，R2 是 0/4 下修，R3 沒有違約事件。
- [R2] 四大 hyperscaler 中，Alphabet（≈$205B）、Amazon（$200B）、Meta（$125–145B）的 2026 capex 指引在 2026-07-28 仍續上修，合計約 $725B（`ai.hyperscaler_capex`）。伺服器 DRAM 交期 30–40 週，3Q26 合約價 QoQ +13–18%（`ai.compute_supply_demand`），需求吃緊，與 capex 下修的前提相反。
- [R3] AI 信用壓力沒有擴散到整體信用與資金市場：HY OAS 2.84%（`monetary.hy_oas`），IG OAS 0.81%（`monetary.ig_oas`），SOFR−IORB 0bp、SRF 動用 $0.003bn（`monetary.repo_stress_srf`）。CFTC 槓桿基金美債期貨淨部位 −7462516 口（2026-07-21），MOVE 由 77.21 降到 74.18（`structural.treasury_basis_trade`），美債基差交易槓桿（Treasury basis-trade leverage）沒有平倉壓力。
- [R1] 情緒與部位已經先降溫，不是極度貪婪下的脆弱頂部：CNN Fear & Greed 37（`retail.fear_greed`），AAII Bear 42.3%（`retail.aaii`），NAAIM 由 95.64 降到 84.02（`retail.naaim`）。市場廣度擴散：RSP 等權 YTD +14.57%，優於 SPY 的 +9.22%（`breadth.rsp_spy`）。
- [R1] 估值溢價收斂：Mag 7 對其餘 493 檔的溢價約 10%，為十年來最便宜的水準之一（`valuation.mag7_multiples`）。Morgan Stanley 對 NVDA 的目標價 $288 以約 22× CY27 EPS 計，目標 PE 未擴張，屬 EPS 驅動（`valuation.analyst_tp_decomposition`）。

## 與前期比較

前次結論：無前次預測（report-2026-07-27 為舊格式評分報告）

report-2026-07-27 是舊格式的六維評分報告，不換算成 yes/no，因此 `flip_evidence` 為空。自 2026-07-27 以來的主要變化如下：

- 市場：NASDAQ-100 收盤由 28039.21（2026-07-27）降到 27192.31（2026-07-29）。S&P 500 自前次基準 −1.31%。VIX 由 18.67 升到 20.66。
- 利率：DGS10 −4bp，DFII10 −3bp，T10YIE +5bp。三腿的視窗不一致，判讀為不可判（視窗不一致）。
- 信用：HY OAS +3bp 到 2.84%，IG OAS 持平。
- 信用事件：2026-07-29 傳出 CoreWeave CDS 約 855bp 與 Oracle BBB- 的信用重定價報導，是本次最重要的新增訊號，但仍未構成 R3 事件。
- 政策：FOMC 於 2026-07-29 維持利率；DFEDTARU/DFEDTARL 不變。

## 資料缺漏與不確定性

⛔ FETCH FAILED 來源：

- structural.zero_dte：搜尋只取得 Cboe 2026-02 的 0DTE 佔比紀錄，沒有當期快照，因此依 required 規則標為 ⛔。0DTE 只是投機結構的輔助指標，即使補上也不會改變本次結論。

✗ NOT DISCLOSED 與證據品質問題，以下來源不作為本次證據：

- monetary.private_credit_liquidity：搜尋結果把 BCRED 突破 5% quarterly redemption cap、比例撥付、redemption-request ratio 升至約 10% 等數字歸給 BCRED，但結果 URL 的標題是 Blue Owl BDC 設限，且 URL 日期（2026-07-02）與列示日期（2026-07-23）不一致，無法追溯到 BCRED 的披露。這是對答案最敏感的缺口：若能證實多家基金出現 gate proration / breach，R3 與 R1 的傳導判讀會明顯偏向 yes。
- monetary.treasury_auctions：結果把 20Y 標售的 dealer takedown 14.67% 與一篇 10Y 標售文章掛在一起，期別不符，無法驗證。
- retail.social_sentiment：BYND 軋空的敘述與結果 URL（Wendy's WEN）不符，無法驗證。
- ai.openai_anthropic_revenue：最新可得的是 2026-06-15 的值，屬上一季，沒有當季披露；只作為 AI 營收對 capex 缺口的沿用組件。
- ai.hyperscaler_financing_mix：quarterly_state 可用（Alphabet Q2 FCF 轉負；hyperscaler 2026 累計發債約 $182B、+1,300% YoY，高於 BIS AER 引用的約 $160bn 全年預估）。但 30 日 event_scan 沒有找到具名發行人、金額與日期的單筆融資事件，依 all 聚合規則整體為 ✗。這方面的融資轉向（from cash flows to debt）只作為背景。
- ai.capital_cycle：兩個組件都沒有披露，增速證據不足，本次不判定週期階段。
- 其他未披露：institutional.bofa_jpm_survey、ai.token_growth、ai.customer_concentration_rpo、ai.depreciation_life、structural.global_leveraged_approvals。
- 零件數篩選：speculation.insider_form4 為 0 件。唯一的搜尋結果是 EDGAR 公司層級 Form 4 清單頁，缺個別 filing URL 與 filing date，不符合 filing-level 要求。structural.us_single_stock_etf 為 0 件，因為窗口內只有申報、沒有核准或上市。
- 數值衝突：Yahoo SKEW 頁面顯示 2026-07-29 VIX 為 19.99，與 FRED VIXCLS 收盤 20.66 不一致，本報告以 FRED 為準。
- margin debt 結果 URL 的路徑日期（2026/06/24）早於 6 月資料應有的發布時點，列示發布日為 2026-07-20，數值照原樣使用，但可追溯性偏弱。margin debt 對整體股市市值的比率本次沒有取得分母，未計算。

最大的不確定性：

1. CoreWeave 類 AI 算力借款人的再融資與到期結構。本次未取得具體到期牆資料；一旦出現再融資受阻，會把答案推向 yes（R3 直接觸發，並經去槓桿帶動 R1）。
2. 下一輪（約 10 月下旬）hyperscaler 財報的 capex 指引。若任兩家由上修轉為下修，R2 會成立。目前方向相反，維持 no。
3. 私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）的真實程度。本次搜尋結果無法追溯；若證實出現跨基金的 net inflow→outflow flip，會提高 R3→R1 的傳導風險。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7316.15 | FRED API (series_id=SP500) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 4.29 | FRED API (series_id=SP500) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 5.83 | FRED API (series_id=SP500) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較前次基準 %） | -1.31 | FRED API (series_id=SP500) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 27192.31 | FRED API (series_id=NASDAQ100) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-30T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 11.31 | FRED API (series_id=NASDAQ100) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026-Q1，家庭股權配置 %） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-30T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 2.84 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 3.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（IG OAS %） | 0.81 | FRED API (series_id=BAMLC0A0CM) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.61 | FRED API (series_id=DGS10) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | -4.0 | FRED API (series_id=DGS10) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.41 | FRED API (series_id=DFII10) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | -3.0 | FRED API (series_id=DFII10) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.26 | FRED API (series_id=T10YIE) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | 5.0 | FRED API (series_id=T10YIE) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl，無新觀測） | 84.25 | FRED API (series_id=DCOILWTICO) | 2026-07-27 | 2026-07-30T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-30T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.28 | FRED API (series_id=T5YIFR) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 0.8376 | FRED API (series_id=THREEFYTP10) | 2026-07-24 | 2026-07-30T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 日） | 5.9 | FRED API (series_id=THREEFYTP10) | 2026-07-24 | 2026-07-30T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.65 | FRED API (series_id=SOFR) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.74 | FRED API (series_id=SOFR99) | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-07-30 | 2026-07-30T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.003（$3M） | FRED API (series_id=RPONTTLD) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| monetary.walcl | WALCL latest（百萬美元，無新觀測） | 6747378.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-22 | 2026-07-30T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（百萬歐元） | 5944015.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-24 | 2026-07-30T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（億日圓） | 6395509.0（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-30T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 20.66 | FRED API (series_id=VIXCLS) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of） | 20.66 | FRED API (series_id=VIXCLS, SP500) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日） | 24.16 | FRED API (series_id=VIXCLS, SP500) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日） | -2.44 | FRED API (series_id=VIXCLS, SP500) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（十億美元，無新觀測） | 2012.1032（$2.01T） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-15 | 2026-07-30T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7462516 | CFTC TFF (cftc_lev_funds) | 2026-07-21 | 2026-07-30T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -45392 | CFTC TFF (cftc_lev_funds) | 2026-07-21 | 2026-07-30T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 74.18 | Yahoo Finance chart API (^MOVE) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2357.5 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-07-29 | 2026-07-30T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl / gurufocus WebSearch | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | CNBC WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | Forbes WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | Yahoo Finance NYSE breadth WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA / Advisor Perspectives WebSearch | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB / cashtag WebSearch（7d） | ✗ NOT DISCLOSED（結果敘述與 URL 不符，無可驗證披露） |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | YCharts WebSearch | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | Reuters / auction recap WebSearch（14d） | ✗ NOT DISCLOSED（標售期別與結果 URL 不符，無可驗證披露） |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch / CNBC WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Bloomberg WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 WebSearch（30d） | ✗ NOT DISCLOSED（BCRED 數字無法追溯至結果 URL） |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報 / CNBC WebSearch | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic / OpenAI / Google WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch / 報導 WebSearch | ✗ NOT DISCLOSED（無當季披露；最新為 2026-06-15） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話 WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：季報 / 發債統計 WebSearch；event_scan：30d 單筆融資掃描 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露（沿用組件）WebSearch | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K / 10-Q WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | quarterly_state：供需增速 WebSearch；event_scan：30d 進出場事件 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | Reuters / Benzinga / Boardroom Alpha 螢幕 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | emarketer WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz / Benzinga / StockTwits / Yahoo movers 螢幕 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | YCharts WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing / etf.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com / Tradr / GraniteShares（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX / TWSE / JPX / ESMA / ETFGI（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe WebSearch | ⛔ FETCH FAILED（僅得 2026-02 舊值，無當期快照） |
| structural.options_volume | 結構｜Options total volume: OCC monthly volume report | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe / Yahoo WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 retail.margin_debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 28.6 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl；原定來源 multpl） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 40.9 | Shiller CAPE ratio July 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio （GuruFocus） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 對其餘 493 檔溢價約 10% | Magnificent 7 valuation premium cheapest decade 2026 | https://www.cnbc.com/2026/07/08/magnificent-seven-stocks-are-the-cheapest-in-a-decade-by-one-measure.html （CNBC） | 2026-07-08 | 2026-07-30T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標價 $288；目標 PE 約 22× CY27 EPS 未擴張，EPS 驅動；舊目標價與 EPS Δ 未披露 | Morgan Stanley NVDA target 288 July 2026 EPS | https://www.gurufocus.com/news/8955458/morgan-stanley-upgrades-nvidia-nvda-with-a-288-target-price （GuruFocus） | 2026-07-13 | 2026-07-30T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 降至 BBB-；CoreWeave 5Y CDS 約 855bp | Oracle BBB- CoreWeave CDS AI credit repricing July 2026 | https://247wallst.com/investing/2026/07/29/nebius-drops-10-coreweave-sinks-9-as-rising-credit-swap-costs-hit-the-ai-cloud-trade/ （247wallst） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| breadth.rsp_spy | SPY +9.22% YTD；RSP +14.57% YTD | RSP vs SPY equal weight YTD 2026 | https://247wallst.com/investing/2026/07/26/is-equal-weighting-the-sp-500-worth-it-heres-what-the-data-says/ （247wallst） | 2026-07-26 | 2026-07-30T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度約 38% | S&P 500 top 10 concentration percent 2026 | https://www.forbes.com/sites/investor-hub/article/sp-500-weight-mag-7-stocks-diversification-risk/ （Forbes） | 2026-07-15 | 2026-07-30T09:30:00+08:00 |
| breadth.advance_decline | NYSE advancers 1.32:1；新高 161、新低 198 | NYSE advance decline new highs new lows July 27 2026 | https://finance.yahoo.com/markets/stocks/articles/stock-market-news-july-27-132000679.html （Yahoo Finance） | 2026-07-27 | 2026-07-30T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（Fear） | CNN Fear and Greed Index July 29 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-06 月資料）$1.502T，YoY +51.5%（URL 路徑日期 2026/06/24 與發布日不一致） | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives；原定來源 FINRA） | 2026-07-20 | 2026-07-30T09:30:00+08:00 |
| retail.aaii | AAII Bear 42.3%／Neutral 28.1%／Bull 29.6% | AAII investor sentiment survey July 23 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-23 | 2026-07-30T09:30:00+08:00 |
| retail.naaim | NAAIM 前值 95.64 → 最新 84.02 | NAAIM exposure index July 2026 | https://ycharts.com/indicators/naaim_number （YCharts；原定來源 naaim.org） | 2026-07-22 | 2026-07-30T09:30:00+08:00 |
| monetary.fedwatch | FOMC 9-3 維持 3.50–3.75%；CME FedWatch 9 月持平機率約 42% | FOMC July 29 2026 hold FedWatch September | https://www.cnbc.com/2026/07/29/fed-rate-decision-july-2026.html （CNBC；原定來源 CME FedWatch） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| monetary.pboc | 人行 MLF 為 5 個月來最大，淨投放約 ¥100B | PBoC MLF net injection liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-24/pboc-adds-most-liquidity-to-economy-in-five-months-to-aid-growth （Bloomberg） | 2026-07-24 | 2026-07-30T09:30:00+08:00 |
| ai.hyperscaler_capex | 2026 capex：Amazon $200B、Alphabet $205B、Meta $125–145B，合計約 $725B，續上修（Microsoft 個別數字未載） | hyperscaler capex 2026 725B raised Meta Amazon Alphabet | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC；Q2 2026 財報季） | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 交期 30–40 週；3Q26 合約價 QoQ +13–18% | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html （TrendForce） | 2026-07-03 | 2026-07-30T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] Alphabet Q2 FCF 轉負；FY26 capex 上修至約 $205B | Alphabet Q2 2026 capex FCF negative debt | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 2026 累計發債約 $182B，+1,300% YoY（趨勢，非單筆事件） | hyperscaler bond issuance 182B 2026 AI credit | https://247wallst.com/investing/2026/07/16/the-ai-revolution-is-reshaping-credit-markets-here-is-what-it-really-says-about-risk/ （247wallst） | 2026-07-16 | 2026-07-30T09:30:00+08:00 |
| ai.revenue_capex_gap | 分子：Anthropic 約 $47B＋OpenAI 約 $25B（沿用 2026-06-15）；分母：年化 capex 約 $725B（CNBC 2026-07-28 hyperscaler 合計，未含 Oracle） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI）；https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-06-15 | 2026-07-30T09:30:00+08:00 |
| speculation.ai_rename_spac | 2026-07-23 至 2026-07-30 的 +AI 改名／SPAC／無營收 IPO 合格事件 0 件 | AI rename SPAC no revenue IPO July 23-30 2026 | Reuters / Benzinga / Boardroom Alpha SPAC 螢幕 | — | 2026-07-30T09:30:00+08:00 |
| speculation.ipo_heat | 2026 IPO 募資 $251B、88 檔；Cerebras（CBRS）首日 +68% | US IPO market 2026 Cerebras first day pop | https://www.emarketer.com/content/ipos-test-investor-appetite-unprofitable-ai-giants （eMarketer） | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週 microcap thematic moonshot 合格 0 件 | microcap 100% single day quantum AI fusion moonshot July 2026 | Finviz / Benzinga / StockTwits / Yahoo movers 螢幕 | — | 2026-07-30T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 考慮延至 2027 IPO、目標估值約 $1T；Anthropic 續進程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground （Benzinga） | 2026-07-28 | 2026-07-30T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內符合 filing-level 要求的 Form 4 合格件數 0 件（結果僅為公司層級 Form 4 清單頁，缺個別 filing URL 與 filing date） | CoreWeave insider Form 4 July 2026 Intrator McBee SEC | SEC EDGAR 公司 Form 4 清單頁（browse-edgar） | — | 2026-07-30T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.66（日值或 5 日均值未載明） | Cboe equity put call ratio July 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio （YCharts；原定來源 Cboe） | 2026-07-27 | 2026-07-30T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高約 $198B（個別 ticker AUM 未載） | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing；原定來源 etf.com） | 2026-07-23 | 2026-07-30T09:30:00+08:00 |
| structural.us_single_stock_etf | 30 日內單股槓桿 ETF 核准／上市合格件數 0 件（僅見 Kioxia 標的申報，非核准或上市） | single-stock leveraged ETF launch July 2026 Kioxia Tuttle | SEC EDGAR / ETF.com / Tradr / GraniteShares / tradingkey | — | 2026-07-30T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 總量 16.0 億口，+45% YoY | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-07-30T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 約 150；VIX term structure contango（頁面 VIX 19.99 與 FRED VIXCLS 20.66 不一致，以 FRED 為準） | VIX SKEW term structure July 29 2026 | https://finance.yahoo.com/quote/%5ESKEW/history/ （Yahoo Finance；原定來源 Cboe） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt $1.502T，+51.5% YoY（交叉引用 retail.margin_debt） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives） | 2026-07-20 | 2026-07-30T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave 今年以來以 GPU 擔保募資約 $25B；5Y CDS 升至約 855bp | AI data center debt financing CoreWeave CDS July 2026 | https://247wallst.com/investing/2026/07/29/nebius-drops-10-coreweave-sinks-9-as-rising-credit-swap-costs-hit-the-ai-cloud-trade/ （247wallst） | 2026-07-29 | 2026-07-30T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-07-30",
  "iso_week": "2026-W31",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-01-28",
  "prior_date": "2026-07-27",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 11.31,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

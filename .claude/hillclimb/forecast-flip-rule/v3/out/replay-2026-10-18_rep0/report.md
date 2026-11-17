> [DRY RUN] this report was not committed to archive.

# 2026-10-18 AI 泡沫破裂預測報告

報告日期：2026-10-18｜ISO 週次：2026-W42｜預測窗口：2026-10-18 → 2027-04-18｜前次基準：report-2026-09-13（35天前）

## 結論

**結論：no**

三條路徑都沒有出現「已在進行中、且可望在窗口內完成」的證據：NASDAQ-100 距 R1 門檻仍需再跌 ≈21.77%，四大 hyperscaler 最新已知 capex 指引仍在擴張、沒有任何一家下修（R2），而 AI 信用端雖明顯重定價（CoreWeave 5Y CDS 創紀錄 1,194.5 bps），但本次來源未顯示任何付款違約、破產申請或 distressed exchange（R3）。信用與流動性壓力正在累積，足以說明脆弱度上升，但不足以推翻「182 天內三項皆不發生」的 base rate。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,935.59（2026-10-15），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 4.13%（`valuation.ndx_drawdown`）。R1 門檻水位為 23,418.52，自最新收盤需再下跌 ≈21.77% 才會觸發。高點僅在九天前創下，指數仍貼近高位；S&P 500 最新 7,659.44（2026-10-16），高於 200 日均線 5.34%、高於 52 週均線 6.78%，自前次基準日僅 +0.03%（`valuation.sp500_trend`）。情緒端已轉弱：Fear & Greed 落在極度恐懼 ≈18（2026-10-16，`retail.fear_greed`），市場廣度上漲 ≈29 對下跌 ≈71（2026-10-16，`breadth.advance_decline`），VIX 自 15.41 升至 16.46（2026-10-08 → 2026-10-15，+6.81%），但同期 S&P 500 −0.27%，未構成 crowded-optionality 同漲讀數（`structural.vix_spx_comove`）。估值端 Shiller CAPE ≈40.54（2026-10-16，`valuation.sp500_pe_cape`），顯示若發生回撤，下檔空間大。

**判讀：** R1 距離門檻仍遠（需再跌 ≈21.77%），目前只是從新高小幅回落。要在窗口內觸發，需要一個能引發估值重置的催化劑——最可能的傳導是 R3 信用事件或利率／油價衝擊（10Y 5.10%、Fed 剛上調 25bp、WTI ≈$101.91）壓縮高 CAPE 下的估值；目前尚無這類強制去槓桿的證據。

### R2 資本支出收縮

本次取得的最新官方口徑來自 2026-07-28 CNBC 報導：Microsoft、Alphabet、Amazon、Meta 四家 2026 年 capex 合計 ≈$725bn（`ai.hyperscaler_capex`，2026 年第二季財報季，carry-forward 至今）。本次來源只提供四家合計，未逐家列出各自的最新指引數字，因此逐家方向如下：

- Microsoft：最新指引見於 2026 年第二季財報季合計口徑；逐家數字本次未確立；本次來源未顯示下修。
- Alphabet：同上；CNBC 報導指其財報後遭遇更高的 capex 審視，但未顯示下修。
- Amazon：同上；未顯示下修。
- Meta：同上；未顯示下修。

截至目前四家中下修家數為 0。下一輪（第三季）財報與再下一輪（第四季，含 2027 年指引）均落在 2026-10-18 → 2027-04-18 窗口內；具體日期本次來源未確立。需求端旁證：H100 隨選中位租金 ≈$4.20／小時（2026-10-07，`ai.compute_supply_demand`），本次未取得利用率或訂單消化證據，無法判定產能缺口已出現。

**判讀：** R2 目前完全沒有啟動跡象（0／4 下修）。窗口內有兩輪財報可供下修，2027 年指引是最大的單一節點；但要觸發需要至少兩家主動下修，通常需先有 R1 式股價壓力或融資成本急升作為前因，現階段證據不支持在窗口內發生。

### R3 AI 信用事件

AI 信用端是本次最明顯的壓力來源：CoreWeave 5Y CDS 創紀錄 1,194.5 bps（2026-10-15，`valuation.ai_credit_schism`），報導標題即為「AI 信用疑慮推升科技違約保險至紀錄高點」。信用端已在重定價，而 NASDAQ-100 只距高點 4.13%，符合「信貸先走闊、股價未跟上」的後期分歧型態。近 30 日 AI 基礎設施融資仍在進行：Lambda 取得 ≈$1bn 的 GPU 擔保融資（2026-10-01，`structural.ai_infrastructure_debt`），顯示融資管道仍開放。整體信用環境轉緊：HY OAS 自 2.65% 走闊至 3.23%（+58 bps，2026-10-15，`monetary.hy_oas`），IG OAS 0.84%（+4 bps，`monetary.ig_oas`）。

是否達到 R3 的 ≥ USD 5bn 負債門檻：本次來源未提供 CoreWeave 或其他 AI 基礎設施借款人的總負債數字，因此規模門檻「未確立」；近期到期牆與再融資需求本次也未取得。本次來源未顯示任何付款違約、契約豁免、distressed exchange 或 going-concern 字樣。

**判讀：** R3 是三條路徑中最接近的一條——CDS 已在高違約風險的定價區間——但從「市場定價高風險」到「破產申請／超過寬限期違約／完成 distressed exchange」之間仍差一個實際事件，且同期 Lambda 仍能融資，代表市場尚未關閉。若窗口內出現再融資失敗、大客戶合約取消或 CDS 持續擴大伴隨評級下調，R3 會成為主驅動並可能連帶觸發 R1。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 創紀錄 1,194.5 bps（2026-10-15），AI 基礎設施信用已被定價為高違約風險，且明顯領先股價（NASDAQ-100 只距高點 4.13%）——典型信貸先行的後期分歧訊號 `valuation.ai_credit_schism` `valuation.ndx_drawdown`
- [整體] 信用與債市波動同步走壞：HY OAS 自 2.65% 升至 3.23%（+58 bps，2026-10-15）`monetary.hy_oas`；MOVE 自 82.21 升至 101.1（2026-10-16）`structural.treasury_basis_trade`
- [整體] 政策緩衝受限：Fed 目標區間上調 25bp 至 3.75%–4.00%（2026-10-17）`monetary.fed_funds`，CPI YoY 3.72%（2026-09 月資料）`monetary.cpi_yoy`，WTI ≈$101.91（2026-10-14）`monetary.wti`，10Y 5.10%（2026-10-15）`monetary.dgs10`——AI 主導的回撤發生時 Fed 降息托底空間小
- [R1] 估值與部位極度延伸：Shiller CAPE ≈40.54（2026-10-16）`valuation.sp500_pe_cape`；BofA 10 月 FMS 科技股淨加碼 ≈37%，為 2020 年 8 月以來最高（2026-10-13）`institutional.bofa_jpm_survey`；家庭股票配置 48.23%（2026 Q2）`retail.household_equity_allocation`——一旦啟動回撤，跌幅可能放大
- [R1] 風險偏好開始退潮：Fear & Greed 極度恐懼 ≈18（2026-10-16）`retail.fear_greed`；市場廣度上漲 ≈29 對下跌 ≈71（2026-10-16）`breadth.advance_decline`；兩週內第 4 檔 IPO 撤件或延後（2026-10-16）`speculation.ipo_heat`
- [R2] 營收對 capex 缺口巨大：年化 AI 終端營收只有 Anthropic run-rate ≈$65bn（2026-08-17）可計入，對比年化 capex ≈$725bn（分母：top-4，Oracle 本次未取得），一旦融資成本續升，capex 回收疑慮可能轉為指引下修 `ai.revenue_capex_gap` `ai.hyperscaler_capex`

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.13%（2026-10-15 收盤 29,935.59 vs 2026-10-06 高點 31,224.69），距 R1 門檻 23,418.52 尚需再跌 ≈21.77%；S&P 500 仍高於 200 日均線 5.34%（2026-10-16）`valuation.ndx_drawdown` `valuation.sp500_trend`
- [R2] 四大 hyperscaler 2026 capex 合計 ≈$725bn（2026-07-28），本次來源沒有任何一家下修，R2 需要四家中兩家下修，目前為 0／4 `ai.hyperscaler_capex`
- [R3] AI 基礎設施融資管道仍開放：Lambda 於 2026-10-01 取得 ≈$1bn GPU 擔保融資 `structural.ai_infrastructure_debt`；CDS 雖高，但本次來源未顯示任何付款違約、破產申請或 distressed exchange `valuation.ai_credit_schism`
- [整體] 系統性資金面未失序：SOFR 3.89% 對 IORB 3.90%（SOFR−IORB −1 bp，2026-10-15），SOFR99 3.97%，SRF 動用 0（2026-10-16）`monetary.repo_stress_srf`；IG OAS 僅 0.84%（2026-10-15）`monetary.ig_oas`；10Y 期限溢價 1.0729% 且近 7 日 −1.2 bps（2026-10-09）`monetary.term_premium`
- [整體] 美債需求與基差部位穩定：10Y 標售 bid-to-cover ≈2.77、需求強勁（2026-10-07）`monetary.treasury_auctions`；槓桿基金美債期貨淨空 −6,883,343 口，近 4 週僅增 309,307 口空單，無平倉潮（2026-10-13），OFR tri-party repo 成交量 $2,264.1bn 持平（2026-10-16）`structural.treasury_basis_trade`
- [整體] 投機端沒有過熱的末段特徵：近 7 日 +AI 改名／SPAC 0 件 `speculation.ai_rename_spac`、microcap moonshot 0 件 `speculation.microcap_moonshots`、近 30 日美國單一個股槓桿 ETF 核准／上市 0 件 `structural.us_single_stock_etf`；AI 需求仍在籌資：Anthropic 目標 11 月中上市（2026-10-05）`speculation.upcoming_ai_ipos`

## 與前期比較

前次結論：無前次預測（report-2026-09-13 為舊格式評分報告）

前次為舊格式評分報告，不轉譯為 yes／no；以下僅摘要自 2026-09-13 以來的重要變化：

- HY OAS 自 2.65% 走闊至 3.23%（+58 bps），MOVE 自 82.21 升至 101.1：信用與利率波動同步升溫（`monetary.hy_oas`、`structural.treasury_basis_trade`）。
- Fed 目標區間上限自 3.75% 上調至 4.00%；10Y 自 4.96% 升至 5.10%（+14 bps），其中 DFII10 +18 bps、T10YIE −1 bp（`monetary.fed_funds`、`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。
- 10Y Δ 分解判讀：不可判（視窗不一致）——T10YIE 最新觀測日（2026-10-16）與 DGS10／DFII10（2026-10-15）不同，driver 不予推斷。
- AI 信用端出現新的紀錄級訊號（CoreWeave 5Y CDS 1,194.5 bps，2026-10-15，`valuation.ai_credit_schism`），但 NASDAQ-100 仍只距高點 4.13%。
- S&P 500 自前次基準 7,656.98 至 7,659.44，幾乎持平（+0.03%，`valuation.sp500_trend`）；銀行對 NBFI 放款增 2.14% 至 $2.10T（`structural.nbfi_bank_loans`）。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `breadth.rsp_spy`：搜尋只取得 2026-07-18 的 RSP YTD ≈12.08%，早於前次基準日、且無 SPY 對照值，不是當期可用值。廣度已有 `breadth.advance_decline` 的當期讀數，此缺口不會改變答案。
- `breadth.top10_concentration`：只取得 2026-07-31 的集中度 ≈38.9%，早於前次基準日，不作當期證據。集中度是脆弱度指標而非時點催化劑，此缺口不會改變答案。

其他資料限制（非 FETCH FAILED）：

- `valuation.mag7_multiples` 只取得單一成員 MSFT 前瞻本益比 24.5（2026-09-24），Mag 7 加權 P/E 與 P/S 對 10 年均值本次未確立，未用作判斷依據。
- `ai.hyperscaler_capex` 只取得四家合計 ≈$725bn，逐家指引數字與方向本次未確立；R2 的 0／4 判讀依據是「本次來源未見任何下修報導」。
- `retail.margin_debt` 只取得 2026-08 水位 ≈$1.45T，YoY 與 margin debt／市值比率本次未確立。
- CoreWeave 等 AI 基礎設施借款人的總負債、到期牆本次未確立，無法確認誰明確達到 R3 的 USD 5bn 門檻。
- `ai.openai_anthropic_revenue` 最新披露（2026-08-17）屬上一季，依規則標 ✗ NOT DISCLOSED；`ai.revenue_capex_gap` 依 carry-forward 規則沿用該數值。`monetary.pboc` 只取得 1–7 月資料（2026-08-15），非當期，標 ✗ NOT DISCLOSED。
- 本次 case 檔的搜尋紀錄將 `structural.treasury_basis_trade` 記為腳本三區塊 fetch_failed，但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 皆為 `status: ok`；依 artifact 以 ✓ API 記錄。

最大不確定性：

1. AI 信用端是否從 CDS 重定價走到實際事件：若窗口內出現 CoreWeave 等借款人再融資失敗、評級大幅下調或 distressed exchange，答案會轉向 yes（R3，並可能連帶 R1）。
2. 第三、四季財報（含 2027 年 capex 指引）：若兩家以上下修，R2 直接成立；若指引續升，則進一步支持 no。
3. 利率與油價：Fed 已上調 25bp、CPI 3.72%、WTI ≈$102，若通膨迫使進一步緊縮並把 10Y 推高，估值壓縮可能加速 R1；反之若緊縮停止，壓力會減輕。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7659.44 | FRED API (series_id=SP500), fetch_macro.py sp500_trend | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 5.34 | FRED API (series_id=SP500), fetch_macro.py sp500_trend | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 6.78 | FRED API (series_id=SP500), fetch_macro.py sp500_trend | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29935.59 | FRED API (series_id=NASDAQ100), fetch_macro.py ndx_drawdown | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100), fetch_macro.py ndx_drawdown | 2026-10-06 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.13 | FRED API (series_id=NASDAQ100), fetch_macro.py ndx_drawdown | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API (series_id=NASDAQ100), fetch_macro.py ndx_drawdown | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q2，家庭股票佔金融資產 %） | 48.2301354474（48.23%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 4.0 | FRED API (series_id=DFEDTARU) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.75 | FRED API (series_id=DFEDTARL) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 3.23 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps（相對前次基準） | 58.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.84 | FRED API (series_id=BAMLC0A0CM) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 5.1 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | 14.0 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.78 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | 18.0 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.35 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | -1.0 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（美元／桶） | 101.91 | FRED API (series_id=DCOILWTICO) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料，YoY %） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.33 | FRED API (series_id=T5YIFR) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 1.0729 | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（序列自身 trailing 7 日） | -1.2 | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.89 | FRED API (series_id=SOFR) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.97 | FRED API (series_id=SOFR99) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.9 | FRED API (series_id=IORB) | 2026-10-18 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.walcl | WALCL latest（百萬美元） | 6,755,639（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（百萬歐元） | 5,943,911（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（億日圓） | 6,250,253（¥625.03T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.46 | FRED API (series_id=VIXCLS) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（7 日窗 as_of） | 16.46 | fetch_macro.py vix_spx_comove block (FRED) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日 %） | 6.81 | fetch_macro.py vix_spx_comove block (FRED) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日 %） | -0.27 | fetch_macro.py vix_spx_comove block (FRED) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（十億美元） | 2097.9713（$2.10T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG chg_pct（相對前次基準 %） | 2.14 | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（槓桿基金美債期貨淨部位，口） | -6883343 | CFTC TFF futures-only (cftc_lev_funds) | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -309307 | CFTC TFF futures-only (cftc_lev_funds) | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 101.1 | Yahoo Finance chart API ^MOVE (move_index) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index delta_abs（相對前次基準） | 18.89 | Yahoo Finance chart API ^MOVE (move_index) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo 成交量，十億美元） | 2264.1 | OFR STFM REPO-TRIV1_TV_TOT-P (ofr_repo) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com，WebSearch primary | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch；僅取得 MSFT 單一成員前瞻 P/E | ✓ SEARCH-VERIFIED（部分：加權 P/E 未確立） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch，90 日且同季窗 | ✗ NOT DISCLOSED（搜尋完成，窗內無合格 TP 上修） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch，14 日窗 | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ⛔ FETCH FAILED（僅取得 2026-07-18 過時值、無 SPY 對照） |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch | ⛔ FETCH FAILED（僅取得 2026-07-31 過時值） |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch，月頻 stock-of-state | ✓ SEARCH-VERIFIED（2026-08 月資料） |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch，7 日窗 | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch primary | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✓ SEARCH-VERIFIED（BofA 10 月 FMS） |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series | fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch，14 日窗 | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch | ✗ NOT DISCLOSED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok，無新觀測） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✗ NOT DISCLOSED（僅取得 1–7 月資料，非當期） |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch，30 日窗 | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch，stock-of-state carry-forward | ✓ SEARCH-VERIFIED（2026 Q2 財報季合計口徑） |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✗ NOT DISCLOSED（最新披露 2026-08-17 屬上一季） |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch；quarterly_state carry；event_scan 30 日窗 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch，各組件 carry-forward | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch，30 日窗 | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch；quarterly_state carry；event_scan 30 日窗 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch＋SEC EDGAR 8-K 篩選，7 日窗 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch，7 日窗 | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch movers 篩選，7 日窗 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch，30 日窗 | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR Form 4＋WebSearch，14 日窗 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch primary | ✗ NOT DISCLOSED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR ETF 申報＋ETF.com feed，30 日窗 | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch，7 日窗 | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED（VIX、SKEW；stock-bond correlation 未取得） |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED（比率未確立） |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch，30 日窗 | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py cftc_lev_funds、move_index、ofr_repo | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE ≈40.54（原定來源 multpl / GuruFocus） | Shiller PE CAPE ratio current October 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.mag7_multiples | MSFT 前瞻本益比 24.5（Mag 7 單一成員） | Magnificent 7 forward P/E valuation October 2026 | https://articlegateway.com/?p=146 | 2026-09-24 | 2026-10-18T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 紀錄 1,194.5 bps | AI credit fears tech default insurance record highs October 2026 | https://www.businessday.co.za/world/international-companies/2026-10-15-ai-credit-fears-push-tech-default-insurance-to-record-highs/ （BusinessDay） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| breadth.advance_decline | 上漲 ≈29 對下跌 ≈71 | market breadth October 16 2026 percent above 200-day advance decline | https://www.thetrading.tools/market-breadth | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 極度恐懼 ≈18（原定來源 CNN） | CNN Fear and Greed Index October 16 2026 extreme fear | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-08 月資料）≈$1.45T（原定來源 FINRA） | FINRA margin debt August 2026 year over year | https://www.thetrading.tools/margin-debt | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| retail.aaii | AAII 看多 ≈38.7%（週至 2026-10-14） | AAII sentiment survey week ending October 14 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA 10 月 FMS 科技股淨加碼 ≈37%，2020 年 8 月以來最高 | BofA October 2026 fund manager survey tech overweight cash | https://www.bloomberg.com/news/articles/2026-10-13/bofa-poll-shows-investors-most-exposed-to-tech-stocks-since-2020 （Bloomberg） | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover ≈2.77，需求強勁 | Treasury 10-year note auction October 7 2026 bid-to-cover | https://www.rttnews.com/3697286/ten-year-note-auction-attracts-strong-demand.aspx （RTTNews） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計 ≈$725bn（2026 Q2 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選中位租金 ≈$4.20／小時 | GPU rental price index HBM DRAM contract price October 2026 | https://uvik.net/blog/gpu-price-index/ | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 2026 年 hyperscaler 發債預估 ≈$190bn（carry 背景） | hyperscaler bond issuance 2026 capex versus free cash flow | https://www.twentyfouram.com/insights/oracle-clears-the-supply-cloud-with-record-demand （TwentyFour AM） | 2026-02-02 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 分子：Anthropic run-rate ≈$65bn；分母取自 ai.hyperscaler_capex top-4 ≈$725bn | AI revenue versus capex gap 2026 annualized | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement October 2026 | 檢查來源：SEC EDGAR 8-K、SPACInsider、Boardroom Alpha | — | 2026-10-18T09:30:00+08:00 |
| speculation.ipo_heat | 兩週內第 4 檔 IPO 撤件或延後 | IPO market October 16 2026 pulled postponed Firmus Oura | https://www.ipox.com/ipox/the-ipox-update-10162026 （IPOX） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描（0 件；PFAI 10/7 +116.7% 落在窗外） | biggest stock gainers week October 12-16 2026 microcap 100% | 檢查來源：Tapeboard movers archive、Financial Modeling Prep daily gainers、Yahoo movers | — | 2026-10-18T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 11 月中上市 | Anthropic IPO October 2026 timing valuation S-1 | https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market （CNN） | 2026-10-05 | 2026-10-18T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件；NVDA 10/9 申報缺 filing-level 細節） | insider selling Form 4 October 2026 Nvidia AI executives SEC | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-10-18T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模 ≈$40.04bn（TSLL 流入居前） | single stock leveraged ETF assets October 2026 weekly flows | https://www.etfaction.com/single-stock-traders-pile-into-tsll-and-intw-as-levered-flows-surge/ （ETF Action） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval October 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed | — | 2026-10-18T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 2026-09 月度 ADV 創紀錄 ≈3.4 百萬口 | Cboe September 2026 derivatives volume 0DTE SPX record | https://www.cboe.com/insights/posts/market-metrics-that-matter-derivatives-september-2026-volume-highlights （Cboe） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.options_volume | OCC 2026-09 月總結算量 1,486,062,415 口 | OCC September 2026 monthly volume data | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report （OCC） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX ≈14.84、SKEW 154.34 | VIX term structure SKEW October 2026 options brief | https://www.home.saxo/content/articles/options/the-middle-got-cheaper-the-edge-did-not---options-brief---12-october-2026-12102026 （Saxo） | 2026-10-12 | 2026-10-18T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-08 月資料）≈$1.45T，市值比率未確立 | margin debt to market cap August 2026 | https://www.thetrading.tools/margin-debt | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Lambda GPU 擔保融資 ≈$1bn | AI data center debt Lambda CoreWeave financing October 2026 | https://valueaddvc.com/pulse/ai-data-center-debt-financing-risk-2026 （ValueAdd VC） | 2026-10-01 | 2026-10-18T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-10-18",
  "iso_week": "2026-W42",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-04-18",
  "prior_date": "2026-09-13",
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 4.13,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

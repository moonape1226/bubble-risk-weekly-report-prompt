> [DRY RUN] this report was not committed to archive.

# 2026-08-06 AI 泡沫破裂預測報告

報告日期：2026-08-06｜ISO 週次：2026-W32｜預測窗口：2026-08-06 → 2027-02-04｜前次基準：report-2026-08-03（3天前）

## 結論

**結論：no**

三條路徑目前都離解析門檻很遠：NASDAQ-100 僅距 52 週高點回撤 3.83%（R1 需要再跌約 22%），四大 hyperscaler 的 2026 capex 指引仍在上修而非下修（R2）。R3 是唯一出現實質壓力的路徑（CoreWeave 5Y CDS ≈855bp、$2.6B 貸款利差 +125bp），但沒有任何付款違約、破產或 distressed exchange 的證據，且整體信用利差仍處緊縮水位，不足以推翻「182 天內三者皆不發生」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,487.79（2026-08-05），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 3.83%；R1 門檻水位為 22,995.45，自最新收盤還需再下跌約 6,492 點（約 22.02%）才會觸發（`valuation.ndx_drawdown`）。指數 7 月 29 日曾回落至 27,192.31，之後一週內反彈逾 8%。估值與價格延伸確實偏高：S&P 500 trailing P/E 29.74、Shiller CAPE 42.19（2026-08-05，`valuation.sp500_pe_cape`），S&P 500 7,723.55 高於 200 日均線 9.71%、高於 52 週均線 11.32%（`valuation.sp500_trend`）。但同期 VIX 由 20.66 降至 15.81、S&P 500 上漲 5.57%（2026-07-29 → 2026-08-05），屬正常的股漲波動降，未出現 crowded-optionality 共振（`structural.vix_spx_comove`）；HY OAS 2.73%、IG OAS 0.78%（2026-08-04）仍極緊（`monetary.hy_oas`、`monetary.ig_oas`）。槓桿與投機面偏熱：FINRA 6 月 margin debt $1.502T、YoY +51.5%（`retail.margin_debt`），US 槓桿 ETF AUM ≈$198B 創高（`structural.leveraged_etf_aum`），代表一旦下跌，跌幅可能被放大。

**判讀：** R1 距門檻很遠（還差約 22%）。要在窗口內成立，需要一個能同時打擊 AI 盈利預期與流動性的催化劑——例如 R3 型信用事件外溢、hyperscaler 下修 capex，或利率／期限溢價急升造成的估值重定價；高 CAPE 與 margin debt YoY +51.5% 說明一旦啟動跌幅可能很深，但目前沒有證據顯示這樣的下跌已在進行中。

### R2 資本支出收縮

CNBC 2026-07-28 報導：hyperscaler 2026 capex 合計續上修至 ≈$725B，Alphabet 在 Q2 財報上修 capex 指引，市場反應為賣壓（`ai.hyperscaler_capex`）。逐家狀態依本次可得證據：

- Alphabet：Q2 2026 財報（2026-07 下旬）上修，方向＝上修。
- Microsoft、Amazon、Meta：本次證據僅提供合計數字「續上修」，未逐家列出最新指引數值；沒有任何一家下修的證據。

截至目前四家之中下修家數為 0。窗口（至 2027-02-04）涵蓋兩次季度財報週期，但具體財報日期不在本次證據內。需求側證據仍支撐 capex：HBM/DRAM 合約價續升、H200 租金 ≈$4.39/hr、供給缺口延至 1H2027（2026-08-01，`ai.compute_supply_demand`）；Microsoft RPO ≈$678B（2026-07-30，`ai.customer_concentration_rpo`）。反面是投資報酬落差：已披露 AI 終端年化營收 ≈$72B（Anthropic ≈$47B＋OpenAI ≈$25B，Epoch 2026-06-15）vs hyperscaler 2026 capex 合計 ≈$725B（分母：CNBC 報導之 hyperscaler 合計，未逐家拆分；不代表全產業），缺口逾十倍（`ai.revenue_capex_gap`）；且 Microsoft RPO 約 32% 繫於單一客戶 OpenAI，存在 backlog 重複計算風險（RPO double-counting）的集中度疑慮。

**判讀：** R2 目前方向相反（上修而非下修）。要成立需四家中兩家在接下來的財報中轉向下修；在算力仍供不應求、RPO 持續累積的情況下，這需要先出現需求面的明確破口（例如主要 AI 客戶融資受阻或 R1 型市場重挫迫使管理層收縮），目前證據不支持窗口內發生。

### R3 AI 信用事件

符合 R3 規模門檻的主要候選是 CoreWeave（AI 算力為主業、負債規模遠超 50 億美元）。信用定價已明顯走闊：CoreWeave 5Y CDS ≈855bp，$2.6B 貸款利差被迫擴大 +125bp，貸款投資人要求加強 covenants；Oracle CDS ≈215bp（2026-08-03，`valuation.ai_credit_schism`）。Bloomberg 2026-07-29 報導 CoreWeave 為 $2.6B 與 Anthropic 掛鉤的貸款調高收益率；Nebius 07-17 取得 $775M 擔保融資（`structural.ai_infrastructure_debt`）。這是 AI 信用定價分歧（equity-vs-credit schism）中「信貸端開始重定價」的訊號：AI 基建借款人的融資成本上升，同時 NASDAQ-100 仍貼近高點。不過，本次證據中沒有任何付款違約、寬限期、covenant waiver、distressed exchange 或 going-concern 文字；CoreWeave 仍能完成融資（雖然代價更高）。整體信用環境也未轉差：HY OAS 2.73%（2026-08-04，`monetary.hy_oas`）、repo 資金壓力（SOFR−IORB）僅 1bp、SOFR99−IORB 9bp、SRF 動用 $0.001bn（`monetary.repo_stress_srf`）。

**判讀：** R3 是三條路徑中最接近的，但仍有距離：855bp 的 CDS 代表市場已將顯著違約風險定價，但要解析為 yes 需要真正的違約／破產／distressed exchange。最可能推過門檻的是：再融資窗口關閉（貸款需求轉弱到無法以任何利差成交）、主要客戶（OpenAI／Anthropic）付款能力出現疑慮，或整體 HY 市場轉向。目前融資仍可取得，判斷窗口內不成立。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS ≈855bp、$2.6B 貸款利差 +125bp 並被要求加 covenants，Oracle CDS ≈215bp（2026-08-03），AI 基建信用已在重定價而股價未跟上（`valuation.ai_credit_schism`）。
- [R3] CoreWeave 2026-07-29 被迫為 $2.6B Anthropic 掛鉤貸款調高收益率，顯示 AI infrastructure debt financing / vendor-financing loops 的邊際融資成本上升、且擔保品集中於少數 AI 客戶（`structural.ai_infrastructure_debt`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）：已披露 AI 終端年化營收 ≈$72B vs hyperscaler 2026 capex 合計 ≈$725B（分母：CNBC 報導之 hyperscaler 合計），Alphabet 上修 capex 已招致賣壓（2026-07-28），投資人對回本的耐心正在下降（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`）。
- [整體] 槓桿與估值延伸：FINRA 6 月 margin debt $1.502T、YoY +51.5%（`retail.margin_debt`），Shiller CAPE 42.19（`valuation.sp500_pe_cape`），US 槓桿 ETF AUM ≈$198B 創高（`structural.leveraged_etf_aum`）——一旦下跌，被強迫去槓桿放大的空間很大。
- [整體] 財政／利率面壓力：美債 5Y 標售連續 14 次 tail、bid-to-cover 為 2022-09 以來最差（2026-07-28，`monetary.treasury_auctions`），10Y 期限溢價（term premium）0.8681%、trailing 7 日 +3bp（2026-07-31，`monetary.term_premium`），長端利率重定價可能壓縮高估值股票。
- [R2] Microsoft RPO ≈$678B，其中約 32% 繫於單一客戶 OpenAI（2026-07-30），集中度意味主要客戶一旦出問題，backlog 可能大幅縮水（`ai.customer_concentration_rpo`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 3.83%（29,487.79，2026-08-05；高點 30,660.6，2026-06-02），離 R1 門檻水位 22,995.45 還需再下跌約 22%（`valuation.ndx_drawdown`）。
- [R2] hyperscaler 2026 capex 合計續上修至 ≈$725B、Alphabet 在 Q2 再上修（2026-07-28），四家中下修家數為 0（`ai.hyperscaler_capex`）。
- [R2] 算力仍供不應求：HBM/DRAM 合約價續升、H200 租金 ≈$4.39/hr、供給缺口延至 1H2027（2026-08-01），不像是會觸發 capex 下修的需求環境（`ai.compute_supply_demand`）。
- [整體] 系統性信用與資金面平穩：HY OAS 2.73%、IG OAS 0.78%（2026-08-04，`monetary.hy_oas`、`monetary.ig_oas`）；SOFR−IORB 1bp、SRF 動用 $0.001bn（`monetary.repo_stress_srf`）；MOVE 73.58、較前次 80.48 下降（`structural.treasury_basis_trade`）——不具備信用事件迅速外溢的條件。
- [R1] VIX 由 20.66 降至 15.81，同期 S&P 500 +5.57%（2026-07-29 → 2026-08-05），co-movement 判讀為 false，市場剛消化 7 月底的回檔（`structural.vix_spx_comove`）。
- [R3] CoreWeave 雖付出更高利差，仍完成 $2.6B 貸款；Nebius 07-17 取得 $775M 擔保融資，AI 基建借款人目前仍可進入融資市場（`structural.ai_infrastructure_debt`）。
- [整體] 情緒未達狂熱：CNN Fear & Greed ≈58（Greed，2026-08-05，`retail.fear_greed`），AAII Bear 42.1% 高於 Bull 31.0%（2026-07-30，`retail.aaii`），RSP 等權 YTD +14.26% 領先 SPY +13.71%（`breadth.rsp_spy`），上漲並非僅由少數權值股支撐。

## 與前期比較

前次結論：無前次預測（report-2026-08-03 為舊格式評分報告）

flip_evidence 為空：前次為舊格式評分報告，其分數不轉譯為 yes/no。自 2026-08-03 以來的主要變化：

- NASDAQ-100 由 28,776.8（2026-08-03）升至 29,487.79（2026-08-05），R1 距離擴大。
- MOVE 由 80.48 降至 73.58，HY OAS 由 2.78% 收窄至 2.73%；10Y 殖利率由 4.70% 降至 4.63%（ΔDGS10 −7bp、ΔDFII10 −3bp、ΔT10YIE −5bp，判讀：不可判（視窗不一致））。
- AI 信用定價分歧報導（2026-08-03）顯示 CoreWeave 信用持續走闊，R3 壓力為本次最重要的新證據，但未達違約層級。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源為 ✗ NOT DISCLOSED（檢索完成但無合格當期披露）：retail.naaim、institutional.bofa_jpm_survey、monetary.private_credit_liquidity、ai.token_growth、ai.openai_anthropic_revenue（最新 Epoch 數據為 2026-06-15，屬上一季，不符當季要求；其數字僅作為 AI 營收對 capex 缺口的沿用組件）、ai.hyperscaler_financing_mix（quarterly_state 可得：Sage Advisory 2026-07-24 稱 top-5 capex 已超越 FCF、2026 發債 ≈$182B、>$120B 表外 SPV；但 30 日 event_scan 無新交易）、ai.depreciation_life、ai.capital_cycle（兩組件皆無合格披露，本次不判定資本週期階段）、structural.global_leveraged_approvals。其中私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）與 hyperscaler 融資事件掃描的缺口與 R3 直接相關：若有未被捕捉的 gate proration / breach 或大型表外融資受阻，可能讓 R3 判讀偏向 yes；其餘缺口不太可能改變答案。

其他資料品質註記：structural.zero_dte 唯一可得數據為 Cboe 發布日 2026-05-31 的 0DTE 佔比 ≈65%，資料偏舊；speculation.insider_form4 的候選（含 Snowflake、Tempus AI 內部人售股報導）缺 Form 4 filing date 與個別 filing URL，未達 filing-level 要求，故記為 0 件；structural.us_single_stock_etf 的 GlobeNewswire 新聞稿 URL 日期為 2026-07-07，與檢索摘要所列 2026-07-30 不一致，本報告採較早的 2026-07-07（仍在 30 日窗內）；monetary.pboc 的逆回購 ≈¥2.1T（7/29–8/3）晚於該文發布日 2026-07-24，日期矛盾，僅採用 7/24 MLF 淨投放 ¥100B。逐家 hyperscaler capex 數值（Microsoft、Amazon、Meta）本次證據只有合計，無法逐家確認方向。

最大的不確定性：

1. CoreWeave 的再融資能力：若信貸市場對 AI 基建借款人關門（CDS 進一步飆升、貸款無法成交），R3 可能在窗口內成立，並可能經由 R1 外溢——這是最可能把答案推向 yes 的因素。
2. 下一輪 hyperscaler 財報（窗口內涵蓋兩次）：若 capex 指引開始轉向持平或下修，R2 會快速升溫；目前趨勢推向 no。
3. 美債供給與期限溢價：5Y 連續 tail 與期限溢價上升若演變為國債市場失序（Treasury market dysfunction），可能觸發高估值股票的 R1 型重定價；目前 MOVE 下降、repo 平穩，推向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7723.55 | FRED API (series_id=SP500) sp500_trend | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 9.71 | FRED API (series_id=SP500) sp500_trend | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 11.32 | FRED API (series_id=SP500) sp500_trend | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29487.79 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-06-02 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（回撤 %） | 3.83 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026-Q1 季資料，% of financial assets） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（%） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（%） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.73 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.63 | FRED API (series_id=DGS10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（vs 2026-08-03） | -7.0 | FRED API (series_id=DGS10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.4 | FRED API (series_id=DFII10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.22 | FRED API (series_id=T10YIE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl） | 81.96 | FRED API (series_id=DCOILWTICO) | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料，%） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-08-06T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.26 | FRED API (series_id=T5YIFR) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（%，Kim-Wright） | 0.8681 | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.66 | FRED API (series_id=SOFR) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.74 | FRED API (series_id=SOFR99) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-06 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（十億美元，SRF 動用 read） | 0.001 | FRED API (series_id=RPONTTLD) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6738190.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5941248.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.81 | FRED API (series_id=VIXCLS) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of 2026-08-05，base_date 2026-07-29，window_days 7） | 15.81 | FRED API vix_spx_comove block | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（%） | -23.48 | FRED API vix_spx_comove block | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（%） | 5.57 | FRED API vix_spx_comove block | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2004.9941（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-22 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7481041 | CFTC TFF cftc_lev_funds | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -52919 | CFTC TFF cftc_lev_funds | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.58 | Yahoo chart ^MOVE move_index | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2342.8 | OFR STFM REPO-TRIV1_TV_TOT-P ofr_repo | 2026-08-05 | 2026-08-06T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com，WebSearch primary | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | SSGA 市場評論，WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方 TP 調整報導（investing.com），WebSearch primary | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py，FRED SP500 sp500_trend | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py，FRED NASDAQ100 ndx_drawdown | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導（techtimes），14 日 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | financecharts，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | Pensions & Investments，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | StockCharts breadth，WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com，WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA via Advisor Perspectives，WebSearch | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com，WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | Reddit WSB／cashtag 報導，7 日 WebSearch | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py，FRED BOGZ1FL153064486Q | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim.org／YCharts，WebSearch primary | ✗ NOT DISCLOSED（檢索完成，無當期週值） |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查報導，WebSearch | ✗ NOT DISCLOSED（檢索完成，無新調查） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py，FRED API | ✓ API DFEDTARU ok；DFEDTARL ok |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py，FRED API | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py，FRED API | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py，FRED API | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py，FRED API | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py，FRED API（FRED 直取，非 DGS10−DFII10 推算） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py，FRED API | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py，FRED API | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py，FRED API | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py，FRED API | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py，FRED API repo_stress block | ✓ API SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | 標售 recap 報導，14 日 WebSearch primary | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要，WebSearch primary | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py，FRED API | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py，FRED API | ✓ API ECBASSETSW ok；JPNASSETS ok |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | investing.com 英文摘要，WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC／interval fund 披露，30 日 WebSearch primary | ✗ NOT DISCLOSED（檢索完成，30 日內無合格披露） |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報報導（CNBC），WebSearch | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露，WebSearch | ✗ NOT DISCLOSED（檢索完成，本季無披露） |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／媒體報導，WebSearch | ✗ NOT DISCLOSED（最新為 2026-06-15，上一季） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話會議報導，WebSearch primary | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | GPU 租金／記憶體價格報導，WebSearch primary | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：Sage Advisory 季頻彙整；event_scan：30 日發債／私募信貸搜尋，WebSearch primary | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露（Epoch 營收＋CNBC capex），WebSearch primary | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K／10-Q／電話會議，30 日 WebSearch primary | ✗ NOT DISCLOSED（檢索完成，30 日內無變動） |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | quarterly_state：供需增速；event_scan：30 日進出場事件，WebSearch primary | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | Reuters／Benzinga／BusinessWire，7 日 WebSearch | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | Renaissance Capital，WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／StockAnalysis／StockTitan gainers，7 日 WebSearch primary | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名媒體報導（Benzinga），30 日 WebSearch | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4，14 日搜尋 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | YCharts，WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing／etf.com，WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire 發行新聞稿，30 日 WebSearch | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA，7 日 WebSearch | ✗ NOT DISCLOSED（檢索完成，7 日內無英文披露） |
| structural.zero_dte | 結構｜0DTE option volume | Cboe 投資人簡報摘要，WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC monthly | theocc.com，WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe insights，WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py，FRED VIXCLS＋vix_spx_comove block | ✓ API VIXCLS ok；vix_spx_comove ok |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 Retail Sentiment margin debt，WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | Bloomberg 等，30 日 WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py，FRED API | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py：cftc_lev_funds＋move_index＋ofr_repo；WebSearch 補充 | ✓ API cftc_lev_funds ok；move_index ok；ofr_repo ok |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.74（原定來源 multpl／gurufocus） | S&P 500 trailing P/E August 5 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.19 | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 ≈29x vs 指數 ≈25.6x，溢價壓縮 | Magnificent 7 valuation premium lowest decade 2026 | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026 （SSGA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA TP $285→$288，EPS-driven（主導成分：EPS 上修） | Morgan Stanley NVDA target 288 July 2026 AI demand | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044 （Investing.com） | 2026-07-13 | 2026-08-06T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS ≈855bp、$2.6B 貸款利差 +125bp、Oracle CDS ≈215bp | CoreWeave CDS spread blows out 125 covenants Oracle August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm （Tech Times） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 總報酬 +14.26% vs SPY +13.71% | RSP vs SPY equal weight total return YTD August 2026 | https://www.financecharts.com/etfs/SPY/performance/total-return （FinanceCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 ≈41% | S&P 500 top 10 concentration percent record 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/ （Pensions & Investments） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| breadth.advance_decline | ≈64% 成分股在 50DMA 上、A/D 線創高、McClellan 轉負 | S&P 500 breadth percent above 50 day moving average August 2026 McClellan | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/ （StockCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed ≈58（Greed） | CNN Fear and Greed Index August 5 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives，原定 FINRA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| retail.aaii | AAII Bear 42.1%／Neutral 26.9%／Bull 31.0% | AAII investor sentiment survey July 30 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| retail.social_sentiment | WSB「Save Wendy's」（WEN）軋空、空頭部位 ≈44% | Reddit WSB Wendy's WEN short squeeze August 2026 | https://finance.yahoo.com/markets/stocks/articles/reddit-wants-save-wendy-inside-161925726.html （Yahoo Finance） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.treasury_auctions | 5Y 連 14 次 tail、bid-to-cover 為 2022-09 以來最差；7Y tail 0.8bp | US Treasury 5 year 7 year auction tail bid to cover July 2026 | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026 （TFTC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| monetary.fedwatch | FOMC 7/29 鷹派持平；CME FedWatch 9 月 ≈62%，定價分歧 | CME FedWatch September 2026 probability FOMC hold | https://growbeansprout.com/tools/fedwatch （Beansprout，原定 CME FedWatch） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.pboc | 人行 7/24 MLF 淨投放 ¥100B（逆回購 ¥2.1T 數字因日期矛盾不採用） | PBoC reverse repo injection 2.1 trillion yuan late July 2026 | https://www.investing.com/news/economy-news/chinas-pboc-to-conduct-overnight-reverse-repos-inject-a-total-of-21-trillion-yuan-4810853 （Investing.com） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計 ≈$725B 續上修；Alphabet Q2 上修觸發賣壓 | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO ≈$678B，≈32% 繫於單一客戶（OpenAI） | Microsoft RPO backlog 678 billion single customer OpenAI 2026 | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/ （Benzinga via TradingView） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| ai.compute_supply_demand | HBM/DRAM 合約價續升、H200 租金 ≈$4.39/hr、缺口延至 1H2027 | H200 GPU rental price HBM DRAM contract 2026 shortage 2027 | https://jarvislabs.ai/blog/h200-price （Jarvislabs） | 2026-08-01 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超越 FCF、2026 發債 ≈$182B、表外融資 >$120B | hyperscaler capex FCF debt issuance 182 billion off balance sheet SPV 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure （Sage Advisory） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.revenue_capex_gap | AI 終端年化營收 ≈$72B（Anthropic $47B＋OpenAI $25B，2026-06-15）vs capex ≈$725B（CNBC 2026-07-28，hyperscaler 合計） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI）；https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-06-15 | 2026-08-06T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收投機 IPO，合格件數 0 | AI rename ticker SPAC no revenue IPO July 30 August 6 2026 | Reuters／Benzinga／BusinessWire SPAC 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.ipo_heat | 本週 ≈21 檔跨週定價、無 blowout 首日、YTD ≈$251B／86 檔 | US IPO pricings week August 3 2026 Renaissance | https://www.renaissancecapital.com/IPO-Center/Pricings （Renaissance Capital） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot 合格件數 0 | microcap 100% single day quantum fusion space nuclear small cap August 2026 | Finviz／StockAnalysis／StockTitan gainers 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 ≈$1T IPO、Anthropic 續進 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground （Benzinga） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內具 filing-level 細節的合格 Form 4 件數 0（候選缺 filing date／個別 filing URL） | Snowflake Dageville Tempus Lefkofsky Form 4 insider sale July 2026 SEC | SEC EDGAR Form 4 公司列表（sec.gov browse-edgar） | — | 2026-08-06T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.55（日讀數） | Cboe equity put call ratio August 3 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio （YCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高 ≈$198B | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing，原定 etf.com） | 2026-07-23 | 2026-08-06T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x 單股槓桿 ETF＋ELOL（TSLA+SpaceX）發行（檢索摘要另列 2026-07-30） | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-07 | 2026-08-06T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量 ≈65% | 0DTE SPX options share volume Cboe Q2 2026 65% | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641 （Investing.com，原定 Cboe） | 2026-05-31 | 2026-08-06T09:30:00+08:00 |
| structural.options_volume | OCC 總量（2026-06 月資料）16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW ≈139.96、VIX ≈16.9 contango、TLT 1M skew 創 GFC 以來高 | VIX SKEW term structure bond volatility August 3 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher （Cboe） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt（2026-06 月資料）$1.502T、+51.5% YoY（交叉檢核，不重複計算） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B Anthropic 掛鉤貸款 07-29 調高收益率；Nebius $775M 擔保融資 07-17 | CoreWeave 2.6 billion loan Anthropic yield boosted July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic （Bloomberg） | 2026-07-29 | 2026-08-06T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-06",
  "iso_week": "2026-W32",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-04",
  "prior_date": "2026-08-03",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 3.83,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

> [DRY RUN] this report was not committed to archive.

# 2026-11-08 AI 泡沫破裂預測報告
報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：report-2026-10-18（21天前）

## 結論

**結論：no**

三條路徑都已出現壓力，但沒有一條在 182 天內完成的可能性高於不完成：R1 的 NASDAQ-100 距 52 週高點回撤 13.56%，還要再跌約 13.23% 才達 25% 門檻（`valuation.ndx_drawdown`）；R2 目前四家中僅 Microsoft 一家小幅下修 capex（`ai.hyperscaler_capex`）；R3 的 CoreWeave CDS 雖已破 1,289 bps（`valuation.ai_credit_schism`），但並無付款違約或 distressed exchange，而 HY OAS 3.48%、repo 資金壓力（SOFR−IORB）僅 2 bps，顯示廣義信用與資金市場並未傳導（`monetary.hy_oas`、`monetary.repo_stress_srf`）。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 26,989.99（2026-11-06），252 交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 13.56%；R1 門檻水位 23,418.52，自最新收盤再跌約 13.23% 即觸發（`valuation.ndx_drawdown`）。這段回撤集中在一個月內：高點 2026-10-06 之後，指數在 2026-11-05 收在 26,629.81，2026-11-06 反彈至 26,989.99。同期 S&P 500 自前次基準日下跌 3.99%（7,353.73，2026-11-05），但仍高於 200 日均線 0.42%、高於 52 週均線 1.84%（`valuation.sp500_trend`）。VIX 在 7 日內由 17.2 升至 28.18（+63.84%），S&P 500 同窗口下跌 4.75%，屬正常的「股跌波動升」，非 crowded-optionality 式同漲（comove=false，`structural.vix_spx_comove`）。Cboe SKEW 149.37、隱含相關性創高 20.93（`structural.cross_asset_derivatives`），股票選擇權賣買權比升至 1.05（`speculation.equity_put_call`），顯示避險需求已大幅升溫。

**判讀：** R1 已經在進行中、走到約一半，不再是遙遠的情境；但剩下的 13.23% 需要新的催化劑。窗口內最可能的推力是：Fed 在 12 月升息（FedWatch 76.8%）把回撤延長成緊縮性空頭、R3 信用事件實際落地，或 2027 年 1–2 月財報季出現第二家 capex 下修。三者都尚未發生，因此 R1 目前未達「可能性高於不可能」的程度。

### R2 資本支出收縮

- Microsoft：2026 年 capex 指引由約 $175bn 下修至約 $170bn（2026-10-29，最近一次季報），方向：**下修**（`ai.hyperscaler_capex`）。
- Alphabet：本次檢索沒有取得其最新正式指引，方向不可判。
- Amazon：本次檢索沒有取得其最新正式指引，方向不可判。
- Meta：本次檢索沒有取得其最新正式指引，方向不可判。

目前四家中已有 1 家下修，R2 需要 2 家。本次證據不含各家下次財報的具體日期；依季報節奏，窗口（至 2027-05-09）會涵蓋兩輪 hyperscaler 季報（約 2027 年 1–2 月與 4 月），也就是 R2 有兩次觸發機會。需求端仍在擴張：Anthropic 上半年營收 16.3（`ai.openai_anthropic_revenue`），Oracle RPO 638（`ai.customer_concentration_rpo`）。融資端，hyperscaler 今年以來發債 296、10/29 起一週內有 5 筆 AI 相關債券合計 67（`ai.hyperscaler_financing_mix`），代表 capex 越來越倚賴舉債而非 FCF。

**判讀：** Microsoft 的下修幅度約 3%，偏向「調整節奏」而非撤退；其餘三家沒有下修證據。只要窗口內再有一家下修，R2 就成立；在 R1 回撤延長或發債成本上升的情況下，下一輪季報出現第二家下修的風險不低，但目前證據不足以判定為「較可能發生」。

### R3 AI 信用事件

AI 算力主業借款人中，CoreWeave 的信用定價已進入 distressed 區間：債券殖利率升破 16%（2026-11-06），五年期 CDS 突破 1,289 bps（2026-11-05），且是在 NASDAQ 反彈的同時走闊（`valuation.ai_credit_schism`）。依 AI 信用定價分歧（equity-vs-credit schism）的讀法，這是信用端先重定價、股權端後跟的後期訊號。CoreWeave 普遍被視為 R3 候選，但本次證據沒有載明其負債金額與近期到期結構，是否達 ≥ 50 億美元門檻需要另行確認。放款端，ING 正出售 12 筆資料中心貸款，規模約 500（2026-11-06，`structural.ai_infrastructure_debt`），顯示銀行在降低 AI infrastructure debt financing 曝險。本次證據中沒有任何破產申請、超過寬限期的付款違約、covenant waiver、distressed exchange 或 going-concern 文字。廣義信用並未傳導：HY OAS 3.48%（較前次 +17 bps，`monetary.hy_oas`）、IG OAS 0.93%（`monetary.ig_oas`）。

**判讀：** R3 是三條路徑中市場定價最偏向事件的一條，但定價不等於違約。以 1,289 bps 的 CDS 粗估，半年內違約的市場隱含風險仍明顯低於一半。若窗口內出現再融資失敗、債權人協商（distressed exchange）或大客戶合約取消，R3 會直接成立，並可能帶動 R1。

## 支持 yes 的證據

- [R1] NASDAQ-100 自 2026-10-06 高點 31,224.69 一個月內跌到 26,989.99（2026-11-06），距 52 週高點回撤 13.56%；同期 VIX 7 日內由 17.2 升至 28.18（+63.84%），R1 已走到門檻的一半以上（`valuation.ndx_drawdown`、`structural.vix_spx_comove`）。
- [R3] CoreWeave 債券殖利率升破 16%（2026-11-06）、五年期 CDS 突破 1,289 bps（2026-11-05），且在 NASDAQ 反彈時仍走闊，信用端已先於股權端重定價（`valuation.ai_credit_schism`）。
- [R2] Microsoft 於 2026-10-29 把 2026 年 capex 指引由約 $175bn 下修至約 $170bn，是 R2 所需兩家中的第一家（`ai.hyperscaler_capex`）。
- [整體] Fed 緩衝空間受限：FedWatch 顯示 12 月升息 25 bps 機率 76.8%（2026-11-06），CPI 年增 3.72%（2026-09），WTI 99.64（2026-11-03），回撤期間難以期待降息托底（`monetary.fedwatch`、`monetary.cpi_yoy`、`monetary.wti`）。
- [R3] hyperscaler 融資結構（capex vs FCF / 發債）轉向舉債：今年以來發債 296，10/29 起一週 5 筆 AI 相關債券合計 67（2026-11-06）；同日 ING 出售 12 筆資料中心貸款，規模約 500（`ai.hyperscaler_financing_mix`、`structural.ai_infrastructure_debt`）。
- [整體] 估值與集中度仍處極端水位，下跌空間大：Shiller CAPE 38.91、S&P 500 trailing P/E 25.14（2026-11-06），Mag 7 前瞻本益比約 28.3，前十大成分股權重約 37.9%（`valuation.sp500_pe_cape`、`valuation.mag7_multiples`、`breadth.top10_concentration`）。
- [整體] 大型 AI 股權供給即將湧入：Anthropic 已遞交 S-1，目標估值 1.5 兆至 2 兆（2026-10-26），可能吸走 AI 類股資金（`speculation.upcoming_ai_ipos`）。

## 支持 no 的證據

- [R1] R1 門檻水位 23,418.52，NASDAQ-100 還需自 26,989.99 再跌約 13.23%；S&P 500 仍高於 200 日均線 0.42%（7,353.73，2026-11-05），指數在 2026-11-06 已自 26,629.81 反彈（`valuation.ndx_drawdown`、`valuation.sp500_trend`）。
- [R3] 廣義信用與資金市場沒有傳導：HY OAS 3.48%、IG OAS 0.93%（2026-11-05），SOFR−IORB 2 bps、SOFR99−IORB 10 bps、SRF 動用 0（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`）；MOVE 由 101.1 降至 92.77（2026-11-06）（`structural.treasury_basis_trade`）。
- [R3] AI 信用壓力仍是定價而非事件，且集中在單一發行人：本次證據沒有破產申請、付款違約或 distressed exchange；ING 出售貸款屬於曝險轉移，不是違約（`valuation.ai_credit_schism`、`structural.ai_infrastructure_debt`）。
- [R2] 四家中僅 1 家下修，幅度約 3%；需求端仍在成長：Anthropic 上半年營收 16.3、OpenAI 與 Anthropic 年化營收合計約 135，Oracle RPO 638，H100 隨選租金中位數 3.87（`ai.hyperscaler_capex`、`ai.openai_anthropic_revenue`、`ai.revenue_capex_gap`、`ai.customer_concentration_rpo`、`ai.compute_supply_demand`）。
- [整體] 情緒已經洗出：CNN Fear & Greed 22（極度恐懼，2026-11-06）、AAII 看空 48.4% 對看多 34.1%（2026-11-04），已非典型頂部的狂熱；10Y 殖利率自前次下降 25 bps 至 4.84%，金融條件在放鬆（`retail.fear_greed`、`retail.aaii`、`monetary.dgs10`）。
- [整體] 投機熱度降溫：本週唯一定價的 IPO 是社區銀行（週漲 8%），microcap 主題暴漲掃描 0 件合格（`speculation.ipo_heat`、`speculation.microcap_moonshots`）。

## 與前期比較

前次結論：無前次預測（report-2026-10-18 為舊格式評分報告）

舊格式評分不轉換成 yes/no，本次結論僅依當前證據與基準率。自 2026-10-18 以來的重要變化：

- NASDAQ-100 由 2026-10-16 的 29,187.55 跌到 26,989.99，S&P 500 自前次基準日下跌 3.99%（`valuation.ndx_drawdown`、`valuation.sp500_trend`）。
- 10Y 殖利率下降 25 bps（DFII10 −14 bps，T10YIE −12 bps；兩者窗口不一致，driver 判讀：不可判（視窗不一致））（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。
- HY OAS 走闊 17 bps、IG OAS 走闊 8 bps，幅度溫和（`monetary.hy_oas`、`monetary.ig_oas`）。
- Microsoft capex 下修（2026-10-29）與 CoreWeave CDS 破 1,289 bps（2026-11-05）是本次新增的路徑證據（`ai.hyperscaler_capex`、`valuation.ai_credit_schism`）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

成功完成檢索、但沒有合格披露（✗ NOT DISCLOSED）的來源：`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.treasury_auctions`、`monetary.private_credit_liquidity`、`ai.token_growth`、`ai.depreciation_life`、`ai.capital_cycle`（quarterly_state 無可用增速披露；event_scan 有找到微軟 10 月取消 Nscale 英國資料中心交易、規模約 3，並收緊 neocloud 專案監督，但因組件聚合為 all，整列不可當成證據引用）、`structural.global_leveraged_approvals`。其中私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）與美債標售需求（auction tail / bid-to-cover）的缺漏最可能影響 R3／R1 判讀：若其實存在 gate proration / breach 或連續標售 tail，會加強 yes 方向；但本次檢索確實沒有發現，因此不改變結論。

資料一致性說明：
- harness 的 evidence.md 寫明 `structural.treasury_basis_trade` 的三個 script 區塊 fetch_failed，並附 MOVE WebSearch 備援值 93.88（2026-11-04）。但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 三塊都是 status ok，因此依 prompt 規則以 artifact 為主（✓ API，MOVE 92.77，2026-11-06），沒有使用該 WebSearch 值。
- Microsoft capex 結果 URL 的 slug 提到「190b capex」，與抓取內文的「約 175 → 約 170」不一致，且沒有釐清是曆年還是財年口徑。這項下修是 R2 唯一已發生的一家，若其實是財年口徑的上修，R2 就會退回 0/4，結論更偏 no。
- Alphabet、Amazon、Meta 的最新 capex 指引本次沒有取得；若其中任何一家其實已下修，R2 就已成立（2/4），會直接翻轉成 yes。這是本次最大的資料缺口。
- CoreWeave 的負債規模與到期牆不在本次證據中，因此無法確認它是否符合 R3 的 ≥ 50 億美元門檻，也無法判斷再融資時點。

最大的三個不確定性：
1. 12 月 FOMC：若照 FedWatch 76.8% 升息，在 CPI 3.72%、WTI 約 99.64 的背景下，回撤延長成 R1 的機會上升（推向 yes）；若按兵不動或轉鴿，偏向 no。
2. 2027 年 1–2 月 hyperscaler 季報：只要再有一家下修 capex，R2 就成立（推向 yes）；維持或上修則偏向 no。
3. CoreWeave 等 AI 算力借款人的再融資：CDS 1,289 bps 代表市場已計入重大違約風險；若出現 distressed exchange，R3 成立並可能連動 R1（推向 yes）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7353.73 | FRED API (series_id=SP500) via scripts/fetch_macro.py sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 0.42 | FRED API (series_id=SP500) via scripts/fetch_macro.py sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 1.84 | FRED API (series_id=SP500) via scripts/fetch_macro.py sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（自前次基準 %） | -3.99 | FRED API (series_id=SP500) via scripts/fetch_macro.py sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 26989.99 | FRED API (series_id=NASDAQ100) via scripts/fetch_macro.py ndx_drawdown | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) via scripts/fetch_macro.py ndx_drawdown | 2026-10-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 13.56 | FRED API (series_id=NASDAQ100) via scripts/fetch_macro.py ndx_drawdown | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API (series_id=NASDAQ100) via scripts/fetch_macro.py ndx_drawdown | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026-Q2 季資料，家庭股票配置 %） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 4.0 | FRED API (series_id=DFEDTARU) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.75 | FRED API (series_id=DFEDTARL) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 3.48 | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（IG OAS %） | 0.93 | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（10Y 殖利率 %） | 4.84 | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（自前次基準） | -25.0 | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（10Y 實質殖利率 %） | 2.6 | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps（自前次基準） | -14.0 | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（10Y breakeven %） | 2.23 | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps（自前次基準） | -12.0 | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（WTI 美元/桶） | 99.64 | FRED API (series_id=DCOILWTICO) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料，CPI 年增 %） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（5y5y forward %） | 2.17 | FRED API (series_id=T5YIFR) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（10Y 期限溢價（term premium），Kim-Wright %） | 0.9089 | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.92 | FRED API (series_id=SOFR) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 4.0 | FRED API (series_id=SOFR99) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.9 | FRED API (series_id=IORB) | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest（Fed 資產負債表） | 6,748,145（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（ECB 資產負債表） | 5,945,410（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（BOJ 資產負債表，no_new_obs） | 6,261,882（¥626.19T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest（VIX 收盤） | 28.18 | FRED API (series_id=VIXCLS) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of；base_date 2026-10-29，window_days 7，comove=false） | 28.18 | FRED API (SP500 shared-date pair) via scripts/fetch_macro.py vix_spx_comove | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日 VIX 變動 %） | 63.84 | FRED API (SP500 shared-date pair) via scripts/fetch_macro.py vix_spx_comove | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（同窗口 S&P 500 變動 %） | -4.75 | FRED API (SP500 shared-date pair) via scripts/fetch_macro.py vix_spx_comove | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（銀行對 NBFI 放款） | 2111.0042（$2.11T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（槓桿基金美債期貨淨部位，口） | -7,249,305 | CFTC TFF via scripts/fetch_macro.py cftc_lev_funds | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（4 週變動，口） | -489,473 | CFTC TFF via scripts/fetch_macro.py cftc_lev_funds | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（MOVE） | 92.77 | Yahoo chart ^MOVE via scripts/fetch_macro.py move_index | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2326.9 | OFR STFM via scripts/fetch_macro.py ofr_repo | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebFetch | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch（Mag 7 前瞻 P/E；AI leader P/S vs 10 年均值未取得） | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季；EPS／PE 拆解未披露） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（月頻 stock-of-state，沿用 2026-09） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | scripts/fetch_macro.py（DFEDTARU ok、DFEDTARL ok） | ✓ API |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok；repo_stress status ok） | ✓ API |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state；僅取得 Microsoft） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch（quarterly_state stock-of-state＋event_scan 30d） | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch（stock-of-state 組合） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch（quarterly_state stock-of-state＋event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（Renaissance Capital 週報） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（7d movers 掃描） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com feed 掃描（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d，KRX／TWSE／JPX／ESMA／ETFGI） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe 月報） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS ok＋vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（交叉檢核，不重複計入） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok；aggregation any） | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻本益比約 28.3 | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ （Vested Finance；原定來源 FactSet／Bloomberg 摘要） | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein 將 TSMC 目標價由 554 上調至 600（EPS／PE 拆解未披露） | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/ （StockAnalysis；原定來源 Bloomberg／Reuters／cnyes） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html （CNBC） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 五年期 CDS 突破 1289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds （Coinpaper） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | 等權指數（RSP）年初至今報酬約 14.13% | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY （Total Real Returns） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大成分股權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration （Chartrow） | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | 紐交所上漲 1,474 對下跌 1,252 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ （McClellan） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 22（極度恐懼） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ （Finhacker；原定來源 cnn.com/markets/fear-and-greed） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 1.48 兆美元、年增約 31.4% | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt （原定來源 FINRA） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives （AAII） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔 | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week （Benzinga） | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | 12 月升息 25 bps 機率 76.8% | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ （24/7 Wall St.；原定來源 CME FedWatch） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000 | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee （BigGo Finance） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年 capex 指引自約 175 下調至約 170 | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex （Global Data Center Hub） | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3 | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html （Yahoo Finance） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle 剩餘履約義務（RPO）638 | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ （Motley Fool） | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87 | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends （GetDeploying） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 今年以來發債 296 | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era （404K Research，引 Goldman） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 10/29 起一週內 5 筆 AI 相關債券發行合計 67 | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era （404K Research，引 Goldman） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic 65＋OpenAI 約 70，合計約 135；分母僅 Microsoft capex 指引約 170 | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html （Yahoo Finance） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] 微軟 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 （Investing.com，引 Bloomberg） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics 完成 SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ （Securities.io） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO（社區銀行）週漲 8% | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears （Renaissance Capital） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描：0 件符合 2＋主題×弱基本面 | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 （Built In） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描：0 件合格 | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe 股票選擇權賣買權比升至 1.05（單日讀數） | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide （Seeking Alpha；原定來源 Cboe） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭基金 10 月底規模 24.31、當月淨流入 7.27 | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html （Yahoo Finance；原定來源 etf.com／ETFGI） | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 （Cboe via PR Newswire） | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 2026-09 月總結算量 1,486,062,415 口 | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report （OCC） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性創高 20.93 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 （Saxo） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-09 月資料）交叉檢核基數約 1.48 兆美元 | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt （原定來源 FINRA） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
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

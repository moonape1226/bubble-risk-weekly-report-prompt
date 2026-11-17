> [DRY RUN] this report was not committed to archive.

# 2026-11-08 AI 泡沫破裂預測報告

報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：report-2026-10-18（21天前）

## 結論

**結論：no**

R1 已走到一半（NASDAQ-100 距 52 週高點回撤 13.56%），R3 的 CoreWeave 信用定價也已進入困境區間，但壓力尚未傳導到整體信用與資金市場：HY OAS 僅 3.48%、SOFR−IORB 僅 2.0 bps、SRF 動用為 0，hyperscaler 一週內仍能發行約 670 億美元 AI 相關債券。R2 在窗口內的下修家數仍是 0（Microsoft 10-29 的下修早於窗口起點）。三條路徑都在動，但沒有一條已具備在 182 天內「較可能完成」的證據，依 base rate 與 yes 的舉證責任，結論為 no。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 26,989.99（2026-11-06），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 13.56%。R1 門檻水位為 23,418.52，自最新收盤還需再跌約 13.23% 才會觸及（`valuation.ndx_drawdown`）。跌勢集中在一個月內：2026-10-16 收盤 29,187.55，11-05 曾收在 26,629.81，11-06 小幅反彈。由於高點在 2026-10-06，整個窗口內 252 日高點不會往下移，門檻將固定在 23,418.52 附近。

同期 S&P 500 為 7,353.73（2026-11-05），自前次基準以來跌 3.99%，仍高於 200 日均線 0.42%（`valuation.sp500_trend`）。VIX 升到 28.18；trailing 7 日窗口（2026-10-29 → 2026-11-05）內 VIX 漲 63.84%、S&P 500 跌 4.75%，屬一般 risk-off，而非指數上漲時 VIX 也同步上漲的 crowded-optionality 型態（`structural.vix_spx_comove`）。選擇權市場的尾部避險需求偏高：SKEW 149.37、隱含相關性創高 20.93（2026-11-06，`structural.cross_asset_derivatives`）。

**判讀：** R1 已走完約一半的距離，是三條路徑中最接近解析的一條。若要在窗口內觸及門檻，需要再出現一個像 10 月那樣的下跌段：例如 Fed 在 12 月真的升息、AI 信用事件傳導到 hyperscaler 股價，或 leveraged ETF／尾部選擇權部位被迫平倉。不過，散戶情緒已在恐懼區、整體信用利差仍窄、長端利率回落，這些條件不支持把「再跌 13%」視為基本情境。

### R2 資本支出收縮

- Microsoft：2026-10-29 財報將 2026 年 capex 指引自約 1,750 億美元下調至約 1,700 億美元，屬**下修**（`ai.hyperscaler_capex`）。但這次下修發生在窗口起點 2026-11-08 之前，不計入本次窗口的 R2 計數。另外，該來源 URL 標題寫的是「Q3 FY2026 ... 190B capex」，與摘要數字和季度不一致，數值出處有疑義（詳見資料缺漏）。
- Alphabet：本次證據未取得最新正式指引，方向無法判定。
- Amazon：本次證據未取得最新正式指引，方向無法判定。
- Meta：本次證據未取得最新正式指引，方向無法判定。

窗口內已下修家數：0／4（窗口外：Microsoft 1 家）。具體下次財報日期本次未取得；依季度財報節奏，窗口（至 2027-05-09）可涵蓋兩個財報季。融資面上，hyperscaler 今年以來發債約 2,960 億美元，10/29 起一週內 5 筆 AI 相關債券合計約 670 億美元（`ai.hyperscaler_financing_mix`），代表 capex 越來越倚賴舉債。需求面上，Anthropic 年化營收約 650 億美元、OpenAI 約 700 億美元，合計約 1,350 億美元（`ai.revenue_capex_gap`）。

**判讀：** Microsoft 的小幅下修（約 3%）證明 R2 的方向已出現，但窗口內需要兩家「新的」下修。在發債市場仍暢通、終端 AI 營收仍在擴大的情況下，hyperscaler 縮手的誘因有限。若下一個財報季有兩家把 capex 指引下調（較可能的觸發點是融資成本隨 Fed 升息上升，或 R1 下跌壓縮估值），R2 才會成立。

### R3 AI 信用事件

AI 基礎設施借款人中，CoreWeave 的信用定價最緊張：債券殖利率升破 16%（2026-11-06），五年期 CDS 突破 1,289 bps（2026-11-05）（`valuation.ai_credit_schism`）。這是股權仍隱含高成長、信用端卻已開始重定價的典型 AI 信用定價分歧（equity-vs-credit schism）後期訊號。CoreWeave 是否符合 R3 的負債 ≥ 50 億美元門檻，以及近期到期與再融資時程，本次證據未直接揭露。本次證據中也沒有任何借款人出現付款違約、covenant waiver、distressed exchange 或 going-concern 語句。

在 AI infrastructure debt financing / vendor-financing loops 這條線上，ING 出售 12 筆資料中心貸款，規模約 500（2026-11-06；擷取片段未載明單位，`structural.ai_infrastructure_debt`），顯示銀行端正在降低資料中心曝險。整體信用市場仍平靜：HY OAS 3.48%、IG OAS 0.93%（2026-11-05，`monetary.hy_oas`、`monetary.ig_oas`），repo 資金壓力（SOFR−IORB）2.0 bps，SRF 動用（Standing Repo Facility usage）為 0（`monetary.repo_stress_srf`）。

**判讀：** 1,000 bps 以上的 CDS 代表市場已為 CoreWeave 計入相當高的違約風險，但 R3 要求的是實際破產、超過寬限期的違約或完成 distressed exchange，而一家能取得新資金的發行人通常能撐過 182 天。能把 R3 推過門檻的，會是再融資失敗、主要客戶合約取消（例如 Microsoft 收緊 neocloud 合作）或私募信貸撤出。目前整體信用與資金市場仍開放，R3 在窗口內完成的證據不足。

## 支持 yes 的證據

- [R1] NASDAQ-100 2026-11-06 收盤 26,989.99，距 52 週高點回撤 13.56%，一個月內自 31,224.69（2026-10-06）跌下，距 R1 門檻 23,418.52 僅需再跌約 13.23%；VIX 28.18（2026-11-05）代表的波動幅度足以在 182 天內覆蓋這段距離（`valuation.ndx_drawdown`、`structural.vix_spx_comove`）。
- [R3] CoreWeave 債券殖利率升破 16%（2026-11-06）、五年期 CDS 突破 1,289 bps（2026-11-05），AI 基礎設施信用已進入困境定價，信用端先於股權重定價（`valuation.ai_credit_schism`）。
- [整體] 12 月升息 25 bps 的 FedWatch 隱含機率為 76.8%（2026-11-06），CPI YoY 3.72%（2026-09 月資料），Fed 沒有空間為 AI 主導的下跌提供緩衝，反而可能收緊融資條件（`monetary.fedwatch`、`monetary.cpi_yoy`）。
- [R2] Microsoft 已於 2026-10-29 將 2026 年 capex 指引自約 1,750 億美元下調至約 1,700 億美元，四大 hyperscaler 中已有一家轉向，方向訊號出現（`ai.hyperscaler_capex`）。
- [R3] ING 出售 12 筆資料中心貸款（2026-11-06），顯示銀行正在減少 AI 資料中心授信曝險，可能壓縮高槓桿借款人的再融資管道（`structural.ai_infrastructure_debt`）。
- [整體] hyperscaler 今年以來發債約 2,960 億美元、10/29 起一週內 AI 相關債券約 670 億美元（2026-11-06），capex 越來越依賴舉債，信用條件一旦收緊會直接傳導到 R2（`ai.hyperscaler_financing_mix`）。
- [R1] 估值與集中度放大下跌空間：Shiller CAPE 38.91、trailing P/E 25.14（2026-11-06）、前十大權重約 37.9%（2026-11-01）；SKEW 149.37、隱含相關性創高 20.93（2026-11-06）（`valuation.sp500_pe_cape`、`breadth.top10_concentration`、`structural.cross_asset_derivatives`）。
- [R1] 半導體 3 倍多頭 ETF 10 月底規模 24.31、當月淨流入 7.27（2026-10-31），融資餘額約 1.48 兆美元、YoY 約 31.4%（2026-09 月資料），一旦續跌，槓桿部位可能被迫去化（`structural.leveraged_etf_aum`、`retail.margin_debt`）。

## 支持 no 的證據

- [R3] 整體信用沒有跟著 AI 信用重定價：HY OAS 3.48%（2026-11-05，較 10-16 僅 +17 bps）、IG OAS 0.93%（+8 bps），仍屬歷史上偏窄的水準（`monetary.hy_oas`、`monetary.ig_oas`）。
- [R3] 資金市場沒有失序：SOFR−IORB 2.0 bps、SOFR99−IORB 10.0 bps（2026-11-05），SRF 動用 0.0（2026-11-06），MOVE 92.77（較 10-16 降 8.33），OFR tri-party repo 成交量 2,326.9 億美元（2026-11-06）正常（`monetary.repo_stress_srf`、`structural.treasury_basis_trade`）。
- [R2] 窗口內 R2 計數為 0：Microsoft 的下修發生於 2026-10-29（窗口前），幅度僅約 3%，且來源數值有疑義；本次沒有任何其他 hyperscaler 下修的證據（`ai.hyperscaler_capex`）。
- [R3] AI 資本市場大門仍開：10/29 起一週內 5 筆 AI 相關債券合計約 670 億美元（2026-11-06），Anthropic 遞交 S-1、目標估值 1.5 兆至 2 兆美元（2026-10-26），資金仍在流入，讓 R3 所需的再融資失敗較難在 182 天內發生（`ai.hyperscaler_financing_mix`、`speculation.upcoming_ai_ipos`）。
- [R2] 終端需求仍在擴張：Anthropic 年化營收約 650 億美元加 OpenAI 約 700 億美元，合計約 1,350 億美元（2026-09-30），Anthropic 上半年營收 163 億美元（2026-10-26）；H100 隨選租金中位數 3.87 美元（2026-11-03），沒有崩價訊號（`ai.revenue_capex_gap`、`ai.openai_anthropic_revenue`、`ai.compute_supply_demand`）。
- [R1] 情緒已經洗盤：CNN Fear & Greed 22 處於極度恐懼（2026-11-06），AAII 看空 48.4%、看多 34.1%（2026-11-04），Cboe 股票選擇權賣買權比 1.05（2026-11-05），這類讀數過去多出現在修正中後段，而非新一波下跌的起點（`retail.fear_greed`、`retail.aaii`、`speculation.equity_put_call`）。
- [整體] 折現率與油價壓力在減輕：10Y 殖利率 4.84%（較 10-16 降 25.0 bps）、10Y 實質殖利率 2.6%（降 14.0 bps），WTI 99.64（2026-11-03，降 7.92%）（`monetary.dgs10`、`monetary.dfii10`、`monetary.wti`）。
- [R1] 廣度沒有崩壞：S&P 500 仍高於 200 日均線 0.42%（2026-11-05），NYSE 上漲 1,474 家、下跌 1,252 家（2026-11-06），等權指數年初至今約 +14.13%（`valuation.sp500_trend`、`breadth.advance_decline`、`breadth.rsp_spy`）。

## 與前期比較

前次結論：無前次預測（report-2026-10-18 為舊格式評分報告）

前次為舊格式評分報告，其分數不轉譯為 yes/no，flip_evidence 為空陣列。自 2026-10-18 以來的主要變化：

- NASDAQ-100 自 29,187.55（2026-10-16）跌至 26,989.99（2026-11-06），S&P 500 跌 3.99%，VIX 自 19.99 升至 28.18（`valuation.ndx_drawdown`、`valuation.sp500_trend`、`structural.vix_spx_comove`）。
- CoreWeave 信用定價惡化到 CDS 超過 1,000 bps、債券殖利率超過 16%（`valuation.ai_credit_schism`）。
- HY OAS 走闊 17 bps、IG OAS 走闊 8 bps，幅度溫和（`monetary.hy_oas`、`monetary.ig_oas`）。
- 10Y 殖利率降 25.0 bps，但 FedWatch 隱含 12 月升息，政策方向偏緊（`monetary.dgs10`、`monetary.fedwatch`）。
- Microsoft 下修 2026 年 capex 指引（窗口前事件）（`ai.hyperscaler_capex`）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED（搜尋完成但無窗內披露）：retail.naaim、institutional.bofa_jpm_survey、monetary.treasury_auctions、monetary.private_credit_liquidity、ai.token_growth、ai.depreciation_life、ai.capital_cycle（quarterly_state 無披露；event_scan 有 Microsoft 取消 Nscale 英國資料中心交易一事，但依 all 聚合規則整體列為 NOT DISCLOSED，不作為正文證據）、structural.global_leveraged_approvals。其中可能影響答案的是私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）：若有大型 BDC 出現 gate proration / breach，會直接削弱 R3 的 no 論據；美債標售需求（auction tail / bid-to-cover）缺漏則使財政面壓力無法交叉確認。其餘缺漏屬確認性訊號，不太可能單獨改變答案。

資料一致性注意：

- case/evidence.md 記載美債基差交易槓桿（Treasury basis-trade leverage）的 script 三區塊 fetch_failed、改走 WebSearch（MOVE 93.88，2026-11-04）；但 macro artifact 顯示 cftc_lev_funds、move_index、ofr_repo 皆為 status ok。本報告依 artifact 記為 ✓ API，採用 MOVE 92.77（2026-11-06），搜尋值不使用。
- ai.hyperscaler_capex 只取得 Microsoft 的指引，Alphabet、Amazon、Meta 的最新指引缺漏；Microsoft 數值來源的 URL 標題（Q3 FY2026、190B capex）與摘要（2026 年約 175 → 約 170）不一致。由於窗口內 R2 計數只看 2026-11-08 之後的新下修，這個缺漏不改變目前的 R2 計數，但會影響「方向已轉」這個判斷的力道。
- CoreWeave CDS 的來源 URL 寫的是「top 1,000 bps」，摘要寫的是「1289」；兩者都代表 1,000 bps 以上的困境區間，不影響判讀。ING 資料中心貸款「約 500」未載明單位。
- retail.margin_debt 的融資餘額／市值比本次無市值分母，只報水位與 YoY。

最大不確定性：

1. 12 月 FOMC 是否升息（FedWatch 76.8%）：若升息並伴隨長端利率回升，會同時推動 R1（估值壓縮）與 R3（再融資成本上升），把答案推向 yes。
2. CoreWeave 的再融資與到期結構：本次未取得負債規模與到期時程。若顯示 2027 年上半年前有大額到期且無法展延，R3 的距離會明顯縮短，推向 yes。
3. 下一個 hyperscaler 財報季的 capex 指引：只要有兩家下修，R2 即成立；若各家維持或上修，則同時削弱 R1 的基本面敘事，推向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7353.73 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 0.42 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 1.84 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較前次基準 %） | -3.99 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 26989.99 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 13.56 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（家計股票配置 %，2026Q2） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 4.0 | FRED API (series_id=DFEDTARU) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.75 | FRED API (series_id=DFEDTARL) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 3.48 | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 17.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.93 | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM delta_bps | 8.0 | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.84 | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | -25.0 | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.6 | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | -14.0 | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.23 | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps（視窗與 DGS10/DFII10 不一致，driver 不可判） | -12.0 | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（美元／桶） | 99.64 | FRED API (series_id=DCOILWTICO) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO chg_pct | -7.92 | FRED API (series_id=DCOILWTICO) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.17 | FRED API (series_id=T5YIFR) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR delta_bps | -16.0 | FRED API (series_id=T5YIFR) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 0.9089 | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 日） | -2.7 | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.92 | FRED API (series_id=SOFR) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 4.0 | FRED API (series_id=SOFR99) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.9 | FRED API (series_id=IORB) | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps（SOFR−IORB，IORB 取 2026-11-05） | 2.0 | FRED API (series_id=SOFR, IORB) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr99_iorb_bps（SOFR99−IORB，IORB 取 2026-11-05） | 10.0 | FRED API (series_id=SOFR99, IORB) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,748,145（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,945,410（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（no_new_obs，持平） | 6,261,882（¥626.19T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED API (series_id=VIXCLS) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（comove=false，base 2026-10-29，window 7 日） | 28.18 | FRED API (series_id=SP500 paired) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 63.84 | FRED API (series_id=SP500 paired) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -4.75 | FRED API (series_id=SP500 paired) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2111.0042（$2.11T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7249305 | CFTC TFF futures-only | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -489473 | CFTC TFF futures-only | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party 成交量） | 2326.9 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebFetch | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | fetch_macro.py sp500_trend 區塊（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown 區塊（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED（無當週值） |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✗ NOT DISCLOSED（無新一期調查） |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | fetch_macro.py（FRED） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | fetch_macro.py（FRED BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | fetch_macro.py（FRED BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | fetch_macro.py（FRED DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | fetch_macro.py（FRED DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | fetch_macro.py（FRED T10YIE 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | fetch_macro.py（FRED DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | fetch_macro.py（FRED CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | fetch_macro.py（FRED T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | fetch_macro.py（FRED THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series | fetch_macro.py repo_stress 區塊 | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch（14d） | ✗ NOT DISCLOSED（窗內無顯著標售結果） |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | fetch_macro.py（FRED WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | fetch_macro.py（FRED ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無合格披露） |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（季頻 stock-of-state） | ✓ SEARCH-VERIFIED（僅取得 Microsoft） |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch：quarterly_state stock-of-state＋event_scan 30d | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch（季頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動（depreciation useful-life change） | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch：quarterly_state stock-of-state＋event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED（1 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe 月報） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | fetch_macro.py（FRED VIXCLS＋vix_spx_comove 區塊） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py cftc_lev_funds／move_index／ofr_repo（any） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻本益比約 28.3（原定來源：Mag 7 weighted P/E） | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein TSM 目標價 554 → 600；EPS／目標 PE 拆解未披露 | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/ | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 五年期 CDS 突破 1,289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | 等權指數（RSP）年初至今報酬約 14.13% | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | 前十大成分股權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 1,474 家對下跌 1,252 家 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 22（極度恐懼；原定來源 cnn.com） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | 融資餘額約 1.48 兆美元、YoY 約 31.4%（2026-09 月資料） | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔 | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | 12 月升息 25 bps 隱含機率 76.8% | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000 | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年 capex 指引約 175 → 約 170（十億美元，下修）；Alphabet／Amazon／Meta 未取得 | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3（十億美元） | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle RPO 638（十億美元）；同一 counterparty 跨供應商承諾加總未披露 | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87 美元／小時 | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 今年以來發債 296（十億美元） | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 10/29 起一週內 5 筆 AI 相關債券發行合計 67（十億美元） | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic 65＋OpenAI 約 70，合計約 135（十億美元）；分母僅 Microsoft capex 約 170 可用 | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] Microsoft 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics 完成 SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO 週漲 8% | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描：0 件符合 2+ 主題×弱基本面 | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆美元 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描：0 件合格 | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe 股票選擇權賣買權比升至 1.05（日讀數） | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭基金 10 月底規模 24.31、當月淨流入 7.27（十億美元） | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 9 月總結算量 1,486,062,415 口（2026-09 月資料） | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性創高 20.93 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.margin_debt_crosscheck | 融資餘額交叉檢核基數約 1.48 兆美元（2026-09 月資料；市值比未計算） | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.ai_infrastructure_debt | ING 出售 12 筆資料中心貸款，規模約 500（單位未載明） | AI data center debt financing private credit November 2026 | https://www.cnbc.com/2026/11/06/ing-ai-data-center-loans-debt.html | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

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

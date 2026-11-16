> [DRY RUN] this report was not committed to archive.

# 2026-11-08 AI 泡沫破裂預測報告
報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：report-2026-10-18（21天前）

## 結論

**結論：no**

三條路徑都已進入壓力區，但本次證據顯示沒有任何一條在窗口內已接近完成：R1 仍需自最新收盤再跌 13.23% 才觸線；R2 目前僅 Microsoft 一家小幅下修（約 175 → 約 170），尚缺第二家；R3 雖有 CoreWeave CDS 1289 bps、債券殖利率破 16% 的劇烈定價，但尚無付款違約、破產或 distressed exchange，且廣義信用（HY OAS 3.48%、repo 利差 2 bps）仍未失序。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 26,989.99（2026-11-06），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 13.56%；R1 門檻水位 23,418.52，需自最新收盤再下跌約 13.23% 才觸及（`valuation.ndx_drawdown`）。回撤是在一個月內形成：2026-10-16 收盤仍為 29,187.55，2026-11-05 一度收在 26,629.81，2026-11-06 反彈。同期 S&P 500 為 7,353.73（2026-11-05），只高於 200 日均線 0.42%、較 2026-10-16 下跌 3.99%（`valuation.sp500_trend`）；VIX 由 17.2（2026-10-29）跳升至 28.18（2026-11-05），屬股跌波動升的正常反向關係，非 crowded-optionality 共振（`structural.vix_spx_comove`）。情緒端已轉為恐懼：CNN Fear & Greed 22（極度恐懼，2026-11-06，`retail.fear_greed`），AAII 看空 48.4% 對看多 34.1%（2026-11-04，`retail.aaii`），Cboe 股票賣買權比升至 1.05（2026-11-05，`speculation.equity_put_call`）。估值仍高：Shiller CAPE 38.91、trailing P/E 25.14（2026-11-06，`valuation.sp500_pe_cape`），Mag 7 前瞻本益比約 28.3（`valuation.mag7_multiples`）。貨幣面可緩衝空間有限：CME FedWatch 顯示 12 月升息 25 bps 機率 76.8%（2026-11-06，`monetary.fedwatch`），CPI YoY 3.72%（2026-09 月資料，`monetary.cpi_yoy`），聯邦基金目標區間 3.75%–4.00%（`monetary.fed_funds`）。

**判讀：** 已走完觸線所需跌幅的一半略多。窗口內推過門檻需要第二波 13% 以上下跌，可能觸發點為 12 月 FOMC 實際升息、2027 年 1–2 月 hyperscaler 季報再出現 capex 下修（R2 連動），或 R3 信用事件外溢；目前極度恐懼與高賣買權比也意味著短期部位已部分清洗，單靠情緒延續不足以完成剩餘跌幅。

### R2 資本支出收縮

- Microsoft：2026 年資本支出指引自約 175 下修至約 170（約 −2.9%，2026-10-29 季報，`ai.hyperscaler_capex`）——方向：下修。
- Alphabet：本次檢索未取得最新指引數值與方向。
- Amazon：本次檢索未取得最新指引數值與方向。
- Meta：本次檢索未取得最新指引數值與方向。

目前四家中已確認下修 1 家（Microsoft），R2 需要第二家。下一輪季報依季度節奏落在 2027 年 1 月下旬至 2 月初，以及 2027 年 4 月下旬，兩輪都在窗口內；確切日期本次未取得。需求側仍有支撐：Anthropic 已遞交 S-1、目標估值 1.5 兆至 2 兆（2026-10-26，`speculation.upcoming_ai_ipos`），Anthropic 上半年營收 16.3（`ai.openai_anthropic_revenue`），年化 AI 終端營收 Anthropic 65＋OpenAI 約 70，合計約 135（`ai.revenue_capex_gap`；本次分母僅取得 Microsoft 一家約 170，無法組出 top-4＋Oracle 的完整缺口）。H100 隨選租金中位數 3.87（2026-11-03，`ai.compute_supply_demand`），本次未見利用率下滑或訂單消化的配對證據。Oracle 剩餘履約義務 638（`ai.customer_concentration_rpo`）顯示承諾仍集中於少數 AI 客戶。

**判讀：** 路徑已啟動但進度是一半，且 Microsoft 的下修幅度很小（約 3%），比較像節奏調整而非收縮。推過門檻需要 Alphabet、Amazon、Meta 任一家在 2027 年 1–2 月或 4 月季報中下修當年度或次年度指引；本次缺三家的指引數據，是判斷 R2 最大的資料缺口。

### R3 AI 信用事件

最接近 R3 的借款人是 CoreWeave：其五年期 CDS 突破 1289 bps（2026-11-05），債券殖利率升破 16%（2026-11-06）（`valuation.ai_credit_schism`）。這是典型的 AI 信用定價分歧（equity-vs-credit schism）後期讀數：信貸端已大幅重定價，而 NASDAQ-100 同期出現反彈。AI infrastructure debt financing / vendor-financing loops 方面，荷蘭國際集團（ING）出售 12 筆資料中心貸款，規模約 500（摘要未標單位，2026-11-06，`structural.ai_infrastructure_debt`），顯示銀行正在減持 AI 資料中心曝險。廣義信用尚未跟進：HY OAS 3.48%（較前次基準 +17 bps）、IG OAS 0.93%（+8 bps）（`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）僅 2 bps、SOFR99 對 IORB 為 10 bps、SRF 動用（Standing Repo Facility usage）為 0（`monetary.repo_stress_srf`）；銀行對 NBFI 放款 $2.11T，兩週增 0.27%（`structural.nbfi_bank_loans`）。本次證據未載明 CoreWeave 的負債規模、近期到期牆或任何付款違約、契約豁免、going-concern 用語，因此其是否符合 R3 的 ≥ 50 億美元門檻本次無法用證據確認。

**判讀：** 市場已替 AI 算力借款人定價出高違約風險，但 R3 要求的是實際事件（破產、逾寬限期違約或完成 distressed exchange），本次無任何此類訊號。推過門檻的情境是：CoreWeave 類借款人在高殖利率下無法再融資、被迫進行 distressed exchange，或 ING 式的銀行減持擴大成融資中斷；此路徑也最可能透過信用外溢觸發 R1。

## 支持 yes 的證據

- [R3] CoreWeave 五年期 CDS 突破 1289 bps（2026-11-05），債券殖利率升破 16%（2026-11-06），是 AI 算力借款人信用已進入困境定價的直接證據，且與股價反彈背離（`valuation.ai_credit_schism`）。
- [R2] Microsoft 於 2026-10-29 季報將 2026 年資本支出指引自約 175 下修至約 170，四家已有一家符合 R2 的下修定義，窗口內還有兩輪季報（`ai.hyperscaler_capex`）。
- [R1] NASDAQ-100 一個月內自 31,224.69（2026-10-06）跌至 26,989.99（2026-11-06），距 52 週高點回撤 13.56%；VIX 同期由 17.2 升至 28.18（`valuation.ndx_drawdown`、`structural.vix_spx_comove`）。
- [整體] 政策緩衝受限：12 月升息 25 bps 機率 76.8%（2026-11-06），CPI YoY 3.72%（2026-09），WTI 99.64（2026-11-03）——Fed 在 AI 主導的下跌中降息托底的空間偏小（`monetary.fedwatch`、`monetary.cpi_yoy`、`monetary.wti`）。
- [R3] ING 出售 12 筆資料中心貸款（規模約 500，2026-11-06），銀行開始減持 AI 資料中心曝險，增加高槓桿借款人的再融資難度（`structural.ai_infrastructure_debt`）。
- [R1] 估值仍處高檔：Shiller CAPE 38.91、trailing P/E 25.14（2026-11-06），Mag 7 前瞻本益比約 28.3，若盈利或 capex 預期轉弱，下行空間大（`valuation.sp500_pe_cape`、`valuation.mag7_multiples`）。

## 支持 no 的證據

- [整體] 基準率：三個條件在任意 182 天窗口內都不常見；目前沒有一條路徑已完成，R1 尚需再跌 13.23%（門檻 23,418.52），R2 尚缺第二家下修（`valuation.ndx_drawdown`、`ai.hyperscaler_capex`）。
- [R3] 廣義信用與資金市場未失序：HY OAS 3.48%、IG OAS 0.93%（2026-11-05），SOFR−IORB 2 bps、SRF 動用 0（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`）——CoreWeave 的壓力目前仍是個別名稱，未擴散成系統性融資中斷。
- [R2] AI 需求與資本市場對 AI 的融資意願仍在：Anthropic 遞交 S-1、目標估值 1.5 兆至 2 兆（2026-10-26），年化 AI 終端營收約 135（Anthropic 65＋OpenAI 約 70），H100 租金中位數 3.87（2026-11-03）未見崩落（`speculation.upcoming_ai_ipos`、`ai.revenue_capex_gap`、`ai.compute_supply_demand`）。
- [R2] Microsoft 的下修幅度僅約 3%（約 175 → 約 170），仍是極高水位的 capex，不構成收縮趨勢的強證據（`ai.hyperscaler_capex`）。
- [R1] 部位已部分清洗：CNN Fear & Greed 22（極度恐懼）、AAII 看空 48.4%、股票賣買權比 1.05，屬逆向指標上的超賣區；同時半導體 3 倍多頭基金 10 月淨流入 7.27，顯示逢低買盤仍在（`retail.fear_greed`、`retail.aaii`、`speculation.equity_put_call`、`structural.leveraged_etf_aum`）。
- [整體] 美債市場未現失序：MOVE 92.77（2026-11-06，較 2026-10-16 的 101.1 回落），10Y 殖利率 4.84% 較前次基準下降 25 bps（`structural.treasury_basis_trade`、`monetary.dgs10`）。

## 與前期比較

前次結論：無前次預測（report-2026-10-18 為舊格式評分報告）

前次為舊格式評分報告，其分數不轉換為 yes/no，flip_evidence 為空。自 2026-10-18 以來的主要變化（僅作摘要）：

- NASDAQ-100 由 29,187.55（2026-10-16）降至 26,989.99（2026-11-06），S&P 500 同期 −3.99%（`valuation.ndx_drawdown`、`valuation.sp500_trend`）。
- VIX 由 19.99 升至 28.18；MOVE 由 101.1 降至 92.77——股市波動升、債市波動降（`structural.vix_spx_comove`、`structural.treasury_basis_trade`）。
- HY OAS +17 bps 至 3.48%，IG OAS +8 bps 至 0.93%（`monetary.hy_oas`、`monetary.ig_oas`）。
- 10Y 殖利率 −25 bps 至 4.84%，DFII10 −14 bps，T10YIE −12 bps；因 T10YIE 視窗與 DGS10/DFII10 不一致，分解判讀：不可判（視窗不一致）（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。
- 美債基差交易槓桿（Treasury basis-trade leverage）：槓桿基金美債期貨淨空單擴大至 -7,249,305 口（2026-11-03），4 週變動 -489,473 口（`structural.treasury_basis_trade`）。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `valuation.analyst_tp_decomposition`（⛔ FETCH FAILED，搜尋技術失敗）：屬估值敘事的輔助證據，不直接決定 R1–R3 任一條件，不太可能改變結論。
- `ai.hyperscaler_financing_mix`（⛔ FETCH FAILED，quarterly_state 與 event_scan 均技術失敗）：缺少 hyperscaler 融資結構（capex vs FCF / 發債）與近 30 日 SPV／發債事件，使 R2／R3 之間的融資傳導無法確認；若 hyperscaler 已大幅轉向舉債或表外 SPV，會增加 R3 與 R2 的可能性，此缺口有可能改變判讀，是本次第二大資料缺口。

其他非成功來源（✗ NOT DISCLOSED）：NAAIM、BofA/JPM 調查、美債標售、私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）、token 成長、折舊年限變動、全球槓桿產品核准，皆為檢索完成但窗口內無合格披露。`ai.capital_cycle` 的 event_scan 找到 Microsoft 10 月取消 Nscale 英國資料中心交易（規模約 3，2026-11-04 報導），但 quarterly_state 無可組合的增速證據，依 component_aggregation: all 標為 ✗ NOT DISCLOSED，不作為主證據；該事件方向上與 R2 下修一致（資本週期階段可能轉折）。

另：證據檔記載美債基差交易槓桿三區塊 fetch_failed 並以 WebSearch 取得 MOVE 93.88（2026-11-04），但本次 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 皆為 status ok；依決策分支以 artifact 為準（✓ API，MOVE 92.77），搜尋值未採用。

最大不確定性：

1. Alphabet、Amazon、Meta 的最新 capex 指引本次未取得：若其中任一家已於 10 月底季報下修，R2 即已成立，答案會翻為 yes——這是本次最可能改變結論的缺口。
2. CoreWeave 的債務規模、到期牆與再融資進度：CDS 1289 bps 已反映高違約風險；若出現 distressed exchange 或逾寬限期違約，R3 直接成立並可能拖動 R1，推向 yes。
3. 12 月 FOMC：若如 FedWatch 所示升息，會壓低估值並加速 R1；若通膨回落使 Fed 轉鴿，則推向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7353.73 | FRED API (series_id=SP500)；sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線偏離 %） | 0.42 | FRED API (series_id=SP500)；sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線偏離 %） | 1.84 | FRED API (series_id=SP500)；sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較前次基準 %） | -3.99 | FRED API (series_id=SP500)；sp500_trend | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 26989.99 | FRED API (series_id=NASDAQ100)；ndx_drawdown | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100)；ndx_drawdown | 2026-10-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 13.56 | FRED API (series_id=NASDAQ100)；ndx_drawdown | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API (series_id=NASDAQ100)；ndx_drawdown | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q2 家庭股票配置 %） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 4.0 | FRED API (series_id=DFEDTARU) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.75 | FRED API (series_id=DFEDTARL) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 3.48 | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.93 | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.84 | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（較前次基準） | -25.0 | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.6 | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.23 | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl） | 99.64 | FRED API (series_id=DCOILWTICO) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料，%） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.17 | FRED API (series_id=T5YIFR) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright 10Y 期限溢價 %） | 0.9089 | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.92 | FRED API (series_id=SOFR) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 4.0 | FRED API (series_id=SOFR99) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.9 | FRED API (series_id=IORB) | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（隔夜 repo 操作 transaction volume，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,748,145（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,945,410（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,261,882（¥626.19T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED API (series_id=VIXCLS) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of；base_date 2026-10-29，comove=false） | 28.18 | FRED API；vix_spx_comove | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日 %） | 63.84 | FRED API；vix_spx_comove | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日 %） | -4.75 | FRED API；vix_spx_comove | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（十億美元） | 2,111.0042（$2.11T） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六檔美債期貨槓桿基金淨部位，口） | -7,249,305 | CFTC TFF；cftc_lev_funds | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -489,473 | CFTC TFF；cftc_lev_funds | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo chart API (^MOVE)；move_index | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（三方 repo transaction volume，十億美元） | 2326.9 | OFR STFM REPO-TRIV1_TV_TOT-P；ofr_repo | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebFetch（direct） | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch [primary: SEARCH]，90d＋同季 | ⛔ FETCH FAILED（搜尋技術失敗，無結果） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch，7d | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch [primary: SEARCH] | ✗ NOT DISCLOSED（檢索完成，無當週值） |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED（檢索完成，無新調查） |
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
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch [primary: SEARCH]，14d | ✗ NOT DISCLOSED（檢索完成，窗口內無顯著標售結果） |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch [primary: SEARCH]，30d | ✗ NOT DISCLOSED（檢索完成，30 日內無合格披露） |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED（僅取得 Microsoft） |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch [primary: SEARCH]；quarterly_state stock_of_state＋event_scan 30d；兩組件搜尋皆技術失敗 | ⛔ FETCH FAILED components=quarterly_state:fetch_failed,event_scan:fetch_failed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch [primary: SEARCH]（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch [primary: SEARCH]，30d | ✗ NOT DISCLOSED（30 日內無變動披露） |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch [primary: SEARCH]；quarterly_state 無可組合增速證據，event_scan 30d 有結果 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch，7d | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch，7d | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch [primary: SEARCH]，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch，30d | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR Form 4，14d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com feed，30d | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch，7d | ✗ NOT DISCLOSED（7 日內無英文披露） |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe 月報） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（交叉檢核） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch [primary: SEARCH]，30d | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo；artifact 三區塊皆 ok，未採用 WebSearch fallback 值） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻本益比約 28.3 | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ （Vested Finance） | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html （CNBC） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 五年期 CDS 突破 1289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds （Coinpaper） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | 等權指數（RSP）年初至今報酬約 14.13% | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY （Total Real Returns） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大成分股權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration （Chartrow） | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 1,474 家對下跌 1,252 家 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ （McClellan） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 22（極度恐懼） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ （FinHacker；原定來源 cnn.com） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 1.48 兆美元、年增約 31.4% | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt （原定來源 FINRA） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives （AAII） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔（TSLA、AMD、MU 等） | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week （Benzinga） | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | 12 月升息 25 bps 機率 76.8% | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ （24/7 Wall St.；原定來源 CME FedWatch） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000 | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee （BigGo Finance） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年資本支出指引自約 175 下修至約 170（Q3 季報） | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex （Global Data Center Hub） | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3 | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html （Yahoo Finance） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle 剩餘履約義務（RPO）638 | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ （Motley Fool） | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87 | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends （GetDeploying） | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic 65＋OpenAI 約 70，合計約 135 | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html （Yahoo Finance） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] Microsoft 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 （Investing.com／Bloomberg News） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics 完成 SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ （Securities.io） | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO 週漲 8 | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears （Renaissance Capital） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描：0 件符合（2＋主題×弱基本面） | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 （Built In） | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描：0 件合格 | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表（窗內無具名申報人／交易日／金額等 filing-level 細節） | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe 股票選擇權賣買權比升至 1.05（S&P 500 下跌 4.4% 期間） | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide （Seeking Alpha） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭基金 10 月底規模 24.31、當月淨流入 7.27 | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html （Yahoo Finance） | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 （Cboe 新聞稿） | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 2026-09 月總結算量 1,486,062,415 口 | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report （OCC） | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、Cboe SKEW 149.37、隱含相關性 20.93（創高） | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 （Saxo） | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
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
  "r1_drawdown_pct": 13.56,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

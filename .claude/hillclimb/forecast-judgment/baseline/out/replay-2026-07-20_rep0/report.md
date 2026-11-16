> [DRY RUN] this report was not committed to archive.

# 2026-07-20 AI 泡沫破裂預測報告

報告日期：2026-07-20｜ISO 週次：2026-W30｜預測窗口：2026-07-20 → 2027-01-18｜前次基準：report-2026-07-16（4天前）

## 結論

**結論：no**

三條路徑目前都未接近觸發：NASDAQ-100 距 52 週高點回撤 6.74%，還需再跌約 19.58% 才達 R1 門檻（`valuation.ndx_drawdown`）；最近一次 hyperscaler capex 指引仍在上修、合計約 $700B（`ai.hyperscaler_capex`）。最強的 yes 側訊號是 Oracle／CoreWeave CDS 走闊（`valuation.ai_credit_schism`），但整體 HY OAS 2.71% 仍窄（`monetary.hy_oas`），尚不足以讓 182 天內 R3 違約或 distressed exchange 成為較可能的結果。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 28,592.66（2026-07-17），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 6.74%；R1 門檻水位為 22,995.45，自最新收盤須再下跌約 19.58% 才觸及（`valuation.ndx_drawdown`）。相較前次基準日 2026-07-16 收盤 29,025.77，指數下跌約 1.49%；2026-07-17 NYSE 下跌家數約為上漲家數 2 倍、新高 241／新低 166，當日報導主軸是晶片股賣壓擴大（`breadth.advance_decline`）。波動率同步上升：VIX 由 2026-07-10 的 15.03 升至 2026-07-17 的 18.77（+24.88%），同期 S&P 500 −1.55%，屬一般的跌價避險、非「漲勢中搶避險」的 co-movement 警戒（`structural.vix_spx_comove`）。S&P 500 仍高於 200 日均線 6.73%、52 週均線 8.42%（`valuation.sp500_trend`），估值面 CAPE 41.52、trailing P/E 32.08（`valuation.sp500_pe_cape`），代表一旦下跌空間大，但目前價格趨勢尚未破壞。

**判讀：** R1 距門檻仍遠（需再跌約 19.58%）。要在窗口內觸發，需要一個把晶片股修正擴大為全面去槓桿的催化劑，例如 hyperscaler 財報下修 capex（連動 R2）、AI 信用事件外溢（連動 R3），或保證金與槓桿 ETF 部位被迫平倉；目前證據顯示的是修正初期，而非失序。

### R2 資本支出收縮

本次取得的最近一次正式指引為 2026-05-15 彙整的 hyperscaler 2026 年 capex 合計約 $700B，且方向仍為上修（`ai.hyperscaler_capex`）。檢索結果是合計口徑，未逐家列出 Microsoft、Alphabet、Amazon、Meta 各自的指引金額；依該來源的方向敘述，四家在最近一季（2026 Q1 財報）皆為上修或維持、未見下修，故目前已下修家數為 0／4。各家下一次財報日期本次證據未取得；依季報節奏，至 2027-01-18 的窗口應涵蓋兩輪季報，是 R2 唯一可能的觸發時點。需求面佐證仍偏強：伺服器 DRAM 3Q26 合約價預估季增 13–18%（`ai.compute_supply_demand`），未見訂單消化或利用率轉弱的披露。AI 營收對 capex 缺口（revenue-to-capex gap）仍大：年化 capex 約 $700B（分母：hyperscaler 合計，來源彙總口徑；Oracle 與 neocloud 本次無可組合的當期披露、未納入）對 AI 終端營收僅數百億美元等級（2026-05-15 組合值，`ai.revenue_capex_gap`），但這是沿用值，不是新證據。

**判讀：** R2 目前離觸發最遠——0 家下修，且最新方向仍為上修。要在窗口內觸發，需要至少兩家在接下來兩輪季報中正式下修指引，通常要先出現 R1 式的股價重挫或 AI 營收不及預期迫使管理層轉向；本次證據沒有任何一家釋出轉向訊號。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）出現走闊：截至 2026-07-16，Oracle 5 年期 CDS 約 198bp（創紀錄），CoreWeave 約 665bp（`valuation.ai_credit_schism`）。CoreWeave 屬可能符合 R3 規模門檻（AI 資料中心／算力為主業、負債 ≥ 50 億美元）的借款人類型；Oracle 雖有大額 AI 資料中心負債，但主業並非算力出租，未必落入 R3 定義。本次證據未含兩者的負債到期表、評等動作或付款違約、covenant waiver、going-concern 等困境訊號；過去 30 天也沒有新的 AI infrastructure debt financing / vendor-financing loops 披露可供檢視再融資壓力。整體信用市場平靜：HY OAS 2.71%、IG OAS 0.78%（2026-07-16，`monetary.hy_oas`、`monetary.ig_oas`），repo 資金壓力（SOFR−IORB）為 −3bp、SRF 動用（Standing Repo Facility usage）為 0（`monetary.repo_stress_srf`）。旁側壓力在私募信貸：Blue Owl OCIC 2026 Q2 redemption-request ratio 18.8%，以 5% quarterly redemption cap 比例撥付，屬 gate proration / breach，但同一報導也指出贖回壓力略為緩和（2026-07-02，`monetary.private_credit_liquidity`）。

**判讀：** R3 是三條路徑中最接近的一條：CoreWeave 約 665bp 的 CDS 已是高收益偏困境水位，但 R3 需要實際的破產、逾寬限期違約或 distressed exchange，而目前沒有任何付款困難或重組的披露，整體利差與 repo 也未見傳染。要在窗口內觸發，需要大型 AI 算力借款人再融資受阻（融資市場關門或主要客戶承諾縮減）；若發生，會透過 R1 股價重挫連動放大。

## 支持 yes 的證據

- [R3] Oracle 5 年期 CDS 約 198bp（創紀錄）、CoreWeave 約 665bp（2026-07-16），信用端先於股權端重定價，是 AI 信用定價分歧轉向後期訊號的跡象（`valuation.ai_credit_schism`）。
- [R1] 晶片股賣壓擴大：2026-07-17 NYSE 下跌約為上漲 2 倍（`breadth.advance_decline`），NASDAQ-100 自 2026-06-02 高點 30,660.60 回落至 28,592.66（`valuation.ndx_drawdown`），VIX 一週升 24.88% 至 18.77（`structural.vix_spx_comove`）。
- [整體] 槓桿與擁擠部位處於極端：FINRA margin debt $1.416T、YoY +53.7%（2026-05 月資料，歷史上 YoY ≥ +40–50% 多見於頂部附近，`retail.margin_debt`）；NAAIM 曝險 95.64（2026-07-15，`retail.naaim`）；US 槓桿 ETF AUM 約 $198B（2026-07-10，`structural.leveraged_etf_aum`）——若 R1 啟動，強制去槓桿會放大跌幅。
- [整體] 估值脆弱度高：Shiller CAPE 41.52、trailing P/E 32.08（2026-07-17，`valuation.sp500_pe_cape`），Mag 7 加權 trailing P/E 約 40（2026-05-15，`valuation.mag7_multiples`）。
- [R3] 私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）：Blue Owl OCIC 2026 Q2 redemption-request ratio 18.8%，觸發 quarterly redemption cap 下的 gate proration / breach（2026-07-02，`monetary.private_credit_liquidity`），顯示非銀行融資管道的流動性承壓。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）懸殊：年化 capex 約 $700B 對 AI 終端營收僅數百億美元等級（2026-05-15 沿用值，分母：hyperscaler 合計，`ai.revenue_capex_gap`），若營收落後持續，是未來指引轉向的根源。

## 支持 no 的證據

- [整體] 基準率與距離：R1 須在現水位再跌約 19.58% 才達 22,995.45 門檻，目前距 52 週高點回撤 6.74%（`valuation.ndx_drawdown`）；三條路徑皆無已在進行中的觸發事件。
- [R2] 最近一次 hyperscaler capex 指引合計約 $700B 且仍上修（2026-05-15，`ai.hyperscaler_capex`），四家中 0 家下修；需求面伺服器 DRAM 3Q26 合約價預估季增 13–18%（2026-07-03，`ai.compute_supply_demand`）。
- [R3] 整體信用與資金市場平靜：HY OAS 2.71%、IG OAS 0.78%（2026-07-16，`monetary.hy_oas`、`monetary.ig_oas`），SOFR−IORB −3bp、SRF 動用為 0（`monetary.repo_stress_srf`），MOVE 70.88（2026-07-17，`structural.treasury_basis_trade`），沒有傳染跡象。
- [R3] AI 資本市場仍開放：Anthropic 以約 $965B 估值進行 IPO 投資人會議、可能 10 月掛牌（2026-07-15，`speculation.upcoming_ai_ipos`）；2026 年迄今約 200 檔 IPO、募資 $141.2B（2026-07-16，`speculation.ipo_heat`）——融資管道暢通降低窗口內大型 AI 借款人違約的可能。
- [整體] 情緒已降溫而非亢奮：CNN Fear & Greed 37（Fear，2026-07-17，`retail.fear_greed`），Cboe equity put/call 0.73（2026-07-17，`speculation.equity_put_call`），等權 RSP 年初至今 +10.68% 勝過 SPY +7.47%（2026-06-10，`breadth.rsp_spy`），漲勢廣度並未只靠少數權值股。
- [整體] 政策面有緩衝空間：Fed funds 目標區間 3.50%–3.75%（`monetary.fed_funds`），CME FedWatch 7/29 會議持平約 86.7%（2026-07-18，`monetary.fedwatch`）；CPI YoY 3.46%（2026-06，`monetary.cpi_yoy`）限制降息力道，但不構成緊縮衝擊。

## 與前期比較

前次結論：無前次預測（report-2026-07-16 為舊格式評分報告）

前次為舊格式評分報告，不轉換為 yes／no；flip_evidence 為空。自 2026-07-16 以來的主要變化：

- NASDAQ-100 由 29,025.77 降至 28,592.66（2026-07-17，約 −1.49%），S&P 500 由 7,533.77 降至 7,457.69（−1.01%），晶片股賣壓為主因。
- VIX 由 16.73 升至 18.77，MOVE 由 68.16 升至 70.88；10Y breakeven 升 2bp、5y5y 升 1bp。DGS10、DFII10 與 HY／IG OAS 本次無新觀測（持平），10Y Δ 分解判讀為不可判（視窗不一致）。
- 新增的信用面證據為 Oracle／CoreWeave CDS 走闊（2026-07-16），但尚無違約或重組事件，未改變 R3 的路徑判斷。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `structural.zero_dte`（必要）：檢索只取得 2026-02-28 的 Cboe 0DTE 佔 SPX 約 63% 的舊值，沒有當期快照，因此不作為證據。0DTE 只是投機結構的佐證，缺口不會改變結論。
- `speculation.insider_form4`（必要）：SEC EDGAR 無法連線，取不到一手 Form 4 URL；必要的 EDGAR 路徑在技術上失敗，所以不能算作 `0 件` 的成功篩選。內部人賣股屬情緒訊號、不是解析條件，缺口不會改變結論。

其他說明：

- `structural.treasury_basis_trade` 的檢索紀錄寫腳本三塊（cftc_lev_funds、move_index、ofr_repo）皆失敗，但 macro artifact 顯示三塊都是 `status: ok`，資料日期都在 14 天窗口內。本報告以 artifact 為準、記為 ✓ API。
- ✗ NOT DISCLOSED（檢索已完成但無合格當期披露）：analyst TP decomposition、social sentiment、BofA／JPM survey、token growth、OpenAI／Anthropic 年化營收（最近披露 2026-05-15 不在本季）、customer concentration／RPO、hyperscaler 融資結構兩組件、折舊年限變動、資本週期階段兩組件、global leveraged approvals、AI infrastructure debt financing。其中 AI infrastructure debt financing 與 hyperscaler 融資結構的缺口與 R3 直接相關：若有未被檢索到的大型再融資困難，可能低估 R3。

最大的不確定性：

1. **下一輪 hyperscaler 季報（窗口內第一輪）**：若有兩家下修 capex 指引即直接觸發 R2，並可能帶動 R1；若持續上修，no 的判斷會更穩固。
2. **CoreWeave 等 AI 算力借款人的再融資**：CDS 約 665bp 代表市場已在為違約風險定價；若出現 covenant waiver、distressed exchange 或主要客戶承諾縮減，答案會往 yes 移動。
3. **晶片股修正是否擴大**：目前距 52 週高點回撤 6.74%；在 margin debt YoY +53.7% 與高槓桿 ETF 部位下，若跌勢加速，強制去槓桿可能讓 R1 比基準率更快接近。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7457.69 | FRED API（series_id=SP500） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 6.73 | FRED API（series_id=SP500） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.42 | FRED API（series_id=SP500） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（NASDAQ-100 最新收盤） | 28592.66 | FRED API（series_id=NASDAQ100） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API（series_id=NASDAQ100） | 2026-06-02 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 6.74 | FRED API（series_id=NASDAQ100） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API（series_id=NASDAQ100） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1 家庭股票配置 %） | 45.76080873390133（約 45.76%） | FRED API（series_id=BOGZ1FL153064486Q） | 2026-01-01 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API（series_id=DFEDTARU） | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API（series_id=DFEDTARL） | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 2.71 | FRED API（series_id=BAMLH0A0HYM2） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（IG OAS %） | 0.78 | FRED API（series_id=BAMLC0A0CM） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（10Y 殖利率 %，無新觀測、Δ 0bp） | 4.57 | FRED API（series_id=DGS10） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（10Y 實質殖利率 %，無新觀測、Δ 0bp） | 2.35 | FRED API（series_id=DFII10） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（10Y breakeven %） | 2.24 | FRED API（series_id=T10YIE） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps（相對 2026-07-16） | 2.0 | FRED API（series_id=T10YIE） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（WTI 美元/桶） | 79.2 | FRED API（series_id=DCOILWTICO） | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料，CPI YoY %） | 3.46 | FRED API（series_id=CPIAUCSL） | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（5y5y forward %） | 2.21 | FRED API（series_id=T5YIFR） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（10Y 期限溢價（term premium），Kim-Wright %） | 0.7788 | FRED API（series_id=THREEFYTP10） | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（序列自身 trailing 約 7 日） | 4.7 | FRED API（series_id=THREEFYTP10） | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API（series_id=SOFR） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API（series_id=SOFR99） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API（series_id=IORB） | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用 transaction volume，十億美元） | 0.0 | FRED API（series_id=RPONTTLD） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps（as_of 與 iorb_date 皆 2026-07-16） | -3.0 | FRED-derived repo_stress block（scripts/fetch_macro.py） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr99_iorb_bps（sofr99_date 與 sofr99_iorb_date 皆 2026-07-16） | 5.0 | FRED-derived repo_stress block（scripts/fetch_macro.py） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.walcl | WALCL latest（Fed 資產負債表） | 6743028.0（$6.74T，百萬美元） | FRED API（series_id=WALCL） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（ECB 資產負債表） | 5970516.0（€5.97T，百萬歐元） | FRED API（series_id=ECBASSETSW） | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（BOJ 資產負債表） | 6395509.0（¥639.55T，億日圓） | FRED API（series_id=JPNASSETS） | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 18.77 | FRED API（series_id=VIXCLS） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（base_date 2026-07-10，window_days 7） | 18.77 | FRED-derived vix_spx_comove block（scripts/fetch_macro.py） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（comove=false） | 24.88 | FRED-derived vix_spx_comove block（scripts/fetch_macro.py） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -1.55 | FRED-derived vix_spx_comove block（scripts/fetch_macro.py） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（銀行對 NBFI 放款） | 2004.0237（$2.00T，十億美元） | FRED API（series_id=LNFACBW027SBOG） | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六檔 UST 期貨槓桿基金淨部位，口） | -7562874 | CFTC TFF futures-only | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -78139 | CFTC TFF futures-only | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（MOVE） | 70.88 | Yahoo Finance chart API（^MOVE，非官方） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2342.6 | OFR Short-term Funding Monitor（REPO-TRIV1_TV_TOT-P） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com，WebSearch primary | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | MarketXLS 估值儀表板，WebSearch | ✓ SEARCH-VERIFIED（最新一版為 2026-05-15） |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報摘要，WebSearch（90d 且同季） | ✗ NOT DISCLOSED（本季無合格 TP 上調披露） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導，WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | ahasignals，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth 報導，WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com（MacroMicro 鏡像），WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA via Advisor Perspectives，WebSearch（月頻沿用） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com，WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag，WebSearch（7d） | ✗ NOT DISCLOSED（無顯著討論） |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | ycharts，WebSearch primary | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查摘要，WebSearch | ✗ NOT DISCLOSED（本次無新調查） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（DFEDTARU ok；DFEDTARL ok） | ✓ API |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） | ✓ API |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | 標售 recap，WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要，WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW ok；JPNASSETS ok） | ✓ API |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Bloomberg，WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露報導，WebSearch（30d） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報彙整，WebSearch（季頻沿用 2026 Q1） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露，WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／The Information，WebSearch | ✗ NOT DISCLOSED（最近披露 2026-05-15，非本季） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話會議，WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce，WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報 quarterly_state 與 30d event_scan，WebSearch；兩組件皆完成檢索、無合格披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露，WebSearch（季頻沿用） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K／10-Q，WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速 quarterly_state 與 30d 進出場 event_scan，WebSearch；兩組件皆完成檢索、無合格披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis，WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／Benzinga／StockTitan movers，WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導，WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR primary（egress 受限）＋ openinsider 搜尋 | ⛔ FETCH FAILED（EDGAR 無法取得一手 Form 4 URL） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe daily statistics，WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing 彙整，WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF.com，WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA，WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe，WebSearch | ⛔ FETCH FAILED（僅取得 2026-02-28 舊值，無當期快照） |
| structural.options_volume | 結構｜Options total volume: OCC monthly | theocc.com，WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe／AInvest，WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS ok；vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 retail.margin_debt，WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds ok；move_index ok；ofr_repo ok；aggregation any） | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.08（原定 multpl.com） | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 41.52（原定 multpl.com） | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 trailing P/E 約 40 | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026 （MarketXLS） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS 約 198bp（創紀錄）、CoreWeave 約 665bp | Oracle CoreWeave CDS spread widening July 2026 | https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/ （Real Investment Advice） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP +10.68% vs SPY +7.47% YTD | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St.） | 2026-06-10 | 2026-07-20T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 36.40%（原定 State Street SPDR 持股） | S&P 500 top 10 concentration percent 2026 | https://ahasignals.com/sp500-concentration-risk/ （AHA Signals） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| breadth.advance_decline | NYSE 下跌約為上漲 2 倍、新高 241／新低 166 | NYSE advance decline breadth July 17 2026 | https://money.usnews.com/investing/news/articles/2026-07-17/wall-st-futures-fall-as-chip-selloff-gathers-pace-netflix-tumbles （US News／Reuters） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（Fear）（原定 cnn.com） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed （MacroMicro） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-05 月資料）$1.416T、YoY +53.7% | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives，2026-06-24 發布） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |
| retail.aaii | AAII Bull 44.9% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number （YCharts） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 2.59、小幅 tail | US Treasury 10Y auction July 2026 bid to cover | https://cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/ （Crypto Briefing） | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 會議持平約 86.7% | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch （CryptoRank） | 2026-07-18 | 2026-07-20T09:30:00+08:00 |
| monetary.pboc | 人行 6 個月買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance （Bloomberg） | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio 18.8%，quarterly redemption cap 5% 下 gate proration / breach | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://whbl.com/2026/07/02/blue-owl-keeps-withdrawal-limits-even-as-redemption-pressure-modestly-eases/ （WHBL／Reuters） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計約 $700B、仍上修（2026 Q1 財報沿用） | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html （Yahoo Finance） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價季增 13–18% | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html （TrendForce） | 2026-07-03 | 2026-07-20T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex 約 $700B vs AI 終端營收數百億美元等級（分母：hyperscaler 合計） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| speculation.ai_rename_spac | EVTV 改名 Azio AI（AZIO），2026-07-13 起以新代碼交易 | AI rename ticker change July 2026 Azio EVTV | https://www.businesswire.com/news/home/20260710628386/en/Azio-AI-Holdings-Inc.-Nasdaq-EVTV-to-Begin-Trading-Under-New-Ticker-Symbol-AZIO-Completing-Corporate-Rebrand （Business Wire） | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| speculation.ipo_heat | 2026 年迄今約 200 檔 IPO、募資 $141.2B | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/ （StockAnalysis） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot 0 件 | microcap 100% single day quantum AI moonshot July 2026 | Finviz biggest gainers、Benzinga movers、StockTitan movers screener | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 投資人會議、估值約 $965B、可能 10 月掛牌 | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html （CNBC） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.73（日讀數） | Cboe equity put call ratio July 2026 | https://www.cboe.com/markets/us/options/market-statistics/daily/ （Cboe） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 約 $198B（未分列 NVDL／TSLL／CONL／TQQQ／SOXL／SQQQ） | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing） | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 新上市 6 檔 2x 單一個股 ETF（GOOGL／AMZN／META／AAPL） | single-stock leveraged ETF launch July 2026 Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-07 | 2026-07-20T09:30:00+08:00 |
| structural.options_volume | OCC 6 月成交 1,603,491,559 口、YoY +45%（2026-06 月資料） | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 145.13、VIX 約 16.5 期限結構 contango | VIX term structure SKEW July 2026 | https://www.ainvest.com/news/0dte-volatility-drives-market-strategies-2026-2602/ （AInvest） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-05 月資料）$1.416T、YoY +53.7%（交叉引用 retail.margin_debt，僅作確認） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-07-20",
  "iso_week": "2026-W30",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-01-18",
  "prior_date": "2026-07-16",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 6.74,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

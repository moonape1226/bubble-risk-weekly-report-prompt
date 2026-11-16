> [DRY RUN] this report was not committed to archive.

# 2026-07-20 AI 泡沫破裂預測報告

報告日期：2026-07-20｜ISO 週次：2026-W30｜預測窗口：2026-07-20 → 2027-01-18｜前次基準：report-2026-07-16（4天前）

## 結論

**結論：no**

三條路徑目前都沒有進入完成段：R1 的 NASDAQ-100 距 52 週高點回撤 6.74%，距 25% 門檻仍需再跌約 19.58%；R2 的 hyperscaler 2026 capex 合計約 $700B 且仍在上修，四家無一下修。AI 信用端已開始重定價（Oracle 5yr CDS 約 198bp、CoreWeave 約 665bp），私募信貸也出現 gate proration / breach，但寬基信用（HY OAS 2.71%）與 repo 資金壓力（SOFR−IORB）仍平靜，尚不足以推翻「182 天內三項皆不發生」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 28,592.66（2026-07-17），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 6.74%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45，自最新收盤還需再下跌約 19.58% 才觸及。

近況：S&P 500 於 2026-07-17 收 7,457.69，較前次基準日（2026-07-16，7,533.77）跌 1.01%，仍高於 200 日均線 6.73%、高於 52 週均線 8.42%（`valuation.sp500_trend`）。2026-07-17 晶片股賣壓擴散，NYSE 下跌家數約為上漲家數的 2 倍，新高 241／新低 166（`breadth.advance_decline`）。VIX 由 2026-07-10 的 15.03 升至 2026-07-17 的 18.77（+24.88%），同窗 S&P 500 −1.55%，屬正常的股跌波動升，非 crowded-optionality 的同向共振（`structural.vix_spx_comove`）。估值處於極端區：S&P 500 trailing P/E 32.08、Shiller CAPE 41.52（2026-07-17，`valuation.sp500_pe_cape`）；槓桿與部位擁擠：FINRA margin debt $1.416T、YoY +53.7%（2026-05 月資料，`retail.margin_debt`），NAAIM 95.64（2026-07-15，`retail.naaim`）。

**判讀：** 尚遠。脆弱度高（估值、margin debt YoY 位於歷史頂部區間、主動經理人部位擁擠），但距門檻仍需約 19.58% 的再下跌；要在窗口內完成，需要 R2 或 R3 的催化（例如 hyperscaler 財報 capex 轉向、AI 信用事件）引發強制去槓桿。

### R2 資本支出收縮

本次可用證據為四家 hyperscaler 合計口徑：2026 年 capex 合計約 $700B，且指引仍在上修（2026-05-15，`ai.hyperscaler_capex`），屬沿用最近一季財報的 stock-of-state。

- Microsoft：分家指引數值本次未個別取得；合計來源未報告下修，方向視為未見下修（分家方向未個別核實）。
- Alphabet：同上，未見下修。
- Amazon：同上，未見下修。
- Meta：同上，未見下修。

目前已下修家數：0／4。下一次財報日期本次證據未取得；依季度節奏，182 天窗口（至 2027-01-18）內至少涵蓋兩輪季報。需求側仍偏強：伺服器 DRAM 3Q26 合約價 QoQ +13–18%（2026-07-03，`ai.compute_supply_demand`），與 capex 收縮相反方向。

**判讀：** 尚遠。R2 需要兩家在窗口內下修正式指引，而現況是合計仍上修、記憶體合約價仍漲；只有在 R1 大幅回撤或 AI 營收對 capex 缺口（revenue-to-capex gap）引發投資人施壓時，下一輪財報才可能出現轉向。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）正朝信貸端重定價方向演變：Oracle 5yr CDS 約 198bp（創紀錄）、CoreWeave 約 665bp（2026-07-16，`valuation.ai_credit_schism`）。CoreWeave 是本次證據中具名、以 AI 算力為主業的借款人；其負債規模、近期到期與再融資需求本次證據未提供，是否達 50 億美元門檻需另行核實。Oracle 並非以 AI 資料中心為主業，不屬 R3 借款人範圍，但其 CDS 走闊反映市場對 AI 融資鏈的定價轉向。

本次未取得任何破產申請、付款違約、covenant waiver、distressed exchange 或 going-concern 語言的證據；AI infrastructure debt financing / vendor-financing loops 的 30 日掃描無新披露。寬基信用仍平靜：HY OAS 2.71%、IG OAS 0.78%（2026-07-16，`monetary.hy_oas`、`monetary.ig_oas`）。非銀行端出現壓力訊號：Blue Owl OCIC 第二季 redemption-request ratio 18.8%，以 5% quarterly redemption cap 比例撥付，屬 gate proration / breach（2026-07-02，`monetary.private_credit_liquidity`）。

**判讀：** 中等距離，三條中最接近。665bp 的 CDS 顯示市場已對 AI 算力借款人計入可觀違約風險，但從利差走闊到實際違約或 distressed exchange 通常需要再融資失敗或流動性斷裂；若私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）擴散到更多基金並壓縮 AI 資料中心放款，R3 可能在窗口內加速，並經 R1 傳導。

## 支持 yes 的證據

- [R3] AI 算力借款人信用重定價：CoreWeave CDS 約 665bp、Oracle 5yr CDS 約 198bp 創紀錄（2026-07-16），信貸端領先股權端走弱，是後期訊號 `valuation.ai_credit_schism`
- [整體] 私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）已出現實際 gate proration / breach：Blue Owl OCIC Q2 redemption-request ratio 18.8%，以 5% quarterly redemption cap 比例撥付（2026-07-02），可能收緊 AI 資料中心的非銀行融資管道 `monetary.private_credit_liquidity`
- [R1] 槓桿與部位擁擠：margin debt $1.416T、YoY +53.7%（2026-05 月資料，落在 1999／2007／2021 頂部附近的 +40–50% 以上區間），NAAIM 95.64（2026-07-15），美國槓桿 ETF AUM 約 $198B（2026-07-10）`retail.margin_debt` `retail.naaim` `structural.leveraged_etf_aum`
- [R1] 短線賣壓已啟動：NASDAQ-100 距 52 週高點回撤 6.74%（2026-07-17），2026-07-17 NYSE 下跌家數約為上漲 2 倍，VIX 7 日 +24.88% 至 18.77 `valuation.ndx_drawdown` `breadth.advance_decline` `structural.vix_spx_comove`
- [R1] 極端估值放大下行幅度：S&P 500 trailing P/E 32.08、Shiller CAPE 41.52（2026-07-17），Mag 7 加權 P/E 約 40（2026-05-15）`valuation.sp500_pe_cape` `valuation.mag7_multiples`
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）巨大：年化 AI 終端營收約 $72B（Anthropic 約 $47B＋OpenAI 約 $25B）vs hyperscaler 2026 capex 合計約 $700B（分母：來源所述 hyperscaler 合計口徑；2026-05-15）`ai.revenue_capex_gap` `ai.openai_anthropic_revenue`
- [整體] 投機熱度：Anthropic IPO 投資人會議估值 $965B、可能 10 月掛牌（2026-07-15）；EVTV 更名 Azio AI（AZIO，2026-07-13）；OCC 6 月期權成交 1,603,491,559 口、YoY +45% `speculation.upcoming_ai_ipos` `speculation.ai_rename_spac` `structural.options_volume`

## 支持 no 的證據

- [R1] 距門檻仍遠：NASDAQ-100 最新收盤 28,592.66 vs R1 門檻 22,995.45，需再跌約 19.58%（2026-07-17）`valuation.ndx_drawdown`
- [R2] capex 仍在上修：hyperscaler 2026 capex 合計約 $700B、指引仍上修（2026-05-15），四家無一下修；伺服器 DRAM 3Q26 合約價 QoQ +13–18%（2026-07-03）顯示需求未見消化 `ai.hyperscaler_capex` `ai.compute_supply_demand`
- [R3] 寬基信用未見傳染：HY OAS 2.71%、IG OAS 0.78%（2026-07-16），本次 Δ 為 0 `monetary.hy_oas` `monetary.ig_oas`
- [整體] 資金市場平靜：repo 資金壓力（SOFR−IORB）為 −3bp、SOFR99−IORB 5bp（2026-07-16），SRF 動用（Standing Repo Facility usage）0（2026-07-17）；MOVE 70.88（2026-07-17）`monetary.repo_stress_srf` `structural.treasury_basis_trade`
- [整體] 情緒並非狂熱：CNN Fear & Greed 37（Fear，2026-07-17），Cboe equity put/call 0.73（2026-07-17），S&P 500 高於 200 日均線僅 6.73% `retail.fear_greed` `speculation.equity_put_call` `valuation.sp500_trend`
- [R3] 主要 AI 終端客戶營收仍在擴張：Anthropic run-rate 約 $47B、OpenAI 約 $25B（2026-05-15），支撐其對算力供應商的付款能力 `ai.openai_anthropic_revenue`

## 與前期比較

前次結論：無前次預測（report-2026-07-16 為舊格式評分報告）

本次為新格式首份 yes/no 預測；舊格式評分不轉換為 yes/no，flip_evidence 為空。自 2026-07-16 以來的主要變化：

- NASDAQ-100 由 2026-07-16 的 29,025.77 跌至 2026-07-17 的 28,592.66；距 52 週高點回撤 6.74%。
- VIX 由 16.73 升至 18.77，MOVE 由 68.16 升至 70.88。
- AI 信用定價分歧（equity-vs-credit schism）新資料（2026-07-16）：Oracle CDS 約 198bp、CoreWeave 約 665bp。
- 10Y 殖利率與實質殖利率無新觀測（DGS10、DFII10 為 stale_series），T10YIE +2.0bp；Δ 分解判讀：不可判（視窗不一致）。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `speculation.insider_form4`：SEC EDGAR 一手 Form 4 URL 因 egress 受限無法取得；搜尋回報「0 件」並非完整篩選結果，因此不能記為 `✓ SEARCH-VERIFIED（0 件）`。影響：內部人賣壓屬情緒確認類訊號，不直接決定 R1–R3，缺口不太可能改變結論。

其他未揭露（✗ NOT DISCLOSED）來源：`valuation.analyst_tp_decomposition`、`retail.social_sentiment`、`institutional.bofa_jpm_survey`、`ai.token_growth`、`ai.customer_concentration_rpo`、`ai.hyperscaler_financing_mix`、`ai.depreciation_life`、`ai.capital_cycle`、`structural.global_leveraged_approvals`、`structural.ai_infrastructure_debt`。其中 `structural.ai_infrastructure_debt` 與 `ai.hyperscaler_financing_mix` 的空白最可能影響 R3 判讀：若有未被捕捉的 AI 資料中心再融資困難，R3 距離會被低估。

資料一致性注記：搜尋結果紀錄將 `structural.treasury_basis_trade` 的三個腳本組件記為 fetch_failed，但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 皆為 status ok，本報告以 macro artifact 為準並記為 ✓ API。

最大不確定性：

1. 下一輪 hyperscaler 季報（日期本次未取得，窗口內至少兩輪）：若兩家以上 capex 指引轉為下修，R2 直接成立，並會推向 yes。
2. CoreWeave 等 AI 算力借款人的負債規模與再融資時程未知：665bp 的 CDS 若伴隨再融資失敗或 distressed exchange，R3 成立並推向 yes；若成功發債，信用分歧收斂，推向 no。
3. 私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）是否擴散：多檔基金出現 gate proration / breach 或 net inflow→outflow flip，會收緊 AI 基建融資並推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7457.69 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線） | 6.73（%） | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線） | 8.42（%） | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28592.66 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤） | 6.74（%） | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1，家庭股票占金融資產 %） | 45.76 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限） | 3.75（%） | FRED API (series_id=DFEDTARU) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限） | 3.5（%） | FRED API (series_id=DFEDTARL) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.71（%） | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.78（%） | FRED API (series_id=BAMLC0A0CM) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.57（%） | FRED API (series_id=DGS10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（無新觀測，Δ=0） | 0.0（bp） | FRED API (series_id=DGS10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.35（%） | FRED API (series_id=DFII10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.24（%） | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | 2.0（bp） | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 79.2（USD/bbl） | FRED API (series_id=DCOILWTICO) | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46（%） | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.21（%） | FRED API (series_id=T5YIFR) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.7788（%） | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（序列自身 trailing 約 7 日） | 4.7（bp） | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.62（%） | FRED API (series_id=SOFR) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.7（%） | FRED API (series_id=SOFR99) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65（%） | FRED API (series_id=IORB) | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用 transaction volume） | 0.0（十億美元） | FRED API (series_id=RPONTTLD) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,743,028（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,970,516（€5.97T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,395,509（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 18.77 | FRED API (series_id=VIXCLS) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of） | 18.77 | FRED 衍生區塊（scripts/fetch_macro.py） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（base 2026-07-10，window 7 日） | 24.88（%） | FRED 衍生區塊（scripts/fetch_macro.py） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（同窗） | -1.55（%） | FRED 衍生區塊（scripts/fetch_macro.py） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2,004.0237（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六個 CBT 美債期貨槓桿基金淨部位，口數） | -7,562,874 | CFTC TFF futures-only | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -78,139 | CFTC TFF futures-only | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 70.88 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2342.6（十億美元） | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | MarketXLS WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500，sp500_trend 區塊） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100，ndx_drawdown 區塊） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | ahasignals WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH]，MacroMicro 鏡像 | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA／Advisor Perspectives WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／ycharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（FRED API） | ✓ API DFEDTARU:ok, DFEDTARL:ok |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（FRED API） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（FRED API） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（FRED API） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED API） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（FRED API 直接取得） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（FRED API） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（FRED API，yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（FRED API） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（FRED API，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（FRED API，repo_stress 區塊） | ✓ API SOFR:ok, SOFR99:ok, IORB:ok, RPONTTLD:ok |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | Reuters／TreasuryDirect 摘要 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（FRED API） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py（FRED API） | ✓ API ECBASSETSW:ok, JPNASSETS:ok |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Bloomberg WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC／interval fund 披露 [primary: SEARCH]（30d） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報／新聞 WebSearch（stock-of-state，沿用最近一季） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／The Information WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報 quarterly_state＋30d event_scan [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 [primary: SEARCH]（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q [primary: SEARCH]（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速 quarterly_state＋30d event_scan [primary: SEARCH] | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis／Renaissance WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／Benzinga／StockTitan movers [primary: SEARCH]（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 [primary: SEC EDGAR]（14d），openinsider 搜尋 | ⛔ FETCH FAILED（SEC EDGAR egress 受限，一手 Form 4 URL 無法取得） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com／ETFGI [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF.com WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe insights WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC monthly | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe／AInvest WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（FRED VIXCLS＋vix_spx_comove 區塊） | ✓ API VIXCLS:ok, vix_spx_comove:ok |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | FINRA／Advisor Perspectives WebSearch（交叉確認） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]（30d） | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED API） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（CFTC TFF、^MOVE、OFR repo），WebSearch 為備援 | ✓ API cftc_lev_funds:ok, move_index:ok, ofr_repo:ok |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.08（原定來源 multpl.com） | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 41.52（原定來源 multpl.com） | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E 約 40 trailing | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026 （MarketXLS） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS 約 198bp 創紀錄、CoreWeave 約 665bp | Oracle CoreWeave CDS spread widening July 2026 | https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/ （Real Investment Advice） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP +10.68% vs SPY +7.47% YTD | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St.） | 2026-06-10 | 2026-07-20T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 36.40% | S&P 500 top 10 concentration percent 2026 | https://ahasignals.com/sp500-concentration-risk/ （AHA Signals） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| breadth.advance_decline | NYSE 2026-07-17 下跌約 2 倍於上漲、新高 241／新低 166 | NYSE advance decline breadth July 17 2026 | https://money.usnews.com/investing/news/articles/2026-07-17/wall-st-futures-fall-as-chip-selloff-gathers-pace-netflix-tumbles （U.S. News／Reuters） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（Fear）（原定來源 cnn.com） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed （MacroMicro） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-05 月資料）$1.416T、YoY +53.7% | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives／FINRA） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |
| retail.aaii | AAII Bull 44.9% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number （YCharts） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 2.59、小幅 tail | US Treasury 10Y auction July 2026 bid to cover | https://cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/ （Crypto Briefing） | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 會議約 86.7% 維持利率 | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch （CryptoRank） | 2026-07-18 | 2026-07-20T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance （Bloomberg） | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio 18.8%，以 5% quarterly redemption cap 比例撥付 | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://whbl.com/2026/07/02/blue-owl-keeps-withdrawal-limits-even-as-redemption-pressure-modestly-eases/ （WHBL／Reuters） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計約 $700B、仍上修（沿用最近一季財報） | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html （Yahoo Finance） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 約 $47B／OpenAI 約 $25B run-rate | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 QoQ +13–18% | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html （TrendForce） | 2026-07-03 | 2026-07-20T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex 約 $700B vs AI 終端營收低百億級 | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| speculation.ai_rename_spac | EVTV 更名 Azio AI（AZIO） | AI rename ticker change July 2026 Azio EVTV | https://www.businesswire.com/news/home/20260710628386/en/Azio-AI-Holdings-Inc.-Nasdaq-EVTV-to-Begin-Trading-Under-New-Ticker-Symbol-AZIO-Completing-Corporate-Rebrand （Business Wire） | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD 約 200 檔 IPO、募資 $141.2B | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/ （StockAnalysis） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot 0 件 | microcap 100% single day quantum AI moonshot July 2026 | Finviz／Benzinga／StockTitan movers screener（已檢查來源） | — | 2026-07-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 投資人會議、估值 $965B、可能 10 月掛牌 | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html （CNBC） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.73（日讀數） | Cboe equity put call ratio July 2026 | https://www.cboe.com/markets/us/options/market-statistics/daily/ （Cboe） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美國槓桿 ETF 總 AUM 約 $198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing） | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 推出 6 檔 2x 單一個股 ETF（GOOGL／AMZN／META／AAPL） | single-stock leveraged ETF launch July 2026 Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-07 | 2026-07-20T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 成交約 63% | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/ （Cboe） | 2026-02-28 | 2026-07-20T09:30:00+08:00 |
| structural.options_volume | OCC 6 月總成交 1,603,491,559 口、YoY +45% | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 145.13、VIX 約 16.5 contango | VIX term structure SKEW July 2026 | https://www.ainvest.com/news/0dte-volatility-drives-market-strategies-2026-2602/ （AInvest） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-05 月資料）$1.416T、YoY +53.7%（交叉確認，不重複計入） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives／FINRA） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |

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

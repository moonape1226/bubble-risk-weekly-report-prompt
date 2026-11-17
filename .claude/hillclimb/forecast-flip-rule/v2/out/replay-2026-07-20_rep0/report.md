> [DRY RUN] this report was not committed to archive.

# 2026-07-20 AI 泡沫破裂預測報告
報告日期：2026-07-20｜ISO 週次：2026-W30｜預測窗口：2026-07-20 → 2027-01-18｜前次基準：report-2026-07-16（4天前）

## 結論

**結論：no**

三條路徑都沒有已在進行中的證據：NASDAQ-100 只比 252 日高點低 6.74%，離 R1 門檻還要再跌 ≈19.58%（`valuation.ndx_drawdown`）；hyperscaler 2026 capex 指引合計 ≈$700B，而且仍在上修，R2 方向相反（`ai.hyperscaler_capex`）。Oracle／CoreWeave CDS 走闊（`valuation.ai_credit_schism`）和 Blue Owl OCIC 的 gate proration / breach（`monetary.private_credit_liquidity`）說明信用端開始承壓，但 HY OAS 2.71% 仍然很緊（`monetary.hy_oas`）。本次沒有看到任何 R3 規模借款人出現違約或 distressed exchange，依 base rate 判 no。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

- NASDAQ-100 最新收盤 28,592.66（2026-07-17）。252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 6.74%（`valuation.ndx_drawdown`）。
- R1 門檻水位 22,995.45（高點 × 0.75）。從最新收盤還要再跌 ≈5,597 點，也就是 ≈19.58%，才會觸發；artifact `r1_met: false`。
- 本週走勢轉弱：S&P 500 07-16 → 07-17 收盤 −1.01%，至 7,457.69，但仍高於 200 日均線 6.73%、高於 52 週均線 8.42%（`valuation.sp500_trend`）。07-17 NYSE 下跌家數約為上漲家數的 2 倍，新高 241／新低 166，相關報導以晶片股賣壓為主題（`breadth.advance_decline`）。
- VIX 在 07-10 → 07-17 的 7 日窗口內 +24.88%，至 18.77；同一窗口 S&P 500 −1.55%。兩者反向，屬於正常避險，不是 crowded-optionality 式的同漲（`structural.vix_spx_comove`）。
- 脆弱度偏高：Shiller CAPE 41.52、trailing P/E 32.08（`valuation.sp500_pe_cape`）；FINRA margin debt $1.416T，YoY +53.7%（`retail.margin_debt`）；NAAIM 95.64（`retail.naaim`）。

**判讀：** R1 目前離觸發還遠，要在窗口內再跌 ≈19.6% 才成立。可能把它推過門檻的是：晶片股賣壓延續成為趨勢、AI 信用重定價傳導到股市，或 margin debt／槓桿 ETF 部位被迫去槓桿。目前這些都只看到早期跡象（VIX 上升、市場廣度轉弱），還沒有證據顯示已進入強制去槓桿階段。

### R2 資本支出收縮

- 本次取得的最新官方指引來源是 Q1 2026 季報後的合計數：四大 hyperscaler 2026 年 capex 合計 ≈$700B，報導描述為「仍上修」，資料日 2026-05-15（`ai.hyperscaler_capex`）。這是 stock-of-state 數據，自上次季報後沿用。
- Microsoft、Alphabet、Amazon、Meta 各自的指引金額與方向，本次證據沒有逐家列出，所以每家的方向只能依合計報導記為「上修」，個別數字未確立。目前沒有任何一家下修的證據，下修家數記為 0／4。
- 下一次財報日期本次未取得。依季報節奏，Q2 與 Q3 兩次季報應落在窗口內（2027-01-18 前）；Q4 季報是否落在窗口內不確定。
- 需求端的佐證：TrendForce 指 3Q26 伺服器 DRAM 合約價季增 13–18%（2026-07-03），顯示 AI 伺服器需求仍強，而不是在消化訂單（`ai.compute_supply_demand`）。
- ROI 的壓力：年化 AI capex ≈$700B（分母：MSFT／GOOGL／AMZN／META 合計，Oracle 未納入），對照 Anthropic ≈$47B 加 OpenAI ≈$25B 的年化終端營收（2026-05-15 披露，沿用），AI 營收對 capex 缺口（revenue-to-capex gap）仍然很大（`ai.revenue_capex_gap`）。這是沿用的季頻組合值，不算新證據。

**判讀：** R2 目前方向相反，指引仍在上修。要觸發，需要兩家在接下來的季報中正式下修。可能推動下修的是：股價大跌後改採防禦性指引、融資成本急升，或電力／供應鏈延後被寫成指引調降。現有證據沒有指向這些情況。

### R3 AI 信用事件

- AI 信用定價分歧（equity-vs-credit schism）出現走闊：Oracle 5 年期 CDS ≈198bp，為紀錄高位；CoreWeave CDS ≈665bp（2026-07-16，`valuation.ai_credit_schism`）。這是信用端先行重定價的後期型訊號。
- 規模門檻：CoreWeave 屬於以 AI 算力為主業的借款人類型，但它的負債總額本次沒有可引用來源，是否 ≥ USD 5bn 未確立。Oracle 的主業不是 AI 資料中心，不符合 R3 借款人定義。其他可能符合門檻的借款人，其負債規模與近期到期牆，本次同樣未確立。
- 窮迫訊號：本次沒有找到任何付款違約、covenant waiver、distressed exchange 或 going-concern 披露。AI infrastructure debt financing / vendor-financing loops 的 30 日事件掃描與 hyperscaler 融資結構（capex vs FCF / 發債）的掃描都沒有找到合格披露，細節見資料缺漏一節。
- 傳導通道：私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）已出現實際的 gate proration / breach。Blue Owl OCIC Q2 的 redemption-request ratio 為 18.8%，實際按 5% 的 quarterly redemption cap 比例撥付（2026-07-02，`monetary.private_credit_liquidity`）。若 AI 資料中心借款人依賴非銀行再融資，這條通道會收緊它們的再融資條件。
- 整體信用環境仍然寬鬆：HY OAS 2.71%、IG OAS 0.78%（2026-07-16，`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）−3.0bp，SRF 動用（Standing Repo Facility usage）為 0（`monetary.repo_stress_srf`）。

**判讀：** R3 的價格訊號正在惡化（CDS 走闊、私募信貸出現 gate proration / breach），但還沒有任何已確認的 ≥ USD 5bn AI 算力借款人違約或交換事件，負債規模與到期牆也未確立。要在窗口內觸發，需要大型 neocloud 再融資失敗、主要客戶合約違約，或私募信貸贖回潮讓再融資管道中斷。

## 支持 yes 的證據

- [R3] AI 信用端已開始重定價：Oracle 5 年期 CDS ≈198bp，為紀錄高位；CoreWeave CDS ≈665bp（2026-07-16）。信用先走闊、股價未完全跟上，是典型的後期訊號，也是 R3 最可能的起點（`valuation.ai_credit_schism`）。
- [R3] 私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）出現實際 gate proration / breach：Blue Owl OCIC Q2 redemption-request ratio 18.8%，按 5% quarterly redemption cap 比例撥付（2026-07-02），非銀行再融資通道已在收緊（`monetary.private_credit_liquidity`）。
- [R1] 槓桿與擁擠度處於高位，一旦下跌，跌幅會被放大：FINRA margin debt $1.416T、YoY +53.7%（2026-05 月資料，`retail.margin_debt`）；NAAIM 95.64（2026-07-15，`retail.naaim`）；美國槓桿 ETF 總 AUM ≈$198B（2026-07-10，`structural.leveraged_etf_aum`）。
- [R1] 估值極高：Shiller CAPE 41.52、trailing P/E 32.08（2026-07-17，`valuation.sp500_pe_cape`）；S&P 500 Top-10 集中度 36.40%（2026-07-02，`breadth.top10_concentration`）。
- [R1] 本週出現轉弱的催化跡象：07-17 晶片股賣壓下，NYSE 下跌家數約為上漲家數 2 倍（`breadth.advance_decline`）；VIX 7 日 +24.88% 至 18.77（`structural.vix_spx_comove`）。
- [整體] 股權供給與投機熱度上升：Anthropic IPO 投資人會議估值 $965B，可能 10 月掛牌（2026-07-15，`speculation.upcoming_ai_ipos`）；EVTV 改名為 Azio AI（AZIO），07-13 起交易（`speculation.ai_rename_spac`）；2026 YTD 約 200 檔 IPO、募資 $141.2B（`speculation.ipo_heat`）。

## 支持 no 的證據

- [R1] NASDAQ-100 只比 252 日高點低 6.74%，要再跌 ≈19.58% 到 22,995.45 才觸發 R1（2026-07-17，`valuation.ndx_drawdown`）；S&P 500 仍高於 200 日均線 6.73%（`valuation.sp500_trend`）。
- [R2] 四大 hyperscaler 2026 capex 合計 ≈$700B，Q1 季報後仍上修（2026-05-15，`ai.hyperscaler_capex`），目前沒有任何一家下修，R2 需要的兩家下修方向相反。
- [R2] 需求端仍然偏緊：3Q26 伺服器 DRAM 合約價季增 13–18%（2026-07-03，`ai.compute_supply_demand`），看不到訂單消化或利用率下滑。
- [R3] 整體信用利差很緊：HY OAS 2.71%、IG OAS 0.78%（2026-07-16，`monetary.hy_oas`、`monetary.ig_oas`），本次也沒有任何合格 AI 算力借款人出現違約或 distressed exchange。
- [整體] 資金面沒有失序：SOFR−IORB −3.0bp、SOFR99−IORB +5.0bp，SRF 動用為 0（`monetary.repo_stress_srf`）；MOVE 70.88（`structural.treasury_basis_trade`）；CME FedWatch 顯示 7/29 會議維持利率的機率約 86.7%（`monetary.fedwatch`）。
- [整體] 情緒已偏恐懼而不是狂熱：CNN Fear & Greed 37，屬 Fear 區（2026-07-17，`retail.fear_greed`）；Cboe equity put/call 0.73，不是低於 0.50 的追 call 型讀數（`speculation.equity_put_call`）。部分去槓桿可能已在發生，而非處於最脆弱的頂點。
- [整體] Base rate：任一 182 日窗口內，NASDAQ-100 回撤 25%、兩家 hyperscaler 同時下修 capex、或 ≥ USD 5bn AI 算力借款人違約，本來就都是少見事件。本次找到的證據只顯示泡沫的脆弱度，沒有顯示任何一條路徑已在進行中（`valuation.ndx_drawdown`、`ai.hyperscaler_capex`）。

## 與前期比較

前次結論：無前次預測（report-2026-07-16 為舊格式評分報告）

- 前次（2026-07-16）是舊格式評分報告，沒有 yes/no 結論，所以無從比較是否翻轉，flip_evidence 為空。
- 2026-07-16 之後的變化：S&P 500 07-16 → 07-17 跌 1.01%，VIX 由 16.73 升至 18.77，07-17 晶片股賣壓拖累市場廣度，T10YIE +2.0bp，MOVE 由 68.16 升至 70.88。這些都屬於溫和轉弱，沒有任何一條路徑因此接近觸發。
- DGS10、DFII10、HY／IG OAS、SOFR 等序列自 07-16 之後沒有新觀測（no_new_obs），Δ 為 0、讀作持平。10Y 分解的 ΔDGS10 0bp、ΔDFII10 0bp、ΔT10YIE +2.0bp，判讀：不可判（視窗不一致）。stale_series 為 DGS10、DFII10。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `speculation.insider_form4`（required）：SEC EDGAR 一手 Form 4 URL 因 egress 受限無法取得。prompt 要求每筆內部人交易都要附 EDGAR filing URL 與日期，因此無法完成合格篩選，本次不能宣稱「0 件」。內部人賣壓只是投機熱度的輔助訊號，不直接對應 R1–R3，**不會改變結論**。
- `structural.zero_dte`（required）：唯一取得的 0DTE 佔 SPX ≈63% 的資料日為 2026-02-28，距執行日已 142 天。超過本次採用的「snapshot 須在 90 天內」的現行值標準，視為沒有取得現行值。0DTE 是結構性槓桿的輔助指標，**不會改變結論**。

其他缺漏（✗ NOT DISCLOSED，可能影響 R2／R3 細節判讀）：AI infrastructure debt financing / vendor-financing loops 的 30 日掃描（structural.ai_infrastructure_debt）、hyperscaler 融資結構（capex vs FCF / 發債）的兩個組件（ai.hyperscaler_financing_mix）、資本週期階段（ai.capital_cycle）、折舊年限變動（ai.depreciation_life）、backlog 重複計算風險（ai.customer_concentration_rpo）都沒有合格披露。OpenAI／Anthropic 營收（ai.openai_anthropic_revenue）最近一次披露是 2026-05-15，屬上一季，依 prompt 的 current-quarter 規則標記 ✗ NOT DISCLOSED，只透過 revenue-to-capex gap 作沿用背景。

資料品質說明：
- Mag 7 加權 P/E 的資料日為 2026-05-15，RSP vs SPY YTD 為 2026-06-10。兩者都是 90 天內、日期明確的 snapshot，但不是本週數值，只作背景。
- 證據檔的取得結果表把美債基差交易槓桿三個 script 組件記為 fetch_failed，但 macro artifact 顯示 cftc_lev_funds、move_index、ofr_repo 都是 `status: ok`（資料日 2026-07-14／2026-07-17）。依 prompt，script 結果以 macro artifact 為準，所以 Coverage 記 ✓ API。

最大不確定性：
1. 下一次 hyperscaler 季報（日期本次未取得，依節奏落在窗口內）：若有兩家下修，會直接推向 yes；若繼續上修，會強化 no。
2. CoreWeave 等 neocloud 的負債規模與再融資時程未確立：若其負債 ≥ USD 5bn 且 CDS 持續走闊、再融資受阻，R3 會快速升溫，推向 yes。
3. 私募信貸贖回潮會不會從 Blue Owl 擴散成多家基金的 gate proration / breach：若擴散，可能同時觸發 R3 與 R1，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7457.69 | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線） | 6.73% | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線） | 8.42% | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（對前次基準） | -1.01% | FRED API (series_id=SP500) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28592.66 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤） | 6.74% | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1 資料，家庭股票配置 %） | 45.76 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限） | 3.75% | FRED API (series_id=DFEDTARU) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限） | 3.5% | FRED API (series_id=DFEDTARL) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.71% | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.78% | FRED API (series_id=BAMLC0A0CM) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.57% | FRED API (series_id=DGS10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.35% | FRED API (series_id=DFII10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.24% | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps（對前次基準） | 2.0 bp | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 79.2（USD/bbl） | FRED API (series_id=DCOILWTICO) | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46% | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.21% | FRED API (series_id=T5YIFR) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.7788% | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 日） | 4.7 bp | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.62% | FRED API (series_id=SOFR) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.7% | FRED API (series_id=SOFR99) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65% | FRED API (series_id=IORB) | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,743,028（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,970,516（€5.97T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,395,509（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 18.77 | FRED API (series_id=VIXCLS) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of，comove=false） | 18.77 | FRED API (vix_spx_comove block) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日窗口，base 2026-07-10） | 24.88% | FRED API (vix_spx_comove block) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日窗口，base 2026-07-10） | -1.55% | FRED API (vix_spx_comove block) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2004.0237（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位） | -7,562,874 口 | CFTC TFF (cftc_lev_funds block) | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -78,139 口 | CFTC TFF (cftc_lev_funds block) | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 70.88 | Yahoo chart API ^MOVE (move_index block) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2342.6（十億美元） | OFR STFM REPO-TRIV1_TV_TOT-P (ofr_repo block) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | MarketXLS WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-05-15，背景） |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 WebSearch，90d＋同季 | ✗ NOT DISCLOSED（無同季合格上調） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch，14d | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-06-10，背景） |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | ahasignals WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth 報導 WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | MacroMicro 轉載 WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | Advisor Perspectives WebSearch，月頻 stock-of-state | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB / cashtag WebSearch，7d | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py BOGZ1FL153064486Q | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | ycharts WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED（月中無新調查） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py BAMLH0A0HYM2 | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py BAMLC0A0CM | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py DGS10 | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py DFII10 | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py T10YIE（FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py DCOILWTICO | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py CPIAUCSL yoy_pct | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py T5YIFR | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py THREEFYTP10 | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | 標售 recap WebSearch，14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 轉載 WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py WALCL | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py ECBASSETSW、JPNASSETS | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Bloomberg WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 WebSearch，30d | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報彙整 WebSearch，stock-of-state 沿用 | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic / OpenAI / Google 披露 WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch / The Information WebSearch | ✗ NOT DISCLOSED（最近披露 2026-05-15 屬上季） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報 quarterly_state＋30d event_scan WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 WebSearch，stock-of-state 沿用 | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K / 10-Q WebSearch，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速 quarterly_state＋30d event_scan WebSearch | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | WebSearch，7d | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz / Benzinga / StockTitan movers WebSearch，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 WebSearch，30d | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 [primary: SEC EDGAR]，14d | ⛔ FETCH FAILED（EDGAR egress 受限，無一手 filing URL） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe daily statistics WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com / 新聞 WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire / ETF.com WebSearch，30d | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX / TWSE / JPX / ESMA WebSearch，7d | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe insights WebSearch | ⛔ FETCH FAILED（僅得 2026-02-28 舊值，無現行值） |
| structural.options_volume | 結構｜Options total volume: OCC monthly volume report | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe / AInvest WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py VIXCLS＋vix_spx_comove | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | Advisor Perspectives WebSearch（交叉引用） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | WebSearch，30d | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py LNFACBW027SBOG | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds / move_index / ofr_repo | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.08 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 41.52 | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 trailing P/E ≈40 | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026 （MarketXLS） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS ≈198bp（紀錄高）、CoreWeave CDS ≈665bp | Oracle CoreWeave CDS spread widening July 2026 | https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/ （RIA） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP +10.68% vs SPY +7.47% YTD | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St.） | 2026-06-10 | 2026-07-20T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 36.40% | S&P 500 top 10 concentration percent 2026 | https://ahasignals.com/sp500-concentration-risk/ （ahasignals；原定 State Street SPDR 持股） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| breadth.advance_decline | NYSE 下跌約 2×上漲、新高 241／新低 166 | NYSE advance decline breadth July 17 2026 | https://money.usnews.com/investing/news/articles/2026-07-17/wall-st-futures-fall-as-chip-selloff-gathers-pace-netflix-tumbles （US News / Reuters） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（Fear） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed （MacroMicro；原定 cnn.com） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-05 月資料）$1.416T、YoY +53.7% | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives；原定 FINRA） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |
| retail.aaii | AAII Bull 44.9% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number （YCharts；原定 naaim.org） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 2.59、小幅 tail | US Treasury 10Y auction July 2026 bid to cover | https://cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/ （Crypto Briefing；原定 Reuters / TreasuryDirect） | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 維持利率 ≈86.7% | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch （CryptoRank；原定 CME） | 2026-07-18 | 2026-07-20T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance （Bloomberg） | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio 18.8%，按 5% quarterly redemption cap 比例撥付（gate proration / breach） | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://whbl.com/2026/07/02/blue-owl-keeps-withdrawal-limits-even-as-redemption-pressure-modestly-eases/ （WHBL / Reuters） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計 ≈$700B、仍上修（Q1 2026 季報） | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html （Yahoo Finance） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 +13–18% QoQ | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html （TrendForce） | 2026-07-03 | 2026-07-20T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex ≈$700B vs Anthropic ≈$47B＋OpenAI ≈$25B run-rate（沿用組件） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| speculation.ai_rename_spac | EVTV 改名 Azio AI（AZIO），2026-07-13 起交易 | AI rename ticker change July 2026 Azio EVTV | https://www.businesswire.com/news/home/20260710628386/en/Azio-AI-Holdings-Inc.-Nasdaq-EVTV-to-Begin-Trading-Under-New-Ticker-Symbol-AZIO-Completing-Corporate-Rebrand （Business Wire） | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD 約 200 檔 IPO、募資 $141.2B | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/ （StockAnalysis） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot 0 件 | microcap 100% single day quantum AI moonshot July 2026 | Finviz / Benzinga / StockTitan movers screener | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 投資人會議，估值 $965B，可能 10 月掛牌 | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html （CNBC） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.73（日讀數） | Cboe equity put call ratio July 2026 | https://www.cboe.com/markets/us/options/market-statistics/daily/ （Cboe） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美國槓桿 ETF 總 AUM ≈$198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing；原定 etf.com / ETFGI） | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 推出 6 檔 2x GOOGL／AMZN／META／AAPL 單一個股 ETF | single-stock leveraged ETF launch July 2026 Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-07 | 2026-07-20T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月成交 1,603,491,559 口、YoY +45% | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 145.13、VIX ≈16.5 contango | VIX term structure SKEW July 2026 | https://www.ainvest.com/news/0dte-volatility-drives-market-strategies-2026-2602/ （AInvest） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-05 月資料）$1.416T、YoY +53.7%（交叉引用） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |

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
  "yes_basis": [],
  "r1_drawdown_pct": 6.74,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

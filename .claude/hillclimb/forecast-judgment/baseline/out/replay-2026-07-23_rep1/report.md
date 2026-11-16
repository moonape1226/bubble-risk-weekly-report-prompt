> [DRY RUN] this report was not committed to archive.

# 2026-07-23 AI 泡沫破裂預測報告
報告日期：2026-07-23｜ISO 週次：2026-W30｜預測窗口：2026-07-23 → 2027-01-21｜前次基準：report-2026-07-20（3天前）

## 結論

**結論：no**

三條路徑都還沒有在推進中：NASDAQ-100 距 52 週高點只回撤 5.42%（R1 門檻還要再跌約 20.70%），hyperscaler 正在上修而不是下修 capex（Alphabet 2026-07-22 上修至約 $205B），也沒有任何 AI 基建借款人違約或進行 distressed exchange。CoreWeave CDS 約 665bp、Oracle CDS 創紀錄，顯示信用端已在重定價，但 HY OAS 仍只有 2.69%，信用壓力尚未擴散，不足以推翻「182 天內三個條件都不成立」的基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 2026-07-22 收盤 28,998.10；252 個交易日最高收盤為 2026-06-02 的 30,660.60，目前距 52 週高點回撤 5.42%（`valuation.ndx_drawdown`）。R1 門檻是 22,995.45，指數須從最新收盤再跌約 20.70% 才會觸及。背景脆弱度偏高：S&P 500 2026-07-22 收在 7,498.96，高於 200 日均線 7.14%、高於 52 週均線 8.80%（`valuation.sp500_trend`）；Shiller CAPE 40.94、trailing P/E 28.85（`valuation.sp500_pe_cape`）；FINRA margin debt 約 $1.416T，年增 +53.7%（2026-05 月資料，`retail.margin_debt`）；NAAIM 95.64（`retail.naaim`）。但避險與波動指標並未失序：VIX 16.64（`structural.vix_spx_comove`），沒有出現漲勢中 VIX 與 S&P 500 同步上揚的情況；CNN Fear & Greed 41，屬 Fear（`retail.fear_greed`）。

**判讀：** 距 R1 還很遠。要在窗口內觸發，需要一次持續的 20% 以上下跌，觸發因素可能是 R3 信用事件外溢、AI 財報引發 capex 回收疑慮，或利率與期限溢價急升。目前價格動能與信用利差都還看不到這樣的軌跡。

### R2 資本支出收縮

- Alphabet：2026-07-22 Q2 財報將 FY2026 capex 上修至約 $205B，方向**上修**（`ai.hyperscaler_capex`）。
- Microsoft：本次證據沒有取得個別最新指引數值，方向無法判定，也未見下修披露。
- Amazon：本次證據沒有取得個別最新 capex 指引數值，方向無法判定。2026-07-07 啟動至少 $25B 的八檔期債券發行，用於 AI 基建（`ai.hyperscaler_financing_mix`），代表仍在加碼投入而非收縮。
- Meta：本次證據沒有取得個別最新指引數值，方向無法判定，也未見下修披露。
- 四家合計 2026 capex 約 $725B 以上（CNBC 2026-07-22，`ai.hyperscaler_capex`）。

目前下修家數：0／4（已確認有變動的唯一一家是上修）。窗口內至少還有兩輪季報（2026 Q2 尚未公布的三家，以及 2026 Q3 財報季），具體日期不在本次證據中。供給面的需求訊號仍偏緊：伺服器 DRAM 3Q26 合約價季增 +13–18%（TrendForce 2026-07-09，`ai.compute_supply_demand`）。

**判讀：** R2 目前朝反方向走。要觸發，需要兩家在接下來兩個財報季內反轉為下修，通常得先有 R1 式股價重挫或融資成本急升作為導火線。AI 營收對 capex 缺口（revenue-to-capex gap）很大（年化 capex 約 $725B，分母為 top-4，對比 Anthropic 約 $47B＋OpenAI 約 $25B run-rate，資料日 2026-05-15，`ai.revenue_capex_gap`），這是中期壓力，但還沒有轉化成指引下修。

### R3 AI 信用事件

- 信用定價：CoreWeave 5yr CDS 約 665bp，Oracle 5yr CDS 約 198bp 創歷史新高（bondblox 2026-07-20，`valuation.ai_credit_schism`），代表 AI 信用定價分歧（equity-vs-credit schism）已轉向信貸端走闊。
- 新增 AI infrastructure debt financing / vendor-financing loops：Galaxy Digital 為 CoreWeave 承租的資料中心計畫發行約 $3.5B 首發垃圾債（Bloomberg 2026-07-22，`structural.ai_infrastructure_debt`），顯示高收益市場仍願意承接，再融資管道沒有關閉。
- 符合 R3 規模門檻（負債 ≥ 50 億美元、以 AI 資料中心／算力為主業）而最可能出事的借款人是 CoreWeave。本次證據中沒有付款違約、covenant waiver、distressed exchange 或 going-concern 字樣。
- 傳導背景：私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）已出現 gate proration / breach：Blue Owl OCIC Q2 的 redemption-request ratio 為 18.8%，按 5% quarterly redemption cap 比例撥付（2026-07-02，`monetary.private_credit_liquidity`）。不過標題寫明申請比率較前一季回落。整體信用利差仍緊：HY OAS 2.69%、IG OAS 0.78%（2026-07-21，`monetary.hy_oas`、`monetary.ig_oas`）。

**判讀：** R3 是三條路徑中最接近的一條，CDS 水位已經反映不小的違約風險，但距離實際違約或 distressed exchange 仍有數個步驟。可能推過門檻的情境：高收益市場關門導致再融資失敗、主要承租客戶（OpenAI 等）付款延遲，或私募信貸贖回升級為多基金同步 gate proration / breach。

## 支持 yes 的證據

- [R3] CoreWeave 5yr CDS 約 665bp，Oracle 5yr CDS 約 198bp 創歷史新高（2026-07-20），AI 信用定價分歧已轉向信貸端重定價，屬後期訊號 `valuation.ai_credit_schism`
- [R3] Blue Owl OCIC Q2 的 redemption-request ratio 為 18.8%，按 5% quarterly redemption cap 比例撥付，構成實際 gate proration / breach（2026-07-02） `monetary.private_credit_liquidity`
- [整體] 槓桿與估值都處於歷史極端：FINRA margin debt 約 $1.416T、年增 +53.7%（2026-05 月資料），Shiller CAPE 40.94（2026-07-22），NAAIM 95.64（2026-07-15） `retail.margin_debt` `valuation.sp500_pe_cape` `retail.naaim`
- [R3] AI 基建持續依賴高收益債：CoreWeave 承租資料中心計畫發行約 $3.5B 垃圾債（2026-07-22），Amazon 啟動至少 $25B 債券發行（2026-07-07），融資結構正從現金流轉向舉債 `structural.ai_infrastructure_debt` `ai.hyperscaler_financing_mix`
- [整體] AI 營收對 capex 缺口巨大：年化 capex 約 $725B（分母：top-4），對比已披露的 AI 終端 run-rate（Anthropic 約 $47B、OpenAI 約 $25B，2026-05-15） `ai.revenue_capex_gap`

## 支持 no 的證據

- [R1] NASDAQ-100 2026-07-22 收盤 28,998.10，距 52 週高點回撤 5.42%，距 R1 門檻 22,995.45 還要再跌約 20.70% `valuation.ndx_drawdown`
- [R2] Alphabet 2026-07-22 將 FY2026 capex 上修至約 $205B，四家合計約 $725B 以上，目前 0／4 下修 `ai.hyperscaler_capex`
- [R3] 整體信用利差仍緊：HY OAS 2.69%、IG OAS 0.78%（2026-07-21），與前次基準相比 0bp 變動 `monetary.hy_oas` `monetary.ig_oas`
- [整體] 資金市場平穩：SOFR−IORB 為 −4bp（2026-07-21），SRF 動用（Standing Repo Facility usage）0.0（RPONTTLD，2026-07-22），MOVE 76.31（2026-07-22），沒有國債市場失序（Treasury market dysfunction）跡象 `monetary.repo_stress_srf` `structural.treasury_basis_trade`
- [R2] AI 硬體需求仍緊：伺服器 DRAM 3Q26 合約價季增 +13–18%（2026-07-09），與產能過剩相反 `ai.compute_supply_demand`
- [R3] 高收益市場仍願意承接 AI 基建新債（約 $3.5B 首發垃圾債，2026-07-22），短期再融資管道沒有關閉 `structural.ai_infrastructure_debt`

## 與前期比較

前次結論：無前次預測（report-2026-07-20 為舊格式評分報告）

report-2026-07-20 為舊格式評分報告，其分數不轉換為 yes/no，因此本次為新格式下的第一個預測，flip_evidence 為空。與前次基準日相比的主要變化：

- NASDAQ-100 由 2026-07-20 的 28,604.23 回升至 2026-07-22 的 28,998.10；S&P 500 自前次基準上漲 0.75%。
- 10Y 殖利率 +3bp 至 4.63%、DFII10 +2bp；T10YIE 視窗不同，Δ 分解判讀為 `不可判（視窗不一致）`。
- Alphabet 於 2026-07-22 上修 capex，CoreWeave 承租資料中心於 2026-07-22 計畫發行垃圾債。兩者分別強化了 R2 的 no 方向與 R3 的融資依賴，但都沒有改變結論。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `valuation.mag7_multiples`：唯一取得的 Mag 7 加權 P/E（約 40）資料日為 2026-05-15，不構成當期 snapshot。它只屬於估值脆弱度，不直接對應任何解析路徑，因此不可能改變結論。
- `structural.zero_dte`：唯一取得的 0DTE 佔比資料日為 2026-02-28，不構成當期 snapshot。它屬於投機結構的確認性輸入，不可能改變結論。

另外有數個來源完成搜尋但沒有合格的當期披露（✗ NOT DISCLOSED），包括 OpenAI / Anthropic 營收（最新為 2026-05-15，非本季）、AI customer concentration 與 backlog 重複計算風險（RPO double-counting）、折舊年限變動（depreciation useful-life change）、資本週期階段（capital cycle stage）、token growth、BofA/JPM 調查、社群情緒、全球槓桿產品核准。其中 RPO 與折舊披露若存在，可能強化 R3 或 R2 的脆弱度判斷，但不會單獨構成觸發。Form 4 篩選為 0 件，但 EDGAR 一手 URL 無法取得，因此內部人訊號只能視為未確認。

最大的三項不確定性：

1. Microsoft、Amazon、Meta 尚未公布的 2026 Q2 capex 指引（日期不在本次證據中）：若兩家同時下修，R2 會直接成立，推向 yes；若延續 Alphabet 的上修，則鞏固 no。
2. CoreWeave 的再融資與承租客戶付款能力：CDS 約 665bp 代表市場已在定價壓力。若高收益市場對 AI 基建關門，R3 可能在窗口內成立並經由信用外溢觸發 R1，推向 yes。
3. 私募信貸贖回趨勢：Blue Owl OCIC 已發生 gate proration / breach，但申請比率較前一季回落。若下一季多基金 redemption-request ratio 同步走升或出現 net inflow→outflow flip，將提高 R3 傳導機率，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7498.96 | FRED API (series_id=SP500) sp500_trend | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線） | 7.14% | FRED API (series_id=SP500) sp500_trend | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線） | 8.8% | FRED API (series_id=SP500) sp500_trend | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（自前次基準） | 0.75% | FRED API (series_id=SP500) sp500_trend | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（NASDAQ-100 最新收盤） | 28998.1 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-06-02 | 2026-07-23T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤） | 5.42% | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻） | 22995.45 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1 家庭股票配置 %） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-23T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標上限） | 3.75% | FRED API (series_id=DFEDTARU) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標下限） | 3.5% | FRED API (series_id=DFEDTARL) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.69% | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.78% | FRED API (series_id=BAMLC0A0CM) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.63% | FRED API (series_id=DGS10) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（自前次基準） | 3.0 bps | FRED API (series_id=DGS10) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.37% | FRED API (series_id=DFII10) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps（自前次基準） | 2.0 bps | FRED API (series_id=DFII10) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.28% | FRED API (series_id=T10YIE) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps（視窗與 DGS10 不同） | 3.0 bps | FRED API (series_id=T10YIE) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（無新觀測，持平） | 84.38 | FRED API (series_id=DCOILWTICO) | 2026-07-20 | 2026-07-23T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46% | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-23T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.26% | FRED API (series_id=T5YIFR) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR delta_bps | 4.0 bps | FRED API (series_id=T5YIFR) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.7787% | FRED API (series_id=THREEFYTP10) | 2026-07-17 | 2026-07-23T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 約 7 日） | -0.0 bps | FRED API (series_id=THREEFYTP10) | 2026-07-17 | 2026-07-23T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.61% | FRED API (series_id=SOFR) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.69% | FRED API (series_id=SOFR99) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65% | FRED API (series_id=IORB) | 2026-07-23 | 2026-07-23T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.walcl | WALCL latest（無新觀測） | 6,743,028.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-15 | 2026-07-23T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（無新觀測） | 5,949,077.0（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-17 | 2026-07-23T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（無新觀測） | 6,395,509.0（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-23T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.64 | FRED API (series_id=VIXCLS) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of 2026-07-22） | 16.64 | FRED API vix_spx_comove block | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日，base 2026-07-15） | 6.19% | FRED API vix_spx_comove block | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日，base 2026-07-15） | -0.97% | FRED API vix_spx_comove block | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（無新觀測） | 2004.0237（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-08 | 2026-07-23T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位） | -7562874 | CFTC TFF cftc_lev_funds | 2026-07-14 | 2026-07-23T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -78139 | CFTC TFF cftc_lev_funds | 2026-07-14 | 2026-07-23T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 76.31 | Yahoo chart ^MOVE move_index | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo 交易量） | 2334.5 | OFR STFM ofr_repo REPO-TRIV1_TV_TOT-P | 2026-07-22 | 2026-07-23T09:30:00+08:00 |

註：repo_stress 區塊 status ok，SOFR−IORB −4bp、SOFR99−IORB +4bp（兩腿日期皆為 2026-07-21，iorb_date 與 sofr99_iorb_date 同為 2026-07-21），SRF 日期 2026-07-22。10Y 分解：ΔDGS10 +3bp、ΔDFII10 +2bp、ΔT10YIE +3bp，driver 判讀為 不可判（視窗不一致），freshness updated。structural.treasury_basis_trade 的搜尋結果 MOVE 74.67（2026-07-21）與 script 值不同，以 script 的 move_index 為準。

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | MarketXLS 搜尋 | ⛔ FETCH FAILED 唯一結果資料日 2026-05-15，非當期 snapshot |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 [primary: SEARCH]，90d 且同季 | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場 [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | portfolioslab 搜尋 | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | MacroMicro 搜尋 | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth 搜尋 | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA | FINRA／Advisor Perspectives 搜尋（月頻沿用） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag 搜尋，7d | ✗ NOT DISCLOSED 搜尋完成，無合格當期聲量 |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／MacroMicro [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查搜尋 | ✗ NOT DISCLOSED 無當期新調查 |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API DFEDTARU ok；DFEDTARL ok |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | RTTNews／TreasuryDirect [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py | ✓ API ECBASSETSW ok；JPNASSETS ok |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Xinhua 搜尋 | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]，30d | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報搜尋（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 搜尋 | ✗ NOT DISCLOSED 本季無披露 |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／The Information 搜尋 | ✗ NOT DISCLOSED 最新披露 2026-05-15 非本季 |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報＋發債事件 [primary: SEARCH]；quarterly_state stock-of-state、event_scan 30d | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 [primary: SEARCH]（沿用最近組合值） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q [primary: SEARCH]，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速＋進出場事件 [primary: SEARCH]；quarterly_state stock-of-state、event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days +AI rename／SPAC | Businesswire／StockTitan 搜尋，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis 搜尋 | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／Benzinga [primary: SEARCH]，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導搜尋，30d | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR／openinsider [primary: SEC EDGAR]，14d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | YCharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com／cryptobriefing [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF.com 搜尋，30d | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA 搜尋，7d | ✗ NOT DISCLOSED 7 日內無英文披露 |
| structural.zero_dte | 結構｜0DTE option volume | Cboe 搜尋 | ⛔ FETCH FAILED 唯一結果資料日 2026-02-28，非當期 snapshot |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com 搜尋 | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Velox／Cboe 搜尋 | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API VIXCLS ok；vix_spx_comove ok |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 retail.margin_debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]，30d | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py cftc_lev_funds／move_index／ofr_repo | ✓ API cftc_lev_funds ok；move_index ok；ofr_repo ok |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 28.85（原定來源 multpl.com） | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 40.94（原定來源 multpl.com） | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標價 $288（約 22× EPS，target PE 未擴張，EPS 修正主導） | Morgan Stanley NVDA target 288 July 2026 EPS | https://www.gurufocus.com/news/8955458/morgan-stanley-upgrades-nvidia-nvda-with-a-288-target-price （GuruFocus） | 2026-07-13 | 2026-07-23T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS 約 198bp 創紀錄、CoreWeave 約 665bp | Oracle CoreWeave CDS spread record July 2026 | https://bondblox.com/news/oracles-5y-cds-spread-hits-all-time-highs （BondbloX） | 2026-07-20 | 2026-07-23T09:30:00+08:00 |
| breadth.rsp_spy | RSP +11.8% vs SPY +9.4% YTD | RSP vs SPY equal weight YTD 2026 | https://portfolioslab.com/tools/stock-comparison/RSP/SPY （PortfoliosLab） | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 36.40% | S&P 500 top 10 concentration percent 2026 | https://en.macromicro.me/collections/34/us-stock-relative/123442/us-sp-500-top-10-companies-total-market-cap-and-share （MacroMicro） | 2026-07-02 | 2026-07-23T09:30:00+08:00 |
| breadth.advance_decline | 07-22 A/D 轉弱，新低多於新高 | NYSE breadth advance decline July 22 2026 | https://ts2.tech/en/nasdaq-ends-flat-as-market-breadth-remains-thin-ahead-of-big-tech-earnings/ （TS2） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 41（Fear，原定來源 cnn.com） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/series/22748/cnn-fear-and-greed （MacroMicro） | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-05 月資料）$1.416T、+53.7% YoY | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives） | 2026-05-31 | 2026-07-23T09:30:00+08:00 |
| retail.aaii | AAII Bull 44.9% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-15 | 2026-07-23T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64 | NAAIM exposure index latest July 2026 | https://en.macromicro.me/series/20540/naaim-exposure-index （MacroMicro） | 2026-07-15 | 2026-07-23T09:30:00+08:00 |
| monetary.treasury_auctions | 20Y 標售 bid-to-cover 2.64、小幅 tail | US Treasury 20Y auction July 2026 bid to cover | https://www.rttnews.com/3669412/twenty-year-bond-auction-attracts-average-demand.aspx （RTTNews） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 會議維持利率約 83.4% | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch （CryptoRank 轉述 CME） | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://english.news.cn/20260714/2d460c4227c244f1bf930993be469262/c.html （Xinhua） | 2026-07-14 | 2026-07-23T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio 18.8%，按 5% quarterly redemption cap 比例撥付（申請較前一季回落） | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://www.investing.com/news/stock-market-news/blue-owl-keeps-5-redemption-caps-as-ocic-requests-ease-from-prior-quarter-4773280 （Investing.com） | 2026-07-02 | 2026-07-23T09:30:00+08:00 |
| ai.hyperscaler_capex | 2026 Q2：Alphabet FY26 capex 上修至約 $205B；四家合計約 $725B 以上 | hyperscaler capex 2026 Alphabet raised 205B Q2 | https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html （CNBC） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 +13–18% QoQ | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260709-13140.html （TrendForce） | 2026-07-09 | 2026-07-23T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] Alphabet FY26 capex 上修至約 $205B，發債佔比上升 | Alphabet capex 205B Q2 2026 debt financing | https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html （CNBC） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] Amazon 啟動至少 $25B 八檔期公司債（AI 基建用途） | Amazon 25 billion bond offering AI data center July 2026 | https://finance.yahoo.com/technology/ai/articles/bond-issuance-backing-ai-investment-135635215.html （Yahoo Finance） | 2026-07-07 | 2026-07-23T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex 約 $725B（分母：top-4，2026-07-22 CNBC）vs AI 終端 run-rate Anthropic 約 $47B＋OpenAI 約 $25B（2026-05-15 沿用） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-05-15 | 2026-07-23T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日內合格 +AI 改名／SPAC 事件 0 件 | AI rename ticker change SPAC July 16-23 2026 | 已檢查：Businesswire、StockTitan movers screener | — | 2026-07-23T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD 約 203 檔 IPO，募資 $141.2B | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/ （StockAnalysis） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| speculation.microcap_moonshots | 7 日內合格 microcap moonshot 0 件 | microcap 100% single day quantum AI fusion moonshot July 2026 | 已檢查：Finviz、Benzinga、StockTwits movers screener | — | 2026-07-23T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 程序啟動，估值 $965B，可能 10 月掛牌 | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html （CNBC） | 2026-07-15 | 2026-07-23T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 cluster 0 件（EDGAR 一手 URL 無法取得，單一 10b5-1 申報不構成 cluster、不具名列出） | insider Form 4 cluster AI leaders July 2026 openinsider | 已檢查：SEC EDGAR、openinsider | — | 2026-07-23T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.65（日讀數） | Cboe equity put call ratio July 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio （YCharts） | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 約 $198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing） | 2026-07-10 | 2026-07-23T09:30:00+08:00 |
| structural.us_single_stock_etf | GraniteShares 推出首檔美國掛牌 SK hynix 2x 多／空 ETF | single-stock leveraged ETF launch July 2026 GraniteShares SK hynix | https://www.globenewswire.com/news-release/2026/07/14/3326857/0/en/GraniteShares-Launches-the-First-U-S-Listed-Leveraged-ETFs-on-SK-hynix.html （GlobeNewswire） | 2026-07-14 | 2026-07-23T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月成交 1,603,491,559 口，+45% YoY | OCC monthly options volume June 2026 | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/monthly-weekly-volume-statistics （OCC） | 2026-07-02 | 2026-07-23T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 146.05，VIX 約 18.7 contango | VIX term structure SKEW July 2026 | https://veloxmacro.com/how-to-read-the-vix-week-ending-july-20-2026/ （Velox Macro） | 2026-07-20 | 2026-07-23T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-05 月資料）$1.416T、+53.7% YoY，僅交叉引用 | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives） | 2026-05-31 | 2026-07-23T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Galaxy Digital 為 CoreWeave 承租資料中心計畫發行約 $3.5B 首發垃圾債 | Galaxy Digital 3.5 billion junk bond CoreWeave data center July 2026 | https://www.bloomberg.com/news/articles/2026-07-22/coreweave-backed-data-center-plans-3-5-billion-junk-bond-sale （Bloomberg） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-07-23",
  "iso_week": "2026-W30",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-01-21",
  "prior_date": "2026-07-20",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 5.42,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

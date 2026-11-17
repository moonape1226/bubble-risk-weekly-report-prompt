> [DRY RUN] this report was not committed to archive.

# 2026-09-13 AI 泡沫破裂預測報告

報告日期：2026-09-13｜ISO 週次：2026-W37｜預測窗口：2026-09-13 → 2027-03-14｜前次基準：report-2026-09-03（10天前）

## 結論

**結論：no**

三條路徑目前都離觸發門檻很遠：NASDAQ-100 距 52 週高點回撤 4.21%，還需再跌約 21.70% 才觸及 R1；四大 hyperscaler 2026 capex 合計約 $725bn（2026-07-28），沒有任何一家下修的披露；HY OAS 仍只有 2.70%，也沒有任何 AI 資料中心借款人出現困境訊號。殖利率走高、9/16 FOMC 市場定價約 85.5% 升息，這些確實是窗口內的催化劑，但還不足以把任何一條路徑推過門檻。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,368.44（2026-09-11）。252 個交易日內的最高收盤為 30,660.60（2026-06-02），距 52 週高點回撤 4.21%。R1 門檻水位是 22,995.45，從最新收盤還要再跌約 21.70% 才會觸及（`valuation.ndx_drawdown`）。自 6 月高點以來，指數最深的回落是 2026-07-29 的 27,192.31，約為高點下方 11.3%，之後已收復大半。S&P 500 收在 7,656.98（2026-09-11），仍高於 200 日均線 6.9%、高於 52 週均線 8.33%；但自前次基準日以來下跌 1.17%（`valuation.sp500_trend`）。

市場層面的變化：VIX 從 14.32 升到 17.84（2026-09-03 → 2026-09-10，+24.58%），同一窗口 S&P 500 下跌 2.01%。這是正常的負相關，不是 crowded-optionality 的同漲讀數（`structural.vix_spx_comove`）。CNBC 2026-09-10 報導 VIX 收在約 17 以上，call skew 位於第 91 百分位（`structural.cross_asset_derivatives`）。CNN Fear & Greed 約 35，屬恐懼區（2026-09-10，`retail.fear_greed`）。估值仍在極端區：Shiller CAPE 約 40.73（2026-09-01，`valuation.sp500_pe_cape`），前十大成分股約佔 S&P 500 的 38%（2026-09-01，`breadth.top10_concentration`）。

**判讀：** R1 離門檻還很遠。若要在窗口內成立，NASDAQ-100 需要從現水位跌掉約五分之一以上。需要一個能觸發強制去槓桿的事件，例如升息後殖利率繼續上衝並擊穿 AI 龍頭估值、AI 信用事件外溢，或 hyperscaler capex 轉向。目前只看到波動率回升與恐懼情緒，還沒有看到這類傳導。

### R2 資本支出收縮

- Microsoft：本次證據沒有取得個別最新指引數字。最新的合計資料來自 2026-07-28 的季報週期（`ai.hyperscaler_capex`），方向：未見下修披露。
- Alphabet：同上，個別數字本次未取得。CNBC 2026-07-28 指出 Alphabet 財報遭市場批評、hyperscaler 的 capex 受到更嚴格檢視，但沒有下修指引的報導。方向：未見下修披露。
- Amazon：個別數字本次未取得，方向：未見下修披露。
- Meta：個別數字本次未取得，方向：未見下修披露。

四家 2026 capex 合計約 $725bn（CNBC，2026-07-28，`ai.hyperscaler_capex`）。目前已下修家數：0。依據是本次掃描中沒有任何一家下修的報導，但個別公司「相較前一次指引」的方向本次無法逐家核對。下一輪（2026 Q3）與再下一輪（2026 Q4）財報都落在窗口（→ 2027-03-14）內，但具體日期不在本次證據中。需求端的佐證：Anthropic 年化 run-rate 約 $65bn（2026-08-17，`ai.openai_anthropic_revenue`）；H100 中位租金約 $3.38/hr（2026-08-31，`ai.compute_supply_demand`），本次沒有閒置或訂單消化的佐證。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 $105bn，對比年化 capex 約 $725bn（分母只含 top-4，Oracle 本次未取得；2026-08-17，`ai.revenue_capex_gap`）。缺口約 $620bn，本次沒有前值可判斷是擴大還是收斂。

**判讀：** R2 需要在兩次財報內有兩家下修。目前 capex 仍在擴張，需求端 run-rate 仍在成長。要推過門檻，可能的情境是 R1 式的大幅回撤迫使管理層轉向，或折舊／融資壓力在 Q3 財報中浮現。本次沒有看到這方面的前兆。

### R3 AI 信用事件

本次證據沒有取得任何符合 R3 規模門檻（AI 資料中心／算力為主業、負債 ≥ 50 億美元）借款人的債券殖利率、利差、CDS 或評等動作。AI 信用定價分歧的 14 日掃描完成，但沒有窗口內披露。30 日窗口內唯一的 AI infrastructure debt financing / vendor-financing loops 事件是 Qualcomm 對 Amazon 的約 $4bn 認股權證安排（2026-09-08，`structural.ai_infrastructure_debt`）。它屬於供應商以股權綁定客戶的循環安排，不是借款人困境訊號。整體信用環境仍然很緊：HY OAS 2.70%（+5bp，2026-09-10，`monetary.hy_oas`）、IG OAS 0.80%（−1bp，`monetary.ig_oas`）。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）的 30 日掃描也沒有窗口內披露。資金面：SOFR−IORB −3bp、SOFR99−IORB +5bp、SRF 動用 0（2026-09-10／2026-09-11，`monetary.repo_stress_srf`），repo 資金壓力（SOFR−IORB）沒有升溫。

**判讀：** R3 目前沒有任何可觀察的困境訊號：沒有付款違約、covenant waiver、distressed exchange，也沒有 going-concern 語言。要在窗口內成立，需要利率上行加上融資窗口關閉，迫使高槓桿 neocloud 無法再融資。由於沒有取得個別借款人的到期牆資料，這條路徑的時點判斷存在盲點，但現有證據不支持在 182 天內完成違約或 distressed exchange。

## 支持 yes 的證據

- [整體] 利率與通膨壓力正在升溫：9/16 FOMC 的升息定價約 85.5%（CME FedWatch，2026-09-12，`monetary.fedwatch`），而目前政策利率區間是 3.50%–3.75%（`monetary.fed_funds`）；CPI YoY 3.35%（2026-08，`monetary.cpi_yoy`），WTI $97.26（+5.09%，2026-09-09，`monetary.wti`）。在 Shiller CAPE 約 40.73 的估值下（`valuation.sp500_pe_cape`），升息週期重啟是對長存續期 AI 股最直接的折現率衝擊。
- [R1] 10Y 殖利率自 2026-09-03 的 4.77% 升到 4.95%（+18bp，2026-09-10，`monetary.dgs10`），其中 10Y 實質殖利率 +13bp 到 2.55%（`monetary.dfii10`）。MOVE 從 74.68 升到 82.21（2026-09-11，`structural.treasury_basis_trade`），VIX 一週升 24.58% 到 17.84（`structural.vix_spx_comove`）。跨資產波動同步回升。
- [R1] 估值與集中度是下跌放大器：前十大佔 S&P 500 約 38%（2026-09-01，`breadth.top10_concentration`），S&P 500 仍高於 200 日均線 6.9%（`valuation.sp500_trend`），margin debt 約 $1.42T（2026-07 月資料，`retail.margin_debt`），家庭股票配置 48.23%（2026 Q2，`retail.household_equity_allocation`）。一旦出現催化劑，下行幅度可能很大。
- [R2] AI 營收對 capex 缺口仍大：年化 AI 終端營收約 $105bn，對比 top-4 年化 capex 約 $725bn（`ai.revenue_capex_gap`）。CNBC 2026-07-28 報導 hyperscaler capex 審視升溫（`ai.hyperscaler_capex`），這是 R2 的潛在前兆。
- [R3] 循環安排仍在累積：Qualcomm 以約 $4bn 認股權證綁定 Amazon 資料中心交易（2026-09-08，`structural.ai_infrastructure_debt`）。供應商與客戶互相持股、互為收入來源，是信用壓力一旦出現時的傳導通道。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.21%（2026-09-11），R1 門檻水位 22,995.45，還需再跌約 21.70%（`valuation.ndx_drawdown`）。從基率看，182 天內再跌兩成以上並不常見。
- [R3] 信用市場沒有重定價：HY OAS 2.70%、IG OAS 0.80%（2026-09-10，`monetary.hy_oas`、`monetary.ig_oas`）；SOFR−IORB −3bp、SRF 動用 0（`monetary.repo_stress_srf`）；銀行對 NBFI 放款約 $2.03T，沒有變化（2026-09-02，`structural.nbfi_bank_loans`）。R3 所需的違約鏈條沒有任何起點。
- [R2] capex 仍在擴張，沒有任何下修：四大 hyperscaler 2026 capex 合計約 $725bn（2026-07-28，`ai.hyperscaler_capex`）；需求端 Anthropic 年化 run-rate 約 $65bn（2026-08-17，`ai.openai_anthropic_revenue`）；H100 中位租金約 $3.38/hr（2026-08-31，`ai.compute_supply_demand`），沒有閒置的跡象。
- [整體] 情緒已偏恐懼而非亢奮：CNN Fear & Greed 約 35（2026-09-10，`retail.fear_greed`），AAII 看多約 38.0%（2026-09-10，`retail.aaii`），equity put/call 約 0.67（2026-09-01，`speculation.equity_put_call`）。單一個股槓桿 ETF 資金流出約 $751m（`structural.leveraged_etf_aum`）。投機部位已在自行去化，不是典型崩盤前的極端追價。
- [整體] Mag 7 前瞻本益比已低於 24，CNBC 稱其為紀錄低估值（2026-08-03，`valuation.mag7_multiples`）。AI 龍頭的估值擴張空間已被壓縮，回撤的起點不如 2000 年極端。

## 與前期比較

前次結論：無前次預測（report-2026-09-03 為舊格式評分報告）

report-2026-09-03 為舊格式評分報告，其分數不轉換為 yes/no，flip_evidence 為 []。自 2026-09-03 以來的主要變化：10Y 殖利率 +18bp（4.77% → 4.95%）、VIX 14.32 → 17.84、MOVE 74.68 → 82.21、WTI +5.09%、S&P 500 −1.17%、HY OAS +5bp。10Y 分解：ΔDGS10 +18bp、ΔDFII10 +13bp、ΔT10YIE +1bp，但 T10YIE 視窗與另兩腿不同，判讀為不可判（視窗不一致）。10Y 期限溢價（term premium）0.8892%（2026-09-04，trailing ≈7d +1.4bp，Kim-Wright）。另外 9/16 FOMC 的升息定價約 85.5%。這是本次新增的主要風險因子，但三條路徑距門檻仍遠。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源的掃描已完成，但沒有窗口內的合格披露（✗ NOT DISCLOSED）：valuation.analyst_tp_decomposition、valuation.ai_credit_schism、retail.social_sentiment、retail.naaim、institutional.bofa_jpm_survey、monetary.private_credit_liquidity、ai.token_growth、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（event_scan 無窗口內事件；quarterly_state 可用）、ai.depreciation_life、ai.capital_cycle（兩個組件皆無披露）、speculation.upcoming_ai_ipos、structural.global_leveraged_approvals。其中對答案影響最大的是 valuation.ai_credit_schism：R3 借款人的利差與 CDS 缺乏直接讀數。若補上的資料顯示 AI 借款人利差顯著走闊，R3 的判讀會往 yes 移動，但整體 HY OAS 2.70% 不支持這種情境。

證據檔對 structural.treasury_basis_trade 記載「script 三區塊 fetch_failed」，但 macro artifact 中 cftc_lev_funds、move_index、ofr_repo 三塊均為 status ok。本報告以 artifact 為準，記為 ✓ API。

最大的不確定性：

1. 9/16 FOMC 的決策與後續路徑。若升息並暗示連續升息、10Y 突破 5%，對長存續期 AI 股的折現率衝擊會推向 yes（R1）；若按兵不動，則壓力暫緩。
2. 2026 Q3 hyperscaler 財報（窗口內）。只要有任一家轉向下修，R2 就從零進入半途，並可能拖累 R1。
3. 個別 neocloud 的再融資與到期資料缺失。R3 的時點判斷依賴目前沒有取得的借款人層級資料。若出現 distressed exchange 的報導，會直接推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7656.98 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 6.9 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 8.33 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（vs 前次基準日） | -1.17 | FRED API (series_id=SP500) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29368.44 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 4.21 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q2 季資料，%） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（%） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（%） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.7 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.8 | FRED API (series_id=BAMLC0A0CM) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.95 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（vs 2026-09-03） | 18.0 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.55 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps（vs 2026-09-03） | 13.0 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.36 | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps（vs 2026-09-03） | 1.0 | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl） | 97.26 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO chg_pct | 5.09 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-08 月資料） | 3.35 | FRED API (series_id=CPIAUCSL) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.32 | FRED API (series_id=T5YIFR) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（%，Kim-Wright） | 0.8892 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API (series_id=SOFR99) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-09-13 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（USD bn，SRF 動用 read） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6740619.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5912178.0（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6446620.0（¥644.66T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 17.84 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 17.84 | FRED API (vix_spx_comove block) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 24.58 | FRED API (vix_spx_comove block) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -2.01 | FRED API (vix_spx_comove block) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2027.9777（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約合計，口數） | -6863118 | CFTC TFF (cftc_lev_funds block) | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | 387809 | CFTC TFF (cftc_lev_funds block) | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 82.21 | Yahoo ^MOVE (move_index block) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2271.6 | OFR STFM (ofr_repo block) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（multpl / GuruFocus） | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED（掃描完成，無合格同季上修） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch（14d） | ✗ NOT DISCLOSED（掃描完成，無窗口內披露） |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch（以 % above 200DMA 代理） | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch（月頻 stock-of-state，沿用 2026-07） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED（無顯著討論） |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED（無當週值） |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✗ NOT DISCLOSED（月中無新調查） |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（DFEDTARU ok；DFEDTARL ok） | ✓ API |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取；fallback 未使用） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） | ✓ API |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch 摘要） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW ok；JPNASSETS ok） | ✓ API |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED（無窗口內披露） |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state，2026-07 季報週期） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | WebSearch | ✗ NOT DISCLOSED（無合格披露） |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch：quarterly_state（stock-of-state）＋ event_scan（30d） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch（分子 Axios；分母 top-4 capex） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動（depreciation useful-life change） | WebSearch（30d） | ✗ NOT DISCLOSED（無窗口內變動） |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch：quarterly_state（stock-of-state）＋ event_scan（30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✗ NOT DISCLOSED（無 S-1 或具名來源） |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR / WebSearch（14d） | ✓ SEARCH-VERIFIED |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED（無英文披露） |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS ok；vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds ok；move_index ok；ofr_repo ok） | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.73（原定來源 multpl / GuruFocus） | S&P 500 Shiller CAPE ratio current September 2026 multpl | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio （GuruFocus） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | Magnificent 7 forward P/E valuation September 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html （CNBC） | 2026-08-03 | 2026-09-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 至 7 月止 YTD 報酬約 13% | RSP equal weight vs SPY S&P 500 YTD performance September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/ （24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.top10_concentration | 前十大集中度約 38% | S&P 500 top 10 concentration percentage September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/ （24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 200 日均線之上約 53% | market breadth advance decline new highs lows September 2026 percent stocks above 200-day | https://condoredge.com/stocks/market-breadth （Condor Edge） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 約 35（恐懼） | CNN Fear and Greed Index today September 2026 reading | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）約 $1.42T | FINRA margin debt August 2026 record year over year | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026 （Advisor Perspectives / FINRA） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.0% | AAII sentiment survey results week September 10 2026 bullish bearish neutral | https://www.aaii.com/sentimentsurvey （AAII） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.71 | Treasury auction results September 2026 tail bid-to-cover 10-year | https://thevaultreport.com/treasury-auctions （The Vault Report） | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.fedwatch | 9/16 FOMC 升息 25bp 定價約 85.5% | CME FedWatch September 12 2026 probability 25 basis point hike | https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html （Yahoo Finance） | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.pboc | 2026 年 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate financing 2026 total social financing | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm （SteelOrbis） | 2026-08-15 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 $725bn（2026 Q2 季報週期） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 $65bn | OpenAI Anthropic annualized revenue run rate September 2026 | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| ai.compute_supply_demand | H100 中位租金約 $3.38/hr | GPU rental price HBM DRAM contract price September 2026 utilization | https://www.thundercompute.com/blog/ai-gpu-rental-market-trends （Thunder Compute） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 增額債務佔 capex 約 32% | hyperscaler capex vs free cash flow debt issuance 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $105bn（分母 top-4 capex 約 $725bn） | AI revenue vs capex gap 2026 annualized run rate | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描：0 件合格事件 | AI company name change ticker SPAC announcement September 7-13 2026 | 檢查來源：SPACInsider、Businesswire SPAC newsroom、Boardroom Alpha | — | 2026-09-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 22 檔 | IPO priced week September 8 2026 first day return debut | https://www.iposcoop.com/current-year-pricings/ （IPOScoop） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描：0 件符合 2+ 主題×弱基本面（Tenon +77%、AEON +35% 未達門檻） | biggest stock gainers week September 7 2026 microcap 100% quantum AI | 檢查來源：Finviz、Benzinga、StockTitan、Yahoo movers | — | 2026-09-13T09:30:00+08:00 |
| speculation.insider_form4 | NVDA 董事 Stevens Form 4 出脫約 $385m | insider selling Form 4 September 2026 Nvidia AI executives SEC filing | https://www.sec.gov/Archives/edgar/data/0001045810/000119903926000012/wk-form4_1788387031.xml （SEC EDGAR） | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| speculation.equity_put_call | equity put/call 約 0.67 | Cboe equity put call ratio September 2026 reading | https://www.thetrading.tools/put-call-ratio （thetrading.tools） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 $40.74bn；資金流出約 $751m | leveraged ETF assets under management September 2026 record single stock | https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/ （ETF Action） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval September 2026 | 檢查來源：SEC EDGAR、ETF.com 新上市 feed | — | 2026-09-13T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比約 62%（8 月紀錄） | 0DTE options share SPX volume September 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august （Cboe） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.options_volume | OCC 2026-08 月總結算量約 1.44 十億口 | OCC options volume August 2026 monthly report | https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/ （Traders Magazine / OCC） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 收在約 17 以上、call skew 第 91 百分位 | fear gauge VIX hedges September 10 2026 volatility | https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html （CNBC） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 $1.42T（2026-07 月資料） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php （CurrentMarketValuation） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Qualcomm 對 Amazon 認股權證約 $4bn（資料中心基礎設施交易） | Qualcomm warrants Amazon 4 billion AI infrastructure deal September 2026 | https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html （CNBC） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-09-13",
  "iso_week": "2026-W37",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-03-14",
  "prior_date": "2026-09-03",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 4.21,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

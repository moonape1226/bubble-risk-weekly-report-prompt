> [DRY RUN] this report was not committed to archive.

# 2026-08-06 AI 泡沫破裂預測報告
報告日期：2026-08-06｜ISO 週次：2026-W32｜預測窗口：2026-08-06 → 2027-02-04｜前次基準：report-2026-08-03（3天前）

## 結論

**結論：no**

三條路徑都沒有在 182 天內完成的具體跡象。R1 方面，NASDAQ-100 已從 7/29 低點反彈，距 52 週高點回撤 3.83%，還要再跌約 22% 才觸及門檻（`valuation.ndx_drawdown`，2026-08-05）。R2 方面，hyperscaler 7 月底財報季是上修 capex，不是下修（`ai.hyperscaler_capex`）。R3 方面，CoreWeave 信用重定價屬實，但目前仍是「加價續借」而非違約，HY OAS 也沒有跟著走闊（`monetary.hy_oas`）。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,487.79（2026-08-05）。252 個交易日最高收盤為 30,660.6（2026-06-02），目前距 52 週高點回撤 3.83%。R1 門檻水位是 22,995.45，從最新收盤還要再跌約 22.02% 才會觸及（`valuation.ndx_drawdown`）。7/29 收盤 27,192.31 是近期低點，之後連續反彈。S&P 500 為 7,723.55，高於 200 日均線 9.71%、高於 52 週均線 11.32%（`valuation.sp500_trend`）。價格仍處延伸狀態，均值回歸的空間存在。VIX 從 7/29 的 20.66 降到 15.81（-23.48%），同期 S&P 500 上漲 5.57%，沒有出現量價同漲的 crowded-optionality 讀數（`structural.vix_spx_comove`）。估值偏高：S&P 500 trailing P/E 29.74、Shiller CAPE 42.19（`valuation.sp500_pe_cape`）；margin debt $1.502T，YoY +51.5%（`retail.margin_debt`）。這些代表一旦下跌，跌幅可能很大，但不代表下跌的時點會落在窗口內。

**判讀：** 目前距門檻還很遠（還需再跌約 22%）。要在窗口內觸發，需要一個系統性催化：例如 AI 信用事件外溢、hyperscaler 財報季集體下修，或是美債標售／期限溢價推升長端殖利率，引發估值壓縮。目前沒有一項正在進行中。

### R2 資本支出收縮

2026-07-28 CNBC 報導，hyperscaler 2026 年 capex 指引持續上修，合計約 $725B；Alphabet 上修後股價反而遭賣壓（`ai.hyperscaler_capex`）。逐家看：Alphabet 是上修。Microsoft、Amazon、Meta 本次證據只顯示整體「續上修」的報導口徑，沒有個別指引數值，因此方向記為「依報導未見下修」，個別數值本次不臆測。四家中目前下修家數為 0。需求側沒有轉弱跡象：HBM/DRAM 合約價續升，H200 租金約 $4.39/hr，供給缺口延續到 1H2027（`ai.compute_supply_demand`）。Microsoft RPO 約 $678B，其中約 32% 繫於單一客戶 OpenAI（`ai.customer_concentration_rpo`），屬集中度風險。下一次財報日期本次證據未載明；窗口到 2027-02-04 為止，涵蓋其後兩個季度的財報季。

**判讀：** R2 目前朝反方向走。四家剛上修完，要在兩個財報季內有兩家正式下修，通常得先出現 R1 等級的市場衝擊，或 AI 客戶（如 OpenAI）付款能力出問題。目前證據只顯示「投資人開始質疑 capex」，還沒有任何公司鬆動指引。

### R3 AI 信用事件

符合 R3 規模門檻的借款人中，壓力最明顯的是 CoreWeave。2026-08-03 報導，CoreWeave 5Y CDS 約 855bp，一筆 $2.6B 貸款利差 +125bp，貸方要求加強 covenants；同一報導列 Oracle CDS 約 215bp（`valuation.ai_credit_schism`）。2026-07-29 CoreWeave 為一筆繫於 Anthropic 合約的 $2.6B 貸款調高票息；Nebius 於 2026-07-17 取得 $775M 擔保融資（`structural.ai_infrastructure_debt`）。這代表 AI 信用定價分歧（equity-vs-credit schism）中的信貸端已開始重定價，是後期訊號。不過重定價的形式是「加價後仍能融資」，證據中沒有付款違約、covenant waiver、distressed exchange 或 going-concern 字樣。廣義信用市場也沒有跟著走：HY OAS 2.73%（2026-08-04，較前次 -5bp）、IG OAS 0.78%（持平）（`monetary.hy_oas`、`monetary.ig_oas`）。repo 資金壓力（SOFR−IORB）僅 1bp，SRF 動用 $0.001bn（`monetary.repo_stress_srf`）。近期到期與再融資牆的具體日期本次證據未載明。

**判讀：** R3 是三條路徑中最接近的一條，但仍有距離。855bp CDS 反映市場對違約有實質定價，但 R3 要求窗口內實際發生破產、超過寬限期的違約或 distressed exchange。CoreWeave 在 7/29 仍能完成加價融資，表示市場尚未關門。會把它推過門檻的是：再融資失敗、主要客戶合約重談，或 covenant 觸發後被迫交換債務。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 約 855bp，$2.6B 貸款利差 +125bp，貸方要求 covenants（2026-08-03），顯示 AI 基建信貸端已開始重定價；R3 規模門檻內的借款人出現實質違約定價（`valuation.ai_credit_schism`）。
- [R3] CoreWeave 2026-07-29 為繫於 Anthropic 的 $2.6B 貸款調高票息，融資成本持續上升，屬 AI infrastructure debt financing / vendor-financing loops 的壓力點（`structural.ai_infrastructure_debt`）。
- [R2] Microsoft RPO 約 $678B，其中約 32% 繫於 OpenAI 單一客戶（2026-07-30），backlog 集中度高，若單一客戶支付能力出問題可能衝擊 capex 規劃（`ai.customer_concentration_rpo`）；AI 終端年化營收約 $72B，對比年化 capex 約 $725B（分母：CNBC 報導之 hyperscaler 合計口徑），AI 營收對 capex 缺口（revenue-to-capex gap）約 10 倍（`ai.revenue_capex_gap`）。
- [R1] 估值與槓桿極端：Shiller CAPE 42.19、trailing P/E 29.74（2026-08-05，`valuation.sp500_pe_cape`）；margin debt $1.502T、YoY +51.5%（2026-06 月資料，`retail.margin_debt`）；S&P 500 高於 200 日均線 9.71%（`valuation.sp500_trend`），一旦下跌，跌幅空間大。
- [整體] 美債標售需求（auction tail / bid-to-cover）轉弱：5Y 標售連續 14 次 tail，bid-to-cover 為 2022-09 以來最差，7Y tail 0.8bp（2026-07-28，`monetary.treasury_auctions`）；10Y 期限溢價（term premium）0.8681%，trailing 7 日 +3bp（`monetary.term_premium`）。長端財政壓力是估值壓縮的潛在催化。
- [R1] Alphabet 上修 capex 後股價遭賣壓（2026-07-28，`ai.hyperscaler_capex`），市場開始懲罰 capex 擴張，情緒拐點的早期跡象。

## 支持 no 的證據

- [R1] NASDAQ-100 2026-08-05 收盤 29,487.79，距 52 週高點回撤 3.83%，較前次預測紀錄的 7.78% 收斂；需再跌約 22.02% 才觸及 R1 門檻 22,995.45（`valuation.ndx_drawdown`）。
- [R2] hyperscaler 2026 capex 指引 7 月底續上修，合計約 $725B；四家下修家數為 0（2026-07-28，`ai.hyperscaler_capex`）。需求側 HBM/DRAM 合約續升，GPU 供給缺口延續到 1H2027（2026-08-01，`ai.compute_supply_demand`），近期沒有削減 capex 的基本面理由。
- [R3] 個別 AI 信用壓力未外溢到整體信用市場：HY OAS 2.73%（2026-08-04，較 2026-08-03 -5bp）（`monetary.hy_oas`），IG OAS 0.78% 持平（`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）1bp、SOFR99−IORB 9bp（`monetary.repo_stress_srf`）。
- [整體] 7/29 的壓力讀數已消退：VIX 從 20.66 降到 15.81（-23.48%），同期 S&P 500 +5.57%（2026-07-29 → 2026-08-05，`structural.vix_spx_comove`）；MOVE 從 80.48 降到 73.58（2026-08-05，`structural.treasury_basis_trade`）。
- [R3] AI 基建融資管道仍然暢通：CoreWeave 7/29 加價後仍完成 $2.6B 融資，Nebius 7/17 取得 $775M 擔保（`structural.ai_infrastructure_debt`）。R3 要求的是違約或 distressed exchange，不只是利差走闊。
- [整體] 情緒尚未極端：CNN Fear & Greed 約 58（Greed，2026-08-05，`retail.fear_greed`）；AAII Bear 42.1%、Bull 31.0%（2026-07-30，`retail.aaii`）；等權 RSP YTD +14.26% 領先 SPY +13.71%（`breadth.rsp_spy`），上漲並非只靠少數權值股。

## 與前期比較

前次結論：yes（report-2026-08-03）
本次結論：翻轉
翻轉依據：
- `valuation.ndx_drawdown`（資料日 2026-08-05）：NASDAQ-100 回撤由前次紀錄的 r1_drawdown_pct 7.78 收斂到 3.83，觸及 R1 門檻所需的跌幅由約 18.7% 擴大到約 22.0%。7/29 的低點沒有延續成趨勢性下跌，R1 路徑從「已在進行中」退回「需要新催化」。
- `monetary.hy_oas`（資料日 2026-08-04）：CoreWeave 信用重定價（2026-08-03，與前次同日，因此不作為翻轉依據）之後，HY OAS 反而收窄 5bp 至 2.73%。R3→R1 的傳導鏈（單一 AI 借款人壓力 → 廣義信用 → 股市）目前沒有在發生。
- `structural.vix_spx_comove`（as-of 2026-08-05）：VIX 7 日 -23.48%、S&P 500 +5.57%，7/29 壓力事件已消退，不支持「壓力正在擴散」的判讀。
- 說明：前次存檔只有 forecast.json，前次 yes 的完整推理本次無法逐條核對。翻轉只依據上列 2026-08-03 之後的資料；CoreWeave 利差、Alphabet capex 賣壓、5Y 標售 tail 等 2026-08-03 當日或之前的證據，都不作為翻轉依據。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下為 ✗ NOT DISCLOSED（檢索完成但窗口內無合格披露），並說明對結論的可能影響：
- `retail.naaim`、`institutional.bofa_jpm_survey`：屬持倉／情緒交叉檢查，缺漏不影響結論。
- `monetary.private_credit_liquidity`：30 日內沒有 BDC 的 redemption-request ratio、gate proration / breach，或 net inflow→outflow flip 披露。若後續出現多檔基金贖回壓力上升，會強化 R3 路徑，是可能改變結論的缺口之一。
- `ai.token_growth`、`ai.depreciation_life`：需求側與盈餘品質訊號，缺漏不影響目前判讀。
- `ai.hyperscaler_financing_mix`：quarterly_state 有資料（2026-07-24：top-5 capex 已超過 FCF，2026 年發債約 $182B），但 30 日 event_scan 沒有新的融資事件，依 all 聚合規則整體記為 ✗ NOT DISCLOSED，本文不引用。
- `ai.capital_cycle`：兩個組件都沒有可引證的增速對比，增速證據不足，本次不判定週期階段。
- `structural.global_leveraged_approvals`：7 日內沒有英文披露，不影響結論。
- `speculation.insider_form4`：SNOW／TEM 的線索缺少完整 Form 4 欄位（filing date 與 transaction date 未分列；TEM 缺 URL 與金額），依規則記為 0 件。

最大的不確定性：
1. CoreWeave 再融資與 covenant 走向：若 855bp CDS 演變成再融資失敗或 distressed exchange，R3 會直接成立，並可能經信用外溢觸發 R1。這是把結論推向 yes 的首要風險。
2. 下兩個 hyperscaler 財報季（窗口涵蓋）：若市場對 capex 的懲罰（如 Alphabet 7/28）迫使兩家改為下修，R2 成立；目前方向相反。這項偏向 no，但屬尾部風險。
3. 美債長端：5Y 連續 tail 加上期限溢價上升、FedWatch 9 月定價分歧（`monetary.fedwatch`），若長端殖利率急升引發估值壓縮，R1 的距離可能快速縮短。這會把結論推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7723.55 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 9.71 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 11.32 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29487.79 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 3.83 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026-Q1，家庭股票配置 %） | 45.76080873390133（約 45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.73 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps（vs 2026-08-03） | -5.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%；ΔDGS10 -7bp） | 4.63 | FRED API (series_id=DGS10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%；ΔDFII10 -3bp） | 2.4 | FRED API (series_id=DFII10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%；ΔT10YIE -5bp，視窗與 DGS10/DFII10 不一致，driver 不可判（視窗不一致）） | 2.22 | FRED API (series_id=T10YIE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD；no_new_obs，持平） | 81.96 | FRED API (series_id=DCOILWTICO) | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料，YoY %） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-08-06T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%；Δ -5bp） | 2.26 | FRED API (series_id=T5YIFR) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%；trailing 7 日 +3bp） | 0.8681 | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.66 | FRED API (series_id=SOFR) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%；SOFR99−IORB 9bp，2026-08-04 同日對齊） | 3.74 | FRED API (series_id=SOFR99) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-06 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.001（$1M） | FRED API (series_id=RPONTTLD) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.walcl | WALCL latest（百萬美元；no_new_obs） | 6738190.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（百萬歐元；no_new_obs） | 5941248.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（億日圓；no_new_obs） | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.81 | FRED API (series_id=VIXCLS) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as-of；base 2026-07-29，window_days 7，comove false） | 15.81 | FRED API (series_id=VIXCLS, SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | -23.48 | FRED API (series_id=VIXCLS, SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | 5.57 | FRED API (series_id=VIXCLS, SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（十億美元；no_new_obs） | 2004.9941（$2.00T） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-22 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口；delta_4w -52919） | -7481041 | CFTC TFF futures-only | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（^MOVE；前值 80.48） | 73.58 | Yahoo Finance chart API (^MOVE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2342.8 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | SSGA 市場評論 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報摘要 WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | financecharts WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | P&I WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | StockCharts breadth WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA／Advisor Perspectives WebSearch | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag WebSearch（7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／YCharts WebSearch | ✗ NOT DISCLOSED（無當週值） |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED（無新調查） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（DFEDTARU ok、DFEDTARL ok） | ✓ API |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE FRED-direct） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok；repo_stress ok） | ✓ API |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | 標售 recap WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要 WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | investing.com WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無合格披露） |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報／財經媒體 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch AI 彙整 WebSearch（最近一次披露） | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話／媒體 WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | jarvislabs／TrendForce WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：Sage Advisory WebSearch；event_scan：30d 發債／私募信貸掃描，無新事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合既有披露 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無變動） |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速對比＋30d 進出場事件 WebSearch，兩組件皆無可引證披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | Reuters／Benzinga／BusinessWire WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | Renaissance Capital WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／StockAnalysis／StockTitan gainers 螢幕（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | YCharts WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing／etf.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire 發行公告 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED（7 日內無英文披露） |
| structural.zero_dte | 結構｜0DTE option volume | Cboe 季報摘要 WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe insights WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS ok、vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用散戶 margin debt（Advisor Perspectives） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | Bloomberg 等 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok）；WebSearch 無新增事件 | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.74（原定來源 multpl） | S&P 500 trailing P/E August 5 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.19 | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 約 29x vs 指數約 25.6x，溢價壓縮 | Magnificent 7 valuation premium lowest decade 2026 | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026 （SSGA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA TP $285→$288，EPS-driven（EPS Δ、target PE Δ 未披露） | Morgan Stanley NVDA target 288 July 2026 AI demand | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044 （Investing.com） | 2026-07-13 | 2026-08-06T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 約 855bp、$2.6B 貸款利差 +125bp、Oracle CDS 約 215bp | CoreWeave CDS spread blows out 125 covenants Oracle August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm （Tech Times） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 總報酬 +14.26% vs SPY +13.71% | RSP vs SPY equal weight total return YTD August 2026 | https://www.financecharts.com/etfs/SPY/performance/total-return （FinanceCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度約 41% | S&P 500 top 10 concentration percent record 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/ （P&I） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| breadth.advance_decline | 約 64% 成分股在 50DMA 上、A/D 創高、McClellan 轉負 | S&P 500 breadth percent above 50 day moving average August 2026 McClellan | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/ （StockCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 58（Greed） | CNN Fear and Greed Index August 5 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-06 月資料）$1.502T，YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives，原定 FINRA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| retail.aaii | AAII Bear 42.1%／Neutral 26.9%／Bull 31.0% | AAII investor sentiment survey July 30 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| retail.social_sentiment | WSB「Save Wendy's」WEN 軋空討論，空頭比約 44% | Reddit WSB Wendy's WEN short squeeze August 2026 | https://finance.yahoo.com/markets/stocks/articles/reddit-wants-save-wendy-inside-161925726.html （Yahoo Finance） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.treasury_auctions | 5Y 連 14 次 tail、bid-to-cover 為 2022-09 以來最差；7Y tail 0.8bp | US Treasury 5 year 7 year auction tail bid to cover July 2026 | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026 （TFTC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| monetary.fedwatch | FOMC 7/29 鷹派持平；FedWatch 9 月約 62%，定價分歧 | CME FedWatch September 2026 probability FOMC hold | https://growbeansprout.com/tools/fedwatch （Beansprout，原定 CME FedWatch） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.pboc | 人行逆回購合計約 ¥2.1T；7/24 MLF 淨投放 ¥100B | PBoC reverse repo injection 2.1 trillion yuan late July 2026 | https://www.investing.com/news/economy-news/chinas-pboc-to-conduct-overnight-reverse-repos-inject-a-total-of-21-trillion-yuan-4810853 （Investing.com） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 續上修，合計約 $725B；Alphabet 上修後遭賣壓（Q2 財報季） | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic run-rate 約 $47B、OpenAI 約 $25B | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-06-15 | 2026-08-06T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO 約 $678B，約 32% 繫於單一客戶 OpenAI | Microsoft RPO backlog 678 billion single customer OpenAI 2026 | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/ （Benzinga via TradingView） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| ai.compute_supply_demand | HBM/DRAM 合約續升、H200 租金約 $4.39/hr、缺口延至 1H2027 | H200 GPU rental price HBM DRAM contract 2026 shortage 2027 | https://jarvislabs.ai/blog/h200-price （Jarvislabs） | 2026-08-01 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超過 FCF、2026 發債約 $182B、表外結構逾 $120B | hyperscaler capex FCF debt issuance 182 billion off balance sheet SPV 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure （Sage Advisory） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.revenue_capex_gap | AI 終端年化營收約 $72B（Anthropic $47B＋OpenAI $25B，2026-06-15）vs 年化 capex 約 $725B（分母：CNBC hyperscaler 合計口徑，2026-07-28） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI）；分母見 ai.hyperscaler_capex 列 | 2026-06-15 | 2026-08-06T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收投機 IPO 螢幕：合格 0 件 | AI rename ticker SPAC no revenue IPO July 30 August 6 2026 | Reuters／Benzinga／BusinessWire SPAC 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.ipo_heat | 本週約 21 檔定價、無 blowout 首日、YTD 約 $251B／86 檔 | US IPO pricings week August 3 2026 Renaissance | https://www.renaissancecapital.com/IPO-Center/Pricings （Renaissance Capital） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot 合格 0 件 | microcap 100% single day quantum fusion space nuclear small cap August 2026 | Finviz／StockAnalysis／StockTitan gainers 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標約 $1T IPO、Anthropic 續進 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground （Benzinga） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| speculation.insider_form4 | Form 4 合格 0 件（SNOW／TEM 線索缺完整 filing／transaction 日期分列，TEM 缺 URL 與金額，不予列名） | Snowflake Dageville Tempus Lefkofsky Form 4 insider sale July 2026 SEC | SEC EDGAR Form 4 檢索（browse-edgar） | — | 2026-08-06T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.55（日值或 5 日均未標明） | Cboe equity put call ratio August 3 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio （YCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高約 $198B（個別 NVDL／TSLL 等未分列） | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing，原定 etf.com） | 2026-07-23 | 2026-08-06T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x 單股槓桿 ETF＋ELOL（TSLA+SpaceX） | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量約 65%（Cboe Q2 2026） | 0DTE SPX options share volume Cboe Q2 2026 65% | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641 （Investing.com） | 2026-05-31 | 2026-08-06T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 總量 16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 約 139.96、VIX 約 16.9 contango、TLT 1M skew 創 GFC 以來高 | VIX SKEW term structure bond volatility August 3 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher （Cboe） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt（2026-06 月資料）$1.502T、YoY +51.5%（交叉檢查，不重複計） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B Anthropic 掛鉤貸款 07-29 調高票息；Nebius $775M 擔保 07-17 | CoreWeave 2.6 billion loan Anthropic yield boosted July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic （Bloomberg） | 2026-07-29 | 2026-08-06T09:30:00+08:00 |

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
  "prior_answer": "yes",
  "flip_evidence": ["valuation.ndx_drawdown", "monetary.hy_oas", "structural.vix_spx_comove"],
  "r1_drawdown_pct": 3.83,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

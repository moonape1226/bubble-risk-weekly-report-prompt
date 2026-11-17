> [DRY RUN] this report was not committed to archive.

# 2026-08-17 AI 泡沫破裂預測報告

報告日期：2026-08-17｜ISO 週次：2026-W34｜預測窗口：2026-08-17 → 2027-02-15｜前次基準：report-2026-08-13（4天前）

## 結論

**結論：no**

三條路徑都沒有在 182 天內走完的跡象。NASDAQ-100 距 52 週高點回撤只有 2.00%，還要再跌約 23.47% 才觸及 R1（`valuation.ndx_drawdown`）；hyperscaler 2026 年 capex 合計約 $725B 而且仍在上修，R2 方向相反（`ai.hyperscaler_capex`）。CoreWeave 的信用利差急速走闊（5Y CDS 約 855bp），是 R3 唯一的實質壓力點，但它剛完成 $2.6B 再融資，沒有違約或 distressed exchange 的證據（`structural.ai_infrastructure_debt`），不足以推翻「多數 182 天窗口不會發生 R1–R3」的 base rate。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 30,046.14（2026-08-14）；252 個交易日最高收盤 30,660.6（2026-06-02）；距 52 週高點回撤 2.00%。R1 門檻水位 22,995.45，從最新收盤還要再跌約 23.47% 才觸及（`valuation.ndx_drawdown`）。同期 S&P 500 收在 7,785.76，高於 200 日均線 10.05%、高於 52 週均線 11.6%（`valuation.sp500_trend`）。價格偏離偏大，但避險指標沒有跟著升溫：VIX 14.63，trailing 7 日（2026-08-06 → 2026-08-13）下跌 3.43%，S&P 500 同窗上漲 1.15%，沒有出現 crowded-optionality 的同漲讀數（`structural.vix_spx_comove`）。估值處在高位：CAPE 42.2、trailing P/E 29.8（`valuation.sp500_pe_cape`），margin debt $1.502T、YoY +51.5%（`retail.margin_debt`）。這些說明一旦下跌，幅度可能很大，但不代表下跌會在窗口內開始。

**判讀：** R1 離門檻很遠，價格仍貼近高點。要在窗口內觸發，需要約 23% 以上的急跌，前提通常是外部觸發點，例如 AI 信用事件外溢、capex 指引轉向，或利率／期限溢價急升造成的強迫去槓桿。高 margin debt 和槓桿 ETF 規模會放大下跌，但目前看不到觸發點已經出現。

### R2 資本支出收縮

本次來源只取得四大 hyperscaler 的合計：2026 年 capex 合計約 $725B，最近一輪（2026 Q2）財報後仍在上修（`ai.hyperscaler_capex`，CNBC 2026-07-28）。Microsoft、Alphabet、Amazon、Meta 各自的指引數字與方向，本次來源沒有分別建立，所以逐家狀態只能寫成：方向未分別取得，合計為上修。已證實下修的家數是 0／4。下一輪財報落在窗口內，但具體日期本次來源沒有取得。需求面沒有轉弱：HBM 合約價約 +40%、H200 租金中位約 $3.99/hr、Blackwell 售罄（`ai.compute_supply_demand`），Microsoft 商用 RPO 約 $678B（`ai.customer_concentration_rpo`）。壓力在融資面與回報面：top-5 capex 已超過 FCF（Alphabet Q2 FCF 轉負），2026 年發債約 $182B（`ai.hyperscaler_financing_mix`）；AI 營收對 capex 缺口（revenue-to-capex gap）沿用最近組合值：年化 AI 終端營收約 $72B vs 年化 capex 約 $725B（分母：top-4＋Oracle），而且這不是新證據（`ai.revenue_capex_gap`，資料日 2026-06-15）。

**判讀：** R2 目前朝反方向走，指引仍在上修。要在窗口內觸發，需要四家中至少兩家在後續財報或 8-K 下修指引。可能的推力有三個：股價大幅下跌（R1 傳導）、債市對 hyperscaler 融資結構（capex vs FCF / 發債）重定價，或 AI 終端需求明顯放緩。目前 GPU 與記憶體仍然短缺，短期內同時出現兩家下修的條件不成立。

### R3 AI 信用事件

AI infrastructure debt financing / vendor-financing loops 的主要壓力點是 CoreWeave。它在 2026-07-29 完成 $2.6B 貸款，但被迫調高利差 +100–125bp 並接受 covenant；5Y CDS 約 855bp（`structural.ai_infrastructure_debt`）。2026-08-03 的報導顯示 AI loan 投資人要求 covenant，Oracle CDS 也來到多年高點（`valuation.ai_credit_schism`）。這是 AI 信用定價分歧（equity-vs-credit schism）的後期訊號：信貸端已經開始重定價，股權端仍貼近高點。CoreWeave 的總負債是否達到 R3 的 50 億美元門檻，本次來源沒有建立；本次也沒有取得任何借款人出現付款違約、寬限期、distressed exchange 或 going-concern 語句的證據。整體信用環境仍然寬鬆：HY OAS 2.71%（`monetary.hy_oas`）、IG OAS 0.79%（`monetary.ig_oas`），repo 資金壓力（SOFR−IORB）為 −3bp，SRF 動用（Standing Repo Facility usage）為 0（`monetary.repo_stress_srf`）。Meta El Paso 資料中心的表外債券結構超過 $12B（`ai.hyperscaler_financing_mix`），說明 R3 相關的表外融資規模還在擴大。

**判讀：** R3 是三條路徑中最接近壓力區的一條，但距離「破產申請／超過寬限期的付款違約／完成 distressed exchange」仍有好幾步。CoreWeave 剛完成再融資，代表市場仍願意以較高代價供給資金。要在窗口內觸發，需要大型 AI 算力借款人的再融資窗口關閉，或客戶合約（例如單一大客戶）出現違約連鎖。目前廣義信用利差偏緊，系統性融資壓力還不支持這一步。

## 支持 yes 的證據

- [R3] CoreWeave $2.6B 貸款（2026-07-29）被迫調高利差 +100–125bp 並附加 covenant，5Y CDS 約 855bp，是 AI 算力借款人信用重定價的直接證據（`structural.ai_infrastructure_debt`）。
- [R3] 2026-08-03 報導：AI loan 投資人要求 covenant，CoreWeave 利差暴走 125bp，Oracle CDS 處於多年高點。信貸端先於股權端轉弱（`valuation.ai_credit_schism`）。
- [R2] top-5 hyperscaler capex 已超過 FCF（Alphabet Q2 FCF 轉負），2026 年發債約 $182B（2026-07-24）。另有 Meta El Paso 表外結構超過 $12B（2026-07-20），擴張越來越依賴舉債（`ai.hyperscaler_financing_mix`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 $72B vs 年化 capex 約 $725B（分母：top-4＋Oracle；2026-06-15 組合值），回報落差極大（`ai.revenue_capex_gap`）。
- [R1] 估值與槓桿處於極端水位：CAPE 42.2、P/E 29.8（2026-08-14，`valuation.sp500_pe_cape`）；margin debt $1.502T、YoY +51.5%（2026-06 月資料，`retail.margin_debt`）；US 槓桿 ETF AUM 約 $198B 創新高（`structural.leveraged_etf_aum`）。
- [整體] Microsoft 商用 RPO 約 $678B，其中約 32% 繫於單一客戶 OpenAI（2026-07-30），集中度造成單點失效風險（`ai.customer_concentration_rpo`）；BofA 8 月 FMS 淨 41% 預期成長轉弱（`institutional.bofa_jpm_survey`）。

## 支持 no 的證據

- [R1] NASDAQ-100 2026-08-14 收盤 30,046.14，距 52 週高點回撤 2.00%，離 R1 門檻 22,995.45 還差約 23.47%（`valuation.ndx_drawdown`）。
- [R2] hyperscaler 2026 年 capex 合計約 $725B，Q2 財報後仍在上修（2026-07-28），目前四家中證實下修者為 0（`ai.hyperscaler_capex`）。
- [R2] 算力供需偏緊：HBM 合約價約 +40%、H200 租金約 $3.99/hr、Blackwell 售罄（2026-08-01），看不到產能過剩或訂單消化（`ai.compute_supply_demand`）。
- [R3] 廣義信用利差偏緊：HY OAS 2.71%（`monetary.hy_oas`）、IG OAS 0.79%（`monetary.ig_oas`），資料日 2026-08-13；repo 資金壓力（SOFR−IORB）−3bp、SRF 動用 0（`monetary.repo_stress_srf`），系統性融資壓力未現。
- [整體] 波動與避險指標平靜：VIX 14.63，trailing 7 日下跌 3.43%，未出現與 S&P 500 同漲（`structural.vix_spx_comove`）；MOVE 69.58（`structural.treasury_basis_trade`）；過去 14 日 AI 領導股合格 Form 4 賣壓 cluster 0 件（`speculation.insider_form4`）。
- [整體] 投機篩檢沒有過熱事件：過去 7 日 +AI 改名／SPAC 0 件（`speculation.ai_rename_spac`），microcap thematic moonshot 0 件（`speculation.microcap_moonshots`）。

## 與前期比較

前次結論：無前次預測（report-2026-08-13 為舊格式評分報告）

- 舊格式評分不轉譯為 yes/no；本次為新格式下的首個預測，flip_evidence 為空。
- 自 2026-08-13 以來的 macro 變動很小：S&P 500 −0.17%（7,798.99 → 7,785.76），T10YIE +3bp，T5YIFR +3bp，DGS10／DFII10 無新觀測（Δ 為 0）。10Y 分解的判讀為 不可判（視窗不一致），stale_series 為 DGS10、DFII10。
- 10Y 期限溢價（term premium）0.8257%（2026-08-07），trailing 7 日 −4.2bp（`monetary.term_premium`），財政再定價壓力略為降溫。
- 美債基差交易槓桿（Treasury basis-trade leverage）：槓桿基金淨空 7,250,927 口（2026-08-11），4 週淨空減少 311,947 口（`structural.treasury_basis_trade`），部位小幅收斂、未見平倉事件。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `breadth.rsp_spy`（required）：唯一取得的 RSP vs SPY YTD 數據（+9.67% vs +8.38%）資料日為 2026-06-10，對本次報告日而言並非當前快照，因此不作證據使用。這是廣度確認指標，不會改變三條路徑的判讀，不影響本次結論。

本次以 ✗ NOT DISCLOSED 處理、不作證據的來源包括：analyst TP decomposition（唯一結果是 Susquehanna 的 TSMC 目標上修，不屬於指定的 top-tier 賣方，也沒有 EPS／PE 拆解數值）、美債標售需求（auction tail / bid-to-cover）（結果宣稱 30Y 2026-08-13 標售 BTC 2.39，但結果 URL 是 10 年期標售報導，數值與來源無法對應）、OpenAI／Anthropic 年化營收（唯一結果資料日 2026-05-29，屬前一季；而且報導標題的 $30B 與摘要的 $47B 不一致），以及私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）、折舊年限變動（depreciation useful-life change）、資本週期階段（capital cycle stage）、token growth、NAAIM、社群情緒、PBoC、全球槓桿產品核准等篩檢的無披露結果。其中私募信貸與折舊年限兩項若有披露，可能影響 R3 與 R2 的判讀，但本次沒有可用的現行事件。

最大的不確定性：

1. CoreWeave 的總負債與到期結構本次未建立。若後續揭露其負債明顯超過 50 億美元，且再融資條件持續惡化，R3 的距離會縮短，結論會往 yes 推。
2. 下一輪 hyperscaler 財報（具體日期本次未取得）是 R2 的主要觸發點。若 Alphabet 等在 FCF 轉負後選擇收斂指引，會往 yes 推；目前證據是持續上修。
3. OpenAI IPO 進程（報導目標 9 月上市、估值約 $730–850B，`speculation.upcoming_ai_ipos`）。上市成功會延續資金供給（往 no 推）；若受挫可能引發 AI 估值與 RPO 品質的重估（往 yes 推）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7785.76 | FRED API (series_id=SP500) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線偏離 %） | 10.05 | FRED API (series_id=SP500) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線偏離 %） | 11.6 | FRED API (series_id=SP500) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 30046.14 | FRED API (series_id=NASDAQ100) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-17T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 2.0 | FRED API (series_id=NASDAQ100) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q1，家庭股票配置 %） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-17T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-16 | 2026-08-17T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-16 | 2026-08-17T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 2.71 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（IG OAS %） | 0.79 | FRED API (series_id=BAMLC0A0CM) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（10Y 殖利率 %） | 4.63 | FRED API (series_id=DGS10) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（10Y 實質殖利率 %） | 2.39 | FRED API (series_id=DFII10) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（10Y breakeven %） | 2.27 | FRED API (series_id=T10YIE) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps（較 2026-08-13） | 3.0 | FRED API (series_id=T10YIE) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（WTI 美元／桶） | 84.77 | FRED API (series_id=DCOILWTICO) | 2026-08-11 | 2026-08-17T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月 CPI YoY %） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-17T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（5y5y forward %） | 2.3 | FRED API (series_id=T5YIFR) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（10Y 期限溢價 %，Kim-Wright） | 0.8257 | FRED API (series_id=THREEFYTP10) | 2026-08-07 | 2026-08-17T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 日） | -4.2 | FRED API (series_id=THREEFYTP10) | 2026-08-07 | 2026-08-17T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API (series_id=SOFR99) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-17 | 2026-08-17T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（Fed 隔夜 repo 操作 transaction volume，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| monetary.walcl | WALCL latest（Fed 資產負債表） | 6759955.0（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-12 | 2026-08-17T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（ECB 資產負債表） | 5923023.0（€5.92T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-07 | 2026-08-17T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（BOJ 資產負債表） | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-17T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 14.63 | FRED API (series_id=VIXCLS) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（trailing 7 日窗終點） | 14.63 | FRED API (series_id=VIXCLS / SP500) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（2026-08-06 → 2026-08-13） | -3.43 | FRED API (series_id=VIXCLS / SP500) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（同窗） | 1.15 | FRED API (series_id=VIXCLS / SP500) | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（銀行對 NBFI 放款） | 2016.0821（$2.02T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-05 | 2026-08-17T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（槓桿基金美債期貨淨部位，口） | -7250927 | CFTC TFF futures-only | 2026-08-11 | 2026-08-17T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 311947 | CFTC TFF futures-only | 2026-08-11 | 2026-08-17T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（^MOVE） | 69.58 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2381.8 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-08-14 | 2026-08-17T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl / gurufocus [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | Fool / SSGA 搜尋 | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報搜尋（90d＋同季） | ✗ NOT DISCLOSED（僅 Susquehanna TSMC，非指定 top-tier、無 EPS/PE 拆解） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場搜尋（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) YTD divergence | 24/7 Wall St 搜尋 | ⛔ FETCH FAILED（僅取得 2026-06-10 舊快照，無當前值） |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | RBC / 財經媒體搜尋 | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | Investing.com breadth 搜尋（以 >50DMA 比例為 proxy） | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | FINRA / Advisor Perspectives 搜尋 | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB / cashtag 搜尋（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim / YCharts [primary: SEARCH] | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查搜尋 | ✓ SEARCH-VERIFIED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED DFEDTARU / DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED CPIAUCSL | scripts/fetch_macro.py（yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED THREEFYTP10 | scripts/fetch_macro.py | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py（SOFR / SOFR99 / IORB / RPONTTLD） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | Reuters / RTTNews recap [primary: SEARCH]（14d） | ✗ NOT DISCLOSED（結果 URL 為 10 年期標售，與 30Y 數值無法對應） |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED WALCL | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（ECBASSETSW / JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | investing / Yicai 搜尋 | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露搜尋（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報搜尋（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic / OpenAI / Google 披露搜尋 | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | 報導搜尋（當季） | ✗ NOT DISCLOSED（唯一結果屬前一季 2026-05-29） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce / jarvislabs [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報／發債搜尋；quarterly_state stock-of-state＋event_scan 30d | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露搜尋（carry-forward） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K / 10-Q 搜尋（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速＋進出場事件搜尋；quarterly_state stock-of-state＋event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | Reuters / Benzinga / SEC 螢幕（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | IPOScoop / Renaissance 搜尋（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz / StockAnalysis gainers [primary: SEARCH]（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | S-1／具名報導搜尋（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR / openinsider / secform4 螢幕（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe / thetrading.tools [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com / cryptobriefing [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | SEC EDGAR / 發行商新聞稿搜尋（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX / TWSE / JPX / ESMA 搜尋（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe 搜尋 | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC monthly | theocc.com 搜尋 | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe 搜尋 | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 FINRA margin debt 搜尋 | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds / move_index / ofr_repo）；WebSearch 補充無披露 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.8、Shiller CAPE 42.2 | S&P 500 trailing P/E Shiller CAPE multpl August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio ；https://www.multpl.com/s-p-500-pe-ratio（gurufocus / multpl） | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E 約 29x vs 指數約 25.6x、佔市值約 33.9% | Magnificent 7 weighted PE vs S&P 500 August 2026 | https://www.fool.com/research/magnificent-seven-sp-500/（Motley Fool） | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 約 855bp、貸款利差 +100–125bp、Oracle CDS 多年高 | CoreWeave Oracle CDS spread AI credit widening August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm（Tech Times） | 2026-08-03 | 2026-08-17T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度約 37% | S&P 500 top 10 concentration percent 2026 | https://www.rbcwealthmanagement.com/en-us/insights/the-great-narrowing-sp-500-concentration（RBC Wealth Management） | 2026-07-24 | 2026-08-17T09:30:00+08:00 |
| breadth.advance_decline | S&P 500 成分股 >50DMA 比例約 71.6%（A/D 與 new high/low 的廣度 proxy） | S&P 500 percent above 50 day moving average August 2026 | https://www.investing.com/indices/s-p-500-stocks-above-50-day-average（Investing.com） | 2026-08-11 | 2026-08-17T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 65（Greed） | CNN Fear and Greed Index August 14 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives／FINRA） | 2026-07-20 | 2026-08-17T09:30:00+08:00 |
| retail.aaii | AAII Bull 38.5%／Neutral 23.3%／Bear 38.1%（週結束 2026-08-12） | AAII investor sentiment survey week August 12 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA 8 月 FMS：現金 3.9%、淨 41% 預期成長轉弱 | BofA Global Fund Manager Survey August 2026 cash levels | https://www.tradingview.com/news/macenews:d7660a8e2094b:0-bofa-global-research-fund-manager-survey-global-investors-increasingly-more-cautious-about-growth-and-inflation-in-august/（TradingView／MNI） | 2026-08-12 | 2026-08-17T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 9/16 會議約 69% 維持不變、無降息定價 | CME FedWatch September 2026 rate probability | https://growbeansprout.com/tools/fedwatch（Beansprout，CME FedWatch 摘要） | 2026-08-14 | 2026-08-17T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計約 $725B、Q2 財報後仍上修（2026 Q2 財報季） | hyperscaler capex 2026 725 billion raised Q2 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-08-17T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft 商用 RPO 約 $678B、約 32% 繫單一客戶 OpenAI | Microsoft RPO backlog 678 billion OpenAI 2026 | https://www.benzinga.com/trading-ideas/long-ideas/26/07/60816147/microsofts-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer（Benzinga） | 2026-07-30 | 2026-08-17T09:30:00+08:00 |
| ai.compute_supply_demand | HBM 合約約 +40%、H200 租金中位約 $3.99/hr、Blackwell 售罄 | H200 GPU rental HBM DRAM 2026 shortage Blackwell | https://jarvislabs.ai/blog/h200-price（Jarvislabs） | 2026-08-01 | 2026-08-17T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 超越 FCF（Alphabet Q2 FCF 轉負）、2026 發債約 $182B | hyperscaler capex FCF debt issuance 182 billion 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure（Sage Advisory） | 2026-07-24 | 2026-08-17T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan][spv_deal] Meta El Paso 資料中心 BlackRock 主導超過 $12B 債券（triple-net lease 表外結構） sponsor_equity_split=undisclosed; residual_value_guarantee=undisclosed; lease_term=20-30yr; debt_tenor=undisclosed; lead_lenders=BlackRock/JPMorgan/MS; | direct fetch（hyperscaler 融資結構 event_scan 結果頁） | https://www.landgate.com/news/blackrock-s-12-billion-bond-sale-signals-a-new-financing-playbook-for-data-center-developers（Landgate） | 2026-07-20 | 2026-08-17T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $72B vs 年化 capex 約 $725B（分母：top-4＋Oracle；carry-forward 組合值） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue（Epoch AI） | 2026-06-15 | 2026-08-17T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收投機 IPO 合格 0 件（過去 7 日） | AI rename ticker SPAC no revenue IPO August 10-17 2026 | 檢查來源：Reuters、Benzinga、SEC 螢幕 | — | 2026-08-17T09:30:00+08:00 |
| speculation.ipo_heat | 本週約 11 檔 IPO 定價、YTD 226 檔 | US IPO pricings week August 2026 IPOScoop | https://www.iposcoop.com/current-year-pricings/（IPOScoop） | 2026-08-17 | 2026-08-17T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot 合格 0 件（過去 7 日） | microcap 100% single day quantum fusion nuclear AI August 2026 | 檢查來源：Finviz、StockAnalysis gainers 螢幕 | — | 2026-08-17T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 9 月上市、估值約 $730–850B；Anthropic 續進 | OpenAI Anthropic IPO timing valuation 2026 | https://cryptobriefing.com/openai-ipo-filing-trillion-valuation/（Crypto Briefing） | 2026-07-28 | 2026-08-17T09:30:00+08:00 |
| speculation.insider_form4 | AI／領導股合格 Form 4 賣壓 cluster 0 件（過去 14 日） | AI leadership insider Form 4 sale August 3-17 2026 SEC | 檢查來源：openinsider、secform4、SEC EDGAR 螢幕 | — | 2026-08-17T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity-only put/call 0.54（日讀數） | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio（thetrading.tools） | 2026-08-07 | 2026-08-17T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 約 $198B（記錄高） | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing） | 2026-07-23 | 2026-08-17T09:30:00+08:00 |
| structural.us_single_stock_etf | 2026-08-11 新發 6 檔單股 2x 槓桿 ETF（Leverage Shares／Tradr） | single-stock leveraged ETF launch August 11 2026 Leverage Shares Tradr | https://www.globenewswire.com/news-release/2026/08/11/3342794/0/en/leverage-shares-by-themes-launches-three-new-2x-etfs-targeting-ai-infrastructure-and-connectivity-leaders.html（GlobeNewswire） | 2026-08-11 | 2026-08-17T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量約 65%（Cboe 2026 Q2） | 0DTE SPX options share Cboe Q2 2026 65% | https://ca.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4768656（Investing.com） | 2026-07-31 | 2026-08-17T09:30:00+08:00 |
| structural.options_volume | OCC 總量（2026-06 月資料）1,603,491,559 口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report（OCC） | 2026-07-02 | 2026-08-17T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 約 135、VIX 14.63、MOVE 約 75 | VIX SKEW MOVE bond volatility August 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-10-2026-spx-skew-collapses-on-upside-chasing（Cboe） | 2026-08-13 | 2026-08-17T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-06 月資料）$1.502T、YoY +51.5%（交叉確認，不重複計入） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026（Advisor Perspectives／FINRA） | 2026-07-20 | 2026-08-17T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B 貸款被迫調高利差 +100–125bp＋covenant、5Y CDS 約 855bp | CoreWeave 2.6 billion loan spread covenant CDS August 2026 | https://www.stocktitan.net/news/CRWV/core-weave-closes-2-6-billion-loan-facility-expanding-financing-gwhngwnf0jt5.html（StockTitan） | 2026-07-29 | 2026-08-17T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-17",
  "iso_week": "2026-W34",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-15",
  "prior_date": "2026-08-13",
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 2.0,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

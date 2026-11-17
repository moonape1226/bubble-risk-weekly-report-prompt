> [DRY RUN] this report was not committed to archive.

# 2026-07-23 AI 泡沫破裂預測報告

報告日期：2026-07-23｜ISO 週次：2026-W30｜預測窗口：2026-07-23 → 2027-01-21｜前次基準：report-2026-07-20（3天前）

## 結論

**結論：no**

三條路徑目前都沒有進行中的觸發：NASDAQ-100 距 52 週高點回撤 5.42%，離 R1 門檻仍需再跌約 20.70%；R2 方向相反，Alphabet 於 2026-07-22 Q2 財報上修 FY26 capex 至 ≈$205B（`ai.hyperscaler_capex`）。R3 端 CoreWeave 5yr CDS ≈665bp、Oracle CDS 創新高顯示信用開始重定價（`valuation.ai_credit_schism`），但本次未見任何違約、破產或 distressed exchange，且 HY OAS 2.69% 持平，相對於 182 天窗口的低基準率，yes 證據不足。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 28,998.10（2026-07-22），252 交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 5.42%（`valuation.ndx_drawdown`）。R1 門檻水位 `r1_threshold_level` = 22,995.45，自最新收盤需再下跌約 20.70% 才觸及。同期 S&P 500 收 7,498.96，高於 200 日均線 7.14%、高於 52 週均線 8.8%（`valuation.sp500_trend`），價格仍處延伸狀態而非破位。波動面平靜：VIX 16.64（2026-07-22），近 7 日 VIX +6.19% 而 S&P 500 −0.97%，未出現同漲的 crowded-optionality 讀數（`structural.vix_spx_comove`）；MOVE 76.31（2026-07-22，`structural.treasury_basis_trade`）。估值與部位脆弱性高：Shiller CAPE 40.94、trailing P/E 28.85（2026-07-22，`valuation.sp500_pe_cape`），NAAIM 95.64（2026-07-15，`retail.naaim`），FINRA margin debt $1.416T、+53.7% YoY（2026-05 資料，`retail.margin_debt`）；07-22 NYSE 廣度轉弱、新低多於新高（`breadth.advance_decline`）。

**判讀：** R1 距離尚遠（約 20.70% 的額外跌幅）；高估值與擁擠部位代表一旦有催化劑跌幅可能很大，但 182 天內要完成需要信用事件（R3）、capex 指引轉向（R2）或流動性衝擊這類觸發，目前皆未見。

### R2 資本支出收縮

- Alphabet：2026-07-22 Q2 2026 財報將 FY26 capex 指引上修至 ≈$205B，方向：上修（`ai.hyperscaler_capex`）。
- Microsoft、Amazon、Meta：本次取得的證據只有 CNBC 所稱 hyperscaler 2026 capex 合計 ≈$725B+（2026-07-22，`ai.hyperscaler_capex`），三家個別最新指引數字與方向本次未個別列示，方向不可判。
- 已下修家數：本次證據中 0 家下修。其他三家下一次財報日期本次未取得。
- 融資面：Alphabet 發債佔比上升（2026-07-22），Amazon 於 2026-07-07 啟動 ≥$25B 八檔期債以支應 AI 基建（`ai.hyperscaler_financing_mix`），顯示 hyperscaler 融資結構（capex vs FCF / 發債）正轉向發債支應，但這是加碼而非收縮。需求面：TrendForce 指伺服器 DRAM 3Q26 合約價 +13–18% QoQ（2026-07-09，`ai.compute_supply_demand`），未見訂單消化訊號。

**判讀：** R2 方向與觸發相反——唯一有新數據的 Alphabet 為上修。要在窗口內成立需兩家正式下修，通常需先有 R1 式股價重挫或融資成本急升迫使收縮；目前兩者皆未出現。

### R3 AI 信用事件

- 信用定價：Oracle 5yr CDS ≈198bp 創歷史新高、CoreWeave ≈665bp（2026-07-20，`valuation.ai_credit_schism`）。AI 信用定價分歧（equity-vs-credit schism）正朝信用端重定價方向發展，屬後期訊號。CoreWeave 以 AI 算力為主業；其總負債是否 ≥ USD 5bn 本次未有來源支持，未確立。Oracle 主業非 AI 資料中心，不屬 R3 借款人範圍。
- 新融資：Galaxy Digital 計畫為 CoreWeave 承租的資料中心發行 ≈$3.5B 首次垃圾債（2026-07-22，`structural.ai_infrastructure_debt`），顯示高收益市場對 AI 基建仍開放。
- 外溢管道：Blue Owl OCIC Q2 redemption-request ratio 18.8%，於 5% quarterly redemption cap 下 gate proration / breach（按比例撥付），但來源標題指申請較前一季回落（2026-07-02，`monetary.private_credit_liquidity`）。
- 整體信用：HY OAS 2.69%、IG OAS 0.78%（2026-07-21），較前次持平（`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）−4.0bp、SOFR99−IORB +4.0bp（2026-07-21），SRF 動用（Standing Repo Facility usage）0.0（2026-07-22）（`monetary.repo_stress_srf`）。
- 近期到期或再融資需求、付款違約、covenant waiver、going-concern 文字：本次證據中皆未見。

**判讀：** R3 是三條路徑中最接近移動的一條（CoreWeave CDS ≈665bp），但 CDS 走闊不等於違約；在 HY 利差持平、融資市場仍開放的情況下，窗口內出現破產／違約／distressed exchange 仍需一個明確的再融資失敗或流動性事件。

## 支持 yes 的證據

- [R3] Oracle 5yr CDS ≈198bp 創歷史新高、CoreWeave 5yr CDS ≈665bp（2026-07-20），AI 信用端開始重定價而股價仍接近高點（`valuation.ai_credit_schism`）。
- [R3] Blue Owl OCIC Q2 redemption-request ratio 18.8%，於 5% quarterly redemption cap 下 gate proration / breach（2026-07-02），私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）已出現實際限額撥付（`monetary.private_credit_liquidity`）。
- [整體] 估值與槓桿處於極端：Shiller CAPE 40.94（2026-07-22，`valuation.sp500_pe_cape`），margin debt $1.416T、+53.7% YoY（2026-05 資料，`retail.margin_debt`），NAAIM 95.64（2026-07-15，`retail.naaim`），US 槓桿 ETF AUM ≈$198B（2026-07-10，`structural.leveraged_etf_aum`）——一旦觸發，下跌放大機制已就位。
- [R2] hyperscaler 融資結構（capex vs FCF / 發債）轉向發債：Amazon 2026-07-07 啟動 ≥$25B 債券、Alphabet 發債佔比升（`ai.hyperscaler_financing_mix`），capex 對融資市場的依賴上升，融資成本衝擊可能迫使日後收縮。
- [R1] 07-22 NYSE 廣度轉弱、新低多於新高（`breadth.advance_decline`），Cboe SKEW 146.05（2026-07-20，`structural.cross_asset_derivatives`），尾部避險需求偏高。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 5.42%（2026-07-22），距 R1 門檻 22,995.45 仍需再跌約 20.70%（`valuation.ndx_drawdown`）。
- [R2] Alphabet 2026-07-22 將 FY26 capex 上修至 ≈$205B，hyperscaler 2026 capex 合計 ≈$725B+，本次證據中 0 家下修（`ai.hyperscaler_capex`）。
- [R3] 整體信用未重定價：HY OAS 2.69%、IG OAS 0.78%（2026-07-21），較 2026-07-20 持平（`monetary.hy_oas`、`monetary.ig_oas`）；Galaxy Digital ≈$3.5B CoreWeave 資料中心垃圾債（2026-07-22）顯示 AI 基建融資管道仍開放（`structural.ai_infrastructure_debt`）。
- [整體] 資金市場平靜：SOFR−IORB −4.0bp（2026-07-21）、SRF 動用 0.0（2026-07-22）（`monetary.repo_stress_srf`），MOVE 76.31（2026-07-22）（`structural.treasury_basis_trade`），VIX 16.64 且無 VIX/S&P 500 同漲（`structural.vix_spx_comove`）。
- [R2] AI 需求面仍強：伺服器 DRAM 3Q26 合約價 +13–18% QoQ（2026-07-09，`ai.compute_supply_demand`）；Anthropic IPO 程序以 $965B 估值進行、可能 10 月掛牌（2026-07-15，`speculation.upcoming_ai_ipos`），股權市場仍在提供資金。
- [整體] 情緒並非亢奮：CNN Fear & Greed 41（Fear，2026-07-21，`retail.fear_greed`），Cboe equity put/call 0.65（2026-07-21，`speculation.equity_put_call`），本週 +AI 改名／SPAC 與 microcap moonshot 合格件數皆為 0（`speculation.ai_rename_spac`、`speculation.microcap_moonshots`）。

## 與前期比較

前次結論：無前次預測（report-2026-07-20 為舊格式評分報告）

- 前次為舊格式評分報告，不轉譯為 yes/no；flip_evidence 為 []。
- 自 2026-07-20 以來的主要變化：Alphabet Q2 財報上修 FY26 capex 至 ≈$205B（2026-07-22，`ai.hyperscaler_capex`）；NASDAQ-100 自 28,604.23（07-20）回升至 28,998.10（07-22）（`valuation.ndx_drawdown`）；10Y 殖利率 +3.0bp 至 4.63%（`monetary.dgs10`）；MOVE 自 72.66 升至 76.31（`structural.treasury_basis_trade`）。這些變化未讓任何路徑接近觸發。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED（搜尋完成、無合格當期披露）：retail.social_sentiment、institutional.bofa_jpm_survey、ai.token_growth、ai.openai_anthropic_revenue（最新 run-rate 為 2026-05-15 Epoch 資料，非本季披露）、ai.customer_concentration_rpo、ai.depreciation_life、ai.capital_cycle（quarterly_state 與 event_scan 皆無可引用披露）、structural.global_leveraged_approvals。其中 ai.customer_concentration_rpo 與 ai.capital_cycle 若有披露（backlog 重複計算風險（RPO double-counting）、資料中心租約取消）可能強化 R2/R3 論述，但單一缺漏不足以把答案翻為 yes。

資料品質註記：

- valuation.mag7_multiples 的 Mag 7 加權 P/E ≈40 資料日為 2026-05-15，structural.zero_dte 的 0DTE 佔 SPX ≈63% 資料日為 2026-02-28，均為舊快照，僅作背景，未列入兩側證據。
- ai.revenue_capex_gap：年化 AI 終端營收（Anthropic ≈$47B＋OpenAI ≈$25B，Epoch 2026-05-15 沿用值）對 hyperscaler 年化 capex ≈$725B+（CNBC 2026-07-22；分母公司集合未於來源列明，不宣稱全產業），缺口仍大；分子為沿用值，不當作新證據。
- speculation.insider_form4：SEC EDGAR 一手 Form 4 URL 本次無法取得，14 日內未見合格 cluster，故不列任何具名內部人或金額。
- 10Y 分解：ΔDGS10 +3.0bp、ΔDFII10 +2.0bp、ΔT10YIE +3.0bp，T10YIE 視窗（至 2026-07-22）與另兩腿（至 2026-07-21）不一致，判讀：不可判（視窗不一致）。

最大的不確定性：

1. Microsoft、Amazon、Meta 的下一次財報 capex 指引（日期本次未取得）：若其中兩家下修，R2 直接成立，會把答案推向 yes；目前唯一新數據（Alphabet）為上修。
2. CoreWeave 信用走勢：CDS ≈665bp 若進一步走闊並伴隨再融資失敗，R3 可能在窗口內成立並經由信用傳導觸發 R1；其總負債規模本次未確立。
3. 私募信貸贖回壓力是否擴散：Blue Owl OCIC 已出現 gate proration，若擴及多檔基金並出現 net inflow→outflow flip，會加大 AI infrastructure debt financing / vendor-financing loops 的再融資風險，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7498.96 | FRED API (series_id=SP500) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 7.14 | FRED API (series_id=SP500) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.8 | FRED API (series_id=SP500) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28998.1 | FRED API (series_id=NASDAQ100) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-07-23T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 5.42 | FRED API (series_id=NASDAQ100) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026-Q1 家庭股票配置 %） | 45.76080873390133 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-23T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 2.69 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（IG OAS %） | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（10Y 殖利率 %） | 4.63 | FRED API (series_id=DGS10) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（較 2026-07-20） | 3.0 | FRED API (series_id=DGS10) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（10Y 實質殖利率 %） | 2.37 | FRED API (series_id=DFII10) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps（較 2026-07-20） | 2.0 | FRED API (series_id=DFII10) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（10Y breakeven %） | 2.28 | FRED API (series_id=T10YIE) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps（較 2026-07-20） | 3.0 | FRED API (series_id=T10YIE) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（WTI，美元） | 84.38 | FRED API (series_id=DCOILWTICO) | 2026-07-20 | 2026-07-23T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料 CPI YoY %） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-23T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（5y5y %） | 2.26 | FRED API (series_id=T5YIFR) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR delta_bps（較 2026-07-20） | 4.0 | FRED API (series_id=T5YIFR) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright 10Y 期限溢價 %） | 0.7787 | FRED API (series_id=THREEFYTP10) | 2026-07-17 | 2026-07-23T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.61 | FRED API (series_id=SOFR) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.69 | FRED API (series_id=SOFR99) | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-07-23 | 2026-07-23T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（Fed 隔夜 repo 操作 transaction volume，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.walcl | WALCL latest（Fed 資產負債表） | 6743028.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-15 | 2026-07-23T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（ECB 資產負債表） | 5949077.0（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-17 | 2026-07-23T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（BOJ 資產負債表） | 6395509.0（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-23T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.64 | FRED API (series_id=VIXCLS) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of 2026-07-22，base 2026-07-15，window 7 日） | 16.64 | FRED API (vix_spx_comove block) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 6.19 | FRED API (vix_spx_comove block) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -0.97 | FRED API (vix_spx_comove block) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（銀行對 NBFI 放款，十億美元） | 2004.0237（$2.00T） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-08 | 2026-07-23T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六檔 UST 期貨槓桿基金淨部位，口） | -7562874 | CFTC TFF (cftc_lev_funds block) | 2026-07-14 | 2026-07-23T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -78139 | CFTC TFF (cftc_lev_funds block) | 2026-07-14 | 2026-07-23T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（^MOVE） | 76.31 | Yahoo chart API (move_index block, ^MOVE) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（OFR tri-party repo transaction volume） | 2334.5 | OFR STFM (ofr_repo block, REPO-TRIV1_TV_TOT-P) | 2026-07-22 | 2026-07-23T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com，WebSearch primary | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | MarketXLS dashboard，WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-05-15，舊快照） |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方 TP 調整摘要，WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導，WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | portfolioslab，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | MacroMicro，WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth 報導，WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | MacroMicro CNN F&G 序列，WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | Advisor Perspectives FINRA 摘要，WebSearch（月頻沿用） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com，WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB / cashtag，WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | MacroMicro NAAIM 序列，WebSearch primary | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查摘要，WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | RTTNews 標售回顧，WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要，WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Xinhua 英文摘要，WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露報導，WebSearch primary（30d） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報／財報報導，WebSearch | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic / OpenAI / Google 披露，WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch / The Information，WebSearch（需本季披露） | ✗ NOT DISCLOSED（最新為 2026-05-15，非本季） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險 | 財報電話會議，WebSearch primary | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce，WebSearch primary | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | quarterly_state：季報 capex／發債；event_scan：30d 發債掃描；WebSearch primary | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露（Epoch 分子沿用、CNBC 分母），WebSearch primary | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K / 10-Q / 法說，WebSearch primary（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | quarterly_state：供需增速；event_scan：30d 進出場事件；WebSearch primary | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | Businesswire / StockTitan 篩選，WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis.com，WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz / Benzinga / StockTwits movers，WebSearch primary（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導，WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR primary（一手 URL 不可得）、openinsider，14d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | YCharts，WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing 彙整，WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire / ETF.com，WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX / TWSE / JPX / ESMA，WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe insights，WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-02-28，舊快照） |
| structural.options_volume | 結構｜Options total volume: OCC monthly volume report | theocc.com，WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Velox Macro VIX／SKEW 週報，WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | Advisor Perspectives（交叉引用散戶 margin debt） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | Bloomberg 等，WebSearch primary（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo），aggregation any | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 28.85 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 40.94 | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 trailing P/E ≈40 | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026 （MarketXLS；原定 Mag 7 multiples） | 2026-05-15 | 2026-07-23T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標價 $288（≈22× EPS、target PE 未擴張，EPS 主導；舊目標價未披露） | Morgan Stanley NVDA target 288 July 2026 EPS | https://www.gurufocus.com/news/8955458/morgan-stanley-upgrades-nvidia-nvda-with-a-288-target-price （GuruFocus） | 2026-07-13 | 2026-07-23T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS ≈198bp 歷史新高、CoreWeave ≈665bp | Oracle CoreWeave CDS spread record July 2026 | https://bondblox.com/news/oracles-5y-cds-spread-hits-all-time-highs （BondBlox） | 2026-07-20 | 2026-07-23T09:30:00+08:00 |
| breadth.rsp_spy | RSP +11.8% vs SPY +9.4% YTD | RSP vs SPY equal weight YTD 2026 | https://portfolioslab.com/tools/stock-comparison/RSP/SPY （PortfoliosLab） | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 36.40% | S&P 500 top 10 concentration percent 2026 | https://en.macromicro.me/collections/34/us-stock-relative/123442/us-sp-500-top-10-companies-total-market-cap-and-share （MacroMicro） | 2026-07-02 | 2026-07-23T09:30:00+08:00 |
| breadth.advance_decline | 07-22 NYSE A/D 轉弱、新低多於新高（未列具體比值） | NYSE breadth advance decline July 22 2026 | https://ts2.tech/en/nasdaq-ends-flat-as-market-breadth-remains-thin-ahead-of-big-tech-earnings/ （TS2） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 41（Fear） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/series/22748/cnn-fear-and-greed （MacroMicro；原定 cnn.com） | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-05 月資料）$1.416T、+53.7% YoY，沿用 | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives；原定 FINRA） | 2026-05-31 | 2026-07-23T09:30:00+08:00 |
| retail.aaii | AAII Bullish 44.9% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-15 | 2026-07-23T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64 | NAAIM exposure index latest July 2026 | https://en.macromicro.me/series/20540/naaim-exposure-index （MacroMicro；原定 naaim.org） | 2026-07-15 | 2026-07-23T09:30:00+08:00 |
| monetary.treasury_auctions | 20Y 標售 bid-to-cover 2.64、小幅 tail | US Treasury 20Y auction July 2026 bid to cover | https://www.rttnews.com/3669412/twenty-year-bond-auction-attracts-average-demand.aspx （RTTNews） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 會議維持利率 ≈83.4% | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch （CryptoRank；原定 CME FedWatch） | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://english.news.cn/20260714/2d460c4227c244f1bf930993be469262/c.html （Xinhua） | 2026-07-14 | 2026-07-23T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio 18.8%，5% quarterly redemption cap 下按比例撥付；申請較前季回落 | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://www.investing.com/news/stock-market-news/blue-owl-keeps-5-redemption-caps-as-ocic-requests-ease-from-prior-quarter-4773280 （Investing.com） | 2026-07-02 | 2026-07-23T09:30:00+08:00 |
| ai.hyperscaler_capex | Alphabet FY26 capex 上修至 ≈$205B（Q2 2026 財報）；hyperscaler 2026 capex 合計 ≈$725B+ | hyperscaler capex 2026 Alphabet raised 205B Q2 | https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html （CNBC） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 +13–18% QoQ | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260709-13140.html （TrendForce） | 2026-07-09 | 2026-07-23T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] Alphabet FY26 capex 上修至 ≈$205B、發債佔比上升 | Alphabet capex 205B Q2 2026 debt financing | https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html （CNBC） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] Amazon 啟動 ≥$25B 八檔期公司債，用於 AI 基建 | Amazon 25 billion bond offering AI data center July 2026 | https://finance.yahoo.com/technology/ai/articles/bond-issuance-backing-ai-investment-135635215.html （Yahoo Finance） | 2026-07-07 | 2026-07-23T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收（Anthropic ≈$47B＋OpenAI ≈$25B，沿用）vs 年化 capex ≈$725B+（分母公司集合未列明） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI）；分母見 ai.hyperscaler_capex | 2026-05-15 | 2026-07-23T09:30:00+08:00 |
| speculation.ai_rename_spac | 本週合格 +AI 改名／SPAC 0 件 | AI rename ticker change SPAC July 16-23 2026 | Businesswire、StockTitan movers screener | 2026-07-23 | 2026-07-23T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD ≈203 檔 IPO、募資 $141.2B | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/ （StockAnalysis） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot 0 件 | microcap 100% single day quantum AI fusion moonshot July 2026 | Finviz、Benzinga、StockTwits movers screener | 2026-07-23 | 2026-07-23T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 投資人會議、估值 $965B、可能 10 月掛牌 | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html （CNBC） | 2026-07-15 | 2026-07-23T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 cluster 0 件（EDGAR 一手 URL 不可得，不列具名內部人） | insider Form 4 cluster AI leaders July 2026 openinsider | SEC EDGAR、openinsider | 2026-07-23 | 2026-07-23T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.65（日讀數） | Cboe equity put call ratio July 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio （YCharts） | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM ≈$198B（個別 NVDL／TSLL／CONL／TQQQ／SOXL／SQQQ 未列） | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing；原定 etf.com） | 2026-07-10 | 2026-07-23T09:30:00+08:00 |
| structural.us_single_stock_etf | GraniteShares 推出首檔美國掛牌 SK hynix 2x 多／空 ETF | single-stock leveraged ETF launch July 2026 GraniteShares SK hynix | https://www.globenewswire.com/news-release/2026/07/14/3326857/0/en/GraniteShares-Launches-the-First-U-S-Listed-Leveraged-ETFs-on-SK-hynix.html （GlobeNewswire） | 2026-07-14 | 2026-07-23T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權成交 ≈63%（舊快照） | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/volatility-insights-evaluating-the-market-impact-of-spx-0-dte-options/ （Cboe） | 2026-02-28 | 2026-07-23T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月成交 1,603,491,559 口、+45% YoY | OCC monthly options volume June 2026 | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/monthly-weekly-volume-statistics （OCC） | 2026-07-02 | 2026-07-23T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 146.05、VIX ≈18.7 contango | VIX term structure SKEW July 2026 | https://veloxmacro.com/how-to-read-the-vix-week-ending-july-20-2026/ （Velox Macro） | 2026-07-20 | 2026-07-23T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-05 月資料）$1.416T、+53.7% YoY，交叉引用 | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives） | 2026-05-31 | 2026-07-23T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Galaxy Digital 計畫為 CoreWeave 承租資料中心發行 ≈$3.5B 首次垃圾債（借款人 Galaxy Digital；定價／評等未披露） | Galaxy Digital 3.5 billion junk bond CoreWeave data center July 2026 | https://www.bloomberg.com/news/articles/2026-07-22/coreweave-backed-data-center-plans-3-5-billion-junk-bond-sale （Bloomberg） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |

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
  "yes_basis": [],
  "r1_drawdown_pct": 5.42,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

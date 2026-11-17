> [DRY RUN] this report was not committed to archive.

# 2026-10-18 AI 泡沫破裂預測報告

報告日期：2026-10-18｜ISO 週次：2026-W42｜預測窗口：2026-10-18 → 2027-04-18｜前次基準：report-2026-09-13（35天前）

## 結論

**結論：no**

三條路徑目前都離觸發還遠：NASDAQ-100 只比 52 週高點低 4.13%，還要再跌約 21.77% 才會觸發 R1（`valuation.ndx_drawdown`）；四大 hyperscaler 最新 2026 capex 指引合計仍約 $725bn，沒有任何下修證據（`ai.hyperscaler_capex`）。CoreWeave 5Y CDS 創 1,194.5 bps 紀錄（`valuation.ai_credit_schism`）是最強的 yes 訊號，但它只反映信用定價，還不是 R3 要求的違約、破產或 distressed exchange；repo 與 IG 信用也沒有出現傳導，所以不足以推翻 182 天窗口內這些事件本來就少見的基準。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,935.59（2026-10-15），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 4.13%；R1 門檻是 23,418.52，從最新收盤還要再跌約 21.77% 才會觸及（`valuation.ndx_drawdown`）。S&P 500 收在 7,659.44（2026-10-16），比 200 日均線高 5.34%，比 52 週均線高 6.78%；距前次基準日（2026-09-11 收盤 7,656.98）僅變動 +0.03%（`valuation.sp500_trend`）。估值仍然偏高：Shiller CAPE 約 40.54（2026-10-16，`valuation.sp500_pe_cape`）；BofA 10 月調查的科技股淨加碼約 37%，是 2020 年 8 月以來最高（`institutional.bofa_jpm_survey`），部位擁擠。不過短線情緒已明顯轉弱：CNN Fear & Greed 約 18，屬極度恐懼（2026-10-16，`retail.fear_greed`）；2026-10-16 上漲對下跌家數約 29 比 71（`breadth.advance_decline`）；VIX 16.46（2026-10-15），近 7 日 VIX +6.81%、S&P 500 −0.27%，沒有出現同漲的 crowded-optionality 讀數（`structural.vix_spx_comove`）。

**判讀：** R1 還差約 21.77% 的跌幅。窗口內要觸發，需要 AI 信用事件（R3）外溢、四大財報 capex 或營收不如預期，或利率再急升來帶動估值壓縮；目前估值高、部位擁擠，代表一旦出事跌幅會很大，但還看不到已經啟動的大幅下跌。

### R2 資本支出收縮

本次證據只取得四大 hyperscaler 2026 年 capex 指引合計約 $725bn（CNBC，2026-07-28，對應 Q2 財報季；`ai.hyperscaler_capex`），以 stock-of-state 方式沿用為 current。Microsoft、Alphabet、Amazon、Meta 各自的指引數值、指引日期，以及相對前一次正式指引的方向（上修／持平／下修），這次的搜尋結果都沒有逐家揭露；本報告不補估。就現有證據看，四家中已下修的家數是 0（沒有任何下修揭露）。下一次財報日期沒有出現在本次證據裡；不過 182 天窗口依季報節奏，至少會涵蓋兩輪四家財報。需求端可參考的分子：Anthropic 年化 run-rate 約 $65bn（2026-08-17，`ai.openai_anthropic_revenue`），與上述分母比較的 AI 營收對 capex 缺口（revenue-to-capex gap）約 $65bn 對 $725bn（分母：top-4，不含 Oracle 與 neocloud；分子只有 Anthropic，OpenAI 本次沒有當季披露；`ai.revenue_capex_gap`）。H100 隨選中位租金約 $4.20/hr（2026-10-07，`ai.compute_supply_demand`），單看價格無法判斷產能過剩。

**判讀：** R2 目前離觸發最遠：沒有任何一家下修，反而是投資人對 capex 的檢視變嚴。要在窗口內觸發，至少需要兩家在接下來兩輪財報中下修指引；這通常要先出現 R1 等級的市場壓力或 AI 營收明顯不達預期，現有證據都還沒看到。

### R3 AI 信用事件

AI 信用定價分歧（equity-vs-credit schism）在信用端明顯走闊：CoreWeave 5Y CDS 創 1,194.5 bps 的紀錄（2026-10-15，`valuation.ai_credit_schism`），報導的標題是 AI 信用疑慮把科技股違約保險推上紀錄高點。CoreWeave 是以 AI 算力為主業的借款人，是 R3 最直接的候選；但它的負債總額、近期到期與再融資時程，本次證據都沒有取得，所以這裡不斷言它已達 50 億美元門檻，只把它列為「若負債達標即為主要候選」。AI infrastructure debt financing / vendor-financing loops 方面，Lambda 在 2026-10-01 完成約 $1bn 的 GPU 擔保融資（`structural.ai_infrastructure_debt`），顯示 neocloud 仍拿得到資金，但槓桿也在增加。整體信用面：HY OAS 3.23%，自 2026-09-11 走闊 58 bps（`monetary.hy_oas`）；IG OAS 0.84%，只 +4 bps（`monetary.ig_oas`）；銀行對 NBFI 放款 $2.10T，週變動 +2.14%（`structural.nbfi_bank_loans`）。本次證據中沒有任何 AI 借款人出現漏付、covenant waiver、distressed exchange、going-concern 或破產申請的揭露。

**判讀：** 在三條路徑中，R3 的定價離門檻最近：CDS 水位代表市場對 CoreWeave 違約的定價已經相當可觀。但 R3 需要實際發生的事件（破產、超過寬限期的違約，或完成 distressed exchange），而窗口內能推過門檻的，是 CDS 持續走闊之後再融資失敗，或客戶合約／GPU 擔保價值出問題；目前看到的是融資仍能完成、repo 沒有壓力，事件還沒發生。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 創 1,194.5 bps 紀錄（2026-10-15），AI 信用疑慮把科技股違約保險推上紀錄高點：信用端已在重新定價，股權端（NASDAQ-100 只回撤 4.13%）還沒跟上，屬於後期訊號（`valuation.ai_credit_schism`）。
- [整體] 信用與利率波動同步升溫：HY OAS 從 2.65% 升到 3.23%（+58 bps，2026-10-15，`monetary.hy_oas`），MOVE 從 82.21 升到 101.1（+18.89，2026-10-16，`structural.treasury_basis_trade`），風險偏好正在收縮。
- [整體] 政策緩衝空間有限：Fed 目標區間升到 3.75%–4.00%（自前次基準 +25 bps，2026-10-17，`monetary.fed_funds`），CPI YoY 3.72%（2026-09，`monetary.cpi_yoy`），10Y 殖利率 5.1%（`monetary.dgs10`），WTI $101.91（`monetary.wti`），一旦 AI 主導的下跌出現，Fed 降息托底的能力受限。
- [R1] 估值與部位擁擠：Shiller CAPE 約 40.54（2026-10-16，`valuation.sp500_pe_cape`）；BofA 10 月調查科技股淨加碼約 37%，是 2020 年 8 月以來最高（2026-10-13，`institutional.bofa_jpm_survey`），下檔空間大。
- [R1] 市場廣度與情緒轉弱、IPO 窗口降溫：Fear & Greed 約 18（極度恐懼，2026-10-16，`retail.fear_greed`）、上漲對下跌家數約 29 比 71（2026-10-16，`breadth.advance_decline`）、兩週內已有第 4 檔 IPO 撤件或延後（2026-10-16，`speculation.ipo_heat`）。
- [R3] 槓桿仍在累積：Lambda 約 $1bn GPU 擔保融資（2026-10-01，`structural.ai_infrastructure_debt`）；銀行對 NBFI 放款 $2.10T、週變動 +2.14%（2026-10-07，`structural.nbfi_bank_loans`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）很大：已披露的年化終端營收約 $65bn（只有 Anthropic），對比年化 capex 約 $725bn（分母：top-4），capex 回收壓力是日後下修的伏筆（`ai.revenue_capex_gap`）。

## 支持 no 的證據

- [R1] 離 R1 還很遠：NASDAQ-100 收 29,935.59（2026-10-15），距 52 週高點回撤 4.13%，還要再跌約 21.77% 才到門檻 23,418.52（`valuation.ndx_drawdown`）；S&P 500 仍比 200 日均線高 5.34%（`valuation.sp500_trend`）。
- [R2] 四家都沒有下修：最新 2026 capex 指引合計約 $725bn（2026-07-28，`ai.hyperscaler_capex`），R2 需要四家中至少兩家下修，目前是 0。
- [R3] 只有定價、沒有事件：本次沒有找到任何 AI 借款人違約、破產或 distressed exchange 的揭露；Lambda 在 2026-10-01 仍順利完成約 $1bn 融資（`structural.ai_infrastructure_debt`），融資管道還開著。
- [整體] 資金市場運作正常：repo 資金壓力（SOFR−IORB）為 −1 bps、SOFR99−IORB +7 bps，SRF 動用（Standing Repo Facility usage）為 0（2026-10-15/16，`monetary.repo_stress_srf`）；IG OAS 只有 0.84%（`monetary.ig_oas`）；這些都顯示 HY 的走闊還沒有傳到投資級與融資市場。
- [整體] 美債標售需求（auction tail / bid-to-cover）穩健：10Y 標售 bid-to-cover 約 2.77，報導稱需求強勁（2026-10-07，`monetary.treasury_auctions`），沒有出現國債市場失序（Treasury market dysfunction）的跡象。
- [整體] AI 需求端仍在擴張：Anthropic 年化 run-rate 約 $65bn（2026-08-17，`ai.openai_anthropic_revenue`），目標 11 月中上市（2026-10-05，`speculation.upcoming_ai_ipos`）；H100 隨選中位租金約 $4.20/hr（2026-10-07，`ai.compute_supply_demand`），沒有看到產能過剩的證據。
- [R1] 極度恐懼本身常是反向指標：VIX 16.46，沒有出現與指數同漲的 crowded-optionality 讀數（2026-10-15，`structural.vix_spx_comove`）；AAII 看多約 38.7%（2026-10-14，`retail.aaii`），散戶不是一面倒的狂熱。

## 與前期比較

前次結論：無前次預測（report-2026-09-13 為舊格式評分報告）

- 前次基準是舊格式評分報告，沒有 yes/no 預測可以比較；本次 `flip_evidence` 為空。
- 自前次基準以來的主要變化：Fed 目標區間上調 25 bps 到 3.75%–4.00%（`monetary.fed_funds`）；HY OAS +58 bps（`monetary.hy_oas`）；MOVE +18.89（`structural.treasury_basis_trade`）；10Y 殖利率 +14 bps、實質殖利率 +18 bps、breakeven −1 bps，因 T10YIE 與另兩腿的觀測窗口不一致，判讀為不可判（視窗不一致）（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。
- 美債基差交易槓桿（Treasury basis-trade leverage）：槓桿基金美債期貨淨部位 −6,883,343 口（2026-10-13），4 週變動 −309,307 口，空方部位擴大（`structural.treasury_basis_trade`）；目前還是槓桿累積，沒有出現平倉事件。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `breadth.rsp_spy`：搜尋只拿到 2026-07-18 的 RSP YTD 報酬（約 12.08%），沒有當前快照，所以不當成本次證據。缺漏不影響答案：廣度方面已有 `breadth.advance_decline` 的當日讀數。
- `breadth.top10_concentration`：搜尋只拿到 2026-07-31 的前十大集中度（約 38.9%），沒有當前快照。缺漏不影響答案：集中度是脆弱度指標，不是時點觸發條件。

其他缺漏（✗ NOT DISCLOSED，不作為證據）：`valuation.analyst_tp_decomposition`、`retail.social_sentiment`、`retail.naaim`、`monetary.fedwatch`、`monetary.private_credit_liquidity`、`ai.token_growth`、`ai.customer_concentration_rpo`、`ai.hyperscaler_financing_mix`（quarterly_state 可沿用，event_scan 30 日內沒有新融資揭露）、`ai.depreciation_life`、`ai.capital_cycle`（增速證據不足，本次不判定週期階段）、`speculation.equity_put_call`、`structural.global_leveraged_approvals`。其中 `monetary.private_credit_liquidity`（私募信貸贖回壓力（private-credit / non-bank fund liquidity stress））缺漏最可能影響 R3：若有 gate proration / breach 或 net inflow→outflow flip，會加強 R3 的傳導路徑，但本次 30 日內沒有揭露。另外 `valuation.mag7_multiples` 只取得單一成員 MSFT 的 forward P/E 24.5（2026-09-24），不是 Mag 7 加權值，因此沒有用於判讀。

資料一致性說明：搜尋紀錄寫著美債基差交易槓桿 bullet 的「script 三區塊 fetch_failed」，但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 都是 `status: ok`。本報告以驗證器實際讀取的 artifact 為準，記為 ✓ API；artifact 以外的 WebSearch 路徑沒有找到任何額外揭露。

最大的不確定性：

1. CoreWeave 的負債規模與再融資時程（本次未取得）：若確認負債 ≥ 50 億美元，且窗口內有大額到期，而 CDS 又持續走闊，R3 會成為最可能翻成 yes 的路徑。
2. 窗口內兩輪四大財報：只要有一家下修 capex，加上 AI 營收不如預期，R1、R2 就會同時受壓。這會把答案推向 yes。
3. Anthropic 11 月中 IPO 與 Fed 升息路徑：IPO 順利會強化 no；IPO 延後或失敗、加上利率再上升，會加速估值壓縮，把答案推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7659.44 | FRED API (series_id=SP500) sp500_trend | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（偏離 200 日均線 %） | 5.34 | FRED API (series_id=SP500) sp500_trend | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（偏離 52 週均線 %） | 6.78 | FRED API (series_id=SP500) sp500_trend | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29935.59 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-06 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（自高點回撤 %） | 4.13 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻） | 23418.52 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2 季資料，家庭股票占金融資產 %） | 48.2301354474（≈48.23%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 4.0 | FRED API (series_id=DFEDTARU) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.75 | FRED API (series_id=DFEDTARL) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 3.23 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps（較 2026-09-11） | 58.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（IG OAS %） | 0.84 | FRED API (series_id=BAMLC0A0CM) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（10Y 殖利率 %） | 5.1 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（較 2026-09-11） | 14.0 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（10Y 實質殖利率 %） | 2.78 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps（較 2026-09-11） | 18.0 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（10Y breakeven %） | 2.35 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps（較 2026-09-11） | -1.0 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（WTI 美元／桶） | 101.91 | FRED API (series_id=DCOILWTICO) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料，CPI YoY %） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（5y5y 遠期通膨預期 %） | 2.33 | FRED API (series_id=T5YIFR) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright 10Y 期限溢價 %） | 1.0729 | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.89 | FRED API (series_id=SOFR) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.97 | FRED API (series_id=SOFR99) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.9 | FRED API (series_id=IORB) | 2026-10-18 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（隔夜 repo 操作 transaction volume，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR−IORB 利差（repo_stress sofr_iorb_bps，IORB 取 2026-10-15） | -1.0 | fetch_macro.py repo_stress（FRED SOFR, IORB） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.walcl | WALCL latest（Fed 資產負債表） | 6,755,639（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（ECB 資產負債表） | 5,943,911（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（BOJ 資產負債表） | 6,250,253（¥625.03T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.46 | FRED API (series_id=VIXCLS) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of 2026-10-15，base 2026-10-08，window 7 日） | 16.46 | fetch_macro.py vix_spx_comove block（與 FRED SP500 對齊） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 6.81 | fetch_macro.py vix_spx_comove block（與 FRED SP500 對齊） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -0.27 | fetch_macro.py vix_spx_comove block（與 FRED SP500 對齊） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（銀行對 NBFI 放款） | 2097.9713（$2.10T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG chg_pct（較 2026-09-09） | 2.14 | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六檔美債期貨槓桿基金淨部位，口） | -6883343 | CFTC TFF cftc_lev_funds | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -309307 | CFTC TFF cftc_lev_funds | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（^MOVE） | 101.1 | Yahoo chart ^MOVE move_index | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index delta_abs（較 2026-09-11） | 18.89 | Yahoo chart ^MOVE move_index | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2264.1 | OFR STFM REPO-TRIV1_TV_TOT-P ofr_repo | 2026-10-16 | 2026-10-18T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch primary（multpl） | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch | ✓ SEARCH-VERIFIED（只取得單一成員 MSFT forward P/E proxy，非加權值） |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch primary（90d、同季） | ✗ NOT DISCLOSED（搜尋完成，沒有同季合格的 TP 上調） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch primary（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ⛔ FETCH FAILED（只取得 2026-07-18 的舊快照，沒有當前值） |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch | ⛔ FETCH FAILED（只取得 2026-07-31 的舊快照，沒有當前值） |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch（月頻 stock-of-state 沿用） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED（7 日內沒有顯著討論） |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch primary | ✗ NOT DISCLOSED（沒有找到當週值） |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | fetch_macro.py（FRED API） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | fetch_macro.py（FRED API） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | fetch_macro.py（FRED API） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | fetch_macro.py（FRED API） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | fetch_macro.py（FRED API） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | fetch_macro.py（FRED API，直接取得） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | fetch_macro.py（FRED API） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | fetch_macro.py（FRED API，yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | fetch_macro.py（FRED API） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | fetch_macro.py（FRED API） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | fetch_macro.py（FRED API）＋repo_stress block | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok；repo_stress status ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch primary（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch primary | ✗ NOT DISCLOSED（沒有找到當前快照） |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | fetch_macro.py（FRED API） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | fetch_macro.py（FRED API） | ✓ API（ECBASSETSW ok；JPNASSETS ok，no_new_obs） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing / liquidity operations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch primary（30d） | ✗ NOT DISCLOSED（30 日內沒有揭露） |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state 沿用 Q2 財報季） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED（本季沒有揭露） |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險 | WebSearch primary | ✗ NOT DISCLOSED（沒有合格揭露） |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch primary | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch primary；quarterly_state 沿用，event_scan 30d 掃描完成，沒有新融資 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch primary＋capex bullet 分母 | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch primary（30d） | ✗ NOT DISCLOSED（30 日內沒有變動揭露） |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch primary；兩組件都掃描完成，沒有可用揭露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch（SEC EDGAR 8-K、SPACInsider、Boardroom Alpha） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch primary（movers 掃描） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 列表＋WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch primary | ✗ NOT DISCLOSED（沒有找到當前值） |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR ETF 申報＋ETF.com 新上市 feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d，各監理機關） | ✗ NOT DISCLOSED（7 日內沒有英文揭露） |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | fetch_macro.py（FRED VIXCLS＋vix_spx_comove block） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（確認用） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch primary（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | fetch_macro.py（FRED API） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py 三區塊（cftc_lev_funds、move_index、ofr_repo）＋WebSearch 事件掃描 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok；WebSearch 沒有額外揭露） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.54 | Shiller PE CAPE ratio current October 2026 multpl | https://www.multpl.com/shiller-pe（multpl；原定來源 multpl / GuruFocus） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 成員 MSFT forward P/E 24.5（單一成員 proxy） | Magnificent 7 forward P/E valuation October 2026 | https://articlegateway.com/?p=146（原定來源 Mag 7 加權 P/E） | 2026-09-24 | 2026-10-18T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 紀錄 1,194.5 bps | AI credit fears tech default insurance record highs October 2026 | https://www.businessday.co.za/world/international-companies/2026-10-15-ai-credit-fears-push-tech-default-insurance-to-record-highs/（BusinessDay） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| breadth.advance_decline | 上漲家數約 29 對下跌 71 | market breadth October 16 2026 percent above 200-day advance decline | https://www.thetrading.tools/market-breadth（thetrading.tools） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 約 18（極度恐懼） | CNN Fear and Greed Index October 16 2026 extreme fear | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/（finhacker；原定來源 CNN） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-08 月資料）約 $1.45T | FINRA margin debt August 2026 year over year | https://www.thetrading.tools/margin-debt（原定來源 FINRA） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.7%（週止 2026-10-14） | AAII sentiment survey week ending October 14 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA 10 月 FMS 科技股淨加碼約 37%，2020 年 8 月以來最高 | BofA October 2026 fund manager survey tech overweight cash | https://www.bloomberg.com/news/articles/2026-10-13/bofa-poll-shows-investors-most-exposed-to-tech-stocks-since-2020（Bloomberg） | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.77（需求強勁） | Treasury 10-year note auction October 7 2026 bid-to-cover | https://www.rttnews.com/3697286/ten-year-note-auction-attracts-strong-demand.aspx（RTTNews） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| monetary.pboc | 2026 年 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate social financing 2026 total | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm（SteelOrbis） | 2026-08-15 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 指引合計約 $725bn（Q2 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 $65bn | OpenAI Anthropic annualized revenue run rate 2026 | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選中位租金約 $4.20/hr | GPU rental price index HBM DRAM contract price October 2026 | https://uvik.net/blog/gpu-price-index/（Uvik） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 2026 年 hyperscaler 發債預估約 $190bn（沿用的背景狀態） | hyperscaler bond issuance 2026 capex versus free cash flow | https://www.twentyfouram.com/insights/oracle-clears-the-supply-cloud-with-record-demand（TwentyFour AM） | 2026-02-02 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 分子：Anthropic run-rate 約 $65bn；分母：`ai.hyperscaler_capex` top-4 約 $725bn | AI revenue versus capex gap 2026 annualized | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement October 2026 | 檢查來源：SEC EDGAR 8-K、SPACInsider、Boardroom Alpha | — | 2026-10-18T09:30:00+08:00 |
| speculation.ipo_heat | 兩週內第 4 檔 IPO 撤件或延後 | IPO market October 16 2026 pulled postponed Firmus Oura | https://www.ipox.com/ipox/the-ipox-update-10162026（IPOX） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描（0 件符合「兩個以上主題＋弱基本面」；PFAI 10/7 +116.7% 落在窗外） | biggest stock gainers week October 12-16 2026 microcap 100% | 檢查來源：Tapeboard movers archive、Financial Modeling Prep daily gainers、Yahoo movers | — | 2026-10-18T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 11 月中上市 | Anthropic IPO October 2026 timing valuation S-1 | https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market（CNN） | 2026-10-05 | 2026-10-18T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件合格；10/9 NVDA 有申報，但沒有具名申報人與金額等 filing-level 細節） | insider selling Form 4 October 2026 Nvidia AI executives SEC | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-10-18T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 $40.04bn | single stock leveraged ETF assets October 2026 weekly flows | https://www.etfaction.com/single-stock-traders-pile-into-tsll-and-intw-as-levered-flows-surge/（ETF Action） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval October 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed | — | 2026-10-18T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 9 月 ADV 創紀錄，約 340 萬口（2026-09 月資料） | Cboe September 2026 derivatives volume 0DTE SPX record | https://www.cboe.com/insights/posts/market-metrics-that-matter-derivatives-september-2026-volume-highlights（Cboe） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.options_volume | OCC 9 月總結算量約 1,486,062,415 口（2026-09 月資料） | OCC September 2026 monthly volume data | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report（OCC） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 約 14.84、Cboe SKEW 154.34 | VIX term structure SKEW October 2026 options brief | https://www.home.saxo/content/articles/options/the-middle-got-cheaper-the-edge-did-not---options-brief---12-october-2026-12102026（Saxo） | 2026-10-12 | 2026-10-18T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-08 月資料）約 $1.45T，作為市值比率的確認基數 | margin debt to market cap August 2026 | https://www.thetrading.tools/margin-debt（原定來源 FINRA） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Lambda GPU 擔保融資約 $1bn | AI data center debt Lambda CoreWeave financing October 2026 | https://valueaddvc.com/pulse/ai-data-center-debt-financing-risk-2026（ValueAdd VC） | 2026-10-01 | 2026-10-18T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-10-18",
  "iso_week": "2026-W42",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-04-18",
  "prior_date": "2026-09-13",
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 4.13,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

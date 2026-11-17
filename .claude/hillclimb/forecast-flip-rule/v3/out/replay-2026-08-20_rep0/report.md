> [DRY RUN] this report was not committed to archive.
# 2026-08-20 AI 泡沫破裂預測報告
報告日期：2026-08-20｜ISO 週次：2026-W34｜預測窗口：2026-08-20 → 2027-02-18｜前次基準：report-2026-08-17（3天前）

## 結論

**結論：no**

三條路徑都還沒啟動：NASDAQ-100 距 52 週高點回撤 4.03%，要再跌約 21.85% 才到 R1 門檻（`valuation.ndx_drawdown`）；HY OAS 2.75%、IG OAS 0.82% 仍很緊，看不到 AI 信用重新定價（`monetary.hy_oas`、`monetary.ig_oas`）；hyperscaler 2026 capex 合計約 $725bn 仍在擴張，沒有下修跡象（`ai.hyperscaler_capex`）。估值與槓桿顯示泡沫存在、下跌時傷害會很大，但本次證據不足以證明任一路徑會在 182 天窗口內完成。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,426.02（2026-08-19），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 4.03%；R1 門檻水位為 22,995.45，從最新收盤還要再下跌約 21.85% 才會觸及（`valuation.ndx_drawdown`）。S&P 500 收 7,707.98（2026-08-19），高於 200 日均線 8.75%、高於 52 週均線 10.25%，與 2026-08-17 相比 −0.48%（`valuation.sp500_trend`）。VIX 15.84（2026-08-18）；2026-08-11 → 2026-08-18 共 7 天的窗口內 VIX +3.66%、S&P 500 −0.47%，沒有出現同漲的 crowded-optionality 警戒（comove = false）（`structural.vix_spx_comove`）。VIX 期限結構仍是 contango，SKEW 偏高（`structural.cross_asset_derivatives`）。

脆弱度偏高：S&P 500 trailing P/E 29.8、Shiller CAPE 41.72（`valuation.sp500_pe_cape`），Mag 7 加權本益比約 29.5x（`valuation.mag7_multiples`）；FINRA margin debt（2026-07）YoY 約 +38.6%（`retail.margin_debt`），美股槓桿 ETF 總 AUM 創紀錄約 $198bn（`structural.leveraged_etf_aum`），SPX 0DTE 佔比在 8 月創下約 62% 的紀錄（`structural.zero_dte`）。不過情緒並不亢奮：CNN Fear & Greed 56（Greed）（`retail.fear_greed`），AAII 偏空 37.9% 高於偏多 34.7%（`retail.aaii`），市場廣度也在確認多頭——A/D 線創新高、RSP YTD 領先 SPY 約 5pp（`breadth.advance_decline`、`breadth.rsp_spy`）。

窗口內的潛在催化劑：Anthropic 目標 10 月 IPO、估值約 $2T（`speculation.upcoming_ai_ipos`），會帶來大量 AI 股權供給；FedWatch 顯示 9/16 會議按兵不動的市場隱含比重約 65.4%（`monetary.fedwatch`）；CPI YoY 3.3%（2026-07）與 5y5y 2.32% 限制了 Fed 緩衝 AI 主導下跌的空間（`monetary.cpi_yoy`、`monetary.t5yifr`）。

**判讀：** R1 距離門檻還很遠（需要再跌約 21.85%）。窗口內要成立，需要像 AI IPO 供給衝擊、獲利或 capex 指引失望、或信用／資金面事件這類催化劑引發強迫去槓桿；目前價格趨勢、廣度與波動率結構都看不到這種傳導。

### R2 資本支出收縮

本次檢索只取得 hyperscaler 2026 capex 的 top-4 合計約 $725bn（2026-08-13）（`ai.hyperscaler_capex`）。Microsoft、Alphabet、Amazon、Meta 各家最新的正式指引數字、所屬財報季，以及與前次指引相比的方向（上修／持平／下修），本次證據都沒有個別確立，因此四家都記為「未確立」，不用記憶補值。本次取得的證據中沒有任何一家下修指引的披露，已確認下修家數為 0。下一次財報的確切日期本次也未確立；182 天窗口會涵蓋兩個季度的財報週期。

需求面目前仍在吸收產能：GPU 現貨租金高於合約價 2 倍以上，產能被利用率吸收（`ai.compute_supply_demand`）；Anthropic 年化營收 $65B、OpenAI $40B（`ai.openai_anthropic_revenue`）。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 $105bn（OpenAI＋Anthropic），年化 capex 約 $725bn（分母：top-4 hyperscaler；Oracle 本次沒有可組合的數字，未納入）（`ai.revenue_capex_gap`）。這個缺口很大，但它衡量的是回本風險，不是短期內的指引方向。BofA 8 月 FMS 中最擁擠的交易是做多半導體（53%）（`institutional.bofa_jpm_survey`）。

**判讀：** R2 目前沒有任何一家下修。窗口內要成立，需要兩家在接下來兩個財報季下修當年度或次年度指引；最可能的推力是需求或變現失望，或者 R1 回撤反過來壓迫 capex。現有的利用率與營收證據都指向繼續擴張。

### R3 AI 信用事件

本次的 AI 信用定價分歧與 AI infrastructure debt financing 掃描都沒有找到窗口內的披露，因此符合 R3 門檻（負債 ≥ USD 5bn、以 AI 資料中心／算力為主業）的借款人名單、它們的債券殖利率／利差／CDS、近期到期與再融資需求，本次都未確立，也沒有取得任何付款違約、covenant waiver、distressed exchange 或 going-concern 的訊號。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）掃描同樣沒有新披露。

整體信用與資金條件很平穩：HY OAS 2.75%（2026-08-18，比 2026-08-17 +5bp），IG OAS 0.82%（+1bp）（`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 0bp，SOFR99−IORB 為 7bp（皆為 2026-08-18），SRF 動用（Standing Repo Facility usage）$0.001bn（2026-08-19）（`monetary.repo_stress_srf`）；銀行對 NBFI 放款約 $2.02T（2026-08-05）（`structural.nbfi_bank_loans`）。美債基差交易槓桿（Treasury basis-trade leverage）：CFTC 槓桿基金美債期貨淨部位 −7,250,927 口（2026-08-11），4 週淨空單減少 311,947 口；MOVE 71.26（2026-08-19，比 2026-08-17 −4.37）；OFR tri-party repo transaction volume $2,361.6bn（`structural.treasury_basis_trade`）。30Y 美債標售需求（auction tail / bid-to-cover）：bid-to-cover 2.39，沒有明顯 tail（2026-08-13）（`monetary.treasury_auctions`）。

**判讀：** R3 沒有找到任何已知的困境借款人，信用利差也沒有重新定價。窗口內要成立，需要大型 neocloud／資料中心借款人出現再融資失敗或違約；但本次在借款人層級的資料缺口很大（見資料缺漏），所以這個判斷主要靠整體信用平穩來支撐。

## 支持 yes 的證據

- [整體] 估值處於極端水位：S&P 500 Shiller CAPE 41.72、trailing P/E 29.8（2026-08-19）（`valuation.sp500_pe_cape`），Mag 7 加權本益比約 29.5x（2026-08-14）（`valuation.mag7_multiples`）；一旦出現觸發點，下跌幅度會很大。
- [R1] 槓桿與投機性部位堆高：FINRA margin debt（2026-07）YoY 約 +38.6%（`retail.margin_debt`），美股槓桿 ETF AUM 創紀錄約 $198bn、TQQQ 37.3、SOXL 17.3（2026-08-17）（`structural.leveraged_etf_aum`），SPX 0DTE 佔比創紀錄約 62%（2026-08-14）（`structural.zero_dte`），OCC 7 月選擇權總量 YoY +26%（`structural.options_volume`）；這些部位會在回撤時放大強迫去槓桿。
- [R2] AI 營收對 capex 缺口很大：年化 AI 終端營收約 $105bn vs top-4 年化 capex 約 $725bn（2026-08-17）（`ai.revenue_capex_gap`）；如果變現不如預期，capex 指引有下修壓力。
- [R1] 窗口內有大型 AI 股權供給：Anthropic 目標 10 月 IPO、估值約 $2T（2026-08-17）（`speculation.upcoming_ai_ipos`），可能吸走資金或成為重新定價的時點。
- [R1] 機構部位擁擠：BofA 8 月 FMS 現金比重 3.5%、最擁擠交易為做多半導體（53%）（2026-08-18）（`institutional.bofa_jpm_survey`）。
- [整體] Fed 緩衝空間有限：CPI YoY 3.3%（2026-07）（`monetary.cpi_yoy`）、5y5y 2.32%（`monetary.t5yifr`）、10Y 期限溢價（term premium）0.8393%（2026-08-14）（`monetary.term_premium`）；家戶股票配置 45.76%（2026Q1）（`retail.household_equity_allocation`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.03%（2026-08-19），離 22,995.45 的門檻還需要再跌約 21.85%（`valuation.ndx_drawdown`）；S&P 500 高於 200 日均線 8.75%（`valuation.sp500_trend`）。
- [R3] 信用沒有重新定價：HY OAS 2.75%、IG OAS 0.82%（2026-08-18）（`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）0bp、SRF 動用 $0.001bn（`monetary.repo_stress_srf`）。
- [R2] capex 仍在擴張：hyperscaler 2026 capex top-4 合計約 $725bn，沒有下修披露（2026-08-13）（`ai.hyperscaler_capex`）；GPU 現貨租金高於合約價 2 倍以上，產能被利用率吸收（`ai.compute_supply_demand`）；Anthropic 年化營收 $65B、OpenAI $40B（2026-08-17）（`ai.openai_anthropic_revenue`）。
- [R1] 廣度健康：A/D 線創新高、新高多於新低（2026-08-14）（`breadth.advance_decline`），RSP YTD 領先 SPY 約 5pp（`breadth.rsp_spy`）；這不是少數權值股獨撐的頂部型態。
- [R1] 情緒沒有過熱：CNN Fear & Greed 56（`retail.fear_greed`），AAII 偏空 37.9% 高於偏多 34.7%（`retail.aaii`），Cboe equity put/call 0.65（`speculation.equity_put_call`），VIX 與 S&P 500 沒有同漲（`structural.vix_spx_comove`）。
- [整體] 美債市場運作有序：30Y 標售 bid-to-cover 2.39、沒有明顯 tail（2026-08-13）（`monetary.treasury_auctions`）；MOVE 71.26 下降（`structural.treasury_basis_trade`）；IPO 週報沒有出現無營收 AI IPO 暴衝（2026-08-19）（`speculation.ipo_heat`）。

## 與前期比較

前次結論：無前次預測（report-2026-08-17 為舊格式評分報告）

report-2026-08-17 是舊格式評分報告，不轉換成 yes/no；flip_evidence 為 []。自 2026-08-17 以來的主要變化：

- S&P 500 −0.48%（7,745.06 → 7,707.98）（`valuation.sp500_trend`）；NASDAQ-100 回撤維持在 4.03%（`valuation.ndx_drawdown`）。
- HY OAS +5bp 到 2.75%（`monetary.hy_oas`）；MOVE −4.37 到 71.26（`structural.treasury_basis_trade`）。
- 10Y：ΔDGS10 −1bp、ΔDFII10 −3bp、ΔT10YIE +2bp（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）；T10YIE 的觀測窗口與另外兩者不同，判讀：不可判（視窗不一致）。

以上變化幅度都很小，不足以改變任一路徑的判斷。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源完成了檢索，但標為 ✗ NOT DISCLOSED，可能影響判斷的是：valuation.ai_credit_schism、structural.ai_infrastructure_debt、monetary.private_credit_liquidity 這三個 R3 相關掃描在窗口內都沒有披露，因此 R3 借款人層級的利差、到期與困境訊號本次未確立；如果這類事件確實存在但沒被搜尋到，R3 判斷可能被低估。ai.hyperscaler_financing_mix 與 ai.capital_cycle 的 quarterly_state 可用（沿用的季頻狀態：capex 已超過 FCF、2026 hyperscaler IG 發債約 $182bn；供給側 capex 年增約 77%），但 30 日 event_scan 沒有新披露，因此整列標為 ✗ NOT DISCLOSED，只作為背景，不作為證據。ai.token_growth 的搜尋結果只有營收成長（Anthropic run-rate 年增約 7×），沒有 token volume 指標，所以標為 ✗ NOT DISCLOSED。其餘 ✗ NOT DISCLOSED 來源（valuation.analyst_tp_decomposition、retail.social_sentiment、retail.naaim、monetary.pboc、ai.customer_concentration_rpo、ai.depreciation_life、structural.global_leveraged_approvals）都是確認性輸入，不太可能改變答案。margin debt 對總市值比率本次未確立。

最大的不確定性：

1. 接下來兩個財報季的 hyperscaler capex 指引（R2）：如果有兩家下修，答案會直接翻成 yes；目前的利用率證據指向反方向。
2. Anthropic 10 月 IPO（R1）：約 $2T 的股權供給加上已經堆高的槓桿部位，可能觸發 AI 股重新定價，推向 yes。
3. R3 借款人層級資料缺口：本次沒有取得任何 neocloud／資料中心借款人的信用定價；如果出現再融資失敗，會推向 yes，並經由 R1 傳導。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7707.98 | FRED API (series_id=SP500) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 8.75 | FRED API (series_id=SP500) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 10.25 | FRED API (series_id=SP500) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29426.02 | FRED API (series_id=NASDAQ100) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.03 | FRED API (series_id=NASDAQ100) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1） | 45.76080873390133（約 45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.75 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.82 | FRED API (series_id=BAMLC0A0CM) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.71 | FRED API (series_id=DGS10) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | -1.0 | FRED API (series_id=DGS10) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.41 | FRED API (series_id=DFII10) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | -3.0 | FRED API (series_id=DFII10) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.3 | FRED API (series_id=T10YIE) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | 2.0 | FRED API (series_id=T10YIE) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 86.48 | FRED API (series_id=DCOILWTICO) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-20T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.32 | FRED API (series_id=T5YIFR) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8393 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.65 | FRED API (series_id=SOFR) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.72 | FRED API (series_id=SOFR99) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-08-20 | 2026-08-20T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.001 | FRED API (series_id=RPONTTLD) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6759955.0（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-12 | 2026-08-20T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5927307.0（€5.93T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-14 | 2026-08-20T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-20T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.84 | FRED API (series_id=VIXCLS) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 15.84 | FRED API (series_id=VIXCLS, SP500) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日，base 2026-08-11） | 3.66 | FRED API (series_id=VIXCLS, SP500) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日，base 2026-08-11） | -0.47 | FRED API (series_id=VIXCLS, SP500) | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2016.0821（$2.02T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-05 | 2026-08-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7250927（口） | CFTC TFF futures-only (UST 2Y/5Y/10Y/Ultra-10Y/Bond/Ultra-Bond) | 2026-08-11 | 2026-08-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | 311947（口） | CFTC TFF futures-only | 2026-08-11 | 2026-08-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 71.26 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index delta_abs | -4.37 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2361.6 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-08-19 | 2026-08-20T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl / GuruFocus [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | 賣方 TP 摘要 WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✗ NOT DISCLOSED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | StockCharts WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | CNN [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | FINRA / GuruFocus WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | AAII [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WSB / X WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | naaim.org [primary: SEARCH] | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | BofA / JPM WebSearch | ✓ SEARCH-VERIFIED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py（DFEDTARU ok；DFEDTARL ok） | ✓ API |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直接取得） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） | ✓ API |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | Reuters / TreasuryDirect WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | CME FedWatch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW ok；JPNASSETS ok） | ✓ API |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | PBoC / NBS WebSearch | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | BDC 披露 WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | 財報摘要 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | 供應商披露 WebSearch（結果只有營收成長，沒有 token volume 指標） | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | CNBC / The Information WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | 財報電話 WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | 產業披露 WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch：quarterly_state 沿用季頻狀態；event_scan 30d 掃描完成、沒有披露 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | 綜合披露 WebSearch（分母：top-4） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | 10-K / 10-Q WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch：quarterly_state 沿用；event_scan 30d 掃描完成、沒有披露 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | 新聞 / SEC EDGAR WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | Renaissance Capital WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | Finviz / Benzinga / StockTwits WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | Bloomberg / CNBC / Yahoo WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR / openinsider WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | Cboe [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | etf.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com WebSearch（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | KRX / TWSE / JPX / ESMA WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | OCC WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | Cboe / SpotGamma WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS ok；vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | FINRA WebSearch（僅作交叉檢核） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | 信用市場 WebSearch（30d） | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds ok；move_index ok；ofr_repo ok）；WebSearch 沒有找到額外披露 | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.8、Shiller CAPE 41.72（原定來源：multpl / GuruFocus） | S&P 500 Shiller CAPE August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio （GuruFocus） | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權本益比約 29.5x（AI leader P/S vs 10 年均值本次未確立） | Magnificent 7 weighted P/E August 2026 | https://www.fool.com/investing/2026/08/14/the-best-magnificent-seven-stocks-to-buy-in-august/ （The Motley Fool） | 2026-08-14 | 2026-08-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 領先 SPY 約 5pp（URL 路徑顯示原文 2026-06-10，搜尋結果標示的資料日期為 2026-08-17） | RSP vs SPY YTD 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St.） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 top-10 集中度約 40% | S&P 500 top 10 concentration 2026 | https://www.ebc.com/forex/rsp-vs-spy （EBC） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| breadth.advance_decline | A/D 線創新高、新高多於新低，3 項廣度訊號確認多頭 | NYSE advance decline breadth August 2026 | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/ （StockCharts） | 2026-08-14 | 2026-08-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 56（Greed） | CNN Fear and Greed today August 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-07 月資料）水位約 1,417,225（百萬美元，約 $1.42T）、YoY 約 +38.6% | FINRA margin debt July 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt （GuruFocus，原定來源 FINRA） | 2026-07-31 | 2026-08-20T09:30:00+08:00 |
| retail.aaii | AAII 偏空 37.9%、偏多 34.7% | AAII investor sentiment August 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-08-12 | 2026-08-20T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA 8 月 FMS：現金 3.5%、最擁擠交易為做多半導體 53%（JPM 調查本次未取得） | BofA fund manager survey August 2026 | https://www.hedgefundtips.com/august-2026-bank-of-america-global-fund-manager-survey-results-summary/ （HedgeFundTips 摘要） | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 標售 bid-to-cover 2.39、沒有明顯 tail | US Treasury 30-year auction August 2026 | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2026/R_20260813_2.pdf （TreasuryDirect） | 2026-08-13 | 2026-08-20T09:30:00+08:00 |
| monetary.fedwatch | FedWatch 9/16 會議按兵不動約 65.4%（URL 路徑顯示原文 2026-08-07，搜尋結果標示的資料日期為 2026-08-19） | CME FedWatch September 2026 hold probability | https://www.cnbc.com/2026/08/07/odds-the-fed-hikes-in-september-tumble-following-big-july-jobs-miss.html （CNBC，原定來源 CME FedWatch） | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex top-4 合計約 $725bn（各家個別指引與方向本次未確立） | hyperscaler 2026 capex guidance Microsoft Google Amazon Meta | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-13 | 2026-08-20T09:30:00+08:00 |
| ai.openai_anthropic_revenue | OpenAI 年化營收 $40B、Anthropic $65B（2026-07） | OpenAI Anthropic annualized revenue August 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html （CNBC） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| ai.compute_supply_demand | GPU 現貨租金高於合約價 2 倍以上，產能被利用率吸收 | AI GPU rental pricing utilization August 2026 | https://www.uncoveralpha.com/p/amazon-google-microsoft-meta-q2-earnings （UncoverAlpha） | 2026-08-13 | 2026-08-20T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] capex 已超過 FCF；2026 hyperscaler IG 發債約 $182bn（+1300%） | hyperscaler external financing capex FCF debt 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow （FactSet） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $105bn（OpenAI 40＋Anthropic 65）vs 年化 capex 約 $725bn（分母：top-4） | AI revenue to capex gap 2026 | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| ai.capital_cycle | [quarterly_state] 供給側 capex 年增約 77%；需求側 token／營收成長並存，但沒有可引用的增速，增速證據不足，本次不判定週期階段 | AI capex growth rate supply demand 2026 | https://valueaddvc.com/ai-spending （ValueAdd VC） | 2026-08-13 | 2026-08-20T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 掃描：0 件合格事件 | AI rename SPAC ticker change August 2026 | Renaissance Capital / SEC EDGAR / 新聞掃描 | — | 2026-08-20T09:30:00+08:00 |
| speculation.ipo_heat | US IPO 週報：pipeline 擴大、Metals Royalty 直接上市；無營收 AI IPO 暴衝 0 起（週 IPO 數與首日報酬本次未確立） | US IPO weekly recap August 2026 | https://www.renaissancecapital.com/IPO-Center/News/118238/US-IPO-Weekly-Recap-Pipeline-swells-with-sizable-IPO-filings-as-Metals-Roya （Renaissance Capital） | 2026-08-19 | 2026-08-20T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot（單日 ≥100%、市值 < $1B、2 個以上主題、弱基本面）掃描：0 檔 | microcap 100% single day surge quantum AI August 2026 | Finviz / Benzinga / StockTwits movers 掃描 | — | 2026-08-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 10 月 IPO、估值約 $2T | Anthropic OpenAI IPO 2026 | https://finance.yahoo.com/markets/article/spacex-openai-and-anthropic-here-are-the-most-anticipated-ipos-in-2026-114439441.html （Yahoo Finance） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 14 日內合格 Form 4 集中賣出：0 起 | insider Form 4 AI executives August 2026 | SEC EDGAR / openinsider 掃描 | — | 2026-08-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.65（來源沒有標明是單日還是 5 日平均） | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio （thetrading.tools，原定來源 Cboe） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美股槓桿 ETF 總 AUM 創紀錄約 $198bn；TQQQ 37.3、SOXL 17.3（$bn；NVDL、TSLL、CONL、SQQQ 本次未確立） | leveraged ETF AUM record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing，原定來源 etf.com） | 2026-08-17 | 2026-08-20T09:30:00+08:00 |
| structural.us_single_stock_etf | 美股單一個股槓桿 ETF 過去 30 日新核准／上市掃描：0 件 | single-stock leveraged ETF launch SEC August 2026 | SEC EDGAR / ETF.com new launches 掃描 | — | 2026-08-20T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 8 月佔比創紀錄約 62% | 0DTE SPX volume share August 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august （Cboe） | 2026-08-14 | 2026-08-20T09:30:00+08:00 |
| structural.options_volume | OCC 2026-07 選擇權總量 YoY +26%、YTD 日均超過 71M 口 | OCC July 2026 options volume | https://mondovisione.com/media-and-resources/news/occ-july-2026-monthly-volume-data-202686 （Mondo Visione，原定來源 OCC） | 2026-07-31 | 2026-08-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 15.84、期限結構 contango、SKEW 偏高（SKEW 數值與股債相關性本次未確立） | VIX term structure SKEW August 2026 | https://www.thetrading.tools/vix-term-structure （thetrading.tools） | 2026-08-18 | 2026-08-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 交叉檢核（2026-07 月資料）：YoY +38.6%，同 retail.margin_debt；margin debt／市值比率本次未確立 | FINRA margin debt equity market cap ratio 2026 | https://kalkine.com/news/financial/finra-margin-debt-hits-record-15-trillion-ratio-climbs-to-340 （Kalkine） | 2026-07-31 | 2026-08-20T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-20",
  "iso_week": "2026-W34",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-18",
  "prior_date": "2026-08-17",
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 4.03,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

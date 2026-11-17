> [DRY RUN] this report was not committed to archive.

# 2026-08-24 AI 泡沫破裂預測報告
報告日期：2026-08-24｜ISO 週次：2026-W35｜預測窗口：2026-08-24 → 2027-02-22｜前次基準：report-2026-08-20（4天前）

## 結論

**結論：no**

三條路徑都沒有已在進行中的跡象：NASDAQ-100 距 52 週高點回撤 4.41%，離 R1 門檻還需再跌約 21.54%；top-4 hyperscaler 2026 capex 合計約 $725bn（+77% YoY），本次證據沒有任何一家下修；HY OAS 2.75%、IG OAS 0.82%，信用端未見 R3 所需的壓力傳導。估值與槓桿指標顯示泡沫脆弱度高，但本次未見能在 182 天內完成破裂的觸發與傳導證據，因此依基準率判 no。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

依 `valuation.ndx_drawdown`：NASDAQ-100 最新收盤 29,308.86（2026-08-21），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 4.41%。R1 門檻水位為 22,995.45，自最新收盤還需再跌約 21.54% 才會觸及；`r1_met` 為 false。

背景脈絡：S&P 500 收 7,674.37（2026-08-21），高於 200 日均線 8.15%、高於 52 週均線 9.61%（`valuation.sp500_trend`），價格延伸幅度大，均值回歸風險偏高。2026-08-13 → 2026-08-20 這 7 天裡 VIX 由 14.63 升到 16.01（+9.43%），同期 S&P 500 −2.02%，屬於正常的反向變動，co-movement 警戒未觸發（`structural.vix_spx_comove`）。估值方面，S&P 500 trailing P/E 約 26.2、Shiller CAPE 約 41.2（`valuation.sp500_pe_cape`），Mag 7 加權 P/E 約 29.5x（`valuation.mag7_multiples`）。槓桿與投機方面，FINRA margin debt（2026-07）YoY 約 +38.6%（`retail.margin_debt`），美股槓桿 ETF 總 AUM 約 $198bn、創紀錄（`structural.leveraged_etf_aum`），SPX 0DTE 佔比約 62.4%、創紀錄（`structural.zero_dte`）。窗口內已知的潛在催化劑是 Anthropic 目標 10 月 IPO、估值約 $2T（`speculation.upcoming_ai_ipos`），這會帶來大量新股供給。

**判讀：** R1 距離門檻還很遠（還需再跌約 21.54%）。要在窗口內觸發，需要一次強制去槓桿事件：槓桿 ETF、margin debt 與 0DTE 部位集中平倉，或 R3／利率衝擊引發的連鎖拋售。本次資料沒有這類傳導正在發生的證據。

### R2 資本支出收縮

依 `ai.hyperscaler_capex`：本次取得的是 Q2 財報季後的彙整數字，Microsoft、Alphabet、Amazon、Meta 2026 年 capex 合計約 $725bn（+77% YoY，資料日 2026-08-13）。本次證據沒有逐家列出最新指引金額，也沒有逐家相對前次指引的方向（上修／持平／下修），所以逐家方向本次無法確認；不過合計成長 +77% YoY 與下修方向不符，本次證據裡沒有任何一家下修的披露，已下修家數為 0。需求側方面，GPU 現貨租金高於合約價 2 倍以上，產能被使用率吸收（`ai.compute_supply_demand`，2026-08-13）；Anthropic run-rate 約 $65B、OpenAI 約 $40B（`ai.openai_anthropic_revenue`，2026-08-17）。下一次財報的確切日期本次沒有取得；窗口（到 2027-02-22）依季度節奏應涵蓋兩輪季報，但具體日期無法確認。

**判讀：** R2 目前沒有任何一家下修，需求訊號（GPU 現貨溢價、AI run-rate 擴張）也支撐 capex 續增。要在窗口內觸發，需要至少兩家在未來兩輪季報中下修指引，通常要先出現 R1 等級的股價重挫或 AI 需求明顯降溫，而本次沒有這類證據。

### R3 AI 信用事件

本次的 AI 信用定價分歧（equity-vs-credit schism）掃描與 AI infrastructure debt financing / vendor-financing loops 掃描都已完成，但 14／30 日窗口內沒有合格披露，因此沒有個別 AI 基礎設施借款人的債券殖利率、利差、CDS 或評級動作可以引用。哪些借款人符合 R3 規模門檻（負債 ≥ 50 億美元、以 AI 資料中心／算力為主業），本次也沒有取得負債數字，不予認定。整體信用環境方面，HY OAS 2.75%、IG OAS 0.82%（2026-08-20，`monetary.hy_oas`、`monetary.ig_oas`），信用利差偏緊。repo 資金壓力（SOFR−IORB）為 −2.0bps，SOFR99−IORB 為 6.0bps（皆為 2026-08-20），SRF 動用（Standing Repo Facility usage）為 0.0（2026-08-21，`monetary.repo_stress_srf`）。銀行對 NBFI 放款約 $2.03T，週變動持平（`structural.nbfi_bank_loans`）。產業層級的 AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 $105bn（OpenAI 約 $40bn ＋ Anthropic 約 $65bn）對年化 capex 約 $725bn（分母只含 top-4；Oracle 本次沒有可組合的數字，未納入），比值約 14.5%（`ai.revenue_capex_gap`）。這是長期償債能力的脆弱點，但不是窗口內的違約訊號。

**判讀：** R3 沒有任何已知的困境訊號（未見付款違約、covenant waiver、distressed exchange 或 going-concern 字樣）。信用利差偏緊、repo 平穩，表示再融資管道仍然暢通。要在窗口內觸發，需要某家大型 AI 基礎設施借款人出現再融資失敗，本次證據沒有指向這種情形。

## 支持 yes 的證據

- [整體] 估值處於極端水位：S&P 500 Shiller CAPE 約 41.2、trailing P/E 約 26.2（2026-08-20，`valuation.sp500_pe_cape`），Mag 7 加權 P/E 約 29.5x，高於 S&P 500 的約 25.6x（2026-08-14，`valuation.mag7_multiples`）；一旦出現觸發事件，下跌空間會很大。
- [R1] 散戶與結構性槓桿處於高檔：FINRA margin debt（2026-07）約 1,417,225、YoY 約 +38.6%（`retail.margin_debt`），美股槓桿 ETF AUM 約 $198bn、創紀錄（TQQQ 31.3、SOXL 17.3，2026-08-17，`structural.leveraged_etf_aum`），SPX 0DTE 佔比約 62.4%、創紀錄（2026-08-14，`structural.zero_dte`）；一旦出現衝擊，強制去槓桿可能放大回撤。
- [R3] AI 營收對 capex 缺口（revenue-to-capex gap）很大：年化 AI 終端營收約 $105bn，對 top-4 年化 capex 約 $725bn（2026-08-17，`ai.revenue_capex_gap`）；capex 回收高度依賴未來營收成長，若融資條件轉緊，債務端的脆弱度就會浮現。
- [R1] 窗口內有大型股票供給事件：Anthropic 目標 10 月 IPO、估值約 $2T（2026-08-17，`speculation.upcoming_ai_ipos`），可能吸走 AI 類股資金，或成為情緒峰值的標記。
- [R1] Fed 緩衝空間有限：CPI YoY 3.3%（2026-07，`monetary.cpi_yoy`），FedWatch 隱含 9/16 按兵不動約 68.4%、尾端情境為升息（2026-08-20，`monetary.fedwatch`），AI 股若下跌，降息救市的空間受限。
- [整體] 價格延伸幅度大：S&P 500 高於 200 日均線 8.15%、高於 52 週均線 9.61%（2026-08-21，`valuation.sp500_trend`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.41%（最新收盤 29,308.86，2026-08-21；高點 30,660.6，2026-06-02），R1 門檻水位 22,995.45，還需再跌約 21.54%（`valuation.ndx_drawdown`）；R1 起點離觸發很遠。
- [R2] capex 仍在擴張而不是收縮：top-4 hyperscaler 2026 capex 合計約 $725bn、+77% YoY（2026-08-13，`ai.hyperscaler_capex`），本次證據沒有任何一家下修；GPU 現貨租金高於合約價 2 倍以上，產能被使用率吸收（2026-08-13，`ai.compute_supply_demand`）。
- [R3] 信用端沒有壓力：HY OAS 2.75%、IG OAS 0.82%（2026-08-20，`monetary.hy_oas`、`monetary.ig_oas`），SOFR−IORB −2.0bps、SRF 動用 0.0（`monetary.repo_stress_srf`），再融資管道暢通，與 R3 所需的違約／distressed exchange 環境相距甚遠。
- [R2] AI 需求端營收持續擴張：Anthropic 年化營收約 $65B、OpenAI 約 $40B（2026-08-17，`ai.openai_anthropic_revenue`），支撐 hyperscaler 維持 capex 指引。
- [整體] 情緒沒有到亢奮：CNN Fear & Greed 55（Greed，2026-08-21，`retail.fear_greed`），AAII 偏多 35.5% 低於偏空 39.9%（週結 2026-08-19，`retail.aaii`），Cboe equity put/call 0.52，未低於 0.50（2026-08-19，`speculation.equity_put_call`）；microcap moonshot 與 +AI 改名／SPAC 掃描都是 0 件（`speculation.microcap_moonshots`、`speculation.ai_rename_spac`）。
- [整體] 廣度擴散而不是收窄：RSP 的 YTD 表現領先 SPY 約 5pp，市場領導由 top-100 擴散到 bottom-400（2026-08-17，`breadth.rsp_spy`、`breadth.advance_decline`）。
- [R1] 美債市場平穩：MOVE 73.4（2026-08-21），CFTC 槓桿基金美債期貨淨空 −7,218,048 口，4 週內減少 244,468 口（2026-08-18，`structural.treasury_basis_trade`）；30Y 標售沒有明顯 tail（2026-08-13，`monetary.treasury_auctions`），沒有國債市場失序（Treasury market dysfunction）的跡象。

## 與前期比較

前次結論：無前次預測（report-2026-08-20 為舊格式評分報告）

report-2026-08-20 是舊格式的評分報告，沒有 yes/no 預測，舊評分不轉換為結論，flip_evidence 為 []。自 2026-08-20 以來的主要數據變化：

- NASDAQ-100 回撤水位見 R1 節；S&P 500 由 7,641.16（2026-08-20）升到 7,674.37（2026-08-21），+0.43%。
- 10Y 分解：ΔDGS10 0.0bps、ΔDFII10 0.0bps、ΔT10YIE 0.0bps，判讀為無變動；其中 DGS10、DFII10 沒有新觀測（最新仍是 2026-08-20），T10YIE 已更新到 2026-08-21。
- HY／IG OAS、SOFR、SOFR99、VIX、WALCL、ECB 資產負債表等序列都沒有新觀測，Δ 為 0，視為持平。
- MOVE 由 73.18 升到 73.4（+0.22）；OFR tri-party repo transaction volume 由 2,400.4 降到 2,328.6（$bn，−2.99%）。
- 10Y 期限溢價（term premium，Kim-Wright）0.8393%（2026-08-14），trailing 約 7 日變動 +1.4bps。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源的檢索已完成，但沒有合格的當期披露（✗ NOT DISCLOSED），不作為證據引用：`valuation.analyst_tp_decomposition`、`valuation.ai_credit_schism`、`retail.social_sentiment`、`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.pboc`、`monetary.private_credit_liquidity`、`ai.token_growth`（搜尋結果是 Anthropic run-rate 年增約 7×，屬營收指標，不是 token volume，所以不採計）、`ai.customer_concentration_rpo`、`ai.hyperscaler_financing_mix`（quarterly_state 可取得：top-5 capex 超過 FCF、發債擴張；30 日 event_scan 沒有新的融資事件）、`ai.depreciation_life`、`ai.capital_cycle`（quarterly_state 可取得；30 日 event_scan 沒有進出場／取消事件；增速證據不足，本次不判定週期階段）、`structural.global_leveraged_approvals`、`structural.ai_infrastructure_debt`。其中與答案最相關的是 `valuation.ai_credit_schism` 與 `structural.ai_infrastructure_debt`：R3 借款人層級的信用定價與融資事件本次空白，若實際存在未被捕捉的困境訊號，可能使 R3 判讀偏向 yes。不過整體 HY OAS 偏緊，不支持這種可能性。`monetary.private_credit_liquidity` 空白代表私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）本次無法確認，同樣屬於 R3 傳導鏈的盲點。

其他資料限制：R2 逐家指引金額與方向本次沒有取得（只有 top-4 合計）；margin debt 對總市值比率本次沒有取得市值來源，無法計算；`breadth.advance_decline` 只有質性描述，沒有數值 A/D ratio；`speculation.ipo_heat` 只有 YTD 件數，沒有週首日報酬與無營收發行人比例；`structural.cross_asset_derivatives` 沒有 rolling stock-bond correlation；槓桿 ETF 個別 AUM 只取得 TQQQ、SOXL。

最大的不確定性：

- 未來兩輪 hyperscaler 季報（日期本次未取得）：若兩家同步下修 capex 指引，R2 直接成立，會把答案推向 yes。目前 +77% YoY 的軌跡指向相反方向。
- Anthropic 10 月 IPO 的定價與承接：若定價失敗或上市後重挫，可能觸發 AI 類股重新定價並經槓桿部位放大，使 R1 的可能性上升，答案偏向 yes。
- 通膨與 Fed 路徑：CPI 3.3%、FedWatch 尾端為升息；若升息情境實現並推高實質利率，高估值股票的折現率衝擊會加大 R1 風險，答案偏向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7674.37 | FRED API (series_id=SP500) via fetch_macro.py sp500_trend | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線偏離 %） | 8.15 | FRED API (series_id=SP500) via fetch_macro.py sp500_trend | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線偏離 %） | 9.61 | FRED API (series_id=SP500) via fetch_macro.py sp500_trend | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（相對前次基準 %） | 0.43 | FRED API (series_id=SP500) via fetch_macro.py sp500_trend | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29308.86 | FRED API (series_id=NASDAQ100) via fetch_macro.py ndx_drawdown | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) via fetch_macro.py ndx_drawdown | 2026-06-02 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.41 | FRED API (series_id=NASDAQ100) via fetch_macro.py ndx_drawdown | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) via fetch_macro.py ndx_drawdown | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1 家庭股票配置 %） | 45.76080873390133（約 45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 2.75 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（IG OAS %） | 0.82 | FRED API (series_id=BAMLC0A0CM) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（10Y 殖利率 %） | 4.69 | FRED API (series_id=DGS10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（相對前次基準，無新觀測） | 0.0 | FRED API (series_id=DGS10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（10Y 實質殖利率 %） | 2.35 | FRED API (series_id=DFII10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（10Y breakeven %） | 2.34 | FRED API (series_id=T10YIE) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（WTI 美元／桶） | 86.48 | FRED API (series_id=DCOILWTICO) | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 CPI YoY %） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（5y5y forward %） | 2.34 | FRED API (series_id=T5YIFR) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（10Y 期限溢價 %，Kim-Wright） | 0.8393 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 約 7 日） | 1.4 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.63 | FRED API (series_id=SOFR) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.71 | FRED API (series_id=SOFR99) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-24 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，$bn） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.walcl | WALCL latest（Fed 資產負債表） | 6745699.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（ECB 資產負債表） | 5927307.0（€5.93T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（BOJ 資產負債表） | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.01 | FRED API (series_id=VIXCLS) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of；base_date 2026-08-13） | 16.01 | FRED derived block vix_spx_comove（fetch_macro.py） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日 %） | 9.43 | FRED derived block vix_spx_comove（fetch_macro.py） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日 %） | −2.02 | FRED derived block vix_spx_comove（fetch_macro.py） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（銀行對 NBFI 放款，$bn） | 2026.1422（約 $2.03T） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-12 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | −7218048 | CFTC TFF futures-only（fetch_macro.py cftc_lev_funds） | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 244468 | CFTC TFF futures-only（fetch_macro.py cftc_lev_funds） | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.4 | Yahoo Finance chart API ^MOVE（fetch_macro.py move_index） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2328.6 | OFR STFM REPO-TRIV1_TV_TOT-P（fetch_macro.py ofr_repo） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值 / S&P 500 P/E and Shiller CAPE | multpl / GuruFocus，WebSearch primary | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值 / Mag 7 weighted P/E and AI leader P/S | 市場資料 WebSearch | ✓ SEARCH-VERIFIED（只取得加權 P/E；AI leader P/S 對 10 年均值未取得） |
| valuation.analyst_tp_decomposition | 估值 / Analyst TP upgrade decomposition | 賣方摘要 WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | 估值 / S&P 500 price-trend deviation | fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值 / NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值 / AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✗ NOT DISCLOSED |
| breadth.rsp_spy | 廣度 / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度 / Top-10 concentration in S&P 500 | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度 / Advance/decline ratio, new high/low ratio | 市場資料 WebSearch | ✓ SEARCH-VERIFIED（質性廣度描述，無數值 ratio） |
| retail.fear_greed | 散戶 / CNN Fear & Greed Index | CNN，WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶 / Margin Debt: FINRA | FINRA / GuruFocus WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶 / Retail survey: AAII | AAII，WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶 / Social sentiment proxies | WSB / X WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶 / Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶 / NAAIM Exposure Index | naaim.org WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | 機構 / BofA Fund Manager Survey and JPM institutional survey | BofA / JPM WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣 / Fed funds rate: FRED | fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣 / High Yield OAS | fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣 / Investment Grade OAS | fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣 / 10Y Treasury yield | fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣 / 10Y Treasury real yield / TIPS | fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣 / 10Y breakeven inflation rate | fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣 / WTI crude oil price | fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣 / CPI YoY: FRED | fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣 / 5y5y forward inflation expectation | fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣 / 10Y 期限溢價（term premium）: FRED | fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣 / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py（SOFR、SOFR99、IORB、RPONTTLD；repo_stress status ok） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣 / 美債標售需求（auction tail / bid-to-cover） | Reuters / TreasuryDirect WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣 / Fed funds rate path expectations | CME FedWatch 摘要 WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣 / Fed balance sheet: FRED | fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣 / Global central bank liquidity cross-check | fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣 / PBoC aggregate financing | PBoC / NBS WebSearch | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | 貨幣 / Private-credit / non-bank fund liquidity stress | BDC／interval fund 披露 WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | 財報摘要 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED（只取得 top-4 合計；逐家方向未取得） |
| ai.token_growth | AI / AI token volume growth rate | 供應商披露 WebSearch | ✗ NOT DISCLOSED（無 token volume 指標） |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | CNBC / Bloomberg WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | 產業披露 WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch：quarterly_state（stock-of-state）＋event_scan（30d） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口（revenue-to-capex gap） | 綜合披露 WebSearch（分母 top-4） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K / 10-Q WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI / 資本週期階段（capital cycle stage） | WebSearch：quarterly_state（stock-of-state）＋event_scan（30d） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機 / Search for past 7 days | 新聞／EDGAR WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機 / IPO market heat | stockanalysis / Renaissance WebSearch（7d） | ✓ SEARCH-VERIFIED（只取得 YTD 件數） |
| speculation.microcap_moonshots | 投機 / Microcap thematic moonshots | Finviz / Benzinga / StockTwits WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機 / Upcoming AI IPOs | Bloomberg / CNBC / Yahoo WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機 / Insider selling at AI / market-leadership companies | SEC EDGAR / openinsider WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機 / Cboe equity-only put/call ratio | Cboe 統計 WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構 / US leveraged ETF AUM | ETF.com WebSearch | ✓ SEARCH-VERIFIED（個別只取得 TQQQ、SOXL） |
| structural.us_single_stock_etf | 結構 / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com WebSearch（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | 結構 / Global leveraged product approvals | KRX / TWSE / JPX / ESMA WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構 / 0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構 / Options total volume | OCC WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構 / Cross-asset derivatives / correlation checks | Cboe / SpotGamma WebSearch | ✓ SEARCH-VERIFIED（stock-bond correlation 未取得） |
| structural.vix_spx_comove | 結構 / VIX / S&P 500 co-movement | fetch_macro.py（VIXCLS＋vix_spx_comove） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構 / Cross-reference only: FINRA margin debt | FINRA / GuruFocus WebSearch（交叉檢核） | ✓ SEARCH-VERIFIED（市值比率未取得） |
| structural.ai_infrastructure_debt | 結構 / AI infrastructure debt financing / vendor-financing loops | 信用市場 WebSearch（30d） | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | 結構 / Bank loans to nondepository financial institutions | fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構 / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）＋WebSearch | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok；WebSearch 無合格平倉事件） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 約 26.2、Shiller CAPE 約 41.2 | Shiller CAPE S&P 500 P/E August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus；預定來源 multpl / GuruFocus） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E 約 29.5x（S&P 500 約 25.6x） | Magnificent 7 weighted P/E August 2026 | https://www.fool.com/investing/2026/08/14/the-best-magnificent-seven-stocks-to-buy-in-august/（The Motley Fool） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 領先 SPY 約 5pp | RSP vs SPY YTD 2026 breadth | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.；URL 路徑為 2026-06-10，搜尋結果資料日 2026-08-17） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 top-10 集中度約 36.5% | S&P 500 top 10 concentration 2026 | https://www.ebc.com/forex/rsp-vs-spy（EBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.advance_decline | 市場領導由 top-100 擴散到 bottom-400，廣度確認多頭（質性） | market breadth advance decline August 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 55（Greed） | CNN Fear and Greed today August 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）約 1,417,225、YoY 約 +38.6%、MoM −5.7% | FINRA margin debt July 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt（GuruFocus；預定來源 FINRA） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |
| retail.aaii | AAII 偏多 35.5%、偏空 39.9%（週結 2026-08-19） | AAII investor sentiment August 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 標售沒有明顯 tail，12.10% allotted at high | US Treasury 30-year auction August 2026 | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2026/R_20260813_3.pdf（TreasuryDirect） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| monetary.fedwatch | FedWatch 9/16 按兵不動約 68.4%，尾端為升息 | CME FedWatch September 2026 hold probability | https://en.macromicro.me/series/1645/probability-fed-rate-decrease（MacroMicro；預定來源 CME FedWatch） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_capex | top-4（MSFT、GOOGL、AMZN、META）2026 capex 合計約 $725bn，+77% YoY | hyperscaler 2026 capex guidance Microsoft Google Amazon Meta | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.openai_anthropic_revenue | OpenAI 約 $40B、Anthropic 約 $65B run-rate | OpenAI Anthropic annualized revenue August 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html（CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.compute_supply_demand | GPU 現貨租金高於合約價 2 倍以上，產能被使用率吸收 | AI GPU rental pricing utilization August 2026 | https://www.uncoveralpha.com/p/amazon-google-microsoft-meta-q2-earnings（UncoverAlpha） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 超過 FCF，2026 hyperscaler 發債擴張 | hyperscaler external financing capex FCF debt 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow（FactSet） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $105bn（OpenAI 40＋Anthropic 65）vs 年化 capex 約 $725bn（分母：top-4） | AI revenue to capex gap 2026 | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.capital_cycle | [quarterly_state] 供給側 capex 年增約 77%，與需求側 token／營收成長並存 | AI capex growth rate supply demand 2026 | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收投機 IPO 掃描：0 件合格事件 | AI rename SPAC ticker change August 2026 | Renaissance Capital / SEC EDGAR / 新聞掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD 美股 IPO 約 232 件（截至 2026-08-21），沒有單週無營收 AI IPO 暴衝 | US IPO count August 2026 | https://stockanalysis.com/ipos/2026/（StockAnalysis） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot（單日 ≥100%、市值低於 $1B、2 個以上主題、弱基本面）掃描：0 檔 | microcap 100% single day surge quantum AI August 2026 | Finviz / Benzinga / StockTwits movers 掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 10 月 IPO，估值約 $2T | Anthropic OpenAI IPO 2026 | https://finance.yahoo.com/markets/article/spacex-openai-and-anthropic-here-are-the-most-anticipated-ipos-in-2026-114439441.html（Yahoo Finance） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 14 日內合格 Form 4 集中賣出：0 起 | insider Form 4 AI executives August 2026 | SEC EDGAR / openinsider 掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.52（單日讀數；9 日均總量 0.85） | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio（The Trading Tools；預定來源 Cboe） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美股槓桿 ETF 總 AUM 約 $198bn、創紀錄；TQQQ 31.3、SOXL 17.3（$bn） | leveraged ETF AUM record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing；預定來源 ETF.com） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| structural.us_single_stock_etf | 美股單一個股槓桿 ETF 30 日內新核准／上市：0 件 | single-stock leveraged ETF launch SEC August 2026 | SEC EDGAR / ETF.com new launches 掃描 | — | 2026-08-24T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 8 月佔比約 62.4%，創紀錄 | 0DTE SPX volume share August 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| structural.options_volume | OCC 2026 YTD 日均超過 71M 口，量能高檔（截至 2026-07） | OCC options volume 2026 | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/historical-volume-statistics（OCC） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 16.01，期限結構 contango（IVTS 約 0.82），SKEW 偏高 | VIX term structure SKEW August 2026 | https://www.thetrading.tools/vix-term-structure（The Trading Tools） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 交叉檢核：YoY 約 +38.6%（市值比率未取得） | FINRA margin debt equity market cap ratio 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt（GuruFocus） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-24",
  "iso_week": "2026-W35",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-22",
  "prior_date": "2026-08-20",
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 4.41,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

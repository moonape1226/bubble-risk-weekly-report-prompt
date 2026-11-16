> [DRY RUN] this report was not committed to archive.

# 2026-08-24 AI 泡沫破裂預測報告

報告日期：2026-08-24｜ISO 週次：2026-W35｜預測窗口：2026-08-24 → 2027-02-22｜前次基準：report-2026-08-20（4天前）

## 結論

**結論：no**

三條路徑都沒有已在進行中的觸發：NASDAQ-100 距 52 週高點僅回撤 4.41%，距 R1 門檻仍需再跌約 21.54%（`valuation.ndx_drawdown`）；hyperscaler top-4 的 2026 capex 合計約 $725bn、年增約 77%，方向仍是擴張而非下修（`ai.hyperscaler_capex`）；HY OAS 2.75%、IG OAS 0.82% 顯示信用市場尚未對 AI 借款人重定價（`monetary.hy_oas`、`monetary.ig_oas`）。估值與槓桿極端說明泡沫存在、下行幅度可能很大，但本次證據不足以支持破裂會在 182 天內完成。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,308.86（2026-08-21），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 4.41%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45；自最新收盤需再下跌約 21.54% 才會觸及。S&P 500 收 7,674.37（2026-08-21），高於 200 日均線 7,095.72 約 8.15%、高於 52 週均線約 9.61%（`valuation.sp500_trend`），價格仍處延伸段而非破位段。VIX/S&P 500 共振：2026-08-13 → 2026-08-20 的 7 日共享窗口內 S&P 500 −2.02%、VIX +9.43%，屬正常的反向走勢，未觸發 crowded-optionality 共振（`structural.vix_spx_comove`）。窗口內可預見的催化劑包括 Anthropic 目標 10 月 IPO、估值約 $2T（`speculation.upcoming_ai_ipos`）——一筆巨量 AI 股權供給，也是對 AI 估值的直接定價測試；以及 Fed 9/16 會議，FedWatch 顯示按兵不動約 68.4%、尾端為升息（`monetary.fedwatch`）。

**判讀：** R1 距離解析仍遠（需再跌約 21.54%），在 182 天內完成需要一個能同時壓縮估值與盈利預期的觸發——例如 R3 型信用事件外溢、hyperscaler capex 指引轉向，或通膨迫使 Fed 轉向升息；目前三者都未出現，但 CAPE 約 41.2 的估值起點意味一旦觸發，下跌幅度足以觸及門檻。

### R2 資本支出收縮

本次取得的 hyperscaler capex 證據是 top-4（Microsoft、Alphabet、Amazon、Meta）2026 capex 合計約 $725bn、年增約 77%（資料日 2026-08-13，沿用最近一輪季報，`ai.hyperscaler_capex`）。各家個別的最新官方指引數字與相對前次指引的方向，未出現在本次搜尋結果中，因此逐家方向只能記為：Microsoft 未提供指引（本次未取得個別數字）、Alphabet 未提供指引（同）、Amazon 未提供指引（同）、Meta 未提供指引（同）；合計值的方向為擴張，且無任何一家下修的報導。目前下修家數：0／4。下一輪季報的確切日期不在本次證據內；182 天窗口必然涵蓋下一輪與再下一輪季報（含次年度 capex 指引的首次發布），這是 R2 的主要決策節點。需求側證據支持 capex 維持：GPU 現貨租金高於合約價 2 倍以上、產能被利用率吸收（`ai.compute_supply_demand`）；OpenAI 年化營收約 $40B、Anthropic 約 $65B（`ai.openai_anthropic_revenue`）。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 $105bn vs 年化 capex 約 $725bn（分母：top-4，Oracle 本次無可組合的數字故未納入），營收約為 capex 的 14.5%（`ai.revenue_capex_gap`）。

**判讀：** R2 需要四家中兩家在窗口內下修指引，而目前方向是全面上修擴張、需求端（租金、營收 run-rate）仍吸收產能；只有在 R1 型市場重挫壓迫股東回報、或利用率證據轉弱時，下修才可能在下一輪季報出現。

### R3 AI 信用事件

本次 AI 信用定價分歧（equity-vs-credit schism）與 AI infrastructure debt financing / vendor-financing loops 兩項掃描都在各自窗口（14 日／30 日）內沒有找到合格披露，因此無法列出任何符合 R3 規模門檻（負債 ≥ 50 億美元、以 AI 資料中心／算力為主業）之借款人的當期債券殖利率、利差、CDS 或評等動作，也沒有找到任何付款違約、covenant waiver、distressed exchange 或 going-concern 字句的報導。可用的整體信用背景是：HY OAS 2.75%、IG OAS 0.82%（2026-08-20，`monetary.hy_oas`、`monetary.ig_oas`），利差處於極窄水位；repo 資金壓力（SOFR−IORB）為 −2bp、SOFR99−IORB 為 +6bp（2026-08-20），SRF 動用（Standing Repo Facility usage）為 0（2026-08-21，`monetary.repo_stress_srf`）；美債基差交易槓桿（Treasury basis-trade leverage）方面，槓桿基金美債期貨淨部位 −7,218,048 口（2026-08-18），4 週變動 +244,468 口（淨空部位縮小），MOVE 73.4（2026-08-21，`structural.treasury_basis_trade`）。銀行對 NBFI 放款約 $2.03T（2026-08-12，`structural.nbfi_bank_loans`）。結構背景（非本次新證據）：BIS Bulletin 120 指出 AI 私募貸款利差與非 AI 幾乎無差（6.2 vs 6.1 pp），即兩個市場只有一個定價正確。

**判讀：** R3 目前沒有任何可觀測的困境訊號，且整體信用與資金市場平靜；要在窗口內解析為 yes，需要一家大型 neocloud／資料中心借款人在再融資或客戶合約落空時出現違約或 distressed exchange——這類事件通常先有數月的利差走闊與評等下調，而本次並未觀測到這些前導訊號（但也因掃描無披露而無法排除）。

## 支持 yes 的證據

- [整體] 估值處於歷史極端：S&P 500 Shiller CAPE 約 41.2、trailing P/E 約 26.2（2026-08-20，`valuation.sp500_pe_cape`），Mag 7 加權 P/E 約 29.5x（2026-08-14，`valuation.mag7_multiples`），top-10 集中度約 36.5%（2026-08-17，`breadth.top10_concentration`）；起點越高，任何觸發導致的回撤越容易達到 R1 的 25%。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）巨大：年化 AI 終端營收約 $105bn vs 年化 capex 約 $725bn（分母：top-4），營收僅約 capex 的 14.5%（2026-08-17，`ai.revenue_capex_gap`）；若投資人或董事會開始要求回報，下修壓力會集中在下一輪季報。
- [整體] 槓桿與投機部位高檔：FINRA margin debt（2026-07）約 1,417,225（百萬美元）、YoY 約 +38.6%，接近歷史頂部常見的 +40–50% 區間（`retail.margin_debt`）；美股槓桿 ETF 總 AUM 創約 $198bn 新高，TQQQ 31.3、SOXL 17.3（$bn，2026-08-17，`structural.leveraged_etf_aum`）；SPX 0DTE 佔比 8 月創紀錄約 62.4%（2026-08-14，`structural.zero_dte`）。這些部位會放大任何下跌的速度。
- [R1] 窗口內有明確的估值測試催化劑：Anthropic 目標 10 月 IPO、估值約 $2T（2026-08-17，`speculation.upcoming_ai_ipos`）；巨量股權供給與定價結果可能改變市場對 AI 龍頭估值的錨。
- [整體] Fed 緩衝空間有限：CPI YoY 3.3%（2026-07，`monetary.cpi_yoy`）、5y5y 2.34%（`monetary.t5yifr`），FedWatch 9/16 按兵不動約 68.4% 且尾端為升息（2026-08-20，`monetary.fedwatch`），10Y 4.69%（`monetary.dgs10`）、10Y 期限溢價（term premium）0.8393%（2026-08-14，`monetary.term_premium`）；AI 主導的回撤難以期待快速降息托底。
- [R1] 選擇權端偏多頭方向：Cboe equity put/call 0.52（2026-08-19，`speculation.equity_put_call`），接近 < 0.50 的 call-heavy 區間。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.41%（2026-08-21），R1 門檻 22,995.45 需再跌約 21.54%（`valuation.ndx_drawdown`）；S&P 500 仍高於 200 日均線 8.15%（`valuation.sp500_trend`）。在 182 天窗口內從接近高點直接跌 25% 是少見事件，基準率偏向 no。
- [R3] 信用市場未見 AI 重定價或資金壓力：HY OAS 2.75%、IG OAS 0.82%（2026-08-20，`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）−2bp、SRF 動用 0（`monetary.repo_stress_srf`）；MOVE 73.4（2026-08-21，`structural.treasury_basis_trade`）。R3 型違約通常有數月利差走闊的前導，目前不存在。
- [R2] capex 方向是擴張：top-4 2026 capex 合計約 $725bn、年增約 77%（2026-08-13，`ai.hyperscaler_capex`），且需求端吸收產能——GPU 現貨租金高於合約價 2 倍以上（2026-08-13，`ai.compute_supply_demand`）；要四家中兩家在窗口內轉為下修，需要需求急轉。
- [R2] AI 終端營收快速成長：Anthropic 年化營收約 $65B、OpenAI 約 $40B（2026-08-17，`ai.openai_anthropic_revenue`），支撐 hyperscaler 維持投資的理由。
- [整體] 情緒並非狂熱：CNN Fear & Greed 55（Greed，2026-08-21，`retail.fear_greed`），AAII 偏多 35.5%、偏空 39.9%（週結 2026-08-19，`retail.aaii`）；廣度擴散，RSP YTD 領先 SPY 約 5pp（`breadth.rsp_spy`），領導由 top-100 向 bottom-400 擴散（`breadth.advance_decline`）。頂部常見的極端貪婪與窄幅領漲未出現。
- [整體] 投機篩選無異常：+AI 改名／SPAC 7 日掃描 0 件（`speculation.ai_rename_spac`），microcap moonshot 0 檔（`speculation.microcap_moonshots`），AI 領導股 14 日內合格 Form 4 集中賣出 0 起（`speculation.insider_form4`）；2026 YTD IPO 約 232 件、無單週無營收 AI IPO 暴衝（2026-08-21，`speculation.ipo_heat`）。

## 與前期比較

前次結論：無前次預測（report-2026-08-20 為舊格式評分報告）

- report-2026-08-20 為舊格式六維度評分報告，其分數不轉譯為 yes/no；本次為新格式下的首個預測，flip_evidence 為空。
- 相對 2026-08-20，macro 序列幾乎無變動：DGS10 4.69%、DFII10 2.35% 自 2026-08-20 起無新觀測；10Y Δ 分解 ΔDGS10 0.0bp ≈ ΔDFII10 0.0bp + ΔT10YIE 0.0bp，判讀：無變動（partial_stale：DGS10、DFII10 無新觀測，T10YIE 已更新至 2026-08-21）。
- S&P 500 由 7,641.16（2026-08-20）升至 7,674.37（2026-08-21），+0.43%（`valuation.sp500_trend`）。
- 10Y 期限溢價（term premium）序列自身 trailing 7 日 +1.4bp 至 0.8393%（2026-08-14，`monetary.term_premium`），幅度不足以改變路徑判斷。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下為 ✗ NOT DISCLOSED（掃描完成但窗口內無合格披露）、且與路徑判斷相關的缺口：

- `valuation.ai_credit_schism`、`structural.ai_infrastructure_debt`：R3 的兩個主要來源都無窗口內披露，無法列出候選借款人的當期信用定價。若實際上已有某大型 neocloud 利差顯著走闊而未被搜到，可能使 R3 判讀轉向；這是本次最大的資料盲點。
- `monetary.private_credit_liquidity`：私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）無 30 日內披露；無法確認 redemption-request ratio 趨勢或 gate proration / breach，對 R3 傳導判讀有中度影響。
- `ai.hyperscaler_financing_mix`、`ai.capital_cycle`：quarterly_state 可用（top-5 capex > FCF、2026 hyperscaler 發債擴張；供給側 capex 年增約 77%），但 30 日 event_scan 無合格事件，故 Coverage 依 all 聚合為 NOT DISCLOSED，本文不以其為引證依據。
- `ai.token_growth`：搜尋結果只有 Anthropic 營收 run-rate 年增約 7×，並非 token volume 指標，故記為 NOT DISCLOSED，不影響結論。
- `valuation.analyst_tp_decomposition`、`retail.social_sentiment`、`retail.naaim`、`institutional.bofa_jpm_survey`、`monetary.pboc`、`ai.customer_concentration_rpo`、`ai.depreciation_life`、`structural.global_leveraged_approvals`：無窗口內披露，屬確認性輸入，單獨不足以改變答案。
- `breadth.rsp_spy`、`breadth.advance_decline` 的結果 URL 路徑顯示原文為 2026-06-10 文章，搜尋結果標示資料日 2026-08-17；廣度讀數因此權重較低。

最大的不確定性：

1. hyperscaler 下一輪季報（窗口內，確切日期不在本次證據中）與次年度 capex 指引：本次未取得逐家官方指引，若兩家同時下修即直接解析 R2，並可能拖動 R1——偏向 yes 的風險。
2. Anthropic 10 月 IPO 的定價與上市後表現：若定價遠低於約 $2T 或上市後重挫，可能觸發 AI 龍頭估值重設——偏向 yes；若順利則強化 no。
3. 通膨與 Fed 路徑：CPI 3.3% 與 FedWatch 升息尾端若兌現為升息，將削弱估值支撐並收緊信用——偏向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7674.37 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 8.15 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 9.61 | FRED API (series_id=SP500) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend prior_spot（前次基準日收盤） | 7641.16 | FRED API (series_id=SP500) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（NASDAQ-100 最新收盤） | 29308.86 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.41 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1，家戶股票配置 %） | 45.76 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（%） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（%） | 3.50 | FRED API (series_id=DFEDTARL) | 2026-08-23 | 2026-08-24T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.75 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.82 | FRED API (series_id=BAMLC0A0CM) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.69 | FRED API (series_id=DGS10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.35 | FRED API (series_id=DFII10) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.34 | FRED API (series_id=T10YIE) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl） | 86.48 | FRED API (series_id=DCOILWTICO) | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料，%） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.34 | FRED API (series_id=T5YIFR) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 0.8393 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（序列自身 trailing 7 日） | 1.4 | FRED API (series_id=THREEFYTP10) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.63 | FRED API (series_id=SOFR) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.71 | FRED API (series_id=SOFR99) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-24 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，$bn） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps（as_of 與 iorb_date 皆 2026-08-20） | −2.0 | FRED API repo_stress block | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr99_iorb_bps（sofr99_date 與 sofr99_iorb_date 皆 2026-08-20） | 6.0 | FRED API repo_stress block | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6745699.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5927307.0（€5.93T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.01 | FRED API (series_id=VIXCLS) | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of 2026-08-20，base_date 2026-08-13，window_days 7） | 16.01 | FRED API derived block | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 9.43 | FRED API derived block | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | −2.02 | FRED API derived block | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2026.1422（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-12 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | −7,218,048 | CFTC TFF futures-only | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | +244,468 | CFTC TFF futures-only | 2026-08-18 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 73.4 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2328.6 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-08-21 | 2026-08-24T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值 / S&P 500 P/E and Shiller CAPE | multpl / GuruFocus WebSearch | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值 / Mag 7 weighted P/E and AI leader P/S | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值 / Analyst TP upgrade decomposition | 賣方摘要 WebSearch（90d＋同季） | ✗ NOT DISCLOSED（無同季合格上修） |
| valuation.sp500_trend | 估值 / S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值 / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值 / AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✗ NOT DISCLOSED（14 日內無合格報導） |
| breadth.rsp_spy | 廣度 / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度 / Top-10 concentration in S&P 500 | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度 / Advance/decline ratio, new high/low ratio | 市場資料 WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶 / CNN Fear & Greed Index | CNN WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶 / Margin Debt: FINRA monthly data | FINRA / GuruFocus WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶 / Retail survey: AAII Investor Sentiment | AAII WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶 / Social sentiment proxies | WSB / X WebSearch（7d） | ✗ NOT DISCLOSED（無顯著討論） |
| retail.household_equity_allocation | 散戶 / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶 / NAAIM Exposure Index | naaim.org WebSearch | ✗ NOT DISCLOSED（無當週值） |
| institutional.bofa_jpm_survey | 機構 / BofA Fund Manager Survey and JPM institutional survey | BofA / JPM WebSearch | ✗ NOT DISCLOSED（無新月度調查） |
| monetary.fed_funds | 貨幣 / Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣 / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣 / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣 / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣 / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣 / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直接取得） | ✓ API |
| monetary.wti | 貨幣 / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣 / CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣 / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣 / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣 / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（repo_stress block） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣 / 美債標售需求（auction tail / bid-to-cover） | TreasuryDirect / Reuters WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣 / Fed funds rate path expectations | CME FedWatch 摘要 WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣 / Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣 / Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣 / PBoC aggregate financing / liquidity operations | PBoC / NBS WebSearch | ✗ NOT DISCLOSED（無當期英文摘要） |
| monetary.private_credit_liquidity | 貨幣 / Private-credit / non-bank fund liquidity stress | BDC / interval fund 披露 WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無合格披露） |
| ai.hyperscaler_capex | AI / Hyperscaler capex guidance | 財報摘要 WebSearch（stock-of-state，沿用最近季報） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI / AI token volume growth rate | 供應商披露 WebSearch | ✗ NOT DISCLOSED（結果僅為營收成長，非 token volume） |
| ai.openai_anthropic_revenue | AI / OpenAI / Anthropic annualized revenue | CNBC 等 WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 WebSearch | ✗ NOT DISCLOSED（無合格披露） |
| ai.compute_supply_demand | AI / AI compute supply/demand and overcapacity risk | 產業披露 WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI / Hyperscaler 融資結構（capex vs FCF / 發債） | 財報 / 發債 WebSearch；quarterly_state stock-of-state＋event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI / AI 營收對 capex 缺口（revenue-to-capex gap） | 綜合披露 WebSearch（分母 top-4） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI / GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K / 10-Q WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無變動披露） |
| ai.capital_cycle | AI / 資本週期階段（capital cycle stage） | 產業披露 WebSearch；quarterly_state stock-of-state＋event_scan 30d | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機 / Search for past 7 days: AI rename / SPAC | 新聞 / SEC EDGAR WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機 / IPO market heat | stockanalysis WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機 / Microcap thematic moonshots | Finviz / Benzinga / StockTwits WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機 / Upcoming AI IPOs | Yahoo Finance 等 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機 / Insider selling at AI / market-leadership companies | SEC EDGAR / openinsider WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機 / Cboe equity-only put/call ratio | Cboe 統計 WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構 / US leveraged ETF AUM | ETF.com 等 WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構 / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com WebSearch（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | 結構 / Global leveraged product approvals | KRX / TWSE / JPX / ESMA WebSearch（7d） | ✗ NOT DISCLOSED（7 日內無英文披露） |
| structural.zero_dte | 結構 / 0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構 / Options total volume | OCC WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構 / Cross-asset derivatives / correlation checks | Cboe 等 WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構 / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove block） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構 / Cross-reference only: FINRA margin debt | FINRA / GuruFocus WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構 / AI infrastructure debt financing / vendor-financing loops | 信用市場 WebSearch（30d） | ✗ NOT DISCLOSED（30 日內無新披露） |
| structural.nbfi_bank_loans | 結構 / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構 / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）；WebSearch 無額外平倉事件 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | trailing P/E 約 26.2、Shiller CAPE 約 41.2 | Shiller CAPE S&P 500 P/E August 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus；原定 multpl / GuruFocus） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| valuation.mag7_multiples | Magnificent 7 加權 P/E 約 29.5x（S&P 500 約 25.6x） | Magnificent 7 weighted P/E August 2026 | https://www.fool.com/investing/2026/08/14/the-best-magnificent-seven-stocks-to-buy-in-august/（Motley Fool） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| breadth.rsp_spy | RSP 領先 SPY YTD 約 5pp | RSP vs SPY YTD 2026 breadth | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 top-10 集中度約 36.5% | S&P 500 top 10 concentration 2026 | https://www.ebc.com/forex/rsp-vs-spy（EBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| breadth.advance_decline | 領導由 top-100 向 bottom-400 擴散、廣度確認多頭 | market breadth advance decline August 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/（24/7 Wall St.） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 55（Greed） | CNN Fear and Greed today August 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料）約 1,417,225（百萬美元）、YoY 約 +38.6%、MoM −5.7% | FINRA margin debt July 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt（GuruFocus；原定 FINRA） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |
| retail.aaii | AAII 偏多 35.5%、偏空 39.9%（週結 2026-08-19） | AAII investor sentiment August 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| monetary.treasury_auctions | 30Y 標售無明顯 tail、12.10% allotted at high | US Treasury 30-year auction August 2026 | https://www.treasurydirect.gov/instit/annceresult/press/preanre/2026/R_20260813_3.pdf（TreasuryDirect） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| monetary.fedwatch | FedWatch 9/16 按兵不動約 68.4%、尾端為升息 | CME FedWatch September 2026 hold probability | https://en.macromicro.me/series/1645/probability-fed-rate-decrease（MacroMicro；原定 CME FedWatch） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_capex | top-4 2026 capex 合計約 $725bn（+77% YoY），沿用最近一輪季報 | hyperscaler 2026 capex guidance Microsoft Google Amazon Meta | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.openai_anthropic_revenue | OpenAI 年化營收約 $40B、Anthropic 約 $65B | OpenAI Anthropic annualized revenue August 2026 | https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html（CNBC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.compute_supply_demand | GPU 現貨租金高於合約價 2 倍以上、產能被利用率吸收 | AI GPU rental pricing utilization August 2026 | https://www.uncoveralpha.com/p/amazon-google-microsoft-meta-q2-earnings（UncoverAlpha） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex > FCF、2026 hyperscaler 發債擴張（capex 由現金流轉向舉債） | hyperscaler external financing capex FCF debt 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow（FactSet） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $105bn（OpenAI 40＋Anthropic 65）vs 年化 capex 約 $725bn（分母：top-4） | AI revenue to capex gap 2026 | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| ai.capital_cycle | [quarterly_state] 供給側 capex 年增約 77%、需求側 token／營收成長並存 | AI capex growth rate supply demand 2026 | https://valueaddvc.com/ai-spending（ValueAdd VC） | 2026-08-13 | 2026-08-24T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描：0 件合格事件 | AI rename SPAC ticker change August 2026 | Renaissance Capital / SEC EDGAR / 新聞掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD IPO 約 232 件（截至 2026-08-21）、無單週無營收 AI IPO 暴衝 | US IPO count August 2026 | https://stockanalysis.com/ipos/2026/（StockAnalysis） | 2026-08-21 | 2026-08-24T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot（≥100% 單日、<$1B、2+ 主題、弱基本面）掃描：0 檔 | microcap 100% single day surge quantum AI August 2026 | Finviz / Benzinga / StockTwits movers 掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 10 月 IPO、估值約 $2T | Anthropic OpenAI IPO 2026 | https://finance.yahoo.com/markets/article/spacex-openai-and-anthropic-here-are-the-most-anticipated-ipos-in-2026-114439441.html（Yahoo Finance） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 14 日內合格 Form 4 集中賣出：0 起 | insider Form 4 AI executives August 2026 | SEC EDGAR / openinsider 掃描 | — | 2026-08-24T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.52（9 日均總量 0.85） | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio（thetrading.tools；原定 Cboe） | 2026-08-19 | 2026-08-24T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美股槓桿 ETF 總 AUM 約 $198bn 新高；TQQQ 31.3、SOXL 17.3（$bn） | leveraged ETF AUM record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing；原定 etf.com） | 2026-08-17 | 2026-08-24T09:30:00+08:00 |
| structural.us_single_stock_etf | 美單一個股槓桿 ETF 30 日新核准／上市掃描：0 件 | single-stock leveraged ETF launch SEC August 2026 | SEC EDGAR / ETF.com new launches 掃描 | — | 2026-08-24T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 8 月佔比創紀錄約 62.4% | 0DTE SPX volume share August 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-14 | 2026-08-24T09:30:00+08:00 |
| structural.options_volume | OCC 2026 YTD 日均 > 71（百萬口，截至 2026-07 月資料） | OCC options volume 2026 | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/historical-volume-statistics（OCC） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 16.01、期限結構 contango（IVTS 約 0.82）、SKEW 偏高 | VIX term structure SKEW August 2026 | https://www.thetrading.tools/vix-term-structure（thetrading.tools；原定 Cboe） | 2026-08-20 | 2026-08-24T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-07 月資料）交叉檢核，YoY +38.6%（主讀數見 retail.margin_debt） | FINRA margin debt equity market cap ratio 2026 | https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt（GuruFocus） | 2026-07-31 | 2026-08-24T09:30:00+08:00 |

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
  "r1_drawdown_pct": 4.41,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

> [DRY RUN] this report was not committed to archive.

# 2026-09-13 AI 泡沫破裂預測報告
報告日期：2026-09-13｜ISO 週次：2026-W37｜預測窗口：2026-09-13 → 2027-03-14｜前次基準：report-2026-09-03（10天前）

## 結論

**結論：no**

三條路徑都沒有已在進行中的觸發：NASDAQ-100 距 52 週高點回撤 4.21%，離 R1 門檻還需再跌約 21.70%（`valuation.ndx_drawdown`）；HY OAS 2.70%、IG OAS 0.80% 仍處緊縮水位，顯示信用市場未替 AI 借款人重定價（`monetary.hy_oas`、`monetary.ig_oas`）。9/16 FOMC 升息預期（`monetary.fedwatch`）與長端利率上行是本次最強的 yes 催化劑，但尚不足以推翻 182 天窗口內 R1–R3 皆不成立的基準情境。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,368.44（2026-09-11），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 4.21%；R1 門檻水位 22,995.45，自最新收盤須再下跌約 21.70% 才會觸及（`valuation.ndx_drawdown`）。指數自 6 月高點後在 29,000–30,000 區間整理，最近一週在 29,103.51 至 29,544.16 之間震盪，未見加速下行。

脆弱度面：Shiller CAPE 約 40.73（`valuation.sp500_pe_cape`），S&P 500 前十大集中度約 38%（`breadth.top10_concentration`），估值與集中度都處歷史極端區，一旦出現催化劑，下行幅度可能放大。催化劑面：CME FedWatch 顯示 9/16 FOMC 升息 25bp 的機率約 85.5%（`monetary.fedwatch`），10Y 殖利率 4.95%、較前次基準上升 18bps，其中 10Y 實質殖利率上升 13bps（`monetary.dgs10`、`monetary.dfii10`）；ΔT10YIE 為 1bps，但三腿視窗不一致，driver 判讀為 不可判（視窗不一致）（`monetary.t10yie`）。VIX 由 14.32 升至 17.84（FRED VIXCLS，見數據附錄），MOVE 由 74.68 升至 82.21（`structural.treasury_basis_trade`），波動率已開始抬升。反向面：CNN Fear & Greed 約 35（恐懼）、AAII 看多約 38.0%（`retail.fear_greed`、`retail.aaii`），情緒並非亢奮，成分股在 200 日均線之上約 53%（`breadth.advance_decline`），尚未出現廣度崩壞。

S&P 500 價格趨勢偏離：本週趨勢偏離不可用——無日序資料。

**判讀：** R1 距門檻仍遠（需再跌約 21.70%）。若要在窗口內成立，需要升息循環重啟、長端利率持續上行與 AI 獲利預期下修同時發生，形成 2022 年式的估值壓縮；目前利率端的催化劑已出現，但股價與信用市場尚未確認。

### R2 資本支出收縮

最新證據（2026-07-28，Q2 財報季後）顯示 Microsoft、Alphabet、Amazon、Meta 四家 2026 年 capex 合計約 $725bn（`ai.hyperscaler_capex`）。本次取得的證據只有四家合計數，沒有逐家拆分。Microsoft、Alphabet、Amazon、Meta 各自的最新官方指引數字，以及與前一次指引相比的方向（上修／持平／下修），本次證據都沒有逐家披露，因此不自行推估。截至本次，沒有任何一家下修 capex 指引的證據，已下修家數為 0 家（四家中）。四家具體財報日期不在本次證據內；依季報節奏，窗口內（至 2027-03-14）應有 2026 Q3 與 Q4 兩輪財報與法說會，都是 R2 的潛在觸發點。

需求側：Anthropic 年化 run-rate 約 $65bn（`ai.openai_anthropic_revenue`，2026-08-17）。AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收約 $105bn vs 年化 capex 約 $725bn（分母：top-4，未含 Oracle），終端營收約為 capex 的 14%（`ai.revenue_capex_gap`）；本次組件無新披露可比較前值，缺口方向不判定。供需面：H100 中位租金約 $3.38/hr（`ai.compute_supply_demand`，2026-08-31），單一價格點不足以判讀利用率是否轉弱。

**判讀：** R2 尚無任何一家下修；要在窗口內成立，需要兩家在 2026 Q3 或 Q4 財報中下修指引，而這通常出現在 R1 式股價重挫或融資條件急遽收緊之後。營收對 capex 的巨大缺口是中期壓力，但目前沒有證據顯示任何一家已轉向收縮。

### R3 AI 信用事件

本次 AI 信用定價分歧（equity-vs-credit schism）掃描在 14 日窗口內沒有合格披露，因此缺少 Oracle、CoreWeave 等 AI 借款人的個別債券利差、CDS 或評等動作的當期數據。AI infrastructure debt financing / vendor-financing loops 掃描在 30 日窗口內找到一筆：Qualcomm 對 Amazon 發行約 $4bn 的認股權證，屬 data-center 基礎設施合作（`structural.ai_infrastructure_debt`，2026-09-08）。這是供應商以股權工具綁定大型買家的循環式安排，不是 R3 定義的債務違約事件。整體信用環境：HY OAS 2.70%（較前次 +5bps）、IG OAS 0.80%（`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 −3bps，SRF 動用（Standing Repo Facility usage）為 0（`monetary.repo_stress_srf`）；銀行對 NBFI 放款 $2.03T，無新觀測（`structural.nbfi_bank_loans`）。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）本次無合格披露。

本次證據未出現任何 AI 資料中心／算力主業、負債 ≥ 50 億美元借款人的付款違約、寬限期、covenant waiver、distressed exchange 或 going-concern 字樣。

**判讀：** R3 目前沒有可見的 distress 訊號，且整體信用利差緊縮。要在窗口內成立，需要某家高槓桿 neocloud 在再融資時遭遇市場關門；升息與 10Y 上行會提高再融資成本，但從信用重定價到違約通常超過 182 天。個別借款人的信用定價本次缺資料，是 R3 判讀最大的盲點。

## 支持 yes 的證據

- [整體] CME FedWatch 顯示 9/16 FOMC 升息 25bp 機率約 85.5%（2026-09-12），在 CAPE 約 40.73 的估值下重啟緊縮，是窗口內最直接的估值壓縮催化劑（`monetary.fedwatch`、`valuation.sp500_pe_cape`）。
- [R1] 10Y 殖利率 4.95%（2026-09-10），較 2026-09-03 上升 18bps，實質殖利率上升 13bps 至 2.55%；WTI 97.26（+5.09%）與 CPI YoY 3.35%（2026-08 月資料）限制 Fed 在 AI 主導回檔時托底的空間（`monetary.dgs10`、`monetary.dfii10`、`monetary.wti`、`monetary.cpi_yoy`）。
- [R1] 波動率同步抬升：MOVE 由 74.68 升至 82.21（2026-09-11），VIX 收在約 17 以上且 call skew 位於第 91 百分位（2026-09-10），顯示避險與上檔選擇權需求同時被推高（`structural.treasury_basis_trade`、`structural.cross_asset_derivatives`）。
- [R2] AI 營收對 capex 缺口：年化 AI 終端營收約 $105bn vs top-4 年化 capex 約 $725bn（2026-08-17／2026-07-28），回本壓力為中期下修指引埋下伏筆（`ai.revenue_capex_gap`、`ai.hyperscaler_capex`）。
- [整體] 集中度與投機結構：前十大佔 S&P 500 約 38%（2026-09-01），SPX 0DTE 佔比創紀錄約 62%（2026-08），本週 IPO 定價約 22 檔（2026-09-11），一旦反轉，傳導可能加速（`breadth.top10_concentration`、`structural.zero_dte`、`speculation.ipo_heat`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.21%（2026-09-11），距 R1 門檻 22,995.45 仍需再跌約 21.70%；基準情境下任一 182 天窗口出現 25% 回撤並不常見（`valuation.ndx_drawdown`）。
- [R3] 信用市場未重定價：HY OAS 2.70%、IG OAS 0.80%（2026-09-10），repo 資金壓力（SOFR−IORB）−3bps 且 SRF 動用為 0（2026-09-10／2026-09-11），沒有 AI 借款人違約前常見的資金面緊張（`monetary.hy_oas`、`monetary.ig_oas`、`monetary.repo_stress_srf`）。
- [R2] 四大 hyperscaler 2026 年 capex 合計約 $725bn（2026-07-28），本次沒有任何一家下修指引的證據；R2 需兩家下修，目前為 0 家（`ai.hyperscaler_capex`）。
- [整體] 情緒並非亢奮：CNN Fear & Greed 約 35（2026-09-10）、AAII 看多約 38.0%（2026-09-10）；Mag 7 前瞻本益比低於 24（2026-08-03），估值已部分消化，降低急殺所需的「最後一棒」條件（`retail.fear_greed`、`retail.aaii`、`valuation.mag7_multiples`）。
- [整體] 槓桿資金正在退場而非加碼：單一個股槓桿 ETF 規模約 $40.74bn（2026-09-08），Cboe equity put/call 約 0.67（2026-09-01），高於 0.50 的 call-heavy 警戒區（`structural.leveraged_etf_aum`、`speculation.equity_put_call`）。

## 與前期比較

前次結論：無前次預測（report-2026-09-03 為舊格式評分報告）

flip_evidence 為空：前次為舊格式評分報告，不轉譯為 yes/no。與 2026-09-03 相比的主要變化：

- 10Y 殖利率 +18bps、實質殖利率 +13bps；ΔT10YIE +1bps，視窗不一致，driver 不可判。
- VIX 由 14.32 升至 17.84、MOVE 由 74.68 升至 82.21，波動率明顯抬升。
- WTI 由 92.55 升至 97.26（+5.09%）。
- HY OAS +5bps 至 2.70%、IG OAS −1bps 至 0.80%，信用利差大致持平。
- NASDAQ-100 由 29,482.32（2026-09-03）變為 29,368.44（2026-09-11），回撤維持在 4.21%。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `valuation.sp500_trend`：腳本 `sp500_trend` 區塊 fetch_failed，本次證據也沒有可用的 S&P 500 現價搜尋結果。本週趨勢偏離不可用——無日序資料。這是衡量價格延伸程度的輔助指標，與 R1 解析（NASDAQ-100）無直接關係，不會改變本次答案。
- `structural.vix_spx_comove`：VIXCLS 已取得（17.84，2026-09-10），但因 `sp500_trend` 失敗，共變區塊為 unavailable，沒有 crowded-optionality 判讀。VIX 上升已由 VIXCLS 與跨資產衍生品證據反映，缺的只是確認層，不會改變答案。

其他：證據摘要把美債基差交易槓桿標為「腳本三區塊 fetch_failed」，但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 都是 `status: ok`，本報告以 artifact 為準，記為 ✓ API。

最大的不確定性：

1. 9/16 FOMC 結果與後續升息路徑：若確認升息且點陣圖偏鷹，長端殖利率進一步上行會壓縮高估值科技股，推向 yes（R1）；若按兵不動或釋出鴿派訊號，維持 no。
2. 個別 hyperscaler 的 capex 指引方向與 2026 Q3 財報日期：本次只取得四家合計數。若 Q3 財報出現任何一家下修，R2 距離會明顯縮短，推向 yes。
3. AI 借款人個別信用定價缺資料：AI 信用定價分歧本次無合格披露，若 neocloud 債券或 CDS 已在走闊而本報告未捕捉，R3 風險會被低估，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.ndx_drawdown | ndx_drawdown latest（NASDAQ-100 最新收盤） | 29368.44 | FRED API (series_id=NASDAQ100)，ndx_drawdown | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100)，ndx_drawdown | 2026-06-02 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.21 | FRED API (series_id=NASDAQ100)，ndx_drawdown | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100)，ndx_drawdown | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q2 家庭股票配置 %） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.7 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 5.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.8 | FRED API (series_id=BAMLC0A0CM) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.95 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | 18.0 | FRED API (series_id=DGS10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.55 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | 13.0 | FRED API (series_id=DFII10) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.36 | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | 1.0 | FRED API (series_id=T10YIE) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl） | 97.26 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.wti | DCOILWTICO chg_pct | 5.09 | FRED API (series_id=DCOILWTICO) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-08 月資料） | 3.35 | FRED API (series_id=CPIAUCSL) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.32 | FRED API (series_id=T5YIFR) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright，%） | 0.8892 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 日） | 1.4 | FRED API (series_id=THREEFYTP10) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API (series_id=SOFR99) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-09-13 | 2026-09-13T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6740619.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5912178.0（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-09-04 | 2026-09-13T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6446620.0（¥644.66T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-08-01 | 2026-09-13T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest（共變區塊 unavailable） | 17.84 | FRED API (series_id=VIXCLS) | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2027.9777（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -6863118 | CFTC TFF futures-only，cftc_lev_funds | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 387809 | CFTC TFF futures-only，cftc_lev_funds | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 82.21 | Yahoo Finance chart API (^MOVE)，move_index | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index prior | 74.68 | Yahoo Finance chart API (^MOVE)，move_index | 2026-09-03 | 2026-09-13T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2271.6 | OFR STFM (REPO-TRIV1_TV_TOT-P)，ofr_repo | 2026-09-11 | 2026-09-13T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（multpl / GuruFocus） | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90 日且同季） | ✗ NOT DISCLOSED（窗口內無合格 TP 上調） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend；WebSearch 現價 | ⛔ FETCH FAILED（sp500_trend fetch_failed，無 S&P 500 現價搜尋結果） |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch（14 日） | ✗ NOT DISCLOSED（窗口內無合格披露） |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch | ✓ SEARCH-VERIFIED（以 200 日均線上方比例為廣度 proxy） |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7 日） | ✗ NOT DISCLOSED（無顯著討論） |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED（無當週數值） |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✗ NOT DISCLOSED（無新一期調查） |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED DFEDTARU / DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED CPIAUCSL | scripts/fetch_macro.py（yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED THREEFYTP10 | scripts/fetch_macro.py（Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED SOFR / SOFR99 / IORB / RPONTTLD | scripts/fetch_macro.py repo_stress | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch（14 日） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations: CME FedWatch | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED WALCL | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok，無新觀測） |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing / liquidity operations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30 日） | ✗ NOT DISCLOSED（窗口內無合格披露） |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state，沿用 Q2 財報） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED（本季無披露） |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | WebSearch | ✗ NOT DISCLOSED（無合格披露） |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch；quarterly_state 沿用 Q2 季資料，event_scan 30 日掃描完成無新事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch＋既有 bullets 組合（分母 top-4） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30 日） | ✗ NOT DISCLOSED（窗口內無變動） |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch；quarterly_state 與 event_scan 皆完成但無合格披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch（7 日） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（Finviz / Benzinga / StockTitan / Yahoo） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30 日） | ✗ NOT DISCLOSED（無 S-1 或具名來源報導） |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR / WebSearch（14 日） | ✓ SEARCH-VERIFIED |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch（etf.com / ETF Action） | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com 新上市 feed（30 日） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7 日，KRX / TWSE / JPX / ESMA） | ✗ NOT DISCLOSED（無英文披露） |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove） | ⛔ FETCH FAILED（VIXCLS ok；vix_spx_comove unavailable，因 sp500_trend fetch_failed） |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30 日） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo） | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.73（原定來源 multpl / GuruFocus） | S&P 500 Shiller CAPE ratio current September 2026 multpl | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | Magnificent 7 forward P/E valuation September 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html（CNBC） | 2026-08-03 | 2026-09-13T09:30:00+08:00 |
| breadth.rsp_spy | RSP 至 7 月止 YTD 報酬約 13% | RSP equal weight vs SPY S&P 500 YTD performance September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度約 38% | S&P 500 top 10 concentration percentage September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/（24/7 Wall St.） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 200 日均線之上約 53% | market breadth advance decline new highs lows September 2026 percent stocks above 200-day | https://condoredge.com/stocks/market-breadth（Condor Edge） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 35（恐懼） | CNN Fear and Greed Index today September 2026 reading | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| retail.margin_debt | margin debt 約 $1.42T（2026-07 月資料） | FINRA margin debt August 2026 record year over year | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026（Advisor Perspectives，原定 FINRA） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.0% | AAII sentiment survey results week September 10 2026 bullish bearish neutral | https://www.aaii.com/sentimentsurvey（AAII） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.71 | Treasury auction results September 2026 tail bid-to-cover 10-year | https://thevaultreport.com/treasury-auctions（The Vault Report） | 2026-09-09 | 2026-09-13T09:30:00+08:00 |
| monetary.fedwatch | 9/16 FOMC 升息 25bp 機率約 85.5% | CME FedWatch September 12 2026 probability 25 basis point hike | https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html（Yahoo Finance，原定 CME FedWatch） | 2026-09-12 | 2026-09-13T09:30:00+08:00 |
| monetary.pboc | 2026 年 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate financing 2026 total social financing | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm（SteelOrbis） | 2026-08-15 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 $725bn（Q2 財報季） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 $65bn | OpenAI Anthropic annualized revenue run rate September 2026 | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| ai.compute_supply_demand | H100 中位租金約 $3.38/hr | GPU rental price HBM DRAM contract price September 2026 utilization | https://www.thundercompute.com/blog/ai-gpu-rental-market-trends（Thunder Compute） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 增額債務佔 capex 約 32%（Q2 財報季） | hyperscaler capex vs free cash flow debt issuance 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-09-13T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $105bn（分母沿用 ai.hyperscaler_capex top-4 合計） | AI revenue vs capex gap 2026 annualized run rate | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai（Axios） | 2026-08-17 | 2026-09-13T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement September 7-13 2026 | 檢查來源：SPACInsider、Businesswire SPAC newsroom、Boardroom Alpha（窗內無合格事件） | — | 2026-09-13T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 22 檔 | IPO priced week September 8 2026 first day return debut | https://www.iposcoop.com/current-year-pricings/（IPOScoop） | 2026-09-11 | 2026-09-13T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（0 件符合 2+ 主題×弱基本面） | biggest stock gainers week September 7 2026 microcap 100% quantum AI | 檢查來源：Finviz、Benzinga、StockTitan、Yahoo movers（Tenon +77%、AEON +35% 皆未達門檻） | — | 2026-09-13T09:30:00+08:00 |
| speculation.insider_form4 | NVDA（CIK 0001045810）董事 Stevens Form 4 賣出約 $385M（證據僅列單一日期） | insider selling Form 4 September 2026 Nvidia AI executives SEC filing | https://www.sec.gov/Archives/edgar/data/0001045810/000119903926000012/wk-form4_1788387031.xml（SEC EDGAR） | 2026-09-02 | 2026-09-13T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 約 0.67（日讀數／5 日均值未標明） | Cboe equity put call ratio September 2026 reading | https://www.thetrading.tools/put-call-ratio（原定 Cboe） | 2026-09-01 | 2026-09-13T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 $40.74bn | leveraged ETF assets under management September 2026 record single stock | https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/（ETF Action，原定 etf.com） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval September 2026 | 檢查來源：SEC EDGAR、ETF.com 新上市 feed（窗內無合格核准或上市） | — | 2026-09-13T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比創紀錄約 62%（2026-08 月資料） | 0DTE options share SPX volume September 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august（Cboe） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.options_volume | OCC 8 月總結算量約 1.44 十億口（2026-08 月資料） | OCC options volume August 2026 monthly report | https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/（Traders Magazine） | 2026-08-31 | 2026-09-13T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 收在約 17 以上、call skew 第 91 百分位 | fear gauge VIX hedges September 10 2026 volatility | https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html（CNBC） | 2026-09-10 | 2026-09-13T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 $1.42T（2026-07 月資料） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php（Current Market Valuation） | 2026-07-31 | 2026-09-13T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Qualcomm 對 Amazon 認股權證約 $4bn（data-center 基礎設施合作） | Qualcomm warrants Amazon 4 billion AI infrastructure deal September 2026 | https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html（CNBC） | 2026-09-08 | 2026-09-13T09:30:00+08:00 |

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

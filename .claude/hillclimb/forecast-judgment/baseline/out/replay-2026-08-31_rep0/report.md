> [DRY RUN] this report was not committed to archive.

# 2026-08-31 AI 泡沫破裂預測報告

報告日期：2026-08-31｜ISO 週次：2026-W36｜預測窗口：2026-08-31 → 2027-03-01｜前次基準：report-2026-08-27（4天前）

## 結論

**結論：no**

三條路徑都看不到已啟動的破裂過程：NASDAQ-100 距 52 週高點回撤 4.00%，離 R1 門檻還差約 21.87% 的跌幅；HY OAS 2.63%、IG OAS 0.79% 仍處緊縮水位，repo 資金壓力（SOFR−IORB）為 −1bp，信用端沒有 R3 前兆。估值與槓桿雖然偏高（CAPE 41.59、槓桿 ETF AUM ≈$198B），但這些只說明泡沫存在、一旦破裂跌幅會大，不足以證明 182 天內會破裂，因此判斷維持在基準率一側。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,433.43（2026-08-28），252 個交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 4.00%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45；從最新收盤再跌約 21.87% 才會觸發。旁證：S&P 500 收 7,711.76（2026-08-28），高於 200 日均線 8.33%、高於 52 週均線 9.76%（`valuation.sp500_trend`），代表價格延伸幅度大、回落的空間也大；但 VIX 14.51（2026-08-27），7 日窗口（2026-08-20 → 2026-08-27）內 S&P 500 +1.18%、VIX −9.37%，沒有出現股價與波動率同步上升的 crowded-optionality 讀數（`structural.vix_spx_comove`）。MOVE 70.97（2026-08-28，較 2026-08-27 +1.11），債市波動同樣平靜（`structural.treasury_basis_trade`）。

**判讀：** 距 R1 很遠。要在窗口內觸發，需要一場跌幅超過 2022 年級的修正（再跌約 22%），通常得有信用重定價、資本支出指引轉向或流動性衝擊作觸發；目前這些觸發條件都沒有出現。可能的推力是 10 月下旬與 2027 年 1 月下旬至 2 月初兩個財報季的 capex／營收落差，以及高 CAPE 下對利率的敏感度。

### R2 資本支出收縮

本次可取得的最新正式資料為 2026-07-28 的彙整報導：四大 hyperscaler（Microsoft、Alphabet、Amazon、Meta）2026 年 capex 合計 725（十億美元），報導重點是市場在 Alphabet 財報後對 capex 的審視升溫（`ai.hyperscaler_capex`，沿用 2026 年第二季財報的指引，stock-of-state）。本次證據沒有提供個別公司的指引數字，因此無法逐家判定與前一次正式指引相比是上修、持平或下修；資料中沒有任何一家下修指引的報導，**目前確認下修的家數為 0／4**。窗口內預期有兩個財報季（2026 年 10 月下旬與 2027 年 1 月下旬至 2 月初），後者通常公布次年度指引；本次證據沒有具體財報日期。

**判讀：** 尚未啟動。要解析為 yes，需要其中兩家在上述兩個財報季下修指引；目前的訊號（市場對 capex 的審視升溫）是壓力，但距離實際下修還有一段距離。若 R1 先發生大幅回撤，或 AI 營收落差被證實，R2 觸發的可能性會明顯上升（路徑互動）。

### R3 AI 信用事件

符合規模門檻的代表性借款人是 CoreWeave：2026-08-10 完成 DDTL 5.5 共 26 億美元的 GPU 抵押貸款（`structural.ai_infrastructure_debt`），顯示 AI infrastructure debt financing / vendor-financing loops 仍在擴張，而且債務市場還願意以 GPU 作抵押放款；本次證據沒有提供其總負債、債券殖利率、CDS 或評等行動數字。寬基信用端：HY OAS 2.63%、IG OAS 0.79%（2026-08-27，`monetary.hy_oas`、`monetary.ig_oas`），處於緊縮水位；repo 資金壓力（SOFR−IORB）−1bp、SOFR99−IORB 7bp（2026-08-27），SRF 動用（Standing Repo Facility usage）0.001（十億美元，2026-08-28）（`monetary.repo_stress_srf`）。資料中沒有付款違約、covenant waiver、distressed exchange 或 going-concern 字樣的報導。

**判讀：** 沒有任何困境訊號。新融資能順利完成，代表短期再融資窗口仍開著；R3 需要在窗口內出現實際違約或 distressed exchange，這通常要先看到 AI 發行人利差明顯走闊或融資失敗。本次 AI 信用定價分歧（equity-vs-credit schism）掃描沒有窗內資料，是主要盲點。

## 支持 yes 的證據

- [整體] 估值處於歷史極端：Shiller CAPE 41.59（2026-08-01），S&P 500 高於 200 日均線 8.33%（2026-08-28），一旦觸發修正，下跌空間大（`valuation.sp500_pe_cape`、`valuation.sp500_trend`）。
- [R1] 槓桿與投機部位擁擠：美國槓桿 ETF 總 AUM ≈$198B 創新高、TQQQ 37.3、SOXL 22（2026-08-28），SPX 0DTE 佔期權量 ≈60%（2026-08-28），margin debt 1.42 兆美元、YoY 38.6%（2026-07 月資料），接近歷史頂部 +40% 區域；下跌時可能出現強制去槓桿放大跌幅（`structural.leveraged_etf_aum`、`structural.zero_dte`、`retail.margin_debt`）。
- [R1] 尾部避險需求與股債相關性轉變：Cboe SKEW 143.9、股債相關轉正（2026-08-24），代表債券對股市的避險效果下降（`structural.cross_asset_derivatives`）。
- [R3] AI 基建債務持續累積：CoreWeave 2026-08-10 完成 26 億美元 GPU 抵押 DDTL 5.5，以 GPU 殘值作抵押的債務堆疊，是 R3 的結構性脆弱點（`structural.ai_infrastructure_debt`）。
- [R2] 市場對 capex 的審視升溫：2026-07-28 報導指 Alphabet 財報後 hyperscaler 面臨更高的 capex 審視，四家 2026 年 capex 合計 725（十億美元）（`ai.hyperscaler_capex`）。
- [整體] 通膨限制 Fed 的緩衝空間：CPI YoY 3.3%（2026-07 月資料），10Y 期限溢價（term premium）0.8682%（2026-08-21，trailing 7 日 +2.9bp），10Y 殖利率 4.67%（`monetary.cpi_yoy`、`monetary.term_premium`、`monetary.dgs10`）。
- [R1] 市場廣度轉弱：成分股在 50 日均線之上的比率 54%（2026-08-28，StockCharts 文章標題指廣度轉弱）（`breadth.advance_decline`）。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 4.00%（2026-08-28），離 R1 門檻 22,995.45 還差約 21.87% 的跌幅；以 182 天窗口的基準率來看，這是距離最遠的路徑之一（`valuation.ndx_drawdown`）。
- [R3] 信用端沒有重定價：HY OAS 2.63%、IG OAS 0.79%（2026-08-27），與前次持平，信用市場沒有預告違約潮（`monetary.hy_oas`、`monetary.ig_oas`）。
- [整體] 融資與流動性管道平靜：SOFR−IORB −1bp、SOFR99−IORB 7bp（2026-08-27），SRF 動用 0.001（十億美元，2026-08-28），MOVE 70.97（2026-08-28），OFR tri-party repo transaction volume 2,355.4（十億美元，2026-08-28）；沒有國債市場失序（Treasury market dysfunction）前兆（`monetary.repo_stress_srf`、`structural.treasury_basis_trade`）。
- [R2] 沒有任何 hyperscaler 下修 capex 指引的證據：最新彙整仍是四家 2026 年合計 725（十億美元）（2026-07-28），確認下修家數 0／4（`ai.hyperscaler_capex`）。
- [整體] 情緒不在狂熱區：CNN Fear & Greed 54（中性，2026-08-28），AAII 看多 32.9%、看空 44.4%（2026-08-26），VIX 14.51 且沒有股價與波動率同步上升（`retail.fear_greed`、`retail.aaii`、`structural.vix_spx_comove`）。
- [R1] 漲勢擴散而非過度集中：equal-weight 對 cap-weight YTD 為 9.67 對 8.38（2026-08-28），前十大集中度 37.6%（2026-07-31）（`breadth.rsp_spy`、`breadth.top10_concentration`）。
- [整體] 投機性狂熱事件篩選為 0：近 7 日 +AI 改名／SPAC 0 件、microcap moonshot 0 件，近 14 日 AI 領導股 Form 4 集中賣出 0 件（`speculation.ai_rename_spac`、`speculation.microcap_moonshots`、`speculation.insider_form4`）。

## 與前期比較

前次結論：無前次預測（report-2026-08-27 為舊格式評分報告）

本次為新格式首次預測，`flip_evidence` 為空陣列。自 2026-08-27 以來的主要數據變化：

- S&P 500 由 7,730.99 降至 7,711.76（−0.25%），NASDAQ-100 由 29,641.56 降至 29,433.43，回撤幅度變化有限（`valuation.sp500_trend`、`valuation.ndx_drawdown`）。
- 10Y breakeven −2bp 至 2.31%、5y5y forward −3bp 至 2.32%（2026-08-28）；DGS10、DFII10、HY／IG OAS 沒有新觀測（`monetary.t10yie`、`monetary.t5yifr`）。
- SRF 動用由 0.101 降至 0.001（十億美元），MOVE +1.11 至 70.97，資金面沒有惡化（`monetary.repo_stress_srf`、`structural.treasury_basis_trade`）。
- 美債期貨槓桿基金淨空單 4 週縮減 478,000 口（至 −7,003,041 口，2026-08-25），美債基差交易槓桿（Treasury basis-trade leverage）小幅去化（`structural.treasury_basis_trade`）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源掃描完成但無窗內披露（✗ NOT DISCLOSED，皆為非必要來源）：analyst TP decomposition、AI 信用定價分歧（equity-vs-credit schism）、social sentiment、NAAIM、BofA／JPM survey、美債標售需求（auction tail / bid-to-cover）、PBoC、私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）、token growth、OpenAI／Anthropic 營收、backlog 重複計算風險（RPO double-counting）、AI compute supply/demand、hyperscaler 融資結構（capex vs FCF / 發債）、AI 營收對 capex 缺口（revenue-to-capex gap）、折舊年限變動（depreciation useful-life change）、資本週期階段（capital cycle stage）、upcoming AI IPOs、global leveraged approvals。其中 AI 信用定價分歧與私募信貸贖回壓力的缺漏最可能影響 R3 判斷：若有 AI 發行人利差走闊或贖回超過 quarterly redemption cap 而被 gate proration / breach，會讓答案往 yes 移動；但寬基 HY／IG OAS 與 repo 指標都平靜，所以目前不認為這些缺口會翻轉結論。另外，搜尋結果紀錄寫明美債基差交易的 script 區塊 fetch_failed，但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 三塊皆為 `status: ok`；本報告以 artifact 為準。

主要不確定性：

1. **2026 年 10 月下旬與 2027 年 1 月下旬至 2 月初的 hyperscaler 財報**：若有兩家下修 capex，R2 直接成立，答案翻為 yes；若持續上修，則支持 no。本次缺個別公司指引方向，是 R2 最大的盲點。
2. **AI 基建債務的再融資與 GPU 抵押品價值**：CoreWeave 等借款人持續加債，若 GPU 租金或殘值下跌導致抵押品不足，可能在窗口後段觸發 R3，並透過信用傳導觸發 R1。
3. **通膨與利率**：CPI 3.3%、10Y 期限溢價上升，若通膨再度上行，Fed 無法在股市修正時提供緩衝，修正可能被放大；這會把答案往 yes 推。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 41.59 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio | 2026-08-01 | 2026-08-31T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權前瞻本益比 | 24 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html | 2026-08-03 | 2026-08-31T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest | 7711.76 | FRED API (series_id=SP500) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 8.33 | FRED API (series_id=SP500) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 9.76 | FRED API (series_id=SP500) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend prior_spot | 7730.99 | FRED API (series_id=SP500) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29433.43 | FRED API (series_id=NASDAQ100) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-31T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 4.0 | FRED API (series_id=NASDAQ100) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| breadth.rsp_spy | equal-weight 對 cap-weight YTD | 9.67 對 8.38 | https://finance.yahoo.com/markets/stocks/articles/rsp-vs-spy-does-equal-185007075.html | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度 % | 37.6 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/ | 2026-07-31 | 2026-08-31T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 50 日均線之上比率 % | 54 | https://articles.stockcharts.com/article/mindfulinvestor-2026-08-weakening-market-breadth-could-signal-trouble-ahead/ | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed | 54（中性） | https://www.cnn.com/markets/fear-and-greed | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-07 月資料），YoY 38.6% | 1.42（兆美元） | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026 | 2026-07-31 | 2026-08-31T09:30:00+08:00 |
| retail.aaii | AAII 看多 %，看空 44.4% | 32.9 | https://www.aaii.com/sentimentsurvey | 2026-08-26 | 2026-08-31T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q1，家庭股票配置 %） | 45.76080873390133（≈45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-31T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-30 | 2026-08-31T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-30 | 2026-08-31T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.63 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.79 | FRED API (series_id=BAMLC0A0CM) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.67 | FRED API (series_id=DGS10) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（無新觀測） | 0.0 | FRED API (series_id=DGS10) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.34 | FRED API (series_id=DFII10) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.31 | FRED API (series_id=T10YIE) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | -2.0 | FRED API (series_id=T10YIE) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 83.9 | FRED API (series_id=DCOILWTICO) | 2026-08-25 | 2026-08-31T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-07 月資料） | 3.3 | FRED API (series_id=CPIAUCSL) | 2026-07-01 | 2026-08-31T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.32 | FRED API (series_id=T5YIFR) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR delta_bps | -3.0 | FRED API (series_id=T5YIFR) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.8682 | FRED API (series_id=THREEFYTP10) | 2026-08-21 | 2026-08-31T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 日） | 2.9 | FRED API (series_id=THREEFYTP10) | 2026-08-21 | 2026-08-31T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.64 | FRED API (series_id=SOFR) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.72 | FRED API (series_id=SOFR99) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED API (series_id=IORB) | 2026-08-31 | 2026-08-31T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用 read，十億美元） | 0.001 | FRED API (series_id=RPONTTLD) | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR−IORB（repo_stress sofr_iorb_bps，IORB 取 2026-08-27） | -1.0 | fetch_macro.py repo_stress（FRED） | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| monetary.fedwatch | FedWatch 9 月 FOMC 維持利率隱含機率 % | 58.6 | https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html | 2026-08-25 | 2026-08-31T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6730912.0（$6.73T，百萬美元） | FRED API (series_id=WALCL) | 2026-08-26 | 2026-08-31T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5913041.0（€5.91T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-08-21 | 2026-08-31T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-31T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計（2026 年第二季財報） | 725（十億美元） | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-07-28 | 2026-08-31T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價件數（BRVE 首週漲 67%） | ≈39 | https://seekingalpha.com/article/4933637-august-kicks-off-with-flurry-of-biotech-ipos | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call（日讀數；9 日均 0.85） | 0.52 | https://www.thetrading.tools/put-call-ratio | 2026-08-19 | 2026-08-31T09:30:00+08:00 |
| structural.leveraged_etf_aum | 槓桿 ETF 總 AUM（十億美元；TQQQ 37.3、SOXL 22） | 198 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔期權量 % | ≈60 | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/ | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| structural.options_volume | OCC 2026-07 月報 ETF 期權 YoY %（總日均量 71） | 26 | https://mondovisione.com/media-and-resources/news/occ-july-2026-monthly-volume-data-202686 | 2026-07-31 | 2026-08-31T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW（VIX 期限結構 contango、股債相關轉正） | 143.9 | https://www.thetrading.tools/vix-term-structure | 2026-08-24 | 2026-08-31T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 14.51 | FRED API (series_id=VIXCLS) | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（comove=false） | 14.51 | fetch_macro.py 衍生區塊（FRED） | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（base 2026-08-20） | -9.37 | fetch_macro.py 衍生區塊（FRED） | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（base 2026-08-20） | 1.18 | fetch_macro.py 衍生區塊（FRED） | 2026-08-27 | 2026-08-31T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率 confirmation（2026-07 月資料，兆美元） | 1.42 | https://www.currentmarketvaluation.com/models/margin-debt.php | 2026-07-31 | 2026-08-31T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave DDTL 5.5 融資收官（GPU 抵押，十億美元） | 2.6 | https://investors.coreweave.com/news/news-details/2026/CoreWeave-Closes-2-6-Billion-Loan-Facility-Expanding-Financing-Flexibility-for-AI-Infrastructure/default.aspx | 2026-08-10 | 2026-08-31T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2026.2859（$2.03T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-08-19 | 2026-08-31T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（口） | -7003041 | CFTC TFF（cftc_lev_funds） | 2026-08-25 | 2026-08-31T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | 478000 | CFTC TFF（cftc_lev_funds） | 2026-08-25 | 2026-08-31T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 70.97 | Yahoo Finance chart API ^MOVE（move_index） | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party transaction volume） | 2355.4 | OFR STFM（ofr_repo） | 2026-08-28 | 2026-08-31T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | WebSearch（gurufocus）；僅取得 CAPE | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch（CNBC）；P/S 對 10 年均值未取得 | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✗ NOT DISCLOSED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch（Yahoo Finance） | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch（Pensions & Investments） | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch（StockCharts；以 50 日均線上方比率作廣度 proxy） | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch（cnn.com） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（Advisor Perspectives，2026-07 月資料） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch（aaii.com） | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED | fetch_macro.py（DFEDTARU ok、DFEDTARL ok） | ✓ API |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield | fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED | fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED | fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok；repo_stress status ok） | ✓ API |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch（CME FedWatch） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✗ NOT DISCLOSED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（CNBC，沿用 2026 年第二季財報） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✗ NOT DISCLOSED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✗ NOT DISCLOSED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch（quarterly_state stock_of_state；event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch | ✗ NOT DISCLOSED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch（quarterly_state stock_of_state；event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch（SPACInsider、Boardroom Alpha、Businesswire） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch（Seeking Alpha） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch（Finviz、Benzinga、StockTitan） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✗ NOT DISCLOSED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR / WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe insights） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報摘要） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | fetch_macro.py（VIXCLS ok、vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch（confirmation only） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok；aggregation any） | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 41.59（原定 multpl／gurufocus） | shiller cape ratio august 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio（GuruFocus） | 2026-08-01 | 2026-08-31T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權前瞻本益比 24 | magnificent 7 forward pe august 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html（CNBC） | 2026-08-03 | 2026-08-31T09:30:00+08:00 |
| breadth.rsp_spy | equal-weight 對 cap-weight YTD 9.67 對 8.38 | rsp vs spy ytd 2026 | https://finance.yahoo.com/markets/stocks/articles/rsp-vs-spy-does-equal-185007075.html（Yahoo Finance） | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大集中度 37.6 | sp500 top 10 concentration 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/（Pensions & Investments） | 2026-07-31 | 2026-08-31T09:30:00+08:00 |
| breadth.advance_decline | 成分股在 50 日均線之上比率 54（原定 advance/decline ratio） | market breadth advance decline august 2026 | https://articles.stockcharts.com/article/mindfulinvestor-2026-08-weakening-market-breadth-could-signal-trouble-ahead/（StockCharts） | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 54（中性） | cnn fear greed index august 2026 | https://www.cnn.com/markets/fear-and-greed（CNN） | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt 1.42 兆美元、YoY 38.6（2026-07 月資料） | finra margin debt july 2026 | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026（Advisor Perspectives） | 2026-07-31 | 2026-08-31T09:30:00+08:00 |
| retail.aaii | AAII 看多 32.9、看空 44.4 | aaii sentiment august 2026 | https://www.aaii.com/sentimentsurvey（AAII） | 2026-08-26 | 2026-08-31T09:30:00+08:00 |
| monetary.fedwatch | FedWatch 9 月維持利率 58.6 | cme fedwatch september 2026 | https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html（CME Group） | 2026-08-25 | 2026-08-31T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計 725 | hyperscaler capex 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html（CNBC） | 2026-07-28 | 2026-08-31T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 掃描，0 件符合 7 日窗口 | +AI rename SPAC aug 24-31 2026 | 檢查來源：SPACInsider、Boardroom Alpha、Businesswire | — | 2026-08-31T09:30:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價≈39 件、BRVE 首週漲 67 | ipo market august 2026 | https://seekingalpha.com/article/4933637-august-kicks-off-with-flurry-of-biotech-ipos（Seeking Alpha） | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描，0 件符合 2+ 主題×弱基本面（RFAI 為窗外 SPAC、XHG 為 insurtech，皆不符） | microcap moonshot quantum ai aug 24-31 2026 | 檢查來源：Finviz、Benzinga、StockTitan | — | 2026-08-31T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 集中賣出掃描，0 件（NVDA 僅 Puri 退休申報，不構成集中賣出） | insider form 4 nvidia aug 2026 | 檢查來源：SEC EDGAR（NVDA） | — | 2026-08-31T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.52（日讀數）、9 日均 0.85 | cboe equity put call ratio august 2026 | https://www.thetrading.tools/put-call-ratio（thetrading.tools） | 2026-08-19 | 2026-08-31T09:30:00+08:00 |
| structural.leveraged_etf_aum | TQQQ 37.3、SOXL 22、槓桿 ETF 總 AUM 198 | leveraged etf aum record 2026 | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/（Crypto Briefing） | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市，0 件經查證日期（多為預備註冊） | single stock leveraged etf launch aug 2026 | 檢查來源：SEC EDGAR、ETF.com | — | 2026-08-31T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔期權量≈60 | 0dte spx share 2026 | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/（Cboe） | 2026-08-28 | 2026-08-31T09:30:00+08:00 |
| structural.options_volume | OCC 月報 ETF 期權 YoY 26、總日均量 71（2026-07 月資料） | occ july 2026 options volume | https://mondovisione.com/media-and-resources/news/occ-july-2026-monthly-volume-data-202686（Mondo Visione） | 2026-07-31 | 2026-08-31T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 期限結構 contango、股債相關轉正、SKEW 143.9 | vix term structure skew august 2026 | https://www.thetrading.tools/vix-term-structure（thetrading.tools） | 2026-08-24 | 2026-08-31T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率 confirmation（1.42 兆美元，2026-07 月資料） | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php（Current Market Valuation） | 2026-07-31 | 2026-08-31T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave DDTL 5.5 融資收官 2.6 十億美元（GPU 抵押） | coreweave debt facility august 2026 | https://investors.coreweave.com/news/news-details/2026/CoreWeave-Closes-2-6-Billion-Loan-Facility-Expanding-Financing-Flexibility-for-AI-Infrastructure/default.aspx（CoreWeave IR） | 2026-08-10 | 2026-08-31T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-31",
  "iso_week": "2026-W36",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-03-01",
  "prior_date": "2026-08-27",
  "prior_answer": null,
  "flip_evidence": [],
  "r1_drawdown_pct": 4.0,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

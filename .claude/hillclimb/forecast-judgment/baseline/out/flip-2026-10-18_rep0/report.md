> [DRY RUN] this report was not committed to archive.

# 2026-10-18 AI 泡沫破裂預測報告
報告日期：2026-10-18｜ISO 週次：2026-W42｜預測窗口：2026-10-18 → 2027-04-18｜前次基準：report-2026-09-13（35天前）

## 結論

**結論：yes**

維持前次 yes：自 2026-09-13 以來的新證據沒有削弱、反而強化了 R3→R1 傳導路徑——CoreWeave 5Y CDS 於 2026-10-15 創紀錄的 1,194.5 bps（`valuation.ai_credit_schism`），同時 HY OAS 擴大 58 bps 至 3.23%（`monetary.hy_oas`）、Fed 目標區間再上調 25 bps 至 3.75–4.00%（`monetary.fed_funds`），信用端已開始對 AI 基礎設施重定價而 NASDAQ-100 仍只距高點 4.13%。R1 與 R2 尚無直接觸發跡象，這是 no 方最強的反證，但不足以構成翻轉所需的新反向證據。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,935.59（2026-10-15），252 個交易日最高收盤 31,224.69（2026-10-06，於前次報告之後再創新高），距 52 週高點回撤 4.13%（`valuation.ndx_drawdown`）。R1 門檻水位為 23,418.52，需自最新收盤再下跌約 21.77% 才會觸發。S&P 500 最新 7,659.44（2026-10-16），高於 200 日均線 5.34%、高於 52 週均線 6.78%（`valuation.sp500_trend`），價格仍處延伸區。脆弱度高：Shiller CAPE 約 40.54（`valuation.sp500_pe_cape`）、BofA 10 月 FMS 科技股淨加碼約 37% 為 2020 年 8 月以來最高（`institutional.bofa_jpm_survey`）、前十大集中度約 38.9%（`breadth.top10_concentration`）。近期催化：CNN Fear & Greed 跌至約 18（極度恐懼，2026-10-16，`retail.fear_greed`）、上漲對下跌家數約 29 對 71（2026-10-16，`breadth.advance_decline`）、兩週內第 4 檔 IPO 撤件或延後（2026-10-16，`speculation.ipo_heat`）；VIX/S&P 500 7 日共同觀測（2026-10-08 → 2026-10-15）VIX +6.81%、S&P 500 −0.27%，comove=false（`structural.vix_spx_comove`）。利率端 10Y 5.10%（ΔDGS10 +14 bps）、實質利率 2.78%（ΔDFII10 +18 bps）、ΔT10YIE −1 bps，判讀：不可判（視窗不一致）（`monetary.dgs10`、`monetary.dfii10`、`monetary.t10yie`）。

**判讀：** R1 距觸發仍遠（需再跌約 21.77%），但情緒已由貪婪轉為極度恐懼、廣度轉弱、IPO 窗口收縮；若 R3 端信用壓力外溢或 Anthropic 11 月中上市引發供給衝擊，配合 5.10% 的 10Y 與升息環境，窗口內完成 25% 回撤是可能但尚未啟動的路徑。

### R2 資本支出收縮

本次可得的最新官方 capex 資料為四大 hyperscaler 2026 年 capex 合計約 $725bn（CNBC，2026-07-28，`ai.hyperscaler_capex`，沿用最近一輪季報的 stock-of-state）。本次證據未提供 Microsoft、Alphabet、Amazon、Meta 個別公司的指引數字與相對前次指引方向，因此逐家方向只能記為：Microsoft 未提供可引證的個別指引、Alphabet 未提供可引證的個別指引、Amazon 未提供可引證的個別指引、Meta 未提供可引證的個別指引；本次證據中四家皆無下修紀錄，已下修家數 0／4。下一輪季報的具體日期未見於本次證據，依季度節奏，下一輪及再下一輪季報都應落在預測窗口內。需求側：H100 隨選中位租金約 $4.20/hr（2026-10-07，`ai.compute_supply_demand`），未見崩跌；AI 營收對 capex 缺口（revenue-to-capex gap）：年化 AI 終端營收（僅 Anthropic run-rate 約 $65bn）vs 年化 capex 約 $725bn（分母：top-4，未含 Oracle），缺口仍大（`ai.revenue_capex_gap`、`ai.openai_anthropic_revenue`）。

**判讀：** R2 目前最遠：無任何一家下修。要在窗口內觸發，需要 R1 回撤或信用收緊迫使至少兩家在接下來的季報中下修指引；以目前證據看，這更可能是 R1/R3 發生後的後續結果，而非獨立起點。

### R3 AI 信用事件

具 R3 規模的代表借款人為 CoreWeave：其 5Y CDS 於 2026-10-15 創紀錄的 1,194.5 bps，報導指 AI 信用疑慮推升科技業違約保險至紀錄高位（`valuation.ai_credit_schism`）。這是 AI 信用定價分歧（equity-vs-credit schism）由「信用與非 AI 無差」轉向「信用端先走闊」的後期訊號，而股權端（NASDAQ-100 距高點 4.13%）尚未跟上。AI infrastructure debt financing / vendor-financing loops：30 日內新披露者為 Lambda GPU 擔保融資約 $1bn（2026-10-01，`structural.ai_infrastructure_debt`），融資管道仍開但轉向資產擔保型。總體信用面 HY OAS 3.23%（+58 bps vs 前次，`monetary.hy_oas`），IG OAS 0.84%（+4 bps，`monetary.ig_oas`）。本次證據未見任何付款違約、covenant waiver、distressed exchange 或 going-concern 字句；個別到期牆與評等動作亦未見於本次證據。

**判讀：** R3 是最接近的路徑：CDS 達約 1,195 bps 代表市場已為 CoreWeave 等高槓桿 AI 算力借款人計入顯著違約風險，但尚無實際違約或 distressed exchange。若窗口內出現再融資失敗、客戶合約重議或 distressed exchange，即可直接觸發 R3，並可能經由信用→股權傳導帶動 R1。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 於 2026-10-15 創紀錄的 1,194.5 bps，AI 信用疑慮推升科技業違約保險至紀錄高位；信用端重定價而股權端仍近高點，是典型後期分歧訊號（`valuation.ai_credit_schism`）。
- [整體] 貨幣與信用條件自前次以來明顯收緊：Fed 目標區間 3.75–4.00%（+25 bps，2026-10-17，`monetary.fed_funds`）、10Y 5.10%（2026-10-15，`monetary.dgs10`）、HY OAS 3.23%（+58 bps，`monetary.hy_oas`）、MOVE 101.1（+18.89，2026-10-16，`structural.treasury_basis_trade`），而 CPI YoY 3.72%（2026-09 月資料，`monetary.cpi_yoy`）限制 Fed 緩衝 AI 主導下跌的空間。
- [R1] 情緒與廣度轉折：CNN Fear & Greed 約 18（極度恐懼，2026-10-16，`retail.fear_greed`）、上漲對下跌家數約 29 對 71（2026-10-16，`breadth.advance_decline`）、兩週內第 4 檔 IPO 撤件或延後（2026-10-16，`speculation.ipo_heat`）。
- [R1] 估值與部位擁擠度提供大幅下跌的空間：Shiller CAPE 約 40.54（2026-10-16，`valuation.sp500_pe_cape`）、BofA FMS 科技股淨加碼約 37% 為 2020 年 8 月以來最高（2026-10-13，`institutional.bofa_jpm_survey`）、單一個股槓桿 ETF 規模約 $40.04bn（2026-10-16，`structural.leveraged_etf_aum`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）仍大：年化 AI 終端營收（Anthropic 約 $65bn，2026-08-17）vs 四大 hyperscaler 2026 capex 約 $725bn（分母：top-4）（`ai.revenue_capex_gap`）。
- [R1] Anthropic 目標 11 月中上市（2026-10-05，`speculation.upcoming_ai_ipos`），大型 AI IPO 供給在情緒轉弱時落入窗口，是潛在的定價催化。

## 支持 no 的證據

- [R1] NASDAQ-100 最新收盤 29,935.59（2026-10-15），2026-10-06 才創 52 週新高 31,224.69，距 52 週高點回撤 4.13%，距 R1 門檻 23,418.52 尚需再跌約 21.77%；S&P 500 仍高於 200 日均線 5.34%（`valuation.ndx_drawdown`、`valuation.sp500_trend`）。
- [R2] 四大 hyperscaler 2026 capex 合計約 $725bn（2026-07-28），本次證據中四家無一下修（0／4），R2 尚無起點（`ai.hyperscaler_capex`）；H100 隨選中位租金約 $4.20/hr（2026-10-07）未見算力過剩式崩價（`ai.compute_supply_demand`）。
- [整體] 融資管線未見失序：SOFR−IORB −1 bps、SOFR99−IORB +7 bps（2026-10-15）、SRF 動用 0（2026-10-16）（`monetary.repo_stress_srf`）；10Y 標售 bid-to-cover 約 2.77、需求強勁（2026-10-07，`monetary.treasury_auctions`）；IG OAS 僅 0.84%（`monetary.ig_oas`）。
- [R3] 30 日內 AI 基礎設施融資仍可取得（Lambda GPU 擔保融資約 $1bn，2026-10-01），本次證據未見任何違約、寬限期付款失敗或 distressed exchange（`structural.ai_infrastructure_debt`）。
- [整體] 基準率：任意 182 天窗口內 R1–R3 皆不成立才是常態；VIX 16.46（2026-10-15）、VIX/S&P 500 未同向上升（comove=false，`structural.vix_spx_comove`），尚未出現波動率失控。

## 與前期比較

前次結論：yes（report-2026-09-13）
本次結論：維持

- CoreWeave 5Y CDS 紀錄 1,194.5 bps（2026-10-15）是前次之後的新信用證據，方向支持 yes，強化 R3 路徑而非削弱（`valuation.ai_credit_schism`）。
- 貨幣條件收緊：Fed 目標上限 3.75% → 4.00%、HY OAS 2.65% → 3.23%、MOVE 82.21 → 101.1；方向支持 yes（`monetary.fed_funds`、`monetary.hy_oas`、`structural.treasury_basis_trade`）。
- 情緒由前次的高檔轉為 Fear & Greed 約 18（極度恐懼），IPO 撤件增加；提高 R1 催化風險（`retail.fear_greed`、`speculation.ipo_heat`）。
- 反向變化：NASDAQ-100 於 2026-10-06 再創新高，R1 回撤由前次 4.21% 變為 4.13%，幾乎持平；R1 距離沒有縮短，但這不是推翻 yes 的新反向證據（`valuation.ndx_drawdown`）。
- R2 無新官方指引（沿用 2026-07-28 資料），repo 與標售需求平穩；這些是延續狀態，不構成翻轉依據（`ai.hyperscaler_capex`、`monetary.repo_stress_srf`）。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

其他缺口（✗ NOT DISCLOSED 或資料品質限制），以及是否可能改變答案：

- `monetary.private_credit_liquidity`（30 日無 redemption-request ratio、gate proration / breach 或 net inflow→outflow flip 披露）：若存在未被搜到的私募信貸贖回壓力（private-credit / non-bank fund liquidity stress），會強化 yes；缺口本身不會翻轉答案。
- `ai.hyperscaler_financing_mix` 的 event_scan 與 `ai.capital_cycle` 兩組件皆無當期披露：無法確認 hyperscaler 融資結構（capex vs FCF / 發債）或資本週期階段（capital cycle stage）的最新轉折，可能低估或高估 R2/R3 傳導速度。
- `ai.hyperscaler_capex` 僅取得四家合計約 $725bn，缺個別公司指引與方向：R2 的逐家判讀不完整；若其中已有公司下修，會直接縮短 R2 距離。
- `valuation.mag7_multiples` 僅取得 MSFT 前瞻本益比 24.5，非 Mag 7 加權 P/E；`breadth.rsp_spy`（2026-07-18）與 `breadth.top10_concentration`（2026-07-31）為較舊快照。估值脆弱度判讀不受影響方向，但精度有限。
- `monetary.fedwatch`、`valuation.analyst_tp_decomposition`、`retail.social_sentiment`、`retail.naaim`、`ai.token_growth`、`ai.customer_concentration_rpo`、`ai.depreciation_life`、`speculation.equity_put_call`、`structural.global_leveraged_approvals` 無當期披露；皆為輔助訊號，不致改變答案。
- 資料一致性註記：搜尋紀錄將 `structural.treasury_basis_trade` 記為 script 三區塊 fetch_failed，但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 皆為 status ok；本報告以 artifact 為準記 ✓ API。

最大不確定性：

1. CoreWeave 等高槓桿 AI 算力借款人的再融資與客戶合約狀態——出現 distressed exchange 或違約即推向 yes（R3 直接觸發），持續順利再融資則推向 no。
2. 窗口內兩輪 hyperscaler 季報的 capex 指引——任兩家下修即觸發 R2；持續上修則削弱 yes。
3. Fed 路徑與 10Y 5.10% 的持續性——進一步升息或長端失序推向 yes；若通膨回落、Fed 轉向寬鬆則推向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7659.44 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 5.34 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 6.78 | FRED API (series_id=SP500) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29935.59 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（回撤 %） | 4.13 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 23418.52 | FRED API (series_id=NASDAQ100) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q2 季資料，%） | 48.2301354474 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（%） | 4.0 | FRED API (series_id=DFEDTARU) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（%） | 3.75 | FRED API (series_id=DFEDTARL) | 2026-10-17 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 3.23 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 58.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.84 | FRED API (series_id=BAMLC0A0CM) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 5.1 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | 14.0 | FRED API (series_id=DGS10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.78 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps | 18.0 | FRED API (series_id=DFII10) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.35 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | -1.0 | FRED API (series_id=T10YIE) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl） | 101.91 | FRED API (series_id=DCOILWTICO) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.33 | FRED API (series_id=T5YIFR) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（%，Kim-Wright） | 1.0729 | FRED API (series_id=THREEFYTP10) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.89 | FRED API (series_id=SOFR) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.97 | FRED API (series_id=SOFR99) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.9 | FRED API (series_id=IORB) | 2026-10-18 | 2026-10-18T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,755,639（$6.76T，百萬美元） | FRED API (series_id=WALCL) | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,943,911（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-09 | 2026-10-18T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,250,253（¥625.03T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-09-01 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.46 | FRED API (series_id=VIXCLS) | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（7 日窗口，base 2026-10-08） | 16.46 | FRED API（衍生共同觀測區塊） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct | 6.81 | FRED API（衍生共同觀測區塊） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -0.27 | FRED API（衍生共同觀測區塊） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（十億美元） | 2097.9713（$2.10T） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -6883343 | CFTC TFF futures-only | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -309307 | CFTC TFF futures-only | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 101.1 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index delta_abs | 18.89 | Yahoo Finance chart API (^MOVE, unofficial) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2264.1 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-10-16 | 2026-10-18T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com，WebSearch primary | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E and AI leader P/S | WebSearch；僅取得 MSFT 前瞻 P/E | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季）；完成但無合格披露 | ✗ NOT DISCLOSED |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧（equity-vs-credit schism） | WebSearch 14 日掃描 | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight (RSP) vs cap-weight (SPY) | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio, new high/low ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA monthly data | WebSearch；沿用 2026-08 月資料 | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII Investor Sentiment | WebSearch primary | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch；完成但 7 日內無顯著討論 | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Retail Sentiment / Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | Retail Sentiment / NAAIM Exposure Index | WebSearch；無當週值 | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | Institutional Sentiment / BofA Fund Manager Survey and JPM institutional survey | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.fed_funds | Monetary & Credit / Fed funds rate: FRED series DFEDTARU and DFEDTARL | fetch_macro.py（DFEDTARU ok、DFEDTARL ok） | ✓ API |
| monetary.hy_oas | Monetary & Credit / High Yield OAS | fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | Monetary & Credit / Investment Grade OAS | fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | Monetary & Credit / 10Y Treasury yield | fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | Monetary & Credit / 10Y Treasury real yield / TIPS | fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | Monetary & Credit / 10Y breakeven inflation rate | fetch_macro.py（T10YIE，FRED 直接取得） | ✓ API |
| monetary.wti | Monetary & Credit / WTI crude oil price | fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | Monetary & Credit / CPI YoY: FRED series CPIAUCSL | fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | Monetary & Credit / 5y5y forward inflation expectation | fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | Monetary & Credit / 10Y 期限溢價（term premium）: FRED series THREEFYTP10 | fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） | ✓ API |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求（auction tail / bid-to-cover） | WebSearch 14 日 | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch；無當期快照 | ✗ NOT DISCLOSED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED series WALCL | fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch 30 日；完成但無合格披露 | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch；沿用最近季報 | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch；本季無披露 | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | WebSearch；無合格披露 | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch：quarterly_state 沿用；30 日 event_scan 完成無披露 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口（revenue-to-capex gap） | WebSearch；組合 Anthropic run-rate 與 top-4 capex | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch 30 日；無變動披露 | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段（capital cycle stage） | WebSearch：兩組件皆完成但無可用披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days: AI rename / SPAC | WebSearch＋SEC EDGAR 7 日掃描 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch movers 7 日掃描 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch 30 日 | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 14 日掃描 | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch；無當期值 | ✗ NOT DISCLOSED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch primary | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR＋ETF.com 30 日掃描 | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch 7 日；無英文披露 | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | fetch_macro.py（VIXCLS ok、vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch；交叉確認 | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch 30 日 | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py 三區塊（cftc_lev_funds ok、move_index ok、ofr_repo ok）；WebSearch 補充無合格事件 | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.54（原定來源 multpl.com） | Shiller PE CAPE ratio current October 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 成員 MSFT 前瞻本益比 24.5（原定來源 Mag 7 加權 P/E） | Magnificent 7 forward P/E valuation October 2026 | https://articlegateway.com/?p=146 （articlegateway） | 2026-09-24 | 2026-10-18T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 紀錄 1,194.5 bps | AI credit fears tech default insurance record highs October 2026 | https://www.businessday.co.za/world/international-companies/2026-10-15-ai-credit-fears-push-tech-default-insurance-to-record-highs/ （BusinessDay） | 2026-10-15 | 2026-10-18T09:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 報酬約 12.08% | RSP equal weight vs SPY YTD performance 2026 | https://pro.thestreet.com/market-commentary/rsp-vs-spy-does-diversification-require-equal-weight （TheStreet Pro） | 2026-07-18 | 2026-10-18T09:30:00+08:00 |
| breadth.top10_concentration | 前十大集中度約 38.9% | S&P 500 top 10 concentration percent record 2026 | https://walnutinvest.com/stats/market-concentration-statistics （Walnut） | 2026-07-31 | 2026-10-18T09:30:00+08:00 |
| breadth.advance_decline | 上漲家數約 29 對下跌 71 | market breadth October 16 2026 percent above 200-day advance decline | https://www.thetrading.tools/market-breadth （thetrading.tools） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.fear_greed | Fear & Greed 約 18（極度恐懼；原定來源 cnn.com） | CNN Fear and Greed Index October 16 2026 extreme fear | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ （finhacker） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| retail.margin_debt | margin debt 約 $1.45T（2026-08 月資料；原定來源 FINRA） | FINRA margin debt August 2026 year over year | https://www.thetrading.tools/margin-debt （thetrading.tools） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| retail.aaii | AAII 看多約 38.7%（週結束 2026-10-14） | AAII sentiment survey week ending October 14 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-10-14 | 2026-10-18T09:30:00+08:00 |
| institutional.bofa_jpm_survey | BofA FMS 科技股淨加碼約 37%，2020 年 8 月以來最高 | BofA October 2026 fund manager survey tech overweight cash | https://www.bloomberg.com/news/articles/2026-10-13/bofa-poll-shows-investors-most-exposed-to-tech-stocks-since-2020 （Bloomberg） | 2026-10-13 | 2026-10-18T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.77 | Treasury 10-year note auction October 7 2026 bid-to-cover | https://www.rttnews.com/3697286/ten-year-note-auction-attracts-strong-demand.aspx （RTTNews） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate social financing 2026 total | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm （SteelOrbis） | 2026-08-15 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 $725bn（最近季報） | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-10-18T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 $65bn | OpenAI Anthropic annualized revenue run rate 2026 | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選中位租金約 $4.20/hr | GPU rental price index HBM DRAM contract price October 2026 | https://uvik.net/blog/gpu-price-index/ （Uvik） | 2026-10-07 | 2026-10-18T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 2026 年 hyperscaler 發債預估約 $190bn（背景，非新事件） | hyperscaler bond issuance 2026 capex versus free cash flow | https://www.twentyfouram.com/insights/oracle-clears-the-supply-cloud-with-record-demand （TwentyFour AM） | 2026-02-02 | 2026-10-18T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic run-rate 約 $65bn（分子）；分母取 ai.hyperscaler_capex top-4 約 $725bn | AI revenue versus capex gap 2026 annualized | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai （Axios） | 2026-08-17 | 2026-10-18T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描：0 件合格事件 | AI company name change ticker SPAC announcement October 2026 | 檢查來源：SEC EDGAR 8-K、SPACInsider、Boardroom Alpha | — | 2026-10-18T09:30:00+08:00 |
| speculation.ipo_heat | 兩週內第 4 檔 IPO 撤件或延後 | IPO market October 16 2026 pulled postponed Firmus Oura | https://www.ipox.com/ipox/the-ipox-update-10162026 （IPOX） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 7 日掃描：0 件符合 2+ 主題×弱基本面（PFAI 10/7 +116.7% 落在窗外） | biggest stock gainers week October 12-16 2026 microcap 100% | 檢查來源：Tapeboard movers archive、Financial Modeling Prep daily gainers、Yahoo movers | — | 2026-10-18T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 11 月中上市 | Anthropic IPO October 2026 timing valuation S-1 | https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market （CNN） | 2026-10-05 | 2026-10-18T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描：0 件合格（NVDA 10/9 申報無 filing-level 細節） | insider selling Form 4 October 2026 Nvidia AI executives SEC | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-10-18T09:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 $40.04bn | single stock leveraged ETF assets October 2026 weekly flows | https://www.etfaction.com/single-stock-traders-pile-into-tsll-and-intw-as-levered-flows-surge/ （ETF Action） | 2026-10-16 | 2026-10-18T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市：0 件 | single stock leveraged ETF launch approval October 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed | — | 2026-10-18T09:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 9 月 ADV 創紀錄約 3.4 百萬口 | Cboe September 2026 derivatives volume 0DTE SPX record | https://www.cboe.com/insights/posts/market-metrics-that-matter-derivatives-september-2026-volume-highlights （Cboe） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.options_volume | 9 月 OCC 總結算量約 1,486,062,415 口 | OCC September 2026 monthly volume data | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report （OCC） | 2026-09-30 | 2026-10-18T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 約 14.84、SKEW 154.34 | VIX term structure SKEW October 2026 options brief | https://www.home.saxo/content/articles/options/the-middle-got-cheaper-the-edge-did-not---options-brief---12-october-2026-12102026 （Saxo） | 2026-10-12 | 2026-10-18T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 交叉確認基數約 $1.45T（2026-08 月資料） | margin debt to market cap August 2026 | https://www.thetrading.tools/margin-debt （thetrading.tools） | 2026-08-31 | 2026-10-18T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Lambda GPU 擔保融資約 $1bn | AI data center debt Lambda CoreWeave financing October 2026 | https://valueaddvc.com/pulse/ai-data-center-debt-financing-risk-2026 （ValueAdd VC） | 2026-10-01 | 2026-10-18T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-10-18",
  "iso_week": "2026-W42",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "yes",
  "horizon_end": "2027-04-18",
  "prior_date": "2026-09-13",
  "prior_answer": "yes",
  "flip_evidence": [],
  "r1_drawdown_pct": 4.13,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

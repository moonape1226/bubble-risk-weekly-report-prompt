> [DRY RUN] this report was not committed to archive.

# 2026-11-08 AI 泡沫破裂預測報告

報告日期：2026-11-08｜ISO 週次：2026-W45｜預測窗口：2026-11-08 → 2027-05-09｜前次基準：report-2026-10-18（21天前）

## 結論

**結論：yes**

三條路徑同時處於「已啟動」狀態：NASDAQ-100 一個月內自高點回撤 13.56%（R1 門檻需再跌約 13.2%），R3 候選借款人 CoreWeave 的債券殖利率升破 16%、5 年 CDS 突破 1289 bps，Microsoft 已率先下修 capex 指引（R2 四缺一已有一）。Fed 在 CPI 3.72% 下反而被定價 12 月升息，沒有寬鬆緩衝，三條路徑互相傳導，使窗口內至少一條完成的可能性高於不完成。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 26,989.99（2026-11-06），252 個交易日最高收盤 31,224.69（2026-10-06），距 52 週高點回撤 13.56%；R1 門檻水位 23,418.52，自最新收盤再跌約 13.23% 即觸發（`valuation.ndx_drawdown`）。前次報告時回撤僅 4.13%，一個月內擴大逾 9 個百分點；2026-11-05 單日收盤 26,629.81，一度更深。S&P 500 收 7,353.73（2026-11-05），自前次基準日 −3.99%，距 200 日均線僅 +0.42%、距 52 週均線 +1.84%，延伸幅度已大致消化（`valuation.sp500_trend`）。壓力讀數同步升高：VIX 28.18（2026-11-05，7 日內 +63.84%，S&P 同窗 −4.75%，屬正常的股跌波動升，非 co-movement 警戒）（`structural.vix_spx_comove`），Cboe 股票賣買權比升至 1.05（`speculation.equity_put_call`），CNN Fear & Greed 22 極度恐懼（`retail.fear_greed`），SKEW 149.37、隱含相關性 20.93（`structural.cross_asset_derivatives`）。估值仍在高位：Shiller CAPE 38.91、trailing P/E 25.14（`valuation.sp500_pe_cape`），Mag 7 前瞻 P/E 約 28.3（`valuation.mag7_multiples`），下跌空間未被估值封頂。

**判讀：** R1 已走完一半以上。窗口內的推進催化劑包括 12 月 FOMC（市場定價升息）、2027-01 下旬至 02 月初與 2027-04 下旬兩次 hyperscaler／Nvidia 財報季、以及 CoreWeave 信用事件若落地的傳導；在 VIX 28 的波動環境下，再跌 13% 屬於半年內可完成的幅度。反向力量是極度恐懼本身常伴隨反彈、S&P 已回到 200 日均線附近。

### R2 資本支出收縮

- Microsoft：2026-10-29 財報將 2026 年資本支出指引自約 175 下調至約 170（十億美元），方向為下修（`ai.hyperscaler_capex`）。
- Alphabet、Amazon、Meta：本次蒐集的證據未載其最新一季正式指引數值，方向本次無法判定（未提供指引），不得以記憶補值。

目前四家中已確認下修 1 家，尚差 1 家。hyperscaler 今年以來發債約 296（十億美元），10/29 起一週內 5 筆 AI 相關債券合計約 67（十億美元）（`ai.hyperscaler_financing_mix`），顯示 capex 已從現金流融資轉向債務融資；Oracle RPO 約 638（十億美元）（`ai.customer_concentration_rpo`）。年化 AI 終端營收：Anthropic 65 ＋ OpenAI 約 70，合計約 135（十億美元，2026-09-30）（`ai.revenue_capex_gap`）；分母本次只取得 Microsoft 約 170，無法組成 top-4＋Oracle 完整分母，缺口方向本次不判定。

**判讀：** R2 已有一家下修，窗口內含兩次完整財報季（2027-01／02 與 2027-04），只需再一家下修即成立。推力：發債依賴上升、Fed 升息抬高資金成本、股價回撤削弱 capex 的股東容忍度。阻力：另三家的指引方向本次缺資料，且 AI 終端營收仍在成長（Anthropic 上半年營收 16.3（十億美元）（`ai.openai_anthropic_revenue`））。

### R3 AI 信用事件

R3 尺寸門檻內最明顯的候選是 CoreWeave（以 AI 算力為主業）。CoreWeave 債券殖利率升破 16%（2026-11-06），5 年 CDS 突破 1289 bps（2026-11-05），且是在 NASDAQ 反彈日仍走闊（`valuation.ai_credit_schism`）——信用端在重定價、股權端未完全跟上，屬後期訊號。放款端同步去風險：ING 出售 12 筆資料中心貸款、規模約 500（2026-11-06）（`structural.ai_infrastructure_debt`）。H100 隨選租金中位數 3.87 美元／小時（2026-11-03）（`ai.compute_supply_demand`），本次無利用率或庫存證據可配對，不單獨解讀為需求轉弱。本次證據未見已發生的付款違約、covenant waiver 或 going-concern 語句，也沒有近期到期牆的具體數字。

**判讀：** CDS 1289 bps 已是 distressed 定價，意味市場認為一年內違約或 distressed exchange 並非尾部事件；若 R1 繼續下跌關閉股權融資窗口，或 hyperscaler 縮減對 neocloud 的承諾，R3 可在窗口內完成。阻力是整體 HY OAS 仍僅 3.48%，信用壓力集中在 AI 單一名稱、尚未擴散，再融資市場對大型發行人仍開放。

## 支持 yes 的證據

- [R1] NASDAQ-100 2026-11-06 收 26,989.99，較 2026-10-06 高點 31,224.69 回撤 13.56%（前次 4.13%），距 R1 門檻 23,418.52 只需再跌約 13.23% `valuation.ndx_drawdown`
- [R3] CoreWeave 債券殖利率升破 16%（2026-11-06）、5 年 CDS 突破 1289 bps（2026-11-05），信用市場以 distressed 水位定價 R3 尺寸內的主要借款人 `valuation.ai_credit_schism`
- [R2] Microsoft 2026-10-29 將 2026 年 capex 指引自約 175 下修至約 170（十億美元），R2 所需兩家已有一家 `ai.hyperscaler_capex`
- [整體] 12 月升息 25 bps 的 FedWatch 隱含機率 76.8%（2026-11-06），而 CPI YoY 3.72%（2026-09）、5y5y 2.17%，Fed 在回撤中被定價收緊而非寬鬆，缺乏政策緩衝 `monetary.fedwatch` `monetary.cpi_yoy`
- [R1] 壓力讀數同步：VIX 28.18（2026-11-05）、股票賣買權比 1.05（2026-11-05）、Fear & Greed 22（2026-11-06）、AAII 看空 48.4%（2026-11-04） `structural.vix_spx_comove` `speculation.equity_put_call` `retail.fear_greed` `retail.aaii`
- [R3] 放款端去風險：ING 出售 12 筆資料中心貸款、規模約 500（2026-11-06）；hyperscaler 今年以來發債約 296（十億美元），AI 建設進入債務融資期 `structural.ai_infrastructure_debt` `ai.hyperscaler_financing_mix`
- [R1] 估值仍高、下跌空間未被封頂：Shiller CAPE 38.91、trailing P/E 25.14（2026-11-06）、Mag 7 前瞻 P/E 約 28.3、前十大權重約 37.9% `valuation.sp500_pe_cape` `valuation.mag7_multiples` `breadth.top10_concentration`

## 支持 no 的證據

- [整體] 廣義信用市場平靜：HY OAS 3.48%、IG OAS 0.93%（2026-11-05），自前次僅走闊 17 bps 與 8 bps，壓力集中在 AI 單一名稱，未見系統性擴散 `monetary.hy_oas` `monetary.ig_oas`
- [R3] 融資窗口仍開放：10/29 起一週內 5 筆 AI 相關債券合計約 67（十億美元）順利發行，再融資管道尚未關閉 `ai.hyperscaler_financing_mix`
- [整體] 資金市場無失序：SOFR−IORB 僅 2 bps、SRF 動用 0.0（2026-11-06）、MOVE 92.77 較前次 101.1 回落 `monetary.repo_stress_srf` `structural.treasury_basis_trade`
- [R2] 只有 Microsoft 一家確認下修，下修幅度僅約 3%；AI 終端營收仍在擴張（Anthropic 上半年營收 16.3（十億美元）、Anthropic＋OpenAI 年化約 135（十億美元）） `ai.hyperscaler_capex` `ai.openai_anthropic_revenue` `ai.revenue_capex_gap`
- [R1] 散戶與資金仍在逢低承接：半導體 3 倍多頭 ETF 10 月淨流入 7.27、規模 24.31（2026-10-31）；Anthropic 遞交 S-1、目標估值 1.5 兆至 2 兆，風險胃口未崩 `structural.leveraged_etf_aum` `speculation.upcoming_ai_ipos`
- [R1] S&P 500 已回到 200 日均線附近（+0.42%），趨勢延伸已消化；極度恐懼（Fear & Greed 22）歷史上常伴隨短期反彈 `valuation.sp500_trend` `retail.fear_greed`

## 與前期比較

前次結論：yes（report-2026-10-18）
本次結論：維持

- 前次 forecast.json 沒有 `yes_basis` 欄位（寫於該欄位存在之前），沒有逐項須回應的決定性理由；本次 yes 依當前證據重新取得，不是沿用前次答案。
- R1：NASDAQ-100 回撤由前次 4.13% 擴大到 13.56%，S&P 500 自前次基準日 −3.99%，VIX 由 19.99 升至 28.18 `valuation.ndx_drawdown` `structural.vix_spx_comove`
- R3：CoreWeave 債券殖利率升破 16%、CDS 突破 1289 bps 是前次之後（2026-11-05／06）的新證據 `valuation.ai_credit_schism`
- R2：Microsoft 2026-10-29 下修 capex 指引，是前次之後新出現的第一家下修 `ai.hyperscaler_capex`
- 反向變化：HY OAS 只走闊 17 bps、MOVE 自 101.1 回落至 92.77、10Y 下行 25 bps，廣義市場未失序，因此 yes 的依據集中在 AI 專屬路徑，而非系統性危機 `monetary.hy_oas` `structural.treasury_basis_trade` `monetary.dgs10`

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

✗ NOT DISCLOSED（不能當證據引用）：retail.naaim、institutional.bofa_jpm_survey、monetary.treasury_auctions、monetary.private_credit_liquidity、ai.token_growth、ai.depreciation_life、ai.capital_cycle（quarterly_state 無披露；event_scan 有 Microsoft 10 月取消 Nscale 英國資料中心交易，規模約 3，2026-11-04，因 aggregation=all 整列不成立，只記錄在附錄）、structural.global_leveraged_approvals。其中私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）與美債標售需求的缺席可能低估 R3 傳導風險，但不至於讓結論翻向 no。

資料一致性備註：harness 搜尋紀錄稱美債基差交易槓桿的腳本三區塊 fetch_failed 並改走 WebSearch（MOVE 93.88，2026-11-04），但 macro artifact 中 `cftc_lev_funds`、`move_index`、`ofr_repo` 三塊均為 status ok；依 macro 決策分支以 artifact 為準記為 ✓ API，搜尋值不使用。10Y Δ 分解：ΔDGS10 −25 bps、ΔDFII10 −14 bps、ΔT10YIE −12 bps，driver 不可判（視窗不一致）。

最大的不確定性：

1. Alphabet、Amazon、Meta 的最新 capex 指引方向本次缺資料。若三家在上一季均已上修，R2 需要的第二家下修可能要等到 2027-04 財報季，對 yes 不利；若其中一家已下修，R2 可能已成立。
2. CoreWeave 的到期與再融資時程本次未取得。若近期沒有大額到期、仍可發新債，R3 可能拖過窗口（推向 no）；若有到期牆或 covenant 壓力，R3 會加速（推向 yes）。
3. 12 月 FOMC：若照市場定價升息，會強化 R1 的下跌推力；若 Fed 因股市回撤按兵不動，可能觸發反彈並延後 R1。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend latest | 7353.73 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 0.42 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 1.84 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（vs 前次基準日） | -3.99 | FRED API (series_id=SP500) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 26989.99 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 31224.69 | FRED API (series_id=NASDAQ100) | 2026-10-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct | 13.56 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level | 23418.52 | FRED API (series_id=NASDAQ100) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026-Q2 季資料） | 48.2301354474（%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-04-01 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest | 4.0 | FRED API (series_id=DFEDTARU) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.75 | FRED API (series_id=DFEDTARL) | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 3.48 | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | 17.0 | FRED API (series_id=BAMLH0A0HYM2) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.93 | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM delta_bps | 8.0 | FRED API (series_id=BAMLC0A0CM) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest | 4.84 | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps | -25.0 | FRED API (series_id=DGS10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest | 2.6 | FRED API (series_id=DFII10) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest | 2.23 | FRED API (series_id=T10YIE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest | 99.64 | FRED API (series_id=DCOILWTICO) | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-09 月資料） | 3.72 | FRED API (series_id=CPIAUCSL) | 2026-09-01 | 2026-11-08T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.17 | FRED API (series_id=T5YIFR) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright） | 0.9089 | FRED API (series_id=THREEFYTP10) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.92 | FRED API (series_id=SOFR) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 4.0 | FRED API (series_id=SOFR99) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.9 | FRED API (series_id=IORB) | 2026-11-08 | 2026-11-08T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6748145.0（$6.75T，百萬美元） | FRED API (series_id=WALCL) | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5945410.0（€5.95T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-10-30 | 2026-11-08T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6261882.0（¥626.19T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-10-01 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED API (series_id=VIXCLS) | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（comove=false） | 28.18 | FRED API derived block（SP500 pairing） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（base 2026-10-29） | 63.84 | FRED API derived block（SP500 pairing） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct | -4.75 | FRED API derived block（SP500 pairing） | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2111.0042（$2.11T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-10-28 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts | -7249305 | CFTC TFF futures-only | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -489473 | CFTC TFF futures-only | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 92.77 | Yahoo Finance chart API (^MOVE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index delta_abs（vs 2026-10-16 前值 101.1） | -8.33 | Yahoo Finance chart API (^MOVE) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn | 2326.9 | OFR Short-term Funding Monitor (REPO-TRIV1_TV_TOT-P) | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | Valuation / S&P 500 P/E and Shiller CAPE | multpl.com WebFetch | ✓ DIRECT |
| valuation.mag7_multiples | Valuation / Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Valuation / Analyst TP upgrade decomposition | WebSearch（90d＋同季） | ✓ SEARCH-VERIFIED（僅 TP 變動；EPS／PE 拆解未披露） |
| valuation.sp500_trend | Valuation / S&P 500 price-trend deviation | fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | Valuation / NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | Valuation / AI 信用定價分歧 | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | Breadth / S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Breadth / Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Breadth / Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | Retail Sentiment / CNN Fear & Greed Index | WebSearch（primary: SEARCH） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Retail Sentiment / Margin Debt: FINRA | WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail Sentiment / Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Retail Sentiment / Social sentiment proxies | WebSearch（7d） | ✓ SEARCH-VERIFIED |
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
| monetary.repo_stress_srf | Monetary & Credit / repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） | ✓ API |
| monetary.treasury_auctions | Monetary & Credit / 美債標售需求 | WebSearch（14d） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Monetary & Credit / Fed funds rate path expectations | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | Monetary & Credit / Fed balance sheet: FRED | fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | Monetary & Credit / Global central bank liquidity cross-check | fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | Monetary & Credit / PBoC aggregate financing | WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Monetary & Credit / Private-credit / non-bank fund liquidity stress | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI Fundamentals / Hyperscaler capex guidance | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI Fundamentals / AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI Fundamentals / OpenAI / Anthropic annualized revenue | WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI Fundamentals / Hyperscaler AI customer concentration | WebSearch | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI Fundamentals / AI compute supply/demand and overcapacity risk | WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI Fundamentals / Hyperscaler 融資結構 | WebSearch（quarterly_state stock-of-state＋event_scan 30d） | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI Fundamentals / AI 營收對 capex 缺口 | WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI Fundamentals / GPU / 伺服器折舊年限變動 | WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI Fundamentals / 資本週期階段 | WebSearch（quarterly_state stock-of-state＋event_scan 30d） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Speculative Behavior / Search for past 7 days | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | Speculative Behavior / IPO market heat | WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Speculative Behavior / Microcap thematic moonshots | WebSearch movers 掃描（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Speculative Behavior / Upcoming AI IPOs | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Speculative Behavior / Insider selling at AI | SEC EDGAR Form 4（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Speculative Behavior / Cboe equity-only put/call ratio | WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | Structural Leverage / US leveraged ETF AUM | WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | Structural Leverage / US single-stock leveraged ETF approvals | SEC EDGAR／ETF.com feed（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Structural Leverage / Global leveraged product approvals | WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | Structural Leverage / 0DTE option volume | WebSearch（Cboe 月報） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Structural Leverage / Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Structural Leverage / Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | Structural Leverage / VIX / S&P 500 co-movement | fetch_macro.py（VIXCLS ok、vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | Structural Leverage / Cross-reference only: FINRA margin debt | WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | Structural Leverage / AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Structural Leverage / Bank loans to nondepository financial institutions | fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | Structural Leverage / 美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok；aggregation any） | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻 P/E 約 28.3（原定來源：Mag 7 weighted P/E） | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ | 2026-10-13 | 2026-11-08T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein TSM 目標價 554 → 600（EPS／目標 PE 拆解未披露） | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/ | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 債券殖利率升破 16% | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5 年 CDS 突破 1289 bps | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| breadth.rsp_spy | RSP 年初至今報酬約 14.13% | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 前十大權重約 37.9% | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration | 2026-11-01 | 2026-11-08T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 1,474／下跌 1,252 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 22（極度恐懼） | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-09 月資料）約 1.48 兆美元、YoY 約 31.4% | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| retail.aaii | AAII 看多 34.1%、看空 48.4% | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 檔 | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week | 2026-11-07 | 2026-11-08T09:30:00+08:00 |
| monetary.fedwatch | 12 月升息 25 bps 隱含機率 76.8% | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000 | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_capex | Microsoft 2026 年 capex 指引約 175 → 約 170（Q3 2026 財報） | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex | 2026-10-29 | 2026-11-08T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3 | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle RPO 638 | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ | 2026-08-31 | 2026-11-08T09:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87 | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends | 2026-11-03 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 今年以來發債 296 | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 10/29 起一週內 5 筆 AI 相關債券發行合計 67 | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic 65 ＋ OpenAI 約 70，合計約 135 | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| ai.capital_cycle | [event_scan] Microsoft 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 件（Agility Robotics 完成 SPAC 合併） | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ | 2026-11-04 | 2026-11-08T09:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO 週漲 8% | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（0 件符合 2+ 主題×弱基本面） | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers | — | 2026-11-08T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 兆 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 | 2026-10-26 | 2026-11-08T09:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件合格） | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表 | — | 2026-11-08T09:30:00+08:00 |
| speculation.equity_put_call | Cboe 股票選擇權賣買權比 1.05 | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide | 2026-11-05 | 2026-11-08T09:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭 ETF 10 月底規模 24.31、當月淨流入 7.27 | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿 | — | 2026-11-08T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65%（2026-10 月資料） | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 | 2026-10-31 | 2026-11-08T09:30:00+08:00 |
| structural.options_volume | OCC 總結算量 1,486,062,415 口（2026-09 月資料） | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 28.18、SKEW 149.37、隱含相關性 20.93 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 | 2026-11-06 | 2026-11-08T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 交叉檢核基數約 1.48 兆美元（2026-09 月資料） | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T09:30:00+08:00 |
| structural.ai_infrastructure_debt | ING 出售 12 筆資料中心貸款，規模約 500 | AI data center debt financing private credit November 2026 | https://www.cnbc.com/2026/11/06/ing-ai-data-center-loans-debt.html | 2026-11-06 | 2026-11-08T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-11-08",
  "iso_week": "2026-W45",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "yes",
  "horizon_end": "2027-05-09",
  "prior_date": "2026-10-18",
  "prior_answer": "yes",
  "flip_evidence": [],
  "yes_basis": [
    {"source_id": "valuation.ndx_drawdown", "claim": "NASDAQ-100 已自 2026-10-06 高點回撤 13.56%，距 R1 門檻只差約 13.2% 跌幅，且回撤在 VIX 28、Fear & Greed 極度恐懼下仍在加速。"},
    {"source_id": "valuation.ai_credit_schism", "claim": "R3 候選借款人 CoreWeave 債券殖利率升破 16%、5 年 CDS 突破 1289 bps，信用市場已按 distressed 水位定價，窗口內出現 distressed exchange 或違約的路徑實質存在。"},
    {"source_id": "ai.hyperscaler_capex", "claim": "Microsoft 已於 2026-10-29 下修資本支出指引（約 175 → 約 170），R2 四家中第一家已下修，窗口內另含兩次財報季。"}
  ],
  "r1_drawdown_pct": 13.56,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

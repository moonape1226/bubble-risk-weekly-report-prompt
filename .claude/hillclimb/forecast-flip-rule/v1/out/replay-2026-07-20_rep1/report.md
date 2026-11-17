> [DRY RUN] this report was not committed to archive.

# 2026-07-20 AI 泡沫破裂預測報告
報告日期：2026-07-20｜ISO 週次：2026-W30｜預測窗口：2026-07-20 → 2027-01-18｜前次基準：report-2026-07-16（4天前）

## 結論

**結論：no**

三條路徑都還遠離解析門檻。R1 方面，NASDAQ-100 距 52 週高點回撤 6.74%，還要再跌約 19.58% 才觸及 25% 門檻。R2 方面，hyperscaler 2026 capex 彙總約 $700B，且仍在上修。R3 方面，AI 信用壓力只見於 Oracle／CoreWeave 的 CDS 走闊，沒有違約或 distressed exchange；HY OAS 2.71% 也顯示整體信用市場仍平靜。高估值與高槓桿說明下檔風險很大，但目前沒有證據顯示任何一條路徑會在 182 天內完成。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

- NASDAQ-100 最新收盤 28,592.66（2026-07-17）。252 個交易日最高收盤為 30,660.6（2026-06-02），距 52 週高點回撤 6.74%（`valuation.ndx_drawdown`）。
- R1 門檻水位 22,995.45。從最新收盤還要再跌約 5,597 點（約 19.58%）才會觸及。
- 近期動能轉弱：2026-07-17 晶片股賣壓擴大，NYSE 下跌家數約為上漲家數 2 倍，新高／新低 241／166（`breadth.advance_decline`）。S&P 500 自前次基準日下跌 1.01%，收在 7,457.69（`valuation.sp500_trend`）。VIX 由 15.03（2026-07-10）升至 18.77（2026-07-17），升幅 24.88%；同期 S&P 500 下跌 1.55%，屬正常的反向走勢，不是 crowded-optionality 讀數（`structural.vix_spx_comove`）。
- 下檔放大器仍在：Shiller CAPE 41.52、trailing P/E 32.08（`valuation.sp500_pe_cape`）；margin debt $1.416T，YoY +53.7%（2026-05 月資料，`retail.margin_debt`）；NAAIM 95.64（`retail.naaim`）。
- 但價格仍在長期趨勢之上：S&P 500 高於 200 日均線 6.73%、高於 52 週均線 8.42%（`valuation.sp500_trend`）。Fear & Greed 37（Fear，`retail.fear_greed`），未見追高式狂熱。
- Fed 緩衝空間有限：CPI YoY 3.46%（2026-06，`monetary.cpi_yoy`）。CME FedWatch 顯示 7/29 會議維持利率約 86.7%（`monetary.fedwatch`）。股市若急跌，Fed 用降息托底的速度可能受通膨限制。

**判讀：** 距離門檻還很遠，要再跌約 19.58% 才成立。要在窗口內觸發，需要類似 2000／2022 年的連續修正，且通常要有 R2 或 R3 的實質催化。可能的催化包括：2026 Q2 財報季的 capex／營收指引失望、AI 信用事件外溢，或通膨迫使利率路徑上移。

### R2 資本支出收縮

- Microsoft、Alphabet、Amazon、Meta 的逐家最新指引數字本次未取得。唯一取得的是彙總報導：hyperscaler 2026 capex 約 $700B，方向仍是上修（2026-05-15，`ai.hyperscaler_capex`）。四家相對前次正式指引的方向：彙總口徑為上修，逐家方向未取得。
- 截至目前，沒有任何一家下修的證據；已下修家數：0／4。
- 需求端仍偏緊：伺服器 DRAM 3Q26 合約價季增 13–18%（2026-07-03，`ai.compute_supply_demand`），與 capex 收縮相反。
- ROI 壓力是 R2 的中期風險。AI 營收對 capex 缺口（revenue-to-capex gap）：已披露的 AI 終端營收 run-rate 中，Anthropic 約 $47B、OpenAI 約 $25B，合計約 $72B，對比年化 capex 約 $700B（分母：報導口徑的 hyperscaler 合計，未逐家拆分；`ai.revenue_capex_gap`、`ai.openai_anthropic_revenue`）。
- 下一輪（2026 Q2）財報季與再下一輪（2026 Q3）都落在窗口內，具體財報日期本次未取得。

**判讀：** R2 目前完全沒有成立跡象；指引仍在上修，記憶體價格也反映需求偏緊。要在窗口內成立，至少要有兩家在 Q2 或 Q3 財報中下修。這通常要先出現 R1 等級的市場修正或融資條件急遽收緊，目前都還沒有。

### R3 AI 信用事件

- 符合規模門檻的可能借款人以 Oracle 與 CoreWeave 為代表（負債規模以公開報導口徑判斷）。Oracle 5 年 CDS 約 198bp，創紀錄；CoreWeave 約 665bp（2026-07-16，`valuation.ai_credit_schism`）。AI 信用定價分歧（equity-vs-credit schism）正朝「信貸端先重定價」方向發展，屬於後期訊號。
- 私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）：Blue Owl OCIC 在 Q2 的 redemption-request ratio 為 18.8%。基金依 5% 的 quarterly redemption cap 比例撥付，構成 gate proration / breach（2026-07-02，`monetary.private_credit_liquidity`）。目前只看到單一基金，尚無多基金的 redemption-request ratio 趨勢或 net inflow→outflow flip 證據。
- 整體信用與資金面平靜：HY OAS 2.71%、IG OAS 0.78%（2026-07-16，`monetary.hy_oas`、`monetary.ig_oas`）。repo 資金壓力（SOFR−IORB）為 −3bp，SOFR99−IORB 為 +5bp（as_of 2026-07-16）；SRF 動用（Standing Repo Facility usage）0.0（2026-07-17，`monetary.repo_stress_srf`）。
- 本次 30 日掃描未發現新的 AI 基礎設施債務融資披露，也沒有破產、付款違約、契約豁免或 going-concern 字樣的報導。沒有披露不等於沒有風險，見資料缺漏段落。

**判讀：** 信用端是三條路徑中最接近警戒的一條：Oracle CDS 創紀錄、CoreWeave 處於高收益／困境邊緣定價，私募信貸也出現 gate proration。但 R3 要求實際的破產、超過寬限期的違約或 distressed exchange，目前距離很遠。要在窗口內觸發，需要 CoreWeave 這類高槓桿 neocloud 的再融資被拒或客戶合約違約。股權市場仍開放，Anthropic IPO 正在籌備，這反而提供了再融資管道。

## 支持 yes 的證據

- [R3] AI 信用定價分歧：Oracle 5 年 CDS 約 198bp 創紀錄，CoreWeave 約 665bp（2026-07-16）。信貸端已開始對 AI 基礎設施借款人重定價，而股權估值仍高，這是後期訊號。若再融資條件惡化，最可能引發 R3，再外溢到 R1（`valuation.ai_credit_schism`）。
- [R1] NASDAQ-100 距 52 週高點回撤 6.74%（高點 2026-06-02，最新 2026-07-17），2026-07-17 晶片股賣壓擴大、NYSE 下跌家數約為上漲 2 倍；VIX 一週升 24.88% 至 18.77（`valuation.ndx_drawdown`、`breadth.advance_decline`、`structural.vix_spx_comove`）。
- [整體] 私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）：Blue Owl OCIC 的 Q2 redemption-request ratio 為 18.8%，依 5% quarterly redemption cap 進行 gate proration / breach（2026-07-02）。非銀行資金端已有流動性摩擦（`monetary.private_credit_liquidity`）。
- [整體] 槓桿與部位擁擠：margin debt $1.416T、YoY +53.7%（2026-05 月資料，與 1999／2007／2021 頂部附近的 YoY 區間相當）；NAAIM 95.64；美國槓桿 ETF 總 AUM 約 $198B。下跌時強制去槓桿可能放大回撤（`retail.margin_debt`、`retail.naaim`、`structural.leveraged_etf_aum`）。
- [整體] 估值極端：Shiller CAPE 41.52、S&P 500 trailing P/E 32.08（2026-07-17），Top-10 集中度 36.40%（`valuation.sp500_pe_cape`、`breadth.top10_concentration`）。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）：Anthropic 與 OpenAI 已披露 run-rate 合計約 $72B，對比 hyperscaler 年化 capex 約 $700B。ROI 缺口是日後 capex 下修的根本壓力（`ai.revenue_capex_gap`、`ai.openai_anthropic_revenue`）。

## 支持 no 的證據

- [R1] R1 距門檻很遠：NASDAQ-100 最新收盤 28,592.66，門檻水位 22,995.45，還要再跌約 19.58%；S&P 500 仍高於 200 日均線 6.73%（`valuation.ndx_drawdown`、`valuation.sp500_trend`）。
- [R2] capex 仍在擴張：hyperscaler 2026 capex 彙總約 $700B 且仍上修，沒有任何一家下修的證據（`ai.hyperscaler_capex`）；伺服器 DRAM 3Q26 合約價季增 13–18%，顯示算力需求仍緊（`ai.compute_supply_demand`）。
- [R3] 整體信用市場平靜：HY OAS 2.71%、IG OAS 0.78%（2026-07-16），信用重定價只限於個別 AI 名字，沒有擴散成系統性利差走闊（`monetary.hy_oas`、`monetary.ig_oas`）。
- [整體] 資金市場沒有失序：SOFR−IORB −3bp、SOFR99−IORB +5bp、SRF 動用 0.0；MOVE 70.88；leveraged funds 美債期貨淨部位 −7,562,874 口，4 週變化 −78,139 口，美債基差交易槓桿（Treasury basis-trade leverage）沒有平倉跡象（`monetary.repo_stress_srf`、`structural.treasury_basis_trade`）。
- [R3] 股權融資窗口開放：Anthropic IPO 投資人會議估值約 $965B、可能 10 月掛牌（2026-07-15）；2026 YTD 約 200 檔 IPO、募資 $141.2B。AI 生態系仍能以股權再融資，降低近期違約的可能（`speculation.upcoming_ai_ipos`、`speculation.ipo_heat`）。
- [整體] 情緒並不狂熱：CNN Fear & Greed 37（Fear）、Cboe equity put/call 0.73。避險需求已在定價，不是典型的頂部亢奮（`retail.fear_greed`、`speculation.equity_put_call`）。

## 與前期比較

前次結論：無前次預測（report-2026-07-16 為舊格式評分報告）

本次是首份 yes/no 預測格式報告，不把舊格式評分換算為 yes/no。自 2026-07-16 以來的主要數據變化：

- S&P 500 由 7,533.77 降至 7,457.69（−1.01%）；NASDAQ-100 降至 28,592.66，回撤擴大到 6.74%，仍遠低於 25% 門檻（`valuation.sp500_trend`、`valuation.ndx_drawdown`）。
- VIX 由 16.73 升至 18.77；MOVE 由 68.16 升至 70.88，波動率溫和上升（`structural.vix_spx_comove`、`structural.treasury_basis_trade`）。
- 10Y breakeven（T10YIE）+2bp 至 2.24%，5y5y +1bp 至 2.21%；DGS10／DFII10 自基準日以來沒有新觀測（`monetary.t10yie`、`monetary.t5yifr`）。
- HY／IG OAS、SOFR、WALCL、ECB／BOJ 資產負債表自基準日以來都沒有新觀測，水位不變。

## 資料缺漏與不確定性

FETCH FAILED 來源：

- `speculation.insider_form4`：搜尋有執行，但 SEC EDGAR 一手 Form 4 URL 因 egress 受限無法取得，無法逐筆核驗 14 日內的 filing，因此不視為成功的零件篩檢。這個缺口不會改變答案：內部人賣股屬情緒／估值類輔助訊號，不直接對應 R1–R3 任一解析條件。

其他缺漏（✗ NOT DISCLOSED，搜尋完成但無合格披露）：analyst TP 分解、社群情緒、BofA／JPM 調查、token growth、RPO 重複計算、hyperscaler 融資結構（兩個組件皆無披露）、折舊年限變動、資本週期階段（兩個組件皆無披露）、全球槓桿產品核准、AI infrastructure debt financing / vendor-financing loops。其中最可能影響 R3 判讀的是 AI infrastructure debt financing 與 hyperscaler 融資結構的 event_scan：若存在未被搜到的 neocloud 再融資困難，R3 風險會被低估。

資料時效與口徑限制：

- 0DTE 佔比（約 63%）的最新可得資料日期為 2026-02-28，非當期，只作背景。
- Mag 7 加權 P/E（2026-05-15）、RSP vs SPY（2026-06-10）為最近可得快照。
- Fear & Greed 取自 MacroMicro 轉載。
- 四家 hyperscaler 的逐家 capex 指引數字沒有取得，R2 只能依彙總口徑判讀。
- 10Y Δ 分解：ΔDGS10 0bp、ΔDFII10 0bp、ΔT10YIE +2bp；DGS10、DFII10 自基準日以來無新觀測（partial_stale），判讀：不可判（視窗不一致）。

最大的不確定性：

1. **2026 Q2 hyperscaler 財報（窗口內）**：若兩家以上下修 capex 指引，R2 直接成立，並可能帶動 R1。目前指引仍在上修，若財報延續上修，答案更偏 no。
2. **Oracle／CoreWeave 的信用軌跡**：CDS 持續走闊或出現評級下調、再融資受阻，是推向 yes 的主要路徑（R3→R1）。Anthropic IPO 若順利完成，會強化 AI 生態系的股權融資管道，偏向 no。
3. **通膨與利率路徑**：CPI YoY 3.46%、10Y 期限溢價（term premium）0.7788%（Kim-Wright，2026-07-10，一週 +4.7bp）。若利率再上移，高估值的貼現壓力加大，偏向 yes。若 Fed 能在回撤時放鬆，則偏向 no。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7,457.69 | FRED API (series_id=SP500) sp500_trend | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 6.73 | FRED API (series_id=SP500) sp500_trend | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.42 | FRED API (series_id=SP500) sp500_trend | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（自前次基準 %） | -1.01 | FRED API (series_id=SP500) sp500_trend | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28,592.66 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30,660.6 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-06-02 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距 52 週高點回撤 %） | 6.74 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22,995.45 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（家庭股票配置 %，2026Q1） | 45.76 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.71 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%） | 4.57 | FRED API (series_id=DGS10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%） | 2.35 | FRED API (series_id=DFII10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.24 | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps（自前次基準） | 2.0 | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD/bbl） | 79.2 | FRED API (series_id=DCOILWTICO) | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.21 | FRED API (series_id=T5YIFR) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（Kim-Wright 10Y 期限溢價 %） | 0.7788 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7d） | 4.7 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API (series_id=SOFR99) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,743,028（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,970,516（€5.97T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,395,509（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 18.77 | FRED API (series_id=VIXCLS) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of；comove=false） | 18.77 | FRED API vix_spx_comove block | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_base（base_date） | 15.03 | FRED API vix_spx_comove block | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日） | 24.88 | FRED API vix_spx_comove block | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日） | -1.55 | FRED API vix_spx_comove block | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2004.0237（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約合計） | -7,562,874 | CFTC TFF cftc_lev_funds | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w | -78,139 | CFTC TFF cftc_lev_funds | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 70.88 | Yahoo chart ^MOVE move_index | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume） | 2342.6 | OFR STFM ofr_repo | 2026-07-17 | 2026-07-20T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com WebSearch | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | MarketXLS WebSearch（AI leader P/S vs 10 年均值未取得） | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | fetch_macro.py sp500_trend（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | fetch_macro.py ndx_drawdown（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | ahasignals WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth WebSearch（US News） | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | WebSearch（MacroMicro 轉載） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA monthly data | Advisor Perspectives WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | ycharts WebSearch | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | fetch_macro.py（DFEDTARU ok、DFEDTARL ok） | ✓ API |
| monetary.hy_oas | 貨幣｜High Yield OAS | fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | fetch_macro.py（THREEFYTP10，Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok；repo_stress status ok） | ✓ API |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | Treasury auction recap WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要 WebSearch | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | Bloomberg WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC／interval fund 披露 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報／彙總報導 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／The Information WebSearch | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話 WebSearch | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce WebSearch | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | WebSearch：quarterly_state（top-5 capex vs FCF／發債）＋event_scan（30d 融資事件） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K／10-Q WebSearch（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | WebSearch：quarterly_state（供需增速）＋event_scan（30d 進出場事件） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days: AI rename / SPAC | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／Benzinga／StockTitan movers WebSearch（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4＋openinsider WebSearch（14d） | ⛔ FETCH FAILED（SEC EDGAR 一手 filing URL 因 egress 受限無法取得） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe daily market statistics WebSearch | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing WebSearch | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF.com WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe insights WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe／AInvest WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | fetch_macro.py（VIXCLS ok、vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | Advisor Perspectives WebSearch（交叉引用） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok；aggregation any） | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.08 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 41.52 | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E 約 40（trailing） | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026 （MarketXLS） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS 約 198bp 創紀錄、CoreWeave 約 665bp | Oracle CoreWeave CDS spread widening July 2026 | https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/ （Real Investment Advice） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP +10.68% vs SPY +7.47% YTD | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St.） | 2026-06-10 | 2026-07-20T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 36.40% | S&P 500 top 10 concentration percent 2026 | https://ahasignals.com/sp500-concentration-risk/ （AHA Signals；原定 State Street SPDR 持股） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| breadth.advance_decline | NYSE 下跌約 2×上漲、新高 241／新低 166 | NYSE advance decline breadth July 17 2026 | https://money.usnews.com/investing/news/articles/2026-07-17/wall-st-futures-fall-as-chip-selloff-gathers-pace-netflix-tumbles （US News／Reuters） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（Fear） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed （MacroMicro；原定 cnn.com） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt $1.416T、YoY +53.7%（2026-05 月資料） | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives；原定 FINRA） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |
| retail.aaii | AAII Bull 44.9% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number （YCharts） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 2.59、小幅 tail | US Treasury 10Y auction July 2026 bid to cover | https://cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/ （Crypto Briefing；原定 Reuters／TreasuryDirect） | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch：7/29 會議維持利率約 86.7% | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch （CryptoRank；原定 CME FedWatch） | 2026-07-18 | 2026-07-20T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance （Bloomberg） | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio 18.8%，依 5% quarterly redemption cap 比例撥付（gate proration / breach） | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://whbl.com/2026/07/02/blue-owl-keeps-withdrawal-limits-even-as-redemption-pressure-modestly-eases/ （WHBL／Reuters） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 約 $700B、仍上修（彙總口徑） | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html （Yahoo Finance） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 約 $47B／OpenAI 約 $25B run-rate | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 +13–18% QoQ | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html （TrendForce） | 2026-07-03 | 2026-07-20T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex 約 $700B vs AI 終端營收（Anthropic＋OpenAI run-rate 約 $72B） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| speculation.ai_rename_spac | EVTV→Azio AI（AZIO）改名、2026-07-13 起以新代號交易 | AI rename ticker change July 2026 Azio EVTV | https://www.businesswire.com/news/home/20260710628386/en/Azio-AI-Holdings-Inc.-Nasdaq-EVTV-to-Begin-Trading-Under-New-Ticker-Symbol-AZIO-Completing-Corporate-Rebrand （Business Wire） | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD 約 200 檔 IPO、募資 $141.2B | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/ （StockAnalysis） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot 0 件 | microcap 100% single day quantum AI moonshot July 2026 | Finviz biggest gainers／Benzinga movers／StockTitan（已檢查） | — | 2026-07-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 投資人會議、估值約 $965B、可能 10 月掛牌 | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html （CNBC） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.73（日讀數） | Cboe equity put call ratio July 2026 | https://www.cboe.com/markets/us/options/market-statistics/daily/ （Cboe） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 約 $198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing；原定 etf.com／ETFGI） | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 推出 6 檔 2x 單一個股 ETF（GOOGL／AMZN／META／AAPL 等） | single-stock leveraged ETF launch July 2026 Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-07 | 2026-07-20T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 成交約 63%（最新可得，非當期） | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/ （Cboe Insights） | 2026-02-28 | 2026-07-20T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 總成交 1,603,491,559 口、YoY +45% | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 145.13、VIX 約 16.5、期限結構 contango | VIX term structure SKEW July 2026 | https://www.ainvest.com/news/0dte-volatility-drives-market-strategies-2026-2602/ （AInvest） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt $1.416T、YoY +53.7%（交叉引用 Retail margin debt） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-07-20",
  "iso_week": "2026-W30",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-01-18",
  "prior_date": "2026-07-16",
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 6.74,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

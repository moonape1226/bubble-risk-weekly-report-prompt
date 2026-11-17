> [DRY RUN] this report was not committed to archive.

# 2026-08-06 AI 泡沫破裂預測報告

報告日期：2026-08-06｜ISO 週次：2026-W32｜預測窗口：2026-08-06 → 2027-02-04｜前次基準：report-2026-08-03（3天前）

## 結論

**結論：no**

三條路徑都離解析門檻很遠：NASDAQ-100 距 52 週高點回撤 3.83%，還要再跌約 22% 才觸及 R1；hyperscaler 在 2026-07 季報仍在上修 capex（合計約 $725B），四家中沒有任何一家下修，R2 尚未起步。最強的 yes 側訊號是 CoreWeave 5Y CDS 約 855bp、貸款利差走闊 125bp（R3 的信用重定價），但目前只看到定價惡化與 covenant 要求，沒有付款違約或 distressed exchange，且整體 HY／IG 利差與 repo 資金壓力仍然平靜，不足以推翻低基準率。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。
解析版本：v1

## 三條路徑現況

### R1 市場回撤

NASDAQ-100 最新收盤 29,487.79（2026-08-05），252 個交易日最高收盤 30,660.6（2026-06-02），距 52 週高點回撤 3.83%（`valuation.ndx_drawdown`）。R1 門檻水位為 22,995.45；從最新收盤還需再下跌約 22.02% 才會觸及。7 月下旬曾有一段明顯回落（2026-07-29 收盤 27,192.31），隨後在 8 月初快速收復。S&P 500 收在 7,723.55（2026-08-05），高於 200 日均線 9.71%、高於 52 週均線 11.32%（`valuation.sp500_trend`），屬價格延伸而非破位。估值仍在極端區：S&P 500 trailing P/E 29.74、Shiller CAPE 42.19（2026-08-05，`valuation.sp500_pe_cape`）；FINRA margin debt $1.502T、YoY +51.5%（2026-06 月資料，`retail.margin_debt`），落在歷史頂部附近常見的 +40–50% 區間之上。這些說明下行空間大，但不構成 182 天內完成 25% 回撤的時點證據。VIX 15.81（2026-08-05），過去 7 日 VIX −23.48%、S&P 500 +5.57%，未出現同漲的 crowded-optionality 讀數（`structural.vix_spx_comove`）。

**判讀：** R1 距門檻仍有約 22% 的空間，目前是在高估值上的回升階段而非下跌趨勢。要在窗口內觸發 R1，需要一個外部催化——例如 R3 信用事件擴散、hyperscaler 財報引發 capex/ROI 重估，或美債供給壓力把長端殖利率推高——並讓高槓桿部位（margin debt、槓桿 ETF）被迫去槓桿。

### R2 資本支出收縮

依 2026-07-28 的報導，hyperscaler 2026 年 capex 在最新一輪（2026 Q2）季報後續上修，合計約 $725B；Alphabet 的上修甚至引發賣壓（`ai.hyperscaler_capex`）。逐家判讀：

- Microsoft：最新指引來自 2026 Q2 季報（2026-07 下旬），方向為上修／未見下修（報導未逐家列出數值）。
- Alphabet：2026 Q2 季報（2026-07 下旬）上修，市場以賣壓回應。
- Amazon：2026 Q2 季報（2026-07 下旬），方向為上修／未見下修（報導未逐家列出數值）。
- Meta：2026 Q2 季報（2026-07 下旬），方向為上修／未見下修（報導未逐家列出數值）。

目前四家中下修家數為 0。下一輪（2026 Q3）季報預期落在 10 月下旬至 11 月初，再下一輪（2026 Q4）約在 2027 年 1 月底至 2 月初，可能跨越窗口終點 2027-02-04；確切日期本次未取得。需求面支撐仍在：H200 租金約 $4.39/hr，HBM／DRAM 合約價續升，供給缺口延至 2027 上半年（2026-08-01，`ai.compute_supply_demand`）。脆弱點在營收品質：Microsoft RPO 約 $678B，其中約 32% 繫於單一客戶 OpenAI（2026-07-30，`ai.customer_concentration_rpo`）；沿用的 AI 營收對 capex 缺口組合為年化 AI 終端營收約 $72B（Anthropic $47B＋OpenAI $25B，2026-06-15 組件）對比 hyperscaler 合計 2026 capex 約 $725B（分母為該報導所指 hyperscaler 集合，不宣稱全產業；`ai.revenue_capex_gap`），缺口仍大，但這是延續的季頻狀態，不是新證據。

**判讀：** R2 尚未起步，方向反而是上修。要在窗口內觸發，至少兩家須在 Q3 或 Q4 季報中下修，這通常需要先有 AI 終端需求轉弱（例如 OpenAI 等集中客戶無法履約）或資本市場關閉；目前算力租金與記憶體價格證據指向需求仍緊。

### R3 AI 信用事件

R3 最相關的借款人是以 AI 算力為主業的 neocloud，尤其 CoreWeave。AI 信用定價已出現明顯分歧：CoreWeave 5Y CDS 約 855bp，其 $2.6B 貸款利差走闊 125bp，投資人開始要求 covenants；Oracle CDS 約 215bp（2026-08-03，`valuation.ai_credit_schism`）。CoreWeave 於 2026-07-29 為與 Anthropic 掛鉤的 $2.6B 貸款調高收益率；Nebius 於 2026-07-17 取得 $775M 擔保融資（`structural.ai_infrastructure_debt`）。這說明信貸端開始對 AI 基礎設施重定價，但同時融資管道仍開放（貸款仍能以更高價格完成）。CoreWeave 的總負債規模本次證據未載明具體數字，故無法在此確認其是否達 R3 的 50 億美元門檻；也沒有任何證據顯示付款違約、寬限期、covenant waiver、distressed exchange 或 going-concern 語言。整體信用環境平靜：HY OAS 2.73%、IG OAS 0.78%（2026-08-04，`monetary.hy_oas`、`monetary.ig_oas`）；repo 資金壓力（SOFR−IORB）為 1bp，SRF 動用（Standing Repo Facility usage）$0.001bn（`monetary.repo_stress_srf`）。

**判讀：** R3 是三條路徑中唯一有方向性惡化的一條，但仍停在「定價走闊」階段，距「違約／破產／distressed exchange」有明顯距離。要在窗口內觸發，需要某個高槓桿 AI 算力借款人遭遇再融資失敗或核心客戶合約中斷；855bp 的 CDS 反映市場給予的違約風險已不低，是下一次需要密切追蹤的指標。

## 支持 yes 的證據

- [R3] CoreWeave 5Y CDS 約 855bp、$2.6B 貸款利差走闊 125bp，貸款人要求加入 covenants（2026-08-03），且 CoreWeave 2026-07-29 必須調高 Anthropic 掛鉤貸款的收益率才能完成融資——AI 信用定價分歧（equity-vs-credit schism）正在從「無差別」轉向「信貸端先重定價」的後期型態（`valuation.ai_credit_schism`、`structural.ai_infrastructure_debt`）。
- [整體] 估值與槓桿處於極端區：Shiller CAPE 42.19、trailing P/E 29.74（2026-08-05，`valuation.sp500_pe_cape`）；FINRA margin debt $1.502T、YoY +51.5%（2026-06 月資料，`retail.margin_debt`）；美國槓桿 ETF 總 AUM 創高約 $198B（2026-07-23，`structural.leveraged_etf_aum`）——一旦有催化，去槓桿會放大 R1 的下行幅度。
- [R2] 營收品質集中：Microsoft RPO 約 $678B，約 32% 繫於 OpenAI 單一客戶（2026-07-30，`ai.customer_concentration_rpo`）；AI 年化終端營收約 $72B 對比 hyperscaler 合計 capex 約 $725B（沿用 2026-06-15 營收組件，`ai.revenue_capex_gap`）。集中客戶若無法履約，capex 下修的觸發點會集中出現。
- [R1] 美債供給壓力升溫：5Y 標售連續 14 次出現 tail、bid-to-cover 為 2022-09 以來最差，7Y tail 0.8bp（2026-07-28，`monetary.treasury_auctions`）；10Y 期限溢價（term premium）0.8681%（Kim-Wright 模型，2026-07-31，trailing 7 日 +3bp，`monetary.term_premium`）；TLT 1M skew 創 GFC 以來新高（2026-08-03，`structural.cross_asset_derivatives`）。長端利率重定價是壓縮高 P/E 的潛在催化。
- [R1] 通膨限制 Fed 的緩衝空間：CPI YoY 3.46%（2026-06 月資料，`monetary.cpi_yoy`），7/29 FOMC 鷹派持平、FedWatch 對 9 月定價分歧（約 62%，2026-08-04，`monetary.fedwatch`），若 AI 股出現回撤，央行不易快速降息托底。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 3.83%（2026-08-05 收盤 29,487.79 vs 2026-06-02 高點 30,660.6），R1 門檻 22,995.45 需再跌約 22.02%；S&P 500 仍高於 200 日均線 9.71%（`valuation.ndx_drawdown`、`valuation.sp500_trend`）。
- [R2] hyperscaler 2026 capex 在 2026-07 季報後續上修至合計約 $725B，四家中下修 0 家（2026-07-28，`ai.hyperscaler_capex`）；算力需求仍緊，H200 租金約 $4.39/hr、HBM／DRAM 合約續升、缺口延至 2027 上半年（2026-08-01，`ai.compute_supply_demand`）。
- [整體] 廣義信用與資金市場平靜：HY OAS 2.73%、IG OAS 0.78%（2026-08-04，`monetary.hy_oas`、`monetary.ig_oas`）；SOFR−IORB 1bp、SOFR99−IORB 9bp、SRF 動用 $0.001bn（`monetary.repo_stress_srf`）；MOVE 73.58（2026-08-05，較 2026-08-03 的 80.48 回落，`structural.treasury_basis_trade`）。R3 若要擴散成系統性事件，目前缺乏傳導跡象。
- [R3] AI 基礎設施融資管道仍開放：CoreWeave $2.6B 貸款以較高收益率完成、Nebius $775M 擔保融資完成（2026-07-17／2026-07-29，`structural.ai_infrastructure_debt`），重定價而非斷貸，與 R3 所需的違約／distressed exchange 相距甚遠。
- [整體] 情緒並非狂熱：AAII 看空 42.1%、看多 31.0%（2026-07-30，`retail.aaii`）；CNN Fear & Greed 約 58（Greed，非 Extreme Greed，2026-08-05，`retail.fear_greed`）；RSP 等權 YTD +14.26% 領先 SPY +13.71%（2026-08-03，`breadth.rsp_spy`），漲勢擴散而非窄化；VIX 過去 7 日 −23.48%、未與指數同漲（`structural.vix_spx_comove`）。

## 與前期比較

前次結論：無前次預測（report-2026-08-03 為舊格式評分報告）

- 前次為舊格式評分報告，其分數不轉換為 yes/no；本次為首次以 yes/no 預測格式產出，flip_evidence 為空。
- 自 2026-08-03 以來：NASDAQ-100 由 28,776.8 回升至 29,487.79；S&P 500 +1.62%；VIX 由 15.86 微降至 15.81；MOVE 由 80.48 降至 73.58；10Y 殖利率 −7bp（ΔDFII10 −3bp、ΔT10YIE −5bp，視窗不一致，driver 判讀為不可判（視窗不一致））；HY OAS −5bp，IG OAS 持平。
- 新的信用面資訊是 CoreWeave CDS／貸款利差走闊（2026-08-03），屬 R3 早期重定價訊號，但不足以讓本次答案轉為 yes。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

未取得當期披露（✗ NOT DISCLOSED）的來源：NAAIM、BofA／JPM 調查、私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）、token 成長、OpenAI／Anthropic 當季營收披露（最新為 2026-06-15 的上一季數據，僅作 AI 營收對 capex 缺口的沿用組件）、hyperscaler 融資結構的 30 日事件掃描（季頻狀態可得：top-5 capex 已超越 FCF、2026 發債約 $182B）、折舊年限變動、資本週期階段（增速證據不足，本次不判定週期階段）、全球槓桿產品核准。其中私募信貸贖回壓力與融資結構事件掃描與 R3 相關，若有未被捕捉的 gate proration / breach 或大型表外融資事件，可能讓 R3 判讀更偏 yes，但不太可能單獨翻轉答案。三項零結果篩查（+AI 改名／SPAC、microcap thematic moonshots、內部人 Form 4）本次均為 0 件合格事件；Form 4 候選紀錄缺少 filing-level 細節（申報日與個別申報 URL），依規則不列名。

最大的不確定性：

- CoreWeave 等 neocloud 的總負債規模與近期到期／再融資需求本次未取得；若證實負債 ≥ $5B 且有大額到期落在窗口內，R3 的可能性會上升（推向 yes）。
- 2026 Q3 hyperscaler 季報（預期 10 月下旬至 11 月初）：若兩家以上轉為下修，R2 可直接觸發（推向 yes）；若續上修則強化 no。
- 美債供給／期限溢價：若標售弱勢持續並推升長端殖利率，可能成為高估值股票的估值壓縮催化（推向 yes）；目前 MOVE 回落、repo 平靜（推向 no）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7723.55 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 9.71 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 11.32 | FRED API (series_id=SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 29487.79 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) | 2026-06-02 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 3.83 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026 Q1，家計股票配置 %） | 45.76080873390133（約 45.76%） | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（目標區間上限） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（目標區間下限） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（HY OAS %） | 2.73 | FRED API (series_id=BAMLH0A0HYM2) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（IG OAS %） | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（10Y 殖利率 %） | 4.63 | FRED API (series_id=DGS10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dgs10 | DGS10 delta_bps（vs 2026-08-03） | -7.0 | FRED API (series_id=DGS10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（10Y 實質殖利率 %） | 2.4 | FRED API (series_id=DFII10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.dfii10 | DFII10 delta_bps（vs 2026-08-03） | -3.0 | FRED API (series_id=DFII10) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（10Y breakeven %） | 2.22 | FRED API (series_id=T10YIE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps（vs 2026-08-03） | -5.0 | FRED API (series_id=T10YIE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（WTI 美元／桶） | 81.96 | FRED API (series_id=DCOILWTICO) | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料，CPI YoY %） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-08-06T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（5y5y forward %） | 2.26 | FRED API (series_id=T5YIFR) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（10Y 期限溢價（term premium），Kim-Wright %） | 0.8681 | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 日） | 3.0 | FRED API (series_id=THREEFYTP10) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.66 | FRED API (series_id=SOFR) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.74 | FRED API (series_id=SOFR99) | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-08-06 | 2026-08-06T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.001 | FRED API (series_id=RPONTTLD) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| monetary.walcl | WALCL latest（Fed 資產負債表） | 6738190.0（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-29 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest（ECB 資產負債表） | 5941248.0（€5.94T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-31 | 2026-08-06T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest（BOJ 資產負債表） | 6442957.0（¥644.30T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-07-01 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 15.81 | FRED API (series_id=VIXCLS) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of） | 15.81 | FRED API (series_id=VIXCLS, SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（7 日，base 2026-07-29） | -23.48 | FRED API (series_id=VIXCLS, SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（7 日，base 2026-07-29） | 5.57 | FRED API (series_id=VIXCLS, SP500) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest（銀行對 NBFI 放款） | 2004.9941（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-22 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（槓桿基金美債期貨淨部位，口） | -7481041 | CFTC TFF futures-only | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -52919 | CFTC TFF futures-only | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest（MOVE） | 73.58 | Yahoo Finance chart API (^MOVE) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index prior（MOVE） | 80.48 | Yahoo Finance chart API (^MOVE) | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2342.8 | OFR STFM (REPO-TRIV1_TV_TOT-P) | 2026-08-05 | 2026-08-06T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | SSGA 研究摘要 WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報摘要 [primary: SEARCH]，90d＋同季 | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500，sp500_trend block） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100，ndx_drawdown block） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場報導 [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | financecharts WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | Pensions & Investments WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | StockCharts breadth WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA | FINRA via Advisor Perspectives WebSearch（月頻 stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag WebSearch，7d | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED BOGZ1FL153064486Q） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／YCharts [primary: SEARCH] | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM institutional survey | 賣方調查 WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED series DFEDTARU and DFEDTARL | scripts/fetch_macro.py | ✓ API（DFEDTARU ok；DFEDTARL ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（FRED BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（FRED BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（FRED DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield / TIPS | scripts/fetch_macro.py（FRED DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（FRED T10YIE，FRED-direct） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（FRED DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED series CPIAUCSL | scripts/fetch_macro.py（yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（FRED T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED series THREEFYTP10 | scripts/fetch_macro.py（Kim-Wright） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED series SOFR, SOFR99, IORB, RPONTTLD | scripts/fetch_macro.py（repo_stress block） | ✓ API（SOFR ok；SOFR99 ok；IORB ok；RPONTTLD ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | 標售 recap [primary: SEARCH]，14d | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch 摘要 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED series WALCL | scripts/fetch_macro.py | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check — ECB / BOJ | scripts/fetch_macro.py（ECBASSETSW、JPNASSETS） | ✓ API（ECBASSETSW ok；JPNASSETS ok） |
| monetary.pboc | 貨幣｜PBoC aggregate financing / liquidity operations | investing.com WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC／interval fund 披露 [primary: SEARCH]，30d | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報／財經報導 WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic／OpenAI／Google 披露 WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／媒體報導 WebSearch（最新披露 2026-06-15 屬上一季，非當季） | ✗ NOT DISCLOSED |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration 與 backlog 重複計算風險（RPO double-counting） | 財報電話摘要 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | GPU 租金／HBM 價格 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | [primary: SEARCH]；quarterly_state＝Sage Advisory 季頻狀態；event_scan＝30d 發債／融資事件掃描，完成但無合格事件 | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組件組合 [primary: SEARCH]（stock-of-state 沿用） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動（depreciation useful-life change） | 10-K／10-Q 掃描 [primary: SEARCH]，30d | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | [primary: SEARCH]；quarterly_state＝供需增速對比；event_scan＝30d 進出場事件掃描；兩者皆完成但無合格披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days +AI rename / SPAC | Reuters／Benzinga／BusinessWire WebSearch，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | Renaissance Capital WebSearch，7d | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／StockAnalysis／StockTitan gainers [primary: SEARCH]，7d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 WebSearch，30d | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership companies | SEC EDGAR Form 4 [primary: SEC EDGAR]，14d | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | YCharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com／財經報導 [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF 發行公告 WebSearch，30d | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch，7d | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe 季報摘要 WebSearch | ✓ SEARCH-VERIFIED |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com WebSearch（月頻） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe insights WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS＋vix_spx_comove block） | ✓ API（VIXCLS ok；vix_spx_comove ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用散戶 margin debt WebSearch | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | Bloomberg 等報導 [primary: SEARCH]，30d | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds、move_index、ofr_repo）；WebSearch 補充無合格事件 | ✓ API（cftc_lev_funds ok；move_index ok；ofr_repo ok） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.74 | S&P 500 trailing P/E August 5 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.19 | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 約 29x vs 指數約 25.6x，溢價壓縮 | Magnificent 7 valuation premium lowest decade 2026 | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026 （State Street） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標價 $285→$288，EPS 驅動為主（EPS Δ 與 target PE Δ 未披露） | Morgan Stanley NVDA target 288 July 2026 AI demand | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044 （Investing.com） | 2026-07-13 | 2026-08-06T09:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 約 855bp、$2.6B 貸款利差 +125bp、貸款人要求 covenants；Oracle CDS 約 215bp | CoreWeave CDS spread blows out 125 covenants Oracle August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm （Tech Times） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.rsp_spy | RSP 總報酬 YTD +14.26% vs SPY +13.71% | RSP vs SPY equal weight total return YTD August 2026 | https://www.financecharts.com/etfs/SPY/performance/total-return （FinanceCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度約 41% | S&P 500 top 10 concentration percent record 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/ （Pensions & Investments） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| breadth.advance_decline | 約 64% 成分股在 50DMA 之上、A/D 線創高、McClellan 轉負 | S&P 500 breadth percent above 50 day moving average August 2026 McClellan | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/ （StockCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 約 58（Greed） | CNN Fear and Greed Index August 5 2026 | https://www.cnn.com/markets/fear-and-greed （CNN） | 2026-08-05 | 2026-08-06T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt（2026-06 月資料）$1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives，原始來源 FINRA） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| retail.aaii | AAII Bear 42.1%／Neutral 26.9%／Bull 31.0% | AAII investor sentiment survey July 30 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| retail.social_sentiment | WSB「Save Wendy's」WEN 軋空討論，空頭比例約 44%（非 AI 標的） | Reddit WSB Wendy's WEN short squeeze August 2026 | https://finance.yahoo.com/markets/stocks/articles/reddit-wants-save-wendy-inside-161925726.html （Yahoo Finance） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.treasury_auctions | 5Y 標售連續 14 次 tail、bid-to-cover 為 2022-09 以來最差；7Y tail 0.8bp | US Treasury 5 year 7 year auction tail bid to cover July 2026 | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026 （TFTC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| monetary.fedwatch | FOMC 7/29 鷹派持平；FedWatch 9 月會議定價約 62%，分歧 | CME FedWatch September 2026 probability FOMC hold | https://growbeansprout.com/tools/fedwatch （CME FedWatch 摘要） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| monetary.pboc | 人行逆回購合計約 ¥2.1T、7/24 MLF 淨投放 ¥100B | PBoC reverse repo injection 2.1 trillion yuan late July 2026 | https://www.investing.com/news/economy-news/chinas-pboc-to-conduct-overnight-reverse-repos-inject-a-total-of-21-trillion-yuan-4810853 （Investing.com） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 續上修，合計約 $725B；Alphabet 上修引發賣壓（2026 Q2 季報） | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO 約 $678B，約 32% 繫於單一客戶 OpenAI | Microsoft RPO backlog 678 billion single customer OpenAI 2026 | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/ （Benzinga via TradingView） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| ai.compute_supply_demand | HBM／DRAM 合約價續升、H200 租金約 $4.39/hr、供給缺口延至 2027 上半年 | H200 GPU rental price HBM DRAM contract 2026 shortage 2027 | https://jarvislabs.ai/blog/h200-price （JarvisLabs） | 2026-08-01 | 2026-08-06T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超越 FCF；2026 發債約 $182B；表外結構逾 $120B（季頻狀態，非 30 日事件） | hyperscaler capex FCF debt issuance 182 billion off balance sheet SPV 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure （Sage Advisory） | 2026-07-24 | 2026-08-06T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 $72B（Anthropic $47B＋OpenAI $25B，2026-06-15 組件）vs hyperscaler 合計 2026 capex 約 $725B（2026-07-28 組件，分母為該報導 hyperscaler 集合） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI）；https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html （CNBC） | 2026-06-15 | 2026-08-06T09:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC／無營收投機 IPO 篩查：0 件合格 | AI rename ticker SPAC no revenue IPO July 30 August 6 2026 | Reuters／Benzinga／BusinessWire SPAC 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.ipo_heat | 本週約 21 檔跨週定價、無 blowout 首日；YTD 約 $251B／86 檔 | US IPO pricings week August 3 2026 Renaissance | https://www.renaissancecapital.com/IPO-Center/Pricings （Renaissance Capital） | 2026-08-04 | 2026-08-06T09:30:00+08:00 |
| speculation.microcap_moonshots | microcap thematic moonshot 篩查：0 件合格 | microcap 100% single day quantum fusion space nuclear small cap August 2026 | Finviz／StockAnalysis／StockTitan gainers 螢幕 | — | 2026-08-06T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標約 $1T IPO 面臨時程考驗；Anthropic 續進 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground （Benzinga） | 2026-07-28 | 2026-08-06T09:30:00+08:00 |
| speculation.insider_form4 | AI／市場領導股 Form 4 篩查：0 件合格（候選紀錄缺 filing date 與個別申報 URL，不列名） | Snowflake Dageville Tempus Lefkofsky Form 4 insider sale July 2026 SEC | SEC EDGAR Form 4 browse | — | 2026-08-06T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.55（日讀數） | Cboe equity put call ratio August 3 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio （YCharts） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.leveraged_etf_aum | 美國槓桿 ETF 總 AUM 創高約 $198B | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing） | 2026-07-23 | 2026-08-06T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x 單股槓桿 ETF＋ELOL（TSLA＋SpaceX）發行 | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-30 | 2026-08-06T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量約 65%（Cboe 2026 Q2） | 0DTE SPX options share volume Cboe Q2 2026 65% | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641 （Investing.com） | 2026-05-31 | 2026-08-06T09:30:00+08:00 |
| structural.options_volume | OCC（2026-06 月資料）總量 16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-08-06T09:30:00+08:00 |
| structural.cross_asset_derivatives | SKEW 約 139.96、VIX 約 16.9 contango、TLT 1M skew 創 GFC 以來高 | VIX SKEW term structure bond volatility August 3 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher （Cboe） | 2026-08-03 | 2026-08-06T09:30:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt（2026-06 月資料）$1.502T、YoY +51.5%（交叉引用，僅確認） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 （Advisor Perspectives） | 2026-07-20 | 2026-08-06T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B Anthropic 掛鉤貸款 2026-07-29 調高收益率；Nebius $775M 擔保融資 2026-07-17 | CoreWeave 2.6 billion loan Anthropic yield boosted July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic （Bloomberg） | 2026-07-29 | 2026-08-06T09:30:00+08:00 |

## 本次預測存檔

```json
{
  "date": "2026-08-06",
  "iso_week": "2026-W32",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "question_version": 1,
  "resolution_version": 1,
  "answer": "no",
  "horizon_end": "2027-02-04",
  "prior_date": "2026-08-03",
  "prior_answer": null,
  "flip_evidence": [],
  "yes_basis": [],
  "r1_drawdown_pct": 3.83,
  "resolution": null
}
```

本報告為條件式判斷，非投資建議或擇時訊號。

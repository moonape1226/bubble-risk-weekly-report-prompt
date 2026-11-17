> [DRY RUN] this report was not committed to archive.

# 2026-07-20 AI 泡沫破裂預測報告
報告日期：2026-07-20｜ISO 週次：2026-W30｜預測窗口：2026-07-20 → 2027-01-18｜前次基準：report-2026-07-16（4天前）

## 結論

**結論：no**

三條路徑都尚未啟動：NASDAQ-100 距 52 週高點回撤 6.74%，距 R1 門檻仍需再跌約 19.58%；四家 hyperscaler 的 2026 capex 合計 ≈$700B 且仍在上修（0/4 下修），R2 沒有起點。AI 信用端已出現重定價（CoreWeave 5yr CDS ≈665bp、Oracle ≈198bp 創紀錄），私募信貸也有實際 gate proration / breach，但 HY OAS 2.71% 仍窄，且沒有任何 R3 規模借款人出現違約或 distressed exchange，不足以推翻 base rate。

## 解析條件

**問題：** 自報告日起 182 天內，AI 泡沫是否破裂？

窗口內以下任一條件成立即解析為 yes，否則為 no：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人，發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

解析版本：v1

## 三條路徑現況

### R1 市場回撤

`valuation.ndx_drawdown`：NASDAQ-100 最新收盤 28,592.66（2026-07-17），252 交易日最高收盤 30,660.60（2026-06-02），距 52 週高點回撤 6.74%。R1 門檻水位 22,995.45；從最新收盤還要再跌約 19.58% 才會觸發。從 07-16 的 29,025.77 到 07-17 這兩天跌了約 1.5%，背景是 07-17 的晶片股拋售（NYSE 下跌家數約為上漲家數的 2 倍，`breadth.advance_decline`）。S&P 500 收 7,457.69，仍比 200 日均線高 6.73%、比 52 週均線高 8.42%，比前次基準日跌 1.01%（`valuation.sp500_trend`）。VIX 在 trailing 7 日窗口（2026-07-10 → 2026-07-17）從 15.03 升到 18.77（+24.88%），同期 S&P 500 跌 1.55%，屬正常的避險反向走勢，沒有出現「指數漲、VIX 也漲」的 crowded-optionality 讀數（comove=false，`structural.vix_spx_comove`）。估值與部位都偏擁擠：S&P 500 trailing P/E 32.08、Shiller CAPE 41.52（`valuation.sp500_pe_cape`），NAAIM 95.64（`retail.naaim`），FINRA margin debt $1.416T、YoY +53.7%（`retail.margin_debt`），所以一旦出現催化劑，跌幅會很大。

**判讀：** 離 R1 還很遠，還要再跌約 19.58%。窗口內要觸發，大概需要兩件事同時發生：Q2 財報季（依季報節奏應在 7 月底至 8 月初，具體日期本次未取得）出現 capex 或 AI 營收失望，加上信用事件或去槓桿把高 margin debt 與擁擠部位一起拖下來。目前只看到一次晶片股回檔，還沒有持續性的傳導。

### R2 資本支出收縮

`ai.hyperscaler_capex`：本次能取得的最新官方指引來自 2026-05-15 的彙整報導（Q1 2026 財報季），四家 hyperscaler 2026 年 capex 合計 ≈$700B，報導描述方向為「仍上修」。各公司個別情況：

- Microsoft：最新指引見 Q1 2026 財報季彙整；方向：上修／持平（彙整未見下修；本次證據沒有個別金額）。
- Alphabet：同上；方向：上修／持平（未見下修）。
- Amazon：同上；方向：上修／持平（未見下修）。
- Meta：同上；方向：上修／持平（未見下修）。

到目前為止 0/4 下修。供給端訊號也沒有轉弱：TrendForce 指出伺服器 DRAM 3Q26 合約價季增 +13–18%（2026-07-03，`ai.compute_supply_demand`），屬於需求強勁的讀數，沒有 order digestion 的跡象。產業層級的 AI 營收對 capex 缺口（revenue-to-capex gap）很大：年化 capex ≈$700B（分母：top-4 hyperscaler；Oracle 本次無季頻披露，不納入），對比 AI 終端營收在低百億美元級（Anthropic ≈$47B、OpenAI ≈$25B run-rate，資料日 2026-05-15，`ai.revenue_capex_gap`）。這個缺口是 R2 的長期壓力來源，但不是窗口內的觸發條件。

**判讀：** R2 沒有起點。窗口內大約涵蓋兩輪財報（Q2 與 Q3），R2 要求至少兩家在其中一輪相對前次指引下修。現有方向全部向上，除非 R1 或 R3 先引發融資條件急轉，否則在 182 天內出現兩家下修的機會很低。

### R3 AI 信用事件

`valuation.ai_credit_schism`：截至 2026-07-16，Oracle 5yr CDS ≈198bp，創紀錄；CoreWeave 5yr CDS ≈665bp。AI 信用端正在走闊，但股價還沒有完全反映（NASDAQ-100 只從高點回撤個位數）。按這個 bullet 的判讀規則，這屬於後期訊號：信用端先重定價，股權端還沒跟上。不過整體信用市場依然平穩：HY OAS 2.71%、IG OAS 0.78%（2026-07-16，`monetary.hy_oas`、`monetary.ig_oas`）。非銀行資金端，Blue Owl OCIC Q2 的 redemption-request ratio 達 18.8%，超過 5% 的 quarterly redemption cap，已發生 gate proration / breach（2026-07-02，`monetary.private_credit_liquidity`），代表私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）是真的，但只有單一基金族群的披露。repo 資金壓力（SOFR−IORB）為 −3bp，SOFR99−IORB 為 +5bp，SRF 動用 0（`monetary.repo_stress_srf`），融資管道沒有失序。本次 30 日掃描沒有找到新的 AI infrastructure debt financing / vendor-financing loops 披露，也沒有任何借款人的付款違約、寬限期、covenant waiver 或 distressed exchange 消息；R3 規模候選人（例如 CoreWeave）的負債規模與到期結構，本次證據沒有提供。

**判讀：** R3 是三條路徑中最接近的一條。CoreWeave CDS ≈665bp 代表市場已在定價明顯的信用風險，但目前只是高利差，不是違約。窗口內要觸發，需要 R3 規模借款人遇到再融資失敗或流動性斷裂，最後走到破產申請、付款違約或 distressed exchange。目前沒有任何這類事件或寬限期消息。

## 支持 yes 的證據

- [R3] AI 信用定價分歧（equity-vs-credit schism）正在擴大：Oracle 5yr CDS ≈198bp 創紀錄、CoreWeave ≈665bp（2026-07-16），屬於信用端先行重定價的後期訊號 `valuation.ai_credit_schism`。
- [R3] 私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）已有實際 gate proration / breach：Blue Owl OCIC Q2 redemption-request ratio 18.8%，超過 5% quarterly redemption cap，按比例撥付（2026-07-02）`monetary.private_credit_liquidity`。
- [R1] 槓桿與部位擁擠：FINRA margin debt $1.416T、YoY +53.7%（2026-05 月資料），已在歷史頂部常見的 +40–50% 區間之上 `retail.margin_debt`；NAAIM 95.64（2026-07-15）`retail.naaim`。
- [R1] 估值極端：S&P 500 trailing P/E 32.08、Shiller CAPE 41.52（2026-07-17）`valuation.sp500_pe_cape`；Top-10 集中度 36.40%（2026-07-02）`breadth.top10_concentration`。
- [R1] 短線已轉弱：07-17 晶片股拋售，NYSE 下跌家數約為上漲的 2 倍 `breadth.advance_decline`；VIX trailing 7 日 +24.88% 至 18.77（2026-07-17）`structural.vix_spx_comove`。
- [整體] Fed 緩衝空間有限：CPI YoY 3.46%（2026-06）`monetary.cpi_yoy`，FedWatch 顯示 7/29 會議維持利率 ≈86.7%（2026-07-18）`monetary.fedwatch`，若 AI 帶動回撤，降息托底較慢。
- [R2] AI 營收對 capex 缺口（revenue-to-capex gap）巨大：年化 capex ≈$700B 對比 AI 終端營收低百億美元級（分母：top-4 hyperscaler，資料日 2026-05-15）`ai.revenue_capex_gap`。

## 支持 no 的證據

- [R1] NASDAQ-100 距 52 週高點回撤 6.74%（2026-07-17），收盤 28,592.66，門檻 22,995.45，還要再跌約 19.58% `valuation.ndx_drawdown`。
- [R2] Hyperscaler capex 仍在上修：四家 2026 年合計 ≈$700B（Q1 2026 財報季彙整，2026-05-15），0/4 下修 `ai.hyperscaler_capex`。
- [整體] 整體信用市場沒有壓力：HY OAS 2.71%、IG OAS 0.78%（2026-07-16）`monetary.hy_oas` `monetary.ig_oas`；與 AI 個別名稱的 CDS 走闊相比，信用壓力仍未擴散。
- [R3] 融資管道正常：SOFR−IORB −3bp、SOFR99−IORB +5bp、SRF 動用 0（2026-07-16／17）`monetary.repo_stress_srf`；MOVE 70.88（2026-07-17）`structural.treasury_basis_trade`；銀行對 NBFI 放款 $2.00T 持平 `structural.nbfi_bank_loans`。
- [R2] 算力需求端仍然強勁：伺服器 DRAM 3Q26 合約價 +13–18% QoQ（2026-07-03），沒有 order digestion 訊號 `ai.compute_supply_demand`。
- [整體] 情緒並不亢奮：CNN Fear & Greed 37（Fear，2026-07-17）`retail.fear_greed`；Cboe equity put/call 0.73（2026-07-17），未見 call 偏重 `speculation.equity_put_call`。
- [整體] Base rate：任意 182 天窗口內 R1–R3 都不成立才是常態；目前看到的是脆弱度高（估值、槓桿），而不是已經在進行中的破裂路徑；S&P 500 仍比 200 日均線高 6.73%（2026-07-17），趨勢沒有破壞 `valuation.sp500_trend`。

## 與前期比較

前次結論：無前次預測（report-2026-07-16 為舊格式評分報告）

前次是舊格式評分報告，不轉換成 yes/no；flip_evidence 為空。2026-07-16 以來的主要變化：

- NASDAQ-100 由 29,025.77 跌到 28,592.66，S&P 500 跌 1.01%（7,533.77 → 7,457.69），VIX 由 16.73 升到 18.77，MOVE 由 68.16 升到 70.88。
- 10Y：DGS10 4.57%、DFII10 2.35% 都沒有新觀測（stale：DGS10、DFII10）；T10YIE 上升 2bp 到 2.24%。三條腿的視窗不一致，判讀：不可判（視窗不一致）。10Y 期限溢價（term premium）0.7788%（2026-07-10，Kim-Wright），trailing 7 日 +4.7bp。
- AI 信用定價分歧（Oracle／CoreWeave CDS）是 2026-07-16 的新資料，但仍屬利差層級，沒有出現 R3 事件。

## 資料缺漏與不確定性

本次無 FETCH FAILED 來源

以下來源標為 ✗ NOT DISCLOSED（搜尋完成但沒有合格的當期披露）：valuation.analyst_tp_decomposition、retail.social_sentiment、institutional.bofa_jpm_survey、ai.token_growth、ai.openai_anthropic_revenue（最近一次披露在 2026-05-15，屬前一季，不算當季披露；其數字只作為 revenue-to-capex gap 的沿用組件）、ai.customer_concentration_rpo、ai.hyperscaler_financing_mix（quarterly_state 與 event_scan 都沒有披露）、ai.depreciation_life、ai.capital_cycle（兩個組件都沒有披露）、structural.global_leveraged_approvals、structural.ai_infrastructure_debt。其中 structural.ai_infrastructure_debt 與 ai.hyperscaler_financing_mix 的缺漏會直接影響 R3：如果有未被發現的大型再融資困難，答案可能改變，所以這是本次判斷最大的資料盲點。

資料品質注意事項：
- speculation.insider_form4 雖記為 0 件，但 SEC EDGAR egress 受限，一手 Form 4 URL 無法取得；這只影響情緒佐證，不影響答案。
- 部分 snapshot 的資料日期偏舊：Mag 7 加權 P/E（2026-05-15）、RSP vs SPY（2026-06-10）、0DTE 佔比（2026-02-28）。都只作為背景，不影響答案。
- structural.treasury_basis_trade 的搜尋結果記為三個 script 組件 fetch_failed，但 macro artifact 顯示 cftc_lev_funds、move_index、ofr_repo 都是 status ok。本次以 artifact 為準，記為 ✓ API。

主要不確定性：
1. Q2 財報季（7 月底至 8 月初，具體日期本次未取得）：如果兩家以上 hyperscaler 下修 capex，或 AI 營收指引讓市場失望，會同時推向 R1 與 R2 的 yes 方向。
2. CoreWeave 等 neocloud 的再融資：CDS ≈665bp 若繼續走闊並伴隨再融資失敗，是最可能把答案推向 yes 的路徑（R3 可能再引發 R1）。
3. 私募信貸贖回壓力是否擴散：如果 Q3 有更多 BDC 出現 gate proration / breach 或 net inflow→outflow flip，AI infrastructure debt financing 的再融資管道會收緊，推向 yes。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | sp500_trend latest（S&P 500 收盤） | 7457.69 | FRED API (series_id=SP500) sp500_trend | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct（距 200 日均線 %） | 6.73 | FRED API (series_id=SP500) sp500_trend | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct（距 52 週均線 %） | 8.42 | FRED API (series_id=SP500) sp500_trend | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct（較前次基準 %） | -1.01 | FRED API (series_id=SP500) sp500_trend | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown latest（最新收盤） | 28592.66 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown high（252 日最高收盤） | 30660.6 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-06-02 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown drawdown_pct（距高點回撤 %） | 6.74 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.ndx_drawdown | ndx_drawdown r1_threshold_level（R1 門檻水位） | 22995.45 | FRED API (series_id=NASDAQ100) ndx_drawdown | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest（2026Q1 觀測期，家庭股票配置 %） | 45.76 | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARU latest（上限 %） | 3.75 | FRED API (series_id=DFEDTARU) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.fed_funds | DFEDTARL latest（下限 %） | 3.5 | FRED API (series_id=DFEDTARL) | 2026-07-19 | 2026-07-20T09:30:00+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest（%） | 2.71 | FRED API (series_id=BAMLH0A0HYM2) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest（%） | 0.78 | FRED API (series_id=BAMLC0A0CM) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dgs10 | DGS10 latest（%，無新觀測） | 4.57 | FRED API (series_id=DGS10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.dfii10 | DFII10 latest（%，無新觀測） | 2.35 | FRED API (series_id=DFII10) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE latest（%） | 2.24 | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.t10yie | T10YIE delta_bps | 2.0 | FRED API (series_id=T10YIE) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.wti | DCOILWTICO latest（USD） | 79.2 | FRED API (series_id=DCOILWTICO) | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct（2026-06 月資料，%） | 3.46 | FRED API (series_id=CPIAUCSL) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| monetary.t5yifr | T5YIFR latest（%） | 2.21 | FRED API (series_id=T5YIFR) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 latest（%，Kim-Wright） | 0.7788 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.term_premium | THREEFYTP10 delta_bps（trailing 7 日） | 4.7 | FRED API (series_id=THREEFYTP10) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR latest（%） | 3.62 | FRED API (series_id=SOFR) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR99 latest（%） | 3.7 | FRED API (series_id=SOFR99) | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB latest（%） | 3.65 | FRED API (series_id=IORB) | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest（SRF 動用，十億美元） | 0.0 | FRED API (series_id=RPONTTLD) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| monetary.repo_stress_srf | repo_stress sofr_iorb_bps（SOFR−IORB，同日 2026-07-16） | −3.0 | FRED API (series_id=SOFR, IORB) repo_stress | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| monetary.walcl | WALCL latest | 6,743,028（$6.74T，百萬美元） | FRED API (series_id=WALCL) | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,970,516（€5.97T，百萬歐元） | FRED API (series_id=ECBASSETSW) | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,395,509（¥639.55T，億日圓） | FRED API (series_id=JPNASSETS) | 2026-06-01 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 18.77 | FRED API (series_id=VIXCLS) | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix（as_of；base_date 2026-07-10，window_days 7，comove=false） | 18.77 | FRED API vix_spx_comove | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix_chg_pct（%） | 24.88 | FRED API vix_spx_comove | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.vix_spx_comove | vix_spx_comove sp500_chg_pct（%） | -1.55 | FRED API vix_spx_comove | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2004.0237（$2.00T，十億美元） | FRED API (series_id=LNFACBW027SBOG) | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds net_contracts（六合約槓桿基金淨部位，口） | -7,562,874 | CFTC TFF futures-only cftc_lev_funds | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | cftc_lev_funds delta_4w（口） | -78,139 | CFTC TFF futures-only cftc_lev_funds | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | move_index latest | 70.88 | Yahoo Finance chart API (^MOVE) move_index | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.treasury_basis_trade | ofr_repo transaction_volume_usd_bn（tri-party repo transaction volume，十億美元） | 2342.6 | OFR STFM (REPO-TRIV1_TV_TOT-P) ofr_repo | 2026-07-17 | 2026-07-20T09:30:00+08:00 |

### Coverage

| source_id | 類別 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E and AI leader P/S | MarketXLS WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-05-15，偏舊） |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 WebSearch（90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ndx_drawdown | 估值｜NASDAQ-100 drawdown from 52-week high | scripts/fetch_macro.py（FRED NASDAQ100） | ✓ API |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場 WebSearch（14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-06-10） |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.margin_debt | 散戶｜Margin Debt: FINRA | FINRA／Advisor Perspectives WebSearch（stock-of-state） | ✓ SEARCH-VERIFIED |
| retail.aaii | 散戶｜Retail survey: AAII | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB／cashtag WebSearch（7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | 散戶｜Household equity allocation | scripts/fetch_macro.py（FRED） | ✓ API |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim／ycharts [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM | WebSearch | ✗ NOT DISCLOSED |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED | scripts/fetch_macro.py（DFEDTARU、DFEDTARL） | ✓ API |
| monetary.hy_oas | 貨幣｜High Yield OAS | scripts/fetch_macro.py（BAMLH0A0HYM2） | ✓ API |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | scripts/fetch_macro.py（BAMLC0A0CM） | ✓ API |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | scripts/fetch_macro.py（DGS10） | ✓ API |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield | scripts/fetch_macro.py（DFII10） | ✓ API |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | scripts/fetch_macro.py（T10YIE，FRED 直取） | ✓ API |
| monetary.wti | 貨幣｜WTI crude oil price | scripts/fetch_macro.py（DCOILWTICO） | ✓ API |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED | scripts/fetch_macro.py（CPIAUCSL yoy_pct） | ✓ API |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | scripts/fetch_macro.py（T5YIFR） | ✓ API |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py（THREEFYTP10） | ✓ API |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py（SOFR ok、SOFR99 ok、IORB ok、RPONTTLD ok） | ✓ API |
| monetary.treasury_auctions | 貨幣｜美債標售需求（auction tail / bid-to-cover） | WebSearch（14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED | scripts/fetch_macro.py（WALCL） | ✓ API |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | scripts/fetch_macro.py（ECBASSETSW ok、JPNASSETS ok） | ✓ API |
| monetary.pboc | 貨幣｜PBoC aggregate financing | Bloomberg WebSearch | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]（30d） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報 WebSearch（stock-of-state，沿用 Q1 2026） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI｜AI token volume growth rate | WebSearch | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch／The Information WebSearch | ✗ NOT DISCLOSED（最近披露 2026-05-15，非當季） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration | 財報電話 [primary: SEARCH] | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構（capex vs FCF / 發債） | 季報＋30 日事件 WebSearch；quarterly_state 與 event_scan 均無披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口（revenue-to-capex gap） | 組合披露 [primary: SEARCH]（沿用組件） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K／10-Q [primary: SEARCH]（30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | AI｜資本週期階段（capital cycle stage） | 供需增速＋進出場事件 WebSearch；兩組件均無披露 | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days（+AI rename／SPAC） | WebSearch（7d） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis WebSearch | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz／Benzinga [primary: SEARCH]（7d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | 具名報導 WebSearch（30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership | SEC EDGAR／openinsider（14d；EDGAR egress 受限） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | WebSearch [primary: SEARCH] | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire／ETF.com WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX／TWSE／JPX／ESMA WebSearch（7d） | ✗ NOT DISCLOSED |
| structural.zero_dte | 結構｜0DTE option volume | Cboe WebSearch | ✓ SEARCH-VERIFIED（資料日 2026-02-28，偏舊） |
| structural.options_volume | 結構｜Options total volume | theocc.com WebSearch | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe／AInvest WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | scripts/fetch_macro.py（VIXCLS ok、vix_spx_comove ok） | ✓ API |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 retail.margin_debt | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]（30d） | ✗ NOT DISCLOSED |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | scripts/fetch_macro.py（LNFACBW027SBOG） | ✓ API |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | scripts/fetch_macro.py（cftc_lev_funds ok、move_index ok、ofr_repo ok；aggregation any） | ✓ API |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.08 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio （multpl；原定 multpl／gurufocus） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 41.52 | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe （multpl） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E ≈40 trailing | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026 （MarketXLS） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS ≈198bp 創紀錄；CoreWeave ≈665bp | Oracle CoreWeave CDS spread widening July 2026 | https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/ （Real Investment Advice） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| breadth.rsp_spy | RSP +10.68% vs SPY +7.47% YTD | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ （24/7 Wall St.） | 2026-06-10 | 2026-07-20T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 36.40% | S&P 500 top 10 concentration percent 2026 | https://ahasignals.com/sp500-concentration-risk/ （AHA Signals；原定 State Street SPDR 持股） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| breadth.advance_decline | NYSE 07-17 下跌約 2 倍於上漲；NH 241／NL 166 | NYSE advance decline breadth July 17 2026 | https://money.usnews.com/investing/news/articles/2026-07-17/wall-st-futures-fall-as-chip-selloff-gathers-pace-netflix-tumbles （US News／Reuters） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（Fear） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed （MacroMicro；原定 cnn.com） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| retail.margin_debt | margin debt（2026-05 月資料）$1.416T、+53.7% YoY | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives；原定 FINRA） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |
| retail.aaii | AAII Bull 44.9% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey （AAII） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number （YCharts；原定 naaim.org） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 BTC 2.59、小幅 tail | US Treasury 10Y auction July 2026 bid to cover | https://cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/ （Crypto Briefing；原定 Reuters／TreasuryDirect） | 2026-07-08 | 2026-07-20T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 維持利率 ≈86.7% | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch （CryptoRank；原定 CME FedWatch） | 2026-07-18 | 2026-07-20T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance （Bloomberg） | 2026-07-14 | 2026-07-20T09:30:00+08:00 |
| monetary.private_credit_liquidity | Blue Owl OCIC Q2 redemption-request ratio 18.8%，於 5% quarterly redemption cap 按比例撥付（gate proration / breach） | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://whbl.com/2026/07/02/blue-owl-keeps-withdrawal-limits-even-as-redemption-pressure-modestly-eases/ （WHBL／Reuters） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| ai.hyperscaler_capex | 四家 hyperscaler 2026 capex 合計 ≈$700B、仍上修（Q1 2026 財報季） | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html （Yahoo Finance） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約價 +13–18% QoQ | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html （TrendForce） | 2026-07-03 | 2026-07-20T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex ≈$700B vs AI 終端營收低百億級（Anthropic ≈$47B／OpenAI ≈$25B run-rate；分母 top-4） | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue （Epoch AI） | 2026-05-15 | 2026-07-20T09:30:00+08:00 |
| speculation.ai_rename_spac | EVTV→Azio AI（AZIO）改名，1 件 | AI rename ticker change July 2026 Azio EVTV | https://www.businesswire.com/news/home/20260710628386/en/Azio-AI-Holdings-Inc.-Nasdaq-EVTV-to-Begin-Trading-Under-New-Ticker-Symbol-AZIO-Completing-Corporate-Rebrand （Business Wire） | 2026-07-13 | 2026-07-20T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD ≈200 檔 IPO、募資 $141.2B | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/ （StockAnalysis） | 2026-07-16 | 2026-07-20T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot 0 件 | microcap 100% single day quantum AI moonshot July 2026 | Finviz／Benzinga／StockTitan movers screener（已檢查） | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 投資人會議，估值 $965B，可能 10 月掛牌 | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html （CNBC） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 cluster 0 件（EDGAR egress 受限） | insider Form 4 cluster AI leaders July 2026 openinsider | SEC EDGAR／openinsider（已檢查；一手 URL 無法取得） | 2026-07-20 | 2026-07-20T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.73（日讀數） | Cboe equity put call ratio July 2026 | https://www.cboe.com/markets/us/options/market-statistics/daily/ （Cboe） | 2026-07-17 | 2026-07-20T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM ≈$198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ （Crypto Briefing；原定 etf.com／ETFGI） | 2026-07-10 | 2026-07-20T09:30:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x 單一個股 ETF（GOOGL／AMZN／META／AAPL） | single-stock leveraged ETF launch July 2026 Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html （GlobeNewswire） | 2026-07-07 | 2026-07-20T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 成交 ≈63% | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/ （Cboe） | 2026-02-28 | 2026-07-20T09:30:00+08:00 |
| structural.options_volume | OCC 2026-06 月成交 1,603,491,559 口、+45% YoY | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report （OCC） | 2026-07-02 | 2026-07-20T09:30:00+08:00 |
| structural.cross_asset_derivatives | Cboe SKEW 145.13、VIX ≈16.5 contango | VIX term structure SKEW July 2026 | https://www.ainvest.com/news/0dte-volatility-drives-market-strategies-2026-2602/ （AInvest） | 2026-07-15 | 2026-07-20T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt（2026-05 月資料）$1.416T、+53.7% YoY（交叉引用） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra （Advisor Perspectives） | 2026-05-31 | 2026-07-20T09:30:00+08:00 |

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

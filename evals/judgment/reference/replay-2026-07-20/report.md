# 2026-07-20 市場泡沫風險評估報告
> 報告日期：2026-07-20；執行日：2026-07-20 Asia/Taipei；ISO 週次：2026-W30；前次基準：report-2026-07-16（4天前）

**總評**：總分 64【警戒】（Δ 0）；扳機狀態：已擊發；最貼近錨點：1997 早期建設（50%）。

## §1 六維度風險條圖
| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▱▱▱ | 79 | 79 | 0 |
| 市場廣度 | ▰▰▰▱▱▱▱▱▱▱ | 30 | 30 | 0 |
| 投機行為 | ▰▰▰▰▰▱▱▱▱▱ | 58 | 58 | 0 |
| 散戶情緒 | ▰▰▰▰▰▱▱▱▱▱ | 50 | 50 | 0 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▰▱▱▱ | 75 | 75 | 0 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 77 | 77 | 0 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **64【警戒】** | 64 | 0 |

## §2 歷史錨點相似度
| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1973/1 Nifty Fifty 頂 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 1997 早期建設 | 50% | ▰▰▰▰▰▱▱▱▱▱ | ◀ 最貼近 |
| 1998 LTCM 衝擊 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 2000/3 頂點 | 15% | ▰▱▱▱▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |

## §3 三角訊號
| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,457.69 | ▼ −1.01%（前次 ≈7,533.77） |
| WTI 原油 | $79.2 /bbl | 持平 0%（無新觀測，前次 ≈$79.2） |
| 10Y Treasury | 4.57% | 持平 0 bps（無新觀測，前次 ≈4.57%） |

**三者狀態**：穩定共存——三者本次多為小幅／持平、未見同向拉伸；S&P 略回、WTI 與 10Y 皆無新觀測（持平），S&P `dev200_pct` ≈+6.73%（< +10% 拉伸門檻）。惟資產面平靜與非銀融資扳機（私募信貸 gate）並存，須分開判讀。
- 股市：≈7,457.69（S&P 500，2026-07-17 收）；較前次 ▼ −1.01%（前次 ≈7,533.77）；距 200 日均線 +6.73%、距 52 週均線 +8.42%——價格延伸較前次回落、非急拉。
- WTI 原油：≈$79.2/bbl（2026-07-13，無新觀測）；較前次 持平 0%（前次 ≈$79.2）。
- 10Y 殖利率：4.57%（2026-07-16，無新觀測）；較前次 持平 0 bps（前次 ≈4.57%）；主要驅動：三腿視窗不一致（driver=unknown）。
**格局轉變**：前次格局＝分歧（讀自 report-2026-07-16 的 `regime`）→ 本次格局＝穩定共存；由 10Y 反向重定價的分歧回到三者小幅／持平的穩定共存。
**10Y 成因拆解**：拆的是週變動（bps）、非水位（`ΔDGS10 ≈ ΔDFII10 + ΔT10YIE`）；三腿視窗不一致（`decomposition.driver=unknown`——ΔT10YIE 取自較新視窗、恆等式不跨視窗成立），判定 不可判（視窗不一致）；三腿實際 signed 週變動如下：
- ΔDGS10 名目殖利率週變動：0 bps
- ΔDFII10 實質殖利率週變動：0 bps
- ΔT10YIE 損益平衡通膨週變動：+2 bps
- 觀測新鮮度：部分未更新（stale_series=DGS10,DFII10）
- 判定：不可判（視窗不一致）
**扳機鏈**：A 通膨鏈（油 → 通膨預期 → Fed 受限 → refinancing 成本）本週未加速——WTI 持平（≈$79.2，無新觀測）、實現通膨續處高位但未再上行：[monetary.cpi_yoy] CPIAUCSL yoy_pct=3.46 data_date=2026-06-01（6 月）、5y5y forward [monetary.t5yifr] T5YIFR latest=2.21 delta_bps=1 data_date=2026-07-17（微升 +1 bps）；CME FedWatch 7/29 會議 ≈86.7% 持平（2026-07-18），Fed 仍受 3.46% 通膨與財政供給牽制，Fed put 可得性中性；無當期電價／能源瓶頸新報導。B 槓桿鏈（衝擊：財政風險再定價 → NBFI 去槓桿 → margin spiral → 國債市場失序 → 官方市場功能回應）乾柴堆積但未點火——衝擊節點：10Y 期限溢價 THREEFYTP10 ≈0.7788%（序列自身 trailing ≈7d +4.7 bps，溫和上行）、7/8 10Y 標售 bid-to-cover 2.59 僅小幅 tail，財政再定價壓力溫和；NBFI 節點：script `cftc_lev_funds`／`move_index`／`ofr_repo` 本次 fetch_failed，WebSearch 亦無視窗內（7 日）MOVE／基差新值（最新可稽 MOVE ≈70 為 06-23、逾窗），無基差／swap-spread 平倉報導；官方回應節點：`repo_stress` SOFR−IORB −3 bps、SOFR99−IORB +5 bps、SRF 動用 $0（無失序）。real-rate 主導的異常 10Y 上行本週不存在（10Y 週 0 bps、無新觀測）。本鏈證據 best-effort，本週無基差交易槓桿新積累／釋放事件。
**扳機理由**：private_credit_gate
⚠ **結論**：扳機狀態：已擊發——本次續命中「私募信貸 gate proration / breach」：Q2 2026（季末 6/30）多檔非交易 BDC／私募信貸區間基金贖回需求遠超 5% 季度上限並比例撥付（Blue Owl OCIC 贖回需求 ≈18.8% NAV 於 5% 上限比例撥付、Blackstone BCRED ≈10% 撥付率 ≈50%、Golub GCRED ≈8.5% 撥付率 ≈59%；BofA 定調 Q2 為贖回高峰，詳 §D5／本次新增訊號），此為 1998 LTCM 型「融資扳機」特徵——非銀信用先於公開 mark-to-market 利差（HY 2.71%／IG 0.78% 仍史窄）出現一階壓力。三者配置歷史意義：估值＋槓桿＝崩跌位能，融資緊縮＝時點扳機；本週三角資產面轉為穩定共存（S&P 小回、油與 10Y 無新觀測），惟公開利差自滿與非銀融資扳機仍並存（自滿側 froth 與扳機側 financing 壓力同框），槓桿鏈 B 未點火，失序仍屬結構化產品閘門層級、非國債市場層級。

## 六維度評分

### 1. 估值溢價 — 79（weight 22%，Δ 0）
- **S&P 500 trailing P/E** ≈**32.08**（2026-07-17，https://www.multpl.com/s-p-500-pe-ratio，source_ids=valuation.sp500_pe_cape）——較前次 32.59 微降（隨指數週回 ≈−1%），仍近歷史高位。
- **Shiller CAPE** ≈**41.52**（2026-07-17，https://www.multpl.com/shiller-pe，source_ids=valuation.sp500_pe_cape）——較前次 42.18 微降，仍逼近歷史高（≈44）。
- **Excess CAPE Yield（ECY）** ≈**0.06%**（`1/41.52 − 2.35/100`，derived 自 CAPE 41.52 與 DFII10 2.35%，2026-07-17，source_ids=valuation.sp500_pe_cape）——接近 0，屬 1929／2000 級別股相對債極貴訊號（confirmation，不主計分）。
- **Mag 7 加權 P/E** trailing ≈**40**（2026-05-15，https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026，source_ids=valuation.mag7_multiples）——絕對高，對 S&P 溢價為近十年較窄區（stock-of-state 沿用）。
- **價格趨勢偏離（Farrell #1/#2/#4）** S&P 距 200 日均線 **+6.73%**、距 52 週均線 +8.42%（`sp500_trend`，2026-07-17，FRED SP500，source_ids=valuation.sp500_trend）——較前次 +8.51% 明顯回落，價格延伸壓力減輕，與 P/E／CAPE 互補、不重複計分。
- **AI capex 現實檢核**：hyperscaler 2026 capex 指引合計 ≈**$700B**（仍在上修；Meta FY26 上修至 $125–145B）（2026-05-15，https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html，source_ids=ai.hyperscaler_capex）——基本面敘事仍撐估值。
- **AI compute 供需現實檢核**：伺服器 DRAM 3Q26 合約 **+13–18% QoQ**（TrendForce，2026-07-03，https://www.trendforce.com/presscenter/news/20260703-13134.html，source_ids=ai.compute_supply_demand）、HBM 定價力續強——供給仍被合約與 token 需求吸收，缺口未成形、非惡化確認。
- **AI 營收對 capex 缺口現實檢核**：分母年化 capex ≈**$700B**（分母：top-4＋Oracle）vs 分子已披露 AI 終端年化營收（Anthropic ≈$47B、OpenAI ≈$25B run-rate）量級缺口仍大且 capex 續升（2026-05-15，https://epoch.ai/data-insights/anthropic-openai-revenue，source_ids=ai.revenue_capex_gap）——回本假設後移，屬估值風險上修的質化依據（缺口未收斂）。
- **AI 信用定價分歧（equity-vs-credit schism）**：Oracle 5yr CDS ≈**198 bp**（歷史紀錄新高、走闊）、CoreWeave 5yr CDS ≈665 bp vs CDX.NA.IG 基準數十 bp（2026-07-16，https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/，source_ids=valuation.ai_credit_schism）——AI 發行人利差為 IG 基準數倍且續走闊、股價未跟＝後期訊號側（confirmation，不主計分）。
- **TP-upgrade phase signal**：過去 90 日同季內無新披露 EPS-vs-multiple 分解的具名賣方升評（Q3 財報季尚早）（✗ NOT DISCLOSED，source_ids=valuation.analyst_tp_decomposition，不納入計分）。
- **折舊年限變動（盈餘品質）**：過去 30 日無新 10-K／10-Q 折舊年限或殘值假設變更披露（財報季未啟）（✗ NOT DISCLOSED，source_ids=ai.depreciation_life，不納入計分）。
- **backlog 重複計算風險（RPO double-counting）**：本次無新客戶集中度／RPO 一手披露（✗ NOT DISCLOSED，source_ids=ai.customer_concentration_rpo，不納入計分）。
- **Hyperscaler 融資結構＋資本週期**：本次無新可組合的融資結構事件掃描與週期增速披露（財報季未啟、30 日內無 hyperscaler 自身發債事件）（✗ NOT DISCLOSED，source_ids=ai.hyperscaler_financing_mix,ai.capital_cycle，不納入計分）。
**結論**：分數維持 **79**（rubric 高位）。P/E 32.08／CAPE 41.52 隨指數微降、趨勢偏離由 +8.51% 回落至 +6.73%（價格延伸壓力減輕），但 Mag7 高檔、capex 續升、ECY 近 0 與 AI 信用分歧（Oracle CDS 紀錄新高）同框對沖——正負相抵，較前次持平。

### 2. 市場廣度 — 30（weight 13%，Δ 0）
- **RSP（等權）vs SPY（市值權）YTD**：RSP ≈**+10.68%** vs SPY ≈+7.47%（2026-06-10，https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/，source_ids=breadth.rsp_spy）——等權領先市值權 ≈+3.2 pp，廣度為轉寬／健康方向、非背離。
- **Top-10 集中度**：≈**36.40%**（2026-07-02，State Street SPDR 持股，https://ahasignals.com/sp500-concentration-risk/，source_ids=breadth.top10_concentration）——絕對偏高但較年底 ≈41% 已回落。
- **Advance/Decline 與新高/新低**：2026-07-17（晶片股回落的 risk-off 日）NYSE 下跌約為上漲 2 倍、新高 **241** vs 新低 166（新高仍 > 新低）（https://money.usnews.com/investing/news/articles/2026-07-17/wall-st-futures-fall-as-chip-selloff-gathers-pace-netflix-tumbles，source_ids=breadth.advance_decline）——單日轉弱但新高/新低仍正、中期廣度未破壞。
**結論**：分數維持 **30**（rubric 21–40 偏健康端）。等權大幅領先市值權（+3.2 pp）＋新高 > 新低＝廣度健康／轉寬，唯 Top-10 ≈36.4% 仍偏高、07-17 單日轉弱為殘餘風險；淨評與前次持平。

### 3. 投機行為 — 58（weight 18%，Δ 0）
- **+AI 改名／SPAC**：本週 **1 件**具名 +AI 改名——Envirotech Vehicles（EVTV）更名 Azio AI Holdings、2026-07-13 起以新代號「AZIO」交易，轉型 AI 資料中心／GPU 運算並引 $27.9M AI 託管合約（https://www.businesswire.com/news/home/20260710628386/en/Azio-AI-Holdings-Inc.-Nasdaq-EVTV-to-Begin-Trading-Under-New-Ticker-Symbol-AZIO-Completing-Corporate-Rebrand，source_ids=speculation.ai_rename_spac）；IQM Quantum de-SPAC（07-01）落 7 日窗外、作背景。無無營收 IPO 暴衝。
- **IPO 熱度**：2026 YTD ≈**200** 檔（+6.95% YoY）、募資 ≈$141.2B（含 SK Hynix $26.5B 交叉掛牌，逼近 2021 紀錄 $142.4B）（2026-07-16，https://stockanalysis.com/ipos/2026/，source_ids=speculation.ipo_heat）——市場活躍、秩序尚可，first-day pop／無營收佔比精確值未取得。
- **Microcap thematic moonshots**：本週 **0 件**合格（<$1B 市值、單日 ≥100%、堆疊 2+ 熱主題＋弱基本面；2026-07-20 螢幕）——✓ SEARCH-VERIFIED（0 件）（source_ids=speculation.microcap_moonshots）；本週最大漲幅為單一題材生技（CRNX、FBRX），非多主題堆疊對弱基本面，皆不合格。
- **Upcoming AI mega-IPO pipeline**：**Anthropic 進行 IPO 投資人會議**（估值 ≈$965B、可能 10 月掛牌），為 30 日內具名報導的巨型 AI IPO pipeline 活躍訊號（2026-07-15，https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html，source_ids=speculation.upcoming_ai_ipos）——液性抽離風險上升（本項計分判讀為投機 pipeline 升溫的質化依據）。
- **Insider selling clusters**：required 螢幕已執行（2026-07-20 螢幕）；14 日內無合格「Form 4 cluster」附 SEC EDGAR filing URL（Jensen Huang 07-08–07-10 之 10b5-1 單一計畫性賣出 ≈$36.4M 為單一內部人、非 cluster，且一手 EDGAR URL 受 403 無法取得）——**0 件合格**（✓ SEARCH-VERIFIED（0 件），source_ids=speculation.insider_form4）。
- **Cboe equity-only put/call**：≈**0.73**（2026-07-17，https://www.cboe.com/markets/us/options/market-statistics/daily/，source_ids=speculation.equity_put_call）——中性偏樂觀、較前次 0.62 略升（call 偏重減輕）、未破 0.50 極端（confirmation，不主計分）。
- **社交情緒代理**：本週（07-13–07-20）無具名主導迷因軋空事件（WEN 軋空熱潮於 6 月底／7 月初高峰、已落窗外）（✗ NOT DISCLOSED，source_ids=retail.social_sentiment，不納入計分）。
**結論**：分數維持 **58**（rubric 41–60「投機升溫」）。1 件 +AI 改名（Azio）、Anthropic $965B IPO 進入投資人會議為 pipeline 升溫，惟 moonshot 0、insider 無合格 cluster、put/call 0.73 未極端、社群無主導軋空——投機體感與前次持平。

### 4. 散戶情緒 — 50（weight 12%，Δ 0）
- **CNN Fear & Greed**：≈**37「Fear」**（2026-07-17，經 en.macromicro.me 鏡像；cnn.com 直抓 WAF 403，https://en.macromicro.me/charts/50108/cnn-fear-and-greed，source_ids=retail.fear_greed）——較前次 46「Neutral」回落至恐懼區、散戶亢奮降溫。
- **Margin Debt**：**$1.416T、YoY +53.7%、MoM +8.5%（2026-05-31，記錄高）**（https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra，source_ids=retail.margin_debt）——月頻 stock-of-state，6 月數未發布、沿用 5 月；YoY +53.7% 屬 1999／2007／2021 頂部級別警訊。
- **AAII 散戶調查**：**Bull 44.9%**（2026-07-16，較前次 36.3% 明顯轉多）（https://www.aaii.com/sentimentsurvey，source_ids=retail.aaii）——多方升破長均 37.5%、樂觀回升。
- **家庭持股佔金融資產比**：**45.76%**（`BOGZ1FL153064486Q`，2026-01-01 資料日，FRED，source_ids=retail.household_equity_allocation）——歷史高位、後續加碼空間有限（Farrell #5，季頻沿用、不計週 Δ）。
- **NAAIM Exposure Index**：**95.64**（2026-07-15，較前次 82.95 上升，https://ycharts.com/indicators/naaim_number，source_ids=retail.naaim）——主動經理人曝險接近滿倉＝擁擠多頭（Farrell #9，confirmation cross-check，不主計分）。
**結論**：分數維持 **50**（rubric 41–60 下緣）。CNN F&G 由 Neutral 回落至 Fear（散戶亢奮降溫）與 AAII 轉多（Bull 44.9%）、NAAIM 近滿倉（擁擠上升）方向相抵；margin debt 仍頂部級別、家庭持股高位——淨評與前次持平。

### 5. 貨幣與信貸環境 — 75（weight 20%，Δ 0）
- **Fed funds rate**：目標區間 **3.50–3.75%**（`DFEDTARU` 3.75%／`DFEDTARL` 3.50%，2026-07-19，FRED，source_ids=monetary.fed_funds）——無變動。
- **市場隱含路徑（CME FedWatch，best-effort）**：7/29 會議 ≈**86.7%** 持平（2026-07-18，https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch，source_ids=monetary.fedwatch）——本次會議幾無降息定價、Fed 寬鬆空間受限（缺值不調分）。
- **Realized inflation vs expectations**：CPI YoY **3.46%**（`CPIAUCSL`，2026-06-01，FRED，source_ids=monetary.cpi_yoy）仍高於 2% 目標、5y5y forward **2.21%**（`T5YIFR`，2026-07-17，週 Δ +1 bps，FRED，source_ids=monetary.t5yifr）微升——通膨黏著、Fed 約束未鬆。
- **10Y 期限溢價（term premium）**：`THREEFYTP10` **0.7788%**（2026-07-10，Kim-Wright 三因子模型，序列自身 trailing ≈7d +4.7 bps，FRED，source_ids=monetary.term_premium）——財政風險再定價溫和上行、未急升。
- **repo 資金壓力（SOFR−IORB）與 SRF 動用**：`repo_stress`——SOFR **3.62%**（2026-07-16，無新觀測）、IORB 3.65%（2026-07-20）、SOFR−IORB **−3 bps**；SOFR99 3.70%、SOFR99−IORB +5 bps；RPONTTLD／SRF 動用 **$0**（2026-07-17，FRED SOFR/SOFR99/IORB/RPONTTLD，source_ids=monetary.repo_stress_srf）——secured-funding 無壓力、SRF 未動用。
- **美債標售需求（auction，best-effort）**：7/8 10Y 重開標 bid-to-cover **2.59**、僅小幅 tail（stop ≈0.6 bp 高於 WI 4.586%，需求穩健）（2026-07-08，https://cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/，source_ids=monetary.treasury_auctions）——無明顯 tail、財政供給壓力事件本週不成立（confirmation；缺值不調分）。
- **HY OAS**：**2.71%**（`BAMLH0A0HYM2`，2026-07-16，無新觀測、週 Δ 0 bps，FRED，source_ids=monetary.hy_oas）——接近循環低、極窄、自滿側訊號（連續走闊 streak 歸零）。
- **IG OAS**：**0.78%**（`BAMLC0A0CM`，2026-07-16，無新觀測、週 Δ 0 bp，FRED，source_ids=monetary.ig_oas）——史窄、信用自滿。
- **10Y nominal 週變動拆解**：ΔDGS10 0 bps ≈ ΔDFII10 0 bps ＋ ΔT10YIE +2 bps（三腿視窗不一致、driver=unknown）；`DGS10` **4.57%**（2026-07-16，無新觀測，FRED，source_ids=monetary.dgs10）、`DFII10` **2.35%**（2026-07-16，source_ids=monetary.dfii10）、`T10YIE` **2.24%**（2026-07-17，source_ids=monetary.t10yie）——殖利率持平、估值折現／再融資壓力無新增（詳 §3）。
- **WTI 原油**：**$79.2**/bbl（`DCOILWTICO`，2026-07-13，無新觀測，FRED，source_ids=monetary.wti）——持平，A 通膨鏈油價端無新推力。
- **Fed balance sheet**：≈$6.74T（原始 **6,743,028** 百萬美元，2026-07-15，無新觀測，FRED WALCL，source_ids=monetary.walcl）——量化緊縮步調持平。
- **全球央行流動性（ECB）**：ECB ≈€5.97T（原始 **5,970,516** 百萬歐元，2026-07-10，無新觀測，FRED ECBASSETSW，source_ids=monetary.ecb_boj）——持平。
- **全球央行流動性（BOJ）**：BOJ ≈¥639.55T（原始 **6,395,509** 億日圓，2026-06-01，無新觀測，FRED JPNASSETS，source_ids=monetary.ecb_boj）——持平。
- **PBoC 流動性操作**：人行 2026-07-14 以 6 個月買斷式逆回購淨投放 ≈**1.4** 兆元（≈$207B、該工具紀錄量，平滑稅期與債券發行）（https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance，source_ids=monetary.pboc）——中國端流動性偏寬（confirmation）。
- **私募信貸贖回壓力（扳機側，event-driven）**：Q2 2026（季末 6/30）多檔非交易 BDC／私募信貸區間基金贖回需求遠超 5% 季度上限並比例撥付——Blue Owl OCIC 贖回需求 ≈**18.8%** NAV 於 5% 上限比例撥付（2026-07-02，https://whbl.com/2026/07/02/blue-owl-keeps-withdrawal-limits-even-as-redemption-pressure-modestly-eases/，source_ids=monetary.private_credit_liquidity），Blackstone BCRED ≈10% 撥付率 ≈50%、Golub GCRED ≈8.5% 撥付率 ≈59%，BofA 定調 Q2 為贖回高峰——多基金 redemption 上限實際觸發＝financing-cycle 緊縮已抵達非銀信用，餵入 §3 融資扳機。
**結論**：扳機側；私募信貸多基金 gate proration（Blue Owl OCIC 18.8% 比例撥付、BCRED ≈50%／Golub ≈59% 撥付）為扳機側事件，同時 HY 2.71%／IG 0.78% 史窄自滿——「自滿側 froth 與扳機側 financing 壓力同框」維持 **75**；macro 多序列持平、標售穩健、repo 無壓、CPI 黏著，故分數較前次持平、扳機側質變見「本次新增訊號」。

### 6. 結構性槓桿 — 77（weight 15%，Δ 0）
- **US 槓桿 ETF AUM**：美國槓桿 ETF 總 AUM ≈**$198B**（記錄高，TQQQ ≈$37.3B／SOXL ≈$17.3B 領先；NVDL >$4B）（2026-07-10，https://cryptobriefing.com/leveraged-etfs-record-198b-aum/，source_ids=structural.leveraged_etf_aum）——水位高。
- **US 單股槓桿 ETF 核准／發行（近 30 日）**：**續擴散**——Leverage Shares 6 檔 2x 單股（GOOGL／AMZN／META／AAPL，2026-07-07，https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html，source_ids=structural.us_single_stock_etf）、SK Hynix ADR 2x 多／空系列（ProShares／Leverage Shares／Rex，07-13 週上市）——美國單股槓桿產品擴散顯著。
- **全球（非美）槓桿產品核准（本週）**：**本週擴散訊號未觸發**——韓／台／日／歐 07-13–07-20 無新單股槓桿／反向 ETF 核准；韓國 FSC/KRX 反於 2026-07-16 起暫停新單股槓桿 ETF 上市（收緊，https://www.bloomberg.com/news/articles/2026-07-16/south-korea-to-halt-new-listings-of-single-stock-leveraged-etfs，source_ids=structural.global_leveraged_approvals，不納入計分）——未達 2+ 非美市場同週核准、rubric floor 81 未啟動（✗ NOT DISCLOSED）。
- **0DTE 佔 SPX 期權量**：≈**63%**（Cboe，2026-02-28 最新確定值、Q2 維持 >55%，https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/，source_ids=structural.zero_dte）——持續高檔。
- **Options 總量（OCC 月報）**：6 月 **1,603,491,559** 口、+45.0% YoY（2026-07-02，https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report，source_ids=structural.options_volume）——衍生品投機量創高。
- **跨資產／相關性確認**：Cboe SKEW ≈**145.13**（偏高、尾端避險付溢價）、VIX ≈16.5 期限結構 contango（前月 18.45 → 1Y 23.28）（2026-07-15，https://www.ainvest.com/news/0dte-volatility-drives-market-strategies-2026-2602/，source_ids=structural.cross_asset_derivatives）——尾端避險升溫、整體波動平靜（confirmation）。
- **Margin debt / 市值 交叉檢核**：$1.416T、YoY +53.7%（2026-05-31，見 D4，https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra，source_ids=structural.margin_debt_crosscheck）——確認零售槓桿頂部級別（confirmation，不在此重複計分）。
- **AI 基礎設施債務／vendor-financing loops**：過去 30 日無具明確窗內日期的新增 AI 資料中心／GPU 抵押債務事件（CoreWeave $8.5B DDTL 為 Q1 已收官、逾窗；產業 off-balance-sheet ≈$120B 為背景）（✗ NOT DISCLOSED，source_ids=structural.ai_infrastructure_debt，不納入計分）。
- **銀行對 NBFI 放款**：≈$2.00T（原始 **2,004.02** 億美元，2026-07-08，無新觀測，FRED LNFACBW027SBOG，source_ids=structural.nbfi_bank_loans）——bank–NBFI linkage 水位持平（confirmation，不主計分）。
- **美債基差交易槓桿（best-effort）**：script `cftc_lev_funds`／`move_index`／`ofr_repo` 本次 `fetch_failed`，WebSearch 亦無視窗內（7 日）MOVE／基差新值（最新可稽 MOVE ≈70 為 06-23、逾窗），無失序平倉報導（✗ NOT DISCLOSED，source_ids=structural.treasury_basis_trade，不納入計分）。
**結論**：分數維持 **77**（rubric 61–80）。0DTE 續 >55%、OCC 量創高、US 單股槓桿產品續擴散（Leverage Shares／SK Hynix）、槓桿 ETF AUM 記錄高＝結構性槓桿高檔；惟本月無窗內新 AI 基礎設施債務事件、全球擴散訊號未觸發（韓國反收緊）、MOVE 低波無失序——正負相抵，淨評與前次持平。

## 綜合分數

| 維度 | 權重 | 分數 | 加權分數 |
|---|---:|---:|---:|
| 估值溢價 | 22% | 79 | 17.38 |
| 市場廣度 | 13% | 30 | 3.90 |
| 投機行為 | 18% | 58 | 10.44 |
| 散戶情緒 | 12% | 50 | 6.00 |
| 貨幣與信貸環境 | 20% | 75 | 15.00 |
| 結構性槓桿 | 15% | 77 | 11.55 |
加權總分：64.27 → 64【警戒】

邊界帶：總分 64 距 警戒/高 邊界 ≤ 2 分，評分固有噪音約 ±2–3，等級判讀需保留餘地。

## 歷史泡沫週期對比

相似度計算：checklist v2

逐項對本次六維度分數、macro/current/prior state 與附錄證據重算命中；相似度 = 命中數 ÷ 特徵數 × 100，四捨五入到最近 5%。「無資料」不計入命中但仍在分母。

- 1973/1 Nifty Fifty 頂：命中 3/8 = 40%
- 1997 早期建設：命中 4/8 = 50%
- 1998 LTCM 衝擊：命中 3/8 = 40%
- 1999 晚期狂熱：命中 4/10 = 40%
- 2000/3 頂點：命中 1/8 = 15%
- 2021/12 Meme 頂：命中 2/8 = 25%

2000/3 高位回落條件：否

**1973/1 Nifty Fifty 頂 feature audit**
- 1973.1｜未命中｜source_ids=—｜估值溢價 79 < 80
- 1973.2｜未命中｜source_ids=—｜市場廣度 30 < 60
- 1973.3｜未命中｜source_ids=—｜CPI YoY 3.46% < 4%
- 1973.4｜命中｜source_ids=—｜T5YIFR 週 Δ +1 bps ≥ 0（通膨預期未回落）
- 1973.5｜未命中｜source_ids=—｜WTI 週漲幅 0%（無新觀測）< +0.5%
- 1973.6｜未命中｜source_ids=—｜decomposition.driver=unknown ≠ breakeven（三腿視窗不一致）
- 1973.7｜命中｜source_ids=—｜扳機狀態＝已擊發 ≥ 初啟
- 1973.8｜命中｜source_ids=—｜散戶情緒 50 < 55
**1997 早期建設 feature audit**
- 1997.1｜未命中｜source_ids=—｜估值溢價 79 > 74（超出 40–74 區間）
- 1997.2｜命中｜source_ids=—｜市場廣度 30 < 45
- 1997.3｜未命中｜source_ids=—｜投機行為 58 ≥ 50
- 1997.4｜命中｜source_ids=ai.hyperscaler_capex｜hyperscaler 2026 capex 指引仍上修（≈$700B）
- 1997.5｜命中｜source_ids=—｜散戶情緒 50 < 55
- 1997.6｜未命中｜source_ids=—｜結構性槓桿 77 ≥ 50
- 1997.7｜命中｜source_ids=—｜HY OAS 2.71% < 4% 且本次週 Δ 0 bps ≤ 0（未走闊）
- 1997.8｜未命中｜source_ids=—｜扳機狀態＝已擊發 ≠ 未擊發
**1998 LTCM 衝擊 feature audit**
- 1998.1｜未命中｜source_ids=structural.cross_asset_derivatives｜HY 週 Δ 0 bps < +30；SKEW 145.13、VIX ≈16.5 contango（無壓力事件）
- 1998.2｜未命中｜source_ids=—｜S&P `sp500_trend.chg_pct` −1.01% > −5%（無回檔）
- 1998.3｜命中｜source_ids=monetary.private_credit_liquidity｜具名非銀壓力：Blue Owl OCIC Q2 18.8% gate proration 等私募信貸贖回上限觸發
- 1998.4｜未命中｜source_ids=monetary.fedwatch｜FedWatch 7/29 ≈86.7% 持平、非轉鴿
- 1998.5｜命中｜source_ids=—｜估值溢價 79 ≥ 60
- 1998.6｜命中｜source_ids=—｜扳機狀態＝已擊發 ≥ 初啟
- 1998.7｜未命中｜source_ids=—｜市場廣度 Δ = 30 − 30 = 0 < +8
- 1998.8｜未命中｜source_ids=—｜ΔT10YIE +2 bps > 0（通膨預期非下行）
**1999 晚期狂熱 feature audit**
- 1999.1｜命中｜source_ids=—｜估值溢價 79 ≥ 75
- 1999.2｜命中｜source_ids=valuation.sp500_pe_cape｜CAPE 41.52 ≥ 38
- 1999.3｜未命中｜source_ids=—｜投機行為 58 < 60
- 1999.4｜未命中｜source_ids=speculation.microcap_moonshots,speculation.ipo_heat｜本週 moonshot 0；無營收 IPO 佔比未達偏高
- 1999.5｜未命中｜source_ids=—｜市場廣度 30 < 45（廣度健康、非轉窄）
- 1999.6｜未命中｜source_ids=—｜D5 monetary_side＝扳機側 ≠ 自滿側，all 不成立
- 1999.7｜命中｜source_ids=—｜結構性槓桿 77 ≥ 60
- 1999.8｜未命中｜source_ids=—｜散戶情緒 50 < 55
- 1999.9｜命中｜source_ids=speculation.upcoming_ai_ipos｜巨型 AI IPO pipeline 活躍：Anthropic 進行 IPO 投資人會議（$965B 估值，30 日內具名報導）
- 1999.10｜未命中｜source_ids=—｜扳機狀態＝已擊發 ≠ 未擊發
**2000/3 頂點 feature audit**
- 2000.1｜未命中｜source_ids=—｜估值溢價 79 < 85
- 2000.2｜命中｜source_ids=—｜扳機狀態＝已擊發 ≥ 初啟
- 2000.3｜未命中｜source_ids=—｜市場廣度 30 < 60
- 2000.4｜未命中｜source_ids=—｜prior `sp500_dev200_pct` 8.51 < +10 使第一分支為否；current chg −1.01% > −5%
- 2000.5｜未命中｜source_ids=—｜投機行為 58 < 70
- 2000.6｜未命中｜source_ids=speculation.insider_form4｜14 日內 0 件合格 Form 4 cluster
- 2000.7｜未命中｜source_ids=—｜散戶情緒 50 < 65
- 2000.8｜未命中｜source_ids=monetary.fedwatch｜FedWatch ≈86.7% 持平、非轉緊；10Y driver≠breakeven
**2021/12 Meme 頂 feature audit**
- 2021.1｜未命中｜source_ids=—｜散戶情緒 50 < 65
- 2021.2｜無資料｜source_ids=—｜本週無具名主導社群軋空（✗ NOT DISCLOSED）
- 2021.3｜命中｜source_ids=—｜結構性槓桿 77 ≥ 65
- 2021.4｜未命中｜source_ids=—｜D5 monetary_side＝扳機側 ≠ 自滿側，all 不成立
- 2021.5｜命中｜source_ids=retail.margin_debt｜margin debt YoY +53.7% ≥ +40%
- 2021.6｜未命中｜source_ids=speculation.microcap_moonshots｜本週 microcap moonshot 0 < 1
- 2021.7｜未命中｜source_ids=—｜市場廣度 30 < 50
- 2021.8｜未命中｜source_ids=—｜CPI YoY 3.46% < 4%，all 不成立

**兩句解讀**：本週相似度最高為「1997 早期建設」（50%）——市場廣度健康（30）、hyperscaler capex 仍上修、散戶未狂熱（50）、HY OAS 2.71% 史窄且本週未走闊，構成「基本面建設仍在、公開信用尚未轉緊」的早期組態；但須注意本週扳機狀態＝已擊發（私募信貸多基金 gate proration）且估值溢價 79 高企，機械最貼近錨與「早期」字面並不同義，實質更接近「估值高企＋非銀融資扳機、公開利差尚未反映」的中段位置。這意味循環位置介於建設與後期之間：真實技術突破吸引超商業回報所能支撐的資本（BIS AER 2026 Ch I：AI 相關投資 ≈1% of US GDP、IT 投資合計 ≈5% 已超 dot-com 峰），最須盯 AI 信用重定價（Oracle CDS 紀錄新高）與私募信貸閘門是否外溢至公開利差。長期指數成長趨勢偏離（Dot-com ≈95%、1929 ≈110%、當前 AI 週期 ≈147%；RIA/Farrell）作跨期敘事錨、不進 checklist。

## 機構情緒對照

本次無新機構調查數據。

## 本次新增訊號

比較基準：vs 前次（4天前）。

- **格局轉變（質化）**：三角格局由前次「分歧」轉為本次「穩定共存」——S&P ▼ −1.01% 小回、WTI 與 10Y 皆無新觀測（持平），10Y 反向重定價的分歧消退、三者回到小幅／持平共存（S&P `dev200_pct` 由 +8.51% 回落至 +6.73%）。
- **貨幣與信貸環境（D5）＝扳機側，score Δ 0——質化新訊號（雙向 Δ 遮蔽防護）**：私募信貸多基金 Q2 gate proration 延續且獲更廣證實（Blue Owl OCIC 18.8% 比例撥付、Blackstone BCRED ≈10% 撥付率 ≈50%、Golub GCRED ≈8.5% 撥付率 ≈59%；BofA 定調 Q2 為贖回高峰），扳機狀態維持「已擊發」；分數未動因先前已因扳機側偏高（前次即 75）。此為前次已存在之扳機側狀態延續（贖回需求 QoQ 略降但仍 >3× 上限、比例撥付事實成立）。
- **投機 pipeline 升溫（質化，score Δ 0）**：Anthropic 進入 IPO 投資人會議（估值 ≈$965B、可能 10 月掛牌），為 30 日內具名的巨型 AI IPO pipeline 活躍訊號（液性抽離風險），惟本週 moonshot 0、無主導軋空，投機分數未動。
- **結構性槓桿質化訊號（score Δ 0）**：US 單股槓桿 ETF 續擴散（Leverage Shares 6 檔 GOOGL/AMZN/META/AAPL、SK Hynix ADR 2x 系列）——惟**全球（非美）擴散訊號未觸發（本週擴散訊號未觸發，未達 2+ 非美市場同週核准；韓國 FSC 反於 07-16 起暫停新單股槓桿 ETF 上市）**，且本月無窗內新 AI 基礎設施債務事件、MOVE 低波，故分數未動。
- 其餘維度（估值 79、廣度 30、投機 58、散戶 50、貨幣 75、結構 77）分數與前次持平；總分 64【警戒】、Δ 0。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | S&P 500 收盤（sp500_trend latest） | 7,457.69 | FRED SP500（sp500_trend） | 2026-07-17 | 2026-07-20T09:20:00+08:00 |
| valuation.sp500_trend | S&P 500 距 200DMA 偏離（sp500_trend dev200_pct） | +6.73% | FRED SP500（sp500_trend） | 2026-07-17 | 2026-07-20T09:20:00+08:00 |
| retail.household_equity_allocation | 家庭持股佔金融資產比 | 45.76 | FRED BOGZ1FL153064486Q | 2026-01-01 | 2026-07-20T09:20:00+08:00 |
| monetary.fed_funds | Fed funds 上限（DFEDTARU） | 3.75% | FRED DFEDTARU | 2026-07-19 | 2026-07-20T09:20:00+08:00 |
| monetary.fed_funds | Fed funds 下限（DFEDTARL） | 3.50% | FRED DFEDTARL | 2026-07-19 | 2026-07-20T09:20:00+08:00 |
| monetary.hy_oas | HY OAS（BAMLH0A0HYM2） | 2.71% | FRED BAMLH0A0HYM2 | 2026-07-16 | 2026-07-20T09:20:00+08:00 |
| monetary.ig_oas | IG OAS（BAMLC0A0CM） | 0.78% | FRED BAMLC0A0CM | 2026-07-16 | 2026-07-20T09:20:00+08:00 |
| monetary.dgs10 | 10Y 名目殖利率（DGS10） | 4.57% | FRED DGS10 | 2026-07-16 | 2026-07-20T09:20:00+08:00 |
| monetary.dfii10 | 10Y 實質殖利率（DFII10） | 2.35% | FRED DFII10 | 2026-07-16 | 2026-07-20T09:20:00+08:00 |
| monetary.t10yie | 10Y breakeven（T10YIE） | 2.24% | FRED T10YIE | 2026-07-17 | 2026-07-20T09:20:00+08:00 |
| monetary.wti | WTI 原油（DCOILWTICO） | $79.2 | FRED DCOILWTICO | 2026-07-13 | 2026-07-20T09:20:00+08:00 |
| monetary.cpi_yoy | CPI YoY（CPIAUCSL yoy_pct） | 3.46% | FRED CPIAUCSL | 2026-06-01 | 2026-07-20T09:20:00+08:00 |
| monetary.t5yifr | 5y5y forward（T5YIFR） | 2.21% | FRED T5YIFR | 2026-07-17 | 2026-07-20T09:20:00+08:00 |
| monetary.term_premium | 10Y 期限溢價（THREEFYTP10） | 0.7788% | FRED THREEFYTP10 | 2026-07-10 | 2026-07-20T09:20:00+08:00 |
| monetary.repo_stress_srf | SOFR 隔夜利率 | 3.62% | FRED SOFR | 2026-07-16 | 2026-07-20T09:20:00+08:00 |
| monetary.repo_stress_srf | SOFR 99th 分位（SOFR99） | 3.70% | FRED SOFR99 | 2026-07-16 | 2026-07-20T09:20:00+08:00 |
| monetary.repo_stress_srf | IORB | 3.65% | FRED IORB | 2026-07-20 | 2026-07-20T09:20:00+08:00 |
| monetary.repo_stress_srf | SRF/隔夜 repo 操作量（RPONTTLD） | 0.0 | FRED RPONTTLD | 2026-07-17 | 2026-07-20T09:20:00+08:00 |
| monetary.walcl | Fed 資產負債表（WALCL） | 6,743,028 百萬美元（≈$6.74T） | FRED WALCL | 2026-07-15 | 2026-07-20T09:20:00+08:00 |
| monetary.ecb_boj | ECB 資產（ECBASSETSW） | 5,970,516 百萬歐元（≈€5.97T） | FRED ECBASSETSW | 2026-07-10 | 2026-07-20T09:20:00+08:00 |
| monetary.ecb_boj | BOJ 資產（JPNASSETS） | 6,395,509 億日圓（≈¥639.55T） | FRED JPNASSETS | 2026-06-01 | 2026-07-20T09:20:00+08:00 |
| structural.nbfi_bank_loans | 銀行對 NBFI 放款（LNFACBW027SBOG） | 2,004.02 億美元（≈$2.00T） | FRED LNFACBW027SBOG | 2026-07-08 | 2026-07-20T09:20:00+08:00 |

### Coverage

| source_id | 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（P/E 32.08、CAPE 41.52 @07-17） |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E | MarketXLS [SEARCH]（stock-of-state 沿用） | ✓ SEARCH-VERIFIED（trailing ≈40 @05-15） |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 [primary: SEARCH]（best-effort） | ✗ NOT DISCLOSED（本季無新 EPS-vs-multiple 分解披露） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500 派生） | ✓ API（dev200 +6.73%／dev52 +8.42%） |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧 | 信用市場 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Oracle CDS ≈198bp record、CoreWeave ≈665bp @07-16） |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst [SEARCH] | ✓ SEARCH-VERIFIED（RSP +10.68% vs SPY +7.47%） |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | State Street SPDR 持股 [SEARCH] | ✓ SEARCH-VERIFIED（36.40% @07-02） |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth [SEARCH] | ✓ SEARCH-VERIFIED（NYSE 07-17 跌約 2×漲、NH 241/NL 166） |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH]（403，經 MacroMicro） | ✓ SEARCH-VERIFIED（37 Fear @07-17） |
| retail.margin_debt | 散戶｜Margin Debt: FINRA | FINRA/Advisor Perspectives [SEARCH]（月頻 stock-of-state） | ✓ SEARCH-VERIFIED（$1.416T、+53.7% YoY、2026-05 沿用） |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（Bull 44.9% @07-16） |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB/cashtag [SEARCH]（best-effort） | ✗ NOT DISCLOSED（本週無主導軋空事件） |
| retail.household_equity_allocation | 散戶｜Household equity allocation | fetch_macro.py BOGZ1FL153064486Q | ✓ API（45.76% @2026-Q1） |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim/ycharts [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（95.64 @07-15） |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM | 賣方調查 [SEARCH]（月頻，best-effort） | ✗ NOT DISCLOSED（7 月 FMS 07-14 發布，早於前次基準、非本次新增） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED DFEDTARU/DFEDTARL | fetch_macro.py FRED API | ✓ API（3.75%/3.50% @07-19） |
| monetary.hy_oas | 貨幣｜High Yield OAS | fetch_macro.py FRED API | ✓ API（2.71% @07-16，Δ0，no_new_obs） |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | fetch_macro.py FRED API | ✓ API（0.78% @07-16，Δ0，no_new_obs） |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | fetch_macro.py FRED API | ✓ API（4.57% @07-16，Δ0，no_new_obs） |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield | fetch_macro.py FRED API | ✓ API（2.35% @07-16，Δ0，no_new_obs） |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | fetch_macro.py FRED API | ✓ API（2.24% @07-17，Δ+2bps） |
| monetary.wti | 貨幣｜WTI crude oil price | fetch_macro.py FRED API | ✓ API（$79.2 @07-13，no_new_obs） |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED | fetch_macro.py FRED API（月頻） | ✓ API（3.46% @2026-06） |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | fetch_macro.py FRED API | ✓ API（2.21% @07-17，Δ+1bp） |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED | fetch_macro.py FRED API | ✓ API（0.7788% @07-10，+4.7bps） |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py repo_stress | ✓ API（SOFR−IORB −3bps、SOFR99−IORB +5bps、SRF $0 @07-16/17） |
| monetary.treasury_auctions | 貨幣｜美債標售需求 | CryptoBriefing/TreasuryDirect [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（10Y BTC 2.59、小幅 tail @07-08） |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（7/29 ≈86.7% 持平 @07-18） |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED WALCL | fetch_macro.py FRED API | ✓ API（$6.74T @07-15，no_new_obs） |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | fetch_macro.py FRED API | ✓ API（€5.97T @07-10／¥639.55T @06-01） |
| monetary.pboc | 貨幣｜PBoC aggregate financing | Bloomberg [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（6M 逆回購 ¥1.4T @07-14） |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Blue Owl OCIC 18.8% gate proration @07-02） |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報 [SEARCH]（stock-of-state） | ✓ SEARCH-VERIFIED（2026 ≈$700B、仍上修） |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic/OpenAI/Google [SEARCH]（best-effort） | ✗ NOT DISCLOSED（本季無量化披露） |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch/The Information [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Anthropic ≈$47B／OpenAI ≈$25B run-rate） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration | 財報電話 [primary: SEARCH]（best-effort） | ✗ NOT DISCLOSED（本次無新一手 RPO 披露） |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（DRAM +13–18% QoQ 3Q26 @07-03；供給仍被吸收） |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構 | 季報 [primary: SEARCH]（best-effort） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口 | 組合披露 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（年化 capex ≈$700B vs 終端營收低百億級） |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K/10-Q [primary: SEARCH]（best-effort，30日） | ✗ NOT DISCLOSED（過去 30 日無新變更） |
| ai.capital_cycle | AI｜資本週期階段 | 供需增速+進出場事件 [SEARCH]（best-effort） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days +AI rename/SPAC | [SEARCH] | ✓ SEARCH-VERIFIED（EVTV→Azio AI 改名 @07-13） |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis/Renaissance [SEARCH] | ✓ SEARCH-VERIFIED（YTD ≈200 檔、$141.2B @07-16） |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz/Benzinga [primary: SEARCH]（required 週螢幕） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | S-1/具名報導 [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Anthropic IPO 投資人會議 $965B @07-15） |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership | SEC EDGAR [primary: EDGAR]（required） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（0.73 @07-17） |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing [primary: SEARCH] | ✓ SEARCH-VERIFIED（總 ≈$198B @07-10） |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire/ETF.com [SEARCH] | ✓ SEARCH-VERIFIED（Leverage Shares 6x @07-07、SK Hynix 2x @07-13） |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX/TWSE/JPX/ESMA [SEARCH]（best-effort，7日） | ✗ NOT DISCLOSED（本週擴散訊號未觸發；韓國反收緊） |
| structural.zero_dte | 結構｜0DTE option volume | Cboe [SEARCH]（Cboe 403） | ✓ SEARCH-VERIFIED（≈63%，Cboe @2026-02） |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com [SEARCH] | ✓ SEARCH-VERIFIED（6 月 16.03 億口、+45% YoY @07-02） |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe/AInvest [SEARCH] | ✓ SEARCH-VERIFIED（SKEW ≈145.13、VIX contango @07-15） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 D4（confirmation） | ✓ SEARCH-VERIFIED（$1.416T/+53.7% YoY，D4 引用不重複計分） |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]（best-effort，30日） | ✗ NOT DISCLOSED（過去 30 日無窗內新事件；CoreWeave $8.5B 為 Q1 背景） |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | fetch_macro.py FRED API | ✓ API（$2.00T @07-08，no_new_obs） |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | script→WebSearch [primary: script]（best-effort） | ✗ NOT DISCLOSED components=cftc_lev_funds:fetch_failed,move_index:fetch_failed,ofr_repo:fetch_failed；無視窗內 MOVE／基差新值 |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.08 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio | 2026-07-17 | 2026-07-20T09:20:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 41.52 | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe | 2026-07-17 | 2026-07-20T09:20:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E ≈40 trailing | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026 | 2026-05-15 | 2026-07-20T09:20:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS ≈198bp record、CoreWeave ≈665bp | Oracle CoreWeave CDS spread widening July 2026 | https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/ | 2026-07-16 | 2026-07-20T09:20:00+08:00 |
| breadth.rsp_spy | RSP +10.68% vs SPY +7.47% YTD | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ | 2026-06-10 | 2026-07-20T09:20:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 36.40% | S&P 500 top 10 concentration percent 2026 | https://ahasignals.com/sp500-concentration-risk/ | 2026-07-02 | 2026-07-20T09:20:00+08:00 |
| breadth.advance_decline | NYSE 07-17 下跌約 2×上漲、NH 241/NL 166 | NYSE advance decline breadth July 17 2026 | https://money.usnews.com/investing/news/articles/2026-07-17/wall-st-futures-fall-as-chip-selloff-gathers-pace-netflix-tumbles | 2026-07-17 | 2026-07-20T09:20:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（Fear） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed | 2026-07-17 | 2026-07-20T09:20:00+08:00 |
| retail.margin_debt | FINRA margin debt $1.416T、+53.7% YoY | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra | 2026-05-31 | 2026-07-20T09:20:00+08:00 |
| retail.aaii | AAII Bull 44.9% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey | 2026-07-16 | 2026-07-20T09:20:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number | 2026-07-15 | 2026-07-20T09:20:00+08:00 |
| monetary.treasury_auctions | 10Y BTC 2.59、小幅 tail | US Treasury 10Y auction July 2026 bid to cover | https://cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/ | 2026-07-08 | 2026-07-20T09:20:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 ≈86.7% 持平 | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch | 2026-07-18 | 2026-07-20T09:20:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance | 2026-07-14 | 2026-07-20T09:20:00+08:00 |
| monetary.private_credit_liquidity | [private_credit_gate] Blue Owl OCIC Q2 贖回 18.8% 於 5% 上限比例撥付 | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://whbl.com/2026/07/02/blue-owl-keeps-withdrawal-limits-even-as-redemption-pressure-modestly-eases/ | 2026-07-02 | 2026-07-20T09:20:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex ≈$700B、仍上修 | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html | 2026-05-15 | 2026-07-20T09:20:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic ≈$47B／OpenAI ≈$25B run-rate | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-05-15 | 2026-07-20T09:20:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約 +13–18% QoQ | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html | 2026-07-03 | 2026-07-20T09:20:00+08:00 |
| ai.revenue_capex_gap | 年化 capex ≈$700B vs AI 終端營收低百億級 | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-05-15 | 2026-07-20T09:20:00+08:00 |
| speculation.ai_rename_spac | EVTV→Azio AI（AZIO）改名 07-13 | AI rename ticker change July 2026 Azio EVTV | https://www.businesswire.com/news/home/20260710628386/en/Azio-AI-Holdings-Inc.-Nasdaq-EVTV-to-Begin-Trading-Under-New-Ticker-Symbol-AZIO-Completing-Corporate-Rebrand | 2026-07-13 | 2026-07-20T09:20:00+08:00 |
| speculation.ipo_heat | 2026 YTD ≈200 檔 IPO、$141.2B | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/ | 2026-07-16 | 2026-07-20T09:20:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot 件數 0 | microcap 100% single day quantum AI moonshot July 2026 | Finviz/Benzinga/StockTitan movers screener | 2026-07-20 | 2026-07-20T09:20:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 投資人會議 $965B、可能 10 月掛牌 | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html | 2026-07-15 | 2026-07-20T09:20:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 cluster 件數 0（EDGAR egress 受限） | insider Form 4 cluster AI leaders July 2026 openinsider | SEC EDGAR / openinsider（一手 URL 無法取得） | 2026-07-20 | 2026-07-20T09:20:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.73 | Cboe equity put call ratio July 2026 | https://www.cboe.com/markets/us/options/market-statistics/daily/ | 2026-07-17 | 2026-07-20T09:20:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM ≈$198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-07-10 | 2026-07-20T09:20:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x GOOGL/AMZN/META/AAPL | single-stock leveraged ETF launch July 2026 Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html | 2026-07-07 | 2026-07-20T09:20:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX ≈63% | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/ | 2026-02-28 | 2026-07-20T09:20:00+08:00 |
| structural.options_volume | OCC 6 月 1,603,491,559 口、+45% YoY | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report | 2026-07-02 | 2026-07-20T09:20:00+08:00 |
| structural.cross_asset_derivatives | [snapshot] Cboe SKEW 145.13、VIX ≈16.5 contango | VIX term structure SKEW July 2026 | https://www.ainvest.com/news/0dte-volatility-drives-market-strategies-2026-2602/ | 2026-07-15 | 2026-07-20T09:20:00+08:00 |
| structural.margin_debt_crosscheck | margin debt $1.416T、+53.7% YoY（cross-ref D4） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra | 2026-05-31 | 2026-07-20T09:20:00+08:00 |

**Macro script 說明**：`python3 scripts/fetch_macro.py 2026-07-16` 於 2026-07-20 執行，FRED 全 20 序列 `status: ok`（多序列前次基準日＝最新觀測日而 `no_new_obs: true`，Δ=0 為成功結果）；`sp500_trend`／`repo_stress`／`decomposition` ok（decomposition driver=unknown、三腿視窗不一致、freshness=partial_stale）；`cftc_lev_funds`／`move_index`／`ofr_repo` `fetch_failed`（改走 best-effort WebSearch）。金鑰未輸出。

## 本次分數存檔
```json
{
  "date": "2026-07-20",
  "iso_week": "2026-W30",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "valuation": 79,
  "breadth": 30,
  "speculation": 58,
  "retail": 50,
  "monetary": 75,
  "structural": 77,
  "total": 64,
  "tier": "警戒",
  "regime": "穩定共存",
  "trigger_state": "已擊發",
  "trigger_reasons": [
    "private_credit_gate"
  ],
  "monetary_side": "扳機側",
  "hy_oas_widening_streak": 0,
  "sp500_dev200_pct": 6.73
}
```

本報告為相對風險溫度計，非擇時訊號。

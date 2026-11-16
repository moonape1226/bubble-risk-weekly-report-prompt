# 2026-07-27 市場泡沫風險評估報告
> 報告日期：2026-07-27；執行日：2026-07-27 Asia/Taipei；ISO 週次：2026-W31；前次基準：report-2026-07-23（4天前）

**總評**：總分 64【警戒】（Δ 0）；扳機狀態：已擊發；最貼近錨點：1997 早期建設（50%）。

## §1 六維度風險條圖
| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▱▱▱ | 78 | 79 | -1 |
| 市場廣度 | ▰▰▰▱▱▱▱▱▱▱ | 30 | 30 | 0 |
| 投機行為 | ▰▰▰▰▰▱▱▱▱▱ | 58 | 58 | 0 |
| 散戶情緒 | ▰▰▰▰▱▱▱▱▱▱ | 48 | 50 | -2 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▰▱▱▱ | 75 | 75 | 0 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 78 | 77 | +1 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **64【警戒】** | 64 | 0 |

## §2 歷史錨點相似度
| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1973/1 Nifty Fifty 頂 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 1997 早期建設 | 50% | ▰▰▰▰▰▱▱▱▱▱ | ◀ 最貼近 |
| 1998 LTCM 衝擊 | 50% | ▰▰▰▰▰▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 2000/3 頂點 | 15% | ▰▱▱▱▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |

## §3 三角訊號
| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,411.98 | 持平 +0.05%（前次 ≈7,408.30） |
| WTI 原油 | $84.38 /bbl | 持平 0%（無新觀測，前次 ≈$84.38） |
| 10Y Treasury | 4.71% | 持平 0 bps（無新觀測，前次 ≈4.71%） |

**三者狀態**：穩定共存——三者本次方向皆為持平、未見同向拉伸；S&P ▲ 幅度僅 +0.05%（< 0.5% 門檻，判持平）、WTI 與 10Y 皆無新觀測（Δ 0），S&P `dev200_pct` ≈+5.8%（< +10% 拉伸門檻），故未升為同向偏高。資產面平靜與非銀融資扳機（私募信貸 gate）並存，須分開判讀。
- 股市：≈7,411.98（S&P 500，2026-07-24 收）；較前次 持平 +0.05%（前次 ≈7,408.30）；距 200 日均線 +5.8%、距 52 週均線 +7.4%——價格延伸較前次（+7.14%）回落、非急拉。
- WTI 原油：≈$84.38/bbl（2026-07-20，無新觀測）；較前次 持平 0%（前次 ≈$84.38）。
- 10Y 殖利率：4.71%（2026-07-23，無新觀測）；較前次 持平 0 bps（前次 ≈4.71%）；主要驅動：三腿視窗不一致（driver=unknown）。
**格局轉變**：前次格局＝穩定共存（讀自 report-2026-07-23 的 `regime`）→ 本次格局＝穩定共存；三者由前次的小幅上行轉為持平／無新觀測，價格延伸未達門檻，維持小幅／持平的穩定共存。
**10Y 成因拆解**：拆的是週變動（bps）、非水位（`ΔDGS10 ≈ ΔDFII10 + ΔT10YIE`）；三腿視窗不一致（`decomposition.driver=unknown`——ΔT10YIE 取自較新視窗、恆等式不跨視窗成立，DGS10／DFII10 本週無新觀測），判定 不可判（視窗不一致）；三腿實際 signed 週變動如下：
- ΔDGS10 名目殖利率週變動：0 bps
- ΔDFII10 實質殖利率週變動：0 bps
- ΔT10YIE 損益平衡通膨週變動：−2 bps
- 觀測新鮮度：部分未更新（stale_series=DGS10,DFII10）
- 判定：不可判（視窗不一致）
**扳機鏈**：A 通膨鏈（油 → 通膨預期 → Fed 受限 → refinancing 成本）本週未加速——WTI 持平（≈$84.38，無新觀測）、實現通膨續處高位且通膨預期微升未回落：[monetary.cpi_yoy] CPIAUCSL yoy_pct=3.46 data_date=2026-06-01（6 月）、5y5y forward [monetary.t5yifr] T5YIFR latest=2.28 delta_bps=1.0 data_date=2026-07-24（週 +1 bps）；CME FedWatch 7/29 會議 ≈61% 持平／≈38% 升息（2026-07-25，較前次更偏鷹、未定價降息），Fed 仍受 3.46% 通膨與財政供給牽制、Fed put 可得性下降；無當期電價／能源瓶頸新報導。B 槓桿鏈（衝擊：財政風險再定價 → NBFI 去槓桿 → margin spiral → 國債市場失序 → 官方市場功能回應）乾柴堆積但未點火——衝擊節點：10Y 期限溢價 THREEFYTP10 ≈0.7787%（序列自身 trailing ≈7d ≈0 bps、本週未再上行）、7/22 20Y 標售明顯轉弱（bid 高利率 5.163%、正 tail ≈+0.5 bp、direct 需求 10.21% 遠低於均值 23.9%、dealer takedown 14.67% 高於均值 10.1%、評級 D+），財政再定價壓力偏溫和但長端需求轉弱；NBFI 節點：script `cftc_lev_funds`／`move_index`／`ofr_repo` 本次 fetch_failed，WebSearch 未取得 7 日窗內可稽核基差交易新證據（CFTC 槓桿基金美債期貨淨空 ≈349,563 口最新為 2026-07-07、落 7 日窗外僅作背景，MOVE 官方水位未能確認，Bloomberg 稱基差交易「sputtering」但無具日期平倉事件）——本鏈本週無新積累／釋放事件；官方回應節點：`repo_stress` SOFR−IORB −1 bps、SOFR99−IORB +7 bps、SRF 動用 ≈$0（無失序）。real-rate 主導的異常 10Y 上行本週不存在（ΔDGS10 0 bps）。本鏈證據 best-effort，本週無基差交易槓桿新積累／釋放事件。
**扳機理由**：private_credit_gate
⚠ **結論**：扳機狀態：已擊發——本次續命中「私募信貸 gate proration / breach」：Blackstone 於 2026-07-23 Q2 財報電話會確認 BCRED（Blackstone Private Credit Fund）Q2 贖回需求達 ≈10% NAV（自 Q1 的 7.9% 升高）、突破 5% 季度贖回上限、僅約 50% 獲償並比例撥付、季內淨流出 ≈$1.2B（inflow→outflow）——此為 1998 LTCM 型「融資扳機」特徵，非銀信用先於公開 mark-to-market 利差（HY 2.77%／IG 0.79% 仍史窄）出現一階壓力；惟 Blackstone 同場指 Q3 初贖回已「明顯放緩」，扳機事實成立但趨勢轉緩。三者配置歷史意義：估值＋槓桿＝崩跌位能，融資緊縮＝時點扳機；本週三角資產面持平仍屬穩定共存，惟公開利差自滿與非銀融資扳機仍並存（自滿側 froth 與扳機側 financing 壓力同框），槓桿鏈 B 未點火，失序仍屬結構化產品閘門層級、非國債市場層級。

## 六維度評分

### 1. 估值溢價 — 78（weight 22%，Δ -1）
- **S&P 500 trailing P/E** ≈**28.52**（2026-07-24，https://www.multpl.com/s-p-500-pe-ratio，source_ids=valuation.sp500_pe_cape）——較前次 28.85 微降（隨 Q2 財報季實現盈餘更新），仍遠高於長期中位（≈16–19）。
- **Shiller CAPE** ≈**40.46**（2026-07-24，https://www.multpl.com/shiller-pe，source_ids=valuation.sp500_pe_cape）——較前次 40.94 微降、仍逼近歷史高（≈44）、遠高於長均 ≈32.4。
- **Excess CAPE Yield（ECY）** ≈**0.04%**（`1/40.46 − 2.43/100`，derived 自 CAPE 40.46 與 DFII10 2.43%，2026-07-24，source_ids=valuation.sp500_pe_cape）——仍接近 0（實質殖利率升至 2.43% 使其更低），屬 1929／2000 級別股相對債極貴訊號（confirmation，不主計分）。
- **Mag 7 加權 P/E**：Mag 7 對其餘 493 檔溢價壓縮至 ≈**10%**（「近十年最低」）、NVDA NTM P/E ≈18.7 低於自身歷史（2026-07-08，https://www.cnbc.com/2026/07/08/magnificent-seven-stocks-are-the-cheapest-in-a-decade-by-one-measure.html，source_ids=valuation.mag7_multiples）——絕對水位仍高但相對溢價續收斂（stock-of-state 沿用），屬估值面緩和訊號。
- **價格趨勢偏離（Farrell #1/#2/#4）** S&P 距 200 日均線 **+5.8%**、距 52 週均線 +7.4%（`sp500_trend`，2026-07-24，FRED SP500，source_ids=valuation.sp500_trend）——較前次 +7.14% 回落，價格延伸壓力減輕、距 +10% 拉伸門檻更遠，與 P/E／CAPE 互補、不重複計分。
- **AI capex 現實檢核**：hyperscaler 2026 capex 指引續上修——Alphabet 7/22 Q2 財報將 FY26 capex 上修至 ≈**$195–205B**（自 $180–190B、+$15B；Q2 capex $44.9B 使 FCF 轉負 −$5.9B），四家合計 ≈$725B+（2026-07-22，https://mlq.ai/news/alphabet-raises-2026-capex-guidance-to-195-205b-cloud-revenue-surges-82/，source_ids=ai.hyperscaler_capex）——基本面敘事仍撐估值（MSFT／META 7/29、AMZN 7/30 才公布，本次為 Alphabet 硬數據沿用）。
- **AI compute 供需現實檢核**：伺服器 DRAM 3Q26 合約 **+13–18% QoQ**、NAND +10–15%、HBM 佔 DRAM 晶圓 23%、標準 DRAM 交期 30–40+ 週（TrendForce，2026-07-03，https://www.trendforce.com/presscenter/news/20260703-13134.html，source_ids=ai.compute_supply_demand）——供給仍被 AI 伺服器合約與 token 需求吸收、缺口未成形（供給緊、非過剩），此渠道未推升估值風險。
- **AI 營收對 capex 缺口現實檢核**：分母年化 capex ≈**$725B**（分母：top-4＋Oracle）vs 分子已披露 AI 終端年化營收（Anthropic ≈$47B、OpenAI ≈$25B run-rate）量級缺口仍逾 10× 且 capex 續升（2026-06-15，https://epoch.ai/data-insights/anthropic-openai-revenue，source_ids=ai.revenue_capex_gap）——回本假設後移，屬估值風險上修的質化依據（缺口未收斂）。
- **Hyperscaler 融資結構（capex vs FCF / 發債）**：quarterly_state——Alphabet FY26 capex 上修至 ≈$205B 且 Q2 FCF 轉負（−$5.9B）＝capex 已超越自身現金流；event_scan——AI 相關 IG 發債 2026 至 7/8 累計 ≈$218–250B（測試投資人胃納）（2026-07-08，https://www.morningstar.com/bonds/bond-issuance-backing-ai-investment-tops-250b-testing-limits-voracious-investor-demand，source_ids=ai.hyperscaler_financing_mix）——capex 愈靠發債支撐、同份 guidance 脆弱性上升（BIS Bulletin 120，confirmation，不主計分）。
- **AI 信用定價分歧（equity-vs-credit schism）**：AI 複合體單一發行人利差走闊（Oracle、CoreWeave、Meta 與半導體 IG 利差升至數月高）而 CDX.NA.IG 基準指數維持平穩＝信貸端開始重定價、股價未跟（後期訊號側）；hyperscaler 2026 發債 ≈**$182B**（≈US IG YTD 15%）（2026-07-16，https://247wallst.com/investing/2026/07/16/the-ai-revolution-is-reshaping-credit-markets-here-is-what-it-really-says-about-risk/，source_ids=valuation.ai_credit_schism）——分歧未解（confirmation，不主計分；缺值不調分）。
- **TP-upgrade phase signal**：本季（Q3 2026）具名賣方升評屬 **EPS-driven**——Morgan Stanley NVDA 目標 $288（≈22× CY27 EPS、target PE 未擴張）（2026-07-13，https://www.gurufocus.com/news/8955458/morgan-stanley-upgrades-nvidia-nvda-with-a-288-target-price，source_ids=valuation.analyst_tp_decomposition）——升評由 E 而非 multiple 主導、同季未見多檔 multiple-driven 重定價，屬相對緩和訊號（confirmation，不主計分）。
- **折舊年限變動（盈餘品質）**：過去 30 日無新 10-K／10-Q 折舊年限或殘值假設變更披露（財報季 7/29–7/30 才啟）（✗ NOT DISCLOSED，source_ids=ai.depreciation_life，不納入計分）。
- **backlog 重複計算風險（RPO double-counting）**：本次無新一手客戶集中度／RPO 披露具乾淨窗內資料日（MSFT RPO 更新落 7/29）（✗ NOT DISCLOSED，source_ids=ai.customer_concentration_rpo，不納入計分）。
- **資本週期階段**：event_scan 無窗內具日期的新進入者／取消事件（neocloud 融資轉緊為背景敘事）、quarterly_state 供需增速證據不足（供給側 capex +77% YoY 有據，需求側 token 增速僅存 3–5 月舊值），本次不判定週期階段（✗ NOT DISCLOSED，source_ids=ai.capital_cycle，不納入計分）。
**結論**：分數由 79 降至 **78**（rubric 高位）。趨勢偏離由 +7.14% 回落至 +5.8%、Mag7 相對溢價壓縮至 ≈10%、CAPE 40.46 微降＝估值面小幅緩和；惟 CAPE 仍近史高、ECY ≈0、capex 續上修（Alphabet $205B）與 AI 信用分歧同框對沖——淨評較前次微降 1 分。

### 2. 市場廣度 — 30（weight 13%，Δ 0）
- **RSP（等權）vs SPY（市值權）YTD**：RSP ≈**+12.39%** YTD、領先 SPY ≈+5 pp（2026-07-24，https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/，source_ids=breadth.rsp_spy）——等權領先市值權且領先幅度較前次 +2.4 pp 擴大，廣度結構偏健康／轉寬方向。
- **Top-10 集中度**：≈**37%**（2026-07-15，較 2025 的 ≈41% 回落，https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/，source_ids=breadth.top10_concentration）——絕對仍偏高但續自高點回落、持平於中 30% 區。
- **Advance/Decline 與新高/新低**：NYSE A/D 線 7 月觸 12 個月新高（廣度參與健康），惟新高家數轉薄（週一 78 檔、較兩週前 175 檔顯著收斂）、新高仍多於新低（≈2026-07-21，https://research.leutholdgroup.com/categories/nyse-advancedecline.1440，source_ids=breadth.advance_decline）——A/D 結構健康但新高動能收斂，屬殘餘負面。
**結論**：分數維持 **30**（rubric 21–40 偏健康端）。等權領先市值權且領先幅度擴大（+5 pp）為結構性健康主訊號、A/D 線創高；新高家數收斂與 Top-10 ≈37% 偏高為殘餘負面——正負相抵，淨評與前次持平。

### 3. 投機行為 — 58（weight 18%，Δ 0）
- **+AI 改名／SPAC**：過去 7 日（07-20–07-27）**2 件**合格 SPAC——B&R Technology Merger（BRTMU）$325M SPAC（AI-target、units 07-21 掛牌）、Southern Cross Acquisition II（SCATU）$100M SPAC 申報（AI-rename「AIB」於 06-25 完成、落窗外）（2026-07-21，https://www.boardroomalpha.com/research/spac-market-update-july-21-2026-cdaq，source_ids=speculation.ai_rename_spac）——✓ SEARCH-VERIFIED，SPAC 活動較前次（0 件）回溫。
- **IPO 熱度**：Renaissance IPO Index YTD **+16.7%** vs S&P +8.9%、週內以 pipeline 建置為主（Reformation ≈$225M、Ionic Digital 直接掛牌、Varsal/Ticketplus 小型；無顯著 first-day pop）（2026-07-23，https://www.renaissancecapital.com/IPO-Center/Stats，source_ids=speculation.ipo_heat）——IPO 表現活躍但秩序尚可、無無營收暴衝。
- **Microcap thematic moonshots**：本週 **0 件**合格（<$1B 市值、單日 ≥100% 或 2–3 日 ≥50%、堆疊 2+ 熱主題＋弱基本面；2026-07-27 螢幕）——✓ SEARCH-VERIFIED（0 件）（source_ids=speculation.microcap_moonshots）；最接近者 American Fusion（AMFN）單日 ≈+58% 但屬單一主題（fusion/輻射認證）、未達 2+ 主題堆疊，不合格。
- **Upcoming AI mega-IPO pipeline**：**Anthropic 續進 IPO 程序**（估值 ≈$965B、confidential S-1、可能秋季掛牌），OpenAI 傳 confidential S-1、目標 9 月 >$1T（2026-07-15，https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html，source_ids=speculation.upcoming_ai_ipos）——30 日內具名巨型 AI IPO pipeline 活躍、流動性抽離風險（投機 pipeline 升溫的質化依據）。
- **Insider selling clusters**：required 螢幕已執行（2026-07-27 螢幕）；14 日內（07-13–07-27）無合格「Form 4 cluster」——僅零星 10b5-1（PLTR Moore 07-15 ≈$2.14M、META Olivan 07-20 ≈$0.95M），NVDA 大額售出均落 07-13 前窗外，未構成多內部人窗內 cluster——**0 件合格**（✓ SEARCH-VERIFIED（0 件），source_ids=speculation.insider_form4）。
- **Cboe equity-only put/call**：≈**0.61**（2026-07-23，https://ycharts.com/indicators/cboe_equity_put_call_ratio，source_ids=speculation.equity_put_call）——call 偏重、較前次 0.65 略降（方向性投機略升），未破 0.50 極端（confirmation，不主計分）。
- **社交情緒代理**：本週（07-20–07-27）WEN（Wendy's）於 r/wallstreetbets 主導軋空、單日 +25%／盤中一度 ≈+42%（高空頭回補）（2026-07-25，https://altindex.com/wallstreetbets，source_ids=retail.social_sentiment）——具名迷因軋空事件重現（投機口袋，非主計分驅動）。
**結論**：分數維持 **58**（rubric 41–60「投機升溫」）。本週 SPAC 回溫（2 件）、WEN 軋空重現、put/call 0.61 call 偏重為升溫面；moonshot 仍 0、insider 無合格 cluster、IPO 無無營收暴衝為抑制面——正負相抵，投機體感與前次持平。

### 4. 散戶情緒 — 48（weight 12%，Δ -2）
- **CNN Fear & Greed**：≈**39「Fear」**（2026-07-24，https://en.macromicro.me/series/22748/cnn-fear-and-greed，source_ids=retail.fear_greed）——較前次 41「Fear」再降、仍處恐懼區，散戶未亢奮。
- **Margin Debt**：**$1.502T（6 月，記錄高）、YoY +51.5%**（2026-07-20 發布，https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026，source_ids=retail.margin_debt）——月頻 stock-of-state；6 月新值續創高、取代前次沿用之 5 月值；YoY +51.5% 仍屬 1999／2007／2021 頂部級別警訊。
- **AAII 散戶調查**：**Bull 29.6%／Bear 42.3%／Neutral 28.1%**（2026-07-23 週，https://www.aaii.com/sentimentsurvey，source_ids=retail.aaii）——多方自前次 44.9% 驟降 ≈15 pp 至 2022-09 以來最低、空方高於長均，散戶情緒明顯轉空。
- **家庭持股佔金融資產比**：**45.76%**（`BOGZ1FL153064486Q`，2026-01-01 資料日／2026-Q1，FRED，source_ids=retail.household_equity_allocation）——歷史高位、後續加碼空間有限（Farrell #5，季頻沿用、不計週 Δ）。
- **NAAIM Exposure Index**：**84.02**（2026-07-22，https://ycharts.com/indicators/naaim_number，source_ids=retail.naaim）——主動經理人曝險自前次 95.64 回落、降至長均 ≈92.6 之下＝已減碼（Farrell #9，confirmation cross-check，不主計分）。
**結論**：分數由 50 降至 **48**（rubric 41–60 下緣）。CNN F&G 由 41 降至 39 續處 Fear、AAII 多方驟降至 29.6%（轉空）、NAAIM 由近滿倉回落至 84＝情緒／擁擠度三表同步降溫；惟 margin debt 6 月創高（YoY +51.5%）、家庭持股高位、WEN 軋空重現為抑跌——淨評較前次降 2 分。

### 5. 貨幣與信貸環境 — 75（weight 20%，Δ 0）
- **Fed funds rate**：目標區間 **3.50–3.75%**（`DFEDTARU` 3.75%／`DFEDTARL` 3.50%，2026-07-26，FRED，source_ids=monetary.fed_funds）——無變動。
- **市場隱含路徑（CME FedWatch，best-effort）**：7/29 會議 ≈**61% 持平／≈38% 升息**、9 月傾向升息、全年未定價降息（2026-07-25，https://www.cnbc.com/2026/07/13/-a-july-rate-hike-from-the-fed-the-odds-are-rising.html，source_ids=monetary.fedwatch）——較前次（≈83% 持平）明顯偏鷹、Fed 寬鬆空間進一步受限（缺值不調分）。
- **Realized inflation vs expectations**：CPI YoY **3.46%**（`CPIAUCSL`，2026-06-01，FRED，source_ids=monetary.cpi_yoy）仍高於 2% 目標、5y5y forward **2.28%**（`T5YIFR`，2026-07-24，週 Δ +1 bps，FRED，source_ids=monetary.t5yifr）微升——通膨黏著、Fed 約束未鬆。
- **10Y 期限溢價（term premium）**：`THREEFYTP10` **0.7787%**（2026-07-17，Kim-Wright 三因子模型，序列自身 trailing ≈7d ≈0 bps，FRED，source_ids=monetary.term_premium）——財政風險再定價本週未再上行、維持溫和高位。
- **repo 資金壓力（SOFR−IORB）與 SRF 動用**：`repo_stress`——SOFR **3.64%**、IORB 3.65%、SOFR−IORB **−1 bps**；SOFR99 3.72%、SOFR99−IORB +7 bps；RPONTTLD／SRF 動用 ≈**$0.001B**（2026-07-23／24，FRED SOFR/SOFR99/IORB/RPONTTLD，source_ids=monetary.repo_stress_srf）——secured-funding 無壓力、SRF 未實質動用。
- **美債標售需求（auction，best-effort）**：7/22 20Y 標售明顯轉弱——high yield 5.163%、正 tail ≈+0.5 bp、direct/domestic 需求 10.21%（遠低於均值 23.9%）、dealer takedown 14.67%（高於均值 10.1%）、評級 D+（2026-07-22，https://investinglive.com/news/us-treasury-auctions-off-13-billion-of-20-year-bonds-at-a-high-yield-of-5-163，source_ids=monetary.treasury_auctions）——長端需求轉弱、財政供給壓力事件溫和偏升（confirmation；缺值不調分）。
- **HY OAS**：**2.77%**（`BAMLH0A0HYM2`，2026-07-23，週 Δ 0 bps，FRED，source_ids=monetary.hy_oas）——接近循環低、極窄、自滿側訊號（連續走闊 streak 歸零）。
- **IG OAS**：**0.79%**（`BAMLC0A0CM`，2026-07-23，週 Δ 0 bp，FRED，source_ids=monetary.ig_oas）——史窄、信用自滿。
- **10Y nominal 週變動拆解**：ΔDGS10 0 bps ≈ ΔDFII10 0 bps ＋ ΔT10YIE −2 bps（三腿視窗不一致、driver=unknown、DGS10／DFII10 無新觀測）；`DGS10` **4.71%**（2026-07-23，FRED，source_ids=monetary.dgs10）、`DFII10` **2.43%**（2026-07-23，source_ids=monetary.dfii10）、`T10YIE` **2.26%**（2026-07-24，source_ids=monetary.t10yie）——殖利率持平、估值折現／再融資壓力未再增（詳 §3）。
- **WTI 原油**：**$84.38**/bbl（`DCOILWTICO`，2026-07-20，無新觀測，FRED，source_ids=monetary.wti）——持平，A 通膨鏈油價端無新推力。
- **Fed balance sheet**：≈$6.75T（原始 **6,747,378** 百萬美元，2026-07-22，無新觀測，FRED WALCL，source_ids=monetary.walcl）——量化緊縮步調持平。
- **全球央行流動性（ECB）**：ECB ≈€5.95T（原始 **5,949,077** 百萬歐元，2026-07-17，FRED ECBASSETSW，source_ids=monetary.ecb_boj）——持平。
- **全球央行流動性（BOJ）**：BOJ ≈¥639.55T（原始 **6,395,509** 億日圓，2026-06-01，FRED JPNASSETS，source_ids=monetary.ecb_boj）——持平。
- **PBoC 流動性操作**：人行 7/20 連 14 個月持穩 LPR（1Y 3.00%／5Y 3.50%）、7/24 以 1Y MLF 淨投放 ≈**¥100B**（5 個月最大、平滑稅期與政治局會議前）（2026-07-24，https://www.bloomberg.com/news/articles/2026-07-24/pboc-adds-most-liquidity-to-economy-in-five-months-to-aid-growth，source_ids=monetary.pboc）——中國端流動性偏寬（confirmation）。
- **私募信貸贖回壓力（扳機側，event-driven）**：Blackstone 於 2026-07-23 Q2 財報電話會確認 **BCRED Q2 突破 5% 季度贖回上限**——贖回需求達 ≈**10%** NAV（自 Q1 7.9% 升高）、僅約 50% 獲償並比例撥付、季內淨流出 ≈$1.2B（inflow→outflow）（2026-07-23，https://www.benzinga.com/markets/private-markets/26/07/60649546/blackstone-says-bcred-redemptions-have-materially-slowed，source_ids=monetary.private_credit_liquidity）——實際 gate proration / breach 事實成立、餵入 §3 融資扳機；惟 Blackstone 同場指 Q3 初贖回「明顯放緩」，趨勢轉緩（多基金 6 月級贖回潮之 Cliffwater 06-02、Apollo 06-23 皆落 30 日窗外，本次僅 BCRED 具窗內硬披露）。
**結論**：扳機側；BCRED Q2 gate proration（≈10% NAV 需求、50% 比例撥付、淨流出 ≈$1.2B，2026-07-23 披露）為扳機側事件，同時 HY 2.77%／IG 0.79% 史窄自滿——「自滿側 froth 與扳機側 financing 壓力同框」維持 **75**；macro 多序列持平、20Y 標售轉弱、FedWatch 偏鷹與私募信貸 Q3 轉緩相抵，故分數較前次持平、扳機側質變見「本次新增訊號」。

### 6. 結構性槓桿 — 78（weight 15%，Δ +1）
- **US 槓桿 ETF AUM**：美國槓桿 ETF 總 AUM ≈**$198B**（記錄高，TQQQ ≈$37.3B／SOXL ≈$22B（YTD +446%）領先；NVDL ≈$3.75B、TSLL ≈$3.67B）（2026-07-23，https://cryptobriefing.com/leveraged-etfs-record-198b-aum/，source_ids=structural.leveraged_etf_aum）——水位維持記錄高。
- **US 單股槓桿 ETF 核准／發行（近 30 日）**：**續加速擴散**——Tradr 7/1 上市 5 檔 2X 單股（CIEN/QNT/RMBS/TSEM/TTMI）、Leverage Shares 7/7 上市 6 檔 ±2X（Alphabet/Amazon/Meta/Apple）、Tradr SK hynix 2X/-2X 07-28 開盤（2026-07-07，https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html，source_ids=structural.us_single_stock_etf）——單股槓桿產品向二線股／科技巨頭密集擴散。
- **全球（非美）槓桿產品核准（本週）**：**本週擴散訊號未觸發**——韓／台／日／歐 07-20–07-27 無新單股槓桿／反向 ETF 核准；韓國 FSC 反於 2026-07-16 起暫停新單股槓桿 ETF 上市並加速提高保證金（收緊，https://www.bloomberg.com/news/articles/2026-07-16/south-korea-to-halt-new-listings-of-single-stock-leveraged-etfs，source_ids=structural.global_leveraged_approvals，不納入計分）——未達 2+ 非美市場同週核准、rubric floor 81 未啟動（✗ NOT DISCLOSED）。
- **0DTE 佔 SPX 期權量**：≈**56%**（2026-02-28，Cboe 記錄值、2026 全年 >45–59% 區間高檔，https://www.cboe.com/insights/posts/spx-0-dte-options-jumped-to-record-56-share-in-feb/，source_ids=structural.zero_dte）——持續 >55% 高檔。
- **Options 總量（OCC 月報）**：最新為 6 月月報（7 月報告 8 月初才發布）（2026-07-02，https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report，source_ids=structural.options_volume）——衍生品投機量續處高檔（stock-of-state 沿用）。
- **跨資產／相關性確認**：Cboe SKEW ≈**150.19**（偏高、尾端避險付溢價、較前次 146 上升）、VIX 18.58 期限結構 contango（VIX3M 20.51、IVTS 0.906）（2026-07-22，https://finance.yahoo.com/quote/%5ESKEW/history/，source_ids=structural.cross_asset_derivatives）——尾端避險升溫、整體波動平靜（confirmation）。
- **Margin debt / 市值 交叉檢核**：$1.502T、YoY +51.5%（2026-07-20，6 月數，見 D4，https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026，source_ids=structural.margin_debt_crosscheck）——確認零售槓桿頂部級別（confirmation，不在此重複計分）。
- **AI 基礎設施債務／vendor-financing loops**：過去 30 日**顯著新增**——Broadcom↔Anthropic ≈**$35B** AI 融資（BofA／Morgan Stanley 分銷）、Oracle ≈$38B 資料中心債（$23.25B 德州＋$14.75B 威州，JPM／MUFG）、Oracle 密州單一設施 $16.3B（PIMCO 錨定 ≈$10B）；循環／表外——Oracle/xAI/Meta/CoreWeave 經 SPV 移出 ≈$120B、CoreWeave 總債 ≈$24.9B（GPU 擔保、$8.5B DDTL 評 A3/A(low)、Nvidia 循環）（2026-07-12，https://www.techtimes.com/articles/320239/20260712/nvidia-circular-financing-249b-coreweave-debt-puts-pension-funds-risk.htm，source_ids=structural.ai_infrastructure_debt）——AI 基建融資規模／循環度本月同時多筆放大＝結構性槓桿升溫因子。
- **銀行對 NBFI 放款**：≈$2.01T（原始 **2,012.10** 億美元，2026-07-15，無新觀測，FRED LNFACBW027SBOG，source_ids=structural.nbfi_bank_loans）——bank–NBFI linkage 水位持平（confirmation，不主計分）。
- **美債基差交易槓桿（best-effort）**：script `cftc_lev_funds`／`move_index`／`ofr_repo` 本次 `fetch_failed`；WebSearch 未取得 7 日窗內可稽核基差交易新證據——CFTC 槓桿基金美債期貨淨空 ≈349,563 口最新為 2026-07-07（落 7 日窗外、僅作背景），MOVE 官方水位未能確認，Bloomberg 稱基差交易「sputtering」但無具日期平倉事件（✗ NOT DISCLOSED，source_ids=structural.treasury_basis_trade，不納入計分、不調 D6 分數）。
**結論**：分數由 77 升至 **78**（rubric 61–80）。0DTE 續 >55%、OCC 量高檔、US 單股槓桿產品加速擴散（Tradr 5＋Leverage Shares 6）、槓桿 ETF AUM 記錄高＝結構性槓桿高檔；本月 AI 基建融資同時多筆放大（Broadcom/Anthropic $35B、Oracle $38B＋$16.3B、表外 $120B、CoreWeave GPU 擔保 $24.9B）＝信用度／循環度升溫，SKEW 升至 150——升溫因子略多於抑制面（全球擴散未觸發、基差交易無窗內新證據），淨評較前次升 1 分。

## 綜合分數

| 維度 | 權重 | 分數 | 加權分數 |
|---|---:|---:|---:|
| 估值溢價 | 22% | 78 | 17.16 |
| 市場廣度 | 13% | 30 | 3.90 |
| 投機行為 | 18% | 58 | 10.44 |
| 散戶情緒 | 12% | 48 | 5.76 |
| 貨幣與信貸環境 | 20% | 75 | 15.00 |
| 結構性槓桿 | 15% | 78 | 11.70 |
加權總分：63.96 → 64【警戒】

邊界帶：總分 64 距 警戒/高 邊界 ≤ 2 分，評分固有噪音約 ±2–3，等級判讀需保留餘地。

## 歷史泡沫週期對比

相似度計算：checklist v2

逐項對本次六維度分數、macro/current/prior state 與附錄證據重算命中；相似度 = 命中數 ÷ 特徵數 × 100，四捨五入到最近 5%。「無資料」不計入命中但仍在分母。

- 1973/1 Nifty Fifty 頂：命中 3/8 = 40%
- 1997 早期建設：命中 4/8 = 50%
- 1998 LTCM 衝擊：命中 4/8 = 50%
- 1999 晚期狂熱：命中 4/10 = 40%
- 2000/3 頂點：命中 1/8 = 15%
- 2021/12 Meme 頂：命中 3/8 = 40%

2000/3 高位回落條件：否

**1973/1 Nifty Fifty 頂 feature audit**
- 1973.1｜未命中｜source_ids=—｜估值溢價 78 < 80
- 1973.2｜未命中｜source_ids=—｜市場廣度 30 < 60
- 1973.3｜未命中｜source_ids=—｜CPI YoY 3.46% < 4%
- 1973.4｜命中｜source_ids=—｜T5YIFR 週 Δ +1 bps ≥ 0（通膨預期未回落）
- 1973.5｜未命中｜source_ids=—｜WTI 週漲幅 0%（無新觀測）< +0.5%
- 1973.6｜未命中｜source_ids=—｜decomposition.driver=unknown ≠ breakeven（三腿視窗不一致）
- 1973.7｜命中｜source_ids=—｜扳機狀態＝已擊發 ≥ 初啟
- 1973.8｜命中｜source_ids=—｜散戶情緒 48 < 55
**1997 早期建設 feature audit**
- 1997.1｜未命中｜source_ids=—｜估值溢價 78 > 74（超出 40–74 區間）
- 1997.2｜命中｜source_ids=—｜市場廣度 30 < 45
- 1997.3｜未命中｜source_ids=—｜投機行為 58 ≥ 50
- 1997.4｜命中｜source_ids=ai.hyperscaler_capex｜hyperscaler 2026 capex 指引仍上修（Alphabet ≈$195–205B、合計 ≈$725B+）
- 1997.5｜命中｜source_ids=—｜散戶情緒 48 < 55
- 1997.6｜未命中｜source_ids=—｜結構性槓桿 78 ≥ 50
- 1997.7｜命中｜source_ids=—｜HY OAS 2.77% < 4% 且本次週 Δ 0 bps ≤ 0（未走闊）
- 1997.8｜未命中｜source_ids=—｜扳機狀態＝已擊發 ≠ 未擊發
**1998 LTCM 衝擊 feature audit**
- 1998.1｜未命中｜source_ids=structural.cross_asset_derivatives｜HY 週 Δ 0 bps < +30；SKEW 150.19、VIX 18.58 contango（無壓力事件）
- 1998.2｜未命中｜source_ids=—｜S&P `sp500_trend.chg_pct` +0.05% > −5%（無回檔）
- 1998.3｜命中｜source_ids=monetary.private_credit_liquidity｜具名非銀壓力：BCRED Q2 5% 上限突破、50% 比例撥付、淨流出 ≈$1.2B（2026-07-23 披露）
- 1998.4｜未命中｜source_ids=monetary.fedwatch｜FedWatch 7/29 ≈61% 持平／≈38% 升息、偏鷹非轉鴿
- 1998.5｜命中｜source_ids=—｜估值溢價 78 ≥ 60
- 1998.6｜命中｜source_ids=—｜扳機狀態＝已擊發 ≥ 初啟
- 1998.7｜未命中｜source_ids=—｜市場廣度 Δ = 30 − 30 = 0 < +8
- 1998.8｜命中｜source_ids=—｜ΔT10YIE −2 bps ≤ 0（通膨預期非上行）
**1999 晚期狂熱 feature audit**
- 1999.1｜命中｜source_ids=—｜估值溢價 78 ≥ 75
- 1999.2｜命中｜source_ids=valuation.sp500_pe_cape｜CAPE 40.46 ≥ 38
- 1999.3｜未命中｜source_ids=—｜投機行為 58 < 60
- 1999.4｜未命中｜source_ids=speculation.microcap_moonshots,speculation.ipo_heat｜本週 moonshot 0；無營收 IPO 佔比未達偏高
- 1999.5｜未命中｜source_ids=—｜市場廣度 30 < 45（廣度健康、非轉窄）
- 1999.6｜未命中｜source_ids=—｜D5 monetary_side＝扳機側 ≠ 自滿側，all 不成立
- 1999.7｜命中｜source_ids=—｜結構性槓桿 78 ≥ 60
- 1999.8｜未命中｜source_ids=—｜散戶情緒 48 < 55
- 1999.9｜命中｜source_ids=speculation.upcoming_ai_ipos｜巨型 AI IPO pipeline 活躍：Anthropic 續進 IPO 程序（$965B 估值，30 日內具名報導）
- 1999.10｜未命中｜source_ids=—｜扳機狀態＝已擊發 ≠ 未擊發
**2000/3 頂點 feature audit**
- 2000.1｜未命中｜source_ids=—｜估值溢價 78 < 85
- 2000.2｜命中｜source_ids=—｜扳機狀態＝已擊發 ≥ 初啟
- 2000.3｜未命中｜source_ids=—｜市場廣度 30 < 60
- 2000.4｜未命中｜source_ids=—｜prior `sp500_dev200_pct` 7.14 < +10 使第一分支為否；current chg +0.05% > −5%
- 2000.5｜未命中｜source_ids=—｜投機行為 58 < 70
- 2000.6｜未命中｜source_ids=speculation.insider_form4｜14 日內 0 件合格 Form 4 cluster
- 2000.7｜未命中｜source_ids=—｜散戶情緒 48 < 65
- 2000.8｜未命中｜source_ids=monetary.fedwatch｜FedWatch 7/29 基準情境仍為持平（≈61%）、非明確轉緊；10Y driver≠breakeven
**2021/12 Meme 頂 feature audit**
- 2021.1｜未命中｜source_ids=—｜散戶情緒 48 < 65
- 2021.2｜命中｜source_ids=retail.social_sentiment｜本週具名社群軋空：WEN（Wendy's）r/wallstreetbets 主導、單日 +25%
- 2021.3｜命中｜source_ids=—｜結構性槓桿 78 ≥ 65
- 2021.4｜未命中｜source_ids=—｜D5 monetary_side＝扳機側 ≠ 自滿側，all 不成立
- 2021.5｜命中｜source_ids=retail.margin_debt｜margin debt YoY +51.5% ≥ +40%
- 2021.6｜未命中｜source_ids=speculation.microcap_moonshots｜本週 microcap moonshot 0 < 1
- 2021.7｜未命中｜source_ids=—｜市場廣度 30 < 50
- 2021.8｜未命中｜source_ids=—｜CPI YoY 3.46% < 4%，all 不成立

**兩句解讀**：本週相似度最高為「1997 早期建設」與「1998 LTCM 衝擊」並列 50%，依 contract 錨點順序取「1997 早期建設」為最貼近——市場廣度健康（30）、hyperscaler capex 仍上修（Alphabet $205B）、散戶未狂熱（48）、HY OAS 2.77% 史窄且本週未走闊，構成「基本面建設仍在、公開信用尚未轉緊」的早期組態；惟本週扳機狀態＝已擊發（BCRED Q2 gate proration）且估值溢價 78 高企、1998 型「非銀融資扳機」同步升至 50%，機械最貼近錨與「早期」字面並不同義，實質更接近「估值高企＋非銀融資扳機、公開利差尚未反映」的中段位置，扳機鏈 A 尚未驗證啟動（driver≠breakeven、WTI 持平）。這意味循環位置介於建設與後期之間：真實技術突破吸引超商業回報所能支撐的資本（BIS AER 2026 Ch I：AI 相關投資 ≈1% of US GDP、IT 投資合計 ≈5% 已超 dot-com 峰），最須盯 AI 信用重定價（Oracle/單一發行人 CDS 走闊）、AI 基建融資規模與循環度本月放大（Broadcom/Anthropic $35B、Oracle $38B＋$16.3B、表外 $120B）與私募信貸閘門是否外溢至公開利差。長期指數成長趨勢偏離（Dot-com ≈95%、1929 ≈110%、當前 AI 週期 ≈147%；RIA/Farrell）作跨期敘事錨、不進 checklist。

## 機構情緒對照

本次無新機構調查數據。

## 本次新增訊號

比較基準：vs 前次（4天前）。

- **散戶情緒（D4）Δ -2**：情緒／擁擠度三表同步降溫——CNN F&G 41→39（續 Fear）、AAII 多方 44.9%→29.6%（2022-09 以來最低、轉空）、NAAIM 95.64→84.02（減碼）；margin debt 6 月創高（$1.502T、YoY +51.5%）與 WEN 軋空重現部分抵銷，淨降 2 分。
- **估值溢價（D1）Δ -1**：價格趨勢偏離由 +7.14% 回落至 +5.8%、Mag7 對其餘 493 檔溢價壓縮至 ≈10%（近十年最低）、CAPE 40.94→40.46 微降——估值面小幅緩和；capex 仍上修（Alphabet $205B、Q2 FCF 轉負）與 AI 信用分歧同框對沖，淨降 1 分。
- **結構性槓桿（D5→D6）Δ +1**：AI 基建融資規模／循環度本月同時多筆放大——Broadcom↔Anthropic ≈$35B、Oracle ≈$38B（德州＋威州）＋密州 $16.3B、表外 SPV ≈$120B、CoreWeave GPU 擔保總債 ≈$24.9B；US 單股槓桿 ETF 加速擴散（Tradr 5＋Leverage Shares 6）、SKEW 升至 150.19——升溫略多於抑制面（**全球（非美）擴散訊號未觸發，本週擴散訊號未觸發**，未達 2+ 非美市場同週核准；韓國 FSC 反於 07-16 起暫停新單股槓桿 ETF 上市），淨升 1 分。
- **貨幣與信貸環境（D5）＝扳機側，score Δ 0——質化新訊號（雙向 Δ 遮蔽防護）**：私募信貸扳機由具窗內硬披露延續——Blackstone 2026-07-23 Q2 財報會確認 BCRED 突破 5% 上限（贖回需求 ≈10% NAV、50% 比例撥付、淨流出 ≈$1.2B），扳機狀態維持「已擊發」；惟 Blackstone 指 Q3 初贖回「明顯放緩」、6 月多基金贖回潮（Cliffwater/Apollo）已落 30 日窗外，扳機事實成立但趨勢轉緩。分數未動因先前已因扳機側偏高（前次即 75）。
- 其餘維度（廣度 30、投機 58、貨幣 75）分數與前次持平；總分 64【警戒】、Δ 0。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | S&P 500 收盤（sp500_trend latest） | 7,411.98 | FRED SP500（sp500_trend） | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.sp500_trend | S&P 500 距 200DMA 偏離（sp500_trend dev200_pct） | +5.8% | FRED SP500（sp500_trend） | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.sp500_trend | S&P 500 距 52 週均線偏離（sp500_trend dev52w_pct） | +7.4% | FRED SP500（sp500_trend） | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| retail.household_equity_allocation | 家庭持股佔金融資產比 | 45.76 | FRED BOGZ1FL153064486Q | 2026-01-01 | 2026-07-27T09:30:00+08:00 |
| monetary.fed_funds | Fed funds 上限（DFEDTARU） | 3.75% | FRED DFEDTARU | 2026-07-26 | 2026-07-27T09:30:00+08:00 |
| monetary.fed_funds | Fed funds 下限（DFEDTARL） | 3.50% | FRED DFEDTARL | 2026-07-26 | 2026-07-27T09:30:00+08:00 |
| monetary.hy_oas | HY OAS（BAMLH0A0HYM2） | 2.77% | FRED BAMLH0A0HYM2 | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.ig_oas | IG OAS（BAMLC0A0CM） | 0.79% | FRED BAMLC0A0CM | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.dgs10 | 10Y 名目殖利率（DGS10） | 4.71% | FRED DGS10 | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.dfii10 | 10Y 實質殖利率（DFII10） | 2.43% | FRED DFII10 | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.t10yie | 10Y breakeven（T10YIE） | 2.26% | FRED T10YIE | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| monetary.wti | WTI 原油（DCOILWTICO） | $84.38 | FRED DCOILWTICO | 2026-07-20 | 2026-07-27T09:30:00+08:00 |
| monetary.cpi_yoy | CPI YoY（CPIAUCSL yoy_pct） | 3.46% | FRED CPIAUCSL | 2026-06-01 | 2026-07-27T09:30:00+08:00 |
| monetary.t5yifr | 5y5y forward（T5YIFR latest） | 2.28% | FRED T5YIFR | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| monetary.term_premium | 10Y 期限溢價（THREEFYTP10） | 0.7787% | FRED THREEFYTP10 | 2026-07-17 | 2026-07-27T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR 隔夜利率 | 3.64% | FRED SOFR | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR 99th 分位（SOFR99） | 3.72% | FRED SOFR99 | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB | 3.65% | FRED IORB | 2026-07-27 | 2026-07-27T09:30:00+08:00 |
| monetary.repo_stress_srf | SRF/隔夜 repo 操作量（RPONTTLD） | 0.001 | FRED RPONTTLD | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| monetary.walcl | Fed 資產負債表（WALCL） | 6,747,378 百萬美元（≈$6.75T） | FRED WALCL | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| monetary.ecb_boj | ECB 資產（ECBASSETSW） | 5,949,077 百萬歐元（≈€5.95T） | FRED ECBASSETSW | 2026-07-17 | 2026-07-27T09:30:00+08:00 |
| monetary.ecb_boj | BOJ 資產（JPNASSETS） | 6,395,509 億日圓（≈¥639.55T） | FRED JPNASSETS | 2026-06-01 | 2026-07-27T09:30:00+08:00 |
| structural.nbfi_bank_loans | 銀行對 NBFI 放款（LNFACBW027SBOG） | 2,012.10 億美元（≈$2.01T） | FRED LNFACBW027SBOG | 2026-07-15 | 2026-07-27T09:30:00+08:00 |

### Coverage

| source_id | 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（P/E 28.52、CAPE 40.46 @07-24） |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E | CNBC/Morgan Stanley [SEARCH]（stock-of-state 沿用） | ✓ SEARCH-VERIFIED（溢價 ≈10%、NVDA NTM ≈18.7 @07-08） |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（MS NVDA $288 EPS-driven @07-13） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500 派生） | ✓ API（dev200 +5.8%／dev52 +7.4%） |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧 | 信用市場 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（AI 單一發行人利差走闊 vs CDX IG 平穩 @07-16） |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst/portfolioslab [SEARCH] | ✓ SEARCH-VERIFIED（RSP +12.39% YTD、領先 SPY ≈+5pp @07-24） |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | P&I/RBC [SEARCH] | ✓ SEARCH-VERIFIED（≈37%，自 2025 ≈41% 回落） |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth [SEARCH] | ✓ SEARCH-VERIFIED（A/D 線 12 月新高、新高家數轉薄 @07-21） |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH]（403，經 MacroMicro） | ✓ SEARCH-VERIFIED（39 Fear @07-24） |
| retail.margin_debt | 散戶｜Margin Debt: FINRA | FINRA/Advisor Perspectives [SEARCH]（月頻 stock-of-state） | ✓ SEARCH-VERIFIED（$1.502T、+51.5% YoY、2026-06 創高） |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（Bull 29.6%／Bear 42.3% @07-23） |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB/cashtag [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（WEN 軋空 +25% @07-25） |
| retail.household_equity_allocation | 散戶｜Household equity allocation | fetch_macro.py BOGZ1FL153064486Q | ✓ API（45.76% @2026-Q1） |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim/YCharts [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（84.02 @07-22） |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM | 賣方調查 [SEARCH]（月頻，best-effort） | ✗ NOT DISCLOSED（7 月 FMS 07-14 發布，早於前次基準、非本次新增） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED DFEDTARU/DFEDTARL | fetch_macro.py FRED API | ✓ API（3.75%/3.50% @07-26） |
| monetary.hy_oas | 貨幣｜High Yield OAS | fetch_macro.py FRED API | ✓ API（2.77% @07-23，Δ0） |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | fetch_macro.py FRED API | ✓ API（0.79% @07-23，Δ0） |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | fetch_macro.py FRED API | ✓ API（4.71% @07-23，no_new_obs） |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield | fetch_macro.py FRED API | ✓ API（2.43% @07-23，no_new_obs） |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | fetch_macro.py FRED API | ✓ API（2.26% @07-24，Δ−2bps） |
| monetary.wti | 貨幣｜WTI crude oil price | fetch_macro.py FRED API | ✓ API（$84.38 @07-20，no_new_obs） |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED | fetch_macro.py FRED API（月頻） | ✓ API（3.46% @2026-06） |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | fetch_macro.py FRED API | ✓ API（2.28% @07-24，Δ+1bps） |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED | fetch_macro.py FRED API | ✓ API（0.7787% @07-17，≈0bps） |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py repo_stress | ✓ API（SOFR−IORB −1bps、SOFR99−IORB +7bps、SRF ≈$0 @07-23/24） |
| monetary.treasury_auctions | 貨幣｜美債標售需求 | Reuters/investinglive [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（20Y HY 5.163%、tail +0.5bp、D+ @07-22） |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（7/29 ≈61% 持平/≈38% 升息 @07-25） |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED WALCL | fetch_macro.py FRED API | ✓ API（$6.75T @07-22，no_new_obs） |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | fetch_macro.py FRED API | ✓ API（€5.95T @07-17／¥639.55T @06-01） |
| monetary.pboc | 貨幣｜PBoC aggregate financing | fxstreet/Bloomberg [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（LPR 持穩、MLF 淨投放 ¥100B @07-24） |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（BCRED Q2 5% 上限突破、50% 比例撥付 @07-23） |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報 [SEARCH]（stock-of-state） | ✓ SEARCH-VERIFIED（Alphabet ≈$195–205B、合計 ≈$725B+、仍上修） |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic/OpenAI/Google [SEARCH]（best-effort） | ✗ NOT DISCLOSED（本季無乾淨量化成長率披露） |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch/報導 [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Anthropic ≈$47B／OpenAI ≈$25B run-rate） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration | 財報電話 [primary: SEARCH]（best-effort） | ✗ NOT DISCLOSED（本次無乾淨窗內一手 RPO 披露） |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（DRAM +13–18% QoQ 3Q26 @07-03；供給仍被吸收） |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構 | 季報/發債 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口 | 組合披露 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（年化 capex ≈$725B vs 終端營收低百億級） |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K/10-Q [primary: SEARCH]（best-effort，30日） | ✗ NOT DISCLOSED（過去 30 日無新變更） |
| ai.capital_cycle | AI｜資本週期階段 | 供需增速+進出場事件 [SEARCH]（best-effort） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days +AI rename/SPAC | [SEARCH] | ✓ SEARCH-VERIFIED（2 件 SPAC：BRTMU/SCATU @07-21） |
| speculation.ipo_heat | 投機｜IPO market heat | Renaissance [SEARCH] | ✓ SEARCH-VERIFIED（IPO Index +16.7% YTD、pipeline @07-23） |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz/Benzinga [primary: SEARCH]（required 週螢幕） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | S-1/具名報導 [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Anthropic IPO 程序 $965B @07-15） |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership | SEC EDGAR [primary: EDGAR]（required） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe/YCharts [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（0.61 @07-23） |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing/etf.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（總 ≈$198B @07-23） |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | Tradr/Leverage Shares [SEARCH] | ✓ SEARCH-VERIFIED（Tradr 5＋Leverage Shares 6 @07-01/07-07） |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX/TWSE/JPX/ESMA [SEARCH]（best-effort，7日） | ✗ NOT DISCLOSED（本週擴散訊號未觸發；韓國反收緊） |
| structural.zero_dte | 結構｜0DTE option volume | Cboe [SEARCH]（Cboe 403） | ✓ SEARCH-VERIFIED（≈56%，Cboe @2026-02） |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com [SEARCH] | ✓ SEARCH-VERIFIED（6 月月報，7 月待發 @07-02） |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe/Yahoo [SEARCH] | ✓ SEARCH-VERIFIED（SKEW 150.19、VIX 18.58 contango @07-22） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 D4（confirmation） | ✓ SEARCH-VERIFIED（$1.502T/+51.5% YoY，D4 引用不重複計分） |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]（best-effort，30日） | ✓ SEARCH-VERIFIED（Broadcom/Anthropic $35B、Oracle $38B＋$16.3B @07 內） |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | fetch_macro.py FRED API | ✓ API（$2.01T @07-15，no_new_obs） |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | script→WebSearch [primary: script]（best-effort） | ✗ NOT DISCLOSED（cftc/move/ofr script fetch_failed，WebSearch 無 7 日窗內基差交易新證據） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 28.52 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 40.46 | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 對其餘 493 溢價 ≈10%、NVDA NTM ≈18.7 | Magnificent 7 valuation premium cheapest decade July 2026 | https://www.cnbc.com/2026/07/08/magnificent-seven-stocks-are-the-cheapest-in-a-decade-by-one-measure.html | 2026-07-08 | 2026-07-27T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | MS NVDA 目標 $288（≈22× EPS、target PE 未擴張、EPS-driven） | Morgan Stanley NVDA target 288 July 2026 EPS | https://www.gurufocus.com/news/8955458/morgan-stanley-upgrades-nvidia-nvda-with-a-288-target-price | 2026-07-13 | 2026-07-27T09:30:00+08:00 |
| valuation.ai_credit_schism | AI 單一發行人利差走闊 vs CDX IG 平穩、hyperscaler 2026 發債 ≈$182B | AI issuer credit spread CDS widening vs CDX IG July 2026 | https://247wallst.com/investing/2026/07/16/the-ai-revolution-is-reshaping-credit-markets-here-is-what-it-really-says-about-risk/ | 2026-07-16 | 2026-07-27T09:30:00+08:00 |
| breadth.rsp_spy | RSP +12.39% YTD、領先 SPY ≈+5pp | RSP vs SPY equal weight YTD 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 ≈37% | S&P 500 top 10 concentration percent 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/ | 2026-07-15 | 2026-07-27T09:30:00+08:00 |
| breadth.advance_decline | NYSE A/D 線 12 月新高、新高家數轉薄 78 vs 175 | NYSE advance decline new highs July 2026 | https://research.leutholdgroup.com/categories/nyse-advancedecline.1440 | 2026-07-21 | 2026-07-27T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 39（Fear） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/series/22748/cnn-fear-and-greed | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt $1.502T、+51.5% YoY（6 月創高） | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-07-27T09:30:00+08:00 |
| retail.aaii | AAII Bull 29.6%／Bear 42.3% | AAII investor sentiment survey July 23 2026 | https://www.aaii.com/sentimentsurvey | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| retail.social_sentiment | WEN（Wendy's）r/wallstreetbets 軋空 +25% | WEN Wendys wallstreetbets short squeeze July 2026 | https://altindex.com/wallstreetbets | 2026-07-25 | 2026-07-27T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 84.02 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| monetary.treasury_auctions | 20Y HY 5.163%、tail +0.5bp、dealer takedown 14.67%、D+ | US Treasury 20Y auction July 22 2026 tail bid to cover | https://investinglive.com/news/us-treasury-auctions-off-13-billion-of-20-year-bonds-at-a-high-yield-of-5-163 | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 ≈61% 持平／≈38% 升息、偏鷹 | CME FedWatch July 29 2026 hike hold probability | https://www.cnbc.com/2026/07/13/-a-july-rate-hike-from-the-fed-the-odds-are-rising.html | 2026-07-25 | 2026-07-27T09:30:00+08:00 |
| monetary.pboc | 人行 LPR 持穩、MLF 淨投放 ¥100B | PBoC MLF net injection LPR July 2026 | https://www.bloomberg.com/news/articles/2026-07-24/pboc-adds-most-liquidity-to-economy-in-five-months-to-aid-growth | 2026-07-24 | 2026-07-27T09:30:00+08:00 |
| monetary.private_credit_liquidity | [private_credit_gate] BCRED Q2 突破 5% 上限、贖回 ≈10% NAV、50% 比例撥付、淨流出 ≈$1.2B | Blackstone BCRED Q2 2026 redemption 5% cap breach proration | https://www.benzinga.com/markets/private-markets/26/07/60649546/blackstone-says-bcred-redemptions-have-materially-slowed | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex：Alphabet 上修至 ≈$195–205B、合計 ≈$725B+ | Alphabet raises 2026 capex 205B Q2 hyperscaler | https://mlq.ai/news/alphabet-raises-2026-capex-guidance-to-195-205b-cloud-revenue-surges-82/ | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic ≈$47B／OpenAI ≈$25B run-rate | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-06-15 | 2026-07-27T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約 +13–18% QoQ、交期 30–40+ 週 | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html | 2026-07-03 | 2026-07-27T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] Alphabet FY26 capex 上修至 ≈$205B、Q2 FCF 轉負（−$5.9B） | Alphabet capex 205B Q2 2026 FCF negative debt | https://mlq.ai/news/alphabet-raises-2026-capex-guidance-to-195-205b-cloud-revenue-surges-82/ | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] AI 相關 IG 發債累計 ≈$218–250B（測試投資人胃納） | AI bond issuance 250B July 2026 hyperscaler | https://www.morningstar.com/bonds/bond-issuance-backing-ai-investment-tops-250b-testing-limits-voracious-investor-demand | 2026-07-08 | 2026-07-27T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex ≈$725B vs AI 終端營收低百億級 | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-06-15 | 2026-07-27T09:30:00+08:00 |
| speculation.ai_rename_spac | 2 件合格 SPAC：BRTMU $325M（AI-target）、SCATU $100M | SPAC IPO announcement July 21 2026 AI | https://www.boardroomalpha.com/research/spac-market-update-july-21-2026-cdaq | 2026-07-21 | 2026-07-27T09:30:00+08:00 |
| speculation.ipo_heat | Renaissance IPO Index +16.7% YTD、pipeline 建置 | US IPO market 2026 Renaissance IPO index YTD | https://www.renaissancecapital.com/IPO-Center/Stats | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot 件數 0 | microcap 100% single day quantum AI fusion moonshot July 2026 | Finviz/Benzinga/StockTwits/Yahoo movers screener | 2026-07-27 | 2026-07-27T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 程序 $965B、OpenAI 傳目標 9 月 | Anthropic OpenAI IPO July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html | 2026-07-15 | 2026-07-27T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 cluster 件數 0（僅零星 10b5-1：PLTR 07-15、META 07-20） | insider Form 4 cluster AI leaders July 2026 openinsider | SEC EDGAR / openinsider（一手 URL 無法取得） | 2026-07-27 | 2026-07-27T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.61 | Cboe equity put call ratio July 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM ≈$198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-07-23 | 2026-07-27T09:30:00+08:00 |
| structural.us_single_stock_etf | Tradr 5 檔 2X 單股、Leverage Shares 6 檔 ±2X | single-stock leveraged ETF launch July 2026 Tradr Leverage Shares | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html | 2026-07-07 | 2026-07-27T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX ≈56%（Cboe 記錄） | 0DTE SPX options share volume 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jumped-to-record-56-share-in-feb/ | 2026-02-28 | 2026-07-27T09:30:00+08:00 |
| structural.options_volume | OCC 6 月月報（7 月待發） | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report | 2026-07-02 | 2026-07-27T09:30:00+08:00 |
| structural.cross_asset_derivatives | [snapshot] Cboe SKEW 150.19、VIX 18.58 contango | VIX term structure SKEW July 2026 | https://finance.yahoo.com/quote/%5ESKEW/history/ | 2026-07-22 | 2026-07-27T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt $1.502T、+51.5% YoY（cross-ref D4） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-07-27T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Broadcom/Anthropic $35B、Oracle $38B＋密州 $16.3B、CoreWeave GPU 擔保 $24.9B | AI data center debt financing July 2026 Broadcom Anthropic Oracle CoreWeave | https://www.techtimes.com/articles/320239/20260712/nvidia-circular-financing-249b-coreweave-debt-puts-pension-funds-risk.htm | 2026-07-12 | 2026-07-27T09:30:00+08:00 |

## 本次分數存檔
```json
{
  "date": "2026-07-27",
  "iso_week": "2026-W31",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "valuation": 78,
  "breadth": 30,
  "speculation": 58,
  "retail": 48,
  "monetary": 75,
  "structural": 78,
  "total": 64,
  "tier": "警戒",
  "regime": "穩定共存",
  "trigger_state": "已擊發",
  "trigger_reasons": [
    "private_credit_gate"
  ],
  "monetary_side": "扳機側",
  "hy_oas_widening_streak": 0,
  "sp500_dev200_pct": 5.8
}
```

本報告為相對風險溫度計，非擇時訊號。

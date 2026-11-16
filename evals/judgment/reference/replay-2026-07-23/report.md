# 2026-07-23 市場泡沫風險評估報告
> 報告日期：2026-07-23；執行日：2026-07-23 Asia/Taipei；ISO 週次：2026-W30；前次基準：report-2026-07-20（3天前）

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
| S&P 500 | 7,498.96 | ▲ +0.75%（前次 ≈7,443.28） |
| WTI 原油 | $84.38 /bbl | 持平 0%（無新觀測，前次 ≈$84.38） |
| 10Y Treasury | 4.63% | ▲ +3 bps（前次 ≈4.60%） |

**三者狀態**：穩定共存——三者本次未見同向拉伸；S&P ▲ +0.75%、10Y ▲ +3 bps 皆小幅上行，WTI 持平（無新觀測），S&P `dev200_pct` ≈+7.14%（< +10% 拉伸門檻），故未升為同向偏高。資產面平靜與非銀融資扳機（私募信貸 gate）並存，須分開判讀。
- 股市：≈7,498.96（S&P 500，2026-07-22 收）；較前次 ▲ +0.75%（前次 ≈7,443.28）；距 200 日均線 +7.14%、距 52 週均線 +8.8%——價格延伸較前次微升、非急拉。
- WTI 原油：≈$84.38/bbl（2026-07-20，無新觀測）；較前次 持平 0%（前次 ≈$84.38）。
- 10Y 殖利率：4.63%（2026-07-21）；較前次 ▲ +3 bps（前次 ≈4.60%）；主要驅動：三腿視窗不一致（driver=unknown）。
**格局轉變**：前次格局＝穩定共存（讀自 report-2026-07-20 的 `regime`）→ 本次格局＝穩定共存；S&P 與 10Y 由前次的回落／持平轉為小幅上行，惟 WTI 持平（無新觀測）且價格延伸未達門檻，三者仍屬小幅／持平的穩定共存。
**10Y 成因拆解**：拆的是週變動（bps）、非水位（`ΔDGS10 ≈ ΔDFII10 + ΔT10YIE`）；三腿視窗不一致（`decomposition.driver=unknown`——ΔT10YIE 取自較新視窗、恆等式不跨視窗成立，三腿均有新觀測 freshness=updated），判定 不可判（視窗不一致）；三腿實際 signed 週變動如下：
- ΔDGS10 名目殖利率週變動：+3 bps
- ΔDFII10 實質殖利率週變動：+2 bps
- ΔT10YIE 損益平衡通膨週變動：+3 bps
- 判定：不可判（視窗不一致）
**扳機鏈**：A 通膨鏈（油 → 通膨預期 → Fed 受限 → refinancing 成本）本週未加速——WTI 持平（≈$84.38，無新觀測）、實現通膨續處高位且通膨預期微升未回落：[monetary.cpi_yoy] CPIAUCSL yoy_pct=3.46 data_date=2026-06-01（6 月）、5y5y forward [monetary.t5yifr] T5YIFR latest=2.26 delta_bps=4 data_date=2026-07-22（週 +4 bps）；CME FedWatch 7/29 會議 ≈83.4% 持平（2026-07-21），Fed 仍受 3.46% 通膨與財政供給牽制、Fed put 可得性中性；無當期電價／能源瓶頸新報導。B 槓桿鏈（衝擊：財政風險再定價 → NBFI 去槓桿 → margin spiral → 國債市場失序 → 官方市場功能回應）乾柴堆積但未點火——衝擊節點：10Y 期限溢價 THREEFYTP10 ≈0.7787%（序列自身 trailing ≈7d ≈0 bps、本週未再上行）、7/22 20Y 標售僅小幅 tail（bid-to-cover 2.64、略低於均值），財政再定價壓力溫和；NBFI 節點：script `cftc_lev_funds`／`move_index`／`ofr_repo` 本次 fetch_failed，WebSearch 補得 ^MOVE 74.67（2026-07-21、週 +2.8%、中性偏低）、CFTC 槓桿基金淨空 ≈72,603 口（07-07、較前週小幅回補），無基差／swap-spread 平倉報導；官方回應節點：`repo_stress` SOFR−IORB −4 bps、SOFR99−IORB +4 bps、SRF 動用 $0（無失序）。real-rate 主導的異常 10Y 上行本週不存在（ΔDGS10 僅 +3 bps）。本鏈證據 best-effort，本週無基差交易槓桿新積累／釋放事件。
**扳機理由**：private_credit_gate
⚠ **結論**：扳機狀態：已擊發——本次續命中「私募信貸 gate proration / breach」：Q2 2026（季末 6/30）多檔非交易 BDC／私募信貸區間基金贖回需求遠超 5% 季度上限並比例撥付（Blue Owl OCIC 贖回需求 ≈18.8% NAV 於 5% 上限比例撥付、每筆僅獲償 ≈27%；Blue Owl OTIC ≈38.1% 需求同遭比例撥付；Blackstone BCRED Q2 贖回峰值 ≈12% NAV；BofA 定調 Q2 為贖回高峰，詳 §D5／本次新增訊號），此為 1998 LTCM 型「融資扳機」特徵——非銀信用先於公開 mark-to-market 利差（HY 2.69%／IG 0.78% 仍史窄）出現一階壓力。三者配置歷史意義：估值＋槓桿＝崩跌位能，融資緊縮＝時點扳機；本週三角資產面小幅上行仍屬穩定共存，惟公開利差自滿與非銀融資扳機仍並存（自滿側 froth 與扳機側 financing 壓力同框），槓桿鏈 B 未點火，失序仍屬結構化產品閘門層級、非國債市場層級。

## 六維度評分

### 1. 估值溢價 — 79（weight 22%，Δ 0）
- **S&P 500 trailing P/E** ≈**28.85**（2026-07-22，https://www.multpl.com/s-p-500-pe-ratio，source_ids=valuation.sp500_pe_cape）——較前次 32.08 下移（隨 Q2 財報季實現盈餘更新、分母 E 上修），惟仍遠高於長期中位（≈16–19）。
- **Shiller CAPE** ≈**40.94**（2026-07-22，https://www.multpl.com/shiller-pe，source_ids=valuation.sp500_pe_cape）——較前次 41.52 幾近持平，仍逼近歷史高（≈44）、遠高於長均 ≈32。
- **Excess CAPE Yield（ECY）** ≈**0.07%**（`1/40.94 − 2.37/100`，derived 自 CAPE 40.94 與 DFII10 2.37%，2026-07-22，source_ids=valuation.sp500_pe_cape）——仍接近 0，屬 1929／2000 級別股相對債極貴訊號（confirmation，不主計分）。
- **Mag 7 加權 P/E** trailing ≈**40**（2026-05-15，https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026，source_ids=valuation.mag7_multiples）——絕對高，對 S&P 溢價為近十年較窄區（stock-of-state 沿用）。
- **價格趨勢偏離（Farrell #1/#2/#4）** S&P 距 200 日均線 **+7.14%**、距 52 週均線 +8.8%（`sp500_trend`，2026-07-22，FRED SP500，source_ids=valuation.sp500_trend）——較前次 +6.73% 微升，價格延伸壓力略增但未達 +10% 拉伸門檻，與 P/E／CAPE 互補、不重複計分。
- **AI capex 現實檢核**：hyperscaler 2026 capex 指引續上修——Alphabet 7/22 Q2 財報將 FY26 capex 上修至 ≈**$205B**（四家合計 ≈$725B+）（2026-07-22，https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html，source_ids=ai.hyperscaler_capex）——基本面敘事仍撐估值（MSFT／META 7/29、AMZN 7/30 才公布，本次為 Alphabet 硬數據）。
- **AI compute 供需現實檢核**：伺服器 DRAM 3Q26 合約 **+13–18% QoQ**（TrendForce，2026-07-09，https://www.trendforce.com/presscenter/news/20260709-13140.html，source_ids=ai.compute_supply_demand）、AI server 需求續撐記憶體但 TrendForce 提示漲幅將趨緩——供給仍被合約與 token 需求吸收、缺口未成形，惟首現降溫語氣。
- **AI 營收對 capex 缺口現實檢核**：分母年化 capex ≈**$725B**（分母：top-4＋Oracle）vs 分子已披露 AI 終端年化營收（Anthropic ≈$47B、OpenAI ≈$25B run-rate）量級缺口仍逾 10× 且 capex 續升（2026-05-15，https://epoch.ai/data-insights/anthropic-openai-revenue，source_ids=ai.revenue_capex_gap）——回本假設後移，屬估值風險上修的質化依據（缺口未收斂）。
- **Hyperscaler 融資結構（capex vs FCF / 發債）**：event_scan——Amazon 7/7 啟動 ≥**$25B** 八檔期債（AI 基建/資料中心，2026 累計發債 ≈$89B）；quarterly_state——Alphabet FY26 capex 上修至 ≈$205B、債務融資佔比續升（2026-07-07，https://finance.yahoo.com/technology/ai/articles/bond-issuance-backing-ai-investment-135635215.html，source_ids=ai.hyperscaler_financing_mix）——capex 愈靠發債支撐、同份 guidance 脆弱性上升（BIS Bulletin 120，confirmation，不主計分）。
- **AI 信用定價分歧（equity-vs-credit schism）**：Oracle 5yr CDS ≈**198 bp**（歷史紀錄新高、續走闊）、CoreWeave 5yr CDS ≈665 bp vs CDX.NA.IG 基準數十 bp（2026-07-20，https://bondblox.com/news/oracles-5y-cds-spread-hits-all-time-highs，source_ids=valuation.ai_credit_schism）——AI 發行人利差為 IG 基準數倍且續走闊、股價未跟＝後期訊號側（confirmation，不主計分）。
- **TP-upgrade phase signal**：本季（Q3 2026）具名賣方升評屬 **EPS-driven**——Morgan Stanley NVDA 目標 $288（≈22× CY27 EPS $13.08、target PE 未擴張）（2026-07-13，https://www.gurufocus.com/news/8955458/morgan-stanley-upgrades-nvidia-nvda-with-a-288-target-price，source_ids=valuation.analyst_tp_decomposition）——升評由 E 而非 multiple 主導，屬相對緩和訊號（confirmation，不主計分）。
- **折舊年限變動（盈餘品質）**：過去 30 日無新 10-K／10-Q 折舊年限或殘值假設變更披露（財報季 7/29–7/30 才啟）（✗ NOT DISCLOSED，source_ids=ai.depreciation_life，不納入計分）。
- **backlog 重複計算風險（RPO double-counting）**：本次無新一手客戶集中度／RPO 披露具乾淨窗內資料日（MSFT RPO 更新落 7/29）（✗ NOT DISCLOSED，source_ids=ai.customer_concentration_rpo，不納入計分）。
- **資本週期階段**：event_scan 見進入者／壓力事件（SoftBank SB Neo、Nebius 選賣）但 quarterly_state 供需增速證據不足、本次不判定週期階段（✗ NOT DISCLOSED，source_ids=ai.capital_cycle，不納入計分）。
**結論**：分數維持 **79**（rubric 高位）。P/E 隨盈餘更新降至 28.85、CAPE 40.94 幾近持平、趨勢偏離 +7.14% 微升，capex 續上修（Alphabet $205B）與 TP 升評 EPS-driven 屬緩和面；惟 Mag7 高檔、ECY 近 0、AI 信用分歧（Oracle CDS 紀錄新高）與發債融資佔比續升同框對沖——正負相抵，較前次持平。

### 2. 市場廣度 — 30（weight 13%，Δ 0）
- **RSP（等權）vs SPY（市值權）YTD**：RSP ≈**+11.8%** vs SPY ≈+9.4%（2026-07-21，https://portfolioslab.com/tools/stock-comparison/RSP/SPY，source_ids=breadth.rsp_spy）——等權仍領先市值權 ≈+2.4 pp，廣度結構偏健康／轉寬方向，惟領先幅度較前次 +3.2 pp 收斂。
- **Top-10 集中度**：≈**36.40%**（2026-07-02，MacroMicro/State Street 持股，https://en.macromicro.me/collections/34/us-stock-relative/123442/us-sp-500-top-10-companies-total-market-cap-and-share，source_ids=breadth.top10_concentration）——絕對偏高但較年底 ≈41% 已回落、持平於中 30% 區。
- **Advance/Decline 與新高/新低**：2026-07-22（大型科技財報前 risk-off）市場廣度轉弱、下跌家數約為上漲 1.8 倍、新低多於新高（https://ts2.tech/en/nasdaq-ends-flat-as-market-breadth-remains-thin-ahead-of-big-tech-earnings/，source_ids=breadth.advance_decline）——單週日內廣度轉負，惟屬財報前觀望、非中期結構破壞。
**結論**：分數維持 **30**（rubric 21–40 偏健康端）。等權仍領先市值權（+2.4 pp）為結構性健康主訊號，Top-10 ≈36.4% 持平；本週日內 A/D 轉弱與領先幅度收斂為殘餘負面，但未構成結構性轉窄——淨評與前次持平。

### 3. 投機行為 — 58（weight 18%，Δ 0）
- **+AI 改名／SPAC**：過去 7 日（07-16–07-23）**0 件**具名合格改名/SPAC（IQMX de-SPAC、Quantum Leap SPAC 皆為 07-01/02、落窗外；2026-07-23 螢幕）——✓ SEARCH-VERIFIED（0 件）（source_ids=speculation.ai_rename_spac）。
- **IPO 熱度**：2026 YTD ≈**203** 檔（+6.84% YoY）、募資 ≈$141.2B（近 2021 紀錄 $142.4B，含 SK Hynix $26.5B 交叉掛牌；Jersey Mike's 07-20 啟動路演）（2026-07-22，https://stockanalysis.com/ipos/2026/，source_ids=speculation.ipo_heat）——市場活躍、秩序尚可。
- **Microcap thematic moonshots**：本週 **0 件**合格（<$1B 市值、單日 ≥100% 或 2–3 日 ≥50%、堆疊 2+ 熱主題＋弱基本面；2026-07-23 螢幕）——✓ SEARCH-VERIFIED（0 件）（source_ids=speculation.microcap_moonshots）；最接近者 AMFN（fusion+defense、pre-revenue）單日 ≈+58% 未達 ≥100% 單日門檻、亦非 2–3 日持續 ≥50%，不合格。
- **Upcoming AI mega-IPO pipeline**：**Anthropic 續進 IPO 程序**（估值 ≈$965B、confidential S-1、投資人會議、可能 10 月掛牌），OpenAI 傳延至 2027（2026-07-15，https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html，source_ids=speculation.upcoming_ai_ipos）——30 日內具名巨型 AI IPO pipeline 活躍、液性抽離風險（投機 pipeline 升溫的質化依據）。
- **Insider selling clusters**：required 螢幕已執行（2026-07-23 螢幕）；14 日內（07-09–07-23）無合格「Form 4 cluster」——CoreWeave McBee 07-13 售 ≈$16.7M 為單一內部人 10b5-1、CEO Intrator 最大筆 07-07 落窗外，未構成多內部人窗內 cluster——**0 件合格**（✓ SEARCH-VERIFIED（0 件），source_ids=speculation.insider_form4）。
- **Cboe equity-only put/call**：≈**0.65**（2026-07-21，https://ycharts.com/indicators/cboe_equity_put_call_ratio，source_ids=speculation.equity_put_call）——call 偏重、較前次 0.73 略降（方向性投機略升），未破 0.50 極端（confirmation，不主計分）。
- **社交情緒代理**：本週（07-16–07-23）無具名主導迷因軋空事件（WEN 軋空高峰於 6 月底、已落窗外）（✗ NOT DISCLOSED，source_ids=retail.social_sentiment，不納入計分）。
**結論**：分數維持 **58**（rubric 41–60「投機升溫」）。本週 +AI 改名 0 件（較前次減）、moonshot 0（AMFN 近門檻未達）、insider 無合格 cluster；惟 IPO record 步調、Anthropic $965B pipeline 續熱、put/call 0.65 call 偏重——正負相抵，投機體感與前次持平。

### 4. 散戶情緒 — 50（weight 12%，Δ 0）
- **CNN Fear & Greed**：≈**41「Fear」**（2026-07-21，經 en.macromicro.me 鏡像；cnn.com 直抓 WAF 403，https://en.macromicro.me/series/22748/cnn-fear-and-greed，source_ids=retail.fear_greed）——較前次 37「Fear」微升、仍處恐懼區，散戶未亢奮。
- **Margin Debt**：**$1.416T、YoY +53.7%、MoM +8.5%（2026-05-31，記錄高）**（https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra，source_ids=retail.margin_debt）——月頻 stock-of-state；6 月數陸續發布（初值續創高、約 $1.5T 級）但跨源數值待校，本次沿用已確認之 5 月值；YoY +53.7% 屬 1999／2007／2021 頂部級別警訊。
- **AAII 散戶調查**：**Bull 44.9%**（2026-07-15，較長均 37.5% 偏多；07-22 週新值尚未發布）（https://www.aaii.com/sentimentsurvey，source_ids=retail.aaii）——多方仍偏高、樂觀未退。
- **家庭持股佔金融資產比**：**45.76%**（`BOGZ1FL153064486Q`，2026-01-01 資料日，FRED，source_ids=retail.household_equity_allocation）——歷史高位、後續加碼空間有限（Farrell #5，季頻沿用、不計週 Δ）。
- **NAAIM Exposure Index**：**95.64**（2026-07-15，https://en.macromicro.me/series/20540/naaim-exposure-index，source_ids=retail.naaim）——主動經理人曝險接近滿倉＝擁擠多頭（Farrell #9，confirmation cross-check，不主計分）。
**結論**：分數維持 **50**（rubric 41–60 下緣）。CNN F&G 續處 Fear（37→41 微升但未脫恐懼區）、AAII 偏多（Bull 44.9%）、NAAIM 近滿倉方向相抵；margin debt 仍頂部級別、家庭持股高位——淨評與前次持平。

### 5. 貨幣與信貸環境 — 75（weight 20%，Δ 0）
- **Fed funds rate**：目標區間 **3.50–3.75%**（`DFEDTARU` 3.75%／`DFEDTARL` 3.50%，2026-07-22，FRED，source_ids=monetary.fed_funds）——無變動。
- **市場隱含路徑（CME FedWatch，best-effort）**：7/29 會議 ≈**83.4%** 持平（2026-07-21，https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch，source_ids=monetary.fedwatch）——本次會議幾無降息定價、Fed 寬鬆空間受限（缺值不調分）。
- **Realized inflation vs expectations**：CPI YoY **3.46%**（`CPIAUCSL`，2026-06-01，FRED，source_ids=monetary.cpi_yoy）仍高於 2% 目標、5y5y forward **2.26%**（`T5YIFR`，2026-07-22，週 Δ +4 bps，FRED，source_ids=monetary.t5yifr）微升——通膨黏著、Fed 約束未鬆。
- **10Y 期限溢價（term premium）**：`THREEFYTP10` **0.7787%**（2026-07-17，Kim-Wright 三因子模型，序列自身 trailing ≈7d ≈0 bps，FRED，source_ids=monetary.term_premium）——財政風險再定價本週未再上行、維持溫和高位。
- **repo 資金壓力（SOFR−IORB）與 SRF 動用**：`repo_stress`——SOFR **3.61%**（2026-07-21）、IORB 3.65%（2026-07-23）、SOFR−IORB **−4 bps**；SOFR99 3.69%（2026-07-21）、SOFR99−IORB +4 bps；RPONTTLD／SRF 動用 **$0**（2026-07-22，FRED SOFR/SOFR99/IORB/RPONTTLD，source_ids=monetary.repo_stress_srf）——secured-funding 無壓力、SRF 未動用。
- **美債標售需求（auction，best-effort）**：7/22 20Y 標售 bid-to-cover **2.64**（略低於均值 2.65）、僅小幅正 tail（≈0.5 bp）、dealer takedown 略升（2026-07-22，https://www.rttnews.com/3669412/twenty-year-bond-auction-attracts-average-demand.aspx，source_ids=monetary.treasury_auctions）——長端需求偏軟但非標售失敗、財政供給壓力事件溫和（confirmation；缺值不調分）。
- **HY OAS**：**2.69%**（`BAMLH0A0HYM2`，2026-07-21，週 Δ 0 bps，FRED，source_ids=monetary.hy_oas）——接近循環低、極窄、自滿側訊號（連續走闊 streak 歸零）。
- **IG OAS**：**0.78%**（`BAMLC0A0CM`，2026-07-21，週 Δ 0 bp，FRED，source_ids=monetary.ig_oas）——史窄、信用自滿。
- **10Y nominal 週變動拆解**：ΔDGS10 +3 bps ≈ ΔDFII10 +2 bps ＋ ΔT10YIE +3 bps（三腿視窗不一致、driver=unknown）；`DGS10` **4.63%**（2026-07-21，FRED，source_ids=monetary.dgs10）、`DFII10` **2.37%**（2026-07-21，source_ids=monetary.dfii10）、`T10YIE` **2.28%**（2026-07-22，source_ids=monetary.t10yie）——殖利率小幅上行、估值折現／再融資壓力略增（詳 §3）。
- **WTI 原油**：**$84.38**/bbl（`DCOILWTICO`，2026-07-20，無新觀測，FRED，source_ids=monetary.wti）——持平，A 通膨鏈油價端無新推力。
- **Fed balance sheet**：≈$6.74T（原始 **6,743,028** 百萬美元，2026-07-15，無新觀測，FRED WALCL，source_ids=monetary.walcl）——量化緊縮步調持平。
- **全球央行流動性（ECB）**：ECB ≈€5.95T（原始 **5,949,077** 百萬歐元，2026-07-17，FRED ECBASSETSW，source_ids=monetary.ecb_boj）——持平。
- **全球央行流動性（BOJ）**：BOJ ≈¥639.55T（原始 **6,395,509** 億日圓，2026-06-01，FRED JPNASSETS，source_ids=monetary.ecb_boj）——持平。
- **PBoC 流動性操作**：人行 2026-07-14 以 6 個月買斷式逆回購淨投放 ≈**1.4** 兆元（≈$207B、該工具紀錄量，平滑稅期與債券發行）（https://english.news.cn/20260714/2d460c4227c244f1bf930993be469262/c.html，source_ids=monetary.pboc）——中國端流動性偏寬（confirmation）。
- **私募信貸贖回壓力（扳機側，event-driven）**：Q2 2026（季末 6/30）多檔非交易 BDC／私募信貸區間基金贖回需求遠超 5% 季度上限並比例撥付——Blue Owl OCIC 贖回需求 ≈**18.8%** NAV 於 5% 上限比例撥付、每筆僅獲償 ≈27%（2026-07-02，https://www.investing.com/news/stock-market-news/blue-owl-keeps-5-redemption-caps-as-ocic-requests-ease-from-prior-quarter-4773280，source_ids=monetary.private_credit_liquidity），Blue Owl OTIC ≈38.1% 需求同遭比例撥付、Blackstone BCRED Q2 峰值 ≈12% NAV，BofA 定調 Q2 為贖回高峰——多基金 redemption 上限實際觸發＝financing-cycle 緊縮已抵達非銀信用，餵入 §3 融資扳機。
**結論**：扳機側；私募信貸多基金 gate proration（Blue Owl OCIC 18.8% 比例撥付、OTIC 38.1%、BCRED ≈12%）為扳機側事件，同時 HY 2.69%／IG 0.78% 史窄自滿——「自滿側 froth 與扳機側 financing 壓力同框」維持 **75**；macro 多序列持平、20Y 標售略軟、repo 無壓、CPI 黏著，故分數較前次持平、扳機側質變見「本次新增訊號」。

### 6. 結構性槓桿 — 77（weight 15%，Δ 0）
- **US 槓桿 ETF AUM**：美國槓桿 ETF 總 AUM ≈**$198B**（記錄高，TQQQ ≈$37.3B／SOXL ≈$22B 領先；NVDL >$4B），週流入續強、水位再創高（2026-07-10，https://cryptobriefing.com/leveraged-etfs-record-198b-aum/，source_ids=structural.leveraged_etf_aum）——水位高。
- **US 單股槓桿 ETF 核准／發行（近 30 日）**：**續擴散**——GraniteShares 7/14 上市首檔美掛 SK hynix ADR 2x 多/空（SKUU）及 NetApp／Teradata／Bitdeer 2x（2026-07-14，https://www.globenewswire.com/news-release/2026/07/14/3326857/0/en/GraniteShares-Launches-the-First-U-S-Listed-Leveraged-ETFs-on-SK-hynix.html，source_ids=structural.us_single_stock_etf）——單股槓桿產品向 ADR／二線股擴散顯著。
- **全球（非美）槓桿產品核准（本週）**：**本週擴散訊號未觸發**——韓／台／日／歐 07-16–07-23 無新單股槓桿／反向 ETF 核准；韓國 FSC/KRX 自 2026-07-16 起暫停新單股槓桿 ETF 上市（收緊，https://www.bloomberg.com/news/articles/2026-07-16/south-korea-to-halt-new-listings-of-single-stock-leveraged-etfs，source_ids=structural.global_leveraged_approvals，不納入計分）——未達 2+ 非美市場同週核准、rubric floor 81 未啟動（✗ NOT DISCLOSED）。
- **0DTE 佔 SPX 期權量**：≈**63%**（Cboe，2026-02-28 最新確定值、Q2 維持 >55%，https://www.cboe.com/insights/posts/volatility-insights-evaluating-the-market-impact-of-spx-0-dte-options/，source_ids=structural.zero_dte）——持續高檔。
- **Options 總量（OCC 月報）**：6 月 **1,603,491,559** 口、+45.0% YoY（2026-07-02，https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/monthly-weekly-volume-statistics，source_ids=structural.options_volume）——衍生品投機量創高。
- **跨資產／相關性確認**：Cboe SKEW ≈**146.05**（偏高、尾端避險付溢價、較前次 145.13 微升）、VIX ≈18.7 期限結構 contango（2026-07-20，https://veloxmacro.com/how-to-read-the-vix-week-ending-july-20-2026/，source_ids=structural.cross_asset_derivatives）——尾端避險升溫、整體波動平靜（confirmation）。
- **Margin debt / 市值 交叉檢核**：$1.416T、YoY +53.7%（2026-05-31，見 D4，https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra，source_ids=structural.margin_debt_crosscheck）——確認零售槓桿頂部級別（confirmation，不在此重複計分）。
- **AI 基礎設施債務／vendor-financing loops**：過去 30 日**新增**具名事件——Galaxy Digital 規劃 ≈**$3.5B** debut 垃圾債為 CoreWeave 相關資料中心融資（junk/HY 級、資料中心/CoreWeave 合約擔保）（2026-07-22，https://www.bloomberg.com/news/articles/2026-07-22/coreweave-backed-data-center-plans-3-5-billion-junk-bond-sale，source_ids=structural.ai_infrastructure_debt）——AI 基建融資向垃圾債層級下滑＝信用品質沉降訊號（Nvidia↔OpenAI/Anthropic circular 網為結構背景，非本窗新事件）。
- **銀行對 NBFI 放款**：≈$2.00T（原始 **2,004.02** 億美元，2026-07-08，無新觀測，FRED LNFACBW027SBOG，source_ids=structural.nbfi_bank_loans）——bank–NBFI linkage 水位持平（confirmation，不主計分）。
- **美債基差交易槓桿（best-effort）**：script `cftc_lev_funds`／`move_index`／`ofr_repo` 本次 `fetch_failed`，WebSearch 補得 ^MOVE **74.67**（週 +2.8%、中性偏低）（2026-07-21，https://finance.yahoo.com/quote/%5EMOVE/，source_ids=structural.treasury_basis_trade）；CFTC 槓桿基金淨空 ≈72,603 口（07-07、較前週回補）——MOVE 低波、無基差/swap-spread 失序平倉，乾柴未點火（confirmation，不主計分）。
**結論**：分數維持 **77**（rubric 61–80）。0DTE 續 >55%、OCC 量創高、US 單股槓桿產品續擴散（GraniteShares SK hynix/NetApp）、槓桿 ETF AUM 記錄高＝結構性槓桿高檔；本月新增 Galaxy $3.5B AI 基建垃圾債（信用沉降）為升溫因子，惟全球擴散訊號未觸發（韓國反收緊）、MOVE 低波無失序——正負相抵，淨評與前次持平。

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
- 1973.4｜命中｜source_ids=—｜T5YIFR 週 Δ +4 bps ≥ 0（通膨預期未回落）
- 1973.5｜未命中｜source_ids=—｜WTI 週漲幅 0%（無新觀測）< +0.5%
- 1973.6｜未命中｜source_ids=—｜decomposition.driver=unknown ≠ breakeven（三腿視窗不一致）
- 1973.7｜命中｜source_ids=—｜扳機狀態＝已擊發 ≥ 初啟
- 1973.8｜命中｜source_ids=—｜散戶情緒 50 < 55
**1997 早期建設 feature audit**
- 1997.1｜未命中｜source_ids=—｜估值溢價 79 > 74（超出 40–74 區間）
- 1997.2｜命中｜source_ids=—｜市場廣度 30 < 45
- 1997.3｜未命中｜source_ids=—｜投機行為 58 ≥ 50
- 1997.4｜命中｜source_ids=ai.hyperscaler_capex｜hyperscaler 2026 capex 指引仍上修（Alphabet ≈$205B、合計 ≈$725B+）
- 1997.5｜命中｜source_ids=—｜散戶情緒 50 < 55
- 1997.6｜未命中｜source_ids=—｜結構性槓桿 77 ≥ 50
- 1997.7｜命中｜source_ids=—｜HY OAS 2.69% < 4% 且本次週 Δ 0 bps ≤ 0（未走闊）
- 1997.8｜未命中｜source_ids=—｜扳機狀態＝已擊發 ≠ 未擊發
**1998 LTCM 衝擊 feature audit**
- 1998.1｜未命中｜source_ids=structural.cross_asset_derivatives｜HY 週 Δ 0 bps < +30；SKEW 146.05、VIX ≈18.7 contango（無壓力事件）
- 1998.2｜未命中｜source_ids=—｜S&P `sp500_trend.chg_pct` +0.75% > −5%（無回檔）
- 1998.3｜命中｜source_ids=monetary.private_credit_liquidity｜具名非銀壓力：Blue Owl OCIC Q2 18.8% gate proration 等私募信貸贖回上限觸發
- 1998.4｜未命中｜source_ids=monetary.fedwatch｜FedWatch 7/29 ≈83.4% 持平、非轉鴿
- 1998.5｜命中｜source_ids=—｜估值溢價 79 ≥ 60
- 1998.6｜命中｜source_ids=—｜扳機狀態＝已擊發 ≥ 初啟
- 1998.7｜未命中｜source_ids=—｜市場廣度 Δ = 30 − 30 = 0 < +8
- 1998.8｜未命中｜source_ids=—｜ΔT10YIE +3 bps > 0（通膨預期非下行）
**1999 晚期狂熱 feature audit**
- 1999.1｜命中｜source_ids=—｜估值溢價 79 ≥ 75
- 1999.2｜命中｜source_ids=valuation.sp500_pe_cape｜CAPE 40.94 ≥ 38
- 1999.3｜未命中｜source_ids=—｜投機行為 58 < 60
- 1999.4｜未命中｜source_ids=speculation.microcap_moonshots,speculation.ipo_heat｜本週 moonshot 0；無營收 IPO 佔比未達偏高
- 1999.5｜未命中｜source_ids=—｜市場廣度 30 < 45（廣度健康、非轉窄）
- 1999.6｜未命中｜source_ids=—｜D5 monetary_side＝扳機側 ≠ 自滿側，all 不成立
- 1999.7｜命中｜source_ids=—｜結構性槓桿 77 ≥ 60
- 1999.8｜未命中｜source_ids=—｜散戶情緒 50 < 55
- 1999.9｜命中｜source_ids=speculation.upcoming_ai_ipos｜巨型 AI IPO pipeline 活躍：Anthropic 續進 IPO 程序（$965B 估值，30 日內具名報導）
- 1999.10｜未命中｜source_ids=—｜扳機狀態＝已擊發 ≠ 未擊發
**2000/3 頂點 feature audit**
- 2000.1｜未命中｜source_ids=—｜估值溢價 79 < 85
- 2000.2｜命中｜source_ids=—｜扳機狀態＝已擊發 ≥ 初啟
- 2000.3｜未命中｜source_ids=—｜市場廣度 30 < 60
- 2000.4｜未命中｜source_ids=—｜prior `sp500_dev200_pct` 6.73 < +10 使第一分支為否；current chg +0.75% > −5%
- 2000.5｜未命中｜source_ids=—｜投機行為 58 < 70
- 2000.6｜未命中｜source_ids=speculation.insider_form4｜14 日內 0 件合格 Form 4 cluster
- 2000.7｜未命中｜source_ids=—｜散戶情緒 50 < 65
- 2000.8｜未命中｜source_ids=monetary.fedwatch｜FedWatch ≈83.4% 持平、非轉緊；10Y driver≠breakeven
**2021/12 Meme 頂 feature audit**
- 2021.1｜未命中｜source_ids=—｜散戶情緒 50 < 65
- 2021.2｜無資料｜source_ids=—｜本週無具名主導社群軋空（✗ NOT DISCLOSED）
- 2021.3｜命中｜source_ids=—｜結構性槓桿 77 ≥ 65
- 2021.4｜未命中｜source_ids=—｜D5 monetary_side＝扳機側 ≠ 自滿側，all 不成立
- 2021.5｜命中｜source_ids=retail.margin_debt｜margin debt YoY +53.7% ≥ +40%
- 2021.6｜未命中｜source_ids=speculation.microcap_moonshots｜本週 microcap moonshot 0 < 1
- 2021.7｜未命中｜source_ids=—｜市場廣度 30 < 50
- 2021.8｜未命中｜source_ids=—｜CPI YoY 3.46% < 4%，all 不成立

**兩句解讀**：本週相似度最高仍為「1997 早期建設」（50%）——市場廣度健康（30）、hyperscaler capex 仍上修（Alphabet $205B）、散戶未狂熱（50）、HY OAS 2.69% 史窄且本週未走闊，構成「基本面建設仍在、公開信用尚未轉緊」的早期組態；但須注意本週扳機狀態＝已擊發（私募信貸多基金 gate proration）且估值溢價 79 高企，機械最貼近錨與「早期」字面並不同義，實質更接近「估值高企＋非銀融資扳機、公開利差尚未反映」的中段位置，扳機鏈 A 尚未驗證啟動（driver≠breakeven、WTI 持平）。這意味循環位置介於建設與後期之間：真實技術突破吸引超商業回報所能支撐的資本（BIS AER 2026 Ch I：AI 相關投資 ≈1% of US GDP、IT 投資合計 ≈5% 已超 dot-com 峰），最須盯 AI 信用重定價（Oracle CDS 紀錄新高）、AI 基建融資向垃圾債沉降（Galaxy $3.5B）與私募信貸閘門是否外溢至公開利差。長期指數成長趨勢偏離（Dot-com ≈95%、1929 ≈110%、當前 AI 週期 ≈147%；RIA/Farrell）作跨期敘事錨、不進 checklist。

## 機構情緒對照

本次無新機構調查數據。

## 本次新增訊號

比較基準：vs 前次（3天前）。

- **格局轉變（質化）**：三角格局維持「穩定共存」，惟組成轉為小幅上行——S&P ▲ +0.75%（前次 ▼ −1.01%）、10Y ▲ +3 bps（前次持平），WTI 持平（無新觀測）；S&P `dev200_pct` 由 +6.73% 升至 +7.14%（< +10% 拉伸門檻），故未升為同向偏高。
- **貨幣與信貸環境（D5）＝扳機側，score Δ 0——質化新訊號（雙向 Δ 遮蔽防護）**：私募信貸多基金 Q2 gate proration 延續（Blue Owl OCIC 18.8% 比例撥付、OTIC 38.1%、Blackstone BCRED Q2 峰值 ≈12% NAV；BofA 定調 Q2 為贖回高峰），扳機狀態維持「已擊發」；分數未動因先前已因扳機側偏高（前次即 75）。贖回需求 QoQ 略降但仍 >3× 上限、比例撥付事實成立。
- **結構性槓桿質化訊號（score Δ 0）**：(1) **新增** AI 基建融資向垃圾債沉降——Galaxy Digital 規劃 ≈$3.5B debut 垃圾債為 CoreWeave 相關資料中心融資（信用品質沉降）；(2) US 單股槓桿 ETF 續擴散（GraniteShares 首檔美掛 SK hynix ADR 2x 多/空、NetApp/Teradata/Bitdeer 2x）——惟**全球（非美）擴散訊號未觸發（本週擴散訊號未觸發，未達 2+ 非美市場同週核准；韓國 FSC 反於 07-16 起暫停新單股槓桿 ETF 上市）**，MOVE 低波（74.67）無失序，故分數未動。
- **估值質化訊號（score Δ 0）**：hyperscaler 融資結構轉向發債（Amazon 7/7 ≥$25B 期債、Alphabet FY26 capex 上修至 ≈$205B），Oracle 5yr CDS ≈198 bp 紀錄新高（AI 信用分歧續擴）——皆屬 confirmation、不主計分，估值維持 79。
- 其餘維度（估值 79、廣度 30、投機 58、散戶 50、貨幣 75、結構 77）分數與前次持平；總分 64【警戒】、Δ 0。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | S&P 500 收盤（sp500_trend latest） | 7,498.96 | FRED SP500（sp500_trend） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.sp500_trend | S&P 500 距 200DMA 偏離（sp500_trend dev200_pct） | +7.14% | FRED SP500（sp500_trend） | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| retail.household_equity_allocation | 家庭持股佔金融資產比 | 45.76 | FRED BOGZ1FL153064486Q | 2026-01-01 | 2026-07-23T09:30:00+08:00 |
| monetary.fed_funds | Fed funds 上限（DFEDTARU） | 3.75% | FRED DFEDTARU | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.fed_funds | Fed funds 下限（DFEDTARL） | 3.50% | FRED DFEDTARL | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.hy_oas | HY OAS（BAMLH0A0HYM2） | 2.69% | FRED BAMLH0A0HYM2 | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.ig_oas | IG OAS（BAMLC0A0CM） | 0.78% | FRED BAMLC0A0CM | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.dgs10 | 10Y 名目殖利率（DGS10） | 4.63% | FRED DGS10 | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.dfii10 | 10Y 實質殖利率（DFII10） | 2.37% | FRED DFII10 | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.t10yie | 10Y breakeven（T10YIE） | 2.28% | FRED T10YIE | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.wti | WTI 原油（DCOILWTICO） | $84.38 | FRED DCOILWTICO | 2026-07-20 | 2026-07-23T09:30:00+08:00 |
| monetary.cpi_yoy | CPI YoY（CPIAUCSL yoy_pct） | 3.46% | FRED CPIAUCSL | 2026-06-01 | 2026-07-23T09:30:00+08:00 |
| monetary.t5yifr | 5y5y forward（T5YIFR latest） | 2.26% | FRED T5YIFR | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.term_premium | 10Y 期限溢價（THREEFYTP10） | 0.7787% | FRED THREEFYTP10 | 2026-07-17 | 2026-07-23T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR 隔夜利率 | 3.61% | FRED SOFR | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR 99th 分位（SOFR99） | 3.69% | FRED SOFR99 | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB | 3.65% | FRED IORB | 2026-07-23 | 2026-07-23T09:30:00+08:00 |
| monetary.repo_stress_srf | SRF/隔夜 repo 操作量（RPONTTLD） | 0.0 | FRED RPONTTLD | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.walcl | Fed 資產負債表（WALCL） | 6,743,028 百萬美元（≈$6.74T） | FRED WALCL | 2026-07-15 | 2026-07-23T09:30:00+08:00 |
| monetary.ecb_boj | ECB 資產（ECBASSETSW） | 5,949,077 百萬歐元（≈€5.95T） | FRED ECBASSETSW | 2026-07-17 | 2026-07-23T09:30:00+08:00 |
| monetary.ecb_boj | BOJ 資產（JPNASSETS） | 6,395,509 億日圓（≈¥639.55T） | FRED JPNASSETS | 2026-06-01 | 2026-07-23T09:30:00+08:00 |
| structural.nbfi_bank_loans | 銀行對 NBFI 放款（LNFACBW027SBOG） | 2,004.02 億美元（≈$2.00T） | FRED LNFACBW027SBOG | 2026-07-08 | 2026-07-23T09:30:00+08:00 |

### Coverage

| source_id | 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（P/E 28.85、CAPE 40.94 @07-22） |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E | MarketXLS [SEARCH]（stock-of-state 沿用） | ✓ SEARCH-VERIFIED（trailing ≈40 @05-15） |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（MS NVDA $288 EPS-driven @07-13） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500 派生） | ✓ API（dev200 +7.14%／dev52 +8.8%） |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧 | 信用市場 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Oracle CDS ≈198bp record、CoreWeave ≈665bp @07-20） |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | portfolioslab [SEARCH] | ✓ SEARCH-VERIFIED（RSP +11.8% vs SPY +9.4%） |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | MacroMicro/State Street [SEARCH] | ✓ SEARCH-VERIFIED（36.40% @07-02） |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth [SEARCH] | ✓ SEARCH-VERIFIED（07-22 A/D 轉弱、新低多於新高） |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH]（403，經 MacroMicro） | ✓ SEARCH-VERIFIED（41 Fear @07-21） |
| retail.margin_debt | 散戶｜Margin Debt: FINRA | FINRA/Advisor Perspectives [SEARCH]（月頻 stock-of-state） | ✓ SEARCH-VERIFIED（$1.416T、+53.7% YoY、2026-05 沿用） |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（Bull 44.9% @07-15） |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB/cashtag [SEARCH]（best-effort） | ✗ NOT DISCLOSED（本週無主導軋空事件） |
| retail.household_equity_allocation | 散戶｜Household equity allocation | fetch_macro.py BOGZ1FL153064486Q | ✓ API（45.76% @2026-Q1） |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim/MacroMicro [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（95.64 @07-15） |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM | 賣方調查 [SEARCH]（月頻，best-effort） | ✗ NOT DISCLOSED（7 月 FMS 07-14 發布，早於前次基準、非本次新增） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED DFEDTARU/DFEDTARL | fetch_macro.py FRED API | ✓ API（3.75%/3.50% @07-22） |
| monetary.hy_oas | 貨幣｜High Yield OAS | fetch_macro.py FRED API | ✓ API（2.69% @07-21，Δ0） |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | fetch_macro.py FRED API | ✓ API（0.78% @07-21，Δ0） |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | fetch_macro.py FRED API | ✓ API（4.63% @07-21，Δ+3bps） |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield | fetch_macro.py FRED API | ✓ API（2.37% @07-21，Δ+2bps） |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | fetch_macro.py FRED API | ✓ API（2.28% @07-22，Δ+3bps） |
| monetary.wti | 貨幣｜WTI crude oil price | fetch_macro.py FRED API | ✓ API（$84.38 @07-20，no_new_obs） |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED | fetch_macro.py FRED API（月頻） | ✓ API（3.46% @2026-06） |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | fetch_macro.py FRED API | ✓ API（2.26% @07-22，Δ+4bps） |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED | fetch_macro.py FRED API | ✓ API（0.7787% @07-17，≈0bps） |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py repo_stress | ✓ API（SOFR−IORB −4bps、SOFR99−IORB +4bps、SRF $0 @07-21/22） |
| monetary.treasury_auctions | 貨幣｜美債標售需求 | RTTNews/TreasuryDirect [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（20Y BTC 2.64、小幅 tail @07-22） |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（7/29 ≈83.4% 持平 @07-21） |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED WALCL | fetch_macro.py FRED API | ✓ API（$6.74T @07-15，no_new_obs） |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | fetch_macro.py FRED API | ✓ API（€5.95T @07-17／¥639.55T @06-01） |
| monetary.pboc | 貨幣｜PBoC aggregate financing | Xinhua/Bloomberg [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（6M 逆回購 ¥1.4T @07-14） |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Blue Owl OCIC 18.8% gate proration @07-02） |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報 [SEARCH]（stock-of-state） | ✓ SEARCH-VERIFIED（Alphabet ≈$205B、合計 ≈$725B+、仍上修） |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic/OpenAI/Google [SEARCH]（best-effort） | ✗ NOT DISCLOSED（本季無乾淨量化成長率披露） |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch/The Information [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Anthropic ≈$47B／OpenAI ≈$25B run-rate） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration | 財報電話 [primary: SEARCH]（best-effort） | ✗ NOT DISCLOSED（本次無乾淨窗內一手 RPO 披露） |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（DRAM +13–18% QoQ 3Q26 @07-09；供給仍被吸收） |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構 | 季報/發債 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口 | 組合披露 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（年化 capex ≈$725B vs 終端營收低百億級） |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K/10-Q [primary: SEARCH]（best-effort，30日） | ✗ NOT DISCLOSED（過去 30 日無新變更） |
| ai.capital_cycle | AI｜資本週期階段 | 供需增速+進出場事件 [SEARCH]（best-effort） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days +AI rename/SPAC | [SEARCH] | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis/Renaissance [SEARCH] | ✓ SEARCH-VERIFIED（YTD ≈203 檔、$141.2B @07-13） |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz/Benzinga [primary: SEARCH]（required 週螢幕） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | S-1/具名報導 [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Anthropic IPO 程序 $965B @07-15） |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership | SEC EDGAR [primary: EDGAR]（required） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe/YCharts [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（0.65 @07-21） |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing [primary: SEARCH] | ✓ SEARCH-VERIFIED（總 ≈$198B @07-10） |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | GlobeNewswire/ETF.com [SEARCH] | ✓ SEARCH-VERIFIED（GraniteShares SK hynix 2x @07-14） |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX/TWSE/JPX/ESMA [SEARCH]（best-effort，7日） | ✗ NOT DISCLOSED（本週擴散訊號未觸發；韓國反收緊） |
| structural.zero_dte | 結構｜0DTE option volume | Cboe [SEARCH]（Cboe 403） | ✓ SEARCH-VERIFIED（≈63%，Cboe @2026-02） |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com [SEARCH] | ✓ SEARCH-VERIFIED（6 月 16.03 億口、+45% YoY @07-02） |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe/Velox [SEARCH] | ✓ SEARCH-VERIFIED（SKEW ≈146.05、VIX contango @07-20） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 D4（confirmation） | ✓ SEARCH-VERIFIED（$1.416T/+53.7% YoY，D4 引用不重複計分） |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]（best-effort，30日） | ✓ SEARCH-VERIFIED（Galaxy $3.5B CoreWeave 資料中心垃圾債 @07-22） |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | fetch_macro.py FRED API | ✓ API（$2.00T @07-08，no_new_obs） |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | script→WebSearch [primary: script]（best-effort） | ✓ SEARCH-VERIFIED（^MOVE 74.67 @07-21；cftc/move/ofr script fetch_failed，WebSearch 補值） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 28.85 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 40.94 | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E ≈40 trailing | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026 | 2026-05-15 | 2026-07-23T09:30:00+08:00 |
| valuation.analyst_tp_decomposition | MS NVDA 目標 $288（≈22× EPS、target PE 未擴張、EPS-driven） | Morgan Stanley NVDA target 288 July 2026 EPS | https://www.gurufocus.com/news/8955458/morgan-stanley-upgrades-nvidia-nvda-with-a-288-target-price | 2026-07-13 | 2026-07-23T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS ≈198bp record、CoreWeave ≈665bp | Oracle CoreWeave CDS spread record July 2026 | https://bondblox.com/news/oracles-5y-cds-spread-hits-all-time-highs | 2026-07-20 | 2026-07-23T09:30:00+08:00 |
| breadth.rsp_spy | RSP +11.8% vs SPY +9.4% YTD | RSP vs SPY equal weight YTD 2026 | https://portfolioslab.com/tools/stock-comparison/RSP/SPY | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 36.40% | S&P 500 top 10 concentration percent 2026 | https://en.macromicro.me/collections/34/us-stock-relative/123442/us-sp-500-top-10-companies-total-market-cap-and-share | 2026-07-02 | 2026-07-23T09:30:00+08:00 |
| breadth.advance_decline | 07-22 A/D 轉弱、新低多於新高 | NYSE breadth advance decline July 22 2026 | https://ts2.tech/en/nasdaq-ends-flat-as-market-breadth-remains-thin-ahead-of-big-tech-earnings/ | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 41（Fear） | CNN Fear and Greed Index July 2026 | https://en.macromicro.me/series/22748/cnn-fear-and-greed | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt $1.416T、+53.7% YoY（5 月沿用） | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra | 2026-05-31 | 2026-07-23T09:30:00+08:00 |
| retail.aaii | AAII Bull 44.9% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey | 2026-07-15 | 2026-07-23T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 95.64 | NAAIM exposure index latest July 2026 | https://en.macromicro.me/series/20540/naaim-exposure-index | 2026-07-15 | 2026-07-23T09:30:00+08:00 |
| monetary.treasury_auctions | 20Y BTC 2.64、小幅 tail | US Treasury 20Y auction July 2026 bid to cover | https://www.rttnews.com/3669412/twenty-year-bond-auction-attracts-average-demand.aspx | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 ≈83.4% 持平 | CME FedWatch rate hold probability July 2026 | https://cryptorank.io/news/feed/2d990-fed-rate-hold-july-cme-fedwatch | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://english.news.cn/20260714/2d460c4227c244f1bf930993be469262/c.html | 2026-07-14 | 2026-07-23T09:30:00+08:00 |
| monetary.private_credit_liquidity | [private_credit_gate] Blue Owl OCIC Q2 贖回 18.8% 於 5% 上限比例撥付 | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://www.investing.com/news/stock-market-news/blue-owl-keeps-5-redemption-caps-as-ocic-requests-ease-from-prior-quarter-4773280 | 2026-07-02 | 2026-07-23T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex：Alphabet 上修至 ≈$205B、合計 ≈$725B+ | hyperscaler capex 2026 Alphabet raised 205B Q2 | https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic ≈$47B／OpenAI ≈$25B run-rate | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-05-15 | 2026-07-23T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 3Q26 合約 +13–18% QoQ | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260709-13140.html | 2026-07-09 | 2026-07-23T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] Alphabet FY26 capex 上修至 ≈$205B、發債佔比升 | Alphabet capex 205B Q2 2026 debt financing | https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] Amazon 啟動 ≥$25B 八檔期債（AI 基建） | Amazon 25 billion bond offering AI data center July 2026 | https://finance.yahoo.com/technology/ai/articles/bond-issuance-backing-ai-investment-135635215.html | 2026-07-07 | 2026-07-23T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex ≈$725B vs AI 終端營收低百億級 | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-05-15 | 2026-07-23T09:30:00+08:00 |
| speculation.ai_rename_spac | 本週合格 +AI 改名/SPAC 件數 0 | AI rename ticker change SPAC July 16-23 2026 | Businesswire/StockTitan movers screener | 2026-07-23 | 2026-07-23T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD ≈203 檔 IPO、$141.2B | US IPO market 2026 YTD count proceeds | https://stockanalysis.com/ipos/2026/ | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot 件數 0 | microcap 100% single day quantum AI fusion moonshot July 2026 | Finviz/Benzinga/StockTwits movers screener | 2026-07-23 | 2026-07-23T09:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic IPO 程序 $965B、可能 10 月掛牌 | Anthropic IPO investor meetings July 2026 valuation | https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html | 2026-07-15 | 2026-07-23T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 cluster 件數 0（CoreWeave 單一內部人 10b5-1、EDGAR egress 受限） | insider Form 4 cluster AI leaders July 2026 openinsider | SEC EDGAR / openinsider（一手 URL 無法取得） | 2026-07-23 | 2026-07-23T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.65 | Cboe equity put call ratio July 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio | 2026-07-21 | 2026-07-23T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM ≈$198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-07-10 | 2026-07-23T09:30:00+08:00 |
| structural.us_single_stock_etf | GraniteShares 首檔美掛 SK hynix ADR 2x 多/空 | single-stock leveraged ETF launch July 2026 GraniteShares SK hynix | https://www.globenewswire.com/news-release/2026/07/14/3326857/0/en/GraniteShares-Launches-the-First-U-S-Listed-Leveraged-ETFs-on-SK-hynix.html | 2026-07-14 | 2026-07-23T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX ≈63% | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/volatility-insights-evaluating-the-market-impact-of-spx-0-dte-options/ | 2026-02-28 | 2026-07-23T09:30:00+08:00 |
| structural.options_volume | OCC 6 月 1,603,491,559 口、+45% YoY | OCC monthly options volume June 2026 | https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/monthly-weekly-volume-statistics | 2026-07-02 | 2026-07-23T09:30:00+08:00 |
| structural.cross_asset_derivatives | [snapshot] Cboe SKEW 146.05、VIX ≈18.7 contango | VIX term structure SKEW July 2026 | https://veloxmacro.com/how-to-read-the-vix-week-ending-july-20-2026/ | 2026-07-20 | 2026-07-23T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt $1.416T、+53.7% YoY（cross-ref D4） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra | 2026-05-31 | 2026-07-23T09:30:00+08:00 |
| structural.ai_infrastructure_debt | Galaxy Digital ≈$3.5B CoreWeave 資料中心 debut 垃圾債 | Galaxy Digital 3.5 billion junk bond CoreWeave data center July 2026 | https://www.bloomberg.com/news/articles/2026-07-22/coreweave-backed-data-center-plans-3-5-billion-junk-bond-sale | 2026-07-22 | 2026-07-23T09:30:00+08:00 |
| structural.treasury_basis_trade | [basis] move_index ^MOVE 74.67（週 +2.8%、中性偏低） | MOVE index level July 21 2026 basis trade | https://finance.yahoo.com/quote/%5EMOVE/ | 2026-07-21 | 2026-07-23T09:30:00+08:00 |

## 本次分數存檔
```json
{
  "date": "2026-07-23",
  "iso_week": "2026-W30",
  "weekday": "Thursday",
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
  "sp500_dev200_pct": 7.14
}
```

本報告為相對風險溫度計，非擇時訊號。

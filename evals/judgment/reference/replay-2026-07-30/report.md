# 2026-07-30 市場泡沫風險評估報告
> 報告日期：2026-07-30；執行日：2026-07-30 Asia/Taipei；ISO 週次：2026-W31；前次基準：report-2026-07-27（3天前）

**總評**：總分 64【警戒】（Δ 0）；扳機狀態：已擊發；最貼近錨點：1973/1 Nifty Fifty 頂（40%）。

## §1 六維度風險條圖
| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▱▱▱ | 77 | 78 | -1 |
| 市場廣度 | ▰▰▰▱▱▱▱▱▱▱ | 30 | 30 | 0 |
| 投機行為 | ▰▰▰▰▰▱▱▱▱▱ | 58 | 58 | 0 |
| 散戶情緒 | ▰▰▰▰▱▱▱▱▱▱ | 47 | 48 | -1 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▰▱▱▱ | 77 | 75 | +2 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 78 | 78 | 0 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **64【警戒】** | 64 | 0 |

## §2 歷史錨點相似度
| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1973/1 Nifty Fifty 頂 | 40% | ▰▰▰▰▱▱▱▱▱▱ | ◀ 最貼近 |
| 1997 早期建設 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 1998 LTCM 衝擊 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 2000/3 頂點 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |

## §3 三角訊號
| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,316.15 | ▼ −1.31%（前次 ≈7,413.18） |
| WTI 原油 | $84.25 /bbl | 持平 0%（無新觀測，前次 ≈$84.25） |
| 10Y Treasury | 4.61% | ▼ −4 bps（前次 ≈4.65%） |

**三者狀態**：穩定共存——三者本次方向為 ▼／持平／▼（無上行腿），既非全數同向上行、亦非 ▲/▼ 混合，依格局判定規則屬穩定共存；S&P `dev200_pct` +4.29%（< +10% 拉伸門檻），未升為同向偏高。資產面走弱與非銀融資扳機（私募信貸 gate）並存，須分開判讀。
- 股市：≈7,316.15（S&P 500，2026-07-29 收）；較前次 ▼ −1.31%（前次 ≈7,413.18）；距 200 日均線 +4.29%、距 52 週均線 +5.83%——7/28–29 科技領跌回檔、價格延伸較前次（+5.8%）進一步回落。
- WTI 原油：≈$84.25/bbl（DCOILWTICO，2026-07-27，無新觀測）；較前次 持平 0%（前次 ≈$84.25）。
- 10Y 殖利率：4.61%（DGS10，2026-07-28）；較前次 ▼ −4 bps（前次 ≈4.65%）；主要驅動：三腿視窗不一致（driver=unknown，ΔT10YIE 取自較新視窗）。
**格局轉變**：前次格局＝穩定共存（讀自 report-2026-07-27 的 `regime`）→ 本次格局＝穩定共存；三者由前次的持平／無新觀測轉為 S&P 與 10Y 小幅下行、WTI 無新觀測，價格延伸未達拉伸門檻，維持穩定共存。
**10Y 成因拆解**：拆的是週變動（bps）、非水位（`ΔDGS10 ≈ ΔDFII10 + ΔT10YIE`）；三腿本週均有新觀測（freshness=updated）但視窗不一致（`decomposition.driver=unknown`——ΔT10YIE 取自 07-29、DGS10／DFII10 取自 07-28，恆等式不跨視窗成立），判定 不可判（視窗不一致）；三腿實際 signed 週變動如下：
- ΔDGS10 名目殖利率週變動：−4 bps
- ΔDFII10 實質殖利率週變動：−3 bps
- ΔT10YIE 損益平衡通膨週變動：+5 bps
- 判定：不可判（視窗不一致）
**扳機鏈**：A 通膨鏈（油 → 通膨預期 → Fed 受限 → refinancing 成本）本週未加速但約束升溫——WTI 持平（≈$84.25，無新觀測）、實現通膨續高且通膨預期回升：[monetary.cpi_yoy] CPIAUCSL yoy_pct=3.46 data_date=2026-06-01（6 月）、5y5y forward [monetary.t5yifr] T5YIFR latest=2.28 delta_bps=4.0 data_date=2026-07-29（週 +4 bps）；FOMC 7/29 以 9-3 維持 3.50–3.75%（三票異議、通膨仍高於 2% 目標），CME FedWatch 9 月持平機率 ≈42%、近端未定價降息——市場憂 Fed 落後通膨，Fed put 可得性下降；無當期電價／能源瓶頸新報導。B 槓桿鏈（衝擊：財政風險再定價 → NBFI 去槓桿 → margin spiral → 國債市場失序 → 官方市場功能回應）乾柴堆積但未點火——衝擊節點：10Y 期限溢價 THREEFYTP10 ≈0.8376%（序列自身 trailing ≈7d ＋5.9 bps、溫和上行）、7/22 20Y 標售長端需求偏弱（dealer takedown 14.67%）；NBFI 節點：script `cftc_lev_funds`／`move_index`／`ofr_repo` 本次 fetch_failed，WebSearch 未取得 7 日窗內可稽核基差交易新平倉事件（基差交易估 ≈$830B 為背景，非窗內事件）；官方回應節點：`repo_stress` SOFR−IORB 0 bps、SOFR99−IORB +9 bps、SRF 動用 ≈$0.003B（無失序）。real-rate 主導的異常 10Y 上行本週不存在（ΔDGS10 −4 bps）。惟 AI 雲端信用本週明顯重定價（Oracle 遭降至 BBB-、CoreWeave 5Y CDS ≈855bp）屬單一發行人／結構化層級，尚未外溢至國債市場層級；本鏈證據 best-effort，本週無國債基差交易失序新事件。
**扳機理由**：private_credit_gate
⚠ **結論**：扳機狀態：已擊發——本次續命中「私募信貸 gate proration / breach」：Blackstone 於 2026-07-23 Q2 財報電話會確認 BCRED（Blackstone Private Credit Fund）Q2 贖回需求升至 ≈10% NAV、突破 5% 季度贖回上限並比例撥付，Blue Owl 兩檔私募信貸基金亦於 07-02 對 19–38% 贖回請求比例撥付——此為 1998 LTCM 型「非銀融資扳機」，先於公開 mark-to-market 利差（HY 2.84%／IG 0.81% 仍史窄）出現一階壓力。三者配置歷史意義：估值＋槓桿＝崩跌位能，融資緊縮＝時點扳機；本週三角資產面走弱仍屬穩定共存，惟公開利差自滿與非銀融資扳機並存（自滿側 froth 與扳機側 financing 壓力同框），且 AI 雲端信用重定價（Oracle BBB-、CoreWeave CDS ≈855bp）為後期訊號側新增證據，槓桿鏈 B 尚未點火至國債市場層級。

## 六維度評分

### 1. 估值溢價 — 77（weight 22%，Δ -1）
- **S&P 500 trailing P/E** ≈**28.6**（2026-07-29，https://www.multpl.com/s-p-500-pe-ratio，source_ids=valuation.sp500_pe_cape）——遠高於長期中位（≈16–19），實現盈餘基礎上市場歷史性偏貴。
- **Shiller CAPE** ≈**40.9**（2026-07-29，https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio，source_ids=valuation.sp500_pe_cape）——逼近歷史高（≈44）、遠高於長均 ≈32.4。
- **Excess CAPE Yield（ECY）** ≈**0.04%**（`1/40.9 − 2.41/100`，derived 自 CAPE **40.9** 與 DFII10 2.41%，2026-07-29，source_ids=valuation.sp500_pe_cape）——接近 0，屬 1929／2000 級別股相對債極貴訊號（confirmation，不主計分）。
- **Mag 7 加權 P/E**：Mag 7 對其餘 493 檔溢價壓縮至 ≈**10%**（近十年最低）（2026-07-08，https://www.cnbc.com/2026/07/08/magnificent-seven-stocks-are-the-cheapest-in-a-decade-by-one-measure.html，source_ids=valuation.mag7_multiples）——絕對水位仍高但相對溢價續收斂（stock-of-state 沿用）。
- **價格趨勢偏離（Farrell #1/#2/#4）** S&P 距 200 日均線 **+4.29%**、距 52 週均線 +5.83%（`sp500_trend`，2026-07-29，FRED SP500，source_ids=valuation.sp500_trend）——7/28–29 科技領跌使價格延伸自 +5.8% 進一步回落，距 +10% 拉伸門檻更遠，與 P/E／CAPE 互補、不重複計分。
- **AI capex 現實檢核**：hyperscaler 2026 capex 指引續上修——Meta 上修至 $125–145B、Amazon $200B、Alphabet 上修至 ≈$205B，四家合計 ≈**$725B**（+77% YoY）（2026-07-28，https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html，source_ids=ai.hyperscaler_capex）——基本面敘事仍撐估值，惟市場已對「capex 上修但回本未現」轉為懲罰（7/28 Alphabet 財報引發賣壓）。
- **AI compute 供需現實檢核**：伺服器 DRAM 交期 30–40 週、3Q26 合約價續漲 +13–**18%** QoQ（TrendForce，2026-07-03，https://www.trendforce.com/presscenter/news/20260703-13134.html，source_ids=ai.compute_supply_demand）——供給仍被 AI 伺服器合約吸收、缺口未成形（供給緊、非過剩），此渠道未推升估值風險。
- **AI 營收對 capex 缺口現實檢核**：AI 終端年化營收（Anthropic ≈$47B＋OpenAI ≈$25B）vs 年化 capex ≈**$725B**（分母：top-4＋Oracle）（2026-06-15，https://epoch.ai/data-insights/anthropic-openai-revenue，source_ids=ai.revenue_capex_gap）——量級缺口仍逾 10× 且 capex 續升，回本假設後移，屬估值風險上修的質化依據（缺口未收斂）。
- **Hyperscaler 融資結構（capex vs FCF / 發債）**：quarterly_state——Alphabet Q2 FCF 轉負、FY26 capex 上修至 ≈$205B；event_scan——hyperscaler 2026 發債 +1,300% YoY 至累計 ≈**$182B**（2026-07-16，https://247wallst.com/investing/2026/07/16/the-ai-revolution-is-reshaping-credit-markets-here-is-what-it-really-says-about-risk/，source_ids=ai.hyperscaler_financing_mix）——capex 愈靠發債支撐、同份 guidance 脆弱性上升（BIS Bulletin 120，confirmation，不主計分）。
- **AI 信用定價分歧（equity-vs-credit schism）**：AI 雲端／基建發行人信用本週明顯重定價——Oracle 遭 S&P 降至 BBB-、CoreWeave 5Y CDS 升至 ≈**855bp**（隱含 ≈50% 違約），Nebius/CoreWeave 7/29 股價重挫（2026-07-29，https://247wallst.com/investing/2026/07/29/nebius-drops-10-coreweave-sinks-9-as-rising-credit-swap-costs-hit-the-ai-cloud-trade/，source_ids=valuation.ai_credit_schism）——信貸端開始重定價而估值仍高＝後期訊號側證據升溫（confirmation，不主計分；缺值不調分）。
- **TP-upgrade phase signal**：本季（Q3 2026）具名賣方升評屬 **EPS-driven**——Morgan Stanley NVDA 目標 未擴張（≈22× CY27 EPS）、目標價 $**288**（2026-07-13，https://www.gurufocus.com/news/8955458/morgan-stanley-upgrades-nvidia-nvda-with-a-288-target-price，source_ids=valuation.analyst_tp_decomposition）——升評由 E 而非 multiple 主導、同季未見多檔 multiple-driven 重定價，屬相對緩和訊號（confirmation，不主計分）。
- **折舊年限變動（盈餘品質）**：過去 30 日無新 10-K／10-Q 折舊年限或殘值假設變更披露（✗ NOT DISCLOSED，source_ids=ai.depreciation_life，不納入計分）。
- **backlog 重複計算風險（RPO double-counting）**：本次無新一手客戶集中度／RPO 具乾淨窗內資料日之披露（✗ NOT DISCLOSED，source_ids=ai.customer_concentration_rpo，不納入計分）。
- **資本週期階段**：event_scan 無窗內具日期的新進入者／取消事件、quarterly_state 供需增速證據不足，本次不判定週期階段（✗ NOT DISCLOSED，source_ids=ai.capital_cycle，不納入計分）。
**結論**：分數由 78 降至 **77**（rubric 高位）。趨勢偏離自 +5.8% 回落至 +4.29%、Mag7 相對溢價壓縮至 ≈10%＝估值面小幅緩和；惟 CAPE 40.9 仍近史高、ECY ≈0、capex 續上修（$725B）與 AI 信用重定價（Oracle BBB-、CoreWeave CDS ≈855bp）同框——淨評較前次微降 1 分。

### 2. 市場廣度 — 30（weight 13%，Δ 0）
- **RSP（等權）vs SPY（市值權）YTD**：SPY +9.22% YTD、RSP 等權 +**14.57%**（領先 ≈+5 pp）（2026-07-26，https://247wallst.com/investing/2026/07/26/is-equal-weighting-the-sp-500-worth-it-heres-what-the-data-says/，source_ids=breadth.rsp_spy）——等權領先市值權，廣度結構偏健康／轉寬方向（科技領跌反使等權相對占優）。
- **Top-10 集中度**：≈**38%**（2026-07-15，https://www.forbes.com/sites/investor-hub/article/sp-500-weight-mag-7-stocks-diversification-risk/，source_ids=breadth.top10_concentration）——遠高於長均 ≈24%、處歷史高位（結構性狹窄）。
- **Advance/Decline 與新高/新低**：NYSE advancers 1.32:1、新高 161 檔、新低 **198** 檔（新低反超）（2026-07-27，https://finance.yahoo.com/markets/stocks/articles/stock-market-news-july-27-132000679.html，source_ids=breadth.advance_decline）——連二／三週下跌、新高動能轉薄、新低反超，屬廣度惡化的殘餘負面。
**結論**：分數維持 **30**（rubric 21–40 偏健康端）。等權領先市值權（+5 pp）為結構性健康主訊號；Top-10 ≈38% 歷史高位與新低反超為殘餘負面——正負相抵，淨評與前次持平。

### 3. 投機行為 — 58（weight 18%，Δ 0）
- **+AI 改名／SPAC**：本週（07-23–07-30）+AI 改名／SPAC 合格 **0** 件（2026-07-30 螢幕）——✓ SEARCH-VERIFIED（0 件）（source_ids=speculation.ai_rename_spac）；上週兩檔 SPAC（BRTMU/SCATU 07-21）已落 7 日窗外。
- **IPO 熱度**：2026 IPO 募資 $251B／88 檔（超越 2025 全年）、Cerebras（CBRS）首日 +**68%**（惟 OpenAI 傳因近期波動考慮延後 IPO）（2026-07-28，https://www.emarketer.com/content/ipos-test-investor-appetite-unprofitable-ai-giants，source_ids=speculation.ipo_heat）——IPO 一級市場活躍、投資人對無獲利 AI 巨頭胃納受考驗。
- **Microcap thematic moonshots**：本週 microcap thematic moonshot 合格 **0** 件（<$1B 市值、單日 ≥100% 或 2–3 日 ≥50%、堆疊 2+ 熱主題＋弱基本面；2026-07-30 螢幕）——✓ SEARCH-VERIFIED（0 件）（source_ids=speculation.microcap_moonshots）；SMCI +78% 屬 >$1B 大型股、不合格。
- **Upcoming AI mega-IPO pipeline**：OpenAI 考慮延至 2027 IPO、目標估值 ≈$**1**T；Anthropic 續進 IPO 程序、Cerebras 已掛牌（2026-07-28，https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground，source_ids=speculation.upcoming_ai_ipos）——30 日內具名巨型 AI IPO pipeline 活躍、流動性抽離風險。
- **Insider selling clusters**：14 日內（07-16–07-30）出現合格 Form 4 cluster——CoreWeave 10b5-1 內部人 cluster：CDO McBee 07-20 售 ≈$14.6M、CEO Intrator 07-21 售 307,692 股 ≈$**24.1**M（2026-07-21，https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001769628&type=4，source_ids=speculation.insider_form4）——✓ SEARCH-VERIFIED（非零），AI 硬體複合體內部人賣壓集中。
- **Cboe equity-only put/call**：≈**0.66**（2026-07-27，https://ycharts.com/indicators/cboe_equity_put_call_ratio，source_ids=speculation.equity_put_call）——中性偏 call，未破 0.50 極端（confirmation，不主計分）。
**結論**：分數維持 **58**（rubric 41–60「投機升溫」）。IPO 一級市場熱（Cerebras +68%）、CoreWeave 內部人賣壓集中為升溫面；+AI 改名／moonshot 均 0、風險趨避週使投機體感降溫（OpenAI 傳延後 IPO）為抑制面——正負相抵，投機分數與前次持平。

### 4. 散戶情緒 — 47（weight 12%，Δ -1）
- **CNN Fear & Greed**：≈**37「Fear」**（2026-07-29，https://www.cnn.com/markets/fear-and-greed，source_ids=retail.fear_greed）——較前次 39 再降、續處恐懼區，散戶未亢奮。
- **Margin Debt**：**$1.502T（6 月，記錄高）、YoY +51.5%**（2026-07-20，https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra，source_ids=retail.margin_debt）——月頻 stock-of-state；YoY +**51.5%** 仍屬 1999／2007／2021 頂部級別警訊。
- **AAII 散戶調查**：Bear 42.3%／Neutral 28.1%／Bull **29.6%**（2026-07-23，https://www.aaii.com/sentimentsurvey，source_ids=retail.aaii）——多方低於長均 37.5%、空方偏高，散戶情緒偏空。
- **家庭持股佔金融資產比**：**45.76%**（`BOGZ1FL153064486Q`，2026-01-01 資料日／2026-Q1，FRED BOGZ1FL153064486Q，source_ids=retail.household_equity_allocation）——歷史高位、後續加碼空間有限（Farrell #5，季頻沿用、不計週 Δ）。
- **NAAIM Exposure Index**：前值 95.64 → 最新 **84.02**（2026-07-22，https://ycharts.com/indicators/naaim_number，source_ids=retail.naaim）——主動經理人曝險回落、已減碼（Farrell #9，confirmation，不主計分）。
- **社群情緒代理**：Beyond Meat（BYND）空頭 37%、r/wallstreetbets 軋空、盤前 +**10**%（2026-07-23，https://www.asktraders.com/analysis/wendys-nasdaq-wen-stock-turns-meme-darling-amid-short-squeeze-and-activist-buzz/，source_ids=retail.social_sentiment）——具名迷因軋空重現（投機口袋，非主計分驅動）。
**結論**：分數由 48 降至 **47**（rubric 41–60 下緣）。CNN F&G 39→37 續處 Fear、AAII 多方 29.6% 偏空、NAAIM 回落至 84＝情緒／擁擠度續降溫；惟 margin debt 6 月創高（YoY +51.5%）、家庭持股高位與 BYND 軋空為抑跌——淨評較前次降 1 分。

### 5. 貨幣與信貸環境 — 77（weight 20%，Δ +2）
- **Fed funds rate**：目標區間 **3.50–3.75%**（`DFEDTARU` 3.75%／`DFEDTARL` 3.50%，2026-07-29，FRED DFEDTARU/DFEDTARL，source_ids=monetary.fed_funds）——FOMC 7/29 以 9-3 維持不變。
- **市場隱含路徑（CME FedWatch，best-effort）**：FOMC 7/29 維持 3.50–3.75%（9-3 票）、CME FedWatch 9 月持平機率 ≈**42%**、近端未定價降息（2026-07-29，https://www.cnbc.com/2026/07/29/fed-rate-decision-july-2026.html，source_ids=monetary.fedwatch）——通膨仍高於目標、Fed 偏鷹持平，寬鬆空間受限（缺值不調分）。
- **Realized inflation vs expectations**：CPI YoY **3.46%**（`CPIAUCSL`，2026-06-01，FRED CPIAUCSL，source_ids=monetary.cpi_yoy）仍高於 2% 目標、5y5y forward **2.28%**（`T5YIFR`，2026-07-29，週 Δ +4 bps，FRED T5YIFR，source_ids=monetary.t5yifr）回升——通膨黏著、通膨預期回升，Fed 約束升溫。
- **10Y 期限溢價（term premium）**：`THREEFYTP10` **0.8376%**（2026-07-24，Kim-Wright 三因子模型，序列自身 trailing ≈7d +5.9 bps，FRED THREEFYTP10，source_ids=monetary.term_premium）——財政風險再定價溫和上行。
- **repo 資金壓力（SOFR−IORB）與 SRF 動用**：SOFR **3.65%**、IORB 3.65%、SOFR−IORB **0 bps**；SOFR99 3.74%、SOFR99−IORB +9 bps；SRF/RPONTTLD 動用 ≈$0.003B（2026-07-28，FRED SOFR/SOFR99/IORB/RPONTTLD，source_ids=monetary.repo_stress_srf）——secured-funding 無壓力、SRF 未實質動用。
- **美債標售需求（auction，best-effort）**：7/22 20Y 標售長端需求偏弱——dealer takedown **14.67%**（高於均值）（2026-07-22，https://www.cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/，source_ids=monetary.treasury_auctions）——財政供給壓力事件溫和（confirmation；缺值不調分）。
- **HY OAS**：**2.84%**（`BAMLH0A0HYM2`，2026-07-28，週 Δ +3 bps，FRED BAMLH0A0HYM2，source_ids=monetary.hy_oas）——接近循環低、極窄、自滿側；本週微幅走闊（streak=1，未達連續兩次）。
- **IG OAS**：**0.81%**（`BAMLC0A0CM`，2026-07-28，週 Δ 0 bp，FRED BAMLC0A0CM，source_ids=monetary.ig_oas）——史窄、信用自滿。
- **10Y nominal 週變動拆解**：ΔDGS10 −4 bps；`DGS10` **4.61%**（2026-07-28，FRED DGS10，source_ids=monetary.dgs10）、`DFII10` **2.41%**（2026-07-28，FRED DFII10，source_ids=monetary.dfii10）、`T10YIE` **2.26%**（2026-07-29，FRED T10YIE，source_ids=monetary.t10yie）——三腿視窗不一致（driver=unknown，詳 §3），殖利率小幅回落。
- **WTI 原油**：**$84.25**/bbl（`DCOILWTICO`，2026-07-27，無新觀測，FRED DCOILWTICO，source_ids=monetary.wti）——持平，A 通膨鏈油價端無新推力。
- **Fed balance sheet**：≈$6.75T（原始 **6,747,378** 百萬美元，2026-07-22，無新觀測，FRED WALCL，source_ids=monetary.walcl）——量化緊縮步調持平。
- **全球央行流動性（ECB）**：ECB ≈€5.94T（原始 **5,944,015** 百萬歐元，2026-07-24，FRED ECBASSETSW，source_ids=monetary.ecb_boj）——持平。
- **全球央行流動性（BOJ）**：BOJ ≈¥639.55T（原始 **6,395,509** 億日圓，2026-06-01，FRED JPNASSETS，source_ids=monetary.ecb_boj）——持平。
- **PBoC 流動性操作**：人行 MLF 5 個月最大、7/24 淨投放 ≈¥**100**B（平滑稅期與政治局會議前），月底連日逆回購合計 ≈¥2.1T（2026-07-24，https://www.bloomberg.com/news/articles/2026-07-24/pboc-adds-most-liquidity-to-economy-in-five-months-to-aid-growth，source_ids=monetary.pboc）——中國端流動性偏寬（confirmation）。
- **私募信貸贖回壓力（扳機側，event-driven）**：Blackstone 於 2026-07-23 Q2 財報電話會確認 **BCRED 突破 5% 季度贖回上限**——贖回需求升至 ≈**10%** NAV、比例撥付；Blue Owl 兩檔基金 07-02 對 19–38% 贖回請求比例撥付（2026-07-23，https://www.bloomberg.com/news/articles/2026-07-02/blue-owl-bdcs-impose-caps-after-facing-19-38-requests-to-exit，source_ids=monetary.private_credit_liquidity）——實際 gate proration / breach 事實成立、餵入 §3 融資扳機。
**結論**：扳機側；BCRED Q2 gate proration（≈10% NAV 需求、比例撥付，2026-07-23 披露）為扳機側事件，同時 HY 2.84%／IG 0.81% 史窄自滿——「自滿側 froth 與扳機側 financing 壓力同框」；本週 Fed 鷹派持平、通膨預期回升（T5YIFR +4 bps）、期限溢價上行與 AI 雲端信用重定價（Oracle BBB-、CoreWeave CDS ≈855bp）使 financing-trigger 側升溫，分數自 75 升至 **77**。

### 6. 結構性槓桿 — 78（weight 15%，Δ 0）
- **US 槓桿 ETF AUM**：美國槓桿 ETF 總 AUM 創高 ≈$**198**B（TQQQ、SOXL 領先）（2026-07-23，https://cryptobriefing.com/leveraged-etfs-record-198b-aum/，source_ids=structural.leveraged_etf_aum）——水位維持記錄高。
- **US 單股槓桿 ETF 核准／發行（近 30 日）**：Kioxia **9** 檔美上市單股槓桿 ETF 申報（首檔日企標的，Tuttle/GraniteShares/Corgi）（2026-07-26，https://www.tradingkey.com/analysis/stocks/us-stocks/262055692-kioxia-etf-softbank-openai-dram-skhynix-samsung-tradingkey，source_ids=structural.us_single_stock_etf）——單股槓桿產品續擴散。
- **全球（非美）槓桿產品核准（本週）**：韓／台／日／歐 07-23–07-30 無新單股槓桿／反向 ETF 英文披露、「全球槓桿擴散訊號」本週未觸發（✗ NOT DISCLOSED，source_ids=structural.global_leveraged_approvals，不納入計分）。
- **0DTE 佔 SPX 期權量**：≈**56**%（2026-02-28，Cboe 記錄值、2026 全年 >45–63% 區間高檔，https://www.cboe.com/insights/posts/spx-0-dte-options-jumped-to-record-56-share-in-feb/，source_ids=structural.zero_dte）——持續 >55% 高檔。
- **Options 總量（OCC 月報）**：OCC 6 月總量 16.0 億口、+**45**% YoY（2026-07-02，https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report，source_ids=structural.options_volume）——衍生品投機量續處高檔（stock-of-state 沿用）。
- **跨資產／相關性確認**：SKEW ≈150、VIX **19.99**（term structure contango，7/29 賣壓下溫和上行、非恐慌）（2026-07-29，https://finance.yahoo.com/quote/%5ESKEW/history/，source_ids=structural.cross_asset_derivatives）——尾端避險略升、整體波動未失控（confirmation）。
- **Margin debt / 市值 交叉檢核**：$1.502T、YoY +**51.5**%（2026-07-20，6 月數，見 D4，https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra，source_ids=structural.margin_debt_crosscheck）——確認零售槓桿頂部級別（confirmation，不在此重複計分）。
- **AI 基礎設施債務／vendor-financing loops**：CoreWeave YTD 募資 ≈$25B、GPU 擔保；5Y CDS 升至 ≈**855**bp（違約風險升、GPU 擔保債估值承壓，Nebius/CoreWeave 7/29 重挫）（2026-07-29，https://247wallst.com/investing/2026/07/29/nebius-drops-10-coreweave-sinks-9-as-rising-credit-swap-costs-hit-the-ai-cloud-trade/，source_ids=structural.ai_infrastructure_debt）——AI 基建融資本週出現抵押品／再融資壓力訊號＝結構性槓桿升溫因子。
- **銀行對 NBFI 放款**：≈$2.01T（原始 **2,012.10** 十億美元，2026-07-15，無新觀測，FRED LNFACBW027SBOG，source_ids=structural.nbfi_bank_loans）——bank–NBFI linkage 水位持平（confirmation，不主計分）。
- **美債基差交易槓桿（best-effort）**：script `cftc_lev_funds`／`move_index`／`ofr_repo` 本次 `fetch_failed`；WebSearch 未取得 7 日窗內可稽核基差交易新平倉事件（基差交易估 ≈$830B 為背景）（✗ NOT DISCLOSED，source_ids=structural.treasury_basis_trade，不納入計分、不調 D6 分數）。
**結論**：分數維持 **78**（rubric 61–80）。0DTE 續 >55%、OCC 量高檔、槓桿 ETF AUM 創高、Kioxia 單股槓桿續擴散＝結構性槓桿高檔；AI 基建融資本週出現抵押品／再融資壓力（CoreWeave CDS ≈855bp）為升溫因子，惟全球擴散未觸發、基差交易無窗內新證據為抑制——升溫與抑制相抵，淨評與前次持平。

## 綜合分數

| 維度 | 權重 | 分數 | 加權分數 |
|---|---:|---:|---:|
| 估值溢價 | 22% | 77 | 16.94 |
| 市場廣度 | 13% | 30 | 3.90 |
| 投機行為 | 18% | 58 | 10.44 |
| 散戶情緒 | 12% | 47 | 5.64 |
| 貨幣與信貸環境 | 20% | 77 | 15.40 |
| 結構性槓桿 | 15% | 78 | 11.70 |
加權總分：64.02 → 64【警戒】

邊界帶：總分 64 距 警戒/高 邊界 ≤ 2 分，評分固有噪音約 ±2–3，等級判讀需保留餘地。

## 歷史泡沫週期對比

相似度計算：checklist v2

逐項對本次六維度分數、macro/current/prior state 與附錄證據重算命中；相似度 = 命中數 ÷ 特徵數 × 100，四捨五入到最近 5%。「無資料」不計入命中但仍在分母。

- 1973/1 Nifty Fifty 頂：命中 3/8 = 40%
- 1997 早期建設：命中 3/8 = 40%
- 1998 LTCM 衝擊：命中 3/8 = 40%
- 1999 晚期狂熱：命中 4/10 = 40%
- 2000/3 頂點：命中 2/8 = 25%
- 2021/12 Meme 頂：命中 3/8 = 40%

2000/3 高位回落條件：否

**1973/1 Nifty Fifty 頂 feature audit**
- 1973.1｜未命中｜source_ids=—｜估值溢價 77 < 80
- 1973.2｜未命中｜source_ids=—｜市場廣度 30 < 60
- 1973.3｜未命中｜source_ids=—｜CPI YoY 3.46% < 4%
- 1973.4｜命中｜source_ids=—｜T5YIFR 週 Δ +4 bps ≥ 0（通膨預期未回落）
- 1973.5｜未命中｜source_ids=—｜WTI 週漲幅 0%（無新觀測）< +0.5%
- 1973.6｜未命中｜source_ids=—｜decomposition.driver=unknown ≠ breakeven（三腿視窗不一致）
- 1973.7｜命中｜source_ids=—｜扳機狀態＝已擊發 ≥ 初啟
- 1973.8｜命中｜source_ids=—｜散戶情緒 47 < 55
**1997 早期建設 feature audit**
- 1997.1｜未命中｜source_ids=—｜估值溢價 77 > 74（超出 40–74 區間）
- 1997.2｜命中｜source_ids=—｜市場廣度 30 < 45
- 1997.3｜未命中｜source_ids=—｜投機行為 58 ≥ 50
- 1997.4｜命中｜source_ids=ai.hyperscaler_capex｜hyperscaler 2026 capex 指引仍上修（合計 ≈$725B）
- 1997.5｜命中｜source_ids=—｜散戶情緒 47 < 55
- 1997.6｜未命中｜source_ids=—｜結構性槓桿 78 ≥ 50
- 1997.7｜未命中｜source_ids=—｜HY OAS 2.84% < 4% 但本週週 Δ +3 bps > 0（走闊，all 不成立）
- 1997.8｜未命中｜source_ids=—｜扳機狀態＝已擊發 ≠ 未擊發
**1998 LTCM 衝擊 feature audit**
- 1998.1｜未命中｜source_ids=structural.cross_asset_derivatives｜HY 週 Δ +3 bps < +30；VIX 19.99 contango（無壓力事件）
- 1998.2｜未命中｜source_ids=—｜S&P chg_pct −1.31% > −5%（未達回檔門檻）
- 1998.3｜命中｜source_ids=monetary.private_credit_liquidity｜具名非銀壓力：BCRED Q2 突破 5% 上限、比例撥付
- 1998.4｜未命中｜source_ids=monetary.fedwatch｜FOMC 7/29 鷹派持平、非轉鴿
- 1998.5｜命中｜source_ids=—｜估值溢價 77 ≥ 60
- 1998.6｜命中｜source_ids=—｜扳機狀態＝已擊發 ≥ 初啟
- 1998.7｜未命中｜source_ids=—｜市場廣度 Δ = 30 − 30 = 0 < +8
- 1998.8｜未命中｜source_ids=—｜ΔT10YIE +5 bps > 0（通膨預期上行）
**1999 晚期狂熱 feature audit**
- 1999.1｜命中｜source_ids=—｜估值溢價 77 ≥ 75
- 1999.2｜命中｜source_ids=valuation.sp500_pe_cape｜CAPE 40.9 ≥ 38
- 1999.3｜未命中｜source_ids=—｜投機行為 58 < 60
- 1999.4｜未命中｜source_ids=speculation.microcap_moonshots,speculation.ipo_heat｜本週 moonshot 0；無營收 IPO 佔比未達偏高
- 1999.5｜未命中｜source_ids=—｜市場廣度 30 < 45（廣度健康、非轉窄）
- 1999.6｜未命中｜source_ids=—｜D5 monetary_side＝扳機側 ≠ 自滿側，all 不成立
- 1999.7｜命中｜source_ids=—｜結構性槓桿 78 ≥ 60
- 1999.8｜未命中｜source_ids=—｜散戶情緒 47 < 55
- 1999.9｜命中｜source_ids=speculation.upcoming_ai_ipos｜巨型 AI IPO pipeline 活躍（OpenAI $1T、Anthropic 續進）
- 1999.10｜未命中｜source_ids=—｜扳機狀態＝已擊發 ≠ 未擊發
**2000/3 頂點 feature audit**
- 2000.1｜未命中｜source_ids=—｜估值溢價 77 < 85
- 2000.2｜命中｜source_ids=—｜扳機狀態＝已擊發 ≥ 初啟
- 2000.3｜未命中｜source_ids=—｜市場廣度 30 < 60
- 2000.4｜未命中｜source_ids=—｜prior sp500_dev200_pct 5.8 < +10 使第一分支為否；current chg −1.31% > −5%
- 2000.5｜未命中｜source_ids=—｜投機行為 58 < 70
- 2000.6｜命中｜source_ids=speculation.insider_form4｜14 日內合格 Form 4 cluster：CoreWeave（Intrator 07-21、McBee 07-20）
- 2000.7｜未命中｜source_ids=—｜散戶情緒 47 < 65
- 2000.8｜未命中｜source_ids=monetary.fedwatch｜FedWatch 基準仍為持平、非明確轉緊；10Y driver≠breakeven
**2021/12 Meme 頂 feature audit**
- 2021.1｜未命中｜source_ids=—｜散戶情緒 47 < 65
- 2021.2｜命中｜source_ids=retail.social_sentiment｜具名社群軋空：Beyond Meat（BYND）07-23 盤前 +10%（37% 空頭）
- 2021.3｜命中｜source_ids=—｜結構性槓桿 78 ≥ 65
- 2021.4｜未命中｜source_ids=—｜D5 monetary_side＝扳機側 ≠ 自滿側，all 不成立
- 2021.5｜命中｜source_ids=retail.margin_debt｜margin debt YoY +51.5% ≥ +40%
- 2021.6｜未命中｜source_ids=speculation.microcap_moonshots｜本週 microcap moonshot 0 < 1
- 2021.7｜未命中｜source_ids=—｜市場廣度 30 < 50
- 2021.8｜未命中｜source_ids=—｜CPI YoY 3.46% < 4%，all 不成立

**兩句解讀**：本週五個錨點（1973/1、1997、1998、1999、2021/12）並列 40%，依 contract 錨點順序取「1973/1 Nifty Fifty 頂」為最貼近——此為**政權訊號**（通膨制約下的窄領導頂部組態），而非科技泡沫週期相位：CPI YoY 3.46%、通膨預期回升（T5YIFR 週 +4 bps）、Fed 鷹派持平受限、Top-10 集中度 ≈38% 的窄領導、散戶未狂熱（F&G 37 Fear、AAII Bull 29.6%）共同構成「高估值＋窄領導＋通膨約束＋散戶不熱」的 Nifty Fifty 型組態。惟需嚴格跟隨機器判定：扳機鏈 A 尚未驗證啟動（driver≠breakeven、WTI 持平、1973.6 未命中），且 1973.3 未命中（CPI < 4%）故不可據 CPI／5y5y 述「Fed 寬鬆空間受壓縮」超出證據；本週實際擊發的是槓桿鏈 B 的非銀融資扳機（BCRED gate proration，1998 型），而非通膨鏈。循環位置意涵：估值＋槓桿位能高企、時點扳機已由私募信貸端點燃，最須盯 AI 信用重定價（Oracle BBB-、CoreWeave CDS ≈855bp）與私募信貸閘門是否外溢至公開利差。長期指數成長趨勢偏離（Dot-com ≈95%、1929 ≈110%、當前 AI 週期 ≈147%；RIA/Farrell）作跨期敘事錨、不進 checklist。

## 機構情緒對照

本次無新機構調查數據。

## 本次新增訊號

比較基準：vs 前次（3天前）。

- **貨幣與信貸環境（D5）Δ +2，且＝扳機側**：私募信貸扳機延續（Blackstone 2026-07-23 確認 BCRED 突破 5% 上限、贖回 ≈10% NAV 比例撥付；Blue Owl 07-02 對 19–38% 贖回比例撥付），扳機狀態維持「已擊發」；本週 financing-trigger 側升溫——FOMC 7/29 鷹派持平（9-3）、通膨預期回升（T5YIFR +4 bps）、期限溢價上行、AI 雲端信用明顯重定價（Oracle 遭降至 BBB-、CoreWeave 5Y CDS ≈855bp），故分數自 75 升至 77（雙向計分中扳機側質變見此，非僅 macro 水位）。
- **估值溢價（D1）Δ -1**：價格趨勢偏離自 +5.8% 回落至 +4.29%、Mag7 對其餘 493 檔溢價壓縮至 ≈10%——估值面小幅緩和；CAPE 40.9 仍近史高、capex 續上修（$725B）與 AI 信用重定價同框對沖，淨降 1 分。
- **散戶情緒（D4）Δ -1**：CNN F&G 39→37（續 Fear）、NAAIM 95.64→84.02（減碼）、AAII 多方 29.6% 偏空＝情緒續降溫；margin debt 6 月創高（YoY +51.5%）與 BYND 軋空為抑跌，淨降 1 分。
- 結構性槓桿（D6，Δ 0）雖分數持平，惟本週 AI 基建融資出現抵押品／再融資壓力（CoreWeave 5Y CDS ≈855bp、Nebius/CoreWeave 7/29 重挫）、US 單股槓桿續擴散（Kioxia 9 檔）——**全球（非美）擴散訊號未觸發，本週擴散訊號未觸發**。
- 其餘維度（廣度 30、投機 58）分數與前次持平；總分 64【警戒】、Δ 0。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | S&P 500 收盤（sp500_trend latest） | 7,316.15 | FRED SP500（sp500_trend） | 2026-07-29 | 2026-07-30T09:15:00+08:00 |
| valuation.sp500_trend | S&P 500 距 200DMA 偏離（sp500_trend dev200_pct） | +4.29% | FRED SP500（sp500_trend） | 2026-07-29 | 2026-07-30T09:15:00+08:00 |
| valuation.sp500_trend | S&P 500 距 52 週均線偏離（sp500_trend dev52w_pct） | +5.83% | FRED SP500（sp500_trend） | 2026-07-29 | 2026-07-30T09:15:00+08:00 |
| retail.household_equity_allocation | 家庭持股佔金融資產比（BOGZ1FL153064486Q） | 45.76 | FRED BOGZ1FL153064486Q | 2026-01-01 | 2026-07-30T09:15:00+08:00 |
| monetary.fed_funds | Fed funds 上限（DFEDTARU） | 3.75% | FRED DFEDTARU | 2026-07-29 | 2026-07-30T09:15:00+08:00 |
| monetary.fed_funds | Fed funds 下限（DFEDTARL） | 3.50% | FRED DFEDTARL | 2026-07-29 | 2026-07-30T09:15:00+08:00 |
| monetary.hy_oas | HY OAS（BAMLH0A0HYM2） | 2.84% | FRED BAMLH0A0HYM2 | 2026-07-28 | 2026-07-30T09:15:00+08:00 |
| monetary.ig_oas | IG OAS（BAMLC0A0CM） | 0.81% | FRED BAMLC0A0CM | 2026-07-28 | 2026-07-30T09:15:00+08:00 |
| monetary.dgs10 | 10Y 名目殖利率（DGS10） | 4.61% | FRED DGS10 | 2026-07-28 | 2026-07-30T09:15:00+08:00 |
| monetary.dfii10 | 10Y 實質殖利率（DFII10） | 2.41% | FRED DFII10 | 2026-07-28 | 2026-07-30T09:15:00+08:00 |
| monetary.t10yie | 10Y breakeven（T10YIE） | 2.26% | FRED T10YIE | 2026-07-29 | 2026-07-30T09:15:00+08:00 |
| monetary.wti | WTI 原油（DCOILWTICO） | $84.25 | FRED DCOILWTICO | 2026-07-27 | 2026-07-30T09:15:00+08:00 |
| monetary.cpi_yoy | CPI YoY（CPIAUCSL yoy_pct） | 3.46% | FRED CPIAUCSL | 2026-06-01 | 2026-07-30T09:15:00+08:00 |
| monetary.t5yifr | 5y5y forward（T5YIFR latest） | 2.28% | FRED T5YIFR | 2026-07-29 | 2026-07-30T09:15:00+08:00 |
| monetary.term_premium | 10Y 期限溢價（THREEFYTP10） | 0.8376% | FRED THREEFYTP10 | 2026-07-24 | 2026-07-30T09:15:00+08:00 |
| monetary.repo_stress_srf | SOFR 隔夜利率 | 3.65% | FRED SOFR | 2026-07-28 | 2026-07-30T09:15:00+08:00 |
| monetary.repo_stress_srf | SOFR99 99th 分位尾端 | 3.74% | FRED SOFR99 | 2026-07-28 | 2026-07-30T09:15:00+08:00 |
| monetary.repo_stress_srf | IORB 準備金利率 | 3.65% | FRED IORB | 2026-07-30 | 2026-07-30T09:15:00+08:00 |
| monetary.repo_stress_srf | 隔夜 repo 操作量（RPONTTLD） | 0.003 | FRED RPONTTLD | 2026-07-29 | 2026-07-30T09:15:00+08:00 |
| monetary.walcl | Fed 資產負債表（WALCL） | 6,747,378 百萬美元（≈$6.75T） | FRED WALCL | 2026-07-22 | 2026-07-30T09:15:00+08:00 |
| monetary.ecb_boj | ECB 資產（ECBASSETSW） | 5,944,015 百萬歐元（≈€5.94T） | FRED ECBASSETSW | 2026-07-24 | 2026-07-30T09:15:00+08:00 |
| monetary.ecb_boj | BOJ 資產（JPNASSETS） | 6,395,509 億日圓（≈¥639.55T） | FRED JPNASSETS | 2026-06-01 | 2026-07-30T09:15:00+08:00 |
| structural.nbfi_bank_loans | 銀行對 NBFI 放款（LNFACBW027SBOG） | 2,012.10 十億美元（≈$2.01T） | FRED LNFACBW027SBOG | 2026-07-15 | 2026-07-30T09:15:00+08:00 |

### Coverage

| source_id | 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl/gurufocus [primary: SEARCH] | ✓ SEARCH-VERIFIED（P/E 28.6、CAPE 40.9 @07-29） |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E | CNBC/Morgan Stanley [SEARCH]（stock-of-state 沿用） | ✓ SEARCH-VERIFIED（溢價 ≈10% @07-08） |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（MS NVDA $288 EPS-driven @07-13） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500 派生） | ✓ API（dev200 +4.29%／dev52 +5.83%） |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧 | 信用市場 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Oracle BBB-、CoreWeave CDS ≈855bp @07-29） |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst [SEARCH] | ✓ SEARCH-VERIFIED（RSP +14.57% YTD、領先 SPY ≈+5pp @07-26） |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | Forbes/財經媒體 [SEARCH] | ✓ SEARCH-VERIFIED（≈38%，歷史高位） |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NYSE breadth [SEARCH] | ✓ SEARCH-VERIFIED（新高 161／新低 198，新低反超 @07-27） |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（37 Fear @07-29） |
| retail.margin_debt | 散戶｜Margin Debt: FINRA | FINRA/Advisor Perspectives [SEARCH]（月頻 stock-of-state） | ✓ SEARCH-VERIFIED（$1.502T、+51.5% YoY、2026-06 創高） |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（Bull 29.6%／Bear 42.3% @07-23） |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB/cashtag [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（BYND 軋空 +10%、37% 空頭 @07-23） |
| retail.household_equity_allocation | 散戶｜Household equity allocation | fetch_macro.py BOGZ1FL153064486Q | ✓ API（45.76% @2026-Q1） |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim/YCharts [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（84.02 @07-22） |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM | 賣方調查 [SEARCH]（月頻，best-effort） | ✗ NOT DISCLOSED（7 月 FMS 07-14 發布、早於前次基準、非本次新增） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED DFEDTARU/DFEDTARL | fetch_macro.py FRED API | ✓ API（3.75%/3.50% @07-29） |
| monetary.hy_oas | 貨幣｜High Yield OAS | fetch_macro.py FRED API | ✓ API（2.84% @07-28，Δ+3bps） |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | fetch_macro.py FRED API | ✓ API（0.81% @07-28，Δ0） |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | fetch_macro.py FRED API | ✓ API（4.61% @07-28，Δ−4bps） |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield | fetch_macro.py FRED API | ✓ API（2.41% @07-28，Δ−3bps） |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | fetch_macro.py FRED API | ✓ API（2.26% @07-29，Δ+5bps） |
| monetary.wti | 貨幣｜WTI crude oil price | fetch_macro.py FRED API | ✓ API（$84.25 @07-27，no_new_obs） |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED | fetch_macro.py FRED API（月頻） | ✓ API（3.46% @2026-06） |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | fetch_macro.py FRED API | ✓ API（2.28% @07-29，Δ+4bps） |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED | fetch_macro.py FRED API | ✓ API（0.8376% @07-24，+5.9bps trailing） |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py repo_stress | ✓ API（SOFR−IORB 0bps、SOFR99−IORB +9bps、SRF ≈$0.003B @07-28/29） |
| monetary.treasury_auctions | 貨幣｜美債標售需求 | Reuters/cryptobriefing [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（20Y dealer takedown 14.67% @07-22） |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（FOMC 持平、9 月 ≈42% 持平 @07-29） |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED WALCL | fetch_macro.py FRED API | ✓ API（$6.75T @07-22，no_new_obs） |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | fetch_macro.py FRED API | ✓ API（€5.94T @07-24／¥639.55T @06-01） |
| monetary.pboc | 貨幣｜PBoC aggregate financing | Bloomberg [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（MLF 淨投放 ¥100B、月底逆回購 ¥2.1T @07-24） |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（BCRED Q2 突破 5% 上限、Blue Owl 07-02 比例撥付 @07-23） |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報 [SEARCH]（stock-of-state） | ✓ SEARCH-VERIFIED（合計 ≈$725B、仍上修 @07-28） |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic/OpenAI/Google [SEARCH]（best-effort） | ✗ NOT DISCLOSED（本季無乾淨量化成長率披露） |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch/報導 [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Anthropic ≈$47B／OpenAI ≈$25B run-rate @06-15） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration | 財報電話 [primary: SEARCH]（best-effort） | ✗ NOT DISCLOSED（本次無乾淨窗內一手 RPO 披露） |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（DRAM +13–18% QoQ 3Q26 @07-03；供給仍被吸收） |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構 | 季報/發債 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口 | 組合披露 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（年化 capex ≈$725B vs 終端營收低百億級 @06-15） |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K/10-Q [primary: SEARCH]（best-effort，30日） | ✗ NOT DISCLOSED（過去 30 日無新變更） |
| ai.capital_cycle | AI｜資本週期階段 | 供需增速+進出場事件 [SEARCH]（best-effort） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days +AI rename/SPAC | [SEARCH] | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | Renaissance/emarketer [SEARCH] | ✓ SEARCH-VERIFIED（$251B/88 檔、Cerebras +68% @07-28） |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz/Benzinga [primary: SEARCH]（required 週螢幕） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | S-1/具名報導 [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（OpenAI $1T IPO、Anthropic 續進 @07-28） |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership | SEC EDGAR [primary: EDGAR]（required） | ✓ SEARCH-VERIFIED（CoreWeave cluster：Intrator/McBee 07-20/21） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe/YCharts [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（0.66 @07-27） |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing/etf.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（總 ≈$198B 創高 @07-23） |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | Tradr/GraniteShares [SEARCH] | ✓ SEARCH-VERIFIED（Kioxia 9 檔申報 @07-26） |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX/TWSE/JPX/ESMA [SEARCH]（best-effort，7日） | ✗ NOT DISCLOSED（本週擴散訊號未觸發） |
| structural.zero_dte | 結構｜0DTE option volume | Cboe [SEARCH]（Cboe 403） | ✓ SEARCH-VERIFIED（≈56%，Cboe @2026-02） |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com [SEARCH] | ✓ SEARCH-VERIFIED（6 月 16.0 億口、+45% YoY @07-02） |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe/Yahoo [SEARCH] | ✓ SEARCH-VERIFIED（SKEW ≈150、VIX 19.99 contango @07-29） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 D4（confirmation） | ✓ SEARCH-VERIFIED（$1.502T/+51.5% YoY，D4 引用不重複計分） |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]（best-effort，30日） | ✓ SEARCH-VERIFIED（CoreWeave CDS ≈855bp、GPU 擔保債壓力 @07-29） |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | fetch_macro.py FRED API | ✓ API（$2.01T @07-15，no_new_obs） |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | script→WebSearch [primary: script]（best-effort） | ✗ NOT DISCLOSED（cftc/move/ofr script fetch_failed，無 7 日窗內基差交易新事件） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 28.6 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio | 2026-07-29 | 2026-07-30T09:15:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 40.9 | Shiller CAPE ratio July 2026 | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio | 2026-07-29 | 2026-07-30T09:15:00+08:00 |
| valuation.mag7_multiples | Mag 7 對其餘 493 檔溢價 ≈10% | Magnificent 7 valuation premium cheapest decade 2026 | https://www.cnbc.com/2026/07/08/magnificent-seven-stocks-are-the-cheapest-in-a-decade-by-one-measure.html | 2026-07-08 | 2026-07-30T09:15:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標 未擴張（≈22× CY27 EPS）、目標價 $288 | Morgan Stanley NVDA target 288 July 2026 EPS | https://www.gurufocus.com/news/8955458/morgan-stanley-upgrades-nvidia-nvda-with-a-288-target-price | 2026-07-13 | 2026-07-30T09:15:00+08:00 |
| valuation.ai_credit_schism | Oracle 遭降至 BBB-、AI 雲端信用重定價，CoreWeave 5Y CDS ≈855bp | Oracle BBB- CoreWeave CDS AI credit repricing July 2026 | https://247wallst.com/investing/2026/07/29/nebius-drops-10-coreweave-sinks-9-as-rising-credit-swap-costs-hit-the-ai-cloud-trade/ | 2026-07-29 | 2026-07-30T09:15:00+08:00 |
| breadth.rsp_spy | SPY +9.22% YTD、RSP 等權 +14.57% | RSP vs SPY equal weight YTD 2026 | https://247wallst.com/investing/2026/07/26/is-equal-weighting-the-sp-500-worth-it-heres-what-the-data-says/ | 2026-07-26 | 2026-07-30T09:15:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 ≈38% | S&P 500 top 10 concentration percent 2026 | https://www.forbes.com/sites/investor-hub/article/sp-500-weight-mag-7-stocks-diversification-risk/ | 2026-07-15 | 2026-07-30T09:15:00+08:00 |
| breadth.advance_decline | NYSE advancers 1.32:1、新高 161、新低 198 | NYSE advance decline new highs new lows July 27 2026 | https://finance.yahoo.com/markets/stocks/articles/stock-market-news-july-27-132000679.html | 2026-07-27 | 2026-07-30T09:15:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 37（Fear） | CNN Fear and Greed Index July 29 2026 | https://www.cnn.com/markets/fear-and-greed | 2026-07-29 | 2026-07-30T09:15:00+08:00 |
| retail.margin_debt | FINRA margin debt 6 月 $1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra | 2026-07-20 | 2026-07-30T09:15:00+08:00 |
| retail.aaii | AAII Bear 42.3%／Neutral 28.1%／Bull 29.6% | AAII investor sentiment survey July 23 2026 | https://www.aaii.com/sentimentsurvey | 2026-07-23 | 2026-07-30T09:15:00+08:00 |
| retail.social_sentiment | Beyond Meat（BYND）空頭 37%、r/wallstreetbets 軋空、盤前 +10% | Beyond Meat BYND wallstreetbets short squeeze July 2026 | https://www.asktraders.com/analysis/wendys-nasdaq-wen-stock-turns-meme-darling-amid-short-squeeze-and-activist-buzz/ | 2026-07-23 | 2026-07-30T09:15:00+08:00 |
| retail.naaim | NAAIM 前值 95.64 → 最新 84.02 | NAAIM exposure index July 2026 | https://ycharts.com/indicators/naaim_number | 2026-07-22 | 2026-07-30T09:15:00+08:00 |
| monetary.treasury_auctions | 20Y 標售 dealer takedown 14.67%（長端需求偏弱） | US Treasury auction July 2026 dealer takedown bid to cover | https://www.cryptobriefing.com/us-treasury-10-year-note-auction-4580-yield/ | 2026-07-22 | 2026-07-30T09:15:00+08:00 |
| monetary.fedwatch | FOMC 維持 3.50–3.75%（9-3 票）、CME FedWatch 9 月持平機率 ≈42% | FOMC July 29 2026 hold FedWatch September | https://www.cnbc.com/2026/07/29/fed-rate-decision-july-2026.html | 2026-07-29 | 2026-07-30T09:15:00+08:00 |
| monetary.pboc | 人行 MLF 5 個月最大、淨投放 ≈¥100B | PBoC MLF net injection liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-24/pboc-adds-most-liquidity-to-economy-in-five-months-to-aid-growth | 2026-07-24 | 2026-07-30T09:15:00+08:00 |
| monetary.private_credit_liquidity | [private_credit_gate] BCRED Q2 突破 5% 季度贖回上限、比例撥付、贖回需求升至 ≈10% NAV | Blackstone BCRED Blue Owl redemption gate 5% cap July 2026 | https://www.bloomberg.com/news/articles/2026-07-02/blue-owl-bdcs-impose-caps-after-facing-19-38-requests-to-exit | 2026-07-23 | 2026-07-30T09:15:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 續上修：Amazon $200B、Alphabet $205B、Meta $125–145B、合計 ≈$725B | hyperscaler capex 2026 725B raised Meta Amazon Alphabet | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-07-28 | 2026-07-30T09:15:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic run-rate ≈$47B、OpenAI ≈$25B | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-06-15 | 2026-07-30T09:15:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 交期 30–40 週、3Q26 合約價續漲 +13–18% QoQ | DRAM HBM contract price 3Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260703-13134.html | 2026-07-03 | 2026-07-30T09:15:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] Alphabet Q2 FCF 轉負、FY26 capex 上修至 ≈$205B | Alphabet Q2 2026 capex FCF negative debt | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-07-28 | 2026-07-30T09:15:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] hyperscaler 2026 發債 +1,300% YoY 至累計 ≈$182B | hyperscaler bond issuance 182B 2026 AI credit | https://247wallst.com/investing/2026/07/16/the-ai-revolution-is-reshaping-credit-markets-here-is-what-it-really-says-about-risk/ | 2026-07-16 | 2026-07-30T09:15:00+08:00 |
| ai.revenue_capex_gap | AI 終端年化營收 Anthropic ≈$47B＋OpenAI ≈$25B vs 年化 capex ≈$725B | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-06-15 | 2026-07-30T09:15:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 螢幕合格件數 0 | AI rename SPAC no revenue IPO July 23-30 2026 | Reuters/Benzinga/Boardroom Alpha SPAC 螢幕 | 2026-07-30 | 2026-07-30T09:15:00+08:00 |
| speculation.ipo_heat | 2026 IPO 募資 $251B、88 檔、Cerebras（CBRS）首日 +68% | US IPO market 2026 Cerebras first day pop | https://www.emarketer.com/content/ipos-test-investor-appetite-unprofitable-ai-giants | 2026-07-28 | 2026-07-30T09:15:00+08:00 |
| speculation.microcap_moonshots | 本週 microcap thematic moonshot 合格 0 件 | microcap 100% single day quantum AI fusion moonshot July 2026 | Finviz/Benzinga/StockTwits/Yahoo movers 螢幕 | 2026-07-30 | 2026-07-30T09:15:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 考慮延至 2027 IPO、目標估值 ≈$1T；Anthropic 續進程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground | 2026-07-28 | 2026-07-30T09:15:00+08:00 |
| speculation.insider_form4 | CoreWeave 10b5-1 內部人 cluster：McBee 07-20 ≈$14.6M、CEO Intrator 07-21 售 307,692 股 ≈$24.1M | CoreWeave insider Form 4 July 2026 Intrator McBee SEC | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001769628&type=4 | 2026-07-21 | 2026-07-30T09:15:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.66 | Cboe equity put call ratio July 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio | 2026-07-27 | 2026-07-30T09:15:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高 ≈$198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-07-23 | 2026-07-30T09:15:00+08:00 |
| structural.us_single_stock_etf | Kioxia 9 檔美上市單股槓桿 ETF 申報（首檔日企標的） | single-stock leveraged ETF launch July 2026 Kioxia Tuttle | https://www.tradingkey.com/analysis/stocks/us-stocks/262055692-kioxia-etf-softbank-openai-dram-skhynix-samsung-tradingkey | 2026-07-26 | 2026-07-30T09:15:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量 ≈56%（Cboe 記錄） | 0DTE SPX options share volume 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jumped-to-record-56-share-in-feb/ | 2026-02-28 | 2026-07-30T09:15:00+08:00 |
| structural.options_volume | OCC 6 月總量 16.0 億口、+45% YoY | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report | 2026-07-02 | 2026-07-30T09:15:00+08:00 |
| structural.cross_asset_derivatives | SKEW ≈150、VIX 19.99（term structure contango） | VIX SKEW term structure July 29 2026 | https://finance.yahoo.com/quote/%5ESKEW/history/ | 2026-07-29 | 2026-07-30T09:15:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt $1.502T、+51.5% YoY（交叉引用 D4） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra | 2026-07-20 | 2026-07-30T09:15:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave YTD 募資 ≈$25B、GPU 擔保；5Y CDS 升至 ≈855bp（違約風險升） | AI data center debt financing CoreWeave CDS July 2026 | https://247wallst.com/investing/2026/07/29/nebius-drops-10-coreweave-sinks-9-as-rising-credit-swap-costs-hit-the-ai-cloud-trade/ | 2026-07-29 | 2026-07-30T09:15:00+08:00 |

## 本次分數存檔
```json
{
  "date": "2026-07-30",
  "iso_week": "2026-W31",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "valuation": 77,
  "breadth": 30,
  "speculation": 58,
  "retail": 47,
  "monetary": 77,
  "structural": 78,
  "total": 64,
  "tier": "警戒",
  "regime": "穩定共存",
  "trigger_state": "已擊發",
  "trigger_reasons": [
    "private_credit_gate"
  ],
  "monetary_side": "扳機側",
  "hy_oas_widening_streak": 1,
  "sp500_dev200_pct": 4.29
}
```

本報告為相對風險溫度計，非擇時訊號。

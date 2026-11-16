# 2026-07-16 市場泡沫風險評估報告
> 報告日期：2026-07-16；執行日：2026-07-16 Asia/Taipei；ISO 週次：2026-W29；前次基準：report-2026-07-13（3天前）

**總評**：總分 64【警戒】（Δ 0）；扳機狀態：已擊發；最貼近錨點：1998 LTCM 衝擊（50%）。

## §1 六維度風險條圖
| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▱▱▱ | 79 | 79 | 0 |
| 市場廣度 | ▰▰▰▱▱▱▱▱▱▱ | 30 | 30 | 0 |
| 投機行為 | ▰▰▰▰▰▱▱▱▱▱ | 58 | 58 | 0 |
| 散戶情緒 | ▰▰▰▰▰▱▱▱▱▱ | 50 | 51 | -1 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▰▱▱▱ | 75 | 75 | 0 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 77 | 77 | 0 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **64【警戒】** | 64 | 0 |

## §2 歷史錨點相似度
| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1997 早期建設 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 1998 LTCM 衝擊 | 50% | ▰▰▰▰▰▱▱▱▱▱ | ◀ 最貼近 |
| 1999 晚期狂熱 | 30% | ▰▰▰▱▱▱▱▱▱▱ |  |
| 2000/3 頂點 | 15% | ▰▱▱▱▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |

## §3 三角訊號
| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,572.4 | ▲ +0.76%（前次 ≈7,515.34） |
| WTI 原油 | $79.2 /bbl | 持平 0%（無新觀測，前次 ≈$79.2） |
| 10Y Treasury | 4.58% | ▼ −4 bps（前次 ≈4.62%） |

**三者狀態**：出現分歧（10Y 在反向重新定價）——股市 ▲ 而 10Y ▼、WTI 持平，三者未同向；S&P `dev200_pct` ≈+8.51%（< +10% 拉伸門檻）。
- 股市：指數 ≈7,572.4（S&P 500，2026-07-15 收），較前次 ▲ +0.76%（前次 ≈7,515.34），距 200 日均線 +8.51%、距 52 週均線 +10.25%——價格延伸偏高但非急拉。
- WTI 原油：≈$79.2/bbl（2026-07-13，無新觀測），較前次 持平 0%。
- 10Y 殖利率：4.58%（2026-07-14），較前次 ▼ −4 bps（前次 ≈4.62%），主要驅動：三腿視窗不一致（driver=unknown），名目／實質／breakeven 週變動同為負向、幅度相近。
**格局轉變**：前次格局＝穩定共存（讀自 report-2026-07-13 的 `regime`）→ 本次格局＝分歧；由三者共存轉為 10Y 反向、格局轉變。
**10Y 成因拆解**：拆的是週變動（bps）、非水位（`ΔDGS10 ≈ ΔDFII10 + ΔT10YIE`）；三腿視窗不一致（`decomposition.driver=unknown`——ΔT10YIE 取自不同視窗、恆等式不跨視窗成立），判定 不可判（視窗不一致）；三腿實際 signed 週變動如下（新鮮度 updated）：
- ΔDGS10 名目殖利率週變動：−4 bps
- ΔDFII10 實質殖利率週變動：−3 bps
- ΔT10YIE 損益平衡通膨週變動：−3 bps
**扳機鏈**：A 通膨鏈（油 → 通膨預期 → Fed 受限 → refinancing 成本）本週未加速——WTI 持平（≈$79.2，無新觀測）、實現通膨回落：[monetary.cpi_yoy] CPIAUCSL yoy_pct=3.46 data_date=2026-06-01（6 月，較 5 月 4.17% 明顯回落）、5y5y forward [monetary.t5yifr] T5YIFR latest=2.21 delta_bps=0 data_date=2026-07-15（持平）；CME FedWatch 7/29 會議 ≈70% 持平（2026-07-08），Fed 仍受 3.46% 通膨與財政供給牽制，惟通膨降溫略放鬆約束、Fed put 可得性中性偏回升；無當期電價／能源瓶頸新報導。B 槓桿鏈（衝擊：財政風險再定價 → NBFI 去槓桿 → margin spiral → 國債市場失序 → 官方市場功能回應）乾柴堆積但未點火——衝擊節點：10Y 期限溢價 THREEFYTP10 ≈0.7788%（序列自身 trailing ≈7d +4.7 bps，溫和上行）、美債標售需求穩健（7/8 10Y bid-to-cover 2.565、7/9 30Y 2.44），財政再定價壓力溫和；NBFI 節點：script `cftc_lev_funds`／`move_index`／`ofr_repo` 本次 fetch_failed，改走 WebSearch——MOVE ≈77.77（2026-07-14，低於 80–100 常態區、subdued），CFTC 槓桿基金美債期貨仍淨空（COT 07-07、近報導紀錄區、精確當週值未鎖定），無基差／swap-spread 平倉報導；官方回應節點：`repo_stress` SOFR−IORB −2 bps、SOFR99−IORB +7 bps、SRF 動用 $0.102bn（例行、非失序），無市場功能干預。real-rate 主導的異常 10Y 上行本週不存在（10Y 週 −4 bps）。本鏈證據 best-effort，本週無基差交易槓桿新積累／釋放事件。
**扳機理由**：private_credit_gate
⚠ **結論**：扳機狀態：已擊發——本次命中「私募信貸 gate proration / breach」：Q2 2026 多檔非交易 BDC／私募信貸區間基金實際觸及 5% 季度贖回上限並比例撥付（Blue Owl OCIC 贖回需求 ≈18.8% NAV、比例撥付；Apollo ADS 與 Blackstone BCRED 亦於 Q2 gated，詳 §D5／本次新增訊號），此為 1998 LTCM 型「融資扳機」特徵——非銀信用先於公開 mark-to-market 利差（HY 2.72%／IG 0.79% 仍史窄）出現一階壓力。三者配置歷史意義：估值＋槓桿＝崩跌位能，融資緊縮＝時點扳機；本週公開利差自滿與非銀融資扳機並存（自滿側 froth 與扳機側 financing 壓力同框），惟三角資產本身分歧（非同向偏高）、槓桿鏈 B 未點火，失序尚屬結構化產品閘門層級、非國債市場層級。

## 六維度評分

### 1. 估值溢價 — 79（weight 22%，Δ 0）
- **S&P 500 trailing P/E** ≈**32.59**（2026-07-15，https://www.multpl.com/s-p-500-pe-ratio，source_ids=valuation.sp500_pe_cape）——較前次 32.60 持平、近歷史高位。
- **Shiller CAPE** ≈**42.18**（2026-07-15，multpl.com/shiller-pe，source_ids=valuation.sp500_pe_cape）——與前次持平，逼近歷史高（≈44）。
- **Excess CAPE Yield（ECY）** ≈**0.04%**（`1/42.18 − 2.33/100`，derived 自 CAPE 42.18 與 DFII10 2.33%，2026-07-15，source_ids=valuation.sp500_pe_cape）——接近 0，屬 1929／2000 級別股相對債極貴訊號（confirmation，不主計分）。
- **Mag 7 加權 P/E** trailing ≈**40**（2026-05-15，https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026，source_ids=valuation.mag7_multiples）——絕對高，但對 S&P 溢價為近十年較窄區。
- **價格趨勢偏離（Farrell #1/#2/#4）** S&P 距 200 日均線 **+8.51%**、距 52 週均線 +10.25%（`sp500_trend`，2026-07-15，FRED SP500，source_ids=valuation.sp500_trend）——較前次 +8.76% 微降，價格延伸偏高但未達急拉，與 P/E／CAPE 互補、不重複計分。
- **AI capex 現實檢核**：hyperscaler 2026 capex 指引合計 ≈**$700B（仍在上修，+約 36% YoY）**（2026-05-15，finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html，source_ids=ai.hyperscaler_capex）——基本面敘事仍撐估值。
- **AI compute 供需現實檢核**：伺服器 DRAM 2Q26 合約 **+58–63% QoQ**（TrendForce，2026-06-02，trendforce.com/presscenter/news/20260602-13074.html，source_ids=ai.compute_supply_demand）、H100 一年期租金 +40%、產能訂滿至 3Q26——供給仍被合約與 token 需求吸收，缺口未成形、非惡化確認。
- **AI 營收對 capex 缺口現實檢核**：分母年化 capex ≈**$700B**（分母：top-4＋Oracle）vs 分子已披露 AI 終端年化營收（Anthropic ≈$47B、OpenAI ≈$25B run-rate）量級缺口仍大且 capex 續升（2026-05-15，epoch.ai/data-insights/anthropic-openai-revenue，source_ids=ai.revenue_capex_gap）——回本假設後移，屬估值風險上修的質化依據（缺口未收斂）。
- **AI 信用定價分歧（equity-vs-credit schism）**：Oracle 5yr CDS ≈**198 bp**（16 年新高、走闊）vs CDX.NA.IG ≈95 bp（2026-07-10，investing.com/analysis/oracle-and-coreweave-credit-default-swap-spreads-widening-omen-or-jitters-200670506，source_ids=valuation.ai_credit_schism）——AI 發行人利差為 IG 基準數倍，信用端開始重定價而股權未跟＝後期訊號側（confirmation，不主計分）。
- **TP-upgrade phase signal**：過去 90 日同季內無新披露 EPS-vs-multiple 分解的具名賣方升評（本季 Q3 尚早、多數銀行未披露分解）（✗ NOT DISCLOSED，source_ids=valuation.analyst_tp_decomposition，不納入計分）。
- **折舊年限變動（盈餘品質）**：過去 30 日無新 10-K／10-Q 折舊年限或殘值假設變更披露（財報季未啟）（✗ NOT DISCLOSED，source_ids=ai.depreciation_life，不納入計分）。
- **backlog 重複計算風險（RPO double-counting）**：本次無新客戶集中度／RPO 披露（Oracle FQ4 後無新一手更新）（✗ NOT DISCLOSED，source_ids=ai.customer_concentration_rpo，不納入計分）。
- **Hyperscaler 融資結構＋資本週期**：本次無新可組合的融資結構事件掃描與週期增速披露（財報季未啟、30 日內無 hyperscaler 自身發債事件）（✗ NOT DISCLOSED，source_ids=ai.hyperscaler_financing_mix,ai.capital_cycle，不納入計分）。
**結論**：分數維持 **79**（rubric 高位）。P/E 32.59／CAPE 42.18 持平、ECY 近 0、Mag7 高檔、趨勢偏離 +8.51% 與 capex 續升敘事同框；供需邊際仍被吸收、缺口未收斂尚未轉為 guidance 下修，故較前次持平。

### 2. 市場廣度 — 30（weight 13%，Δ 0）
- **RSP（等權）vs SPY（市值權）YTD**：RSP ≈**+9.67%** vs SPY ≈+8.38%（2026-06-26，247wallst.com/investing/2026/06/26/forget-the-magnificent-seven-this-equal-weight-sp-fund-beats-the-mega-caps-for-just-0-20/，source_ids=breadth.rsp_spy）——等權領先市值權 ≈+1.3 pp，廣度為轉寬／健康方向、非背離。
- **Top-10 集中度**：≈**35.59%**（2026-04-30，S&P DJI factor dashboard，spglobal.com/spdji/en/documents/performance-reports/dashboard-sp-500-factor.pdf，source_ids=breadth.top10_concentration）——絕對偏高但較前次 36.40% 微降、未再創高。
- **Advance/Decline 與新高/新低**：NYSE 2026-07-13 上漲 **2008** 家 vs 下跌 2749 家、累積 A/D 線仍處建設性高位（mcoscillator.com/market_breadth_data/，source_ids=breadth.advance_decline）——近端單日轉弱但中期 A/D 線未破壞、廣度確認。
**結論**：分數維持 **30**（rubric 21–40 偏健康端）。等權領先＋A/D 線中期確認＝廣度健康／轉寬，唯 Top-10 ≈35.6% 仍偏高為殘餘風險；淨評與前次持平。

### 3. 投機行為 — 58（weight 18%，Δ 0）
- **+AI 改名／SPAC**：本週 **1 件**具名 SPAC 上市——General Fusion（GFUZ）與 Spring Valley Acquisition III 完成 SPAC 合併、2026-07-10 起交易，成首檔上市核融合公司（≈$150M 現金）（morningstar.com/news/pr-newswire/20260710ln02448/，source_ids=speculation.ai_rename_spac）；xAI→SpaceXAI 品牌更名（07-06）落 7 日窗外、作背景。無無營收 IPO 暴衝。
- **IPO 熱度**：2026 YTD ≈**200** 檔（+8.2% YoY）、募資 ≈$141.2B（含 SK Hynix $26.5B 交叉掛牌）（2026-07-13，axios.com/2026/07/13/us-ipo-market-record-proceeds，source_ids=speculation.ipo_heat）——市場活躍、秩序尚可，first-day pop／無營收佔比精確值未取得。
- **Microcap thematic moonshots**：本週 **0 件**合格（<$1B 市值、單日 ≥100%、堆疊 2+ 熱主題＋弱基本面；2026-07-16 螢幕）——✓ SEARCH-VERIFIED（0 件）（source_ids=speculation.microcap_moonshots）；AEHR +43.6% 但市值 $3.25B 且 <100%，NNBR +159% 為 YTD 非單日，皆不合格。
- **Insider selling clusters**：required 螢幕已執行（2026-07-16 螢幕）；14 日內無法取得具 SEC EDGAR Form 4 filing／transaction 日期＋URL 的合格 cluster（EDGAR egress 受限；DDOG／AAOI 僅二手彙整、不計分）——**0 件合格**（✓ SEARCH-VERIFIED（0 件），source_ids=speculation.insider_form4）。
- **Cboe equity-only put/call**：≈**0.62**（2026-07-14，https://ycharts.com/indicators/cboe_equity_put_call_ratio，source_ids=speculation.equity_put_call）——call 偏重／偏樂觀，但未破 0.50 極端（confirmation，不主計分）。
- **Upcoming AI mega-IPO pipeline**：OpenAI／Anthropic／SpaceX 之 confidential/draft S-1 皆 >30 日窗、作背景不作本週事件（✗ NOT DISCLOSED，source_ids=speculation.upcoming_ai_ipos，不納入計分）。
- **社交情緒代理**：本週無具名主導迷因軋空事件（WSB mention 以 MU／NVDA／AMD 等大型 AI 股為主、無協同軋空）（✗ NOT DISCLOSED，source_ids=retail.social_sentiment，不納入計分）。
**結論**：分數維持 **58**（rubric 41–60「投機升溫」）。1 件 SPAC（General Fusion）為孤立新事件，moonshot 0、insider 一手未確認、put/call 0.62 未極端、IPO 活躍但秩序尚可、社群無主導軋空——投機體感與前次持平。

### 4. 散戶情緒 — 50（weight 12%，Δ -1）
- **CNN Fear & Greed**：≈**46「Fear」**（2026-07-15，經 macromicro.me/charts/50108/cnn-fear-and-greed 鏡像；cnn.com 直抓 WAF 403，source_ids=retail.fear_greed）——較前次 48「Neutral」回落 2 點、重返恐懼區。
- **Margin Debt**：**$1.416T、YoY +53.7%、MoM +8.5%（2026-05-31，記錄高）**（https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra，source_ids=retail.margin_debt）——月頻 stock-of-state，6 月數未發布、沿用 5 月；YoY +53.7% 屬 1999／2007／2021 頂部級別警訊。
- **AAII 散戶調查**：**Bull 36.3%／Bear 37.2%／Neutral 26.5%**（2026-07-09，aaii.com/sentimentsurvey，source_ids=retail.aaii）——多空大致平衡、多方仍低於長均 37.5%。
- **家庭持股佔金融資產比**：**45.76%**（`BOGZ1FL153064486Q`，2026-01-01 資料日，FRED，source_ids=retail.household_equity_allocation）——歷史高位、後續加碼空間有限（Farrell #5，季頻沿用、不計週 Δ）。
- **NAAIM Exposure Index**：**82.95**（2026-07-08，ycharts.com/indicators/naaim_number，source_ids=retail.naaim）——主動經理人仍高曝險＝擁擠多頭（Farrell #9，confirmation cross-check，不主計分）。
**結論**：分數降至 **50**（Δ -1，rubric 41–60 下緣）。F&G 由 Neutral 回落至 Fear、本週無主導迷因軋空＝散戶情緒邊際回落；但 AAII 大致平衡、margin debt 仍頂部級別、NAAIM 高曝險，故僅微降 1 分。

### 5. 貨幣與信貸環境 — 75（weight 20%，Δ 0）
- **Fed funds rate**：目標區間 **3.50–3.75%**（`DFEDTARU` 3.75%／`DFEDTARL` 3.50%，2026-07-15，FRED，source_ids=monetary.fed_funds）——無變動。
- **市場隱含路徑（CME FedWatch，best-effort）**：7/29 會議 ≈**70%** 持平（2026-07-08，en.macromicro.me/series/78109/probability-fed-rate-325-350-2026，source_ids=monetary.fedwatch）——Fed 寬鬆空間受限、年底路徑略偏一碼寬鬆（缺 07-16 當日快照不調分）。
- **Realized inflation vs expectations**：CPI YoY **3.46%**（`CPIAUCSL`，2026-06-01，FRED，source_ids=monetary.cpi_yoy）較 5 月 4.17% 明顯回落、5y5y forward **2.21%**（`T5YIFR`，2026-07-15，週 Δ 0，FRED，source_ids=monetary.t5yifr）持平——通膨降溫略放鬆 Fed 約束，惟仍高於 2% 目標。
- **10Y 期限溢價（term premium）**：`THREEFYTP10` **0.7788%**（2026-07-10，Kim-Wright 三因子模型，序列自身 trailing ≈7d +4.7 bps，FRED，source_ids=monetary.term_premium）——財政風險再定價溫和上行、未急升。
- **repo 資金壓力（SOFR−IORB）與 SRF 動用**：`repo_stress`——SOFR **3.63%**（2026-07-14）、IORB 3.65%、SOFR−IORB **−2 bps**；SOFR99 3.72%、SOFR99−IORB +7 bps；RPONTTLD／SRF 動用 **$0.102bn**（2026-07-15，FRED SOFR/SOFR99/IORB/RPONTTLD，source_ids=monetary.repo_stress_srf）——secured-funding 無壓力、SRF 僅例行小額。
- **美債標售需求（auction，best-effort）**：7/8 10Y bid-to-cover **2.565**（stop-through、需求強）、7/9 30Y 2.44（高殖利率 5.058% 下仍穩）（2026-07-09，https://www.tradingview.com/news/macenews:30b090608094b:0-us-treasury-30-year-bond-auction-high-yield-5-058-bid-cover-ratio-at-2-44/，source_ids=monetary.treasury_auctions）——無 tail、財政供給壓力事件本週不成立（confirmation；缺值不調分）。
- **HY OAS**：**2.72%**（`BAMLH0A0HYM2`，2026-07-14，週 Δ +3 bps，FRED，source_ids=monetary.hy_oas）——接近循環低、極窄、自滿側訊號（連續走闊 streak=1）。
- **IG OAS**：**0.79%**（`BAMLC0A0CM`，2026-07-14，週 Δ +1 bp，FRED，source_ids=monetary.ig_oas）——史窄、信用自滿。
- **10Y nominal 週變動拆解**：ΔDGS10 −4 bps ≈ ΔDFII10 −3 bps ＋ ΔT10YIE −3 bps（三腿視窗不一致、driver=unknown）；`DGS10` **4.58%**（2026-07-14，FRED，source_ids=monetary.dgs10）、`DFII10` **2.33%**（2026-07-14，source_ids=monetary.dfii10）、`T10YIE` **2.23%**（2026-07-15，source_ids=monetary.t10yie）——殖利率小幅回落、估值折現／再融資壓力無新增（詳 §3）。
- **WTI 原油**：**$79.2**/bbl（`DCOILWTICO`，2026-07-13，無新觀測，FRED，source_ids=monetary.wti）——持平，A 通膨鏈油價端無新推力。
- **Fed balance sheet**：≈$6.74T（原始 **6,735,609** 百萬美元，2026-07-08，無新觀測，FRED WALCL，source_ids=monetary.walcl）——量化緊縮步調持平。
- **全球央行流動性（ECB）**：ECB ≈€5.97T（原始 **5,970,516** 百萬歐元，2026-07-10，FRED ECBASSETSW，source_ids=monetary.ecb_boj）——持平。
- **全球央行流動性（BOJ）**：BOJ ≈¥639.55T（原始 **6,395,509** 億日圓，2026-06-01，FRED JPNASSETS，source_ids=monetary.ecb_boj）——持平。
- **PBoC 流動性操作**：人行 2026-07-14 以 6 個月買斷式逆回購淨投放 ≈**1.4** 兆元（≈$207B、該工具紀錄量，平滑稅期與債券發行）（https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance，source_ids=monetary.pboc）——中國端流動性偏寬（confirmation）。
- **私募信貸贖回壓力（扳機側，event-driven）**：Q2 2026 多檔非交易 BDC／私募信貸區間基金實際觸及 5% 季度贖回上限並比例撥付——Blue Owl OCIC 贖回需求 ≈**18.8%** NAV（≈$3.6B）比例撥付（2026-07-02，pitchbook.com/news/articles/private-credit-bdc-redemption-requests-likely-to-peak-in-q2-2026-bofa，source_ids=monetary.private_credit_liquidity），Apollo ADS 與 Blackstone BCRED 亦於 Q2 gated——多基金 redemption 上限實際觸發＝financing-cycle 緊縮已抵達非銀信用，餵入 §3 融資扳機。
**結論**：扳機側；私募信貸多基金 gate proration（Blue Owl OCIC 18.8% 比例撥付、Apollo／BCRED Q2 gated）為扳機側事件，同時 HY 2.72%／IG 0.79% 史窄自滿——「自滿側 froth 與扳機側 financing 壓力同框」推高分數並維持 **75**；macro 多序列持平、標售穩健、repo 無壓、CPI 回落，故分數較前次持平、扳機側質變見「本次新增訊號」。

### 6. 結構性槓桿 — 77（weight 15%，Δ 0）
- **US 槓桿 ETF AUM**：美國槓桿 ETF 總 AUM ≈**$198B**（記錄高，TQQQ／SOXL 領先；NVDL +68% YTD、SOXL +50% YTD）（2026-07-10，cryptobriefing.com/leveraged-etfs-record-198b-aum/，source_ids=structural.leveraged_etf_aum）——水位高。
- **US 單股槓桿 ETF 核准／發行（近 30 日）**：**大量**——Tradr 2x 單股（CIEN／QNT/RMBS/TSEM/TTMI，07-01）、Leverage Shares 6 檔 2x（GOOGL/AMZN/META/AAPL，07-07）、GraniteShares 首檔 SK Hynix 2x long/short（SKUU/SKDD，2026-07-14，globenewswire.com/news-release/2026/07/14/3326857/0/en/GraniteShares-Launches-the-First-U-S-Listed-Leveraged-ETFs-on-SK-hynix.html，source_ids=structural.us_single_stock_etf）——美國單股槓桿產品擴散顯著。
- **全球（非美）槓桿產品核准（本週）**：**本週擴散訊號未觸發**——韓／台／日／歐本週無新單股槓桿／反向 ETF 核准；韓國 FSC 反傾向收緊既有單股槓桿 ETF（2026-07-14，bloomberg.com/opinion/articles/2026-07-14/south-korea-s-leveraged-etfs-have-the-worst-timing，source_ids=structural.global_leveraged_approvals，不納入計分）——未達 2+ 非美市場同週核准、rubric floor 81 未啟動（✗ NOT DISCLOSED）。
- **0DTE 佔 SPX 期權量**：≈**63%**（Cboe，2026-02-28 最新確定值、Q2 維持 >60%，cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/，source_ids=structural.zero_dte）——持續高檔。
- **Options 總量（OCC 月報）**：6 月 **1,603,491,559** 口、+45.0% YoY（2026-07-02，theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report，source_ids=structural.options_volume）——衍生品投機量創高。
- **跨資產／相關性確認**：Cboe SKEW ≈**149.6**（偏高、避險付溢價）、VIX 期限結構 contango（VIX1D 11.61 → VIX3M 19.00）（2026-07-01，home.saxo/content/articles/options/options-brief---calm-on-top-nervous-underneath---1-july-2026-01072026，source_ids=structural.cross_asset_derivatives）——尾端避險升溫、整體波動平靜（confirmation）。
- **Margin debt / 市值 交叉檢核**：$1.416T、YoY +53.7%（2026-05-31，見 D4，advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra，source_ids=structural.margin_debt_crosscheck）——確認零售槓桿頂部級別（confirmation，不在此重複計分）。
- **AI 基礎設施債務／vendor-financing loops**：本月續擴張——CoreWeave 收官 **$8.5B** DDTL（首檔 IG 評級 GPU 抵押融資）、Applied Digital $1.59B 高收益債資助 CoreWeave 產能、Nvidia／CoreWeave 循環融資曝險 ≈$24.9B（2026-07-12，techtimes.com/articles/320239/20260712/nvidia-circular-financing-249b-coreweave-debt-puts-pension-funds-risk.htm，source_ids=structural.ai_infrastructure_debt）——collateral-light 循環網續增。
- **銀行對 NBFI 放款**：≈$2.00T（原始 **1,995.08** 億美元，2026-07-01，無新觀測，FRED LNFACBW027SBOG，source_ids=structural.nbfi_bank_loans）——bank–NBFI linkage 水位持平（confirmation，不主計分）。
- **美債基差交易槓桿（best-effort）**：script `cftc_lev_funds`／`move_index`／`ofr_repo` 本次 `fetch_failed`、改走 WebSearch——MOVE ≈**77.77**（2026-07-14，低於 80–100 常態區、低波，finance.yahoo.com/quote/%5EMOVE/，source_ids=structural.treasury_basis_trade），CFTC 槓桿基金美債期貨仍淨空、無失序平倉——乾柴高位但未點火（見 §3 槓桿鏈 B）。
**結論**：分數維持 **77**（rubric 61–80）。0DTE 續 >60%、OCC 量創高、US 單股槓桿產品擴散強、AI 基礎設施循環債續增（CoreWeave $8.5B）＝結構性槓桿高檔；惟全球擴散訊號未觸發（無 floor-81）、MOVE 低波、無失序平倉——淨評與前次持平。

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

- 1997 早期建設：命中 3/8 = 40%
- 1998 LTCM 衝擊：命中 4/8 = 50%
- 1999 晚期狂熱：命中 3/10 = 30%
- 2000/3 頂點：命中 1/8 = 15%
- 2021/12 Meme 頂：命中 2/8 = 25%

2000/3 高位回落條件：否

**1997 早期建設 feature audit**
- 1997.1｜未命中｜source_ids=—｜估值溢價 79 > 74（超出 40–74 區間）
- 1997.2｜命中｜source_ids=—｜市場廣度 30 < 45
- 1997.3｜未命中｜source_ids=—｜投機行為 58 ≥ 50
- 1997.4｜命中｜source_ids=ai.hyperscaler_capex｜hyperscaler 2026 capex 指引仍上修（≈$700B）
- 1997.5｜命中｜source_ids=—｜散戶情緒 50 < 55
- 1997.6｜未命中｜source_ids=—｜結構性槓桿 77 ≥ 50
- 1997.7｜未命中｜source_ids=—｜HY OAS 2.72% < 4% 成立，但本次週 Δ +3 bps > 0（走闊），all 條件不成立
- 1997.8｜未命中｜source_ids=—｜扳機狀態＝已擊發 ≠ 未擊發
**1998 LTCM 衝擊 feature audit**
- 1998.1｜未命中｜source_ids=structural.cross_asset_derivatives｜HY 週 Δ +3 bps < +30；VIX 期限結構 contango、VIX ≈16 < 25（無壓力事件）
- 1998.2｜未命中｜source_ids=—｜S&P `sp500_trend.chg_pct` +0.76% > −5%（無回檔）
- 1998.3｜命中｜source_ids=monetary.private_credit_liquidity｜具名非銀壓力：Blue Owl OCIC Q2 18.8% gate proration 等私募信貸贖回上限觸發
- 1998.4｜未命中｜source_ids=monetary.fedwatch｜FedWatch 7/29 ≈70% 持平、非轉鴿（無隱含寬鬆或降息）
- 1998.5｜命中｜source_ids=—｜估值溢價 79 ≥ 60
- 1998.6｜命中｜source_ids=—｜扳機狀態＝已擊發 ≥ 初啟
- 1998.7｜未命中｜source_ids=—｜市場廣度 Δ = 30 − 30 = 0 < +8
- 1998.8｜命中｜source_ids=—｜ΔT10YIE −3 bps ≤ 0（通膨預期非主因）
**1999 晚期狂熱 feature audit**
- 1999.1｜命中｜source_ids=—｜估值溢價 79 ≥ 75
- 1999.2｜命中｜source_ids=valuation.sp500_pe_cape｜CAPE 42.18 ≥ 38
- 1999.3｜未命中｜source_ids=—｜投機行為 58 < 60
- 1999.4｜未命中｜source_ids=speculation.microcap_moonshots,speculation.ipo_heat｜本週 moonshot 0；無營收 IPO 佔比未達偏高
- 1999.5｜未命中｜source_ids=—｜市場廣度 30 < 45（廣度健康、非轉窄）
- 1999.6｜未命中｜source_ids=—｜D5 monetary_side＝扳機側 ≠ 自滿側，all 不成立
- 1999.7｜命中｜source_ids=—｜結構性槓桿 77 ≥ 60
- 1999.8｜未命中｜source_ids=—｜散戶情緒 50 < 55
- 1999.9｜無資料｜source_ids=—｜巨型 AI IPO S-1／定價皆 >30 日窗（✗ NOT DISCLOSED）
- 1999.10｜未命中｜source_ids=—｜扳機狀態＝已擊發 ≠ 未擊發
**2000/3 頂點 feature audit**
- 2000.1｜未命中｜source_ids=—｜估值溢價 79 < 85
- 2000.2｜命中｜source_ids=—｜扳機狀態＝已擊發 ≥ 初啟
- 2000.3｜未命中｜source_ids=—｜市場廣度 30 < 60
- 2000.4｜未命中｜source_ids=—｜prior `sp500_dev200_pct`＝null（legacy）使第一分支為否；current chg +0.76% > −5%
- 2000.5｜未命中｜source_ids=—｜投機行為 58 < 70
- 2000.6｜未命中｜source_ids=speculation.insider_form4｜14 日內 0 件合格 Form 4 cluster
- 2000.7｜未命中｜source_ids=—｜散戶情緒 50 < 65
- 2000.8｜未命中｜source_ids=monetary.fedwatch｜FedWatch ≈70% 持平、非轉緊；10Y 週 −4 bps 且 driver≠breakeven
**2021/12 Meme 頂 feature audit**
- 2021.1｜未命中｜source_ids=—｜散戶情緒 50 < 65
- 2021.2｜無資料｜source_ids=—｜本週無具名主導社群軋空（✗ NOT DISCLOSED）
- 2021.3｜命中｜source_ids=—｜結構性槓桿 77 ≥ 65
- 2021.4｜未命中｜source_ids=—｜D5 monetary_side＝扳機側 ≠ 自滿側，all 不成立
- 2021.5｜命中｜source_ids=retail.margin_debt｜margin debt YoY +53.7% ≥ +40%
- 2021.6｜未命中｜source_ids=speculation.microcap_moonshots｜本週 microcap moonshot 0 < 1
- 2021.7｜未命中｜source_ids=—｜市場廣度 30 < 50
- 2021.8｜未命中｜source_ids=—｜CPI YoY 3.46% < 4%，all 不成立

**兩句解讀**：本週最貼近「1998 LTCM 衝擊」（50%）——估值偏高（79）、扳機狀態已擊發（私募信貸多基金 gate proration）、ΔT10YIE ≤0（通膨預期非主因），構成「估值高企下的非銀融資扳機、公開利差尚未反映」的 LTCM 型格局，而非純粹的晚期狂熱（1999／2021 因廣度健康、社群無主導軋空、CPI 回落至 3.46% 而降溫）。這意味當前處「froth 與 financing 壓力同框、失序仍局部（結構化產品閘門）」的中段位置——真實技術突破吸引超商業回報所能支撐的資本（BIS AER 2026 Ch I：AI 相關投資 ≈1% of US GDP、IT 投資合計 ≈5% 已超 dot-com 峰），最須盯 AI 信用重定價（Oracle CDS 走闊）與私募信貸閘門是否外溢至公開利差。長期指數成長趨勢偏離（Dot-com ≈95%、1929 ≈110%、當前 AI 週期 ≈147%；RIA/Farrell）作跨期敘事錨、不進 checklist。

## 機構情緒對照

本次無新機構調查數據。

## 本次新增訊號

比較基準：vs 前次（3天前）。

- **散戶情緒 -1（51 → 50）**：CNN F&G 由 48「Neutral」回落至 46「Fear」（2026-07-15）、本週無主導迷因軋空——散戶情緒邊際回落；AAII 大致平衡（Bull 36.3%／Bear 37.2%）、margin debt 沿用 5 月（+53.7% YoY），故僅 −1。
- **貨幣與信貸環境（D5）＝扳機側，score Δ 0——質化新訊號（雙向 Δ 遮蔽防護）**：私募信貸多基金 gate proration 延續（Blue Owl OCIC 18.8% 比例撥付、Apollo ADS／Blackstone BCRED Q2 gated），扳機狀態維持「已擊發」；分數未動因先前已因扳機側偏高（前次即 75）。此為前次已存在之扳機側狀態延續。
- **格局轉變（質化）**：三角格局由前次「穩定共存」轉為本次「分歧」——S&P ▲ +0.76% 而 10Y ▼ −4 bps、WTI 持平，10Y 在反向重新定價（殖利率小幅回落，CPI 由 4.17% 回落至 3.46% 為背景）。
- **結構性槓桿質化訊號（score Δ 0）**：US 單股槓桿 ETF 續擴散（GraniteShares SK Hynix SKUU/SKDD、Tradr、Leverage Shares）、AI 基礎設施新債（CoreWeave $8.5B DDTL、Applied Digital $1.59B）——惟**全球（非美）擴散訊號未觸發（本週擴散訊號未觸發，未達 2+ 非美市場同週核准）**，MOVE 低波、無失序平倉，故分數未動。
- 其餘維度（估值 79、廣度 30、投機 58、貨幣 75、結構 77）分數與前次持平。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | S&P 500 收盤（sp500_trend latest） | 7,572.4 | FRED SP500（sp500_trend） | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.sp500_trend | S&P 500 距 200DMA 偏離（sp500_trend dev200_pct） | +8.51% | FRED SP500（sp500_trend） | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| retail.household_equity_allocation | 家庭持股佔金融資產比 | 45.76 | FRED BOGZ1FL153064486Q | 2026-01-01 | 2026-07-16T09:30:00+08:00 |
| monetary.fed_funds | Fed funds 上限（DFEDTARU） | 3.75% | FRED DFEDTARU | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| monetary.fed_funds | Fed funds 下限（DFEDTARL） | 3.50% | FRED DFEDTARL | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| monetary.hy_oas | HY OAS（BAMLH0A0HYM2） | 2.72% | FRED BAMLH0A0HYM2 | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.ig_oas | IG OAS（BAMLC0A0CM） | 0.79% | FRED BAMLC0A0CM | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.dgs10 | 10Y 名目殖利率（DGS10） | 4.58% | FRED DGS10 | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.dfii10 | 10Y 實質殖利率（DFII10） | 2.33% | FRED DFII10 | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.t10yie | 10Y breakeven（T10YIE） | 2.23% | FRED T10YIE | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| monetary.wti | WTI 原油（DCOILWTICO） | $79.2 | FRED DCOILWTICO | 2026-07-13 | 2026-07-16T09:30:00+08:00 |
| monetary.cpi_yoy | CPI YoY（CPIAUCSL yoy_pct） | 3.46% | FRED CPIAUCSL | 2026-06-01 | 2026-07-16T09:30:00+08:00 |
| monetary.t5yifr | 5y5y forward（T5YIFR） | 2.21% | FRED T5YIFR | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| monetary.term_premium | 10Y 期限溢價（THREEFYTP10） | 0.7788% | FRED THREEFYTP10 | 2026-07-10 | 2026-07-16T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR 隔夜利率 | 3.63% | FRED SOFR | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.repo_stress_srf | SOFR 99th 分位（SOFR99） | 3.72% | FRED SOFR99 | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.repo_stress_srf | IORB | 3.65% | FRED IORB | 2026-07-16 | 2026-07-16T09:30:00+08:00 |
| monetary.repo_stress_srf | SRF/隔夜 repo 操作量（RPONTTLD） | 0.102 | FRED RPONTTLD | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| monetary.walcl | Fed 資產負債表（WALCL） | 6,735,609 百萬美元（≈$6.74T） | FRED WALCL | 2026-07-08 | 2026-07-16T09:30:00+08:00 |
| monetary.ecb_boj | ECB 資產（ECBASSETSW） | 5,970,516 百萬歐元（≈€5.97T） | FRED ECBASSETSW | 2026-07-10 | 2026-07-16T09:30:00+08:00 |
| monetary.ecb_boj | BOJ 資產（JPNASSETS） | 6,395,509 億日圓（≈¥639.55T） | FRED JPNASSETS | 2026-06-01 | 2026-07-16T09:30:00+08:00 |
| structural.nbfi_bank_loans | 銀行對 NBFI 放款（LNFACBW027SBOG） | 1,995.08 億美元（≈$2.00T） | FRED LNFACBW027SBOG | 2026-07-01 | 2026-07-16T09:30:00+08:00 |

### Coverage

| source_id | 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（P/E 32.59、CAPE 42.18 @07-15） |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E | MarketXLS [SEARCH] | ✓ SEARCH-VERIFIED（trailing ≈40 @05-15） |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 [primary: SEARCH]（best-effort） | ✗ NOT DISCLOSED（本季無新 EPS-vs-multiple 分解披露） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500 派生） | ✓ API（dev200 +8.51%／dev52w +10.25%） |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧 | 信用市場 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Oracle CDS ≈198bp vs CDX IG ≈95bp @07-10） |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst [SEARCH] | ✓ SEARCH-VERIFIED（RSP +9.67% vs SPY +8.38%） |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | S&P DJI factor dashboard [SEARCH] | ✓ SEARCH-VERIFIED（35.59% @2026-04） |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | McClellan/StockCharts [SEARCH] | ✓ SEARCH-VERIFIED（NYSE A/D 2008/2749 @07-13、A/D 線建設性） |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH]（403，經 MacroMicro） | ✓ SEARCH-VERIFIED（46 Fear @07-15） |
| retail.margin_debt | 散戶｜Margin Debt: FINRA | FINRA/Advisor Perspectives [SEARCH]（月頻 stock-of-state） | ✓ SEARCH-VERIFIED（$1.416T、+53.7% YoY、2026-05 沿用） |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（Bull 36.3%/Bear 37.2% @07-09） |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB/cashtag [SEARCH]（best-effort） | ✗ NOT DISCLOSED（本週無主導軋空事件） |
| retail.household_equity_allocation | 散戶｜Household equity allocation | fetch_macro.py BOGZ1FL153064486Q | ✓ API（45.76% @2026-Q1） |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim/ycharts [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（82.95 @07-08） |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM | 賣方調查 [SEARCH]（月頻，best-effort） | ✗ NOT DISCLOSED（自前次無新一期） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED DFEDTARU/DFEDTARL | fetch_macro.py FRED API | ✓ API（3.75%/3.50% @07-15） |
| monetary.hy_oas | 貨幣｜High Yield OAS | fetch_macro.py FRED API | ✓ API（2.72% @07-14，Δ+3bps） |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | fetch_macro.py FRED API | ✓ API（0.79% @07-14，Δ+1bp） |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | fetch_macro.py FRED API | ✓ API（4.58% @07-14，Δ−4bps） |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield | fetch_macro.py FRED API | ✓ API（2.33% @07-14，Δ−3bps） |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | fetch_macro.py FRED API | ✓ API（2.23% @07-15，Δ−3bps） |
| monetary.wti | 貨幣｜WTI crude oil price | fetch_macro.py FRED API | ✓ API（$79.2 @07-13，no_new_obs） |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED | fetch_macro.py FRED API（月頻） | ✓ API（3.46% @2026-06） |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | fetch_macro.py FRED API | ✓ API（2.21% @07-15，Δ0） |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED | fetch_macro.py FRED API | ✓ API（0.7788% @07-10，+4.7bps） |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py repo_stress | ✓ API（SOFR−IORB −2bps、SOFR99−IORB +7bps、SRF $0.102bn @07-14/15） |
| monetary.treasury_auctions | 貨幣｜美債標售需求 | Reuters/TradingView [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（10Y BTC 2.565 @07-08；30Y 2.44 @07-09） |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME/MacroMicro [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（7/29 ≈70% 持平 @07-08） |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED WALCL | fetch_macro.py FRED API | ✓ API（$6.74T @07-08，no_new_obs） |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | fetch_macro.py FRED API | ✓ API（€5.97T @07-10／¥639.55T @06-01） |
| monetary.pboc | 貨幣｜PBoC aggregate financing | Bloomberg [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（6M 逆回購 ¥1.4T @07-14） |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Blue Owl OCIC 18.8% gate proration @07-02） |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報 [SEARCH]（stock-of-state） | ✓ SEARCH-VERIFIED（2026 ≈$700B、仍上修） |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic/OpenAI/Google [SEARCH]（best-effort） | ✗ NOT DISCLOSED（本季無量化披露） |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch/The Information [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Anthropic ≈$47B／OpenAI ≈$25B run-rate） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration | 財報電話 [primary: SEARCH]（best-effort） | ✗ NOT DISCLOSED（本次無新一手 RPO 披露） |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（DRAM +58–63% QoQ @06-02；供給仍被吸收） |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構 | 季報 [primary: SEARCH]（best-effort） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口 | 組合披露 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（年化 capex ≈$700B vs 終端營收低百億級） |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K/10-Q [primary: SEARCH]（best-effort，30日） | ✗ NOT DISCLOSED（過去 30 日無新變更） |
| ai.capital_cycle | AI｜資本週期階段 | 供需增速+進出場事件 [SEARCH]（best-effort） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days +AI rename/SPAC | [SEARCH] | ✓ SEARCH-VERIFIED（General Fusion SPAC @07-10） |
| speculation.ipo_heat | 投機｜IPO market heat | stockanalysis/Axios [SEARCH] | ✓ SEARCH-VERIFIED（YTD ≈200 檔、$141.2B @07-13） |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz/Benzinga [primary: SEARCH]（required 週螢幕） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | S-1/具名報導 [SEARCH]（best-effort） | ✗ NOT DISCLOSED（S-1 皆 >30 日窗） |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership | SEC EDGAR [primary: EDGAR]（required） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe/ycharts [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（0.62 @07-14） |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | etf.com/cryptobriefing [primary: SEARCH] | ✓ SEARCH-VERIFIED（總 ≈$198B @07-10） |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | SEC/ETF.com [SEARCH] | ✓ SEARCH-VERIFIED（Tradr/Leverage Shares/GraniteShares SK Hynix @07-01–07-14） |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX/TWSE/JPX/ESMA [SEARCH]（best-effort，7日） | ✗ NOT DISCLOSED（本週擴散訊號未觸發） |
| structural.zero_dte | 結構｜0DTE option volume | Cboe [SEARCH]（Cboe 403） | ✓ SEARCH-VERIFIED（≈63%，Cboe @2026-02） |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com [SEARCH] | ✓ SEARCH-VERIFIED（6 月 16.03 億口、+45% YoY @07-02） |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe/Saxo [SEARCH] | ✓ SEARCH-VERIFIED（SKEW ≈149.6、VIX contango @07-01） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 D4（confirmation） | ✓ SEARCH-VERIFIED（$1.416T/+53.7% YoY，D4 引用不重複計分） |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]（best-effort，30日） | ✓ SEARCH-VERIFIED（CoreWeave $8.5B DDTL、Nvidia 循環 $24.9B @07-12） |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | fetch_macro.py FRED API | ✓ API（$2.00T @07-01，no_new_obs） |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | script→WebSearch [primary: script]（best-effort） | ✓ SEARCH-VERIFIED components=cftc_lev_funds:fetch_failed,move_index:fetch_failed,ofr_repo:fetch_failed；MOVE 77.77 @07-14 |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 32.59 | S&P 500 trailing P/E July 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.18 | Shiller CAPE ratio July 2026 multpl | https://www.multpl.com/shiller-pe | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E ≈40 trailing | Magnificent 7 weighted PE 2026 | https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026 | 2026-05-15 | 2026-07-16T09:30:00+08:00 |
| valuation.ai_credit_schism | Oracle 5yr CDS ≈198bp vs CDX.NA.IG ≈95bp | Oracle CoreWeave CDS spread vs CDX IG July 2026 | https://www.investing.com/analysis/oracle-and-coreweave-credit-default-swap-spreads-widening-omen-or-jitters-200670506 | 2026-07-10 | 2026-07-16T09:30:00+08:00 |
| breadth.rsp_spy | RSP +9.67% vs SPY +8.38% YTD | RSP vs SPY equal weight YTD 2026 divergence | https://247wallst.com/investing/2026/06/26/forget-the-magnificent-seven-this-equal-weight-sp-fund-beats-the-mega-caps-for-just-0-20/ | 2026-06-26 | 2026-07-16T09:30:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 35.59% | S&P 500 top 10 concentration percent 2026 | https://www.spglobal.com/spdji/en/documents/performance-reports/dashboard-sp-500-factor.pdf | 2026-04-30 | 2026-07-16T09:30:00+08:00 |
| breadth.advance_decline | NYSE 上漲 2008／下跌 2749、A/D 線建設性 | NYSE advance decline breadth July 2026 | https://www.mcoscillator.com/market_breadth_data/ | 2026-07-13 | 2026-07-16T09:30:00+08:00 |
| retail.fear_greed | CNN Fear & Greed 46（Fear） | CNN Fear and Greed Index today July 2026 | https://en.macromicro.me/charts/50108/cnn-fear-and-greed | 2026-07-15 | 2026-07-16T09:30:00+08:00 |
| retail.margin_debt | FINRA margin debt $1.416T、+53.7% YoY | FINRA margin debt May 2026 YoY | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra | 2026-05-31 | 2026-07-16T09:30:00+08:00 |
| retail.aaii | AAII Bull 36.3%/Bear 37.2% | AAII investor sentiment survey July 2026 | https://www.aaii.com/sentimentsurvey | 2026-07-09 | 2026-07-16T09:30:00+08:00 |
| retail.naaim | NAAIM Exposure Index 82.95 | NAAIM exposure index latest July 2026 | https://ycharts.com/indicators/naaim_number | 2026-07-08 | 2026-07-16T09:30:00+08:00 |
| monetary.treasury_auctions | 10Y BTC 2.565、30Y BTC 2.44 | US Treasury 10Y 30Y auction July 2026 bid to cover | https://www.tradingview.com/news/macenews:30b090608094b:0-us-treasury-30-year-bond-auction-high-yield-5-058-bid-cover-ratio-at-2-44/ | 2026-07-09 | 2026-07-16T09:30:00+08:00 |
| monetary.fedwatch | CME FedWatch 7/29 ≈70% 持平 | CME FedWatch rate hold probability July 2026 | https://en.macromicro.me/series/78109/probability-fed-rate-325-350-2026 | 2026-07-08 | 2026-07-16T09:30:00+08:00 |
| monetary.pboc | 人行 6M 買斷式逆回購投放 1.4 兆元 | PBoC reverse repo liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-14/pboc-boosts-liquidity-to-smooth-tax-payments-debt-issuance | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| monetary.private_credit_liquidity | [private_credit_gate] Blue Owl OCIC Q2 贖回 18.8% 觸及 5% 上限比例撥付 | private credit BDC redemption gate proration Q2 2026 Blue Owl | https://pitchbook.com/news/articles/private-credit-bdc-redemption-requests-likely-to-peak-in-q2-2026-bofa | 2026-07-02 | 2026-07-16T09:30:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex ≈$700B、仍上修 | hyperscaler capex 2026 guidance raised | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html | 2026-05-15 | 2026-07-16T09:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic ≈$47B／OpenAI ≈$25B run-rate | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-05-15 | 2026-07-16T09:30:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 2Q26 合約 +58–63% QoQ | DRAM HBM contract price 2Q26 TrendForce | https://www.trendforce.com/presscenter/news/20260602-13074.html | 2026-06-02 | 2026-07-16T09:30:00+08:00 |
| ai.revenue_capex_gap | 年化 capex ≈$700B vs AI 終端營收低百億級 | AI revenue to capex gap 2026 | https://finance.yahoo.com/sectors/technology/articles/hyperscalers-hit-700-billion-2026-111243744.html | 2026-05-15 | 2026-07-16T09:30:00+08:00 |
| speculation.ai_rename_spac | General Fusion（GFUZ）SPAC 上市 07-10 | AI rename SPAC July 2026 General Fusion | https://www.morningstar.com/news/pr-newswire/20260710ln02448/ | 2026-07-10 | 2026-07-16T09:30:00+08:00 |
| speculation.ipo_heat | 2026 YTD ≈200 檔 IPO、$141.2B | US IPO market 2026 YTD count proceeds | https://www.axios.com/2026/07/13/us-ipo-market-record-proceeds | 2026-07-13 | 2026-07-16T09:30:00+08:00 |
| speculation.microcap_moonshots | 本週合格 microcap moonshot 件數 0 | microcap 100% single day quantum AI moonshot July 2026 | Finviz/Benzinga/StockTitan movers screener | 2026-07-16 | 2026-07-16T09:30:00+08:00 |
| speculation.insider_form4 | 14 日內合格 Form 4 cluster 件數 0（EDGAR egress 受限） | insider Form 4 cluster AI leaders July 2026 openinsider | SEC EDGAR / openinsider（一手 URL 無法取得） | 2026-07-16 | 2026-07-16T09:30:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.62 | Cboe equity put call ratio July 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM ≈$198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-07-10 | 2026-07-16T09:30:00+08:00 |
| structural.us_single_stock_etf | GraniteShares SK Hynix SKUU/SKDD 2x | single-stock leveraged ETF launch July 2026 SK Hynix Tradr | https://www.globenewswire.com/news-release/2026/07/14/3326857/0/en/GraniteShares-Launches-the-First-U-S-Listed-Leveraged-ETFs-on-SK-hynix.html | 2026-07-14 | 2026-07-16T09:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX ≈63% | 0DTE SPX options share volume 2026 Cboe | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/ | 2026-02-28 | 2026-07-16T09:30:00+08:00 |
| structural.options_volume | OCC 6 月 1,603,491,559 口、+45% YoY | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report | 2026-07-02 | 2026-07-16T09:30:00+08:00 |
| structural.cross_asset_derivatives | [snapshot] VIX 期限結構 contango、Cboe SKEW 149.6 | VIX term structure SKEW July 2026 | https://www.home.saxo/content/articles/options/options-brief---calm-on-top-nervous-underneath---1-july-2026-01072026 | 2026-07-01 | 2026-07-16T09:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt $1.416T、+53.7% YoY（cross-ref D4） | FINRA margin debt equity market cap 2026 | https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra | 2026-05-31 | 2026-07-16T09:30:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $8.5B DDTL、Nvidia 循環 $24.9B | AI data center debt CoreWeave Nvidia circular financing July 2026 | https://www.techtimes.com/articles/320239/20260712/nvidia-circular-financing-249b-coreweave-debt-puts-pension-funds-risk.htm | 2026-07-12 | 2026-07-16T09:30:00+08:00 |
| structural.treasury_basis_trade | [move_index] MOVE 77.77（move_index block fetch_failed，WebSearch 補） | MOVE index level July 2026 Treasury basis trade | https://finance.yahoo.com/quote/%5EMOVE/ | 2026-07-14 | 2026-07-16T09:30:00+08:00 |

**Macro script 說明**：`python3 scripts/fetch_macro.py 2026-07-13` 於 2026-07-16 執行，FRED 全 20 序列 `status: ok`（部分序列前次基準日＝最新觀測日而 `no_new_obs: true`，Δ=0 為成功結果）；`sp500_trend`／`repo_stress`／`decomposition` ok（decomposition driver=unknown、三腿視窗不一致）；`cftc_lev_funds`／`move_index`／`ofr_repo` `fetch_failed`（改走 best-effort WebSearch）。金鑰未輸出。

## 本次分數存檔
```json
{
  "date": "2026-07-16",
  "iso_week": "2026-W29",
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
  "regime": "分歧",
  "trigger_state": "已擊發",
  "trigger_reasons": [
    "private_credit_gate"
  ],
  "monetary_side": "扳機側",
  "hy_oas_widening_streak": 1,
  "sp500_dev200_pct": 8.51
}
```

本報告為相對風險溫度計，非擇時訊號。

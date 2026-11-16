# 2026-08-13 市場泡沫風險評估報告
> 報告日期：2026-08-13；執行日：2026-08-13 Asia/Taipei；ISO 週次：2026-W33；前次基準：report-2026-08-10（3天前）

**總評**：總分 64【警戒】（Δ −1）；扳機狀態：未擊發；最貼近錨點：1999 晚期狂熱（60%）。

## §1 六維度風險條圖
| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▱▱▱ | 78 | 78 | 0 |
| 市場廣度 | ▰▰▰▱▱▱▱▱▱▱ | 30 | 30 | 0 |
| 投機行為 | ▰▰▰▰▰▱▱▱▱▱ | 55 | 57 | −2 |
| 散戶情緒 | ▰▰▰▰▰▱▱▱▱▱ | 53 | 54 | −1 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▰▱▱▱ | 76 | 76 | 0 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 78 | 78 | 0 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **64【警戒】** | 65 | −1 |

## §2 歷史錨點相似度
| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1973/1 Nifty Fifty 頂 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 1997 早期建設 | 50% | ▰▰▰▰▰▱▱▱▱▱ |  |
| 1998 LTCM 衝擊 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 60% | ▰▰▰▰▰▰▱▱▱▱ | ◀ 最貼近 |
| 2000/3 頂點 | 15% | ▰▱▱▱▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |

## §3 三角訊號
| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,748.5 | 持平 −0.06%（前次 ≈7,753.11） |
| WTI 原油 | $84.77 /bbl | ▲ +1.21%（前次 ≈$83.76） |
| 10Y Treasury | 4.70% | ▼ −2 bps（前次 ≈4.72%） |

**三者狀態**：出現分歧（10Y 殖利率與通膨預期反向下行、油價獨漲）——三者本次方向為股市 持平（−0.06%）、WTI ▲（+1.21%）、10Y ▼（−2 bps），出現 ▲/▼ 混合（油價上行但殖利率／breakeven 反向下行），依格局判定規則屬「分歧」。公開信用利差維持極度自滿（HY 2.72%／IG 0.79% 史窄）與 AI 雲端信用單一發行人重定價須分開判讀。
- 股市：≈7,748.5（S&P 500，2026-08-12）；較前次 持平 −0.06%（前次 ≈7,753.11）；距 200 日均線 +9.67%、距 52 週均線 +11.23%——價格自前次（+10.04%）小幅回落、微跌破 +10% 拉伸門檻。
- WTI 原油：≈$84.77/bbl（DCOILWTICO，2026-08-11）；較前次 ▲ +1.21%（前次 ≈$83.76）。
- 10Y 殖利率：4.70%（DGS10，2026-08-11）；較前次 ▼ −2 bps（前次 ≈4.72%）；主要驅動：三腿視窗不一致（driver=unknown，ΔT10YIE 取自較新視窗）。
**格局轉變**：前次格局＝穩定共存（讀自 report-2026-08-10 的 `regime`）→ 本次格局＝分歧；三者由前次的股市單邊小幅延伸、WTI／10Y 無新觀測（穩定共存），轉為本次油價獨漲而 10Y 殖利率與通膨預期反向下行（▲/▼ 混合），格局轉為分歧。
**10Y 成因拆解**：拆的是週變動（bps）、非水位（`ΔDGS10 ≈ ΔDFII10 + ΔT10YIE`）；三腿均有新觀測（freshness=updated）但視窗不一致——`decomposition.driver=unknown`（ΔT10YIE 取自 2026-08-12 較新視窗、DGS10／DFII10 對齊 08-11，恆等式不跨視窗成立），判定 不可判（視窗不一致）；三腿實際 signed 週變動如下：
- ΔDGS10 名目殖利率週變動：−2 bps
- ΔDFII10 實質殖利率週變動：0 bps
- ΔT10YIE 損益平衡通膨週變動：−3 bps
- 判定：不可判（視窗不一致）
**扳機鏈**：A 通膨鏈（油 → 通膨預期 → Fed 受限 → refinancing 成本）本週訊號分歧——油價 ▲（≈$84.77、+1.21%）但通膨預期反向回落：[monetary.cpi_yoy] CPIAUCSL yoy_pct=3.3 data_date=2026-07-01（7 月 CPI YoY 3.3%）、5y5y forward [monetary.t5yifr] T5YIFR latest=2.28 delta_bps=-5 data_date=2026-08-12（週 Δ −5 bps）；FOMC 維持 3.50–3.75%、CME FedWatch 9 月 ≈45% 定價升息（無降息定價、偏鷹）——油價獨漲未帶動通膨預期，Fed put 可得性未惡化，本鏈未加速。無當期電價／能源瓶頸新報導。B 槓桿鏈（衝擊：財政風險再定價 → NBFI 去槓桿 → margin spiral → 國債市場失序 → 官方市場功能回應；BIS AER 2026 Ch II 傳導鏈，2025-04 swap-spread unwind 為原型）乾柴堆積但衝擊節點壓力本週反而緩解——衝擊節點：10Y 期限溢價 THREEFYTP10 ≈0.8257%（Kim-Wright 三因子模型、序列自身 trailing ≈7d −4.2 bps、回落，遠未達 +15 bps 初啟門檻），且本週美債標售需求轉強（3Y 08-11 bid-to-cover 2.71、tail −0.5bp「stopped through」；10Y 08-12 bid-to-cover 2.58、需求略高於均值；30Y 08-13 在執行時點後、未出結果）＝財政供給壓力事件證據本週轉弱；NBFI 節點：script `cftc_lev_funds`／`move_index`／`ofr_repo` 本次 fetch_failed，WebSearch 顯示 MOVE ≈74.67 絕對水位仍低、無 7 日窗內基差交易新平倉具名事件（Fed 估基差交易結構部位 ≈$830B 仍處紀錄高但未釋放）；官方回應節點：`repo_stress` SOFR−IORB −1 bps、SOFR99−IORB +8 bps、SRF 動用 ≈$0（無失序）。real-rate 主導的異常 10Y 上行本週不存在（ΔDGS10 −2 bps、殖利率下行）。AI 雲端信用本週轉為走闊——CoreWeave $2.6B 貸款被迫調高利差 +100–125bp、Oracle 5Y CDS ≈75bp（7 年高）、Fitch／Moody's 對 AI 基建發出信用預警；屬單一發行人／結構化層級的後期訊號，尚未外溢至國債市場層級；本鏈證據 best-effort。
**扳機理由**：none
**結論**：扳機狀態：未擊發——本週無任一 contract 扳機理由成立：HY OAS 週 Δ +2 bps（未達 +50 已擊發門檻、streak 由 0 增至 1、未達 2 初啟門檻）、10Y driver≠breakeven（且殖利率下行）、期限溢價週 −4.2 bps（回落、未達 +15 bps）、私募信貸端 30 日窗內無新 gate proration／breach、無多基金 net inflow→outflow flip。三者配置歷史意義：估值＋槓桿＝崩跌位能，融資緊縮＝時點扳機；本週公開信用利差維持極度自滿（HY 2.72%／IG 0.79% 史窄）、美債標售需求轉強、非銀融資扳機未擊發，屬「froth 自滿而扳機未擊發」的組態，惟 AI 雲端信用轉為走闊（CoreWeave +100–125bp、Oracle CDS 7 年高）為後期側背景壓力，最須盯其是否外溢至公開利差與國債市場層級。

## 六維度評分

### 1. 估值溢價 — 78（weight 22%，Δ 0）
- **S&P 500 trailing P/E** ≈**29.85**（2026-08-12，https://www.multpl.com/s-p-500-pe-ratio，source_ids=valuation.sp500_pe_cape）——遠高於長期中位（≈16–19），實現盈餘基礎上歷史性偏貴、較前次（29.7）微升。
- **Shiller CAPE** ≈**42.34**（2026-08-12，https://www.multpl.com/shiller-pe，source_ids=valuation.sp500_pe_cape）——2000 以來次高、遠高於長均 ≈17，較前次 42.19 微升。
- **Excess CAPE Yield（ECY）** ≈**−0.07%**（`1/42.34 − 2.43/100`，derived 自 CAPE 42.34（2026-08-12）與 DFII10 2.43%（2026-08-11），source_ids=valuation.sp500_pe_cape）——維持負值，1929／2000 級別股相對債極貴訊號（confirmation，不主計分）。
- **Mag 7 加權 P/E**：Mag 7 ≈**29x** vs 指數 ≈25.6x（Mag 7 佔 S&P 500 市值 ≈33.9%）（2026-08-12，https://www.fool.com/research/magnificent-seven-sp-500/，source_ids=valuation.mag7_multiples）——絕對水位仍高但相對溢價維持近十年低，緩和面。
- **價格趨勢偏離（Farrell #1/#2/#4）** S&P 距 200 日均線 **+9.67%**、距 52 週均線 +11.23%（`sp500_trend`，2026-08-12，FRED SP500，source_ids=valuation.sp500_trend）——價格自前次 +10.04% 小幅回落、微跌破 +10% 拉伸門檻，均值回歸下行位能仍高，與 P/E／CAPE 互補、不重複計分。
- **AI capex 現實檢核**：hyperscaler 2026 capex 維持上修——MSFT ≈$190B、AWS ≈$200B、Alphabet $175–205B、Meta $125–145B，四家合計 ≈**$725B**（Alphabet Q2 上修頂端至 $205B 且 FCF 轉負；stock-of-state 沿用，本週無新財報）（2026-07-28，https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html，source_ids=ai.hyperscaler_capex）——基本面敘事仍撐估值，惟回本未現。
- **AI compute 供需現實檢核**：HBM/DRAM 合約續漲（≈**+40%**）、H200 租金中位 ≈$3.99/hr、Blackwell B200/GB200 售罄至 2026 年中（2026-08-01，https://jarvislabs.ai/blog/h200-price，source_ids=ai.compute_supply_demand）——供給仍緊、被需求吸收（非過剩），未取得利用率轉弱證據，此渠道未推升估值風險。
- **AI 營收對 capex 缺口現實檢核**：AI 終端年化營收（Anthropic ≈$47B＋OpenAI ≈$25B）≈**$72B** vs 年化 capex ≈$725B（分母：top-4＋Oracle）（2026-06-15，https://epoch.ai/data-insights/anthropic-openai-revenue，source_ids=ai.revenue_capex_gap）——量級缺口逾 10× 且 capex 續升，回本假設後移，估值風險上修質化依據（缺口未收斂，stock-of-state 沿用）。
- **Hyperscaler 融資結構（capex vs FCF / 發債）**：quarterly_state——top-5 capex 已超越 FCF（Alphabet Q2 FCF 轉負）、續靠外部融資、2026 發債 ≈$182B；event_scan——Meta El Paso 資料中心於 2026-07-20 由 BlackRock 主導行銷 >**$12B** 債券（20–30yr triple-net lease、表外結構）（2026-07-20，https://www.landgate.com/news/blackrock-s-12-billion-bond-sale-signals-a-new-financing-playbook-for-data-center-developers，source_ids=ai.hyperscaler_financing_mix）——capex 愈靠發債與表外 SPV 支撐、同份 guidance 脆弱性上升（BIS Bulletin 120，confirmation，不主計分）。
- **AI 信用定價分歧（equity-vs-credit schism）**：AI 雲端／基建信用本週轉為走闊——CoreWeave $2.6B 貸款被迫調高利差 **+100–125bp**、Oracle 5Y CDS ≈75bp（7 年高），Fitch／Moody's 發 AI 基建信用預警（2026-08-03，https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm，source_ids=valuation.ai_credit_schism）——信貸端開始重定價（走闊）而股價未跟＝後期訊號，分歧朝「信貸先醒」方向演進（confirmation，不主計分；缺值不調分）。
- **backlog 重複計算風險（RPO double-counting）**：Microsoft 商用 RPO ≈**$678B**（≈32% 繫 OpenAI）、Oracle RPO ≈$638B（≈$300B 繫 OpenAI／Stargate）——同一 OpenAI 承諾被多家供應商同時入帳（2026-07-30，https://www.benzinga.com/trading-ideas/long-ideas/26/07/60816147/microsofts-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer，source_ids=ai.customer_concentration_rpo）——營收品質訊號：可支付的終端現金流只有一份（confirmation，不主計分；缺值不調分）。
- **TP-upgrade phase signal**：本季（Q3 2026）具名賣方升評屬 **EPS-driven**——Susquehanna 將 TSMC 目標自 $575 上修至 $**600**（Q2 淨利 +77%、FY 指引二度上修驅動），目標 PE 未擴張（2026-07-16，https://www.tipranks.com/news/tsmc-stock-price-forecast-top-analysts-raise-targets-ahead-of-q2-earnings，source_ids=valuation.analyst_tp_decomposition）——升評由 E 而非 multiple 主導、同季未見多檔 multiple-driven 重定價，相對緩和（confirmation，不主計分）。
- **折舊年限變動（盈餘品質）**：過去 30 日無新 10-K／10-Q 折舊年限或殘值假設變更披露（✗ NOT DISCLOSED，source_ids=ai.depreciation_life，不納入計分）。
- **資本週期階段**：event_scan 無窗內具日期之新事件、quarterly_state 供需增速證據不足，本次不判定週期階段（✗ NOT DISCLOSED，source_ids=ai.capital_cycle，不納入計分）。
**結論**：分數維持 **78**（rubric 高位）。CAPE ≈42.34（2000 以來次高）、P/E ≈29.85、趨勢偏離自 +10.04% 小幅回落至 +9.67%（微跌破拉伸門檻）、ECY 維持負值、RPO 集中度風險續在為升溫面；AI 雲端信用本週轉為走闊（後期訊號）亦屬升溫，惟 Mag 7 相對溢價維持近十年低、趨勢偏離略降為緩和——升緩相抵，淨評與前次持平。

### 2. 市場廣度 — 30（weight 13%，Δ 0）
- **RSP（等權）vs SPY（市值權）YTD**：RSP 等權 YTD 總報酬 ≈+**9.67%** 領先 SPY ≈+8.38%、等權維持小幅領先（Mag 7 集中度成為拖累）（2026-06-10，https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/，source_ids=breadth.rsp_spy）——等權領先＝廣度參與尚健康（snapshot 沿用最近明確 YTD 比較）。
- **Top-10 集中度**：≈**37%**（歷史高位區間）（2026-07-24，https://www.rbcwealthmanagement.com/en-us/insights/the-great-narrowing-sp-500-concentration，source_ids=breadth.top10_concentration）——遠高於長均 ≈25%、結構性狹窄。
- **Advance/Decline 與新高/新低（proxy）**：≈**71.6%** S&P 500 成分股在 50 日均線上（2026-08-11，https://www.investing.com/indices/s-p-500-stocks-above-50-day-average，source_ids=breadth.advance_decline）——參與度維持改善、A/D 健康。
**結論**：分數維持 **30**（rubric 21–40 偏健康端）。RSP 等權維持領先、≈71.6% 成分股在 50DMA 上為健康面，與 Top-10 ≈37% 歷史高位相抵——正負相抵，淨評與前次持平。

### 3. 投機行為 — 55（weight 18%，Δ −2）
- **+AI 改名／SPAC**：本週（08-06–08-13）+AI 改名合格 **0** 件（2026-08-13 螢幕；ISSC→IA 08-11 為航太更名非 +AI，本窗無合格 +AI 改名／投機性 SPAC）——✓ SEARCH-VERIFIED（0 件）（source_ids=speculation.ai_rename_spac）。
- **IPO 熱度**：本週（08-06–08-13）一級市場定價密集——08-12 與 08-13 各約 **12** 檔定價、平均首日漲幅 ≈18%，惟無單檔無營收 blowout（2026-08-13，https://www.iposcoop.com/current-year-pricings/，source_ids=speculation.ipo_heat）——發行偏熱但無極端首日暴衝，體感中性偏熱。
- **Microcap thematic moonshots**：本週（08-06–08-13）microcap thematic moonshot 合格 **0** 件（2026-08-13 螢幕；<$1B、單日 ≥100% 或 2–3 日 ≥50%＋2 主題堆疊＋弱基本面；核／融合／量子主題有熱度但無單名達門檻）——✓ SEARCH-VERIFIED（0 件）（source_ids=speculation.microcap_moonshots）。
- **Upcoming AI mega-IPO pipeline**：OpenAI 傳目標 9 月上市、估值 ≈$**730**–850B（部分分析看逾 $1T、S-1 進程中）、Anthropic（$965B）與 SpaceX 亦在列（2026-07-28，https://cryptobriefing.com/openai-ipo-filing-trillion-valuation/，source_ids=speculation.upcoming_ai_ipos）——巨型 AI IPO pipeline 活躍、流動性抽離風險（時點轉保守）。
- **Insider selling clusters**：過去 14 日（07-30–08-13）無合格 AI／領導股 Form 4 賣壓 cluster **0** 件（2026-08-13 螢幕；openinsider／secform4 於本環境政策封鎖，窗內無可稽核之具名 filing-level 賣出）——✓ SEARCH-VERIFIED（0 件）（source_ids=speculation.insider_form4）。
- **Cboe equity-only put/call**：≈**0.54**（2026-08-07，https://www.thetrading.tools/put-call-ratio，source_ids=speculation.equity_put_call）——偏 call、未破 0.50 極端（計分輸入；較前次 0.55 略降）。
**結論**：分數自 57 降至 **55**（rubric 41–60「投機升溫」）。內部人賣壓 cluster 本週已滾出 14 日窗（前次升溫因子消退）、+AI 改名／microcap moonshot 均 0、put/call 0.54 略降為抑制面；IPO 定價密集、AI 巨型 IPO pipeline 活躍為支撐——抑制略多於支撐，淨評較前次降 2 分。

### 4. 散戶情緒 — 53（weight 12%，Δ −1）
- **CNN Fear & Greed**：≈**61「Greed」**（2026-08-12，https://www.cnn.com/markets/fear-and-greed，source_ids=retail.fear_greed）——由前次 ≈64 回落但仍處貪婪帶，散戶風險偏好邊際降溫。
- **Margin Debt**：6 月 **$1.502T（記錄高）、YoY +51.5%**（2026-07-20，https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026，source_ids=retail.margin_debt）——月頻 stock-of-state（7 月數據約 8 月下旬發布，沿用 6 月）；YoY +51.5% 仍屬 1999／2007／2021 頂部級別。
- **AAII 散戶調查**：Bull **37.0%**／Neutral 25.0%／Bear 38.0%（週結束 08-05）（2026-08-06，https://seekingalpha.com/article/4932187-aaii-sentiment-survey-optimism-jumps，source_ids=retail.aaii）——多方約長均、空方略高，散戶調查端中性。
- **家庭持股佔金融資產比**：**45.76%**（`BOGZ1FL153064486Q`，2026-01-01 資料日／2026-Q1，FRED BOGZ1FL153064486Q，source_ids=retail.household_equity_allocation）——歷史高位（Farrell #5，季頻沿用、不計週 Δ）。
- **社群情緒代理**：本週（08-06–08-13）無新具名迷因軋空——WEN「Save Wendy's」為 6–7 月事件、8 月延續但無新催化（✗ NOT DISCLOSED，source_ids=retail.social_sentiment，不納入計分）。
- **NAAIM Exposure Index**：本次無當期公開值——自 2026-08-01 改訂閱制、公開最新停於 79.70（07-29）（✗ NOT DISCLOSED，source_ids=retail.naaim，不納入計分；缺值不調降主分）。
**結論**：分數自 54 降至 **53**（rubric 41–60，F&G Greed 帶）。F&G 由 64 回落至 61 為降溫主因；margin debt 續創高（YoY +51.5%）、家庭持股歷史高位為背景，AAII 中性、社群與 NAAIM 無新增，淨評較前次降 1 分。

### 5. 貨幣與信貸環境 — 76（weight 20%，Δ 0）
- **Fed funds rate**：目標區間 **3.50–3.75%**（`DFEDTARU` 3.75%／`DFEDTARL` 3.50%，2026-08-12，FRED DFEDTARU/DFEDTARL，source_ids=monetary.fed_funds）——FOMC 維持不變。
- **市場隱含路徑（CME FedWatch，best-effort）**：CME FedWatch 9/16 會議 ≈**45%** 定價升息、無降息定價、偏鷹（2026-08-12，https://cryptobriefing.com/traders-45-percent-chance-september-fed-rate-hike/，source_ids=monetary.fedwatch）——Fed 未轉鴿、寬鬆空間受通膨制約（缺值不調分）。
- **Realized inflation vs expectations**：CPI YoY **3.3%**（`CPIAUCSL`，2026-07-01，FRED CPIAUCSL，source_ids=monetary.cpi_yoy）仍高於 2% 目標、5y5y forward **2.28%**（`T5YIFR`，2026-08-12，週 Δ −5 bps，FRED T5YIFR，source_ids=monetary.t5yifr）本週回落——通膨黏著但預期端回落，Fed 約束略鬆。
- **10Y 期限溢價（term premium）**：`THREEFYTP10` **0.8257%**（2026-08-07，Kim-Wright 三因子模型，序列自身 trailing ≈7d −4.2 bps，FRED THREEFYTP10，source_ids=monetary.term_premium）——財政風險再定價本週回落、遠未達 +15 bps 初啟門檻。
- **repo 資金壓力（SOFR−IORB）與 SRF 動用**：SOFR **3.64%**、IORB 3.65%、SOFR−IORB **−1 bps**；SOFR99 3.73%、SOFR99−IORB +8 bps；SRF/RPONTTLD 動用 ≈$0（2026-08-11，FRED SOFR/SOFR99/IORB/RPONTTLD，source_ids=monetary.repo_stress_srf）——secured-funding 無壓力、SRF 未動用。
- **美債標售需求（auction，best-effort）**：過去 14 日窗內標售需求轉強——3Y（08-11）bid-to-cover **2.71**、tail −0.5bp「stopped through」；10Y（08-12）bid-to-cover 2.58、需求略高於均值（30Y 08-13 在執行時點後未出）（2026-08-12，https://www.rttnews.com/3679611/ten-year-note-auction-attracts-modestly-above-average-demand.aspx，source_ids=monetary.treasury_auctions）——belly／長端需求改善＝財政供給壓力事件證據本週轉弱（confirmation；缺值不調分）。
- **HY OAS**：**2.72%**（`BAMLH0A0HYM2`，2026-08-11，週 Δ +2 bps，FRED BAMLH0A0HYM2，source_ids=monetary.hy_oas）——接近循環低、極窄、自滿側；本週微幅走闊（streak 由 0 增至 1、未達 2）。
- **IG OAS**：**0.79%**（`BAMLC0A0CM`，2026-08-11，週 Δ +1 bp，FRED BAMLC0A0CM，source_ids=monetary.ig_oas）——史窄、信用自滿。
- **10Y nominal 週變動拆解**：ΔDGS10 −2 bps；`DGS10` **4.70%**（2026-08-11，FRED DGS10，source_ids=monetary.dgs10）、`DFII10` **2.43%**（2026-08-11，FRED DFII10，source_ids=monetary.dfii10）、`T10YIE` **2.26%**（2026-08-12，FRED T10YIE，source_ids=monetary.t10yie）——三腿視窗不一致（driver=unknown，詳 §3），殖利率本週下行。
- **WTI 原油**：**$84.77**/bbl（`DCOILWTICO`，2026-08-11，週 +1.21%，FRED DCOILWTICO，source_ids=monetary.wti）——油價獨漲，A 通膨鏈油端有推力但未帶動通膨預期。
- **Fed balance sheet**：≈$6.75T（原始 **6,748,567** 百萬美元，2026-08-05，無新觀測，FRED WALCL，source_ids=monetary.walcl）——QT 步調持平。
- **全球央行流動性（ECB）**：ECB ≈€5.92T（原始 **5,923,023** 百萬歐元，2026-08-07，FRED ECBASSETSW，source_ids=monetary.ecb_boj）——持平。
- **全球央行流動性（BOJ）**：BOJ ≈¥644.30T（原始 **6,442,957** 億日圓，2026-07-01，FRED JPNASSETS，source_ids=monetary.ecb_boj）——持平。
- **PBoC 流動性操作**：本次無過去窗內新的人行／NBS 英文流動性摘要可稽核（✗ NOT DISCLOSED，source_ids=monetary.pboc，不納入計分）。
- **私募信貸贖回壓力（event-driven）**：過去 30 日（07-14–08-13）無新 gate proration / breach、無多基金 net inflow→outflow flip——最近具名事件（Blue Owl OCIC/OTIC 07-02、BCRED 5% gate 06-04）均已落 30 日窗外（✗ NOT DISCLOSED，source_ids=monetary.private_credit_liquidity，不納入計分）。
**結論**：自滿側；公開信用利差維持極度自滿（HY 2.72%／IG 0.79% 史窄），非銀融資扳機未擊發、30 日窗內無新 gate／breach，且本週美債標售需求轉強、期限溢價回落——屬「self-satisfied froth 而扳機未擊發」的自滿側組態；惟 AI 雲端信用轉為走闊為後期側背景壓力，尚未點燃任一 contract 扳機，分數維持 **76**。

### 6. 結構性槓桿 — 78（weight 15%，Δ 0）
- **US 槓桿 ETF AUM**：美國槓桿 ETF 總 AUM 維持記錄高 ≈$**198**B（TQQQ ≈$37.3B、SOXL ≈$22B 領先）（2026-07-23，https://cryptobriefing.com/leveraged-etfs-record-198b-aum/，source_ids=structural.leveraged_etf_aum）——水位記錄高（stock-of-state 沿用）。
- **US 單股槓桿 ETF 核准／發行（近 30 日）**：08-11 新發共 **6** 檔——Leverage Shares LITG／STLL／MXLL（2x 單股）、Tradr MRAX／SITX／UMCU（2026-08-11，https://www.globenewswire.com/news-release/2026/08/11/3342794/0/en/leverage-shares-by-themes-launches-three-new-2x-etfs-targeting-ai-infrastructure-and-connectivity-leaders.html，source_ids=structural.us_single_stock_etf）——單股槓桿產品續擴散（30 日窗內在案發行）。
- **全球（非美）槓桿產品核准（本週）**：韓國 FSC 反向收緊——2026-08-10 宣布暫停新單股槓桿 ETF 上市並調高保證金；台／日／歐 08-06–08-13 無新披露，「全球槓桿擴散訊號」本週未觸發，**本週擴散訊號未觸發**（✗ NOT DISCLOSED，source_ids=structural.global_leveraged_approvals，不納入計分）。
- **0DTE 佔 SPX 期權量**：≈**65**%（Cboe Q2 2026，資料日 2026-07-31，https://ca.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4768656，source_ids=structural.zero_dte）——持續 >55% 高檔（snapshot 沿用）。
- **Options 總量（OCC 月報）**：OCC 6 月總量 **1,603,491,559** 口（≈16.0 億口、YoY +45%）（2026-07-02，https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report，source_ids=structural.options_volume）——衍生品投機量續處高檔（stock-of-state 沿用；7 月報總量本次未取得）。
- **跨資產／相關性確認**：SKEW ≈**135.59**（2026-08-11）、VIX ≈15.28、MOVE ≈74.67（債市波動偏低）（2026-08-11，https://www.cboe.com/insights/posts/week-of-8-10-2026-spx-skew-collapses-on-upside-chasing，source_ids=structural.cross_asset_derivatives）——SKEW 回落（上檔追價）、股與債波動皆平靜（confirmation）。
- **VIX／S&P 500 同向（vix_spx_comove）**：本窗 VIX ≈**15.28**、S&P 500 −0.11%、VIX −7.39%，`comove=false`（as_of 2026-08-11、base_date 2026-08-04、window_days 7；FRED VIXCLS＋sp500_trend，source_ids=structural.vix_spx_comove）——股與波動未同向上行（波動端回落），crowded-optionality 同漲警戒未觸發、不調分。
- **Margin debt / 市值 交叉檢核**：6 月 $1.502T、YoY +**51.5**%（2026-07-20，見 D4，https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026，source_ids=structural.margin_debt_crosscheck）——確認零售槓桿頂部級別（confirmation，不在此重複計分）。
- **AI 基礎設施債務／vendor-financing loops**：本窗（30 日）披露——CoreWeave $**2.6**B 槓桿定期貸款（SOFR+5.50%、超額認購但被迫調高利差 +100–125bp、接受維持性 covenant）07-29 定價；另 Galaxy Digital 傳 ≈$3.5B 垃圾債為 CoreWeave 資料中心、Vantage/Stargate 傳籌 ≈$38B（2026-07-29，https://www.stocktitan.net/news/CRWV/core-weave-closes-2-6-billion-loan-facility-expanding-financing-gwhngwnf0jt5.html，source_ids=structural.ai_infrastructure_debt）——circular／vendor-financing 迴圈續在、且本週再融資成本上升，結構性槓桿背景升溫因子。
- **銀行對 NBFI 放款**：≈$2.00T（原始 **2,002.49** 十億美元，2026-07-29，無新觀測，FRED LNFACBW027SBOG，source_ids=structural.nbfi_bank_loans）——bank–NBFI linkage 水位持平（confirmation，不主計分）。
- **美債基差交易槓桿（best-effort）**：script `cftc_lev_funds`／`move_index`／`ofr_repo` 本次 `fetch_failed`（CFTC/OCC 網域於本環境政策封鎖）；WebSearch 顯示 MOVE ≈74.67 絕對水位仍低、無 7 日窗內具名基差交易平倉事件（Fed 估基差交易結構部位 ≈$830B 仍處紀錄高但未釋放）（✗ NOT DISCLOSED，source_ids=structural.treasury_basis_trade，不納入計分、不調 D6 分數）。
**結論**：分數維持 **78**（rubric 61–80）。0DTE 續 >55%、OCC 量高檔、槓桿 ETF AUM 維持創高、US 單股槓桿續擴散（08-11 新發 6 檔）、AI 基建融資迴圈續在且再融資成本上升＝結構性槓桿高檔；惟全球擴散未觸發（韓國反收緊）、VIX/S&P 未同漲、基差交易無窗內具名新事件為抑制——升抑相抵，淨評與前次持平。

## 綜合分數

| 維度 | 權重 | 分數 | 加權分數 |
|---|---:|---:|---:|
| 估值溢價 | 22% | 78 | 17.16 |
| 市場廣度 | 13% | 30 | 3.90 |
| 投機行為 | 18% | 55 | 9.90 |
| 散戶情緒 | 12% | 53 | 6.36 |
| 貨幣與信貸環境 | 20% | 76 | 15.20 |
| 結構性槓桿 | 15% | 78 | 11.70 |
加權總分：64.22 → 64【警戒】

邊界帶：總分 64 距 警戒/高 邊界 ≤ 2 分，評分固有噪音約 ±2–3，等級判讀需保留餘地。

## 歷史泡沫週期對比

相似度計算：checklist v2

逐項對本次六維度分數、macro/current/prior state 與附錄證據重算命中；相似度 = 命中數 ÷ 特徵數 × 100，四捨五入到最近 5%。「無資料」不計入命中但仍在分母。

- 1973/1 Nifty Fifty 頂：命中 2/8 = 25%
- 1997 早期建設：命中 4/8 = 50%
- 1998 LTCM 衝擊：命中 2/8 = 25%
- 1999 晚期狂熱：命中 6/10 = 60%
- 2000/3 頂點：命中 1/8 = 15%
- 2021/12 Meme 頂：命中 3/8 = 40%

2000/3 高位回落條件：是

**1973/1 Nifty Fifty 頂 feature audit**
- 1973.1｜未命中｜source_ids=—｜估值溢價 78 < 80
- 1973.2｜未命中｜source_ids=—｜市場廣度 30 < 60
- 1973.3｜未命中｜source_ids=—｜CPI YoY 3.3% < 4%
- 1973.4｜未命中｜source_ids=—｜T5YIFR 週 Δ −5 bps < 0（通膨預期回落）
- 1973.5｜命中｜source_ids=—｜WTI 週漲幅 +1.21% ≥ +0.5%（方向 ▲）
- 1973.6｜未命中｜source_ids=—｜decomposition.driver=unknown ≠ breakeven（三腿視窗不一致）
- 1973.7｜未命中｜source_ids=—｜扳機狀態＝未擊發 < 初啟
- 1973.8｜命中｜source_ids=—｜散戶情緒 53 < 55
**1997 早期建設 feature audit**
- 1997.1｜未命中｜source_ids=—｜估值溢價 78 > 74（超出 40–74 區間）
- 1997.2｜命中｜source_ids=—｜市場廣度 30 < 45
- 1997.3｜未命中｜source_ids=—｜投機行為 55 ≥ 50
- 1997.4｜命中｜source_ids=ai.hyperscaler_capex｜hyperscaler 2026 capex 指引仍上修（合計 ≈$725B）
- 1997.5｜命中｜source_ids=—｜散戶情緒 53 < 55
- 1997.6｜未命中｜source_ids=—｜結構性槓桿 78 ≥ 50
- 1997.7｜未命中｜source_ids=—｜HY OAS 2.72% < 4% 但週 Δ +2 bps > 0（本週走闊，all 不成立）
- 1997.8｜命中｜source_ids=—｜扳機狀態＝未擊發
**1998 LTCM 衝擊 feature audit**
- 1998.1｜未命中｜source_ids=structural.cross_asset_derivatives｜HY 週 Δ +2 bps < +30；VIX ≈15.28、SKEW 回落（無壓力事件）
- 1998.2｜未命中｜source_ids=—｜S&P chg −0.06% > −5%（未達回檔門檻）
- 1998.3｜無資料｜source_ids=—｜私募信貸與美債基差交易本次皆 ✗ NOT DISCLOSED（無成功事件證據）
- 1998.4｜未命中｜source_ids=monetary.fedwatch｜FedWatch 偏鷹（≈45% 升息定價、無降息），非轉鴿
- 1998.5｜命中｜source_ids=—｜估值溢價 78 ≥ 60
- 1998.6｜未命中｜source_ids=—｜扳機狀態＝未擊發 < 初啟
- 1998.7｜未命中｜source_ids=—｜市場廣度 Δ = 30 − 30 = 0 < +8
- 1998.8｜命中｜source_ids=—｜ΔT10YIE −3 bps ≤ 0（通膨預期非上行）
**1999 晚期狂熱 feature audit**
- 1999.1｜命中｜source_ids=—｜估值溢價 78 ≥ 75
- 1999.2｜命中｜source_ids=valuation.sp500_pe_cape｜CAPE 42.34 ≥ 38
- 1999.3｜未命中｜source_ids=—｜投機行為 55 < 60
- 1999.4｜未命中｜source_ids=speculation.microcap_moonshots,speculation.ipo_heat｜本週 moonshot 0；無營收 IPO 佔比未達偏高
- 1999.5｜未命中｜source_ids=—｜市場廣度 30 < 45（廣度健康、非轉窄）
- 1999.6｜命中｜source_ids=—｜D5 monetary_side＝自滿側 且 HY OAS 2.72% < 3.5%（all 成立）
- 1999.7｜命中｜source_ids=—｜結構性槓桿 78 ≥ 60
- 1999.8｜未命中｜source_ids=—｜散戶情緒 53 < 55
- 1999.9｜命中｜source_ids=speculation.upcoming_ai_ipos｜巨型 AI IPO pipeline 活躍（OpenAI ≈$730–850B、Anthropic）
- 1999.10｜命中｜source_ids=—｜扳機狀態＝未擊發
**2000/3 頂點 feature audit**
- 2000.1｜未命中｜source_ids=—｜估值溢價 78 < 85
- 2000.2｜未命中｜source_ids=—｜扳機狀態＝未擊發 < 初啟
- 2000.3｜未命中｜source_ids=—｜市場廣度 30 < 60
- 2000.4｜命中｜source_ids=—｜high_retreat：prior sp500_dev200_pct 10.04 > +10 且 current 9.67 < prior（高位回落成立）
- 2000.5｜未命中｜source_ids=—｜投機行為 55 < 70
- 2000.6｜未命中｜source_ids=speculation.insider_form4｜14 日窗內合格 Form 4 cluster 0 件（✓ SEARCH-VERIFIED 0 件）
- 2000.7｜未命中｜source_ids=—｜散戶情緒 53 < 65
- 2000.8｜未命中｜source_ids=monetary.fedwatch｜FedWatch 未定價明確緊縮週期（政策維持）；10Y driver≠breakeven（且殖利率下行）
**2021/12 Meme 頂 feature audit**
- 2021.1｜未命中｜source_ids=—｜散戶情緒 53 < 65
- 2021.2｜無資料｜source_ids=—｜retail.social_sentiment ✗ NOT DISCLOSED（無新具名社群軋空）
- 2021.3｜命中｜source_ids=—｜結構性槓桿 78 ≥ 65
- 2021.4｜命中｜source_ids=monetary.walcl,monetary.ecb_boj｜D5 76 ≥ 60 且自滿側、央行資產負債表可得（流動性氾濫，all 命中）
- 2021.5｜命中｜source_ids=retail.margin_debt｜margin debt YoY +51.5% ≥ +40%
- 2021.6｜未命中｜source_ids=speculation.microcap_moonshots｜本週 microcap moonshot 0 < 1
- 2021.7｜未命中｜source_ids=—｜市場廣度 30 < 50
- 2021.8｜未命中｜source_ids=—｜CPI YoY 3.3% < 4%（all 不成立）

**兩句解讀**：本週最貼近錨點由「1997 早期建設」轉為「1999 晚期狂熱」（60%）——當前組態為高估值（CAPE ≈42.34、估值溢價 78、1999.1/1999.2 命中）＋高結構性槓桿（78，1999.7）＋極度自滿的公開信用（HY 2.72% < 3.5%、自滿側，1999.6）＋活躍的巨型 AI IPO pipeline（1999.9），且扳機狀態＝未擊發（1999.10），最像 1999 晚期狂熱相位，惟廣度尚健康（30）、投機未達狂熱（55）、散戶未全面貪婪（53），為「晚期狂熱的前段」而非頂點。循環位置意涵：估值＋槓桿位能高企、AI 信貸開始重定價（後期訊號）、格局轉為分歧（油漲而殖利率／通膨預期反向），屬 froth 續高但時點扳機未擊發的中後段，且「扳機鏈 A 尚未驗證啟動」（1973.6 未命中、扳機理由無 breakeven_wti_up）；與 2000/3 頂點（15%）的關鍵分歧在於扳機未擊發、廣度未極窄、散戶未狂熱，惟 2000/3「高位回落條件＝是」已成立（S&P 距 200DMA 自 +10.04% 回落至 +9.67%），最須盯 AI 雲端信用走闊是否外溢至公開利差與國債市場。長期指數成長趨勢偏離（Dot-com ≈95%、1929 ≈110%、當前 AI 週期 ≈147%；RIA/Farrell）作跨期敘事錨、不進 checklist。

## 機構情緒對照

本次無新機構調查數據。（BofA FMS 8 月版尚未發布、7 月版早於前次基準；JPM 亦無本次新增。）背景參照：7 月 BofA FMS 現金水位 ≈3.6% AUM、觸及 <4% 的「賣出訊號」極端；NAAIM Exposure Index 自 2026-08-01 改訂閱制，公開最新值停於 79.70（2026-07-29，主動經理人曝險中高、已自近高回落，Farrell #9，於 D4 作 confirmation cross-check、本節僅敘述不計分）。

## 本次新增訊號

比較基準：vs 前次（3天前）。

- **投機行為（D3）Δ −2**：內部人賣壓 cluster 本週滾出 14 日窗（前次升溫因子消退）、+AI 改名／microcap moonshot 均 0 件、put/call 0.54 略降；IPO 定價密集但無無營收 blowout——分數自 57 降至 55。
- **散戶情緒（D4）Δ −1**：CNN Fear & Greed 由 ≈64 回落至 ≈61「Greed」（2026-08-12）、AAII 多方 37.0% 中性；margin debt 續創高（$1.502T、YoY +51.5%）為背景——froth 邊際降溫，分數自 54 降至 53。
- **總分退回「警戒」帶**：加權總分自 64.70 降至 64.22 → 64【警戒】（Δ −1），tier 由 高 轉 警戒；動因為投機 −2、散戶 −1，其餘四維度持平。屬邊界帶內（距 警戒/高 邊界 ≤ 2 分）之降級，等級判讀需保留 ±2–3 噪音餘地。
- **格局由「穩定共存」轉「分歧」**：本週油價獨漲（+1.21%）而 10Y 殖利率（−2 bps）與通膨預期（ΔT10YIE −3 bps）反向下行，出現 ▲/▼ 混合，格局判定為分歧；`regime` 由前次穩定共存更新為分歧。
- **貨幣與信貸環境（D5，Δ 0，＝自滿側）**：公開信用利差維持極度自滿（HY 2.72%／IG 0.79% 史窄），非銀融資扳機未擊發、30 日窗內無新 gate／breach；本週美債標售需求轉強（3Y BTC 2.71、10Y BTC 2.58）、期限溢價回落，financing 壓力事件面反而轉弱，monetary_side 維持自滿側、分數持平。
- **AI 雲端信用轉為走闊（後期訊號）**：CoreWeave $2.6B 貸款被迫調高利差 +100–125bp、Oracle 5Y CDS ≈75bp（7 年高）、Fitch／Moody's 發 AI 基建信用預警——issuer 層級信貸先醒、公開 HY/IG 尚未跟進；屬 D1／D6 質化升溫背景，最須盯是否外溢至公開利差。
- **HY OAS streak 由 0 增至 1**：本次 HY OAS 週 Δ +2 bps（走闊），依決定性公式 streak = 0+1 = 1——「HY 連續兩次走闊」初啟判準（≥2）本次未成立。
- **結構性槓桿（D6，Δ 0）**：US 單股槓桿續擴散（08-11 新發 6 檔）、AI 基建融資迴圈續在且再融資成本上升；全球（非美）槓桿擴散本週未觸發（韓國 FSC 暫停新上市）、本週擴散訊號未觸發、VIX/S&P 未同漲，分數持平。
- 其餘維度（估值 78、廣度 30）分數與前次持平。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | S&P 500 收盤（sp500_trend latest） | 7,748.5 | FRED SP500（sp500_trend） | 2026-08-12 | 2026-08-13T09:13:33+08:00 |
| valuation.sp500_trend | S&P 500 距 200DMA 偏離（sp500_trend dev200_pct） | +9.67% | FRED SP500（sp500_trend） | 2026-08-12 | 2026-08-13T09:13:33+08:00 |
| valuation.sp500_trend | S&P 500 距 52 週均線偏離（sp500_trend dev52w_pct） | +11.23% | FRED SP500（sp500_trend） | 2026-08-12 | 2026-08-13T09:13:33+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 29.85 | https://www.multpl.com/s-p-500-pe-ratio | 2026-08-12 | 2026-08-13T09:35:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE | 42.34 | https://www.multpl.com/shiller-pe | 2026-08-12 | 2026-08-13T09:35:00+08:00 |
| valuation.sp500_pe_cape | Excess CAPE Yield（derived：1/CAPE − DFII10/100） | −0.07% | derived（CAPE 42.34／DFII10 2.43%） | 2026-08-12 | 2026-08-13T09:35:00+08:00 |
| valuation.mag7_multiples | Mag 7 加權 P/E vs 指數（佔市值 ≈33.9%） | ≈29x vs ≈25.6x | https://www.fool.com/research/magnificent-seven-sp-500/ | 2026-08-12 | 2026-08-13T09:35:00+08:00 |
| valuation.analyst_tp_decomposition | Susquehanna TSMC 目標 $575→$600（EPS-driven） | $600 | https://www.tipranks.com/news/tsmc-stock-price-forecast-top-analysts-raise-targets-ahead-of-q2-earnings | 2026-07-16 | 2026-08-13T09:35:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 貸款利差調高／Oracle 5Y CDS | +100–125bp（Oracle CDS ≈75bp） | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm | 2026-08-03 | 2026-08-13T09:35:00+08:00 |
| breadth.rsp_spy | RSP 等權 vs SPY YTD 總報酬 | +9.67% vs +8.38% | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ | 2026-06-10 | 2026-08-13T09:35:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 | ≈37% | https://www.rbcwealthmanagement.com/en-us/insights/the-great-narrowing-sp-500-concentration | 2026-07-24 | 2026-08-13T09:35:00+08:00 |
| breadth.advance_decline | S&P 500 成分股 >50DMA 比例 | ≈71.6% | https://www.investing.com/indices/s-p-500-stocks-above-50-day-average | 2026-08-11 | 2026-08-13T09:35:00+08:00 |
| retail.fear_greed | CNN Fear & Greed | ≈61（Greed） | https://www.cnn.com/markets/fear-and-greed | 2026-08-12 | 2026-08-13T09:35:00+08:00 |
| retail.margin_debt | FINRA margin debt（6 月）／YoY | $1.502T／+51.5% | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-13T09:35:00+08:00 |
| retail.aaii | AAII Bull／Neutral／Bear | 37.0%／25.0%／38.0% | https://seekingalpha.com/article/4932187-aaii-sentiment-survey-optimism-jumps | 2026-08-06 | 2026-08-13T09:35:00+08:00 |
| retail.household_equity_allocation | 家庭持股佔金融資產比（BOGZ1FL153064486Q） | 45.76 | FRED BOGZ1FL153064486Q | 2026-01-01 | 2026-08-13T09:13:33+08:00 |
| monetary.fed_funds | Fed funds 上限（DFEDTARU） | 3.75% | FRED DFEDTARU | 2026-08-12 | 2026-08-13T09:13:33+08:00 |
| monetary.fed_funds | Fed funds 下限（DFEDTARL） | 3.50% | FRED DFEDTARL | 2026-08-12 | 2026-08-13T09:13:33+08:00 |
| monetary.fedwatch | CME FedWatch 9/16 升息機率 | ≈45%（無降息定價、偏鷹） | https://cryptobriefing.com/traders-45-percent-chance-september-fed-rate-hike/ | 2026-08-12 | 2026-08-13T09:35:00+08:00 |
| monetary.hy_oas | HY OAS（BAMLH0A0HYM2） | 2.72% | FRED BAMLH0A0HYM2 | 2026-08-11 | 2026-08-13T09:13:33+08:00 |
| monetary.ig_oas | IG OAS（BAMLC0A0CM） | 0.79% | FRED BAMLC0A0CM | 2026-08-11 | 2026-08-13T09:13:33+08:00 |
| monetary.dgs10 | 10Y 名目殖利率（DGS10） | 4.70% | FRED DGS10 | 2026-08-11 | 2026-08-13T09:13:33+08:00 |
| monetary.dfii10 | 10Y 實質殖利率（DFII10） | 2.43% | FRED DFII10 | 2026-08-11 | 2026-08-13T09:13:33+08:00 |
| monetary.t10yie | 10Y breakeven（T10YIE） | 2.26% | FRED T10YIE | 2026-08-12 | 2026-08-13T09:13:33+08:00 |
| monetary.wti | WTI 原油（DCOILWTICO） | $84.77 | FRED DCOILWTICO | 2026-08-11 | 2026-08-13T09:13:33+08:00 |
| monetary.cpi_yoy | CPI YoY（CPIAUCSL yoy_pct） | 3.3% | FRED CPIAUCSL | 2026-07-01 | 2026-08-13T09:13:33+08:00 |
| monetary.t5yifr | 5y5y forward（T5YIFR latest） | 2.28% | FRED T5YIFR | 2026-08-12 | 2026-08-13T09:13:33+08:00 |
| monetary.term_premium | 10Y 期限溢價（THREEFYTP10） | 0.8257% | FRED THREEFYTP10 | 2026-08-07 | 2026-08-13T09:13:33+08:00 |
| monetary.repo_stress_srf | SOFR 隔夜擔保融資利率 | 3.64% | FRED SOFR | 2026-08-11 | 2026-08-13T09:13:33+08:00 |
| monetary.repo_stress_srf | SOFR99 99th 分位尾端利率 | 3.73% | FRED SOFR99 | 2026-08-11 | 2026-08-13T09:13:33+08:00 |
| monetary.repo_stress_srf | IORB 準備金餘額利率 | 3.65% | FRED IORB | 2026-08-13 | 2026-08-13T09:13:33+08:00 |
| monetary.repo_stress_srf | 隔夜 repo 操作量（RPONTTLD） | 0.0（≈$0） | FRED RPONTTLD | 2026-08-12 | 2026-08-13T09:13:33+08:00 |
| monetary.treasury_auctions | 3Y／10Y 標售 bid-to-cover（14 日窗內、需求轉強） | 3Y 2.71／10Y 2.58 | https://www.rttnews.com/3679611/ten-year-note-auction-attracts-modestly-above-average-demand.aspx | 2026-08-12 | 2026-08-13T09:35:00+08:00 |
| monetary.walcl | Fed 資產負債表（WALCL） | 6,748,567 百萬美元（≈$6.75T） | FRED WALCL | 2026-08-05 | 2026-08-13T09:13:33+08:00 |
| monetary.ecb_boj | ECB 資產（ECBASSETSW） | 5,923,023 百萬歐元（≈€5.92T） | FRED ECBASSETSW | 2026-08-07 | 2026-08-13T09:13:33+08:00 |
| monetary.ecb_boj | BOJ 資產（JPNASSETS） | 6,442,957 億日圓（≈¥644.30T） | FRED JPNASSETS | 2026-07-01 | 2026-08-13T09:13:33+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計（仍上修） | ≈$725B | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-07-28 | 2026-08-13T09:35:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 超越 FCF（Alphabet Q2 FCF 轉負）、2026 發債 ≈$182B | hyperscaler capex FCF debt issuance 182 billion 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure | 2026-07-24 | 2026-08-13T09:35:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan][spv_deal] Meta El Paso 資料中心 BlackRock 主導 >$12B 債券（20-30yr triple-net lease、表外結構） sponsor_equity_split=undisclosed;residual_value_guarantee=undisclosed;lease_term=20-30yr;debt_tenor=undisclosed;lead_lenders=BlackRock/JPMorgan/MS; | >$12B | https://www.landgate.com/news/blackrock-s-12-billion-bond-sale-signals-a-new-financing-playbook-for-data-center-developers | 2026-07-20 | 2026-08-13T09:35:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic／OpenAI 年化 run-rate | ≈$47B／≈$25B | https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth | 2026-05-29 | 2026-08-13T09:35:00+08:00 |
| ai.customer_concentration_rpo | Microsoft 商用 RPO／單一客戶佔比 | $678B／≈32%（OpenAI） | https://www.benzinga.com/trading-ideas/long-ideas/26/07/60816147/microsofts-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer | 2026-07-30 | 2026-08-13T09:35:00+08:00 |
| ai.compute_supply_demand | H200 租金中位／HBM 合約 | ≈$3.99/hr／≈+40% | https://jarvislabs.ai/blog/h200-price | 2026-08-01 | 2026-08-13T09:35:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收 vs 年化 capex（top-4＋Oracle） | ≈$72B vs ≈$725B | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-06-15 | 2026-08-13T09:35:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價密集／平均首日 | ≈12 檔/日（首日 ≈18%） | https://www.iposcoop.com/current-year-pricings/ | 2026-08-13 | 2026-08-13T09:35:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI IPO 估值／pipeline | ≈$730–850B | https://cryptobriefing.com/openai-ipo-filing-trillion-valuation/ | 2026-07-28 | 2026-08-13T09:35:00+08:00 |
| speculation.equity_put_call | Cboe equity-only put/call | 0.54 | https://www.thetrading.tools/put-call-ratio | 2026-08-07 | 2026-08-13T09:35:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM（記錄高） | ≈$198B | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-07-23 | 2026-08-13T09:35:00+08:00 |
| structural.us_single_stock_etf | 08-11 新發單股 2x 槓桿 ETF（30 日窗內） | 6 檔 | https://www.globenewswire.com/news-release/2026/08/11/3342794/0/en/leverage-shares-by-themes-launches-three-new-2x-etfs-targeting-ai-infrastructure-and-connectivity-leaders.html | 2026-08-11 | 2026-08-13T09:35:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量（Cboe Q2） | ≈65% | https://ca.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4768656 | 2026-07-31 | 2026-08-13T09:35:00+08:00 |
| structural.options_volume | OCC 6 月總量 | 1,603,491,559 口（≈16.0 億口） | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report | 2026-07-02 | 2026-08-13T09:35:00+08:00 |
| structural.cross_asset_derivatives | SKEW／VIX／MOVE | 135.59／15.28／74.67 | https://www.cboe.com/insights/posts/week-of-8-10-2026-spx-skew-collapses-on-upside-chasing | 2026-08-11 | 2026-08-13T09:35:00+08:00 |
| structural.vix_spx_comove | VIX 收盤（VIXCLS） | 15.28 | FRED VIXCLS | 2026-08-11 | 2026-08-13T09:13:33+08:00 |
| structural.vix_spx_comove | vix_spx_comove 同向讀數（comove=false） | 15.28 | FRED vix_spx_comove 派生（base_date 2026-08-04、window 7d） | 2026-08-11 | 2026-08-13T09:13:33+08:00 |
| structural.margin_debt_crosscheck | margin debt／YoY（交叉引用 D4） | $1.502T／+51.5% | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-13T09:35:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B 貸款調高票息＋covenant | +100–125bp | https://www.stocktitan.net/news/CRWV/core-weave-closes-2-6-billion-loan-facility-expanding-financing-gwhngwnf0jt5.html | 2026-07-29 | 2026-08-13T09:35:00+08:00 |
| structural.nbfi_bank_loans | 銀行對 NBFI 放款（LNFACBW027SBOG） | 2,002.49 十億美元（≈$2.00T） | FRED LNFACBW027SBOG | 2026-07-29 | 2026-08-13T09:13:33+08:00 |

### Coverage

| source_id | 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl/gurufocus [primary: SEARCH] | ✓ SEARCH-VERIFIED（P/E 29.85、CAPE 42.34 @08-12） |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E | Fool/SSGA [SEARCH]（stock-of-state 沿用） | ✓ SEARCH-VERIFIED（Mag7 ≈29x vs 指數 ≈25.6x @08-12） |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Susquehanna TSMC $600 EPS-driven @07-16，Q3 內） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500 派生） | ✓ API（dev200 +9.67%／dev52 +11.23%） |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧 | 信用市場 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（CoreWeave +100–125bp、Oracle CDS ≈75bp @08-03） |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 24/7 Wall St [SEARCH] | ✓ SEARCH-VERIFIED（RSP +9.67% 領先 SPY +8.38% TR @06-10） |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | RBC/財經媒體 [SEARCH] | ✓ SEARCH-VERIFIED（≈37%，歷史高位 @07-24） |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | Investing.com breadth [SEARCH] | ✓ SEARCH-VERIFIED（≈71.6% >50DMA @08-11） |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（≈61 Greed @08-12） |
| retail.margin_debt | 散戶｜Margin Debt: FINRA | FINRA/Advisor Perspectives [SEARCH]（月頻 stock-of-state） | ✓ SEARCH-VERIFIED（$1.502T、+51.5% YoY、2026-06；7 月未發布沿用） |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（Bull 37.0%／Bear 38.0% 週結束 08-05 @08-06） |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB/cashtag [SEARCH]（best-effort） | ✗ NOT DISCLOSED（WEN 為 6–7 月事件、本窗無新具名投機熱） |
| retail.household_equity_allocation | 散戶｜Household equity allocation | fetch_macro.py BOGZ1FL153064486Q | ✓ API（45.76% @2026-Q1） |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim/YCharts [primary: SEARCH]（best-effort） | ✗ NOT DISCLOSED（08-01 起訂閱制、無當期公開值；末公開 79.70 @07-29） |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM | 賣方調查 [SEARCH]（月頻，best-effort） | ✗ NOT DISCLOSED（8 月 FMS 未發布、7 月早於前次基準） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED DFEDTARU/DFEDTARL | fetch_macro.py FRED API | ✓ API（3.75%/3.50% @08-12；DFEDTARU/DFEDTARL 皆 ok） |
| monetary.hy_oas | 貨幣｜High Yield OAS | fetch_macro.py FRED API | ✓ API（2.72% @08-11，Δ +2bps） |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | fetch_macro.py FRED API | ✓ API（0.79% @08-11，Δ +1bp） |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | fetch_macro.py FRED API | ✓ API（4.70% @08-11，Δ −2bps） |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield | fetch_macro.py FRED API | ✓ API（2.43% @08-11，Δ 0bps） |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | fetch_macro.py FRED API | ✓ API（2.26% @08-12，Δ −3bps） |
| monetary.wti | 貨幣｜WTI crude oil price | fetch_macro.py FRED API | ✓ API（$84.77 @08-11，+1.21%） |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED | fetch_macro.py FRED API（月頻） | ✓ API（3.3% @2026-07） |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | fetch_macro.py FRED API | ✓ API（2.28% @08-12，Δ −5bps） |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED | fetch_macro.py FRED API | ✓ API（0.8257% @08-07，−4.2bps trailing） |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py repo_stress | ✓ API（SOFR−IORB −1bps、SOFR99−IORB +8bps、SRF ≈$0 @08-11；SOFR/SOFR99/IORB/RPONTTLD 皆 ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求 | Reuters/RTTNews recap [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（3Y BTC 2.71、10Y BTC 2.58、需求轉強 @08-12，14 日窗內） |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（9 月 ≈45% 升息定價、偏鷹 @08-12） |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED WALCL | fetch_macro.py FRED API | ✓ API（$6.75T @08-05，無新觀測） |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | fetch_macro.py FRED API | ✓ API（€5.92T @08-07／¥644.30T @07-01） |
| monetary.pboc | 貨幣｜PBoC aggregate financing | investing/Yicai [SEARCH]（best-effort） | ✗ NOT DISCLOSED（本次無窗內新的英文流動性摘要） |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]（best-effort） | ✗ NOT DISCLOSED（Blue Owl 07-02、BCRED 06-04 均落 30 日窗外、無新事件） |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報 [SEARCH]（stock-of-state） | ✓ SEARCH-VERIFIED（合計 ≈$725B、仍上修 @07-28） |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic/OpenAI/Google [SEARCH]（best-effort） | ✗ NOT DISCLOSED（本季無乾淨可歸期之量化成長率） |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | VentureBeat/報導 [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Anthropic ≈$47B／OpenAI ≈$25B run-rate @05-29） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration | 財報電話 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（MSFT RPO $678B、≈32% 繫 OpenAI @07-30） |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce/jarvislabs [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（HBM ≈+40%、H200 租金 ≈$3.99/hr、Blackwell 售罄 @08-01） |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構 | 季報/發債 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口 | 組合披露 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（年化 capex ≈$725B vs 終端營收 ≈$72B @06-15） |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K/10-Q [primary: SEARCH]（best-effort，30日） | ✗ NOT DISCLOSED（過去 30 日無新變更） |
| ai.capital_cycle | AI｜資本週期階段 | 供需增速+進出場事件 [SEARCH]（best-effort） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days +AI rename/SPAC | [SEARCH] | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | IPOScoop/Renaissance [SEARCH] | ✓ SEARCH-VERIFIED（08-12/08-13 各 ≈12 檔定價 @08-13） |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz/StockAnalysis [primary: SEARCH]（required 週螢幕） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | S-1/具名報導 [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（OpenAI ≈$730–850B、Anthropic 續進 @07-28） |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership | SEC EDGAR [primary: EDGAR]（required） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe/thetrading.tools [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（0.54 @08-07） |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing/etf.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（總 ≈$198B 記錄高 @07-23） |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | Leverage Shares/Tradr [SEARCH] | ✓ SEARCH-VERIFIED（08-11 新發 6 檔 @08-11，30 日窗內） |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX/TWSE/JPX/ESMA [SEARCH]（best-effort，7日） | ✗ NOT DISCLOSED（韓國反收緊、本週擴散訊號未觸發） |
| structural.zero_dte | 結構｜0DTE option volume | Cboe [SEARCH]（Cboe 403） | ✓ SEARCH-VERIFIED（≈65%，Cboe Q2 @07-31） |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com [SEARCH] | ✓ SEARCH-VERIFIED（6 月 16.0 億口 @07-02；7 月報總量未取得） |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe/Convex [SEARCH] | ✓ SEARCH-VERIFIED（SKEW 135.59、VIX 15.28、MOVE 74.67 @08-11） |
| structural.vix_spx_comove | 結構｜VIX / S&P 500 co-movement | fetch_macro.py vix_spx_comove（FRED VIXCLS＋sp500_trend） | ✓ API（comove=false、VIX 15.28、window 7d @08-11；VIXCLS/vix_spx_comove 皆 ok） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 D4（confirmation） | ✓ SEARCH-VERIFIED（$1.502T/+51.5% YoY，D4 引用不重複計分） |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]（best-effort，30日） | ✓ SEARCH-VERIFIED（CoreWeave $2.6B 調高利差 +100–125bp @07-29） |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | fetch_macro.py FRED API | ✓ API（$2.00T @07-29，無新觀測） |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | script→WebSearch [primary: script]（best-effort） | ✗ NOT DISCLOSED（cftc/move/ofr script fetch_failed、無 7 日窗內具名新事件） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E ≈29.85、CAPE ≈42.34 | S&P 500 trailing P/E CAPE August 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio | 2026-08-12 | 2026-08-13T09:35:00+08:00 |
| valuation.mag7_multiples | Mag 7 ≈29x vs 指數 ≈25.6x、佔市值 ≈33.9% | Magnificent 7 weighted PE vs S&P 500 August 2026 | https://www.fool.com/research/magnificent-seven-sp-500/ | 2026-08-12 | 2026-08-13T09:35:00+08:00 |
| valuation.analyst_tp_decomposition | Susquehanna TSMC 目標 $575→$600、EPS-driven（Q3 內） | Susquehanna TSMC price target 600 July 2026 earnings | https://www.tipranks.com/news/tsmc-stock-price-forecast-top-analysts-raise-targets-ahead-of-q2-earnings | 2026-07-16 | 2026-08-13T09:35:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 貸款利差 +100–125bp、Oracle CDS ≈75bp（7 年高）、Fitch/Moody's 預警 | CoreWeave Oracle CDS spread AI credit widening August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm | 2026-08-03 | 2026-08-13T09:35:00+08:00 |
| breadth.rsp_spy | RSP 等權 YTD +9.67% 領先 SPY +8.38% | RSP vs SPY equal weight YTD total return August 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ | 2026-06-10 | 2026-08-13T09:35:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 ≈37% | S&P 500 top 10 concentration percent 2026 | https://www.rbcwealthmanagement.com/en-us/insights/the-great-narrowing-sp-500-concentration | 2026-07-24 | 2026-08-13T09:35:00+08:00 |
| breadth.advance_decline | ≈71.6% S&P 500 在 50DMA 上 | S&P 500 percent above 50 day moving average August 2026 | https://www.investing.com/indices/s-p-500-stocks-above-50-day-average | 2026-08-11 | 2026-08-13T09:35:00+08:00 |
| retail.fear_greed | CNN Fear & Greed ≈61（Greed） | CNN Fear and Greed Index August 12 2026 | https://www.cnn.com/markets/fear-and-greed | 2026-08-12 | 2026-08-13T09:35:00+08:00 |
| retail.margin_debt | FINRA 6 月 margin debt $1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-13T09:35:00+08:00 |
| retail.aaii | AAII Bull 37.0%／Neutral 25.0%／Bear 38.0%（週結束 08-05） | AAII investor sentiment survey week August 5 2026 | https://seekingalpha.com/article/4932187-aaii-sentiment-survey-optimism-jumps | 2026-08-06 | 2026-08-13T09:35:00+08:00 |
| monetary.treasury_auctions | 3Y 08-11 BTC 2.71 tail −0.5bp、10Y 08-12 BTC 2.58 需求略高於均值（14 日窗內） | US Treasury 3 year 10 year auction bid to cover August 2026 | https://www.rttnews.com/3679611/ten-year-note-auction-attracts-modestly-above-average-demand.aspx | 2026-08-12 | 2026-08-13T09:35:00+08:00 |
| monetary.fedwatch | CME FedWatch 9/16 ≈45% 升息、無降息定價、偏鷹 | CME FedWatch September 2026 rate hike probability | https://cryptobriefing.com/traders-45-percent-chance-september-fed-rate-hike/ | 2026-08-12 | 2026-08-13T09:35:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 合計 ≈$725B、仍上修 | hyperscaler capex 2026 725 billion raised Q2 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-07-28 | 2026-08-13T09:35:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 超越 FCF、2026 發債 ≈$182B | hyperscaler capex FCF debt issuance 182 billion 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure | 2026-07-24 | 2026-08-13T09:35:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic run-rate ≈$47B、OpenAI ≈$25B | OpenAI Anthropic annualized revenue run-rate 2026 | https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth | 2026-05-29 | 2026-08-13T09:35:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO ≈$678B、≈32% 繫單一客戶（OpenAI） | Microsoft RPO backlog 678 billion OpenAI 2026 | https://www.benzinga.com/trading-ideas/long-ideas/26/07/60816147/microsofts-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer | 2026-07-30 | 2026-08-13T09:35:00+08:00 |
| ai.compute_supply_demand | HBM 合約 ≈+40%、H200 租金 ≈$3.99/hr、Blackwell 售罄 | H200 GPU rental HBM DRAM 2026 shortage Blackwell | https://jarvislabs.ai/blog/h200-price | 2026-08-01 | 2026-08-13T09:35:00+08:00 |
| ai.revenue_capex_gap | AI 終端年化營收 ≈$72B vs 年化 capex ≈$725B（top-4＋Oracle） | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-06-15 | 2026-08-13T09:35:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 超越 FCF、續靠發債 | hyperscaler capex vs free cash flow debt 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure | 2026-07-24 | 2026-08-13T09:35:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 螢幕合格件數 0 | AI rename ticker SPAC no revenue IPO August 6-13 2026 | Reuters/Benzinga/SEC 螢幕 | 2026-08-13 | 2026-08-13T09:40:00+08:00 |
| speculation.ipo_heat | 本週 08-12/08-13 各 ≈12 檔定價、平均首日 ≈18% | US IPO pricings week August 2026 IPOScoop | https://www.iposcoop.com/current-year-pricings/ | 2026-08-13 | 2026-08-13T09:35:00+08:00 |
| speculation.microcap_moonshots | 本週 microcap thematic moonshot 合格 0 件 | microcap 100% single day quantum fusion nuclear AI August 2026 | Finviz/StockAnalysis gainers 螢幕 | 2026-08-13 | 2026-08-13T09:40:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 9 月上市 ≈$730–850B、Anthropic 續進 | OpenAI Anthropic IPO timing valuation 2026 | https://cryptobriefing.com/openai-ipo-filing-trillion-valuation/ | 2026-07-28 | 2026-08-13T09:35:00+08:00 |
| speculation.insider_form4 | 過去 14 日 AI/領導股合格 Form 4 賣壓 cluster 0 件 | AI leadership insider Form 4 sale July 30 August 13 2026 SEC | openinsider/secform4/SEC EDGAR 螢幕 | 2026-08-13 | 2026-08-13T09:40:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.54 | Cboe equity put call ratio August 2026 | https://www.thetrading.tools/put-call-ratio | 2026-08-07 | 2026-08-13T09:35:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 記錄高 ≈$198B | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-07-23 | 2026-08-13T09:35:00+08:00 |
| structural.us_single_stock_etf | 08-11 新發 6 檔單股 2x 槓桿 ETF（Leverage Shares／Tradr） | single-stock leveraged ETF launch August 11 2026 Leverage Shares Tradr | https://www.globenewswire.com/news-release/2026/08/11/3342794/0/en/leverage-shares-by-themes-launches-three-new-2x-etfs-targeting-ai-infrastructure-and-connectivity-leaders.html | 2026-08-11 | 2026-08-13T09:35:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量 ≈65%（Cboe Q2 2026） | 0DTE SPX options share Cboe Q2 2026 65% | https://ca.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4768656 | 2026-07-31 | 2026-08-13T09:35:00+08:00 |
| structural.options_volume | OCC 6 月總量 16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report | 2026-07-02 | 2026-08-13T09:35:00+08:00 |
| structural.cross_asset_derivatives | SKEW 135.59、VIX 15.28、MOVE 74.67 | VIX SKEW MOVE bond volatility August 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-10-2026-spx-skew-collapses-on-upside-chasing | 2026-08-11 | 2026-08-13T09:35:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt $1.502T、+51.5% YoY（交叉引用 D4） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-13T09:35:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B 貸款被迫調高利差 +100–125bp＋covenant | CoreWeave 2.6 billion loan spread covenant August 2026 | https://www.stocktitan.net/news/CRWV/core-weave-closes-2-6-billion-loan-facility-expanding-financing-gwhngwnf0jt5.html | 2026-07-29 | 2026-08-13T09:35:00+08:00 |

## 本次分數存檔
```json
{
  "date": "2026-08-13",
  "iso_week": "2026-W33",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "valuation": 78,
  "breadth": 30,
  "speculation": 55,
  "retail": 53,
  "monetary": 76,
  "structural": 78,
  "total": 64,
  "tier": "警戒",
  "regime": "分歧",
  "trigger_state": "未擊發",
  "trigger_reasons": [],
  "monetary_side": "自滿側",
  "hy_oas_widening_streak": 1,
  "sp500_dev200_pct": 9.67
}
```

本報告為相對風險溫度計，非擇時訊號。

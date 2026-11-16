# 2026-08-06 市場泡沫風險評估報告
> 報告日期：2026-08-06；執行日：2026-08-06 Asia/Taipei；ISO 週次：2026-W32；前次基準：report-2026-08-03（3天前）

**總評**：總分 64【警戒】（Δ 0）；扳機狀態：未擊發；最貼近錨點：1997 早期建設（65%）。

## §1 六維度風險條圖
| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▱▱▱ | 78 | 77 | +1 |
| 市場廣度 | ▰▰▰▱▱▱▱▱▱▱ | 30 | 30 | 0 |
| 投機行為 | ▰▰▰▰▰▱▱▱▱▱ | 57 | 57 | 0 |
| 散戶情緒 | ▰▰▰▰▰▱▱▱▱▱ | 52 | 47 | +5 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▰▱▱▱ | 76 | 76 | 0 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 78 | 78 | 0 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **64【警戒】** | 64 | 0 |

## §2 歷史錨點相似度
| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1973/1 Nifty Fifty 頂 | 15% | ▰▱▱▱▱▱▱▱▱▱ |  |
| 1997 早期建設 | 65% | ▰▰▰▰▰▰▱▱▱▱ | ◀ 最貼近 |
| 1998 LTCM 衝擊 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 60% | ▰▰▰▰▰▰▱▱▱▱ |  |
| 2000/3 頂點 | 15% | ▰▱▱▱▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 50% | ▰▰▰▰▰▱▱▱▱▱ |  |

## §3 三角訊號
| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,723.55 | ▲ +1.62%（前次 ≈7,600.5） |
| WTI 原油 | $81.96 /bbl | 持平 0%（無新觀測，前次 ≈$81.96） |
| 10Y Treasury | 4.63% | ▼ -7 bps（前次 ≈4.70%） |

**三者狀態**：出現分歧（10Y 反向下行）——三者本次方向為股市 ▲、WTI 持平、10Y ▼，出現 ▲/▼ 混合，依格局判定規則屬「出現分歧」；股市延伸上行而 10Y 殖利率反向下行（殖利率回落）是反向重定價的一腿。S&P `dev200_pct` +9.71%（逼近但未達 +10% 拉伸門檻），未升為同向偏高。公開信用利差自滿（HY 2.73%／IG 0.78% 史窄）與 AI 雲端信用重定價、債市波動轉升並存，須分開判讀。
- 股市：≈7,723.55（S&P 500，2026-08-05 收）；較前次 ▲ +1.62%（前次 ≈7,600.5）；距 200 日均線 +9.71%、距 52 週均線 +11.32%——月初科技股走高使價格延伸自前次（+6.63%）續升，逼近 +10% 拉伸門檻。
- WTI 原油：≈$81.96/bbl（DCOILWTICO，2026-08-03，無新觀測）；較前次 持平 0%（前次 ≈$81.96）。
- 10Y 殖利率：4.63%（DGS10，2026-08-04）；較前次 ▼ -7 bps（前次 ≈4.70%）；主要驅動：三腿視窗不一致（driver=unknown，ΔT10YIE 取自較新視窗）。
**格局轉變**：前次格局＝穩定共存（讀自 report-2026-08-03 的 `regime`）→ 本次格局＝分歧；三者由前次的股市小幅上行、WTI／10Y 無新觀測（穩定共存），轉為本次股市延伸上行、10Y 殖利率反向下行的 ▲/▼ 混合，格局轉為分歧。
**10Y 成因拆解**：拆的是週變動（bps）、非水位（`ΔDGS10 ≈ ΔDFII10 + ΔT10YIE`）；三腿視窗不一致——`decomposition.driver=unknown`（ΔT10YIE 取自 2026-08-05 新觀測、DGS10／DFII10 為 2026-08-04，恆等式不跨視窗成立），判定 不可判（視窗不一致）；三腿實際 signed 週變動如下：
- ΔDGS10 名目殖利率週變動：-7 bps
- ΔDFII10 實質殖利率週變動：-3 bps
- ΔT10YIE 損益平衡通膨週變動：-5 bps
- 判定：不可判（視窗不一致）
**扳機鏈**：A 通膨鏈（油 → 通膨預期 → Fed 受限 → refinancing 成本）本週未加速——WTI 持平（≈$81.96，無新觀測）、實現通膨仍高但通膨預期回落：[monetary.cpi_yoy] CPIAUCSL yoy_pct=3.46 data_date=2026-06-01（6 月）、5y5y forward [monetary.t5yifr] T5YIFR latest=2.26 delta_bps=-5 data_date=2026-08-05（週 Δ -5 bps）；FOMC 7/29 以 9-3 鷹派持平、CME FedWatch 9 月 ≈62% 定價分歧——通膨預期本週回落使 Fed put 邊際可得性略升，油價端無新推力，本鏈未加速。無當期電價／能源瓶頸新報導。B 槓桿鏈（衝擊：財政風險再定價 → NBFI 去槓桿 → margin spiral → 國債市場失序 → 官方市場功能回應；BIS AER 2026 Ch II 傳導鏈，2025-04 swap-spread unwind 為原型）乾柴堆積、衝擊節點壓力初現但未點火——衝擊節點：10Y 期限溢價 THREEFYTP10 ≈0.8681%（Kim-Wright 三因子模型、序列自身 trailing ≈7d +3 bps、溫和上行，未達 +15 bps 初啟門檻），且美債標售需求本週明顯轉弱（5Y 連續第 14 次 tail、bid-to-cover 為 2022-09 以來最差、7Y tail 0.8bp，2026-07-27／28）＝財政供給壓力事件證據；NBFI 節點：script `cftc_lev_funds`／`move_index`／`ofr_repo` 本次 fetch_failed，WebSearch 顯示 MOVE ≈74–75（絕對水位仍低）惟本週債市波動明顯轉升（VIXTLT 升至 68th 分位、TLT 1M skew 創 GFC 以來高），無 7 日窗內基差交易新平倉具名事件；官方回應節點：`repo_stress` SOFR−IORB +1 bps、SOFR99−IORB +9 bps、SRF 動用 ≈$0（無失序）。real-rate 主導的異常 10Y 上行本週不存在（ΔDGS10 -7 bps、殖利率反而回落）。惟 AI 雲端信用本週續重定價（CoreWeave 5Y CDS ≈855bp、$2.6B Anthropic 掛鉤貸款 07-29 調高票息、Oracle 5Y CDS ≈215bp 創高）屬單一發行人／結構化層級的後期訊號，尚未外溢至國債市場層級；本鏈證據 best-effort。
**扳機理由**：none
**結論**：扳機狀態：未擊發——本週無任一 contract 扳機理由成立：HY OAS 週 Δ -5 bps（未走闊、streak 歸零）、10Y driver≠breakeven（且殖利率回落）、期限溢價週 +3 bps 未達 +15 bps 初啟門檻且 funding 併發條件未滿足；私募信貸端最近事件（Blue Owl OCIC/OTIC 5% 上限撥付 2026-07-02）已落 30 日窗外，本週無新 gate proration / breach、無多基金 net inflow→outflow flip。三者配置歷史意義：估值＋槓桿＝崩跌位能，融資緊縮＝時點扳機；本週公開信用利差回到極度自滿（HY 2.73%／IG 0.78% 史窄）、非銀融資扳機未擊發，屬「froth 自滿而扳機未擊發」的組態，惟債市波動轉升、美債標售轉弱與 AI 雲端信用重定價（CoreWeave CDS ≈855bp、$2.6B 貸款調高票息）為後期側新增壓力，最須盯其是否外溢至公開利差與國債市場層級。

## 六維度評分

### 1. 估值溢價 — 78（weight 22%，Δ +1）
- **S&P 500 trailing P/E** ≈**29.74**（2026-08-05，https://www.multpl.com/s-p-500-pe-ratio，source_ids=valuation.sp500_pe_cape）——遠高於長期中位（≈16–19），實現盈餘基礎上市場歷史性偏貴、且較前次（28.84）續升。
- **Shiller CAPE** ≈**42.19**（2026-08-05，https://www.multpl.com/shiller-pe，source_ids=valuation.sp500_pe_cape）——為 2000-08 以來最高、遠高於長均 ≈32.4，較前次 40.91 續升。
- **Excess CAPE Yield（ECY）** ≈**-0.03%**（`1/42.19 − 2.40/100`，derived 自 CAPE **42.19**（2026-08-05）與 DFII10 2.40%（2026-08-04），source_ids=valuation.sp500_pe_cape）——轉負，屬 1929／2000 級別股相對債極貴訊號（confirmation，不主計分）。
- **Mag 7 加權 P/E**：Mag 7（≈33% 指數權重）對指數溢價壓縮至近十年最低（Mag 7 ≈**29x** vs 指數 ≈25.6x）（2026-07-20，https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026，source_ids=valuation.mag7_multiples）——絕對水位仍高但相對溢價續收斂（stock-of-state 沿用），屬緩和面。
- **價格趨勢偏離（Farrell #1/#2/#4）** S&P 距 200 日均線 **+9.71%**、距 52 週均線 +11.32%（`sp500_trend`，2026-08-05，FRED SP500，source_ids=valuation.sp500_trend）——價格延伸自前次 +6.63% 明顯拉伸、逼近 +10% 拉伸門檻，與 P/E／CAPE 互補、不重複計分。
- **AI capex 現實檢核**：hyperscaler 2026 capex 續上修——MSFT ≈$190B、AWS 上修至 ≈$220B、Alphabet $195–205B、Meta $130–145B，四家合計 ≈**$725B**（Q2 財報後仍上修，Alphabet 上修觸發 -7% 賣壓）（2026-07-28，https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html，source_ids=ai.hyperscaler_capex）——基本面敘事仍撐估值，惟回本未現、市場對 capex 上修轉為懲罰。
- **AI compute 供需現實檢核**：HBM3e 2026 合約 +≈20%、DRAM/NAND 合約價續漲、H200 租金中位 ≈**$4.39/hr**（+25% YoY）、HBM／CoWoS 缺口延至 1H2027（2026-08-01，https://jarvislabs.ai/blog/h200-price，source_ids=ai.compute_supply_demand）——供給仍緊、被需求吸收（非過剩），未取得利用率轉弱證據，此渠道未推升估值風險。
- **AI 營收對 capex 缺口現實檢核**：AI 終端年化營收（Anthropic ≈$47B＋OpenAI ≈$25B）vs 年化 capex ≈**$725B**（分母：top-4＋Oracle）（2026-06-15，https://epoch.ai/data-insights/anthropic-openai-revenue，source_ids=ai.revenue_capex_gap）——量級缺口仍逾 10× 且 capex 續升，回本假設後移，屬估值風險上修的質化依據（缺口未收斂）。
- **Hyperscaler 融資結構（capex vs FCF / 發債）**：quarterly_state——top-5 capex 已超越 FCF、續靠外部融資，2026 發債規模擴至 ≈**$182B**（vs 前次 $159B），另 >$120B 資料中心資產經表外 SPV 移出（2026-07-24，https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure，source_ids=ai.hyperscaler_financing_mix）——capex 愈靠發債與表外結構支撐、同份 guidance 脆弱性上升（BIS Bulletin 120，confirmation，不主計分；event_scan 本窗無具名新交易）。
- **AI 信用定價分歧（equity-vs-credit schism）**：AI 雲端／基建發行人信用本週續惡化——CoreWeave 5Y CDS ≈**855bp**（隱含 ≈50% 違約）、其 $2.6B 槓桿貸款利差爆走 +125bp（投資人要求 covenant）、Oracle 5Y CDS ≈215bp 創高（2026-08-03，https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm，source_ids=valuation.ai_credit_schism）——信貸端重定價而股價未跟＝後期訊號續升溫（confirmation，不主計分；缺值不調分）。
- **backlog 重複計算風險（RPO double-counting）**：Microsoft 商用 RPO ≈**$678B**（+84% YoY），約 **32%** 繫於單一客戶（OpenAI）；同一 OpenAI／Oracle 承諾被多家供應商同時入帳（2026-07-30，https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/，source_ids=ai.customer_concentration_rpo）——營收品質訊號：市場以各家 backlog 加總定價成長，可支付的終端現金流只有一份（confirmation，不主計分；缺值不調分）。
- **TP-upgrade phase signal**：本季（Q3 2026）具名賣方升評屬 **EPS-driven**——Morgan Stanley NVDA 目標 $**285**→$**288**、Overweight、由 AI 運算需求（EPS）驅動、目標 PE 未擴張（2026-07-13，https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044，source_ids=valuation.analyst_tp_decomposition）——升評由 E 而非 multiple 主導、同季未見多檔 multiple-driven 重定價，屬相對緩和訊號（confirmation，不主計分）。
- **折舊年限變動（盈餘品質）**：過去 30 日無新 10-K／10-Q 折舊年限或殘值假設變更披露（Amazon 6→5 年為 2025 舊事、窗外）（✗ NOT DISCLOSED，source_ids=ai.depreciation_life，不納入計分）。
- **資本週期階段**：供給側（資料中心容量）呈停滯訊號（30–50% 2026 美國容量恐延後／取消）、需求側 token／capex 仍熱，惟 event_scan 無窗內具日期之新進入者／取消事件、quarterly_state 供需增速證據不足，本次不判定週期階段（✗ NOT DISCLOSED，source_ids=ai.capital_cycle，不納入計分）。
**結論**：分數自 77 升至 **78**（rubric 高位）。CAPE 42.19（2000 以來最高）、P/E 29.74、趨勢偏離自 +6.63% 拉伸至 +9.71%（逼近 +10% 門檻）、ECY 轉負、AI 信用重定價續惡化（CoreWeave CDS ≈855bp、貸款 +125bp）、RPO 集中度風險具體披露——升溫面明顯，僅 Mag7 相對溢價壓縮至近十年低為緩和面，淨評較前次微升 1 分。

### 2. 市場廣度 — 30（weight 13%，Δ 0）
- **RSP（等權）vs SPY（市值權）YTD**：RSP 等權總報酬 YTD +**14.26%** 對 SPY 市值權 +13.71%、領先幅度收斂至 ≈0.55 pp（2026-08-03，https://www.financecharts.com/etfs/SPY/performance/total-return，source_ids=breadth.rsp_spy）——等權仍略領先但領先幅度較年中收斂，廣度驅動的超額報酬轉淡。
- **Top-10 集中度**：≈**41%**（歷史高位／再創高區間）（2026-07-02，https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/，source_ids=breadth.top10_concentration）——遠高於長均 ≈25%、處歷史高位（結構性狹窄）。
- **Advance/Decline 與新高/新低（proxy）**：≈**64%** S&P 500 成分股在 50 日均線上（週內一度觸 70%、為 1 月以來首見）、A/D 線 7 月創新高，惟 McClellan Oscillator 已連約兩週為負（動能轉緩）（2026-08-03，https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/，source_ids=breadth.advance_decline）——參與度較前次改善，但動能指標轉負屬輕度警訊。
**結論**：分數維持 **30**（rubric 21–40 偏健康端）。50 日均線上比例升至 ≈64%、A/D 創高為改善面，與等權領先收斂、Top-10 ≈41% 歷史高位、McClellan 轉負相抵——正負相抵，淨評與前次持平。

### 3. 投機行為 — 57（weight 18%，Δ 0）
- **+AI 改名／SPAC**：本週（07-30–08-06）+AI 改名合格 **0** 件（2026-08-06 螢幕；在窗 SPAC 屬一般 IPO／併購流、非投機 +AI 改名；Azio EVTV→AZIO 為 07-13、窗外）——✓ SEARCH-VERIFIED（0 件）（source_ids=speculation.ai_rename_spac）。
- **IPO 熱度**：本週為密集定價週（≈**21** 檔跨週定價，8/3–8/6），與 2026 YTD ≈$251B／86 檔一致，惟無明顯 blowout 首日漲幅（2026-08-04，https://www.renaissancecapital.com/IPO-Center/Pricings，source_ids=speculation.ipo_heat）——一級市場發行量偏熱、aftermarket 體感中性。
- **Microcap thematic moonshots**：本週 microcap thematic moonshot 合格 **0** 件（2026-08-06 螢幕；<$1B 市值、單日 ≥100% 或 2–3 日 ≥50%、堆疊 2+ 熱主題＋弱基本面；週最大漲幅為 MSFT／AMZN 財報大型股，SATS +75% 為 08-26 未來/窗外）——✓ SEARCH-VERIFIED（0 件）（source_ids=speculation.microcap_moonshots）。
- **Upcoming AI mega-IPO pipeline**：OpenAI 目標 ≈$**1**T IPO（惟傳可能延至 2027）、Anthropic（≈$965B 估值）續進 IPO 程序（2026-07-28，https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground，source_ids=speculation.upcoming_ai_ipos）——30 日內具名巨型 AI IPO pipeline 仍活躍、流動性抽離風險（惟時點轉趨保守）。
- **Insider selling clusters**：14 日內（07-23–08-06）出現合格 Form 4 cluster——Snowflake（SNOW）董事 Dageville 07-29 售 50,000 股 ≈$**14.0**M（@$280）、Tempus AI（TEM）董事長兼 CEO Lefkofsky 07-28 售 250,000 股（2026-07-29，https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1640147&type=4，source_ids=speculation.insider_form4）——✓ SEARCH-VERIFIED（非零），AI 領導股內部人賣壓集中（前次 CoreWeave Intrator 07-21 已落窗外）。
- **Cboe equity-only put/call**：≈**0.55**（2026-08-03，https://ycharts.com/indicators/cboe_equity_put_call_ratio，source_ids=speculation.equity_put_call）——較前次 0.63 更偏 call、未破 0.50 極端（confirmation，不主計分）。
**結論**：分數維持 **57**（rubric 41–60「投機升溫」）。IPO 定價週偏熱、內部人賣壓 cluster 續現（SNOW／TEM）、put/call 降至 0.55 為升溫面；+AI 改名／microcap moonshot 均 0、AI 巨型 IPO 時點轉保守為抑制面——升溫與抑制相抵，淨評與前次持平。

### 4. 散戶情緒 — 52（weight 12%，Δ +5）
- **CNN Fear & Greed**：≈**58「Greed」**（2026-08-05，https://www.cnn.com/markets/fear-and-greed，source_ids=retail.fear_greed）——由前次 ≈39「Fear」翻升入 Greed 區、Dow 8/5 創高，散戶風險偏好明顯轉升。
- **Margin Debt**：6 月 **$1.502T（記錄高）、YoY +51.5%**（2026-07-20，https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026，source_ids=retail.margin_debt）——月頻 stock-of-state（7 月數據約 8/20 才發布，沿用 6 月）；YoY +**51.5%** 仍屬 1999／2007／2021 頂部級別警訊。
- **AAII 散戶調查**：Bear 42.1%／Neutral 26.9%／Bull **31.0%**（2026-07-30，https://www.aaii.com/sentimentsurvey，source_ids=retail.aaii）——本週無可稽核的新一期數字，沿用最近一期；多方低於長均 37.5%、空方偏高，散戶調查端仍偏空、為 F&G 轉貪的反向制衡。
- **家庭持股佔金融資產比**：**45.76%**（`BOGZ1FL153064486Q`，2026-01-01 資料日／2026-Q1，FRED BOGZ1FL153064486Q，source_ids=retail.household_equity_allocation）——歷史高位、後續加碼空間有限（Farrell #5，季頻沿用、不計週 Δ）。
- **社群情緒代理**：本週（7 日窗）出現具名迷因軋空——Wendy's（WEN，≈44% 空頭部位、WSB「Save Wendy's」、8/7 財報為催化）為主軸，另 DORK 籃子（DNUT／OPEN／RKLB／KSS）仍受討論（2026-08-04，https://finance.yahoo.com/markets/stocks/articles/reddit-wants-save-wendy-inside-161925726.html，source_ids=retail.social_sentiment）——✓ SEARCH-VERIFIED（非零），具名散戶軋空活動重現、froth 訊號。
- **NAAIM Exposure Index**：本次無當期公開值——NAAIM 自 2026-08-01 改採訂閱制，公開來源最新僅停於 79.70（07-29），本週無可用新值（✗ NOT DISCLOSED，source_ids=retail.naaim，不納入計分；其缺值不調降主分）。
**結論**：分數自 47 升至 **52**（rubric 41–60，F&G Greed 55–75 帶）。CNN F&G 由 Fear（39）翻升至 Greed（58）、WEN 具名軋空重現、margin debt 續創高（YoY +51.5%）為升溫主因；AAII 多方 31% 仍偏空、NAAIM 公開值停更為制衡，淨評較前次升 5 分。

### 5. 貨幣與信貸環境 — 76（weight 20%，Δ 0）
- **Fed funds rate**：目標區間 **3.50–3.75%**（`DFEDTARU` 3.75%／`DFEDTARL` 3.50%，2026-08-05，FRED DFEDTARU/DFEDTARL，source_ids=monetary.fed_funds）——FOMC 7/29 以 9-3 維持不變。
- **市場隱含路徑（CME FedWatch，best-effort）**：FOMC 7/29 鷹派持平（9-3 票），CME FedWatch 9/16 會議定價 ≈**62%** 會有 25bp 動作、但方向（降/升）市場敘述分歧（2026-08-04，https://growbeansprout.com/tools/fedwatch，source_ids=monetary.fedwatch）——Fed 未明確轉鴿、寬鬆空間受通膨制約（缺值不調分）。
- **Realized inflation vs expectations**：CPI YoY **3.46%**（`CPIAUCSL`，2026-06-01，FRED CPIAUCSL，source_ids=monetary.cpi_yoy）仍高於 2% 目標、5y5y forward **2.26%**（`T5YIFR`，2026-08-05，週 Δ -5 bps，FRED T5YIFR，source_ids=monetary.t5yifr）本週回落——通膨黏著但預期端邊際回落，Fed 約束略鬆。
- **10Y 期限溢價（term premium）**：`THREEFYTP10` **0.8681%**（2026-07-31，Kim-Wright 三因子模型，序列自身 trailing ≈7d +3 bps，FRED THREEFYTP10，source_ids=monetary.term_premium）——財政風險再定價溫和上行、未達 +15 bps 初啟門檻。
- **repo 資金壓力（SOFR−IORB）與 SRF 動用**：SOFR **3.66%**、IORB 3.65%、SOFR−IORB **+1 bps**；SOFR99 3.74%、SOFR99−IORB +9 bps；SRF/RPONTTLD 動用 ≈$0.001B（2026-08-04／05，FRED SOFR/SOFR99/IORB/RPONTTLD，source_ids=monetary.repo_stress_srf）——secured-funding 無壓力、SRF 未實質動用。
- **美債標售需求（auction，best-effort）**：過去 14 日在窗標售呈兩極——5Y（$70B）連續第 14 次 tail、bid-to-cover 為 2022-09 以來最差；7Y tail 0.8bp（均值 0.3bp）偏弱；2Y 強勁（2026-07-28，https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026，source_ids=monetary.treasury_auctions）——belly/長端需求轉弱＝財政供給壓力事件證據，餵入 §3 槓桿鏈衝擊節點（confirmation）。
- **HY OAS**：**2.73%**（`BAMLH0A0HYM2`，2026-08-04，週 Δ -5 bps，FRED BAMLH0A0HYM2，source_ids=monetary.hy_oas）——接近循環低、極窄、續收窄、自滿側；未走闊（streak 歸零）。
- **IG OAS**：**0.78%**（`BAMLC0A0CM`，2026-08-04，週 Δ 0 bp，FRED BAMLC0A0CM，source_ids=monetary.ig_oas）——史窄、信用自滿。
- **10Y nominal 週變動拆解**：ΔDGS10 -7 bps；`DGS10` **4.63%**（2026-08-04，FRED DGS10，source_ids=monetary.dgs10）、`DFII10` **2.40%**（2026-08-04，FRED DFII10，source_ids=monetary.dfii10）、`T10YIE` **2.22%**（2026-08-05，FRED T10YIE，source_ids=monetary.t10yie）——三腿視窗不一致（driver=unknown，詳 §3），殖利率本週回落。
- **WTI 原油**：**$81.96**/bbl（`DCOILWTICO`，2026-08-03，無新觀測，FRED DCOILWTICO，source_ids=monetary.wti）——持平，A 通膨鏈油價端無新推力。
- **Fed balance sheet**：≈$6.74T（原始 **6,738,190** 百萬美元，2026-07-29，無新觀測，FRED WALCL，source_ids=monetary.walcl）——量化緊縮步調持平。
- **全球央行流動性（ECB）**：ECB ≈€5.94T（原始 **5,941,248** 百萬歐元，2026-07-31，FRED ECBASSETSW，source_ids=monetary.ecb_boj）——持平。
- **全球央行流動性（BOJ）**：BOJ ≈¥644.30T（原始 **6,442,957** 億日圓，2026-07-01，FRED JPNASSETS，source_ids=monetary.ecb_boj）——持平。
- **PBoC 流動性操作**：人行 7/29–8/3 連日隔夜逆回購淨投放（合計 ≈¥**2.1**T 平滑月末），另 7/24 MLF 淨投放 ≈¥100B（2026-07-24，https://www.investing.com/news/economy-news/chinas-pboc-to-conduct-overnight-reverse-repos-inject-a-total-of-21-trillion-yuan-4810853，source_ids=monetary.pboc）——中國端流動性偏寬、屬季節性微調（confirmation）。
- **私募信貸贖回壓力（event-driven）**：最近事件為 Blue Owl OCIC/OTIC 維持 5% 季度上限並比例撥付（2026-07-02、落 30 日窗外）；過去 30 日（07-07–08-06）無新 gate proration / breach、無多基金 net inflow→outflow flip（✗ NOT DISCLOSED，source_ids=monetary.private_credit_liquidity，不納入計分）。
**結論**：自滿側；公開信用利差回到極度自滿（HY 2.73%／IG 0.78% 史窄、皆續收窄），非銀融資扳機未擊發、本週無新 gate / breach，屬「self-satisfied froth 而扳機未擊發」的自滿側組態；惟美債標售轉弱、債市波動轉升與 AI 雲端信用重定價為後期側新增壓力，尚未點燃任一 contract 扳機，分數維持 **76**。

### 6. 結構性槓桿 — 78（weight 15%，Δ 0）
- **US 槓桿 ETF AUM**：美國槓桿 ETF 總 AUM 創高 ≈$**198**B（TQQQ ≈$40B、SOXL ≈$34B 領先）（2026-07-23，https://cryptobriefing.com/leveraged-etfs-record-198b-aum/，source_ids=structural.leveraged_etf_aum）——水位維持記錄高。
- **US 單股槓桿 ETF 核准／發行（近 30 日）**：Leverage Shares/Themes 07-07 起推 6 檔 2x 單股槓桿 ETF（GOOGL／AMZN／META／AAPL），並於 07-30 推 ELOL（TSLA＋SpaceX）（2026-07-30，https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html，source_ids=structural.us_single_stock_etf）——單股槓桿產品續擴散（30 日窗內在案發行）。
- **全球（非美）槓桿產品核准（本週）**：韓國反收緊——FSC 07-16 起暫停新單股槓桿 ETF/ETN 上市、現金保證金 08-05 起調高三倍，新發行停滯；台／日／歐 07-30–08-06 無新單股槓桿／反向 ETF 英文披露、「全球槓桿擴散訊號」本週未觸發，**本週擴散訊號未觸發**（✗ NOT DISCLOSED，source_ids=structural.global_leveraged_approvals，不納入計分）。
- **0DTE 佔 SPX 期權量**：≈**65**%（Cboe Q2 2026，資料月 2026-05，https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641，source_ids=structural.zero_dte）——持續 >55% 高檔（資料日 2026-05-31）。
- **Options 總量（OCC 月報）**：OCC 6 月總量 **16.0** 億口（1,603,491,559 口）（2026-07-02，https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report，source_ids=structural.options_volume）——衍生品投機量續處高檔（stock-of-state 沿用；7 月報 8/4 已發布惟總量數字本次未能取得）。
- **跨資產／相關性確認**：SKEW ≈**139.96**、VIX ≈16.9（term structure contango、股票端平靜），惟本週股債脫鉤——利率/債券波動急升（VIXTLT 16th→68th 分位、TLT 1M skew 創 GFC 以來高）（2026-08-03，https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher，source_ids=structural.cross_asset_derivatives）——股票端尾端避險穩定、風險本週移轉至利率/債市（confirmation）。
- **Margin debt / 市值 交叉檢核**：6 月 $1.502T、YoY +**51.5**%（2026-07-20，見 D4，https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026，source_ids=structural.margin_debt_crosscheck）——確認零售槓桿頂部級別（confirmation，不在此重複計分）。
- **AI 基礎設施債務／vendor-financing loops**：本窗新披露——CoreWeave 07-29 將 $**2.6**B 槓桿定期貸款（掛鉤 Anthropic／Jane Street 合約）票息調高（弱需求訊號）；另 Oracle/xAI/Meta/CoreWeave >$120B 經 Pimco/BlackRock/Blue Owl 表外融資；Nebius $775M 擔保（07-17）（2026-07-29，https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic，source_ids=structural.ai_infrastructure_debt）——circular／vendor-financing 迴圈續強化、CoreWeave 須調高票息＝融資市場消化不良，結構性槓桿升溫因子。
- **銀行對 NBFI 放款**：≈$2.00T（原始 **2,004.99** 十億美元，2026-07-22，無新觀測，FRED LNFACBW027SBOG，source_ids=structural.nbfi_bank_loans）——bank–NBFI linkage 水位持平（confirmation，不主計分）。
- **美債基差交易槓桿（best-effort）**：script `cftc_lev_funds`／`move_index`／`ofr_repo` 本次 `fetch_failed`（CFTC/OCC 網域於本執行環境政策封鎖）；WebSearch 顯示 MOVE ≈74–75（絕對水位仍低）、本週債市波動轉升但無 7 日窗內具名基差交易平倉事件、槓桿基金淨部位無可稽核當期數字（✗ NOT DISCLOSED，source_ids=structural.treasury_basis_trade，不納入計分、不調 D6 分數）。
**結論**：分數維持 **78**（rubric 61–80）。0DTE 續 >55%、OCC 量高檔、槓桿 ETF AUM 創高、Leverage Shares 單股槓桿續擴散、AI 基建融資新披露升溫（CoreWeave $2.6B 貸款調高票息）＝結構性槓桿高檔；惟全球擴散未觸發（韓國反收緊）、基差交易無窗內具名新事件（MOVE ≈74–75）為抑制——升溫與抑制相抵，淨評與前次持平。

## 綜合分數

| 維度 | 權重 | 分數 | 加權分數 |
|---|---:|---:|---:|
| 估值溢價 | 22% | 78 | 17.16 |
| 市場廣度 | 13% | 30 | 3.90 |
| 投機行為 | 18% | 57 | 10.26 |
| 散戶情緒 | 12% | 52 | 6.24 |
| 貨幣與信貸環境 | 20% | 76 | 15.20 |
| 結構性槓桿 | 15% | 78 | 11.70 |
加權總分：64.46 → 64【警戒】

邊界帶：總分 64 距 警戒/高 邊界 ≤ 2 分，評分固有噪音約 ±2–3，等級判讀需保留餘地。

## 歷史泡沫週期對比

相似度計算：checklist v2

逐項對本次六維度分數、macro/current/prior state 與附錄證據重算命中；相似度 = 命中數 ÷ 特徵數 × 100，四捨五入到最近 5%。「無資料」不計入命中但仍在分母。

- 1973/1 Nifty Fifty 頂：命中 1/8 = 15%
- 1997 早期建設：命中 5/8 = 65%
- 1998 LTCM 衝擊：命中 2/8 = 25%
- 1999 晚期狂熱：命中 6/10 = 60%
- 2000/3 頂點：命中 1/8 = 15%
- 2021/12 Meme 頂：命中 4/8 = 50%

2000/3 高位回落條件：否

**1973/1 Nifty Fifty 頂 feature audit**
- 1973.1｜未命中｜source_ids=—｜估值溢價 78 < 80
- 1973.2｜未命中｜source_ids=—｜市場廣度 30 < 60
- 1973.3｜未命中｜source_ids=—｜CPI YoY 3.46% < 4%
- 1973.4｜未命中｜source_ids=—｜T5YIFR 週 Δ -5 bps < 0（通膨預期回落）
- 1973.5｜未命中｜source_ids=—｜WTI 週漲幅 0%（無新觀測）< +0.5%
- 1973.6｜未命中｜source_ids=—｜decomposition.driver=unknown ≠ breakeven（三腿視窗不一致）
- 1973.7｜未命中｜source_ids=—｜扳機狀態＝未擊發 < 初啟
- 1973.8｜命中｜source_ids=—｜散戶情緒 52 < 55
**1997 早期建設 feature audit**
- 1997.1｜未命中｜source_ids=—｜估值溢價 78 > 74（超出 40–74 區間）
- 1997.2｜命中｜source_ids=—｜市場廣度 30 < 45
- 1997.3｜未命中｜source_ids=—｜投機行為 57 ≥ 50
- 1997.4｜命中｜source_ids=ai.hyperscaler_capex｜hyperscaler 2026 capex 指引仍上修（合計 ≈$725B）
- 1997.5｜命中｜source_ids=—｜散戶情緒 52 < 55
- 1997.6｜未命中｜source_ids=—｜結構性槓桿 78 ≥ 50
- 1997.7｜命中｜source_ids=—｜HY OAS 2.73% < 4% 且週 Δ -5 bps ≤ 0（未走闊，all 成立）
- 1997.8｜命中｜source_ids=—｜扳機狀態＝未擊發
**1998 LTCM 衝擊 feature audit**
- 1998.1｜未命中｜source_ids=structural.cross_asset_derivatives｜HY 週 Δ -5 bps < +30；VIX ≈16.9 contango（無壓力事件）
- 1998.2｜未命中｜source_ids=—｜S&P chg +1.62% > −5%（未達回檔門檻）
- 1998.3｜無資料｜source_ids=—｜私募信貸與美債基差交易本次皆 ✗ NOT DISCLOSED（無成功事件證據）
- 1998.4｜未命中｜source_ids=monetary.fedwatch｜FOMC 7/29 鷹派持平、非轉鴿
- 1998.5｜命中｜source_ids=—｜估值溢價 78 ≥ 60
- 1998.6｜未命中｜source_ids=—｜扳機狀態＝未擊發 < 初啟
- 1998.7｜未命中｜source_ids=—｜市場廣度 Δ = 30 − 30 = 0 < +8
- 1998.8｜命中｜source_ids=—｜ΔT10YIE -5 bps ≤ 0（通膨預期非上行）
**1999 晚期狂熱 feature audit**
- 1999.1｜命中｜source_ids=—｜估值溢價 78 ≥ 75
- 1999.2｜命中｜source_ids=valuation.sp500_pe_cape｜CAPE 42.19 ≥ 38
- 1999.3｜未命中｜source_ids=—｜投機行為 57 < 60
- 1999.4｜未命中｜source_ids=speculation.microcap_moonshots,speculation.ipo_heat｜本週 moonshot 0；無營收 IPO 佔比未達偏高
- 1999.5｜未命中｜source_ids=—｜市場廣度 30 < 45（廣度健康、非轉窄）
- 1999.6｜命中｜source_ids=—｜D5 monetary_side＝自滿側 且 HY OAS 2.73% < 3.5%（all 成立）
- 1999.7｜命中｜source_ids=—｜結構性槓桿 78 ≥ 60
- 1999.8｜未命中｜source_ids=—｜散戶情緒 52 < 55
- 1999.9｜命中｜source_ids=speculation.upcoming_ai_ipos｜巨型 AI IPO pipeline 活躍（OpenAI ≈$1T、Anthropic 續進）
- 1999.10｜命中｜source_ids=—｜扳機狀態＝未擊發
**2000/3 頂點 feature audit**
- 2000.1｜未命中｜source_ids=—｜估值溢價 78 < 85
- 2000.2｜未命中｜source_ids=—｜扳機狀態＝未擊發 < 初啟
- 2000.3｜未命中｜source_ids=—｜市場廣度 30 < 60
- 2000.4｜未命中｜source_ids=—｜prior sp500_dev200_pct 6.63 < +10 使第一分支為否；current chg +1.62% > −5%
- 2000.5｜未命中｜source_ids=—｜投機行為 57 < 70
- 2000.6｜命中｜source_ids=speculation.insider_form4｜14 日內合格 Form 4 cluster：SNOW（Dageville 07-29 ≈$14.0M）、TEM（Lefkofsky 07-28）
- 2000.7｜未命中｜source_ids=—｜散戶情緒 52 < 65
- 2000.8｜未命中｜source_ids=monetary.fedwatch｜FedWatch 未定價明確緊縮（方向分歧）；10Y driver≠breakeven（且殖利率回落）
**2021/12 Meme 頂 feature audit**
- 2021.1｜未命中｜source_ids=—｜散戶情緒 52 < 65
- 2021.2｜命中｜source_ids=retail.social_sentiment｜本週具名社群軋空（WEN「Save Wendy's」、7 日窗內）
- 2021.3｜命中｜source_ids=—｜結構性槓桿 78 ≥ 65
- 2021.4｜命中｜source_ids=monetary.walcl,monetary.ecb_boj｜D5 76 ≥ 60 且自滿側、央行資產負債表可得（流動性氾濫，all 命中）
- 2021.5｜命中｜source_ids=retail.margin_debt｜margin debt YoY +51.5% ≥ +40%
- 2021.6｜未命中｜source_ids=speculation.microcap_moonshots｜本週 microcap moonshot 0 < 1
- 2021.7｜未命中｜source_ids=—｜市場廣度 30 < 50
- 2021.8｜未命中｜source_ids=—｜CPI YoY 3.46% < 4%（all 不成立）

**兩句解讀**：本週最貼近錨點仍為「1997 早期建設」（65%），1999 晚期狂熱（60%）緊追其後——當前組態是高估值（CAPE 42.19、估值溢價 78）＋極度自滿的公開信用（HY 2.73%／IG 0.78% 史窄、自滿側）＋窄領導但等權尚健康的廣度，且扳機狀態＝未擊發，最像 1997 早期建設向 1999 晚期狂熱過渡的中段。與 2000/3 頂點（15%）的關鍵分歧在於扳機未擊發、散戶未全面狂熱（F&G 58 Greed 但 AAII Bull 31% 仍偏空）、廣度未極窄——循環位置意涵：估值＋槓桿位能高企但時點扳機尚未點燃，屬「froth 續升、扳機待命」的中後段，且「扳機鏈 A 尚未驗證啟動」（1973.6 未命中、扳機理由無 breakeven_wti_up），最須盯 AI 雲端信用重定價（CoreWeave CDS ≈855bp、$2.6B 貸款調高票息）與美債標售轉弱是否外溢至公開利差、國債市場與私募信貸閘門。長期指數成長趨勢偏離（Dot-com ≈95%、1929 ≈110%、當前 AI 週期 ≈147%；RIA/Farrell）作跨期敘事錨、不進 checklist。

## 機構情緒對照

本次無新機構調查數據。（BofA FMS 為 7 月中發布、JPM 亦無本次新增；下次 FMS 約 8 月中。）背景參照：7 月 BofA FMS 現金水位 ≈3.6% AUM、觸及 <4% 的「賣出訊號」極端；NAAIM Exposure Index 自 2026-08-01 改訂閱制，公開最新值停於 79.70（07-29，主動經理人曝險中高、已自近高回落，Farrell #9，於 D4 作 confirmation cross-check、本節僅敘述不計分）。

## 本次新增訊號

比較基準：vs 前次（3天前）。

- **散戶情緒（D4）Δ +5**：CNN Fear & Greed 由 ≈39「Fear」翻升至 ≈58「Greed」（2026-08-05）、本週出現具名迷因軋空（Wendy's WEN「Save Wendy's」、≈44% 空頭部位、8/7 財報催化），margin debt 6 月續創高（$1.502T、YoY +51.5%）；AAII 多方仍僅 31%（偏空）、NAAIM 公開值停更為制衡，散戶 froth 明顯轉升、分數自 47 升至 52。
- **估值溢價（D1）Δ +1**：CAPE 升至 42.19（2000 以來最高）、P/E 29.74、趨勢偏離拉伸至 +9.71%（逼近 +10% 門檻）、ECY 轉負；AI 雲端信用重定價續惡化（CoreWeave 5Y CDS ≈855bp、$2.6B Anthropic 貸款利差 +125bp、Oracle CDS ≈215bp 創高）、Microsoft RPO ≈$678B 約 32% 繫 OpenAI（backlog 重複計算風險具體披露）——升溫面明顯，僅 Mag7 相對溢價壓縮為緩和，分數自 77 升至 78。
- **格局由「穩定共存」轉「分歧」**：本週股市延伸上行（+1.62%）、10Y 殖利率反向下行（-7 bps）、WTI 持平，出現 ▲/▼ 混合，格局判定為分歧（10Y 反向重定價）；`regime` 由前次穩定共存更新為分歧。
- **貨幣與信貸環境（D5，Δ 0，＝自滿側）**：公開信用利差回到極度自滿（HY 2.73%／IG 0.78% 史窄、續收窄），非銀融資扳機未擊發、無新 gate / breach；惟本週美債標售需求轉弱（5Y 連續第 14 次 tail、bid-to-cover 為 2022-09 以來最差）、債市波動明顯轉升（TLT 1M skew 創 GFC 以來高）屬後期側新增壓力，尚未達任一 contract 扳機門檻（term premium +3 bps、SOFR−IORB +1 bps），故 monetary_side 維持自滿側、分數持平。
- **投機行為（D3，Δ 0）**：內部人賣壓 cluster 由前次 CoreWeave（已落窗外）轉為 Snowflake（Dageville 07-29 ≈$14.0M）、Tempus AI（Lefkofsky 07-28）；IPO 定價週偏熱（≈21 檔）、put/call 降至 0.55；+AI 改名／microcap moonshot 均 0——升抑相抵、分數持平。
- **結構性槓桿（D6，Δ 0）**：AI 基建融資新披露升溫（CoreWeave $2.6B Anthropic 掛鉤貸款 07-29 調高票息＝融資消化不良）、US 單股槓桿續擴散（Leverage Shares 6 檔＋ELOL）；惟**全球（非美）槓桿擴散本週未觸發（韓國反收緊），本週擴散訊號未觸發**、基差交易無窗內具名新事件（MOVE ≈74–75），分數持平。
- **HY OAS 連續走闊 streak 歸零**：本次 HY OAS 週 Δ -5 bps（未走闊），依決定性公式 streak 歸 0——「HY 連續兩次走闊」初啟判準本次不成立。
- 其餘維度（廣度 30）分數與前次持平；總分 64【警戒】、Δ 0。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | S&P 500 收盤（sp500_trend latest） | 7,723.55 | FRED SP500（sp500_trend） | 2026-08-05 | 2026-08-06T09:20:00+08:00 |
| valuation.sp500_trend | S&P 500 距 200DMA 偏離（sp500_trend dev200_pct） | +9.71% | FRED SP500（sp500_trend） | 2026-08-05 | 2026-08-06T09:20:00+08:00 |
| valuation.sp500_trend | S&P 500 距 52 週均線偏離（sp500_trend dev52w_pct） | +11.32% | FRED SP500（sp500_trend） | 2026-08-05 | 2026-08-06T09:20:00+08:00 |
| retail.household_equity_allocation | 家庭持股佔金融資產比（BOGZ1FL153064486Q） | 45.76 | FRED BOGZ1FL153064486Q | 2026-01-01 | 2026-08-06T09:20:00+08:00 |
| monetary.fed_funds | Fed funds 上限（DFEDTARU） | 3.75% | FRED DFEDTARU | 2026-08-05 | 2026-08-06T09:20:00+08:00 |
| monetary.fed_funds | Fed funds 下限（DFEDTARL） | 3.50% | FRED DFEDTARL | 2026-08-05 | 2026-08-06T09:20:00+08:00 |
| monetary.hy_oas | HY OAS（BAMLH0A0HYM2） | 2.73% | FRED BAMLH0A0HYM2 | 2026-08-04 | 2026-08-06T09:20:00+08:00 |
| monetary.ig_oas | IG OAS（BAMLC0A0CM） | 0.78% | FRED BAMLC0A0CM | 2026-08-04 | 2026-08-06T09:20:00+08:00 |
| monetary.dgs10 | 10Y 名目殖利率（DGS10） | 4.63% | FRED DGS10 | 2026-08-04 | 2026-08-06T09:20:00+08:00 |
| monetary.dfii10 | 10Y 實質殖利率（DFII10） | 2.40% | FRED DFII10 | 2026-08-04 | 2026-08-06T09:20:00+08:00 |
| monetary.t10yie | 10Y breakeven（T10YIE） | 2.22% | FRED T10YIE | 2026-08-05 | 2026-08-06T09:20:00+08:00 |
| monetary.wti | WTI 原油（DCOILWTICO） | $81.96 | FRED DCOILWTICO | 2026-08-03 | 2026-08-06T09:20:00+08:00 |
| monetary.cpi_yoy | CPI YoY（CPIAUCSL yoy_pct） | 3.46% | FRED CPIAUCSL | 2026-06-01 | 2026-08-06T09:20:00+08:00 |
| monetary.t5yifr | 5y5y forward（T5YIFR latest） | 2.26% | FRED T5YIFR | 2026-08-05 | 2026-08-06T09:20:00+08:00 |
| monetary.term_premium | 10Y 期限溢價（THREEFYTP10） | 0.8681% | FRED THREEFYTP10 | 2026-07-31 | 2026-08-06T09:20:00+08:00 |
| monetary.repo_stress_srf | SOFR 隔夜擔保融資利率 | 3.66% | FRED SOFR | 2026-08-04 | 2026-08-06T09:20:00+08:00 |
| monetary.repo_stress_srf | SOFR99 99th 分位尾端利率 | 3.74% | FRED SOFR99 | 2026-08-04 | 2026-08-06T09:20:00+08:00 |
| monetary.repo_stress_srf | IORB 準備金餘額利率 | 3.65% | FRED IORB | 2026-08-06 | 2026-08-06T09:20:00+08:00 |
| monetary.repo_stress_srf | 隔夜 repo 操作量（RPONTTLD） | 0.001 | FRED RPONTTLD | 2026-08-05 | 2026-08-06T09:20:00+08:00 |
| monetary.walcl | Fed 資產負債表（WALCL） | 6,738,190 百萬美元（≈$6.74T） | FRED WALCL | 2026-07-29 | 2026-08-06T09:20:00+08:00 |
| monetary.ecb_boj | ECB 資產（ECBASSETSW） | 5,941,248 百萬歐元（≈€5.94T） | FRED ECBASSETSW | 2026-07-31 | 2026-08-06T09:20:00+08:00 |
| monetary.ecb_boj | BOJ 資產（JPNASSETS） | 6,442,957 億日圓（≈¥644.30T） | FRED JPNASSETS | 2026-07-01 | 2026-08-06T09:20:00+08:00 |
| structural.nbfi_bank_loans | 銀行對 NBFI 放款（LNFACBW027SBOG） | 2,004.99 十億美元（≈$2.00T） | FRED LNFACBW027SBOG | 2026-07-22 | 2026-08-06T09:20:00+08:00 |

### Coverage

| source_id | 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl/gurufocus [primary: SEARCH] | ✓ SEARCH-VERIFIED（P/E 29.74、CAPE 42.19 @08-05） |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E | SSGA/advisorperspectives [SEARCH]（stock-of-state 沿用） | ✓ SEARCH-VERIFIED（溢價壓縮、Mag7 ≈29x @07-20） |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（MS NVDA $288 EPS-driven @07-13） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500 派生） | ✓ API（dev200 +9.71%／dev52 +11.32%） |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧 | 信用市場 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（CoreWeave CDS ≈855bp、loan +125bp、Oracle CDS ≈215bp @08-03） |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | financecharts/247wallst [SEARCH] | ✓ SEARCH-VERIFIED（RSP +14.26% 領先 SPY +13.71% TR、領先收斂 @08-03） |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | P&I/財經媒體 [SEARCH] | ✓ SEARCH-VERIFIED（≈41%，歷史高位 @07-02） |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | StockCharts breadth [SEARCH] | ✓ SEARCH-VERIFIED（≈64% >50DMA、A/D 創高、McClellan 轉負 @08-03） |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（≈58 Greed @08-05） |
| retail.margin_debt | 散戶｜Margin Debt: FINRA | FINRA/Advisor Perspectives [SEARCH]（月頻 stock-of-state） | ✓ SEARCH-VERIFIED（$1.502T、+51.5% YoY、2026-06；7 月未發布沿用） |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（Bull 31.0%／Bear 42.1% @07-30，本週無新一期沿用） |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB/cashtag [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（WEN「Save Wendy's」軋空 @08-04，7 日窗內） |
| retail.household_equity_allocation | 散戶｜Household equity allocation | fetch_macro.py BOGZ1FL153064486Q | ✓ API（45.76% @2026-Q1） |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim/YCharts [primary: SEARCH]（best-effort） | ✗ NOT DISCLOSED（08-01 起訂閱制、無當期公開值；末公開 79.70 @07-29） |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM | 賣方調查 [SEARCH]（月頻，best-effort） | ✗ NOT DISCLOSED（7 月 FMS 早於前次基準、本次無新增） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED DFEDTARU/DFEDTARL | fetch_macro.py FRED API | ✓ API（3.75%/3.50% @08-05） |
| monetary.hy_oas | 貨幣｜High Yield OAS | fetch_macro.py FRED API | ✓ API（2.73% @08-04，Δ-5bps） |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | fetch_macro.py FRED API | ✓ API（0.78% @08-04，Δ 0） |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | fetch_macro.py FRED API | ✓ API（4.63% @08-04，Δ-7bps） |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield | fetch_macro.py FRED API | ✓ API（2.40% @08-04，Δ-3bps） |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | fetch_macro.py FRED API | ✓ API（2.22% @08-05，Δ-5bps） |
| monetary.wti | 貨幣｜WTI crude oil price | fetch_macro.py FRED API | ✓ API（$81.96 @08-03，無新觀測） |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED | fetch_macro.py FRED API（月頻） | ✓ API（3.46% @2026-06） |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | fetch_macro.py FRED API | ✓ API（2.26% @08-05，Δ-5bps） |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED | fetch_macro.py FRED API | ✓ API（0.8681% @07-31，+3bps trailing） |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py repo_stress | ✓ API（SOFR−IORB +1bps、SOFR99−IORB +9bps、SRF ≈$0 @08-04/05；SOFR/SOFR99/IORB/RPONTTLD 皆 ok） |
| monetary.treasury_auctions | 貨幣｜美債標售需求 | Reuters/Bloomberg recap [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（5Y 連 14 次 tail、BTC 2022-09 以來最差；7Y tail 0.8bp @07-28） |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（9 月 ≈62% 定價、方向分歧 @08-04） |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED WALCL | fetch_macro.py FRED API | ✓ API（$6.74T @07-29，無新觀測） |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | fetch_macro.py FRED API | ✓ API（€5.94T @07-31／¥644.30T @07-01） |
| monetary.pboc | 貨幣｜PBoC aggregate financing | investing/Yicai [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（逆回購 ≈¥2.1T、MLF 淨投放 ¥100B @07-24） |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]（best-effort） | ✗ NOT DISCLOSED（Blue Owl 5% 撥付 07-02 落窗外、30 日窗內無新事件） |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報 [SEARCH]（stock-of-state） | ✓ SEARCH-VERIFIED（合計 ≈$725B、仍上修 @07-28） |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic/OpenAI/Google [SEARCH]（best-effort） | ✗ NOT DISCLOSED（本季 Anthropic/OpenAI 無乾淨量化成長率） |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch/報導 [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Anthropic ≈$47B／OpenAI ≈$25B run-rate @06-15） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration | 財報電話 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（MSFT RPO $678B、≈32% 繫 OpenAI @07-30） |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce/jarvislabs [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（HBM/DRAM 緊、H200 租金 ≈$4.39/hr、缺口延至 1H2027 @08-01） |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構 | 季報/發債 [primary: SEARCH]（best-effort） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口 | 組合披露 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（年化 capex ≈$725B vs 終端營收 ≈$72B @06-15） |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K/10-Q [primary: SEARCH]（best-effort，30日） | ✗ NOT DISCLOSED（過去 30 日無新變更） |
| ai.capital_cycle | AI｜資本週期階段 | 供需增速+進出場事件 [SEARCH]（best-effort） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days +AI rename/SPAC | [SEARCH] | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | Renaissance/iposcoop [SEARCH] | ✓ SEARCH-VERIFIED（≈21 檔定價週、無 blowout 首日 @08-04） |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz/StockAnalysis [primary: SEARCH]（required 週螢幕） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | S-1/具名報導 [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（OpenAI ≈$1T、Anthropic 續進 @07-28） |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership | SEC EDGAR [primary: EDGAR]（required） | ✓ SEARCH-VERIFIED（cluster：SNOW Dageville 07-29 ≈$14.0M、TEM Lefkofsky 07-28） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe/YCharts [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（0.55 @08-03） |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing/etf.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（總 ≈$198B 創高 @07-23） |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | Leverage Shares/GlobeNewswire [SEARCH] | ✓ SEARCH-VERIFIED（6 檔 2x＋ELOL 發行 @07-30） |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX/TWSE/JPX/ESMA [SEARCH]（best-effort，7日） | ✗ NOT DISCLOSED（韓國反收緊、本週擴散訊號未觸發） |
| structural.zero_dte | 結構｜0DTE option volume | Cboe [SEARCH]（Cboe 403） | ✓ SEARCH-VERIFIED（≈65%，Cboe Q2 @2026-05） |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com [SEARCH] | ✓ SEARCH-VERIFIED（6 月 16.0 億口 @07-02；7 月報數字未取得） |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Cboe/Saxo [SEARCH] | ✓ SEARCH-VERIFIED（SKEW ≈139.96、VIX ≈16.9 contango、債市波動轉升 @08-03） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 D4（confirmation） | ✓ SEARCH-VERIFIED（$1.502T/+51.5% YoY，D4 引用不重複計分） |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]（best-effort，30日） | ✓ SEARCH-VERIFIED（CoreWeave $2.6B Anthropic 貸款調高票息 @07-29；Nebius $775M @07-17） |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | fetch_macro.py FRED API | ✓ API（$2.00T @07-22，無新觀測） |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | script→WebSearch [primary: script]（best-effort） | ✗ NOT DISCLOSED（cftc/move/ofr script fetch_failed，MOVE ≈74–75、無 7 日窗內具名新事件） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 29.74 | S&P 500 trailing P/E August 5 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio | 2026-08-05 | 2026-08-06T09:20:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 42.19 | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe | 2026-08-05 | 2026-08-06T09:20:00+08:00 |
| valuation.mag7_multiples | Mag 7 對指數溢價壓縮、Mag7 ≈29x vs 指數 ≈25.6x | Magnificent 7 valuation premium lowest decade 2026 | https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-20-july-2026 | 2026-07-20 | 2026-08-06T09:20:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標 $285→$288、EPS-driven | Morgan Stanley NVDA target 288 July 2026 AI demand | https://www.investing.com/news/analyst-ratings/morgan-stanley-raises-nvidia-stock-price-target-to-288-on-ai-demand-93CH-4703044 | 2026-07-13 | 2026-08-06T09:20:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS ≈855bp、$2.6B 貸款利差 +125bp、Oracle CDS ≈215bp | CoreWeave CDS spread blows out 125 covenants Oracle August 2026 | https://www.techtimes.com/articles/322772/20260803/ai-loan-investors-demand-covenants-after-coreweave-spread-blows-out-125-points.htm | 2026-08-03 | 2026-08-06T09:20:00+08:00 |
| breadth.rsp_spy | RSP 等權總報酬 YTD +14.26% 領先 SPY +13.71% | RSP vs SPY equal weight total return YTD August 2026 | https://www.financecharts.com/etfs/SPY/performance/total-return | 2026-08-03 | 2026-08-06T09:20:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 ≈41% | S&P 500 top 10 concentration percent record 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/ | 2026-07-02 | 2026-08-06T09:20:00+08:00 |
| breadth.advance_decline | ≈64% S&P 500 在 50DMA 上、A/D 創高、McClellan 轉負 | S&P 500 breadth percent above 50 day moving average August 2026 McClellan | https://articles.stockcharts.com/article/three-breadth-signals-confirming-the-markets-bullish-trend/ | 2026-08-03 | 2026-08-06T09:20:00+08:00 |
| retail.fear_greed | CNN Fear & Greed ≈58（Greed） | CNN Fear and Greed Index August 5 2026 | https://www.cnn.com/markets/fear-and-greed | 2026-08-05 | 2026-08-06T09:20:00+08:00 |
| retail.margin_debt | FINRA 6 月 margin debt $1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-06T09:20:00+08:00 |
| retail.aaii | AAII Bear 42.1%／Neutral 26.9%／Bull 31.0% | AAII investor sentiment survey July 30 2026 | https://www.aaii.com/sentimentsurvey | 2026-07-30 | 2026-08-06T09:20:00+08:00 |
| retail.social_sentiment | Wendy's（WEN）「Save Wendy's」WSB 軋空、≈44% 空頭 | Reddit WSB Wendy's WEN short squeeze August 2026 | https://finance.yahoo.com/markets/stocks/articles/reddit-wants-save-wendy-inside-161925726.html | 2026-08-04 | 2026-08-06T09:20:00+08:00 |
| monetary.treasury_auctions | 5Y 連 14 次 tail、BTC 2022-09 以來最差；7Y tail 0.8bp | US Treasury 5 year 7 year auction tail bid to cover July 2026 | https://www.tftc.io/treasury-139-billion-auction-2-year-5-year-bifurcated-results-july-2026 | 2026-07-28 | 2026-08-06T09:20:00+08:00 |
| monetary.fedwatch | FOMC 7/29 鷹派持平、CME FedWatch 9 月 ≈62% 定價分歧 | CME FedWatch September 2026 probability FOMC hold | https://growbeansprout.com/tools/fedwatch | 2026-08-04 | 2026-08-06T09:20:00+08:00 |
| monetary.pboc | 人行 7/29–8/3 逆回購 ≈¥2.1T、7/24 MLF 淨投放 ¥100B | PBoC reverse repo injection 2.1 trillion yuan late July 2026 | https://www.investing.com/news/economy-news/chinas-pboc-to-conduct-overnight-reverse-repos-inject-a-total-of-21-trillion-yuan-4810853 | 2026-07-24 | 2026-08-06T09:20:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 續上修：合計 ≈$725B、Alphabet 上修觸發賣壓 | hyperscaler capex 2026 725B raised Alphabet Q2 scrutiny | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-07-28 | 2026-08-06T09:20:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic run-rate ≈$47B、OpenAI ≈$25B | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-06-15 | 2026-08-06T09:20:00+08:00 |
| ai.customer_concentration_rpo | Microsoft RPO ≈$678B、≈32% 繫單一客戶（OpenAI） | Microsoft RPO backlog 678 billion single customer OpenAI 2026 | https://www.tradingview.com/news/benzinga:9aade6896094b:0-microsoft-s-backlog-just-hit-678b-almost-a-third-traces-to-a-single-customer/ | 2026-07-30 | 2026-08-06T09:20:00+08:00 |
| ai.compute_supply_demand | HBM/DRAM 合約續升、H200 租金 ≈$4.39/hr、缺口延至 1H2027 | H200 GPU rental price HBM DRAM contract 2026 shortage 2027 | https://jarvislabs.ai/blog/h200-price | 2026-08-01 | 2026-08-06T09:20:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超越 FCF、2026 發債 ≈$182B、>$120B 表外 SPV | hyperscaler capex FCF debt issuance 182 billion off balance sheet SPV 2026 | https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure | 2026-07-24 | 2026-08-06T09:20:00+08:00 |
| ai.revenue_capex_gap | AI 終端年化營收 ≈$72B（Anthropic $47B＋OpenAI $25B）vs 年化 capex ≈$725B | AI revenue to capex gap 2026 hyperscaler | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-06-15 | 2026-08-06T09:20:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 螢幕合格件數 0 | AI rename ticker SPAC no revenue IPO July 30 August 6 2026 | Reuters/Benzinga/BusinessWire SPAC 螢幕 | 2026-08-06 | 2026-08-06T09:20:00+08:00 |
| speculation.ipo_heat | 本週 ≈21 檔跨週定價、無 blowout 首日、YTD ≈$251B/86 檔 | US IPO pricings week August 3 2026 Renaissance | https://www.renaissancecapital.com/IPO-Center/Pricings | 2026-08-04 | 2026-08-06T09:20:00+08:00 |
| speculation.microcap_moonshots | 本週 microcap thematic moonshot 合格 0 件 | microcap 100% single day quantum fusion space nuclear small cap August 2026 | Finviz/StockAnalysis/StockTitan gainers 螢幕 | 2026-08-06 | 2026-08-06T09:20:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 ≈$1T IPO、Anthropic 續進 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground | 2026-07-28 | 2026-08-06T09:20:00+08:00 |
| speculation.insider_form4 | SNOW 董事 Dageville 07-29 售 50,000 股 ≈$14.0M；TEM Lefkofsky 07-28 售 250,000 股 | Snowflake Dageville Tempus Lefkofsky Form 4 insider sale July 2026 SEC | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1640147&type=4 | 2026-07-29 | 2026-08-06T09:20:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.55 | Cboe equity put call ratio August 3 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio | 2026-08-03 | 2026-08-06T09:20:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高 ≈$198B | leveraged ETF AUM record 198 billion 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-07-23 | 2026-08-06T09:20:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x 單股槓桿 ETF＋ELOL（TSLA+SpaceX）發行 | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | https://www.globenewswire.com/news-release/2026/07/07/3323273/0/en/Leverage-Shares-by-Themes-Expands-Tech-Offering-with-Six-New-Single-Stock-Leveraged-ETFs.html | 2026-07-30 | 2026-08-06T09:20:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量 ≈65%（Cboe Q2 2026） | 0DTE SPX options share volume Cboe Q2 2026 65% | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641 | 2026-05-31 | 2026-08-06T09:20:00+08:00 |
| structural.options_volume | OCC 6 月總量 16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report | 2026-07-02 | 2026-08-06T09:20:00+08:00 |
| structural.cross_asset_derivatives | SKEW ≈139.96、VIX ≈16.9 contango、債市波動轉升（TLT 1M skew 創 GFC 以來高） | VIX SKEW term structure bond volatility August 3 2026 Cboe | https://www.cboe.com/insights/posts/week-of-8-3-2026-the-fed-holds-but-bond-volatility-breaks-higher | 2026-08-03 | 2026-08-06T09:20:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt $1.502T、+51.5% YoY（交叉引用 D4） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-06T09:20:00+08:00 |
| structural.ai_infrastructure_debt | CoreWeave $2.6B Anthropic 掛鉤貸款 07-29 調高票息；Nebius $775M 擔保 07-17 | CoreWeave 2.6 billion loan Anthropic yield boosted July 2026 | https://www.bloomberg.com/news/articles/2026-07-29/coreweave-boosts-yield-on-2-6-billion-loan-tied-to-anthropic | 2026-07-29 | 2026-08-06T09:20:00+08:00 |

## 本次分數存檔
```json
{
  "date": "2026-08-06",
  "iso_week": "2026-W32",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "valuation": 78,
  "breadth": 30,
  "speculation": 57,
  "retail": 52,
  "monetary": 76,
  "structural": 78,
  "total": 64,
  "tier": "警戒",
  "regime": "分歧",
  "trigger_state": "未擊發",
  "trigger_reasons": [],
  "monetary_side": "自滿側",
  "hy_oas_widening_streak": 0,
  "sp500_dev200_pct": 9.71
}
```

本報告為相對風險溫度計，非擇時訊號。

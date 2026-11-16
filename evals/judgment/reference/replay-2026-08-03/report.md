# 2026-08-03 市場泡沫風險評估報告
> 報告日期：2026-08-03；執行日：2026-08-03 Asia/Taipei；ISO 週次：2026-W32；前次基準：report-2026-07-30（4天前）

**總評**：總分 64【警戒】（Δ 0）；扳機狀態：未擊發；最貼近錨點：1997 早期建設（65%）。

## §1 六維度風險條圖
| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▱▱▱ | 77 | 77 | 0 |
| 市場廣度 | ▰▰▰▱▱▱▱▱▱▱ | 30 | 30 | 0 |
| 投機行為 | ▰▰▰▰▰▱▱▱▱▱ | 57 | 58 | -1 |
| 散戶情緒 | ▰▰▰▰▱▱▱▱▱▱ | 47 | 47 | 0 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▰▱▱▱ | 76 | 77 | -1 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 78 | 78 | 0 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **64【警戒】** | 64 | 0 |

## §2 歷史錨點相似度
| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1973/1 Nifty Fifty 頂 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 1997 早期建設 | 65% | ▰▰▰▰▰▰▱▱▱▱ | ◀ 最貼近 |
| 1998 LTCM 衝擊 | 15% | ▰▱▱▱▱▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 60% | ▰▰▰▰▰▰▱▱▱▱ |  |
| 2000/3 頂點 | 15% | ▰▱▱▱▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |

## §3 三角訊號
| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,489.72 | ▲ +0.7%（前次 ≈7,437.63） |
| WTI 原油 | $84.25 /bbl | 持平 0%（無新觀測，前次 ≈$84.25） |
| 10Y Treasury | 4.68% | 持平 0 bps（無新觀測，前次 ≈4.68%） |

**三者狀態**：穩定共存——三者本次方向為 ▲／持平／持平（僅股市小幅上行、無下行腿），既非全數同向上行、亦非 ▲/▼ 混合，依格局判定規則屬穩定共存；S&P `dev200_pct` +6.63%（< +10% 拉伸門檻），未升為同向偏高。公開信用利差自滿（HY 2.84%／IG 0.80% 史窄）與 AI 雲端信用重定價並存，須分開判讀。
- 股市：≈7,489.72（S&P 500，2026-07-31 收）；較前次 ▲ +0.7%（前次 ≈7,437.63）；距 200 日均線 +6.63%、距 52 週均線 +8.2%——月底科技股回穩，價格延伸自前次（+4.29%）小幅回升，仍低於 +10% 拉伸門檻。
- WTI 原油：≈$84.25/bbl（DCOILWTICO，2026-07-27，無新觀測）；較前次 持平 0%（前次 ≈$84.25）。
- 10Y 殖利率：4.68%（DGS10，2026-07-30，無新觀測）；較前次 持平 0 bps（前次 ≈4.68%）；主要驅動：三腿視窗不一致（driver=unknown，ΔT10YIE 取自較新視窗）。
**格局轉變**：前次格局＝穩定共存（讀自 report-2026-07-30 的 `regime`）→ 本次格局＝穩定共存；三者由前次的小幅下行／無新觀測轉為股市小幅回升、WTI 與 10Y 無新觀測，價格延伸未達拉伸門檻，維持穩定共存。
**10Y 成因拆解**：拆的是週變動（bps）、非水位（`ΔDGS10 ≈ ΔDFII10 + ΔT10YIE`）；三腿視窗不一致——`decomposition.driver=unknown`（ΔT10YIE 取自 2026-07-31 新觀測、DGS10／DFII10 為 2026-07-30 無新觀測，恆等式不跨視窗成立），判定 不可判（視窗不一致）；三腿實際 signed 週變動如下：
- ΔDGS10 名目殖利率週變動：0 bps
- ΔDFII10 實質殖利率週變動：0 bps
- ΔT10YIE 損益平衡通膨週變動：+1 bps
- 觀測新鮮度：部分未更新（stale_series=DGS10,DFII10）
- 判定：不可判（視窗不一致）
**扳機鏈**：A 通膨鏈（油 → 通膨預期 → Fed 受限 → refinancing 成本）本週未加速——WTI 持平（≈$84.25，無新觀測）、實現通膨仍高但通膨預期持平：[monetary.cpi_yoy] CPIAUCSL yoy_pct=3.46 data_date=2026-06-01（6 月）、5y5y forward [monetary.t5yifr] T5YIFR latest=2.3 delta_bps=0 data_date=2026-07-31（週 Δ 0 bps）；FOMC 7/29 以 9-3 鷹派持平、通膨仍高於 2% 目標，CME FedWatch 9 月定價分歧（≈54–63%）——Fed put 可得性受通膨制約，但油價端無新推力，本鏈未加速。無當期電價／能源瓶頸新報導。B 槓桿鏈（衝擊：財政風險再定價 → NBFI 去槓桿 → margin spiral → 國債市場失序 → 官方市場功能回應）乾柴堆積但未點火——衝擊節點：10Y 期限溢價 THREEFYTP10 ≈0.8376%（序列自身 trailing ≈7d ＋5.9 bps、溫和上行，未達 +15 bps 初啟門檻）；NBFI 節點：script `cftc_lev_funds`／`move_index`／`ofr_repo` 本次 fetch_failed，WebSearch 顯示 MOVE ≈74（07-29，低於 80 平靜區）、槓桿基金美債期貨淨空倉 07-14 較前月回補 ≈14 萬口，無 7 日窗內基差交易新平倉事件；官方回應節點：`repo_stress` SOFR−IORB 0 bps、SOFR99−IORB +8 bps、SRF 動用 ≈$0（無失序）。real-rate 主導的異常 10Y 上行本週不存在（ΔDGS10 0 bps）。惟 AI 雲端信用本週續重定價（Oracle 5Y CDS ≈200bp、CoreWeave 5Y CDS ≈675bp、hyperscaler 債利差 ≈78bp）屬單一發行人／結構化層級的後期訊號，尚未外溢至國債市場層級；本鏈證據 best-effort，本週無國債基差交易失序新事件。
**扳機理由**：none
**結論**：扳機狀態：未擊發——本週無任一 contract 扳機理由成立：HY OAS 週 Δ 0 bps（未走闊，streak 歸零）、10Y driver≠breakeven、期限溢價週 +5.9 bps 未達 +15 bps 初啟門檻；私募信貸端 BCRED 5% 贖回上限事件（2026-06-04）已落 30 日窗外，且 7 月贖回請求「明顯轉緩」、本週無新 gate proration / breach。三者配置歷史意義：估值＋槓桿＝崩跌位能，融資緊縮＝時點扳機；本週公開信用利差回到極度自滿（HY 2.84%／IG 0.80% 史窄）、非銀融資扳機暫時消退，屬「froth 自滿而扳機未擊發」的組態，最須盯 AI 雲端信用重定價（Oracle BBB-／CDS ≈200bp、CoreWeave CDS ≈675bp）是否外溢至公開利差與私募信貸閘門是否再現。

## 六維度評分

### 1. 估值溢價 — 77（weight 22%，Δ 0）
- **S&P 500 trailing P/E** ≈**28.84**（2026-07-31，https://www.multpl.com/s-p-500-pe-ratio，source_ids=valuation.sp500_pe_cape）——遠高於長期中位（≈16–19），實現盈餘基礎上市場歷史性偏貴。
- **Shiller CAPE** ≈**40.91**（2026-07-31，https://www.multpl.com/shiller-pe，source_ids=valuation.sp500_pe_cape）——逼近歷史高（≈44）、遠高於長均 ≈32.4。
- **Excess CAPE Yield（ECY）** ≈**0.03%**（`1/40.91 − 2.41/100`，derived 自 CAPE **40.91** 與 DFII10 2.41%，2026-07-31，source_ids=valuation.sp500_pe_cape）——接近 0，屬 1929／2000 級別股相對債極貴訊號（confirmation，不主計分）。
- **Mag 7 加權 P/E**：Mag 7 對其餘 493 檔溢價壓縮至 ≈**10%**（≈2.4 個 P/E 點，近十年最低）（2026-07-09，https://www.advisorperspectives.com/articles/2026/07/09/magnificent-sevens-weakness-become-problem-wall-street，source_ids=valuation.mag7_multiples）——絕對水位仍高但相對溢價續收斂（stock-of-state 沿用）。
- **價格趨勢偏離（Farrell #1/#2/#4）** S&P 距 200 日均線 **+6.63%**、距 52 週均線 +8.2%（`sp500_trend`，2026-07-31，FRED SP500，source_ids=valuation.sp500_trend）——月底科技股回穩使價格延伸自 +4.29% 小幅回升，仍低於 +10% 拉伸門檻，與 P/E／CAPE 互補、不重複計分。
- **AI capex 現實檢核**：hyperscaler 2026 capex 指引續上修——MSFT ≈$190B、Alphabet 上修至 ≈$190B、Amazon ≈$200B、Meta $125–145B，四家合計 ≈**$725B**（+77% YoY）（2026-07-28，https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion，source_ids=ai.hyperscaler_capex）——基本面敘事仍撐估值，惟回本未現、市場對 capex 上修轉為懲罰。
- **AI compute 供需現實檢核**：伺服器 DRAM 交期 30–40 週、3Q26 合約價續漲 +13–**18%** QoQ（TrendForce，2026-07-03，https://www.trendforce.com/presscenter/news/20260703-13134.html，source_ids=ai.compute_supply_demand）——供給仍被 AI 伺服器合約吸收、缺口未成形（供給緊、非過剩），此渠道未推升估值風險。
- **AI 營收對 capex 缺口現實檢核**：AI 終端年化營收（Anthropic ≈$47B＋OpenAI ≈$25B）vs 年化 capex ≈**$725B**（分母：top-4＋Oracle）（2026-06-15，https://epoch.ai/data-insights/anthropic-openai-revenue，source_ids=ai.revenue_capex_gap）——量級缺口仍逾 10× 且 capex 續升，回本假設後移，屬估值風險上修的質化依據（缺口未收斂）。
- **Hyperscaler 融資結構（capex vs FCF / 發債）**：quarterly_state——top-5 capex 已超越 FCF、續靠外部融資；event_scan——五大 2026 發債 ≈**$159B**（+47% YoY）、Amazon 7 月遭 S&P 降至 BBB-（2026-07-22，https://cryptobriefing.com/tech-giants-record-159b-bonds-ai/，source_ids=ai.hyperscaler_financing_mix）——capex 愈靠發債支撐、同份 guidance 脆弱性上升（BIS Bulletin 120，confirmation，不主計分）。
- **AI 信用定價分歧（equity-vs-credit schism）**：AI 雲端／基建發行人信用本週續重定價——hyperscaler 債利差擴至 ≈**78bp**（vs 兩月前 ≈50bp）、Oracle 5Y CDS ≈200bp、CoreWeave 5Y CDS ≈675bp（隱含 ≈50% 違約）（2026-07-30，https://www.techtimes.com/articles/322222/20260730/coreweave-cds-hits-50-default-odds-bond-market-calls-time-gpu-debt-spiral.htm，source_ids=valuation.ai_credit_schism）——信貸端開始重定價而股價未跟＝後期訊號側證據升溫（confirmation，不主計分；缺值不調分）。
- **TP-upgrade phase signal**：本季（Q3 2026）具名賣方升評屬 **EPS-driven**——Morgan Stanley NVDA 目標未擴張、目標價 $**288**（2026-07-13，https://www.gurufocus.com/news/8955458/morgan-stanley-upgrades-nvidia-nvda-with-a-288-target-price，source_ids=valuation.analyst_tp_decomposition）——升評由 E 而非 multiple 主導、同季未見多檔 multiple-driven 重定價，屬相對緩和訊號（confirmation，不主計分）。
- **折舊年限變動（盈餘品質）**：過去 30 日無新 10-K／10-Q 折舊年限或殘值假設變更披露（✗ NOT DISCLOSED，source_ids=ai.depreciation_life，不納入計分）。
- **backlog 重複計算風險（RPO double-counting）**：本次無新一手客戶集中度／RPO 具乾淨窗內資料日之披露（✗ NOT DISCLOSED，source_ids=ai.customer_concentration_rpo，不納入計分）。
- **資本週期階段**：event_scan 無窗內具日期的新進入者／取消事件、quarterly_state 供需增速證據不足，本次不判定週期階段（✗ NOT DISCLOSED，source_ids=ai.capital_cycle，不納入計分）。
**結論**：分數維持 **77**（rubric 高位）。趨勢偏離自 +4.29% 小幅回升至 +6.63%、CAPE 40.91 近史高、ECY ≈0、capex 續上修（$725B）、AI 信用重定價升溫（Oracle CDS ≈200bp、CoreWeave CDS ≈675bp）——升溫面與 Mag7 相對溢價壓縮至 ≈10% 的緩和面相抵，淨評與前次持平。

### 2. 市場廣度 — 30（weight 13%，Δ 0）
- **RSP（等權）vs SPY（市值權）YTD**：RSP 等權 YTD +**9.67%** 領先 SPY 市值權 +8.38%（2026-06-10，https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/，source_ids=breadth.rsp_spy）——等權領先市值權，廣度結構偏健康／轉寬方向（科技領導趨緩使等權相對占優）。
- **Top-10 集中度**：≈**40%**（近歷史高位）（2026-07-02，https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/，source_ids=breadth.top10_concentration）——遠高於長均 ≈25%、處歷史高位（結構性狹窄）。
- **Advance/Decline 與新高/新低（proxy）**：Nasdaq-100 廣度——48.0% 成分股在 50 日均線上、63.7% 在 200 日均線上、10 日淨新高 ≈**0.1%**（2026-07-29，https://streetstats.finance/markets/breadth-momentum/NQ100，source_ids=breadth.advance_decline）——半數成分股跌破 50 日均線、淨新高近零，廣度動能中性偏弱。
**結論**：分數維持 **30**（rubric 21–40 偏健康端）。等權領先市值權（+1.3 pp）為結構性健康主訊號；Top-10 ≈40% 歷史高位與 50 日均線上比例僅 48% 為殘餘負面——正負相抵，淨評與前次持平。

### 3. 投機行為 — 57（weight 18%，Δ -1）
- **+AI 改名／SPAC**：本週（07-27–08-03）+AI 改名／SPAC 合格 **0** 件（2026-08-03 螢幕）——✓ SEARCH-VERIFIED（0 件）（source_ids=speculation.ai_rename_spac）；最近一起 Azio（EVTV→AZIO）為 07-13、已落 7 日窗外。
- **IPO 熱度**：2026 YTD 募資 ≈$251B／**86** 檔（超越 2025 全年），惟本週 Jersey Mike's（JMKE）募 ≈$1B 收平、Cerebras／Quantinuum 回吐首日漲幅（aftermarket 轉弱）（2026-08-01，https://valueaddvc.com/blog/ipo-market-2026-which-companies-are-going-public-and-what-the-window-looks-like，source_ids=speculation.ipo_heat）——一級市場活躍但 aftermarket 疲弱、投機體感降溫。
- **Microcap thematic moonshots**：本週 microcap thematic moonshot 合格 **0** 件（<$1B 市值、單日 ≥100% 或 2–3 日 ≥50%、堆疊 2+ 熱主題＋弱基本面；2026-08-03 螢幕）——✓ SEARCH-VERIFIED（0 件）（source_ids=speculation.microcap_moonshots）；AMFN +58%（07-20、單一主題）不合格且落窗外。
- **Upcoming AI mega-IPO pipeline**：OpenAI 目標 ≈$**1**T IPO、Anthropic 續進 IPO 程序（2026-07-28，https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground，source_ids=speculation.upcoming_ai_ipos）——30 日內具名巨型 AI IPO pipeline 活躍、流動性抽離風險。
- **Insider selling clusters**：14 日內（07-20–08-03）出現合格 Form 4 cluster——CoreWeave（CRWV）CEO Intrator 07-21 售 307,692 股 ≈$**24.07**M，另 07-29 有 CoreWeave 內部人賣單（2026-07-21，https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001769628&type=4，source_ids=speculation.insider_form4）——✓ SEARCH-VERIFIED（非零），AI 硬體複合體內部人賣壓集中。
- **Cboe equity-only put/call**：≈**0.63**（2026-07-31，https://ycharts.com/indicators/cboe_equity_put_call_ratio，source_ids=speculation.equity_put_call）——中性偏 call，未破 0.50 極端（confirmation，不主計分）。
**結論**：分數由 58 降至 **57**（rubric 41–60「投機升溫」）。CoreWeave 內部人賣壓集中、巨型 AI IPO pipeline 活躍為升溫面；+AI 改名／moonshot 均 0、IPO aftermarket 轉弱（Cerebras／Quantinuum 回吐）為抑制面——淨評較前次微降 1 分。

### 4. 散戶情緒 — 47（weight 12%，Δ 0）
- **CNN Fear & Greed**：≈**39「Fear」**（2026-07-31，https://www.cnn.com/markets/fear-and-greed，source_ids=retail.fear_greed）——續處恐懼區，散戶未亢奮。
- **Margin Debt**：6 月 **$1.502T（記錄高）、YoY +51.5%**（2026-07-20，https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026，source_ids=retail.margin_debt）——月頻 stock-of-state；YoY +**51.5%** 仍屬 1999／2007／2021 頂部級別警訊。
- **AAII 散戶調查**：Bear 42.1%／Neutral 26.9%／Bull **31.0%**（2026-07-30，https://www.aaii.com/sentimentsurvey，source_ids=retail.aaii）——多方低於長均 37.5%、空方偏高，散戶情緒偏空。
- **家庭持股佔金融資產比**：**45.76%**（`BOGZ1FL153064486Q`，2026-01-01 資料日／2026-Q1，FRED BOGZ1FL153064486Q，source_ids=retail.household_equity_allocation）——歷史高位、後續加碼空間有限（Farrell #5，季頻沿用、不計週 Δ）。
- **NAAIM Exposure Index**：前值 84.02 → 最新 **79.70**（2026-07-29，https://ycharts.com/indicators/naaim_number，source_ids=retail.naaim）——主動經理人曝險續回落、已減碼（Farrell #9，confirmation，不主計分）。
- **社群情緒代理**：本週（7 日窗）無具名迷因軋空／WSB 熱門標的（WEN 軋空為 6 月底、窗外）（✗ NOT DISCLOSED，source_ids=retail.social_sentiment，不納入計分）。
**結論**：分數維持 **47**（rubric 41–60 下緣）。CNN F&G ≈39 續處 Fear、AAII 多方 31% 偏空、NAAIM 續回落至 79.7＝擁擠度續降溫；惟 margin debt 6 月創高（YoY +51.5%）、家庭持股高位為抑跌——正負相抵，淨評與前次持平。

### 5. 貨幣與信貸環境 — 76（weight 20%，Δ -1）
- **Fed funds rate**：目標區間 **3.50–3.75%**（`DFEDTARU` 3.75%／`DFEDTARL` 3.50%，2026-08-02，FRED DFEDTARU/DFEDTARL，source_ids=monetary.fed_funds）——FOMC 7/29 以 9-3 維持不變。
- **市場隱含路徑（CME FedWatch，best-effort）**：FOMC 7/29 鷹派持平（9-3 票），CME FedWatch 9 月路徑定價分歧（降息機率市場報導 ≈**63%**、但通膨仍高使近端未定論）（2026-07-30，https://growbeansprout.com/tools/fedwatch，source_ids=monetary.fedwatch）——Fed 未明確轉鴿、寬鬆空間受通膨制約（缺值不調分）。
- **Realized inflation vs expectations**：CPI YoY **3.46%**（`CPIAUCSL`，2026-06-01，FRED CPIAUCSL，source_ids=monetary.cpi_yoy）仍高於 2% 目標、5y5y forward **2.30%**（`T5YIFR`，2026-07-31，週 Δ 0 bps，FRED T5YIFR，source_ids=monetary.t5yifr）持平——通膨黏著，Fed 約束未鬆。
- **10Y 期限溢價（term premium）**：`THREEFYTP10` **0.8376%**（2026-07-24，Kim-Wright 三因子模型，序列自身 trailing ≈7d +5.9 bps，FRED THREEFYTP10，source_ids=monetary.term_premium）——財政風險再定價溫和上行、未達 +15 bps 初啟門檻。
- **repo 資金壓力（SOFR−IORB）與 SRF 動用**：SOFR **3.65%**、IORB 3.65%、SOFR−IORB **0 bps**；SOFR99 3.73%、SOFR99−IORB +8 bps；SRF/RPONTTLD 動用 ≈$0（2026-07-30，FRED SOFR/SOFR99/IORB/RPONTTLD，source_ids=monetary.repo_stress_srf）——secured-funding 無壓力、SRF 未動用。
- **美債標售需求（auction，best-effort）**：過去 14 日（07-20–08-03）無具日期之顯著標售 tail／dealer takedown 惡化的可稽核 recap（最近 10Y 為 07-08、窗外）（✗ NOT DISCLOSED，source_ids=monetary.treasury_auctions，不納入計分）。
- **HY OAS**：**2.84%**（`BAMLH0A0HYM2`，2026-07-30，週 Δ 0 bps，FRED BAMLH0A0HYM2，source_ids=monetary.hy_oas）——接近循環低、極窄、自滿側；本週無新觀測、未走闊（streak 歸零）。
- **IG OAS**：**0.80%**（`BAMLC0A0CM`，2026-07-30，週 Δ 0 bp，FRED BAMLC0A0CM，source_ids=monetary.ig_oas）——史窄、信用自滿。
- **10Y nominal 週變動拆解**：ΔDGS10 0 bps；`DGS10` **4.68%**（2026-07-30，FRED DGS10，source_ids=monetary.dgs10）、`DFII10` **2.41%**（2026-07-30，FRED DFII10，source_ids=monetary.dfii10）、`T10YIE` **2.28%**（2026-07-31，FRED T10YIE，source_ids=monetary.t10yie）——三腿視窗不一致（driver=unknown，詳 §3），殖利率無新觀測。
- **WTI 原油**：**$84.25**/bbl（`DCOILWTICO`，2026-07-27，無新觀測，FRED DCOILWTICO，source_ids=monetary.wti）——持平，A 通膨鏈油價端無新推力。
- **Fed balance sheet**：≈$6.74T（原始 **6,738,190** 百萬美元，2026-07-29，無新觀測，FRED WALCL，source_ids=monetary.walcl）——量化緊縮步調持平。
- **全球央行流動性（ECB）**：ECB ≈€5.94T（原始 **5,944,015** 百萬歐元，2026-07-24，FRED ECBASSETSW，source_ids=monetary.ecb_boj）——持平。
- **全球央行流動性（BOJ）**：BOJ ≈¥639.55T（原始 **6,395,509** 億日圓，2026-06-01，FRED JPNASSETS，source_ids=monetary.ecb_boj）——持平。
- **PBoC 流動性操作**：人行 7/24 MLF 淨投放 ≈¥**100**B（5 個月最大）、另 7/14 以 6 個月逆回購紀錄注入 ¥1.4T、月底連日逆回購（2026-07-24，https://www.bloomberg.com/news/articles/2026-07-24/pboc-adds-most-liquidity-to-economy-in-five-months-to-aid-growth，source_ids=monetary.pboc）——中國端流動性偏寬（confirmation）。
- **私募信貸贖回壓力（event-driven）**：BCRED 5% 季度贖回上限比例撥付事件為 2026-06-04、已落 30 日窗外；7 月 Blackstone 表示 BCRED 贖回請求「明顯轉緩」，過去 30 日無新 gate proration / breach、無多基金 net inflow→outflow flip（✗ NOT DISCLOSED，source_ids=monetary.private_credit_liquidity，不納入計分）。
**結論**：自滿側；公開信用利差回到極度自滿（HY 2.84%／IG 0.80% 史窄、皆無新觀測未走闊），非銀融資扳機（前次 BCRED gate）已消退至窗外、本週無新擊發事件——屬「self-satisfied froth 而扳機未擊發」的自滿側組態；惟 AI 雲端信用重定價（Oracle CDS ≈200bp、CoreWeave CDS ≈675bp）與期限溢價溫和上行為後期側新增壓力，分數自 77 微降至 **76**（financing 扳機側消退，自滿側 froth 續高）。

### 6. 結構性槓桿 — 78（weight 15%，Δ 0）
- **US 槓桿 ETF AUM**：美國槓桿 ETF 總 AUM 創高 ≈$**198**B（TQQQ、SOXL 領先）（2026-07-23，https://cryptobriefing.com/leveraged-etfs-record-198b-aum/，source_ids=structural.leveraged_etf_aum）——水位維持記錄高。
- **US 單股槓桿 ETF 核准／發行（近 30 日）**：Leverage Shares 07-07 起推 6 檔 2x 單股槓桿 ETF（GOOGL／AMZN／META／AAPL），並於 07-30 推 ELOL（TSLA＋SpaceX 100%/100%）（2026-07-30，https://www.manilatimes.net/2026/07/30/tmt-newswire/globenewswire/two-industry-leaders-one-ticker-leverage-shares-by-themes-launches-elol/2395125，source_ids=structural.us_single_stock_etf）——單股槓桿產品續擴散。
- **全球（非美）槓桿產品核准（本週）**：韓國反而收緊——KRX/FSC 07-31 起暫停新單股槓桿 ETF 上市並將現金保證金要求調高三倍；台／日／歐 07-27–08-03 無新單股槓桿／反向 ETF 英文披露、「全球槓桿擴散訊號」本週未觸發（✗ NOT DISCLOSED，source_ids=structural.global_leveraged_approvals，不納入計分）。
- **0DTE 佔 SPX 期權量**：≈**65**%（Cboe Q2 2026，資料月 2026-05，https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641，source_ids=structural.zero_dte）——持續 >55% 高檔（資料日 2026-05-31）。
- **Options 總量（OCC 月報）**：OCC 6 月總量 **16.0** 億口（1,603,491,559 口）（2026-07-02，https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report，source_ids=structural.options_volume）——衍生品投機量續處高檔（stock-of-state 沿用；7 月報未發布）。
- **跨資產／相關性確認**：SKEW ≈**139.9**、VIX 17.09（term structure contango、月底賣壓下溫和上行、非恐慌）（2026-07-31，https://www.home.saxo/content/articles/options/index-up-average-stock-down---options-brief---31-july-2026-31072026，source_ids=structural.cross_asset_derivatives）——尾端避險略升、整體波動未失控（confirmation）。
- **Margin debt / 市值 交叉檢核**：6 月 $1.502T、YoY +**51.5**%（2026-07-20，見 D4，https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026，source_ids=structural.margin_debt_crosscheck）——確認零售槓桿頂部級別（confirmation，不在此重複計分）。
- **AI 基礎設施債務／vendor-financing loops**：Nebius 07-17 完成首筆 $**775**M 擔保債務融資（SOFR+2.50%、GPU 基建與 IG 客戶合約現金流擔保）；Oracle／xAI／Meta／CoreWeave 另將 >$120B AI 資料中心支出透過私募信貸移至表外（2026-07-17，https://nebius.com/newsroom/nebius-raises-775-million-in-first-secured-debt-financing-to-accelerate-global-buildout，source_ids=structural.ai_infrastructure_debt）——AI 基建融資續擴張、GPU 擔保債規模上升＝結構性槓桿升溫因子。
- **銀行對 NBFI 放款**：≈$2.00T（原始 **2,004.99** 十億美元，2026-07-22，無新觀測，FRED LNFACBW027SBOG，source_ids=structural.nbfi_bank_loans）——bank–NBFI linkage 水位持平（confirmation，不主計分）。
- **美債基差交易槓桿（best-effort）**：script `cftc_lev_funds`／`move_index`／`ofr_repo` 本次 `fetch_failed`；WebSearch 顯示 MOVE ≈74（07-29 平靜）、槓桿基金淨空倉 07-14 回補中，無 7 日窗內基差交易新平倉事件（✗ NOT DISCLOSED，source_ids=structural.treasury_basis_trade，不納入計分、不調 D6 分數）。
**結論**：分數維持 **78**（rubric 61–80）。0DTE 續 >55%、OCC 量高檔、槓桿 ETF AUM 創高、Leverage Shares 單股槓桿續擴散、AI 基建融資續擴張（Nebius $775M、表外 >$120B）＝結構性槓桿高檔；惟全球擴散未觸發（韓國反收緊）、基差交易無窗內新證據（MOVE ≈74 平靜）為抑制——升溫與抑制相抵，淨評與前次持平。

## 綜合分數

| 維度 | 權重 | 分數 | 加權分數 |
|---|---:|---:|---:|
| 估值溢價 | 22% | 77 | 16.94 |
| 市場廣度 | 13% | 30 | 3.90 |
| 投機行為 | 18% | 57 | 10.26 |
| 散戶情緒 | 12% | 47 | 5.64 |
| 貨幣與信貸環境 | 20% | 76 | 15.20 |
| 結構性槓桿 | 15% | 78 | 11.70 |
加權總分：63.64 → 64【警戒】

邊界帶：總分 64 距 警戒/高 邊界 ≤ 2 分，評分固有噪音約 ±2–3，等級判讀需保留餘地。

## 歷史泡沫週期對比

相似度計算：checklist v2

逐項對本次六維度分數、macro/current/prior state 與附錄證據重算命中；相似度 = 命中數 ÷ 特徵數 × 100，四捨五入到最近 5%。「無資料」不計入命中但仍在分母。

- 1973/1 Nifty Fifty 頂：命中 2/8 = 25%
- 1997 早期建設：命中 5/8 = 65%
- 1998 LTCM 衝擊：命中 1/8 = 15%
- 1999 晚期狂熱：命中 6/10 = 60%
- 2000/3 頂點：命中 1/8 = 15%
- 2021/12 Meme 頂：命中 3/8 = 40%

2000/3 高位回落條件：否

**1973/1 Nifty Fifty 頂 feature audit**
- 1973.1｜未命中｜source_ids=—｜估值溢價 77 < 80
- 1973.2｜未命中｜source_ids=—｜市場廣度 30 < 60
- 1973.3｜未命中｜source_ids=—｜CPI YoY 3.46% < 4%
- 1973.4｜命中｜source_ids=—｜T5YIFR 週 Δ 0 bps ≥ 0（通膨預期未回落）
- 1973.5｜未命中｜source_ids=—｜WTI 週漲幅 0%（無新觀測）< +0.5%
- 1973.6｜未命中｜source_ids=—｜decomposition.driver=unknown ≠ breakeven（三腿視窗不一致）
- 1973.7｜未命中｜source_ids=—｜扳機狀態＝未擊發 < 初啟
- 1973.8｜命中｜source_ids=—｜散戶情緒 47 < 55
**1997 早期建設 feature audit**
- 1997.1｜未命中｜source_ids=—｜估值溢價 77 > 74（超出 40–74 區間）
- 1997.2｜命中｜source_ids=—｜市場廣度 30 < 45
- 1997.3｜未命中｜source_ids=—｜投機行為 57 ≥ 50
- 1997.4｜命中｜source_ids=ai.hyperscaler_capex｜hyperscaler 2026 capex 指引仍上修（合計 ≈$725B）
- 1997.5｜命中｜source_ids=—｜散戶情緒 47 < 55
- 1997.6｜未命中｜source_ids=—｜結構性槓桿 78 ≥ 50
- 1997.7｜命中｜source_ids=—｜HY OAS 2.84% < 4% 且週 Δ 0 bps ≤ 0（未走闊，all 成立）
- 1997.8｜命中｜source_ids=—｜扳機狀態＝未擊發
**1998 LTCM 衝擊 feature audit**
- 1998.1｜未命中｜source_ids=structural.cross_asset_derivatives｜HY 週 Δ 0 bps < +30；VIX 17.09 contango（無壓力事件）
- 1998.2｜未命中｜source_ids=—｜S&P chg +0.70% > −5%（未達回檔門檻）
- 1998.3｜無資料｜source_ids=—｜私募信貸與美債基差交易本次皆 ✗ NOT DISCLOSED（無成功事件證據）
- 1998.4｜未命中｜source_ids=monetary.fedwatch｜FOMC 7/29 鷹派持平、非轉鴿
- 1998.5｜命中｜source_ids=—｜估值溢價 77 ≥ 60
- 1998.6｜未命中｜source_ids=—｜扳機狀態＝未擊發 < 初啟
- 1998.7｜未命中｜source_ids=—｜市場廣度 Δ = 30 − 30 = 0 < +8
- 1998.8｜未命中｜source_ids=—｜ΔT10YIE +1 bps > 0（通膨預期非下行）
**1999 晚期狂熱 feature audit**
- 1999.1｜命中｜source_ids=—｜估值溢價 77 ≥ 75
- 1999.2｜命中｜source_ids=valuation.sp500_pe_cape｜CAPE 40.91 ≥ 38
- 1999.3｜未命中｜source_ids=—｜投機行為 57 < 60
- 1999.4｜未命中｜source_ids=speculation.microcap_moonshots,speculation.ipo_heat｜本週 moonshot 0；無營收 IPO 佔比未達偏高
- 1999.5｜未命中｜source_ids=—｜市場廣度 30 < 45（廣度健康、非轉窄）
- 1999.6｜命中｜source_ids=—｜D5 monetary_side＝自滿側 且 HY OAS 2.84% < 3.5%（all 成立）
- 1999.7｜命中｜source_ids=—｜結構性槓桿 78 ≥ 60
- 1999.8｜未命中｜source_ids=—｜散戶情緒 47 < 55
- 1999.9｜命中｜source_ids=speculation.upcoming_ai_ipos｜巨型 AI IPO pipeline 活躍（OpenAI ≈$1T、Anthropic 續進）
- 1999.10｜命中｜source_ids=—｜扳機狀態＝未擊發
**2000/3 頂點 feature audit**
- 2000.1｜未命中｜source_ids=—｜估值溢價 77 < 85
- 2000.2｜未命中｜source_ids=—｜扳機狀態＝未擊發 < 初啟
- 2000.3｜未命中｜source_ids=—｜市場廣度 30 < 60
- 2000.4｜未命中｜source_ids=—｜prior sp500_dev200_pct 4.29 < +10 使第一分支為否；current chg +0.70% > −5%
- 2000.5｜未命中｜source_ids=—｜投機行為 57 < 70
- 2000.6｜命中｜source_ids=speculation.insider_form4｜14 日內合格 Form 4 cluster：CoreWeave（Intrator 07-21 售 ≈$24.07M）
- 2000.7｜未命中｜source_ids=—｜散戶情緒 47 < 65
- 2000.8｜未命中｜source_ids=monetary.fedwatch｜FedWatch 未定價明確緊縮（隱含可能降息）；10Y driver≠breakeven
**2021/12 Meme 頂 feature audit**
- 2021.1｜未命中｜source_ids=—｜散戶情緒 47 < 65
- 2021.2｜無資料｜source_ids=—｜本週（7 日）無具名社群投機標的（WEN 軋空為 6 月底、窗外）
- 2021.3｜命中｜source_ids=—｜結構性槓桿 78 ≥ 65
- 2021.4｜命中｜source_ids=monetary.walcl,monetary.ecb_boj｜D5 76 ≥ 60 且自滿側、央行資產負債表可得（流動性氾濫，all 命中）
- 2021.5｜命中｜source_ids=retail.margin_debt｜margin debt YoY +51.5% ≥ +40%
- 2021.6｜未命中｜source_ids=speculation.microcap_moonshots｜本週 microcap moonshot 0 < 1
- 2021.7｜未命中｜source_ids=—｜市場廣度 30 < 50
- 2021.8｜未命中｜source_ids=—｜CPI YoY 3.46% < 4%（all 不成立）

**兩句解讀**：本週最貼近錨點為「1997 早期建設」（65%），1999 晚期狂熱（60%）緊追其後——當前組態是高估值（CAPE 40.91、估值溢價 77）＋極度自滿的公開信用（HY 2.84%／IG 0.80% 史窄、自滿側）＋窄領導但等權健康的廣度，且扳機狀態＝未擊發（前次已擊發的私募信貸扳機已消退至 30 日窗外），最像 1997 早期建設向 1999 晚期狂熱過渡的中段。與 2000/3 頂點（15%）的關鍵分歧在於：扳機未擊發、散戶未狂熱（F&G ≈39 Fear、AAII Bull 31%）、廣度未極窄——循環位置意涵：估值＋槓桿位能高企但時點扳機尚未點燃，屬「froth 未見頂、扳機待命」的中後段，最須盯 AI 雲端信用重定價（Oracle CDS ≈200bp、CoreWeave CDS ≈675bp）是否由結構化層級外溢至公開利差與私募信貸閘門。長期指數成長趨勢偏離（Dot-com ≈95%、1929 ≈110%、當前 AI 週期 ≈147%；RIA/Farrell）作跨期敘事錨、不進 checklist。

## 機構情緒對照

本次無新機構調查數據。

## 本次新增訊號

比較基準：vs 前次（4天前）。

- **貨幣與信貸環境（D5）Δ -1，且＝自滿側**：前次擊發的私募信貸扳機已消退——BCRED 5% 贖回上限事件為 2026-06-04、已落 30 日窗外，7 月 Blackstone 表示贖回請求「明顯轉緩」，本週無新 gate proration / breach；公開信用利差回到極度自滿（HY 2.84%／IG 0.80% 史窄、皆無新觀測），扳機狀態由「已擊發」回落至「未擊發」、monetary_side 由扳機側轉自滿側。惟 AI 雲端信用重定價（Oracle 5Y CDS ≈200bp、CoreWeave 5Y CDS ≈675bp、hyperscaler 債利差 ≈78bp）與期限溢價溫和上行（THREEFYTP10 +5.9 bps）為後期側新增壓力，financing 扳機側消退使分數自 77 微降至 76。
- **投機行為（D3）Δ -1**：本週 +AI 改名／SPAC 與 microcap moonshot 均 0 件、IPO aftermarket 轉弱（Cerebras／Quantinuum 回吐首日漲幅、JMKE 收平）——投機體感降溫；CoreWeave 內部人賣壓集中（Intrator 07-21 售 ≈$24.07M）與 OpenAI ≈$1T IPO pipeline 為升溫面，淨降 1 分。
- **HY OAS 連續走闊 streak 歸零**：前次 streak=1，本次 HY OAS 無新觀測、週 Δ 0 bps（未走闊），依決定性公式 streak 歸 0——「HY 連續兩次走闊」初啟判準本次不成立。
- 結構性槓桿（D6，Δ 0）雖分數持平，惟本週 AI 基建融資續擴張（Nebius $775M 擔保、表外 >$120B）、US 單股槓桿續擴散（Leverage Shares 6 檔＋ELOL）——**全球（非美）槓桿擴散本週未觸發（韓國反收緊），本週擴散訊號未觸發**。
- 其餘維度（估值 77、廣度 30、散戶 47）分數與前次持平；總分 64【警戒】、Δ 0。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | S&P 500 收盤（sp500_trend latest） | 7,489.72 | FRED SP500（sp500_trend） | 2026-07-31 | 2026-08-03T09:20:00+08:00 |
| valuation.sp500_trend | S&P 500 距 200DMA 偏離（sp500_trend dev200_pct） | +6.63% | FRED SP500（sp500_trend） | 2026-07-31 | 2026-08-03T09:20:00+08:00 |
| valuation.sp500_trend | S&P 500 距 52 週均線偏離（sp500_trend dev52w_pct） | +8.2% | FRED SP500（sp500_trend） | 2026-07-31 | 2026-08-03T09:20:00+08:00 |
| retail.household_equity_allocation | 家庭持股佔金融資產比（BOGZ1FL153064486Q） | 45.76 | FRED BOGZ1FL153064486Q | 2026-01-01 | 2026-08-03T09:20:00+08:00 |
| monetary.fed_funds | Fed funds 上限（DFEDTARU） | 3.75% | FRED DFEDTARU | 2026-08-02 | 2026-08-03T09:20:00+08:00 |
| monetary.fed_funds | Fed funds 下限（DFEDTARL） | 3.50% | FRED DFEDTARL | 2026-08-02 | 2026-08-03T09:20:00+08:00 |
| monetary.hy_oas | HY OAS（BAMLH0A0HYM2） | 2.84% | FRED BAMLH0A0HYM2 | 2026-07-30 | 2026-08-03T09:20:00+08:00 |
| monetary.ig_oas | IG OAS（BAMLC0A0CM） | 0.80% | FRED BAMLC0A0CM | 2026-07-30 | 2026-08-03T09:20:00+08:00 |
| monetary.dgs10 | 10Y 名目殖利率（DGS10） | 4.68% | FRED DGS10 | 2026-07-30 | 2026-08-03T09:20:00+08:00 |
| monetary.dfii10 | 10Y 實質殖利率（DFII10） | 2.41% | FRED DFII10 | 2026-07-30 | 2026-08-03T09:20:00+08:00 |
| monetary.t10yie | 10Y breakeven（T10YIE） | 2.28% | FRED T10YIE | 2026-07-31 | 2026-08-03T09:20:00+08:00 |
| monetary.wti | WTI 原油（DCOILWTICO） | $84.25 | FRED DCOILWTICO | 2026-07-27 | 2026-08-03T09:20:00+08:00 |
| monetary.cpi_yoy | CPI YoY（CPIAUCSL yoy_pct） | 3.46% | FRED CPIAUCSL | 2026-06-01 | 2026-08-03T09:20:00+08:00 |
| monetary.t5yifr | 5y5y forward（T5YIFR latest） | 2.30% | FRED T5YIFR | 2026-07-31 | 2026-08-03T09:20:00+08:00 |
| monetary.term_premium | 10Y 期限溢價（THREEFYTP10） | 0.8376% | FRED THREEFYTP10 | 2026-07-24 | 2026-08-03T09:20:00+08:00 |
| monetary.repo_stress_srf | SOFR 隔夜擔保融資利率 | 3.65% | FRED SOFR | 2026-07-30 | 2026-08-03T09:20:00+08:00 |
| monetary.repo_stress_srf | SOFR99 99th 分位尾端 | 3.73% | FRED SOFR99 | 2026-07-30 | 2026-08-03T09:20:00+08:00 |
| monetary.repo_stress_srf | IORB 準備金餘額利率 | 3.65% | FRED IORB | 2026-08-03 | 2026-08-03T09:20:00+08:00 |
| monetary.repo_stress_srf | 隔夜 repo 操作量（RPONTTLD） | 0.000 | FRED RPONTTLD | 2026-07-31 | 2026-08-03T09:20:00+08:00 |
| monetary.walcl | Fed 資產負債表（WALCL） | 6,738,190 百萬美元（≈$6.74T） | FRED WALCL | 2026-07-29 | 2026-08-03T09:20:00+08:00 |
| monetary.ecb_boj | ECB 資產（ECBASSETSW） | 5,944,015 百萬歐元（≈€5.94T） | FRED ECBASSETSW | 2026-07-24 | 2026-08-03T09:20:00+08:00 |
| monetary.ecb_boj | BOJ 資產（JPNASSETS） | 6,395,509 億日圓（≈¥639.55T） | FRED JPNASSETS | 2026-06-01 | 2026-08-03T09:20:00+08:00 |
| structural.nbfi_bank_loans | 銀行對 NBFI 放款（LNFACBW027SBOG） | 2,004.99 十億美元（≈$2.00T） | FRED LNFACBW027SBOG | 2026-07-22 | 2026-08-03T09:20:00+08:00 |

### Coverage

| source_id | 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | 估值｜S&P 500 P/E and Shiller CAPE | multpl/gurufocus [primary: SEARCH] | ✓ SEARCH-VERIFIED（P/E 28.84、CAPE 40.91 @07-31） |
| valuation.mag7_multiples | 估值｜Mag 7 weighted P/E | advisorperspectives [SEARCH]（stock-of-state 沿用） | ✓ SEARCH-VERIFIED（溢價 ≈10% @07-09） |
| valuation.analyst_tp_decomposition | 估值｜Analyst TP upgrade decomposition | 賣方研報 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（MS NVDA $288 EPS-driven @07-13） |
| valuation.sp500_trend | 估值｜S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend（FRED SP500 派生） | ✓ API（dev200 +6.63%／dev52 +8.2%） |
| valuation.ai_credit_schism | 估值｜AI 信用定價分歧 | 信用市場 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Oracle CDS ≈200bp、CoreWeave CDS ≈675bp @07-30） |
| breadth.rsp_spy | 廣度｜S&P 500 equal-weight (RSP) vs cap-weight (SPY) | 247wallst [SEARCH] | ✓ SEARCH-VERIFIED（RSP +9.67% 領先 SPY +8.38% YTD @06-10） |
| breadth.top10_concentration | 廣度｜Top-10 concentration in S&P 500 | P&I/財經媒體 [SEARCH] | ✓ SEARCH-VERIFIED（≈40%，歷史高位 @07-02） |
| breadth.advance_decline | 廣度｜Advance/decline ratio, new high/low ratio | NQ100 breadth proxy [SEARCH] | ✓ SEARCH-VERIFIED（48% >50DMA、淨新高 ≈0.1% @07-29） |
| retail.fear_greed | 散戶｜CNN Fear & Greed Index | cnn.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（≈39 Fear @07-31） |
| retail.margin_debt | 散戶｜Margin Debt: FINRA | FINRA/Advisor Perspectives [SEARCH]（月頻 stock-of-state） | ✓ SEARCH-VERIFIED（$1.502T、+51.5% YoY、2026-06 創高） |
| retail.aaii | 散戶｜Retail survey: AAII Investor Sentiment | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（Bull 31.0%／Bear 42.1% @07-30） |
| retail.social_sentiment | 散戶｜Social sentiment proxies | WSB/cashtag [SEARCH]（best-effort） | ✗ NOT DISCLOSED（7 日窗內無具名迷因軋空） |
| retail.household_equity_allocation | 散戶｜Household equity allocation | fetch_macro.py BOGZ1FL153064486Q | ✓ API（45.76% @2026-Q1） |
| retail.naaim | 散戶｜NAAIM Exposure Index | naaim/YCharts [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（79.70 @07-29） |
| institutional.bofa_jpm_survey | 機構｜BofA Fund Manager Survey and JPM | 賣方調查 [SEARCH]（月頻，best-effort） | ✗ NOT DISCLOSED（7 月 FMS 早於前次基準、無本次新增） |
| monetary.fed_funds | 貨幣｜Fed funds rate: FRED DFEDTARU/DFEDTARL | fetch_macro.py FRED API | ✓ API（3.75%/3.50% @08-02） |
| monetary.hy_oas | 貨幣｜High Yield OAS | fetch_macro.py FRED API | ✓ API（2.84% @07-30，Δ 0，無新觀測） |
| monetary.ig_oas | 貨幣｜Investment Grade OAS | fetch_macro.py FRED API | ✓ API（0.80% @07-30，Δ 0） |
| monetary.dgs10 | 貨幣｜10Y Treasury yield | fetch_macro.py FRED API | ✓ API（4.68% @07-30，無新觀測） |
| monetary.dfii10 | 貨幣｜10Y Treasury real yield | fetch_macro.py FRED API | ✓ API（2.41% @07-30，無新觀測） |
| monetary.t10yie | 貨幣｜10Y breakeven inflation rate | fetch_macro.py FRED API | ✓ API（2.28% @07-31，Δ+1bps） |
| monetary.wti | 貨幣｜WTI crude oil price | fetch_macro.py FRED API | ✓ API（$84.25 @07-27，無新觀測） |
| monetary.cpi_yoy | 貨幣｜CPI YoY: FRED | fetch_macro.py FRED API（月頻） | ✓ API（3.46% @2026-06） |
| monetary.t5yifr | 貨幣｜5y5y forward inflation expectation | fetch_macro.py FRED API | ✓ API（2.30% @07-31，Δ 0） |
| monetary.term_premium | 貨幣｜10Y 期限溢價（term premium）: FRED | fetch_macro.py FRED API | ✓ API（0.8376% @07-24，+5.9bps trailing） |
| monetary.repo_stress_srf | 貨幣｜repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | fetch_macro.py repo_stress | ✓ API（SOFR−IORB 0bps、SOFR99−IORB +8bps、SRF ≈$0 @07-30/31） |
| monetary.treasury_auctions | 貨幣｜美債標售需求 | Reuters/Bloomberg recap [primary: SEARCH]（best-effort） | ✗ NOT DISCLOSED（14 日窗內無顯著標售 tail 具日期 recap） |
| monetary.fedwatch | 貨幣｜Fed funds rate path expectations | CME FedWatch [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（FOMC 鷹派持平、9 月路徑分歧 @07-30） |
| monetary.walcl | 貨幣｜Fed balance sheet: FRED WALCL | fetch_macro.py FRED API | ✓ API（$6.74T @07-29，無新觀測） |
| monetary.ecb_boj | 貨幣｜Global central bank liquidity cross-check | fetch_macro.py FRED API | ✓ API（€5.94T @07-24／¥639.55T @06-01） |
| monetary.pboc | 貨幣｜PBoC aggregate financing | Bloomberg [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（MLF 淨投放 ¥100B、6M 逆回購 ¥1.4T @07-24） |
| monetary.private_credit_liquidity | 貨幣｜Private-credit / non-bank fund liquidity stress | BDC 披露 [primary: SEARCH]（best-effort） | ✗ NOT DISCLOSED（BCRED gate 06-04 落窗外、7 月贖回轉緩、無新事件） |
| ai.hyperscaler_capex | AI｜Hyperscaler capex guidance | 季報 [SEARCH]（stock-of-state） | ✓ SEARCH-VERIFIED（合計 ≈$725B、仍上修 @07-28） |
| ai.token_growth | AI｜AI token volume growth rate | Anthropic/OpenAI/Google [SEARCH]（best-effort） | ✗ NOT DISCLOSED（本季無乾淨量化成長率披露） |
| ai.openai_anthropic_revenue | AI｜OpenAI / Anthropic annualized revenue | Epoch/報導 [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Anthropic ≈$47B／OpenAI ≈$25B run-rate @06-15） |
| ai.customer_concentration_rpo | AI｜Hyperscaler AI customer concentration | 財報電話 [primary: SEARCH]（best-effort） | ✗ NOT DISCLOSED（本次無乾淨窗內一手 RPO 披露） |
| ai.compute_supply_demand | AI｜AI compute supply/demand and overcapacity risk | TrendForce [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（DRAM +13–18% QoQ 3Q26 @07-03；供給仍被吸收） |
| ai.hyperscaler_financing_mix | AI｜Hyperscaler 融資結構 | 季報/發債 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI｜AI 營收對 capex 缺口 | 組合披露 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（年化 capex ≈$725B vs 終端營收 ≈$72B @06-15） |
| ai.depreciation_life | AI｜GPU / 伺服器折舊年限變動 | 10-K/10-Q [primary: SEARCH]（best-effort，30日） | ✗ NOT DISCLOSED（過去 30 日無新變更） |
| ai.capital_cycle | AI｜資本週期階段 | 供需增速+進出場事件 [SEARCH]（best-effort） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | 投機｜Search for past 7 days +AI rename/SPAC | [SEARCH] | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | 投機｜IPO market heat | Renaissance/valueaddvc [SEARCH] | ✓ SEARCH-VERIFIED（$251B/86 檔、JMKE 收平、aftermarket 弱 @08-01） |
| speculation.microcap_moonshots | 投機｜Microcap thematic moonshots | Finviz/Benzinga [primary: SEARCH]（required 週螢幕） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | 投機｜Upcoming AI IPOs | S-1/具名報導 [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（OpenAI ≈$1T IPO、Anthropic 續進 @07-28） |
| speculation.insider_form4 | 投機｜Insider selling at AI / market-leadership | SEC EDGAR [primary: EDGAR]（required） | ✓ SEARCH-VERIFIED（CoreWeave cluster：Intrator 07-21 ≈$24.07M） |
| speculation.equity_put_call | 投機｜Cboe equity-only put/call ratio | Cboe/YCharts [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（0.63 @07-31） |
| structural.leveraged_etf_aum | 結構｜US leveraged ETF AUM | cryptobriefing/etf.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（總 ≈$198B 創高 @07-23） |
| structural.us_single_stock_etf | 結構｜US single-stock leveraged ETF approvals | Leverage Shares/GlobeNewswire [SEARCH] | ✓ SEARCH-VERIFIED（6 檔 2x＋ELOL 發行 @07-30） |
| structural.global_leveraged_approvals | 結構｜Global leveraged product approvals | KRX/TWSE/JPX/ESMA [SEARCH]（best-effort，7日） | ✗ NOT DISCLOSED（韓國反收緊、本週擴散訊號未觸發） |
| structural.zero_dte | 結構｜0DTE option volume | Cboe [SEARCH]（Cboe 403） | ✓ SEARCH-VERIFIED（≈65%，Cboe Q2 @2026-05） |
| structural.options_volume | 結構｜Options total volume: OCC | theocc.com [SEARCH] | ✓ SEARCH-VERIFIED（6 月 16.0 億口 @07-02） |
| structural.cross_asset_derivatives | 結構｜Cross-asset derivatives / correlation checks | Saxo/Cboe [SEARCH] | ✓ SEARCH-VERIFIED（SKEW ≈139.9、VIX 17.09 contango @07-31） |
| structural.margin_debt_crosscheck | 結構｜Cross-reference only: FINRA margin debt | 交叉引用 D4（confirmation） | ✓ SEARCH-VERIFIED（$1.502T/+51.5% YoY，D4 引用不重複計分） |
| structural.ai_infrastructure_debt | 結構｜AI infrastructure debt financing / vendor-financing loops | [primary: SEARCH]（best-effort，30日） | ✓ SEARCH-VERIFIED（Nebius $775M 擔保、表外 >$120B @07-17） |
| structural.nbfi_bank_loans | 結構｜Bank loans to nondepository financial institutions | fetch_macro.py FRED API | ✓ API（$2.00T @07-22，無新觀測） |
| structural.treasury_basis_trade | 結構｜美債基差交易槓桿（Treasury basis-trade leverage） | script→WebSearch [primary: script]（best-effort） | ✗ NOT DISCLOSED（cftc/move/ofr script fetch_failed，MOVE ≈74 平靜、無 7 日窗內新事件） |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 trailing P/E 28.84 | S&P 500 trailing P/E August 2026 multpl | https://www.multpl.com/s-p-500-pe-ratio | 2026-07-31 | 2026-08-03T09:20:00+08:00 |
| valuation.sp500_pe_cape | Shiller CAPE 40.91 | Shiller CAPE ratio August 2026 multpl | https://www.multpl.com/shiller-pe | 2026-07-31 | 2026-08-03T09:20:00+08:00 |
| valuation.mag7_multiples | Mag 7 對其餘 493 檔溢價 ≈10% | Magnificent 7 valuation premium compressed 2026 | https://www.advisorperspectives.com/articles/2026/07/09/magnificent-sevens-weakness-become-problem-wall-street | 2026-07-09 | 2026-08-03T09:20:00+08:00 |
| valuation.analyst_tp_decomposition | Morgan Stanley NVDA 目標未擴張、目標價 $288（EPS-driven） | Morgan Stanley NVDA target 288 July 2026 EPS | https://www.gurufocus.com/news/8955458/morgan-stanley-upgrades-nvidia-nvda-with-a-288-target-price | 2026-07-13 | 2026-08-03T09:20:00+08:00 |
| valuation.ai_credit_schism | AI 雲端信用重定價：Oracle 5Y CDS ≈200bp、CoreWeave 5Y CDS ≈675bp、hyperscaler 債利差 ≈78bp | Oracle CoreWeave CDS AI credit repricing hyperscaler spread August 2026 | https://www.techtimes.com/articles/322222/20260730/coreweave-cds-hits-50-default-odds-bond-market-calls-time-gpu-debt-spiral.htm | 2026-07-30 | 2026-08-03T09:20:00+08:00 |
| breadth.rsp_spy | RSP 等權 YTD +9.67% 領先 SPY 市值權 +8.38% | RSP vs SPY equal weight YTD 2026 | https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ | 2026-06-10 | 2026-08-03T09:20:00+08:00 |
| breadth.top10_concentration | S&P 500 Top-10 集中度 ≈40% | S&P 500 top 10 concentration percent 2026 | https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/ | 2026-07-02 | 2026-08-03T09:20:00+08:00 |
| breadth.advance_decline | Nasdaq-100 廣度：48.0% >50DMA、63.7% >200DMA、10 日淨新高 ≈0.1% | Nasdaq 100 breadth percent above 50 day 200 day July 2026 | https://streetstats.finance/markets/breadth-momentum/NQ100 | 2026-07-29 | 2026-08-03T09:20:00+08:00 |
| retail.fear_greed | CNN Fear & Greed ≈39（Fear） | CNN Fear and Greed Index July 31 2026 | https://www.cnn.com/markets/fear-and-greed | 2026-07-31 | 2026-08-03T09:20:00+08:00 |
| retail.margin_debt | FINRA 6 月 margin debt $1.502T、YoY +51.5% | FINRA margin debt June 2026 YoY record | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-03T09:20:00+08:00 |
| retail.aaii | AAII Bear 42.1%／Neutral 26.9%／Bull 31.0% | AAII investor sentiment survey July 30 2026 | https://www.aaii.com/sentimentsurvey | 2026-07-30 | 2026-08-03T09:20:00+08:00 |
| retail.naaim | NAAIM 前值 84.02 → 最新 79.70 | NAAIM exposure index July 2026 | https://ycharts.com/indicators/naaim_number | 2026-07-29 | 2026-08-03T09:20:00+08:00 |
| monetary.fedwatch | FOMC 7/29 鷹派持平（9-3）、CME FedWatch 9 月路徑分歧 ≈63% | FOMC July 29 2026 hold FedWatch September cut probability | https://growbeansprout.com/tools/fedwatch | 2026-07-30 | 2026-08-03T09:20:00+08:00 |
| monetary.pboc | 人行 7/24 MLF 淨投放 ≈¥100B（5 個月最大） | PBoC MLF net injection liquidity July 2026 | https://www.bloomberg.com/news/articles/2026-07-24/pboc-adds-most-liquidity-to-economy-in-five-months-to-aid-growth | 2026-07-24 | 2026-08-03T09:20:00+08:00 |
| ai.hyperscaler_capex | hyperscaler 2026 capex 續上修：合計 ≈$725B（+77% YoY） | hyperscaler capex 2026 725B raised Meta Amazon Alphabet Microsoft | https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion | 2026-07-28 | 2026-08-03T09:20:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic run-rate ≈$47B、OpenAI ≈$25B | OpenAI Anthropic annualized revenue run-rate 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-06-15 | 2026-08-03T09:20:00+08:00 |
| ai.compute_supply_demand | 伺服器 DRAM 交期 30–40 週、3Q26 合約價續漲 +13–18% QoQ | DRAM contract price 3Q26 TrendForce lead time | https://www.trendforce.com/presscenter/news/20260703-13134.html | 2026-07-03 | 2026-08-03T09:20:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] top-5 capex 已超越 FCF、續靠外部融資、Amazon 遭 S&P 降至 BBB- | hyperscaler capex FCF debt Amazon downgrade BBB- 2026 | https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow | 2026-07-24 | 2026-08-03T09:20:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 五大 2026 發債 ≈$159B（+47% YoY） | hyperscaler bond issuance 159B 2026 AI credit | https://cryptobriefing.com/tech-giants-record-159b-bonds-ai/ | 2026-07-22 | 2026-08-03T09:20:00+08:00 |
| ai.revenue_capex_gap | AI 終端年化營收 ≈$72B（Anthropic ≈$47B＋OpenAI ≈$25B）vs 年化 capex ≈$725B | AI revenue to capex gap 2026 | https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-06-15 | 2026-08-03T09:20:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 螢幕合格件數 0 | AI rename SPAC no revenue IPO July 27 August 3 2026 | Reuters/Benzinga/Boardroom Alpha SPAC 螢幕 | 2026-08-03 | 2026-08-03T09:20:00+08:00 |
| speculation.ipo_heat | 2026 YTD 86 檔／募資 ≈$251B、JMKE 收平、aftermarket 轉弱 | US IPO market 2026 Jersey Mike's Cerebras aftermarket | https://valueaddvc.com/blog/ipo-market-2026-which-companies-are-going-public-and-what-the-window-looks-like | 2026-08-01 | 2026-08-03T09:20:00+08:00 |
| speculation.microcap_moonshots | 本週 microcap thematic moonshot 合格 0 件 | microcap 100% single day quantum AI fusion moonshot July August 2026 | Finviz/Benzinga/StockTwits/Yahoo movers 螢幕 | 2026-08-03 | 2026-08-03T09:20:00+08:00 |
| speculation.upcoming_ai_ipos | OpenAI 目標 ≈$1T IPO、Anthropic 續進 IPO 程序 | OpenAI Anthropic IPO timing 1 trillion July 2026 | https://www.benzinga.com/markets/private-markets/26/07/60739151/openai-1-trillion-ipo-ambition-faces-new-timing-test-as-anthropic-gains-ground | 2026-07-28 | 2026-08-03T09:20:00+08:00 |
| speculation.insider_form4 | CoreWeave 內部人 cluster：CEO Intrator 07-21 售 307,692 股 ≈$24.07M | CoreWeave insider Form 4 July 2026 Intrator SEC | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001769628&type=4 | 2026-07-21 | 2026-08-03T09:20:00+08:00 |
| speculation.equity_put_call | Cboe equity put/call 0.63 | Cboe equity put call ratio July 31 2026 | https://ycharts.com/indicators/cboe_equity_put_call_ratio | 2026-07-31 | 2026-08-03T09:20:00+08:00 |
| structural.leveraged_etf_aum | US 槓桿 ETF 總 AUM 創高 ≈$198B | leveraged ETF AUM record 2026 TQQQ SOXL | https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-07-23 | 2026-08-03T09:20:00+08:00 |
| structural.us_single_stock_etf | Leverage Shares 6 檔 2x 單股槓桿 ETF＋ELOL（TSLA+SpaceX）發行 | single-stock leveraged ETF launch July 2026 Leverage Shares ELOL | https://www.manilatimes.net/2026/07/30/tmt-newswire/globenewswire/two-industry-leaders-one-ticker-leverage-shares-by-themes-launches-elol/2395125 | 2026-07-30 | 2026-08-03T09:20:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 期權量 ≈65%（Cboe Q2 2026） | 0DTE SPX options share volume Cboe Q2 2026 | https://www.investing.com/news/company-news/cboe-q2-2026-slides-record-revenue-0dte-options-surge-to-65-of-spx-93CH-4828641 | 2026-05-31 | 2026-08-03T09:20:00+08:00 |
| structural.options_volume | OCC 6 月總量 16.0 億口 | OCC monthly options volume June 2026 | https://www.theocc.com/newsroom/views/2026/07-02-june-2026-monthly-volume-report | 2026-07-02 | 2026-08-03T09:20:00+08:00 |
| structural.cross_asset_derivatives | SKEW ≈139.9、VIX 17.09（term structure contango） | VIX SKEW term structure July 31 2026 | https://www.home.saxo/content/articles/options/index-up-average-stock-down---options-brief---31-july-2026-31072026 | 2026-07-31 | 2026-08-03T09:20:00+08:00 |
| structural.margin_debt_crosscheck | FINRA margin debt $1.502T、+51.5% YoY（交叉引用 D4） | FINRA margin debt June 2026 equity market cap | https://www.advisorperspectives.com/dshort/updates/2026/07/20/margin-debt-finra-june-2026 | 2026-07-20 | 2026-08-03T09:20:00+08:00 |
| structural.ai_infrastructure_debt | Nebius 07-17 完成首筆 $775M 擔保債務融資、GPU 基建擔保 | AI data center debt financing Nebius secured facility July 2026 | https://nebius.com/newsroom/nebius-raises-775-million-in-first-secured-debt-financing-to-accelerate-global-buildout | 2026-07-17 | 2026-08-03T09:20:00+08:00 |

## 本次分數存檔
```json
{
  "date": "2026-08-03",
  "iso_week": "2026-W32",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "valuation": 77,
  "breadth": 30,
  "speculation": 57,
  "retail": 47,
  "monetary": 76,
  "structural": 78,
  "total": 64,
  "tier": "警戒",
  "regime": "穩定共存",
  "trigger_state": "未擊發",
  "trigger_reasons": [],
  "monetary_side": "自滿側",
  "hy_oas_widening_streak": 0,
  "sp500_dev200_pct": 6.63
}
```

本報告為相對風險溫度計，非擇時訊號。

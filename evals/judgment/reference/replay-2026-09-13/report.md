# 2026-09-13 市場泡沫風險評估報告
> 報告日期：2026-09-13；執行日：2026-09-13 Asia/Taipei；ISO 週次：2026-W37；前次基準：report-2026-09-03（10天前）

**總評**：總分 63【警戒】（Δ 0）；扳機狀態：初啟；最貼近錨點：1997 早期建設（50%）。

## §1 六維度風險條圖
| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▱▱▱ | 75 | 76 | -1 |
| 市場廣度 | ▰▰▰▰▱▱▱▱▱▱ | 42 | 32 | +10 ⚠ |
| 投機行為 | ▰▰▰▰▱▱▱▱▱▱ | 48 | 55 | -7 |
| 散戶情緒 | ▰▰▰▰▱▱▱▱▱▱ | 46 | 44 | +2 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▰▱▱▱ | 79 | 76 | +3 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 77 | 78 | -1 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **63【警戒】** | 63 | 0 |

## §2 歷史錨點相似度
| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1973/1 Nifty Fifty 頂 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 1997 早期建設 | 50% | ▰▰▰▰▰▱▱▱▱▱ | ◀ 最貼近 |
| 1998 LTCM 衝擊 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 30% | ▰▰▰▱▱▱▱▱▱▱ |  |
| 2000/3 頂點 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 15% | ▰▱▱▱▱▱▱▱▱▱ |  |

## §3 三角訊號
| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,656.98 | ▼ -1.17%（前次 約 7,747.71） |
| WTI 原油 | $97.26 /bbl | ▲ +5.09%（前次 約 $92.55） |
| 10Y Treasury | 4.95% | ▲ +18 bps（前次 約 4.77%） |

**三者狀態**：出現分歧（股市在反向重新定價——WTI 與 10Y 同步上行，S&P 500 卻回落，能源／利率端的再通膨定價未被股市跟隨）。
- 股市：本次 7,656.98；較前次 ▼（-1.17%，前次 約 7,747.71）；距 200DMA +6.9%，未達 +10% 拉伸門檻。
- WTI 原油：本次 $97.26；較前次 ▲（+5.09%，前次 約 $92.55）。
- 10Y 殖利率：本次 4.95%；較前次 ▲（+18 bps，前次 約 4.77%）；主要驅動：三腿視窗不一致、不可判。
**格局轉變**：前次 穩定共存 轉為 本次 分歧——油與債同向上行而股價反向回落，原本的同步高位穩態被打破。
**10Y 成因拆解**：本次 ΔDGS10 +18 bps 為近月最大單次升幅，惟 ΔT10YIE 覆蓋與 DGS10／DFII10 不同視窗（`driver=unknown`），恆等式不跨視窗成立，故歸因為 不可判（視窗不一致）；三腿皆有新觀測、無 stale leg。
- ΔDGS10 名目殖利率週變動：+18 bps
- ΔDFII10 實質殖利率週變動：+13 bps
- ΔT10YIE 損益平衡通膨週變動：+1 bps
- 判定：不可判（視窗不一致）
**扳機鏈**：A 通膨鏈（油 → 通膨預期 → Fed 受限 → refinancing 成本）本次出現實質推進但未完成傳導——[monetary.cpi_yoy] CPIAUCSL yoy_pct=3.35 data_date=2026-08-01 顯示實現通膨自 3.3% 微升且仍低於 4%，[monetary.t5yifr] T5YIFR latest=2.32 delta_bps=-1 data_date=2026-09-11 顯示長端通膨預期不升反微降、仍被錨定；惟 WTI ▲ +5.09% 併同 CME FedWatch 隱含 9/16 FOMC 升息機率約 85.5%（2026-09-12），Fed put 的可得性本次明顯下降，屬本鏈中段（油價已推、預期未脫錨、政策端已轉緊）。B 槓桿鏈（財政風險再定價 → NBFI 去槓桿 → margin spiral → 國債市場失序 → 官方市場功能回應）未啟動——10Y 期限溢價（THREEFYTP10）0.8892%、週Δ 僅 +1.4 bps 遠低於 +15 bps 初啟門檻，repo 資金壓力（SOFR−IORB）-3 bps 為負、99th 尾差 +5 bps、SRF 動用 0，9/9 的 10Y 標售 bid-to-cover 2.71、indirect 79.2% 屬正常需求，且 `cftc_lev_funds`／`move_index`／`ofr_repo` 本次 fetch_failed、7 日窗內無具名基差／swap-spread 失序報導，故本鏈述為「本週無基差交易槓桿新證據」。
**扳機理由**：hy_streak
**結論**：扳機狀態：初啟——HY OAS 連續兩次運行走闊（2.65% → 2.70%，本次 +5 bps，持續 streak 達 2）觸發初啟判準；歷史意義在於：信用利差的絕對水位仍在循環低點（HY 2.70%／IG 0.80%，froth 未退），但方向已由收斂轉為連續走闊，且同時出現 Fed 由觀望轉向升息定價、10Y 升至 4.95%、油價續揚，屬「估值與槓桿位能已滿、融資環境開始由寬轉緊」的過渡配置；尚無私募信貸 gate proration／breach、無再融資或信用事件、無國債市場失序或官方市場功能回應，故未達已擊發。美債基差交易槓桿本週無新證據，槓桿鏈仍為乾柴而未點火。

## 六維度評分

### 1. 估值溢價 — 75（weight 22%，Δ -1）
- **Shiller CAPE** 約 40.73（2026-09-01，[GuruFocus](https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio)，source_ids=valuation.sp500_pe_cape）——自前次約 41.6 微降，仍是 1881 年以來次高、僅 1999–2000 曾更高，估值溢價維持極端。
- **Mag 7 加權前瞻本益比** 低於 24（2026-08-03，[CNBC](https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html)，source_ids=valuation.mag7_multiples）——MAGS ETF 前瞻 P/E 續處設立以來低檔，最貴族群仍在去評價（盈餘上修快於股價）。
- **價格趨勢偏離（Farrell #1/#2/#4）** S&P 500 距 200DMA +6.9%、距 52 週均 +8.33%（2026-09-11，FRED series=SP500，source_ids=valuation.sp500_trend）——偏離自前次 +7.5% 再收斂，價格拉伸程度下降，未達 +10% 門檻。
- **Excess CAPE Yield（ECY，跨時代校準）** 約 -0.10%（1/CAPE 40.73 − DFII10 2.55%/100；CAPE 資料日 2026-09-01、DFII10 資料日 2026-09-10，FRED series=DFII10，source_ids=valuation.sp500_pe_cape,monetary.dfii10）——本次由前次約 +0.03% 轉為負值，股相對抗通膨債已無風險溢酬，屬 1929／2000 級別讀數（confirmation，不主計分）。
- **hyperscaler capex reality check** 四大 2026 capex 合計約 725（十億美元，較 2025 年約 410 增 77%；Alphabet 上修至 180–190、Meta 上修至 125–145、Amazon 約 200）（2026-07-28，[CNBC](https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html)，source_ids=ai.hyperscaler_capex）——指引仍在上修、無下修跡象，屬估值支撐但脆弱性同步上升（capex 已超越合計 FCF，增額債務佔 capex 由 9% 升至約 32%）。
- **AI 營收對 capex 缺口** 年化 AI 終端營收約 105（十億美元；Anthropic 約 65 ＋ OpenAI 約 40）對年化 capex 約 725（分母：MSFT／GOOGL／AMZN／META top-4，Oracle 因本次無新季度披露未納入）（2026-08-17，[Axios](https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai)，source_ids=ai.revenue_capex_gap）——缺口約 1:7、與前次同量級且未收斂，回本假設持續後移，為估值風險的質化上修依據。
- **AI compute 供需 reality check** H100 中位租金約 3.38 美元／小時、合約價年增約 40%、Blackwell 約 48%，DRAM 5 月季上漲約 40%、8 月再升約 15%（2026-08-31，[Thunder Compute](https://www.thundercompute.com/blog/ai-gpu-rental-market-trends)，source_ids=ai.compute_supply_demand）——產能仍被利用率與付費需求吸收（供給緊、非過剩），本次為估值風險的減項而非加項。
- **AI 信用定價分歧（equity-vs-credit schism）** ✗ NOT DISCLOSED（source_ids=valuation.ai_credit_schism）——14 日窗（2026-08-30 起）內無具名 AI 信用重定價揭露；hyperscaler CDS 創高與 Oracle 5Y CDS 約 198 bps 屬 8 月中旬前事件（窗外背景，BIS Bulletin 120 方向一致），不納入計分。
- **分析師目標價拆解** ✗ NOT DISCLOSED（source_ids=valuation.analyst_tp_decomposition）——本季內雖有 Morgan Stanley 上修 NVDA／AVGO 目標價的報導，但未見可稽核的 EPS 修正對目標 PE 擴張拆解揭露，不納入計分。
- **折舊年限變動（盈餘品質）** ✗ NOT DISCLOSED（source_ids=ai.depreciation_life）——30 日窗內無新的 GPU／伺服器折舊年限或殘值假設變更披露，不納入計分。
- **backlog 重複計算風險（RPO double-counting）** ✗ NOT DISCLOSED（source_ids=ai.customer_concentration_rpo）——本次無同一 AI 終端客戶承諾被多家供應商同時入帳的具名金額披露，不納入計分。
- **hyperscaler 融資結構（capex vs FCF / 發債）** ✗ NOT DISCLOSED（source_ids=ai.hyperscaler_financing_mix）——季度狀態可沿用（capex 超越 FCF、增額債務佔 capex 約 32%），惟 30 日事件掃描無新的 hyperscaler 發債／SPV 融資披露，複合狀態不成立，不納入計分。
- **資本週期階段** ✗ NOT DISCLOSED（source_ids=ai.capital_cycle）——供給增速有據（capex 年增 77%）但需求側缺可引證的已實現增速 proxy，且 30 日內無新進入者／租約取消事件，增速證據不足，本次不判定週期階段、不納入計分。
- **AI token 成長** ✗ NOT DISCLOSED（source_ids=ai.token_growth）——本季無 Anthropic／OpenAI／Google 的新 token 量揭露，不納入計分。
**結論**：75 落於估值溢價高檔（CAPE 次高、ECY 轉負），較前次降 1——CAPE、趨勢偏離與 Mag 7 三項主計分輸入同步小幅鬆動，抵銷 ECY 轉負與 AI 回本缺口未收斂的上行壓力。

### 2. 市場廣度 — 42（weight 13%，Δ +10）
- **equal-weight 對 cap-weight（RSP/SPY）** RSP 至 7 月止 YTD 約 13（%）對 S&P 500 約 9%（2026-09-01，[24/7 Wall St.](https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/)，source_ids=breadth.rsp_spy）——等權續領先 cap-weight，是本維度唯一仍偏健康的訊號。
- **前十大集中度** 約 38（%）（2026-09-01，[24/7 Wall St.](https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/)，source_ids=breadth.top10_concentration）——自前次約 37.6% 續升、逼近紀錄，十檔皆為兆美元市值。
- **市場廣度（A/D 與新高新低）** S&P 500 成分股在 200 日均線之上約 53（%）；9/9 單日上漲家數僅 21.6%、下跌 75.9%，新高佔 1.5% 對新低 6.9%，NYSE 年度新低擴大至 331 檔、為去年 3–4 月修正以來最多（2026-09-11，[CondorEdge](https://condoredge.com/stocks/market-breadth)，source_ids=breadth.advance_decline）——新低明顯超過新高，短線廣度由「持平」轉為「負向」。
**結論**：42 落於明顯轉窄（41–60）下緣，較前次升 10——集中度創高且新高／新低比首次明確翻負、A/D 一面倒偏弱，僅等權 YTD 領先撐住上緣；本次為六維中唯一觸發 ⚠ 的位移。

### 3. 投機行為 — 48（weight 18%，Δ -7）
- **+AI 改名／SPAC** ✓ SEARCH-VERIFIED（0 件，source_ids=speculation.ai_rename_spac）——7 日窗（2026-09-06 起）掃描完成，無合格的 +AI 改名／代號變更或 SPAC 宣布事件（前次的 Paradium.AI／PAAI 為 8/31 生效、已出窗）。
- **IPO 熱度** 本週定價約 22（件；9/8 四件、9/9 兩件、9/10 十二件、9/11 四件，post-Labor Day 排程集中）（2026-09-11，[IPOScoop](https://www.iposcoop.com/current-year-pricings/)，source_ids=speculation.ipo_heat）——件數活躍但以中小型與非科技發行人為主，未見無營收 AI 發行人暴衝。
- **AI 領導股 insider 集中賣出** NVDA 董事 Mark A. Stevens 經家族信託分批出脫約 385（百萬美元）（2026-09-02，[SEC EDGAR Form 4](https://www.sec.gov/Archives/edgar/data/0001045810/000119903926000012/wk-form4_1788387031.xml)，source_ids=speculation.insider_form4）——落在 14 日窗內，AI 龍頭大額董事賣壓延續。
- **Cboe equity put/call** 約 0.67（2026-09-01，[thetrading.tools](https://www.thetrading.tools/put-call-ratio)，source_ids=speculation.equity_put_call）——自前次約 0.54 大幅回升至 0.60–0.70 區間，call 方向失衡明顯緩解，對應 rubric 21–40 級距。
- **microcap thematic moonshot** ✓ SEARCH-VERIFIED（0 件，source_ids=speculation.microcap_moonshots）（掃描窗 2026-09-06 起，資料日期 —）——7 日窗內無 <$1B 市值、季營收 ≤$5M 且疊 2＋ 熱門主題的單日 ≥100% 標的（Tenon Medical +77%、AEON Biopharma +35% 皆未達門檻且催化劑非主題堆疊）。
- **巨型 AI IPO pipeline** ✗ NOT DISCLOSED（source_ids=speculation.upcoming_ai_ipos）——30 日窗內無 OpenAI／Anthropic／xAI／SpaceX 的具名 S-1 或定價報導，不納入計分。
**結論**：48 落於投機升溫（41–60）下緣，較前次降 7——改名／SPAC 與 moonshot 雙雙 0 件、put/call 自 0.54 回升至 0.67 使方向性投機明顯降溫，僅 insider 集中賣出與活躍的 IPO 定價排程撐住分數。

### 4. 散戶情緒 — 46（weight 12%，Δ +2）
- **CNN Fear & Greed** 約 35（Fear）（2026-09-10，[CNN](https://www.cnn.com/markets/fear-and-greed)，source_ids=retail.fear_greed）——較前次 33.8 微升但仍在「恐懼」區，散戶風險胃納未回溫。
- **FINRA margin debt** 約 1.42（兆美元；7 月 MoM -5.7%、YoY +38.6%）（2026-07-31，[FINRA/dshort](https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026)，source_ids=retail.margin_debt）——8 月數據尚未發布，沿用 7 月月報（stock-of-state）；YoY 逼近但未破 +40% 的頂部級門檻。
- **AAII 投資人調查** 看多約 38.0（%）、看空 39.3%、中性 22.7%（2026-09-10，[AAII](https://www.aaii.com/sentimentsurvey)，source_ids=retail.aaii）——看多自前次 32.9% 明顯反彈並回到歷史均值 37.5% 之上，多空價差收斂至 -1.4%。
- **家庭股票配置** 約 48.23（% of 金融資產，2026-04-01 季，FRED series=BOGZ1FL153064486Q，source_ids=retail.household_equity_allocation）——新一季（Q2）自前季 45.76% 跳升至歷史高位附近，家庭部位已滿、後續加碼空間受限（Farrell #5）。
- **NAAIM 曝險指數** ✗ NOT DISCLOSED（source_ids=retail.naaim）——8/1 起轉訂閱制，本次無可公開稽核的當週值，不納入計分（confirmation cross-check，其缺值不得調降主分）。
- **社群投機（WSB／cashtag）** ✗ NOT DISCLOSED（source_ids=retail.social_sentiment）——7 日窗內無可稽核發布日期的具名迷因狂熱事件（GME／ORCL 提及上升屬即時追蹤器讀數、無固定發布日），不納入計分。
**結論**：46 落於 41–60 下緣，較前次升 2——AAII 看多反彈與家庭持股佔比跳升至 48.23% 推升結構性熱度，惟 F&G 仍在恐懼區、margin debt 自紀錄回落，整體僅小幅回溫。

### 5. 貨幣與信貸環境 — 79（weight 20%，Δ +3）
- **Fed funds 目標區間** 3.50–3.75%（上緣 3.75，2026-09-12，FRED series=DFEDTARU，source_ids=monetary.fed_funds）——會前維持不變，DFEDTARL 下緣同日為 3.50%。
- **FedWatch 政策路徑** 9/16 FOMC 升息 25 bps 機率約 85.5（%）（2026-09-12，[Yahoo Finance／CME FedWatch](https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html)，source_ids=monetary.fedwatch）——一週內自約 62% 跳升，市場定價已由「按兵不動」翻轉為「升息近乎定局」，降息機率 0%，本次為 D5 最重大的質變。
- **HY OAS** 2.70%（週Δ +5 bps，2026-09-10，FRED series=BAMLH0A0HYM2，source_ids=monetary.hy_oas）——仍接近循環低點，但連續兩次運行走闊使 `hy_oas_widening_streak` 達 2、觸發扳機初啟判準。
- **IG OAS** 0.80%（2026-09-10，FRED series=BAMLC0A0CM，source_ids=monetary.ig_oas）——較前次 0.81% 再收窄、續創史低區間，投資級信用自滿與 HY 的方向分歧並存。
- **CPI YoY** 3.35%（資料月 2026-08-01，FRED series=CPIAUCSL，source_ids=monetary.cpi_yoy）——8 月印出自 7 月 3.3% 微升、仍低於 4%，惟核心月增高於市場預期，是 Fed 升息定價翻轉的直接觸媒。
- **5y5y forward（T5YIFR）** 2.32%（週Δ -1 bps，2026-09-11，FRED series=T5YIFR，source_ids=monetary.t5yifr）——長端通膨預期不升反微降，仍被良好錨定，是本次通膨鏈尚未完成傳導的關鍵證據。
- **10Y 期限溢價（term premium）** 0.8892%（週Δ +1.4 bps，2026-09-04，FRED series=THREEFYTP10，source_ids=monetary.term_premium）——Kim-Wright 三因子模型；僅小升、遠低於 +15 bps 的槓桿鏈初啟門檻，財政風險再定價尚未啟動。
- **repo 資金壓力（SOFR−IORB）與 SRF 動用** SOFR 3.62%、SOFR−IORB -3 bps、99th 尾差 +5 bps、SRF 動用 0（as_of 2026-09-10，FRED series=SOFR，source_ids=monetary.repo_stress_srf）——利差為負、尾差溫和、SRF 零動用，secured-funding 完全無壓力，非扳機側證據。
- **美債標售需求（auction tail / bid-to-cover）** 9/9 的 10Y 標售得標利率 4.834%、bid-to-cover 約 2.71、indirect 承接 79.2%（2026-09-09，[TheVaultReport](https://thevaultreport.com/treasury-auctions)，source_ids=monetary.treasury_auctions）——需求正常、無明顯 tail，財政供給壓力尚未反映在標售端（confirmation，不主計分）。
- **Fed 資產負債表（WALCL）** $6.74T（6,740,619 百萬美元，2026-09-09，FRED series=WALCL，source_ids=monetary.walcl）——週增約 34 億美元、大致持平，準備金環境未收緊。
- **ECB 資產（ECBASSETSW）** €5.91T（5,912,178 百萬歐元，2026-09-04，FRED series=ECBASSETSW，source_ids=monetary.ecb_boj）——週減約 32 億歐元，歐元區流動性緩步收縮。
- **BOJ 資產（JPNASSETS）** ¥644.66T（6,446,620 億日圓，2026-08-01，FRED series=JPNASSETS，source_ids=monetary.ecb_boj）——月頻、本次無新觀測，資產負債表持平。
- **PBoC 流動性** 社會融資規模 1–7 月約 22.25（兆人民幣，年減 1.74 兆；7 月新增人民幣貸款罕見負增約 -3,400 億）（2026-08-15，[SteelOrbis](https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm)，source_ids=monetary.pboc）——8 月數據尚未發布、沿用最新月報；中國信用脈衝續縮但央行維持「充裕」操作（confirmation，全球流動性交叉檢核）。
- **私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）** ✗ NOT DISCLOSED（source_ids=monetary.private_credit_liquidity）——30 日窗（2026-08-14 起）內無新的 gate proration / breach、redemption-request ratio 惡化或 net inflow→outflow flip 披露；Q2 的 BCRED 閘門與 Blue Owl tender proration 屬窗外背景，不納入計分、不觸發扳機。
**結論**：扳機側；HY OAS 連續兩次運行走闊（streak 2）已觸發初啟判準，且 CME FedWatch 隱含升息機率跳升至約 85.5%、10Y 升至 4.95%、WTI ▲ +5.09%，融資環境的方向已由寬轉緊；79 較前次升 3（仍在 61–80 上緣）——IG 0.80% 的極端自滿與初啟的融資收緊在雙向計分下同時推高分數，但 repo／期限溢價／標售三項壓力指標皆正常，尚未達 81–100 的擊發級。

### 6. 結構性槓桿 — 77（weight 15%，Δ -1）
- **槓桿 ETF AUM** 單一個股槓桿 ETF 規模約 40.74（十億美元；611 檔／18 家發行人，當週淨流出約 7.51 億美元），全體槓桿 ETF 仍約 $198B 紀錄水位（2026-09-08，[ETF Action](https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/)，source_ids=structural.leveraged_etf_aum）——本次首見 TSLA／NVDA 槓桿部位淨贖回，槓桿需求邊際降溫。
- **0DTE 佔比** 約 62（%）SPX 期權量（8 月創紀錄，日均約 240 萬口）（2026-08-31，[Cboe](https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august)，source_ids=structural.zero_dte）——續處 55–65% 區間上緣、方向性投機強度未退。
- **OCC 期權總量** 8 月總結算量約 1.44（十億口，YoY +14.4%；股票期權 7.249 億口 YoY +30.3%、ETF 期權 4.281 億口）（2026-08-31，[Traders Magazine](https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/)，source_ids=structural.options_volume）——量能續創高檔。
- **跨資產衍生性** VIX 於 9/10 收在約 17（點）以上、為 28 個交易日以來首見，VIX 三個月 call skew 升至歷史第 91 百分位，MOVE 續處高檔（2026-09-10，[CNBC](https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html)，source_ids=structural.cross_asset_derivatives）——尾部避險需求明顯轉貴，惟近端無失序（confirmation）。
- **VIX/S&P 500 同向檢測** comove=false（VIX 17.84、vix_chg +24.58%、sp500_chg -2.01%；as_of 2026-09-10、base_date 2026-09-03、window_days 7，FRED series=VIXCLS，source_ids=structural.vix_spx_comove）——指數回落而 VIX 大漲，屬正常負相關避險、非 crowded-optionality 同漲，不上調級距。
- **AI 基礎建設債務融資／vendor-financing loops** Qualcomm 對 Amazon 發行可認購 2,500 萬股、總額約 4（十億美元）的認股權證，與 Amazon 最高約 600 億美元的 AI 資料中心晶片採購承諾掛鉤（2026-09-08，[CNBC](https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html)，source_ids=structural.ai_infrastructure_debt）——供應商以自身股權對價換取客戶採購承諾，屬 30 日窗內新的 circular／vendor-financing 具名事件，結構槓桿的加項。
- **銀行對 NBFI 放款（LNFACBW027SBOG）** $2.03T（2,027.98 十億美元，週持平、無新觀測，2026-09-02，FRED series=LNFACBW027SBOG，source_ids=structural.nbfi_bank_loans）——bank–NBFI 曝險水位未再擴張（confirmation，不主計分）。
- **美國單一個股槓桿 ETF 核准／上市** ✓ SEARCH-VERIFIED（0 件，source_ids=structural.us_single_stock_etf）（掃描窗 2026-08-14 起，資料日期 —）——30 日窗內 SEC EDGAR／ETF.com 掃描完成，無新的美國單一個股槓桿 ETF 核准或上市。
- **margin debt 交叉檢核** margin debt 約 1.42（兆美元，2026-07-31，[Current Market Valuation](https://www.currentmarketvaluation.com/models/margin-debt.php)，source_ids=structural.margin_debt_crosscheck）——margin debt／股票市值比率僅作交叉檢核，主計分留在 D4（confirmation，不主計分）。
- **全球槓桿產品擴散** ✗ NOT DISCLOSED（source_ids=structural.global_leveraged_approvals）——7 日窗內韓／台／日／歐皆無英文具名單一個股槓桿核准（韓國自 8/2 起新上市審查仍壅塞），本週擴散訊號未觸發，不納入計分。
- **美債基差交易槓桿（Treasury basis-trade leverage）** ✗ NOT DISCLOSED（source_ids=structural.treasury_basis_trade）——script 的 `cftc_lev_funds`／`move_index`／`ofr_repo` 三區塊本次 fetch_failed，且 7 日窗內無具名基差／swap-spread 失序平倉或國債市場失序報導，不納入計分。
**結論**：77 落於高度集中（61–80）上緣，較前次降 1——單一個股槓桿 ETF 首見淨流出、擴散訊號未觸發、comove=false 使部位面降溫，僅 Qualcomm／Amazon 的 circular financing 新事件與 0DTE 62%、OCC 量能續高撐住水位。

## 綜合分數

| 維度 | 權重 | 分數 | 加權分數 |
|---|---:|---:|---:|
| 估值溢價 | 22% | 75 | 16.50 |
| 市場廣度 | 13% | 42 | 5.46 |
| 投機行為 | 18% | 48 | 8.64 |
| 散戶情緒 | 12% | 46 | 5.52 |
| 貨幣與信貸環境 | 20% | 79 | 15.80 |
| 結構性槓桿 | 15% | 77 | 11.55 |

加權總分：63.47 → 63【警戒】
邊界帶：總分 63 距 警戒/高 邊界 ≤ 2 分，評分固有噪音約 ±2–3，等級判讀需保留餘地。

## 歷史泡沫週期對比

相似度計算：checklist v2
- 1973/1 Nifty Fifty 頂：命中 3/8 = 40%
- 1997 早期建設：命中 4/8 = 50%
- 1998 LTCM 衝擊：命中 3/8 = 40%
- 1999 晚期狂熱：命中 3/10 = 30%
- 2000/3 頂點：命中 3/8 = 40%
- 2021/12 Meme 頂：命中 1/8 = 15%
2000/3 高位回落條件：否

**1973/1 Nifty Fifty 頂 feature audit**
- 1973.1｜未命中｜source_ids=—｜估值溢價 75 < 80
- 1973.2｜未命中｜source_ids=—｜市場廣度 42 < 60
- 1973.3｜未命中｜source_ids=—｜CPIAUCSL yoy_pct 3.35% < 4
- 1973.4｜未命中｜source_ids=—｜T5YIFR 週Δ -1 bps < 0（通膨預期微降）
- 1973.5｜命中｜source_ids=—｜DCOILWTICO chg_pct +5.09% ≥ 0.5
- 1973.6｜未命中｜source_ids=—｜decomposition.driver=unknown ≠ breakeven
- 1973.7｜命中｜source_ids=—｜扳機狀態 初啟 ≥ 初啟
- 1973.8｜命中｜source_ids=—｜散戶情緒 46 < 55（機構主導、散戶未狂熱）

**1997 早期建設 feature audit**
- 1997.1｜未命中｜source_ids=—｜估值溢價 75 不在 40–74
- 1997.2｜命中｜source_ids=—｜市場廣度 42 < 45
- 1997.3｜命中｜source_ids=—｜投機行為 48 < 50
- 1997.4｜命中｜source_ids=ai.hyperscaler_capex｜hyperscaler capex 指引仍上修（2026 合計約 725、年增 77%）
- 1997.5｜命中｜source_ids=—｜散戶情緒 46 < 55
- 1997.6｜未命中｜source_ids=—｜結構性槓桿 77 ≥ 50
- 1997.7｜未命中｜source_ids=—｜HY OAS 2.70% < 4 但週Δ +5 bps > 0（本次走闊）
- 1997.8｜未命中｜source_ids=—｜扳機狀態 初啟 ≠ 未擊發

**1998 LTCM 衝擊 feature audit**
- 1998.1｜未命中｜source_ids=structural.cross_asset_derivatives｜HY 週Δ +5 bps < 30 且 VIX 17.84 < 25，無 cross-asset 衝擊事件
- 1998.2｜未命中｜source_ids=—｜S&P 500 週變動 -1.17% > -5
- 1998.3｜無資料｜source_ids=—｜私募信貸與基差槓桿本次皆無窗內具名壓力事件
- 1998.4｜未命中｜source_ids=monetary.fedwatch｜FedWatch 隱含升息機率約 85.5%，Fed 路徑轉鷹非轉鴿
- 1998.5｜命中｜source_ids=—｜估值溢價 75 ≥ 60
- 1998.6｜命中｜source_ids=—｜扳機狀態 初啟 ≥ 初啟
- 1998.7｜命中｜source_ids=—｜市場廣度 Δ +10 ≥ 8（急轉弱）
- 1998.8｜未命中｜source_ids=—｜ΔT10YIE +1 bps > 0（通膨預期非下行）

**1999 晚期狂熱 feature audit**
- 1999.1｜命中｜source_ids=—｜估值溢價 75 ≥ 75
- 1999.2｜命中｜source_ids=valuation.sp500_pe_cape｜Shiller CAPE 約 40.73 ≥ 38
- 1999.3｜未命中｜source_ids=—｜投機行為 48 < 60
- 1999.4｜未命中｜source_ids=speculation.microcap_moonshots,speculation.ipo_heat｜本週 moonshot 0 件，且 IPO 定價雖多但無無營收發行人佔比偏高的揭露
- 1999.5｜未命中｜source_ids=—｜市場廣度 42 < 45
- 1999.6｜未命中｜source_ids=—｜D5 為扳機側（非自滿側）
- 1999.7｜命中｜source_ids=—｜結構性槓桿 77 ≥ 60
- 1999.8｜未命中｜source_ids=—｜散戶情緒 46 < 55
- 1999.9｜無資料｜source_ids=—｜巨型 AI IPO pipeline 30 日內無具名 S-1／定價
- 1999.10｜未命中｜source_ids=—｜扳機狀態 初啟 ≠ 未擊發

**2000/3 頂點 feature audit**
- 2000.1｜未命中｜source_ids=—｜估值溢價 75 < 85
- 2000.2｜命中｜source_ids=—｜扳機狀態 初啟 ≥ 初啟
- 2000.3｜未命中｜source_ids=—｜市場廣度 42 < 60
- 2000.4｜未命中｜source_ids=—｜前次 dev200 7.5% ≤ 10 且 S&P 週變動 -1.17% > -5（高位回落不成立）
- 2000.5｜未命中｜source_ids=—｜投機行為 48 < 70
- 2000.6｜命中｜source_ids=speculation.insider_form4｜14 日內合格 Form 4 集中賣出 ≥ 1（NVDA 董事約 3.85 億美元）
- 2000.7｜未命中｜source_ids=—｜散戶情緒 46 < 65
- 2000.8｜命中｜source_ids=monetary.fedwatch｜FedWatch 隱含 9/16 升息機率約 85.5%、降息機率 0%，貨幣轉緊成立

**2021/12 Meme 頂 feature audit**
- 2021.1｜未命中｜source_ids=—｜散戶情緒 46 < 65
- 2021.2｜無資料｜source_ids=—｜社群投機（WSB／cashtag）本次無可稽核發布日期的具名標的
- 2021.3｜命中｜source_ids=—｜結構性槓桿 77 ≥ 65
- 2021.4｜未命中｜source_ids=—｜D5 79 ≥ 60 但側別為扳機側、非自滿側
- 2021.5｜未命中｜source_ids=retail.margin_debt｜margin debt YoY +38.6% < 40
- 2021.6｜未命中｜source_ids=speculation.microcap_moonshots｜本週 microcap moonshot 0 件
- 2021.7｜未命中｜source_ids=—｜市場廣度 42 < 50
- 2021.8｜未命中｜source_ids=—｜CPIAUCSL yoy_pct 3.35% < 4

本次六維組態最貼近「1997 早期建設」（50%）：估值偏高但 Mag 7 續去評價、廣度偏窄、capex 指引仍上修、散戶偏冷——屬泡沫循環的建設期，惟 1997 型態本身已因結構性槓桿 77 與扳機轉初啟而失去兩項特徵（1997.6／1997.8 皆未命中），相似度未升。真正的位移在第二順位：1998 型態由前次 15% 躍升至 40%，來源是市場廣度單次 Δ +10 的急轉弱、估值仍 ≥60、扳機進入初啟三項同時成立；換言之，配置正由「建設期的高位穩態」向「衝擊前夕」滑移，而非向 1999／2021 的狂熱型態靠攏（兩者本次分別僅 30%／15%，且雙雙因 D5 轉扳機側而失去自滿側特徵）。循環位置判讀為「建設期末端、首度出現融資收緊的方向性證據」：估值與槓桿位能已積累多時，本次首見 HY OAS 連續走闊與 Fed 升息定價翻轉，屬扳機鏈 A 的中段推進；但 5y5y forward 週Δ -1 bps 仍被錨定、CPI YoY 3.35% < 4%，不符 1973.3／1973.4 的雙重命中條件，故不得援引「Fed 寬鬆空間受壓縮」的定性，且扳機理由未含 `breakeven_wti_up`、扳機鏈 A 尚未驗證啟動。結構性槓桿的期間調整對比：相對 1999／2000 年 3 月的 margin debt 與指數期貨／選擇權投機，本次對應物為 0DTE 佔比 62%、槓桿 ETF 約 $198B 與單一個股槓桿 40.74；相對 2021 年 12 月的迷因槓桿，本次社群投機面明顯缺席（✗ NOT DISCLOSED、moonshot 0 件），這正是 2021 型態僅 15% 的主因。

跨期價格錨（敘事用，不重算）：S&P 500 距 200 日均線 +6.9%、距 52 週均 +8.33%，屬溫和拉伸；長期相對指數成長趨勢偏離的文章錨點為 Dot-com 約 95%、1929 約 110%、當前 AI 週期約 147%（RIA/Farrell），僅作跨時代敘事對照。投資泡沫宏觀錨（narrative only，BIS AER 2026 Ch I）：AI 投資週期與運河熱（1830s）、英國鐵路狂熱（1840s）、1920s 電氣化、dot-com 並列——真實技術突破吸引超過商業回報所能支撐的資本，且均以投資反轉收場；規模上 AI 相關投資約占美國 GDP 1%、IT 投資合計約 5% 已超越 2000 年峰值。BIS contest model（Rungcharoenkitkul 2026b，經 AER Ch I Graph 11.B 引用）指出 winner-take-all 結構使理性廠商也會過度承諾 capex，累計 capex 由約 $2trn 走向約 $4.5trn 時全行業淨經濟剩餘轉負。歷史細部類比錨（narrative only）：1999–2001 光纖／電信週期與當前 AI 投資週期結構最近——vendor financing 與 IRU capacity swap 使同一筆收入被多方重複認列，本次 Qualcomm 以約 40 億美元認股權證交換 Amazon 最高 600 億美元採購承諾，正是該型態的現代版對應。

## 機構情緒對照

本次無新機構調查數據。（BofA 9 月 Global Fund Manager Survey 通常於 9 月中旬發布、晚於本報告日；最新可引述者為 7 月 FMS 的現金水位 3.6%，已早於前次基準。）

另補 NAAIM Exposure Index：最新可公開取得值仍為 79.70（2026-07-29，[MacroMicro](https://en.macromicro.me/series/20540/naaim-exposure-index)）——8/1 起轉訂閱制，近期週值不可公開稽核，僅作背景（於 D4 為 confirmation cross-check，本次 ✗ NOT DISCLOSED 不計分）。

## 本次新增訊號

各維度變化 vs 前次（10天前）（基準 report-2026-09-03）：
- 估值溢價 76→75（-1）：CAPE 41.6→40.73、距 200DMA +7.5%→+6.9%、Mag 7 續去評價；惟 ECY 由約 +0.03% 轉為約 -0.10%（首度轉負，1929／2000 級別讀數），AI 年化終端營收約 $105B 對年化 capex 約 $725B 的缺口未收斂。
- 市場廣度 32→42（+10 ⚠）：本次唯一觸發 ⚠ 的位移——前十大集中度 37.6%→約 38%、200DMA 之上佔比約 53%，9/9 上漲家數 21.6% 對下跌 75.9%、新高 1.5% 對新低 6.9%，NYSE 年度新低擴大至 331 檔為今年 3–4 月修正以來最多。
- 投機行為 55→48（-7）：+AI 改名／SPAC 與 microcap moonshot 雙雙 0 件、Cboe equity put/call 自約 0.54 回升至約 0.67（方向失衡緩解）；僅 NVDA 董事約 3.85 億美元 Form 4 賣出與本週約 22 件 IPO 定價撐住。
- 散戶情緒 44→46（+2）：AAII 看多 32.9%→38.0% 回到歷史均值之上、家庭股票配置新一季自 45.76% 跳升至 48.23%；F&G 33.8→約 35 仍在恐懼區。
- 貨幣與信貸環境 76→79（+3）：**側別由自滿側轉為扳機側**——HY OAS 2.65%→2.70%（+5 bps）使 `hy_oas_widening_streak` 達 2、觸發 `hy_streak` 初啟判準；CME FedWatch 9/16 升息機率約 85.5%（一週前約 62%）、降息機率 0%；10Y 4.77%→4.95%（+18 bps）、WTI +5.09%。分數雖僅 +3，質變在於側別翻轉而非幅度：IG OAS 0.80% 的極端自滿仍撐住水位，故雙向計分下 Δ 偏小、不足以反映融資方向的轉折。
- 結構性槓桿 78→77（-1）：單一個股槓桿 ETF 約 $40.74B、當週淨流出約 7.51 億美元（首見 TSLA／NVDA 槓桿部位贖回）；VIX 9/10 收破 17 為 28 個交易日首見、三個月 call skew 升至第 91 百分位；新增 Qualcomm 對 Amazon 約 40 億美元認股權證／最高 600 億美元採購承諾的 circular financing 事件。
- 私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）：本次 ✗ NOT DISCLOSED，30 日窗內無新的 gate proration / breach、redemption-request ratio 惡化或 net inflow→outflow flip。
- 美債基差交易槓桿（Treasury basis-trade leverage）：本次 ✗ NOT DISCLOSED，script 三區塊 fetch_failed 且 7 日窗內無具名國債市場失序（Treasury market dysfunction）事件。
- 格局：穩定共存 → 分歧；扳機狀態：未擊發 → 初啟（理由 hy_streak）。
全球槓桿產品擴散：本週擴散訊號未觸發（韓國新上市審查自 8/2 起仍壅塞；台／日／歐 7 日窗內無英文具名核准）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | S&P 500 sp500_trend latest | 7,656.98 | FRED series=SP500 | 2026-09-11 | 2026-09-13T09:29:59+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 6.9 | FRED series=SP500 | 2026-09-11 | 2026-09-13T09:29:59+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 8.33 | FRED series=SP500 | 2026-09-11 | 2026-09-13T09:29:59+08:00 |
| valuation.sp500_trend | sp500_trend prior_spot | 7,747.71 | FRED series=SP500 | 2026-09-03 | 2026-09-13T09:29:59+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest | 48.23 | FRED series=BOGZ1FL153064486Q | 2026-04-01 | 2026-09-13T09:29:59+08:00 |
| monetary.fed_funds | DFEDTARU latest | 3.75 | FRED series=DFEDTARU | 2026-09-12 | 2026-09-13T09:29:59+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.50 | FRED series=DFEDTARL | 2026-09-12 | 2026-09-13T09:29:59+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 2.70 | FRED series=BAMLH0A0HYM2 | 2026-09-10 | 2026-09-13T09:29:59+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.80 | FRED series=BAMLC0A0CM | 2026-09-10 | 2026-09-13T09:29:59+08:00 |
| monetary.dgs10 | DGS10 latest | 4.95 | FRED series=DGS10 | 2026-09-10 | 2026-09-13T09:29:59+08:00 |
| monetary.dfii10 | DFII10 latest | 2.55 | FRED series=DFII10 | 2026-09-10 | 2026-09-13T09:29:59+08:00 |
| monetary.t10yie | T10YIE latest | 2.36 | FRED series=T10YIE | 2026-09-11 | 2026-09-13T09:29:59+08:00 |
| monetary.wti | DCOILWTICO latest | 97.26 | FRED series=DCOILWTICO | 2026-09-09 | 2026-09-13T09:29:59+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct | 3.35 | FRED series=CPIAUCSL | 2026-08-01 | 2026-09-13T09:29:59+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.32 | FRED series=T5YIFR | 2026-09-11 | 2026-09-13T09:29:59+08:00 |
| monetary.term_premium | THREEFYTP10 latest | 0.8892 | FRED series=THREEFYTP10 | 2026-09-04 | 2026-09-13T09:29:59+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.62 | FRED series=SOFR | 2026-09-10 | 2026-09-13T09:29:59+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.70 | FRED series=SOFR99 | 2026-09-10 | 2026-09-13T09:29:59+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.65 | FRED series=IORB | 2026-09-13 | 2026-09-13T09:29:59+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest | 0.0 | FRED series=RPONTTLD | 2026-09-11 | 2026-09-13T09:29:59+08:00 |
| monetary.walcl | WALCL latest | 6,740,619（$6.74T，百萬美元） | FRED series=WALCL | 2026-09-09 | 2026-09-13T09:29:59+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,912,178（€5.91T，百萬歐元） | FRED series=ECBASSETSW | 2026-09-04 | 2026-09-13T09:29:59+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,446,620（¥644.66T，億日圓） | FRED series=JPNASSETS | 2026-08-01 | 2026-09-13T09:29:59+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 17.84 | FRED series=VIXCLS | 2026-09-10 | 2026-09-13T09:29:59+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 17.84 | FRED series=VIXCLS,SP500 | 2026-09-10 | 2026-09-13T09:29:59+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2,027.98（$2.03T，十億美元） | FRED series=LNFACBW027SBOG | 2026-09-02 | 2026-09-13T09:29:59+08:00 |

### Coverage

| source_id | 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 P/E and Shiller CAPE | WebSearch（multpl/GuruFocus） | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Analyst TP upgrade decomposition | WebSearch（best-effort，90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ai_credit_schism | AI 信用定價分歧 | WebSearch（best-effort，14d） | ✗ NOT DISCLOSED |
| breadth.rsp_spy | S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | CNN Fear & Greed Index | WebSearch（CNN） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Margin Debt: FINRA | WebSearch（FINRA/dshort） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Social sentiment proxies | WebSearch（best-effort，7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Household equity allocation | scripts/fetch_macro.py（FRED） | ✓ API |
| retail.naaim | NAAIM Exposure Index | WebSearch（best-effort） | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | BofA Fund Manager Survey | WebSearch（best-effort） | ✗ NOT DISCLOSED |
| monetary.fed_funds | Fed funds rate: FRED | scripts/fetch_macro.py（FRED DFEDTARU/DFEDTARL 均 ok） | ✓ API |
| monetary.hy_oas | High Yield OAS | scripts/fetch_macro.py（FRED） | ✓ API |
| monetary.ig_oas | Investment Grade OAS | scripts/fetch_macro.py（FRED） | ✓ API |
| monetary.dgs10 | 10Y Treasury yield | scripts/fetch_macro.py（FRED） | ✓ API |
| monetary.dfii10 | 10Y Treasury real yield | scripts/fetch_macro.py（FRED） | ✓ API |
| monetary.t10yie | 10Y breakeven inflation rate | scripts/fetch_macro.py（FRED 直抓 ok，未走 derived） | ✓ API |
| monetary.wti | WTI crude oil price | scripts/fetch_macro.py（FRED） | ✓ API |
| monetary.cpi_yoy | CPI YoY: FRED | scripts/fetch_macro.py（FRED，yoy_pct） | ✓ API |
| monetary.t5yifr | 5y5y forward inflation expectation | scripts/fetch_macro.py（FRED） | ✓ API |
| monetary.term_premium | 10Y 期限溢價（term premium）: FRED | scripts/fetch_macro.py（FRED） | ✓ API |
| monetary.repo_stress_srf | repo 資金壓力（SOFR−IORB）與 SRF 動用: FRED | scripts/fetch_macro.py（FRED，SOFR/SOFR99/IORB/RPONTTLD 四腿均 ok） | ✓ API |
| monetary.treasury_auctions | 美債標售需求 | WebSearch（best-effort，14d） | ✓ SEARCH-VERIFIED |
| monetary.fedwatch | Fed funds rate path expectations | WebSearch（CME FedWatch，best-effort） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Fed balance sheet: FRED | scripts/fetch_macro.py（FRED） | ✓ API |
| monetary.ecb_boj | Global central bank liquidity cross-check | scripts/fetch_macro.py（FRED ECBASSETSW/JPNASSETS 均 ok） | ✓ API |
| monetary.pboc | PBoC aggregate financing | WebSearch（gov.cn/NBS 轉載，best-effort） | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Private-credit / non-bank fund liquidity stress | WebSearch（best-effort，30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | Hyperscaler capex guidance | WebSearch（Q2 2026 財報，stock-of-state） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI token volume growth rate | WebSearch（best-effort） | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | OpenAI / Anthropic annualized revenue | WebSearch（best-effort） | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | Hyperscaler AI customer concentration | WebSearch（best-effort） | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI compute supply/demand and overcapacity risk | WebSearch（best-effort） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | Hyperscaler 融資結構 | WebSearch（composite：季度狀態＋30 日事件掃描） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI 營收對 capex 缺口 | WebSearch（best-effort，季頻沿用） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | GPU / 伺服器折舊年限變動 | WebSearch（best-effort，30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | 資本週期階段 | WebSearch（composite：季度狀態＋30 日事件掃描） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Search for past 7 days | WebSearch（7d 掃描） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | IPO market heat | WebSearch（IPOScoop／Renaissance） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Microcap thematic moonshots | WebSearch（7d 掃描） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Upcoming AI IPOs | WebSearch（best-effort，30d） | ✗ NOT DISCLOSED |
| speculation.insider_form4 | Insider selling at AI | SEC EDGAR / WebSearch（14d） | ✓ SEARCH-VERIFIED |
| speculation.equity_put_call | Cboe equity-only put/call ratio | WebSearch（best-effort） | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | US leveraged ETF AUM | WebSearch（ETF Action／etf.com） | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | US single-stock leveraged ETF approvals | SEC EDGAR / ETF.com（30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Global leveraged product approvals | WebSearch（7d，best-effort） | ✗ NOT DISCLOSED |
| structural.zero_dte | 0DTE option volume | WebSearch（Cboe） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Options total volume | WebSearch（OCC） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Cross-asset derivatives / correlation checks | WebSearch | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | VIX / S&P 500 co-movement | scripts/fetch_macro.py（FRED VIXCLS＋SP500） | ✓ API |
| structural.margin_debt_crosscheck | Cross-reference only: FINRA margin debt | WebSearch（confirmation） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | AI infrastructure debt financing / vendor-financing loops | WebSearch（30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED H.8） | ✓ API |
| structural.treasury_basis_trade | 美債基差交易槓桿（Treasury basis-trade leverage） | script 三區塊 fetch_failed ＋ WebSearch（7d） | ✗ NOT DISCLOSED |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.73 | S&P 500 Shiller CAPE ratio current September 2026 multpl | https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio | 2026-09-01 | 2026-09-13T10:45:00+08:00 |
| valuation.mag7_multiples | Mag 7 前瞻本益比低於 24 | Magnificent 7 forward P/E valuation September 2026 | https://www.cnbc.com/2026/08/03/mag-7-etf-falls-to-record-low-valuation-its-a-great-buy-here-say-analysts.html | 2026-08-03 | 2026-09-13T10:45:00+08:00 |
| breadth.rsp_spy | RSP 至 7 月止 YTD 報酬約 13 | RSP equal weight vs SPY S&P 500 YTD performance September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/ | 2026-09-01 | 2026-09-13T10:45:00+08:00 |
| breadth.top10_concentration | 前十大集中度約 38 | S&P 500 top 10 concentration percentage September 2026 | https://247wallst.com/investing/2026/09/01/ten-stocks-are-now-38-of-the-sp-500-these-3-etfs-are-the-escape-hatch/ | 2026-09-01 | 2026-09-13T10:45:00+08:00 |
| breadth.advance_decline | 成分股在 200 日均線之上約 53 | market breadth advance decline new highs lows September 2026 percent stocks above 200-day | https://condoredge.com/stocks/market-breadth | 2026-09-11 | 2026-09-13T10:45:00+08:00 |
| retail.fear_greed | Fear Greed 恐懼約 35 | CNN Fear and Greed Index today September 2026 reading | https://www.cnn.com/markets/fear-and-greed | 2026-09-10 | 2026-09-13T10:45:00+08:00 |
| retail.margin_debt | margin debt 約 1.42 兆美元 | FINRA margin debt August 2026 record year over year | https://www.advisorperspectives.com/dshort/updates/2026/08/20/margin-debt-finra-july-2026 | 2026-07-31 | 2026-09-13T10:45:00+08:00 |
| retail.aaii | AAII 看多約 38.0 | AAII sentiment survey results week September 10 2026 bullish bearish neutral | https://www.aaii.com/sentimentsurvey | 2026-09-10 | 2026-09-13T10:45:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.71 | Treasury auction results September 2026 tail bid-to-cover 10-year | https://thevaultreport.com/treasury-auctions | 2026-09-09 | 2026-09-13T10:45:00+08:00 |
| monetary.fedwatch | 9/16 FOMC 升息機率約 85.5 | CME FedWatch September 12 2026 probability 25 basis point hike | https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html | 2026-09-12 | 2026-09-13T10:45:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate financing 2026 total social financing | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm | 2026-08-15 | 2026-09-13T10:45:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 725 | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-07-28 | 2026-09-13T10:45:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65 | OpenAI Anthropic annualized revenue run rate September 2026 | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai | 2026-08-17 | 2026-09-13T10:45:00+08:00 |
| ai.compute_supply_demand | H100 中位租金約 3.38 | GPU rental price HBM DRAM contract price September 2026 utilization | https://www.thundercompute.com/blog/ai-gpu-rental-market-trends | 2026-08-31 | 2026-09-13T10:45:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 增額債務佔 capex 約 32 | hyperscaler capex vs free cash flow debt issuance 2026 | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-07-28 | 2026-09-13T10:45:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收約 105 | AI revenue vs capex gap 2026 annualized run rate | https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai | 2026-08-17 | 2026-09-13T10:45:00+08:00 |
| speculation.ipo_heat | 本週 IPO 定價約 22 | IPO priced week September 8 2026 first day return debut | https://www.iposcoop.com/current-year-pricings/ | 2026-09-11 | 2026-09-13T10:45:00+08:00 |
| speculation.insider_form4 | 董事 Stevens 出脫約 385 百萬美元 | insider selling Form 4 September 2026 Nvidia AI executives SEC filing | https://www.sec.gov/Archives/edgar/data/0001045810/000119903926000012/wk-form4_1788387031.xml | 2026-09-02 | 2026-09-13T10:45:00+08:00 |
| speculation.equity_put_call | equity put/call 約 0.67 | Cboe equity put call ratio September 2026 reading | https://www.thetrading.tools/put-call-ratio | 2026-09-01 | 2026-09-13T10:45:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.74 | leveraged ETF assets under management September 2026 record single stock | https://www.etfaction.com/traders-pull-751m-from-single-stock-etfs-shedding-levered-tech-bets/ | 2026-09-08 | 2026-09-13T10:45:00+08:00 |
| structural.zero_dte | SPX 0DTE 佔比創紀錄約 62 | 0DTE options share SPX volume September 2026 Cboe record | https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august | 2026-08-31 | 2026-09-13T10:45:00+08:00 |
| structural.options_volume | 8 月總結算量約 1.44 十億口 | OCC options volume August 2026 monthly report | https://www.tradersmagazine.com/news/occ-august-2026-monthly-volume-data/ | 2026-08-31 | 2026-09-13T10:45:00+08:00 |
| structural.cross_asset_derivatives | VIX 收在約 17 以上、call skew 第 91 百分位 | fear gauge VIX hedges September 10 2026 volatility | https://www.cnbc.com/2026/09/10/fear-gauge-vix-hedges-volatility-stocks.html | 2026-09-10 | 2026-09-13T10:45:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 1.42 兆美元 | margin debt to market cap 2026 | https://www.currentmarketvaluation.com/models/margin-debt.php | 2026-07-31 | 2026-09-13T10:45:00+08:00 |
| structural.ai_infrastructure_debt | Qualcomm 對 Amazon 認股權證約 4 十億美元 | Qualcomm warrants Amazon 4 billion AI infrastructure deal September 2026 | https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html | 2026-09-08 | 2026-09-13T10:45:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement September 7-13 2026 | 檢查來源：SPACInsider、Businesswire SPAC newsroom、Boardroom Alpha（窗內無合格事件） | — | 2026-09-13T10:45:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（0 件符合 2+ 主題×弱基本面） | biggest stock gainers week September 7 2026 microcap 100% quantum AI | 檢查來源：Finviz、Benzinga、StockTitan、Yahoo movers（Tenon +77%、AEON +35% 皆未達門檻） | — | 2026-09-13T10:45:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval September 2026 | 檢查來源：SEC EDGAR、ETF.com 新上市 feed（窗內無合格核准或上市） | — | 2026-09-13T10:45:00+08:00 |

## 本次分數存檔
```json
{
  "date": "2026-09-13",
  "iso_week": "2026-W37",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "valuation": 75,
  "breadth": 42,
  "speculation": 48,
  "retail": 46,
  "monetary": 79,
  "structural": 77,
  "total": 63,
  "tier": "警戒",
  "regime": "分歧",
  "trigger_state": "初啟",
  "trigger_reasons": ["hy_streak"],
  "monetary_side": "扳機側",
  "hy_oas_widening_streak": 2,
  "sp500_dev200_pct": 6.9
}
```

本報告為相對風險溫度計，非擇時訊號。

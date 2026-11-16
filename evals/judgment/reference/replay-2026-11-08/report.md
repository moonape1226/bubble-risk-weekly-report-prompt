# 2026-11-08 市場泡沫風險評估報告
> 報告日期：2026-11-08；執行日：2026-11-08 Asia/Taipei；ISO 週次：2026-W45；前次基準：report-2026-10-18（21天前）

**總評**：總分 61【警戒】（Δ -5）；扳機狀態：已擊發；最貼近錨點：1998 LTCM 衝擊（50%）。

## §1 六維度風險條圖
| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▱▱▱ | 75 | 76 | -1 |
| 市場廣度 | ▰▰▰▰▱▱▱▱▱▱ | 48 | 56 | -8 |
| 投機行為 | ▰▰▰▱▱▱▱▱▱▱ | 32 | 44 | -12 ⚠ |
| 散戶情緒 | ▰▰▱▱▱▱▱▱▱▱ | 28 | 42 | -14 ⚠ |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▰▰▱▱ | 82 | 85 | -3 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▰▱▱ | 82 | 80 | +2 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **61【警戒】** | 66 | -5 |

## §2 歷史錨點相似度
| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1973/1 Nifty Fifty 頂 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 1997 早期建設 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 1998 LTCM 衝擊 | 50% | ▰▰▰▰▰▱▱▱▱▱ | ◀ 最貼近 |
| 1999 晚期狂熱 | 50% | ▰▰▰▰▰▱▱▱▱▱ |  |
| 2000/3 頂點 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |

## §3 三角訊號
| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,353.73 | ▼ -3.99%（前次 ≈7,659.44） |
| WTI 原油 | $99.64 /bbl | ▼ -7.92%（前次 ≈$108.21） |
| 10Y Treasury | 4.84% | ▼ -25 bps（前次 ≈5.09%） |

**三者狀態**：穩定共存（三者本次方向一致皆為下行、無一項反向重新定價，且 S&P 500 距 200DMA 僅 +0.42%、遠未達 +10% 拉伸門檻，故機器判定為穩定共存）。必須明說此標籤的機械性：契約的「分歧」只定義為 ▲／▼ 混合，本次是三者同步下行的 risk-off 收縮，方向一致但絕非風險下降——質變發生在三角之外的波動率與 AI 信用，見下方扳機理由與 D5／D6。
- 股市：本次 **7,353.73**（2026-11-05）；較前次 ▼ -3.99%（前次 ≈7,659.44，2026-10-16）；距 200DMA 自前次 +5.34% 壓縮至 +0.42%，價格拉伸幾乎全數回吐，11/05 單日 AI 類股重挫為主要路徑。
- WTI 原油：本次 **$99.64**（2026-11-03）；較前次 ▼ -7.92%（前次 ≈$108.21，2026-10-16）；跌破百元、為三角中跌幅最大者，通膨鏈的上游推力明確轉弱。
- 10Y 殖利率：本次 **4.84%**（2026-11-05）；較前次 ▼ -25 bps（前次 ≈5.09%，2026-10-16）；主要驅動因素：三腿視窗不一致、不可判（惟 ΔDFII10 -14 bps 與 ΔT10YIE -12 bps 幅度相近，實質利率與通膨預期同步回落）。
**格局轉變**：前次 穩定共存 維持為 本次 穩定共存——標籤未變，但內涵由「股持平、油債小升的收斂」轉為「三者同步下行的 risk-off」，背離壓力進一步由三角內部移往波動率與 AI 信用利差。
**10Y 成因拆解**：ΔDGS10 -25 bps，而 ΔDFII10 -14 bps、ΔT10YIE -12 bps；惟 ΔT10YIE 的觀測視窗（2026-11-06）與 DGS10／DFII10（2026-11-05）不同，`driver=unknown`，恆等式不跨視窗成立，故歸因判定為 不可判（視窗不一致）；三腿皆有新觀測、無 stale leg。方向上實質利率與損益平衡通膨同幅下行，屬避險性全曲線下移而非單一成因主導。
- ΔDGS10 名目殖利率週變動：-25 bps
- ΔDFII10 實質殖利率週變動：-14 bps
- ΔT10YIE 損益平衡通膨週變動：-12 bps
- 判定：不可判（視窗不一致）
**扳機鏈**：A 通膨鏈（油 → 通膨預期 → Fed 受限 → refinancing 成本）本次明確退火——[monetary.cpi_yoy] CPIAUCSL yoy_pct=3.72 data_date=2026-09-01 的 9 月實現通膨與前次相同（10 月 CPI 排定 11/10 公布、本次尚無新印），而 [monetary.t5yifr] T5YIFR latest=2.17 delta_bps=-16 data_date=2026-11-06 顯示 5y5y forward 長端通膨預期自 2.33% 大幅回落 16 bps、錨定更紮實；WTI ▼ -7.92% 跌破百元、ΔT10YIE -12 bps 同步下行，上游與預期兩端同時轉弱，本鏈的三個環節無一在推進。須注意 Fed 政策端方向與本鏈相反：FedWatch 隱含 12 月升息機率 76.8%（2026-11-06），政策受限來自就業數據而非能源通膨，故不得由本鏈推論「Fed 寬鬆空間受壓縮」。B 槓桿鏈（衝擊：財政風險再定價 → NBFI 去槓桿 → margin spiral → 國債市場失序 → 官方市場功能回應）未啟動——10Y 期限溢價（THREEFYTP10）0.9089%、週Δ -2.7 bps 為下行，遠低於 +15 bps 初啟門檻，財政再定價本次不是衝擊源；repo 資金壓力（SOFR−IORB）+2 bps、99th 尾差 +10 bps、SRF 動用 0，secured funding 無壓力；`cftc_lev_funds`／`move_index`／`ofr_repo` 三區塊本次 fetch_failed，WebSearch fallback 取得 MOVE 93.88（2026-11-04、自 11/03 的 99.97 回落、低於 10/05 的 113.60 高點）與槓桿型投資人基差名目部位自年初約 $1.26trn 降至約 $900bn 的縮減報導，且 7 日窗內無具名基差／swap-spread 失序平倉或國債市場失序報導，故本鏈述為乾柴反而在減少、未點火。本次的擊發來自 AI 複合體的具名再融資壓力與 HY OAS 的連續走闊，而非上述兩鏈的傳導節點。
**扳機理由**：refinancing_credit_event、hy_streak
⚠ **結論**：扳機狀態：已擊發——契約的「具名再融資壓力或信用事件披露」判準由 AI 複合體直接滿足（`refinancing_credit_event`）：CoreWeave 2031 年到期債殖利率升破 16%（2026-11-06）、五年期信用違約交換 11/05 一度突破 1,289 bps，荷蘭國際集團（ING）同日被報導正出售 12 筆、約 $500M 的資料中心貸款以減持風險，AI 投資級債利差約 148 bps 對其餘市場約 77 bps；同時 `hy_oas_widening_streak` 累進至 4、連續走闊判準（`hy_streak`）續成立。歷史意義在於：這次與前次的擊發性質不同——前次是 HY OAS 單期 +58 bps 的速度擊發（`hy_oas_fired`，本次 +17 bps 已不成立），本次是**具名發行人的再融資價格**擊發，壓力由指數層級的利差下沉到個別資產負債表，對應 §2 最貼近的 1998 型態（衝擊已至、尚未演成系統性失序）。限制條件須明說：私募信貸 gate proration / breach 本次無窗內可稽核揭露、國債市場失序（Treasury market dysfunction）與官方市場功能回應（official market-functioning backstop）皆未出現、repo 與期限溢價雙雙無壓力、HY／IG 絕對水位（3.48%／0.93%）仍處循環低位，故本次仍為「AI 信用單點擊發」而非全面 financing crisis；且三角的通膨鏈同步退火、S&P 500 拉伸幾乎歸零，位能面已明顯洩壓。

## 六維度評分

### 1. 估值溢價 — 75（weight 22%，Δ -1）
- **Shiller CAPE** **38.91**（2026-11-06，[multpl](https://www.multpl.com/shiller-pe)，source_ids=valuation.sp500_pe_cape）——自前次約 40.54 回落約 4%，仍處 1881 年以來次高區間（均值 17.45、僅 1999–2000 曾更高），回落幅度遠不足以改變估值溢價的極端定性。
- **S&P 500 本益比** **25.14** 倍（2026-11-06，[multpl](https://www.multpl.com/s-p-500-pe-ratio)，source_ids=valuation.sp500_pe_cape）——與 CAPE 同步小幅收斂，但仍在長期區間上緣，盈餘尚未追上價格。
- **Excess CAPE Yield（ECY，跨時代校準）** 約 **-0.03**%（1/CAPE 38.91 − DFII10 2.60%/100；CAPE 資料日 2026-11-06、DFII10 資料日 2026-11-05，FRED series=DFII10，source_ids=valuation.sp500_pe_cape,monetary.dfii10）——仍為負值但自前次約 -0.31% 收斂至近乎零，主因是實質利率自 2.74% 降至 2.60%（-14 bps）而非股價便宜；股相對抗通膨債的風險溢酬仍不存在，屬 1929／2000 級別讀數（confirmation，不主計分）。
- **Mag 7 前瞻本益比** 群體約 **28.3** 倍對 S&P 500 約 21.8 倍、對除 Mag 7 之外約 19.7 倍（2026-10-13，[Vested Finance](https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/)，source_ids=valuation.mag7_multiples）——最貴族群相對溢價約 1.3 倍，本次 AI 類股重挫主要壓縮的是價格而非估值分母，溢價結構未解除。
- **價格趨勢偏離 (Farrell #1/#2/#4)** S&P 500 距 200DMA **+0.42**%、距 52 週均 +1.84%（2026-11-05，FRED series=SP500，source_ids=valuation.sp500_trend）——自前次 +5.34% 壓縮至 +0.42%，均值回歸的下行位能本次幾乎全數釋放，是本維度最明確的減項，也是總分下行的主要來源之一。
- **hyperscaler capex reality check** 微軟將 2026 年 capex 指引自約 175 下調至約 **170**（十億美元；四大合計指引約 720–745，Alphabet 維持 195–205、Amazon 重申約 220、Meta 收窄至 135–145）（2026-10-29，[Global Data Center Hub](https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex)，source_ids=ai.hyperscaler_capex）——**本循環首見 hyperscaler 下修 capex 指引**（原因為第三方算力交付延後、容量遞延至 2027 上半年）；依本維度判準，capex 指引一旦開始被下修，即使本益比不變估值風險亦顯著上升，是本次最重要的質化加項。
- **AI 營收對 capex 缺口（revenue-to-capex gap）** 年化 AI 終端營收：Anthropic 65 ＋ OpenAI 約 70，合計約 **135**（十億美元）對年化 capex 約 730（分母：MSFT／GOOGL／AMZN／META top-4 ＋ Oracle 季頻指引）（2026-09-30，[Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html)，source_ids=ai.revenue_capex_gap）——缺口約 1:5.4，較前次的 1:6.3 小幅收斂（分子自約 115 升至約 135），但量級未改變；回本假設仍後移，且本次信用市場已開始對「回本前的利息負擔」直接定價（stock-of-state carry-forward，逐組件標註資料日期）。
- **AI compute 供需 reality check** H100 隨選租金中位數 **3.87** 美元／小時（46 家供應商中位數，四週 +11%、一年 +30%；Nebius 於 10/01 將 H100 由 3.85 調升至 4.50、H200 由 4.50 調升至 5.40；DRAM／NAND 報價年內漲 200–400%、HBM 續緊）（2026-11-03，[GetDeploying GPU Price Trends](https://getdeploying.com/gpu-price-trends)，source_ids=ai.compute_supply_demand）——租金與記憶體價同步上行、供給仍緊，產能尚被付費需求吸收；惟本次未取得直接利用率證據，依判準只能述為「capex 與租金仍支撐，但未取得直接利用率證據」，為估值風險的減項而非加項。
- **hyperscaler 融資結構（capex vs FCF / 發債）** 今年以來 hyperscaler 發債約 **296**（十億美元，Goldman Sachs 估，約占投資級公司債供給 9%；10/29 起一週內 5 筆 AI 相關發行合計 67，2027 年預估約 440 再加專案層級約 300）（2026-11-06，[404k Research](https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era)，source_ids=ai.hyperscaler_financing_mix）——發債規模已遠超 Goldman 年初約 250 的基線預估，capex 自 2024–25 年起持續超越 FCF，英國央行亦警示自由現金流收縮正把 hyperscaler 推向表外融資；同一份 capex 指引的脆弱性隨債務占比上升而加大（confirmation，不主計分）。
- **AI 信用定價分歧（equity-vs-credit schism）** CoreWeave 五年期信用違約交換 11/05 一度突破 **1,289** bps（盤後回落至約 1,155，11/10 財報前；2031 年到期債殖利率升破 16%、債價跌至約 79.5；Oracle 五年期約 308 bps 創高且 7 月已被 S&P 降至投資級最低一級）（2026-11-05，[Coinpaper](https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds)，source_ids=valuation.ai_credit_schism）——分歧本次由「信用端先行確認」進一步惡化為「信用端價格已進入壓力區」：信貸對 AI 複合體的重定價幅度明確大於股權，屬 BIS Bulletin 120 所述兩個市場只有一個是對的之後期訊號（confirmation，不主計分）。
- **資本週期階段（capital cycle stage）** 微軟 10 月取消 Nscale 英國資料中心交易，規模約 **3**（十億美元；同時放棄西維吉尼亞 1.35 GW 意向書、拒絕擴大德州合約，並對 Nebius／IREN／Nscale 三家 neocloud 專案加強審查，衛星影像顯示 IREN 德州園區與 Nebius 紐澤西約 140 MW 可能遞延至 2027）（2026-11-04，[Reuters via Investing.com](https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281)，source_ids=ai.capital_cycle）——30 日事件掃描首度出現密集的租約取消／專案延後與進場者退場，屬週期轉折訊號、估值風險上修；惟供給側與需求側皆缺可引證的同期增速，增速證據不足，本次不判定週期階段（複合狀態 quarterly_state:not_disclosed、event_scan:ok，僅事件腿納入判讀）。
- **backlog 重複計算風險（RPO double-counting）** Oracle 剩餘履約義務 **638**（十億美元，報導稱約半數來自 OpenAI；OpenAI 自身財報揭露之採購承諾約 665，含 Broadcom 約 350、Microsoft Azure 約 250、Nvidia 系統約 100）（2026-08-31，[The Motley Fool](https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/)，source_ids=ai.customer_concentration_rpo）——同一終端客戶的承諾同時支撐多家供應商的 backlog，而可支付的終端現金流只有一份（OpenAI 年化營收約 70 對承諾約 665），屬光纖時代 IRU capacity swap 的現代版營收品質訊號；Nvidia 執行長已公開稱其中約 100 從未構成承諾（confirmation，不主計分）。
- **分析師目標價拆解（TP-upgrade phase signal）** Bernstein 將 TSMC 目標價由 554 上調至 **600** 美元並維持 Outperform（2026-11-03，[StockAnalysis](https://stockanalysis.com/stocks/tsm/)，source_ids=valuation.analyst_tp_decomposition）——本季（2026-Q4）內唯一取得的合格上調；該檔 forward PE 約 26 倍、上調主要繫於 CoWoS 與 2nm 2027 年初調價的 EPS 路徑，無法判定為 multiple-driven，且僅一檔不足以構成「2 檔以上 bellwether 同步多重擴張」的晚期循環訊號，本次不作加分。
- **折舊年限變動（盈餘品質）** ✗ NOT DISCLOSED（source_ids=ai.depreciation_life）——30 日窗內無新的 GPU／伺服器折舊年限或殘值假設變更披露；既有的 Nebius 自 4 年延長至 5 年（2026 年 1 月起）、Meta 5.5 年、Amazon 縮短至 5 年均屬窗外背景，不納入計分。
- **AI token 成長** ✗ NOT DISCLOSED（source_ids=ai.token_growth）——本季（2026-Q4）無 Anthropic／OpenAI／Google 的新 token 量揭露；Google 於 I/O 2026 揭露的每月 3.2 千兆 token 屬窗外背景，不納入計分。
**結論**：75 落於估值溢價高檔，較前次降 1——CAPE 40.54→38.91、距 200DMA +5.34%→+0.42% 兩項主計分輸入同步鬆動，但幾乎被三項質化上修完全抵銷：微軟本循環首度下修 capex 指引、30 日內密集的資料中心取消／延後事件、以及 AI 信用利差已進入具名壓力區。

### 2. 市場廣度 — 48（weight 13%，Δ -8）
- **equal-weight 對 cap-weight（RSP/SPY）** RSP 年初至今報酬約 **14.13**% 對 SPY 約 8.67%（2026-11-06，[TotalRealReturns](https://totalrealreturns.com/n/RSP,SPY)，source_ids=breadth.rsp_spy）——等權領先 cap-weight 約 5.5 個百分點，權值股主導的狹窄領導在本次 AI 重挫中明確斷裂，是本維度最大的減項。
- **前十大集中度** 約 **37.9**%（2026-11-01，[Chartrow](https://chartrow.com/sp500/concentration)，source_ids=breadth.top10_concentration）——自 2025 年 12 月約 40.7% 的高點回落，但仍遠高於 2000 年 3 月的歷史泡沫水位，結構性集中度未解除，是分數無法進一步下行的主因。
- **市場廣度（A/D）** 11/06 紐交所上漲家數 1,474 對下跌 **1,252**（淨 +222；上漲量能約 28.9 億股對下跌約 27.5 億股）（2026-11-06，[McClellan Market Breadth](https://www.mcoscillator.com/market_breadth_data/)，source_ids=breadth.advance_decline）——週線最後一個交易日廣度轉正、晶片與 AI 股同步反彈（NVDA +3.9%、AMD +10.8%），惟那斯達克仍連續第四週收跌，且 Saxo 報告的隱含相關性創歷史新高 20.93 顯示個股正趨同移動，廣度的改善帶有 risk-off 齊跌齊漲的性質。
**結論**：48 落於明顯轉窄（41–60）下緣，較前次降 8——RSP 以 14.13% 對 8.67% 大幅領先、11/06 上漲家數淨 +222，兩項主計分輸入自前次的「指數與廣度背離」明顯修復；僅前十大集中度仍約 37.9% 與隱含相關性創高把分數留在 41–60 區間而未落入 21–40。

### 3. 投機行為 — 32（weight 18%，Δ -12）
- **+AI 改名／SPAC** 7 日窗內合格事件 **1** 件——Agility Robotics 完成與 Churchill Capital Corp XI 的合併並於 11/05 以 AGLT 掛牌納斯達克，同週另有 Football Manager SPAC（FBLLU）以每單位 10 美元募 1 億美元、3 家 SPAC 遞交初次申報（2026-11-04，[Securities.io](https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/)，source_ids=speculation.ai_rename_spac）——SPAC 管道仍運作但規模小、無 +AI 改名事件，屬零星投機而非狂熱。
- **IPO 熱度** 本週美國僅 1 檔 IPO 定價：Narragansett Bancorp（NARA）募 9,100 萬美元、市值 2.12 億、週漲 **8**%（近 100 檔 IPO 累計 42 漲／56 跌／2 平；Q3 約三分之一低於區間定價、平均首日後轉為水下）（2026-11-06，[Renaissance Capital](https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears)，source_ids=speculation.ipo_heat）——唯一新股是社區銀行而非無營收題材股、且 IPO 窗口被描述為「market fears」下的清淡開局，無營收發行人佔比並未偏高。
- **microcap thematic moonshot** ✓ SEARCH-VERIFIED（0 件，source_ids=speculation.microcap_moonshots）（掃描窗 2026-11-01 起，資料日期 —）——7 日窗內無 <$1B 市值、季營收 ≤$5M 且疊 2＋ 熱門主題的單日 ≥100% 標的（Zapata Quantum 的 +52% 與 Xanadu 的 +30% 皆為窗外且未達門檻）。
- **巨型 AI IPO pipeline** Anthropic 於 10/26 遞交 S-1，據華爾街日報報導目標估值 1.5 兆至 **2** 兆美元、代號 ANT 掛納斯達克、募資規模上限達 1,000 億美元，目標 11 月中（11/16 當週，一說 11/19–11/20）掛牌（2026-10-26，[Built In](https://builtin.com/articles/anthropic-ipo-filing-s1)，source_ids=speculation.upcoming_ai_ipos）——30 日窗內具名且已遞交公開 S-1，為史上規模最大的 IPO 之一，屬流動性抽離風險與晚期循環標記，是本維度唯一的明確加項、也是分數未落入 21–40 下半的主因。
- **AI 領導股 insider 集中賣出** ✓ SEARCH-VERIFIED（0 件，source_ids=speculation.insider_form4）（掃描窗 2026-10-25 起，資料日期 —）——14 日窗內 SEC EDGAR 的 NVDA Form 4 檢索無符合契約要求的具名申報人、交易日與金額等 filing-level 細節；Protos 統計 5–10 月九家 AI 公司內部人出售 73.9 億美元、Mark Stevens 個人 13.5 億美元皆為窗外彙總，依規定不得引用。
- **Cboe equity put/call** **1.05**（2026-11-05，[Seeking Alpha](https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide)，source_ids=speculation.equity_put_call）——升破 1.0、且被報導為高於 2025 年 4 月關稅日的讀數，遠高於 rubric 的 0.70 低投機門檻；方向失衡完全翻轉為買權重於賣權的對立面，是本次最強的投機降溫證據。
**結論**：32 落於零星投機（21–40）上緣，較前次降 12 並觸發 ⚠——equity put/call 自低檔直接翻轉至 1.05、moonshot 與 insider 兩項篩選 0 件、IPO 市場僅一檔社區銀行定價且近百檔累計 42 漲對 56 跌，四項主計分輸入同時指向 21–40；僅 Anthropic 近 2 兆美元估值的 S-1 與零星 SPAC 管道撐住上緣。

### 4. 散戶情緒 — 28（weight 12%，Δ -14）
- **CNN Fear & Greed** **22**（Extreme Fear）（2026-11-06，[Finhacker](https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/)，source_ids=retail.fear_greed）——自一週前的 26 續降至極度恐懼區（盤中一度 20），低於 rubric 的 25 門檻，散戶風險胃納處於 0–20 級距，是本維度最大的下行推力。
- **FINRA margin debt** 約 1.48 兆美元（月增 1.8%、YoY 約 **+31.4**%；6 月紀錄 1.502 兆，7 月創史上最大單月降幅至 1.417 兆後回升）（2026-09-30，[The Trading Tools](https://www.thetrading.tools/margin-debt)，source_ids=retail.margin_debt）——10 月數據預計 11 月第三週才發布，沿用 9 月月報（stock-of-state）；YoY 雖高但已明確低於 +40–50% 的 1999／2007／2021 頂部級門檻，且絕對水位低於 6 月紀錄約 1.5%。
- **AAII 投資人調查** 看多 34.1%、看空 **48.4**%（多空價差 -14.3%；看空月增 6.9 個百分點、連續 39 週高於 31.5% 均值，中性 17.5% 連 35 週低於均值）（2026-11-04，[AAII Insights](https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives)，source_ids=retail.aaii）——看多已低於 37.5% 的歷史均值、看空接近 50%，散戶調查落在 0–20 級距。
- **家庭股票配置** **48.23**（% of 金融資產，2026-04-01 季，FRED series=BOGZ1FL153064486Q，source_ids=retail.household_equity_allocation）——季頻、本次無新一季揭露，沿用 Q1 2026 水位；仍在歷史高位附近，家庭部位已滿、後續加碼空間受限（Farrell #5），是分數的結構性地板。
- **社群投機（WSB／cashtag）** r/wallstreetbets 本週熱議具名標的 **5** 檔：AMD、INTC、TSLA、NVDA、MU（AMD 財報後討論串為當日 Reddit 最熱；DJT 轉為看空主題）（2026-11-07，[Benzinga](https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week)，source_ids=retail.social_sentiment）——7 日窗內有具名標的且散戶在重挫後重新湧入 AI 交易，但集中於大型 AI 權值股而非典型迷因股，屬小幅加項。
- **NAAIM 曝險指數** ✗ NOT DISCLOSED（source_ids=retail.naaim）——本次無可公開稽核的當週值（最近可得為 2026-07-29 的 79.70，naaim.org 於本執行環境無法解析），不納入計分（confirmation cross-check，其缺值不得調降主分）。
**結論**：28 落於 21–40 下緣，較前次降 14 並觸發 ⚠——F&G 22（Extreme Fear）與 AAII 看空 48.4%／看多 34.1% 兩項主計分輸入同時落入 0–20 級距，情緒面已進入恐懼；惟 margin debt 1.48 兆（YoY +31.4%）與家庭持股 48.23% 的結構性滿倉為分數設下地板——情緒已冷而部位未退，仍是本次最明顯的脆弱點。

### 5. 貨幣與信貸環境 — 82（weight 20%，Δ -3）
- **Fed funds 目標區間** 3.75–4.00%（上緣 **4.00**，2026-11-07，FRED series=DFEDTARU，source_ids=monetary.fed_funds）——與前次持平、週Δ 0 bps，DFEDTARL 下緣同日 3.75%；9 月升息後 10 月按兵不動。
- **Fed funds 路徑預期（FedWatch）** 12 月升息 25 bps 機率 **76.8**%（11/06，一週前 66.9%；另有 11/05 報價 80.7%，2027 年 1 月再升 25 bps 機率 63.4%）（2026-11-06，[24/7 Wall St.](https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/)，source_ids=monetary.fedwatch）——強勁非農使市場隱含路徑由觀望轉為「12/09 再升息」，是明確的貨幣轉緊訊號，與通膨鏈的退火方向相反（驅動來自就業而非能源通膨）。
- **HY OAS** **3.48**%（週Δ +17 bps，2026-11-05，FRED series=BAMLH0A0HYM2，source_ids=monetary.hy_oas）——續走闊使 `hy_oas_widening_streak` 累進至 4、`hy_streak` 續成立；惟 +17 bps 已遠低於前次 +58 bps、不再觸發 +50 bps 的 `hy_oas_fired`，走闊的速度明確放緩而方向未變。
- **IG OAS** **0.93**%（週Δ +8 bps，2026-11-05，FRED series=BAMLC0A0CM，source_ids=monetary.ig_oas）——投資級自 0.85% 走闊 8 bps、脫離史低但仍處循環低位；HY／IG 同步小幅走闊，壓力開始由低評級向投資級邊緣擴散，惟幅度仍溫和。
- **CPI YoY** **3.72**%（資料月 2026-09-01，FRED series=CPIAUCSL，source_ids=monetary.cpi_yoy）——與前次相同的 9 月印，10 月 CPI 排定 11/10 公布、本次尚無新印（stock-of-state carry-forward）；仍低於 4% 的錨點門檻。
- **5y5y forward（T5YIFR）** **2.17**%（週Δ -16 bps，2026-11-06，FRED series=T5YIFR，source_ids=monetary.t5yifr）——長端通膨預期自 2.33% 大幅回落 16 bps、錨定更紮實，是通膨鏈退火的核心證據，也意味 Fed put 在衰退情境下的可得性回升。
- **10Y 名目／實質／損益平衡** DGS10 **4.84**%（週Δ -25 bps）、DFII10 2.60%（-14 bps，2026-11-05）、T10YIE 2.23%（-12 bps，2026-11-06）（FRED series=DGS10,DFII10,T10YIE，source_ids=monetary.dgs10,monetary.dfii10,monetary.t10yie）——全曲線避險性下移、三腿視窗不一致故歸因不可判；名目殖利率回落 25 bps 本身降低折現與再融資壓力，是 D5 分數下行的主要數值來源。
- **WTI 原油** **99.64** 美元／桶（週Δ -7.92%，2026-11-03，FRED series=DCOILWTICO，source_ids=monetary.wti）——跌破百元，通膨鏈上游推力轉弱（confirmation，不主計分）。
- **10Y 期限溢價（term premium）** **0.9089**%（週Δ -2.7 bps，2026-10-30，FRED series=THREEFYTP10，source_ids=monetary.term_premium）——Kim-Wright 三因子模型；自前次 1.0729% 續降、本次為小幅下行，遠低於 +15 bps 的槓桿鏈初啟門檻，財政風險再定價本次不是衝擊源。
- **repo 資金壓力（SOFR−IORB）與 SRF 動用** **SOFR** 3.92%、SOFR−IORB +2 bps、99th 尾差 +10 bps、SRF 動用 0（as_of 2026-11-05，FRED series=SOFR，source_ids=monetary.repo_stress_srf）——利差由前次的 -1 bps 轉為 +2 bps、尾差自 +7 擴至 +10 bps，屬極輕微的邊際收緊；SRF 零動用，secured-funding 實質無壓力；四腿（SOFR／SOFR99／IORB／RPONTTLD）均成功取得，IORB 以 3.90% 的當日生效觀測對齊。
- **Fed 資產負債表（WALCL）** $6.75T（**6,748,145** 百萬美元，2026-11-04，FRED series=WALCL，source_ids=monetary.walcl）——較前次的 6,755,639 減約 75 億美元、大致持平微降，準備金環境未同步放水，本次信用走闊並非央行流動性抽離所致，亦未獲流動性對沖。
- **ECB 資產（ECBASSETSW）** €5.95T（**5,945,410** 百萬歐元，2026-10-30，FRED series=ECBASSETSW，source_ids=monetary.ecb_boj）——較前次增約 101 億歐元，歐元區流動性小幅回升。
- **BOJ 資產（JPNASSETS）** ¥626.19T（**6,261,882** 億日圓，2026-10-01，FRED series=JPNASSETS，source_ids=monetary.ecb_boj）——月頻、本次無新觀測（no_new_obs），資產負債表持平。
- **PBoC 流動性** 人民銀行 10 月公開市場淨投放 **4000** 億元人民幣（10/15 進行 7,000 億元 6 個月買斷式逆回購、10/26 進行 7,000 億元一年期 MLF、10/21 宣布為非銀行金融機構設立債券流動性支持工具；前三季社會融資規模增量 27.46 兆元、較去年同期少 2.63 兆）（2026-10-26，[BigGo Finance](https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee)，source_ids=monetary.pboc）——中國轉為淨投放的寬鬆姿態、並首度為 NBFI 建立債市流動性後盾，與美歐的緊縮方向分化（confirmation，全球流動性交叉檢核）。
- **美債標售需求（auction tail / bid-to-cover）** ✗ NOT DISCLOSED（source_ids=monetary.treasury_auctions）——14 日窗（2026-10-25 起）內無已完成的 10Y／30Y 標售；最近可得為 10/07 的 10Y（bid-to-cover 2.77、indirect 80.3%）與 10/08 的 30Y（2.54、tail 5.1 bp）皆屬窗外，11/10 與 11/12 的標售尚未舉行，不納入計分。
- **私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）** ✗ NOT DISCLOSED（source_ids=monetary.private_credit_liquidity）——30 日窗（2026-10-09 起）內無具可稽核發布日期的新 gate proration / breach、redemption-request ratio 惡化或 net inflow→outflow flip 揭露。背景（窗外、不計分、不觸發扳機）：Q2 2026 有 16 檔 BDC 中 10 檔突破贖回上限、申請總額 155 億美元，Q1 十二大非交易型 BDC 平均 redemption-request ratio 12.1%、7 檔以 5% quarterly redemption cap 按比例限縮，Blue Owl OTIC 申請比率 40.7%；上述皆無法確認落在本窗內，依規定不納入計分。
**結論**：扳機側；擊發判準本次由 `refinancing_credit_event` 承接（CoreWeave 債殖利率升破 16%、五年期 CDS 一度 1,289 bps、ING 出售約 $500M 資料中心貸款），`hy_oas_widening_streak` 累進至 4 使 `hy_streak` 續成立，側別維持扳機側；82 較前次降 3 但仍落 81–100——HY +17 bps（對前次 +58 bps）、10Y -25 bps、T5YIFR -16 bps、期限溢價 -2.7 bps 四項同時緩解了融資環境的邊際壓力，惟 FedWatch 隱含 12 月升息 76.8%、IG 續走闊 8 bps 與具名發行人的再融資價格壓力使擊發狀態未解除。

### 6. 結構性槓桿 — 82（weight 15%，Δ +2）
- **槓桿 ETF AUM** SOXL 10 月底規模 24.31（十億美元）、當月淨流入 **7.27**（十億美元）（TQQQ 約 37 為全球最大槓桿 ETF、NVDL 約 3.9；類別總規模報導達紀錄 198）（2026-10-31，[Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html)，source_ids=structural.leveraged_etf_aum）——在 SOXL 自身下跌 31.33% 的同一個月湧入 72.7 億美元，是典型的逆勢加槓桿；惟 SOXL 與 TQQQ 的年初至今資金流已雙雙轉負，加槓桿的持續性正在被價格懲罰。
- **0DTE 佔比** SPX 0DTE 佔 SPX 選擇權量約 **65**%（10 月 0DTE 月度 ADV 創紀錄 360 萬口、SPX 整體月度 ADV 創紀錄 550 萬口；Cboe Q3 財報揭露季度佔比 65% 為該指數複合體歷史新高，7 月曾達 66.2%）（2026-10-31，[Cboe via Morningstar](https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026)，source_ids=structural.zero_dte）——落在 rubric 的 55–65% 區間上緣、逼近 >65% 的最高級距門檻，方向性短天期投機強度續創紀錄。
- **OCC 期權總量** 9 月總結算量 **1,486,062,415** 口（YoY +6.2%；指數選擇權 137,042,283 口、ETF 選擇權 642,086,022 口；前九月日均 7,060 萬口、YoY +20.6%。Cboe 指數選擇權 10 月日均創紀錄 690 萬口）（2026-09-30，[OCC](https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report)，source_ids=structural.options_volume）——量能續處紀錄區間，衍生品參與度未因波動跳升而退場。
- **跨資產衍生性** VIX 28.18、期限結構轉為 backwardation、SKEW 149.37，隱含相關性單日 +72.26% 至創紀錄 **20.93**、離散度指數 +9.78% 至 41.31（2026-11-06，[Saxo Options Brief](https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026)，source_ids=structural.cross_asset_derivatives）——近月波動率高於遠月（高波動空頭格局）、且隱含相關性創歷史新高代表市場已為「個股同步下跌」付費，是 crowded-optionality 解開過程中的典型讀數（confirmation）。
- **VIX/S&P 500 同向檢測** comove=false（VIX **28.18**、vix_chg +63.84%、sp500_chg -4.75%；as_of 2026-11-05、base_date 2026-10-29、window_days=7，FRED series=VIXCLS，source_ids=structural.vix_spx_comove）——VIX 在共同時間軸的 7 日窗內暴漲遠超 +5% 門檻，但 S&P 500 同窗為 -4.75% 的下跌、未達 +0.5%，屬正常負相關避險而非 crowded-optionality 同漲，本次不上調級距（不得反向解讀為安全）。
- **AI 基礎建設債務融資／vendor-financing loops** 荷蘭國際集團（ING）出售 12 筆資料中心貸款，規模約 **500**（百萬美元；含 OpenAI／SoftBank／Oracle 的新墨西哥 Stargate 專案約 2,500 萬美元分券，11/19 截標。Morgan Stanley 估約 1.75 兆美元資料中心債務中私募信貸約 7,000 億美元；BofA 估 AI 相關信用發行 2027 年增 31% 至 6,850 億美元；Moody's 10 月警示 2027–29 年私募信貸到期潮）（2026-11-06，[CNBC](https://www.cnbc.com/2026/11/06/ing-ai-data-center-loans-debt.html)，source_ids=structural.ai_infrastructure_debt）——30 日窗內同時存在多筆大額、抵押品依賴租金假設、且銀行端已開始主動減持的融資；英國央行另對「無租戶資料中心貸款」展開調查，屬本維度最重要的加項。
- **銀行對 NBFI 放款（LNFACBW027SBOG）** $2.11T（**2,111.00** 十億美元，週增 0.27%，2026-10-28，FRED series=LNFACBW027SBOG，source_ids=structural.nbfi_bank_loans）——bank–NBFI 曝險自前次 2,105.31 續擴至紀錄水位，BIS AER 2026 Ch II 的失序外溢管道持續加寬（confirmation，不主計分）。
- **margin debt 交叉檢核** margin debt 交叉檢核基數約 **1.48** 兆美元（2026-09-30，[The Trading Tools](https://www.thetrading.tools/margin-debt)，source_ids=structural.margin_debt_crosscheck）——margin debt／股票市值比率僅作交叉檢核，主計分留在 D4（confirmation，不主計分）。
- **美國單一個股槓桿 ETF 核准／上市** ✓ SEARCH-VERIFIED（0 件，source_ids=structural.us_single_stock_etf）（掃描窗 2026-10-09 起，資料日期 —）——30 日窗內 SEC EDGAR／ETF.com 新上市 feed 掃描完成，無新的美國單一個股槓桿 ETF 核准或上市；SEC 10/02 核准的 Volatility Shares 六檔 3 倍產品僅涵蓋加密與商品、不適用個股，單一個股槓桿上限仍為 2 倍，Direxion 的 Anthropic 2 倍多空（ANTO／ANTD）需待其 IPO 後首個交易日。
- **全球槓桿產品擴散** ✗ NOT DISCLOSED（source_ids=structural.global_leveraged_approvals）——7 日窗內韓／台／日／歐皆無英文具名單一個股槓桿核准，且方向與「擴散」相反：韓國 FSC 已暫停新上市並將最低現金保證金提高至 3,000 萬韓元、金融監督院長表態後悔當初開放，台灣金管會明言無開放計畫，日本 TSE 的 20% 單一持股上限與 FSA 指引實質封鎖該產品；「全球槓桿擴散訊號」本週未觸發，不納入計分。
- **美債基差交易槓桿（Treasury basis-trade leverage）** move_index fallback：MOVE 指數 **93.88**（2026-11-04，自 11/03 的 99.97 回落，低於 10/05 的 113.60 高點；槓桿型投資人基差名目部位據 Morgan Stanley 估自年初約 $1.26trn 降至約 $900bn、為兩年多最小，被歸因於相對價值機會收窄而非壓力；對沖基金現券美債持有約 2 兆美元）（2026-11-04，[StreetStats](https://streetstats.finance/markets/volatility)，source_ids=structural.treasury_basis_trade）——script 的 `cftc_lev_funds`／`move_index`／`ofr_repo` 三區塊本次皆 fetch_failed，改走 WebSearch fallback；MOVE 本週回落、基差部位縮減、repo 無壓力，三項同時指向乾柴減少而非積累，`basis_extreme_move` 的機器前置條件不成立（confirmation，不主計分）。
**結論**：82 落於 81–100 下緣，較前次升 2——AI 基礎建設融資同月內出現多筆大額且抵押品依賴租金假設的交易、銀行端首度主動減持（ING 出售 12 筆、約 $500M）、0DTE 佔比約 65% 與 OCC 量能續處紀錄、SOXL 在單月下跌 31.33% 中仍淨流入 72.7 億美元，已滿足 81–100 的 AI 融資判準；未升更高是因全球擴散訊號未觸發、comove=false，且美債基差槓桿與 MOVE 本次雙雙縮減。

## 綜合分數

| 維度 | 權重 | 分數 | 加權分數 |
|---|---:|---:|---:|
| 估值溢價 | 22% | 75 | 16.50 |
| 市場廣度 | 13% | 48 | 6.24 |
| 投機行為 | 18% | 32 | 5.76 |
| 散戶情緒 | 12% | 28 | 3.36 |
| 貨幣與信貸環境 | 20% | 82 | 16.40 |
| 結構性槓桿 | 15% | 82 | 12.30 |

加權總分：60.56 → 61【警戒】

## 歷史泡沫週期對比

相似度計算：checklist v2
- 1973/1 Nifty Fifty 頂：命中 2/8 = 25%
- 1997 早期建設：命中 2/8 = 25%
- 1998 LTCM 衝擊：命中 4/8 = 50%
- 1999 晚期狂熱：命中 5/10 = 50%
- 2000/3 頂點：命中 2/8 = 25%
- 2021/12 Meme 頂：命中 2/8 = 25%
2000/3 高位回落條件：否

**1973/1 Nifty Fifty 頂 feature audit**
- 1973.1｜未命中｜source_ids=—｜估值溢價 75 < 80
- 1973.2｜未命中｜source_ids=—｜市場廣度 48 < 60
- 1973.3｜未命中｜source_ids=—｜CPIAUCSL yoy_pct 3.72% < 4
- 1973.4｜未命中｜source_ids=—｜T5YIFR 週Δ -16 bps < 0（通膨預期明確回落）
- 1973.5｜未命中｜source_ids=—｜DCOILWTICO chg_pct -7.92% < 0.5（油價大跌）
- 1973.6｜未命中｜source_ids=—｜decomposition.driver=unknown ≠ breakeven，且 ΔDGS10 -25 bps 不大於 0
- 1973.7｜命中｜source_ids=—｜扳機狀態 已擊發 ≥ 初啟
- 1973.8｜命中｜source_ids=—｜散戶情緒 28 < 55（散戶未狂熱）

**1997 早期建設 feature audit**
- 1997.1｜未命中｜source_ids=—｜估值溢價 75 不在 40–74
- 1997.2｜未命中｜source_ids=—｜市場廣度 48 ≥ 45
- 1997.3｜命中｜source_ids=—｜投機行為 32 < 50
- 1997.4｜未命中｜source_ids=ai.hyperscaler_capex｜微軟本循環首度下修 2026 capex 指引（約 175 → 約 170 十億美元），capex 指引不再一致上修
- 1997.5｜命中｜source_ids=—｜散戶情緒 28 < 55
- 1997.6｜未命中｜source_ids=—｜結構性槓桿 82 ≥ 50
- 1997.7｜未命中｜source_ids=—｜HY OAS 3.48% < 4 但週Δ +17 bps > 0（本次續走闊）
- 1997.8｜未命中｜source_ids=—｜扳機狀態 已擊發 ≠ 未擊發

**1998 LTCM 衝擊 feature audit**
- 1998.1｜命中｜source_ids=structural.cross_asset_derivatives｜VIX 28.18 > 25（HY OAS 週Δ +17 bps < 30，由波動率分支成立）
- 1998.2｜未命中｜source_ids=—｜S&P 500 較前次 -3.99% > -5（未達 5% 回檔門檻）
- 1998.3｜未命中｜source_ids=structural.treasury_basis_trade｜美債基差槓桿本次證據顯示部位縮減（名目約 $900bn、自年初約 $1.26trn 下降）、MOVE 回落，7 日窗內無具名非銀／槓桿機構壓力事件
- 1998.4｜未命中｜source_ids=monetary.fedwatch｜FedWatch 隱含 12 月升息機率 76.8%，Fed 路徑為轉鷹而非轉鴿
- 1998.5｜命中｜source_ids=—｜估值溢價 75 ≥ 60
- 1998.6｜命中｜source_ids=—｜扳機狀態 已擊發 ≥ 初啟
- 1998.7｜未命中｜source_ids=—｜市場廣度 Δ -8 < 8（廣度本次改善而非急轉弱）
- 1998.8｜命中｜source_ids=—｜ΔT10YIE -12 bps ≤ 0（通膨預期非主因）

**1999 晚期狂熱 feature audit**
- 1999.1｜命中｜source_ids=—｜估值溢價 75 ≥ 75
- 1999.2｜命中｜source_ids=valuation.sp500_pe_cape｜Shiller CAPE 38.91 ≥ 38
- 1999.3｜未命中｜source_ids=—｜投機行為 32 < 60
- 1999.4｜未命中｜source_ids=speculation.microcap_moonshots,speculation.ipo_heat｜本週 moonshot 0 件，且本週唯一 IPO 為社區銀行、無無營收發行人佔比偏高的揭露
- 1999.5｜命中｜source_ids=—｜市場廣度 48 ≥ 45（轉窄）
- 1999.6｜未命中｜source_ids=—｜D5 為扳機側（非自滿側）
- 1999.7｜命中｜source_ids=—｜結構性槓桿 82 ≥ 60
- 1999.8｜未命中｜source_ids=—｜散戶情緒 28 < 55
- 1999.9｜命中｜source_ids=speculation.upcoming_ai_ipos｜Anthropic 於 30 日內遞交公開 S-1、目標估值 1.5–2 兆美元、目標 11 月中掛牌
- 1999.10｜未命中｜source_ids=—｜扳機狀態 已擊發 ≠ 未擊發

**2000/3 頂點 feature audit**
- 2000.1｜未命中｜source_ids=—｜估值溢價 75 < 85
- 2000.2｜命中｜source_ids=—｜扳機狀態 已擊發 ≥ 初啟
- 2000.3｜未命中｜source_ids=—｜市場廣度 48 < 60
- 2000.4｜未命中｜source_ids=—｜前次 dev200 5.34% ≤ 10 且 S&P 本次 -3.99% > -5（高位回落兩分支皆不成立）
- 2000.5｜未命中｜source_ids=—｜投機行為 32 < 70
- 2000.6｜未命中｜source_ids=speculation.insider_form4｜14 日窗內 Form 4 篩選完成但 0 件合格（無 filing-level 具名細節）
- 2000.7｜未命中｜source_ids=—｜散戶情緒 28 < 65
- 2000.8｜命中｜source_ids=monetary.fedwatch｜FedWatch 隱含 12 月升息 25 bps 機率 76.8%、2027 年 1 月再升機率 63.4%，貨幣轉緊成立

**2021/12 Meme 頂 feature audit**
- 2021.1｜未命中｜source_ids=—｜散戶情緒 28 < 65
- 2021.2｜命中｜source_ids=retail.social_sentiment｜r/wallstreetbets 本週有具名標的（AMD、INTC、TSLA、NVDA、MU）
- 2021.3｜命中｜source_ids=—｜結構性槓桿 82 ≥ 65
- 2021.4｜未命中｜source_ids=—｜D5 82 ≥ 60 但側別為扳機側、非自滿側
- 2021.5｜未命中｜source_ids=retail.margin_debt｜margin debt YoY 約 +31.4% < 40
- 2021.6｜未命中｜source_ids=speculation.microcap_moonshots｜本週 microcap moonshot 0 件
- 2021.7｜未命中｜source_ids=—｜市場廣度 48 < 50
- 2021.8｜未命中｜source_ids=—｜CPIAUCSL yoy_pct 3.72% < 4

本次六維組態同時以 50% 貼近「1998 LTCM 衝擊」與「1999 晚期狂熱」，依契約錨點順序由 1998 取得「◀ 最貼近」。循環位置判讀為「衝擊已至、位能正在洩壓，但尚未演成系統性失序」：1998 側的四項命中是 VIX 28.18 突破 25 的波動率衝擊、估值溢價 75 ≥ 60 的高位能、扳機狀態已擊發、以及 ΔT10YIE -12 bps 確認通膨預期不是本次利率變動的主因——這正是 1998 型態的核心定義（高估值與高槓桿積累後由外生衝擊先在信用與波動率市場引爆，本次的衝擊是期中選舉後對資料中心監管的重新定價疊加 AI 債務回本疑慮）。與前次（1998 相似度 65%）相比本次反而下降，原因是兩項 1998 判準轉為未命中：市場廣度由 Δ +14 的急轉弱翻為 Δ -8 的修復，且 Fed 路徑由無資料轉為明確轉鷹（FedWatch 12 月升息 76.8%）而非 1998 年的轉鴿——後者是本次與 1998 年 9 月最關鍵的差異：當年聯準會連續三次降息承接衝擊，本次市場反而在定價升息，政策緩衝不在同一方向。1999 側同為 50% 則由「位能」而非「亢奮」構成：命中的五項是估值溢價 75、CAPE 38.91、廣度 48 ≥ 45、結構性槓桿 82、以及 Anthropic 1.5–2 兆美元的巨型 IPO pipeline；而投機行為 32 < 60、散戶情緒 28 < 55、moonshot 0 件、扳機狀態已非未擊發等四項全數落空——換言之估值與槓桿仍在 1999 的水位，情緒與投機卻已在 1998 的位置。扳機措辭依機器判定：扳機理由為 `refinancing_credit_event`、`hy_streak`，不含 `breakeven_wti_up`，且 1973.3 與 1973.4 未雙雙命中（CPI 3.72% < 4%、T5YIFR 週Δ -16 bps），故**不得**援引 CPI YoY／5y5y forward 述「Fed 寬鬆空間受壓縮」，扳機鏈 A 尚未驗證啟動——本次的擊發是具名發行人的再融資價格，不是通膨鏈的完成傳導。2000/3 僅 25% 的主因是估值溢價 75 < 85、廣度 48 < 60、投機 32 < 70、散戶 28 < 65 四項位能判準同時不足，且高位回落條件兩分支皆不成立（前次 dev200 5.34% 未超過 10% 門檻、本次回檔 -3.99% 未達 -5%）；2021/12 的 25% 則因散戶情緒與 margin debt YoY 雙雙不足，社群具名標的集中於大型 AI 權值股而非迷因股。結構性槓桿的期間調整對比：相對 1999／2000 年 3 月的 margin debt 與指數期貨／選擇權投機，本次對應物為 margin debt 1.48 兆（YoY +31.4%）、SOXL 單月淨流入 72.7 億美元與 0DTE 佔 SPX 量約 65%；相對 2021 年 12 月的迷因槓桿，本次社群投機雖有具名標的但集中於 AI 權值股、且 moonshot 0 件、equity put/call 升至 1.05，這正是 2021 型態僅 25% 的主因。

跨期價格錨（敘事用，不重算）：S&P 500 距 200 日均線 +0.42%、距 52 週均 +1.84%，拉伸程度自前次的 +5.34%／+6.78% 幾乎全數回吐；長期相對指數成長趨勢偏離的文章錨點為 Dot-com 約 95%、1929 約 110%、當前 AI 週期約 147%（RIA/Farrell），僅作跨時代敘事對照。投資泡沫宏觀錨（narrative only，BIS AER 2026 Ch I）：AI 投資週期與運河熱（1830s）、英國鐵路狂熱（1840s）、1920s 電氣化、dot-com 並列——真實技術突破吸引超過商業回報所能支撐的資本，且均以投資反轉收場並伴隨衰退；規模上 AI 相關投資約占美國 GDP 1%、IT 投資合計約 5% 已超越 2000 年 dot-com 峰值，歷史投資 boom 結束後 GDP 增速平均下修逾 1pp。BIS contest model（Rungcharoenkitkul 2026b，未公開 mimeo，經 AER Ch I Graph 11.B 引用）指出 winner-take-all 結構使理性廠商也會過度承諾 capex，累計 capex 由約 $2trn 走向約 $4.5trn 時全行業淨經濟剩餘轉負，而修正之所以急促，正是因為 circular financing 網把單點失望快速傳導至全網——本次微軟一家調整第三方算力採購（取消 Nscale 英國約 30 億美元交易、放棄西維吉尼亞 1.35 GW 意向書）即令 Nebius 與 IREN 單日下跌約 14% 與 17%、CoreWeave 下跌約 10%、neocloud 類股單月約 -45%，是該傳導機制的直接演示。歷史細部類比錨（narrative only）：1999–2001 光纖／電信週期與當前 AI 投資週期結構最近——vendor financing 與 IRU capacity swap 使同一筆收入被多方重複認列，報酬下滑先以會計處理（折舊年限、swap 認列）掩蓋，最終以 capex 反轉與信用事件收場；本次 Oracle 剩餘履約義務 6,380 億美元（約半數來自 OpenAI）對 OpenAI 自身約 6,650 億美元採購承諾與約 700 億美元年化營收的組合，以及 Morgan Stanley 估約 1.75 兆美元資料中心債務中私募信貸約 7,000 億美元，對應該型態的現代版。

## 機構情緒對照

本次無新機構調查數據。

## 本次新增訊號

各維度變化 vs 前次（21天前）（基準 report-2026-10-18）：
- 估值溢價 76→75（-1）：CAPE 40.54→38.91、距 200DMA +5.34%→+0.42%，價格拉伸幾乎全數回吐、ECY 由約 -0.31% 收斂至約 -0.03%；但三項質化訊號反向惡化——**微軟本循環首度下修 2026 capex 指引**（約 175→約 170 十億美元，因第三方算力交付延後）、30 日內首見密集的資料中心取消／延後（微軟取消 Nscale 英國約 30 億美元交易、放棄西維吉尼亞 1.35 GW 意向書）、CoreWeave 五年期 CDS 一度 1,289 bps 且債殖利率升破 16%。
- 市場廣度 56→48（-8）：本次最明顯的修復——RSP 年初至今 14.13% 對 SPY 8.67%、領先約 5.5 個百分點，權值股主導的狹窄領導在 AI 重挫中斷裂；11/06 紐交所上漲 1,474 對下跌 1,252、淨 +222。前十大集中度約 37.9%（自 2025/12 的約 40.7% 回落）仍為結構性地板，且隱含相關性創高 20.93 使廣度改善帶有齊跌齊漲性質。
- 投機行為 44→32（-12 ⚠）：**equity put/call 翻轉至 1.05**（11/05，報導稱高於 2025 年 4 月關稅日）為最強降溫證據；moonshot 與 insider Form 4 續 0 件，本週唯一 IPO 為社區銀行 Narragansett Bancorp（募 9,100 萬、週漲 8%），近百檔 IPO 累計 42 漲對 56 跌。僅 Anthropic 10/26 遞交 S-1（目標估值 1.5–2 兆美元、目標 11 月中掛牌）與 Agility Robotics 的 SPAC 掛牌撐住上緣。
- 散戶情緒 42→28（-14 ⚠）：F&G 由 18 短暫回升至 26 後再降至 **22（Extreme Fear）**；AAII 看空升至 48.4%（月增 6.9 個百分點、連 39 週高於均值）、看多降至 34.1%、多空價差 -14.3%。惟 margin debt 1.48 兆（YoY +31.4%、低於 +40% 門檻）與家庭股票配置 48.23% 的滿倉結構未退——情緒已冷而部位未退。
- 貨幣與信貸環境 85→82（-3）：**側別維持扳機側，但擊發理由換手**——`hy_oas_fired` 本次不再成立（HY OAS 週Δ 由 +58 bps 降至 +17 bps），改由 `refinancing_credit_event` 承接：CoreWeave 2031 債殖利率升破 16%、五年期 CDS 11/05 一度 1,289 bps、ING 出售 12 筆約 $500M 資料中心貸款、AI 投資級債利差約 148 bps 對其餘約 77 bps；`hy_oas_widening_streak` 累進至 4 使 `hy_streak` 續成立。緩解面：10Y 5.09%→4.84%（-25 bps）、T5YIFR 2.33%→2.17%（-16 bps）、期限溢價 1.0729%→0.9089%、WTI -7.92% 跌破百元，通膨鏈四個環節同步退火；反向面：FedWatch 隱含 12 月升息機率 76.8%（一週前 66.9%）、IG OAS 0.85%→0.93%、SOFR−IORB 由 -1 轉為 +2 bps。
- 結構性槓桿 80→82（+2）：AI 基礎建設融資首度出現**銀行端主動減持**（ING 出售 12 筆、約 $500M 資料中心貸款，含 Stargate 新墨西哥專案分券，11/19 截標），Goldman 統計 10/29 起一週內 5 筆 AI 相關發行合計 670 億美元、今年以來 hyperscaler 發債 2,960 億美元遠超年初 2,500 億基線；SOXL 在單月下跌 31.33% 中仍淨流入 72.7 億美元（逆勢加槓桿）；0DTE 佔 SPX 量約 65%、Cboe 指數選擇權 10 月日均創紀錄 690 萬口；銀行對 NBFI 放款 2,105.31→2,111.00 億美元創高。減項：MOVE 93.88 自 99.97 回落、槓桿型投資人基差名目部位自年初約 $1.26trn 降至約 $900bn。
- 私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）：本次 ✗ NOT DISCLOSED，30 日窗（2026-10-09 起）內無具可稽核發布日期的新 gate proration / breach、redemption-request ratio 惡化或 net inflow→outflow flip；Q1／Q2 2026 的 BDC 統計（16 檔中 10 檔突破上限、申請總額 155 億美元、平均 redemption-request ratio 12.1%）屬窗外背景，不計分、不觸發扳機。
- 美債基差交易槓桿（Treasury basis-trade leverage）：script 三區塊 fetch_failed 後改走 WebSearch fallback，取得 MOVE 93.88（11/04）與基差名目部位約 $900bn 的縮減報導——方向為乾柴減少而非積累，`basis_extreme_move` 的機器前置條件不成立；7 日窗內無具名國債市場失序（Treasury market dysfunction）事件。
- 機構部位：本次無新 BofA／JPM 調查數據（9 月調查為最近可得：現金 3.9%、債市無序升息已取代 AI 泡沫成為首要尾部風險、AI 泡沫占比降至 28%）；NAAIM 本次 ✗ NOT DISCLOSED。
- 格局：穩定共存 → 穩定共存（標籤未變，但內涵由股持平、油債小升的收斂轉為三者同步下行的 risk-off）；扳機狀態：已擊發 → **已擊發**（理由由 hy_oas_fired、hy_streak 換手為 refinancing_credit_event、hy_streak）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE | 38.91 | https://www.multpl.com/shiller-pe | 2026-11-06 | 2026-11-08T09:40:00+08:00 |
| valuation.sp500_pe_cape | S&P 500 trailing P/E | 25.14 | https://www.multpl.com/s-p-500-pe-ratio | 2026-11-06 | 2026-11-08T09:40:00+08:00 |
| valuation.sp500_pe_cape | Excess CAPE Yield（derived：1/CAPE − DFII10/100） | -0.03 | derived：multpl CAPE ＋ FRED series=DFII10 | 2026-11-06 | 2026-11-08T09:40:00+08:00 |
| valuation.sp500_trend | sp500_trend latest | 7,353.73 | FRED series=SP500 | 2026-11-05 | 2026-11-08T09:17:33+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 0.42 | FRED series=SP500（ma200=7,322.74） | 2026-11-05 | 2026-11-08T09:17:33+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 1.84 | FRED series=SP500（ma52w=7,221.05） | 2026-11-05 | 2026-11-08T09:17:33+08:00 |
| valuation.sp500_trend | sp500_trend chg_pct | -3.99 | FRED series=SP500 | 2026-11-05 | 2026-11-08T09:17:33+08:00 |
| valuation.sp500_trend | sp500_trend prior_spot | 7,659.44 | FRED series=SP500 | 2026-10-16 | 2026-11-08T09:17:33+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest | 48.23 | FRED series=BOGZ1FL153064486Q | 2026-04-01 | 2026-11-08T09:17:33+08:00 |
| monetary.fed_funds | DFEDTARU latest | 4.00 | FRED series=DFEDTARU | 2026-11-07 | 2026-11-08T09:17:33+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.75 | FRED series=DFEDTARL | 2026-11-07 | 2026-11-08T09:17:33+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 3.48 | FRED series=BAMLH0A0HYM2 | 2026-11-05 | 2026-11-08T09:17:33+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 delta_bps | +17 | FRED series=BAMLH0A0HYM2 | 2026-11-05 | 2026-11-08T09:17:33+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.93 | FRED series=BAMLC0A0CM | 2026-11-05 | 2026-11-08T09:17:33+08:00 |
| monetary.dgs10 | DGS10 latest | 4.84 | FRED series=DGS10 | 2026-11-05 | 2026-11-08T09:17:33+08:00 |
| monetary.dfii10 | DFII10 latest | 2.60 | FRED series=DFII10 | 2026-11-05 | 2026-11-08T09:17:33+08:00 |
| monetary.t10yie | T10YIE latest | 2.23 | FRED series=T10YIE | 2026-11-06 | 2026-11-08T09:17:33+08:00 |
| monetary.wti | DCOILWTICO latest | 99.64 | FRED series=DCOILWTICO | 2026-11-03 | 2026-11-08T09:17:33+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct | 3.72 | FRED series=CPIAUCSL | 2026-09-01 | 2026-11-08T09:17:33+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.17 | FRED series=T5YIFR | 2026-11-06 | 2026-11-08T09:17:33+08:00 |
| monetary.term_premium | THREEFYTP10 latest | 0.9089 | FRED series=THREEFYTP10 | 2026-10-30 | 2026-11-08T09:17:33+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.92 | FRED series=SOFR | 2026-11-05 | 2026-11-08T09:17:33+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 4.00 | FRED series=SOFR99 | 2026-11-05 | 2026-11-08T09:17:33+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.90 | FRED series=IORB | 2026-11-08 | 2026-11-08T09:17:33+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest | 0.0 | FRED series=RPONTTLD | 2026-11-06 | 2026-11-08T09:17:33+08:00 |
| monetary.walcl | WALCL latest | 6,748,145（$6.75T，百萬美元） | FRED series=WALCL | 2026-11-04 | 2026-11-08T09:17:33+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,945,410（€5.95T，百萬歐元） | FRED series=ECBASSETSW | 2026-10-30 | 2026-11-08T09:17:33+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,261,882（¥626.19T，億日圓） | FRED series=JPNASSETS | 2026-10-01 | 2026-11-08T09:17:33+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 28.18 | FRED series=VIXCLS | 2026-11-05 | 2026-11-08T09:17:33+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 28.18 | FRED 衍生區塊（window_days=7，base_date=2026-10-29） | 2026-11-05 | 2026-11-08T09:17:33+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2,111.00（$2.11T，十億美元） | FRED series=LNFACBW027SBOG | 2026-10-28 | 2026-11-08T09:17:33+08:00 |

### Coverage

| source_id | 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 P/E and Shiller CAPE | WebFetch（multpl 直抓成功） | ✓ DIRECT |
| valuation.mag7_multiples | Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Analyst TP upgrade decomposition | WebSearch（best-effort，90d＋同季） | ✓ SEARCH-VERIFIED |
| valuation.sp500_trend | S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ai_credit_schism | AI 信用定價分歧 | WebSearch（best-effort，14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Top-10 concentration | WebSearch（slickcharts 於本環境無法解析） | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | CNN Fear & Greed Index | WebSearch（CNN 轉載） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Margin Debt: FINRA | WebSearch（FINRA 轉載） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Social sentiment proxies | WebSearch（best-effort，7d） | ✓ SEARCH-VERIFIED |
| retail.household_equity_allocation | Household equity allocation | scripts/fetch_macro.py（FRED） | ✓ API |
| retail.naaim | NAAIM Exposure Index | WebSearch（best-effort；naaim.org 無法解析、無當週值） | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | BofA Fund Manager Survey | WebSearch（best-effort；前次基準以來無新調查） | ✗ NOT DISCLOSED |
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
| monetary.treasury_auctions | 美債標售需求 | WebSearch（best-effort，14d；窗內無已完成標售） | ✗ NOT DISCLOSED |
| monetary.fedwatch | Fed funds rate path expectations | WebSearch（CME FedWatch 轉載） | ✓ SEARCH-VERIFIED |
| monetary.walcl | Fed balance sheet: FRED | scripts/fetch_macro.py（FRED） | ✓ API |
| monetary.ecb_boj | Global central bank liquidity cross-check | scripts/fetch_macro.py（FRED ECBASSETSW/JPNASSETS 均 ok） | ✓ API |
| monetary.pboc | PBoC aggregate financing | WebSearch（best-effort） | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Private-credit / non-bank fund liquidity stress | WebSearch（best-effort，30d；窗內無新揭露） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | Hyperscaler capex guidance | WebSearch（季度指引 carry-forward） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI token volume growth rate | WebSearch（best-effort；本季無新揭露） | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | OpenAI / Anthropic annualized revenue | WebSearch（best-effort） | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | Hyperscaler AI customer concentration | WebSearch（best-effort） | ✓ SEARCH-VERIFIED |
| ai.compute_supply_demand | AI compute supply/demand and overcapacity risk | WebSearch（best-effort） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | Hyperscaler 融資結構 | WebSearch（quarterly_state 沿用＋30d 事件掃描） | ✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok |
| ai.revenue_capex_gap | AI 營收對 capex 缺口 | WebSearch（組件 carry-forward） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | GPU / 伺服器折舊年限變動 | WebSearch（best-effort，30d；窗內無變更） | ✗ NOT DISCLOSED |
| ai.capital_cycle | 資本週期階段 | WebSearch（quarterly_state 增速證據不足；30d 事件掃描成功） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:ok |
| speculation.ai_rename_spac | Search for past 7 days | WebSearch（7d 改名／SPAC 掃描） | ✓ SEARCH-VERIFIED |
| speculation.ipo_heat | IPO market heat | WebSearch（Renaissance 週報） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Microcap thematic moonshots | WebSearch（7d movers 掃描） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Upcoming AI IPOs | WebSearch（30d 具名 S-1） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Insider selling at AI | SEC EDGAR Form 4（14d 掃描） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Cboe equity-only put/call ratio | WebSearch（Cboe 轉載） | ✓ SEARCH-VERIFIED |
| structural.leveraged_etf_aum | US leveraged ETF AUM | WebSearch（etf.com／發行人轉載） | ✓ SEARCH-VERIFIED |
| structural.us_single_stock_etf | US single-stock leveraged ETF approvals | WebSearch（SEC EDGAR／ETF.com 新上市 feed，30d） | ✓ SEARCH-VERIFIED（0 件） |
| structural.global_leveraged_approvals | Global leveraged product approvals | WebSearch（best-effort，7d；KRX/TWSE/JPX/ESMA 無英文揭露） | ✗ NOT DISCLOSED |
| structural.zero_dte | 0DTE option volume | WebSearch（Cboe 月報轉載） | ✓ SEARCH-VERIFIED |
| structural.options_volume | Options total volume | WebSearch（OCC 月報） | ✓ SEARCH-VERIFIED |
| structural.cross_asset_derivatives | Cross-asset derivatives / correlation checks | WebSearch（Saxo Options Brief） | ✓ SEARCH-VERIFIED |
| structural.vix_spx_comove | VIX / S&P 500 co-movement | scripts/fetch_macro.py（FRED VIXCLS ＋ vix_spx_comove 區塊均 ok） | ✓ API |
| structural.margin_debt_crosscheck | Cross-reference only: FINRA margin debt | WebSearch（FINRA 轉載，交叉檢核） | ✓ SEARCH-VERIFIED |
| structural.ai_infrastructure_debt | AI infrastructure debt financing / vendor-financing loops | WebSearch（best-effort，30d） | ✓ SEARCH-VERIFIED |
| structural.nbfi_bank_loans | Bank loans to nondepository financial institutions | scripts/fetch_macro.py（FRED H.8） | ✓ API |
| structural.treasury_basis_trade | 美債基差交易槓桿（Treasury basis-trade leverage） | script 三區塊 fetch_failed → WebSearch fallback（move_index） | ✓ SEARCH-VERIFIED |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.mag7_multiples | Mag 7 群體前瞻本益比約 28.3 | Magnificent 7 forward P/E valuation November 2026 | https://vestedfinance.com/blog/us-stocks/is-the-magnificent-7-growth-story-over/ | 2026-10-13 | 2026-11-08T10:30:00+08:00 |
| valuation.analyst_tp_decomposition | Bernstein 將 TSMC 目標價由 554 上調至 600 | analyst price target raise November 2026 TSMC Bernstein | https://stockanalysis.com/stocks/tsm/ | 2026-11-03 | 2026-11-08T10:30:00+08:00 |
| valuation.ai_credit_schism | [refinancing_credit_event] CoreWeave 債券殖利率升破 16 | CoreWeave bond yield tops 16% AI credit stress November 2026 | https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html | 2026-11-06 | 2026-11-08T10:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 五年期信用違約交換突破 1289 | CoreWeave credit default swap 1289 bps November 5 2026 | https://coinpaper.com/38478/core-weave-default-protection-costs-top-1-000-basis-points-even-as-nasdaq-rebounds | 2026-11-05 | 2026-11-08T10:30:00+08:00 |
| breadth.rsp_spy | 等權指數年初至今報酬約 14.13 | RSP equal-weight ETF year to date return November 6 2026 SPY | https://totalrealreturns.com/n/RSP,SPY | 2026-11-06 | 2026-11-08T10:30:00+08:00 |
| breadth.top10_concentration | 前十大成分股權重約 37.9 | S&P 500 top 10 largest companies index weight percent November 2026 | https://chartrow.com/sp500/concentration | 2026-11-01 | 2026-11-08T10:30:00+08:00 |
| breadth.advance_decline | 紐交所上漲家數 1,474 對下跌 1,252 | NYSE advance decline November 6 2026 market breadth | https://www.mcoscillator.com/market_breadth_data/ | 2026-11-06 | 2026-11-08T10:30:00+08:00 |
| retail.fear_greed | 恐懼與貪婪指數極度恐懼 22 | CNN Fear and Greed Index reading November 6 2026 | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ | 2026-11-06 | 2026-11-08T10:30:00+08:00 |
| retail.margin_debt | 融資餘額約 1.48 兆美元、年增約 31.4 | FINRA margin debt September October 2026 record billion | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T10:30:00+08:00 |
| retail.aaii | 散戶調查看多 34.1、看空 48.4 | AAII investor sentiment survey bullish bearish November 2026 | https://insights.aaii.com/p/aaii-sentiment-survey-pessimism-revives | 2026-11-04 | 2026-11-08T10:30:00+08:00 |
| retail.social_sentiment | r/wallstreetbets 本週熱議具名標的 5 | wallstreetbets reddit meme stock chatter November 2026 retail traders | https://www.benzinga.com/markets/equities/26/11/63017848/tsla-amd-mu-and-more-5-stocks-investors-couldnt-stop-buzzing-about-this-week | 2026-11-07 | 2026-11-08T10:30:00+08:00 |
| monetary.fedwatch | 12 月升息 25 bps 機率 76.8 | CME FedWatch December 2026 rate hike probability November 2026 | https://247wallst.com/investing/2026/11/07/odds-of-a-december-rate-hike-jump-to-77-after-a-blowout-jobs-report/ | 2026-11-06 | 2026-11-08T10:30:00+08:00 |
| monetary.pboc | 人民銀行 10 月公開市場淨投放 4000 | PBoC aggregate financing October 2026 liquidity operations | https://finance.biggo.com/news/65d07fbd-382e-4e49-bd6f-1d9ecf551bee | 2026-10-26 | 2026-11-08T10:30:00+08:00 |
| ai.hyperscaler_capex | 微軟將 2026 年資本支出指引自約 175 下調至約 170 | hyperscaler capex guidance Q3 2026 Microsoft Alphabet Amazon Meta | https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex | 2026-10-29 | 2026-11-08T10:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 上半年營收 16.3 | Anthropic IPO S-1 revenue valuation November 2026 | https://finance.yahoo.com/technology/ai/articles/anthropic-prepares-potential-2-trillion-100000960.html | 2026-10-26 | 2026-11-08T10:30:00+08:00 |
| ai.customer_concentration_rpo | Oracle 剩餘履約義務 638 | Oracle RPO backlog OpenAI double counting 2026 | https://www.fool.com/investing/2026/07/02/this-ai-infrastructure-company-has-a-638-billion-b/ | 2026-08-31 | 2026-11-08T10:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選租金中位數 3.87 | GPU rental prices utilization HBM DRAM pricing November 2026 | https://getdeploying.com/gpu-price-trends | 2026-11-03 | 2026-11-08T10:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] hyperscaler 今年以來發債 296 | Goldman hyperscaler debt issuance 296 billion 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T10:30:00+08:00 |
| ai.hyperscaler_financing_mix | [event_scan] 10/29 起一週內 5 筆 AI 相關債券發行合計 67 | Goldman AI bond deals 67 billion week October 29 2026 | https://404kresearch.substack.com/p/the-ai-buildout-enters-the-debt-era | 2026-11-06 | 2026-11-08T10:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic 65 ＋ OpenAI 約 70，合計約 135 | OpenAI annualized revenue run rate 2026 Anthropic revenue | https://finance.yahoo.com/markets/stocks/articles/openai-q3-2026-revenue-run-171727199.html | 2026-09-30 | 2026-11-08T10:30:00+08:00 |
| ai.capital_cycle | [event_scan] 微軟 10 月取消 Nscale 英國資料中心交易，規模約 3 | Microsoft neocloud data center cancellation delay November 2026 | https://www.investing.com/news/stock-market-news/microsoft-tightens-oversight-of-neocloud-data-center-projects-bloomberg-news-reports-5005281 | 2026-11-04 | 2026-11-08T10:30:00+08:00 |
| speculation.ai_rename_spac | 7 日窗內合格 SPAC 事件 1 | company ticker change AI rename SPAC announcement November 2026 | https://www.securities.io/agility-robotics-completes-spac-merger-ahead-of-nasdaq-debut/ | 2026-11-04 | 2026-11-08T10:30:00+08:00 |
| speculation.ipo_heat | 本週唯一定價 IPO 週漲 8 | IPO pricing week November 2 6 2026 Renaissance Capital weekly recap | https://www.renaissancecapital.com/IPO-Center/News/122629/us-ipo-weekly-recap-community-bank-debuts-amid-market-fears | 2026-11-06 | 2026-11-08T10:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 遞交 S-1，目標估值 1.5 兆至 2 | Anthropic IPO valuation filing November 2026 | https://builtin.com/articles/anthropic-ipo-filing-s1 | 2026-10-26 | 2026-11-08T10:30:00+08:00 |
| speculation.equity_put_call | Cboe 股票選擇權賣買權比升至 1.05 | Cboe equity put call ratio November 2026 reading | https://seekingalpha.com/news/4667879-equity-putcall-ratio-tops-10-as-sp-500-suffers-44-slide | 2026-11-05 | 2026-11-08T10:30:00+08:00 |
| structural.leveraged_etf_aum | 半導體 3 倍多頭基金 10 月底規模 24.31、當月淨流入 7.27 | leveraged ETF AUM NVDL TQQQ SOXL assets November 2026 | https://finance.yahoo.com/markets/stocks/articles/dip-buyers-leveraged-tech-etfs-133557447.html | 2026-10-31 | 2026-11-08T10:30:00+08:00 |
| structural.zero_dte | 0DTE 佔 SPX 選擇權量約 65 | 0DTE share of SPX options volume October 2026 percent Cboe | https://www.morningstar.com/news/pr-newswire/20261104cg89381/cboe-global-markets-reports-trading-volume-for-october-2026 | 2026-10-31 | 2026-11-08T10:30:00+08:00 |
| structural.options_volume | 9 月總結算量 1,486,062,415 | OCC options total volume September 2026 monthly contracts | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report | 2026-09-30 | 2026-11-08T10:30:00+08:00 |
| structural.cross_asset_derivatives | 波動率指數 28.18、偏斜指數 149.37、隱含相關性創高 20.93 | VIX term structure backwardation SKEW index November 6 2026 | https://www.home.saxo/en-ch/content/articles/options/eight-times-the-priced-move---options-brief---6-november-2026-06112026 | 2026-11-06 | 2026-11-08T10:30:00+08:00 |
| structural.margin_debt_crosscheck | 融資餘額交叉檢核基數約 1.48 | FINRA margin debt to market cap September 2026 | https://www.thetrading.tools/margin-debt | 2026-09-30 | 2026-11-08T10:30:00+08:00 |
| structural.ai_infrastructure_debt | 荷蘭國際集團出售 12 筆資料中心貸款，規模約 500 | AI data center debt financing private credit November 2026 | https://www.cnbc.com/2026/11/06/ing-ai-data-center-loans-debt.html | 2026-11-06 | 2026-11-08T10:30:00+08:00 |
| structural.treasury_basis_trade | move_index fallback：波動率指標 93.88 | MOVE index Treasury volatility level November 2026 | https://streetstats.finance/markets/volatility | 2026-11-04 | 2026-11-08T10:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（0 件符合 2+ 主題×弱基本面） | microcap stock surged 100% single day press release quantum AI November 2026 | 檢查來源：TradingView／Stocktwits movers、Globe and Mail 微型股新聞、Yahoo day gainers（窗內無合格標的） | — | 2026-11-08T10:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件合格） | insider selling Form 4 AI companies October November 2026 SEC EDGAR | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表（窗內無具名申報人／交易日／金額等 filing-level 細節） | — | 2026-11-08T10:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval October November 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed、Direxion 新聞稿（窗內無合格核准或上市） | — | 2026-11-08T10:30:00+08:00 |

## 本次分數存檔
```json
{
  "date": "2026-11-08",
  "iso_week": "2026-W45",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "valuation": 75,
  "breadth": 48,
  "speculation": 32,
  "retail": 28,
  "monetary": 82,
  "structural": 82,
  "total": 61,
  "tier": "警戒",
  "regime": "穩定共存",
  "trigger_state": "已擊發",
  "trigger_reasons": [
    "refinancing_credit_event",
    "hy_streak"
  ],
  "monetary_side": "扳機側",
  "hy_oas_widening_streak": 4,
  "sp500_dev200_pct": 0.42
}
```

本報告為相對風險溫度計，非擇時訊號。

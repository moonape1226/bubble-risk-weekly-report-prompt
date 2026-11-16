# 2026-10-18 市場泡沫風險評估報告
> 報告日期：2026-10-18；執行日：2026-10-18 Asia/Taipei；ISO 週次：2026-W42；前次基準：report-2026-09-13（35天前）

**總評**：總分 66【高】（Δ +3）；扳機狀態：已擊發；最貼近錨點：1998 LTCM 衝擊（65%）。

## §1 六維度風險條圖
| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▱▱▱ | 76 | 75 | +1 |
| 市場廣度 | ▰▰▰▰▰▱▱▱▱▱ | 56 | 42 | +14 ⚠ |
| 投機行為 | ▰▰▰▰▱▱▱▱▱▱ | 44 | 48 | -4 |
| 散戶情緒 | ▰▰▰▰▱▱▱▱▱▱ | 42 | 46 | -4 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▰▰▱▱ | 85 | 79 | +6 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▰▱▱ | 80 | 77 | +3 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **66【高】** | 63 | +3 |

## §2 歷史錨點相似度
| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1973/1 Nifty Fifty 頂 | 50% | ▰▰▰▰▰▱▱▱▱▱ |  |
| 1997 早期建設 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 1998 LTCM 衝擊 | 65% | ▰▰▰▰▰▰▱▱▱▱ | ◀ 最貼近 |
| 1999 晚期狂熱 | 50% | ▰▰▰▰▰▱▱▱▱▱ |  |
| 2000/3 頂點 | 15% | ▰▱▱▱▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |

## §3 三角訊號
| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,659.44 | 持平（+0.03%，前次 約 7,656.98） |
| WTI 原油 | $101.91 /bbl | ▲ +0.63%（前次 約 $101.27） |
| 10Y Treasury | 5.10% | ▲ +14 bps（前次 約 4.96%） |

**三者狀態**：穩定共存（三者本次無一反向重新定價：股市持平、油與債小幅上行，且 S&P 500 距 200DMA 僅 +5.34%、未達 +10% 拉伸門檻，故機器判定為穩定共存）。須注意此判定只描述 {股、油、債} 三角的方向組態，不代表整體風險下降——本次的質變發生在三角之外的信用利差與廣度，見下方扳機理由與 D2／D5。
- 股市：本次 **7,659.44**；較前次 持平（+0.03%，前次 約 7,656.98）；距 200DMA +5.34%，35 日淨變動幾近於零，但路徑是先衝高至 7,818 再於 10/14–10/16 回落，週線跌近 2%。
- WTI 原油：本次 **$101.91**；較前次 ▲（+0.63%，前次 約 $101.27）；續站百元之上，中東供給疑慮使 Brent 一度觸及 $110。
- 10Y 殖利率：本次 **5.10%**；較前次 ▲（+14 bps，前次 約 4.96%）；主要驅動：三腿視窗不一致、不可判（惟 ΔDFII10 +18 bps 大於 ΔDGS10，實質利率為可見推力）。
**格局轉變**：前次 分歧 轉為 本次 穩定共存——前次是油與債上行而股價回落的方向背離，本次三者方向重新收斂（股持平、油債小升），背離壓力由三角內部移轉到信用與廣度。
**10Y 成因拆解**：ΔDGS10 +14 bps，而 ΔDFII10 +18 bps、ΔT10YIE -1 bps；惟 ΔT10YIE 的觀測視窗（2026-10-16）與 DGS10／DFII10（2026-10-15）不同，`driver=unknown`，恆等式不跨視窗成立，故歸因判定為 不可判（視窗不一致）；三腿皆有新觀測、無 stale leg。方向上實質利率升幅大於名目、損益平衡通膨微降，與 B 槓桿鏈的 real-rate 主導型態一致，但因視窗不一致不作正式歸因。
- ΔDGS10 名目殖利率週變動：+14 bps
- ΔDFII10 實質殖利率週變動：+18 bps
- ΔT10YIE 損益平衡通膨週變動：-1 bps
- 判定：不可判（視窗不一致）
**扳機鏈**：A 通膨鏈（油 → 通膨預期 → Fed 受限 → refinancing 成本）本次完成了「政策端受限」環節但預期端仍錨定——[monetary.cpi_yoy] CPIAUCSL yoy_pct=3.72 data_date=2026-09-01 顯示 9 月實現通膨自 8 月 3.4% 跳升至 3.7%（月增 0.6%）、為本次全市場重定價的直接觸媒，[monetary.t5yifr] T5YIFR latest=2.33 delta_bps=1.0 data_date=2026-10-16 顯示長端通膨預期僅微升 1 bp、仍被良好錨定；Fed 已於前次基準以來實際升息 25 bps（DFEDTARU 3.75% → 4.00%），Fed put 的可得性進一步下降，故本鏈述為中段推進而非完成傳導（預期未脫錨）。WTI ▲ +0.63% 僅小幅、油價非本次主要推力。B 槓桿鏈（衝擊：財政風險再定價 → NBFI 去槓桿 → margin spiral → 國債市場失序 → 官方市場功能回應）未啟動——10Y 期限溢價（THREEFYTP10）1.0729%、週Δ -1.2 bps 為下行，遠低於 +15 bps 初啟門檻，財政再定價本次不是衝擊源；repo 資金壓力（SOFR−IORB）-1 bps 為負、99th 尾差 +7 bps、SRF 動用 0，secured funding 無壓力；10/7 的 10Y 標售 bid-to-cover 2.77、dealer 僅承接 2.54% 屬強勁需求。`cftc_lev_funds`／`move_index`／`ofr_repo` 三區塊本次 fetch_failed（cftc.gov 於本執行環境遭 403 封鎖），且 7 日窗內無具名基差／swap-spread 失序平倉或國債市場失序報導，故本鏈述為「本週無基差交易槓桿新證據」。本次的擊發來自信用利差本身（HY OAS 週Δ +58 bps）與 AI 複合體的信用重定價，而非上述兩鏈的傳導節點。
**扳機理由**：hy_oas_fired、hy_streak
⚠ **結論**：扳機狀態：已擊發——HY OAS 單期走闊 +58 bps（2.65% → 3.23%）已達並超過 contract 的 +50 bps 擊發門檻（`hy_oas_fired`），同時 `hy_oas_widening_streak` 累進至 3、連續走闊判準（`hy_streak`）亦成立。歷史意義在於：信用利差的絕對水位仍不算高（HY 3.23%、IG 0.84% 續處循環低位，froth 未全退），但走闊的**速度**已是此信用循環最快，且與三項條件同時出現——Fed 實際升息至 3.75–4.00%、9 月 CPI 升至 3.7%、AI 複合體信用保險費創歷史新高（CoreWeave 5Y CDS 1,194.5 bps、Oracle 288 bps）。這正是「估值與槓桿位能已滿、融資管道開始由寬轉緊並首度出現具名信用壓力」的配置，對應 §2 最貼近的 1998 型態（衝擊已至、尚未演成系統性失序）。限制條件須明說：私募信貸 gate proration／breach 本次無可稽核的窗內揭露、國債市場失序與官方市場功能回應皆未出現、repo 與期限溢價均無壓力，故本次為「信用面單點擊發」，不是全面的 financing crisis；美債基差交易槓桿仍為乾柴而未點火。

## 六維度評分

### 1. 估值溢價 — 76（weight 22%，Δ +1）
- **Shiller CAPE** 約 **40.54**（2026-10-16，[multpl](https://www.multpl.com/shiller-pe)，source_ids=valuation.sp500_pe_cape）——自前次約 40.73 微降，仍處 1881 年以來次高區間、僅 1999–2000 曾更高，估值溢價維持極端。
- **Mag 7 前瞻本益比** MSFT 約 **24.5** 倍、為群內第三便宜，NVDA 約 14.3 倍對 40%＋成長（2026-09-24，[Magnificent Seven Market Desk](https://articlegateway.com/?p=146)，source_ids=valuation.mag7_multiples）——最貴族群續去評價，盈餘上修快於股價，為本維度唯一明顯的減項。
- **價格趨勢偏離（Farrell #1/#2/#4）** S&P 500 距 200DMA **+5.34%**、距 52 週均 +6.78%（2026-10-16，FRED series=SP500，source_ids=valuation.sp500_trend）——偏離自前次 +6.9% 再收斂，價格拉伸程度下降、遠未達 +10% 門檻，是本次拉回後的直接結果。
- **Excess CAPE Yield（ECY，跨時代校準）** 約 **-0.31%**（1/CAPE 40.54 − DFII10 2.78%/100；CAPE 資料日 2026-10-16、DFII10 資料日 2026-10-15，FRED series=DFII10，source_ids=valuation.sp500_pe_cape,monetary.dfii10）——自前次約 -0.10% 進一步深化為負，實質利率上行 18 bps 是主因；股相對抗通膨債已無風險溢酬且負值加深，屬 1929／2000 級別讀數（confirmation，不主計分）。
- **hyperscaler capex reality check** 四大 2026 capex 合計約 **725**（十億美元，較 2025 年約 410 增 77%；Alphabet 已將上限上修至 205）（2026-07-28，[CNBC](https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html)，source_ids=ai.hyperscaler_capex）——Q3 財報尚未發布，沿用 Q2 季度指引（stock-of-state，carry-forward）；指引仍在上修、無下修跡象，屬估值支撐，但在融資成本已重定價的環境下其脆弱性同步上升。
- **AI 營收對 capex 缺口** 年化 AI 終端營收約 115（十億美元；Anthropic 約 **65** ＋ OpenAI 約 50）對年化 capex 約 725（分母：MSFT／GOOGL／AMZN／META top-4，Oracle 本次無新季度披露未納入）（2026-08-17，[Axios](https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai)，source_ids=ai.revenue_capex_gap）——缺口約 1:6.3，與前次同量級、未收斂；回本假設持續後移，而本次信用市場已開始對「回本前的利息負擔」定價，使此缺口由純質化隱憂轉為有價格對應的風險。
- **AI compute 供需 reality check** H100 隨選中位租金約 **4.20** 美元／小時（16 家供應商中位數；H200 約 5.70、B200 約 8.19），DRAM 合約價 Q3 季升 13–18%（Q2 約 +60%）、HBM3E 2026 合約價年增約 20%（2026-10-07，[Uvik GPU Price Index](https://uvik.net/blog/gpu-price-index/)，source_ids=ai.compute_supply_demand）——租金與記憶體價同步偏高、供給仍緊，產能尚被付費需求吸收，本次為估值風險的減項而非加項。
- **AI 信用定價分歧（equity-vs-credit schism）** CoreWeave 5Y CDS 升至紀錄 **1,194.5** bps（ICE 報價；隱含 5 年內違約機率約 63%，2031 年到期債殖利率一度升至 16% 後回落至約 14%），Oracle 5Y CDS 單夜 +26 bps 至紀錄 288 bps，Amazon／Alphabet／Meta／Nvidia 的 CDS 亦同創新高（2026-10-15，[BusinessDay／Reuters](https://www.businessday.co.za/world/international-companies/2026-10-15-ai-credit-fears-push-tech-default-insurance-to-record-highs/)，source_ids=valuation.ai_credit_schism）——分歧本次由「未解」轉為「信用端先行確認」：信貸已明確對 AI 複合體重定價而股權估值僅部分跟上，屬 BIS Bulletin 120 所述兩個市場只有一個是對的之解答開始出現，是本維度最重要的質化上修項（confirmation，不主計分）。
- **分析師目標價拆解** ✗ NOT DISCLOSED（source_ids=valuation.analyst_tp_decomposition）——契約要求 90 日內且同屬本季（2026-Q4，10/1 起）的可稽核 EPS 修正對目標 PE 擴張拆解；BofA 將 TSMC 目標 PE 由 21 升至 22 倍屬本季之前的註記，窗外不採，本次無合格揭露，不納入計分。
- **折舊年限變動（盈餘品質）** ✗ NOT DISCLOSED（source_ids=ai.depreciation_life）——30 日窗內無新的 GPU／伺服器折舊年限或殘值假設變更披露；既有的 Meta 延長至 5.5 年、Amazon 縮短至 5 年屬窗外背景，不納入計分。
- **backlog 重複計算風險（RPO double-counting）** ✗ NOT DISCLOSED（source_ids=ai.customer_concentration_rpo）——雖有 Morgan Stanley 對 OpenAI 占 Oracle／CoreWeave RPO 比重的估計流傳，但本次未能取得具可稽核發布日期的來源，依 Fetch protocol 不得用於計分，不納入計分。
- **hyperscaler 融資結構（capex vs FCF / 發債）** ✗ NOT DISCLOSED（source_ids=ai.hyperscaler_financing_mix）——季度狀態可沿用（capex 已超越自身 FCF、2026 年 hyperscaler 發債預估約 190 十億美元），惟 30 日事件掃描無新的 hyperscaler 自身發債或 SPV 融資具名披露，複合狀態不成立，不納入計分。
- **資本週期階段** ✗ NOT DISCLOSED（source_ids=ai.capital_cycle）——供給側增速有據（capex 年增 77%），但需求側缺少同一披露內可引證的已實現增速 proxy，且 30 日內的資料中心延後多歸因於電力與併網瓶頸而非需求轉弱，增速證據不足，本次不判定週期階段、不納入計分。
- **AI token 成長** ✗ NOT DISCLOSED（source_ids=ai.token_growth）——本季無 Anthropic／OpenAI／Google 的新 token 量揭露，不納入計分。
**結論**：76 落於估值溢價高檔（CAPE 次高、ECY 負值加深），較前次升 1——CAPE 與趨勢偏離兩項主計分輸入因拉回而鬆動，但被 ECY 轉為 -0.31% 與 AI 信用定價分歧首度明確firing 所抵銷並略微超過。

### 2. 市場廣度 — 56（weight 13%，Δ +14）
- **市場廣度（A/D 與均線之上佔比）** 10/16 全市場上漲家數約 **29**（%）對下跌 71%，僅 27% 在 50 日均線之上、36% 在 200 日均線之上，綜合均線之上佔比連續第九週下滑至收盤低點 31.27%（2026-10-16，[The Trading Tools](https://www.thetrading.tools/market-breadth)，source_ids=breadth.advance_decline）——200DMA 之上佔比自前次約 53% 崩落至 36%、A/D 一面倒偏弱，為本次最大的單項惡化。
- **前十大集中度** 約 **38.9**（%）美國大型股總市值（科技類股占 S&P 500 市值 33.9%、為 2000 年 3 月以來最高）（2026-07-31，[Walnut Invest](https://walnutinvest.com/stats/market-concentration-statistics)，source_ids=breadth.top10_concentration）——仍處 2025 年 10 月紀錄 41.7% 下方但高於歷史任一泡沫期（2000 年約 26%），集中度結構未改善。
- **equal-weight 對 cap-weight（RSP/SPY）** RSP YTD 約 **12.08**（%）對 SPY 約 11.28%（2026-07-18，[TheStreet Pro](https://pro.thestreet.com/market-commentary/rsp-vs-spy-does-diversification-require-equal-weight)，source_ids=breadth.rsp_spy）——等權在年中仍小幅領先 cap-weight，是本維度唯一尚未轉負的訊號，但該讀數為年中快照、未反映 10 月的權值股主導回落。
**結論**：56 落於明顯轉窄（41–60）上緣，較前次升 14 並觸發 ⚠——200DMA 之上佔比 53%→36%、上漲家數僅 29%、綜合廣度連九週下滑，指數淨變動幾近持平卻由少數權值股撐住，是「指數與廣度背離」的典型；僅 RSP 年中領先與集中度未再創高撐住上緣。

### 3. 投機行為 — 44（weight 18%，Δ -4）
- **+AI 改名／SPAC** ✓ SEARCH-VERIFIED（0 件，source_ids=speculation.ai_rename_spac）——7 日窗（2026-10-11 起）掃描完成，無合格的 +AI 改名／代號變更或 SPAC 宣布事件。
- **IPO 熱度** 本週美國定價檔數稀少、且兩週內已有第 **4** 檔交易撤件或延後（Firmus 於 10/9 因機構需求不足撤回 50 億美元 IPO，Oura 延後 21 億美元 IPO；Accelevation 以低於區間定價募 5.4 億美元；Anthropic 掛在 10/23 日曆但尚無價格區間）（2026-10-16，[IPOX Update](https://www.ipox.com/ipox/the-ipox-update-10162026)，source_ids=speculation.ipo_heat）——IPO 窗口正在收窄而非狂熱，投資人開始要求估值折價，尤其對 AI 基礎建設發行人；屬投機降溫的主要證據。
- **巨型 AI IPO pipeline** Anthropic 目標最快 **11** 月中上市（10/14 於舊金山舉行法人說明會，承銷由 Goldman Sachs／JPMorgan／Morgan Stanley 主辦，據 Reuters 看過的 S-1 目標估值達 2 兆美元）（2026-10-05，[CNN](https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market)，source_ids=speculation.upcoming_ai_ipos）——30 日窗內具名且已進入法人行銷階段，屬流動性抽離風險與晚期循環標記，是本維度唯一的明確加項。
- **microcap thematic moonshot** ✓ SEARCH-VERIFIED（0 件，source_ids=speculation.microcap_moonshots）（掃描窗 2026-10-11 起，資料日期 —）——7 日窗內無 <$1B 市值、季營收 ≤$5M 且疊 2＋ 熱門主題的單日 ≥100% 標的（PFAI 10/7 的 +116.7% 落在窗外）。
- **AI 領導股 insider 集中賣出** ✓ SEARCH-VERIFIED（0 件，source_ids=speculation.insider_form4）（掃描窗 2026-10-04 起，資料日期 —）——14 日窗內 NVDA 雖有 10/9 的 Form 4 申報，但無法取得符合契約要求的具名申報人、交易日與金額等 filing-level 細節，依規定不得引用舊名單或舊金額，故記 0 件。
- **Cboe equity put/call** ✗ NOT DISCLOSED（source_ids=speculation.equity_put_call）——Cboe 當期每日統計本次無可公開稽核的當前值（最近可得為 8/3 的 0.55，已過期），該輸入退出計分、不因缺值調降分數，不納入計分。
**結論**：44 落於投機升溫（41–60）下緣，較前次降 4——改名／SPAC、moonshot、insider 三項篩選同時 0 件，且 IPO 市場兩週內四檔撤件、AI 基礎建設發行人募資失敗，投機面明顯收縮；僅 Anthropic 近 2 兆美元估值的巨型 IPO 進入行銷階段撐住分數不致更低。

### 4. 散戶情緒 — 42（weight 12%，Δ -4）
- **CNN Fear & Greed** 約 **18**（Extreme Fear）（2026-10-16，[Finhacker](https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/)，source_ids=retail.fear_greed）——自一週前的 46（中性）崩落至極度恐懼區、單日下挫約 12 點，散戶風險胃納急速轉冷，是本維度最大的下行推力。
- **FINRA margin debt** 約 **1.45**（兆美元；8 月月增約 366 億、YoY 約 +37%，為歷史次高、僅低於 6 月的 1.50 兆）（2026-08-31，[The Trading Tools](https://www.thetrading.tools/margin-debt)，source_ids=retail.margin_debt）——9 月數據尚未發布，沿用 8 月月報（stock-of-state）；7 月創紀錄單月降幅後 8 月再度回升，YoY 逼近但未破 +40% 的頂部級門檻。
- **AAII 投資人調查** 看多約 **38.7**（%）、看空 41.6%、中性 19.7%，多空價差 -2.9%（2026-10-14，[AAII](https://www.aaii.com/sentimentsurvey)，source_ids=retail.aaii）——看多仍高於歷史均值 37.5%，但看空連續第 36 週高於均值、中性異常偏低，散戶分歧加大而非一致看多。
- **家庭股票配置** 約 **48.23**（% of 金融資產，2026-04-01 季，FRED series=BOGZ1FL153064486Q，source_ids=retail.household_equity_allocation）——季頻、本次無新一季揭露，沿用 Q2 水位；仍在歷史高位附近，家庭部位已滿、後續加碼空間受限（Farrell #5）。
- **NAAIM 曝險指數** ✗ NOT DISCLOSED（source_ids=retail.naaim）——8/1 起對非會員轉為訂閱制，本次無可公開稽核的當週值，不納入計分（confirmation cross-check，其缺值不得調降主分）。
- **社群投機（WSB／cashtag）** ✗ NOT DISCLOSED（source_ids=retail.social_sentiment）——7 日窗內無可稽核發布日期的具名迷因狂熱事件，不納入計分。
**結論**：42 落於 41–60 下緣，較前次降 4——F&G 自 46 崩落至 18（極度恐懼）主導本次下修，AAII 看空升至 41.6%；惟 margin debt 回升至 1.45 兆（YoY 約 +37%）與家庭持股 48.23% 的結構性滿倉為分數設下地板，情緒已冷而部位未退正是脆弱點。

### 5. 貨幣與信貸環境 — 85（weight 20%，Δ +6）
- **Fed funds 目標區間** 3.75–4.00%（上緣 **4.00**，2026-10-17，FRED series=DFEDTARU，source_ids=monetary.fed_funds）——自前次基準以來實際升息 25 bps（自 3.50–3.75%），DFEDTARL 下緣同日為 3.75%，政策端已由觀望轉為實際緊縮。
- **HY OAS** **3.23**%（週Δ +58 bps，2026-10-15，FRED series=BAMLH0A0HYM2，source_ids=monetary.hy_oas）——單期走闊 +58 bps 超過 +50 bps 的擊發門檻、且使 `hy_oas_widening_streak` 累進至 3；絕對水位仍在循環低位，但走闊速度為此信用循環最快，是本次扳機擊發的直接來源。
- **IG OAS** **0.84**%（週Δ +4 bps，2026-10-15，FRED series=BAMLC0A0CM，source_ids=monetary.ig_oas）——投資級僅微幅走闊、續處史低區間，與 HY 的 +58 bps 形成強烈分化：壓力集中在低評級與 AI 相關債，尚未擴散至整體投資級。
- **CPI YoY** **3.72**%（資料月 2026-09-01，FRED series=CPIAUCSL，source_ids=monetary.cpi_yoy）——9 月印出自 8 月約 3.4% 跳升、月增 0.6%，為本次全市場重定價與 Fed 升息定價的直接觸媒；仍低於 4% 的錨點門檻。
- **5y5y forward（T5YIFR）** **2.33**%（週Δ +1 bps，2026-10-16，FRED series=T5YIFR，source_ids=monetary.t5yifr）——長端通膨預期僅微升、仍被良好錨定，是通膨鏈尚未完成傳導的關鍵證據，也意味 Fed put 在衰退情境下仍部分可得。
- **10Y 期限溢價（term premium）** **1.0729**%（週Δ -1.2 bps，2026-10-09，FRED series=THREEFYTP10，source_ids=monetary.term_premium）——Kim-Wright 三因子模型；本次為小幅下行、遠低於 +15 bps 的槓桿鏈初啟門檻，財政風險再定價本次不是衝擊源。
- **repo 資金壓力（SOFR−IORB）與 SRF 動用** **SOFR** 3.89%、SOFR−IORB -1 bps、99th 尾差 +7 bps、SRF 動用 0（as_of 2026-10-15，FRED series=SOFR，source_ids=monetary.repo_stress_srf）——利差為負、尾差溫和、SRF 零動用，secured-funding 完全無壓力；四腿（SOFR／SOFR99／IORB／RPONTTLD）均成功取得，IORB 以 3.90% 的生效日觀測對齊。
- **美債標售需求（auction tail / bid-to-cover）** 10/7 的 10Y 標售得標利率 5.300%、bid-to-cover 約 **2.77**（高於前次 2.71 與近十次均值 2.52）、indirect 承接 80.34%、primary dealer 僅 2.54%（2026-10-07，[RTTNews](https://www.rttnews.com/3697286/ten-year-note-auction-attracts-strong-demand.aspx)，source_ids=monetary.treasury_auctions）——需求強勁、無明顯 tail，財政供給壓力未反映在標售端（confirmation，不主計分）。
- **Fed 資產負債表（WALCL）** $6.76T（**6,755,639** 百萬美元，2026-10-14，FRED series=WALCL，source_ids=monetary.walcl）——較前次增約 150 億美元、大致持平微增，準備金環境未同步收緊，是本次信用走闊並非源於央行流動性抽離的證據。
- **ECB 資產（ECBASSETSW）** €5.94T（**5,943,911** 百萬歐元，2026-10-09，FRED series=ECBASSETSW，source_ids=monetary.ecb_boj）——較前次增約 327 億歐元，歐元區流動性小幅回升。
- **BOJ 資產（JPNASSETS）** ¥625.03T（**6,250,253** 億日圓，2026-09-01，FRED series=JPNASSETS，source_ids=monetary.ecb_boj）——月頻、本次無新觀測（no_new_obs），資產負債表持平。
- **PBoC 流動性** 社會融資規模 1–7 月約 **22.25**（兆人民幣，年減 1.74 兆；存量 463.27 兆、YoY +7.4%）（2026-08-15，[SteelOrbis](https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm)，source_ids=monetary.pboc）——9 月數據尚未取得、沿用最新可得月報；中國信用脈衝續縮（confirmation，全球流動性交叉檢核）。
- **私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）** ✗ NOT DISCLOSED（source_ids=monetary.private_credit_liquidity）——30 日窗（2026-09-18 起）內無具可稽核發布日期的新 gate proration / breach、redemption-request ratio 惡化或 net inflow→outflow flip 揭露。背景（窗外、不計分、不觸發扳機）：Fitch 統計 16 檔永續非交易型 BDC 中 10 檔於 Q2 觸及 5% 上限、產業平均申請比率 10.3%，BCRED 連續第三季以 5% 上限限縮、Apollo 估 2026 年申請者於 Q3 付款後約可取回 75%；上述皆無法確認落在本窗內，依規定不納入計分。
**結論**：扳機側；HY OAS 單期 +58 bps 已觸發 `hy_oas_fired` 擊發判準、streak 累進至 3 同時觸發 `hy_streak`，且 Fed 實際升息至 3.75–4.00%、CPI 升至 3.72%、AI 複合體 CDS 創歷史新高，融資環境已由「寬鬆但自滿」轉為「擊發中」；85 較前次升 6 而落入 81–100——雙向計分下 IG 0.84% 的極端自滿與已擊發的信用走闊同時推高分數，惟 repo、期限溢價、標售三項壓力指標皆正常，故屬信用面單點擊發而非全面 financing crisis。

### 6. 結構性槓桿 — 80（weight 15%，Δ +3）
- **槓桿 ETF AUM** 單一個股槓桿 ETF 規模約 **40.04**（十億美元；620 檔／18 家發行人，近五日淨流入約 8.36 億美元、YTD 約 125.84 億美元）（2026-10-16，[ETF Action](https://www.etfaction.com/single-stock-traders-pile-into-tsll-and-intw-as-levered-flows-surge/)，source_ids=structural.leveraged_etf_aum）——自前次約 40.74 億規模持平，但本次由前次的淨流出翻轉為淨流入：在指數回落的同一週散戶仍加碼槓桿多頭，屬逆勢加槓桿的警訊。
- **0DTE 佔比** SPX 0DTE 月度 ADV 創紀錄約 **3.4**（百萬口；季度 ADV 亦創紀錄 3.2 百萬口，SPX 整體季度 ADV 4.9 百萬口為史上第二佳）（2026-09-30，[Cboe](https://www.cboe.com/insights/posts/market-metrics-that-matter-derivatives-september-2026-volume-highlights)，source_ids=structural.zero_dte）——Cboe 9 月統計未揭露 0DTE 占 SPX 量的百分比（最近可得為 7 月的 66.2%），本次以創紀錄 ADV 判讀方向性投機強度續處高檔。
- **OCC 期權總量** 9 月總結算量約 **1,486,062,415**（口，YoY +6.2%；全市場總量 1,490,108,057 口，2026 年 YTD 日均 70,565,120 口、YoY +20.6%）（2026-09-30，[OCC](https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report)，source_ids=structural.options_volume）——量能續創高檔且月增，衍生品參與度未因波動上升而退場。
- **跨資產衍生性** 10/12 時 VIX 約 **14.84**、VIX 近月期貨 17.00（contango），SKEW 升至 154.34（+3.45%）、逼近區間高點（2026-10-12，[Saxo Options Brief](https://www.home.saxo/content/articles/options/the-middle-got-cheaper-the-edge-did-not---options-brief---12-october-2026-12102026)，source_ids=structural.cross_asset_derivatives）——分佈中段變便宜而尾部變貴：市場在 10/14 重定價之前已先為尾部付費，與其後的 VIX 跳升一致（confirmation）。
- **VIX/S&P 500 同向檢測** comove=false（VIX **16.46**、vix_chg +6.81%、sp500_chg -0.27%；as_of 2026-10-15、base_date 2026-10-08、window_days 7，FRED series=VIXCLS，source_ids=structural.vix_spx_comove）——VIX 漲逾門檻但 S&P 500 同窗為小幅下跌、未達 +0.5%，屬正常負相關避險而非 crowded-optionality 同漲，本次不上調級距（不得反向解讀為安全）。
- **AI 基礎建設債務融資／vendor-financing loops** Lambda 於 10/1 完成年內第三筆 GPU 擔保融資、規模約 **1**（十億美元）；CoreWeave 負債已近 350 億美元、季利息約 6.4 億美元且最新 facility 評等僅低於投資級一級，Fluidstack 另有 100 億美元 facility（2026-10-01，[ValueAdd VC](https://valueaddvc.com/pulse/ai-data-center-debt-financing-risk-2026)，source_ids=structural.ai_infrastructure_debt）——30 日窗內多筆大額、以 GPU 為擔保、抵押品價值依賴租金假設的融資同時存在，且本次 CoreWeave 的 CDS 與債券殖利率已明確反映債務條件惡化，屬結構槓桿的主要加項。
- **銀行對 NBFI 放款（LNFACBW027SBOG）** $2.10T（**2,097.97** 十億美元，週增約 2.14%，2026-10-07，FRED series=LNFACBW027SBOG，source_ids=structural.nbfi_bank_loans）——bank–NBFI 曝險自前次 2,054 億續擴至紀錄水位，BIS AER 2026 Ch II 的失序外溢管道持續加寬（confirmation，不主計分）。
- **margin debt 交叉檢核** margin debt 約 **1.45**（兆美元，2026-08-31，[The Trading Tools](https://www.thetrading.tools/margin-debt)，source_ids=structural.margin_debt_crosscheck）——margin debt／股票市值比率僅作交叉檢核，主計分留在 D4（confirmation，不主計分）。
- **美國單一個股槓桿 ETF 核准／上市** ✓ SEARCH-VERIFIED（0 件，source_ids=structural.us_single_stock_etf）（掃描窗 2026-09-18 起，資料日期 —）——30 日窗內 SEC EDGAR／ETF.com 新上市 feed 掃描完成，無新的美國單一個股槓桿 ETF 核准或上市（SEC 對新產品的槓桿上限仍維持 2 倍）。
- **全球槓桿產品擴散** ✗ NOT DISCLOSED（source_ids=structural.global_leveraged_approvals）——7 日窗內韓／台／日／歐皆無英文具名單一個股槓桿核准；韓國 FSC 於 10/8 僅就既有制度爭議答辯、且新上市審查仍處暫停與門檻提高狀態，本週擴散訊號未觸發，不納入計分。
- **美債基差交易槓桿（Treasury basis-trade leverage）** ✗ NOT DISCLOSED（source_ids=structural.treasury_basis_trade）——script 的 `cftc_lev_funds`／`move_index`／`ofr_repo` 三區塊本次皆 fetch_failed（cftc.gov 於本執行環境遭 403 封鎖），WebSearch fallback 亦未取得當期 CFTC 淨部位或 MOVE 週變動的可稽核值，且 7 日窗內無具名基差／swap-spread 失序平倉或國債市場失序（Treasury market dysfunction）報導，不納入計分。
**結論**：80 落於高度集中（61–80）上緣，較前次升 3——AI 基礎建設債務的條件惡化首度被價格確認（CoreWeave CDS 創紀錄、債券殖利率一度 16%）、銀行對 NBFI 放款續創高、0DTE 與 OCC 量能雙創紀錄，且單一個股槓桿 ETF 在回落週仍淨流入；未進一步升至 81–100 是因全球擴散訊號未觸發、comove=false，且美債基差交易槓桿本次無新證據。

## 綜合分數

| 維度 | 權重 | 分數 | 加權分數 |
|---|---:|---:|---:|
| 估值溢價 | 22% | 76 | 16.72 |
| 市場廣度 | 13% | 56 | 7.28 |
| 投機行為 | 18% | 44 | 7.92 |
| 散戶情緒 | 12% | 42 | 5.04 |
| 貨幣與信貸環境 | 20% | 85 | 17.00 |
| 結構性槓桿 | 15% | 80 | 12.00 |

加權總分：65.96 → 66【高】
邊界帶：總分 66 距 警戒/高 邊界 ≤ 2 分，評分固有噪音約 ±2–3，等級判讀需保留餘地。

## 歷史泡沫週期對比

相似度計算：checklist v2
- 1973/1 Nifty Fifty 頂：命中 4/8 = 50%
- 1997 早期建設：命中 3/8 = 40%
- 1998 LTCM 衝擊：命中 5/8 = 65%
- 1999 晚期狂熱：命中 5/10 = 50%
- 2000/3 頂點：命中 1/8 = 15%
- 2021/12 Meme 頂：命中 2/8 = 25%
2000/3 高位回落條件：否

**1973/1 Nifty Fifty 頂 feature audit**
- 1973.1｜未命中｜source_ids=—｜估值溢價 76 < 80
- 1973.2｜未命中｜source_ids=—｜市場廣度 56 < 60
- 1973.3｜未命中｜source_ids=—｜CPIAUCSL yoy_pct 3.72% < 4
- 1973.4｜命中｜source_ids=—｜T5YIFR 週Δ +1 bps ≥ 0（通膨預期未回落）
- 1973.5｜命中｜source_ids=—｜DCOILWTICO chg_pct +0.63% ≥ 0.5
- 1973.6｜未命中｜source_ids=—｜decomposition.driver=unknown ≠ breakeven（三腿視窗不一致）
- 1973.7｜命中｜source_ids=—｜扳機狀態 已擊發 ≥ 初啟
- 1973.8｜命中｜source_ids=—｜散戶情緒 42 < 55（機構主導、散戶未狂熱）

**1997 早期建設 feature audit**
- 1997.1｜未命中｜source_ids=—｜估值溢價 76 不在 40–74
- 1997.2｜未命中｜source_ids=—｜市場廣度 56 ≥ 45
- 1997.3｜命中｜source_ids=—｜投機行為 44 < 50
- 1997.4｜命中｜source_ids=ai.hyperscaler_capex｜hyperscaler capex 指引仍上修（2026 合計約 725、年增 77%，Alphabet 上修至 205）
- 1997.5｜命中｜source_ids=—｜散戶情緒 42 < 55
- 1997.6｜未命中｜source_ids=—｜結構性槓桿 80 ≥ 50
- 1997.7｜未命中｜source_ids=—｜HY OAS 3.23% < 4 但週Δ +58 bps > 0（本次大幅走闊）
- 1997.8｜未命中｜source_ids=—｜扳機狀態 已擊發 ≠ 未擊發

**1998 LTCM 衝擊 feature audit**
- 1998.1｜命中｜source_ids=structural.cross_asset_derivatives｜HY OAS 週Δ +58 bps ≥ 30（機器判準已成立；VIX 14.84 < 25 不另需）
- 1998.2｜未命中｜source_ids=—｜S&P 500 較前次 +0.03% > -5
- 1998.3｜無資料｜source_ids=—｜私募信貸與美債基差槓桿本次皆無窗內具名壓力事件證據（兩者均 ✗ NOT DISCLOSED）
- 1998.4｜無資料｜source_ids=—｜FedWatch 本次無可稽核當期快照（✗ NOT DISCLOSED），無法判定 Fed 路徑是否轉鴿
- 1998.5｜命中｜source_ids=—｜估值溢價 76 ≥ 60
- 1998.6｜命中｜source_ids=—｜扳機狀態 已擊發 ≥ 初啟
- 1998.7｜命中｜source_ids=—｜市場廣度 Δ +14 ≥ 8（急轉弱）
- 1998.8｜命中｜source_ids=—｜ΔT10YIE -1 bps ≤ 0（通膨預期非主因）

**1999 晚期狂熱 feature audit**
- 1999.1｜命中｜source_ids=—｜估值溢價 76 ≥ 75
- 1999.2｜命中｜source_ids=valuation.sp500_pe_cape｜Shiller CAPE 約 40.54 ≥ 38
- 1999.3｜未命中｜source_ids=—｜投機行為 44 < 60
- 1999.4｜未命中｜source_ids=speculation.microcap_moonshots,speculation.ipo_heat｜本週 moonshot 0 件，且 IPO 市場兩週內四檔撤件、無無營收發行人佔比偏高的揭露
- 1999.5｜命中｜source_ids=—｜市場廣度 56 ≥ 45（轉窄）
- 1999.6｜未命中｜source_ids=—｜D5 為扳機側（非自滿側）
- 1999.7｜命中｜source_ids=—｜結構性槓桿 80 ≥ 60
- 1999.8｜未命中｜source_ids=—｜散戶情緒 42 < 55
- 1999.9｜命中｜source_ids=speculation.upcoming_ai_ipos｜Anthropic 30 日內具名進入法人行銷、目標 11 月中上市
- 1999.10｜未命中｜source_ids=—｜扳機狀態 已擊發 ≠ 未擊發

**2000/3 頂點 feature audit**
- 2000.1｜未命中｜source_ids=—｜估值溢價 76 < 85
- 2000.2｜命中｜source_ids=—｜扳機狀態 已擊發 ≥ 初啟
- 2000.3｜未命中｜source_ids=—｜市場廣度 56 < 60
- 2000.4｜未命中｜source_ids=—｜前次 dev200 6.9% ≤ 10 且 S&P 本次 +0.03% > -5（高位回落不成立）
- 2000.5｜未命中｜source_ids=—｜投機行為 44 < 70
- 2000.6｜未命中｜source_ids=speculation.insider_form4｜14 日窗內 Form 4 篩選完成但 0 件合格（無 filing-level 具名細節）
- 2000.7｜未命中｜source_ids=—｜散戶情緒 42 < 65
- 2000.8｜無資料｜source_ids=—｜FedWatch 無當期快照（✗ NOT DISCLOSED），且 decomposition.driver=unknown 非 breakeven 主導，貨幣轉緊判據無可稽核輸入

**2021/12 Meme 頂 feature audit**
- 2021.1｜未命中｜source_ids=—｜散戶情緒 42 < 65
- 2021.2｜無資料｜source_ids=—｜社群投機（WSB／cashtag）本次無可稽核發布日期的具名標的
- 2021.3｜命中｜source_ids=—｜結構性槓桿 80 ≥ 65
- 2021.4｜未命中｜source_ids=—｜D5 85 ≥ 60 但側別為扳機側、非自滿側
- 2021.5｜未命中｜source_ids=retail.margin_debt｜margin debt YoY 約 +37% < 40
- 2021.6｜未命中｜source_ids=speculation.microcap_moonshots｜本週 microcap moonshot 0 件
- 2021.7｜命中｜source_ids=—｜市場廣度 56 ≥ 50（指數與廣度背離）
- 2021.8｜未命中｜source_ids=—｜CPIAUCSL yoy_pct 3.72% < 4

本次六維組態最貼近「1998 LTCM 衝擊」（65%），且相似度自前次 40% 大幅躍升、首度成為單一最貼近錨：五項命中同時成立——HY OAS 單期走闊 +58 bps 遠超 +30 bps 的衝擊判準、估值溢價 76 ≥ 60、扳機狀態進入已擊發、市場廣度單次 Δ +14 的急轉弱、以及 ΔT10YIE -1 bps 確認通膨預期不是本次利率上行的主因。這正是 1998 型態的核心定義：高估值與高槓桿的位能已積累到頂，然後由一個外生衝擊（1998 年是 LTCM 與俄債，本次是 9 月 CPI 跳升至 3.7% 疊加 AI 債務的回本疑慮）先在信用市場而非股票市場引爆。循環位置判讀為「衝擊已至、尚未演成系統性失序」：信用壓力明確集中在低評級與 AI 複合體（HY +58 bps 對 IG 僅 +4 bps，CoreWeave CDS 1,194.5 bps 對 Oracle 288 bps），而 repo 利差為負、SRF 零動用、10Y 標售 bid-to-cover 2.77 強勁、期限溢價下行——傳導的三個放大節點全部安靜，這是本次與 1998 年 9 月最大的差異，也是「未演成失序」的實證基礎。須明確區分的是，1998.3 與 1998.4 兩項為無資料（私募信貸、基差槓桿、FedWatch 皆無窗內可稽核證據），若後續出現具名非銀機構壓力或 Fed 轉鴿，此錨的相似度將進一步上升。扳機措辭依機器判定：扳機理由為 `hy_oas_fired`、`hy_streak`，不含 `breakeven_wti_up`，且 1973.3 與 1973.4 未雙雙命中（CPI 3.72% < 4%），故**不得**援引「Fed 寬鬆空間受壓縮」的定性，扳機鏈 A 尚未驗證啟動——本次的擊發是信用利差本身，不是通膨鏈的完成傳導。相對 1999／2021 的狂熱型態（本次 50%／25%），差異在於投機與散戶兩面同時缺席：moonshot、改名、insider 三項篩選 0 件，F&G 已在 18 的極度恐懼，IPO 市場兩週四檔撤件——這是衝擊後的收縮，不是頂部前的亢奮。結構性槓桿的期間調整對比：相對 1999／2000 年 3 月的 margin debt 與指數期貨／選擇權投機，本次對應物為 margin debt 1.45 兆（YoY 約 +37%）、單一個股槓桿 ETF 約 400.4 億美元與 0DTE 月度 ADV 創紀錄 3.4 百萬口；相對 2021 年 12 月的迷因槓桿，本次社群投機面明顯缺席（✗ NOT DISCLOSED、moonshot 0 件），這正是 2021 型態僅 25% 的主因。

跨期價格錨（敘事用，不重算）：S&P 500 距 200 日均線 +5.34%、距 52 週均 +6.78%，屬溫和拉伸且本次續收斂；長期相對指數成長趨勢偏離的文章錨點為 Dot-com 約 95%、1929 約 110%、當前 AI 週期約 147%（RIA/Farrell），僅作跨時代敘事對照。投資泡沫宏觀錨（narrative only，BIS AER 2026 Ch I）：AI 投資週期與運河熱（1830s）、英國鐵路狂熱（1840s）、1920s 電氣化、dot-com 並列——真實技術突破吸引超過商業回報所能支撐的資本，且均以投資反轉收場；規模上 AI 相關投資約占美國 GDP 1%、IT 投資合計約 5% 已超越 2000 年峰值。BIS contest model（Rungcharoenkitkul 2026b，經 AER Ch I Graph 11.B 引用）指出 winner-take-all 結構使理性廠商也會過度承諾 capex，累計 capex 由約 $2trn 走向約 $4.5trn 時全行業淨經濟剩餘轉負，而修正之所以急促，正是因為 circular financing 網把單點失望快速傳導至全網——本次 CoreWeave 的 CDS 由 6 月的三分之一水位躍升至 1,194.5 bps、並同步推升 Oracle 至 288 bps 與四大 hyperscaler CDS 齊創新高，是該傳導機制的首次實價演示。歷史細部類比錨（narrative only）：1999–2001 光纖／電信週期與當前 AI 投資週期結構最近——vendor financing 與 IRU capacity swap 使同一筆收入被多方重複認列，報酬下滑先以會計處理（折舊年限、swap 認列）掩蓋，最終以 capex 反轉與信用事件收場；本次 Lambda 第三筆 GPU 擔保融資、Fluidstack 100 億美元 facility 與 CoreWeave 近 350 億美元負債的組合，對應該型態的現代版。

## 機構情緒對照

BofA 10 月 Global Fund Manager Survey（調查期 10/3–10/9，[Bloomberg](https://www.bloomberg.com/news/articles/2026-10-13/bofa-poll-shows-investors-most-exposed-to-tech-stocks-since-2020) 2026-10-13）為本次新增的機構調查數據：

- 共識部位：科技股淨加碼升至 37%，為 2020 年 8 月以來最高；整體股票淨加碼同步處於高位——機構在調查期（10 月上旬，即本次重定價之前）部位最為擁擠。
- 尾部風險：約 45% 受訪者預期 AI 泡沫會在 2027 年破裂、42% 不認為，另有報導指債券市場風險已超越 AI 泡沫成為首要關切。
- 現金水位：3.9%，與前月持平，仍在 BofA Cash Rule 的 4.0% 賣出訊號門檻之下。
- 反向解讀：高比例的「預期未來崩盤」本身是反向訊號；但本次更值得注意的是調查期落在 10/14 重定價之前，故 37% 的科技淨加碼是衝擊前的部位快照——機構以最擁擠的科技部位迎接了本次 AI 信用重定價，這是後續去槓桿壓力的來源之一。AAII 僅作散戶對照（看多 38.7%、看空 41.6%），不列為機構數據。

另補 NAAIM Exposure Index：最新可公開取得值仍為 79.70（2026-07-29，[MacroMicro](https://en.macromicro.me/series/20540/naaim-exposure-index)）——8/1 起對非會員轉訂閱制，近期週值不可公開稽核，僅作背景（於 D4 為 confirmation cross-check，本次 ✗ NOT DISCLOSED 不計分）。

## 本次新增訊號

各維度變化 vs 前次（35天前）（基準 report-2026-09-13）：
- 估值溢價 75→76（+1）：CAPE 40.73→40.54、距 200DMA +6.9%→+5.34% 雙雙收斂，但 ECY 由約 -0.10% 深化至約 -0.31%（實質利率 +18 bps 所致）；**AI 信用定價分歧首度明確 firing**——CoreWeave 5Y CDS 創紀錄 1,194.5 bps（隱含違約機率約 63%、2031 債殖利率一度 16%）、Oracle 創紀錄 288 bps、Amazon／Alphabet／Meta／Nvidia CDS 齊創新高，信用端已先於股權確認 AI 回本風險。
- 市場廣度 42→56（+14 ⚠）：本次唯一觸發 ⚠ 的位移，也是六維最大單項惡化——200DMA 之上佔比約 53%→36%、50DMA 之上僅 27%，10/16 上漲家數 29% 對下跌 71%，綜合均線之上佔比連續第九週下滑至 31.27% 收盤低點；指數 35 日淨變動幾近持平卻由少數權值股撐住。
- 投機行為 48→44（-4）：+AI 改名／SPAC、microcap moonshot、insider Form 4 三項篩選同時 0 件；IPO 市場兩週內第 4 檔撤件或延後（Firmus 10/9 因機構需求不足撤回 50 億美元 AI 基礎建設 IPO、Oura 延後 21 億美元），Accelevation 低於區間定價。僅 Anthropic 目標 11 月中上市、據 Reuters 看過的 S-1 目標估值 2 兆美元，10/14 已舉行法人說明會，撐住分數。
- 散戶情緒 46→42（-4）：**F&G 自約 35 崩落至 18（Extreme Fear）**、一週前尚為 46 中性；AAII 看空升至 41.6%、連 36 週高於均值，中性 19.7% 異常偏低。惟 margin debt 8 月回升 366 億至 1.45 兆（YoY 約 +37%、歷史次高）、家庭股票配置仍 48.23%——情緒已冷而部位未退。
- 貨幣與信貸環境 79→85（+6）：**側別維持扳機側，但狀態由初啟升級為已擊發**——HY OAS 2.65%→3.23%（單期 +58 bps）超過 +50 bps 擊發門檻、觸發 `hy_oas_fired`，`hy_oas_widening_streak` 累進至 3 使 `hy_streak` 續成立；Fed 實際升息 25 bps 至 3.75–4.00%，9 月 CPI YoY 跳升至 3.72%（月增 0.6%）為直接觸媒，10Y 4.96%→5.10%。關鍵分化：IG OAS 僅 +4 bps 至 0.84%、仍處史低，壓力集中於低評級與 AI 相關債而未擴散。
- 結構性槓桿 77→80（+3）：AI 基礎建設債務條件惡化首度被價格確認——Lambda 10/1 完成年內第三筆 GPU 擔保融資約 10 億美元、CoreWeave 負債近 350 億美元且季利息約 6.4 億美元、最新 facility 僅低於投資級一級，Fluidstack 另有 100 億美元 facility；銀行對 NBFI 放款自 2,054 億續擴至 2,097.97 億（+2.14%）創高；0DTE 月度 ADV 與 OCC 9 月量能雙創高檔；單一個股槓桿 ETF 約 400.4 億美元並在回落週翻為淨流入約 8.36 億美元（逆勢加槓桿）。
- 私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）：本次 ✗ NOT DISCLOSED，30 日窗內無具可稽核發布日期的新 gate proration / breach、redemption-request ratio 惡化或 net inflow→outflow flip；Fitch 的 Q2 統計（16 檔 BDC 中 10 檔觸及 5% 上限、平均申請比率 10.3%）與 BCRED 連三季限縮屬無法確認窗內的背景資訊，不計分、不觸發扳機。
- 美債基差交易槓桿（Treasury basis-trade leverage）：本次 ✗ NOT DISCLOSED，script 的 `cftc_lev_funds`／`move_index`／`ofr_repo` 三區塊皆 fetch_failed（cftc.gov 於本執行環境遭 403），且 7 日窗內無具名國債市場失序（Treasury market dysfunction）事件。
- 機構部位：BofA 10 月 FMS（調查期 10/3–10/9）科技股淨加碼 37% 為 2020 年 8 月以來最高、現金 3.9% 仍低於 4.0% 賣出門檻——機構以衝擊前最擁擠的科技部位迎接本次 AI 信用重定價。
- 格局：分歧 → 穩定共存（三角方向重新收斂，背離壓力移至信用與廣度）；扳機狀態：初啟 → **已擊發**（理由 hy_oas_fired、hy_streak）。
全球槓桿產品擴散：本週擴散訊號未觸發（韓國新上市審查仍暫停且門檻提高，10/8 FSC 僅就既有制度爭議答辯；台／日／歐 7 日窗內無英文具名核准）。

## 數據附錄

### Raw data

| source_id | 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_trend | S&P 500 sp500_trend latest | 7,659.44 | FRED series=SP500 | 2026-10-16 | 2026-10-18T09:08:48+08:00 |
| valuation.sp500_trend | sp500_trend dev200_pct | 5.34 | FRED series=SP500 | 2026-10-16 | 2026-10-18T09:08:48+08:00 |
| valuation.sp500_trend | sp500_trend dev52w_pct | 6.78 | FRED series=SP500 | 2026-10-16 | 2026-10-18T09:08:48+08:00 |
| valuation.sp500_trend | sp500_trend prior_spot | 7,656.98 | FRED series=SP500 | 2026-09-11 | 2026-10-18T09:08:48+08:00 |
| retail.household_equity_allocation | BOGZ1FL153064486Q latest | 48.23 | FRED series=BOGZ1FL153064486Q | 2026-04-01 | 2026-10-18T09:08:48+08:00 |
| monetary.fed_funds | DFEDTARU latest | 4.00 | FRED series=DFEDTARU | 2026-10-17 | 2026-10-18T09:08:48+08:00 |
| monetary.fed_funds | DFEDTARL latest | 3.75 | FRED series=DFEDTARL | 2026-10-17 | 2026-10-18T09:08:48+08:00 |
| monetary.hy_oas | BAMLH0A0HYM2 latest | 3.23 | FRED series=BAMLH0A0HYM2 | 2026-10-15 | 2026-10-18T09:08:48+08:00 |
| monetary.ig_oas | BAMLC0A0CM latest | 0.84 | FRED series=BAMLC0A0CM | 2026-10-15 | 2026-10-18T09:08:48+08:00 |
| monetary.dgs10 | DGS10 latest | 5.10 | FRED series=DGS10 | 2026-10-15 | 2026-10-18T09:08:48+08:00 |
| monetary.dfii10 | DFII10 latest | 2.78 | FRED series=DFII10 | 2026-10-15 | 2026-10-18T09:08:48+08:00 |
| monetary.t10yie | T10YIE latest | 2.35 | FRED series=T10YIE | 2026-10-16 | 2026-10-18T09:08:48+08:00 |
| monetary.wti | DCOILWTICO latest | 101.91 | FRED series=DCOILWTICO | 2026-10-14 | 2026-10-18T09:08:48+08:00 |
| monetary.cpi_yoy | CPIAUCSL yoy_pct | 3.72 | FRED series=CPIAUCSL | 2026-09-01 | 2026-10-18T09:08:48+08:00 |
| monetary.t5yifr | T5YIFR latest | 2.33 | FRED series=T5YIFR | 2026-10-16 | 2026-10-18T09:08:48+08:00 |
| monetary.term_premium | THREEFYTP10 latest | 1.0729 | FRED series=THREEFYTP10 | 2026-10-09 | 2026-10-18T09:08:48+08:00 |
| monetary.repo_stress_srf | SOFR latest | 3.89 | FRED series=SOFR | 2026-10-15 | 2026-10-18T09:08:48+08:00 |
| monetary.repo_stress_srf | SOFR99 latest | 3.97 | FRED series=SOFR99 | 2026-10-15 | 2026-10-18T09:08:48+08:00 |
| monetary.repo_stress_srf | IORB latest | 3.90 | FRED series=IORB | 2026-10-18 | 2026-10-18T09:08:48+08:00 |
| monetary.repo_stress_srf | RPONTTLD latest | 0.0 | FRED series=RPONTTLD | 2026-10-16 | 2026-10-18T09:08:48+08:00 |
| monetary.walcl | WALCL latest | 6,755,639（$6.76T，百萬美元） | FRED series=WALCL | 2026-10-14 | 2026-10-18T09:08:48+08:00 |
| monetary.ecb_boj | ECBASSETSW latest | 5,943,911（€5.94T，百萬歐元） | FRED series=ECBASSETSW | 2026-10-09 | 2026-10-18T09:08:48+08:00 |
| monetary.ecb_boj | JPNASSETS latest | 6,250,253（¥625.03T，億日圓） | FRED series=JPNASSETS | 2026-09-01 | 2026-10-18T09:08:48+08:00 |
| structural.vix_spx_comove | VIXCLS latest | 16.46 | FRED series=VIXCLS | 2026-10-15 | 2026-10-18T09:08:48+08:00 |
| structural.vix_spx_comove | vix_spx_comove vix | 16.46 | FRED series=VIXCLS,SP500 | 2026-10-15 | 2026-10-18T09:08:48+08:00 |
| structural.nbfi_bank_loans | LNFACBW027SBOG latest | 2,097.97（$2.10T，十億美元） | FRED series=LNFACBW027SBOG | 2026-10-07 | 2026-10-18T09:08:48+08:00 |

### Coverage

| source_id | 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| valuation.sp500_pe_cape | S&P 500 P/E and Shiller CAPE | WebSearch／WebFetch（multpl/GuruFocus） | ✓ SEARCH-VERIFIED |
| valuation.mag7_multiples | Mag 7 weighted P/E | WebSearch | ✓ SEARCH-VERIFIED |
| valuation.analyst_tp_decomposition | Analyst TP upgrade decomposition | WebSearch（best-effort，90d＋同季） | ✗ NOT DISCLOSED |
| valuation.sp500_trend | S&P 500 price-trend deviation | scripts/fetch_macro.py（FRED SP500） | ✓ API |
| valuation.ai_credit_schism | AI 信用定價分歧 | WebSearch（best-effort，14d） | ✓ SEARCH-VERIFIED |
| breadth.rsp_spy | S&P 500 equal-weight | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.top10_concentration | Top-10 concentration | WebSearch | ✓ SEARCH-VERIFIED |
| breadth.advance_decline | Advance/decline ratio | WebSearch | ✓ SEARCH-VERIFIED |
| retail.fear_greed | CNN Fear & Greed Index | WebSearch（CNN 轉載） | ✓ SEARCH-VERIFIED |
| retail.margin_debt | Margin Debt: FINRA | WebSearch（FINRA 轉載） | ✓ SEARCH-VERIFIED |
| retail.aaii | Retail survey: AAII | WebSearch | ✓ SEARCH-VERIFIED |
| retail.social_sentiment | Social sentiment proxies | WebSearch（best-effort，7d） | ✗ NOT DISCLOSED |
| retail.household_equity_allocation | Household equity allocation | scripts/fetch_macro.py（FRED） | ✓ API |
| retail.naaim | NAAIM Exposure Index | WebSearch（best-effort） | ✗ NOT DISCLOSED |
| institutional.bofa_jpm_survey | BofA Fund Manager Survey | WebSearch（best-effort） | ✓ SEARCH-VERIFIED |
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
| monetary.fedwatch | Fed funds rate path expectations | WebSearch（CME FedWatch，best-effort） | ✗ NOT DISCLOSED |
| monetary.walcl | Fed balance sheet: FRED | scripts/fetch_macro.py（FRED） | ✓ API |
| monetary.ecb_boj | Global central bank liquidity cross-check | scripts/fetch_macro.py（FRED ECBASSETSW/JPNASSETS 均 ok） | ✓ API |
| monetary.pboc | PBoC aggregate financing | WebSearch（PBoC 月報轉載，best-effort） | ✓ SEARCH-VERIFIED |
| monetary.private_credit_liquidity | Private-credit / non-bank fund liquidity stress | WebSearch（best-effort，30d） | ✗ NOT DISCLOSED |
| ai.hyperscaler_capex | Hyperscaler capex guidance | WebSearch（Q2 2026 財報，stock-of-state 沿用） | ✓ SEARCH-VERIFIED |
| ai.token_growth | AI token volume growth rate | WebSearch（best-effort） | ✗ NOT DISCLOSED |
| ai.openai_anthropic_revenue | OpenAI / Anthropic annualized revenue | WebSearch（best-effort） | ✓ SEARCH-VERIFIED |
| ai.customer_concentration_rpo | Hyperscaler AI customer concentration | WebSearch（best-effort） | ✗ NOT DISCLOSED |
| ai.compute_supply_demand | AI compute supply/demand and overcapacity risk | WebSearch（best-effort） | ✓ SEARCH-VERIFIED |
| ai.hyperscaler_financing_mix | Hyperscaler 融資結構 | WebSearch（composite：季度狀態＋30 日事件掃描） | ✗ NOT DISCLOSED components=quarterly_state:ok,event_scan:not_disclosed |
| ai.revenue_capex_gap | AI 營收對 capex 缺口 | WebSearch（best-effort，季頻沿用） | ✓ SEARCH-VERIFIED |
| ai.depreciation_life | GPU / 伺服器折舊年限變動 | WebSearch（best-effort，30d） | ✗ NOT DISCLOSED |
| ai.capital_cycle | 資本週期階段 | WebSearch（composite：季度狀態＋30 日事件掃描） | ✗ NOT DISCLOSED components=quarterly_state:not_disclosed,event_scan:not_disclosed |
| speculation.ai_rename_spac | Search for past 7 days | WebSearch（7d 掃描） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.ipo_heat | IPO market heat | WebSearch（IPOX／Renaissance） | ✓ SEARCH-VERIFIED |
| speculation.microcap_moonshots | Microcap thematic moonshots | WebSearch（7d 掃描） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.upcoming_ai_ipos | Upcoming AI IPOs | WebSearch（best-effort，30d） | ✓ SEARCH-VERIFIED |
| speculation.insider_form4 | Insider selling at AI | SEC EDGAR / WebSearch（14d） | ✓ SEARCH-VERIFIED（0 件） |
| speculation.equity_put_call | Cboe equity-only put/call ratio | WebSearch（best-effort） | ✗ NOT DISCLOSED |
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
| structural.treasury_basis_trade | 美債基差交易槓桿（Treasury basis-trade leverage） | script 三區塊 fetch_failed（cftc.gov 403）＋ WebSearch（7d） | ✗ NOT DISCLOSED |

### SEARCH-VERIFIED traceability

| source_id | 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|---|
| valuation.sp500_pe_cape | Shiller CAPE 約 40.54 | Shiller PE CAPE ratio current October 2026 multpl | https://www.multpl.com/shiller-pe | 2026-10-16 | 2026-10-18T10:30:00+08:00 |
| valuation.mag7_multiples | Mag 7 成員 MSFT 前瞻本益比 24.5 | Magnificent 7 forward P/E valuation October 2026 | https://articlegateway.com/?p=146 | 2026-09-24 | 2026-10-18T10:30:00+08:00 |
| valuation.ai_credit_schism | CoreWeave 5Y CDS 紀錄 1,194.5 bps | AI credit fears tech default insurance record highs October 2026 | https://www.businessday.co.za/world/international-companies/2026-10-15-ai-credit-fears-push-tech-default-insurance-to-record-highs/ | 2026-10-15 | 2026-10-18T10:30:00+08:00 |
| breadth.rsp_spy | RSP YTD 報酬約 12.08 | RSP equal weight vs SPY YTD performance 2026 | https://pro.thestreet.com/market-commentary/rsp-vs-spy-does-diversification-require-equal-weight | 2026-07-18 | 2026-10-18T10:30:00+08:00 |
| breadth.top10_concentration | 前十大集中度約 38.9 | S&P 500 top 10 concentration percent record 2026 | https://walnutinvest.com/stats/market-concentration-statistics | 2026-07-31 | 2026-10-18T10:30:00+08:00 |
| breadth.advance_decline | 上漲家數約 29 對下跌 71 | market breadth October 16 2026 percent above 200-day advance decline | https://www.thetrading.tools/market-breadth | 2026-10-16 | 2026-10-18T10:30:00+08:00 |
| retail.fear_greed | Fear Greed 極度恐懼約 18 | CNN Fear and Greed Index October 16 2026 extreme fear | https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/ | 2026-10-16 | 2026-10-18T10:30:00+08:00 |
| retail.margin_debt | margin debt 約 1.45 兆美元 | FINRA margin debt August 2026 year over year | https://www.thetrading.tools/margin-debt | 2026-08-31 | 2026-10-18T10:30:00+08:00 |
| retail.aaii | AAII 看多約 38.7 | AAII sentiment survey week ending October 14 2026 | https://www.aaii.com/sentimentsurvey | 2026-10-14 | 2026-10-18T10:30:00+08:00 |
| institutional.bofa_jpm_survey | 科技股淨加碼約 37 為 2020 年 8 月以來最高 | BofA October 2026 fund manager survey tech overweight cash | https://www.bloomberg.com/news/articles/2026-10-13/bofa-poll-shows-investors-most-exposed-to-tech-stocks-since-2020 | 2026-10-13 | 2026-10-18T10:30:00+08:00 |
| monetary.treasury_auctions | 10Y 標售 bid-to-cover 約 2.77 | Treasury 10-year note auction October 7 2026 bid-to-cover | https://www.rttnews.com/3697286/ten-year-note-auction-attracts-strong-demand.aspx | 2026-10-07 | 2026-10-18T10:30:00+08:00 |
| monetary.pboc | 1–7 月社會融資規模約 22.25 兆人民幣 | PBoC aggregate social financing 2026 total | https://www.steelorbis.com/steel-news/latest-news/chinas-new-aggregate-social-financing-increases-to-rmb-2225-trillion-in-jan-july-2026-1471093.htm | 2026-08-15 | 2026-10-18T10:30:00+08:00 |
| ai.hyperscaler_capex | 四大 hyperscaler 2026 capex 合計約 725 | hyperscaler capex guidance 2026 Microsoft Alphabet Amazon Meta | https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html | 2026-07-28 | 2026-10-18T10:30:00+08:00 |
| ai.openai_anthropic_revenue | Anthropic 年化 run-rate 約 65 | OpenAI Anthropic annualized revenue run rate 2026 | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai | 2026-08-17 | 2026-10-18T10:30:00+08:00 |
| ai.compute_supply_demand | H100 隨選中位租金約 4.20 | GPU rental price index HBM DRAM contract price October 2026 | https://uvik.net/blog/gpu-price-index/ | 2026-10-07 | 2026-10-18T10:30:00+08:00 |
| ai.hyperscaler_financing_mix | [quarterly_state] 2026 年 hyperscaler 發債預估約 190 | hyperscaler bond issuance 2026 capex versus free cash flow | https://www.twentyfouram.com/insights/oracle-clears-the-supply-cloud-with-record-demand | 2026-02-02 | 2026-10-18T10:30:00+08:00 |
| ai.revenue_capex_gap | 年化 AI 終端營收：Anthropic run-rate 約 65 | AI revenue versus capex gap 2026 annualized | https://axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai | 2026-08-17 | 2026-10-18T10:30:00+08:00 |
| speculation.ipo_heat | 兩週內第 4 檔 IPO 撤件或延後 | IPO market October 16 2026 pulled postponed Firmus Oura | https://www.ipox.com/ipox/the-ipox-update-10162026 | 2026-10-16 | 2026-10-18T10:30:00+08:00 |
| speculation.upcoming_ai_ipos | Anthropic 目標 11 月中上市 | Anthropic IPO October 2026 timing valuation S-1 | https://www.cnn.com/2026/10/05/business/anthropic-ipo-stock-market | 2026-10-05 | 2026-10-18T10:30:00+08:00 |
| structural.leveraged_etf_aum | 單一個股槓桿 ETF 規模約 40.04 | single stock leveraged ETF assets October 2026 weekly flows | https://www.etfaction.com/single-stock-traders-pile-into-tsll-and-intw-as-levered-flows-surge/ | 2026-10-16 | 2026-10-18T10:30:00+08:00 |
| structural.zero_dte | SPX 0DTE 月度 ADV 創紀錄約 3.4 百萬口 | Cboe September 2026 derivatives volume 0DTE SPX record | https://www.cboe.com/insights/posts/market-metrics-that-matter-derivatives-september-2026-volume-highlights | 2026-09-30 | 2026-10-18T10:30:00+08:00 |
| structural.options_volume | 9 月總結算量約 1,486,062,415 口 | OCC September 2026 monthly volume data | https://www.theocc.com/newsroom/views/2026/10-02-september-2026-monthly-volume-report | 2026-09-30 | 2026-10-18T10:30:00+08:00 |
| structural.cross_asset_derivatives | VIX 約 14.84、SKEW 154.34 | VIX term structure SKEW October 2026 options brief | https://www.home.saxo/content/articles/options/the-middle-got-cheaper-the-edge-did-not---options-brief---12-october-2026-12102026 | 2026-10-12 | 2026-10-18T10:30:00+08:00 |
| structural.margin_debt_crosscheck | margin debt 對股票市值比率基數約 1.45 兆美元 | margin debt to market cap August 2026 | https://www.thetrading.tools/margin-debt | 2026-08-31 | 2026-10-18T10:30:00+08:00 |
| structural.ai_infrastructure_debt | Lambda GPU 擔保融資約 1 十億美元 | AI data center debt Lambda CoreWeave financing October 2026 | https://valueaddvc.com/pulse/ai-data-center-debt-financing-risk-2026 | 2026-10-01 | 2026-10-18T10:30:00+08:00 |
| speculation.ai_rename_spac | +AI 改名／SPAC 7 日掃描（0 件） | AI company name change ticker SPAC announcement October 2026 | 檢查來源：SEC EDGAR 8-K、SPACInsider、Boardroom Alpha（窗內無合格事件） | — | 2026-10-18T10:30:00+08:00 |
| speculation.microcap_moonshots | microcap moonshot 掃描（0 件符合 2+ 主題×弱基本面） | biggest stock gainers week October 12-16 2026 microcap 100% | 檢查來源：Tapeboard movers archive、Financial Modeling Prep daily gainers、Yahoo movers（PFAI 10/7 +116.7% 落在窗外） | — | 2026-10-18T10:30:00+08:00 |
| speculation.insider_form4 | AI 領導股 Form 4 14 日掃描（0 件合格） | insider selling Form 4 October 2026 Nvidia AI executives SEC | 檢查來源：SEC EDGAR NVDA CIK 0001045810 Form 4 列表（10/9 有申報但無具名申報人／金額等 filing-level 細節） | — | 2026-10-18T10:30:00+08:00 |
| structural.us_single_stock_etf | 美國單一個股槓桿 ETF 30 日核准／上市（0 件） | single stock leveraged ETF launch approval October 2026 SEC | 檢查來源：SEC EDGAR ETF 申報、ETF.com 新上市 feed（窗內無合格核准或上市） | — | 2026-10-18T10:30:00+08:00 |

## 本次分數存檔
```json
{
  "date": "2026-10-18",
  "iso_week": "2026-W42",
  "weekday": "Sunday",
  "timezone": "Asia/Taipei",
  "valuation": 76,
  "breadth": 56,
  "speculation": 44,
  "retail": 42,
  "monetary": 85,
  "structural": 80,
  "total": 66,
  "tier": "高",
  "regime": "穩定共存",
  "trigger_state": "已擊發",
  "trigger_reasons": [
    "hy_oas_fired",
    "hy_streak"
  ],
  "monetary_side": "扳機側",
  "hy_oas_widening_streak": 3,
  "sp500_dev200_pct": 5.34
}
```

本報告為相對風險溫度計，非擇時訊號。

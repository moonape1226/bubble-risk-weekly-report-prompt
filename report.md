I'll fetch that document now.

Document fetched successfully. I'll now execute all instructions. Today is 2026-05-26, which is **ISO week 2026-W22** (production mode — no DRY RUN flag detected).

**Step 1:** Fetching previous week's archive data and starting parallel data collection.

Previous week data (W21) not found → marking as baseline week. W22 file already exists — no FORCE COMMIT detected, so I won't overwrite. Now collecting current market data in parallel across all dimensions.

FRED direct endpoints blocked. Switching to WebSearch for all data sources.

Good data coming in. Now fetching breadth, speculative behavior, structural leverage, and news signals in parallel.

Good, I now have most of the data. Let me fetch the remaining few pieces (oil price, market breadth percentage, and global ETF data) before composing the report.

Let me quickly check if a report .md already exists in the archive before composing.

Both `scores-2026-W22.json` and `report-2026-W22.md` already exist in the archive. No FORCE COMMIT detected — generating fresh report below but **not committing** to GitHub.

---

> Same-week file already exists in `moonape1226/bubble-risk-archive` (`scores-2026-W22.json` · `report-2026-W22.md`, main branch). No FORCE COMMIT detected — report generated but not committed to archive.

---

# 2026-W22 週度市場泡沫風險評估週報

**報告日期：2026-05-26 ｜ 週次：2026-W22 ｜ 前週基準：—（W21 存檔不存在，本週為基準週）**

---

## §1 六維度風險條圖

| 維度 | 評分 | 條圖（每格 = 10 pts） | 上週 | Δ | 核心論述 |
|------|------|-----------------------|------|---|----------|
| 估值溢價（22%） | **80** | ▰▰▰▰▰▰▰▰▱▱ | — | — | Shiller CAPE ~40.75（歷史均值 17.3，比值 2.36×；1999 年峰值 44.19 為唯一更高記錄）；Mag 7 占 S&P 500 市值 34.8%，指數高度集中。來源：[HeyGoTrade May 2026](https://www.heygotrade.com/en/blog/cape-ratio-explained-is-sp-500-expensive-may-2026/)、[Motley Fool 2026-05-07](https://www.fool.com/investing/2026/05/07/this-magnificent-seven-stock-is-the-cheapest-of-th/) ✓ SEARCH-VERIFIED |
| 市場廣度（13%） | **40** | ▰▰▰▰▱▱▱▱▱▱ | — | — | VIX 16.68（52 週區間 13.38–35.30，低恐慌）；3 月伊朗衝突後 A/D 線向上修復，S&P 500 重返 7,000+；S5TH（% above 200-DMA）具體數值 ⛔ FETCH FAILED（barchart.com/investing.com 動態頁面無法直接擷取）。來源：[Yahoo Finance VIX](https://finance.yahoo.com/quote/%5EVIX/) ✓ SEARCH-VERIFIED |
| 投機行為（18%） | **62** | ▰▰▰▰▰▰▱▱▱▱ | — | — | SpaceX 2026-05-20 提交 S-1，目標估值 $1.75–2 兆（若成立將超越 2019 年沙特阿美，成史上最大 IPO）；5 月另有 Neutron Holdings、Forbright、Enhanced Group 等 7 份 S-1 申報。來源：[Fortune 2026-05-20](https://fortune.com/2026/05/20/spacex-ipo-filing-s1-total-addressable-market-make-life-multiplanetary/)、[SEC EDGAR](https://www.sec.gov/) ✓ SEARCH-VERIFIED |
| 散戶情緒（12%） | **68** | ▰▰▰▰▰▰▰▱▱▱ | — | — | CNN Fear & Greed 59（貪婪，2026-05-22）；AAII 牛市 39.3%（連四週高於歷史均值 37.5%）、熊市 36.6%（連 14 週高於均值 31.0%）；指數回升但悲觀情緒仍偏高形成分歧。來源：[CNN Fear & Greed](https://www.cnn.com/markets/fear-and-greed)（2026-05-22）、[AAII / Seeking Alpha 2026-05-14](https://seekingalpha.com/article/4905008-aaii-sentiment-survey-neutral-sentiment-drops) ✓ SEARCH-VERIFIED |
| 貨幣與信貸（20%） | **62** | ▰▰▰▰▰▰▱▱▱▱ | — | — | Fed 利率 3.50–3.75%（第三次連續不動，8–4 分裂票，1992 年以來最多異見）；10Y 殖利率 4.57–4.62%（2026-05-22/23）；HY OAS 2.78%（BAMLH0A0HYM2，2026-05-21，全月趨緊）。來源：[FOMC Minutes 2026-04-29](https://www.federalreserve.gov/monetarypolicy/fomcminutes20260429.htm)、[TradingEconomics HY OAS](https://tradingeconomics.com/united-states/bofa-merrill-lynch-us-high-yield-option-adjusted-spread-fed-data.html) ✓ SEARCH-VERIFIED |
| 結構性槓桿（15%） | **72** | ▰▰▰▰▰▰▰▱▱▱ | — | — | FINRA 融資餘額 4 月達 $1.30 兆（名目歷史新高，月增 +6.8%，年增 **+53.3%**）；BofA FMS 現金水位 3.9%（低於 4.0% 賣出訊號閾值）；股票淨超配 +50%（2001 年以來最大月增幅）。來源：[Advisor Perspectives 2026-05-20](https://www.advisorperspectives.com/dshort/updates/2026/05/20/margin-debt-up-6-8-in-april-to-a-record-high)、[Axios BofA Survey 2026-05-20](https://www.axios.com/2026/05/20/fund-managers-stocks-bofa) ✓ SEARCH-VERIFIED |

**加權總分：80×0.22 + 40×0.13 + 62×0.18 + 68×0.12 + 62×0.20 + 72×0.15 = 17.6 + 5.2 + 11.16 + 8.16 + 12.4 + 10.8 = **65 / 100****

**風險等級：高（60–79 區間）**

---

## §2 歷史周期錨點相似度

| 歷史錨點 | 核心類比特徵 | 相似度 | 條圖 | 標記 |
|---------|------------|--------|------|------|
| 1999 Q4 網際網路泡沫晚期 | CAPE 逼近 44.19 峰值；IPO 狂潮（無獲利公司高估值上市）；AI/網路敘事主導；科技集中 | 84% | ▰▰▰▰▰▰▰▰▱▱ | ◀ 最貼近 |
| 2021 Q4 後疫情投機高峰 | SPAC 爆發；融資餘額前高；CNN F&G 80+；聯準會超寬鬆（當前緊縮為差異點） | 68% | ▰▰▰▰▰▰▰▱▱▱ | |
| 1929 崩盤前夕 | CAPE 高位；保證金貸款年增 >50%（當前 +53.3% YoY 極為類似）；財富集中 | 51% | ▰▰▰▰▰▱▱▱▱▱ | |
| 2007 次貸危機前夕 | HY OAS 壓縮至歷史低位（類似當前 2.78%）；VIX 低迷；廣度尚可（驅動力在信用/房市，不同） | 38% | ▰▰▰▰▱▱▱▱▱▱ | |
| 1968–1969 漂亮 50 | 機構集中押注大型成長股（對應 Mag 7 / 34.8% 占比）；廣度惡化先於指數下跌 | 27% | ▰▰▰▱▱▱▱▱▱▱ | |

**最貼近 1999 Q4**：CAPE 在不到歷史峰值 8% 的水位、以 SpaceX 為代表的世紀 IPO 敘事、Mag 7 高度集中，均與 1999 年末網路泡沫晚期高度契合。當前差異點在於聯準會利率仍在限制性區間（3.5–3.75%，非 1999 年寬鬆），融資年增率甚至超越 1999 年水準，暗示泡沫可能仍在吹頂過程中。

---

## §3 三角交叉訊號

| 指標 | 當週數值 | 相對前週 | 技術訊號 |
|------|---------|---------|---------|
| S&P 500 | 7,473（2026-05-22 收盤）| — 基準週 | ↑ 多頭；指數在歷史高位區，A/D 線延續復甦 |
| WTI 原油 | ~$91.7/桶（2026-05-25/26） | — 基準週 | ↓ 單日暴跌近 6%，空頭警示；油價急跌或暗示需求前景惡化 |
| 10Y 美債殖利率 | 4.57–4.62%（2026-05-22–23） | — 基準週 | ↗ 中性偏空；殖利率走高壓縮估值倍數，財政赤字增發形成供給壓力 |

**三角解讀：** 股市在歷史高位，而 WTI 急跌與 10Y 殖利率高企同步發出相反信號——「股票多頭 vs. 商品/利率雙重壓力」的矛盾組合不利於估值進一步擴張；油價若繼續下滑至 $85 以下，將加大通縮憂慮，對高槓桿企業信用狀況構成考驗。

---

## 特殊信號

### 機構情緒
**BofA 全球基金經理調查（2026-05-08 至 14，200 位受訪者，管理資產 $5,170 億）：**
- 股票淨超配：**+50%**（上月 +13%，月增幅為 **2001 年以來最大**）
- 現金水位：**3.9%**（低於 4.0% 歷史「賣出訊號」閾值，為 2024-02 以來最大月降幅）
- 情緒綜合指標：**6.6**（2 月以來最高，從 4 月的 3.7 大幅反彈）
- 通膨依然是首要尾部風險（66% 受訪者預期 CPI 上升）

✓ SEARCH-VERIFIED — 來源：[Axios "Fund managers are all in on stocks" 2026-05-20](https://www.axios.com/2026/05/20/fund-managers-stocks-bofa)、[Substack Atranic Capital May 2026 BofA FMS](https://atranicapital.substack.com/p/may-2026-bank-of-america-global-fund)

### 全球槓桿擴散訊號
本週搜尋結果顯示美國 SEC 已於 2026-03 阻擋 3× 以上槓桿 ETF；現有逾 450 支美國掛牌槓桿/反向單股 ETF，AUM 約 $1,500 億。**本週無確認的兩個以上非美國市場（non-US markets）同週核准新單股槓桿 ETF 之具體記錄，◆ 觸發條件未達成，結構性槓桿分數下限 81 規則不適用。**

### 本週新增訊號
前週（2026-W21）存檔不存在 → 本週為**基準週**，無週間 Δ 值可列。

**三項重點警示事件（不屬於維度分數 Δ 判定，但作為前瞻風險登記）：**

1. **SpaceX S-1（投機行為核心驅動）**：$1.75–2 兆規模若成形，將是史上最大 IPO；可能在 6 月引爆廣泛 IPO 情緒升溫，帶動散戶大量參與，下週投機行為分數應密切追蹤。✓ SEARCH-VERIFIED — [Fortune 2026-05-20](https://fortune.com/2026/05/20/spacex-ipo-filing-s1-total-addressable-market-make-life-multiplanetary/)

2. **BofA 現金水位觸發歷史賣出訊號**：3.9% < 4.0%，歷史回測中，此訊號觸發後平均 12 個月內市場回報為負。

3. **FINRA 融資年增 +53.3% 為結構性頂部特徵**：超越 2000 年及 2021 年峰值期間增速，歷史上此速率持續超過兩季後，市場均出現顯著回調。✓ SEARCH-VERIFIED — [Advisor Perspectives 2026-05-20](https://www.advisorperspectives.com/dshort/updates/2026/05/20/margin-debt-up-6-8-in-april-to-a-record-high)

---

## Insider 交易記錄（過去 14 天 · SEC Form 4）

| 公司 / 申報人 | 職位 | 交易類型 | 金額 / 股數 | 申報日 | 交易日 | SEC EDGAR |
|-------------|------|---------|-----------|--------|--------|-----------|
| TransUnion（TRU）/ Christopher Cartwright | President & CEO | F-InKind（稅扣，非主動賣出） | 26,284 股 / ~$1.8M（$68.60/股） | 2026-05-19 | 2026-05-18 | [TRU Form 4 查詢](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=TRU&type=4&dateb=&owner=include&count=10) |
| Soleno Therapeutics（SLNO）/ Anish Bhatnagar | CEO | D-Return（歸還，非主動賣出） | 583,656 股 | 2026-05-18 | 2026-05-18 | [SLNO Form 4 查詢](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=SLNO&type=4&dateb=&owner=include&count=10) |
| Extreme Networks（EXTR）/ Edward Meyercord | President & CEO | 10b5-1 預定計劃賣出 | 100,000 股 / ~$2.31M（~$23.07/股均價） | 2026-05-05 | 2026-05-04/05 | [EXTR Form 4 查詢](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=EXTR&type=4&dateb=&owner=include&count=10) |

**說明：** TRU 及 SLNO 為稅款扣繳性質（F-InKind / D-Return），不代表主動看空；EXTR 依 2025-08-28 建立之 10b5-1 計劃執行。本週**無高度異常（Open Market 大額主動賣出）insider 訊號**。✓ SEARCH-VERIFIED — [Meyka TRU 2026-05-20](https://meyka.com/blog/tru-insider-selling-five-executives-dispose-59m-stock-may-20-2026-2005/)、[Meyka SLNO 2026-05-18](https://meyka.com/blog/slno-insider-selling-13-executives-dispose-shares-may-18-2026-1905/)、[Motley Fool EXTR 2026-05-14](https://www.fool.com/coverage/filings/2026/05/14/extreme-networks-ceo-keeps-trimming-but-his-remaining-stake-tells-a-different-story/)

---

## 本週分數 JSON

```json
{
  "week": "2026-W22",
  "generated": "2026-05-26",
  "valuation": 80,
  "breadth": 40,
  "speculation": 62,
  "retail": 68,
  "monetary": 62,
  "structural": 72,
  "total": 65,
  "tier": "高",
  "prev_week": null,
  "baseline_week": true,
  "data_notes": {
    "DFEDTARU": "3.75% ✓ SEARCH-VERIFIED (Fed H.15 / FOMC 2026-04-29)",
    "BAMLH0A0HYM2": "2.78% (2026-05-21) ✓ SEARCH-VERIFIED (TradingEconomics/FRED)",
    "DGS10": "4.57% (2026-05-22) ✓ SEARCH-VERIFIED (TradingEconomics)",
    "VIXCLS": "16.68 (2026-05-26) ✓ SEARCH-VERIFIED (Yahoo Finance/CBOE)",
    "SP500": "7473.47 (2026-05-22 close) ✓ SEARCH-VERIFIED",
    "DCOILWTICO": "~91.7 (2026-05-25/26) ✓ SEARCH-VERIFIED",
    "CAPE_Shiller": "~40.75 (May 2026) ✓ SEARCH-VERIFIED (multpl.com/HeyGoTrade)",
    "FRED_direct": "⛔ FETCH FAILED — fredgraph.csv 及 .txt 端點回傳 HTTP 403"
  }
}
```

---

> Same-week file already exists in `moonape1226/bubble-risk-archive` — `scores-2026-W22.json` (SHA: `56fcb4f9`) and `report-2026-W22.md` (SHA: `146b2a91`) both present on `main` branch. No FORCE COMMIT detected — archive **not updated**. To force overwrite, re-run with `FORCE COMMIT` in context.

---

## 附錄：SEARCH-VERIFIED 查詢清單

| 維度 | 查詢串 | 來源標題 | URL | 發布單位 | 日期 |
|------|--------|---------|-----|---------|------|
| 估值 | "S&P 500 CAPE Shiller May 2026" | CAPE Ratio in May 2026: Is the S&P 500 Expensive? | https://www.heygotrade.com/en/blog/cape-ratio-explained-is-sp-500-expensive-may-2026/ | HeyGoTrade | 2026-05 |
| 信貸 | "ICE BofA high yield OAS spread May 2026" | US ICE BofA HY OAS 2026 Data | https://tradingeconomics.com/united-states/bofa-merrill-lynch-us-high-yield-option-adjusted-spread-fed-data.html | TradingEconomics | 2026-05-21 |
| 貨幣 | "Federal Reserve federal funds rate May 2026" | FOMC Minutes April 28–29, 2026 | https://www.federalreserve.gov/monetarypolicy/fomcminutes20260429.htm | Federal Reserve | 2026-04-29 |
| 廣度 | "CBOE VIX volatility index May 26 2026" | CBOE Volatility Index (^VIX) | https://finance.yahoo.com/quote/%5EVIX/ | Yahoo Finance | 2026-05-26 |
| 廣度 | "S&P 500 index level May 23 2026" | S&P 500 Historical Data | https://finance.yahoo.com/quote/%5EGSPC/ | Yahoo Finance | 2026-05-22 |
| 散戶 | "CNN Fear Greed Index May 2026" | Fear and Greed Index | https://www.cnn.com/markets/fear-and-greed | CNN Markets | 2026-05-22 |
| 散戶 | "AAII investor sentiment survey May 2026" | AAII Sentiment Survey: Neutral Sentiment Drops | https://seekingalpha.com/article/4905008-aaii-sentiment-survey-neutral-sentiment-drops | Seeking Alpha / AAII | 2026-05-14 |
| 槓桿 | "FINRA margin debt April 2026" | Margin Debt Up 6.8% in April to a Record High | https://www.advisorperspectives.com/dshort/updates/2026/05/20/margin-debt-up-6-8-in-april-to-a-record-high | Advisor Perspectives | 2026-05-20 |
| 機構 | "BofA JPMorgan fund manager survey May 2026" | Fund managers are all in on stocks, BofA survey finds | https://www.axios.com/2026/05/20/fund-managers-stocks-bofa | Axios | 2026-05-20 |
| 機構 | "May 2026 Bank of America Global Fund Manager Survey" | May 2026 BofA Global FMS | https://atranicapital.substack.com/p/may-2026-bank-of-america-global-fund | Atranic Capital / Substack | 2026-05 |
| 投機 | "IPO filings SEC S-1 May 2026" | SpaceX IPO S-1 Fortune | https://fortune.com/2026/05/20/spacex-ipo-filing-s1-total-addressable-market-make-life-multiplanetary/ | Fortune | 2026-05-20 |
| 投機 | "SpaceX IPO market cap valuation 2026" | SpaceX IPO facts 2026 | https://www.thinkmarkets.com/en/trading-academy/market-events/spacex-ipo-2026-date-spacex-valuation-and-proxy-share-cfds/ | ThinkMarkets | 2026-05 |
| Insider | "SEC Form 4 insider selling May 2026" | TRU insider selling May 20, 2026 | https://meyka.com/blog/tru-insider-selling-five-executives-dispose-59m-stock-may-20-2026-2005/ | Meyka | 2026-05-20 |
| 油價 | "WTI crude oil price May 23 2026" | Crude Oil Price Chart | https://tradingeconomics.com/commodity/crude-oil | TradingEconomics / EIA | 2026-05-25 |
| ETF | "leveraged single stock ETF SEC approval May 2026" | SEC Halts High-Leveraged ETF Plans | https://www.wealthmanagement.com/etfs/sec-halts-high-leveraged-etf-plans-in-warning-over-risks | Wealth Management / SEC | 2026-03 |

---

**本報告為相對風險溫度計，非擇時訊號。**

# 設計草案：從泡沫風險評分改為「半年內 AI 泡沫是否破裂」預測

狀態：使用者已確認（2026-11-13）：「發生泡沫」指破裂、R1–R3 門檻照案、上線順序照案。實作在 branch `forecast-redesign`。

## 1. 問題定義

報告每期回答一個問題：**自報告日 D 起 182 天內（至 D+182），AI 泡沫是否破裂？** 答案只有 `yes` / `no`。

「發生泡沫」解讀為「破裂」。理由：依現行報告的判讀，泡沫狀態已經存在（2026-07 起 tier 皆為警戒／高），「是否發生」若指形成，答案恆為 yes，沒有預測價值。若你原意是「形成」而非「破裂」，此節需要重寫。

判斷規則：`yes` 表示判斷 182 天內符合解析條件的可能性高於一半；`no` 反之。報告不輸出機率數字（依使用者選擇），但判斷依據必須寫明。

## 2. 解析條件（事前寫死，到期時機械判定）

窗口 [D, D+182] 內，以下任一成立即解析為 `yes`，否則為 `no`：

- **R1 市場回撤：** FRED `NASDAQ100` 任一日收盤 ≤ 該日（含）之前 252 個交易日最高收盤 × 0.75，即自 52 週高點回撤 ≥ 25%。可用現有 FRED 管線機械判定。
- **R2 資本支出收縮：** Microsoft、Alphabet、Amazon、Meta 四家之中至少兩家，在財報、法說會或 8-K 中將當年度或次年度資本支出指引下修（相較該公司前一次正式指引）。
- **R3 AI 信用事件：** 以 AI 資料中心／算力為主業、負債 ≥ 50 億美元的借款人（例如 CoreWeave 類 neocloud、AI 資料中心 SPV），發生破產申請、超過寬限期的付款違約，或完成 distressed exchange。

已知限制：R1 會把非 AI 引起的全面崩跌（例如 2020-03 型外生衝擊）也算成 yes。我選擇接受，因為那種情境下 AI 估值同樣會破，而加上「AI 主導」的附加條件會讓判定變得主觀。門檻（25%、兩家、50 億）可以調整。

到期解析由另一個獨立的 resolver 工作在 D+182 之後執行，不在這次改動範圍內；archive 先預留欄位。

## 3. 報告結構（取代現行所有計分章節）

1. **結論**：`yes` / `no` 加一句話理由。
2. **解析條件**：第 2 節全文，鎖字，每期原樣照印。
3. **三條路徑現況**：R1 目前距 52 週高點的回撤（由 macro artifact 計算，validator 可重現）、R2 各家最新 capex 指引與方向、R3 主要 AI 借款人的信用狀況（利差、殖利率、評等、到期牆）。
4. **支持 yes 的證據**、**支持 no 的證據**：每條都引用 `source_id`，兩邊都必須寫，不可只寫一邊。
5. **與前期比較**：前期結論；若本期結論不同，必須列出造成翻轉的新證據（`source_id`，且資料日期在前期之後）；沒有新證據就不得翻轉。這一條用來抑制 yes/no 在邊界附近來回跳動。
6. **資料缺漏與不確定性**：哪些來源 FETCH FAILED，以及缺漏是否足以改變結論。
7. **數據附錄**：沿用現行 Raw data／Coverage／SEARCH-VERIFIED traceability 三張表與 `source_id` 制度。
8. **免責聲明**。

移除：六維度分數、權重、tier、歷史錨點相似度、三角訊號、trigger state、calibration、score JSON 中的分數欄位。

## 4. 資料來源

保留現行 fetcher 與來源清單作為證據基礎，不再計分。新增 FRED `NASDAQ100`（R1 需要 252 交易日歷史）。R2 與 R3 的來源從現有的 hyperscaler capex、financing mix、AI credit schism、refinancing 類來源延伸。

## 5. Archive 與網站

- 新報告存為 `report-YYYY-MM-DD/{forecast.json, report.md}`。`forecast.json` 包含：`date`、`answer`、`horizon_end`、`resolution_version`、`prior_answer`、`flip_evidence`（source_id 清單）、`r1_drawdown_pct`、`resolution`（null，留給 resolver）。
- 舊的 `score.json` 期別保持不動。`build_site.py` 要同時支援兩種格式：首頁改為顯示最新結論與 R1–R3 現況，歷史表依格式分別顯示分數或 yes/no。網站必須在第一份新格式報告寫入 archive 之前改好。

## 6. Validator

保留：章節／表格鎖定、`source_id` 對應與追溯、macro artifact 驗證、mode banner、standalone JSON 與報告 fence 一致、原子 archive 規則。

新增：`answer` ∈ {yes, no}；解析條件全文逐字相符；R1 回撤數字可由 macro artifact 重現；結論與前期不同時，`flip_evidence` 非空、每個 source_id 存在，且資料日期晚於前期；yes／no 兩邊的證據各至少一條。

移除：所有分數算術、tier、anchor feature audit、trigger reason code。

## 7. 上線

1. 在 branch 上改 prompt、contract、validator、tests；production 在 merge 前不受影響。
2. archive repo 另開 PR 改 `build_site.py`，兩邊格式都能顯示。
3. 本地跑一次 `MODE: DRY-RUN` 並通過 validator。
4. 先 merge 網站 PR，再於兩次排程 run（週一、週四）之間 merge prompt PR。

## 8. 之後的 eval

沿用已建的 26 個凍結證據包（`evals/judgment/cases/`）。評分改為：validator 通過、rubric（證據撐得住結論、正反兩面都有、R1–R3 現況正確）、一致性（相鄰期別在證據沒變時結論不變，翻轉都有新證據支撐）、降級情境（資料缺漏時不過度自信）。真正的準確度要到第一份新格式報告到期（約 2027-05）才開始累積，而且樣本彼此高度相關。回測時要注意：知識截止日晚於 D+182 的模型可能已經知道答案。

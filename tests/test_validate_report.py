"""Golden-fixture tests for scripts/validate_report.py.

Each test builds a minimal report that satisfies every lock, applies one
mutation, and asserts the validator's exit code. stdlib only.
"""
import subprocess, sys, tempfile, unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VALIDATOR = REPO / "scripts" / "validate_report.py"

SCORE_JSON = """{
  "date": "2026-07-13", "iso_week": "2026-W29", "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "valuation": 50, "breadth": 40, "speculation": 40,
  "retail": 40, "monetary": 40, "structural": 40,
  "total": 42, "tier": "警戒", "regime": "穩定共存"
}"""

VALID = """# 2026-07-13 市場泡沫風險評估報告
> 報告日期：2026-07-13；執行日：2026-07-13 Asia/Taipei；ISO 週次：2026-W29；前次基準：report-2026-07-09（4天前）

**總評**：總分 42【警戒】（Δ +1）；扳機狀態：未擊發；最貼近錨點：1997 早期建設（50%）。

## §1 六維度風險條圖

| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---|---|---|
| 估值溢價 | ▰▰▰▰▰▱▱▱▱▱ | 50 | 49 | +1 |
| 市場廣度 | ▰▰▰▰▱▱▱▱▱▱ | 40 | 40 | 0 |
| 投機行為 | ▰▰▰▰▱▱▱▱▱▱ | 40 | 40 | 0 |
| 散戶情緒 | ▰▰▰▰▱▱▱▱▱▱ | 40 | 40 | 0 |
| 貨幣與信貸環境 | ▰▰▰▰▱▱▱▱▱▱ | 40 | 40 | 0 |
| 結構性槓桿 | ▰▰▰▰▱▱▱▱▱▱ | 40 | 40 | 0 |
| **加權總分** | ▰▰▰▰▱▱▱▱▱▱ | **42【警戒】** | 41 | +1 |

## §2 歷史錨點相似度

| 錨點 | 相似度 | 條圖 | 標記 |
|---|---|---|---|
| 1997 早期建設 | 50% | ▰▰▰▰▰▱▱▱▱▱ | ◀ 最貼近 |
| 1998 LTCM 衝擊 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 30% | ▰▰▰▱▱▱▱▱▱▱ |  |
| 2000/3 頂點 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 50% | ▰▰▰▰▰▱▱▱▱▱ |  |

## §3 三角訊號

| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,575.39 | ▲ +0.42%（前次 ≈7,543.64） |
| WTI 原油 | $69.6 /bbl | 持平（前次 ≈$69.6） |
| 10Y Treasury | 4.54% | 持平（前次 4.54%） |

**三者狀態**：穩定共存
**格局轉變**：無。
**10Y 成因拆解**：ΔDFII10 0 bps、ΔT10YIE 0 bps、判定 none。
**扳機鏈**：無新事證。
**結論**：扳機狀態：未擊發——測試基準。

## 六維度評分

內文。

## 綜合分數

42【警戒】

## 歷史泡沫週期對比

相似度計算：checklist v2

## 機構情緒對照

本次無新機構調查數據。

## 本次新增訊號

無。

## 數據附錄

| 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|
| D1 / S&P 500 | FRED | ✓ API |
| D5 / HY OAS | FRED | ✓ API |
| D6 / CFTC | CFTC | ✓ DIRECT |

## 本次分數存檔

```json
{SCORE}
```

本報告為相對風險溫度計，非擇時訊號。
""".replace("{SCORE}", SCORE_JSON)

MINI_PROMPT = """# Intro

text

# Data sources (fetch fresh data each run)

- bullet one
- bullet two
  - indented sub-bullet, not counted
- bullet three

```
- fenced, not counted
```

# Next section

- not under Data sources, not counted
"""


def run_validator(report_text, *extra_args):
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                     encoding="utf-8") as f:
        f.write(report_text)
        path = f.name
    proc = subprocess.run([sys.executable, str(VALIDATOR), path, *extra_args],
                          capture_output=True, text=True)
    return proc.returncode, proc.stdout


class ValidReport(unittest.TestCase):
    def test_valid_passes(self):
        code, out = run_validator(VALID)
        self.assertEqual(code, 0, out)


class ScoreJsonFailClosed(unittest.TestCase):
    def test_null_score_fails(self):
        code, out = run_validator(VALID.replace(SCORE_JSON, "null"))
        self.assertEqual(code, 1, out)

    def test_empty_object_score_fails(self):
        code, out = run_validator(VALID.replace(SCORE_JSON, "{}"))
        self.assertEqual(code, 1, out)

    def test_array_score_fails(self):
        code, out = run_validator(VALID.replace(SCORE_JSON, "[]"))
        self.assertEqual(code, 1, out)

    def test_wrong_total_still_fails(self):
        code, out = run_validator(VALID.replace('"total": 42', '"total": 55'))
        self.assertEqual(code, 1, out)


class S2AnchorLock(unittest.TestCase):
    def test_renamed_anchor_fails(self):
        code, out = run_validator(VALID.replace("1998 LTCM 衝擊", "1998 危機"))
        self.assertEqual(code, 1, out)

    def test_missing_anchor_fails(self):
        code, out = run_validator(
            VALID.replace("| 2000/3 頂點 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |\n", ""))
        self.assertEqual(code, 1, out)


class S3Checks(unittest.TestCase):
    def test_empty_s3_table_fails(self):
        mutated = VALID
        for row in ("| S&P 500 | 7,575.39 | ▲ +0.42%（前次 ≈7,543.64） |\n",
                    "| WTI 原油 | $69.6 /bbl | 持平（前次 ≈$69.6） |\n",
                    "| 10Y Treasury | 4.54% | 持平（前次 4.54%） |\n"):
            mutated = mutated.replace(row, "")
        code, out = run_validator(mutated)
        self.assertEqual(code, 1, out)

    def test_wrong_indicator_name_fails(self):
        code, out = run_validator(VALID.replace("| WTI 原油 |", "| 布蘭特原油 |"))
        self.assertEqual(code, 1, out)

    def test_missing_conclusion_line_fails(self):
        code, out = run_validator(
            VALID.replace("**結論**：扳機狀態：未擊發——測試基準。\n", ""))
        self.assertEqual(code, 1, out)


class ZongpingCrossChecks(unittest.TestCase):
    def test_delta_mismatch_fails(self):
        # 總評 says Δ +3 but §1 加權總分 row says +1
        code, out = run_validator(VALID.replace("（Δ +1）", "（Δ +3）"))
        self.assertEqual(code, 1, out)

    def test_trigger_state_mismatch_fails(self):
        # 總評 says 已擊發 but §3 結論 says 未擊發
        code, out = run_validator(
            VALID.replace("**總評**：總分 42【警戒】（Δ +1）；扳機狀態：未擊發",
                          "**總評**：總分 42【警戒】（Δ +1）；扳機狀態：已擊發"))
        self.assertEqual(code, 1, out)

    def test_bold_warning_conclusion_accepted(self):
        # real-report style: **結論**：⚠ **扳機狀態：已擊發**——...
        mutated = VALID.replace(
            "**結論**：扳機狀態：未擊發——測試基準。",
            "**結論**：⚠ **扳機狀態：已擊發**——測試基準。").replace(
            "**總評**：總分 42【警戒】（Δ +1）；扳機狀態：未擊發",
            "**總評**：總分 42【警戒】（Δ +1）；扳機狀態：已擊發")
        code, out = run_validator(mutated)
        self.assertEqual(code, 0, out)


class CoverageGate(unittest.TestCase):
    def test_coverage_rows_flag_still_works(self):
        code, out = run_validator(VALID, "--coverage-rows", "5")
        self.assertEqual(code, 1, out)

    def test_prompt_flag_count_match_passes(self):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                         encoding="utf-8") as f:
            f.write(MINI_PROMPT + "- extra bullet\n")  # appended after Next section: not counted
            prompt_path = f.name
        # mini prompt has 3 countable bullets, report has 3 rows -> pass
        code, out = run_validator(VALID, "--prompt", prompt_path)
        self.assertEqual(code, 0, out)

    def test_prompt_flag_mismatch_fails(self):
        mutated = VALID.replace("| D6 / CFTC | CFTC | ✓ DIRECT |\n", "")
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                         encoding="utf-8") as f:
            f.write(MINI_PROMPT)
            prompt_path = f.name
        code, out = run_validator(mutated, "--prompt", prompt_path)  # 2 rows vs 3 bullets
        self.assertEqual(code, 1, out)


if __name__ == "__main__":
    unittest.main()

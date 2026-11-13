"""End-to-end contract tests for ``scripts/validate_report.py``.

The golden report is a complete synthetic forecast report (conclusion,
resolution block, three path sections, evidence sections, comparison, gaps,
appendix, forecast JSON).  Negative tests mutate one invariant at a time and
assert the specific failure.  stdlib only; no network and no wall clock.
"""

import contextlib
import copy
import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date, timedelta
from unittest import mock
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
VALIDATOR = REPO / "scripts" / "validate_report.py"
PROMPT = REPO / "bubble-risk-weekly-prompt.md"
CONTRACT_PATH = REPO / "report_contract.json"
CONTRACT = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))

DATE = "2026-07-13"
PRIOR_DATE = "2026-07-09"
HORIZON_END = (date.fromisoformat(DATE) + timedelta(
    days=CONTRACT["question"]["horizon_days"])).isoformat()
PRIOR_HORIZON_END = (date.fromisoformat(PRIOR_DATE) + timedelta(
    days=CONTRACT["question"]["horizon_days"])).isoformat()
# 8 days before the 07-10 macro observation date: inside the trailing window
COMOVE_BASE_DATE = "2026-07-02"
TIMESTAMP = "2026-07-13T08:00:00+08:00"
SEARCH_ID = "speculation.ai_rename_spac"
NDX_ID = "valuation.ndx_drawdown"
# Optional sources promoted to successful DIRECT evidence in the golden so the
# R3 path can cite a successful source.
DIRECT_OPTIONAL = {"valuation.ai_credit_schism"}
NDX_LATEST, NDX_HIGH, NDX_DRAWDOWN = 19950.0, 21000.0, 5.0
RESOLUTION_BLOCK = CONTRACT["resolution"]["block"]
DRY_BANNER = "> [DRY RUN] this report was not committed to archive."


def load_validator_module():
    spec = importlib.util.spec_from_file_location(
        "validate_report_under_test", VALIDATOR
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def weekdays_descending(end, count):
    days, day = [], date.fromisoformat(end)
    while len(days) < count:
        if day.weekday() < 5:
            days.append(day.isoformat())
        day -= timedelta(days=1)
    return days


def ndx_drawdown_block():
    lookback = CONTRACT["macro_schema"]["ndx_drawdown"]["lookback_trading_days"]
    days = weekdays_descending("2026-07-10", lookback)
    window = []
    for index, day in enumerate(days):
        if index == 0:
            value = NDX_LATEST
        elif index == 100:
            value = NDX_HIGH
        else:
            value = 19000.0 + (index % 7) * 10
        window.append({"date": day, "value": value})
    return {
        "status": "ok", "source": "FRED API", "series": "NASDAQ100",
        "latest_date": days[0], "latest": NDX_LATEST,
        "high_date": days[100], "high": NDX_HIGH,
        "drawdown_pct": NDX_DRAWDOWN,
        "r1_threshold_pct": CONTRACT["resolution"]["r1"]["drawdown_pct"],
        "r1_threshold_level": 15750.0, "r1_met": False,
        "window_observations": window,
    }


def macro_payload(baseline=False):
    levels = {
        "DGS10": 4.54, "DFII10": 2.20, "T10YIE": 2.34,
        "BAMLH0A0HYM2": 2.80, "BAMLC0A0CM": 0.85,
        "DFEDTARU": 4.50, "DFEDTARL": 4.25, "WALCL": 6800000.0,
        "DCOILWTICO": 69.60, "ECBASSETSW": 7000000.0,
        "JPNASSETS": 7500000.0, "BOGZ1FL153064486Q": 43.0,
        "T5YIFR": 2.20, "CPIAUCSL": 320.0, "THREEFYTP10": 0.65,
        "SOFR": 4.30, "SOFR99": 4.35, "IORB": 4.31,
        "RPONTTLD": 0.1, "LNFACBW027SBOG": 1200.0, "VIXCLS": 15.2,
    }
    common_series = {
        sid: {
            "status": "ok", "source": "FRED API", "latest": value,
            "latest_date": "2026-07-10",
        }
        for sid, value in levels.items()
    }
    for sid in CONTRACT["macro_schema"]["alignment_proof_series"]:
        common_series[sid]["alignment_observations"] = [{
            "date": common_series[sid]["latest_date"],
            "value": common_series[sid]["latest"],
        }]
    # VIXCLS needs a trailing base so vix_spx_comove has a shared window
    common_series["VIXCLS"]["alignment_observations"].append(
        {"date": COMOVE_BASE_DATE, "value": 15.2}
    )
    common_series["CPIAUCSL"].update({
        "yoy_base_date": "2025-07-10",
        "yoy_base": 310.6796116504854,
        "yoy_pct": 3.0,
    })
    payload = {
        "contract_version": CONTRACT["version"],
        "macro_schema_version": CONTRACT["macro_schema"]["version"],
        "generated_at": TIMESTAMP,
        "prior_run_date": "none" if baseline else PRIOR_DATE,
        "fred_key_present": True,
        "eia_key_present": False,
        "series": common_series,
        "sp500_trend": {
            "status": "ok", "source": "FRED API",
            "latest": 7575.39,
            "latest_date": "2026-07-10",
            "ma200": 6763.74,
            "dev200_pct": 12.0,
            "alignment_observations": [
                {"date": "2026-07-10", "value": 7575.39},
                {"date": COMOVE_BASE_DATE, "value": 7543.64},
            ],
        },
        "vix_spx_comove": {
            "status": "ok",
            "as_of": "2026-07-10",
            "base_date": COMOVE_BASE_DATE,
            "window_days": 8,
            "vix": 15.2,
            "vix_base": 15.2,
            "vix_chg_pct": 0.0,
            "sp500": 7575.39,
            "sp500_base": 7543.64,
            "sp500_chg_pct": 0.42,
            "comove": False,
            "note": "trailing window; thresholds not met",
        },
        "ndx_drawdown": ndx_drawdown_block(),
        "cftc_lev_funds": {
            "status": "ok", "source": "CFTC", "latest_date": "2026-07-10",
            "net_contracts": -500000,
        },
        "move_index": {
            "status": "ok", "source": "Yahoo", "latest_date": "2026-07-10",
            "latest": 95.0,
        },
        "ofr_repo": {
            "status": "ok", "source": "OFR", "latest_date": "2026-07-10",
            "transaction_volume_usd_bn": 700.0,
        },
        "repo_stress": {
            "status": "ok", "as_of": "2026-07-10", "sofr": 4.30,
            "iorb": 4.31, "iorb_date": "2026-07-10",
            "sofr_iorb_bps": -1.0,
            "srf_usage_bn": 0.1, "srf_date": "2026-07-10",
        },
    }
    if baseline:
        payload["decomposition"] = {
            "status": "baseline_no_prior",
            "driver": "baseline",
            "freshness": "not_applicable",
            "stale_series": [],
            "d_dgs10_bps": None,
            "d_dfii10_bps": None,
            "d_t10yie_bps": None,
        }
    else:
        payload["sp500_trend"].update({
            "prior_spot": 7543.64,
            "prior_spot_date": PRIOR_DATE,
            "chg_pct": 0.42,
        })
        prior_levels = {
            **levels,
        }
        for sid, value in prior_levels.items():
            common_series[sid].update({"prior": value, "prior_date": PRIOR_DATE})
        common_series["THREEFYTP10"].update({
            "prior_date": "2026-07-03",
            "delta_note": (
                "trailing ~7d within the series' own timeline "
                "(publication lag; not aligned to prior-run date)"
            ),
        })
        for sid in levels:
            common_series[sid]["delta_abs"] = 0.0
            if sid not in ("CPIAUCSL", "BOGZ1FL153064486Q"):
                if sid in ("DCOILWTICO", "RPONTTLD", "LNFACBW027SBOG"):
                    common_series[sid]["chg_pct"] = 0.0
                elif sid not in ("WALCL", "ECBASSETSW", "JPNASSETS", "VIXCLS"):
                    common_series[sid]["delta_bps"] = 0.0
        payload["move_index"].update({
            "prior": 95.0, "prior_date": PRIOR_DATE, "delta_abs": 0.0,
        })
        payload["decomposition"] = {
            "status": "ok",
            "d_dgs10_bps": 0.0,
            "d_dfii10_bps": 0.0,
            "d_t10yie_bps": 0.0,
            "driver": "none",
            "freshness": "updated",
            "stale_series": [],
        }
    return payload


def forecast_payload(mode="forecast", answer="no", **overrides):
    """Current forecast.  mode: forecast prior | legacy prior | baseline."""
    flip = mode == "forecast" and answer != "no"
    payload = {
        "date": DATE,
        "iso_week": "2026-W29",
        "weekday": "Monday",
        "timezone": "Asia/Taipei",
        "question_version": CONTRACT["question"]["version"],
        "resolution_version": CONTRACT["resolution"]["version"],
        "answer": answer,
        "horizon_end": HORIZON_END,
        "prior_date": None if mode == "baseline" else PRIOR_DATE,
        "prior_answer": "no" if mode == "forecast" else None,
        "flip_evidence": ["ai.hyperscaler_capex"] if flip else [],
        "r1_drawdown_pct": NDX_DRAWDOWN,
        "resolution": None,
    }
    payload.update(overrides)
    return payload


def prior_forecast_payload(answer="no", **overrides):
    payload = {
        "date": PRIOR_DATE,
        "iso_week": "2026-W28",
        "weekday": "Thursday",
        "timezone": "Asia/Taipei",
        "question_version": CONTRACT["question"]["version"],
        "resolution_version": CONTRACT["resolution"]["version"],
        "answer": answer,
        "horizon_end": PRIOR_HORIZON_END,
        "prior_date": None,
        "prior_answer": None,
        "flip_evidence": [],
        "r1_drawdown_pct": 4.5,
        "resolution": None,
    }
    payload.update(overrides)
    return payload


def markdown_table(header, rows):
    columns = len(header.strip().strip("|").split("|"))
    separator = "|" + "|".join(["---"] * columns) + "|"
    return "\n".join([header, separator, *rows])


def coverage_block(ndx_failed=False):
    rows = []
    for source in CONTRACT["sources"]:
        if source["id"] == SEARCH_ID:
            status = "✓ SEARCH-VERIFIED"
        elif ndx_failed and source["id"] == NDX_ID:
            status = "⛔ FETCH FAILED"
        elif source.get("macro"):
            status = "✓ API"
        elif source.get("window") == "composite":
            status = (
                "✗ NOT DISCLOSED components="
                "quarterly_state:not_disclosed,event_scan:not_disclosed"
            )
        elif not source["required"] and source["id"] not in DIRECT_OPTIONAL:
            status = "✗ NOT DISCLOSED"
        else:
            status = "✓ DIRECT"
        rows.append(
            f"| {source['id']} | {source['prompt_match']} | contract method | {status} |"
        )
    return markdown_table(CONTRACT["coverage_header"], rows)


def ndx_raw_rows():
    return [
        f"| {NDX_ID} | ndx_drawdown latest 收盤 | {NDX_LATEST:.2f} | "
        f"FRED NASDAQ100 (ndx_drawdown) | 2026-07-10 | {TIMESTAMP} |",
        f"| {NDX_ID} | ndx_drawdown high 252 日最高收盤 | {NDX_HIGH:.2f} | "
        f"FRED NASDAQ100 (ndx_drawdown) | {ndx_drawdown_block()['high_date']} | {TIMESTAMP} |",
        f"| {NDX_ID} | ndx_drawdown drawdown_pct | {NDX_DRAWDOWN:.2f} | "
        f"FRED NASDAQ100 (ndx_drawdown) | 2026-07-10 | {TIMESTAMP} |",
    ]


def raw_block(ndx_failed=False):
    macro = macro_payload()
    rows = []
    for source in CONTRACT["sources"]:
        source_id = source["id"]
        optional = (not source["required"] and not source.get("macro")
                    and source_id not in DIRECT_OPTIONAL)
        if source_id == SEARCH_ID or optional:
            continue
        if source_id == NDX_ID:
            if not ndx_failed:
                rows.extend(ndx_raw_rows())
            continue
        binding = source.get("macro")
        if binding:
            for component in binding["components"]:
                key = component["key"]
                block = (macro["series"][key] if component["kind"] == "series"
                         else macro[key])
                if component["kind"] == "series":
                    value = block.get(component.get("value_field", "latest"))
                    data_date = block["latest_date"]
                elif key == "vix_spx_comove":
                    value = block["vix"]
                    data_date = block["as_of"]
                else:
                    value = block.get(
                        "latest",
                        block.get(
                            "net_contracts",
                            block.get("transaction_volume_usd_bn", 1),
                        ),
                    )
                    data_date = block["latest_date"]
                rows.append(
                    f"| {source_id} | {key} | {value} | API {key} | "
                    f"{data_date} | {TIMESTAMP} |"
                )
        else:
            event_window = source["window"] in ("7d", "14d", "30d", "90d")
            data_date = "2026-07-12" if event_window else "2026-07-10"
            rows.append(
                f"| {source_id} | contract evidence | 1 | "
                f"https://example.com/{source_id} | {data_date} | {TIMESTAMP} |"
            )
    return markdown_table(CONTRACT["raw_data_header"], rows)


RAW_BLOCK = raw_block()

TRACE_ROW = (
    f"| {SEARCH_ID} | AI rename scan | AI rename SPAC past 7 days | "
    f"https://example.com/rename | 2026-07-12 | {TIMESTAMP} |"
)
TRACE_BLOCK = markdown_table(CONTRACT["traceability_header"], [TRACE_ROW])

R1_TEXT = (
    "NASDAQ-100 最新收盤 19,950.00（2026-07-10），252 個交易日收盤高點 21,000.00，"
    f"距 52 週高點回撤 {NDX_DRAWDOWN:.2f}%；R1 門檻 15,750.00。`{NDX_ID}`"
)
R1_UNAVAILABLE_TEXT = "R1 回撤不可用——腳本未取得 NASDAQ100 日序資料"


def make_report(mode="forecast", answer="no", ndx_failed=False, forecast=None):
    """Complete golden report for a prior mode and answer."""
    flip = mode == "forecast" and answer != "no"
    forecast = forecast if forecast is not None else forecast_payload(mode, answer)
    if ndx_failed and forecast.get("r1_drawdown_pct") == NDX_DRAWDOWN:
        forecast = {**forecast, "r1_drawdown_pct": None}
    prior_meta = "無（基準）" if mode == "baseline" else f"report-{PRIOR_DATE}（4天前）"
    if mode == "forecast":
        comparison = [
            f"前次結論：no（report-{PRIOR_DATE}）",
            "",
            "本次結論：翻轉" if flip else "本次結論：維持",
            "",
        ]
        if flip:
            comparison += [
                "翻轉依據：",
                "- 四大雲端業者之一下修資本支出指引，見 `ai.hyperscaler_capex`，資料日期晚於前次預測。",
            ]
        else:
            comparison += ["- 自前次預測以來無足以改變結論的新證據。"]
    elif mode == "legacy":
        comparison = [
            f"前次結論：無前次預測（report-{PRIOR_DATE} 為舊格式評分報告）",
            "",
            "- 前次為評分報告，不轉換為 yes/no。",
        ]
    else:
        comparison = ["前次結論：無前次（基準）", "", "- 基準日，無比較對象。"]
    r1 = R1_UNAVAILABLE_TEXT if ndx_failed else R1_TEXT
    gaps = (
        [f"- `{NDX_ID}` 為 FETCH FAILED，缺口不影響 R2、R3 的判斷。"]
        if ndx_failed else ["本次無 FETCH FAILED 來源"]
    )
    lines = [
        f"# {DATE} AI 泡沫破裂預測報告",
        f"報告日期：{DATE}｜ISO 週次：2026-W29｜預測窗口：{DATE} → {HORIZON_END}"
        f"｜前次基準：{prior_meta}",
        "",
        "## 結論",
        CONTRACT["conclusion_line"][answer],
        "",
        "三條路徑皆未接近解析條件，市場回撤與資本支出指引均無破裂訊號。",
        "",
        "## 解析條件",
        RESOLUTION_BLOCK,
        "",
        f"解析版本：v{CONTRACT['resolution']['version']}",
        "",
        "## 三條路徑現況",
        "",
        "### R1 市場回撤",
        r1,
        "",
        "**判讀：** 距離門檻仍遠，窗口內需再下跌約兩成才會觸發。",
        "",
        "### R2 資本支出收縮",
        "四家業者最新指引皆為上修。`ai.hyperscaler_capex`",
        "",
        "**判讀：** 尚無任何一家下修，距離至少兩家下修的條件很遠。",
        "",
        "### R3 AI 信用事件",
        "目前未見符合規模的借款人違約。`valuation.ai_credit_schism`",
        "",
        "**判讀：** 信用定價平穩，窗口內需出現違約或 distressed exchange 才會觸發。",
        "",
        "## 支持 yes 的證據",
        "",
        "- [R3] AI 信用定價出現分歧，部分借款人利差擴大。`valuation.ai_credit_schism`",
        "",
        "## 支持 no 的證據",
        "",
        f"- [R1] 距 52 週高點回撤僅 {NDX_DRAWDOWN:.2f}%。`{NDX_ID}`"
        if not ndx_failed else
        "- [R2] 四家業者資本支出指引皆未下修。`ai.hyperscaler_capex`",
        "- [整體] 資本支出指引維持上修。`ai.hyperscaler_capex`",
        "",
        "## 與前期比較",
        "",
        *comparison,
        "",
        "## 資料缺漏與不確定性",
        "",
        *gaps,
        "- 下一次財報日期尚未公布，可能使 R2 提前出現下修。",
        "",
        "## 數據附錄",
        "",
        "### Raw data",
        "",
        raw_block(ndx_failed),
        "",
        "### Coverage",
        "",
        coverage_block(ndx_failed),
        "",
        "### SEARCH-VERIFIED traceability",
        "",
        TRACE_BLOCK,
        "",
        "## 本次預測存檔",
        "",
        "```json",
        json.dumps(forecast, ensure_ascii=False, indent=2),
        "```",
        "",
        CONTRACT["disclaimer"],
        "",
    ]
    return "\n".join(lines)


def replace_once(text, old, new):
    if text.count(old) != 1:
        raise AssertionError(f"fixture mutation expected exactly one match: {old!r}")
    return text.replace(old, new, 1)


def coverage_row(source_id):
    return next(
        line for line in coverage_block().splitlines()
        if line.startswith(f"| {source_id} |")
    )


def raw_row(source_id, component=None):
    rows = [
        line for line in RAW_BLOCK.splitlines()
        if line.startswith(f"| {source_id} |")
        and (component is None or component in line)
    ]
    if len(rows) != 1:
        raise AssertionError(f"expected one raw row for {source_id}/{component}: {rows}")
    return rows[0]


def ndx_failed_macro(baseline=False):
    macro = macro_payload(baseline)
    macro["ndx_drawdown"] = {"status": "fetch_failed", "source": "FRED API"}
    return macro


def comove_unavailable_report(report=None):
    """Degrade the co-movement Coverage row and drop its derived Raw row."""
    source_id = "structural.vix_spx_comove"
    coverage = coverage_row(source_id)
    report = replace_once(
        report if report is not None else make_report(),
        coverage, coverage.replace("✓ API", "⛔ FETCH FAILED"),
    )
    report = replace_once(
        report, "本次無 FETCH FAILED 來源",
        f"- `{source_id}` 為 FETCH FAILED，缺口不影響三條路徑的判斷。")
    return replace_once(report, raw_row(source_id, "| vix_spx_comove |") + "\n", "")


def spv_event_item(omit=(), **overrides):
    marker = CONTRACT["spv_deal_marker"]
    values = {
        "sponsor_equity_split": "60/40",
        "residual_value_guarantee": "undisclosed",
        "lease_term": "15y",
        "debt_tenor": "7y",
        "lead_lenders": "Bank A, Bank B",
    }
    values.update(overrides)
    pairs = "".join(
        f"{key}={values[key]};" for key in marker["required_keys"] if key not in omit
    )
    return f"[{marker['component_id']}]{marker['tag']} SPV data-center financing deal {pairs}"


def spv_deal_marker_fixture(event_item=None):
    marker = CONTRACT["spv_deal_marker"]
    source = next(s for s in CONTRACT["sources"] if s["id"] == marker["source_id"])
    other_component = next(
        c["id"] for c in source["window_components"] if c["id"] != marker["component_id"]
    )
    quarterly_row = (
        f"| {marker['source_id']} | [{other_component}] top-5 capex vs FCF | "
        "hyperscaler quarterly financing state | "
        "https://example.com/hyperscaler-financing-quarterly | "
        f"2026-07-01 | {TIMESTAMP} |"
    )
    event_row = (
        f"| {marker['source_id']} | {event_item or spv_event_item()} | "
        "SPV financing event scan | https://example.com/hyperscaler-financing-spv | "
        f"2026-07-12 | {TIMESTAMP} |"
    )
    report = make_report()
    coverage = coverage_row(marker["source_id"])
    report = replace_once(
        report, coverage,
        coverage.replace(
            "✗ NOT DISCLOSED components="
            "quarterly_state:not_disclosed,event_scan:not_disclosed",
            "✓ SEARCH-VERIFIED components=quarterly_state:ok,event_scan:ok",
        ),
    )
    report = replace_once(
        report, TRACE_ROW, TRACE_ROW + "\n" + quarterly_row + "\n" + event_row
    )
    return report


class ValidatorCase(unittest.TestCase):
    def run_validator(
        self,
        report=None,
        *,
        mode="forecast",
        answer="no",
        baseline=False,
        macro=None,
        macro_text=None,
        current_forecast=None,
        prior_forecast=None,
        prompt_text=None,
        dry_run=False,
        macro_markers=True,
        extra_args=(),
        include_required_args=True,
        prior_flag=True,
    ):
        if baseline:
            mode = "baseline"
        generated_report = report is None
        report = make_report(mode, answer) if generated_report else report
        if dry_run and generated_report:
            report = DRY_BANNER + "\n\n" + report
        macro = macro_payload(mode == "baseline") if macro is None else macro
        if current_forecast is None:
            current_forecast = forecast_payload(mode, answer)
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            report_path = root / "report.md"
            prompt_path = root / "prompt.md"
            contract_path = root / "report_contract.json"
            macro_path = root / "macro.json"
            prior_path = root / "prior.json"
            current_path = root / "current-forecast.json"
            report_path.write_text(report, encoding="utf-8")
            prompt_path.write_text(
                PROMPT.read_text(encoding="utf-8") if prompt_text is None else prompt_text,
                encoding="utf-8",
            )
            contract_path.write_text(
                json.dumps(CONTRACT, ensure_ascii=False), encoding="utf-8"
            )
            if macro_text is None:
                macro_json = json.dumps(macro, ensure_ascii=False, indent=2)
                macro_text = (
                    "===MACRO_JSON_START===\n" + macro_json
                    + "\n===MACRO_JSON_END===\n"
                    if macro_markers else macro_json
                )
            macro_path.write_text(macro_text, encoding="utf-8")
            current_path.write_text(
                json.dumps(current_forecast, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            argv = [sys.executable, str(VALIDATOR), str(report_path)]
            if include_required_args:
                argv += [
                    "--prompt", str(prompt_path),
                    "--contract", str(contract_path),
                    "--macro-json", str(macro_path),
                    "--current-forecast", str(current_path),
                    "--dry-run" if dry_run else "--production",
                ]
                if prior_flag:
                    if mode == "forecast":
                        prior_path.write_text(
                            json.dumps(
                                prior_forecast_payload()
                                if prior_forecast is None else prior_forecast,
                                ensure_ascii=False, indent=2),
                            encoding="utf-8",
                        )
                        argv += ["--prior-forecast", str(prior_path)]
                    else:
                        argv.append("--no-prior-forecast")
            argv += list(extra_args)
            return subprocess.run(argv, capture_output=True, text=True, timeout=30)

    def assert_passes(self, **kwargs):
        proc = self.run_validator(**kwargs)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("PASS", proc.stdout)
        self.assertNotIn("Traceback", proc.stdout + proc.stderr)

    def assert_fails(self, contains=None, **kwargs):
        proc = self.run_validator(**kwargs)
        self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("FAIL", proc.stdout)
        self.assertNotIn("Traceback", proc.stdout + proc.stderr)
        if contains is not None:
            self.assertIn(contains, proc.stdout, proc.stdout)


class GoldenReports(ValidatorCase):
    def test_forecast_prior_maintain_passes_in_both_run_modes(self):
        self.assert_passes()
        self.assert_passes(dry_run=True)

    def test_forecast_prior_flip_passes_in_both_run_modes(self):
        self.assert_passes(answer="yes")
        self.assert_passes(answer="yes", dry_run=True)

    def test_legacy_prior_passes_in_both_run_modes(self):
        self.assert_passes(mode="legacy")
        self.assert_passes(mode="legacy", dry_run=True)

    def test_baseline_passes_in_both_run_modes(self):
        self.assert_passes(baseline=True)
        self.assert_passes(baseline=True, dry_run=True)

    def test_ndx_fetch_failed_passes(self):
        self.assert_passes(
            report=make_report(ndx_failed=True), macro=ndx_failed_macro(),
            current_forecast=forecast_payload(r1_drawdown_pct=None),
        )



class SpvDealMarkerTests(ValidatorCase):
    def test_tagged_row_with_all_attributes_passes(self):
        self.assert_passes(report=spv_deal_marker_fixture())

    def test_tagged_row_missing_a_required_key_fails(self):
        report = spv_deal_marker_fixture(
            event_item=spv_event_item(omit=["debt_tenor"])
        )
        self.assert_fails(report=report)

    def test_tagged_row_with_empty_value_fails(self):
        report = spv_deal_marker_fixture(
            event_item=spv_event_item(lease_term=" ")
        )
        self.assert_fails(report=report)

    def test_tag_on_quarterly_state_row_fails(self):
        report = spv_deal_marker_fixture()
        report = replace_once(
            report,
            "[quarterly_state] top-5 capex vs FCF",
            "[quarterly_state][spv_deal] top-5 capex vs FCF",
        )
        self.assert_fails(report=report)

    def test_tag_on_a_different_sources_row_fails(self):
        report = spv_deal_marker_fixture()
        report = replace_once(
            report, TRACE_ROW,
            TRACE_ROW.replace("AI rename scan", "AI rename scan [spv_deal]"),
        )
        self.assert_fails(report=report)

    def test_untagged_event_scan_row_without_attributes_passes(self):
        report = spv_deal_marker_fixture(event_item="[event_scan] large bond financing disclosed")
        self.assert_passes(report=report)

    def test_substring_key_impostor_is_rejected(self):
        # sublease_term= must not satisfy the lease_term= requirement, and
        # non_debt_tenor= must not satisfy debt_tenor= -- no unanchored
        # substring match may stand in for the real key.
        marker = CONTRACT["spv_deal_marker"]
        item = (
            f"[{marker['component_id']}]{marker['tag']} SPV deal "
            "sublease_term=15y;non_debt_tenor=7y;"
            "sponsor_equity_split=60/40;residual_value_guarantee=undisclosed;"
            "lead_lenders=Bank A;"
        )
        self.assert_fails(report=spv_deal_marker_fixture(event_item=item))

    def test_reversed_order_attributes_fails(self):
        marker = CONTRACT["spv_deal_marker"]
        values = {
            "sponsor_equity_split": "60/40",
            "residual_value_guarantee": "undisclosed",
            "lease_term": "15y",
            "debt_tenor": "7y",
            "lead_lenders": "Bank A, Bank B",
        }
        pairs = "".join(
            f"{key}={values[key]};" for key in reversed(marker["required_keys"])
        )
        item = f"[{marker['component_id']}]{marker['tag']} SPV deal {pairs}"
        self.assert_fails(report=spv_deal_marker_fixture(event_item=item))

    def test_duplicated_attribute_key_fails(self):
        item = spv_event_item() + "lease_term=20y;"
        self.assert_fails(report=spv_deal_marker_fixture(event_item=item))

    def test_uppercase_tag_variant_fails(self):
        marker = CONTRACT["spv_deal_marker"]
        item = (
            f"[{marker['component_id']}]{marker['tag'].upper()} "
            "SPV deal with zero recorded attributes at all"
        )
        self.assert_fails(report=spv_deal_marker_fixture(event_item=item))

    def test_key_nested_in_preceding_value_fails(self):
        # No standalone lease_term= token exists here -- it only appears
        # unseparated inside residual_value_guarantee's captured value, at a
        # position that still satisfies the exactly-once and ordering checks.
        marker = CONTRACT["spv_deal_marker"]
        item = (
            f"[{marker['component_id']}]{marker['tag']} SPV deal "
            "sponsor_equity_split=60/40;"
            "residual_value_guarantee=undisclosed lease_term=15y;"
            "debt_tenor=7y;lead_lenders=Bank A;"
        )
        self.assert_fails(report=spv_deal_marker_fixture(event_item=item))

    def test_punctuation_prefixed_key_impostor_fails(self):
        # not.sponsor_equity_split= must not satisfy sponsor_equity_split --
        # a key only counts when it follows whitespace or ';'.
        marker = CONTRACT["spv_deal_marker"]
        item = (
            f"[{marker['component_id']}]{marker['tag']} SPV deal "
            "not.sponsor_equity_split=60/40;not.residual_value_guarantee=undisclosed;"
            "not.lease_term=15y;not.debt_tenor=7y;not.lead_lenders=Bank A;"
        )
        self.assert_fails(report=spv_deal_marker_fixture(event_item=item))

    def test_untagged_row_with_spv_keyword_fails(self):
        self.assert_fails(report=spv_deal_marker_fixture(
            event_item="[event_scan] SPV sale-leaseback financing disclosed"
        ))

    def test_spv_keyword_on_other_source_row_is_not_blocked(self):
        # Deliberate scope decision: SPV keywords plus a hyperscaler name on
        # another source's row stay valid -- structural.ai_infrastructure_debt
        # legitimately records neocloud sale-leaseback deals whose disclosed
        # backing names a hyperscaler as customer, and tenant-vs-customer is
        # not machine-decidable from free text. Routing lives in the prompt.
        report = spv_deal_marker_fixture()
        report = replace_once(
            report, TRACE_ROW,
            TRACE_ROW.replace(
                "AI rename scan",
                "AI rename scan; CoreWeave sale-leaseback SPV backed by "
                "Microsoft capacity commitments",
            ),
        )
        self.assert_passes(report=report)

    def test_untagged_row_with_jv_keyword_fails(self):
        self.assert_fails(report=spv_deal_marker_fixture(
            event_item="[event_scan] JV vehicle with third-party majority "
                       "equity financing disclosed"
        ))

    def test_last_pair_missing_terminator_fails(self):
        item = spv_event_item()
        assert item.endswith(";")
        self.assert_fails(report=spv_deal_marker_fixture(event_item=item[:-1]))

    def test_missing_semicolon_between_pairs_fails(self):
        marker = CONTRACT["spv_deal_marker"]
        item = (
            f"[{marker['component_id']}]{marker['tag']} SPV deal "
            "sponsor_equity_split=60/40;residual_value_guarantee=undisclosed;"
            "lease_term=15y debt_tenor=7y;lead_lenders=Bank A;"
        )
        self.assert_fails(report=spv_deal_marker_fixture(event_item=item))


class RoundTwoReviewFixes(ValidatorCase):
    def test_indented_uncited_bullet_after_blank_line_fails(self):
        report = replace_once(
            make_report(), "## 支持 no 的證據\n", "## 支持 no 的證據\n\n - [R1] 沒有引用的證據。\n")
        self.assert_fails(report=report, contains="cites no successful contract source_id")

    def test_uniformly_indented_valid_bullets_pass(self):
        report = make_report()
        for heading in ("## 支持 yes 的證據", "## 支持 no 的證據"):
            start = report.index(heading)
            end = report.index("\n## ", start + 1)
            section = report[start:end].replace("\n- ", "\n - ")
            report = report[:start] + section + report[end:]
        self.assert_passes(report=report)

    def test_stray_prose_in_evidence_section_fails(self):
        report = replace_once(
            make_report(), "## 支持 yes 的證據\n", "## 支持 yes 的證據\n\n本次無可用資料\n")
        self.assert_fails(report=report, contains="stray text")

    def test_false_drawdown_claim_in_appendix_fails(self):
        report = replace_once(
            make_report(), "### Raw data\n", "距 52 週高點回撤 99.99%\n\n### Raw data\n")
        self.assert_fails(report=report, contains="drawdown claim")

    def test_ordered_item_after_cited_bullet_fails(self):
        line = f"- [R1] 距 52 週高點回撤僅 {NDX_DRAWDOWN:.2f}%。`{NDX_ID}`"
        report = replace_once(make_report(), line, line + "\n1. [R1] 沒有引用的證據。")
        self.assert_fails(report=report, contains="stray text")

    def test_blockquote_in_evidence_section_fails(self):
        report = replace_once(
            make_report(), "## 支持 no 的證據\n", "## 支持 no 的證據\n\n> 沒有引用的引言。\n")
        self.assert_fails(report=report, contains="stray text")

    def test_negative_drawdown_claim_fails(self):
        report = replace_once(
            make_report(), "### Raw data\n",
            f"距 52 週高點回撤 -{NDX_DRAWDOWN:.2f}%\n\n### Raw data\n")
        self.assert_fails(report=report, contains="drawdown claim")

    def test_english_score_or_probability_prose_fails(self):
        report = replace_once(
            make_report(), "**結論：no**\n",
            "**結論：no**\n\nAI bubble Burst Probability: 80%; Tier: high.\n")
        self.assert_fails(report=report, contains="scoring/probability term")

    def test_score_or_probability_prose_fails(self):
        report = replace_once(
            make_report(), "**結論：no**\n", "**結論：no**\n\n泡沫評分 99/100，破裂機率 75%。\n")
        self.assert_fails(report=report, contains="scoring/probability term")


class HeadingsTitleMeta(ValidatorCase):
    """Check 1: exact H2 headings, title, meta line."""

    def test_missing_h2_fails(self):
        report = replace_once(make_report(), "## 與前期比較\n", "")
        self.assert_fails(report=report, contains="H2 headings/order mismatch")

    def test_reordered_h2_fails(self):
        report = make_report()
        report = report.replace("## 支持 yes 的證據", "@@A").replace(
            "## 支持 no 的證據", "## 支持 yes 的證據").replace(
            "@@A", "## 支持 no 的證據")
        self.assert_fails(report=report, contains="H2 headings/order mismatch")

    def test_extra_h2_fails(self):
        report = replace_once(
            make_report(), "## 數據附錄", "## 本次總分\n\n無。\n\n## 數據附錄")
        self.assert_fails(report=report, contains="H2 headings/order mismatch")

    def test_removed_scoring_sections_are_not_demanded(self):
        report = make_report()
        for old_heading in ("## 六維度評分", "## 綜合分數", "## 本次分數存檔"):
            self.assertNotIn(old_heading, report)
        self.assert_passes()

    def test_wrong_title_fails(self):
        report = replace_once(
            make_report(), f"# {DATE} AI 泡沫破裂預測報告",
            f"# {DATE} 市場泡沫風險評估報告")
        self.assert_fails(report=report, contains="report title must be")

    def test_title_date_must_match_forecast_date(self):
        report = replace_once(
            make_report(), f"# {DATE} AI", "# 2026-07-14 AI")
        self.assert_fails(report=report)

    def test_missing_meta_line_fails(self):
        meta = next(line for line in make_report().splitlines()
                    if line.startswith("報告日期："))
        self.assert_fails(
            report=replace_once(make_report(), meta + "\n", ""),
            contains="title area must contain exactly")

    def test_meta_window_must_end_at_horizon(self):
        report = replace_once(
            make_report(), f"{DATE} → {HORIZON_END}", f"{DATE} → 2027-01-12")
        self.assert_fails(report=report, contains="預測窗口 must be")

    def test_meta_prior_reference_must_match_prior_date(self):
        report = replace_once(
            make_report(), f"report-{PRIOR_DATE}（4天前）",
            f"report-{PRIOR_DATE}（5天前）")
        self.assert_fails(report=report, contains="meta prior reference")

    def test_meta_iso_week_must_match_date(self):
        report = replace_once(make_report(), "ISO 週次：2026-W29", "ISO 週次：2026-W30")
        self.assert_fails(report=report, contains="meta ISO week")


class ConclusionSection(ValidatorCase):
    """Check 2: the conclusion line."""

    def test_conclusion_must_agree_with_forecast_answer(self):
        report = replace_once(make_report(), "**結論：no**", "**結論：yes**")
        self.assert_fails(report=report, contains="does not match forecast answer")

    def test_hedged_first_line_fails(self):
        report = replace_once(make_report(), "**結論：no**", "**結論：偏 no**")
        self.assert_fails(report=report, contains="first conclusion line")

    def test_text_before_conclusion_line_fails(self):
        report = replace_once(
            make_report(), "## 結論\n**結論：no**", "## 結論\n前言。\n**結論：no**")
        self.assert_fails(report=report, contains="first conclusion line")

    def test_second_conclusion_line_fails(self):
        report = replace_once(
            make_report(), "三條路徑皆未接近", "**結論：yes**\n\n三條路徑皆未接近")
        self.assert_fails(report=report, contains="repeats a conclusion line")


class ResolutionSection(ValidatorCase):
    """Check 3: verbatim resolution block and version line."""

    def test_paraphrased_block_fails(self):
        report = replace_once(
            make_report(), "≥ 25%", "≥ 20%")
        self.assert_fails(report=report, contains="verbatim")

    def test_block_missing_fails(self):
        report = replace_once(make_report(), RESOLUTION_BLOCK, "見前次報告。")
        self.assert_fails(report=report, contains="verbatim")

    def test_version_line_missing_fails(self):
        report = replace_once(
            make_report(), f"解析版本：v{CONTRACT['resolution']['version']}\n", "")
        self.assert_fails(report=report, contains="解析版本")

    def test_wrong_version_line_fails(self):
        report = replace_once(
            make_report(), f"解析版本：v{CONTRACT['resolution']['version']}",
            "解析版本：v9")
        self.assert_fails(report=report, contains="解析版本")

    def test_version_line_must_follow_block(self):
        version_line = f"解析版本：v{CONTRACT['resolution']['version']}"
        report = replace_once(
            make_report(), RESOLUTION_BLOCK + "\n\n" + version_line,
            RESOLUTION_BLOCK + "\n\n補充說明。\n\n" + version_line)
        self.assert_fails(report=report, contains="解析版本")


    def test_annotation_after_version_line_fails(self):
        version_line = f"解析版本：v{CONTRACT['resolution']['version']}"
        report = replace_once(
            make_report(), version_line,
            version_line + "\n\n補充：R1 門檻改採回撤 10%。")
        self.assert_fails(report=report, contains="must contain only the contract block")

    def test_text_before_block_fails(self):
        report = replace_once(
            make_report(), RESOLUTION_BLOCK, "本次解析條件如下。\n\n" + RESOLUTION_BLOCK)
        self.assert_fails(report=report, contains="must contain only the contract block")


class PathSections(ValidatorCase):
    """Check 4: three path H3s, 判讀 lines, R1 drawdown text."""

    def test_stray_h3_outside_paths_and_appendix_fails(self):
        report = replace_once(
            make_report(), "## 支持 yes 的證據\n", "## 支持 yes 的證據\n\n### 不合約標題\n")
        self.assert_fails(report=report, contains="H3 headings outside")

    def test_false_drawdown_claim_in_evidence_fails(self):
        report = replace_once(
            make_report(), f"距 52 週高點回撤僅 {NDX_DRAWDOWN:.2f}%", "距 52 週高點回撤僅 95.00%")
        self.assert_fails(report=report, contains="drawdown claim")

    def test_unrounded_matching_drawdown_claim_passes(self):
        report = replace_once(
            make_report(), f"距 52 週高點回撤僅 {NDX_DRAWDOWN:.2f}%",
            f"距 52 週高點回撤僅 {NDX_DRAWDOWN:g}%")
        self.assert_passes(report=report)

    def test_drawdown_claim_when_block_failed_fails(self):
        report = make_report(ndx_failed=True).replace(
            "## 支持 no 的證據\n", "## 支持 no 的證據\n\n- [R1] 距 52 週高點回撤 12.00%。`valuation.sp500_trend`\n", 1)
        self.assert_fails(
            report=report, macro=ndx_failed_macro(),
            current_forecast=forecast_payload(r1_drawdown_pct=None),
            contains="although ndx_drawdown failed")

    def test_missing_path_h3_fails(self):
        report = replace_once(make_report(), "### R2 資本支出收縮\n", "")
        self.assert_fails(report=report, contains="path H3 headings/order mismatch")

    def test_reordered_path_h3_fails(self):
        report = make_report()
        report = report.replace("### R2 資本支出收縮", "@@").replace(
            "### R3 AI 信用事件", "### R2 資本支出收縮").replace(
            "@@", "### R3 AI 信用事件")
        self.assert_fails(report=report, contains="path H3 headings/order mismatch")

    def test_missing_judgement_line_fails(self):
        report = replace_once(
            make_report(), "**判讀：** 尚無任何一家下修，距離至少兩家下修的條件很遠。",
            "尚無任何一家下修。")
        self.assert_fails(report=report, contains="lacks a `**判讀：**` line")

    def test_r1_drawdown_text_must_match_artifact(self):
        report = replace_once(make_report(), "回撤 5.00%", "回撤 4.00%")
        self.assert_fails(report=report, contains="距 52 週高點回撤 5.00%")

    def test_r1_drawdown_needs_two_decimals(self):
        report = replace_once(make_report(), "回撤 5.00%", "回撤 5%")
        self.assert_fails(report=report, contains="距 52 週高點回撤 5.00%")

    def test_r1_failed_block_requires_unavailable_text(self):
        report = replace_once(
            make_report(ndx_failed=True), R1_UNAVAILABLE_TEXT, "NASDAQ-100 回撤約五成。")
        self.assert_fails(
            report=report, macro=ndx_failed_macro(),
            current_forecast=forecast_payload(r1_drawdown_pct=None),
            contains="R1 回撤不可用")


class EvidenceSections(ValidatorCase):
    """Check 5: tagged, source-cited bullets citing only successful sources."""

    def test_bullet_without_path_tag_fails(self):
        report = replace_once(
            make_report(), "- [R3] AI 信用定價出現分歧", "- AI 信用定價出現分歧")
        self.assert_fails(report=report, contains="must start with a path tag")

    def test_bullet_without_citation_fails(self):
        report = replace_once(
            make_report(),
            "- [R3] AI 信用定價出現分歧，部分借款人利差擴大。`valuation.ai_credit_schism`",
            "- [R3] AI 信用定價出現分歧，部分借款人利差擴大。")
        self.assert_fails(report=report, contains="cites no successful contract source_id")

    def test_bullet_citing_only_unsuccessful_source_fails(self):
        report = replace_once(
            make_report(), "利差擴大。`valuation.ai_credit_schism`",
            "利差擴大。`structural.ai_infrastructure_debt`")
        self.assert_fails(report=report, contains="cites no successful contract source_id")

    def test_empty_evidence_section_fails(self):
        report = replace_once(
            make_report(),
            "- [R3] AI 信用定價出現分歧，部分借款人利差擴大。`valuation.ai_credit_schism`\n",
            "")
        self.assert_fails(report=report, contains="needs at least 1 top-level bullet")

    def test_body_citation_of_unsuccessful_source_fails(self):
        report = replace_once(
            make_report(), "三條路徑皆未接近解析條件，",
            "三條路徑皆未接近解析條件（`structural.ai_infrastructure_debt`），")
        self.assert_fails(report=report, contains="whose Coverage status is not successful")

    def test_failed_ndx_source_cannot_be_cited_in_path_text(self):
        report = replace_once(
            make_report(ndx_failed=True), R1_UNAVAILABLE_TEXT,
            R1_UNAVAILABLE_TEXT + f"`{NDX_ID}`")
        self.assert_fails(
            report=report, macro=ndx_failed_macro(),
            current_forecast=forecast_payload(r1_drawdown_pct=None),
            contains=f"body cites {NDX_ID}")

    def test_unsuccessful_source_may_be_named_in_gaps_section(self):
        report = replace_once(
            make_report(), "- 下一次財報日期尚未公布",
            "- `structural.ai_infrastructure_debt` 本次未揭露。\n- 下一次財報日期尚未公布")
        self.assert_passes(report=report)


class ForecastObject(ValidatorCase):
    """Check 6: forecast JSON fence vs standalone file vs report."""

    def test_fence_must_equal_standalone_file(self):
        self.assert_fails(
            current_forecast=forecast_payload(r1_drawdown_pct=5.5),
            contains="does not equal the report JSON fence")

    def test_type_conflation_between_bool_and_number_fails(self):
        current = forecast_payload(question_version=True)
        report = make_report(forecast=current)
        self.assert_fails(report=report, current_forecast=current,
                          contains="question_version")

    def _both(self, **overrides):
        current = forecast_payload(**overrides)
        return dict(report=make_report(forecast=current), current_forecast=current)

    def test_extra_key_fails(self):
        current = {**forecast_payload(), "total": 42}
        self.assert_fails(
            report=make_report(forecast=current), current_forecast=current,
            contains="fields mismatch")

    def test_missing_key_fails(self):
        current = forecast_payload()
        del current["flip_evidence"]
        self.assert_fails(
            report=make_report(forecast=current), current_forecast=current,
            contains="fields mismatch")

    def test_date_must_equal_report_date(self):
        self.assert_fails(**self._both(date="2026-07-14"), contains="date does not match")

    def test_iso_week_must_match(self):
        self.assert_fails(**self._both(iso_week="2026-W30"), contains="iso_week")

    def test_weekday_must_match(self):
        self.assert_fails(**self._both(weekday="Tuesday"), contains="weekday")

    def test_timezone_must_match(self):
        self.assert_fails(**self._both(timezone="UTC"), contains="timezone")

    def test_question_version_must_match_contract(self):
        self.assert_fails(**self._both(question_version=2), contains="question_version")

    def test_resolution_version_must_match_contract(self):
        self.assert_fails(**self._both(resolution_version=2), contains="resolution_version")

    def test_answer_must_be_yes_or_no(self):
        self.assert_fails(**self._both(answer="maybe"), contains="answer must be one of")

    def test_horizon_end_must_be_date_plus_horizon(self):
        self.assert_fails(**self._both(horizon_end="2027-01-12"), contains="horizon_end")

    def test_r1_drawdown_must_equal_macro(self):
        self.assert_fails(**self._both(r1_drawdown_pct=6.0), contains="r1_drawdown_pct")

    def test_r1_drawdown_null_fails_when_block_ok(self):
        self.assert_fails(**self._both(r1_drawdown_pct=None), contains="r1_drawdown_pct")

    def test_r1_drawdown_must_be_null_when_block_failed(self):
        current = forecast_payload()
        self.assert_fails(
            report=make_report(ndx_failed=True, forecast=current),
            macro=ndx_failed_macro(), current_forecast=current,
            contains="must be null when ndx_drawdown failed")

    def test_resolution_must_be_null(self):
        self.assert_fails(**self._both(resolution="yes"), contains="resolution must be null")

    def test_forecast_json_in_wrong_section_fails(self):
        report = make_report()
        fence_start = report.index("```json")
        fence_end = report.index("```\n", fence_start + 7) + 4
        fence = report[fence_start:fence_end]
        report = report[:fence_start] + "存檔見附錄。\n" + report[fence_end:]
        report = replace_once(report, "## 數據附錄\n", "## 數據附錄\n\n" + fence + "\n")
        self.assert_fails(report=report, contains="outside")

    def test_duplicate_json_key_fails(self):
        report = replace_once(
            make_report(), '"date": "2026-07-13",',
            '"date": "2026-07-13",\n  "date": "2026-07-13",')
        self.assert_fails(report=report, contains="duplicate JSON key")


class PriorAndFlip(ValidatorCase):
    """Check 7: prior forecast, flip discipline, legacy and baseline lines."""

    def test_macro_prior_run_date_must_match_prior_forecast(self):
        macro = macro_payload()
        macro["prior_run_date"] = "2026-07-11"
        self.assert_fails(macro=macro, contains="macro prior_run_date")

    def test_prior_forecast_missing_fields_fails(self):
        prior = prior_forecast_payload()
        del prior["horizon_end"]
        self.assert_fails(prior_forecast=prior, contains="prior forecast lacks fields")

    def test_prior_date_must_match_prior_forecast_date(self):
        current = forecast_payload(prior_date="2026-07-11")
        macro = macro_payload()
        macro["prior_run_date"] = "2026-07-11"
        self.assert_fails(
            report=make_report(forecast=current), current_forecast=current,
            macro=macro, contains="prior_date does not match prior forecast date")

    def test_prior_answer_must_match_prior_forecast_answer(self):
        current = forecast_payload(prior_answer="yes")
        self.assert_fails(
            report=make_report(forecast=current), current_forecast=current,
            contains="prior_answer does not match")

    def test_first_line_must_state_prior_conclusion(self):
        report = replace_once(
            make_report(), f"前次結論：no（report-{PRIOR_DATE}）",
            f"前次結論：yes（report-{PRIOR_DATE}）")
        self.assert_fails(report=report, contains="first line must be")

    def test_unchanged_answer_requires_maintain_line(self):
        report = replace_once(make_report(), "本次結論：維持", "本次結論：翻轉")
        self.assert_fails(report=report, contains="本次結論：維持")

    def test_unchanged_answer_requires_empty_flip_evidence(self):
        current = forecast_payload(flip_evidence=["ai.hyperscaler_capex"])
        self.assert_fails(
            report=make_report(forecast=current), current_forecast=current,
            contains="flip_evidence must be [] when the answer is unchanged")

    def test_flip_requires_flip_line(self):
        report = replace_once(
            make_report(answer="yes"), "本次結論：翻轉", "本次結論：維持")
        self.assert_fails(report=report, answer="yes", contains="本次結論：翻轉")

    def test_flip_requires_nonempty_flip_evidence(self):
        current = forecast_payload(answer="yes", flip_evidence=[])
        self.assert_fails(
            report=make_report(answer="yes", forecast=current),
            answer="yes", current_forecast=current,
            contains="flip_evidence must be non-empty")

    def test_flip_evidence_must_be_deduplicated(self):
        ids = ["ai.hyperscaler_capex", "ai.hyperscaler_capex"]
        current = forecast_payload(answer="yes", flip_evidence=ids)
        self.assert_fails(
            report=make_report(answer="yes", forecast=current),
            answer="yes", current_forecast=current, contains="duplicates")

    def test_flip_evidence_must_be_contract_source(self):
        current = forecast_payload(answer="yes", flip_evidence=["made.up_source"])
        self.assert_fails(
            report=make_report(answer="yes", forecast=current),
            answer="yes", current_forecast=current, contains="not a contract source_id")

    def test_flip_evidence_must_be_successful_source(self):
        current = forecast_payload(
            answer="yes", flip_evidence=["structural.ai_infrastructure_debt"])
        report = replace_once(
            make_report(answer="yes", forecast=current),
            "見 `ai.hyperscaler_capex`，", "見 `structural.ai_infrastructure_debt`，")
        self.assert_fails(
            report=report, answer="yes", current_forecast=current,
            contains="lacks a successful Coverage status")

    def test_flip_evidence_must_postdate_prior_forecast(self):
        row = raw_row("ai.hyperscaler_capex")
        report = replace_once(
            make_report(answer="yes"), row,
            row.replace("| 2026-07-10 |", f"| {PRIOR_DATE} |"))
        self.assert_fails(report=report, answer="yes", contains="dated after")

    def test_flip_evidence_must_be_cited_in_comparison(self):
        report = replace_once(
            make_report(answer="yes"), "見 `ai.hyperscaler_capex`，", "見資本支出來源，")
        self.assert_fails(report=report, answer="yes", contains="is not cited in")

    def test_legacy_prior_requires_legacy_line(self):
        report = replace_once(
            make_report(mode="legacy"),
            f"前次結論：無前次預測（report-{PRIOR_DATE} 為舊格式評分報告）",
            "前次結論：無前次（基準）")
        self.assert_fails(report=report, mode="legacy", contains="first line must be")

    def test_legacy_prior_must_not_carry_prior_answer(self):
        current = forecast_payload("legacy", prior_answer="no")
        self.assert_fails(
            report=make_report("legacy", forecast=current), mode="legacy",
            current_forecast=current, contains="prior_answer must be null")

    def test_legacy_prior_must_not_carry_flip_evidence(self):
        current = forecast_payload("legacy", flip_evidence=["ai.hyperscaler_capex"])
        self.assert_fails(
            report=make_report("legacy", forecast=current), mode="legacy",
            current_forecast=current, contains="flip_evidence must be []")

    def test_legacy_prior_date_must_match_macro(self):
        macro = macro_payload()
        macro["prior_run_date"] = "2026-07-11"
        self.assert_fails(mode="legacy", macro=macro, contains="macro prior_run_date")

    def test_baseline_requires_baseline_line(self):
        report = replace_once(
            make_report(mode="baseline"), "前次結論：無前次（基準）",
            f"前次結論：無前次預測（report-{PRIOR_DATE} 為舊格式評分報告）")
        self.assert_fails(report=report, mode="baseline", contains="first line must be")

    def test_baseline_requires_macro_none(self):
        self.assert_fails(
            baseline=True, macro=macro_payload(), contains="prior_run_date")


class GapsSection(ValidatorCase):
    """Check 8: FETCH FAILED sources are listed."""

    def failed_kwargs(self, report):
        return dict(
            report=report, macro=ndx_failed_macro(),
            current_forecast=forecast_payload(r1_drawdown_pct=None))

    def test_failed_source_must_be_mentioned(self):
        report = replace_once(
            make_report(ndx_failed=True), f"- `{NDX_ID}` 為 FETCH FAILED，", "- 某來源缺漏，")
        self.assert_fails(**self.failed_kwargs(report), contains="must mention FETCH FAILED")

    def test_none_line_required_when_nothing_failed(self):
        report = replace_once(make_report(), "本次無 FETCH FAILED 來源\n", "資料齊備。\n")
        self.assert_fails(report=report, contains="本次無 FETCH FAILED 來源")

    def test_none_line_contradicts_a_failed_source(self):
        report = replace_once(
            make_report(ndx_failed=True), "- 下一次財報日期",
            "本次無 FETCH FAILED 來源\n- 下一次財報日期")
        self.assert_fails(**self.failed_kwargs(report), contains="claims no FETCH FAILED")


class NdxDrawdownMacro(ValidatorCase):
    """The ndx_drawdown block is reproduced from its 252 observations."""

    def mutated(self, mutate):
        macro = macro_payload()
        mutate(macro["ndx_drawdown"])
        return macro

    def test_missing_block_fails(self):
        macro = macro_payload()
        del macro["ndx_drawdown"]
        self.assert_fails(macro=macro, contains="macro top-level fields mismatch")

    def test_window_must_hold_exactly_252_observations(self):
        macro = self.mutated(lambda b: b["window_observations"].pop())
        self.assert_fails(macro=macro, contains="window_observations must hold exactly")

    def test_window_dates_must_be_unique_newest_first(self):
        def mutate(block):
            window = block["window_observations"]
            window[5], window[6] = window[6], window[5]
        self.assert_fails(
            macro=self.mutated(mutate), contains="not unique newest-first")

    def test_duplicate_window_dates_fail(self):
        def mutate(block):
            block["window_observations"][3]["date"] = block["window_observations"][2]["date"]
        self.assert_fails(
            macro=self.mutated(mutate), contains="not unique newest-first")

    def test_latest_must_equal_first_observation(self):
        macro = self.mutated(lambda b: b.update(latest=19900.0))
        self.assert_fails(macro=macro, contains="window_observations[0]")

    def test_high_must_be_window_maximum(self):
        macro = self.mutated(lambda b: b.update(high=20900.0))
        self.assert_fails(macro=macro, contains="max of window_observations")

    def test_high_date_must_belong_to_high_observation(self):
        macro = self.mutated(
            lambda b: b.update(high_date=b["window_observations"][50]["date"]))
        self.assert_fails(macro=macro, contains="high_date/high is absent")

    def test_drawdown_arithmetic_is_recomputed(self):
        macro = self.mutated(lambda b: b.update(drawdown_pct=4.9))
        self.assert_fails(macro=macro, contains="drawdown_pct arithmetic")

    def test_threshold_level_is_recomputed(self):
        macro = self.mutated(lambda b: b.update(r1_threshold_level=15000.0))
        self.assert_fails(macro=macro, contains="r1_threshold_level arithmetic")

    def test_threshold_pct_must_match_contract(self):
        macro = self.mutated(lambda b: b.update(r1_threshold_pct=20))
        self.assert_fails(macro=macro, contains="r1_threshold_pct")

    def test_r1_met_must_match_drawdown(self):
        macro = self.mutated(lambda b: b.update(r1_met=True))
        self.assert_fails(macro=macro, contains="r1_met")

    def test_fetch_failed_must_not_retain_success_fields(self):
        macro = ndx_failed_macro()
        macro["ndx_drawdown"]["latest"] = 19950.0
        self.assert_fails(
            report=make_report(ndx_failed=True), macro=macro,
            current_forecast=forecast_payload(r1_drawdown_pct=None),
            contains="fetch_failed retains success fields")

    def test_invalid_status_fails(self):
        macro = self.mutated(lambda b: b.update(status="stale"))
        self.assert_fails(macro=macro, contains="invalid status")

    def test_raw_rows_must_reproduce_artifact_values(self):
        report = replace_once(
            make_report(), f"| {NDX_HIGH:.2f} |", "| 20999.00 |")
        self.assert_fails(report=report, contains="ndx_drawdown high")

    def test_raw_rows_must_include_drawdown_pct(self):
        report = replace_once(
            make_report(), ndx_raw_rows()[2] + "\n", "")
        self.assert_fails(report=report, contains="ndx_drawdown drawdown_pct")

    def test_coverage_cannot_claim_success_for_failed_block(self):
        report = make_report(ndx_failed=True).replace(
            coverage_row(NDX_ID).replace("✓ API", "⛔ FETCH FAILED"),
            coverage_row(NDX_ID))
        self.assert_fails(
            report=report, macro=ndx_failed_macro(),
            current_forecast=forecast_payload(r1_drawdown_pct=None),
            contains="cannot claim script/direct success")


class CliAndGlobal(ValidatorCase):
    def test_missing_all_cli_args_fails_cleanly(self):
        proc = subprocess.run(
            [sys.executable, str(VALIDATOR)], capture_output=True, text=True, timeout=20)
        self.assertNotEqual(proc.returncode, 0)
        self.assertNotIn("Traceback", proc.stdout + proc.stderr)

    def test_prior_mode_flag_is_required(self):
        proc = self.run_validator(prior_flag=False)
        self.assertEqual(proc.returncode, 2, proc.stdout + proc.stderr)
        self.assertIn("one of the arguments", proc.stderr)

    def test_prior_flags_are_mutually_exclusive(self):
        proc = self.run_validator(extra_args=("--no-prior-forecast",))
        self.assertEqual(proc.returncode, 2, proc.stdout + proc.stderr)
        self.assertIn("not allowed with", proc.stderr)

    def test_run_mode_flags_are_mutually_exclusive(self):
        proc = self.run_validator(extra_args=("--dry-run",))
        self.assertEqual(proc.returncode, 2, proc.stdout + proc.stderr)
        self.assertIn("not allowed with", proc.stderr)

    def test_run_mode_flag_is_required(self):
        proc = self.run_validator(include_required_args=False)
        self.assertNotEqual(proc.returncode, 0)

    def test_old_score_flags_are_rejected(self):
        proc = self.run_validator(extra_args=("--current-score", "x.json"))
        self.assertEqual(proc.returncode, 2, proc.stdout + proc.stderr)

    def test_macro_requires_marker_envelope(self):
        self.assert_fails(macro_markers=False, contains="marker-delimited envelope")

    def test_dry_run_requires_banner(self):
        self.assert_fails(report=make_report(), dry_run=True, contains="DRY RUN banner")

    def test_production_rejects_dry_run_banner(self):
        self.assert_fails(
            report=DRY_BANNER + "\n\n" + make_report(), contains="must not contain")

    def test_ascii_tilde_fails(self):
        report = replace_once(make_report(), "約兩成", "~兩成")
        self.assert_fails(report=report, contains="ASCII `~`")

    def test_api_key_query_secret_fails(self):
        report = make_report().replace(
            "FRED NASDAQ100 (ndx_drawdown)",
            "https://api.stlouisfed.org/fred?series_id=NASDAQ100&api_key=super-secret", 1)
        self.assert_fails(report=report, contains="credential-like")

    def test_final_line_must_be_exact_disclaimer(self):
        report = make_report().replace(CONTRACT["disclaimer"], "本報告僅供參考。")
        self.assert_fails(report=report, contains="disclaimer")

    def test_synonym_in_comparison_section_fails(self):
        report = replace_once(
            make_report(), "- 自前次預測以來", "- 本期自前次預測以來")
        self.assert_fails(report=report, contains="terminology-locked")

    def test_synonym_in_ordinary_unlocked_prose_passes(self):
        report = replace_once(
            make_report(), "目前未見符合規模", "本期目前未見符合規模")
        self.assert_passes(report=report)

    def test_unexpected_table_fails(self):
        report = replace_once(
            make_report(), "## 資料缺漏與不確定性\n",
            "## 資料缺漏與不確定性\n\n| a | b |\n|---|---|\n| 1 | 2 |\n")
        self.assert_fails(report=report, contains="uncontracted Markdown table")

    def test_html_comment_fails(self):
        report = replace_once(
            make_report(), "- 下一次財報", "<!-- hidden -->\n- 下一次財報")
        self.assert_fails(report=report, contains="HTML comments")



class FetcherValidatorIntegration(ValidatorCase):
    def test_fetcher_main_exact_stdout_envelope_passes_validator(self):
        spec = importlib.util.spec_from_file_location(
            "fetch_macro_validator_integration", REPO / "scripts" / "fetch_macro.py"
        )
        fetch_macro = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(fetch_macro)
        expected = macro_payload()
        output = io.StringIO()

        def mocked_series(series_id, _unit):
            return copy.deepcopy(expected["series"][series_id])

        fixed_now = fetch_macro.datetime.fromisoformat(TIMESTAMP)
        with (
            mock.patch.object(fetch_macro, "PRIOR", PRIOR_DATE),
            mock.patch.object(fetch_macro, "FRED_KEY", "test-key-present"),
            mock.patch.object(fetch_macro, "EIA_KEY", ""),
            mock.patch.object(fetch_macro, "execution_now", return_value=fixed_now),
            mock.patch.object(fetch_macro, "series_block", side_effect=mocked_series),
            mock.patch.object(
                fetch_macro, "sp500_trend",
                return_value=copy.deepcopy(expected["sp500_trend"]),
            ),
            mock.patch.object(
                fetch_macro, "ndx_drawdown",
                return_value=copy.deepcopy(expected["ndx_drawdown"]),
            ),
            mock.patch.object(
                fetch_macro, "cftc_lev_funds",
                return_value=copy.deepcopy(expected["cftc_lev_funds"]),
            ),
            mock.patch.object(
                fetch_macro, "move_index",
                return_value=copy.deepcopy(expected["move_index"]),
            ),
            mock.patch.object(
                fetch_macro, "ofr_repo",
                return_value=copy.deepcopy(expected["ofr_repo"]),
            ),
            mock.patch.object(
                fetch_macro, "repo_stress_block",
                return_value=copy.deepcopy(expected["repo_stress"]),
            ),
            mock.patch.object(
                fetch_macro, "decomposition_block",
                return_value=copy.deepcopy(expected["decomposition"]),
            ),
            contextlib.redirect_stdout(output),
        ):
            fetch_macro.main()

        macro_text = output.getvalue()
        self.assertTrue(macro_text.startswith("===MACRO_JSON_START===\n"))
        self.assertTrue(macro_text.endswith("\n===MACRO_JSON_END===\n"))
        self.assert_passes(macro_text=macro_text)


class MarkdownSectionAwareness(ValidatorCase):
    def test_tilde_fence_content_is_excluded_from_ascii_tilde_scan(self):
        validator = load_validator_module()
        failures = validator.Failures()
        doc = validator.MarkdownDocument(
            "~~~text\ninside ~ is code\n~~~\n\n" + CONTRACT["disclaimer"],
            failures,
        )
        validator.validate_global_security(doc, CONTRACT, failures)
        self.assertEqual(failures.items, [])

    def test_raw_table_in_wrong_section_fails(self):
        report = replace_once(make_report(), RAW_BLOCK, "Raw data moved below.")
        report = replace_once(
            report, "## 資料缺漏與不確定性\n", f"## 資料缺漏與不確定性\n\n{RAW_BLOCK}\n")
        self.assert_fails(report=report)

    def test_fenced_raw_table_does_not_count(self):
        report = replace_once(make_report(), RAW_BLOCK, f"```text\n{RAW_BLOCK}\n```")
        self.assert_fails(report=report)

    def test_fenced_heading_does_not_count(self):
        report = replace_once(
            make_report(),
            "## 與前期比較",
            "```text\n## 與前期比較\n```",
        )
        self.assert_fails(report=report)

    def test_indented_code_table_does_not_count(self):
        indented = "\n".join("    " + line for line in RAW_BLOCK.splitlines())
        self.assert_fails(report=replace_once(make_report(), RAW_BLOCK, indented))

    def test_raw_html_wrapped_table_fails(self):
        wrapped = f"<script type=\"text/plain\">\n{RAW_BLOCK}\n</script>"
        self.assert_fails(report=replace_once(make_report(), RAW_BLOCK, wrapped))

    def test_incomplete_script_start_cannot_hide_table(self):
        wrapped = f"<script\n{RAW_BLOCK}\n</script>"
        self.assert_fails(report=replace_once(make_report(), RAW_BLOCK, wrapped))

    def test_cdata_wrapped_table_fails(self):
        wrapped = f"<![CDATA[\n{RAW_BLOCK}\n]]>"
        self.assert_fails(report=replace_once(make_report(), RAW_BLOCK, wrapped))

    def test_multiline_inline_code_cannot_hide_table(self):
        wrapped = f"`\n{RAW_BLOCK}\n`"
        self.assert_fails(report=replace_once(make_report(), RAW_BLOCK, wrapped))

    def test_four_space_closing_fence_fails(self):
        report = replace_once(
            make_report(),
            "\n```\n\n" + CONTRACT["disclaimer"],
            "\n    ```\n\n" + CONTRACT["disclaimer"],
        )
        self.assert_fails(report=report)

    def test_comment_hidden_checklist_does_not_count(self):
        report = replace_once(
            make_report(),
            "本次無 FETCH FAILED 來源",
            "<!-- 本次無 FETCH FAILED 來源 -->",
        )
        self.assert_fails(report=report)

    def test_setext_heading_syntax_is_rejected(self):
        report = replace_once(
            make_report(),
            "## 與前期比較",
            "與前期比較\n----------------",
        )
        self.assert_fails(report=report)

    def test_unbalanced_fence_fails(self):
        self.assert_fails(report=make_report() + "\n```\n")


class CoverageAndTraceability(ValidatorCase):
    def test_macro_raw_value_and_date_must_match_on_the_same_row(self):
        original = raw_row("monetary.dgs10", "DGS10")
        correct_date_wrong_value = original.replace("| 4.54 |", "| 9.99 |")
        correct_value_wrong_date = original.replace(
            "| 2026-07-10 |", "| 2026-07-09 |"
        )
        report = replace_once(
            make_report(), original,
            correct_date_wrong_value + "\n" + correct_value_wrong_date,
        )
        self.assert_fails(report=report)


    def test_sofr_component_cannot_be_satisfied_by_sofr99_prefix(self):
        sofr = raw_row("monetary.repo_stress_srf", "| SOFR |")
        sofr99 = raw_row("monetary.repo_stress_srf", "SOFR99")
        fake_prefix = sofr99.replace("| 4.35 |", "| 4.3 |")
        report = replace_once(
            make_report(), sofr + "\n" + sofr99,
            fake_prefix + "\n" + sofr99,
        )
        self.assert_fails(report=report)



    def test_fabricated_source_id_fails(self):
        row = coverage_row(CONTRACT["sources"][0]["id"])
        self.assert_fails(
            report=replace_once(make_report(), row, row.replace(
                CONTRACT["sources"][0]["id"], "valuation.fabricated"
            ))
        )

    def test_reordered_source_ids_fail(self):
        first = coverage_row(CONTRACT["sources"][0]["id"])
        second = coverage_row(CONTRACT["sources"][1]["id"])
        report = replace_once(make_report(), first + "\n" + second, second + "\n" + first)
        self.assert_fails(report=report)

    def test_duplicate_source_id_fails(self):
        first = coverage_row(CONTRACT["sources"][0]["id"])
        second = coverage_row(CONTRACT["sources"][1]["id"])
        self.assert_fails(report=replace_once(make_report(), second, first))

    def test_unknown_status_fails(self):
        row = coverage_row(CONTRACT["sources"][0]["id"])
        self.assert_fails(report=replace_once(
            make_report(), row, row.replace("✓ DIRECT", "✓ INVENTED")
        ))

    def test_multiple_status_tokens_fail(self):
        row = coverage_row(CONTRACT["sources"][0]["id"])
        self.assert_fails(report=replace_once(
            make_report(), row, row.replace("✓ DIRECT", "✓ DIRECT / ✓ API")
        ))

    def test_required_source_cannot_be_not_disclosed(self):
        required_id = next(s["id"] for s in CONTRACT["sources"] if s["required"])
        row = coverage_row(required_id)
        self.assert_fails(report=replace_once(
            make_report(), row, row.replace("✓ DIRECT", "✗ NOT DISCLOSED")
        ))

    def test_missing_search_trace_fails(self):
        self.assert_fails(report=replace_once(make_report(), TRACE_ROW + "\n", ""))

    def test_nonzero_search_trace_requires_http_url(self):
        report = replace_once(
            make_report(),
            TRACE_ROW,
            TRACE_ROW.replace(
                "https://example.com/rename", "ftp://example.com/rename"
            ),
        )
        self.assert_fails(report=report)

    def test_nonzero_search_trace_rejects_bare_https_scheme(self):
        report = replace_once(
            make_report(),
            TRACE_ROW,
            TRACE_ROW.replace("https://example.com/rename", "https://"),
        )
        self.assert_fails(report=report)

    def test_stale_event_trace_date_fails(self):
        self.assert_fails(report=replace_once(
            make_report(), TRACE_ROW, TRACE_ROW.replace("2026-07-12", "2026-06-01")
        ))

    def test_trace_id_must_match_coverage_search_id(self):
        self.assert_fails(report=replace_once(
            make_report(), TRACE_ROW, TRACE_ROW.replace(SEARCH_ID, "speculation.fake", 1)
        ))

    def test_prompt_contract_mapping_mismatch_fails(self):
        prompt = PROMPT.read_text(encoding="utf-8")
        needle = CONTRACT["sources"][0]["prompt_match"]
        self.assertEqual(prompt.count(needle), 1)
        prompt = prompt.replace(needle, "renamed source that is absent from contract", 1)
        self.assert_fails(prompt_text=prompt)

    def test_prompt_source_hidden_by_tilde_fence_with_backticks_fails(self):
        prompt = PROMPT.read_text(encoding="utf-8")
        needle = CONTRACT["sources"][0]["prompt_match"]
        source_line = next(
            line for line in prompt.splitlines()
            if line.startswith("- ") and needle in line
        )
        hidden = f"~~~ audit `source hidden`\n{source_line}\n~~~"
        self.assert_fails(prompt_text=replace_once(prompt, source_line, hidden))

    def test_successful_direct_source_requires_raw_evidence(self):
        row = raw_row("valuation.sp500_pe_cape")
        self.assert_fails(report=replace_once(make_report(), row + "\n", ""))

    def test_direct_event_evidence_obeys_contract_window(self):
        row = raw_row("speculation.microcap_moonshots")
        self.assert_fails(report=replace_once(
            make_report(), row, row.replace("2026-07-12", "2026-06-01")
        ))

    def test_all_macro_bindings_crosscheck_coverage(self):
        macro = macro_payload()
        macro["series"]["CPIAUCSL"] = {"status": "fetch_failed", "source": None}
        self.assert_fails(macro=macro)

    def test_zero_result_status_is_contract_limited(self):
        source_id = "valuation.sp500_pe_cape"
        row = coverage_row(source_id)
        report = replace_once(
            make_report(), row,
            row.replace("✓ DIRECT", "✓ SEARCH-VERIFIED（0 件）"),
        )
        self.assert_fails(report=report)

    def test_ten_results_is_not_zero_result(self):
        row = coverage_row(SEARCH_ID)
        report = replace_once(
            make_report(), row,
            row.replace("✓ SEARCH-VERIFIED", "✓ SEARCH-VERIFIED（10 件）"),
        )
        report = replace_once(
            report, TRACE_ROW, TRACE_ROW.replace("2026-07-12", "—")
        )
        self.assert_fails(report=report)

    def test_future_wrong_timezone_retrieval_timestamp_fails(self):
        row = raw_row("valuation.sp500_pe_cape")
        self.assert_fails(report=replace_once(
            make_report(), row, row.replace(TIMESTAMP, "2099-01-01T00:00:00+00:00")
        ))


class VixSpxComoveArtifact(ValidatorCase):
    """The co-movement verdict must be reproducible from the emitted proofs."""

    def comove_true_macro(self):
        """Lower both trailing bases so the recomputed verdict is genuinely true.

        Only the proof bases move, so every reported level, §3 direction and
        appendix row in the golden report stays valid.
        """
        macro = macro_payload()
        macro["series"]["VIXCLS"]["alignment_observations"][1]["value"] = 14.0
        macro["sp500_trend"]["alignment_observations"][1]["value"] = 7500.0
        macro["vix_spx_comove"].update({
            "vix_base": 14.0, "vix_chg_pct": 8.57,
            "sp500_base": 7500.0, "sp500_chg_pct": 1.01,
            "comove": True,
        })
        return macro

    def test_golden_verdict_is_recomputed(self):
        self.assert_passes()

    def test_flipped_verdict_fails(self):
        macro = macro_payload()
        macro["vix_spx_comove"]["comove"] = True
        self.assert_fails(macro=macro)

    def test_vix_chg_pct_arithmetic_is_recomputed(self):
        macro = macro_payload()
        macro["vix_spx_comove"]["vix_chg_pct"] = 8.0
        self.assert_fails(macro=macro)

    def test_sp500_chg_pct_arithmetic_is_recomputed(self):
        macro = macro_payload()
        macro["vix_spx_comove"]["sp500_chg_pct"] = 0.9
        self.assert_fails(macro=macro)

    def test_legs_must_match_the_vix_proof(self):
        macro = macro_payload()
        macro["vix_spx_comove"]["vix_base"] = 14.0
        self.assert_fails(macro=macro)

    def test_legs_must_match_the_sp500_proof(self):
        macro = macro_payload()
        macro["vix_spx_comove"]["sp500"] = 7600.0
        self.assert_fails(macro=macro)

    def test_window_dates_must_match_the_shared_timeline(self):
        for field, value in (
            ("as_of", "2026-07-09"),
            ("base_date", "2026-07-01"),
            ("window_days", 7),
        ):
            with self.subTest(field=field):
                macro = macro_payload()
                macro["vix_spx_comove"][field] = value
                self.assert_fails(macro=macro)

    def test_unavailable_while_window_is_reproducible_fails(self):
        macro = macro_payload()
        macro["vix_spx_comove"] = {
            "status": "unavailable", "comove": False, "note": "x",
        }
        self.assert_fails(macro=macro)

    def test_verdict_without_a_shared_base_fails(self):
        macro = macro_payload()
        del macro["series"]["VIXCLS"]["alignment_observations"][1]
        self.assert_fails(macro=macro)

    def test_missing_shared_base_degrades_to_unavailable(self):
        macro = macro_payload()
        del macro["series"]["VIXCLS"]["alignment_observations"][1]
        macro["vix_spx_comove"] = {
            "status": "unavailable", "comove": False,
            "note": "no shared base observation",
        }
        self.assert_passes(report=comove_unavailable_report(), macro=macro)

    def test_nonpositive_latest_leg_forces_unavailable(self):
        macro = macro_payload()
        macro["series"]["VIXCLS"]["alignment_observations"][0]["value"] = 0.0
        macro["series"]["VIXCLS"]["latest"] = 0.0
        self.assert_fails(macro=macro)


    def test_unavailable_block_cannot_be_certified_as_api_coverage(self):
        # the VIX level still fetched, but with no verdict the Coverage row
        # must not claim script success on the strength of that leg alone
        macro = macro_payload()
        del macro["series"]["VIXCLS"]["alignment_observations"][1]
        macro["vix_spx_comove"] = {
            "status": "unavailable", "comove": False,
            "note": "no shared base observation",
        }
        self.assert_fails(macro=macro)

    def test_derived_raw_row_must_reproduce_from_the_block(self):
        source_id = "structural.vix_spx_comove"
        row = raw_row(source_id, "| vix_spx_comove |")
        report = replace_once(
            make_report(), row, row.replace("| 15.2 |", "| 19.9 |")
        )
        self.assert_fails(report=report)

    def test_base_older_than_twice_the_window_is_unavailable(self):
        macro = macro_payload()
        stale = "2026-06-20"
        macro["series"]["VIXCLS"]["alignment_observations"][1]["date"] = stale
        macro["sp500_trend"]["alignment_observations"][1]["date"] = stale
        self.assert_fails(macro=macro)
        macro["vix_spx_comove"] = {
            "status": "unavailable", "comove": False,
            "note": "shared trailing base is too old",
        }
        self.assert_passes(report=comove_unavailable_report(), macro=macro)

    def test_unavailable_must_not_retain_legs(self):
        macro = macro_payload()
        macro["vix_spx_comove"]["status"] = "unavailable"
        self.assert_fails(macro=macro)

    def test_failed_vix_series_requires_unavailable(self):
        macro = macro_payload()
        macro["series"]["VIXCLS"] = {"status": "fetch_failed", "source": None}
        self.assert_fails(macro=macro)

    def test_invalid_status_fails(self):
        macro = macro_payload()
        macro["vix_spx_comove"]["status"] = "partial"
        self.assert_fails(macro=macro)

    def test_nonboolean_comove_fails(self):
        macro = macro_payload()
        macro["vix_spx_comove"]["comove"] = "false"
        self.assert_fails(macro=macro)

    def test_unexpected_field_fails(self):
        macro = macro_payload()
        macro["vix_spx_comove"]["prior_date"] = PRIOR_DATE
        self.assert_fails(macro=macro)

    def test_missing_block_fails(self):
        macro = macro_payload()
        del macro["vix_spx_comove"]
        self.assert_fails(macro=macro)

    def test_sp500_proof_head_must_be_the_latest_observation(self):
        macro = macro_payload()
        macro["sp500_trend"]["alignment_observations"][0]["value"] = 7000.0
        self.assert_fails(macro=macro)

    def test_sp500_proof_dates_must_be_unique_descending(self):
        macro = macro_payload()
        macro["sp500_trend"]["alignment_observations"].reverse()
        self.assert_fails(macro=macro)

    def test_genuine_comove_passes(self):
        self.assert_passes(macro=self.comove_true_macro())

    def test_genuine_comove_denied_fails(self):
        macro = self.comove_true_macro()
        macro["vix_spx_comove"]["comove"] = False
        self.assert_fails(macro=macro)

    def test_baseline_run_still_produces_a_verdict(self):
        # the trailing window lives on the series timeline, so a baseline run
        # is not a reason to drop the signal
        self.assert_passes(baseline=True)


class MacroArtifactHardening(ValidatorCase):
    def test_fallback_failed_years_shape_is_strict(self):
        for bad_value in ("not-a-list", [], [True], [2026, 2026]):
            with self.subTest(value=bad_value):
                macro = macro_payload()
                macro["series"]["DGS10"]["fallback_failed_years"] = bad_value
                self.assert_fails(macro=macro)

    def test_fallback_failed_years_is_limited_to_treasury_series(self):
        macro = macro_payload()
        macro["series"]["CPIAUCSL"]["fallback_failed_years"] = [2025]
        self.assert_fails(macro=macro)

    def test_fetch_failed_treasury_accepts_valid_fallback_failed_years(self):
        validator = load_validator_module()
        macro = macro_payload(baseline=True)
        macro["series"]["DGS10"] = {
            "status": "fetch_failed",
            "source": None,
            "fallback_failed_years": [2026],
        }
        failures = validator.Failures()
        self.assertTrue(validator.validate_macro_shape(macro, CONTRACT, failures))
        self.assertEqual(failures.items, [])

    def test_no_new_obs_must_be_boolean_in_every_supported_block(self):
        cases = (
            ("series", "DCOILWTICO", "macro series DCOILWTICO"),
            (None, "sp500_trend", "macro sp500_trend"),
            (None, "move_index", "macro move_index"),
            (None, "ofr_repo", "macro ofr_repo"),
        )
        for parent, key, label in cases:
            with self.subTest(block=key):
                macro = macro_payload()
                block = macro[parent][key] if parent else macro[key]
                block["no_new_obs"] = 0
                proc = self.run_validator(macro=macro)
                self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
                self.assertIn(f"{label}.no_new_obs must be boolean", proc.stdout)
                self.assertNotIn("Traceback", proc.stdout + proc.stderr)

    def test_no_new_obs_rejects_boolean_delta_values(self):
        cases = (
            (
                "sp500_trend", "chg_pct", "macro sp500_trend.chg_pct",
                {
                    "prior_spot_date": "2026-07-10",
                    "prior_spot": 7575.39,
                    "chg_pct": False,
                    "no_new_obs": True,
                },
            ),
            (
                "ofr_repo", "chg_pct", "macro ofr_repo.chg_pct",
                {
                    "prior_date": "2026-07-10",
                    "prior_transaction_volume_usd_bn": 700.0,
                    "chg_pct": False,
                    "no_new_obs": True,
                },
            ),
        )
        for key, _field, label, values in cases:
            with self.subTest(block=key):
                macro = macro_payload()
                macro[key].update(values)
                proc = self.run_validator(macro=macro)
                self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
                self.assertIn(f"{label} must be finite numeric", proc.stdout)
                self.assertNotIn("Traceback", proc.stdout + proc.stderr)

    def test_sp500_nonnumeric_latest_fails_without_traceback(self):
        macro = macro_payload()
        macro["sp500_trend"]["latest"] = "not-a-number"
        self.assert_fails(macro=macro)

    def test_sp500_zero_prior_fails_without_traceback(self):
        macro = macro_payload()
        macro["sp500_trend"]["prior_spot"] = 0
        macro["sp500_trend"]["chg_pct"] = 0.0
        self.assert_fails(macro=macro)

    def test_sp500_invalid_prior_date_fails(self):
        macro = macro_payload()
        macro["sp500_trend"]["prior_spot_date"] = "last Thursday"
        self.assert_fails(macro=macro)

    def test_sp500_same_date_prior_requires_no_new_obs(self):
        macro = macro_payload()
        block = macro["sp500_trend"]
        block.update({
            "prior_spot_date": block["latest_date"],
            "prior_spot": block["latest"],
            "chg_pct": 0.0,
        })
        block.pop("no_new_obs", None)
        self.assert_fails(macro=macro)

    def test_sp500_no_new_obs_cannot_hide_nonzero_change(self):
        macro = macro_payload()
        block = macro["sp500_trend"]
        block.update({
            "prior_spot_date": block["latest_date"],
            "prior_spot": 7500.0,
            "chg_pct": round((block["latest"] - 7500.0) / 7500.0 * 100, 2),
            "no_new_obs": True,
        })
        self.assert_fails(macro=macro)

    def test_sp500_valid_same_date_no_new_obs_passes(self):
        macro = macro_payload()
        block = macro["sp500_trend"]
        block.update({
            "latest_date": PRIOR_DATE,
            "prior_spot_date": PRIOR_DATE,
            "prior_spot": block["latest"],
            "chg_pct": 0.0,
            "no_new_obs": True,
        })
        block["alignment_observations"][0]["date"] = PRIOR_DATE
        # VIXCLS still prints for 07-10, so the only shared date left is the
        # trailing base itself: no window remains and the verdict must drop
        # out rather than mix two timelines.
        macro["vix_spx_comove"] = {
            "status": "unavailable",
            "comove": False,
            "note": "no shared base observation",
        }
        row = raw_row("valuation.sp500_trend", "sp500_trend")
        report = replace_once(
            make_report(), row, row.replace("| 2026-07-10 |", f"| {PRIOR_DATE} |")
        )
        self.assert_passes(
            report=comove_unavailable_report(report), macro=macro
        )

    def test_move_nonnumeric_prior_fails(self):
        macro = macro_payload()
        macro["move_index"]["prior"] = "not-a-number"
        self.assert_fails(macro=macro)

    def test_move_zero_prior_fails(self):
        macro = macro_payload()
        macro["move_index"].update({"prior": 0, "delta_abs": 95.0})
        self.assert_fails(macro=macro)

    def test_move_invalid_prior_date_fails(self):
        macro = macro_payload()
        macro["move_index"]["prior_date"] = "yesterday"
        self.assert_fails(macro=macro)

    def test_move_same_date_prior_requires_no_new_obs(self):
        macro = macro_payload()
        block = macro["move_index"]
        block.update({
            "prior_date": block["latest_date"],
            "prior": block["latest"],
            "delta_abs": 0.0,
        })
        block.pop("no_new_obs", None)
        self.assert_fails(macro=macro)

    def test_move_no_new_obs_cannot_hide_nonzero_change(self):
        macro = macro_payload()
        block = macro["move_index"]
        block.update({
            "prior_date": block["latest_date"],
            "prior": 94.0,
            "delta_abs": 1.0,
            "no_new_obs": True,
        })
        self.assert_fails(macro=macro)

    def test_move_valid_same_date_no_new_obs_passes(self):
        macro = macro_payload()
        block = macro["move_index"]
        block.update({
            "latest_date": PRIOR_DATE,
            "prior_date": PRIOR_DATE,
            "prior": block["latest"],
            "delta_abs": 0.0,
            "no_new_obs": True,
        })
        row = raw_row("structural.treasury_basis_trade", "move_index")
        report = replace_once(
            make_report(), row, row.replace("| 2026-07-10 |", f"| {PRIOR_DATE} |")
        )
        self.assert_passes(report=report, macro=macro)

    @staticmethod
    def macro_with_ofr_prior():
        macro = macro_payload()
        macro["ofr_repo"].update({
            "prior_transaction_volume_usd_bn": 650.0,
            "prior_date": PRIOR_DATE,
            "chg_pct": 7.69,
        })
        return macro

    def test_ofr_nonnumeric_prior_fails_without_traceback(self):
        macro = self.macro_with_ofr_prior()
        macro["ofr_repo"]["prior_transaction_volume_usd_bn"] = "not-a-number"
        self.assert_fails(macro=macro)

    def test_ofr_zero_prior_fails_without_traceback(self):
        macro = self.macro_with_ofr_prior()
        macro["ofr_repo"]["prior_transaction_volume_usd_bn"] = 0
        macro["ofr_repo"]["chg_pct"] = 0.0
        self.assert_fails(macro=macro)

    def test_ofr_invalid_prior_date_fails(self):
        macro = self.macro_with_ofr_prior()
        macro["ofr_repo"]["prior_date"] = "yesterday"
        self.assert_fails(macro=macro)

    def test_ofr_same_date_prior_requires_no_new_obs(self):
        macro = self.macro_with_ofr_prior()
        block = macro["ofr_repo"]
        block.update({
            "prior_date": block["latest_date"],
            "prior_transaction_volume_usd_bn": block["transaction_volume_usd_bn"],
            "chg_pct": 0.0,
        })
        block.pop("no_new_obs", None)
        self.assert_fails(macro=macro)

    def test_ofr_no_new_obs_cannot_hide_nonzero_change(self):
        macro = self.macro_with_ofr_prior()
        block = macro["ofr_repo"]
        block.update({"prior_date": block["latest_date"], "no_new_obs": True})
        self.assert_fails(macro=macro)

    def test_ofr_same_date_zero_volume_no_new_obs_passes(self):
        macro = macro_payload()
        macro["ofr_repo"].update({
            "transaction_volume_usd_bn": 0.0,
            "latest_date": PRIOR_DATE,
            "prior_transaction_volume_usd_bn": 0.0,
            "prior_date": PRIOR_DATE,
            "chg_pct": 0.0,
            "no_new_obs": True,
        })
        row = raw_row("structural.treasury_basis_trade", "ofr_repo")
        replacement = row.replace("| 700.0 |", "| 0.0 |").replace(
            "| 2026-07-10 |", f"| {PRIOR_DATE} |"
        )
        report = replace_once(make_report(), row, replacement)
        self.assert_passes(report=report, macro=macro)

    def test_usd_series_same_date_zero_no_new_obs_passes(self):
        macro = macro_payload()
        macro["series"]["RPONTTLD"].update({
            "latest": 0.0,
            "latest_date": PRIOR_DATE,
            "prior": 0.0,
            "prior_date": PRIOR_DATE,
            "chg_pct": 0.0,
            "delta_abs": 0.0,
            "no_new_obs": True,
        })
        macro["repo_stress"]["srf_usage_bn"] = 0.0
        macro["repo_stress"]["srf_date"] = PRIOR_DATE
        row = raw_row("monetary.repo_stress_srf", "RPONTTLD")
        replacement = row.replace("| 0.1 |", "| 0.0 |").replace(
            "| 2026-07-10 |", f"| {PRIOR_DATE} |"
        )
        report = replace_once(make_report(), row, replacement)
        self.assert_passes(report=report, macro=macro)

    def test_repo_headline_iorb_leg_must_match_series(self):
        macro = macro_payload()
        macro["repo_stress"].update({
            "iorb": 4.30,
            "iorb_date": "2026-07-10",
            "sofr_iorb_bps": 0.0,
        })
        self.assert_fails(macro=macro)

    def test_repo_historical_iorb_leg_requires_alignment_proof(self):
        macro = macro_payload()
        macro["repo_stress"].update({
            "iorb": 4.29,
            "iorb_date": "2026-07-09",
            "sofr_iorb_bps": 1.0,
        })
        self.assert_fails(macro=macro)

    def test_repo_historical_iorb_leg_with_alignment_proof_passes(self):
        macro = macro_payload()
        macro["repo_stress"].update({
            "iorb": 4.29,
            "iorb_date": "2026-07-09",
            "sofr_iorb_bps": 1.0,
        })
        macro["series"]["IORB"]["alignment_observations"].append({
            "date": "2026-07-09",
            "value": 4.29,
        })
        self.assert_passes(macro=macro)

    def test_repo_sofr99_leg_must_match_series(self):
        macro = macro_payload()
        macro["repo_stress"].update({
            "sofr99": 5.35,
            "sofr99_date": "2026-07-10",
            "sofr99_iorb": 4.31,
            "sofr99_iorb_date": "2026-07-10",
            "sofr99_iorb_bps": 104.0,
        })
        self.assert_fails(macro=macro)

    def test_derived_t10yie_provenance_cannot_be_forged(self):
        macro = macro_payload()
        block = macro["series"]["T10YIE"]
        block.update({
            "status": "derived",
            "source": "DGS10 - DFII10",
            "derived_from": {
                "DGS10": {"date": block["latest_date"], "value": 99.0},
                "DFII10": {"date": block["latest_date"], "value": 98.9},
            },
        })
        self.assert_fails(macro=macro)

    def test_cpi_success_requires_complete_yoy_fields(self):
        macro = macro_payload()
        for field in ("yoy_base_date", "yoy_base", "yoy_pct"):
            macro["series"]["CPIAUCSL"].pop(field)
        self.assert_fails(macro=macro)

    def test_cpi_yoy_base_age_must_obey_contract_window(self):
        macro = macro_payload()
        macro["series"]["CPIAUCSL"]["yoy_base_date"] = "2024-07-10"
        self.assert_fails(macro=macro)

    def test_non_cpi_yoy_fields_fail_without_traceback(self):
        macro = macro_payload()
        macro["series"]["DGS10"].update({
            "yoy_base_date": "2025-07-10",
            "yoy_base": 4.0,
            "yoy_pct": 13.5,
        })
        self.assert_fails(macro=macro)


if __name__ == "__main__":
    unittest.main()

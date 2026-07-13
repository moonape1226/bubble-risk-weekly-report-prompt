"""End-to-end contract tests for ``scripts/validate_report.py``.

The golden reports deliberately contain every mandatory section and appendix
table.  Negative tests mutate one invariant at a time.  stdlib only; no
network and no dependency on the current wall clock.
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
from unittest import mock
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
VALIDATOR = REPO / "scripts" / "validate_report.py"
PROMPT = REPO / "bubble-risk-weekly-prompt.md"
CONTRACT_PATH = REPO / "report_contract.json"
CONTRACT = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))

DATE = "2026-07-13"
PRIOR_DATE = "2026-07-09"
TIMESTAMP = "2026-07-13T08:00:00+08:00"
SEARCH_ID = "speculation.ai_rename_spac"

CURRENT_SCORES = {
    "valuation": 50,
    "breadth": 40,
    "speculation": 40,
    "retail": 40,
    "monetary": 40,
    "structural": 40,
}
PRIOR_SCORES = {**CURRENT_SCORES, "valuation": 49}


def load_validator_module():
    spec = importlib.util.spec_from_file_location(
        "validate_report_under_test", VALIDATOR
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bar(score):
    return "▰" * (score // 10) + "▱" * (10 - score // 10)


def prior_score():
    return {
        "date": PRIOR_DATE,
        "iso_week": "2026-W28",
        "weekday": "Thursday",
        "timezone": "Asia/Taipei",
        **PRIOR_SCORES,
        # 49*.22 + five weighted 40s = 41.98 -> half-up 42.
        "total": 42,
        "tier": "警戒",
        "regime": "穩定共存",
        "trigger_state": "未擊發",
        "trigger_reasons": [],
        "monetary_side": "中性",
        "hy_oas_widening_streak": 0,
        "sp500_dev200_pct": 11.5,
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
        "RPONTTLD": 0.1, "LNFACBW027SBOG": 1200.0,
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
    common_series["CPIAUCSL"].update({
        "yoy_base_date": "2025-07-10",
        "yoy_base": 310.6796116504854,
        "yoy_pct": 3.0,
    })
    payload = {
        "contract_version": 1,
        "macro_schema_version": 1,
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
        },
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
                elif sid not in ("WALCL", "ECBASSETSW", "JPNASSETS"):
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


def score_payload(baseline=False):
    return {
        "date": DATE,
        "iso_week": "2026-W29",
        "weekday": "Monday",
        "timezone": "Asia/Taipei",
        **CURRENT_SCORES,
        "total": 42,
        "tier": "警戒",
        "regime": "基準日" if baseline else "穩定共存",
        "trigger_state": "未擊發",
        "trigger_reasons": [],
        "monetary_side": "中性",
        "hy_oas_widening_streak": 0,
        "sp500_dev200_pct": 12.0,
    }


def markdown_table(header, rows):
    columns = len(header.strip().strip("|").split("|"))
    separator = "|" + "|".join(["---"] * columns) + "|"
    return "\n".join([header, separator, *rows])


def coverage_block():
    rows = []
    for source in CONTRACT["sources"]:
        if source["id"] == SEARCH_ID:
            status = "✓ SEARCH-VERIFIED"
        elif source.get("macro"):
            status = "✓ API"
        elif source.get("window") == "composite":
            status = (
                "✗ NOT DISCLOSED components="
                "quarterly_state:not_disclosed,event_scan:not_disclosed"
            )
        elif not source["required"]:
            status = "✗ NOT DISCLOSED"
        else:
            status = "✓ DIRECT"
        rows.append(
            f"| {source['id']} | {source['prompt_match']} | contract method | {status} |"
        )
    return markdown_table(CONTRACT["coverage_header"], rows)


def raw_block():
    macro = macro_payload()
    rows = []
    for source in CONTRACT["sources"]:
        source_id = source["id"]
        if source_id == SEARCH_ID or (not source["required"] and not source.get("macro")):
            continue
        binding = source.get("macro")
        if binding:
            for component in binding["components"]:
                key = component["key"]
                block = (macro["series"][key] if component["kind"] == "series"
                         else macro[key])
                if component["kind"] == "series":
                    value = block.get(component.get("value_field", "latest"))
                else:
                    value = block.get(
                        "latest",
                        block.get(
                            "net_contracts",
                            block.get("transaction_volume_usd_bn", 1),
                        ),
                    )
                rows.append(
                    f"| {source_id} | {key} | {value} | API {key} | "
                    f"{block['latest_date']} | {TIMESTAMP} |"
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


def anchor_audit(baseline=False):
    hits = {
        "1997.1", "1997.2", "1997.3", "1997.5", "1997.6", "1997.8",
        "1999.10",
    }
    no_data = set()
    if baseline:
        no_data.update({"1997.7", "1998.2", "1998.7", "1998.8"})
    else:
        hits.update({"1997.7", "1998.8"})
    lines = []
    summaries = []
    percentages = {}
    for anchor in CONTRACT["anchors"]:
        features = CONTRACT["anchor_features"][anchor]
        count = 0
        lines.append(f"**{anchor} feature audit**")
        for feature in features:
            feature_id = feature["id"]
            if feature_id in hits:
                status = "命中"
                count += 1
            elif feature_id in no_data:
                status = "無資料"
            else:
                status = "未命中"
            def evidence_ids(rule):
                ids = set(rule.get("source_ids", []))
                for child in rule.get("rules", []):
                    ids.update(evidence_ids(child))
                return ids

            allowed = evidence_ids(feature["rule"])
            source_text = "—"
            available = [
                source_id for source_id in sorted(allowed)
                if next(item for item in CONTRACT["sources"]
                        if item["id"] == source_id).get("macro")
                or next(item for item in CONTRACT["sources"]
                        if item["id"] == source_id)["required"]
                or source_id == SEARCH_ID
            ]
            if allowed and not available:
                status = "無資料"
            elif allowed and status == "未命中":
                source_text = available[0]
            lines.append(
                f"- {feature_id}｜{status}｜source_ids={source_text}｜contract feature audit"
            )
        total = len(features)
        percentage = int(count * 100 / total / 5 + 0.5) * 5
        percentages[anchor] = percentage
        summaries.append(f"- {anchor}：命中 {count}/{total} = {percentage}%")
    return percentages, summaries, lines


def make_report(baseline=False):
    previous = "—" if baseline else None
    delta = "—" if baseline else None
    s1_rows = []
    for dimension in CONTRACT["dimensions"]:
        name, key = dimension["name"], dimension["key"]
        current = CURRENT_SCORES[key]
        prior = previous if baseline else PRIOR_SCORES[key]
        change = delta if baseline else current - PRIOR_SCORES[key]
        change_cell = change if change in ("—", 0) else f"{change:+d}"
        s1_rows.append(
            f"| {name} | {bar(current)} | {current} | {prior} | {change_cell} |"
        )
    s1_rows.append(
        f"| **加權總分** | {bar(42)} | **42【警戒】** | "
        f"{'—' if baseline else 42} | {'—' if baseline else '0'} |"
    )

    percentages, audit_summaries, feature_lines = anchor_audit(baseline)
    closest = max(CONTRACT["anchors"], key=lambda item: percentages[item])
    similarities = [
        (anchor, percentages[anchor], "◀ 最貼近" if anchor == closest else "")
        for anchor in CONTRACT["anchors"]
    ]
    s2_rows = [
        f"| {name} | {pct}% | {bar(pct)} | {mark} |"
        for name, pct, mark in similarities
    ]

    if baseline:
        meta_prior = "基準日"
        total_delta = "—"
        s3_rows = [
            "| S&P 500 | 7,575.39 | 基準日（無前次可比） |",
            "| WTI 原油 | $69.60 /bbl | 基準日（無前次可比） |",
            "| 10Y Treasury | 4.54% | 基準日（無前次可比） |",
        ]
        regime = "基準日"
        transition = "前次無格局紀錄；本次為基準日。"
        decomposition = "判定 基準日。"
        decomposition_bullets = (
            "- ΔDGS10 名目殖利率週變動：基準日\n"
            "- ΔDFII10 實質殖利率週變動：基準日\n"
            "- ΔT10YIE 損益平衡通膨週變動：基準日"
        )
        new_signal = "基準日；無前次可比。"
    else:
        meta_prior = f"report-{PRIOR_DATE}（4天前）"
        total_delta = "0"
        s3_rows = [
            "| S&P 500 | 7,575.39 | 持平（+0.42%；前次 7,543.64） |",
            "| WTI 原油 | $69.60 /bbl | 持平（0.00%；前次 $69.60） |",
            "| 10Y Treasury | 4.54% | 持平（0.0 bps；前次 4.54%） |",
        ]
        regime = "穩定共存"
        transition = "穩定共存 → 穩定共存。"
        decomposition = "判定 無變動。"
        decomposition_bullets = (
            "- ΔDGS10 名目殖利率週變動：0.0 bps\n"
            "- ΔDFII10 實質殖利率週變動：0.0 bps\n"
            "- ΔT10YIE 損益平衡通膨週變動：0.0 bps"
        )
        new_signal = "vs 前次（4天前）\n\n- 估值溢價較前次上升 1 分。"

    h3_blocks = []
    for index, dimension in enumerate(CONTRACT["dimensions"], 1):
        name, key, weight = dimension["name"], dimension["key"], dimension["weight"]
        score = CURRENT_SCORES[key]
        d = "—" if baseline else score - PRIOR_SCORES[key]
        d_text = d if d in ("—", 0) else f"{d:+d}"
        conclusion = (
            "中性；信用環境位於測試區間。"
            if key == "monetary"
            else "本次位於測試 rubric 區間，依契約計分。"
        )
        evidence_source = [
            "valuation.sp500_pe_cape",
            "breadth.rsp_spy",
            "speculation.ipo_heat",
            "retail.fear_greed",
            "monetary.hy_oas",
            "structural.zero_dte",
        ][index - 1]
        evidence_date = "2026-07-12" if key == "speculation" else "2026-07-10"
        evidence_value = 2.8 if key == "monetary" else 1
        required_input_bullets = ""
        if key == "monetary":
            required_input_bullets = (
                "\n\n- BAMLC0A0CM **0.85**（2026-07-10，FRED BAMLC0A0CM；"
                "source_ids=monetary.ig_oas）——IG OAS 輸入。"
                "\n\n- WALCL **6800000.0**（2026-07-10，FRED WALCL；"
                "source_ids=monetary.walcl）——Fed 資產負債表輸入。"
                "\n\n- ECBASSETSW **7000000.0**（2026-07-10，FRED ECBASSETSW；"
                "source_ids=monetary.ecb_boj）——ECB 流動性輸入。"
                "\n\n- JPNASSETS **7500000.0**（2026-07-10，FRED JPNASSETS；"
                "source_ids=monetary.ecb_boj）——BOJ 流動性輸入。"
                "\n\n- PBoC：✗ NOT DISCLOSED；不納入計分"
                "（source_ids=monetary.pboc）。"
            )
        h3_blocks.append(
            f"### {index}. {name} — {score}（weight {weight}%，Δ {d_text}）\n\n"
            f"- **測試指標** **{evidence_value}**（{evidence_date}，"
            f"https://example.com/{evidence_source}；source_ids={evidence_source}）"
            "——可稽核輸入。"
            f"{required_input_bullets}\n\n"
            f"**結論**：{conclusion}"
        )

    weighted_rows = []
    weighted_total = 0
    for dimension in CONTRACT["dimensions"]:
        name, key, weight = dimension["name"], dimension["key"], dimension["weight"]
        component = CURRENT_SCORES[key] * weight / 100
        weighted_total += component
        weighted_rows.append(
            f"| {name} | {weight}% | {CURRENT_SCORES[key]} | {component:.2f} |"
        )

    score_json = json.dumps(score_payload(baseline), ensure_ascii=False, indent=2)
    return f"""# {DATE} 市場泡沫風險評估報告
> 報告日期：{DATE}；執行日：{DATE} Asia/Taipei；ISO 週次：2026-W29；前次基準：{meta_prior}

**總評**：總分 42【警戒】（Δ {total_delta}）；扳機狀態：未擊發；最貼近錨點：{closest}（{percentages[closest]}%）。

## §1 六維度風險條圖

{markdown_table(CONTRACT['section1_header'], s1_rows)}

## §2 歷史錨點相似度

{markdown_table(CONTRACT['section2_header'], s2_rows)}

## §3 三角訊號

{markdown_table(CONTRACT['section3_header'], s3_rows)}

**三者狀態**：{regime}

- 股市：{'7,575.39，基準日，無前次可比。' if baseline else '7,575.39，持平 +0.42%。'}
- WTI 原油：{'69.60，基準日，無前次可比。' if baseline else '69.60，持平 0.00%。'}
- 10Y 殖利率：{'4.54，基準日，無前次可比。' if baseline else '4.54，持平 0.0 bps。'}

**格局轉變**：{transition}

**10Y 成因拆解**：{decomposition}

{decomposition_bullets}

**扳機鏈**：A 通膨鏈未啟動；[monetary.cpi_yoy] CPIAUCSL yoy_pct=3.0 data_date=2026-07-10；[monetary.t5yifr] T5YIFR latest=2.2 delta_bps={'基準日' if baseline else '0.0'} data_date=2026-07-10；B 槓桿鏈未啟動。

**扳機理由**：none

**結論**：扳機狀態：未擊發——目前未見決定性觸發。

## 六維度評分

{chr(10).join(chr(10) + block for block in h3_blocks).lstrip()}

## 綜合分數

{markdown_table(CONTRACT['weighted_score_header'], weighted_rows)}

加權總分：{weighted_total:.2f} → 42【警戒】

## 歷史泡沫週期對比

相似度計算：checklist v2

{chr(10).join(audit_summaries)}

2000/3 高位回落條件：否

{chr(10).join(feature_lines)}

## 機構情緒對照

本次無新機構調查數據。

## 本次新增訊號

{new_signal}

## 數據附錄

### Raw data

{RAW_BLOCK}

### Coverage

{coverage_block()}

### SEARCH-VERIFIED traceability

{TRACE_BLOCK}

## 本次分數存檔

```json
{score_json}
```

{CONTRACT['disclaimer']}
"""


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


def wti_search_fallback_fixture(marker=None):
    value = 70.25
    marker = marker or f"[triangle_fallback] DCOILWTICO fallback_value={value}"
    macro = macro_payload()
    macro["series"]["DCOILWTICO"] = {
        "status": "fetch_failed",
        "source": None,
    }
    report = make_report()
    coverage = coverage_row("monetary.wti")
    report = replace_once(
        report, coverage,
        coverage.replace("✓ API", "✓ SEARCH-VERIFIED"),
    )
    report = replace_once(
        report, raw_row("monetary.wti", "DCOILWTICO") + "\n", ""
    )
    fallback_trace = (
        f"| monetary.wti | {marker} | DCOILWTICO current spot search | "
        f"https://example.com/wti-fallback | 2026-07-12 | {TIMESTAMP} |"
    )
    report = replace_once(report, TRACE_ROW, TRACE_ROW + "\n" + fallback_trace)
    report = replace_once(
        report,
        "| WTI 原油 | $69.60 /bbl | 持平（0.00%；前次 $69.60） |",
        f"| WTI 原油 | ${value:.2f} /bbl | — |",
    )
    report = replace_once(
        report,
        "- WTI 原油：69.60，持平 0.00%。",
        f"- WTI 原油：{value:.2f}，方向不可用。",
    )
    report = replace_once(
        report, "**三者狀態**：穩定共存", "**三者狀態**：不可判"
    )
    report = replace_once(
        report,
        "**格局轉變**：穩定共存 → 穩定共存。",
        "**格局轉變**：穩定共存 → 不可判。",
    )
    report = replace_once(
        report, '"regime": "穩定共存"', '"regime": "不可判"'
    )
    current = score_payload()
    current["regime"] = "不可判"
    return report, macro, current


def ig_oas_search_fallback_fixture(marker, bullet_value):
    macro = macro_payload()
    macro["series"]["BAMLC0A0CM"] = {
        "status": "fetch_failed", "source": None,
    }
    report = make_report()
    coverage = coverage_row("monetary.ig_oas")
    report = replace_once(
        report, coverage,
        coverage.replace("✓ API", "✓ SEARCH-VERIFIED"),
    )
    report = replace_once(
        report, raw_row("monetary.ig_oas", "BAMLC0A0CM") + "\n", ""
    )
    trace = (
        f"| monetary.ig_oas | {marker} | BAMLC0A0CM current OAS | "
        f"https://example.com/ig-oas | 2026-07-10 | {TIMESTAMP} |"
    )
    report = replace_once(report, TRACE_ROW, TRACE_ROW + "\n" + trace)
    report = replace_once(
        report,
        "BAMLC0A0CM **0.85**（2026-07-10",
        f"BAMLC0A0CM **{bullet_value}**（2026-07-10",
    )
    return report, macro


class ValidatorCase(unittest.TestCase):
    def run_validator(
        self,
        report=None,
        *,
        baseline=False,
        prior=None,
        macro=None,
        macro_text=None,
        current_score=None,
        prompt_text=None,
        dry_run=False,
        macro_markers=True,
        extra_args=(),
        include_required_args=True,
    ):
        generated_report = report is None
        report = make_report(baseline) if generated_report else report
        if dry_run and generated_report:
            report = "> [DRY RUN] this report was not committed to archive.\n\n" + report
        macro = macro_payload(baseline) if macro is None else macro
        current_score = score_payload(baseline) if current_score is None else current_score
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            report_path = root / "report.md"
            prompt_path = root / "prompt.md"
            contract_path = root / "report_contract.json"
            macro_path = root / "macro.json"
            prior_path = root / "prior.json"
            current_path = root / "current-score.json"
            report_path.write_text(report, encoding="utf-8")
            prompt_path.write_text(
                PROMPT.read_text(encoding="utf-8") if prompt_text is None else prompt_text,
                encoding="utf-8",
            )
            contract_path.write_text(
                json.dumps(CONTRACT, ensure_ascii=False), encoding="utf-8"
            )
            if macro_text is None:
                # Exercise acceptance of the fetcher's marker-delimited output.
                macro_json = json.dumps(macro, ensure_ascii=False, indent=2)
                macro_text = (
                    "===MACRO_JSON_START===\n" + macro_json
                    + "\n===MACRO_JSON_END===\n"
                    if macro_markers else macro_json
                )
            macro_path.write_text(macro_text, encoding="utf-8")
            current_path.write_text(
                json.dumps(current_score, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            argv = [sys.executable, str(VALIDATOR), str(report_path)]
            if include_required_args:
                argv += [
                    "--prompt", str(prompt_path),
                    "--contract", str(contract_path),
                    "--macro-json", str(macro_path),
                    "--current-score", str(current_path),
                    "--dry-run" if dry_run else "--production",
                ]
                if baseline:
                    argv.append("--baseline")
                else:
                    prior_path.write_text(
                        json.dumps(prior_score() if prior is None else prior,
                                   ensure_ascii=False, indent=2),
                        encoding="utf-8",
                    )
                    argv += ["--prior-score", str(prior_path)]
            argv += list(extra_args)
            return subprocess.run(argv, capture_output=True, text=True, timeout=20)

    def assert_passes(self, **kwargs):
        proc = self.run_validator(**kwargs)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("PASS", proc.stdout)
        self.assertNotIn("Traceback", proc.stdout + proc.stderr)

    def assert_fails(self, **kwargs):
        proc = self.run_validator(**kwargs)
        self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("FAIL", proc.stdout)
        self.assertNotIn("Traceback", proc.stdout + proc.stderr)


class GoldenReports(ValidatorCase):
    def test_complete_prior_mode_report_passes(self):
        self.assert_passes()

    def test_complete_baseline_report_passes(self):
        self.assert_passes(baseline=True)

    def test_zero_result_search_trace_exception_passes(self):
        report = make_report()
        row = coverage_row(SEARCH_ID)
        report = replace_once(
            report, row, row.replace("✓ SEARCH-VERIFIED", "✓ SEARCH-VERIFIED（0 件）")
        )
        report = replace_once(
            report,
            TRACE_ROW,
            f"| {SEARCH_ID} | AI rename zero-result screen | AI rename past 7 days | "
            f"SEC and Nasdaq checked; 0 qualifying results | — | {TIMESTAMP} |",
        )
        self.assert_passes(report=report)


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
        report = replace_once(report, "## 本次新增訊號\n", f"## 本次新增訊號\n\n{RAW_BLOCK}\n")
        self.assert_fails(report=report)

    def test_score_json_in_wrong_section_fails(self):
        score_fence = "```json\n" + json.dumps(score_payload(), ensure_ascii=False, indent=2) + "\n```"
        report = replace_once(make_report(), score_fence, "分數區塊遺失。")
        report = replace_once(report, "## 數據附錄\n", f"## 數據附錄\n\n{score_fence}\n")
        self.assert_fails(report=report)

    def test_fenced_raw_table_does_not_count(self):
        report = replace_once(make_report(), RAW_BLOCK, f"```text\n{RAW_BLOCK}\n```")
        self.assert_fails(report=report)

    def test_fenced_heading_does_not_count(self):
        report = replace_once(
            make_report(),
            "## 機構情緒對照",
            "```text\n## 機構情緒對照\n```",
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
            "相似度計算：checklist v2",
            "<!-- 相似度計算：checklist v2 -->",
        )
        self.assert_fails(report=report)

    def test_setext_heading_syntax_is_rejected(self):
        report = replace_once(
            make_report(),
            "## 機構情緒對照",
            "機構情緒對照\n----------------",
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

    def test_extra_fabricated_macro_raw_row_cannot_feed_dimension(self):
        original = raw_row("monetary.walcl", "WALCL")
        fabricated = original.replace("| 6800000.0 |", "| 9999999.0 |")
        report = replace_once(make_report(), original, original + "\n" + fabricated)
        report = replace_once(
            report,
            "WALCL **6800000.0**（2026-07-10",
            "WALCL **9999999.0**（2026-07-10",
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

    def test_required_input_accepts_explicit_search_fallback_value(self):
        report, macro = ig_oas_search_fallback_fixture(
            "BAMLC0A0CM spread=0.90", "0.90"
        )
        self.assert_passes(report=report, macro=macro)

    def test_series_digits_alone_are_not_a_search_fallback_value(self):
        report, macro = ig_oas_search_fallback_fixture("BAMLC0A0CM", "0")
        self.assert_fails(report=report, macro=macro)

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


class HistoricalEvidenceSemantics(ValidatorCase):
    def test_missing_qualitative_evidence_cannot_be_declared_miss(self):
        source_id = "speculation.microcap_moonshots"
        coverage = coverage_row(source_id)
        raw = raw_row(source_id)
        report = replace_once(
            make_report(), coverage,
            coverage.replace("✓ DIRECT", "⛔ FETCH FAILED"),
        )
        report = replace_once(report, raw + "\n", "")
        # 2021.6 still says 未命中 and cites this now-unavailable source.
        self.assert_fails(report=report)

    def test_zero_result_trace_cannot_support_positive_feature_hit(self):
        source_id = "speculation.microcap_moonshots"
        coverage = coverage_row(source_id)
        raw = raw_row(source_id)
        zero_trace = (
            f"| {source_id} | microcap zero-result screen | microcap past 7 days | "
            f"SEC checked; 0 qualifying results | — | {TIMESTAMP} |"
        )
        report = replace_once(
            make_report(), coverage,
            coverage.replace("✓ DIRECT", "✓ SEARCH-VERIFIED（0 件）"),
        )
        report = replace_once(report, raw + "\n", "")
        report = replace_once(report, TRACE_ROW, TRACE_ROW + "\n" + zero_trace)
        report = replace_once(
            report,
            "- 1999.4｜未命中｜source_ids=speculation.ipo_heat｜contract feature audit",
            "- 1999.4｜命中｜source_ids=speculation.microcap_moonshots｜contract feature audit",
        )
        report = replace_once(
            report,
            "- 1999 晚期狂熱：命中 1/10 = 10%",
            "- 1999 晚期狂熱：命中 2/10 = 20%",
        )
        report = replace_once(
            report,
            f"| 1999 晚期狂熱 | 10% | {bar(10)} |  |",
            f"| 1999 晚期狂熱 | 20% | {bar(20)} |  |",
        )
        self.assert_fails(report=report)


class MetadataAndStrictCells(ValidatorCase):
    def test_meta_report_date_mismatch_fails(self):
        report = replace_once(make_report(), "報告日期：2026-07-13", "報告日期：2026-07-12")
        self.assert_fails(report=report)

    def test_meta_iso_week_mismatch_fails(self):
        report = replace_once(make_report(), "ISO 週次：2026-W29", "ISO 週次：2026-W28")
        self.assert_fails(report=report)

    def test_meta_prior_interval_mismatch_fails(self):
        report = replace_once(
            make_report(),
            "前次基準：report-2026-07-09（4天前）",
            "前次基準：report-2026-07-09（5天前）",
        )
        self.assert_fails(report=report)

    def test_meta_timezone_mismatch_fails(self):
        report = replace_once(
            make_report(),
            "執行日：2026-07-13 Asia/Taipei",
            "執行日：2026-07-13 UTC",
        )
        self.assert_fails(report=report)

    def test_decorated_dimension_score_fails(self):
        row = f"| 估值溢價 | {bar(50)} | 50 | 49 | +1 |"
        self.assert_fails(report=replace_once(make_report(), row, row.replace("| 50 |", "| 50 points |")))

    def test_decorated_delta_fails(self):
        row = f"| 估值溢價 | {bar(50)} | 50 | 49 | +1 |"
        self.assert_fails(report=replace_once(make_report(), row, row.replace("| +1 |", "| +1 point |")))

    def test_bar_characters_must_be_ordered(self):
        row = f"| 估值溢價 | {bar(50)} | 50 | 49 | +1 |"
        bad = "▰▱▰▰▰▱▱▱▱▱"
        self.assert_fails(report=replace_once(
            make_report(), row, row.replace(bar(50), bad)
        ))

    def test_bar_must_have_exactly_ten_cells(self):
        row = f"| 估值溢價 | {bar(50)} | 50 | 49 | +1 |"
        self.assert_fails(report=replace_once(
            make_report(), row, row.replace(bar(50), bar(50) + "▱")
        ))


class CrossRunState(ValidatorCase):
    def test_same_day_prior_artifact_fails(self):
        prior = prior_score()
        prior.update({
            "date": DATE,
            "iso_week": "2026-W29",
            "weekday": "Monday",
        })
        macro = macro_payload()
        macro["prior_run_date"] = DATE
        self.assert_fails(prior=prior, macro=macro)

    def test_future_prior_artifact_fails(self):
        prior = prior_score()
        prior.update({
            "date": "2026-07-14",
            "iso_week": "2026-W29",
            "weekday": "Tuesday",
        })
        macro = macro_payload()
        macro["prior_run_date"] = "2026-07-14"
        self.assert_fails(prior=prior, macro=macro)

    def test_corrupt_prior_weighted_total_fails(self):
        prior = prior_score()
        prior["total"] = 41
        self.assert_fails(prior=prior)

    def test_corrupt_prior_tier_fails(self):
        prior = prior_score()
        prior["tier"] = "溫和"
        self.assert_fails(prior=prior)

    def test_section1_previous_score_must_match_prior(self):
        row = f"| 估值溢價 | {bar(50)} | 50 | 49 | +1 |"
        self.assert_fails(report=replace_once(
            make_report(), row, row.replace("| 49 |", "| 48 |")
        ))

    def test_json_regime_must_match_section3(self):
        self.assert_fails(report=replace_once(
            make_report(), '"regime": "穩定共存"', '"regime": "分歧"'
        ))

    def test_json_trigger_state_must_match_visible_labels(self):
        self.assert_fails(report=replace_once(
            make_report(), '"trigger_state": "未擊發"', '"trigger_state": "初啟"'
        ))

    def test_json_monetary_side_must_match_d5_conclusion(self):
        self.assert_fails(report=replace_once(
            make_report(), '"monetary_side": "中性"', '"monetary_side": "自滿側"'
        ))

    def test_hy_widening_streak_is_recomputed(self):
        self.assert_fails(report=replace_once(
            make_report(), '"hy_oas_widening_streak": 0', '"hy_oas_widening_streak": 1'
        ))

    def test_sp500_deviation_is_copied_from_macro(self):
        self.assert_fails(report=replace_once(
            make_report(), '"sp500_dev200_pct": 12.0', '"sp500_dev200_pct": 13.0'
        ))

    def test_trigger_side_invariant_fails(self):
        report = replace_once(
            make_report(),
            "**結論**：中性；信用環境位於測試區間。",
            "**結論**：扳機側；信用環境位於測試區間。",
        )
        report = replace_once(
            report, '"monetary_side": "中性"', '"monetary_side": "扳機側"'
        )
        self.assert_fails(report=report)

    def test_trigger_state_cannot_be_arbitrarily_upgraded(self):
        report = make_report()
        report = replace_once(
            report, "扳機狀態：未擊發；最貼近錨點", "扳機狀態：已擊發；最貼近錨點"
        )
        report = replace_once(
            report,
            "**結論**：扳機狀態：未擊發——目前未見決定性觸發。",
            "⚠ **結論**：扳機狀態：已擊發——測試升級。",
        )
        report = replace_once(
            report, '"trigger_state": "未擊發"', '"trigger_state": "已擊發"'
        )
        current = score_payload()
        current["trigger_state"] = "已擊發"
        self.assert_fails(report=report, current_score=current)

    def test_active_machine_trigger_reason_is_mandatory(self):
        macro = macro_payload()
        macro["series"]["BAMLH0A0HYM2"]["delta_bps"] = 50.0
        self.assert_fails(macro=macro)

    def test_tagged_trigger_evidence_must_declare_matching_reason(self):
        source_id = "monetary.private_credit_liquidity"
        coverage = coverage_row(source_id)
        tagged_row = (
            f"| {source_id} | [private_credit_gate] liquidity gate | 1 | "
            f"https://example.com/private-credit-gate | 2026-07-12 | {TIMESTAMP} |"
        )
        insertion_point = raw_row("monetary.hy_oas")
        report = replace_once(
            make_report(), coverage,
            coverage.replace("✗ NOT DISCLOSED", "✓ DIRECT"),
        )
        report = replace_once(
            report, insertion_point, insertion_point + "\n" + tagged_row
        )
        # Score JSON still declares no reasons; tagged trigger evidence must
        # not silently upgrade the narrative without a persisted reason code.
        self.assert_fails(report=report)

    def test_baseline_ignores_cross_run_term_premium_trigger(self):
        macro = macro_payload(baseline=True)
        macro["series"]["THREEFYTP10"].update({
            "prior_date": "2026-07-03", "prior": 0.45,
            "delta_abs": 0.2, "delta_bps": 20.0,
            "delta_note": (
                "trailing ~7d within the series' own timeline "
                "(publication lag; not aligned to prior-run date)"
            ),
        })
        macro["repo_stress"]["iorb"] = 4.29
        macro["repo_stress"]["iorb_date"] = "2026-07-09"
        macro["repo_stress"]["sofr_iorb_bps"] = 1.0
        macro["series"]["IORB"]["alignment_observations"].append({
            "date": "2026-07-09", "value": 4.29,
        })
        self.assert_passes(baseline=True, macro=macro)

    def test_invalid_streak_type_fails_without_traceback(self):
        report = replace_once(
            make_report(), '"hy_oas_widening_streak": 0',
            '"hy_oas_widening_streak": "bad"',
        )
        current = score_payload()
        current["hy_oas_widening_streak"] = "bad"
        self.assert_fails(report=report, current_score=current)


class RequiredStructure(ValidatorCase):
    def test_locked_locations_reject_this_run_synonyms(self):
        original = "**結論**：本次位於測試 rubric 區間，依契約計分。"
        for synonym in CONTRACT["wording_lock"]["forbidden_synonyms"]:
            with self.subTest(synonym=synonym):
                report = make_report().replace(
                    original,
                    f"**結論**：{synonym}位於測試 rubric 區間，依契約計分。",
                    1,
                )
                self.assert_fails(report=report)

    def test_new_signals_body_rejects_this_run_synonyms(self):
        original = "- 估值溢價較前次上升 1 分。"
        for synonym in CONTRACT["wording_lock"]["forbidden_synonyms"]:
            with self.subTest(synonym=synonym):
                report = replace_once(
                    make_report(), original, f"{original}（{synonym}補充）"
                )
                proc = self.run_validator(report=report)
                self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
                self.assertIn(
                    f"{synonym} appears in a terminology-locked location",
                    proc.stdout,
                )
                self.assertNotIn("Traceback", proc.stdout + proc.stderr)

    def test_triangle_body_rejects_this_run_synonyms(self):
        original = "- 股市：7,575.39，持平 +0.42%。"
        for synonym in CONTRACT["wording_lock"]["forbidden_synonyms"]:
            with self.subTest(synonym=synonym):
                report = replace_once(
                    make_report(), original, f"{original}（較{synonym}）"
                )
                proc = self.run_validator(report=report)
                self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
                self.assertIn(
                    f"{synonym} appears in a terminology-locked location",
                    proc.stdout,
                )
                self.assertNotIn("Traceback", proc.stdout + proc.stderr)

    def test_full_section_wording_lock_follows_renamed_contract_headings(self):
        validator = load_validator_module()
        policy = CONTRACT["wording_lock"]
        synonym = policy["forbidden_synonyms"][0]
        for heading_index in policy["full_section_heading_indexes"]:
            with self.subTest(heading_index=heading_index):
                contract = copy.deepcopy(CONTRACT)
                renamed = f"## Renamed locked section {heading_index}"
                contract["headings"][heading_index] = renamed
                failures = validator.Failures()
                doc = validator.MarkdownDocument(
                    f"{renamed}\n\n- ordinary bullet with {synonym}", failures
                )
                validator.validate_wording_lock(doc, contract, failures)
                self.assertTrue(any(
                    "terminology-locked location" in message
                    for message in failures.items
                ), failures.items)

    def test_wording_lock_does_not_reject_ordinary_prose(self):
        self.assert_passes(report=make_report().replace(
            "——可稽核輸入。", "——本期可稽核輸入。", 1
        ))

    def test_missing_full_h2_section_fails(self):
        report = replace_once(
            make_report(),
            "## 機構情緒對照\n\n本次無新機構調查數據。\n\n",
            "",
        )
        self.assert_fails(report=report)

    def test_missing_dimension_h3_fails(self):
        self.assert_fails(report=replace_once(
            make_report(),
            "### 2. 市場廣度 — 40（weight 13%，Δ 0）",
            "市場廣度 rationale：",
        ))

    def test_dimension_h3_score_mismatch_fails(self):
        self.assert_fails(report=replace_once(
            make_report(),
            "### 2. 市場廣度 — 40（weight 13%，Δ 0）",
            "### 2. 市場廣度 — 41（weight 13%，Δ 0）",
        ))

    def test_missing_dimension_conclusion_fails(self):
        block = (
            "### 1. 估值溢價 — 50（weight 22%，Δ +1）\n\n"
            "- **測試指標** **1**（2026-07-10，"
            "https://example.com/valuation.sp500_pe_cape；"
            "source_ids=valuation.sp500_pe_cape）——可稽核輸入。\n\n"
            "**結論**：本次位於測試 rubric 區間，依契約計分。"
        )
        self.assert_fails(report=replace_once(
            make_report(),
            block,
            block.replace("**結論**：本次位於測試 rubric 區間，依契約計分。", "結論遺失。"),
        ))

    def test_dimension_bullet_cannot_fabricate_appendix_value_link(self):
        old = (
            "- **測試指標** **1**（2026-07-10，"
            "https://example.com/valuation.sp500_pe_cape；"
            "source_ids=valuation.sp500_pe_cape）——可稽核輸入。"
        )
        new = old.replace("**1**", "**999**")
        self.assert_fails(report=replace_once(make_report(), old, new))

    def test_monetary_dimension_cannot_omit_required_walcl_input(self):
        report = make_report()
        required = next(
            line for line in report.splitlines()
            if line.startswith("- WALCL **6800000.0**")
        )
        self.assert_fails(report=replace_once(report, required + "\n\n", ""))

    def test_missing_raw_data_table_fails(self):
        self.assert_fails(report=replace_once(make_report(), RAW_BLOCK, "無 raw data。"))

    def test_appendix_h3_headings_are_required(self):
        report = make_report()
        for heading in (
            "### Raw data\n\n", "### Coverage\n\n",
            "### SEARCH-VERIFIED traceability\n\n",
        ):
            report = replace_once(report, heading, "")
        self.assert_fails(report=report)

    def test_appendix_table_must_belong_to_its_h3(self):
        report = replace_once(make_report(), RAW_BLOCK + "\n\n### Coverage", "### Coverage\n\n" + RAW_BLOCK)
        self.assert_fails(report=report)

    def test_malformed_raw_data_row_fails(self):
        row = (
            f"| valuation.sp500_trend | sp500_trend | 7575.39 | "
            f"API sp500_trend | 2026-07-10 | {TIMESTAMP} |"
        )
        bad = "| valuation.sp500_trend | nonsense | fake | not-a-source | not-a-date | yesterday |"
        self.assert_fails(report=replace_once(make_report(), row, bad))

    def test_missing_checklist_label_fails(self):
        self.assert_fails(report=replace_once(
            make_report(), "相似度計算：checklist v2", "相似度計算：自由判斷"
        ))

    def test_checklist_summary_must_match_section2(self):
        self.assert_fails(report=replace_once(
            make_report(),
            "- 1997 早期建設：命中 7/8 = 90%",
            "- 1997 早期建設：命中 6/8 = 75%",
        ))

    def test_anchor_feature_machine_truth_is_recomputed(self):
        report = replace_once(
            make_report(),
            "- 1997.1｜命中｜source_ids=—｜contract feature audit",
            "- 1997.1｜未命中｜source_ids=—｜contract feature audit",
        )
        report = replace_once(
            report, "- 1997 早期建設：命中 7/8 = 90%",
            "- 1997 早期建設：命中 6/8 = 75%",
        )
        report = replace_once(report, "| 1997 早期建設 | 90% |", "| 1997 早期建設 | 75% |")
        report = replace_once(report, bar(90), bar(75))
        report = replace_once(report, "1997 早期建設（90%）", "1997 早期建設（75%）")
        self.assert_fails(report=report)

    def test_each_anchor_feature_needs_one_audit_line(self):
        line = "- 1997.1｜命中｜source_ids=—｜contract feature audit\n"
        self.assert_fails(report=replace_once(make_report(), line, ""))

    def test_missing_high_retreat_audit_label_fails(self):
        self.assert_fails(report=replace_once(
            make_report(), "2000/3 高位回落條件：否", "高位回落：否"
        ))

    def test_missing_triangle_label_fails(self):
        self.assert_fails(report=replace_once(
            make_report(), "**格局轉變**：穩定共存 → 穩定共存。", "格局沒有變化。"
        ))

    def test_trigger_chain_must_assess_both_paths(self):
        chain = (
            "**扳機鏈**：A 通膨鏈未啟動；"
            "[monetary.cpi_yoy] CPIAUCSL yoy_pct=3.0 data_date=2026-07-10；"
            "[monetary.t5yifr] T5YIFR latest=2.2 delta_bps=0.0 "
            "data_date=2026-07-10；B 槓桿鏈未啟動。"
        )
        self.assert_fails(report=replace_once(
            make_report(),
            chain,
            "**扳機鏈**：",
        ))

    def test_trigger_chain_cpi_yoy_value_must_match_macro(self):
        report = replace_once(
            make_report(),
            "[monetary.cpi_yoy] CPIAUCSL yoy_pct=3.0 data_date=2026-07-10",
            "[monetary.cpi_yoy] CPIAUCSL yoy_pct=3.1 data_date=2026-07-10",
        )
        self.assert_fails(report=report)

    def test_trigger_chain_t5yifr_delta_must_match_macro(self):
        report = replace_once(
            make_report(),
            "[monetary.t5yifr] T5YIFR latest=2.2 delta_bps=0.0 "
            "data_date=2026-07-10",
            "[monetary.t5yifr] T5YIFR latest=2.2 delta_bps=1.0 "
            "data_date=2026-07-10",
        )
        self.assert_fails(report=report)

    def test_institutional_section_cannot_be_empty(self):
        self.assert_fails(report=replace_once(
            make_report(), "\n本次無新機構調查數據。\n\n## 本次新增訊號",
            "\n## 本次新增訊號",
        ))

    def test_institutional_no_data_placeholder_must_be_exclusive(self):
        report = replace_once(
            make_report(),
            "本次無新機構調查數據。\n\n## 本次新增訊號",
            "本次無新機構調查數據。\n\n"
            "- BofA survey update（2026-07-12）。\n\n## 本次新增訊號",
        )
        self.assert_fails(report=report)

    def test_weighted_table_component_mismatch_fails(self):
        self.assert_fails(report=replace_once(
            make_report(), "| 估值溢價 | 22% | 50 | 11.00 |", "| 估值溢價 | 22% | 50 | 10.00 |"
        ))

    def test_missing_weighted_summary_fails(self):
        self.assert_fails(report=replace_once(
            make_report(), "加權總分：42.20 → 42【警戒】", "總分為 42。"
        ))

    def test_new_signals_prior_interval_is_required(self):
        self.assert_fails(report=replace_once(
            make_report(), "vs 前次（4天前）", "本次變動"
        ))


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
        row = raw_row("valuation.sp500_trend", "sp500_trend")
        report = replace_once(
            make_report(), row, row.replace("| 2026-07-10 |", f"| {PRIOR_DATE} |")
        )
        report = replace_once(
            report,
            "| S&P 500 | 7,575.39 | 持平（+0.42%；前次 7,543.64） |",
            "| S&P 500 | 7,575.39 | 持平（0.00%；無新觀測；前次 7,575.39） |",
        )
        report = replace_once(
            report,
            "- 股市：7,575.39，持平 +0.42%。",
            "- 股市：7,575.39，持平 0.00%（無新觀測）。",
        )
        self.assert_passes(report=report, macro=macro)

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


class MacroTriangleCrossChecks(ValidatorCase):
    def test_wti_exact_search_fallback_trace_passes(self):
        report, macro, current = wti_search_fallback_fixture()
        self.assert_passes(report=report, macro=macro, current_score=current)

    def test_wti_search_fallback_rejects_noncanonical_marker(self):
        report, macro, current = wti_search_fallback_fixture(
            "[triangle_fallback] DCOILWTICO fallback=70.25"
        )
        self.assert_fails(report=report, macro=macro, current_score=current)

    def test_sp500_value_must_match_macro(self):
        self.assert_fails(report=replace_once(
            make_report(),
            "| S&P 500 | 7,575.39 | 持平（+0.42%；前次 7,543.64） |",
            "| S&P 500 | 9,999.99 | 持平（+0.42%；前次 7,543.64） |",
        ))

    def test_sp500_below_threshold_must_be_flat(self):
        self.assert_fails(report=replace_once(
            make_report(), "持平（+0.42%；前次 7,543.64）", "▲ +0.42%（前次 7,543.64）"
        ))

    def test_wti_value_must_match_macro(self):
        row = "| WTI 原油 | $69.60 /bbl | 持平（0.00%；前次 $69.60） |"
        self.assert_fails(report=replace_once(
            make_report(), row, row.replace("$69.60 /bbl", "$80.00 /bbl")
        ))

    def test_wti_direction_must_match_macro(self):
        self.assert_fails(report=replace_once(
            make_report(), "持平（0.00%；前次 $69.60）", "▼ -1.00%（前次 $69.60）"
        ))

    def test_ten_year_value_must_match_macro(self):
        row = "| 10Y Treasury | 4.54% | 持平（0.0 bps；前次 4.54%） |"
        self.assert_fails(report=replace_once(
            make_report(), row, row.replace("| 4.54% |", "| 5.54% |")
        ))

    def test_ten_year_direction_must_match_decomposition(self):
        self.assert_fails(report=replace_once(
            make_report(), "持平（0.0 bps；前次 4.54%）", "▲ +5.0 bps（前次 4.54%）"
        ))

    def test_macro_prior_date_must_match_prior_artifact(self):
        macro = macro_payload()
        macro["prior_run_date"] = "2026-07-08"
        self.assert_fails(macro=macro)

    def test_previous_levels_must_match_macro(self):
        self.assert_fails(report=replace_once(
            make_report(), "前次 7,543.64", "前次 99,999"
        ))

    def test_decomposition_leg_values_must_match_macro(self):
        self.assert_fails(report=replace_once(
            make_report(),
            "- ΔDFII10 實質殖利率週變動：0.0 bps",
            "- ΔDFII10 實質殖利率週變動：+999 bps",
        ))

    def test_prompt_precision_rounding_is_accepted(self):
        report = make_report()
        report = replace_once(
            report,
            "| S&P 500 | 7,575.39 | 持平（+0.42%；前次 7,543.64） |",
            "| S&P 500 | 7,575 | 持平（+0.4%；前次 7,544） |",
        )
        report = replace_once(
            report, "- 股市：7,575.39，持平 +0.42%。",
            "- 股市：7,575，持平 +0.4%。",
        )
        self.assert_passes(report=report)


class SecurityAndCli(ValidatorCase):
    def test_api_key_query_secret_fails(self):
        self.assert_fails(report=replace_once(
            make_report(),
            "API sp500_trend",
            "https://api.stlouisfed.org/fred?series_id=SP500&api_key=super-secret",
        ))

    def test_percent_encoded_api_key_query_secret_fails(self):
        self.assert_fails(report=replace_once(
            make_report(),
            "API sp500_trend",
            "https://api.stlouisfed.org/fred?series_id=SP500&api%5Fkey=super-secret",
        ))

    def test_missing_all_cli_args_fails_cleanly(self):
        proc = subprocess.run(
            [sys.executable, str(VALIDATOR)], capture_output=True, text=True, timeout=20
        )
        self.assertNotEqual(proc.returncode, 0)
        self.assertNotIn("Traceback", proc.stdout + proc.stderr)

    def test_report_only_missing_required_flags_fails_cleanly(self):
        proc = self.run_validator(include_required_args=False)
        self.assertNotEqual(proc.returncode, 0)
        self.assertNotIn("Traceback", proc.stdout + proc.stderr)

    def test_prior_and_baseline_are_mutually_exclusive(self):
        proc = self.run_validator(extra_args=("--baseline",))
        self.assertNotEqual(proc.returncode, 0)
        self.assertNotIn("Traceback", proc.stdout + proc.stderr)

    def test_macro_requires_marker_envelope(self):
        self.assert_fails(macro_markers=False)

    def test_nonfinite_json_number_fails(self):
        report = replace_once(
            make_report(), '"sp500_dev200_pct": 12.0',
            '"sp500_dev200_pct": Infinity',
        )
        current = score_payload()
        current["sp500_dev200_pct"] = float("inf")
        self.assert_fails(report=report, current_score=current)

    def test_duplicate_json_key_fails(self):
        report = replace_once(
            make_report(), '"date": "2026-07-13",',
            '"date": "2026-07-13",\n  "date": "2026-07-13",',
        )
        self.assert_fails(report=report)

    def test_standalone_current_score_must_equal_report_fence(self):
        current = score_payload()
        current["valuation"] = 51
        current["total"] = 42
        self.assert_fails(current_score=current)

    def test_dry_run_requires_banner_and_passes_with_it(self):
        self.assert_passes(dry_run=True)
        self.assert_fails(report=make_report(), dry_run=True)

    def test_production_rejects_dry_run_banner(self):
        report = "> [DRY RUN] this report was not committed to archive.\n\n" + make_report()
        self.assert_fails(report=report)


if __name__ == "__main__":
    unittest.main()

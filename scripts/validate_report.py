#!/usr/bin/env python3
"""Fail-closed, section-aware validator for bubble-risk reports.

The machine contract, prompt, macro snapshot and prior/baseline mode are all
mandatory inputs.  Only visible Markdown in the owning section can satisfy a
requirement; fenced, commented or relocated content never counts.
"""

import argparse
import json
import math
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from urllib.parse import unquote, urlsplit


BOX_CHARS = "╔╗╚╝║═╠╣╬┌┐└┘─│├┤┬┴┼"
DATE_RE = r"\d{4}-\d{2}-\d{2}"
SECRET_PATTERNS = (
    re.compile(r"(?i)\b(?:api[_-]?key|access[_-]?token|password|secret)\s*="),
    re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
)


class Failures:
    def __init__(self):
        self.items = []

    def add(self, message):
        self.items.append(message)

    def emit_and_exit(self):
        if not self.items:
            print("PASS: all report-contract checks passed.")
            return 0
        for message in self.items:
            print(f"FAIL: {message}")
        print(f"\n{len(self.items)} failure(s).")
        return 1


def strict_date(value, where, failures):
    if not isinstance(value, str) or not re.fullmatch(DATE_RE, value):
        failures.add(f"{where} must be canonical YYYY-MM-DD: {value!r}")
        return None
    try:
        parsed = date.fromisoformat(value)
    except ValueError:
        failures.add(f"{where} is not a real calendar date: {value!r}")
        return None
    if parsed.isoformat() != value:
        failures.add(f"{where} is not canonical YYYY-MM-DD: {value!r}")
        return None
    return parsed


def finite_number(value):
    """JSON number excluding booleans and non-finite values."""
    return type(value) in (int, float) and math.isfinite(value)


def validate_no_new_obs_pair(
        block, label, *, latest_date_field, prior_date_field,
        latest_value_field, prior_value_field, delta_fields, pair_present,
        require_marker_on_same_date, failures):
    """Apply the shared same-date/zero-change contract to any observation pair."""
    marker = block.get("no_new_obs")
    if "no_new_obs" in block and type(marker) is not bool:
        failures.add(f"{label}.no_new_obs must be boolean")
    missing_delta = [field for field in delta_fields if field not in block]
    if marker is True and (not pair_present or missing_delta):
        failures.add(f"{label}.no_new_obs requires complete prior/delta fields")
    if not pair_present:
        return
    same_date = block.get(prior_date_field) == block.get(latest_date_field)
    if require_marker_on_same_date and same_date and marker is not True:
        failures.add(f"{label} same-date prior requires no_new_obs")
    if marker is True and (
            not same_date
            or block.get(prior_value_field) != block.get(latest_value_field)
            or any(not finite_number(block.get(field))
                   or block.get(field) != 0 for field in delta_fields)):
        failures.add(f"{label}.no_new_obs conflicts with observations")


HTTP_URL_RE = re.compile(r"https?://[^\s|<>]+", re.I)


def contains_valid_http_url(text):
    """Whether text contains an absolute HTTP(S) URL with a real hostname."""
    if not isinstance(text, str):
        return False
    for match in HTTP_URL_RE.finditer(text):
        candidate = match.group().rstrip(".,;:!?)]}，。；：！？）】》」』")
        try:
            parsed = urlsplit(candidate)
        except ValueError:
            continue
        if parsed.scheme.lower() in ("http", "https") and parsed.hostname:
            return True
    return False


def read_text(path, label, failures):
    try:
        return Path(path).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        failures.add(f"cannot read {label} {path!s}: {exc}")
        return None


def _reject_json_constant(value):
    raise ValueError(f"non-finite JSON constant {value}")


def _unique_json_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def parse_json_text(text, label, failures, allow_markers=False,
                    require_markers=False):
    if text is None:
        return None
    payload = text.strip()
    has_marker = "===MACRO_JSON_START===" in payload or "===MACRO_JSON_END===" in payload
    if require_markers and not has_marker:
        failures.add(f"{label} must retain the complete marker-delimited envelope")
        return None
    if allow_markers and has_marker:
        match = re.fullmatch(
            r"\s*===MACRO_JSON_START===\s*\n(.*?)\n"
            r"===MACRO_JSON_END===\s*", text, re.S,
        )
        if not match:
            failures.add(f"{label} has incomplete or duplicate marker delimiters")
            return None
        payload = match.group(1)
    try:
        value = json.loads(
            payload,
            parse_constant=_reject_json_constant,
            object_pairs_hook=_unique_json_object,
        )
    except (TypeError, ValueError, json.JSONDecodeError) as exc:
        failures.add(f"{label} is not valid JSON: {exc}")
        return None
    if not isinstance(value, dict):
        failures.add(f"{label} must be a JSON object")
        return None
    return value


def load_json_file(path, label, failures, allow_markers=False,
                   require_markers=False):
    return parse_json_text(
        read_text(path, label, failures), label, failures,
        allow_markers=allow_markers, require_markers=require_markers,
    )


def validate_contract(contract, failures):
    required = {
        "version", "timezone", "question", "resolution", "headings",
        "wording_lock", "conclusion_line", "evidence_sections",
        "forecast_schema", "disclaimer", "macro_schema", "calibration",
        "coverage_statuses", "coverage_header", "raw_data_header",
        "traceability_header", "appendix_headings", "spv_deal_marker", "sources",
    }
    if not isinstance(contract, dict):
        failures.add("report contract must be a JSON object")
        return False
    missing = required - set(contract)
    if missing:
        failures.add(f"report contract missing keys: {sorted(missing)}")
        return False
    try:
        if contract["version"] != 2:
            failures.add(f"unsupported report contract version: {contract['version']!r}")
        macro_schema = contract["macro_schema"]
        if macro_schema.get("version") != 2:
            failures.add("unsupported macro schema version in contract")
        if len(macro_schema["required_series"]) != 21 or len(
                set(macro_schema["required_series"])) != 21:
            failures.add("contract macro schema must define 21 unique series")
        if set(macro_schema.get("series_units", {})) != set(
                macro_schema["required_series"]):
            failures.add("contract series_units must cover the exact series schema")
        if not set(macro_schema.get("series_units", {}).values()) <= {
                "pct", "usd_mn", "usd", "eur_mn", "jpy_100mn",
                "level", "usd_bn"}:
            failures.add("contract series_units contains an unknown unit")
        trailing = macro_schema.get("trailing_delta_days")
        if trailing != {"THREEFYTP10": 7}:
            failures.add("contract trailing_delta_days is invalid")
        yoy_ages = macro_schema.get("yoy_base_age_days")
        if (not isinstance(yoy_ages, dict) or set(yoy_ages) != {"CPIAUCSL"}
                or not isinstance(yoy_ages.get("CPIAUCSL"), dict)
                or set(yoy_ages["CPIAUCSL"]) != {
                    "min", "max", "same_month_previous_year"}
                or not 0 < yoy_ages["CPIAUCSL"]["min"]
                <= yoy_ages["CPIAUCSL"]["max"]
                or yoy_ages["CPIAUCSL"]["same_month_previous_year"] is not True):
            failures.add("contract yoy_base_age_days is invalid")
        if macro_schema.get("alignment_proof_series") != [
                "DGS10", "DFII10", "IORB", "SOFR99", "VIXCLS"]:
            failures.add("contract alignment_proof_series is invalid")
        derived = macro_schema.get("derived_series")
        if not isinstance(derived, dict) or set(derived) != {"T10YIE"}:
            failures.add("contract derived_series policy is invalid")
        else:
            policy = derived["T10YIE"]
            if (set(policy) != {"source", "left", "right"}
                    or policy["left"] != "DGS10"
                    or policy["right"] != "DFII10"
                    or not isinstance(policy["source"], str)
                    or not policy["source"]):
                failures.add("contract T10YIE derived-series policy is invalid")
        if len(set(macro_schema["required_blocks"])) != len(
                macro_schema["required_blocks"]):
            failures.add("contract macro blocks are not unique")
        if "ndx_drawdown" not in macro_schema["required_blocks"]:
            failures.add("contract macro blocks must include ndx_drawdown")

        question = contract["question"]
        if (not isinstance(question, dict)
                or set(question) != {"version", "text", "horizon_days", "answers"}
                or type(question["version"]) is not int
                or not isinstance(question["text"], str) or not question["text"]
                or type(question["horizon_days"]) is not int
                or question["horizon_days"] <= 0
                or question["answers"] != ["yes", "no"]):
            failures.add("contract question is invalid")
            return False
        answers = question["answers"]
        resolution = contract["resolution"]
        r1 = resolution.get("r1") if isinstance(resolution, dict) else None
        if (not isinstance(resolution, dict)
                or set(resolution) != {"version", "block", "r1", "paths"}
                or type(resolution["version"]) is not int
                or not isinstance(resolution["block"], str)
                or not resolution["block"].strip()
                or not isinstance(r1, dict)
                or set(r1) != {"series", "lookback_trading_days", "drawdown_pct"}
                or not isinstance(r1["series"], str)
                or type(r1["lookback_trading_days"]) is not int
                or r1["lookback_trading_days"] <= 0
                or not finite_number(r1["drawdown_pct"])
                or not 0 < r1["drawdown_pct"] < 100):
            failures.add("contract resolution is invalid")
            return False
        ndx_cfg = macro_schema.get("ndx_drawdown")
        if (not isinstance(ndx_cfg, dict)
                or ndx_cfg.get("series") != r1["series"]
                or ndx_cfg.get("lookback_trading_days")
                != r1["lookback_trading_days"]
                or type(ndx_cfg.get("fetch_back_days")) is not int):
            failures.add("contract macro ndx_drawdown policy conflicts with resolution.r1")
        ids = [source["id"] for source in contract["sources"]]
        if not ids or len(set(ids)) != len(ids):
            failures.add("contract must define a nonempty set of unique source IDs")
        source_ids = set(ids)
        paths = resolution["paths"]
        if (not isinstance(paths, list) or len(paths) != 3
                or [p.get("id") for p in paths] != ["R1", "R2", "R3"]
                or any(not isinstance(p.get("heading"), str)
                       or not p["heading"].startswith("### ")
                       or not isinstance(p.get("source_ids"), list)
                       or not p["source_ids"]
                       or not set(p["source_ids"]) <= source_ids
                       for p in paths)
                or len({p["heading"] for p in paths}) != 3):
            failures.add("contract resolution paths are invalid")

        headings = contract["headings"]
        if (not isinstance(headings, list) or len(headings) != 9
                or len(set(headings)) != 9
                or any(not isinstance(h, str) or not h.startswith("## ")
                       for h in headings)):
            failures.add("contract must define nine unique H2 headings")
            return False
        appendix_headings = contract["appendix_headings"]
        if (not isinstance(appendix_headings, list) or len(appendix_headings) != 3
                or len(set(appendix_headings)) != 3
                or any(not isinstance(h, str) or not h.startswith("### ")
                       for h in appendix_headings)):
            failures.add("contract appendix_headings must be three unique H3 headings")
        spv_marker = contract["spv_deal_marker"]
        if not isinstance(spv_marker, dict) or set(spv_marker) != {
                "source_id", "component_id", "tag", "required_keys", "keywords"}:
            failures.add("contract spv_deal_marker is invalid")
        else:
            marker_source = next(
                (source for source in contract["sources"]
                 if source["id"] == spv_marker.get("source_id")),
                None,
            )
            if marker_source is None:
                failures.add("contract spv_deal_marker source_id is unknown")
            elif marker_source.get("window") != "composite":
                failures.add("contract spv_deal_marker source is not a composite source")
            else:
                marker_component = next(
                    (item for item in marker_source.get("window_components", [])
                     if item.get("id") == spv_marker.get("component_id")),
                    None,
                )
                if marker_component is None:
                    failures.add("contract spv_deal_marker component_id is invalid")
                elif marker_component.get("window") != "30d":
                    failures.add(
                        "contract spv_deal_marker component is not a 30d event scan"
                    )
            if not re.fullmatch(r"\[[a-z_]+\]", spv_marker.get("tag", "")):
                failures.add("contract spv_deal_marker lacks a stable tag")
            required_keys = spv_marker.get("required_keys")
            if (not isinstance(required_keys, list) or not required_keys
                    or any(not isinstance(key, str) or not re.fullmatch(r"[a-z_]+", key)
                           for key in required_keys)
                    or len(required_keys) != len(set(required_keys))):
                failures.add("contract spv_deal_marker required_keys is invalid")
            keywords = spv_marker.get("keywords")
            if (not isinstance(keywords, list) or not keywords
                    or any(not isinstance(keyword, str) or not keyword.strip()
                           for keyword in keywords)
                    or len(keywords) != len(set(keywords))):
                failures.add("contract spv_deal_marker keywords is invalid")

        wording_lock = contract["wording_lock"]
        if (not isinstance(wording_lock, dict)
                or set(wording_lock) != {
                    "full_section_heading_indexes", "forbidden_synonyms",
                    "forbidden_scoring_terms"}
                or not isinstance(wording_lock["forbidden_scoring_terms"], list)
                or not wording_lock["forbidden_scoring_terms"]
                or any(not isinstance(term, str) or not term.strip()
                       for term in wording_lock["forbidden_scoring_terms"])):
            failures.add("contract wording_lock is invalid")
        else:
            locked_indexes = wording_lock["full_section_heading_indexes"]
            forbidden_synonyms = wording_lock["forbidden_synonyms"]
            if (not isinstance(locked_indexes, list) or not locked_indexes
                    or any(type(index) is not int
                           or not 0 <= index < len(headings)
                           for index in locked_indexes)
                    or len(locked_indexes) != len(set(locked_indexes))):
                failures.add("contract wording-lock section indexes are invalid")
            if (not isinstance(forbidden_synonyms, list)
                    or not forbidden_synonyms
                    or any(not isinstance(term, str) or not term
                           for term in forbidden_synonyms)
                    or len(forbidden_synonyms) != len(set(forbidden_synonyms))):
                failures.add("contract wording-lock synonyms are invalid")
        conclusion = contract["conclusion_line"]
        if (not isinstance(conclusion, dict) or set(conclusion) != set(answers)
                or any(not isinstance(line, str) or not line
                       for line in conclusion.values())
                or len(set(conclusion.values())) != len(conclusion)):
            failures.add("contract conclusion_line is invalid")
        evidence = contract["evidence_sections"]
        if (not isinstance(evidence, dict)
                or set(evidence) != {"heading_indexes", "min_bullets", "citation"}
                or not isinstance(evidence["heading_indexes"], list)
                or not evidence["heading_indexes"]
                or any(type(i) is not int or not 0 <= i < len(headings)
                       for i in evidence["heading_indexes"])
                or len(set(evidence["heading_indexes"]))
                != len(evidence["heading_indexes"])
                or type(evidence["min_bullets"]) is not int
                or evidence["min_bullets"] < 1):
            failures.add("contract evidence_sections is invalid")
        schema = contract["forecast_schema"]
        fields = schema.get("current_fields") if isinstance(schema, dict) else None
        if (not isinstance(fields, list)
                or len(fields) != len(set(fields))
                or not {"date", "iso_week", "weekday", "timezone",
                        "question_version", "resolution_version", "answer",
                        "horizon_end", "prior_date", "prior_answer",
                        "flip_evidence", "r1_drawdown_pct", "resolution"
                        } == set(fields)):
            failures.add("contract forecast_schema.current_fields is invalid")
        calibration = contract["calibration"]
        if (not isinstance(calibration, dict) or set(calibration) != {
                "decomposition_identity_tolerance_bps", "vix_comove_chg_pct",
                "vix_comove_sp500_chg_pct", "vix_comove_trailing_days"}
                or any(not finite_number(v) or v <= 0
                       for v in calibration.values())):
            failures.add("contract calibration is invalid")
        if not isinstance(contract["disclaimer"], str) or not contract["disclaimer"]:
            failures.add("contract disclaimer is invalid")

        zero_ids = {
            source["id"] for source in contract["sources"]
            if source.get("zero_result_allowed")
        }
        expected_zero = {
            "speculation.ai_rename_spac", "speculation.microcap_moonshots",
            "speculation.insider_form4", "structural.us_single_stock_etf",
        }
        if zero_ids != expected_zero:
            failures.add("contract zero-result eligibility set is invalid")
        bound_series = set()
        bound_blocks = set()
        for source in contract["sources"]:
            if source.get("window") == "composite":
                if source.get("component_aggregation") not in ("all", "any"):
                    failures.add(
                        f"invalid component aggregation for {source['id']}"
                    )
                components = source.get("window_components", [])
                if (not components
                        or len({item.get("id") for item in components}) != len(components)):
                    failures.add(f"invalid window components for {source['id']}")
            macro = source.get("macro")
            if not macro:
                continue
            if macro.get("aggregation") not in ("all", "any"):
                failures.add(f"invalid macro aggregation for {source['id']}")
            for component in macro.get("components", []):
                kind, key = component.get("kind"), component.get("key")
                value_field = component.get("value_field")
                if value_field is not None and (
                        kind != "series" or value_field != "yoy_pct"
                        or key != "CPIAUCSL"):
                    failures.add(f"invalid macro component value_field for {source['id']}")
                if kind == "series":
                    bound_series.add(key)
                elif kind == "block":
                    bound_blocks.add(key)
                else:
                    failures.add(f"invalid macro component for {source['id']}")
        if bound_series != set(macro_schema["required_series"]):
            failures.add("source macro bindings do not cover the exact series schema")
        uncovered_blocks = set(macro_schema["required_blocks"]) - {
            "repo_stress", "decomposition"
        }
        if bound_blocks != uncovered_blocks:
            failures.add("source macro bindings do not cover reportable macro blocks")
    except (AttributeError, IndexError, KeyError, TypeError, ValueError) as exc:
        failures.add(f"malformed report contract: {exc}")
        return False
    return not failures.items


class MarkdownDocument:
    FENCE_RE = re.compile(r"^( {0,3})(`{3,}|~{3,})(.*)$")
    HEADING_RE = re.compile(r"^( {0,3})(#{1,6})[ \t]+(.+?)\s*$")
    RAW_HTML_RE = re.compile(
        r"</?[A-Za-z][A-Za-z0-9-]*(?:\s[^<>]*|\s*/|/?)>"
    )
    # CommonMark raw-HTML blocks can begin before an opening tag is complete.
    # In particular, a lone ``<script`` hides everything through a later
    # closing tag (or EOF), while block tags such as ``<table`` start a type-6
    # block.  Searching only for a terminating ``>`` therefore fails open.
    RAW_HTML_BLOCK_START_RE = re.compile(
        r"^ {0,3}</?[A-Za-z][A-Za-z0-9-]*(?:[ \t]|/?>|$)", re.I
    )
    RAW_HTML_DECL_RE = re.compile(r"^ {0,3}(?:<!|<\?|\]\]>)")
    SETEXT_UNDERLINE_RE = re.compile(r"^ {0,3}(?:=+|-+)\s*$")

    def __init__(self, text, failures):
        self.text = text
        self.lines = [line.rstrip() for line in text.splitlines()]
        self.visible = []
        self.fences = []
        self.headings = []
        self._scan(failures)

    def _scan(self, failures):
        in_fence = None
        fence_content = []
        current_h2 = None
        if "<!--" in self.text or "-->" in self.text:
            failures.add("HTML comments are forbidden in archived reports")

        for index, line in enumerate(self.lines):
            fence_match = self.FENCE_RE.match(line)
            if (fence_match and fence_match.group(2).startswith("`")
                    and "`" in fence_match.group(3)):
                fence_match = None
            if in_fence:
                if re.fullmatch(
                    r" {0,3}" + re.escape(in_fence["char"])
                    + r"{%d,}\s*" % in_fence["length"],
                    line,
                ):
                    self.fences.append({
                        **in_fence,
                        "end": index,
                        "content": "\n".join(fence_content),
                    })
                    in_fence = None
                    fence_content = []
                else:
                    fence_content.append(line)
                continue

            if fence_match:
                token = fence_match.group(2)
                in_fence = {
                    "start": index,
                    "char": token[0],
                    "length": len(token),
                    "info": fence_match.group(3).strip(),
                    "section": current_h2,
                }
                continue

            # Four-space/tab indentation is a CommonMark code block.  It must
            # never be allowed to masquerade as a visible contract table or
            # heading after ``strip()`` normalization.
            if line.startswith("\t") or line.startswith("    "):
                failures.add(
                    f"indented code blocks are forbidden (line {index + 1})"
                )
                continue

            # The structural contract counts ATX headings.  A Setext
            # underline would render an additional H1/H2 while remaining
            # invisible to that count, so the syntax is forbidden outright.
            if self.SETEXT_UNDERLINE_RE.fullmatch(line):
                failures.add(f"Setext headings/thematic underlines are forbidden (line {index + 1})")

            # Raw HTML containers can suppress their Markdown children in the
            # rendered report (for example, a table inside <script>).  Reports
            # have no legitimate raw-HTML requirement, so reject the syntax.
            if (self.RAW_HTML_RE.search(line)
                    or self.RAW_HTML_DECL_RE.search(line)
                    or self.RAW_HTML_BLOCK_START_RE.search(line)):
                failures.add(f"raw HTML is forbidden (line {index + 1})")

            # CommonMark code spans may cross line breaks.  The contract uses
            # inline code only as same-line pairs; an unmatched run could hide
            # an otherwise required table from the renderer.
            runs = re.findall(r"`+", line)
            for length in {len(run) for run in runs}:
                if sum(len(run) == length for run in runs) % 2:
                    failures.add(
                        f"inline code spans must close on the same line (line {index + 1})"
                    )
                    break

            self.visible.append((index, line))
            heading_match = self.HEADING_RE.match(line)
            if heading_match:
                level = len(heading_match.group(2))
                title = heading_match.group(3)
                normalized = f"{'#' * level} {title}"
                self.headings.append((index, level, title, normalized))
                if level == 2:
                    current_h2 = normalized

        if in_fence:
            failures.add(f"unclosed code fence beginning on line {in_fence['start'] + 1}")

    def visible_nonempty(self):
        return [(index, line.strip()) for index, line in self.visible if line.strip()]

    def section_lines(self, heading):
        matches = [h for h in self.headings if h[3] == heading]
        if len(matches) != 1:
            return []
        start = matches[0][0]
        later_h2 = [h[0] for h in self.headings if h[1] == 2 and h[0] > start]
        end = min(later_h2) if later_h2 else len(self.lines)
        return [(i, line) for i, line in self.visible if start < i < end]

    def subsection_lines(self, heading, parent_h2):
        """Return one H3's visible body only when it belongs to parent_h2."""
        parent = [h for h in self.headings if h[3] == parent_h2 and h[1] == 2]
        matches = [h for h in self.headings if h[3] == heading and h[1] == 3]
        if len(parent) != 1 or len(matches) != 1:
            return []
        start = matches[0][0]
        parent_start = parent[0][0]
        next_h2 = min(
            (h[0] for h in self.headings if h[1] == 2 and h[0] > parent_start),
            default=len(self.lines),
        )
        if not parent_start < start < next_h2:
            return []
        end = min(
            (h[0] for h in self.headings if h[0] > start and h[1] <= 3),
            default=len(self.lines),
        )
        return [(i, line) for i, line in self.visible if start < i < end]


def table_cells(line):
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    return [cell.strip() for cell in stripped[1:-1].split("|")]


def is_separator(line, count):
    cells = table_cells(line)
    return (
        cells is not None and len(cells) == count
        and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)
    )


def find_table(section_lines, header, where, failures):
    positions = [i for i, (_, line) in enumerate(section_lines) if line.strip() == header]
    if len(positions) != 1:
        failures.add(f"{where} must contain exactly one `{header}` table header")
        return []
    position = positions[0]
    header_cells = table_cells(header)
    if header_cells is None:
        failures.add(f"contract header for {where} is malformed")
        return []
    if position + 1 >= len(section_lines) or not is_separator(
            section_lines[position + 1][1], len(header_cells)):
        failures.add(f"{where} table has no valid Markdown separator row")
        return []
    rows = []
    cursor = position + 2
    while cursor < len(section_lines):
        line = section_lines[cursor][1]
        if not line.strip():
            break
        cells = table_cells(line)
        if cells is None:
            break
        if len(cells) != len(header_cells):
            failures.add(
                f"{where} row has {len(cells)} columns; expected {len(header_cells)}: {line}"
            )
        else:
            rows.append(cells)
        cursor += 1
    return rows


def bounded_proof_pairs(proof, label, failures, latest_day=None, latest_value=None):
    """Validate a bounded alignment proof; return [(date, value)] newest first."""
    if not isinstance(proof, list) or not 1 <= len(proof) <= 32:
        failures.add(f"{label} lacks bounded alignment observations")
        return None
    pairs = []
    for index, observation in enumerate(proof):
        if (not isinstance(observation, dict)
                or set(observation) != {"date", "value"}
                or not finite_number(observation.get("value"))):
            failures.add(f"{label} alignment observation {index} is malformed")
            return None
        day = strict_date(
            observation["date"], f"{label} alignment date {index}", failures
        )
        if day is None:
            return None
        pairs.append((day, observation["value"]))
    days = [day for day, _value in pairs]
    if days != sorted(days, reverse=True) or len(days) != len(set(days)):
        failures.add(f"{label} alignment dates are not unique descending")
        return None
    if latest_day is not None and pairs[0] != (latest_day, latest_value):
        failures.add(f"{label} alignment proof does not start at the latest observation")
        return None
    return pairs


def proof_levels(block):
    """Date-keyed levels from an already-validated alignment proof."""
    levels = {}
    proof = block.get("alignment_observations") if isinstance(block, dict) else None
    for observation in proof if isinstance(proof, list) else []:
        if (isinstance(observation, dict)
                and isinstance(observation.get("date"), str)
                and finite_number(observation.get("value"))):
            try:
                levels[date.fromisoformat(observation["date"])] = observation["value"]
            except ValueError:
                continue
    return levels


def expected_comove_legs(macro, contract):
    """Recompute the trailing-window co-movement legs, or None when unavailable.

    Mirrors ``fetch_macro.vix_spx_comove_block``: the window is the newest
    date the two series share plus the newest shared date at or before the
    trailing target, read only from the bounded proofs in the artifact.
    """
    series = macro.get("series") if isinstance(macro.get("series"), dict) else {}
    vix = series.get("VIXCLS") if isinstance(series.get("VIXCLS"), dict) else {}
    sp500 = macro.get("sp500_trend") if isinstance(macro.get("sp500_trend"), dict) else {}
    if vix.get("status") != "ok" or sp500.get("status") != "ok":
        return None
    vix_levels, sp500_levels = proof_levels(vix), proof_levels(sp500)
    shared = sorted(set(vix_levels) & set(sp500_levels), reverse=True)
    if not shared:
        return None
    trailing_days = contract["calibration"]["vix_comove_trailing_days"]
    latest = shared[0]
    target = latest - timedelta(days=trailing_days)
    base = next((day for day in shared if day <= target), None)
    if base is None:
        return None
    window_days = (latest - base).days
    if window_days > trailing_days * 2:
        return None
    if min(vix_levels[latest], vix_levels[base],
           sp500_levels[latest], sp500_levels[base]) <= 0:
        return None
    vix_chg_pct = round(
        (vix_levels[latest] - vix_levels[base]) / vix_levels[base] * 100, 2)
    sp500_chg_pct = round(
        (sp500_levels[latest] - sp500_levels[base]) / sp500_levels[base] * 100, 2)
    return {
        "as_of": latest.isoformat(), "base_date": base.isoformat(),
        "window_days": window_days,
        "vix": vix_levels[latest], "vix_base": vix_levels[base],
        "vix_chg_pct": vix_chg_pct,
        "sp500": sp500_levels[latest], "sp500_base": sp500_levels[base],
        "sp500_chg_pct": sp500_chg_pct,
        "comove": (
            sp500_chg_pct >= contract["calibration"]["vix_comove_sp500_chg_pct"]
            and vix_chg_pct >= contract["calibration"]["vix_comove_chg_pct"]),
    }


NDX_SUCCESS_FIELDS = {
    "series", "latest_date", "latest", "high_date", "high", "drawdown_pct",
    "r1_threshold_pct", "r1_threshold_level", "r1_met", "window_observations",
}


def validate_ndx_drawdown(macro, contract, generated, failures):
    """Reproduce the R1 drawdown block from its own 252 closing observations."""
    block = macro.get("ndx_drawdown")
    if not isinstance(block, dict):
        return
    status = block.get("status")
    if status not in ("ok", "fetch_failed"):
        failures.add("macro block ndx_drawdown has invalid status")
        return
    if status == "fetch_failed":
        stale = sorted(NDX_SUCCESS_FIELDS & set(block))
        if stale:
            failures.add(
                f"macro block ndx_drawdown fetch_failed retains success fields: {stale}"
            )
        return
    cfg = contract["macro_schema"]["ndx_drawdown"]
    r1 = contract["resolution"]["r1"]
    if set(block) != NDX_SUCCESS_FIELDS | {"status", "source"}:
        failures.add(
            "macro block ndx_drawdown fields mismatch: "
            f"missing {sorted(NDX_SUCCESS_FIELDS | {'status', 'source'} - set(block))}, "
            f"extra {sorted(set(block) - NDX_SUCCESS_FIELDS - {'status', 'source'})}"
        )
        return
    if not isinstance(block["source"], str) or not block["source"]:
        failures.add("macro block ndx_drawdown success lacks source")
    if block["series"] != cfg["series"]:
        failures.add("macro block ndx_drawdown.series does not match contract")
    window = block["window_observations"]
    if not isinstance(window, list) or len(window) != cfg["lookback_trading_days"]:
        failures.add(
            "macro block ndx_drawdown.window_observations must hold exactly "
            f"{cfg['lookback_trading_days']} observations"
        )
        return
    pairs = []
    for index, observation in enumerate(window):
        if (not isinstance(observation, dict)
                or set(observation) != {"date", "value"}
                or not finite_number(observation.get("value"))
                or observation["value"] <= 0):
            failures.add(f"macro ndx_drawdown observation {index} is malformed")
            return
        day = strict_date(
            observation["date"], f"macro ndx_drawdown observation date {index}",
            failures,
        )
        if day is None:
            return
        pairs.append((day, observation["value"]))
    days = [day for day, _value in pairs]
    if days != sorted(days, reverse=True) or len(days) != len(set(days)):
        failures.add("macro ndx_drawdown observation dates are not unique newest-first")
        return
    latest_day = strict_date(
        block["latest_date"], "macro block ndx_drawdown latest_date", failures
    )
    if latest_day and generated and latest_day > generated.date():
        failures.add("macro block ndx_drawdown latest_date is after generated_at")
    if (latest_day, block["latest"]) != pairs[0]:
        failures.add("macro ndx_drawdown latest/latest_date != window_observations[0]")
        return
    high = max(value for _day, value in pairs)
    if block["high"] != high:
        failures.add("macro ndx_drawdown.high != max of window_observations")
    high_day = strict_date(
        block["high_date"], "macro block ndx_drawdown high_date", failures
    )
    if high_day and (high_day, block["high"]) not in pairs:
        failures.add("macro ndx_drawdown high_date/high is absent from window_observations")
    if not finite_number(block["drawdown_pct"]) or block["drawdown_pct"] != round(
            (high - pairs[0][1]) / high * 100, 2):
        failures.add("macro ndx_drawdown.drawdown_pct arithmetic is invalid")
    threshold = r1["drawdown_pct"]
    if block["r1_threshold_pct"] != threshold:
        failures.add("macro ndx_drawdown.r1_threshold_pct does not match contract")
    if block["r1_threshold_level"] != round(high * (1 - threshold / 100), 2):
        failures.add("macro ndx_drawdown.r1_threshold_level arithmetic is invalid")
    if type(block["r1_met"]) is not bool or block["r1_met"] != (
            (high - pairs[0][1]) / high * 100 >= threshold):
        failures.add("macro ndx_drawdown.r1_met is inconsistent with the drawdown")


def validate_macro_shape(macro, contract, failures):
    """Reject malformed nested macro data before any semantic traversal."""
    failure_count = len(failures.items)
    schema = contract["macro_schema"]
    if not isinstance(macro, dict):
        failures.add("macro JSON must be an object")
        return False
    expected_top = {
        "contract_version", "macro_schema_version", "generated_at",
        "prior_run_date", "fred_key_present", "eia_key_present", "series",
        *schema["required_blocks"],
    }
    if set(macro) != expected_top:
        failures.add(
            f"macro top-level fields mismatch: missing {sorted(expected_top - set(macro))}, "
            f"extra {sorted(set(macro) - expected_top)}"
        )
    if macro.get("contract_version") != contract["version"]:
        failures.add("macro contract_version does not match report contract")
    if macro.get("macro_schema_version") != schema["version"]:
        failures.add("macro_schema_version does not match report contract")
    generated = parse_iso_timestamp(macro.get("generated_at"))
    if generated is None or generated.utcoffset() != timedelta(hours=8):
        failures.add("macro generated_at must be timezone-aware Asia/Taipei time")
    prior_day = None
    if not isinstance(macro.get("prior_run_date"), str):
        failures.add("macro prior_run_date must be a string")
    elif macro["prior_run_date"] != "none":
        prior_day = strict_date(
            macro["prior_run_date"], "macro prior_run_date", failures
        )
        if generated and prior_day and prior_day >= generated.date():
            failures.add("macro prior_run_date must be strictly before generated_at date")
    for key in ("fred_key_present", "eia_key_present"):
        if type(macro.get(key)) is not bool:
            failures.add(f"macro {key} must be boolean")
    for key in ("series", "sp500_trend", "decomposition"):
        if not isinstance(macro.get(key), dict):
            failures.add(f"macro {key} must be an object")
    series_data = macro.get("series") if isinstance(macro.get("series"), dict) else {}

    def alignment_proves(block, observation_day, observation_value):
        proof = block.get("alignment_observations", []) if isinstance(block, dict) else []
        return any(
            isinstance(item, dict)
            and item.get("date") == observation_day
            and item.get("value") == observation_value
            for item in proof
        )

    if isinstance(macro.get("series"), dict):
        actual = set(series_data)
        expected = set(schema["required_series"])
        if actual != expected:
            failures.add(
                f"macro series IDs mismatch: missing {sorted(expected - actual)}, "
                f"extra {sorted(actual - expected)}"
            )
        success_only_fields = {
            "latest_date", "latest", "prior_date", "prior", "delta_bps",
            "chg_pct", "delta_abs", "no_new_obs", "yoy_base_date",
            "yoy_base", "yoy_pct", "delta_note", "alignment_observations",
        }
        series_units = schema["series_units"]
        trailing_policies = schema["trailing_delta_days"]
        derived_policies = schema["derived_series"]
        for series_id, block in series_data.items():
            if not isinstance(series_id, str) or not isinstance(block, dict):
                failures.add("every macro series entry must map a string ID to an object")
                continue
            status = block.get("status")
            if status not in ("ok", "derived", "fetch_failed"):
                failures.add(f"macro series {series_id} has invalid status")
                continue
            if "fallback_failed_years" in block:
                failed_years = block["fallback_failed_years"]
                if series_id not in ("DGS10", "DFII10"):
                    failures.add(
                        f"macro series {series_id} cannot carry fallback_failed_years"
                    )
                if (not isinstance(failed_years, list) or not failed_years
                        or any(type(year) is not int or not 1900 <= year <= 9999
                               for year in failed_years)
                        or len(failed_years) != len(set(failed_years))):
                    failures.add(
                        f"macro series {series_id}.fallback_failed_years must be "
                        "a nonempty array of unique four-digit years"
                    )
            if status == "derived" and series_id != "T10YIE":
                failures.add(f"macro series {series_id} cannot be derived")
            if status == "fetch_failed":
                stale = sorted(success_only_fields & set(block))
                if stale:
                    failures.add(
                        f"macro series {series_id} fetch_failed retains success fields: {stale}"
                    )
                continue
            if status in ("ok", "derived"):
                unit = series_units.get(series_id)
                if unit is None:
                    failures.add(f"macro series {series_id} lacks a contract unit")
                    continue
                latest_day = strict_date(
                    block.get("latest_date"),
                    f"macro series {series_id} latest_date", failures,
                )
                if generated and latest_day and latest_day > generated.date():
                    failures.add(f"macro series {series_id} latest_date is after generated_at")
                latest = block.get("latest")
                if type(latest) not in (int, float) or not math.isfinite(latest):
                    failures.add(f"macro series {series_id} latest must be finite numeric")
                if not isinstance(block.get("source"), str) or not block["source"]:
                    failures.add(f"macro series {series_id} success lacks source")
                proof_required = (
                    series_id in schema["alignment_proof_series"] and status == "ok"
                )
                proof = block.get("alignment_observations")
                if proof_required:
                    if (not isinstance(proof, list) or not 1 <= len(proof) <= 32):
                        failures.add(
                            f"macro series {series_id} lacks bounded alignment observations"
                        )
                    else:
                        parsed_proof = []
                        for proof_index, observation in enumerate(proof):
                            if (not isinstance(observation, dict)
                                    or set(observation) != {"date", "value"}):
                                failures.add(
                                    f"macro series {series_id} alignment observation is malformed"
                                )
                                parsed_proof = []
                                break
                            proof_day = strict_date(
                                observation.get("date"),
                                f"macro series {series_id} alignment date {proof_index}",
                                failures,
                            )
                            if not finite_number(observation.get("value")):
                                failures.add(
                                    f"macro series {series_id} alignment value is invalid"
                                )
                                parsed_proof = []
                                break
                            parsed_proof.append((proof_day, observation["value"]))
                        if len(parsed_proof) == len(proof):
                            proof_days = [item[0] for item in parsed_proof]
                            if (None in proof_days or proof_days != sorted(
                                    proof_days, reverse=True)
                                    or len(proof_days) != len(set(proof_days))):
                                failures.add(
                                    f"macro series {series_id} alignment dates are not unique descending"
                                )
                            if (parsed_proof[0] != (latest_day, block.get("latest"))):
                                failures.add(
                                    f"macro series {series_id} alignment proof head != latest"
                                )
                elif "alignment_observations" in block:
                    failures.add(
                        f"macro series {series_id} cannot carry alignment observations"
                    )
                if "prior_date" in block:
                    observed_prior = strict_date(
                        block["prior_date"],
                        f"macro series {series_id} prior_date", failures,
                    )
                    if observed_prior and latest_day and observed_prior > latest_day:
                        failures.add(f"macro series {series_id} prior_date is after latest_date")
                    if (observed_prior and prior_day and observed_prior > prior_day
                            and series_id not in trailing_policies):
                        failures.add(f"macro series {series_id} prior_date is after prior_run_date")
                    if (type(block.get("prior")) not in (int, float)
                            or not math.isfinite(block["prior"])):
                        failures.add(f"macro series {series_id} prior must be numeric")
                for field in (
                    "delta_bps", "chg_pct", "delta_abs", "yoy_base", "yoy_pct"
                ):
                    value = block.get(field)
                    if value is not None and (
                            type(value) not in (int, float) or not math.isfinite(value)):
                        failures.add(
                            f"macro series {series_id}.{field} must be finite numeric"
                        )
                has_prior_date = "prior_date" in block
                has_prior_value = "prior" in block
                wide = series_id in ("BOGZ1FL153064486Q", "CPIAUCSL")
                if has_prior_date != has_prior_value:
                    failures.add(
                        f"macro series {series_id} prior_date/prior must appear together"
                    )
                delta_fields = {"delta_bps", "chg_pct", "delta_abs"} & set(block)
                if delta_fields and not (has_prior_date and has_prior_value):
                    failures.add(
                        f"macro series {series_id} deltas require prior_date/prior"
                    )
                expected_no_new_deltas = ["delta_abs"]
                if unit == "pct":
                    expected_no_new_deltas.append("delta_bps")
                elif unit in ("usd", "usd_bn"):
                    expected_no_new_deltas.append("chg_pct")
                validate_no_new_obs_pair(
                    block, f"macro series {series_id}",
                    latest_date_field="latest_date", prior_date_field="prior_date",
                    latest_value_field="latest", prior_value_field="prior",
                    delta_fields=expected_no_new_deltas,
                    pair_present=has_prior_date and has_prior_value,
                    require_marker_on_same_date=not wide,
                    failures=failures,
                )
                if (has_prior_date and has_prior_value
                        and type(block.get("prior")) in (int, float)
                        and finite_number(block.get("prior"))
                        and type(block.get("latest")) in (int, float)
                        and finite_number(block.get("latest"))):
                    raw_delta = block["latest"] - block["prior"]
                    delta_required = block["prior_date"] != block["latest_date"] or not wide
                    if delta_required and "delta_abs" not in block:
                        failures.add(f"macro series {series_id} prior pair lacks delta_abs")
                    if (delta_required and unit == "pct"
                            and "delta_bps" not in block):
                        failures.add(f"macro series {series_id} prior pair lacks delta_bps")
                    if (delta_required and unit in ("usd", "usd_bn")
                            and block["prior"] and "chg_pct" not in block):
                        failures.add(f"macro series {series_id} prior pair lacks chg_pct")
                    if ("delta_abs" in block
                            and block["delta_abs"] != round(raw_delta, 3)):
                        failures.add(f"macro series {series_id}.delta_abs arithmetic is invalid")
                    if (unit == "pct" and "delta_bps" in block
                            and block["delta_bps"] != round(raw_delta * 100, 1)):
                        failures.add(f"macro series {series_id}.delta_bps arithmetic is invalid")
                    if (unit in ("usd", "usd_bn")
                            and "chg_pct" in block):
                        expected_chg = (
                            round(raw_delta / block["prior"] * 100, 2)
                            if block["prior"] else None
                        )
                        if (expected_chg is None and block.get("no_new_obs") is True
                                and raw_delta == 0):
                            expected_chg = 0.0
                        if expected_chg is None or block["chg_pct"] != expected_chg:
                            failures.add(f"macro series {series_id}.chg_pct arithmetic is invalid")
                if series_id in trailing_policies and has_prior_date and has_prior_value:
                    expected_note = (
                        "trailing ~7d within the series' own timeline "
                        "(publication lag; not aligned to prior-run date)"
                    )
                    if block.get("delta_note") != expected_note:
                        failures.add(
                            f"macro series {series_id} trailing delta lacks exact delta_note"
                        )
                    if latest_day:
                        observed_prior = strict_date(
                            block.get("prior_date"),
                            f"macro series {series_id} trailing prior_date", failures,
                        )
                        if observed_prior:
                            age = (latest_day - observed_prior).days
                            target = trailing_policies[series_id]
                            if age < target or age > target + 7:
                                failures.add(
                                    f"macro series {series_id} trailing delta window is invalid"
                                )
                elif "delta_note" in block:
                    failures.add(f"macro series {series_id} has an unexpected delta_note")
                yoy_fields = {"yoy_base_date", "yoy_base", "yoy_pct"} & set(block)
                if series_id == "CPIAUCSL" and yoy_fields != {
                        "yoy_base_date", "yoy_base", "yoy_pct"}:
                    failures.add("macro series CPIAUCSL success requires complete YoY fields")
                if series_id != "CPIAUCSL" and yoy_fields:
                    failures.add(
                        f"macro series {series_id} cannot carry CPI YoY fields"
                    )
                if yoy_fields and yoy_fields != {"yoy_base_date", "yoy_base", "yoy_pct"}:
                    failures.add(f"macro series {series_id} has incomplete YoY fields")
                elif yoy_fields:
                    base_day = strict_date(
                        block["yoy_base_date"],
                        f"macro series {series_id} yoy_base_date", failures,
                    )
                    base = block["yoy_base"]
                    if base_day and latest_day:
                        age = (latest_day - base_day).days
                        age_policy = schema.get("yoy_base_age_days", {}).get(series_id)
                        if base_day >= latest_day:
                            failures.add(f"macro series {series_id} YoY base is not earlier")
                        elif age_policy and not (
                                age_policy["min"] <= age <= age_policy["max"]):
                            failures.add(f"macro series {series_id} YoY base age is invalid")
                        elif (age_policy and age_policy.get(
                                "same_month_previous_year") and (
                                base_day.year != latest_day.year - 1
                                or base_day.month != latest_day.month)):
                            failures.add(
                                f"macro series {series_id} YoY base is not the prior-year month"
                            )
                    if (type(base) not in (int, float) or not math.isfinite(base)
                            or base == 0):
                        failures.add(f"macro series {series_id} YoY base is invalid")
                    elif (finite_number(block.get("latest"))
                          and finite_number(block.get("yoy_pct"))
                          and block["yoy_pct"] != round(
                              (block["latest"] / base - 1) * 100, 2)):
                        failures.add(f"macro series {series_id}.yoy_pct arithmetic is invalid")
                if status == "derived":
                    policy = derived_policies.get(series_id)
                    derived_from = block.get("derived_from")
                    if not policy or block.get("source") != policy["source"]:
                        failures.add(f"macro series {series_id} has invalid derived source")
                    if (not isinstance(derived_from, dict) or not policy
                            or set(derived_from) != {policy["left"], policy["right"]}):
                        failures.add(f"macro series {series_id} lacks exact derivation legs")
                    else:
                        legs = []
                        for leg_id in (policy["left"], policy["right"]):
                            leg = derived_from[leg_id]
                            if not isinstance(leg, dict) or set(leg) != {"date", "value"}:
                                failures.add(
                                    f"macro series {series_id} derivation leg {leg_id} is malformed"
                                )
                                legs = []
                                break
                            leg_day = strict_date(
                                leg.get("date"),
                                f"macro series {series_id} derivation leg {leg_id} date",
                                failures,
                            )
                            if not finite_number(leg.get("value")):
                                failures.add(
                                    f"macro series {series_id} derivation leg {leg_id} value is invalid"
                                )
                                legs = []
                                break
                            legs.append((leg_id, leg_day, leg["value"]))
                        if len(legs) == 2:
                            if any(day != latest_day for _leg, day, _value in legs):
                                failures.add(
                                    f"macro series {series_id} derivation dates do not match latest_date"
                                )
                            expected_level = round(legs[0][2] - legs[1][2], 3)
                            if block.get("latest") != expected_level:
                                failures.add(
                                    f"macro series {series_id} derived arithmetic is invalid"
                                )
                            for leg_id, leg_day, leg_value in legs:
                                source_leg = series_data.get(leg_id, {})
                                if not isinstance(source_leg, dict):
                                    source_leg = {}
                                if source_leg.get("status") != "ok":
                                    failures.add(
                                        f"macro series {series_id} derivation leg {leg_id} "
                                        "requires a successful source series"
                                    )
                                if not alignment_proves(
                                        source_leg,
                                        leg_day.isoformat() if leg_day else None,
                                        leg_value):
                                    failures.add(
                                        f"macro series {series_id} derivation leg {leg_id} "
                                        "is absent from source alignment proof"
                                    )
                elif "derived_from" in block:
                    failures.add(f"macro series {series_id} cannot carry derived_from")
    safe_series = {
        key: value for key, value in series_data.items()
        if isinstance(key, str) and isinstance(value, dict)
    }
    for key in schema["required_blocks"]:
        if not isinstance(macro.get(key), dict):
            failures.add(f"macro required block {key} must be an object")
    for key in ("sp500_trend", "move_index", "ofr_repo", "cftc_lev_funds"):
        block = macro.get(key, {})
        if isinstance(block, dict) and block.get("status") not in ("ok", "fetch_failed"):
            failures.add(f"macro block {key} has invalid status")
    block_fields = {
        "sp500_trend": ("latest", "dev200_pct"),
        "cftc_lev_funds": ("net_contracts",),
        "move_index": ("latest",),
        "ofr_repo": ("transaction_volume_usd_bn",),
    }
    block_no_new_specs = {
        "sp500_trend": (
            "latest_date", "prior_spot_date", "latest", "prior_spot", ("chg_pct",)
        ),
        "move_index": (
            "latest_date", "prior_date", "latest", "prior", ("delta_abs",)
        ),
        "ofr_repo": (
            "latest_date", "prior_date", "transaction_volume_usd_bn",
            "prior_transaction_volume_usd_bn", ("chg_pct",)
        ),
    }
    for key, numeric_fields in block_fields.items():
        block = macro.get(key)
        if not isinstance(block, dict):
            continue
        if block.get("status") == "fetch_failed":
            success_fields = {
                "latest_date", "latest", "dev200_pct", "ma200", "ma52w",
                "dev52w_pct", "prior_spot_date", "prior_spot", "chg_pct",
                "no_new_obs", "net_contracts", "recent_weeks", "delta_4w",
                "prior_date", "prior", "delta_abs",
                "transaction_volume_usd_bn",
                "prior_transaction_volume_usd_bn",
                "alignment_observations",
            }
            stale = sorted(success_fields & set(block))
            if stale:
                failures.add(
                    f"macro block {key} fetch_failed retains success fields: {stale}"
                )
            continue
        if block.get("status") != "ok":
            continue
        latest_day = strict_date(
            block.get("latest_date"), f"macro block {key} latest_date", failures
        )
        if generated and latest_day and latest_day > generated.date():
            failures.add(f"macro block {key} latest_date is after generated_at")
        if not isinstance(block.get("source"), str) or not block["source"]:
            failures.add(f"macro block {key} success lacks source")
        for field in numeric_fields:
            value = block.get(field)
            if type(value) not in (int, float) or not math.isfinite(value):
                failures.add(f"macro block {key}.{field} must be finite numeric")
        if (key == "move_index" and finite_number(block.get("latest"))
                and block["latest"] <= 0):
            failures.add("macro block move_index.latest must be positive")
        if (key == "ofr_repo"
                and finite_number(block.get("transaction_volume_usd_bn"))
                and block["transaction_volume_usd_bn"] < 0):
            failures.add("macro block ofr_repo transaction volume must be nonnegative")
        if key == "sp500_trend":
            for field in ("ma200", "dev200_pct"):
                if not finite_number(block.get(field)):
                    failures.add(f"macro block sp500_trend.{field} must be finite numeric")
            if finite_number(block.get("latest")) and block["latest"] <= 0:
                failures.add("macro block sp500_trend.latest must be positive")
            if finite_number(block.get("ma200")) and block["ma200"] <= 0:
                failures.add("macro block sp500_trend.ma200 must be positive")
            if (finite_number(block.get("latest"))
                    and finite_number(block.get("ma200")) and block["ma200"] > 0
                    and finite_number(block.get("dev200_pct"))
                    and block.get("dev200_pct") != round(
                        (block["latest"] - block["ma200"]) / block["ma200"] * 100, 2
                    )):
                failures.add("macro sp500_trend.dev200_pct arithmetic is invalid")
            bounded_proof_pairs(
                block.get("alignment_observations"), "macro sp500_trend",
                failures, latest_day=latest_day, latest_value=block.get("latest"),
            )
            ma52_fields = {"ma52w", "dev52w_pct"} & set(block)
            if ma52_fields and ma52_fields != {"ma52w", "dev52w_pct"}:
                failures.add("macro sp500_trend 52-week fields are incomplete")
            elif ma52_fields:
                if not finite_number(block.get("ma52w")) or block["ma52w"] <= 0:
                    failures.add("macro sp500_trend.ma52w must be positive finite numeric")
                elif (not finite_number(block.get("dev52w_pct"))
                      or not finite_number(block.get("latest"))
                      or block["dev52w_pct"] != round(
                          (block["latest"] - block["ma52w"]) / block["ma52w"] * 100, 2)):
                    failures.add("macro sp500_trend.dev52w_pct arithmetic is invalid")
            if "prior_spot" in block or "prior_spot_date" in block:
                if not {"prior_spot", "prior_spot_date"} <= set(block):
                    failures.add("macro sp500_trend prior fields are incomplete")
                else:
                    observed_prior = strict_date(
                        block["prior_spot_date"],
                        "macro sp500_trend prior_spot_date", failures,
                    )
                    if observed_prior and latest_day and observed_prior > latest_day:
                        failures.add("macro sp500_trend prior_spot_date is after latest_date")
                    if observed_prior and prior_day and observed_prior > prior_day:
                        failures.add("macro sp500_trend prior_spot_date is after prior_run_date")
                    if (not finite_number(block["prior_spot"])
                            or block["prior_spot"] <= 0):
                        failures.add("macro sp500_trend prior_spot must be positive finite numeric")
                    elif "chg_pct" not in block:
                        failures.add("macro sp500_trend prior pair lacks chg_pct")
                    elif (finite_number(block.get("latest"))
                          and finite_number(block.get("chg_pct"))):
                        expected = round(
                            (block["latest"] - block["prior_spot"])
                            / block["prior_spot"] * 100, 2
                        )
                        if block["chg_pct"] != expected:
                            failures.add("macro sp500_trend.chg_pct arithmetic is invalid")
        elif key == "move_index" and ({"prior", "prior_date", "delta_abs"} & set(block)):
            if not {"prior", "prior_date", "delta_abs"} <= set(block):
                failures.add("macro move_index delta requires prior fields")
            else:
                observed_prior = strict_date(
                    block.get("prior_date"), "macro move_index prior_date", failures
                )
                if observed_prior and latest_day and observed_prior > latest_day:
                    failures.add("macro move_index prior_date is after latest_date")
                if observed_prior and prior_day and observed_prior > prior_day:
                    failures.add("macro move_index prior_date is after prior_run_date")
                if (not finite_number(block.get("prior"))
                        or block.get("prior") <= 0):
                    failures.add("macro move_index.prior must be positive finite numeric")
                if (finite_number(block.get("latest"))
                        and finite_number(block.get("prior"))
                        and finite_number(block.get("delta_abs"))
                        and block["delta_abs"] != round(
                            block["latest"] - block["prior"], 2)):
                    failures.add("macro move_index.delta_abs arithmetic is invalid")
        elif key == "ofr_repo" and (
                {"chg_pct", "prior_transaction_volume_usd_bn", "prior_date"} & set(block)):
            required_prior = {"prior_transaction_volume_usd_bn", "prior_date"}
            if not required_prior <= set(block):
                failures.add("macro ofr_repo change requires prior fields")
            else:
                prior_value = block["prior_transaction_volume_usd_bn"]
                observed_prior = strict_date(
                    block.get("prior_date"), "macro ofr_repo prior_date", failures
                )
                if observed_prior and latest_day and observed_prior > latest_day:
                    failures.add("macro ofr_repo prior_date is after latest_date")
                if observed_prior and prior_day and observed_prior > prior_day:
                    failures.add("macro ofr_repo prior_date is after prior_run_date")
                if not finite_number(prior_value) or prior_value < 0:
                    failures.add(
                        "macro ofr_repo prior_transaction_volume_usd_bn must be nonnegative finite numeric"
                    )
                if "chg_pct" not in block and finite_number(prior_value) and prior_value:
                    failures.add("macro ofr_repo prior pair lacks chg_pct")
                expected = (
                    round((block["transaction_volume_usd_bn"] - prior_value)
                          / prior_value * 100, 2)
                    if (finite_number(prior_value) and prior_value
                        and finite_number(block.get("transaction_volume_usd_bn")))
                    else None
                )
                if (expected is None and block.get("no_new_obs") is True
                        and prior_value == block.get("transaction_volume_usd_bn") == 0):
                    expected = 0.0
                if "chg_pct" in block and (expected is None or block["chg_pct"] != expected):
                    failures.add("macro ofr_repo.chg_pct arithmetic is invalid")
        no_new_spec = block_no_new_specs.get(key)
        if no_new_spec:
            (latest_date_field, prior_date_field, latest_value_field,
             prior_value_field, delta_fields) = no_new_spec
            for field in delta_fields:
                if field in block and not finite_number(block[field]):
                    failures.add(f"macro {key}.{field} must be finite numeric")
            validate_no_new_obs_pair(
                block, f"macro {key}",
                latest_date_field=latest_date_field,
                prior_date_field=prior_date_field,
                latest_value_field=latest_value_field,
                prior_value_field=prior_value_field,
                delta_fields=delta_fields,
                pair_present=(
                    prior_date_field in block and prior_value_field in block
                ),
                require_marker_on_same_date=True,
                failures=failures,
            )
    repo = macro.get("repo_stress", {})
    if isinstance(repo, dict) and repo.get("status") not in (
            "ok", "partial", "unavailable"):
        failures.add("macro repo_stress has invalid status")
    if isinstance(repo, dict) and repo.get("status") in (
            "ok", "partial", "unavailable"):
        for field in (
            "sofr", "iorb", "sofr_iorb_bps", "sofr99", "sofr99_iorb",
            "sofr99_iorb_bps",
            "srf_usage_bn",
        ):
            value = repo.get(field)
            if value is not None and (
                    type(value) not in (int, float) or not math.isfinite(value)):
                failures.add(f"macro repo_stress.{field} must be finite numeric")
        parsed_repo_dates = {}
        for field in (
            "as_of", "iorb_date", "sofr99_date", "sofr99_iorb_date", "srf_date"
        ):
            if field in repo:
                parsed_repo_dates[field] = strict_date(
                    repo[field], f"macro repo_stress.{field}", failures
                )
                if (generated and parsed_repo_dates[field]
                        and parsed_repo_dates[field] > generated.date()):
                    failures.add(f"macro repo_stress.{field} is after generated_at")
        has_spread = finite_number(repo.get("sofr_iorb_bps"))
        has_srf = finite_number(repo.get("srf_usage_bn"))
        expected_repo_status = (
            "ok" if has_spread and has_srf
            else "partial" if has_spread or has_srf
            else "unavailable"
        )
        if repo.get("status") != expected_repo_status:
            failures.add(
                f"macro repo_stress status {repo.get('status')!r} != fields-derived "
                f"{expected_repo_status!r}"
            )
        primary_fields = {"as_of", "sofr", "iorb", "iorb_date", "sofr_iorb_bps"}
        present_primary = primary_fields & set(repo)
        if has_spread and not primary_fields <= set(repo):
            failures.add("macro repo_stress spread lacks complete dated legs")
        if not has_spread and present_primary:
            failures.add("macro repo_stress has orphaned primary spread fields")
        if has_spread and (
                not finite_number(repo.get("sofr"))
                or not finite_number(repo.get("iorb"))):
            failures.add("macro repo_stress spread requires finite numeric sofr and iorb legs")
        elif has_spread and repo["sofr_iorb_bps"] != round(
                (repo["sofr"] - repo["iorb"]) * 100, 1):
            failures.add("macro repo_stress spread arithmetic is invalid")
        secondary_fields = {
            "sofr99", "sofr99_date", "sofr99_iorb", "sofr99_iorb_date",
            "sofr99_iorb_bps",
        }
        present_secondary = secondary_fields & set(repo)
        if present_secondary and present_secondary != secondary_fields:
            failures.add("macro repo_stress SOFR99 spread has incomplete dated legs")
        if present_secondary and not has_spread:
            failures.add("macro repo_stress SOFR99 spread requires the primary spread")
        if present_secondary == secondary_fields:
            if (not finite_number(repo.get("sofr99"))
                    or not finite_number(repo.get("sofr99_iorb"))
                    or not finite_number(repo.get("sofr99_iorb_bps"))):
                failures.add("macro repo_stress SOFR99 legs must be finite numeric")
            elif repo["sofr99_iorb_bps"] != round(
                    (repo["sofr99"] - repo["sofr99_iorb"]) * 100, 1):
                failures.add("macro repo_stress SOFR99 spread arithmetic is invalid")
        if has_srf and "srf_date" not in repo:
            failures.add("macro repo_stress SRF value lacks srf_date")
        if not has_srf and ("srf_usage_bn" in repo or "srf_date" in repo):
            failures.add("macro repo_stress has orphaned SRF fields")
        if repo.get("status") == "unavailable" and set(repo) != {"status"}:
            failures.add("unavailable macro repo_stress must not retain leg fields")
        sofr_series = safe_series.get("SOFR", {})
        iorb_series = safe_series.get("IORB", {})
        if has_spread:
            if sofr_series.get("status") != "ok" or iorb_series.get("status") != "ok":
                failures.add("macro repo_stress spread requires successful SOFR and IORB")
            if repo.get("as_of") != sofr_series.get("latest_date"):
                failures.add("macro repo_stress as_of != SOFR latest_date")
            if repo.get("sofr") != sofr_series.get("latest"):
                failures.add("macro repo_stress SOFR leg != SOFR latest")
            as_of_day = parsed_repo_dates.get("as_of")
            iorb_day = parsed_repo_dates.get("iorb_date")
            iorb_latest_day = strict_date(
                iorb_series.get("latest_date"), "macro series IORB latest_date", failures
            )
            if as_of_day and iorb_day and iorb_day > as_of_day:
                failures.add("macro repo_stress IORB date is after SOFR as_of")
            if iorb_latest_day and iorb_day and iorb_day > iorb_latest_day:
                failures.add("macro repo_stress IORB date is after IORB latest_date")
            if not alignment_proves(
                    iorb_series, repo.get("iorb_date"), repo.get("iorb")):
                failures.add("macro repo_stress IORB leg lacks source alignment proof")
        if present_secondary == secondary_fields:
            sofr99_series = safe_series.get("SOFR99", {})
            if sofr99_series.get("status") != "ok" or iorb_series.get("status") != "ok":
                failures.add("macro repo_stress SOFR99 spread requires successful source series")
            as_of_day = parsed_repo_dates.get("as_of")
            sofr99_day = parsed_repo_dates.get("sofr99_date")
            iorb99_day = parsed_repo_dates.get("sofr99_iorb_date")
            sofr99_latest_day = strict_date(
                sofr99_series.get("latest_date"),
                "macro series SOFR99 latest_date", failures,
            )
            iorb_latest_day = strict_date(
                iorb_series.get("latest_date"), "macro series IORB latest_date", failures
            )
            if as_of_day and sofr99_day and sofr99_day > as_of_day:
                failures.add("macro repo_stress SOFR99 date is after as_of")
            if sofr99_latest_day and sofr99_day and sofr99_day > sofr99_latest_day:
                failures.add("macro repo_stress SOFR99 date is after series latest_date")
            if iorb99_day and sofr99_day and iorb99_day > sofr99_day:
                failures.add("macro repo_stress SOFR99 IORB date is after SOFR99 date")
            if iorb_latest_day and iorb99_day and iorb99_day > iorb_latest_day:
                failures.add("macro repo_stress SOFR99 IORB date is after IORB latest_date")
            if not alignment_proves(
                    sofr99_series, repo.get("sofr99_date"), repo.get("sofr99")):
                failures.add("macro repo_stress SOFR99 leg lacks source alignment proof")
            if not alignment_proves(
                    iorb_series, repo.get("sofr99_iorb_date"),
                    repo.get("sofr99_iorb")):
                failures.add(
                    "macro repo_stress SOFR99 IORB leg lacks source alignment proof"
                )
        srf_series = safe_series.get("RPONTTLD", {})
        if has_srf:
            if srf_series.get("status") != "ok":
                failures.add("macro repo_stress SRF leg requires successful RPONTTLD")
            elif repo["srf_usage_bn"] != srf_series.get("latest"):
                failures.add("macro repo_stress SRF value != RPONTTLD latest")
            if repo.get("srf_date") != srf_series.get("latest_date"):
                failures.add("macro repo_stress SRF date != RPONTTLD latest_date")
    comove_block = macro.get("vix_spx_comove", {})
    if isinstance(comove_block, dict):
        comove_leg_fields = {
            "as_of", "base_date", "window_days", "vix", "vix_base",
            "vix_chg_pct", "sp500", "sp500_base", "sp500_chg_pct",
        }
        status = comove_block.get("status")
        if status not in ("ok", "unavailable"):
            failures.add("macro vix_spx_comove has invalid status")
        if type(comove_block.get("comove")) is not bool:
            failures.add("macro vix_spx_comove.comove must be boolean")
        extra = sorted(
            set(comove_block) - comove_leg_fields - {"status", "comove", "note"}
        )
        if extra:
            failures.add(f"macro vix_spx_comove has unexpected fields: {extra}")
        expected_legs = expected_comove_legs(macro, contract)
        if expected_legs is None:
            if status == "ok":
                failures.add(
                    "macro vix_spx_comove claims a verdict without a "
                    "reproducible shared trailing window"
                )
            if comove_block.get("comove") is not False:
                failures.add(
                    "macro vix_spx_comove without a verdict must report comove false"
                )
            retained = sorted(comove_leg_fields & set(comove_block))
            if retained:
                failures.add(
                    f"macro vix_spx_comove unavailable retains leg fields: {retained}"
                )
        elif status == "unavailable":
            failures.add(
                "macro vix_spx_comove is unavailable although its window is "
                "reproducible from the emitted proofs"
            )
        else:
            for field, expected_value in expected_legs.items():
                if comove_block.get(field) != expected_value:
                    failures.add(
                        f"macro vix_spx_comove.{field} "
                        f"{comove_block.get(field)!r} != recomputed "
                        f"{expected_value!r}"
                    )
            as_of_day = strict_date(
                comove_block.get("as_of"), "macro vix_spx_comove.as_of", failures
            )
            if generated and as_of_day and as_of_day > generated.date():
                failures.add("macro vix_spx_comove.as_of is after generated_at")
    decomposition = macro.get("decomposition", {})
    if isinstance(decomposition, dict):
        driver = decomposition.get("driver")
        status = decomposition.get("status")
        allowed_statuses = {
            "ok", "baseline_no_prior", "unavailable_no_daily_history"
        }
        allowed_drivers = {"none", "unknown", "real-rate", "breakeven", "mixed"}
        if not isinstance(status, str) or status not in allowed_statuses:
            failures.add("macro decomposition has invalid status")
        if status == "baseline_no_prior":
            if driver != "baseline":
                failures.add("baseline macro decomposition driver must be baseline")
            if decomposition.get("freshness") != "not_applicable":
                failures.add("baseline macro decomposition freshness must be not_applicable")
            if decomposition.get("stale_series") != []:
                failures.add("baseline macro decomposition stale_series must be empty")
        elif status == "unavailable_no_daily_history":
            if driver is not None:
                failures.add("unavailable decomposition must not claim a driver")
        elif status == "ok" and (
                not isinstance(driver, str) or driver not in allowed_drivers):
            failures.add("ok macro decomposition has invalid driver")
        if decomposition.get("freshness") not in (
                "updated", "partial_stale", "all_stale", "not_applicable"):
            failures.add("macro decomposition has invalid freshness")
        stale_series = decomposition.get("stale_series")
        if not isinstance(stale_series, list):
            failures.add("macro decomposition stale_series must be an array")
        elif (not all(isinstance(item, str) for item in stale_series)
              or len(stale_series) != len(set(stale_series))
              or not set(stale_series) <= {"DGS10", "DFII10", "T10YIE"}):
            failures.add("macro decomposition stale_series is invalid")
        for field in ("d_dgs10_bps", "d_dfii10_bps", "d_t10yie_bps"):
            value = decomposition.get(field)
            if value is not None and (
                    type(value) not in (int, float) or not math.isfinite(value)):
                failures.add(f"macro decomposition {field} must be finite numeric/null")
        deltas = {
            "DGS10": safe_series.get("DGS10", {}).get("delta_bps"),
            "DFII10": safe_series.get("DFII10", {}).get("delta_bps"),
            "T10YIE": safe_series.get("T10YIE", {}).get("delta_bps"),
        }
        emitted = {
            "DGS10": decomposition.get("d_dgs10_bps"),
            "DFII10": decomposition.get("d_dfii10_bps"),
            "T10YIE": decomposition.get("d_t10yie_bps"),
        }
        if status != "baseline_no_prior":
            for key in ("DGS10", "DFII10"):
                if emitted[key] != deltas[key]:
                    failures.add(f"macro decomposition {key} delta != series delta_bps")
            if deltas["T10YIE"] is not None and emitted["T10YIE"] != deltas["T10YIE"]:
                failures.add("macro decomposition T10YIE delta != series delta_bps")
        if status == "baseline_no_prior" and any(
                value is not None for value in emitted.values()):
            failures.add("baseline macro decomposition deltas must all be null")
        if status == "ok" and (
                emitted["DGS10"] is None or emitted["DFII10"] is None):
            failures.add("ok macro decomposition requires DGS10 and DFII10 deltas")
        if status == "unavailable_no_daily_history" and (
                emitted["DGS10"] is not None and emitted["DFII10"] is not None):
            failures.add("unavailable decomposition has both required daily deltas")
        series = safe_series
        delta_bearing = [key for key, value in deltas.items() if value is not None]
        expected_stale = [
            key for key in delta_bearing if series.get(key, {}).get("no_new_obs") is True
        ]
        expected_freshness = (
            "all_stale" if delta_bearing and len(expected_stale) == len(delta_bearing)
            else "partial_stale" if expected_stale
            else "updated"
        )
        if status in ("ok", "unavailable_no_daily_history"):
            if decomposition.get("freshness") != expected_freshness:
                failures.add("macro decomposition freshness does not match series observations")
            if stale_series != expected_stale:
                failures.add("macro decomposition stale_series does not match series observations")
        if status == "unavailable_no_daily_history":
            if emitted["T10YIE"] != deltas["T10YIE"]:
                failures.add("unavailable decomposition T10YIE delta != series delta_bps")
        if status == "ok" and all(
                finite_number(emitted[key]) for key in ("DGS10", "DFII10")):
            nominal = series.get("DGS10", {})
            real = series.get("DFII10", {})
            breakeven = series.get("T10YIE", {})
            w_nominal = (nominal.get("latest_date"), nominal.get("prior_date"))
            w_real = (real.get("latest_date"), real.get("prior_date"))
            w_breakeven = (
                breakeven.get("latest_date"), breakeven.get("prior_date")
            )
            rebuilt = False
            expected_t = deltas["T10YIE"]
            if expected_t is None and w_nominal == w_real:
                expected_t = round(emitted["DGS10"] - emitted["DFII10"], 1)
                rebuilt = True
            if emitted["T10YIE"] != expected_t:
                failures.add("macro decomposition T10YIE identity/rebuild is invalid")
            if expected_t is None or not finite_number(expected_t):
                expected_driver = "unknown"
            elif (emitted["DGS10"] == 0 and emitted["DFII10"] == 0
                  and expected_t == 0):
                expected_driver = "none"
            elif (not rebuilt and w_nominal == w_real == w_breakeven
                  and abs(emitted["DGS10"] - emitted["DFII10"] - expected_t)
                  > contract["calibration"]["decomposition_identity_tolerance_bps"]):
                expected_driver = "unknown"
            elif not rebuilt and not w_nominal == w_real == w_breakeven:
                expected_driver = "unknown"
            elif abs(expected_t) > abs(emitted["DFII10"]):
                expected_driver = "breakeven"
            elif abs(emitted["DFII10"]) > abs(expected_t):
                expected_driver = "real-rate"
            else:
                expected_driver = "mixed"
            if driver != expected_driver:
                failures.add(
                    f"macro decomposition driver {driver!r} != {expected_driver!r}"
                )
    validate_ndx_drawdown(macro, contract, generated, failures)
    return len(failures.items) == failure_count


def prompt_source_bullets(prompt, failures):
    # Prompt syntax is richer than archived-report syntax, so use a dedicated
    # visibility scan: ignore fenced/indented code, and fail closed on comment
    # or raw-HTML attempts that could hide a source bullet from rendering.
    if "<!--" in prompt or "-->" in prompt:
        failures.add("prompt HTML comments are forbidden in source mapping")
    visible = []
    fence = None
    for index, line in enumerate(prompt.splitlines()):
        match = MarkdownDocument.FENCE_RE.match(line)
        if (match and match.group(2).startswith("`")
                and "`" in match.group(3)):
            match = None
        if fence:
            if re.fullmatch(
                    r" {0,3}" + re.escape(fence[0]) + r"{%d,}\s*" % fence[1],
                    line):
                fence = None
            continue
        if match:
            token = match.group(2)
            fence = (token[0], len(token))
            continue
        if line.startswith("\t") or line.startswith("    "):
            continue
        without_code = re.sub(r"`[^`]*`", "", line)
        if (MarkdownDocument.RAW_HTML_RE.search(without_code)
                or MarkdownDocument.RAW_HTML_DECL_RE.search(without_code)
                or MarkdownDocument.RAW_HTML_BLOCK_START_RE.search(without_code)):
            failures.add(f"prompt raw HTML is forbidden (line {index + 1})")
            continue
        visible.append((index, line))
    if fence:
        failures.add("prompt contains an unclosed code fence")
    starts = [item for item in visible if item[1].startswith("# Data sources")]
    ends = [item for item in visible if item[1] == "# Output structure"]
    if len(starts) != 1 or len(ends) != 1 or starts[0][0] >= ends[0][0]:
        failures.add("prompt must contain exactly one top-level Data sources section")
        return []
    start, end = starts[0][0], ends[0][0]
    return [
        line[2:] for index, line in visible
        if start < index < end and line.startswith("- ")
    ]


def validate_prompt_mapping(prompt, contract, failures):
    bullets = prompt_source_bullets(prompt, failures)
    sources = contract["sources"]
    if len(bullets) != len(sources):
        failures.add(f"prompt source bullet count {len(bullets)} != contract {len(sources)}")
        return
    for index, (bullet, source) in enumerate(zip(bullets, sources), 1):
        match = source["prompt_match"]
        if match not in bullet:
            failures.add(
                f"prompt source {index} does not match {source['id']}: missing {match!r}"
            )
        matched_indices = [i for i, candidate in enumerate(bullets) if match in candidate]
        if matched_indices != [index - 1]:
            failures.add(
                f"contract prompt_match for {source['id']} is not one-to-one: {matched_indices}"
            )




DISPLAY_NUMBER_RE = re.compile(r"[+−-]?\d[\d,]*(?:\.\d+)?")


def extract_display_number(text, last=False):
    """Return (value, rounding tolerance) from a rendered number.

    Tolerance follows the displayed precision, so prompt-sanctioned values
    such as 7,575 and 69.6 can be checked against exact macro JSON without
    forcing false precision into the report.
    """
    matches = list(DISPLAY_NUMBER_RE.finditer(text))
    if not matches:
        return None, None
    token = matches[-1 if last else 0].group().replace(",", "").replace("−", "-")
    decimals = len(token.rsplit(".", 1)[1]) if "." in token else 0
    try:
        return float(token), 0.5 * (10 ** -decimals) + 1e-9
    except ValueError:
        return None, None




def displayed_matches(text, expected, last=False):
    if type(expected) not in (int, float) or not math.isfinite(expected):
        return False
    value, tolerance = extract_display_number(text, last=last)
    return value is not None and abs(value - expected) <= tolerance




def status_token(cell, contract, where, failures):
    hits = [token for token in contract["coverage_statuses"] if token in cell]
    if len(hits) != 1 or not cell.startswith(hits[0]):
        failures.add(f"{where} must start with exactly one allowed status token: {cell!r}")
        return None
    return hits[0]


def parse_iso_timestamp(value):
    if not isinstance(value, str) or "T" not in value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None
    return parsed if parsed.tzinfo is not None else None


def validate_retrieval_timestamp(value, report_day, where, failures):
    parsed = parse_iso_timestamp(value)
    if parsed is None:
        failures.add(f"{where} is not timezone-aware ISO-8601")
        return None
    if parsed.utcoffset() != timedelta(hours=8):
        failures.add(f"{where} must use the Asia/Taipei UTC+08:00 offset")
    if report_day and parsed.date() != report_day:
        failures.add(f"{where} must fall on the report date in Asia/Taipei")
    return parsed


def evidence_window(source, indicator, failures):
    window = source["window"]
    if window != "composite":
        return window
    match = re.match(r"^\[([a-z0-9_]+)\]", indicator)
    components = {item["id"]: item["window"] for item in source["window_components"]}
    if not match or match.group(1) not in components:
        failures.add(
            f"composite source {source['id']} evidence indicator must start with "
            f"one of {sorted(components)}"
        )
        return None
    return components[match.group(1)]


def validate_evidence_date(value, source, indicator, report_day, where, failures):
    data_day = strict_date(value, where, failures)
    if not data_day or not report_day:
        return data_day
    if data_day > report_day:
        failures.add(f"{where} is in the future")
    if source.get("same_quarter") and (
            data_day.year, (data_day.month - 1) // 3
    ) != (
            report_day.year, (report_day.month - 1) // 3
    ):
        failures.add(f"{where} must be in the report's calendar quarter")
    window = evidence_window(source, indicator, failures)
    if window in ("7d", "14d", "30d", "90d"):
        days = int(window[:-1])
        if data_day < report_day - timedelta(days=days):
            failures.add(f"{where} is outside {window} window")
    return data_day


def macro_component(macro, component):
    if component["kind"] == "series":
        return macro.get("series", {}).get(component["key"], {})
    return macro.get(component["key"], {})


def mentions_identifier(text, identifier):
    """Match a machine identifier without accepting a longer identifier."""
    if not isinstance(text, str) or not isinstance(identifier, str):
        return False
    return re.search(
        r"(?<![A-Za-z0-9_.^-])" + re.escape(identifier)
        + r"(?![A-Za-z0-9_.^-])",
        text,
    ) is not None


def macro_component_evidence_fields(component, block):
    """Return ``(primary_field, field -> (value, data_date))`` for Raw rows."""
    if component["kind"] == "series":
        primary = component.get("value_field", "latest")
        date_fields = {
            "latest": "latest_date", "prior": "prior_date",
            "delta_bps": "latest_date", "chg_pct": "latest_date",
            "delta_abs": "latest_date", "yoy_base": "yoy_base_date",
            "yoy_pct": "latest_date",
        }
    elif component["key"] == "sp500_trend":
        primary = "latest"
        date_fields = {
            "latest": "latest_date", "ma200": "latest_date",
            "dev200_pct": "latest_date", "ma52w": "latest_date",
            "dev52w_pct": "latest_date", "prior_spot": "prior_spot_date",
            "chg_pct": "latest_date",
        }
    elif component["key"] == "cftc_lev_funds":
        primary = "net_contracts"
        date_fields = {
            "net_contracts": "latest_date", "delta_4w": "latest_date",
        }
    elif component["key"] == "move_index":
        primary = "latest"
        date_fields = {
            "latest": "latest_date", "prior": "prior_date",
            "delta_abs": "latest_date",
        }
    elif component["key"] == "ofr_repo":
        primary = "transaction_volume_usd_bn"
        date_fields = {
            "transaction_volume_usd_bn": "latest_date",
            "prior_transaction_volume_usd_bn": "prior_date",
            "chg_pct": "latest_date",
        }
    elif component["key"] == "ndx_drawdown":
        primary = "latest"
        date_fields = {
            "latest": "latest_date", "high": "high_date",
            "drawdown_pct": "latest_date", "r1_threshold_level": "latest_date",
        }
    elif component["key"] == "vix_spx_comove":
        primary = "vix"
        date_fields = {
            "vix": "as_of", "vix_base": "base_date", "vix_chg_pct": "as_of",
            "sp500": "as_of", "sp500_base": "base_date",
            "sp500_chg_pct": "as_of", "window_days": "as_of",
        }
    else:
        return None, {}
    fields = {
        field: (block.get(field), block.get(date_field))
        for field, date_field in date_fields.items()
        if finite_number(block.get(field)) and isinstance(block.get(date_field), str)
    }
    return primary, fields


# Heading roles.  The contract owns the heading text and count; these indexes
# only name which contract heading plays which role.
H_CONCLUSION, H_RESOLUTION, H_PATHS = 0, 1, 2
H_COMPARISON, H_GAPS, H_APPENDIX, H_ARCHIVE = 5, 6, 7, 8
DRY_RUN_BANNER = "> [DRY RUN] this report was not committed to archive."
PATH_TAGS = ("[R1]", "[R2]", "[R3]", "[整體]")


def json_equal(left, right):
    """JSON equality that never conflates booleans with numbers."""
    if isinstance(left, bool) or isinstance(right, bool):
        return type(left) is type(right) and left == right
    if isinstance(left, dict) and isinstance(right, dict):
        return set(left) == set(right) and all(
            json_equal(left[key], right[key]) for key in left)
    if isinstance(left, list) and isinstance(right, list):
        return len(left) == len(right) and all(
            json_equal(a, b) for a, b in zip(left, right))
    if type(left) in (int, float) and type(right) in (int, float):
        return left == right
    return type(left) is type(right) and left == right


def section_text(doc, heading):
    return "\n".join(line for _, line in doc.section_lines(heading))


def validate_headings_and_fence(doc, contract, failures):
    h1 = [h for h in doc.headings if h[1] == 1]
    if len(h1) != 1:
        failures.add(f"report must contain exactly one visible H1; found {len(h1)}")
    actual_h2 = [h[3] for h in doc.headings if h[1] == 2]
    if actual_h2 != contract["headings"]:
        failures.add(f"visible H2 headings/order mismatch: {actual_h2}")
        return None
    headings = contract["headings"]
    paths_start = next(h[0] for h in doc.headings if h[3] == headings[H_PATHS])
    paths_end = next(
        (h[0] for h in doc.headings if h[1] == 2 and h[0] > paths_start),
        len(doc.lines),
    )
    path_h3 = [h[3] for h in doc.headings
               if h[1] == 3 and paths_start < h[0] < paths_end]
    expected_paths = [p["heading"] for p in contract["resolution"]["paths"]]
    if path_h3 != expected_paths:
        failures.add(f"path H3 headings/order mismatch: {path_h3}")
    appendix_start = next(h[0] for h in doc.headings if h[3] == headings[H_APPENDIX])
    appendix_end = next(h[0] for h in doc.headings if h[3] == headings[H_ARCHIVE])
    appendix_h3 = [h[3] for h in doc.headings
                   if h[1] == 3 and appendix_start < h[0] < appendix_end]
    stray_h3 = [h[3] for h in doc.headings
                if h[1] == 3 and not paths_start < h[0] < paths_end
                and not appendix_start < h[0] < appendix_end]
    if stray_h3:
        failures.add(f"H3 headings outside 三條路徑現況/數據附錄 are not allowed: {stray_h3}")
    if appendix_h3 != contract["appendix_headings"]:
        failures.add("appendix H3 headings/order must be Raw data, Coverage, traceability")
    if len(doc.fences) != 1:
        failures.add(f"report must contain exactly one code fence; found {len(doc.fences)}")
        return None
    fence = doc.fences[0]
    if fence["char"] != "`" or fence["info"] != "json":
        failures.add("the only code fence must be labelled exactly `json`")
    if fence["section"] != headings[H_ARCHIVE]:
        failures.add(f"forecast JSON fence is outside `{headings[H_ARCHIVE]}`")
    return parse_json_text(fence["content"], "forecast JSON fence", failures)


def validate_title_and_meta(doc, forecast, dry_run, contract, failures):
    """Banner, title and meta line; returns the report date."""
    nonempty = doc.visible_nonempty()
    has_banner = bool(nonempty and nonempty[0][1] == DRY_RUN_BANNER)
    if dry_run and not has_banner:
        failures.add("dry-run report must begin with the locked DRY RUN banner")
    if not dry_run and has_banner:
        failures.add("production report must not contain the DRY RUN banner")
    if has_banner:
        nonempty = nonempty[1:]
    first_h2_line = min((h[0] for h in doc.headings if h[1] == 2), default=len(doc.lines))
    prefix = [(i, line) for i, line in nonempty if i < first_h2_line]
    if len(prefix) != 2:
        failures.add("title area must contain exactly the H1 title and the meta line")
        return None
    title_match = re.fullmatch(f"# ({DATE_RE}) AI 泡沫破裂預測報告", prefix[0][1])
    if not title_match:
        failures.add("report title must be `# YYYY-MM-DD AI 泡沫破裂預測報告`")
        return None
    report_day = strict_date(title_match.group(1), "report title date", failures)
    meta_match = re.fullmatch(
        f"報告日期：({DATE_RE})｜ISO 週次：(\\d{{4}}-W\\d{{2}})"
        f"｜預測窗口：({DATE_RE}) → ({DATE_RE})｜前次基準：(.+)",
        prefix[1][1],
    )
    if not meta_match:
        failures.add("meta line format is invalid")
        return report_day
    if report_day is None:
        return None
    if meta_match.group(1) != title_match.group(1):
        failures.add("meta report date must match title date")
    iso = report_day.isocalendar()
    if meta_match.group(2) != f"{iso.year}-W{iso.week:02d}":
        failures.add(f"meta ISO week {meta_match.group(2)} is incorrect")
    horizon_end = (
        report_day + timedelta(days=contract["question"]["horizon_days"])
    ).isoformat()
    if (meta_match.group(3), meta_match.group(4)) != (
            report_day.isoformat(), horizon_end):
        failures.add(f"meta 預測窗口 must be {report_day.isoformat()} → {horizon_end}")
    prior_meta = meta_match.group(5)
    prior_date = forecast.get("prior_date") if isinstance(forecast, dict) else None
    if prior_date is None:
        if prior_meta != "無（基準）":
            failures.add("baseline meta must say `前次基準：無（基準）`")
    else:
        prior_day = None
        if isinstance(prior_date, str) and re.fullmatch(DATE_RE, prior_date):
            try:
                prior_day = date.fromisoformat(prior_date)
            except ValueError:
                prior_day = None
        if prior_day is None:
            return report_day
        expected = f"report-{prior_date}（{(report_day - prior_day).days}天前）"
        if prior_meta != expected:
            failures.add(f"meta prior reference must be `{expected}`")
    return report_day


def validate_conclusion(doc, forecast, contract, failures):
    heading = contract["headings"][H_CONCLUSION]
    lines = [line.strip() for _, line in doc.section_lines(heading) if line.strip()]
    literals = contract["conclusion_line"]
    answer = forecast.get("answer")
    if not lines:
        failures.add("conclusion section is empty")
        return
    if lines[0] not in literals.values():
        failures.add(f"first conclusion line must be one of {sorted(literals.values())}")
    elif answer in literals and lines[0] != literals[answer]:
        failures.add("conclusion line does not match forecast answer")
    for line in lines[1:]:
        if any(literal in line for literal in literals.values()):
            failures.add(f"conclusion section repeats a conclusion line: {line[:60]}")


def validate_resolution_section(doc, contract, failures):
    heading = contract["headings"][H_RESOLUTION]
    lines = [line for _, line in doc.section_lines(heading)]
    block = contract["resolution"]["block"].split("\n")
    starts = [
        i for i in range(len(lines) - len(block) + 1)
        if [line.rstrip() for line in lines[i:i + len(block)]]
        == [line.rstrip() for line in block]
    ]
    if len(starts) != 1:
        failures.add("resolution section must contain the contract resolution block verbatim exactly once")
        return
    before = [line for line in lines[:starts[0]] if line.strip()]
    rest = [line.strip() for line in lines[starts[0] + len(block):] if line.strip()]
    version_line = f"解析版本：v{contract['resolution']['version']}"
    if not rest or rest[0] != version_line:
        failures.add(f"resolution block must be followed by the line `{version_line}`")
    elif before or len(rest) != 1:
        failures.add(
            "resolution section must contain only the contract block and the "
            f"`{version_line}` line"
        )


NDX_CLAIM_RE = re.compile(
    r"距\s*52\s*週高點回撤[^0-9%\n\-−]{0,4}?([-−]?\s*[0-9]+(?:\.[0-9]+)?)\s*%"
)


def validate_paths_section(doc, macro, contract, failures):
    parent = contract["headings"][H_PATHS]
    ndx = macro.get("ndx_drawdown", {})
    for path in contract["resolution"]["paths"]:
        lines = doc.subsection_lines(path["heading"], parent)
        if not lines:
            failures.add(f"path section {path['heading']} is missing or empty")
            continue
        text = "\n".join(line for _, line in lines)
        if not any(line.strip().startswith("**判讀：**") for _, line in lines):
            failures.add(f"path section {path['heading']} lacks a `**判讀：**` line")
        if path["id"] != "R1":
            continue
        if ndx.get("status") == "ok":
            expected = f"距 52 週高點回撤 {ndx['drawdown_pct']:.2f}%"
            if expected not in text:
                failures.add(f"R1 section must state `{expected}` from the macro artifact")
        elif "R1 回撤不可用" not in text:
            failures.add("R1 section must state `R1 回撤不可用` when ndx_drawdown failed")
    for heading in contract["headings"]:
        for match in NDX_CLAIM_RE.finditer(section_text(doc, heading)):
            claimed = float(re.sub(r"\s", "", match.group(1)).replace("−", "-"))
            if ndx.get("status") != "ok":
                failures.add(
                    f"{heading} states a NASDAQ-100 drawdown `{match.group(0)}` "
                    "although ndx_drawdown failed"
                )
            elif round(claimed, 2) != ndx["drawdown_pct"]:
                failures.add(
                    f"{heading} drawdown claim `{match.group(0)}` != artifact "
                    f"drawdown_pct {ndx['drawdown_pct']:.2f}"
                )


def top_level_bullets(lines):
    """Split a section into top-level list items plus any stray prose lines.

    CommonMark allows 0-3 spaces before a top-level marker. An indented marker
    directly continuing a bullet (no blank line) is a nested item and stays
    part of its parent; after a blank line it starts a new top-level item.
    """
    bullets, current, stray = [], None, []
    for _, line in lines:
        marker = re.match(r"( {0,3})[-*+] ", line)
        if re.match(r" {0,3}(?:[0-9]{1,9}[.)](?: |$)|>)", line):
            # Ordered items and blockquotes are separate blocks, never part
            # of a cited bullet, and are not allowed in evidence sections.
            current = None
            stray.append(line.strip())
        elif marker and (current is None or len(marker.group(1)) < 2):
            current = [line.lstrip()]
            bullets.append(current)
        elif not line.strip() or re.match(r" {0,3}#{1,6} ", line):
            current = None
        elif current is not None:
            current.append(line)
        else:
            stray.append(line.strip())
    return ["\n".join(bullet) for bullet in bullets], stray


def cited_source_ids(text, source_ids):
    return [token.strip() for token in re.findall(r"`([^`\n]+)`", text)
            if token.strip() in source_ids]


def validate_evidence_sections(doc, evidence, contract, failures):
    source_ids = {source["id"] for source in contract["sources"]}
    available = evidence["available"]
    spec = contract["evidence_sections"]
    for index in spec["heading_indexes"]:
        heading = contract["headings"][index]
        bullets, stray = top_level_bullets(doc.section_lines(heading))
        if stray:
            failures.add(
                f"{heading} may contain only tagged, cited bullets; stray text: {stray[0][:40]}"
            )
        if len(bullets) < spec["min_bullets"]:
            failures.add(
                f"{heading} needs at least {spec['min_bullets']} top-level bullet(s)"
            )
        for bullet in bullets:
            body = bullet[2:].lstrip()
            if not body.startswith(PATH_TAGS):
                failures.add(f"{heading} bullet must start with a path tag: {body[:40]}")
            cited = cited_source_ids(bullet, source_ids)
            if not any(available.get(source_id) for source_id in cited):
                failures.add(
                    f"{heading} bullet cites no successful contract source_id: {body[:40]}"
                )
    skipped = {contract["headings"][H_APPENDIX], contract["headings"][H_GAPS]}
    h2_by_line = {h[0]: h[3] for h in doc.headings if h[1] == 2}
    section = None
    flagged = set()
    for index, line in doc.visible:
        section = h2_by_line.get(index, section)
        if section in skipped:
            continue
        for source_id in cited_source_ids(line, source_ids):
            if not available.get(source_id) and source_id not in flagged:
                flagged.add(source_id)
                failures.add(
                    f"body cites {source_id} whose Coverage status is not successful"
                )


def validate_forecast_object(forecast, contract, macro, report_day, label, failures):
    fields = contract["forecast_schema"]["current_fields"]
    if set(forecast) != set(fields):
        failures.add(
            f"{label} fields mismatch: missing {sorted(set(fields) - set(forecast))}, "
            f"extra {sorted(set(forecast) - set(fields))}"
        )
        return
    day = strict_date(forecast["date"], f"{label} date", failures)
    if day and report_day and day != report_day:
        failures.add(f"{label} date does not match report title")
    if day:
        iso = day.isocalendar()
        if forecast["iso_week"] != f"{iso.year}-W{iso.week:02d}":
            failures.add(f"{label} iso_week does not match date")
        if forecast["weekday"] != day.strftime("%A"):
            failures.add(f"{label} weekday does not match date")
        expected_end = (
            day + timedelta(days=contract["question"]["horizon_days"])
        ).isoformat()
        if forecast["horizon_end"] != expected_end:
            failures.add(f"{label} horizon_end must be {expected_end}")
    if forecast["timezone"] != contract["timezone"]:
        failures.add(f"{label} timezone must be {contract['timezone']}")
    if (type(forecast["question_version"]) is not int
            or forecast["question_version"] != contract["question"]["version"]):
        failures.add(f"{label} question_version does not match contract")
    if (type(forecast["resolution_version"]) is not int
            or forecast["resolution_version"] != contract["resolution"]["version"]):
        failures.add(f"{label} resolution_version does not match contract")
    if forecast["answer"] not in contract["question"]["answers"]:
        failures.add(f"{label} answer must be one of {contract['question']['answers']}")
    if forecast["prior_date"] is not None:
        prior_day = strict_date(forecast["prior_date"], f"{label} prior_date", failures)
        if prior_day and day and prior_day >= day:
            failures.add(f"{label} prior_date must be strictly before date")
    if (forecast["prior_answer"] is not None
            and forecast["prior_answer"] not in contract["question"]["answers"]):
        failures.add(f"{label} prior_answer must be null or one of the answers")
    flips = forecast["flip_evidence"]
    if not isinstance(flips, list) or any(not isinstance(i, str) for i in flips):
        failures.add(f"{label} flip_evidence must be an array of strings")
    ndx = macro.get("ndx_drawdown", {})
    if ndx.get("status") == "ok":
        if (not finite_number(forecast["r1_drawdown_pct"])
                or forecast["r1_drawdown_pct"] != ndx.get("drawdown_pct")):
            failures.add(f"{label} r1_drawdown_pct must equal macro ndx_drawdown.drawdown_pct")
    elif forecast["r1_drawdown_pct"] is not None:
        failures.add(f"{label} r1_drawdown_pct must be null when ndx_drawdown failed")
    if forecast["resolution"] is not None:
        failures.add(f"{label} resolution must be null")


def evidence_days(evidence, source_id):
    days = []
    for row in (evidence["raw_by_id"].get(source_id, [])
                + evidence["traces_by_id"].get(source_id, [])):
        if re.fullmatch(DATE_RE, row[4]):
            try:
                days.append(date.fromisoformat(row[4]))
            except ValueError:
                pass
    return days


def validate_prior_and_flip(doc, forecast, prior, evidence, macro, contract, failures):
    fields = contract["forecast_schema"]["current_fields"]
    heading = contract["headings"][H_COMPARISON]
    lines = [line.strip() for _, line in doc.section_lines(heading) if line.strip()]
    text = "\n".join(lines)
    first = lines[0] if lines else None
    prior_date, prior_answer = forecast.get("prior_date"), forecast.get("prior_answer")
    flips = forecast.get("flip_evidence")
    macro_prior = macro.get("prior_run_date")
    if prior is None:
        if prior_answer is not None:
            failures.add("prior_answer must be null without a prior forecast")
        if flips != []:
            failures.add("flip_evidence must be [] without a prior forecast")
        if prior_date is None:
            if macro_prior != "none":
                failures.add("baseline forecast requires macro prior_run_date `none`")
            expected = "前次結論：無前次（基準）"
        else:
            if macro_prior != prior_date:
                failures.add("macro prior_run_date does not match forecast prior_date")
            expected = f"前次結論：無前次預測（report-{prior_date} 為舊格式評分報告）"
        if first != expected:
            failures.add(f"{heading} first line must be `{expected}`")
        return
    missing = [field for field in fields if field not in prior]
    if missing:
        failures.add(f"prior forecast lacks fields: {missing}")
        return
    prior_day = strict_date(prior["date"], "prior forecast date", failures)
    if prior["answer"] not in contract["question"]["answers"]:
        failures.add("prior forecast answer is invalid")
        return
    if prior_date != prior["date"]:
        failures.add("forecast prior_date does not match prior forecast date")
    if prior_answer != prior["answer"]:
        failures.add("forecast prior_answer does not match prior forecast answer")
    if macro_prior != prior["date"]:
        failures.add("macro prior_run_date does not match prior forecast date")
    expected = f"前次結論：{prior['answer']}（report-{prior['date']}）"
    if first != expected:
        failures.add(f"{heading} first line must be `{expected}`")
    verdict_lines = [line for line in lines if line.startswith("本次結論：")]
    answer = forecast.get("answer")
    if answer != prior["answer"]:
        if verdict_lines != ["本次結論：翻轉"]:
            failures.add(f"{heading} must contain exactly the line `本次結論：翻轉`")
        if not isinstance(flips, list) or not flips:
            failures.add("flip_evidence must be non-empty when the answer flipped")
            return
        if len(flips) != len(set(flips)):
            failures.add("flip_evidence must not contain duplicates")
        source_ids = {source["id"] for source in contract["sources"]}
        cited = set(cited_source_ids(text, source_ids))
        for source_id in flips:
            if source_id not in source_ids:
                failures.add(f"flip_evidence {source_id!r} is not a contract source_id")
                continue
            if not evidence["available"].get(source_id):
                failures.add(f"flip_evidence {source_id} lacks a successful Coverage status")
            if prior_day and not any(
                    day > prior_day for day in evidence_days(evidence, source_id)):
                failures.add(
                    f"flip_evidence {source_id} has no Raw/traceability row dated after "
                    "the prior forecast"
                )
            if source_id not in cited:
                failures.add(f"flip_evidence {source_id} is not cited in {heading}")
    else:
        if verdict_lines != ["本次結論：維持"]:
            failures.add(f"{heading} must contain exactly the line `本次結論：維持`")
        if flips != []:
            failures.add("flip_evidence must be [] when the answer is unchanged")


def validate_gaps_section(doc, evidence, contract, failures):
    heading = contract["headings"][H_GAPS]
    text = section_text(doc, heading)
    failed = [source_id for source_id, token in evidence["coverage_tokens"].items()
              if token == "⛔ FETCH FAILED"]
    none_line = "本次無 FETCH FAILED 來源"
    if failed:
        for source_id in failed:
            if not mentions_identifier(text, source_id):
                failures.add(f"{heading} must mention FETCH FAILED source {source_id}")
        if none_line in text:
            failures.add(f"{heading} claims no FETCH FAILED source although some failed")
    elif not any(line.strip() == none_line for line in text.splitlines()):
        failures.add(f"{heading} must contain the line `{none_line}`")


def validate_spv_deal_rows(rows, marker, where, failures):
    """Conditionally enforce required attributes on a tagged SPV deal row.

    A row is only inspected when its item cell contains the contract's
    ``spv_deal_marker`` tag (matched case-insensitively), with one tripwire:
    an untagged event-scan row of the marker's source whose item cell
    mentions a contract-listed SPV keyword fails, so an obviously described
    SPV deal cannot dodge the attribute requirements by omitting the tag.
    Other untagged rows are never checked (same conditional-enforcement
    philosophy as trigger ``evidence_tag``). A case-variant of the exact tag
    is rejected outright -- it would otherwise read as tagged to a human but
    silently skip every check below, since the case-sensitive gate would
    treat it as absent.
    """
    tag = marker["tag"]
    prefix = f"[{marker['component_id']}]{tag}"

    def keyword_hit(text):
        for keyword in marker["keywords"]:
            if keyword.isascii():
                if re.search(rf"(?<![A-Za-z0-9]){re.escape(keyword)}", text,
                             re.IGNORECASE):
                    return keyword
            elif keyword in text:
                return keyword
        return None

    for row in rows:
        item = row[1] if len(row) > 1 else ""
        tag_match = re.search(re.escape(tag), item, re.IGNORECASE)
        if not tag_match:
            if (row[0] == marker["source_id"]
                    and item.startswith(f"[{marker['component_id']}]")):
                keyword = keyword_hit(item)
                if keyword:
                    failures.add(
                        f"{where} spv_deal keyword '{keyword}' on an untagged "
                        f"{marker['component_id']} row requires the {tag} tag: {row}"
                    )
            continue
        if tag_match.group(0) != tag:
            failures.add(
                f"{where} spv_deal marker must use the exact-case tag {tag}: {row}"
            )
            continue
        if row[0] != marker["source_id"] or not item.startswith(prefix):
            failures.add(
                f"{where} spv_deal marker {tag} may only appear on "
                f"{marker['source_id']}/{marker['component_id']} rows: {row}"
            )
            continue
        found = []
        all_present = True
        for key in marker["required_keys"]:
            matches = list(re.finditer(
                rf"(?<=[\s;]){re.escape(key)}=([^;|]*)", item
            ))
            if len(matches) > 1:
                failures.add(
                    f"{where} spv_deal marker on {row[0]} has duplicate attribute {key}"
                )
                all_present = False
                continue
            if len(matches) != 1 or not matches[0].group(1).strip():
                failures.add(
                    f"{where} spv_deal marker on {row[0]} missing required attribute {key}"
                )
                all_present = False
                continue
            if matches[0].end() >= len(item) or item[matches[0].end()] != ";":
                failures.add(
                    f"{where} spv_deal marker on {row[0]} attribute {key} "
                    "is not terminated by ';'"
                )
                all_present = False
                continue
            found.append((key, matches[0]))
        if all_present:
            positions = [match.start() for _, match in found]
            if positions != sorted(positions):
                failures.add(
                    f"{where} spv_deal marker on {row[0]} attributes are not in contract order"
                )
            # A key token landing inside another key's captured value means the
            # pairs are not ;-separated tokens (e.g. "residual_value_guarantee=
            # undisclosed lease_term=15y;" carries no standalone lease_term=).
            for outer_key, outer in found:
                for inner_key, inner in found:
                    if inner is not outer and outer.start() < inner.start() < outer.end():
                        failures.add(
                            f"{where} spv_deal marker on {row[0]} attribute "
                            f"{inner_key} is nested inside the value of {outer_key}"
                        )


def validate_appendix(doc, report_day, macro, contract, failures):
    appendix_h2 = contract["headings"][H_APPENDIX]
    raw_heading, coverage_heading, trace_heading = contract["appendix_headings"]
    raw_section = doc.subsection_lines(raw_heading, appendix_h2)
    coverage_section = doc.subsection_lines(coverage_heading, appendix_h2)
    trace_section = doc.subsection_lines(
        trace_heading, appendix_h2
    )
    raw_rows = find_table(
        raw_section, contract["raw_data_header"], "raw data", failures
    )
    coverage_rows = find_table(
        coverage_section, contract["coverage_header"], "Coverage", failures
    )
    trace_rows = find_table(
        trace_section, contract["traceability_header"], "traceability", failures
    )
    validate_spv_deal_rows(raw_rows, contract["spv_deal_marker"], "raw data", failures)
    validate_spv_deal_rows(trace_rows, contract["spv_deal_marker"], "traceability", failures)
    sources = contract["sources"]
    source_by_id = {source["id"]: source for source in sources}
    raw_by_id = {}
    if not raw_rows:
        failures.add("raw data table must contain at least one concrete data row")
    for row in raw_rows:
        if any(cell == "" for cell in row):
            failures.add(f"raw data row has an empty cell: {row}")
            continue
        source_id = row[0]
        if source_id not in source_by_id:
            failures.add(f"raw data row has unknown source_id {source_id!r}")
            continue
        raw_by_id.setdefault(source_id, []).append(row)
        if row[1] == "—" or row[2] == "—" or not re.search(r"\d", row[2]):
            failures.add(f"raw data row is not a concrete numeric observation: {row}")
        if not (
            contains_valid_http_url(row[3])
            or re.search(r"\b[A-Z][A-Z0-9.^_-]{1,}\b", row[3])
        ):
            failures.add(f"raw data source lacks a series ID or URL: {row[3]!r}")
        validate_evidence_date(
            row[4], source_by_id[source_id], row[1], report_day,
            f"raw data {source_id} date", failures,
        )
        validate_retrieval_timestamp(
            row[5], report_day, f"raw data {source_id} fetch timestamp", failures
        )

    if len(coverage_rows) != len(sources):
        failures.add(f"Coverage has {len(coverage_rows)} rows; expected {len(sources)}")
    coverage_tokens = {}
    zero_result_ids = set()
    composite_states = {}
    for index, (row, source) in enumerate(zip(coverage_rows, sources), 1):
        if row[0] != source["id"]:
            failures.add(f"Coverage row {index} ID/order mismatch: {row[0]!r}")
        if source["prompt_match"] not in row[1]:
            failures.add(f"Coverage {source['id']} source-bullet cell lacks contract prompt_match")
        if row[2] in ("", "—"):
            failures.add(f"Coverage {source['id']} method cell is empty")
        token = status_token(row[3], contract, f"Coverage {source['id']}", failures)
        coverage_tokens[source["id"]] = token
        if token == "✗ NOT DISCLOSED" and source["required"]:
            failures.add(f"required source {source['id']} cannot be NOT DISCLOSED")
        if token == "derived" and source["id"] != "monetary.t10yie":
            failures.add(f"derived status is not allowed for {source['id']}")
        has_zero_text = "0 件" in row[3]
        is_exact_zero = row[3] == "✓ SEARCH-VERIFIED（0 件）"
        if has_zero_text and not is_exact_zero:
            failures.add(f"Coverage {source['id']} has malformed zero-result status")
        if is_exact_zero:
            if not source.get("zero_result_allowed"):
                failures.add(f"Coverage {source['id']} is not eligible for zero-result status")
            zero_result_ids.add(source["id"])
        if source.get("window") == "composite":
            component_ids = [item["id"] for item in source["window_components"]]
            detail_re = re.compile(
                re.escape(token or "") + r" components="
                + ",".join(
                    re.escape(component_id)
                    + r":(ok|not_disclosed|fetch_failed)"
                    for component_id in component_ids
                )
            )
            detail_match = detail_re.fullmatch(row[3])
            if not detail_match:
                failures.add(
                    f"Coverage {source['id']} must declare exact component states/order"
                )
                states = {}
            else:
                states = dict(zip(component_ids, detail_match.groups()))
            composite_states[source["id"]] = states
            if states:
                aggregation = source["component_aggregation"]
                if ((aggregation == "all" and all(
                        value == "ok" for value in states.values()))
                        or (aggregation == "any" and "ok" in states.values())):
                    expected_composite_token = token
                    if token not in ("✓ API", "✓ DIRECT", "✓ SEARCH-VERIFIED"):
                        failures.add(
                            f"Coverage {source['id']} all-ok components need a success token"
                        )
                elif ((aggregation == "all" and "fetch_failed" in states.values())
                      or (aggregation == "any" and all(
                          value == "fetch_failed" for value in states.values()))):
                    expected_composite_token = "⛔ FETCH FAILED"
                else:
                    expected_composite_token = "✗ NOT DISCLOSED"
                if token != expected_composite_token:
                    failures.add(
                        f"Coverage {source['id']} token conflicts with component states"
                    )

    traces_by_id = {}
    for row in trace_rows:
        source_id = row[0]
        if source_id not in source_by_id:
            failures.add(f"traceability row has unknown source_id {source_id!r}")
            continue
        token = coverage_tokens.get(source_id)
        source = source_by_id[source_id]
        component_match = re.match(r"^\[([a-z0-9_]+)\]", row[1])
        composite_partial_ok = (
            source.get("window") == "composite"
            and component_match
            and composite_states.get(source_id, {}).get(component_match.group(1)) == "ok"
        )
        if token not in ("✓ API", "✓ DIRECT", "✓ SEARCH-VERIFIED", "derived") \
                and not composite_partial_ok:
            failures.add(f"traceability {source_id} has no successful Coverage status")
        traces_by_id.setdefault(source_id, []).append(row)
        if row[1] in ("", "—") or row[2] in ("", "—") or row[3] in ("", "—"):
            failures.add(f"traceability {source_id} lacks item/query/result source")
        validate_retrieval_timestamp(
            row[5], report_day, f"traceability {source_id} timestamp", failures
        )
        if source_id in zero_result_ids:
            if row[4] != "—":
                validate_evidence_date(
                    row[4], source, row[1], report_day,
                    f"traceability {source_id} date", failures,
                )
            continue
        if not contains_valid_http_url(row[3]):
            failures.add(f"non-zero traceability {source_id} must contain a result URL")
        validate_evidence_date(
            row[4], source, row[1], report_day,
            f"traceability {source_id} date", failures,
        )
    for source_id, token in coverage_tokens.items():
        if token == "✓ SEARCH-VERIFIED" and source_id not in traces_by_id:
            failures.add(f"SEARCH-VERIFIED source {source_id} lacks traceability row")

    success_tokens = {"✓ API", "✓ DIRECT", "✓ SEARCH-VERIFIED", "derived"}
    success = {}
    available = {}
    for source in sources:
        source_id = source["id"]
        token = coverage_tokens.get(source_id)
        available[source_id] = token in success_tokens
        # A zero-result screen is real completed evidence of a miss, but it
        # cannot support a positive feature or trigger claim.
        success[source_id] = (
            available[source_id] and source_id not in zero_result_ids
        )
        binding = source.get("macro")
        if token in ("✓ API", "✓ DIRECT", "derived") and source_id not in raw_by_id:
            failures.add(f"successful Coverage {source_id} lacks source-linked raw evidence")
        if token == "✓ SEARCH-VERIFIED" and source_id not in traces_by_id:
            failures.add(f"SEARCH-VERIFIED source {source_id} lacks traceability row")
        # A failed composite may still contain usable API legs.  Preserve and
        # prove those legs instead of forcing the appendix to discard them;
        # only a non-macro failed source is forbidden from claiming raw data.
        if (token not in success_tokens and source_id in raw_by_id and not binding
                and source.get("window") != "composite"):
            failures.add(f"unsuccessful Coverage {source_id} must not claim raw evidence")

        if not binding:
            if source.get("window") == "composite":
                states = composite_states.get(source_id, {})
                for component in source["window_components"]:
                    component_id = component["id"]
                    raw_matches = [
                        row for row in raw_by_id.get(source_id, [])
                        if row[1].startswith(f"[{component_id}]")
                    ]
                    trace_matches = [
                        row for row in traces_by_id.get(source_id, [])
                        if row[1].startswith(f"[{component_id}]")
                    ]
                    if states.get(component_id) == "ok" and not (
                            raw_matches or trace_matches):
                        failures.add(
                            f"composite {source_id}/{component_id} ok lacks evidence"
                        )
                    if states.get(component_id) != "ok" and (
                            raw_matches or trace_matches):
                        failures.add(
                            f"composite {source_id}/{component_id} non-ok claims evidence"
                        )
            continue
        component_states = []
        for component in binding["components"]:
            block = macro_component(macro, component)
            component_states.append((component, block, block.get("status")))
        usable = [state in ("ok", "derived") for _, _, state in component_states]
        script_success = all(usable) if binding["aggregation"] == "all" else any(usable)
        derived_success = (
            script_success and len(component_states) == 1
            and component_states[0][2] == "derived"
        )
        expected_token = "derived" if derived_success else "✓ API"
        if script_success and token != expected_token:
            failures.add(
                f"Coverage {source_id} must be {expected_token} for its macro aggregation"
            )
        if not script_success and token in ("✓ API", "✓ DIRECT", "derived"):
            failures.add(
                f"Coverage {source_id} cannot claim script/direct success after macro failure"
            )
        successful_components = [
            item for item in component_states if item[2] in ("ok", "derived")
        ]
        failed_components = [
            item for item in component_states if item[2] not in ("ok", "derived")
        ]
        # Every value emitted by the deterministic fetcher remains auditable,
        # including usable legs of an otherwise failed ``all`` composite.
        component_keys = [item[0]["key"] for item in component_states]
        for component, block, _state in successful_components:
            key = component["key"]
            matching = [
                row for row in raw_by_id.get(source_id, [])
                if (mentions_identifier(row[1], key)
                    or mentions_identifier(row[3], key))
            ]
            if not matching:
                failures.add(f"raw evidence for {source_id} does not identify macro component {key}")
                continue
            primary_field, evidence_fields = macro_component_evidence_fields(
                component, block
            )
            expected_value, latest_date = evidence_fields.get(
                primary_field, (None, None)
            )
            if (latest_date and finite_number(expected_value)
                    and not any(
                        row[4] == latest_date
                        and displayed_matches(row[2], expected_value)
                        for row in matching
                    )):
                failures.add(
                    f"raw evidence value/date for {source_id}/{key} != macro value/date"
                )

            for row in matching:
                row_hits = [
                    candidate for candidate in component_keys
                    if (mentions_identifier(row[1], candidate)
                        or mentions_identifier(row[3], candidate))
                ]
                # A compound derived row such as SOFR-IORB can mention two
                # source legs; it is not a representation of either leg alone.
                if row_hits != [key]:
                    continue
                explicit_fields = [
                    field for field in evidence_fields
                    if mentions_identifier(row[1], field)
                ]
                candidate_fields = explicit_fields or [primary_field]
                if not any(
                        field in evidence_fields
                        and row[4] == evidence_fields[field][1]
                        and displayed_matches(row[2], evidence_fields[field][0])
                        for field in candidate_fields):
                    failures.add(
                        f"raw evidence row for {source_id}/{key} is not reproducible "
                        "from the macro artifact"
                    )

        if (token == "✓ API" and any(
                item[0]["key"] == "ndx_drawdown" for item in successful_components)):
            ndx_block = macro["ndx_drawdown"]
            for field in ("latest", "high", "drawdown_pct"):
                day_field = "high_date" if field == "high" else "latest_date"
                if not any(
                        mentions_identifier(row[1], field)
                        and row[4] == ndx_block[day_field]
                        and displayed_matches(row[2], ndx_block[field])
                        for row in raw_by_id.get(source_id, [])):
                    failures.add(
                        f"raw evidence for {source_id} lacks a reproducible "
                        f"ndx_drawdown {field} row"
                    )

        if token == "✓ SEARCH-VERIFIED" and failed_components:
            trace_rows_for_source = traces_by_id.get(source_id, [])

            def trace_identifies(component):
                key = component["key"]
                return any(
                    any(mentions_identifier(cell, key) for cell in row[1:4])
                    for row in trace_rows_for_source
                )

            if binding["aggregation"] == "all":
                for component, _block, _state in failed_components:
                    if not trace_identifies(component):
                        failures.add(
                            f"SEARCH fallback for {source_id} does not prove required "
                            f"macro component {component['key']}"
                        )
            elif not any(
                    trace_identifies(component)
                    for component, _block, _state in failed_components):
                failures.add(
                    f"SEARCH fallback for {source_id} does not identify any eligible "
                    "macro component"
                )

    return {
        "coverage_tokens": coverage_tokens,
        "success": success,
        "available": available,
        "raw_by_id": raw_by_id,
        "traces_by_id": traces_by_id,
        "zero_result_ids": zero_result_ids,
        "composite_states": composite_states,
    }


def validate_global_security(doc, contract, failures):
    hit = sorted({char for char in doc.text if char in BOX_CHARS})
    if hit:
        failures.add(f"report contains forbidden box characters: {''.join(hit)}")
    decoded = doc.text
    for _ in range(3):
        next_decoded = unquote(decoded)
        if next_decoded == decoded:
            break
        decoded = next_decoded
    for pattern in SECRET_PATTERNS:
        if pattern.search(decoded):
            failures.add("report contains a credential-like secret or api_key query")
            break
    unsafe_tilde_lines = []
    # MarkdownDocument.visible already excludes both backtick and tilde
    # fences, including their delimiters.  Re-parsing only ``` here used to
    # misclassify content inside a ~~~ fence as visible prose.
    for index, line in doc.visible:
        visible = re.sub(r"`[^`]*`", "", line)
        visible = re.sub(r"https?://\S+", "", visible)
        if "~" in visible:
            unsafe_tilde_lines.append(index + 1)
    if unsafe_tilde_lines:
        failures.add(f"visible ASCII `~` is forbidden on lines {unsafe_tilde_lines[:10]}")
    nonempty = doc.visible_nonempty()
    if not nonempty or nonempty[-1][1] != contract["disclaimer"]:
        failures.add("final visible line is not the exact contract disclaimer")


def validate_wording_lock(doc, contract, failures):
    """Reject contract-declared synonyms in locked lines and full sections."""
    policy = contract["wording_lock"]
    locked_sections = {
        contract["headings"][index]
        for index in policy["full_section_heading_indexes"]
    }
    h2_by_line = {
        index: normalized
        for index, level, _title, normalized in doc.headings
        if level == 2
    }
    current_section = None
    for index, line in doc.visible:
        stripped = line.strip()
        if index in h2_by_line:
            current_section = h2_by_line[index]
        locked_line = stripped.startswith(("#", "|", ">", "**"))
        if locked_line or current_section in locked_sections:
            for synonym in policy["forbidden_synonyms"]:
                if synonym in stripped:
                    failures.add(
                        f"{synonym} appears in a terminology-locked location: "
                        f"{stripped[:80]}"
                    )


def validate_scoring_terms(doc, contract, failures):
    """The report answers yes/no only: no scores or forecast probabilities."""
    appendix = contract["headings"][H_APPENDIX]
    h2_by_line = {h[0]: h[3] for h in doc.headings if h[1] == 2}
    section = None
    for index, line in doc.visible:
        section = h2_by_line.get(index, section)
        if section == appendix:
            continue
        for term in contract["wording_lock"]["forbidden_scoring_terms"]:
            if term.casefold() in line.casefold():
                failures.add(f"scoring/probability term `{term}` is not allowed: {line.strip()[:80]}")


def validate_unexpected_tables(doc, contract, failures):
    allowed = {
        contract["coverage_header"], contract["raw_data_header"],
        contract["traceability_header"],
    }
    visible = doc.visible
    for index, (_, line) in enumerate(visible[:-1]):
        cells = table_cells(line)
        if cells is None:
            continue
        next_line = visible[index + 1][1]
        if is_separator(next_line, len(cells)) and line.strip() not in allowed:
            failures.add(f"unexpected/uncontracted Markdown table header: {line.strip()}")


def build_parser():
    parser = argparse.ArgumentParser(
        description="Validate a bubble-risk forecast report before archive mutation."
    )
    parser.add_argument("report", help="complete report Markdown")
    parser.add_argument("--current-forecast", required=True,
                        help="standalone forecast.json payload that will be archived")
    parser.add_argument("--prompt", required=True, help="version-matched prompt Markdown")
    parser.add_argument("--contract", required=True, help="report_contract.json")
    parser.add_argument("--macro-json", required=True, help="exact fetch_macro JSON output")
    prior = parser.add_mutually_exclusive_group(required=True)
    prior.add_argument("--prior-forecast", help="accepted prior forecast.json")
    prior.add_argument("--no-prior-forecast", action="store_true",
                       help="legacy score.json prior or baseline run")
    run_mode = parser.add_mutually_exclusive_group(required=True)
    run_mode.add_argument("--production", action="store_true")
    run_mode.add_argument("--dry-run", action="store_true")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    failures = Failures()
    contract = load_json_file(args.contract, "report contract", failures)
    if contract is None or not validate_contract(contract, failures):
        return failures.emit_and_exit()
    prompt = read_text(args.prompt, "prompt", failures)
    report = read_text(args.report, "report", failures)
    macro = load_json_file(
        args.macro_json, "macro JSON", failures,
        allow_markers=True, require_markers=True,
    )
    current = load_json_file(args.current_forecast, "current forecast", failures)
    prior = None
    if args.prior_forecast:
        prior = load_json_file(args.prior_forecast, "prior forecast", failures)
        if prior is None:
            return failures.emit_and_exit()
    if prompt is None or report is None or macro is None or current is None:
        return failures.emit_and_exit()
    if not validate_macro_shape(macro, contract, failures):
        return failures.emit_and_exit()

    validate_prompt_mapping(prompt, contract, failures)
    if macro.get("prior_run_date") == "none":
        decomposition = macro.get("decomposition", {})
        if (decomposition.get("status"), decomposition.get("driver"),
                decomposition.get("freshness")) != (
                    "baseline_no_prior", "baseline", "not_applicable"):
            failures.add("baseline macro decomposition state is invalid")

    doc = MarkdownDocument(report, failures)
    validate_global_security(doc, contract, failures)
    validate_wording_lock(doc, contract, failures)
    validate_scoring_terms(doc, contract, failures)
    fenced = validate_headings_and_fence(doc, contract, failures)
    if fenced is None:
        return failures.emit_and_exit()
    if not json_equal(fenced, current):
        failures.add("standalone current forecast file does not equal the report JSON fence")

    report_day = validate_title_and_meta(
        doc, current, args.dry_run, contract, failures
    )
    validate_forecast_object(
        current, contract, macro, report_day, "current forecast", failures
    )
    generated = parse_iso_timestamp(macro.get("generated_at"))
    if generated and report_day and generated.date() != report_day:
        failures.add("macro generated_at date does not match report date")

    evidence = validate_appendix(doc, report_day, macro, contract, failures)
    validate_conclusion(doc, current, contract, failures)
    validate_resolution_section(doc, contract, failures)
    validate_paths_section(doc, macro, contract, failures)
    validate_evidence_sections(doc, evidence, contract, failures)
    validate_prior_and_flip(
        doc, current, prior, evidence, macro, contract, failures
    )
    validate_gaps_section(doc, evidence, contract, failures)
    validate_unexpected_tables(doc, contract, failures)

    # Each exact contract table header belongs to exactly one visible table.
    for key in ("coverage_header", "raw_data_header", "traceability_header"):
        count = sum(1 for _, line in doc.visible if line.strip() == contract[key])
        if count != 1:
            failures.add(f"contract table header {key} must occur once; found {count}")
    return failures.emit_and_exit()


if __name__ == "__main__":
    sys.exit(main())

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
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from urllib.parse import unquote, urlsplit


BOX_CHARS = "╔╗╚╝║═╠╣╬┌┐└┘─│├┤┬┴┼"
DATE_RE = r"\d{4}-\d{2}-\d{2}"
NUMBER_RE = re.compile(r"[+−-]?\d+(?:\.\d+)?")
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
        "version", "timezone", "macro_schema", "disclaimer", "headings", "dimensions",
        "wording_lock",
        "tiers", "anchors", "anchor_feature_counts", "regimes",
        "trigger_states", "monetary_sides", "triangle_indicators",
        "triangle_labels", "triangle_fallbacks", "dimension_required_inputs",
        "triangle_chain_inputs", "historical_audit_labels",
        "direction_thresholds", "calibration", "trigger_reason_codes",
        "spv_deal_marker", "anchor_features", "score_schema",
        "coverage_statuses", "section1_header", "section2_header",
        "section3_header", "weighted_score_header", "coverage_header",
        "raw_data_header", "traceability_header", "sources",
    }
    if not isinstance(contract, dict):
        failures.add("report contract must be a JSON object")
        return False
    missing = required - set(contract)
    if missing:
        failures.add(f"report contract missing keys: {sorted(missing)}")
        return False
    try:
        if contract["version"] != 1:
            failures.add(f"unsupported report contract version: {contract['version']!r}")
        macro_schema = contract["macro_schema"]
        if macro_schema.get("version") != 1:
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
        dimensions = contract["dimensions"]
        if len(dimensions) != 6:
            failures.add("contract must define exactly six dimensions")
        if sum(d["weight"] for d in dimensions) != 100:
            failures.add("contract dimension weights must sum to 100")
        if len({d["name"] for d in dimensions}) != len(dimensions):
            failures.add("contract dimension names are not unique")
        if len({d["key"] for d in dimensions}) != len(dimensions):
            failures.add("contract dimension keys are not unique")
        if len(contract["headings"]) != 10 or len(set(contract["headings"])) != 10:
            failures.add("contract must define ten unique H2 headings")
        wording_lock = contract["wording_lock"]
        if (not isinstance(wording_lock, dict)
                or set(wording_lock) != {
                    "full_section_heading_indexes", "forbidden_synonyms"}):
            failures.add("contract wording_lock is invalid")
        else:
            locked_indexes = wording_lock["full_section_heading_indexes"]
            forbidden_synonyms = wording_lock["forbidden_synonyms"]
            if (not isinstance(locked_indexes, list) or not locked_indexes
                    or any(type(index) is not int
                           or not 0 <= index < len(contract["headings"])
                           for index in locked_indexes)
                    or len(locked_indexes) != len(set(locked_indexes))):
                failures.add("contract wording-lock section indexes are invalid")
            if (not isinstance(forbidden_synonyms, list)
                    or not forbidden_synonyms
                    or any(not isinstance(term, str) or not term
                           for term in forbidden_synonyms)
                    or len(forbidden_synonyms) != len(set(forbidden_synonyms))):
                failures.add("contract wording-lock synonyms are invalid")
        ids = [source["id"] for source in contract["sources"]]
        if not ids or len(set(ids)) != len(ids):
            failures.add("contract must define a nonempty set of unique source IDs")
        if list(contract["anchor_feature_counts"]) != contract["anchors"]:
            failures.add("contract anchor counts must follow anchor order")
        if list(contract["anchor_features"]) != contract["anchors"]:
            failures.add("contract anchor features must follow anchor order")
        feature_ids = []
        for anchor in contract["anchors"]:
            features = contract["anchor_features"][anchor]
            if len(features) != contract["anchor_feature_counts"][anchor]:
                failures.add(f"contract feature count mismatch for {anchor}")
            feature_ids.extend(feature["id"] for feature in features)
        if len(feature_ids) != len(set(feature_ids)):
            failures.add("contract anchor feature IDs are not unique")
        tiers = contract["tiers"]
        if tiers[0]["min"] != 0 or tiers[-1]["max"] != 100:
            failures.add("contract tiers must cover 0 through 100")
        for left, right in zip(tiers, tiers[1:]):
            if left["max"] + 1 != right["min"]:
                failures.add("contract tiers are not contiguous")
        source_ids = set(ids)
        fallbacks = contract["triangle_fallbacks"]
        if ([item.get("key") for item in fallbacks]
                != ["sp500", "wti", "dgs10"]
                or len({item.get("source_id") for item in fallbacks}) != 3
                or not all(item.get("source_id") in source_ids
                           and isinstance(item.get("component"), str)
                           and item["component"] for item in fallbacks)):
            failures.add("contract triangle_fallbacks is invalid")
        required_inputs = contract["dimension_required_inputs"]
        if set(required_inputs) != {"monetary"} or not isinstance(
                required_inputs.get("monetary"), list):
            failures.add("contract dimension_required_inputs is invalid")
        else:
            for requirement in required_inputs["monetary"]:
                if (not isinstance(requirement, dict)
                        or set(requirement) != {"source_id", "indicator"}
                        or requirement.get("source_id") not in source_ids
                        or (requirement.get("indicator") is not None
                            and not isinstance(requirement["indicator"], str))):
                    failures.add("contract monetary input requirement is invalid")
        chain_inputs = contract["triangle_chain_inputs"]
        if (not isinstance(chain_inputs, list) or len(chain_inputs) != 2
                or [item.get("series") for item in chain_inputs]
                != ["CPIAUCSL", "T5YIFR"]):
            failures.add("contract triangle_chain_inputs is invalid")
        else:
            for requirement in chain_inputs:
                if (set(requirement) != {
                        "source_id", "series", "value_field", "delta_field"}
                        or requirement["source_id"] not in source_ids
                        or requirement["series"] not in macro_schema["required_series"]
                        or not isinstance(requirement["value_field"], str)
                        or (requirement["delta_field"] is not None
                            and not isinstance(requirement["delta_field"], str))):
                    failures.add("contract triangle chain input is invalid")
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
        for reason in contract["trigger_reason_codes"].values():
            if reason.get("state") not in contract["trigger_states"]:
                failures.add("trigger reason has invalid state")
            if reason.get("kind") not in ("machine", "evidence"):
                failures.add("trigger reason has invalid kind")
            if not set(reason.get("source_ids", [])) <= source_ids:
                failures.add("trigger reason refers to an unknown source ID")
            if reason.get("kind") == "evidence":
                if not re.fullmatch(r"\[[a-z_]+\]", reason.get("evidence_tag", "")):
                    failures.add("evidence trigger reason lacks a stable evidence_tag")
                if reason.get("window") not in ("7d", "14d", "30d", "90d"):
                    failures.add("evidence trigger reason has invalid evidence window")
                if "trace_required" in reason and type(reason["trace_required"]) is not bool:
                    failures.add("trigger reason trace_required must be boolean")
        evidence_tags = [
            reason.get("evidence_tag")
            for reason in contract["trigger_reason_codes"].values()
            if reason.get("kind") == "evidence"
        ]
        if len(evidence_tags) != len(set(evidence_tags)):
            failures.add("trigger evidence tags are not unique")

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
            elif spv_marker["tag"] in evidence_tags:
                failures.add("contract spv_deal_marker tag collides with a trigger evidence_tag")
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

        score_keys = {dimension["key"] for dimension in dimensions}
        macro_roots = {"series", *macro_schema["required_blocks"]}

        def validate_rule(rule, where):
            if not isinstance(rule, dict):
                failures.add(f"{where} rule must be an object")
                return
            kind = rule.get("type")
            simple_score = {"score_between", "score_lt", "score_gte", "score_delta_gte"}
            if kind in simple_score and rule.get("key") not in score_keys:
                failures.add(f"{where} rule has invalid score key")
            if kind == "evidence":
                ids_in_rule = rule.get("source_ids")
                if (not isinstance(ids_in_rule, list) or not ids_in_rule
                        or not set(ids_in_rule) <= source_ids):
                    failures.add(f"{where} evidence rule has invalid source IDs")
            elif kind in ("all", "any"):
                children = rule.get("rules")
                if not isinstance(children, list) or not children:
                    failures.add(f"{where} logical rule must have children")
                else:
                    for child_index, child in enumerate(children):
                        validate_rule(child, f"{where}.{child_index}")
            elif kind in ("macro_compare", "macro_equals"):
                path = rule.get("path")
                if (not isinstance(path, list) or len(path) < 2
                        or not all(isinstance(part, str) for part in path)
                        or path[0] not in macro_roots):
                    failures.add(f"{where} macro rule has invalid path")
                if kind == "macro_compare" and rule.get("op") not in {
                        "lt", "le", "gt", "ge", "eq"}:
                    failures.add(f"{where} macro rule has invalid operator")
            elif kind == "trigger_eq" and rule.get("value") not in contract["trigger_states"]:
                failures.add(f"{where} trigger rule has invalid value")
            elif kind == "trigger_gte" and rule.get("value") not in contract["trigger_states"]:
                failures.add(f"{where} trigger-rank rule has invalid value")
            elif kind == "monetary_side_eq" and rule.get("value") not in contract["monetary_sides"]:
                failures.add(f"{where} monetary-side rule has invalid value")
            elif kind not in simple_score | {
                    "evidence", "all", "any", "macro_compare", "macro_equals",
                    "trigger_eq", "trigger_gte", "monetary_side_eq", "high_retreat"}:
                failures.add(f"{where} has unknown rule type {kind!r}")

        for anchor in contract["anchors"]:
            for feature in contract["anchor_features"][anchor]:
                validate_rule(feature.get("rule"), f"anchor feature {feature.get('id')}")
        for code, reason in contract["trigger_reason_codes"].items():
            if "prerequisite" in reason:
                validate_rule(reason["prerequisite"], f"trigger reason {code}")
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


def tier_for(total, contract):
    for item in contract["tiers"]:
        if item["min"] <= total <= item["max"]:
            return item["name"]
    return None


def weighted_total(values, contract):
    numerator = sum(
        values[dimension["key"]] * dimension["weight"]
        for dimension in contract["dimensions"]
    )
    return (numerator + 50) // 100, Decimal(numerator) / Decimal(100)


def validate_score_object(score, contract, failures, label="score.json", exact=True):
    if not isinstance(score, dict):
        failures.add(f"{label} must be a JSON object")
        return False
    fields = set(contract["score_schema"]["current_fields"])
    if exact and set(score) != fields:
        failures.add(
            f"{label} fields mismatch: missing {sorted(fields - set(score))}, "
            f"extra {sorted(set(score) - fields)}"
        )
        return False
    dimensions = contract["dimensions"]
    numeric_ok = True
    for dimension in dimensions:
        key = dimension["key"]
        value = score.get(key)
        if type(value) is not int or not 0 <= value <= 100:
            failures.add(f"{label}.{key} must be an integer from 0 to 100")
            numeric_ok = False
    total = score.get("total")
    if type(total) is not int or not 0 <= total <= 100:
        failures.add(f"{label}.total must be an integer from 0 to 100")
        numeric_ok = False
    if numeric_ok:
        expected_total, _ = weighted_total(score, contract)
        if total != expected_total:
            failures.add(f"{label}.total {total} != weighted half-up {expected_total}")
        expected_tier = tier_for(total, contract)
        if score.get("tier") != expected_tier:
            failures.add(f"{label}.tier {score.get('tier')!r} != {expected_tier!r}")
    if exact or "trigger_reasons" in score:
        reasons = score.get("trigger_reasons")
        allowed = list(contract["trigger_reason_codes"])
        if not isinstance(reasons, list) or any(
                not isinstance(item, str) for item in reasons):
            failures.add(f"{label}.trigger_reasons must be an array of reason-code strings")
        elif len(reasons) != len(set(reasons)) or any(
                item not in allowed for item in reasons):
            failures.add(f"{label}.trigger_reasons contains duplicate/unknown codes")
        elif reasons != [item for item in allowed if item in reasons]:
            failures.add(f"{label}.trigger_reasons must follow contract order")
    dev = score.get("sp500_dev200_pct")
    if dev is not None and (
            type(dev) not in (int, float) or not math.isfinite(dev)):
        failures.add(f"{label}.sp500_dev200_pct must be a finite number or null")
    return numeric_ok


def validate_prior(prior, contract, failures):
    failure_count = len(failures.items)
    required = set(contract["score_schema"]["legacy_prior_required_fields"])
    recognized = set(contract["score_schema"]["current_fields"])
    if not isinstance(prior, dict):
        failures.add("prior score must be a JSON object")
        return None
    if not required <= set(prior):
        failures.add(f"prior score missing legacy fields: {sorted(required - set(prior))}")
        return None
    unknown = set(prior) - recognized
    if unknown:
        failures.add(f"prior score has unknown fields: {sorted(unknown)}")
    validate_score_object(prior, contract, failures, "prior score", exact=False)

    prior_day = None
    if "date" in prior:
        prior_day = strict_date(prior["date"], "prior score date", failures)
    if prior_day and "iso_week" in prior:
        expected_week = (
            f"{prior_day.isocalendar().year}-W{prior_day.isocalendar().week:02d}"
        )
        if prior["iso_week"] != expected_week:
            failures.add("prior score iso_week does not match its date")
    if prior_day and "weekday" in prior and prior["weekday"] != prior_day.strftime("%A"):
        failures.add("prior score weekday does not match its date")
    if "timezone" in prior and prior["timezone"] != contract["timezone"]:
        failures.add("prior score timezone does not match contract")
    if "regime" in prior and prior["regime"] not in contract["regimes"]:
        failures.add("prior score regime is invalid")
    if "trigger_state" in prior and prior["trigger_state"] not in contract["trigger_states"]:
        failures.add("prior score trigger_state is invalid")
    if "monetary_side" in prior and prior["monetary_side"] not in contract["monetary_sides"]:
        failures.add("prior score monetary_side is invalid")
    if "hy_oas_widening_streak" in prior:
        streak = prior["hy_oas_widening_streak"]
        if type(streak) is not int or streak < 0:
            failures.add("prior score hy_oas_widening_streak must be a nonnegative integer")
    if "sp500_dev200_pct" in prior:
        value = prior["sp500_dev200_pct"]
        if value is not None and (
                type(value) not in (int, float) or not math.isfinite(value)):
            failures.add("prior score sp500_dev200_pct must be finite numeric or null")

    merged = dict(contract["score_schema"]["legacy_prior_defaults"])
    merged.update(prior)
    return None if len(failures.items) != failure_count else merged


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
    if vix_levels[base] <= 0 or sp500_levels[base] <= 0:
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
        "comove": (sp500_chg_pct >= contract["direction_thresholds"]["sp500_chg_pct"]
                   and vix_chg_pct >= contract["calibration"]["vix_comove_chg_pct"]),
    }


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


def extract_number(text):
    match = NUMBER_RE.search(text.replace(",", ""))
    if not match:
        return None
    try:
        return float(match.group().replace("−", "-"))
    except ValueError:
        return None


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


def extract_trace_evidence_number(text):
    """Read the last value-like number after removing machine identifiers."""
    if not isinstance(text, str):
        return None
    # Digits inside DGS10/SOFR99/BAMLC0A0CM are identifiers, not evidence.
    without_ids = re.sub(r"\b[A-Z][A-Z0-9.^_-]{1,}\b", " ", text)
    value, _tolerance = extract_display_number(without_ids, last=True)
    return value


def displayed_matches(text, expected, last=False):
    if type(expected) not in (int, float) or not math.isfinite(expected):
        return False
    value, tolerance = extract_display_number(text, last=last)
    return value is not None and abs(value - expected) <= tolerance


def displayed_contains(text, expected):
    if type(expected) not in (int, float) or not math.isfinite(expected):
        return False
    for match in DISPLAY_NUMBER_RE.finditer(text):
        token = match.group().replace(",", "").replace("−", "-")
        decimals = len(token.rsplit(".", 1)[1]) if "." in token else 0
        try:
            if abs(float(token) - expected) <= 0.5 * (10 ** -decimals) + 1e-9:
                return True
        except ValueError:
            pass
    return False


def direction(value, threshold):
    if type(value) not in (int, float):
        return None
    if abs(value) < threshold:
        return "flat"
    return "up" if value > 0 else "down"


def trusted_decomposition_leg(macro, key):
    block = macro.get("decomposition", {})
    if block.get("status") not in ("ok", "unavailable_no_daily_history"):
        return None
    value = block.get(key)
    return value if type(value) in (int, float) and math.isfinite(value) else None


def expected_regime(macro, baseline, contract):
    if baseline:
        return "基準日", {"sp500": None, "wti": None, "dgs10": None}
    series = macro.get("series", {}) if isinstance(macro, dict) else {}
    sp500 = macro.get("sp500_trend", {}) if isinstance(macro, dict) else {}
    decomposition = macro.get("decomposition", {}) if isinstance(macro, dict) else {}
    values = {
        "sp500": sp500.get("chg_pct") if sp500.get("status") == "ok" else None,
        "wti": series.get("DCOILWTICO", {}).get("chg_pct")
        if series.get("DCOILWTICO", {}).get("status") == "ok" else None,
        "dgs10": trusted_decomposition_leg(macro, "d_dgs10_bps"),
    }
    thresholds = contract["direction_thresholds"]
    directions = {
        "sp500": direction(values["sp500"], thresholds["sp500_chg_pct"]),
        "wti": direction(values["wti"], thresholds["wti_chg_pct"]),
        "dgs10": direction(values["dgs10"], thresholds["dgs10_delta_bps"]),
    }
    if any(value is None for value in directions.values()):
        return "不可判", directions
    if all(value == "up" for value in directions.values()):
        dev = sp500.get("dev200_pct")
        if type(dev) in (int, float) and dev >= contract["calibration"]["sp500_high_deviation_pct"]:
            return "同向偏高", directions
    if "up" in directions.values() and "down" in directions.values():
        return "分歧", directions
    return "穩定共存", directions


def direction_cell_matches(cell, expected, no_new_obs=False):
    value = cell.strip()
    if expected is None:
        return value == "—"
    if expected == "up":
        return value.startswith("▲")
    if expected == "down":
        return value.startswith("▼")
    if expected == "flat":
        if not value.startswith("持平"):
            return False
        return ("無新觀測" in value) if no_new_obs else ("無新觀測" not in value)
    return False


def parse_delta_cell(cell, warning_threshold, where, failures):
    if cell == "—":
        return None
    match = re.fullmatch(r"([+]\d+|0|[-−]\d+)( ⚠)?", cell)
    if not match:
        failures.add(f"{where} delta cell has invalid format: {cell!r}")
        return "invalid"
    value = int(match.group(1).replace("−", "-"))
    warned = bool(match.group(2))
    if warned != (abs(value) >= warning_threshold):
        failures.add(f"{where} warning marker does not match |delta| threshold")
    return value


def check_bar(cell, score, cells, where, failures):
    expected = "▰" * (score // 10) + "▱" * (cells - score // 10)
    if cell != expected:
        failures.add(f"{where} bar {cell!r} != {expected!r}")


def parse_current_score(cell, where, failures):
    match = re.fullmatch(r"(\d{1,3})(?: ◆)?", cell)
    if not match:
        failures.add(f"{where} score cell has invalid format: {cell!r}")
        return None
    value = int(match.group(1))
    if not 0 <= value <= 100:
        failures.add(f"{where} score is outside 0-100")
        return None
    return value


def validate_title_meta_summary(doc, score, macro, prior, baseline, dry_run,
                                contract, failures):
    nonempty = doc.visible_nonempty()
    banner = "> [DRY RUN] this report was not committed to archive."
    has_banner = bool(nonempty and nonempty[0][1] == banner)
    if dry_run and not has_banner:
        failures.add("dry-run report must begin with the locked DRY RUN banner")
    if not dry_run and has_banner:
        failures.add("production report must not contain the DRY RUN banner")
    if has_banner:
        nonempty = nonempty[1:]
    first_h2_line = min((h[0] for h in doc.headings if h[1] == 2), default=len(doc.lines))
    prefix = [(i, line) for i, line in nonempty if i < first_h2_line]
    if len(prefix) != 3:
        failures.add("title area must contain exactly H1, meta and summary lines")
        return None, None

    title_match = re.fullmatch(f"# ({DATE_RE}) 市場泡沫風險評估報告", prefix[0][1])
    if not title_match:
        failures.add("report title must be `# YYYY-MM-DD 市場泡沫風險評估報告`")
        return None, None
    report_date_text = title_match.group(1)
    report_day = strict_date(report_date_text, "report title date", failures)

    meta_match = re.fullmatch(
        f"> 報告日期：({DATE_RE})；執行日：({DATE_RE}) Asia/Taipei；"
        rf"ISO 週次：(\d{{4}}-W\d{{2}})；前次基準：(.+)",
        prefix[1][1],
    )
    if not meta_match:
        failures.add("meta line format/timezone is invalid")
    elif report_day:
        if meta_match.group(1) != report_date_text or meta_match.group(2) != report_date_text:
            failures.add("meta report/execution dates must match title date")
        expected_week = f"{report_day.isocalendar().year}-W{report_day.isocalendar().week:02d}"
        if meta_match.group(3) != expected_week:
            failures.add(f"meta ISO week {meta_match.group(3)} != {expected_week}")
        prior_meta = meta_match.group(4)
        if baseline:
            if prior_meta != "基準日":
                failures.add("baseline meta must say `前次基準：基準日`")
        else:
            prior_match = re.fullmatch(rf"report-({DATE_RE})（(\d+)天前）", prior_meta)
            if not prior_match:
                failures.add("prior meta must identify report date and day interval")
            else:
                prior_day = strict_date(prior_match.group(1), "meta prior date", failures)
                if prior_day:
                    if prior_day >= report_day:
                        failures.add("meta prior date must be strictly before report date")
                    if (report_day - prior_day).days != int(prior_match.group(2)):
                        failures.add("meta prior day interval is incorrect")
                if macro and macro.get("prior_run_date") != prior_match.group(1):
                    failures.add("meta prior date does not match macro prior_run_date")
                if prior and prior.get("date") and prior["date"] != prior_match.group(1):
                    failures.add("meta prior date does not match prior score date")

    anchor_union = "|".join(re.escape(item) for item in contract["anchors"])
    tier_union = "|".join(re.escape(item["name"]) for item in contract["tiers"])
    trigger_union = "|".join(re.escape(item) for item in contract["trigger_states"])
    summary_match = re.fullmatch(
        rf"\*\*總評\*\*：總分 (\d+)【({tier_union})】（Δ (—|0|[+−-]\d+)）；"
        rf"扳機狀態：({trigger_union})；最貼近錨點：({anchor_union})（(\d+)%）。",
        prefix[2][1],
    )
    if not summary_match:
        failures.add("summary line does not match the locked format")
        return report_day, None
    return report_day, {
        "total": int(summary_match.group(1)),
        "tier": summary_match.group(2),
        "delta": summary_match.group(3),
        "trigger": summary_match.group(4),
        "anchor": summary_match.group(5),
        "similarity": int(summary_match.group(6)),
    }


def validate_headings_and_fence(doc, contract, failures):
    h1 = [h for h in doc.headings if h[1] == 1]
    if len(h1) != 1:
        failures.add(f"report must contain exactly one visible H1; found {len(h1)}")
    actual_h2 = [h[3] for h in doc.headings if h[1] == 2]
    if actual_h2 != contract["headings"]:
        failures.add(f"visible H2 headings/order mismatch: {actual_h2}")
    for _, level, _, normalized in doc.headings:
        if level >= 4:
            failures.add(f"unexpected level-{level} heading: {normalized}")

    allowed_appendix_h3 = [
        "### Raw data", "### Coverage", "### SEARCH-VERIFIED traceability"
    ]
    dimension_h3 = [
        h for h in doc.headings
        if h[1] == 3 and h[0] > next(
            (x[0] for x in doc.headings if x[3] == "## 六維度評分"), len(doc.lines)
        ) and h[0] < next(
            (x[0] for x in doc.headings if x[3] == "## 綜合分數"), len(doc.lines)
        )
    ]
    appendix_start = next(
        (h[0] for h in doc.headings if h[3] == "## 數據附錄"), len(doc.lines)
    )
    appendix_end = next(
        (h[0] for h in doc.headings if h[3] == "## 本次分數存檔"), len(doc.lines)
    )
    appendix_h3 = [
        h for h in doc.headings
        if h[1] == 3 and appendix_start < h[0] < appendix_end
    ]
    if [h[3] for h in appendix_h3] != allowed_appendix_h3:
        failures.add("appendix H3 headings/order must be Raw data, Coverage, traceability")
    other_h3 = [
        h for h in doc.headings
        if h[1] == 3 and h not in dimension_h3 and h not in appendix_h3
    ]
    for heading in other_h3:
        failures.add(f"unexpected H3 heading: {heading[3]}")

    if len(doc.fences) != 1:
        failures.add(f"report must contain exactly one code fence; found {len(doc.fences)}")
        return None
    fence = doc.fences[0]
    if fence["char"] != "`" or fence["info"] != "json":
        failures.add("the only code fence must be labelled exactly `json`")
    if fence["section"] != "## 本次分數存檔":
        failures.add("score JSON fence is outside `## 本次分數存檔`")
    return parse_json_text(fence["content"], "score JSON fence", failures)


def validate_section1(doc, score, prior, baseline, contract, failures):
    rows = find_table(
        doc.section_lines("## §1 六維度風險條圖"),
        contract["section1_header"], "§1", failures,
    )
    expected_names = [d["name"] for d in contract["dimensions"]] + ["加權總分"]
    names = [row[0].replace("**", "") for row in rows]
    if names != expected_names:
        failures.add(f"§1 row names/order mismatch: {names}")
        return None
    warning = contract["calibration"]["dimension_delta_warning_abs"]
    bar_cells = contract["calibration"]["bar_cells"]
    total_delta = None
    for row, dimension in zip(rows[:6], contract["dimensions"]):
        name, key = dimension["name"], dimension["key"]
        if row[2].endswith(" ◆") and key != "structural":
            failures.add("§1 ◆ marker is allowed only on 結構性槓桿")
        current = parse_current_score(row[2], f"§1 {name}", failures)
        if current is None:
            continue
        if current != score.get(key):
            failures.add(f"§1 {name} score {current} != score.json {score.get(key)}")
        check_bar(row[1], current, bar_cells, f"§1 {name}", failures)
        delta = parse_delta_cell(row[4], warning, f"§1 {name}", failures)
        if baseline:
            if row[3] != "—" or delta is not None:
                failures.add(f"baseline §1 {name} prior/delta must both be —")
        else:
            if not re.fullmatch(r"\d{1,3}", row[3]):
                failures.add(f"§1 {name} previous score has invalid format")
                continue
            previous = int(row[3])
            if previous != prior.get(key):
                failures.add(f"§1 {name} previous {previous} != prior score {prior.get(key)}")
            if isinstance(delta, int) and delta != current - previous:
                failures.add(f"§1 {name} delta {delta} != current - prior")

    if len(rows) != 7:
        return None
    total_row = rows[-1]
    total_match = re.fullmatch(r"\*\*(\d+)【([^】]+)】\*\*", total_row[2])
    if not total_match:
        failures.add("§1 total current cell has invalid score/tier format")
        return None
    total = int(total_match.group(1))
    tier = total_match.group(2)
    if total != score.get("total") or tier != score.get("tier"):
        failures.add("§1 total/tier does not match score.json")
    check_bar(total_row[1], total, bar_cells, "§1 加權總分", failures)
    total_delta = parse_delta_cell(total_row[4], warning, "§1 加權總分", failures)
    if baseline:
        if total_row[3] != "—" or total_delta is not None:
            failures.add("baseline §1 total prior/delta must both be —")
    else:
        previous_match = re.fullmatch(r"(?:\*\*)?(\d+)(?:【[^】]+】)?(?:\*\*)?", total_row[3])
        if not previous_match:
            failures.add("§1 total previous cell has invalid format")
        else:
            previous_total = int(previous_match.group(1))
            if previous_total != prior.get("total"):
                failures.add("§1 previous total does not match validated prior total")
            if isinstance(total_delta, int) and total_delta != total - previous_total:
                failures.add("§1 total delta != current total - prior total")
    return total_delta


def rounded_similarity(hits, count, step):
    raw_steps = (Decimal(hits) * Decimal(100)) / Decimal(count) / Decimal(step)
    return int(raw_steps.quantize(Decimal("1"), rounding=ROUND_HALF_UP) * step)


def nested_value(value, path):
    for key in path:
        if not isinstance(value, dict) or key not in value:
            return None
        value = value[key]
    return value


def trusted_macro_value(macro, path):
    """Read a rule value only from a block whose status makes it usable."""
    if not path:
        return None
    if path[0] == "series":
        if len(path) < 3:
            return None
        block = macro.get("series", {}).get(path[1], {})
        if block.get("status") not in ("ok", "derived"):
            return None
    else:
        block = macro.get(path[0], {})
        if not isinstance(block, dict):
            return None
        allowed = (
            ("ok", "partial") if path[0] == "repo_stress"
            else ("ok",)
        )
        if block.get("status") not in allowed:
            return None
    return nested_value(macro, path)


def rule_evidence_ids(rule):
    ids = set(rule.get("source_ids", []))
    for child in rule.get("rules", []):
        ids.update(rule_evidence_ids(child))
    return ids


def evaluate_anchor_rule(rule, score, macro, prior, baseline, contract):
    """Evaluate machine-known feature truth; None means evidence judgment."""
    kind = rule.get("type")
    if kind == "evidence":
        return None
    if kind == "score_between":
        value = score.get(rule["key"])
        return rule["min"] <= value <= rule["max"]
    if kind == "score_lt":
        return score.get(rule["key"]) < rule["value"]
    if kind == "score_gte":
        return score.get(rule["key"]) >= rule["value"]
    if kind == "score_delta_gte":
        if baseline or prior is None:
            return None
        return score.get(rule["key"]) - prior.get(rule["key"]) >= rule["value"]
    if kind == "trigger_eq":
        return score.get("trigger_state") == rule["value"]
    if kind == "trigger_gte":
        ranks = {state: i for i, state in enumerate(contract["trigger_states"])}
        return ranks.get(score.get("trigger_state"), -1) >= ranks[rule["value"]]
    if kind == "monetary_side_eq":
        return score.get("monetary_side") == rule["value"]
    if kind == "macro_equals":
        value = trusted_macro_value(macro, rule["path"])
        return None if value is None else value == rule["value"]
    if kind == "macro_compare":
        value = trusted_macro_value(macro, rule["path"])
        if type(value) not in (int, float) or not math.isfinite(value):
            return None
        target = rule["value"]
        return {
            "lt": value < target, "le": value <= target,
            "gt": value > target, "ge": value >= target,
            "eq": value == target,
        }[rule["op"]]
    if kind in ("all", "any"):
        results = [
            evaluate_anchor_rule(child, score, macro, prior, baseline, contract)
            for child in rule["rules"]
        ]
        if kind == "all":
            if False in results:
                return False
            return True if all(value is True for value in results) else None
        if True in results:
            return True
        return False if all(value is False for value in results) else None
    if kind == "high_retreat":
        if baseline or prior is None:
            return False
        prior_dev = prior.get("sp500_dev200_pct")
        current_dev = trusted_macro_value(macro, ["sp500_trend", "dev200_pct"])
        retreat = (
            type(prior_dev) in (int, float)
            and type(current_dev) in (int, float)
            and prior_dev > contract["calibration"]["sp500_high_deviation_pct"]
            and current_dev < prior_dev
        )
        chg = trusted_macro_value(macro, ["sp500_trend", "chg_pct"])
        return retreat or (type(chg) in (int, float) and chg <= -5)
    return None


def validate_section2_and_history(doc, summary, score, macro, prior, baseline,
                                  evidence, contract, failures):
    rows = find_table(
        doc.section_lines("## §2 歷史錨點相似度"),
        contract["section2_header"], "§2", failures,
    )
    names = [row[0] for row in rows]
    if names != contract["anchors"]:
        failures.add(f"§2 anchor names/order mismatch: {names}")
        return
    percentages = []
    marked = []
    step = contract["calibration"]["historical_similarity_step_pct"]
    for index, row in enumerate(rows):
        match = re.fullmatch(r"(\d{1,3})%", row[1])
        if not match:
            failures.add(f"§2 {row[0]} similarity format is invalid")
            percentages.append(None)
            continue
        percentage = int(match.group(1))
        percentages.append(percentage)
        if not 0 <= percentage <= 100 or percentage % step:
            failures.add(f"§2 {row[0]} similarity must be 0-100 on {step}% steps")
        check_bar(
            row[2], percentage, contract["calibration"]["bar_cells"],
            f"§2 {row[0]}", failures,
        )
        if row[3] == "◀ 最貼近":
            marked.append(index)
        elif row[3] != "":
            failures.add(f"§2 {row[0]} marker is invalid")
    if len(marked) != 1:
        failures.add("§2 must mark exactly one closest anchor")
    elif all(value is not None for value in percentages):
        expected_index = max(range(len(percentages)), key=lambda i: percentages[i])
        if marked[0] != expected_index:
            failures.add("§2 closest marker is not on the highest/first-tie anchor")
        if summary and (
            summary["anchor"] != contract["anchors"][marked[0]]
            or summary["similarity"] != percentages[marked[0]]
        ):
            failures.add("summary closest anchor does not match §2")

    history = [line.strip() for _, line in doc.section_lines("## 歷史泡沫週期對比") if line.strip()]
    if history.count("相似度計算：checklist v2") != 1:
        failures.add("historical section must contain exact `相似度計算：checklist v2`")
    audit_line_re = re.compile(
        r"^- ([A-Za-z0-9./]+)｜(命中|未命中|無資料)｜"
        r"source_ids=([^｜]+)｜(.+)$"
    )
    parsed_features = {}
    parsed_feature_order = []
    for line in history:
        match = audit_line_re.fullmatch(line)
        if match:
            parsed_features.setdefault(match.group(1), []).append(match.groups()[1:])
            parsed_feature_order.append(match.group(1))
    expected_feature_ids = {
        feature["id"] for anchor in contract["anchors"]
        for feature in contract["anchor_features"][anchor]
    }
    unknown_feature_ids = set(parsed_features) - expected_feature_ids
    if unknown_feature_ids:
        failures.add(f"historical audit has unknown feature IDs: {sorted(unknown_feature_ids)}")
    expected_feature_order = [
        feature["id"] for anchor in contract["anchors"]
        for feature in contract["anchor_features"][anchor]
    ]
    if parsed_feature_order != expected_feature_order:
        failures.add("historical feature audit lines are missing/reordered/duplicated")
    feature_headings = [
        line for line in history
        if re.fullmatch(r"\*\*.+ feature audit\*\*", line)
    ]
    expected_feature_headings = [
        f"**{anchor} feature audit**" for anchor in contract["anchors"]
    ]
    if feature_headings != expected_feature_headings:
        failures.add("historical feature-audit headings are missing or out of order")

    summary_values = {}
    machine_retreat = False
    for anchor in contract["anchors"]:
        pattern = re.compile(
            rf"^- {re.escape(anchor)}：命中 (\d+)/(\d+) = (\d+)%$"
        )
        matches = [pattern.fullmatch(line) for line in history]
        matches = [match for match in matches if match]
        if len(matches) != 1:
            failures.add(f"historical section needs one exact audit summary for {anchor}")
            continue
        declared_hits, count, percentage = map(int, matches[0].groups())
        expected_count = contract["anchor_feature_counts"][anchor]
        if count != expected_count or not 0 <= declared_hits <= count:
            failures.add(f"historical audit count for {anchor} is invalid")
            continue
        actual_hits = 0
        for feature in contract["anchor_features"][anchor]:
            feature_id = feature["id"]
            entries = parsed_features.get(feature_id, [])
            if len(entries) != 1:
                failures.add(f"historical feature {feature_id} needs one exact audit line")
                continue
            status, source_text, _detail = entries[0]
            source_ids = [] if source_text == "—" else source_text.split(",")
            if len(source_ids) != len(set(source_ids)):
                failures.add(f"historical feature {feature_id} repeats source IDs")
            allowed_sources = rule_evidence_ids(feature["rule"])
            if not set(source_ids) <= allowed_sources:
                failures.add(f"historical feature {feature_id} cites disallowed source IDs")
            known = evaluate_anchor_rule(
                feature["rule"], score, macro, prior, baseline, contract
            )
            if known is True and status != "命中":
                failures.add(f"historical feature {feature_id} contradicts machine truth")
            elif known is False and status != "未命中":
                failures.add(f"historical feature {feature_id} contradicts machine truth")
            elif known is None:
                positive_allowed = {
                    source_id for source_id in allowed_sources
                    if evidence["success"].get(source_id)
                }
                available_allowed = {
                    source_id for source_id in allowed_sources
                    if evidence["available"].get(source_id)
                }
                if status == "命中" and (
                        not source_ids or not set(source_ids) <= positive_allowed):
                    failures.add(
                        f"historical feature {feature_id} hit lacks successful evidence"
                    )
                if status == "未命中" and (
                        not source_ids or not set(source_ids) <= available_allowed):
                    failures.add(
                        f"historical feature {feature_id} miss lacks completed evidence"
                    )
                if status == "無資料" and available_allowed:
                    failures.add(
                        f"historical feature {feature_id} says 無資料 despite evidence"
                    )
                if status == "無資料" and source_ids:
                    failures.add(f"historical feature {feature_id} 無資料 must cite —")
                if not available_allowed and status != "無資料":
                    failures.add(
                        f"historical feature {feature_id} has no completed evidence and must be 無資料"
                    )
            if status == "命中":
                actual_hits += 1
            if feature_id == "2000.4":
                machine_retreat = known is True
        if declared_hits != actual_hits:
            failures.add(
                f"historical audit {anchor} declares {declared_hits} hits; feature lines yield {actual_hits}"
            )
        expected_percentage = rounded_similarity(actual_hits, count, step)
        if percentage != expected_percentage:
            failures.add(f"historical audit arithmetic for {anchor} is invalid")
        summary_values[anchor] = percentage
    if len(summary_values) == len(rows):
        for row, percentage in zip(rows, percentages):
            if percentage is not None and summary_values.get(row[0]) != percentage:
                failures.add(f"historical audit {row[0]} does not match §2")

    audit_label = contract["historical_audit_labels"][0]
    audit_matches = [
        re.fullmatch(rf"{re.escape(audit_label)}：(是|否)", line) for line in history
    ]
    audit_matches = [match for match in audit_matches if match]
    if len(audit_matches) != 1:
        failures.add(f"historical section needs exact `{audit_label}：是|否`")
    else:
        expected = "是" if machine_retreat else "否"
        if audit_matches[0].group(1) != expected:
            failures.add(f"{audit_label} does not match persisted/macro inputs")


def triangle_fallback_level(spec, evidence, failures):
    """Read a search fallback spot from one auditable traceability marker."""
    source_id = spec["source_id"]
    if evidence["coverage_tokens"].get(source_id) != "✓ SEARCH-VERIFIED":
        failures.add(f"triangle fallback {source_id} requires SEARCH-VERIFIED Coverage")
        return None
    matches = []
    pattern = re.compile(
        r"^\[triangle_fallback\]\s+" + re.escape(spec["component"])
        + r"\s+fallback_value=([+−-]?\d+(?:\.\d+)?)$"
    )
    for row in evidence["traces_by_id"].get(source_id, []):
        match = pattern.fullmatch(row[1])
        if match and contains_valid_http_url(row[3]):
            matches.append(match)
    if len(matches) != 1:
        failures.add(
            f"triangle fallback {source_id} needs one exact [triangle_fallback] trace"
        )
        return None
    try:
        return float(matches[0].group(1).replace("−", "-"))
    except ValueError:
        failures.add(f"triangle fallback {source_id} value is invalid")
        return None


def validate_triangle(doc, score, summary, macro, prior, baseline, evidence,
                      contract, failures):
    section = doc.section_lines("## §3 三角訊號")
    rows = find_table(section, contract["section3_header"], "§3", failures)
    if [row[0] for row in rows] != contract["triangle_indicators"]:
        failures.add(f"§3 indicator rows/order mismatch: {[row[0] for row in rows]}")
        return None
    regime, directions = expected_regime(macro, baseline, contract)
    series = macro.get("series", {})
    sp500 = macro.get("sp500_trend", {})
    decomposition = macro.get("decomposition", {})
    expected_levels = [
        trusted_macro_value(macro, ["sp500_trend", "latest"]),
        trusted_macro_value(macro, ["series", "DCOILWTICO", "latest"]),
        trusted_macro_value(macro, ["series", "DGS10", "latest"]),
    ]
    display_levels = list(expected_levels)
    for index, spec in enumerate(contract["triangle_fallbacks"]):
        if not finite_number(display_levels[index]):
            display_levels[index] = triangle_fallback_level(
                spec, evidence, failures
            )
    expected_priors = [
        trusted_macro_value(macro, ["sp500_trend", "prior_spot"]),
        trusted_macro_value(macro, ["series", "DCOILWTICO", "prior"]),
        trusted_macro_value(macro, ["series", "DGS10", "prior"]),
    ]
    keys = ["sp500", "wti", "dgs10"]
    no_new = [
        bool(sp500.get("no_new_obs")),
        bool(series.get("DCOILWTICO", {}).get("no_new_obs")),
        bool(series.get("DGS10", {}).get("no_new_obs")),
    ]
    changes = [
        trusted_macro_value(macro, ["sp500_trend", "chg_pct"]),
        trusted_macro_value(macro, ["series", "DCOILWTICO", "chg_pct"]),
        trusted_decomposition_leg(macro, "d_dgs10_bps"),
    ]
    for index, row in enumerate(rows):
        if row[1] in ("", "—"):
            failures.add(f"§3 {row[0]} current value is empty")
        expected_level = display_levels[index]
        if type(expected_level) in (int, float):
            if not displayed_matches(row[1], expected_level):
                failures.add(f"§3 {row[0]} level does not match macro/fallback evidence")
        elif row[1] != "不可用":
            failures.add(f"§3 {row[0]} unavailable level must use exact `不可用`")
        if baseline:
            if row[2] != "基準日（無前次可比）":
                failures.add(f"baseline §3 {row[0]} comparison must use locked baseline text")
            continue
        expected_direction = directions[keys[index]]
        if not direction_cell_matches(row[2], expected_direction, no_new[index]):
            failures.add(f"§3 {row[0]} direction does not match macro threshold")
        if expected_direction is not None and type(changes[index]) in (int, float):
            unit = "%" if index < 2 else "bps"
            match = re.search(
                rf"([+−-]?\d[\d,]*(?:\.\d+)?)\s*{re.escape(unit)}", row[2]
            )
            if not match or not displayed_matches(match.group(1), changes[index]):
                failures.add(f"§3 {row[0]} displayed change does not match macro JSON")
        expected_prior = expected_priors[index]
        if type(expected_prior) in (int, float):
            prior_match = re.search(r"前次\s*(.+?)(?:）|$)", row[2])
            if not prior_match or not displayed_matches(
                    prior_match.group(1), expected_prior):
                failures.add(f"§3 {row[0]} previous level does not match macro JSON")

    visible = [line.strip() for _, line in section if line.strip()]
    label_positions = []
    label_lines = {}
    label_warnings = {}
    for label in contract["triangle_labels"]:
        pattern = re.compile(
            rf"^(⚠ )?\*\*{re.escape(label)}\*\*：(.*)$"
        )
        matches = [(i, pattern.fullmatch(line)) for i, line in enumerate(visible)]
        matches = [(i, match) for i, match in matches if match]
        if len(matches) != 1:
            failures.add(f"§3 needs exactly one visible `{label}` label")
            continue
        label_positions.append(matches[0][0])
        label_warnings[label] = bool(matches[0][1].group(1))
        label_lines[label] = matches[0][1].group(2).strip()
    if len(label_positions) == len(contract["triangle_labels"]) and label_positions != sorted(label_positions):
        failures.add("§3 interpretation labels are out of order")

    bullet_names = []
    bullet_text = {}
    bullet_positions = []
    for position, line in enumerate(visible):
        match = re.fullmatch(r"- (股市|WTI 原油|10Y 殖利率)：(.+)", line)
        if match:
            bullet_names.append(match.group(1))
            bullet_text[match.group(1)] = match.group(2)
            bullet_positions.append(position)
    if bullet_names != ["股市", "WTI 原油", "10Y 殖利率"]:
        failures.add("§3 三者狀態 must contain the three locked indicator bullets in order")
    else:
        state_position = next((i for i, line in enumerate(visible)
                               if re.match(r"^(?:⚠ )?\*\*三者狀態\*\*：", line)), -1)
        transition_position = next((i for i, line in enumerate(visible)
                                    if re.match(r"^(?:⚠ )?\*\*格局轉變\*\*：", line)), -1)
        if not all(state_position < pos < transition_position for pos in bullet_positions):
            failures.add("§3 indicator bullets must immediately belong to 三者狀態")
        for bullet_index, (label, key) in enumerate(zip(
            ("股市", "WTI 原油", "10Y 殖利率"),
            ("sp500", "wti", "dgs10"),
        )):
            text = bullet_text[label]
            expected_display = display_levels[bullet_index]
            if finite_number(expected_display):
                if not displayed_matches(text, expected_display):
                    failures.add(
                        f"§3 {label} bullet lacks the macro/fallback current value"
                    )
            elif "水位不可用" not in text:
                failures.add(f"§3 {label} bullet must disclose 水位不可用")
            if baseline:
                if "基準日" not in text:
                    failures.add(f"baseline §3 {label} bullet must say 基準日")
            else:
                required_token = {
                    "up": "▲", "down": "▼", "flat": "持平", None: "方向不可用",
                }[directions[key]]
                if required_token not in text:
                    failures.add(f"§3 {label} bullet direction conflicts with its table row")
                if type(changes[bullet_index]) in (int, float) and not displayed_matches(
                        text[text.find(required_token) + len(required_token):],
                        changes[bullet_index]):
                    failures.add(f"§3 {label} bullet lacks the macro change amplitude")

    state_line = label_lines.get("三者狀態", "")
    regime_term = {
        "穩定共存": "穩定共存", "同向偏高": "同向偏高",
        "分歧": "分歧", "基準日": "基準日", "不可判": "不可判",
    }[regime]
    if regime_term not in state_line:
        failures.add("§3 三者狀態 does not match macro-derived regime")
    if score.get("regime") != regime:
        failures.add(f"score.json regime {score.get('regime')!r} != derived {regime!r}")

    transition_line = label_lines.get("格局轉變", "")
    if baseline or prior.get("regime") is None:
        if "前次無格局紀錄" not in transition_line:
            failures.add("§3 格局轉變 must disclose that prior regime is unavailable")
    else:
        visible_current = regime
        if prior.get("regime") not in transition_line or visible_current not in transition_line:
            failures.add("§3 格局轉變 does not contain prior and current regimes")

    decomposition_line = label_lines.get("10Y 成因拆解", "")
    driver = decomposition.get("driver")
    decomposition_status = decomposition.get("status")
    freshness = decomposition.get("freshness")
    leg_specs = [
        ("ΔDGS10 名目殖利率週變動", trusted_decomposition_leg(macro, "d_dgs10_bps")),
        ("ΔDFII10 實質殖利率週變動", trusted_decomposition_leg(macro, "d_dfii10_bps")),
        ("ΔT10YIE 損益平衡通膨週變動", trusted_decomposition_leg(macro, "d_t10yie_bps")),
    ]
    decomposition_bullets = {}
    for line in visible:
        for name, _expected in leg_specs:
            match = re.fullmatch(rf"- {re.escape(name)}：(.+)", line)
            if match:
                decomposition_bullets.setdefault(name, []).append(match.group(1))
    for name, expected in leg_specs:
        values = decomposition_bullets.get(name, [])
        if len(values) != 1:
            failures.add(f"§3 decomposition needs one `{name}` bullet")
            continue
        value_text = values[0]
        if baseline:
            if value_text != "基準日":
                failures.add(f"baseline {name} must say 基準日")
        elif type(expected) in (int, float):
            if "bps" not in value_text or not displayed_matches(value_text, expected):
                failures.add(f"§3 {name} does not match macro decomposition")
        elif value_text != "不可用（無日序資料）":
            failures.add(f"§3 {name} missing unavailable-history wording")
    if baseline:
        if driver != "baseline" or "基準日" not in decomposition_line:
            failures.add("baseline 10Y decomposition is not labelled as baseline")
    elif decomposition_status == "unavailable_no_daily_history":
        if decomposition_line != "本週 Δ 分解不可用——無日序資料":
            failures.add("unavailable decomposition needs the locked no-history wording")
    elif driver == "none":
        if "無變動" not in decomposition_line:
            failures.add("zero-delta decomposition must say 無變動")
        if ("無新觀測" in decomposition_line) != (freshness == "all_stale"):
            failures.add("decomposition no-new-observation wording conflicts with freshness")
    elif driver == "unknown" and "不可判" not in decomposition_line:
        failures.add("unknown decomposition driver must say 不可判")
    elif driver in ("real-rate", "breakeven", "mixed") and driver not in decomposition_line:
        failures.add("10Y decomposition label does not match macro driver")
    freshness_lines = [line for line in visible if line.startswith("- 觀測新鮮度：")]
    if freshness == "partial_stale":
        expected_stale = ",".join(decomposition.get("stale_series", []))
        exact = f"- 觀測新鮮度：部分未更新（stale_series={expected_stale}）"
        if freshness_lines != [exact]:
            failures.add("partial-stale decomposition must list exact stale_series")
    elif freshness_lines:
        failures.add("觀測新鮮度 bullet is only allowed for partial_stale")

    trigger_chain = label_lines.get("扳機鏈", "")
    if not trigger_chain or "A 通膨鏈" not in trigger_chain or "B 槓桿鏈" not in trigger_chain:
        failures.add("§3 扳機鏈 must contain nonempty A/B chain assessments")
    for requirement in contract["triangle_chain_inputs"]:
        source_id = requirement["source_id"]
        series_id = requirement["series"]
        block = series.get(series_id, {})
        prefix = rf"\[{re.escape(source_id)}\]\s+{re.escape(series_id)}\s+"
        if block.get("status") in ("ok", "derived"):
            value_field = requirement["value_field"]
            delta_field = requirement["delta_field"]
            pattern = prefix + re.escape(value_field) + (
                r"=([+−-]?\d+(?:\.\d+)?)\s+"
                + (re.escape(delta_field)
                   + r"=([+−-]?\d+(?:\.\d+)?|基準日|不可用)\s+"
                   if delta_field else "")
                + rf"data_date=({DATE_RE})"
            )
            matches = list(re.finditer(pattern, trigger_chain))
            if len(matches) != 1:
                failures.add(
                    f"§3 A-chain needs one exact marker for {source_id}/{series_id}"
                )
                continue
            match = matches[0]
            if not displayed_matches(match.group(1), block.get(value_field)):
                failures.add(
                    f"§3 A-chain {series_id}.{value_field} != macro JSON"
                )
            date_group = 3 if delta_field else 2
            if match.group(date_group) != block.get("latest_date"):
                failures.add(f"§3 A-chain {series_id} data_date != macro JSON")
            if delta_field:
                rendered_delta = match.group(2)
                expected_delta = block.get(delta_field)
                if finite_number(expected_delta):
                    if not displayed_matches(rendered_delta, expected_delta):
                        failures.add(
                            f"§3 A-chain {series_id}.{delta_field} != macro JSON"
                        )
                else:
                    expected_text = "基準日" if baseline else "不可用"
                    if rendered_delta != expected_text:
                        failures.add(
                            f"§3 A-chain {series_id}.{delta_field} needs {expected_text}"
                        )
        else:
            token = evidence["coverage_tokens"].get(source_id)
            pattern = prefix + re.escape(token or "") + r"\s+不納入判讀"
            if len(re.findall(pattern, trigger_chain)) != 1:
                failures.add(
                    f"§3 A-chain missing input {source_id}/{series_id} "
                    "lacks exact Coverage disclosure"
                )

    reason_line = label_lines.get("扳機理由", "")
    visible_reasons = [] if reason_line == "none" else reason_line.split("、")
    if visible_reasons != score.get("trigger_reasons"):
        failures.add("§3 扳機理由 does not match score.json trigger_reasons")

    conclusion = label_lines.get("結論", "")
    trigger_match = re.search(
        "扳機狀態：(" + "|".join(map(re.escape, contract["trigger_states"])) + ")",
        conclusion,
    )
    trigger = trigger_match.group(1) if trigger_match else None
    if trigger is None:
        failures.add("§3 conclusion lacks a valid trigger state")
    else:
        if not conclusion.startswith(f"扳機狀態：{trigger}"):
            failures.add("§3 conclusion must begin with its trigger-state label")
        if score.get("trigger_state") != trigger:
            failures.add("score.json trigger_state != §3 conclusion")
        if summary and summary["trigger"] != trigger:
            failures.add("summary trigger state != §3 conclusion")
    expected_warning = trigger == "已擊發" or regime == "同向偏高"
    for label, warned in label_warnings.items():
        if label != "結論" and warned:
            failures.add(f"§3 ⚠ prefix is forbidden on {label}")
    if label_warnings.get("結論", False) != expected_warning:
        failures.add("§3 結論 ⚠ prefix does not match trigger/regime rule")
    return trigger


def validate_dimensions(doc, score, prior, baseline, report_day, evidence,
                        macro, contract, failures):
    start = next((h[0] for h in doc.headings if h[3] == "## 六維度評分"), None)
    end = next((h[0] for h in doc.headings if h[3] == "## 綜合分數"), None)
    if start is None or end is None:
        return None
    h3s = [h for h in doc.headings if h[1] == 3 and start < h[0] < end]
    if len(h3s) != 6:
        failures.add(f"六維度評分 must contain exactly six H3 subsections; found {len(h3s)}")
        return None
    monetary_side = None
    for index, (heading, dimension) in enumerate(zip(h3s, contract["dimensions"]), 1):
        expected_delta = "—" if baseline else str(score[dimension["key"]] - prior[dimension["key"]])
        if expected_delta not in ("—", "0") and int(expected_delta) > 0:
            expected_delta = "+" + expected_delta
        pattern = re.compile(
            rf"^### {index}\. {re.escape(dimension['name'])} — (\d+)"
            rf"（weight (\d+)%，Δ (—|0|[+−-]\d+)）$"
        )
        match = pattern.fullmatch(heading[3])
        if not match:
            failures.add(f"dimension H3 format mismatch: {heading[3]}")
            continue
        if int(match.group(1)) != score[dimension["key"]]:
            failures.add(f"dimension H3 score mismatch for {dimension['name']}")
        if int(match.group(2)) != dimension["weight"]:
            failures.add(f"dimension H3 weight mismatch for {dimension['name']}")
        if match.group(3).replace("−", "-") != expected_delta:
            failures.add(f"dimension H3 delta mismatch for {dimension['name']}")
        block_end = h3s[index][0] if index < len(h3s) else end
        block = [
            line.strip() for line_no, line in doc.visible
            if heading[0] < line_no < block_end and line.strip()
        ]
        bullets = [line for line in block if line.startswith("- ")]
        if not bullets:
            failures.add(f"dimension {dimension['name']} has no scoring-input bullet")
        for bullet in bullets:
            source_match = re.search(
                r"(?:^|[；，,（(\s])source_ids=([a-z][a-z0-9_.]*(?:,[a-z][a-z0-9_.]*)*)",
                bullet,
            )
            if not source_match:
                failures.add(
                    f"dimension {dimension['name']} bullet lacks exact source_ids linkage"
                )
                source_ids = []
            else:
                source_ids = source_match.group(1).split(",")
                if len(source_ids) != len(set(source_ids)) or any(
                        source_id not in evidence["coverage_tokens"]
                        for source_id in source_ids):
                    failures.add(
                        f"dimension {dimension['name']} bullet has invalid source_ids"
                    )
            if "✗ NOT DISCLOSED" in bullet or "⛔ FETCH FAILED" in bullet:
                if "不納入計分" not in bullet:
                    failures.add(
                        f"dimension {dimension['name']} missing-data bullet must say 不納入計分"
                    )
                for source_id in source_ids:
                    expected_token = evidence["coverage_tokens"].get(source_id)
                    if expected_token not in ("✗ NOT DISCLOSED", "⛔ FETCH FAILED") \
                            or expected_token not in bullet:
                        failures.add(
                            f"dimension {dimension['name']} missing bullet status/source mismatch"
                        )
                continue
            if not re.search(r"\d", bullet):
                failures.add(f"dimension {dimension['name']} has a non-concrete bullet")
            dates = re.findall(DATE_RE, bullet)
            if not dates:
                failures.add(f"dimension {dimension['name']} bullet lacks a data date")
            else:
                bullet_day = strict_date(
                    dates[-1], f"dimension {dimension['name']} bullet date", failures
                )
                if bullet_day and report_day and bullet_day > report_day:
                    failures.add(f"dimension {dimension['name']} bullet date is in the future")
            if not (
                contains_valid_http_url(bullet)
                or re.search(r"\b[A-Z][A-Z0-9.^_-]{1,}\b", bullet)
            ):
                failures.add(f"dimension {dimension['name']} bullet lacks a source ID/URL")
            for source_id in source_ids:
                candidates = [
                    (extract_number(row[2]), row[4])
                    for row in evidence["raw_by_id"].get(source_id, [])
                ] + [
                    (extract_trace_evidence_number(row[1]), row[4])
                    for row in evidence["traces_by_id"].get(source_id, [])
                ]
                linked = False
                for value, data_date in candidates:
                    if (value is not None and data_date in bullet
                            and displayed_contains(bullet, value)):
                        linked = True
                        break
                if not linked:
                    failures.add(
                        f"dimension {dimension['name']} bullet value/date is not linked "
                        f"to appendix evidence for {source_id}"
                    )
        if dimension["key"] in contract["dimension_required_inputs"]:
            requirements = contract["dimension_required_inputs"][dimension["key"]]
            for requirement in requirements:
                source_id = requirement["source_id"]
                indicator = requirement["indicator"]
                matching = [
                    bullet for bullet in bullets
                    if re.search(
                        rf"(?:^|[;；，,（(\s])source_ids=(?:"
                        rf"[a-z][a-z0-9_.]*,)*{re.escape(source_id)}"
                        rf"(?:,[a-z][a-z0-9_.]*)*(?=$|[^a-z0-9_.])",
                        bullet,
                    ) and (indicator is None or indicator in bullet)
                ]
                macro_block = (
                    macro.get("series", {}).get(indicator, {})
                    if indicator in macro.get("series", {}) else None
                ) if indicator is not None else None
                component_ok = (
                    isinstance(macro_block, dict)
                    and macro_block.get("status") in ("ok", "derived")
                )
                source_ok = evidence["available"].get(source_id)
                # A failed API component can still be satisfied by an
                # auditable SEARCH-VERIFIED fallback for the same source.
                should_have_value = bool(component_ok or source_ok)
                if len(matching) != 1:
                    failures.add(
                        f"dimension {dimension['name']} needs one required input bullet "
                        f"for {source_id}/{indicator or 'source'}"
                    )
                    continue
                required_bullet = matching[0]
                if should_have_value:
                    candidates = [
                        (extract_number(row[2]), row[4])
                        for row in evidence["raw_by_id"].get(source_id, [])
                        if (indicator is None
                            or mentions_identifier(row[1], indicator)
                            or mentions_identifier(row[3], indicator))
                    ] + [
                        (extract_trace_evidence_number(row[1]), row[4])
                        for row in evidence["traces_by_id"].get(source_id, [])
                        if (indicator is None
                            or mentions_identifier(row[1], indicator)
                            or mentions_identifier(row[2], indicator))
                    ]
                    if not any(
                            data_date in required_bullet
                            and value is not None
                            and displayed_contains(required_bullet, value)
                            for value, data_date in candidates):
                        failures.add(
                            f"dimension {dimension['name']} required input {source_id}/"
                            f"{indicator or 'source'} lacks its appendix value/date"
                        )
                else:
                    token = evidence["coverage_tokens"].get(source_id)
                    if (token is None or token not in required_bullet
                            or "不納入計分" not in required_bullet):
                        failures.add(
                            f"dimension {dimension['name']} missing required input "
                            f"{source_id}/{indicator or 'source'} lacks status disclosure"
                        )
        conclusions = [line for line in block if line.startswith("**結論**：")]
        if len(conclusions) != 1:
            failures.add(f"dimension {dimension['name']} needs exactly one conclusion")
        elif block[-1] != conclusions[0]:
            failures.add(f"dimension {dimension['name']} conclusion must be its final line")
        if dimension["key"] == "monetary" and len(conclusions) == 1:
            side_pattern = "|".join(map(re.escape, contract["monetary_sides"]))
            side_match = re.fullmatch(
                rf"\*\*結論\*\*：({side_pattern})；.+", conclusions[0]
            )
            hits = [side_match.group(1)] if side_match else []
            if len(hits) != 1:
                failures.add("D5 conclusion must contain exactly one monetary side")
            else:
                monetary_side = hits[0]
                if score.get("monetary_side") != monetary_side:
                    failures.add("score.json monetary_side != D5 conclusion")
    return monetary_side


def validate_weighted_section(doc, score, contract, failures):
    section = doc.section_lines("## 綜合分數")
    rows = find_table(section, contract["weighted_score_header"], "綜合分數", failures)
    if [row[0] for row in rows] != [d["name"] for d in contract["dimensions"]]:
        failures.add("weighted-score row names/order mismatch")
    for row, dimension in zip(rows, contract["dimensions"]):
        if row[1] != f"{dimension['weight']}%":
            failures.add(f"weighted-score weight mismatch for {dimension['name']}")
        if row[2] != str(score[dimension["key"]]):
            failures.add(f"weighted-score score mismatch for {dimension['name']}")
        expected = Decimal(score[dimension["key"]] * dimension["weight"]) / Decimal(100)
        if not re.fullmatch(r"\d+\.\d{2}", row[3]):
            failures.add(f"weighted component format invalid for {dimension['name']}")
        elif Decimal(row[3]) != expected.quantize(Decimal("0.01")):
            failures.add(f"weighted component mismatch for {dimension['name']}")
    _, raw_total = weighted_total(score, contract)
    summary_line = f"加權總分：{raw_total:.2f} → {score['total']}【{score['tier']}】"
    visible = [line.strip() for _, line in section if line.strip()]
    if visible.count(summary_line) != 1:
        failures.add(f"weighted section needs exact `{summary_line}`")

    distance = contract["calibration"]["tier_boundary_distance"]
    boundaries = [item["min"] for item in contract["tiers"]][1:]
    needs_boundary = any(boundary - distance <= score["total"] <= boundary + distance - 1
                         for boundary in boundaries)
    boundary_lines = [line for line in visible if line.startswith("邊界帶：")]
    if needs_boundary and len(boundary_lines) != 1:
        failures.add("weighted total near a tier boundary requires one 邊界帶 note")
    if not needs_boundary and boundary_lines:
        failures.add("邊界帶 note is present outside a contract boundary band")


def active_machine_trigger_reasons(score, macro, baseline, monetary_side, contract):
    if baseline:
        return set()
    active = set()
    hy_delta = trusted_macro_value(
        macro, ["series", "BAMLH0A0HYM2", "delta_bps"]
    )
    if (type(hy_delta) in (int, float)
            and hy_delta >= contract["calibration"]["hy_oas_fired_delta_bps"]):
        active.add("hy_oas_fired")
    streak = score.get("hy_oas_widening_streak")
    if (type(streak) is int
            and streak >= contract["calibration"]["hy_oas_initial_widening_streak"]):
        active.add("hy_streak")
    decomposition = macro.get("decomposition", {})
    wti_change = trusted_macro_value(
        macro, ["series", "DCOILWTICO", "chg_pct"]
    )
    dgs_change = trusted_macro_value(
        macro, ["decomposition", "d_dgs10_bps"]
    )
    if (trusted_macro_value(macro, ["decomposition", "driver"]) == "breakeven"
            and direction(dgs_change, contract["direction_thresholds"]["dgs10_delta_bps"]) == "up"
            and direction(wti_change, contract["direction_thresholds"]["wti_chg_pct"]) == "up"):
        active.add("breakeven_wti_up")
    term_delta = trusted_macro_value(
        macro, ["series", "THREEFYTP10", "delta_bps"]
    )
    move_delta = trusted_macro_value(macro, ["move_index", "delta_abs"])
    repo_spread = trusted_macro_value(
        macro, ["repo_stress", "sofr_iorb_bps"]
    )
    funding = (
        type(move_delta) in (int, float) and move_delta > 0
    ) or (
        type(repo_spread) in (int, float) and repo_spread >= 0
    )
    if (type(term_delta) in (int, float)
            and term_delta >= contract["calibration"]["term_premium_initial_delta_bps"]
            and funding):
        active.add("term_premium_funding")
    return active


def validate_state_fields(score, macro, prior, baseline, monetary_side, trigger,
                          evidence, contract, failures):
    if score.get("timezone") != contract["timezone"]:
        failures.add("score.json timezone does not match contract")
    if score.get("regime") not in contract["regimes"]:
        failures.add("score.json regime is invalid")
    if score.get("trigger_state") not in contract["trigger_states"]:
        failures.add("score.json trigger_state is invalid")
    if score.get("monetary_side") not in contract["monetary_sides"]:
        failures.add("score.json monetary_side is invalid")
    streak = score.get("hy_oas_widening_streak")
    valid_streak = type(streak) is int and streak >= 0
    if not valid_streak:
        failures.add("score.json hy_oas_widening_streak must be a nonnegative integer")
    current_dev = score.get("sp500_dev200_pct")
    if current_dev is not None and (
            type(current_dev) not in (int, float) or not math.isfinite(current_dev)):
        failures.add("score.json sp500_dev200_pct must be finite numeric or null")

    macro_dev = trusted_macro_value(macro, ["sp500_trend", "dev200_pct"])
    expected_dev = macro_dev if type(macro_dev) in (int, float) else None
    if current_dev != expected_dev:
        failures.add("score.json sp500_dev200_pct != macro sp500_trend.dev200_pct")

    delta = trusted_macro_value(
        macro, ["series", "BAMLH0A0HYM2", "delta_bps"]
    )
    previous_streak = 0 if baseline else prior.get("hy_oas_widening_streak", 0)
    expected_streak = previous_streak + 1 if type(delta) in (int, float) and delta > 0 else 0
    if streak != expected_streak:
        failures.add(f"score.json HY widening streak {streak} != {expected_streak}")

    reasons = score.get("trigger_reasons")
    if not isinstance(reasons, list):
        return
    machine_active = active_machine_trigger_reasons(
        score, macro, baseline, monetary_side, contract
    )
    configured = contract["trigger_reason_codes"]
    declared_machine = {
        reason for reason in reasons
        if reason in configured and configured[reason]["kind"] == "machine"
    }
    if declared_machine != machine_active:
        failures.add(
            f"score.json machine trigger reasons {sorted(declared_machine)} "
            f"!= active {sorted(machine_active)}"
        )

    report_day = date.fromisoformat(score["date"])

    def qualifying_evidence(rule):
        tag = rule["evidence_tag"]
        allowed_sources = set(rule["source_ids"])
        raw_matches = [
            (source_id, row) for source_id, rows in evidence["raw_by_id"].items()
            for row in rows
            if row[1].startswith(tag) and contains_valid_http_url(row[3])
        ]
        trace_matches = [
            (source_id, row) for source_id, rows in evidence["traces_by_id"].items()
            for row in rows
            if row[1].startswith(tag) and contains_valid_http_url(row[3])
        ]
        tagged = trace_matches if rule.get("trace_required") else raw_matches + trace_matches
        eligible = [
            (source_id, row) for source_id, row in tagged
            if source_id in allowed_sources and evidence["success"].get(source_id)
        ]
        max_age = int(rule["window"][:-1])
        in_window = []
        for source_id, row in eligible:
            try:
                evidence_day = date.fromisoformat(row[4])
            except (TypeError, ValueError):
                continue
            if report_day - timedelta(days=max_age) <= evidence_day <= report_day:
                in_window.append((source_id, row))
        prerequisite = rule.get("prerequisite")
        prerequisite_ok = not prerequisite or evaluate_anchor_rule(
            prerequisite, score, macro, prior, baseline, contract
        ) is True
        return in_window if prerequisite_ok else []

    active_evidence = {
        code for code, rule in configured.items()
        if rule["kind"] == "evidence" and qualifying_evidence(rule)
    }
    declared_evidence = {
        reason for reason in reasons
        if reason in configured and configured[reason]["kind"] == "evidence"
    }
    if declared_evidence != active_evidence:
        failures.add(
            f"score.json evidence trigger reasons {sorted(declared_evidence)} "
            f"!= active tagged evidence {sorted(active_evidence)}"
        )
    for reason in declared_evidence:
        rule = configured[reason]
        eligible = qualifying_evidence(rule)
        if not eligible:
            required_kind = "trace" if rule.get("trace_required") else "raw/trace"
            failures.add(
                f"trigger reason {reason} lacks tagged in-window {required_kind} evidence"
            )
        prerequisite = rule.get("prerequisite")
        if prerequisite and evaluate_anchor_rule(
                prerequisite, score, macro, prior, baseline, contract) is not True:
            failures.add(f"trigger reason {reason} fails its machine prerequisite")
    ranks = {state: index for index, state in enumerate(contract["trigger_states"])}
    expected_state = "未擊發"
    for reason in reasons:
        rule = configured.get(reason)
        if rule and ranks[rule["state"]] > ranks[expected_state]:
            expected_state = rule["state"]
    if monetary_side == "扳機側" and expected_state == "未擊發":
        failures.add(
            "D5 扳機側 requires an independently validated trigger reason"
        )
    if trigger != expected_state or score.get("trigger_state") != expected_state:
        failures.add(
            f"deterministic trigger state must be {expected_state}, not {trigger!r}"
        )


def validate_new_signals(doc, score, prior, macro, baseline, monetary_side,
                         report_day, contract, failures):
    visible = [line.strip() for _, line in doc.section_lines("## 本次新增訊號") if line.strip()]
    body = "\n".join(visible)
    if not body:
        failures.add("本次新增訊號 section is empty")
        return
    structural_rows = find_table(
        doc.section_lines("## §1 六維度風險條圖"),
        contract["section1_header"], "§1 marker cross-check", failures,
    )
    has_global_marker = any(
        row[0] == "結構性槓桿" and row[2].endswith(" ◆")
        for row in structural_rows
    )
    mentions_global = "全球槓桿擴散訊號" in body
    if has_global_marker != mentions_global:
        failures.add("§1 ◆ marker and 本次新增訊號 global-leverage disclosure disagree")
    if baseline:
        if "基準日" not in body:
            failures.add("baseline new-signals section must say 基準日")
        return
    prior_date_text = prior.get("date") or macro.get("prior_run_date")
    prior_day = (
        strict_date(prior_date_text, "effective prior date", failures)
        if prior_date_text and prior_date_text != "none" else None
    )
    if report_day and prior_day:
        interval = (report_day - prior_day).days
        if f"vs 前次（{interval}天前）" not in body:
            failures.add("new-signals section lacks the exact prior-run interval label")
    for dimension in contract["dimensions"]:
        key = dimension["key"]
        if score[key] != prior[key] and dimension["name"] not in body:
            failures.add(f"new-signals section omits changed dimension {dimension['name']}")
    if monetary_side == "扳機側" and "貨幣與信貸環境" not in body:
        failures.add("D5 扳機側 must be surfaced in 本次新增訊號")
    if any(score[d["key"]] != prior[d["key"]] for d in contract["dimensions"]):
        if body in ("無。", "- 無。"):
            failures.add("new-signals section cannot say 無 when scores changed")


def validate_institutional_section(doc, report_day, failures):
    body = [
        line.strip() for _, line in doc.section_lines("## 機構情緒對照")
        if line.strip()
    ]
    if not body:
        failures.add("機構情緒對照 section must not be empty")
        return
    placeholder = "本次無新機構調查數據。"
    if placeholder in body:
        if body != [placeholder]:
            failures.add(
                "institutional no-data placeholder must be the section's only content"
            )
        return
    joined = "\n".join(body)
    if "BofA" not in joined and "JPM" not in joined:
        failures.add("機構情緒對照 needs the locked no-data line or BofA/JPM evidence")
    dates = re.findall(DATE_RE, joined)
    if not dates:
        failures.add("institutional survey evidence lacks a data date")
    else:
        survey_day = strict_date(dates[-1], "institutional survey date", failures)
        if survey_day and report_day and survey_day > report_day:
            failures.add("institutional survey date is in the future")


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
    raw_section = doc.subsection_lines("### Raw data", "## 數據附錄")
    coverage_section = doc.subsection_lines("### Coverage", "## 數據附錄")
    trace_section = doc.subsection_lines(
        "### SEARCH-VERIFIED traceability", "## 數據附錄"
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


def validate_unexpected_tables(doc, contract, failures):
    allowed = {
        contract["section1_header"], contract["section2_header"],
        contract["section3_header"], contract["weighted_score_header"],
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
        description="Validate a bubble-risk report before archive mutation."
    )
    parser.add_argument("report", help="complete report Markdown")
    parser.add_argument("--prompt", required=True, help="version-matched prompt Markdown")
    parser.add_argument("--contract", required=True, help="report_contract.json")
    parser.add_argument("--macro-json", required=True, help="exact fetch_macro JSON output")
    parser.add_argument(
        "--current-score", required=True,
        help="standalone score.json payload that will be archived",
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--prior-score", help="accepted prior score.json")
    mode.add_argument("--baseline", action="store_true", help="validate without a prior run")
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
    current_score = load_json_file(args.current_score, "current score", failures)
    prior_raw = None
    prior = None
    if args.prior_score:
        prior_raw = load_json_file(args.prior_score, "prior score", failures)
        if prior_raw is not None:
            prior = validate_prior(prior_raw, contract, failures)
    if (prompt is None or report is None or macro is None or current_score is None
            or (not args.baseline and prior is None)):
        return failures.emit_and_exit()
    if not validate_macro_shape(macro, contract, failures):
        return failures.emit_and_exit()

    validate_prompt_mapping(prompt, contract, failures)
    if args.baseline:
        if macro.get("prior_run_date") != "none":
            failures.add("baseline mode requires macro prior_run_date `none`")
        decomposition = macro.get("decomposition", {})
        if (decomposition.get("status"), decomposition.get("driver"),
                decomposition.get("freshness")) != (
                    "baseline_no_prior", "baseline", "not_applicable"):
            failures.add("baseline macro decomposition state is invalid")
    else:
        if macro.get("prior_run_date") == "none":
            failures.add("prior mode cannot use macro prior_run_date `none`")
        if prior.get("date") and macro.get("prior_run_date") != prior.get("date"):
            failures.add("macro prior_run_date does not match prior score artifact")

    doc = MarkdownDocument(report, failures)
    validate_global_security(doc, contract, failures)
    validate_wording_lock(doc, contract, failures)
    score = validate_headings_and_fence(doc, contract, failures)
    if score is None:
        return failures.emit_and_exit()
    if not validate_score_object(score, contract, failures, exact=True):
        return failures.emit_and_exit()
    if not validate_score_object(
            current_score, contract, failures, label="current score file", exact=True):
        return failures.emit_and_exit()
    if current_score != score:
        failures.add("standalone current score file does not equal the report JSON fence")

    report_day, summary = validate_title_meta_summary(
        doc, score, macro, prior, args.baseline, args.dry_run, contract, failures
    )
    score_day = strict_date(score.get("date"), "score.json date", failures)
    if report_day and score_day and report_day != score_day:
        failures.add("score.json date does not match report title")
    if score_day:
        expected_week = f"{score_day.isocalendar().year}-W{score_day.isocalendar().week:02d}"
        if score.get("iso_week") != expected_week:
            failures.add("score.json iso_week does not match date")
        if score.get("weekday") != score_day.strftime("%A"):
            failures.add("score.json weekday does not match date")
    generated = parse_iso_timestamp(macro.get("generated_at"))
    if generated and report_day and generated.date() != report_day:
        failures.add("macro generated_at date does not match report date")

    total_delta = validate_section1(doc, score, prior, args.baseline, contract, failures)
    if summary:
        if summary["total"] != score.get("total") or summary["tier"] != score.get("tier"):
            failures.add("summary total/tier does not match score.json")
        expected_summary_delta = (
            "—" if total_delta is None
            else str(total_delta) if type(total_delta) is int
            else None
        )
        if type(total_delta) is int and total_delta > 0:
            expected_summary_delta = "+" + expected_summary_delta
        if (expected_summary_delta is not None
                and summary["delta"].replace("−", "-") != expected_summary_delta):
            failures.add("summary delta does not match §1 total delta")
    evidence = validate_appendix(doc, report_day, macro, contract, failures)
    validate_section2_and_history(
        doc, summary, score, macro, prior, args.baseline,
        evidence, contract, failures
    )
    trigger = validate_triangle(
        doc, score, summary, macro, prior, args.baseline, evidence,
        contract, failures
    )
    monetary_side = validate_dimensions(
        doc, score, prior, args.baseline, report_day, evidence, macro,
        contract, failures
    )
    validate_weighted_section(doc, score, contract, failures)
    validate_state_fields(
        score, macro, prior, args.baseline, monetary_side, trigger,
        evidence, contract, failures
    )
    validate_new_signals(
        doc, score, prior, macro, args.baseline, monetary_side, report_day,
        contract, failures
    )
    validate_institutional_section(doc, report_day, failures)
    validate_unexpected_tables(doc, contract, failures)

    # Each exact contract table header belongs to exactly one visible table.
    for key in (
        "section1_header", "section2_header", "section3_header",
        "weighted_score_header", "coverage_header", "raw_data_header",
        "traceability_header",
    ):
        count = sum(1 for _, line in doc.visible if line.strip() == contract[key])
        if count != 1:
            failures.add(f"contract table header {key} must occur once; found {count}")
    return failures.emit_and_exit()


if __name__ == "__main__":
    sys.exit(main())

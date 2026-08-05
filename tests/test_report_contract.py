import copy
import importlib.util
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "report_contract.json"
PROMPT_PATH = ROOT / "bubble-risk-weekly-prompt.md"
GUIDANCE_PATH = ROOT / "CLAUDE.md"
VALIDATOR_PATH = ROOT / "scripts" / "validate_report.py"


def data_source_bullets(text):
    lines = text.splitlines()
    start = next(i for i, line in enumerate(lines)
                 if line.startswith("# Data sources"))
    end = next(i for i, line in enumerate(lines[start + 1:], start + 1)
               if line == "# Output structure")
    return [line[2:] for line in lines[start + 1:end]
            if line.startswith("- ")]


class ReportContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
        cls.prompt = PROMPT_PATH.read_text(encoding="utf-8")
        cls.guidance = GUIDANCE_PATH.read_text(encoding="utf-8")

    def test_contract_core_is_internally_consistent(self):
        contract = self.contract
        self.assertEqual(contract["version"], 1)
        self.assertEqual(contract["macro_schema"]["version"], 1)
        self.assertEqual(len(contract["macro_schema"]["required_series"]), 20)
        self.assertEqual(contract["timezone"], "Asia/Taipei")
        self.assertEqual(len(contract["headings"]), 10)
        self.assertEqual(len(set(contract["headings"])), 10)
        wording_lock = contract["wording_lock"]
        self.assertIn(2, wording_lock["full_section_heading_indexes"])
        self.assertEqual(
            len(wording_lock["full_section_heading_indexes"]),
            len(set(wording_lock["full_section_heading_indexes"])),
        )
        self.assertTrue(all(
            0 <= index < len(contract["headings"])
            for index in wording_lock["full_section_heading_indexes"]
        ))
        self.assertTrue(wording_lock["forbidden_synonyms"])
        self.assertEqual(sum(d["weight"] for d in contract["dimensions"]), 100)
        self.assertEqual(len({d["name"] for d in contract["dimensions"]}), 6)
        self.assertEqual(len({d["key"] for d in contract["dimensions"]}), 6)
        self.assertEqual(
            list(contract["anchor_feature_counts"]), contract["anchors"]
        )
        self.assertEqual(list(contract["anchor_features"]), contract["anchors"])
        self.assertTrue(all(
            type(count) is int and count > 0
            for count in contract["anchor_feature_counts"].values()
        ))
        self.assertTrue(all(
            type(value) in (int, float) and value > 0
            for value in contract["calibration"].values()
        ))
        self.assertTrue(all(
            type(value) in (int, float) and value > 0
            for value in contract["direction_thresholds"].values()
        ))

        tiers = contract["tiers"]
        self.assertEqual(tiers[0]["min"], 0)
        self.assertEqual(tiers[-1]["max"], 100)
        for left, right in zip(tiers, tiers[1:]):
            self.assertEqual(left["max"] + 1, right["min"])

        current_fields = contract["score_schema"]["current_fields"]
        self.assertEqual(len(current_fields), len(set(current_fields)))
        for dimension in contract["dimensions"]:
            self.assertIn(dimension["key"], current_fields)
        for field in contract["score_schema"]["legacy_prior_required_fields"]:
            self.assertIn(field, current_fields)
        self.assertIn("trigger_reasons", current_fields)

        feature_ids = []
        for anchor in contract["anchors"]:
            features = contract["anchor_features"][anchor]
            self.assertEqual(
                len(features), contract["anchor_feature_counts"][anchor]
            )
            feature_ids.extend(feature["id"] for feature in features)
        self.assertEqual(len(feature_ids), 50)
        self.assertEqual(len(feature_ids), len(set(feature_ids)))

    def test_headers_have_locked_column_counts(self):
        expected_columns = {
            "section1_header": 5,
            "section2_header": 4,
            "section3_header": 3,
            "weighted_score_header": 4,
            "coverage_header": 4,
            "raw_data_header": 6,
            "traceability_header": 6,
        }
        for key, count in expected_columns.items():
            cells = [cell.strip() for cell in self.contract[key].strip().strip("|").split("|")]
            self.assertEqual(len(cells), count, key)
            self.assertTrue(all(cells), key)

    def test_sources_are_stable_unique_and_map_one_to_one_to_prompt(self):
        sources = self.contract["sources"]
        bullets = data_source_bullets(self.prompt)
        self.assertTrue(sources)
        self.assertEqual(len(bullets), len(sources))
        self.assertEqual(len({source["id"] for source in sources}), len(sources))

        allowed_windows = {
            "snapshot", "stock_of_state", "7d", "14d", "30d", "90d",
            "composite",
        }
        for source, bullet in zip(sources, bullets):
            self.assertRegex(source["id"], r"^[a-z][a-z0-9_]*(?:\.[a-z][a-z0-9_]*)+$")
            self.assertIs(type(source["required"]), bool)
            self.assertIn(source["window"], allowed_windows)
            if source["window"] == "composite":
                self.assertEqual(
                    {item["window"] for item in source["window_components"]},
                    {"stock_of_state", "30d"},
                )
            self.assertIn(source["prompt_match"], bullet, source["id"])
            if source.get("same_quarter"):
                self.assertEqual(source["window"], "90d")
            if "best-effort" in bullet.lower():
                self.assertFalse(source["required"], source["id"])
            if not source["required"]:
                self.assertTrue(
                    "best-effort" in bullet.lower() or "NOT DISCLOSED" in bullet,
                    f"optional source lacks a deterministic no-disclosure rule: {source['id']}",
                )

    def test_contract_validation_does_not_hand_lock_source_count(self):
        spec = importlib.util.spec_from_file_location(
            "validate_report_contract_count_test", VALIDATOR_PATH
        )
        validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(validator)
        contract = copy.deepcopy(self.contract)
        source = copy.deepcopy(contract["sources"][-1])
        source.update({
            "id": "structural.dynamic_contract_source",
            "prompt_match": "dynamic contract source",
        })
        contract["sources"].append(source)
        failures = validator.Failures()
        self.assertTrue(validator.validate_contract(contract, failures))
        self.assertEqual(failures.items, [])

    def test_contract_rejects_invalid_wording_lock_policy(self):
        spec = importlib.util.spec_from_file_location(
            "validate_report_wording_policy_test", VALIDATOR_PATH
        )
        validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(validator)
        bad_policies = (
            {
                "full_section_heading_indexes": [2, len(self.contract["headings"])],
                "forbidden_synonyms": ["本期"],
            },
            {
                "full_section_heading_indexes": [2, 2],
                "forbidden_synonyms": ["本期"],
            },
            {
                "full_section_heading_indexes": [2],
                "forbidden_synonyms": ["本期", "本期"],
            },
        )
        for policy in bad_policies:
            with self.subTest(policy=policy):
                contract = copy.deepcopy(self.contract)
                contract["wording_lock"] = policy
                failures = validator.Failures()
                self.assertFalse(
                    validator.validate_contract(contract, failures), failures.items
                )
                self.assertTrue(any(
                    "wording-lock" in message for message in failures.items
                ), failures.items)

    def test_prompt_does_not_hand_copy_contract_source_count(self):
        forbidden = (
            r"expected\s+\d+\s+Coverage rows",
            r"each of the\s+\d+\s+objects",
            r"<\d+\s+contract source rows",
            r"iterate the\s+\d+\s+report_contract",
        )
        for pattern in forbidden:
            with self.subTest(pattern=pattern):
                self.assertNotRegex(self.prompt, re.compile(pattern, re.I))

    def test_prompt_forbidden_synonyms_only_define_the_wording_lock(self):
        allowed_markers = (
            "**Exact wording lock:**",
            "- All required `本次` wording remains exact;",
        )
        for synonym in self.contract["wording_lock"]["forbidden_synonyms"]:
            offenders = [
                (line_number, line)
                for line_number, line in enumerate(self.prompt.splitlines(), 1)
                if synonym in line
                and not any(marker in line for marker in allowed_markers)
            ]
            self.assertEqual(offenders, [], synonym)

    def test_guidance_uses_contract_monetary_side_spelling(self):
        self.assertNotIn("扣機側", self.guidance)
        self.assertIn("`扳機側`", self.guidance)

    def test_macro_bindings_and_zero_result_policy_are_canonical(self):
        contract = self.contract
        bound_series = set()
        bound_blocks = set()
        source_ids = {source["id"] for source in contract["sources"]}
        for source in contract["sources"]:
            binding = source.get("macro")
            if not binding:
                continue
            self.assertIn(binding["aggregation"], {"all", "any"})
            for component in binding["components"]:
                self.assertIn(component["kind"], {"series", "block"})
                target = bound_series if component["kind"] == "series" else bound_blocks
                target.add(component["key"])
        self.assertEqual(bound_series, set(contract["macro_schema"]["required_series"]))
        self.assertEqual(
            bound_blocks,
            set(contract["macro_schema"]["required_blocks"])
            - {"repo_stress", "decomposition"},
        )
        self.assertEqual(
            {source["id"] for source in contract["sources"]
             if source.get("zero_result_allowed")},
            {
                "speculation.ai_rename_spac",
                "speculation.microcap_moonshots",
                "speculation.insider_form4",
                "structural.us_single_stock_etf",
            },
        )
        for reason in contract["trigger_reason_codes"].values():
            self.assertIn(reason["state"], contract["trigger_states"])
            self.assertIn(reason["kind"], {"machine", "evidence"})
            self.assertLessEqual(set(reason.get("source_ids", [])), source_ids)

    def test_spv_deal_marker_shape_is_valid(self):
        marker = self.contract["spv_deal_marker"]
        source_ids = {source["id"] for source in self.contract["sources"]}
        self.assertIn(marker["source_id"], source_ids)
        source = next(
            item for item in self.contract["sources"]
            if item["id"] == marker["source_id"]
        )
        self.assertEqual(source["window"], "composite")
        self.assertIn(
            marker["component_id"],
            {item["id"] for item in source["window_components"]},
        )
        self.assertRegex(marker["tag"], r"^\[[a-z_]+\]$")
        evidence_tags = {
            reason["evidence_tag"]
            for reason in self.contract["trigger_reason_codes"].values()
            if reason["kind"] == "evidence"
        }
        self.assertNotIn(marker["tag"], evidence_tags)
        self.assertTrue(marker["required_keys"])
        self.assertTrue(all(
            re.fullmatch(r"[a-z_]+", key) for key in marker["required_keys"]
        ))
        self.assertEqual(
            len(marker["required_keys"]), len(set(marker["required_keys"]))
        )

    def test_contract_rejects_spv_deal_marker_when_source_window_is_not_composite(self):
        spec = importlib.util.spec_from_file_location(
            "validate_report_spv_marker_composite_test", VALIDATOR_PATH
        )
        validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(validator)
        contract = copy.deepcopy(self.contract)
        marker = contract["spv_deal_marker"]
        source = next(
            item for item in contract["sources"] if item["id"] == marker["source_id"]
        )
        source["window"] = "30d"  # window_components deliberately left stale
        failures = validator.Failures()
        self.assertFalse(
            validator.validate_contract(contract, failures), failures.items
        )
        self.assertTrue(any(
            "composite" in message for message in failures.items
        ), failures.items)

    def test_contract_rejects_spv_deal_marker_on_non_event_component(self):
        spec = importlib.util.spec_from_file_location(
            "validate_report_spv_marker_component_test", VALIDATOR_PATH
        )
        validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(validator)
        contract = copy.deepcopy(self.contract)
        contract["spv_deal_marker"]["component_id"] = "quarterly_state"
        failures = validator.Failures()
        self.assertFalse(
            validator.validate_contract(contract, failures), failures.items
        )
        self.assertTrue(any(
            "30d" in message for message in failures.items
        ), failures.items)

    def test_source_and_state_enums_are_unique(self):
        for key in (
            "anchors",
            "regimes",
            "trigger_states",
            "monetary_sides",
            "triangle_indicators",
            "triangle_labels",
            "historical_audit_labels",
            "coverage_statuses",
        ):
            values = self.contract[key]
            self.assertEqual(len(values), len(set(values)), key)


if __name__ == "__main__":
    unittest.main()

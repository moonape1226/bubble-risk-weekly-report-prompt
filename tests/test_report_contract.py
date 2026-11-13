import copy
import importlib.util
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "report_contract.json"
PROMPT_PATH = ROOT / "bubble-risk-weekly-prompt.md"
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

    def test_contract_core_is_internally_consistent(self):
        contract = self.contract
        self.assertEqual(contract["version"], 2)
        self.assertEqual(contract["macro_schema"]["version"], 2)
        self.assertEqual(len(contract["macro_schema"]["required_series"]), 21)
        self.assertEqual(contract["timezone"], "Asia/Taipei")
        self.assertEqual(len(contract["headings"]), 9)
        self.assertEqual(len(set(contract["headings"])), 9)
        wording_lock = contract["wording_lock"]
        self.assertEqual(
            len(wording_lock["full_section_heading_indexes"]),
            len(set(wording_lock["full_section_heading_indexes"])),
        )
        self.assertTrue(all(
            0 <= index < len(contract["headings"])
            for index in wording_lock["full_section_heading_indexes"]
        ))
        self.assertTrue(wording_lock["forbidden_synonyms"])
        self.assertTrue(all(
            type(value) in (int, float) and value > 0
            for value in contract["calibration"].values()
        ))

        question = contract["question"]
        self.assertEqual(question["answers"], ["yes", "no"])
        self.assertEqual(set(contract["conclusion_line"]), set(question["answers"]))
        resolution = contract["resolution"]
        self.assertIn(question["text"], resolution["block"])
        self.assertEqual(
            [path["id"] for path in resolution["paths"]], ["R1", "R2", "R3"])
        self.assertEqual(
            resolution["r1"]["lookback_trading_days"],
            contract["macro_schema"]["ndx_drawdown"]["lookback_trading_days"],
        )
        self.assertIn("ndx_drawdown", contract["macro_schema"]["required_blocks"])
        source_ids = {source["id"] for source in contract["sources"]}
        for path in resolution["paths"]:
            self.assertTrue(path["heading"].startswith("### "))
            self.assertLessEqual(set(path["source_ids"]), source_ids)
        for index in contract["evidence_sections"]["heading_indexes"]:
            self.assertIn("證據", contract["headings"][index])

        fields = contract["forecast_schema"]["current_fields"]
        self.assertEqual(len(fields), len(set(fields)))
        self.assertEqual(fields[-1], "resolution")
        removed = {
            "dimensions", "tiers", "anchors", "anchor_features", "regimes",
            "trigger_states", "trigger_reason_codes", "score_schema", "direction_thresholds", "weighted_score_header",
        }
        self.assertEqual(removed & set(contract), set())

    def test_headers_have_locked_column_counts(self):
        expected_columns = {
            "coverage_header": 4,
            "raw_data_header": 6,
            "traceability_header": 6,
        }
        for key, count in expected_columns.items():
            cells = [cell.strip() for cell in self.contract[key].strip().strip("|").split("|")]
            self.assertEqual(len(cells), count, key)
            self.assertTrue(all(cells), key)

    def test_shipped_contract_passes_validator_self_check(self):
        spec = importlib.util.spec_from_file_location(
            "validate_report_contract_selfcheck_test", VALIDATOR_PATH
        )
        validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(validator)
        failures = validator.Failures()
        self.assertTrue(
            validator.validate_contract(self.contract, failures), failures.items)
        self.assertEqual(failures.items, [])

    def test_contract_rejects_inconsistent_v2_policies(self):
        spec = importlib.util.spec_from_file_location(
            "validate_report_v2_policy_test", VALIDATOR_PATH
        )
        validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(validator)

        def mutate_version(contract):
            contract["version"] = 1

        def drop_question(contract):
            del contract["question"]

        def bad_answers(contract):
            contract["question"]["answers"] = ["yes", "no", "maybe"]

        def r1_lookback_conflict(contract):
            contract["macro_schema"]["ndx_drawdown"]["lookback_trading_days"] = 200

        def eight_headings(contract):
            contract["headings"].pop()

        def unknown_path_source(contract):
            contract["resolution"]["paths"][0]["source_ids"] = ["made.up"]

        def conclusion_keys(contract):
            contract["conclusion_line"] = {"yes": "**結論：yes**"}

        for mutate in (
            mutate_version, drop_question, bad_answers, r1_lookback_conflict,
            eight_headings, unknown_path_source, conclusion_keys,
        ):
            with self.subTest(mutation=mutate.__name__):
                contract = copy.deepcopy(self.contract)
                mutate(contract)
                failures = validator.Failures()
                self.assertFalse(
                    validator.validate_contract(contract, failures), failures.items)
                self.assertTrue(failures.items)

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

    def test_contract_rejects_invalid_appendix_headings(self):
        spec = importlib.util.spec_from_file_location(
            "validate_report_appendix_headings_test", VALIDATOR_PATH
        )
        validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(validator)
        contract = copy.deepcopy(self.contract)
        contract["appendix_headings"] = ["### Raw data", "### Coverage"]
        failures = validator.Failures()
        validator.validate_contract(contract, failures)
        self.assertIn(
            "contract appendix_headings must be three unique H3 headings", failures.items)

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
                "forbidden_scoring_terms": ["總分"],
            },
            {
                "full_section_heading_indexes": [2, 2],
                "forbidden_synonyms": ["本期"],
                "forbidden_scoring_terms": ["總分"],
            },
            {
                "full_section_heading_indexes": [2],
                "forbidden_synonyms": ["本期", "本期"],
                "forbidden_scoring_terms": ["總分"],
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

    def test_coverage_statuses_are_unique(self):
        values = self.contract["coverage_statuses"]
        self.assertEqual(len(values), len(set(values)))

    def test_ndx_drawdown_source_is_bound_to_its_macro_block(self):
        source = next(
            item for item in self.contract["sources"]
            if item["id"] == "valuation.ndx_drawdown")
        self.assertEqual(
            source["macro"]["components"], [{"kind": "block", "key": "ndx_drawdown"}])


if __name__ == "__main__":
    unittest.main()

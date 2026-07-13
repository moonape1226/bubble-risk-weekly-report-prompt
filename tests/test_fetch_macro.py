"""Tests for scripts/fetch_macro.py date handling. stdlib only, no network."""
import importlib.util, subprocess, sys, unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "fetch_macro.py"

spec = importlib.util.spec_from_file_location("fetch_macro", SCRIPT)
fm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fm)


class PriorValidation(unittest.TestCase):
    """Invalid prior date must be rejected before any fetching (exit 2)."""

    def _run(self, arg):
        try:
            p = subprocess.run([sys.executable, str(SCRIPT), arg],
                               capture_output=True, text=True, timeout=15)
            return p.returncode
        except subprocess.TimeoutExpired:
            return None  # started fetching instead of rejecting

    def test_unpadded_date_rejected(self):
        self.assertEqual(self._run("2026-7-9"), 2)

    def test_garbage_rejected(self):
        self.assertEqual(self._run("yesterday"), 2)

    def test_wrong_separator_rejected(self):
        self.assertEqual(self._run("07/09/2026"), 2)


class FetchWindow(unittest.TestCase):
    """Monthly series need a lookback wide enough to survive FRED's
    period-end observation_start semantics + publication lag."""

    def test_monthly_series_gets_wide_lookback(self):
        self.assertEqual(fm.fetch_window("JPNASSETS"), (90, 120))

    def test_daily_series_keeps_short_lookback(self):
        self.assertEqual(fm.fetch_window("DGS10"), (21, 120))

    def test_wide_window_series_unchanged(self):
        self.assertEqual(fm.fetch_window("CPIAUCSL"), (540, 540))
        self.assertEqual(fm.fetch_window("BOGZ1FL153064486Q"), (540, 540))


class DerivedT10yie(unittest.TestCase):
    """Derived T10YIE must subtract DGS10 and DFII10 on a common as-of date,
    not mix each series' own latest."""

    def setUp(self):
        fm.OBS_CACHE.clear()

    def test_aligned_to_common_date(self):
        fm.OBS_CACHE.update({
            "DGS10": [("2026-07-10", 4.50), ("2026-07-09", 4.48)],
            "DFII10": [("2026-07-09", 2.20), ("2026-07-08", 2.18)],
        })
        n = {"status": "ok", "latest_date": "2026-07-10", "latest": 4.50}
        r = {"status": "ok", "latest_date": "2026-07-09", "latest": 2.20}
        blk = fm.derived_t10yie(n, r)
        self.assertEqual(blk["status"], "derived")
        self.assertEqual(blk["latest_date"], "2026-07-09")
        self.assertAlmostEqual(blk["latest"], 2.28)  # 4.48-2.20, not 4.50-2.20

    def test_component_dates_reported_when_misaligned(self):
        fm.OBS_CACHE.update({
            "DGS10": [("2026-07-10", 4.50), ("2026-07-08", 4.46)],
            "DFII10": [("2026-07-09", 2.20)],
        })
        n = {"status": "ok", "latest_date": "2026-07-10", "latest": 4.50}
        r = {"status": "ok", "latest_date": "2026-07-09", "latest": 2.20}
        blk = fm.derived_t10yie(n, r)
        self.assertAlmostEqual(blk["latest"], 2.26)  # 4.46-2.20 on nearest common dates
        self.assertEqual(blk["dgs10_date"], "2026-07-08")
        self.assertEqual(blk["dfii10_date"], "2026-07-09")


class Pick(unittest.TestCase):
    def test_on_or_before(self):
        obs = [("2026-07-10", 2.0), ("2026-07-08", 1.0)]
        self.assertEqual(fm.pick(obs, "2026-07-09"), ("2026-07-08", 1.0))

    def test_none_when_all_newer(self):
        obs = [("2026-07-10", 2.0)]
        self.assertIsNone(fm.pick(obs, "2026-07-01"))


if __name__ == "__main__":
    unittest.main()

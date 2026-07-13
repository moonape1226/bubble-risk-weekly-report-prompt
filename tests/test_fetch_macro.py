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
    """Derived T10YIE must subtract DGS10 and DFII10 on their latest SHARED
    observation date; if the series share no date, no derived value."""

    def setUp(self):
        fm.OBS_CACHE.clear()

    def test_latest_shared_date(self):
        fm.OBS_CACHE.update({
            "DGS10": [("2026-07-10", 4.50), ("2026-07-09", 4.48)],
            "DFII10": [("2026-07-09", 2.20), ("2026-07-08", 2.18)],
        })
        blk = fm.derived_t10yie()
        self.assertEqual(blk["status"], "derived")
        self.assertEqual(blk["latest_date"], "2026-07-09")
        self.assertAlmostEqual(blk["latest"], 2.28)  # 4.48-2.20, both from 07-09

    def test_skips_unshared_newer_dates(self):
        fm.OBS_CACHE.update({
            "DGS10": [("2026-07-10", 4.50), ("2026-07-08", 4.46)],
            "DFII10": [("2026-07-09", 2.20), ("2026-07-08", 2.18)],
        })
        blk = fm.derived_t10yie()
        self.assertEqual(blk["latest_date"], "2026-07-08")
        self.assertAlmostEqual(blk["latest"], 2.28)  # 4.46-2.18, both from 07-08

    def test_no_shared_date_returns_none(self):
        fm.OBS_CACHE.update({
            "DGS10": [("2026-07-10", 4.50)],
            "DFII10": [("2026-07-09", 2.20)],
        })
        self.assertIsNone(fm.derived_t10yie())


class RepoStressAlignment(unittest.TestCase):
    """Each spread leg pair must share an observation date: when SOFR99 lags
    the SOFR print across an FOMC move, IORB must be re-picked at the SOFR99
    date, not reused from the SOFR date."""

    def setUp(self):
        fm.OBS_CACHE.clear()

    def test_sofr99_leg_uses_iorb_at_sofr99_date(self):
        # FOMC cut on 07-31: IORB 4.40 -> 4.15; SOFR99 only printed through 07-30
        fm.OBS_CACHE.update({
            "SOFR": [("2026-07-31", 4.40), ("2026-07-30", 4.62)],
            "IORB": [("2026-07-31", 4.15), ("2026-07-30", 4.40)],
            "SOFR99": [("2026-07-30", 4.55)],
        })
        series = {
            "SOFR": {"status": "ok", "latest_date": "2026-07-31", "latest": 4.40},
            "IORB": {"status": "ok", "latest_date": "2026-07-31", "latest": 4.15},
            "SOFR99": {"status": "ok", "latest_date": "2026-07-30", "latest": 4.55},
        }
        rs = fm.repo_stress_block(series)
        self.assertEqual(rs["status"], "ok")
        self.assertAlmostEqual(rs["sofr_iorb_bps"], 25.0)   # 4.40-4.15, both 07-31
        self.assertAlmostEqual(rs["sofr99_iorb_bps"], 15.0)  # 4.55-4.40, both 07-30
        self.assertEqual(rs["sofr99_date"], "2026-07-30")

    def test_sofr99_leg_skipped_when_no_iorb_at_or_before(self):
        # IORB cache has nothing on/before the SOFR99 date: emitting the
        # spread would silently mix dates, so the leg must be omitted
        fm.OBS_CACHE.update({
            "SOFR": [("2026-07-31", 4.40)],
            "IORB": [("2026-07-31", 4.15)],
            "SOFR99": [("2026-07-25", 4.55)],
        })
        series = {
            "SOFR": {"status": "ok", "latest_date": "2026-07-31", "latest": 4.40},
            "IORB": {"status": "ok", "latest_date": "2026-07-31", "latest": 4.15},
            "SOFR99": {"status": "ok", "latest_date": "2026-07-25", "latest": 4.55},
        }
        rs = fm.repo_stress_block(series)
        self.assertEqual(rs["status"], "ok")
        self.assertNotIn("sofr99_iorb_bps", rs)

    def test_unavailable_when_no_iorb_at_or_before_sofr(self):
        # IORB cache only has a print NEWER than the SOFR date: no tuple
        # fallback to iorb.latest — the block must degrade to unavailable
        fm.OBS_CACHE.update({
            "SOFR": [("2026-07-30", 4.62)],
            "IORB": [("2026-07-31", 4.15)],
        })
        series = {
            "SOFR": {"status": "ok", "latest_date": "2026-07-30", "latest": 4.62},
            "IORB": {"status": "ok", "latest_date": "2026-07-31", "latest": 4.15},
        }
        rs = fm.repo_stress_block(series)
        self.assertEqual(rs["status"], "unavailable")

    def test_sofr99_skipped_when_only_newer_than_as_of(self):
        # SOFR99 printed only after as_of: no fallback to its newer latest
        fm.OBS_CACHE.update({
            "SOFR": [("2026-07-30", 4.62)],
            "IORB": [("2026-07-30", 4.40)],
            "SOFR99": [("2026-07-31", 4.70)],
        })
        series = {
            "SOFR": {"status": "ok", "latest_date": "2026-07-30", "latest": 4.62},
            "IORB": {"status": "ok", "latest_date": "2026-07-30", "latest": 4.40},
            "SOFR99": {"status": "ok", "latest_date": "2026-07-31", "latest": 4.70},
        }
        rs = fm.repo_stress_block(series)
        self.assertEqual(rs["status"], "ok")
        self.assertAlmostEqual(rs["sofr_iorb_bps"], 22.0)
        self.assertNotIn("sofr99_iorb_bps", rs)

    def test_sofr99_leg_disclosed_when_iorb_older_than_sofr99(self):
        # SOFR99 lags as_of and IORB has no print on the SOFR99 date either:
        # the leg may use the older IORB but must disclose its date
        fm.OBS_CACHE.update({
            "SOFR": [("2026-08-01", 4.40)],
            "IORB": [("2026-08-01", 4.15), ("2026-07-28", 3.90)],
            "SOFR99": [("2026-07-30", 4.55)],
        })
        series = {
            "SOFR": {"status": "ok", "latest_date": "2026-08-01", "latest": 4.40},
            "IORB": {"status": "ok", "latest_date": "2026-08-01", "latest": 4.15},
            "SOFR99": {"status": "ok", "latest_date": "2026-07-30", "latest": 4.55},
        }
        rs = fm.repo_stress_block(series)
        self.assertAlmostEqual(rs["sofr99_iorb_bps"], 65.0)  # 4.55 - 3.90
        self.assertEqual(rs["sofr99_date"], "2026-07-30")
        self.assertEqual(rs["sofr99_iorb_date"], "2026-07-28")

    def test_unavailable_when_sofr_missing(self):
        rs = fm.repo_stress_block({"IORB": {"status": "ok"}})
        self.assertEqual(rs["status"], "unavailable")


class DecompositionWindow(unittest.TestCase):
    """ΔT10YIE may be rebuilt from ΔDGS10 − ΔDFII10 only when both legs
    cover the same window (same latest and prior dates)."""

    def test_rebuild_on_same_window(self):
        series = {
            "DGS10": {"status": "ok", "latest_date": "2026-07-10",
                      "prior_date": "2026-07-03", "delta_bps": 6.0},
            "DFII10": {"status": "ok", "latest_date": "2026-07-10",
                       "prior_date": "2026-07-03", "delta_bps": 2.0},
            "T10YIE": {"status": "derived"},
        }
        blk = fm.decomposition_block(series)
        self.assertAlmostEqual(blk["d_t10yie_bps"], 4.0)
        self.assertEqual(blk["driver"], "breakeven")

    def test_no_rebuild_on_mismatched_window(self):
        series = {
            "DGS10": {"status": "ok", "latest_date": "2026-07-10",
                      "prior_date": "2026-07-03", "delta_bps": 6.0},
            "DFII10": {"status": "ok", "latest_date": "2026-07-09",
                       "prior_date": "2026-07-02", "delta_bps": 2.0},
            "T10YIE": {"status": "derived"},
        }
        blk = fm.decomposition_block(series)
        self.assertIsNone(blk["d_t10yie_bps"])
        self.assertEqual(blk["driver"], "unknown")

    def test_direct_t10yie_delta_passthrough(self):
        series = {
            "DGS10": {"status": "ok", "latest_date": "2026-07-10",
                      "prior_date": "2026-07-03", "delta_bps": 6.0},
            "DFII10": {"status": "ok", "latest_date": "2026-07-10",
                       "prior_date": "2026-07-03", "delta_bps": 5.0},
            "T10YIE": {"status": "ok", "delta_bps": 1.0},
        }
        blk = fm.decomposition_block(series)
        self.assertAlmostEqual(blk["d_t10yie_bps"], 1.0)
        self.assertEqual(blk["driver"], "real-rate")


class Pick(unittest.TestCase):
    def test_on_or_before(self):
        obs = [("2026-07-10", 2.0), ("2026-07-08", 1.0)]
        self.assertEqual(fm.pick(obs, "2026-07-09"), ("2026-07-08", 1.0))

    def test_none_when_all_newer(self):
        obs = [("2026-07-10", 2.0)]
        self.assertIsNone(fm.pick(obs, "2026-07-01"))


if __name__ == "__main__":
    unittest.main()

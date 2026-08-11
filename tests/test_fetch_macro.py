"""Tests for scripts/fetch_macro.py date handling. stdlib only, no network."""
import contextlib, importlib.util, io, json, subprocess, sys, unittest
from pathlib import Path
from unittest import mock

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

    def test_same_day_rejected(self):
        same_day = fm.execution_now().strftime("%Y-%m-%d")
        self.assertEqual(self._run(same_day), 2)

    def test_future_day_rejected(self):
        future_day = (fm.execution_now() + fm.timedelta(days=1)).strftime(
            "%Y-%m-%d")
        self.assertEqual(self._run(future_day), 2)


class FredMalformedPayload(unittest.TestCase):
    """An upstream FRED schema error degrades one series instead of aborting
    construction of the complete macro artifact."""

    def setUp(self):
        fm.OBS_CACHE.clear()

    def test_malformed_json_and_shapes_return_fetch_failed(self):
        payloads = (
            "{not-json",
            json.dumps([]),
            json.dumps({"observations": "not-an-array"}),
            json.dumps({"observations": [None]}),
        )
        for payload in payloads:
            with self.subTest(payload=payload), \
                 mock.patch.object(fm, "PRIOR", "none"), \
                 mock.patch.object(fm, "_get", return_value=payload):
                blk = fm.series_block("WALCL", "usd_mn")

            self.assertEqual(blk, {"status": "fetch_failed", "source": None})

    def test_malformed_dates_and_non_finite_values_are_filtered(self):
        payload = {"observations": [
            {"date": "2026-07-09", "value": "4.25"},
            {"date": "2026-7-10", "value": "9.99"},
            {"date": "2026-02-30", "value": "9.99"},
            {"date": 20260710, "value": "9.99"},
            {"date": "2026-07-10", "value": "NaN"},
            {"date": "2026-07-10", "value": "Infinity"},
            {"date": "2026-07-11", "value": "4.50"},
        ]}
        with mock.patch.object(fm, "PRIOR", "none"), \
             mock.patch.object(fm, "_get", return_value=json.dumps(payload)):
            obs = fm.fred_obs("WALCL")

        self.assertEqual(obs, [
            ("2026-07-11", 4.50),
            ("2026-07-09", 4.25),
        ])

    def test_eia_observation_filter_matches_fred_filter(self):
        payload = {"response": {"data": [
            {"period": "2026-07-10", "value": 70.25},
            {"period": "2026-7-09", "value": 99.0},
            {"period": "2026-07-08", "value": "-Infinity"},
            {"period": None, "value": 75.0},
        ]}}
        with mock.patch.object(fm, "_get", return_value=json.dumps(payload)):
            obs = fm.eia_wti()

        self.assertEqual(obs, [("2026-07-10", 70.25)])

    def test_conflicting_duplicate_date_degrades_series(self):
        payload = {"observations": [
            {"date": "2026-07-10", "value": "4.25"},
            {"date": "2026-07-10", "value": "4.30"},
        ]}
        with mock.patch.object(fm, "PRIOR", "none"), \
             mock.patch.object(fm, "_get", return_value=json.dumps(payload)):
            block = fm.series_block("WALCL", "usd_mn")

        self.assertEqual(block, {"status": "fetch_failed", "source": None})


class SeriesPolicies(unittest.TestCase):
    def setUp(self):
        fm.OBS_CACHE.clear()

    def test_stale_trailing_base_omits_term_premium_delta(self):
        # Target is seven days before 07-10.  The only eligible older print is
        # 15 days old, outside the contract's 7..14-day trailing window.
        obs = [("2026-07-10", 0.45), ("2026-06-25", 0.30)]
        with mock.patch.object(fm, "PRIOR", "2026-07-03"), \
             mock.patch.object(fm, "fred_obs", return_value=obs):
            blk = fm.series_block("THREEFYTP10", "pct")

        self.assertEqual(blk["status"], "ok")
        self.assertEqual(blk["latest"], 0.45)
        for field in ("prior", "prior_date", "delta_bps", "delta_abs",
                      "delta_note"):
            self.assertNotIn(field, blk)

    def test_cpi_accepts_base_in_exact_prior_year_calendar_month(self):
        # The publication day need not be identical; the base must be in the
        # same calendar month one year earlier and inside the age policy.
        obs = [("2026-07-15", 310.0), ("2025-07-01", 300.0)]
        with mock.patch.object(fm, "PRIOR", "none"), \
             mock.patch.object(fm, "fred_obs", return_value=obs):
            blk = fm.series_block("CPIAUCSL", "level")

        self.assertEqual(blk["status"], "ok")
        self.assertEqual(blk["yoy_base_date"], "2025-07-01")
        self.assertEqual(blk["yoy_pct"], 3.33)

    def test_cpi_rejects_adjacent_month_even_when_age_is_plausible(self):
        # 06-30 is 366 days before 07-01, so the age test alone would pass;
        # the exact prior-year calendar-month requirement must still reject it.
        obs = [("2026-07-01", 310.0), ("2025-06-30", 300.0)]
        with mock.patch.object(fm, "PRIOR", "none"), \
             mock.patch.object(fm, "fred_obs", return_value=obs):
            blk = fm.series_block("CPIAUCSL", "level")

        self.assertEqual(blk["status"], "fetch_failed")
        self.assertEqual(blk["source"], None)
        self.assertIn("year-ago base", blk["reason"])

    def test_zero_denominator_same_date_is_explicit_no_new_change(self):
        obs = [("2026-07-10", 0.0)]
        with mock.patch.object(fm, "PRIOR", "2026-07-10"), \
             mock.patch.object(fm, "fred_obs", return_value=obs):
            blk = fm.series_block("RPONTTLD", "usd_bn")

        self.assertTrue(blk["no_new_obs"])
        self.assertEqual(blk["prior"], 0.0)
        self.assertEqual(blk["chg_pct"], 0.0)
        self.assertEqual(blk["delta_abs"], 0.0)


class AlignmentProof(unittest.TestCase):
    def setUp(self):
        fm.OBS_CACHE.clear()

    def test_emitted_proof_is_newest_32_observations_only(self):
        start = fm.datetime(2026, 8, 10)
        obs = [
            ((start - fm.timedelta(days=i)).strftime("%Y-%m-%d"), 4.0 + i)
            for i in range(40)
        ]
        with mock.patch.object(fm, "PRIOR", "none"), \
             mock.patch.object(fm, "fred_obs", return_value=obs):
            blk = fm.series_block("IORB", "pct")

        expected = [
            {"date": day, "value": value} for day, value in obs[:32]
        ]
        self.assertEqual(blk["alignment_observations"], expected)
        self.assertEqual(fm.OBS_CACHE["IORB"], obs)

    def test_every_selected_derived_and_repo_leg_is_in_emitted_proof(self):
        observations = {
            "DGS10": [("2026-07-10", 4.50), ("2026-07-09", 4.48)],
            "DFII10": [("2026-07-10", 2.20), ("2026-07-09", 2.18)],
            "IORB": [("2026-07-10", 4.30), ("2026-07-09", 4.25)],
            "SOFR99": [("2026-07-09", 4.35)],
        }

        def fetch(sid):
            return observations[sid]

        blocks = {}
        with mock.patch.object(fm, "PRIOR", "none"), \
             mock.patch.object(fm, "fred_obs", side_effect=fetch):
            for sid in observations:
                blocks[sid] = fm.series_block(sid, "pct")

        derived = fm.derived_t10yie()
        self.assertEqual(derived["latest_date"], "2026-07-10")
        for sid in ("DGS10", "DFII10"):
            selected = derived["derived_from"][sid]
            self.assertIn(selected, blocks[sid]["alignment_observations"])

        series = {
            "SOFR": {"status": "ok", "latest_date": "2026-07-10",
                     "latest": 4.40},
            "IORB": blocks["IORB"],
            "SOFR99": blocks["SOFR99"],
        }
        repo = fm.repo_stress_block(series)
        self.assertIn(
            {"date": repo["iorb_date"], "value": repo["iorb"]},
            blocks["IORB"]["alignment_observations"],
        )
        self.assertIn(
            {"date": repo["sofr99_date"], "value": repo["sofr99"]},
            blocks["SOFR99"]["alignment_observations"],
        )
        self.assertIn(
            {"date": repo["sofr99_iorb_date"],
             "value": repo["sofr99_iorb"]},
            blocks["IORB"]["alignment_observations"],
        )


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


class TreasuryFallback(unittest.TestCase):
    """Treasury's XML endpoint is calendar-year partitioned; a cross-year
    prior baseline must survive either partition failing independently."""

    @staticmethod
    def _xml(date, value, real=False):
        field = "TC_10YEAR" if real else "BC_10YEAR"
        return (f"<entry><d:NEW_DATE>{date}T00:00:00</d:NEW_DATE>"
                f"<d:{field}>{value}</d:{field}></entry>")

    def setUp(self):
        fm.OBS_CACHE.clear()

    def test_series_block_combines_current_and_prior_year(self):
        current_year = fm.execution_now().year
        prior_year = current_year - 1
        latest_date = f"{current_year}-01-03"
        prior_date = f"{prior_year}-12-27"

        def get_year(url, timeout=20):
            if f"field_tdr_date_value={current_year}" in url:
                return self._xml(latest_date, 4.50)
            if f"field_tdr_date_value={prior_year}" in url:
                return self._xml(prior_date, 4.40)
            raise AssertionError(f"unexpected Treasury URL: {url}")

        with mock.patch.object(fm, "PRIOR", prior_date), \
             mock.patch.object(fm, "fred_obs", side_effect=OSError("FRED down")), \
             mock.patch.object(fm, "_get", side_effect=get_year) as get:
            blk = fm.series_block("DGS10", "pct")

        self.assertEqual(get.call_count, 2)
        self.assertEqual(blk["source"], "US Treasury")
        self.assertEqual(blk["latest_date"], latest_date)
        self.assertEqual(blk["prior_date"], prior_date)
        self.assertAlmostEqual(blk["delta_bps"], 10.0)

    def test_partition_failure_is_reported_with_partial_rows(self):
        current_year = fm.execution_now().year
        prior_year = current_year - 1
        prior_date = f"{prior_year}-12-27"

        def get_year(url, timeout=20):
            if f"field_tdr_date_value={current_year}" in url:
                raise OSError("current-year partition unavailable")
            return self._xml(prior_date, 4.40)

        with mock.patch.object(fm, "PRIOR", prior_date), \
             mock.patch.object(fm, "_get", side_effect=get_year):
            obs, meta = fm.treasury_10y()

        self.assertEqual(obs, [(prior_date, 4.40)])
        self.assertEqual(meta["failed_years"], [current_year])

    def test_current_partition_failure_cannot_masquerade_as_stale_ok(self):
        current_year = fm.execution_now().year
        prior_year = current_year - 1
        prior_date = f"{prior_year}-12-27"

        def get_year(url, timeout=20):
            if f"field_tdr_date_value={current_year}" in url:
                raise OSError("current-year partition unavailable")
            return self._xml(prior_date, 4.40)

        with mock.patch.object(fm, "PRIOR", prior_date), \
             mock.patch.object(fm, "fred_obs", side_effect=OSError("FRED down")), \
             mock.patch.object(fm, "_get", side_effect=get_year):
            blk = fm.series_block("DGS10", "pct")

        self.assertEqual(blk["status"], "fetch_failed")
        self.assertEqual(blk["fallback_failed_years"], [current_year])
        self.assertNotIn("no_new_obs", blk)

    def test_prior_partition_failure_keeps_current_level_but_not_delta(self):
        current_year = fm.execution_now().year
        prior_year = current_year - 1
        latest_date = f"{current_year}-01-03"
        prior_date = f"{prior_year}-12-27"

        def get_year(url, timeout=20):
            if f"field_tdr_date_value={prior_year}" in url:
                raise OSError("prior-year partition unavailable")
            return self._xml(latest_date, 4.50)

        with mock.patch.object(fm, "PRIOR", prior_date), \
             mock.patch.object(fm, "fred_obs", side_effect=OSError("FRED down")), \
             mock.patch.object(fm, "_get", side_effect=get_year):
            blk = fm.series_block("DGS10", "pct")

        self.assertEqual(blk["status"], "ok")
        self.assertEqual(blk["latest_date"], latest_date)
        self.assertEqual(blk["fallback_failed_years"], [prior_year])
        self.assertNotIn("delta_bps", blk)

    def test_xml_parser_never_pairs_across_entries(self):
        current_year = fm.execution_now().year
        bad_date = f"{current_year}-07-09"
        good_date = f"{current_year}-07-10"
        xml = (f"<entry><d:NEW_DATE>{bad_date}T00:00:00</d:NEW_DATE>"
               "<d:BC_10YEAR m:null=\"true\" /></entry>"
               + self._xml(good_date, 4.50))

        with mock.patch.object(fm, "PRIOR", "none"), \
             mock.patch.object(fm, "_get", return_value=xml):
            obs, meta = fm.treasury_10y()

        self.assertEqual(obs, [(good_date, 4.50)])
        self.assertEqual(meta["failed_years"], [])

    def test_valid_empty_feed_is_allowed_during_first_january_week(self):
        current_year = 2027
        prior_year = 2026
        prior_date = "2026-12-31"

        for day in (1, 7):
            with self.subTest(day=day):
                now = fm.datetime(2027, 1, day, 1, 0,
                                  tzinfo=fm.TAIPEI_TZ)

                def get_year(url, timeout=20):
                    if f"field_tdr_date_value={current_year}" in url:
                        # HTTP 200 with a recognizable Atom feed, but no
                        # current-year market observation yet.
                        return '<feed xmlns="http://www.w3.org/2005/Atom"></feed>'
                    if f"field_tdr_date_value={prior_year}" in url:
                        return self._xml(prior_date, 4.40)
                    raise AssertionError(f"unexpected Treasury URL: {url}")

                with mock.patch.object(fm, "PRIOR", "none"), \
                     mock.patch.object(fm, "execution_now", return_value=now), \
                     mock.patch.object(fm, "_get", side_effect=get_year) as get:
                    obs, meta = fm.treasury_10y()

                self.assertEqual(get.call_count, 2)
                self.assertEqual(meta["requested_years"],
                                 [current_year, prior_year])
                self.assertEqual(meta["empty_years"], [current_year])
                self.assertEqual(meta["failed_years"], [])
                self.assertEqual(obs, [(prior_date, 4.40)])

    def test_html_schema_drift_is_rejected_even_during_january_grace(self):
        current_year = 2027
        prior_year = 2026
        now = fm.datetime(2027, 1, 3, 1, 0, tzinfo=fm.TAIPEI_TZ)

        def get_year(url, timeout=20):
            if f"field_tdr_date_value={current_year}" in url:
                return "<html><body>scheduled maintenance</body></html>"
            return self._xml("2026-12-31", 4.40)

        with mock.patch.object(fm, "PRIOR", "none"), \
             mock.patch.object(fm, "execution_now", return_value=now), \
             mock.patch.object(fm, "_get", side_effect=get_year):
            obs, meta = fm.treasury_10y()

        self.assertEqual(obs, [("2026-12-31", 4.40)])
        self.assertEqual(meta["empty_years"], [])
        self.assertEqual(meta["failed_years"], [current_year])

    def test_empty_feed_is_rejected_after_first_january_week(self):
        current_year = 2027
        prior_year = 2026
        now = fm.datetime(2027, 1, 31, 12, 0, tzinfo=fm.TAIPEI_TZ)

        def get_year(url, timeout=20):
            if f"field_tdr_date_value={current_year}" in url:
                return '<feed xmlns="http://www.w3.org/2005/Atom"></feed>'
            return self._xml("2026-12-31", 4.40)

        with mock.patch.object(fm, "PRIOR", "none"), \
             mock.patch.object(fm, "execution_now", return_value=now), \
             mock.patch.object(fm, "_get", side_effect=get_year):
            obs, meta = fm.treasury_10y()

        self.assertEqual(obs, [("2026-12-31", 4.40)])
        self.assertEqual(meta["empty_years"], [])
        self.assertEqual(meta["failed_years"], [current_year])

    def test_http_200_empty_current_partition_fails_outside_january(self):
        now = fm.datetime(2027, 7, 13, 12, 0, tzinfo=fm.TAIPEI_TZ)

        with mock.patch.object(fm, "PRIOR", "none"), \
             mock.patch.object(fm, "execution_now", return_value=now), \
             mock.patch.object(fm, "fred_obs", side_effect=OSError("FRED down")), \
             mock.patch.object(fm, "_get", return_value=""):
            blk = fm.series_block("DGS10", "pct")

        self.assertEqual(blk["status"], "fetch_failed")
        self.assertEqual(blk["fallback_failed_years"], [2027])


class OutputSchema(unittest.TestCase):
    def test_main_emits_versioned_taipei_timestamp(self):
        now = fm.datetime(2027, 1, 1, 1, 2, 3, tzinfo=fm.TAIPEI_TZ)
        failed = {"status": "fetch_failed", "source": None}
        stdout = io.StringIO()

        with mock.patch.object(fm, "PRIOR", "none"), \
             mock.patch.object(fm, "execution_now", return_value=now), \
             mock.patch.object(fm, "series_block", return_value=failed.copy()), \
             mock.patch.object(fm, "sp500_trend", return_value=failed.copy()), \
             mock.patch.object(fm, "cftc_lev_funds", return_value=failed.copy()), \
             mock.patch.object(fm, "move_index", return_value=failed.copy()), \
             mock.patch.object(fm, "ofr_repo", return_value=failed.copy()), \
             contextlib.redirect_stdout(stdout):
            fm.main()

        payload = stdout.getvalue().split("===MACRO_JSON_START===\n", 1)[1]
        payload = payload.split("\n===MACRO_JSON_END===", 1)[0]
        out = json.loads(payload)
        self.assertEqual(out["contract_version"], 1)
        self.assertEqual(out["macro_schema_version"], 1)
        self.assertEqual(out["generated_at"], "2027-01-01T01:02:03+08:00")
        generated = fm.datetime.fromisoformat(out["generated_at"])
        self.assertIsNotNone(generated.utcoffset())
        self.assertEqual(generated.utcoffset(), fm.timedelta(hours=8))


class Cftc(unittest.TestCase):
    def test_history_year_uses_taipei_execution_year(self):
        # 2027 in Taipei is still 2026 UTC; output partitioning follows the
        # report timezone, not UTC.
        now = fm.datetime(2027, 1, 1, 0, 30, tzinfo=fm.TAIPEI_TZ)
        requested = []

        def fail_archive(url, timeout=20):
            requested.append(url)
            raise OSError("offline")

        with mock.patch.object(fm, "execution_now", return_value=now), \
             mock.patch.object(fm, "_get_bytes", side_effect=fail_archive), \
             mock.patch.object(fm, "_get", side_effect=OSError("offline")):
            blk = fm.cftc_lev_funds()

        self.assertEqual(blk["status"], "fetch_failed")
        self.assertIn("fut_fin_txt_2027.zip", requested[0])
        self.assertIn("fut_fin_txt_2026.zip", requested[1])

    def test_noncanonical_and_impossible_report_dates_are_ignored(self):
        def row(day, long_count, short_count):
            fields = [""] * 17
            fields[0] = "UST 10Y NOTE"
            fields[2] = day
            fields[14] = str(long_count)
            fields[15] = str(short_count)
            return ",".join(fields)

        weekly = "\n".join([
            row("2026-7-10", 999, 1),
            row("2026-02-30", 999, 1),
            row("not-a-date", 999, 1),
            row("2026-07-10", 150, 100),
        ])
        with mock.patch.object(fm, "_get_bytes", side_effect=OSError("offline")), \
             mock.patch.object(fm, "_get", return_value=weekly):
            blk = fm.cftc_lev_funds()

        self.assertEqual(blk["status"], "ok")
        self.assertEqual(blk["latest_date"], "2026-07-10")
        self.assertEqual(blk["net_contracts"], 50)
        self.assertEqual(blk["recent_weeks"], [
            {"date": "2026-07-10", "net": 50},
        ])


class Sp500Trend(unittest.TestCase):
    def test_percentages_are_computed_from_emitted_rounded_legs(self):
        start = fm.datetime(2026, 7, 10)
        raw_values = [100.004, 99.996] + [99.9951] * 198
        observations = [
            {
                "date": (start - fm.timedelta(days=i)).strftime("%Y-%m-%d"),
                "value": str(value),
            }
            for i, value in enumerate(raw_values)
        ]
        payload = json.dumps({"observations": observations})

        with mock.patch.object(fm, "PRIOR", "2026-07-09"), \
             mock.patch.object(fm, "_get", return_value=payload):
            blk = fm.sp500_trend()

        self.assertEqual(blk["status"], "ok")
        self.assertEqual(blk["latest"], 100.0)
        self.assertEqual(blk["ma200"], 100.0)
        self.assertEqual(blk["dev200_pct"], 0.0)
        self.assertEqual(blk["prior_spot"], 100.0)
        self.assertEqual(blk["chg_pct"], 0.0)
        # Raw inputs would round to a different deviation; this proves the
        # percentage is reproducible from the values actually serialized.
        raw_ma = sum(raw_values) / len(raw_values)
        self.assertEqual(round((raw_values[0] - raw_ma) / raw_ma * 100, 2),
                         0.01)


class MoveIndex(unittest.TestCase):
    def test_bad_element_is_skipped_without_crashing(self):
        payload = {"chart": {"result": [{
            "timestamp": [1_788_739_200, "bad timestamp"],
            "indicators": {"quote": [{"close": [101.25, "bad close"]}]},
        }]}}
        with mock.patch.object(fm, "PRIOR", "none"), \
             mock.patch.object(fm, "_get", return_value=json.dumps(payload)):
            blk = fm.move_index()

        self.assertEqual(blk["status"], "ok")
        self.assertEqual(blk["latest"], 101.25)


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
    """Each spread uses an IORB print no newer than its SOFR leg.  When
    SOFR99 lags the SOFR print, IORB must be looked up again at that earlier
    as-of date rather than reused from the headline SOFR spread."""

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
        self.assertEqual(rs["status"], "partial")  # spread usable; SRF omitted
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
        self.assertEqual(rs["status"], "partial")  # spread usable; SRF omitted
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
        self.assertEqual(rs["status"], "partial")  # spread usable; SRF omitted
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

    def test_srf_survives_sofr_and_iorb_failure_as_partial(self):
        series = {
            "SOFR": {"status": "fetch_failed", "source": None},
            "IORB": {"status": "fetch_failed", "source": None},
            "RPONTTLD": {"status": "ok", "latest_date": "2026-07-10",
                          "latest": 12.5},
        }
        rs = fm.repo_stress_block(series)
        self.assertEqual(rs["status"], "partial")
        self.assertEqual(rs["srf_usage_bn"], 12.5)
        self.assertEqual(rs["srf_date"], "2026-07-10")
        self.assertNotIn("sofr_iorb_bps", rs)

    def test_srf_survives_unalignable_iorb_as_partial(self):
        # IORB's only observation is newer than SOFR, so no spread is valid;
        # the independent RPONTTLD reading must still be returned.
        fm.OBS_CACHE.update({
            "SOFR": [("2026-07-30", 4.62)],
            "IORB": [("2026-07-31", 4.15)],
        })
        series = {
            "SOFR": {"status": "ok", "latest_date": "2026-07-30",
                      "latest": 4.62},
            "IORB": {"status": "ok", "latest_date": "2026-07-31",
                      "latest": 4.15},
            "RPONTTLD": {"status": "ok", "latest_date": "2026-07-30",
                          "latest": 8.0},
        }
        rs = fm.repo_stress_block(series)
        self.assertEqual(rs["status"], "partial")
        self.assertEqual(rs["srf_usage_bn"], 8.0)

    def test_spread_and_srf_make_complete_ok_block(self):
        fm.OBS_CACHE.update({
            "SOFR": [("2026-07-31", 4.40)],
            "IORB": [("2026-07-31", 4.15)],
        })
        series = {
            "SOFR": {"status": "ok", "latest_date": "2026-07-31",
                      "latest": 4.40},
            "IORB": {"status": "ok", "latest_date": "2026-07-31",
                      "latest": 4.15},
            "RPONTTLD": {"status": "ok", "latest_date": "2026-07-31",
                          "latest": 5.0},
        }
        rs = fm.repo_stress_block(series)
        self.assertEqual(rs["status"], "ok")
        self.assertEqual(rs["sofr_iorb_bps"], 25.0)
        self.assertEqual(rs["srf_usage_bn"], 5.0)


class DecompositionWindow(unittest.TestCase):
    """ΔT10YIE may be rebuilt from ΔDGS10 − ΔDFII10 only when both legs
    cover the same window (same latest and prior dates)."""

    def test_baseline_is_not_misreported_as_missing_daily_history(self):
        series = {
            "DGS10": {"status": "ok", "latest_date": "2026-07-10",
                      "latest": 4.5},
            "DFII10": {"status": "ok", "latest_date": "2026-07-10",
                       "latest": 2.2},
            "T10YIE": {"status": "ok", "latest_date": "2026-07-10",
                       "latest": 2.3},
        }
        blk = fm.decomposition_block(series, baseline=True)
        self.assertEqual(blk["status"], "baseline_no_prior")
        self.assertEqual(blk["driver"], "baseline")
        self.assertEqual(blk["freshness"], "not_applicable")
        self.assertNotIn("daily history", blk["note"])

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
            "T10YIE": {"status": "ok", "latest_date": "2026-07-10",
                       "prior_date": "2026-07-03", "delta_bps": 1.0},
        }
        blk = fm.decomposition_block(series)
        self.assertEqual(blk["status"], "ok")
        self.assertAlmostEqual(blk["d_t10yie_bps"], 1.0)
        self.assertEqual(blk["driver"], "real-rate")

    def test_same_window_identity_residual_over_tolerance_is_unknown(self):
        contract = json.loads((REPO / "report_contract.json").read_text())
        tolerance = contract["calibration"][
            "decomposition_identity_tolerance_bps"]
        self.assertEqual(fm.DECOMPOSITION_IDENTITY_TOLERANCE_BPS, tolerance)
        series = {
            "DGS10": {"status": "ok", "latest_date": "2026-07-10",
                      "prior_date": "2026-07-03", "delta_bps": 6.0},
            "DFII10": {"status": "ok", "latest_date": "2026-07-10",
                       "prior_date": "2026-07-03", "delta_bps": 2.0},
            "T10YIE": {"status": "ok", "latest_date": "2026-07-10",
                       "prior_date": "2026-07-03",
                       "delta_bps": 4.0 + tolerance + 0.1},
        }

        blk = fm.decomposition_block(series)

        self.assertEqual(blk["status"], "ok")
        self.assertEqual(blk["driver"], "unknown")
        self.assertIn("identity residual exceeds tolerance", blk["note"])

    def test_all_zero_no_new_obs_is_none_despite_window_mismatch(self):
        # holiday run: every series stale vs prior (delta 0 by construction),
        # T10YIE last printed one business day earlier — zero change needs no
        # window alignment to attribute, so the driver is 無變動, not 不可判
        series = {
            "DGS10": {"status": "ok", "latest_date": "2026-07-09",
                      "prior_date": "2026-07-09", "delta_bps": 0.0,
                      "no_new_obs": True},
            "DFII10": {"status": "ok", "latest_date": "2026-07-09",
                       "prior_date": "2026-07-09", "delta_bps": 0.0,
                       "no_new_obs": True},
            "T10YIE": {"status": "ok", "latest_date": "2026-07-08",
                       "prior_date": "2026-07-08", "delta_bps": 0.0,
                       "no_new_obs": True},
        }
        blk = fm.decomposition_block(series)
        self.assertEqual(blk["driver"], "none")
        self.assertEqual(blk["freshness"], "all_stale")
        self.assertEqual(blk["stale_series"], ["DGS10", "DFII10", "T10YIE"])
        self.assertIn("all delta-bearing input series have no new observations",
                      blk["note"])

    def test_all_zero_updated_observations_is_none_but_not_stale(self):
        series = {
            "DGS10": {"status": "ok", "latest_date": "2026-07-10",
                      "prior_date": "2026-07-03", "delta_bps": 0.0},
            "DFII10": {"status": "ok", "latest_date": "2026-07-10",
                       "prior_date": "2026-07-03", "delta_bps": 0.0},
            "T10YIE": {"status": "ok", "latest_date": "2026-07-10",
                       "prior_date": "2026-07-03", "delta_bps": 0.0},
        }
        blk = fm.decomposition_block(series)
        self.assertEqual(blk["driver"], "none")
        self.assertEqual(blk["freshness"], "updated")
        self.assertEqual(blk["stale_series"], [])
        self.assertIn("all available delta-bearing input series updated", blk["note"])
        self.assertNotIn("no new observations", blk["note"])

    def test_partial_stale_lists_only_unchanged_series(self):
        # All deltas happen to be zero, but only DGS10 reused its prior print.
        # Driver and freshness therefore remain independent.
        series = {
            "DGS10": {"status": "ok", "latest_date": "2026-07-03",
                      "prior_date": "2026-07-03", "delta_bps": 0.0,
                      "no_new_obs": True},
            "DFII10": {"status": "ok", "latest_date": "2026-07-10",
                       "prior_date": "2026-07-03", "delta_bps": 0.0},
            "T10YIE": {"status": "ok", "latest_date": "2026-07-10",
                       "prior_date": "2026-07-03", "delta_bps": 0.0},
        }
        blk = fm.decomposition_block(series)
        self.assertEqual(blk["driver"], "none")
        self.assertEqual(blk["freshness"], "partial_stale")
        self.assertEqual(blk["stale_series"], ["DGS10"])
        self.assertIn("no new observations for DGS10", blk["note"])
        self.assertIn("remaining delta-bearing input series updated", blk["note"])

    def test_derived_breakeven_inherits_all_stale_freshness_from_rate_legs(self):
        # A missing direct T10YIE delta is rebuilt from two stale, aligned legs;
        # it must not make the overall freshness look merely partial.
        series = {
            "DGS10": {"status": "ok", "latest_date": "2026-07-09",
                      "prior_date": "2026-07-09", "delta_bps": 0.0,
                      "no_new_obs": True},
            "DFII10": {"status": "ok", "latest_date": "2026-07-09",
                       "prior_date": "2026-07-09", "delta_bps": 0.0,
                       "no_new_obs": True},
            "T10YIE": {"status": "derived"},
        }
        blk = fm.decomposition_block(series)
        self.assertEqual(blk["driver"], "none")
        self.assertEqual(blk["freshness"], "all_stale")
        self.assertEqual(blk["stale_series"], ["DGS10", "DFII10"])

    def test_direct_t10yie_mismatched_window_keeps_delta_but_unknown_driver(self):
        # 6 ≠ 2 + 20: the direct T10YIE delta covers a different window, so
        # the identity does not hold and the driver must not be judged
        series = {
            "DGS10": {"status": "ok", "latest_date": "2026-07-10",
                      "prior_date": "2026-07-03", "delta_bps": 6.0},
            "DFII10": {"status": "ok", "latest_date": "2026-07-10",
                       "prior_date": "2026-07-03", "delta_bps": 2.0},
            "T10YIE": {"status": "ok", "latest_date": "2026-07-09",
                       "prior_date": "2026-07-02", "delta_bps": 20.0},
        }
        blk = fm.decomposition_block(series)
        self.assertAlmostEqual(blk["d_t10yie_bps"], 20.0)
        self.assertEqual(blk["driver"], "unknown")


class Pick(unittest.TestCase):
    def test_on_or_before(self):
        obs = [("2026-07-10", 2.0), ("2026-07-08", 1.0)]
        self.assertEqual(fm.pick(obs, "2026-07-09"), ("2026-07-08", 1.0))

    def test_none_when_all_newer(self):
        obs = [("2026-07-10", 2.0)]
        self.assertIsNone(fm.pick(obs, "2026-07-01"))


class OfrRepo(unittest.TestCase):
    def test_transaction_volume_fields_are_explicit(self):
        mnemonic = "REPO-TRIV1_TV_TOT-P"
        payload = {
            mnemonic: {"timeseries": {"aggregation": [
                ["2026-07-03", 3_000_000_000.0],
                ["2026-07-10", 3_300_000_000.0],
            ]}}
        }
        with mock.patch.object(fm, "PRIOR", "2026-07-03"), \
             mock.patch.object(fm, "_get", return_value=json.dumps(payload)):
            blk = fm.ofr_repo()

        self.assertEqual(blk["status"], "ok")
        self.assertEqual(blk["transaction_volume_usd_bn"], 3.3)
        self.assertEqual(blk["prior_transaction_volume_usd_bn"], 3.0)
        self.assertEqual(blk["chg_pct"], 10.0)
        self.assertNotIn("latest_usd_bn", blk)
        self.assertNotIn("prior_usd_bn", blk)

    def test_change_is_computed_from_emitted_rounded_volumes(self):
        mnemonic = "REPO-TRIV1_TV_TOT-P"
        latest_raw = 1_049_000_000.0
        prior_raw = 1_041_000_000.0
        payload = {
            mnemonic: {"timeseries": {"aggregation": [
                ["2026-07-03", prior_raw],
                ["2026-07-10", latest_raw],
            ]}}
        }
        with mock.patch.object(fm, "PRIOR", "2026-07-03"), \
             mock.patch.object(fm, "_get", return_value=json.dumps(payload)):
            blk = fm.ofr_repo()

        self.assertEqual(blk["transaction_volume_usd_bn"], 1.0)
        self.assertEqual(blk["prior_transaction_volume_usd_bn"], 1.0)
        self.assertEqual(blk["chg_pct"], 0.0)
        self.assertEqual(round((latest_raw - prior_raw) / prior_raw * 100, 2),
                         0.77)

    def test_zero_same_date_volume_is_explicit_no_new_change(self):
        mnemonic = "REPO-TRIV1_TV_TOT-P"
        payload = {
            mnemonic: {"timeseries": {"aggregation": [
                ["2026-07-10", 0.0],
            ]}}
        }
        with mock.patch.object(fm, "PRIOR", "2026-07-10"), \
             mock.patch.object(fm, "_get", return_value=json.dumps(payload)):
            blk = fm.ofr_repo()

        self.assertTrue(blk["no_new_obs"])
        self.assertEqual(blk["transaction_volume_usd_bn"], 0.0)
        self.assertEqual(blk["prior_transaction_volume_usd_bn"], 0.0)
        self.assertEqual(blk["chg_pct"], 0.0)


class VixSpxComove(unittest.TestCase):
    """Derived VIX / S&P 500 co-movement block.

    The window comes from the dates the two series share inside their bounded
    alignment proofs, not from the prior-run date: FRED publishes SP500 one
    business day ahead of VIXCLS.
    """

    LATEST = "2026-07-10"
    BASE = "2026-07-02"          # 8 days back: inside the trailing window

    def vix(self, latest=15.0, base=15.0, latest_date=None, base_date=None):
        return {"VIXCLS": {
            "status": "ok", "source": "FRED API",
            "latest_date": latest_date or self.LATEST, "latest": latest,
            "alignment_observations": [
                {"date": latest_date or self.LATEST, "value": latest},
                {"date": base_date or self.BASE, "value": base},
            ],
        }}

    def sp500(self, latest=7575.39, base=7500.0, latest_date=None,
              base_date=None):
        return {
            "status": "ok", "source": "FRED API",
            "latest_date": latest_date or self.LATEST, "latest": latest,
            "alignment_observations": [
                {"date": latest_date or self.LATEST, "value": latest},
                {"date": base_date or self.BASE, "value": base},
            ],
        }

    def test_both_legs_rising_beyond_threshold_is_comove(self):
        blk = fm.vix_spx_comove_block(self.vix(latest=17.0), self.sp500())
        self.assertEqual(blk["status"], "ok")
        self.assertTrue(blk["comove"])
        self.assertEqual(blk["vix_chg_pct"], 13.33)
        self.assertEqual(blk["sp500_chg_pct"], 1.01)
        self.assertEqual(blk["as_of"], self.LATEST)
        self.assertEqual(blk["base_date"], self.BASE)
        self.assertEqual(blk["window_days"], 8)

    def test_vix_rise_below_threshold_is_not_comove(self):
        # +2.0% VIX clears zero but not calibration.vix_comove_chg_pct
        blk = fm.vix_spx_comove_block(self.vix(latest=15.3), self.sp500())
        self.assertEqual(blk["status"], "ok")
        self.assertFalse(blk["comove"])
        self.assertEqual(blk["vix_chg_pct"], 2.0)

    def test_equity_leg_below_threshold_is_not_comove(self):
        # VIX spiking while the index is flat is ordinary risk-off, not the
        # crowded-optionality read this block exists to flag
        blk = fm.vix_spx_comove_block(
            self.vix(latest=18.0), self.sp500(latest=7502.0)
        )
        self.assertEqual(blk["status"], "ok")
        self.assertFalse(blk["comove"])

    def test_falling_equity_leg_is_not_comove(self):
        blk = fm.vix_spx_comove_block(
            self.vix(latest=18.0), self.sp500(latest=7200.0)
        )
        self.assertEqual(blk["status"], "ok")
        self.assertFalse(blk["comove"])

    def test_lagging_vix_publication_still_yields_a_window(self):
        # the live failure mode: SP500 prints 07-13, VIXCLS only through 07-10
        sp500 = self.sp500(latest_date="2026-07-13")
        sp500["alignment_observations"] = [
            {"date": "2026-07-13", "value": 7600.0},
            {"date": self.LATEST, "value": 7575.39},
            {"date": self.BASE, "value": 7500.0},
        ]
        blk = fm.vix_spx_comove_block(self.vix(latest=17.0), sp500)
        self.assertEqual(blk["status"], "ok")
        self.assertEqual(blk["as_of"], self.LATEST)   # newest SHARED date
        self.assertEqual(blk["sp500"], 7575.39)
        self.assertTrue(blk["comove"])

    def test_failed_vix_series_is_unavailable(self):
        blk = fm.vix_spx_comove_block(
            {"VIXCLS": {"status": "fetch_failed", "source": None}}, self.sp500()
        )
        self.assertEqual(blk["status"], "unavailable")
        self.assertFalse(blk["comove"])
        self.assertNotIn("vix", blk)

    def test_failed_sp500_block_is_unavailable(self):
        blk = fm.vix_spx_comove_block(
            self.vix(latest=17.0), {"status": "fetch_failed", "source": None}
        )
        self.assertEqual(blk["status"], "unavailable")

    def test_no_shared_date_is_unavailable(self):
        blk = fm.vix_spx_comove_block(
            self.vix(latest=17.0, latest_date="2026-07-09",
                     base_date="2026-07-01"),
            self.sp500(),
        )
        self.assertEqual(blk["status"], "unavailable")
        self.assertNotIn("vix_chg_pct", blk)

    def test_no_shared_base_is_unavailable(self):
        vix = self.vix(latest=17.0)
        del vix["VIXCLS"]["alignment_observations"][1]
        blk = fm.vix_spx_comove_block(vix, self.sp500())
        self.assertEqual(blk["status"], "unavailable")

    def test_base_older_than_twice_the_window_is_unavailable(self):
        stale = "2026-06-20"     # 20 days > 2 x 7
        blk = fm.vix_spx_comove_block(
            self.vix(latest=17.0, base_date=stale),
            self.sp500(base_date=stale),
        )
        self.assertEqual(blk["status"], "unavailable")

    def test_base_at_the_window_edge_is_accepted(self):
        edge = "2026-06-26"      # exactly 14 days back
        blk = fm.vix_spx_comove_block(
            self.vix(latest=17.0, base_date=edge),
            self.sp500(base_date=edge),
        )
        self.assertEqual(blk["status"], "ok")
        self.assertEqual(blk["window_days"], 14)

    def test_nonpositive_base_is_unavailable(self):
        blk = fm.vix_spx_comove_block(
            self.vix(latest=17.0, base=0.0), self.sp500()
        )
        self.assertEqual(blk["status"], "unavailable")

    def test_thresholds_come_from_the_contract(self):
        contract = json.loads(
            (REPO / "report_contract.json").read_text(encoding="utf-8")
        )
        self.assertEqual(
            fm.VIX_COMOVE_CHG_PCT, contract["calibration"]["vix_comove_chg_pct"]
        )
        self.assertEqual(
            fm.VIX_COMOVE_TRAILING_DAYS,
            contract["calibration"]["vix_comove_trailing_days"],
        )
        self.assertEqual(
            fm.SP500_COMOVE_CHG_PCT,
            contract["direction_thresholds"]["sp500_chg_pct"],
        )


if __name__ == "__main__":
    unittest.main()

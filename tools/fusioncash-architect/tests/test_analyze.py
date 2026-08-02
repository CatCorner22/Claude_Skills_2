from fusioncash_architect.ingest import Extract
from fusioncash_architect.analyze import analyze, build_waterfalls, gl_audit, health_score


def _extracts(tcr_rows, matching_rows, recon_rows, tol_rows):
    return {
        "tcr": Extract("tcr", "tcr.xlsx", tcr_rows),
        "matching": Extract("matching", "m.xlsx", matching_rows),
        "recon": Extract("recon", "r.xlsx", recon_rows),
        "tolerance": Extract("tolerance", "t.xlsx", tol_rows),
    }


def _clean():
    """A small, best-practice-clean config: few TCRs, all bank-originated,
    1:1 before 1:M, tight tolerance, clean GL."""
    tcr = [
        {"name": "Bank Fee", "txn_type": "BKF", "bank_account": "BOA - Master",
         "cash_gl": "01-1100098-000", "offset_gl": "01-6500000-000"},
        {"name": "Interest", "txn_type": "INT", "bank_account": "BOA - Master",
         "cash_gl": "01-1100098-000", "offset_gl": "01-4900000-000"},
    ]
    matching = [
        {"name": "R1", "match_type": "1:1"},
        {"name": "R2", "match_type": "1:M"},
    ]
    recon = [
        {"ruleset": "RS", "description": "d", "sequence": "1", "matching_rule": "R1", "tolerance_rule": "T"},
        {"ruleset": "RS", "description": "d", "sequence": "2", "matching_rule": "R2", "tolerance_rule": "T"},
    ]
    tol = [{"name": "T", "date_enabled": "Y", "days_before": "2", "days_after": "2"}]
    return _extracts(tcr, matching, recon, tol)


def _messy():
    """Lots of subledger-suspect TCRs, an inverted ruleset, wide tolerance."""
    tcr = [{"name": f"ACH {i}", "txn_type": "ACH", "bank_account": "BOA - Master",
            "cash_gl": "01-1100098-000", "offset_gl": "01-2000000-000"} for i in range(50)]
    matching = [{"name": "R1", "match_type": "1:1"}, {"name": "R2", "match_type": "1:M"}]
    recon = [  # 1:M before 1:1 -> inversion
        {"ruleset": "RS", "description": "d", "sequence": "1", "matching_rule": "R2", "tolerance_rule": "T"},
        {"ruleset": "RS", "description": "d", "sequence": "2", "matching_rule": "R1", "tolerance_rule": "T"},
    ]
    tol = [{"name": "T", "date_enabled": "Y", "days_before": "30", "days_after": "30"}]
    return _extracts(tcr, matching, recon, tol)


class TestWaterfalls:
    def test_orders_by_sequence_and_flags_inversion(self):
        w = build_waterfalls(_messy())
        assert len(w) == 1
        steps = w[0]["steps"]
        assert [s["sequence"] for s in steps] == ["1", "2"]
        assert steps[0]["match_type"] == "1:M"
        assert steps[1]["match_type"] == "1:1"
        assert steps[1]["precedence_violation"] is True
        assert w[0]["violations"] == 1

    def test_clean_has_no_violation(self):
        w = build_waterfalls(_clean())
        assert w[0]["violations"] == 0


class TestGlAudit:
    def test_natural_account_extraction(self):
        gl = gl_audit(_clean())
        assert "1100098" in gl["cash_accounts"]
        assert gl["anomalies"] == []

    def test_identical_cash_offset_flagged(self):
        ex = _extracts(
            [{"name": "Bad", "txn_type": "BKF", "bank_account": "X",
              "cash_gl": "01-1100098-000", "offset_gl": "01-1100098-000"}],
            [{"name": "R1", "match_type": "1:1"}], [], [])
        gl = gl_audit(ex)
        assert any("identical" in a["issue"] for a in gl["anomalies"])


class TestHealthScore:
    def test_clean_scores_well(self):
        ex = _clean()
        h = health_score(ex, build_waterfalls(ex), gl_audit(ex))
        assert h["score"] >= 85 and h["grade"] in ("A", "B")

    def test_messy_scores_poorly(self):
        ex = _messy()
        h = health_score(ex, build_waterfalls(ex), gl_audit(ex))
        assert h["score"] < 60 and h["grade"] in ("D", "F")
        principles = {f["principle"] for f in h["findings"]}
        assert "Minimize TCRs" in principles
        assert "Subledger supremacy" in principles

    def test_score_bounded(self):
        for ex in (_clean(), _messy()):
            h = health_score(ex, build_waterfalls(ex), gl_audit(ex))
            assert 0 <= h["score"] <= 100


class TestAnalyzePayload:
    def test_shape(self):
        res = analyze(_messy())
        for key in ("counts", "health", "tcr_types", "bank_accounts",
                    "gl_audit", "waterfalls", "advanced_criteria_examples", "parse_patterns"):
            assert key in res
        assert res["counts"]["tcr_rows"] == 50
        assert res["counts"]["bank_accounts"] == 1

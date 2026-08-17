import json

from fusioncash_architect.ingest import Extract
from fusioncash_architect.report import build_payload, render_html


def _extracts():
    tcr = [{"name": "Bank Fee", "txn_type": "BKF", "bank_account": "BOA - Master",
            "cash_gl": "01-1100098-000", "offset_gl": "01-6500000-000"}]
    matching = [{"name": "AP Bank Card 1:1", "match_type": "1:1",
                 "advanced_criteria": "( s.ADDENDA_TXT LIKE '%'|| 'BANK CARD' ||'%' )"}]
    recon = [{"ruleset": "RS", "description": "d", "sequence": "1",
              "matching_rule": "AP Bank Card 1:1", "tolerance_rule": "T"}]
    parse = [{"parse_rule": "(X~)", "txn_code": "142"}]
    tol = [{"name": "T", "date_enabled": "Y", "days_before": "2", "days_after": "2"}]
    return {
        "tcr": Extract("tcr", "tcr.xlsx", tcr),
        "matching": Extract("matching", "m.xlsx", matching),
        "recon": Extract("recon", "r.xlsx", recon),
        "parse": Extract("parse", "p.xlsx", parse),
        "tolerance": Extract("tolerance", "t.xlsx", tol),
    }


def test_payload_has_examples_with_derived_sample():
    p = build_payload(_extracts())
    assert p["baseline_pdf"]["tcrs"] == 1050
    ce = p["criteria_examples"]
    assert ce and ce[0]["criteria"]
    # the BANK CARD example should get a synthesized satisfying sample
    assert ce[0]["sample"]["s.ADDENDA_TXT"] == "BANK CARD"
    assert p["parse_examples"][0]["rule"] == "(X~)"
    # advanced_criteria_examples/parse_patterns are consumed, not re-exported
    assert "advanced_criteria_examples" not in p
    assert "parse_patterns" not in p


def test_render_injects_data_and_no_placeholder():
    html = render_html(_extracts())
    assert "__DATA_JSON__" not in html
    assert "const DATA =" in html
    assert "FusionCash Architect" in html
    # embedded JSON must not contain a raw '<' that could break the script
    start = html.index("const DATA =") + len("const DATA =")
    end = html.index(";\n", start)
    blob = html[start:end].strip()
    data = json.loads(blob.replace("\\u003c", "<"))
    assert data["counts"]["tcr_rows"] == 1

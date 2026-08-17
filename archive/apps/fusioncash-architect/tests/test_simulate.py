from fusioncash_architect.simulate import (
    simulate_criteria, simulate_parse_rule, fields_referenced,
)

BANK_CARD = ("(  (  ( s.ADDENDA_TXT LIKE '%'|| 'BANK CARD' ||'%' ) AND "
             "( t.CPARTY_NAME LIKE '%'|| 'BANK OF AMERICA, N.A.' ||'%' )  )   )")


class TestCriteria:
    def test_pdf_example_true(self):
        r = simulate_criteria(BANK_CARD, {
            "s.ADDENDA_TXT": "DEPOSIT BANK CARD MERCH 123",
            "t.CPARTY_NAME": "BANK OF AMERICA, N.A.",
        })
        assert r["result"] is True and r["error"] is None

    def test_pdf_example_false_wrong_cparty(self):
        r = simulate_criteria(BANK_CARD, {
            "s.ADDENDA_TXT": "DEPOSIT BANK CARD MERCH 123",
            "t.CPARTY_NAME": "WELLS FARGO",
        })
        assert r["result"] is False

    def test_case_sensitive(self):
        r = simulate_criteria("s.X LIKE '%'|| 'ABC' ||'%'", {"s.X": "abc"})
        assert r["result"] is False

    def test_fields_referenced(self):
        assert fields_referenced(BANK_CARD) == ["s.ADDENDA_TXT", "t.CPARTY_NAME"]

    def test_equality(self):
        e = "t.RECON_MATCH_REFERENCE = '011413'"
        assert simulate_criteria(e, {"t.RECON_MATCH_REFERENCE": "011413"})["result"] is True
        assert simulate_criteria(e, {"t.RECON_MATCH_REFERENCE": "999"})["result"] is False

    def test_or_and_not(self):
        assert simulate_criteria("s.X LIKE '%A%' OR s.X LIKE '%B%'", {"s.X": "zzB"})["result"] is True
        assert simulate_criteria("s.X NOT LIKE '%FEE%'", {"s.X": "DEPOSIT"})["result"] is True
        assert simulate_criteria("s.X NOT LIKE '%FEE%'", {"s.X": "BANK FEE"})["result"] is False

    def test_in_list(self):
        e = "s.CODE IN ('142', '174', '495')"
        assert simulate_criteria(e, {"s.CODE": "174"})["result"] is True
        assert simulate_criteria(e, {"s.CODE": "999"})["result"] is False

    def test_wildcards(self):
        assert simulate_criteria("s.X LIKE 'AB_D'", {"s.X": "ABCD"})["result"] is True
        assert simulate_criteria("s.X LIKE 'AB%'", {"s.X": "ABANYTHING"})["result"] is True
        assert simulate_criteria("s.X LIKE 'AB_'", {"s.X": "ABCD"})["result"] is False

    def test_syntax_error_reported(self):
        r = simulate_criteria("( s.X LIKE 'a' ", {})
        assert r["result"] is None and "parenthesis" in r["error"]

    def test_missing_field_is_empty(self):
        # unspecified field resolves to empty string, so a contains-match is False
        assert simulate_criteria("s.X LIKE '%A%'", {})["result"] is False


class TestParse:
    def test_capture_all(self):
        r = simulate_parse_rule("(X~)", "0006789599")
        assert r["matched"] and r["output"] == "0006789599"

    def test_delimiter_bounded(self):
        r = simulate_parse_rule("SENDING CO NAME: (X~)ENTRY DES",
                                "XSENDING CO NAME: ACME CORP ENTRY DESCR")
        assert r["output"] == "ACME CORP "

    def test_positional(self):
        assert simulate_parse_rule("(1-10)", "ABCDEFGHIJKLMNOP")["output"] == "ABCDEFGHIJ"

    def test_positional_with_prefix(self):
        r = simulate_parse_rule("SERVICMERCH DEP (16-25)", "SERVICMERCH DEP 1234567890 X")
        assert r["output"] == " 123456789"

    def test_leading_zero_ladder_match(self):
        # 9 zeros + "42": the 9-zero ladder rule captures "42"
        r = simulate_parse_rule("000000000(NN)", "00000000042")
        assert r["matched"] and r["output"] == "42"

    def test_leading_zero_ladder_skip(self):
        # 10-zero rule must NOT match a value with only 9 leading zeros
        r = simulate_parse_rule("0000000000(N)", "00000000042")
        assert r["matched"] is False

    def test_class_mismatch(self):
        r = simulate_parse_rule("(NNN)", "AB1")
        assert r["matched"] is False and "N-class" in r["error"]

    def test_class_alpha(self):
        assert simulate_parse_rule("(AAA)", "ABC123")["output"] == "ABC"

    def test_unknown_token(self):
        r = simulate_parse_rule("(Q?)", "x")
        assert r["matched"] is False and "unsupported" in r["error"]

    def test_missing_delimiter(self):
        r = simulate_parse_rule("PREFIX (X~)", "no prefix here")
        assert r["matched"] is False and "not found" in r["error"]

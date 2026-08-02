"""Analysis of ingested CM configuration extracts.

Produces the data behind FusionCash Architect's four modules:
  1. Dashboard + Health Score (Oracle best-practice scoring)
  2. Recon ruleset waterfall (with 1:1-before-1:M precedence checks)
  3. (Advanced-criteria simulation lives in simulate.py / the browser)
  4. (Parse-rule sandbox lives in simulate.py / the browser)

The Health Score is a weighted 0-100 index. Every weight and threshold below
is justified in a comment — no voodoo constants — and every deduction produces
a human-readable finding tied to the best-practice principle it enforces.
"""
from __future__ import annotations

from .ingest import Extract

# Transaction types that LEGITIMATELY originate at the bank and therefore
# justify a Transaction Creation Rule (subledger-supremacy: TCRs are reserved
# for items with no upstream AP/AR record).
BANK_ORIGINATED_TYPES = {"BKF", "INT", "ZBA"}  # bank fee, interest, sweep/ZBA
# Types that usually SHOULD have an upstream subledger source and thus make a
# TCR a candidate architectural smell (a patch for AP/AR that AutoMatch/Lockbox
# should own).
SUBLEDGER_SUSPECT_TYPES = {"ACH", "CHK", "EFT", "MSC"}

# A day tolerance beyond this many days is "loose" — timing differences rarely
# exceed a few business days, and wider windows invite false-positive matches.
LOOSE_DAY_TOLERANCE = 5


def _to_int(s, default=None):
    try:
        return int(str(s).strip())
    except (TypeError, ValueError):
        return default


def _match_type_of(name: str, matching_index: dict[str, str]) -> str:
    """Resolve a recon-referenced matching-rule name to its match type, by
    exact lookup first, then by inference from the name text."""
    if name in matching_index:
        return matching_index[name]
    low = name.lower()
    if "m:m" in low or "many to many" in low:
        return "M:M"
    if "1:m" in low or "one to many" in low or "receivable" in low or "many" in low:
        return "1:M"
    if "reversal" in low:
        return "REVERSAL"
    if "1:1" in low or "one to one" in low:
        return "1:1"
    return "?"


def _rank(mtype: str) -> int:
    """Precision rank: lower = more precise / should run earlier."""
    return {"1:1": 0, "REVERSAL": 1, "1:M": 2, "M:1": 2, "M:M": 3}.get(mtype, 2)


def build_waterfalls(extracts: dict[str, Extract]):
    """Module 2 data: per-ruleset ordered sequence with precedence violations."""
    recon = extracts.get("recon")
    matching = extracts.get("matching")
    matching_index = {}
    if matching:
        for r in matching.records:
            if r.get("name"):
                matching_index.setdefault(r["name"], r.get("match_type", "?"))

    rulesets: dict[str, list] = {}
    if recon:
        for r in recon.records:
            rs = r.get("ruleset") or "(unnamed)"
            rulesets.setdefault(rs, []).append(r)

    out = []
    for rs, rows in rulesets.items():
        rows = sorted(rows, key=lambda x: _to_int(x.get("sequence"), 9999))
        steps = []
        worst_rank_so_far = -1
        violations = 0
        for x in rows:
            mname = x.get("matching_rule", "")
            mtype = _match_type_of(mname, matching_index)
            rank = _rank(mtype)
            violation = rank < worst_rank_so_far  # a more-precise rule AFTER a broader one
            if violation:
                violations += 1
            worst_rank_so_far = max(worst_rank_so_far, rank)
            steps.append({
                "sequence": x.get("sequence", ""),
                "matching_rule": mname,
                "match_type": mtype,
                "tolerance_rule": x.get("tolerance_rule", ""),
                "precedence_violation": violation,
            })
        out.append({"ruleset": rs, "description": rows[0].get("description", ""),
                    "steps": steps, "violations": violations})
    return out


def gl_audit(extracts: dict[str, Extract]):
    """Module 1 SLA & GL audit: summarize cash vs offset natural accounts and
    flag anomalies (blank GL, cash == offset)."""
    tcr = extracts.get("tcr")
    if not tcr:
        return {"cash_accounts": {}, "offset_accounts": {}, "anomalies": []}

    def natural(gl: str) -> str:
        parts = gl.split("-")
        return parts[1] if len(parts) > 1 else gl

    cash_accts: dict[str, int] = {}
    offset_accts: dict[str, int] = {}
    anomalies = []
    for r in tcr.records:
        cash, off = r.get("cash_gl", ""), r.get("offset_gl", "")
        name = r.get("name", "")
        if cash:
            cash_accts[natural(cash)] = cash_accts.get(natural(cash), 0) + 1
        if off:
            offset_accts[natural(off)] = offset_accts.get(natural(off), 0) + 1
        if r.get("txn_type") in BANK_ORIGINATED_TYPES and not (cash and off):
            anomalies.append({"rule": name, "issue": "missing Cash or Offset GL on a bank-originated TCR"})
        if cash and off and cash == off:
            anomalies.append({"rule": name, "issue": "Cash and Offset GL are identical (no clearing separation)"})
    return {
        "cash_accounts": dict(sorted(cash_accts.items(), key=lambda kv: -kv[1])),
        "offset_accounts": dict(sorted(offset_accts.items(), key=lambda kv: -kv[1])),
        "anomalies": anomalies[:50],
    }


def _tcr_type_breakdown(tcr: Extract):
    counts: dict[str, int] = {}
    for r in tcr.records:
        t = r.get("txn_type") or "(blank)"
        counts[t] = counts.get(t, 0) + 1
    return dict(sorted(counts.items(), key=lambda kv: -kv[1]))


def health_score(extracts: dict[str, Extract], waterfalls, gl):
    """Weighted 0-100 best-practice score with itemized findings."""
    tcr = extracts.get("tcr")
    matching = extracts.get("matching")
    tolerance = extracts.get("tolerance")

    tcr_rows = len(tcr.records) if tcr else 0
    matching_rules = len({r["name"] for r in matching.records if r.get("name")}) if matching else 0
    findings = []
    components = {}

    # --- Component 1: TCR volume discipline (30 pts) --------------------------
    # Full marks when TCR count <= 2x matching-rule count; linear penalty as the
    # ratio climbs, zeroed by a 20x ratio. Rationale: a healthy config leans on
    # matching (mirroring subledgers), not on manufacturing transactions. The
    # 20x ceiling (rather than 10x) leaves a visible improvement gradient so a
    # re-run after consolidating TCRs moves the needle.
    distinct_tcr = len({r.get("name", "") for r in tcr.records if r.get("name")}) if tcr else 0
    deposit_id_keyed = sum(
        1 for r in (tcr.records if tcr else [])
        if "DEPOSIT ID" in (r.get("name", "") + " " + r.get("search_string", "")).upper()
    )
    ratio = (tcr_rows / matching_rules) if matching_rules else float("inf")
    if ratio <= 2:
        c1 = 30.0
    elif ratio >= 20:
        c1 = 0.0
    else:
        c1 = round(30 * (20 - ratio) / 18, 1)
    components["tcr_volume"] = c1
    if c1 < 30:
        detail = (f"{tcr_rows} transaction creation rules against {matching_rules} matching rules "
                  f"(ratio {ratio:.1f}:1)")
        if distinct_tcr:
            detail += f"; {distinct_tcr} are distinct rules — not one template reused, genuine sprawl"
        if deposit_id_keyed:
            detail += (f", including {deposit_id_keyed} keyed to individual deposit IDs "
                       f"(the exact pattern AR Lockbox is built to replace)")
        findings.append({
            "severity": "high" if c1 < 12 else "medium", "principle": "Minimize TCRs",
            "text": detail + ". TCRs should be the exception, not the engine — migrate "
                    "subledger-suspect TCRs into AP AutoMatch and AR Lockbox.",
        })

    # --- Component 2: TCR type discipline (25 pts) ----------------------------
    # Penalize the share of TCRs whose type usually has an upstream subledger
    # source (ACH/CHK/EFT/MSC) rather than being bank-originated (BKF/INT/ZBA).
    suspect = sum(1 for r in tcr.records if r.get("txn_type") in SUBLEDGER_SUSPECT_TYPES) if tcr else 0
    suspect_share = (suspect / tcr_rows) if tcr_rows else 0
    c2 = round(25 * (1 - suspect_share), 1)
    components["tcr_type"] = c2
    if suspect_share > 0.10:
        findings.append({
            "severity": "high" if suspect_share > 0.5 else "medium", "principle": "Subledger supremacy",
            "text": f"{suspect} of {tcr_rows} TCRs ({suspect_share:.0%}) use subledger-suspect types "
                    f"(ACH/CHK/EFT/MSC). These likely patch AP/AR gaps; reserve TCRs for bank-originated "
                    f"items (fees, interest, sweeps).",
        })

    # --- Component 3: rule sequencing (20 pts) --------------------------------
    # Proportional to the share of steps that are precedence inversions (a
    # more-precise 1:1 running after a broader 1:M/M:M). These are review flags,
    # not proven defects — whether a broad rule actually steals a narrow rule's
    # transactions depends on advanced-criteria overlap we can't see without the
    # data — so we scale the penalty rather than zeroing on the first inversion.
    total_inversions = sum(w["violations"] for w in waterfalls)
    total_steps = sum(len(w["steps"]) for w in waterfalls) or 1
    c3 = round(20 * (1 - min(1.0, total_inversions / total_steps)), 1)
    components["sequencing"] = c3
    if total_inversions:
        findings.append({
            "severity": "medium" if total_inversions / total_steps > 0.25 else "low",
            "principle": "Matching hierarchy",
            "text": f"{total_inversions} precedence inversion(s) across {total_steps} sequenced steps: a "
                    f"broader (1:M/M:M) rule runs before a more precise (1:1) rule in the same ruleset. "
                    f"Where their advanced criteria overlap, the broad rule can consume transactions the "
                    f"exact rule should have matched — review these and resequence 1:1 first.",
        })

    # --- Component 4: tolerance discipline (15 pts) ---------------------------
    loose = 0
    if tolerance:
        for r in tolerance.records:
            db, da = _to_int(r.get("days_before"), 0), _to_int(r.get("days_after"), 0)
            if r.get("date_enabled", "").upper() == "Y" and max(db, da) > LOOSE_DAY_TOLERANCE:
                loose += 1
    c4 = 15.0 if loose == 0 else max(0.0, 15 - 5 * loose)
    components["tolerance"] = c4
    if loose:
        findings.append({
            "severity": "low", "principle": "Judicious tolerances",
            "text": f"{loose} day-tolerance rule(s) exceed ±{LOOSE_DAY_TOLERANCE} days. Wide date windows "
                    f"raise the false-positive risk; tighten unless the bank genuinely posts that late.",
        })

    # --- Component 5: GL mapping integrity (10 pts) ---------------------------
    anomalies = len(gl["anomalies"])
    c5 = 10.0 if anomalies == 0 else max(0.0, 10 - min(10, anomalies))
    components["gl_integrity"] = c5
    if anomalies:
        findings.append({
            "severity": "medium", "principle": "Clean SLA / clearing separation",
            "text": f"{anomalies} TCR(s) have GL anomalies (missing Cash/Offset, or Cash == Offset), which "
                    f"breaks the Cash vs Cash-Clearing separation reconciliation accounting relies on.",
        })

    score = round(sum(components.values()), 1)
    grade = ("A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70
             else "D" if score >= 60 else "F")
    return {
        "score": score, "grade": grade, "components": components, "findings": findings,
        "ratio": None if ratio == float("inf") else round(ratio, 1),
    }


def analyze(extracts: dict[str, Extract]) -> dict:
    """Top-level: produce the full analysis payload for the report/app."""
    tcr = extracts.get("tcr")
    matching = extracts.get("matching")
    parse = extracts.get("parse")
    recon = extracts.get("recon")
    tolerance = extracts.get("tolerance")

    waterfalls = build_waterfalls(extracts)
    gl = gl_audit(extracts)
    health = health_score(extracts, waterfalls, gl)

    counts = {
        "tcr_rows": len(tcr.records) if tcr else 0,
        "matching_rows": len(matching.records) if matching else 0,
        "matching_rules": len({r["name"] for r in matching.records if r.get("name")}) if matching else 0,
        "parse_rows": len(parse.records) if parse else 0,
        "recon_rows": len(recon.records) if recon else 0,
        "rulesets": len(waterfalls),
        "tolerance_rules": len(tolerance.records) if tolerance else 0,
        "bank_accounts": len({r["bank_account"] for r in tcr.records if r.get("bank_account")}) if tcr else 0,
    }

    # Bank account -> TCR summary (the extracts don't carry ruleset-to-account
    # assignment; that lives on the bank account setup, so we map what we have).
    ba: dict[str, dict] = {}
    if tcr:
        for r in tcr.records:
            b = r.get("bank_account")
            if not b:
                continue
            d = ba.setdefault(b, {"tcrs": 0, "types": {}})
            d["tcrs"] += 1
            t = r.get("txn_type") or "(blank)"
            d["types"][t] = d["types"].get(t, 0) + 1
    bank_accounts = [{"name": k, **v} for k, v in sorted(ba.items(), key=lambda kv: -kv[1]["tcrs"])]

    # A few real advanced-criteria examples to seed the Module 3 simulator.
    adv_examples = []
    if matching:
        seen = set()
        for r in matching.records:
            ac = (r.get("advanced_criteria") or "").strip()
            if ac and ac not in seen:
                seen.add(ac)
                adv_examples.append({"name": r.get("name", ""), "criteria": ac})
            if len(adv_examples) >= 8:
                break

    # Distinct parse-rule patterns to seed Module 4.
    parse_patterns = sorted({r["parse_rule"] for r in parse.records if r.get("parse_rule")}) if parse else []

    return {
        "counts": counts,
        "health": health,
        "tcr_types": _tcr_type_breakdown(tcr) if tcr else {},
        "bank_accounts": bank_accounts,
        "gl_audit": gl,
        "waterfalls": waterfalls,
        "advanced_criteria_examples": adv_examples,
        "parse_patterns": parse_patterns,
    }

"""Render the analysis into a single self-contained HTML app.

The generated file embeds the computed analysis JSON and the four interactive
modules. It has no external dependencies: it opens in any browser offline and
nothing it contains is transmitted anywhere. Because it embeds the real
configuration, callers should treat the output as private (deliver locally; do
not publish or commit it).
"""
from __future__ import annotations

import json
from pathlib import Path

from .analyze import analyze
from .ingest import Extract
from .simulate import parse_criteria, CriteriaError

_TEMPLATE = Path(__file__).with_name("templates") / "app.html"

# The scale figures printed in the design document, shown on the dashboard as a
# reference line beside the live-computed counts.
BASELINE_PDF = {"tcrs": 1050, "matching": 81, "recon_sequences": 9, "parse": 42}


def _strip_wildcards(s: str) -> str:
    return s.replace("%", "").replace("_", "")


def _derive_sample(node, sample: dict) -> None:
    """Walk a criteria AST and synthesize field values that satisfy the positive
    LIKE / = conditions, so a loaded example evaluates TRUE by default. Best
    effort only — good enough for the common AND-of-LIKE baseline rules."""
    tag = node[0]
    if tag in ("and", "or"):
        _derive_sample(node[1], sample)
        _derive_sample(node[2], sample)
    elif tag == "not":
        return  # don't try to satisfy negations
    elif tag == "like" and not node[3]:
        left, right = node[1], node[2]
        if left[0] == "field":
            sample[left[1]] = _strip_wildcards(_literal_of(right))
    elif tag == "cmp" and node[1] == "=":
        left, right = node[2], node[3]
        if left[0] == "field":
            sample[left[1]] = _literal_of(right)
    elif tag == "in":
        left = node[1]
        if left[0] == "field" and node[2]:
            sample[left[1]] = _literal_of(node[2][0])


def _literal_of(node) -> str:
    if node[0] == "str":
        return node[1]
    if node[0] == "concat":
        return "".join(_literal_of(p) for p in node[1])
    return ""  # a field on the RHS — nothing to synthesize


def _criteria_examples(payload) -> list[dict]:
    out = []
    for ex in payload["advanced_criteria_examples"]:
        item = {"name": ex["name"] or "rule", "criteria": ex["criteria"]}
        try:
            ast = parse_criteria(ex["criteria"])
            sample: dict = {}
            _derive_sample(ast, sample)
            if sample:
                item["sample"] = sample
        except CriteriaError:
            pass
        out.append(item)
    return out


def _parse_examples(payload) -> list[dict]:
    """Curated demonstrations of each parse-mask shape, with representative
    source strings (the extracts carry rules, not sample inputs)."""
    have = set(payload["parse_patterns"])
    examples = [
        ("Capture whole reference — (X~)", "(X~)", "0006789599"),
        ("Company name between delimiters", "SENDING CO NAME: (X~)ENTRY DES",
         "TRN*ACH SENDING CO NAME: ACME UNIVERSITY ENTRY DESCR PAYMENT"),
        ("First 10 characters — (1-10)", "(1-10)", "1234567890TRAILINGTEXT"),
        ("Positions 16-25 after anchor", "SERVICMERCH DEP (16-25)",
         "SERVICMERCH DEP 0000012345 EXTRA"),
        ("Leading-zero strip (9 zeros)", "000000000(NN)", "00000000042"),
    ]
    # Keep only shapes that echo the real data where we can tell; always keep the
    # first two since (X~) and delimiter captures dominate the baseline.
    out = []
    for label, rule, sample in examples:
        out.append({"label": label, "rule": rule, "sample": sample})
    # Surface any other distinct real rule the curated set didn't cover.
    covered = {e["rule"] for e in out}
    for rule in payload["parse_patterns"]:
        if rule not in covered and len(out) < 10:
            out.append({"label": f"Baseline rule — {rule}", "rule": rule, "sample": ""})
            covered.add(rule)
    return out


def build_payload(extracts: dict[str, Extract], generated_note: str = "") -> dict:
    payload = analyze(extracts)
    payload["baseline_pdf"] = BASELINE_PDF
    payload["criteria_examples"] = _criteria_examples(payload)
    payload["parse_examples"] = _parse_examples(payload)
    payload["generated_note"] = generated_note or "generated from uploaded CM configuration extracts"
    # These two are consumed only via the curated example lists above.
    payload.pop("advanced_criteria_examples", None)
    payload.pop("parse_patterns", None)
    return payload


def render_html(extracts: dict[str, Extract], generated_note: str = "") -> str:
    payload = build_payload(extracts, generated_note)
    # Escape '<' so an embedded '</script>' or '<' inside config text can never
    # break out of the data island.
    data_json = json.dumps(payload, ensure_ascii=False).replace("<", "\\u003c")
    template = _TEMPLATE.read_text(encoding="utf-8")
    return template.replace("__DATA_JSON__", data_json)


def write_report(extracts: dict[str, Extract], out_path: str | Path,
                 generated_note: str = "") -> Path:
    out_path = Path(out_path)
    out_path.write_text(render_html(extracts, generated_note), encoding="utf-8")
    return out_path

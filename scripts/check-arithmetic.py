#!/usr/bin/env python3
"""Verify the worked arithmetic in every skill and doc.

Finds chains of the form `expr = expr = result` (or `≈`) where every link is
pure arithmetic — digits, operators, parentheses, %, √, exponents — and reports
any chain whose links disagree. Links containing variables, units, or prose are
skipped, so a chain is checked only when all of it is machine-evaluable.

Percent is genuinely ambiguous in worked text: "6%" can mean 0.06 (a ratio) or
6 (a count of percentage points, as when averaging rates). A bare percent link
therefore carries *both* readings, and a chain is flagged only when no reading
makes it consistent. Being wrong in the accusing direction is what makes a
checker get ignored.

WHAT THIS DOES NOT SEE — read before quoting a clean run as "the arithmetic is
verified". It finds chains that sit after a sentence, colon, dash, or pipe
boundary. Two independent reviewers hit the limit on the same day:

  * A chain embedded mid-prose is skipped entirely. An author planting
    deliberate errors inside prose sentences watched all of them pass, then had
    to reword the lines to sit after a boundary before the gate could see them.
  * A quantitative claim with no equation is invisible by construction. "The
    project can close roughly a third of the gap" was wrong by a factor of
    nearly three — 290 reopens is a third of total reopens but 86% of the gap to
    target — and this script passed the file before and after the fix.

So a clean run means "no chain I could parse disagrees", not "the numbers are
right". The prose still needs a reader.

Exit status is 1 if any chain disagrees. Run from the repo root:

    python3 scripts/check-arithmetic.py
"""
import glob
import math
import re
import sys

SEG = re.compile(r"^[\s\d.,%()×÷*/+^√±−-]+$")
BARE_PCT = re.compile(r"^\s*[-+−]?\d+(?:\.\d+)?\s*%\s*$")
# "150 − 25%" reads two ways: subtract the ratio 0.25, or take 25% *of 150*.
# Financial prose almost always means the second, so both readings are kept.
PCT_OF_BASE = re.compile(r"^\s*([\d,.]+)\s*([-+−])\s*(\d+(?:\.\d+)?)\s*%\s*$")
# Trap tables deliberately show wrong arithmetic. A cell under a "Wrong way"
# column is quoting an error on purpose, so checking it reports the trap as a
# defect — which is how a checker teaches authors to ignore it.
WRONG_COL = re.compile(r"wrong|trap|myth|trip|mistake|don'?t|never|✗|❌", re.I)
OPERATOR = re.compile(r"[-+*/^×÷√−]")
TOL_REL = 0.015          # worked examples round; 1.5% is the house tolerance
TOL_ABS = 1e-4

# A chain ends wherever a new thought can start: sentence end, arrow, pipe,
# colon, semicolon, spaced dash, or a comma followed by prose.
BOUNDARY = re.compile(r"(?:\.\s|\.$|→|\||;|:|\s—\s|\s-\s|,\s)")


def to_python(seg: str) -> str:
    s = seg.replace("×", "*").replace("÷", "/").replace("−", "-")
    s = s.replace(",", "").replace("$", "").strip().rstrip(".")
    s = re.sub(r"√\s*\(([^()]*)\)", r"((\1)**0.5)", s)
    s = re.sub(r"√\s*([\d.]+)", r"((\1)**0.5)", s)
    s = re.sub(r"(\d+(?:\.\d+)?)\s*%", r"(\1/100)", s)
    s = s.replace("^", "**")
    s = re.sub(r"(\d)\s*\(", r"\1*(", s)      # 0.7(0.73)   -> 0.7*(0.73)
    s = re.sub(r"\)\s*\(", r")*(", s)         # (21/30)(22/30)
    return s


def _eval(expr: str):
    try:
        v = eval(expr, {"__builtins__": {}}, {})   # noqa: S307 - arithmetic only, regex-gated
    except Exception:
        return None
    return v if isinstance(v, (int, float)) and math.isfinite(v) else None


def readings(seg: str):
    """Every numeric reading of one link, or None if it is not arithmetic."""
    seg = seg.strip().strip("*_`")
    if not SEG.match(seg) or not re.search(r"\d", seg):
        return None
    if seg.count("(") != seg.count(")"):
        return None
    m = PCT_OF_BASE.match(seg)
    if m:
        base = float(m.group(1).replace(",", ""))
        pct = float(m.group(3)) / 100
        sign = -1 if m.group(2) in "-−" else 1
        return [base + sign * base * pct, base + sign * pct]
    if BARE_PCT.match(seg):
        n = float(seg.strip().rstrip("%").strip().replace("−", "-"))
        return [n / 100, n]                    # ratio, or percentage points
    v = _eval(to_python(seg))
    return None if v is None else [v]


def check_line(line: str, wrong_cols=()):
    """Yield (chain, readings) for every chain no reading can reconcile."""
    if line.lstrip().startswith("|"):
        cells = line.split("|")
        line = " . ".join(c for i, c in enumerate(cells) if i not in wrong_cols)
    for chain in BOUNDARY.split(line):
        parts = re.split(r"\s*(?:=|≈)\s*", chain)
        if len(parts) < 2:
            continue
        cand = [readings(p) for p in parts]
        if any(c is None for c in cand):
            continue
        # At least one link must actually compute something; a chain of bare
        # numbers ("0.25 = 25%") is a restatement, not a calculation.
        if not any(OPERATOR.search(re.sub(r"^\s*[-−]", "", p.strip()))
                   for p in parts):
            continue
        ok = False
        for anchor in cand[0]:
            if all(any(abs(v - anchor) <= max(abs(anchor) * TOL_REL, TOL_ABS)
                       for v in c) for c in cand[1:]):
                ok = True
                break
        if not ok:
            yield chain.strip(), cand


def main() -> int:
    targets = sorted(glob.glob("plugins/**/*.md", recursive=True)
                     + glob.glob("docs/**/*.md", recursive=True))
    bad = []
    for path in targets:
        wrong_cols = ()
        with open(path, encoding="utf-8", errors="replace") as fh:
            for n, line in enumerate(fh, 1):
                line = line.rstrip("\n")
                if line.lstrip().startswith("|"):
                    cells = line.split("|")
                    if any(WRONG_COL.search(c) for c in cells):
                        wrong_cols = tuple(i for i, c in enumerate(cells)
                                           if WRONG_COL.search(c))
                else:
                    wrong_cols = ()
                for chain, cand in check_line(line, wrong_cols):
                    bad.append((path, n, chain, cand))
    for path, n, chain, cand in bad:
        print(f"MISMATCH {path}:{n}\n         {chain}\n         links read as {cand}")
    print(f"== arithmetic: {len(bad)} disagreeing chain(s) across {len(targets)} files ==")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

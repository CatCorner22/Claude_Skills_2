# FusionCash Architect

Turns your five Oracle Fusion Cash Management configuration extracts — Matching
Rules, Recon Rulesets, Transaction Creation Rules (TCRs), Tolerance Rules, and
Parse Rules — into an interactive, self-contained report that helps you *see*
and *fix* the configuration against Oracle best practices.

It is the working tool behind the *FusionCash Architect* product design: a
Configuration Ingestor + Health Score, a Reconciliation Ruleset flow
visualizer, an Advanced Criteria SQL simulator, and a bank-string Parse Rule
sandbox.

## Why it exists

The design premise is that a large Transaction-Creation-Rule footprint is a
deviation from Oracle best practice: TCRs *manufacture* transactions and should
be the exception, with matching mirroring the AP/AR subledgers instead. This
tool makes that (and other best-practice gaps) measurable, and lets you test
Advanced Criteria and Parse Rules **locally** so you stop discovering syntax
errors inside a failed AutoRecon job.

## The four modules

1. **Dashboard & Health Score** — live-computed counts, a weighted 0–100 health
   score with itemized findings, a TCR-type distribution, the SLA/GL audit
   (Cash vs Cash-Clearing natural accounts), and a bank-account data map.
2. **Ruleset Flow Visualizer** — each recon ruleset as a top-to-bottom
   waterfall in execution order, highlighting precedence inversions (a broad
   1:M rule sequenced before a precise 1:1 rule).
3. **Advanced Criteria Simulator** — parse, validate, and evaluate
   `s.FIELD`/`t.FIELD` expressions (`LIKE`, `=`, `IN`, `AND`/`OR`/`NOT`, `||`)
   against sample values; case-sensitive, matching Oracle.
4. **Parse Rule Sandbox** — apply a parse mask (`(X~)`, `(a-b)`, `(N)`/`(A)`/
   `(X)`, leading-zero ladders) to a raw statement string and see exactly what
   lands in `RECON_REFERENCE`.

## Install

```bash
pip install -r requirements.txt   # just openpyxl
```

## Use

Generate the interactive report from your extracts (a directory or explicit
files):

```bash
python -m fusioncash_architect.cli report out.html /path/to/config_folder
python -m fusioncash_architect.cli report out.html Matching.xlsx Recon.xlsx TCR.xlsx Tolerance.xlsx Parse.xlsx
```

Open `out.html` in any browser. It is fully self-contained and offline — no
server, no database, and nothing it contains is transmitted anywhere.

Quick JSON summary (counts + health score) without generating HTML:

```bash
python -m fusioncash_architect.cli summary /path/to/config_folder
```

Try a rule from the command line:

```bash
python -m fusioncash_architect.cli criteria \
  "( s.ADDENDA_TXT LIKE '%'|| 'BANK CARD' ||'%' ) AND ( t.CPARTY_NAME = 'BANK OF AMERICA, N.A.' )" \
  "s.ADDENDA_TXT=DEPOSIT BANK CARD 123" "t.CPARTY_NAME=BANK OF AMERICA, N.A."

python -m fusioncash_architect.cli parse "SENDING CO NAME: (X~)ENTRY DES" \
  "TRN ACH SENDING CO NAME: ACME UNIVERSITY ENTRY DESCR"
```

## Design decisions

- **Every cell is read as a string** via `openpyxl`. GL segment strings and
  BAI2 transaction codes must never be float-coerced (which `pandas` does on
  ingest), so identifier fidelity is preserved. The header row is *located* by
  anchor tokens, not assumed at row 1, and "last updated by" columns are dropped
  on ingest.
- **The health score is transparent.** Every weight and threshold is documented
  in `analyze.py` and every deduction emits a finding tied to the best-practice
  principle it enforces — no opaque constants.
- **The simulators have one source of truth.** `simulate.py` is the reference
  implementation, unit-tested against real baseline rules; the browser mirrors
  the same logic in JavaScript so the sandbox runs with no server.
- **Privacy.** Generated reports embed your real configuration. They are meant
  to stay local — `.gitignore` excludes `*.xlsx` and generated reports so
  production configuration is never committed.

## Layout

```
fusioncash_architect/
  ingest.py            # openpyxl strings-only ingestion of the 5 extracts
  analyze.py           # health score, ruleset waterfalls, SLA/GL audit
  simulate.py          # Advanced Criteria + Parse Rule engines (reference impl)
  report.py            # injects analysis into the HTML template
  cli.py               # command-line entry point
  templates/app.html   # self-contained interactive app (mirrors simulate.py in JS)
tests/                 # pytest suite (uses synthetic data, not real extracts)
```

## Test

```bash
pytest -q
```

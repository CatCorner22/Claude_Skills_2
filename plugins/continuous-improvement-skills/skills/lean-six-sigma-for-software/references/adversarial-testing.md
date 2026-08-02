# Adversarial testing

Ordinary testing proves the software does what you meant on inputs you thought of. Adversarial
testing assumes an intelligent opponent — a hostile user, a chaotic network, a malformed file,
your own future mistakes — and tries to *break* the system before reality does. This is
inspection with teeth, run early enough to be construction.

Contents: §1 The adversarial mindset · §2 Property-based testing · §3 Fuzzing & mutation ·
§4 Fault injection & chaos · §5 Security adversaries · §6 Adversarial UX pass ·
§7 The gauntlet checklist

## §1 The adversarial mindset

- Flip the question from "does it work?" to "**how do I make it fail?**" — then make each
  discovered failure impossible (poka-yoke), not just fixed.
- Budget it: every feature of consequence gets an adversarial pass before release; every
  incident's root cause becomes a permanent adversarial test (regression tests are kaizen).
- Layer it (Swiss cheese): property tests, fuzzers, fault injection, security scans, and human
  red-team review each catch what the others miss. No single layer needs to be perfect; the
  stack does.
- Findings are process data: Pareto them (which class of weakness dominates?) and fix the
  *generator* of the weakness — a recurring injection finding means the team needs a query
  builder, not another ticket.

## §2 Property-based testing (the workhorse)

Instead of asserting `f(2)==4`, assert *properties* that must hold for all inputs, and let the
framework hunt for counterexamples and shrink them to minimal repro:

- Tools: **Hypothesis** (Python), **fast-check** (TypeScript/JS). Mature, standard, cheap to
  adopt.
- Properties that pay rent:
  - **Round-trip**: `parse(render(x)) == x` — serializers, importers, converters.
  - **Invariant**: ledger debits == credits after any operation sequence; balance never NaN.
  - **Oracle**: fast/clever implementation agrees with slow/obvious one.
  - **Idempotence**: applying twice == applying once (critical for payment posting, sync).
  - **Metamorphic**: adding a line item never decreases the total.
- Point it at the algorithmic core first: money math, date/period logic, matching/recon rules,
  parsers, state machines — anywhere the input space is too big to enumerate by hand.
- Keep the failure corpus: every counterexample found becomes a pinned regression case.

## §3 Fuzzing & mutation testing

- **Fuzzing** feeds massive volumes of random/mutated input to anything that parses external
  data (file importers, API payload handlers, string parsers): coverage-guided fuzzers
  (AFL++ actively developed; libFuzzer works but is maintenance-only; Atheris for Python;
  Jazzer for JVM; OSS-Fuzz as the hosted pattern), or pragmatic in-process fuzzing with
  Hypothesis strategies over bytes. For HTTP APIs, **schemathesis** fuzzes directly from your
  OpenAPI contract — cheap and vicious.
  Any crash, hang, or memory spike on malformed input is a finding.
- **Mutation testing** tests your *tests*: it seeds small code mutations (`>` → `>=`, dropped
  branch) and checks your suite kills them (mutmut/cosmic-ray for Python, Stryker for JS/TS).
  Surviving mutants = coverage theater. Run it on the critical core periodically, not the whole
  repo nightly — it's expensive and its value concentrates where correctness matters most.

## §4 Fault injection & chaos engineering (adversarial operations)

Test the system's *stability claims* the way an outage would:

- Inject at the seams: kill the DB connection mid-transaction; add 3 s latency to the payments
  API; return 500s/429s from a dependency; fill the disk; skew the clock; deliver the webhook
  twice, out of order, then not at all.
- Verify the promises in `stability-and-redundancy.md`: retries actually retry (with backoff +
  jitter, without duplicating side effects), circuit breakers open, timeouts fire, degraded
  mode engages, the queue drains after recovery.
- Practice: start in staging with a hypothesis ("if the cache dies, p95 stays < 800 ms"),
  gameday it with the team, graduate to controlled production experiments only with blast-radius
  limits and an abort switch (LitmusChaos or Chaos Mesh for OSS; AWS Fault Injection Service or
  Gremlin managed — tooling matters less than the discipline of hypothesis → inject → observe
  → fix).
- Restore drills are chaos tests too: an untested backup is a rumor, not redundancy.

## §5 Security adversaries

The literal adversary. Minimum bar for anything networked:

- **Threat model first** (STRIDE per component/data flow: spoofing, tampering, repudiation,
  information disclosure, DoS, elevation). One hour of whiteboard threat modeling redirects
  more risk than a week of late scanning.
- **Abuse cases** alongside use cases: "as a hostile user I fetch other tenants' records by
  iterating IDs" (IDOR), "I replay the payment webhook", "I upload a 2 GB 'CSV'", "I inject
  `'; DROP` into the search box", "I brute-force the login".
- Automated layers in CI: SAST (Semgrep/CodeQL-class), dependency + container audit
  (pip-audit/npm audit/Trivy-class — and pin CI actions by digest; the 2026 trivy-action
  compromise is the cautionary tale), secret scanning (gitleaks-class), DAST (ZAP — formerly
  OWASP ZAP, now ZAP by Checkmarx) against staging.
- Map to **OWASP** (Top 10 — the 2025 edition adds Software Supply Chain Failures; API Top 10;
  LLM Top 10 if the product embeds a model; ASVS 5.0 for depth) — and test authorization *per
  resource*, the perennial number-one real-world hole.
- Human red-team review for high-stakes flows (money movement, auth, PHI/PII): one session,
  attacker hat, no politeness.

## §6 The adversarial UX pass

Hostile-input thinking applied to the interface — run it on every form and import:

- Names: `O'Brien`, `José`, `æ`, two-character names, 70-character names, emoji, RTL text.
- Numbers/money: `0`, negatives, `1e9`, `0.001`, thousands separators, currency symbols pasted
  in, leading zeros that must survive (account numbers are text!).
- Dates: Feb 29, DST transitions, timezone boundaries, `12/01` ambiguity, year 1900/2100.
- Files: empty, huge, wrong-extension, correct-extension-wrong-content, zip bombs, CSV with
  formulas (`=cmd|...` — CSV injection), BOMs, mixed encodings.
- Behavior: double-click submit, back button mid-flow, two tabs, session expiry mid-form,
  offline mid-save, paste-everything users, screen-reader + keyboard-only runs (accessibility
  failures are adversarial-UX failures — see `accessible-ui-design-system.md`).
- The system should refuse gracefully, preserve the user's work, and explain the fix — never
  corrupt, never silently truncate, never lose a half-filled form.

## §7 The gauntlet checklist (pre-release)

- [ ] Properties written for the algorithmic core; counterexample corpus pinned
- [ ] Parser/import surfaces fuzzed (schemathesis for APIs; bytes-level for files)
- [ ] Mutation run on the critical module — surviving mutants triaged
- [ ] Fault-injection hypotheses tested at each external seam; degraded modes verified
- [ ] STRIDE pass done; abuse cases written and automated where possible
- [ ] SAST/deps/secrets/DAST gates green; authz tested per resource
- [ ] Adversarial UX sweep on every new form/import (the §6 list)
- [ ] Every finding either poka-yoked or pinned as a regression test with an owner

# Oracle Cash Management vocabulary

Read at stage 2, UT work only. **Read this as orientation, never as evidence.** It supplies the
vocabulary, the processing chain, and a map of where live figures live — and no figures itself, on
purpose. Any number that reaches a slide must come from an artifact you opened this session and
recorded in the source ledger (see `evidence-discipline.md`).

## Contents
- [Why this file holds no numbers](#why-this-file-holds-no-numbers)
- [The processing chain](#the-processing-chain)
- [Defined terms](#defined-terms)
- [Defect patterns worth a slide](#defect-patterns-worth-a-slide)
- [Where the live figures live](#where-the-live-figures-live)
- [Explaining this to a Controller](#explaining-this-to-a-controller)
- [Institutional context](#institutional-context)

## Why this file holds no numbers

Configuration changes. Rule counts change when a change request lands. Match rates change with every
run. A reference file that hard-codes those figures turns stale silently, and a stale figure in a
leadership deck is exactly the failure this skill exists to prevent. So this file carries only what
stays true: how the pipeline is shaped, what the parts are called, and which artifact answers which
question.

## The processing chain

Slides about this ecosystem almost always need one diagram of the whole chain, shown early, so later
slides can point at a stage. Build it left to right:

```
Bank                Oracle Cash Management                    Outcome
────────────────    ──────────────────────────────────────    ─────────────
Bank file      →    Parse Rules                          →    Reconciled
(BAI2, CAMT.053,    Transaction Creation Rules (TCR)           (REC)
 MT940)             External Cash Transactions (ECT)
                    Matching Rules + Tolerance Rules      →    Unreconciled
                    Reconciliation Rule Sets                   (UNR)
                                ↑
                    System Transactions (ST) from
                    Receivables, Payables, and
                    other subledgers
```

Two lanes converge at matching. The bank lane produces Bank Statement Lines. The internal lane
produces System Transactions from the subledgers. Matching pairs them. Whatever fails to pair stays
unreconciled. Draw the diagram with seven or fewer boxes. Number the stages so a later headline can
say "stage 3" without re-explaining the chain.

## Defined terms

Use these terms consistently across a deck. Switching between a term and a synonym forces the
audience to re-derive that they mean the same thing — exactly the cognitive load the method removes.
Define an abbreviation once, on first use, then use the abbreviation alone.

| Term | Use it to mean |
|---|---|
| Bank Statement Line (BSL) | One transaction row delivered by the bank |
| System Transaction (ST) | One transaction recorded in a subledger, available to match |
| External Cash Transaction (ECT) | A transaction Oracle creates from a bank line when no subledger transaction exists to match |
| Parse Rule | Configuration that extracts a field from bank-file text into a usable column |
| Transaction Creation Rule (TCR) | Configuration that decides when a bank line becomes an ECT |
| Matching Rule | Configuration defining what makes a bank line and a system transaction a pair |
| Tolerance Rule | Configuration setting the permitted date and amount variance for a match |
| Reconciliation Rule Set | The ordered bundle of matching and tolerance rules applied to an account |
| Reconciled (REC) | A bank line paired to a system transaction and closed |
| Unreconciled (UNR) | A bank line with no accepted pairing |
| Auto-reconciliation | Matching performed by the system without human review |
| Review | The queue of items a person must resolve |
| DASH | The University of Tennessee's name for its Oracle Fusion Cloud environment |

**A caution about ECT.** Oracle intends external cash transactions for items that genuinely
originate at the bank — fees, interest, and similar charges with no subledger counterpart. When
transaction creation rules fire too broadly, real subledger activity gets converted into external
cash transactions and is stranded outside the normal matching path. Explaining that consequence in
one sentence is usually worth a whole slide, because it converts a configuration detail into a
control problem a Controller recognizes immediately.

## Defect patterns worth a slide

These are shapes to look for, not findings to assert. Each becomes a slide only after the underlying
artifact confirms it in the current configuration.

- **Rule concentration.** A large share of transaction creation rules pointing at a small number of
  codes. The slide claim is about the consequence — stranded activity — not the rule count.
- **Tolerance mismatch.** A date window far wider than actual settlement lag, combined with a
  disabled or absent amount tolerance. The consequence: matches that pass on amount and fail on
  date, corrupting the date-integrity signal even on rows the system considers reconciled.
- **Fragile string comparison.** Matching rules that compare counterparty names by exact equality,
  so case or whitespace differences break an otherwise-correct pair.
- **Inert parse anchors.** A parse rule anchored on a literal string the bank does not actually
  emit, so the rule silently extracts nothing. Invisible in the configuration; only shows in output.
- **Operator or co-occurrence errors.** A rule whose logic inverts a comparison or requires two
  conditions that cannot both hold.
- **Migration residue.** Duplicate or superseded rule sets left active after a configuration
  migration, so which rule set governs an account becomes ambiguous.
- **Upstream process backlog.** Review volume driven by receipts banked but never entered in the
  system. This one matters most for a leadership deck, because no amount of engine tuning fixes it —
  the fix is a process change and a service-level commitment, which only leadership can authorize.
  When the evidence supports this claim, it usually deserves its own slide and its own ask.

## Where the live figures live

Match the question to the artifact. Open the artifact; do not rely on a summary of it.

| Question | Look in |
|---|---|
| How many accounts, and at which banks? | Bank account configuration export |
| How many rules of each type, and what do they target? | Configuration forensics export for parse, transaction creation, matching, and tolerance rules |
| Which rule set governs which account? | Rule-set-to-account assignment export |
| What are the current match, candidate, and review counts? | The most recent engine run output, with its run date |
| Which lines failed and why? | Unreconciled-line report with rule attribution |
| What did the auditors find? | The audit report itself, cited by report number and fiscal year |
| What has the team committed to, and by when? | The corrective action plan or open-items list |
| What changed recently? | The active change request and its waves |

When an artifact does not exist, that absence is itself a finding worth a line on the gap slide —
name the export, name what it would answer, name who can produce it.

## Explaining this to a Controller

Leadership decides about exposure, cost, and time. Translate each technical claim into one of those
before it becomes a headline.

| Technical claim | Leadership translation |
|---|---|
| Rules generate external cash transactions too broadly | Real activity bypasses the normal match path, so the reconciliation is incomplete |
| The tolerance window is too wide | Items marked reconciled may not be reconciled on date, weakening the control |
| A parse rule anchors on the wrong string | A field the matching depends on is empty, so those lines can never auto-match |
| Review volume is high | Staff time is consumed by items that a process change upstream would eliminate |
| One person holds the knowledge | The remediation stops if that person leaves; documentation and code reduce that risk |

Keep the technical term in the headline and add the consequence. Removing the term entirely leaves
leadership unable to ask their systems team about it; using it without the consequence leaves them
unable to act.

## Institutional context

Structural facts, stable enough to state, and each verifiable at its source:
- The Tennessee Comptroller of the Treasury, Division of State Audit, conducts financial and
  compliance audits of the University of Tennessee and publishes the resulting reports.
- That office also uses a Limited Official Use designation for material excluded from a public
  report, which is why an audit response can require parallel public and confidential versions.
- The State of Tennessee Single Audit covers the state as a whole, including university funds, under
  the federal Uniform Guidance.
- The University of Tennessee System publishes its financial reports and audit reports through the
  Office of the Treasurer.

**Specific report numbers, finding text, dollar amounts, and deadlines must come from the report
itself**, cited by report number and fiscal year. Never state an audit figure from memory or from a
summary; open the report, quote the figure, and record it in the source ledger with the report's
date.

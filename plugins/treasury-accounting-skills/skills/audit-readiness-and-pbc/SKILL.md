---
name: audit-readiness-and-pbc
description: >-
  Gets finance and treasury through an external audit efficiently — running the PBC
  (prepared-by-client) list as a managed project, producing workpapers and reconciliations that
  stand alone, preparing for the cash/debt/investment areas auditors always hit (confirmations,
  cutoff, coverage of controls), handling walkthroughs and sample requests, and responding to
  findings without thrash. Use when an audit or interim fieldwork is coming, a PBC list just
  arrived, an auditor asks for support or a walkthrough, or a finding needs a response.
  Triggers: audit, PBC list, prepared by client, auditor request, bank confirmation,
  walkthrough, audit evidence, workpaper, audit finding, management letter, interim fieldwork,
  audit readiness, support for the auditors.
---

# Audit readiness and PBC management

## When to use
- An external audit (year-end, interim, or a lender/parent audit) is approaching, or the PBC
  list has landed and needs organizing.
- Preparing the areas auditors focus on in treasury/accounting: cash and bank confirmations,
  debt and covenants, investments, reconciliations, cutoff, and journal-entry testing.
- Responding to auditor questions, walkthrough requests, or findings.
- Not for: designing the controls being audited → see
  `cash-management-skills:cash-management-controls`. For SOX-style control *testing* method →
  that's the auditor's craft; this skill is the client side.

## Do it
1. **Run the PBC list as a project, not an inbox.** On receipt: load every item into one
   tracker (item, audit area, owner, due date, status, delivery link), challenge items that
   don't apply or duplicate prior-year, and agree the delivery mechanism (portal, not email
   attachments). One coordinator owns the tracker and all auditor communication routing —
   scattered side-channels are how items get answered twice, differently.
   `references/pbc-and-evidence.md` has the tracker format and a treasury/accounting PBC
   starter list.
2. **Make every workpaper stand alone.** The standard: an auditor who knows accounting but not
   your company can follow it without asking. Each schedule shows: what it is and the period,
   source of every number (system + report + date pulled), tie-out to the trial balance,
   preparer/reviewer and dates, and explanation of judgments. A reconciliation that "ties in
   my head" generates three follow-up requests; the standalone version generates none.
3. **Pre-audit the perennial areas before the auditors do.** Walk the known focus list:
   - **Cash:** every bank account reconciled through year end (stale items dispositioned);
     the complete bank account list matches what confirmations will reveal — auditors confirm
     *with the banks*, so an account you forgot looks like concealment.
   - **Debt:** facility schedules tie to statements and to
     `treasury-accounting-skills:debt-facilities-and-covenants` covenant workpapers;
     compliance certificates on file; accrued interest recomputes cleanly.
   - **Investments:** holdings from custody data, policy compliance runs on file
     (`treasury-accounting-skills:investment-policy-compliance`), valuations supportable.
   - **Cutoff and accruals:** the search-for-unrecorded-liabilities work is already done —
     hand them your own cutoff testing (`treasury-accounting-skills:accruals-and-prepaids`).
   - **Intercompany:** the matrix reconciles, eliminations netted
     (`treasury-accounting-skills:intercompany-accounting`).
   - **Estimates:** every material estimate (reserves, accrual bases) has its rationale
     written down *from when it was made*.
4. **Prepare people for walkthroughs.** Auditors will ask a process owner to narrate a
   transaction end-to-end (a payment, a journal, a hedge). Brief owners: describe what
   *actually happens* (not the policy's aspiration), name the systems and the control points,
   and say "I'd need to check" rather than guessing. A walkthrough that contradicts the
   documented process is a finding factory.
5. **Serve samples fast and exactly.** Sample requests (25 payments, 40 journals) are
   turnaround-time battles: deliver precisely the items requested, complete (approval evidence
   included — the approval is usually the point), in one organized package. Partial or
   trickled delivery multiplies follow-ups and burns fieldwork days.
6. **Manage the finding conversation.** For each proposed finding: verify the facts first
   (auditors misread systems too — correct factual errors with evidence, politely), assess
   severity honestly, and for real issues respond with a concrete remediation owner and date
   rather than defensiveness. Findings you self-identified and disclosed land softer than
   findings they caught — which is the deep argument for step 3.
7. **Close the loop for next year.** Archive the final PBC package as delivered, note which
   items caused pain, and fold fixes into the close process — audit readiness is a byproduct
   of a clean close (`accounting-skills:month-end-close`,
   `oracle-fusion-finance-skills:fusion-period-close`), not a fourth-quarter project.

## Why / learn
An audit is an evidence game with asymmetric information: the auditor must build support for an
opinion from the outside, and everything that frustrates people about audits — confirmations
sent to your banks instead of asking you, samples with approval evidence, walkthroughs that
ignore the policy binder — is the auditor rationally preferring evidence that *doesn't depend
on your say-so*. Once you see that, the client-side strategy writes itself: minimize the
distance between your records and independently verifiable reality. Standalone workpapers work
because they let the auditor consume your support without interviewing you (every interview is
billable hours and a chance for inconsistency); pre-auditing the perennial areas works because
self-identified issues cost a remediation plan while auditor-identified issues cost a finding,
extended testing, and credibility; fast exact sample service works because auditor time is the
scarcest resource in fieldwork and delays get repaid in skepticism. The PBC tracker, finally,
is just project management applied to a process with a hundred small deliverables and a hard
deadline — the audit doesn't fail on the hard accounting question, it fails on item 73 nobody
owned.

## Common mistakes
- PBC items scattered across emails and owners → one tracker, one coordinator, portal delivery.
- Workpapers that need the preparer alive and present → standalone standard: source, tie-out, judgment notes.
- Forgetting a bank account the confirmation reveals → maintain the complete account inventory; confirmations are independent.
- Walkthrough owners narrating the policy instead of the practice → brief them; the gap is the finding.
- Trickling samples or omitting approval evidence → the approval *is* the test; deliver complete, once.
- Arguing findings from defensiveness instead of facts → correct factual errors with evidence; own real issues with a dated plan.
- Writing estimate rationale when the auditor asks → rationale documented at decision time, not reverse-engineered.
- Treating readiness as a Q4 sprint → it's the exhaust of a clean monthly close; fix the close, inherit the audit.

## Tailor to your environment
Keep your audit profile in `references/your-environment.md` (auditor correspondence and real
findings in `your-environment.private.md`, git-ignored): audit firm and timeline, portal used,
the coordinator, your standing PBC list mapped to owners, perennial pain points, and open
remediation items. **Never commit real findings, confirmations, or auditor correspondence.**

## References
- references/pbc-and-evidence.md — PBC tracker format, treasury/accounting PBC starter list, workpaper standard, walkthrough briefing
- references/your-environment.md — your auditors, timeline, owners, pain points (fill in)

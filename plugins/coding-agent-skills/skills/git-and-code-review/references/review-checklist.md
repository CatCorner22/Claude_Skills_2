# Code review method: order, checklists, evidence, feedback, worked example

Review in priority order: correctness first, readability second, style last. A wrong answer
that is beautifully formatted is still wrong; a nit is the cheapest thing to fix.

## Contents
- Why the fixed order
- Correctness (blocking)
- Readability and design
- Tests and verification
- Style and consistency
- Size and pacing — the evidence
- The feedback grammar
- Severity labels
- Worked example: reviewing a small diff
- Reviewing as the author (making your PR reviewable)
- Special cases

## Why the fixed order
Attention spent early is not available late. If a reviewer opens a diff and starts with
naming and formatting, the style pass consumes the fresh attention that correctness needed —
and correctness defects are the ones that cost real money, data, or trust after merge.
Running the same order every time also makes reviews predictable for authors: they learn
that a blocking comment means "wrong result possible," not "not how I'd write it."

## Correctness (blocking)
- Does it actually do what the PR says it does? Re-read the description, then the diff.
- Edge cases: empty input, nulls/NaN, zero, negatives, duplicates, very large inputs,
  timezones, encodings.
- Error handling: are failures caught specifically and reported, not silently swallowed?
- Off-by-one, boundary conditions, inverted conditionals, integer vs float division.
- Does it change a shared behavior or data contract others depend on? Any
  migration/back-compat concern?
- Concurrency and ordering: can two runs interleave? Is anything read-modify-write?
- Security/data: no secrets committed, no injection via unescaped input, least-privilege
  access, no sensitive data in logs.
- If review confirms a real bug: the fix is step one, not the whole job — contact-trace the
  pattern's other copies with `coding-agent-skills:defect-epidemiology` before closing.

## Readability and design
- Could the next person understand this without asking the author?
- Names say what things are; functions do one thing; nesting is shallow.
- No copy-paste duplication that should be a shared helper; no dead code.
- Comments explain *why*, not *what the code already says*.
- Is the mechanism proportionate to the job? Correct-but-overbuilt is a real finding — raise
  it as a question, and review the code against
  `full-stack-dev-skills:lean-code-principles`; if the *whole solution*, not the code, is
  what's overbuilt, run the Pencil Pass in `coding-agent-skills:soviet-space-graphite`.

## Tests and verification
- Is there a test that would fail without this change and passes with it?
- Are the important edge cases covered, not just the happy path?
- Did the author state how they verified it (numbers, screenshots, commands)?
- For a bug fix: does the test encode the bug, so it can never silently return?

## Style and consistency (lowest priority — automate it)
- Formatting/lint should be enforced by a tool, not by a human reviewer. If a formatter
  exists, don't spend review comments on whitespace.
- Consistency with the surrounding code's conventions beats abstract preference.

## Size and pacing — the evidence
The SmartBear study of Cisco Systems' peer-review data (2,500 reviews covering 3.2M lines
of code, roughly 50 developers) is the most-cited empirical anchor for review economics.
Its findings, verified via search snippets and marked accordingly:
- Reviewers should take on **no more than about 200–400 changed lines at a time**; the
  ability to find defects diminishes beyond ~400 LOC [snippet-only].
- Defect density drops significantly at inspection rates **faster than ~500 LOC per
  hour** [snippet-only].
- SmartBear pairs those two findings into a target: a 200–400 LOC review taking
  **60–90 minutes** *should yield* **70–90% defect discovery** [snippet-only].

Practical consequences:
- A large feature ships as a stack of small PRs, each independently reviewable, rather
  than one unreviewable diff.
- "Approved" on a 2,000-line PR reviewed in ten minutes is a signature, not a review —
  treat it as unreviewed risk, not cleared risk.
- Purely mechanical bulk changes (a rename, a formatter run) are the exception: verify the
  mechanism (the script/command used), spot-check, and keep them in their own commit so
  the human-authored diff stays small.

## The feedback grammar
Every substantive comment carries three parts: **the line, the concern, the fix.**
- Point at the line (or range) — never "somewhere in here."
- State the concern as an observable consequence: what goes wrong, for whom, when.
- Suggest a fix or a direction — even a question ("dedup on `txn_id` first?") counts.

"This sums before dedup, so duplicate fee rows double-count month-end totals — dedup on
`txn_id` before the groupby?" beats "this looks wrong."

Tone rules that keep the review a collaboration:
- Critique the code, not the person: "this loop re-reads the file each pass" — never "you
  always do this."
- Ask where you might be missing context; the author knows things the diff doesn't show.
- Praise specifically: name the behavior that's good and why it works, with the same
  precision as criticism.
- If a drafted comment reads as a verdict on the author, rewrite it with
  `collaboration-skills:feedback-that-lands` before posting.

## Severity labels
Label every comment so the author can triage:
- **blocking:** — wrong result, data loss, security, broken contract. Must change before merge.
- **should:** — real improvement, author's call whether now or follow-up; say which you'd accept.
- **nit:** — style/preference; never blocks, batch-fixable, ideally automated away.
- **question:** — genuine uncertainty; the answer may dissolve the comment.
- **praise:** — worth labeling too; it calibrates future work.

Approve when the change is correct and clear, not when it is perfect. Perfection blocks
shipping; leave polish as named follow-ups.

## Worked example: reviewing a small diff
The change (any role's automation script — a report generator, an intake filter, a data
clean-up; the method is identical):

```diff
 def monthly_totals(rows):
-    total = sum(r["amount"] for r in rows)
-    return {"month_total": total}
+    total = 0
+    for r in rows:
+        total += float(r["amount"])
+    return {"month_total": round(total, 2)}
```

PR description: "Fix month-end totals being wrong when the export contains duplicates."

A correct review, in order:

1. **Correctness first — and the diff fails it.** The description says duplicates were the
   bug, but nothing here deduplicates; the rewrite only changes summing mechanics.
   > blocking: The PR says duplicates caused the wrong totals, but this diff never dedups —
   > rows with the same `txn_id` still double-count. Dedup before summing
   > (e.g. `{r["txn_id"]: r for r in rows}.values()`), and add a test with a duplicated row
   > that fails on the old code?
2. **Correctness, second finding.** `float(...)` on money introduces representation error;
   `round(total, 2)` hides it.
   > blocking: `float` on currency accumulates representation error and the `round` masks
   > it. Use `Decimal(r["amount"])` (or integer cents) so totals tie out exactly.
3. **Readability.** The loop is fine, but the original comprehension was clearer once the
   real fix exists.
   > nit: once dedup is in, the original `sum(...)` comprehension over deduped rows reads
   > cleaner than the manual loop.
4. **Verification.**
   > question: how was this verified? A before/after total on the month that surfaced the
   > bug in the PR description would make this easy to approve.
5. **Praise where earned.**
   > praise: returning a dict keeps the interface stable for the report layer — good call
   > not to change the shape while fixing the value.

Outcome: the author adds dedup + a failing-then-passing test, switches to `Decimal`, keeps
the comprehension, posts the before/after totals. Second pass: correctness clean, tests
encode the bug, approve — and because review confirmed a real defect pattern
(sum-before-dedup), the reviewer asks whether other reports share the pattern before the
ticket closes (that hunt is `coding-agent-skills:defect-epidemiology`).

## Reviewing as the author (making your PR reviewable)
- Self-review the diff in the PR view before requesting review — you will catch the
  leftover debug line and the accidental file.
- Write the description as: what changed / why / how verified. State the risk you're most
  unsure about; that's where you want the reviewer's attention.
- Keep mechanical changes (renames, formatting) in separate commits — or separate PRs — so
  the reviewable core stays small.
- Answer every comment: fix it, or say why not. Silence reads as "missed it."
- A claim that a phase is "done" is not reviewable in a diff; completion claims get
  verified by inspection (`coding-agent-skills:the-foreman`), not by approving the last PR.

## Special cases
- **Generated or vendored code:** review the generator/config and the decision to vendor,
  not the output line-by-line; pin versions and checksums.
- **Config and data changes:** the diff looks trivial and the blast radius isn't — review
  against the consumer of the config, and ask what happens on the first bad value.
- **Long-standing code being deleted:** absence of callers in the repo is not absence of
  users. Prefer a reversible disable-and-wait (a scream test) over immediate deletion;
  the whole-site version of that discipline is `coding-agent-skills:software-archaeology`.
- **Emergency fixes:** review still happens — after merge if it must, on the calendar, with
  the same checklist; "reviewed later" only works when later is scheduled.

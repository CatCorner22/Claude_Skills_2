# Code review checklist and how to give feedback

Review in priority order: correctness first, readability second, style last. A wrong answer that is
beautifully formatted is still wrong; a nit is the cheapest thing to fix.

## Contents
- Correctness
- Readability and design
- Tests and verification
- Style and consistency
- How to write the feedback

## Correctness (blocking)
- Does it actually do what the PR says it does?
- Edge cases: empty input, nulls/NaN, zero, negatives, duplicates, very large inputs, timezones.
- Error handling: are failures caught specifically and reported, not silently swallowed?
- Off-by-one, boundary conditions, and inverted conditionals.
- Does it change a shared behavior or data contract others depend on? Any migration/back-compat concern?
- Security/data: no secrets committed, no injection via unescaped input, least-privilege access.

## Readability and design
- Could the next person understand this without asking the author?
- Names say what things are; functions do one thing; nesting is shallow.
- No copy-paste duplication that should be a shared helper; no dead code.
- Comments explain *why*, not *what the code already says*.

## Tests and verification
- Is there a test that would fail without this change and passes with it?
- Are the important edge cases covered, not just the happy path?
- Did the author state how they verified it (numbers, screenshots, commands)?

## Style and consistency (lowest priority — automate it)
- Formatting/lint should be enforced by a tool, not by a human reviewer. If a formatter exists, don't
  spend review comments on whitespace.
- Consistency with the surrounding code's conventions.

## How to write the feedback
- **Point at the line, state the concern, suggest a fix.** "This sums before dedup, so duplicate fees
  double-count — dedup on `txn_id` first?" beats "this looks wrong."
- **Label severity.** Mark blocking issues vs. nice-to-haves vs. optional nits (e.g. prefix `nit:`).
- **Be kind and specific.** Critique the code, not the person; ask questions where you might be missing
  context. Praise a genuinely good solution — it calibrates future reviews.
- **Approve when it's correct and clear, not when it's perfect.** Perfection blocks shipping; leave the
  small polish as follow-ups.

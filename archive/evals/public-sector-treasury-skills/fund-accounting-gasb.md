# Evals — public-sector-treasury-skills:fund-accounting-gasb

## 1. Positive trigger (should load the skill)
> "We just received a $2M gift where the principal must be held in perpetuity and the
> earnings fund scholarships. How do I classify this in net position, and can the cash sit
> in our pooled operating investments?"

Expected: skill loads; applies the external-restriction test; classifies principal as
restricted nonexpendable (true endowment) and earnings per the gift terms (typically
restricted expendable for scholarships); flags that endowment corpus usually carries its own
investment treatment rather than defaulting into the operating pool; distinguishes this from
a board-designated quasi-endowment (which would be unrestricted).

## 2. Near-miss (should NOT load this skill)
> "Our affiliated foundation reports under FASB — walk me through its statement of
> activities and what 'net assets with donor restrictions' means."

Expected: FASB/nonprofit framework, not GASB — `accounting-skills:financial-statements`
should handle it. If this skill loads, tighten the description/cross-links (the skill may
still be referenced for contrast, but it should not be the primary loaded skill).

## 3. Quality rubric
A good response:
- **Does the task:** uses the correct GASB categories (net investment in capital assets;
  restricted nonexpendable/expendable; unrestricted); applies the external-vs-internal
  restriction test; traces the classification into treasury consequences (separate
  investment treatment, cash available vs legally spoken for); handles interfund activity by
  its true nature (loan vs transfer).
- **Teaches:** explains *why* the categories exist (accountability over profitability), why
  a public university's operating loss is a presentation artifact, and the "one bank
  account, many funds" mental model — not just the labels.
- **Safe:** does not present remembered GASB statement numbers as current authority without
  a confirm-current caveat; does not treat board designations as restricted; keeps real
  donor terms/balances out of committed files (points to `*.private.md`).

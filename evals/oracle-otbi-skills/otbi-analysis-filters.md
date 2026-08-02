# Evals — oracle-otbi-skills:otbi-analysis-filters

## 1. Positive trigger (should load the skill)
> "In my OTBI report I want an As-of Date and Bank Account prompt that drive the whole dashboard,
> plus an aging bucket column (0-30, 31-60, 61-90, 90+). How do I set that up?"

Expected: skill loads; sets the filters to "is prompted"; builds a dashboard prompt for As-of Date
and Bank Account; writes a CASE column formula for the aging buckets ordered low-to-high; tests the
prompt binding.

## 2. Near-miss (should NOT load this skill)
> "Which subject area has opening and closing bank balances by account and date?"

Expected: this is a subject-area choice — `oracle-otbi-skills:otbi-subject-area-selection` (Bank
Statement Balances Real Time). If this filters skill loads instead, tighten the description /
cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** uses "is prompted" filters, builds the right prompt type (a dashboard prompt for
  a shared As-of Date / Bank Account), and writes a non-overlapping CASE aging formula.
- **Teaches:** distinguishes filter (which rows) vs. prompt (supplies a value) vs. formula (how a
  column is computed), and why buckets belong in a formula, not a filter.
- **Safe:** orders CASE branches so rows fall into exactly one bucket; doesn't hard-code values that
  should be prompts.

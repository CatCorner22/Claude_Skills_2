# Evals — full-stack-dev-skills:lean-code-principles

## 1. Positive trigger (should load the skill)
> "Review this module — it's 800 lines with an interface, a factory, and a config object,
> and I have a feeling it could be a tenth of the size. Simplify it."

Expected: skill loads; applies the resolution order (stdlib/framework first); flags
single-implementation abstractions for inlining, unused config options, and dead code;
proposes the boring concrete version; measures the result in net lines and owned concepts,
not characters.

## 2. Near-miss (should NOT load this skill)
> "Walk me through running our PR review process — branch, diff, comments, approvals."

Expected: review *process* — `coding-agent-skills:git-and-code-review`. If this skill
loads, tighten the code-simplicity framing.

## 3. Quality rubric
A good response:
- **Does the task:** concrete deletions/inlinings with before/after, framework-native
  replacements named, net-lines accounting shown.
- **Teaches:** code as liability with maintenance coupons, the YAGNI asymmetry, wrong
  abstraction vs duplication economics, and why lean ≠ code golf.
- **Decides, doesn't hedge:** names which of the four gates each abstraction passes or
  fails (shared axis of change / name-and-docstring / signature projection / read-through)
  rather than saying "it depends"; where history is available, actually checks whether the
  duplicates were ever edited in the same commit.
- **Safe:** preserves behavior, keeps clarity over character-count cleverness, and doesn't
  delete the audit-trail/validation code that regulated domains actually require.
- **Doesn't under-engineer:** applies the "is the later fix a code change, or a data repair
  / disclosure / incident?" test before deleting anything, and leaves a "not touched, and
  why" note for the code it deliberately left duplicated or defensive.

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
- **Safe:** preserves behavior, keeps clarity over character-count cleverness, and doesn't
  delete the audit-trail/validation code that regulated domains actually require.

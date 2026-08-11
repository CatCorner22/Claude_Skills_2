# Evals — cash-management-skills:liquidity-management

## 1. Positive trigger (should load the skill)
> "We've got cash scattered across eight operating accounts and we keep a big buffer in each one. I
> want to set proper target balances, sweep everything into a concentration account, and figure out
> how much of the pile we can safely invest versus keep as a liquidity buffer."

Expected: skill loads; maps the account structure; sets minimum/target balances from outflow patterns;
designs ZBA/target sweeps into a concentration account; sizes a buffer to a defined stress backed by a
committed facility; identifies the surplus above the buffer as investable (deferring instrument choice
to `finance-skills:short-term-investments`).

## 2. Near-miss (should NOT load this skill)
> "Given our closing position today, exactly how much should I sweep out of the operating account this
> afternoon?"

Expected: this is sizing a single sweep from today's actual position — a positioning task. The
`cash-management-skills:cash-positioning` skill should handle it. If this skill loads, tighten the
description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** sets minimum and target balances from outflow behavior, designs concentration/ZBA
  sweeps, sizes a buffer to a stress case backed by committed capacity, and splits surplus (investable)
  from buffer (safe/liquid).
- **Teaches:** explains the *idle-drag vs. liquidity-risk* trade-off, why concentration makes the
  decision once, and why the buffer must be sized to stress and backed by committed (not uncommitted)
  facilities — not just the sweep mechanics.
- **Safe:** does not invest the buffer itself for yield, does not rely on uncommitted lines as core
  backup, and does not set targets to round numbers detached from the account's outflow pattern.

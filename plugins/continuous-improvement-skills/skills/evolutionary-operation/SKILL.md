---
name: evolutionary-operation
description: >-
  Runs Box's Evolutionary Operation (EVOP): continuous improvement performed by the live
  production process itself — a tiny factorial pattern of settings for 2–3 process factors,
  perturbed within owner-approved safe operating limits around the current operating point,
  cycled on live production until factor effects separate from experimental error, then the
  operating center shifts toward the winner and the cycle repeats indefinitely. Output never
  leaves spec and the process never stops. Fits any tuned production process — reconciliation
  matching-rule tolerances, cash-forecast model parameters, collections dunning cadence — where
  offline experimentation is not an option. Use when tuning a running process without taking it
  down, or choosing among settings using live output. Triggers: EVOP, evolutionary operation,
  tune the matching rules, can't take it offline to test, keep improving in production, which
  tolerance is best, improve without stopping the process.
---

# Evolutionary operation (EVOP)

## When to use
- Tuning a production process you cannot stop to experiment on: a reconciliation engine's
  matching-rule tolerances, the parameters behind a live forecasting model, or the dunning
  cadence of a collections pipeline.
- Making investigation the process's *normal operating mode* — always-on, small-step improvement
  rather than a one-off study.
- Not for: designed experiments run offline in dedicated bursts with bold factor settings → see
  `continuous-improvement-skills:design-of-experiments` (the seam: DOE stops the world and takes
  big steps; EVOP never stops and takes steps small enough that every unit still ships). A
  one-time process redesign project → see `continuous-improvement-skills:dmaic-problem-solving`.

## Do it
1. **Get safe operating limits from the process owner before any perturbation** (the human gate).
   The owner — not the analyst, not the LLM — states the bounds inside which every setting is
   safe, and names the guard responses with hard limits. On a recon engine, false-match rate is a
   hard bound: a false match posts wrong cash. Write the limits down. Any drift outside spec stops
   the experiment immediately and returns the process to the last known-good center.
2. **Pick 2–3 process factors** you can actually set: an amount tolerance, a date window, a
   dunning wait. More than three makes the pattern too large to run unobtrusively in production.
3. **Define a tiny factorial pattern around the current operating point.** A 2×2 (low/high per
   factor) plus the current center — five settings, all inside the safe limits, steps small enough
   that output stays in spec at every point. See `references/evop-method.md` for the pattern
   geometry and a worked recon-tolerance example.
4. **Run cycles on live production.** One cycle = one pass through all pattern points in
   randomized order, recording every response at each point — the response you want to improve
   (match rate) *and* the guard (false-match rate). No interruption: production keeps shipping
   throughout.
5. **After each phase (several cycles), test factor effects against experimental error.** Compute
   each effect and its standard error from cycle-to-cycle scatter; act only on effects clearing
   about two standard errors. This ledger-and-significance work was historically a resident
   statistician's job — have the LLM maintain the EVOP log, run the small-sample tests, and state
   plainly what is and is not yet signal (mechanics in `references/evop-method.md`).
6. **When a direction wins, shift the operating center there** — with the owner ratifying the new
   center and refreshing the limits if the map has moved. Start the next phase around the new
   center, rotating in a fresh factor if an old one has gone quiet.
7. **Apply the stopping rules.** Effects flat for two phases → hold the center, swap factors, or
   (owner-approved) widen the pattern slightly. Never chase differences that haven't cleared the
   error bar.

## Why / learn
Box's observation, from chemical plants (Box & Draper, *Evolutionary Operation*, Wiley), is that a
process run at one fixed "best" setting produces product but zero information — nothing is ever
learned about the settings next door, so the process improves only by crisis. Run with tiny
deliberate perturbations instead, the same process produces product *and* information at once:
effects far too small to see in one cycle separate cleanly from noise after several, because
replication shrinks the standard error (roughly with the square root of the cycle count). That is
the whole trade: EVOP swaps the bold, fast, offline steps of a designed experiment for timid,
perpetual, in-production steps that cost nothing and never end. The method is canonical in
chemical and pharma operations, yet the quality press calls it an underused "tool in waiting"
[snippet-only] — and the barrier was never that the statistics were hard, but that they were
*constant*: someone had to keep the information board current and re-test effects after every
cycle, which historically meant a resident statistician per plant. An LLM removes exactly that
barrier — it designs the cycle plan, keeps the ledger, and does the significance arithmetic —
while the judgment EVOP always reserved for people stays with people: the process owner sets the
safe limits, ratifies every center shift, and owns the guard response. Respect the asymmetry of
the responses on something like a recon engine: match rate is a hill to climb, false-match rate is
a cliff — you climb the first only inside limits set by the second.

## Common mistakes
- Perturbing before the owner has set safe limits → experimenting on production with no guard.
  Limits first, always.
- Steps big enough that some output leaves spec → that's a designed experiment leaking into
  production, not EVOP. Shrink the pattern.
- Declaring a winner after one cycle → one cycle is one sample. Replicate until the effect clears
  its standard error.
- Moving the center on a non-significant effect → tampering (Deming's funnel): variance added
  while feeling productive.
- Watching only the response you want to improve → track the guard with equal rigor; a match-rate
  gain bought with false matches is a loss.
- Keeping no EVOP log → without the ledger there is no experimental-error estimate, so nothing can
  ever be called significant. Log from cycle one.

## Tailor to your environment
Record in `references/your-environment.md` the live processes you would tune, their settable
factors, response and guard metrics, the owner who sets limits, and the current operating center
(use `your-environment.private.md`, which is git-ignored, for anything naming real systems, rule
names, or bounds). Never commit real transaction data — structure only.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/evolutionary-operation.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/evop-method.md — phase/cycle mechanics, a worked 2×2 recon-tolerance example,
  significance from small samples, stopping rules, and the safe-bounds discipline
- references/your-environment.md — your tunable processes, factors, guards, limits, and owners

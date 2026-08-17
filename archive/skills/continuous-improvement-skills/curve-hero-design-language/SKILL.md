---
name: curve-hero-design-language
description: >-
  Provides the pre-built design-language map of Curve Hero — Curve Dental's cloud
  practice-management platform: its modules (Scheduler, Charting, Billing, Claims), shell
  patterns (Sidekick, SnapShot, Playbook Dashboards), verified field and workflow vocabulary
  (Recare not recall, Responsible Party not guarantor, Invoice not walkout, Carrier, Operatory,
  fee guide, days-owing aging), a say-this-not-that term map with provenance caveats — plus the
  reusable UI sync-audit method for making software feel native to users of any reference
  product. Use when building or labeling UI for Curve Hero users, answering Curve Hero
  terminology, module, or pattern questions, or syncing vocabulary to a reference product.
  Triggers: curve hero, curve dental, sidekick, recare, design language, terminology map,
  sync the UI, feel native to, reference product vocabulary, dental practice management
  software UI.
---

# Curve Hero design language (and the UI sync-audit method)

Make software feel native to users of **Curve Hero** — Curve Dental's cloud
practice-management platform — by mirroring its vocabulary, field labels, and interaction
patterns. The method below works for *any* reference product; the pre-built Curve Hero map
lives in `references/curve-hero-map.md`.

> **Provenance.** The map was compiled from public sources (Curve's sites block automated
> reads); every uncertain term is quarantined in the map's §7 "Unverified" list. **Scope:**
> mirror vocabulary, field semantics, and interaction patterns only — never branding, logos,
> trade dress, or trademarked names.

## When to use
- Building, reviewing, or labeling UI that Curve Hero users (dental front office, clinical,
  billing staff) will use — screens, fields, statuses, reports, empty states, docs.
- Answering "what does Curve Hero call X" terminology, module, or pattern questions.
- Running a vocabulary/pattern sync audit against any reference product, not just Curve Hero.
- Not for: the full build-or-improve-software process (charters, control charts, adversarial
  testing) → see `continuous-improvement-skills:lean-six-sigma-for-software`, which loads this
  skill at its UI-sync step. Generic UI naming with no reference product → see
  `full-stack-dev-skills:frontend-modern-ui`.

## Do it

For Curve Hero work, open `references/curve-hero-map.md` first (§2 platform map, §3 shell,
§4 modules, §5 vocabulary, §6 term map, §7 unverified) and apply it through the audit below.
For any other reference product, run the audit from scratch.

1. **Inventory the surface.** Screenshot every screen your users touch in the reference
   product; list modules, screen names, tabs, panels, buttons, and column headers verbatim
   (capitalization included).
2. **Harvest the vocabulary.** Build a term list from three sources: the UI itself, the
   vendor's help guides (guide titles are label-rich), and the words users *say* at the gemba.
   Where they conflict, users win for concepts, the UI wins for labels.
3. **Build the terminology map.** Three columns: concept → reference product's term → your
   product's term (usually identical). Mark conflicts with your existing vocabulary and decide
   once — **one term per concept, everywhere** (a half-synced app is worse than an unsynced
   one).
4. **Mirror the patterns, not the pixels.** Identify the interaction habits users have
   trained: where patient context lives, how scheduling works, what color codes mean, what a
   status list looks like. Reproduce the *behavioral contract* in your own design system (for
   an accessible one, see `continuous-improvement-skills:lean-six-sigma-for-software`
   references/accessible-ui-design-system.md) — and fix accessibility gaps rather than
   cloning them.
5. **Verify in the live product.** Every term marked uncertain gets checked in a real tenant
   or with a daily user; date-stamp the audit (cloud products rename things without notice).
6. **Standardize.** The terminology map becomes part of your design system's content-style
   layer; new screens are reviewed against it (a wrong label is a lint error, not a taste
   issue).

## Why / learn

Vocabulary sync works because **translation cost is cognitive waste paid on every click**: a
user who must map "guarantor" to the "Responsible Party" they know does it dozens of times a
day, and every mismatch erodes trust in the tool. Mirroring the *words and habits* (not the
pixels) transfers years of trained behavior for free — while keeping your product legally and
visually your own. The transferable patterns behind Curve Hero's design, worth carrying into
any operational product:

1. **Persistent patient/entity context** — one always-visible panel carrying identity,
   alerts, money, and to-dos, doubling as navigation. Users stop re-orienting per screen.
2. **Status = configurable object, not enum** — Curve makes confirmation types tenant-defined
   (name + color). Build status lists as admin-managed data.
3. **Color-coded status + Legend** — mirror the legend pattern but add non-color redundancy
   (icon/text) to meet WCAG 1.4.1, which color-only grids fail.
4. **Drag-and-drop with an alternative** — Curve leans on drag-and-drop scheduling; provide
   the keyboard/menu alternative WCAG 2.5.7 requires.
5. **Guide-title = label discipline** — help articles named exactly after UI actions
   ("Adding a Patient Payment"). Name your docs after your labels; it keeps both honest.
6. **Verb-phrase permissions** — permissions named as the action they allow (*Check Out
   Appointment*) are self-documenting; adopt the convention.
7. **The system is an actor** — automated entries attributed by name ("Curve Hero") in
   Created/Modified by. Give your automation a visible identity in audit trails.
8. **Low-friction patient-facing auth** — secure tokenized link + DOB beats a password portal
   for episodic users; pair with WCAG 3.3.8 (no cognitive tests).

## Common mistakes
- Cross-PMS vocabulary contamination → "recall", "guarantor", "walkout", "day sheet", "Money
  Finder" are Dentrix/Eaglesoft words; use the §6 term map (Recare, Responsible Party,
  Invoice, Production/Period Summary, Total Owing filters).
- Presenting §7-unverified terms as fact → quote them with the caveat and verify in a live
  tenant before shipping.
- Copying branding, logos, or trademarked names → sync vocabulary and patterns only; trade
  dress is off-limits.
- Hard-coding tenant-defined objects (confirmation types, tags) as enums → build them as
  admin-managed data, like Curve does.
- Cloning the reference product's accessibility gaps → mirror the pattern, fix the gap
  (color-only status, drag-only scheduling).
- Conflating Curve SuperHero (bundle) / Curve Capture (local agent) / Bridge (imaging display
  module) → three distinct things; see the map's §2.

## Tailor to your environment
Record live-tenant verifications in `references/your-environment.md`: your practice's Curve
Hero Practice ID's module set, verified label corrections (date-stamped), tenant-defined
confirmation types and tags. Keep anything identifying a real practice or patient out of git —
put raw detail in `your-environment.private.md` (git-ignored).

## References
- references/curve-hero-map.md — the full Curve Hero map: platform (§2), shell & navigation
  (§3), modules (§4), field & workflow vocabulary (§5), term map (§6), unverified list (§7)
- references/your-environment.md — your tenant's verified labels and corrections (fill in)

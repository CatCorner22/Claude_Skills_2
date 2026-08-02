# Accessible UI design system (beautiful, WCAG 2.2 AA, data-dense)

A design system for professional operational software — the Curve-Hero-class genre: busy
users, dense data, all day in the app. Beauty here means calm, ordered, and fast to read;
accessibility is engineered in as poka-yoke, not audited in at the end. Target conformance:
**WCAG 2.2 Level AA**.

Contents: §1 Design tokens · §2 Color · §3 Typography · §4 Layout & density · §5 Focus &
keyboard · §6 Forms · §7 Components · §8 Motion · §9 Content style · §10 Testing checklist

## §1 Design tokens (single source of truth)

Define once, consume everywhere (CSS custom properties / Tailwind theme / style dictionary):

```css
:root {
  /* Type scale — 1.25 ratio, rem-based (respects user font-size settings) */
  --text-xs: 0.75rem;  --text-sm: 0.875rem; --text-base: 1rem;
  --text-lg: 1.125rem; --text-xl: 1.25rem;  --text-2xl: 1.5625rem;
  --text-3xl: 1.953rem;

  /* Spacing — 4px base grid */
  --space-1: 0.25rem; --space-2: 0.5rem; --space-3: 0.75rem;
  --space-4: 1rem;    --space-6: 1.5rem; --space-8: 2rem; --space-12: 3rem;

  /* Radii and elevation — one family, used consistently */
  --radius-sm: 6px; --radius-md: 10px; --radius-lg: 14px;
  --shadow-1: 0 1px 2px rgb(16 24 40 / 0.06), 0 1px 3px rgb(16 24 40 / 0.10);
  --shadow-2: 0 4px 8px -2px rgb(16 24 40 / 0.10), 0 2px 4px -2px rgb(16 24 40 / 0.06);

  /* Motion */
  --ease-standard: cubic-bezier(0.2, 0, 0, 1);
  --duration-fast: 120ms; --duration-base: 200ms;
}
```

Tokens are poka-yoke for design: a hard-coded hex or px value in a component is a review
finding. Rem units + reflow-friendly layout are what make 200% zoom (SC 1.4.4) and 320 px
reflow (SC 1.4.10) work without heroics.

## §2 Color

Structure the palette by *role*, not by hue list:

- **Neutrals (90% of the UI)**: a warm-gray 11-step ramp for text/surfaces/borders. Body text
  on background ≥ **4.5:1** (SC 1.4.3); secondary text also ≥ 4.5:1 — if it can't hit that,
  it's decoration, not text.
- **One brand/action color**: used for primary actions, active states, links, focus — sparingly
  is what makes it legible as "interactive." Interactive component boundaries and states
  against adjacent colors ≥ **3:1** (SC 1.4.11).
- **Semantic set**: success / warning / danger / info, each with an accessible-on-white text
  shade and a pale surface shade. **Never color alone** (SC 1.4.1): pair with an icon and a
  word ("● Overdue" with icon + label, not a red dot).
- Large text (≥ 24 px, or ≥ ~18.7 px bold) may drop to 3:1, but a system is simpler when
  everything readable clears 4.5:1.
- Dark mode: same token roles remapped (not inverted); re-verify every contrast pair in both
  themes — dark mode fails contrast more often than light.
- Data visualization: sequential/diverging ramps for quantity, color-blind-safe categorical
  set, and always a redundant channel (shape, pattern, label).

## §3 Typography

- One UI family (a workhorse sans — e.g. Inter/Source Sans class) + optional mono for
  numbers/code. Tabular figures (`font-variant-numeric: tabular-nums`) in tables and money
  columns so digits align.
- Body at `--text-base` (16 px), line-height ~1.5 for prose, 1.3 for dense tables/labels.
- Hierarchy by weight and size steps from the scale — not by adding more colors.
- Line length ≤ ~75 characters for reading surfaces; data grids exempt.
- Real text, not text-in-images (SC 1.4.5); honors user text-spacing overrides (SC 1.4.12).

## §4 Layout & density (the operational-software problem)

Busy professionals want *density with order*, not whitespace theater:

- **Card-on-canvas**: a soft neutral canvas with white/raised cards grouping related data —
  the genre's (and Curve Hero's) native pattern. One elevation step; don't stack shadows.
- Density modes: comfortable (default) and compact (tables at `--text-sm`, tighter row
  padding) — user-selectable, remembered.
- Alignment grid: 4 px base; labels left-aligned; numbers right-aligned; dates in one format
  everywhere (see §9).
- Landmarks and structure: one `<h1>` per screen, sequential headings, `<nav>/<main>/<aside>`
  landmarks — structure is what makes density navigable for screen-reader users (and
  keyboard power users).
- Responsive: reflow to 320 px without horizontal scroll (SC 1.4.10) — wide tables get an
  in-container horizontal scroll with sticky first column, never a page-level scroll (data
  tables are formally excepted as two-dimensional content; contain their scroll anyway).

## §5 Focus & keyboard (where operational software usually fails)

Power users live on the keyboard; so do assistive-tech users. Same investment serves both:

- Everything operable by keyboard, no traps (SC 2.1.1/2.1.2); visible focus (SC 2.4.7). Adopt
  a **2 px outline + 2 px offset, ≥ 3:1 against adjacent colors** as the single global style —
  AA sets no numeric minimum, so this house standard bakes in the AAA Focus Appearance
  (SC 2.4.13) math and never has to be argued per-component:

```css
:focus-visible { outline: 2px solid var(--color-focus); outline-offset: 2px; }
```

- Focus never hidden behind sticky headers/toasts (SC 2.4.11 Focus Not Obscured — new in 2.2):
  `scroll-padding-top` ≥ sticky-header height.
- Logical tab order = visual order (SC 2.4.3); skip-to-content link first.
- Targets ≥ **24×24 CSS px** (SC 2.5.8 — new in 2.2); 40–44 px for primary touch targets
  (comfort, and the AAA bar).
- Anything draggable (calendar appointments, reorder lists) has a click/keyboard alternative
  (SC 2.5.7 Dragging Movements — new in 2.2): move via menu, cut/paste, or arrow keys.
- Keyboard shortcuts for the daily loop (search, new record, save) — documented, discoverable
  (`?` overlay), and remappable or at least disable-able (SC 2.1.4).

## §6 Forms (the heart of practice-management software)

- **Persistent labels above fields** — never placeholder-as-label (placeholders vanish on
  focus and fail low-vision users). Placeholder only for format hints (`MM/DD/YYYY`).
- Programmatic association: `<label for>`, `fieldset/legend` for groups, `aria-describedby`
  for help and error text (SC 1.3.1, 3.3.2).
- `autocomplete` attributes on identity/contact fields (SC 1.3.5 Identify Input Purpose) —
  faster for everyone, critical for cognitive accessibility.
- Errors: identify in text at the field *and* in a summary that receives focus on submit
  (SC 3.3.1); say *how to fix* (SC 3.3.3: "ZIP must be 5 digits", not "Invalid input");
  `aria-invalid` + error text linked via `aria-describedby`. Never color-only error states.
- **Never make the user re-enter what the system knows** (SC 3.3.7 Redundant Entry — new in
  2.2) — auto-fill from the existing record; "same as billing address" checkboxes.
- No cognitive-test logins (SC 3.3.8): support paste in password fields, offer
  passkeys/SSO/magic links over CAPTCHA gymnastics.
- Validate inline on blur (not on every keystroke), preserve input on error, autosave drafts
  (see `stability-and-redundancy.md` §3), and confirm destructive/irreversible submissions
  (SC 3.3.4 for legal/financial commitments).
- Help in a consistent location on every screen (SC 3.2.6 Consistent Help — new in 2.2).

## §7 Components (buy the hard ones, style the tokens)

- Build on headless accessible primitives (Radix/shadcn-class) for dialogs, comboboxes, menus,
  tabs, tooltips — correct focus management, ARIA per the ARIA Authoring Practices Guide, and
  screen-reader behavior are *hard*; hand-rolling them is how apps fail audits
  (→ `full-stack-dev-skills:frontend-modern-ui`).
- Tables/grids: real `<table>` semantics (or ARIA grid for editable grids), `<th scope>`,
  sortable headers as buttons announcing state (`aria-sort`), sticky header, per-row actions
  reachable by keyboard.
- Async regions: `aria-live="polite"` for status updates ("Payment posted"), `role="alert"`
  for errors; toasts also logged to a notifications panel (toasts alone are missable — 
  SC 4.1.3 Status Messages).
- Loading: skeletons over spinners for structure; always paired with an accessible status.
- Icons: labeled when interactive (`aria-label`), `aria-hidden` when decorative; never the
  only carrier of meaning.

## §8 Motion

- Motion is feedback, not decoration: 120–200 ms, standard easing, small distances.
- Honor `prefers-reduced-motion` globally (crossfade instead of slide/zoom; no parallax):

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
```

- Nothing flashes > 3×/second (SC 2.3.1); no auto-playing carousels on work screens.

## §9 Content style (the words are part of the design system)

- Labels in the **user's professional vocabulary** — harvested at the gemba and from the
  reference product (see `curve-hero-design-language.md`), one term per concept everywhere
  (if the reference says "Recare," the app never says "Recall" in one screen and "Recare" in
  another).
- Buttons say the verb + object ("Post Payment", "Save Treatment Plan"), never "OK"/"Submit".
- Empty states teach ("No claims yet — claims appear here after a visit is checked out") and
  offer the next action.
- Dates, money, and phone formats consistent app-wide; times carry timezone when it can differ.
- Reading level: plain, direct sentences; abbreviations expanded on first use per screen.

## §10 Testing checklist (accessibility as jidoka)

- [ ] Automated axe-core (or equivalent) scan in CI on every PR — blocking (catches ~30–40%;
      necessary, not sufficient)
- [ ] Keyboard-only pass on every new screen: complete every task, focus always visible,
      order logical, no traps
- [ ] Screen-reader smoke test on the critical paths (NVDA or VoiceOver): labels, states,
      live announcements make sense by ear
- [ ] 200% zoom and 320 px reflow pass; text-spacing override pass
- [ ] Both themes contrast-verified (tooling, not eyeballs) — text 4.5:1, UI components 3:1
- [ ] Reduced-motion verified; target sizes ≥ 24 px verified
- [ ] Forms: labels persistent, errors textual + focused, redundant entry eliminated,
      autocomplete set
- [ ] Include an accessibility acceptance line in the Definition of Done (see
      `full-stack-standards.md` §9) — a screen isn't done because it looks right; it's done
      when it *works blind, zoomed, and mouseless*

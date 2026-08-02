---
name: frontend-modern-ui
description: >-
  Builds lean, dynamic frontends — React + Vite when the UI is a real application (components
  by feature, server state via TanStack Query vs local UI state, forms, accessibility
  basics), htmx + server templates when it's mostly forms and tables, and the judgment call
  between them. Use when building or restructuring a web UI, untangling React state, wiring
  data fetching, choosing React vs htmx, or reviewing frontend code for excess complexity.
  Triggers: react component, frontend state management, tanstack query, useEffect fetch,
  htmx, vite setup, form handling react, UI architecture, frontend too complex, SPA vs server
  rendered, component design.
---

# Frontend: modern, dynamic, lean

## When to use
- Building or restructuring the UI of a full-stack app; deciding React vs htmx; fixing
  state-management tangles or data-fetching bugs.
- Not for: the rendering-split *architecture* decision → made in
  `full-stack-dev-skills:full-stack-app-architecture` (this skill executes it). Realtime
  updates (WebSockets/SSE) → `full-stack-dev-skills:realtime-and-dynamic-features`.
  Dashboard/visualization design → `data-analytics-bi-skills:dashboard-design`.

## Do it
1. **Honor the split decision, and default down.** Forms-and-tables UIs → **htmx**: the
   server renders HTML, htmx swaps fragments on interaction — no build step, no client
   state, routinely ~5x less code. App-like UIs (editors, live dashboards, rich
   interactions) → **React + Vite**. A hybrid (server pages + one React island) covers the
   common middle case.
2. **In React, separate the two kinds of state — this is most of frontend sanity:**
   - **Server state** (data that lives in the API): owned by **TanStack Query** —
     `useQuery(['invoices'], fetchInvoices)` gives caching, refetching, loading/error
     states; after a mutation, `invalidateQueries` re-syncs. Never copy server data into
     `useState` — that copy is a cache you now maintain by hand.
   - **UI state** (which tab is open, form drafts): plain `useState`/`useReducer`, kept in
     the component that owns it. Reach for context only for genuine cross-cutting state
     (theme, session); reach for a store library rarely.
3. **Structure components by feature, sized by responsibility.** `features/invoices/`
   holds its components, hooks, and API calls (mirroring the backend layout). Split a
   component when it has two reasons to change, not at a line count; extract a custom hook
   when *stateful logic* (not JSX) repeats.
4. **Fetch through one thin API layer.** A single `api.ts` wrapping `fetch` (base URL, auth
   header, error → thrown exception, JSON parsing) — components call named functions
   (`getInvoices()`), never raw fetch. Types come from the backend's OpenAPI schema
   (generate or mirror them) so the contract is checked, not assumed.
5. **Forms: use the platform first.** Uncontrolled inputs + `FormData` on submit covers most
   forms in a few lines; controlled inputs only where the UI reacts per keystroke; a form
   library (react-hook-form) only when validation complexity actually arrives. Server-side
   validation is the real gate either way (`full-stack-dev-skills:backend-api-development`) —
   client validation is UX, not security.
6. **Bake in the accessibility floor:** semantic elements (`button`, `label`, `nav` — not
   div-with-onClick), labels tied to inputs, keyboard reachability, visible focus. It's
   less code than the div-soup alternative and it's the difference between working and
   working for everyone.
7. **Keep the toolchain stock.** Vite defaults, one CSS approach (Tailwind *or* CSS modules
   — pick once), no bespoke webpack surgery, dependencies added the lean way
   (`full-stack-dev-skills:lean-code-principles`). `references/frontend-recipes.md` has the
   htmx patterns, TanStack Query setup, API-layer template, and the component checklist.

## Why / learn
Frontend complexity is almost always *state* complexity, and the deepest simplification is
recognizing that most "state" isn't yours: it's the server's data, briefly visiting the
browser. Treating it that way — a cache managed by a library built for caching — dissolves
the classic bug family (stale copies, manual refetches, loading flags drifting out of sync)
that `useState`+`useEffect` fetching breeds; what remains is genuinely local UI state, which
is small and easy. The React-vs-htmx call is the same insight at page scale: if the browser
holds no meaningful state between interactions, shipping a client-side application framework
to manage no state is pure overhead — htmx keeps the state where it already lives (the
server) and swaps the HTML it renders. Feature-folder components, the single API layer, and
OpenAPI-derived types are all one move — keep the frontend's shape congruent with the
backend's, so a feature is one vertical slice and the contract between the halves is checked
by tooling instead of by hope. And the platform-first form rule is lean-code applied to the
browser: HTML has been able to submit forms since 1993; libraries earn their place only when
the requirement outgrows the platform, not before.

## Common mistakes
- React by default for CRUD screens → htmx/server-rendered is drastically less code; decide per UI reality.
- Copying query results into `useState` → a hand-maintained cache; render from the query, invalidate to update.
- `useEffect` + fetch + loading flags by hand → TanStack Query exists; that pattern is its bug-prone reimplementation.
- Global store for everything → most state is local or server; stores for the rare true-global slice.
- Components split by line count or reuse speculation → split on responsibility; extract hooks for repeated *logic*.
- Raw `fetch` scattered through components → one API layer; typed functions per endpoint.
- Client-side validation as the only gate → it's UX; the server validates for real.
- Div-with-onClick UI → semantic HTML is less code and accessible; the floor is cheap.
- Toolchain tinkering (custom bundler configs) → stock Vite until a measured need says otherwise.

## Tailor to your environment
Record your frontend conventions in `references/your-environment.md`: React-vs-htmx decision
per surface, CSS approach, component/folder conventions, how types are derived from the API,
and your accessibility bar — so new UI (human- or agent-written) matches the house shape.

## References
- references/frontend-recipes.md — htmx fragment patterns, TanStack Query setup, API layer template, component checklist
- references/your-environment.md — your surfaces, conventions, and bars (fill in)

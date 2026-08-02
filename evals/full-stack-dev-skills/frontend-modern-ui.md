# Evals — full-stack-dev-skills:frontend-modern-ui

## 1. Positive trigger (should load the skill)
> "Our React app copies API data into useState everywhere, refetches by hand, and the
> invoice list is stale half the time. Untangle the state management — and honestly, half
> these screens are just tables and forms."

Expected: skill loads; separates server state (→ TanStack Query, invalidate on mutation)
from UI state (local useState); kills the useState-copy antipattern; routes raw fetches
through one API layer; flags the tables-and-forms screens as htmx/server-rendered
candidates per the architecture split.

## 2. Near-miss (should NOT load this skill)
> "What makes a good KPI dashboard — layout, chart choice, color for a monthly finance
> deck?"

Expected: dashboard craft — `data-analytics-bi-skills:dashboard-design`. If this skill
loads, sharpen the build-the-UI framing.

## 3. Quality rubric
A good response:
- **Does the task:** query-based data flow with invalidation, one API layer, feature-folder
  components, htmx recommendation where interactivity is thin.
- **Teaches:** server state vs UI state as the core distinction, why the copy is a
  hand-maintained cache, React-vs-htmx as a state-location question.
- **Safe:** keeps server-side validation as the real gate, semantic/accessible elements,
  stock toolchain.

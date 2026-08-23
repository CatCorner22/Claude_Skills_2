# Your environment (sanitized template)

Fill this in with your real recurring messes so the diagramming starts from your actual
structure. Keep it **structural**: no real figures, names, or client data. Anything sensitive
goes in `your-environment.private.md` — that suffix is git-ignored and never committed.

## Recurring messes (candidate systems to map)
- <problem that keeps coming back — e.g., "quarter-end backlog spike," "the same integration
  breaks after every fix"> — how long the pattern has repeated: <n cycles/quarters>
- <fix that decayed — what was tried, how long relief lasted, what came back>

## Stocks you track (and flows you don't)
- Stocks with real measurements: <backlog levels, balances, headcount, WIP — and where the
  history lives: dashboard, export, tracker>
- Flows that feed/drain them but go unmeasured: <arrival rates, reopen rates, attrition — the
  usual gaps>
- Slow stocks nobody measures: <trust, fatigue, tech debt — note any proxy you could use>

## Known delays
- <cause → visible effect lags you have observed: e.g., "policy change → behavior shift takes
  about a cycle," "hiring → productive takes <n> months">

## Known compensating actors (policy-resistance map)
- <who benefits from the current level of each contested stock, and how they have compensated
  when it was pushed before>

## Diagram conventions
- Where corrected causal-loop diagrams are kept: <repo/wiki/folder>
- House node-naming rules, if any: <e.g., "stocks in Title Case, flows lowercase">

## Hand-offs
- Quantitative loop tests go to: <who owns the data analysis, and which datasets they pull>
- Single-bottleneck findings go to: <the owner of the theory-of-constraints work>

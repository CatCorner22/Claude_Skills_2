# Your environment (sanitized template)

Fill this in with the anchor quantities and conventions of your own world so rough figuring
and gut-checks run on your numbers, not generic ones. Keep it **structural**: no real dollar
figures, client names, or account-level data. Anything sensitive goes in
`your-environment.private.md` — that suffix is git-ignored and never committed.

## Domain anchor quantities (your benchmark table)
- Headcount / staff: <e.g., "our office ≈ N people; the org ≈ N">
- Daily volumes: <e.g., "≈ N transactions/day", "≈ N appointments/day", "≈ N tickets/week">
- Typical sizes: <e.g., "a typical invoice is order $10³", "a typical payment run is order $10⁵">
- Revenue / cost per working day: <order of magnitude only in committed files>
- Calendar: <your working days per year, cycle lengths, seasonal peaks>

## Figures you are most often asked to gut-check
- <e.g., "month-end totals from system X", "the Y dashboard's daily number"> — the usual
  failure mode for each: <units slip / double count / stale filter / wrong period>

## Rounding and reporting conventions
- House precision for quoted figures: <e.g., "dollars to the nearest thousand in decks;
  to the cent only in ledgers">
- Range style: <e.g., "always give low–high with a central figure">

## Escalation
- When an estimate and a computed figure disagree beyond <threshold>, who investigates:
  <role / process>

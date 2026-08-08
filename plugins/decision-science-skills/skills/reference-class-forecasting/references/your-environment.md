# Your environment (sanitized template)

Fill this in with your real conventions so the outside view starts from your actual histories.
Keep it **structural**: no real dollar figures, counterparty names, or client data. Anything
sensitive goes in `your-environment.private.md` — that suffix is git-ignored and never committed.

## Variance histories (candidate reference classes you already own)
- **Cash drivers:** <where the per-driver forecast-vs-actual history lives — e.g., the accuracy
  tab of the 13-week model, an OTBI export, a variance workbook> — grain <weekly/monthly>,
  depth <n cycles>, per driver: <tuition receipts, payroll, grant drawdowns, AP runs, ...>
- **Projects/features:** <where estimated-vs-actual delivery history lives — tracker export,
  sprint reports> — unit <days/points>, depth <n items>
- **Other:** <bank-fee true-ups, investment-income projections, headcount plans, ...>

## Class conventions
- Default class definitions per estimate type: <e.g., "same driver, trailing 24 cycles,
  excluding definition-change periods (list them)">
- Exclusion log: <cases excluded from any class, each with its outcome-independent reason>

## Certainty levels (house policy)
- Disbursements / costs / schedules: <e.g., P80>
- Receipts feeding a liquidity floor: <e.g., P20>
- Who owns changes to these levels: <role>

## Decision journal
- Location: <file/system, append-only>
- Review cadence: <e.g., score at each cycle close; calibration buckets quarterly>
- Who sees the scores: <analyst only / team / leadership>

## Hand-offs
- Model corrections found via run tests go to: <the owner of the projection model —
  e.g., the cash-forecasting process owner> with the written diagnosis.

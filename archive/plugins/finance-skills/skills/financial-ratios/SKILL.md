---
name: financial-ratios
description: >-
  Computes and interprets liquidity, leverage, profitability, and efficiency ratios — current and
  quick ratios, debt-to-equity, interest coverage, gross/operating/net margins, ROA, ROE, asset and
  inventory turnover — and decomposes ROE with DuPont, always read against a benchmark or trend. Use
  when analyzing a company's ratios or financial health, or when explaining what is driving its
  return on equity. Triggers: financial ratios, current ratio, quick ratio, debt to equity, interest
  coverage, ROE, ROA, gross margin, operating margin, net margin, DuPont, asset turnover, inventory
  turnover, receivables turnover, financial health.
---

# Financial ratios

## When to use
- Calculating liquidity, leverage, profitability, or efficiency ratios from financial statements.
- Assessing a company's financial health, or diagnosing what drives its ROE via DuPont.
- Comparing a company against peers, its own history, covenant thresholds, or a target.
- Not for: building or reading the underlying income statement, balance sheet, and cash flow
  statement themselves → see `accounting-skills:financial-statements`. For freeing cash from
  receivables/inventory/payables specifically → see `finance-skills:working-capital-management`.

## Do it
1. **Gather clean statement inputs.** From the income statement and balance sheet, pull revenue, COGS,
   gross profit, EBIT (operating income), interest expense, net income; and current assets, inventory,
   cash, current liabilities, total assets, total debt, total equity. Use **average** balance-sheet
   figures when pairing a flow (income) with a stock (balance) — e.g. ROA, ROE, turnover.
2. **Compute liquidity ratios** (short-term solvency):
   - `Current ratio = Current Assets / Current Liabilities`
   - `Quick (acid-test) = (Current Assets − Inventory − Prepaids) / Current Liabilities`
   - `Cash ratio = (Cash + Cash equivalents) / Current Liabilities`
3. **Compute leverage / solvency ratios:**
   - `Debt-to-equity = Total Debt / Total Equity` (state whether "debt" is interest-bearing debt or
     total liabilities — the two differ materially).
   - `Interest coverage (TIE) = EBIT / Interest Expense`
   - `Debt-to-assets = Total Debt / Total Assets`; `Equity multiplier = Total Assets / Total Equity`.
4. **Compute profitability ratios:**
   - Margins: `Gross = Gross Profit / Revenue`, `Operating = EBIT / Revenue`, `Net = Net Income / Revenue`.
   - `ROA = Net Income / Average Total Assets`; `ROE = Net Income / Average Total Equity`.
5. **Compute efficiency (activity) ratios:**
   - `Asset turnover = Revenue / Average Total Assets`
   - `Inventory turnover = COGS / Average Inventory`; `Receivables turnover = Credit Sales / Average AR`.
6. **Decompose ROE with DuPont** to locate the driver (see `references/ratio-formulas.md`):
   - 3-step: `ROE = Net margin × Asset turnover × Equity multiplier`
     `= (NI/Sales) × (Sales/Assets) × (Assets/Equity)`.
   - 5-step splits net margin into tax burden × interest burden × operating margin, isolating whether
     ROE comes from operations, leverage, or taxes.
7. **Interpret against a reference, never in isolation.** Compare each ratio to the industry/peer set,
   the company's own trend, and any covenant or target. State the *direction* a value implies and
   whether the benchmark is even apt (see caveats). A ratio without a comparison is a number, not a
   conclusion.

## Why / learn
A financial ratio is a **diagnostic**, not a verdict. On its own, "current ratio = 1.4" or "ROE = 18%"
tells you almost nothing — the entire information content lives in the comparison: against peers in the
same industry, against the company's own history, or against a target or covenant. That is the one idea
to carry: ratios are meaningful only *relative* to a benchmark or trend, because what counts as healthy
is industry- and structure-specific. A grocer lives on thin margins and high asset turnover; a software
firm on fat margins and low turnover — the *same* ROE assembled completely differently. This is exactly
why DuPont matters: it factors ROE into how profitable each sale is (margin), how hard assets are worked
(turnover), and how much leverage amplifies both (equity multiplier). Two firms with identical ROE can
be opposites underneath — one earning it through operations, another borrowing its way there — and the
decomposition makes that visible so you praise or worry about the right thing. Leverage is the sharpest
example: it multiplies ROE in good years and multiplies losses in bad ones, so a high ROE built on a
high equity multiplier is fragile, not admirable. And ratios can be quietly gamed or distorted —
accounting-policy choices, seasonality, one-time items, window dressing at period-end, or a near-zero
denominator — so a ratio is a question ("why is this off-trend?"), and the analysis is the answer.

## Common mistakes
- Reading a ratio with no benchmark or trend → a bare number is not a conclusion. Always compare.
- Pairing a flow with a period-end stock (e.g. ROE on ending equity) → use *average* balances.
- Comparing across industries as if one norm fits all → grocer vs software have opposite structures.
- Ambiguous "debt" in D/E → say whether it is interest-bearing debt or total liabilities.
- Cheering high ROE without DuPont → it may be leverage, which cuts both ways.
- Ignoring one-time items and accounting-policy differences → normalize before comparing peers.
- Dividing by a tiny or negative denominator (near-zero equity, negative EBIT) → the ratio is unstable.

## Tailor to your environment
Record your setup in `references/your-environment.md` (or `your-environment.private.md`, git-ignored, if
it names real figures — never commit real data). Capture your peer/benchmark set, your definition of
"debt" for leverage ratios, any loan covenants and their thresholds, whether you use average or
period-end balances, and any normalization rules for one-time items. The generic formulas then run
against your statements and comparators.

## References
- references/ratio-formulas.md — full ratio catalog by category, DuPont 3- and 5-step, and interpretation caveats
- references/your-environment.md — your peer set, debt definition, covenants, and normalization rules (add when supplied)

# Factor-label chains, the dimensional-check protocol, and the trap catalog

Contents: §1 Factor-label worked chains · §2 Per-unit rates: building, multiplying,
dividing · §3 Annualizing and de-annualizing · §4 The formula dimensional-check
protocol, with a worked catch · §5 The trap catalog, with verified numbers

Every number below is recomputed, not quoted. The habit transfers: any chain you write
should be checkable the same way by someone with only the page in front of them.

## §1 Factor-label worked chains
A conversion factor is a fraction equal to 1 — its top and bottom are the same quantity
in different clothes. Multiplying by 1 changes representation, never value, so a chain
of factors is a proof that the start and end quantities are equal.

**Speed (two hops in one chain).** 45 mi/hr in ft/s:
```
45 mi     5280 ft     1 hr        45 × 5280      237,600
------ × --------- × --------  =  ---------  =  --------- ft/s  =  66 ft/s
 1 hr      1 mi      3600 s         3600           3600
```
Miles cancel against miles, hours against hours; only ft/s survives. The arithmetic is
checked separately: 45 × 5280 = 237,600; 237,600 ÷ 3600 = 66.

**Volume and time (three hops).** A pump moves 3 L/min; gallons per 8-hour day
(1 gal = 3.785 L):
```
3 L      60 min     8 hr      1 gal
----- × -------- × ------ × --------  =  (3 × 60 × 8 / 3.785) gal/day
1 min     1 hr     1 day    3.785 L
```
3 × 60 = 180 L/hr; × 8 = 1,440 L/day; 1,440 ÷ 3.785 ≈ 380.4 gal/day.
(Check: 3.785 × 380 = 1,438.3, so 380.4 is right to one decimal.)

**Currency as a unit.** 8,400 EUR at 1.08 USD/EUR:
```
            1.08 USD
8,400 EUR × --------  =  9,072 USD
             1 EUR
```
EUR cancels; 8,400 × 1.08 = 8,400 + 672 = 9,072. An FX rate is nothing but a conversion
factor, so the whole method applies unchanged — including the upside-down test: dividing
by 1.08 here would leave units of EUR²/USD, which is the chain telling you it's wrong.

**Scale as a unit.** A report column headed "$ thousands" shows 2,340:
```
             1,000 $                          1 M$
2,340 k$ × ---------  =  2,340,000 $ ;  2,340 k$ × ----------  =  2.34 M$
              1 k$                              1,000 k$
```
Writing k$ and M$ as real units turns a silent 1,000× hazard into an explicit,
checkable step.

## §2 Per-unit rates: building, multiplying, dividing
"Per" is division. A per-unit rate is a full quantity with a compound unit, and it
obeys the same algebra as everything else.

**Building one (chain downward through packaging).** A carton holds 24 boxes; a box
holds 500 sheets; a carton costs $54:
```
 54 $      1 carton     1 box          54
-------- × --------- × ----------  =  ------ $/sheet  =  0.0045 $/sheet
1 carton   24 boxes    500 sheets     12,000
```
24 × 500 = 12,000 sheets/carton; 54 ÷ 12,000 = $0.0045/sheet.

**Multiplying rates (units chain through).** A team clears 480 invoices per 8-hour day
→ 480/8 = 60 invoices/hour. One processor handles 12 invoices/hour, so staffing the
flow takes 60 ÷ 12 = 5 processors — (invoices/hr) ÷ (invoices/hr·person) leaves
persons, which is the unit the question wanted.

**Dividing rates (common time base first).** Cost $900/day, throughput 60 invoices/hour.
The naive division 900/60 = "15" is not $15/invoice — its unit is
($/day)/(invoices/hr) = $·hr/(invoice·day), which is not a cost per invoice, and the
unit says so before any number can mislead. Convert to one base:
60 invoices/hr × 8 hr/day = 480 invoices/day, then 900 ÷ 480 = $1.875/invoice.

## §3 Annualizing and de-annualizing
**Flows: ×12 is itself a factor-label move.** $2,350/month:
```
2,350 $     12 mo
-------- × ------  =  28,200 $/yr
  1 mo      1 yr
```
Months cancel; 2,350 × 12 = 28,200. De-annualizing runs the factor the other way:
$46,800/yr ÷ 12 = $3,900/month.

**Rates of return: ×12 understates, because growth compounds.** 1% per month for a year
is (1.01)¹² − 1 = 0.126825 ≈ 12.68%/yr, not 12% — each month's 1% acts on a base the
earlier months already grew. The unit lens shows why the cases differ: a flow's unit is
$/month, and multiplying by 12 months/yr cancels cleanly; a periodic return is
dimensionless-per-period and lives in an exponent, where no unit may appear. The ×12
figure is the "nominal annual" convention — fine as a label, wrong as a prediction of
what a balance does. The (1+r)ⁿ machinery, CAGR, and doubling times belong to
the archived `math-foundations-skills:exponential-growth-and-logs`; this skill's job is routing you
to the right one of the two moves.

## §4 The formula dimensional-check protocol
Run this on any formula before trusting it — inherited spreadsheet logic, a draft of
your own, a formula from a document you cannot interrogate.

1. **Write the unit of every symbol** next to the formula ($, $/month, invoices/day,
   dimensionless, …). A symbol nobody can assign a unit to is finding #1.
2. **Work out the unit of every term** by multiplying and cancelling.
3. **Apply the three laws:**
   - Terms added or subtracted share one unit ($ + $/month is meaningless).
   - The two sides of the equation carry the same unit.
   - Arguments of exp, ln, trig — and any exponent — are dimensionless.
4. **Verdict.** Any violation refutes the formula outright; no numeric test needed.
   Passing does not prove it right (a dimensionless constant can still be wrong) — it
   promotes the formula to "worth testing numerically."

**Worked catch — from this library's own history.** The
the archived `safety-and-reliability-skills:weight-of-the-books` skill dates each safety margin: how
long until a growing load erodes the factor F = capacity/load down to its written floor.
A draft formula said:

> time to exhaustion = F ÷ g   (g = load growth per year)

Check it. F is capacity/load — the units cancel; it is a pure number. g is fractional
growth per year, so "per year" is its only dimension. F ÷ g then carries "years" only
in the way a coin toss carries destiny — divide any pure number by any per-year figure
and "years" pops out, regardless of whether the quantity means anything. The check
forces the real question: *what is the law relating F to time?* Load grows as
L(t) = L₀(1+g)ᵗ, so F(t) = F₀/(1+g)ᵗ — exponential, not linear. Solving
F(t) = F_floor gives:

> t = ln(F₀/F_floor) ÷ ln(1+g)

Both logarithm arguments are dimensionless, as the third law requires. The numbers show
how far off the draft was: F₀ = 3.0, floor = 1.5, g = 25%/yr. Correct:
t = ln(2) ÷ ln(1.25) = 0.6931 ÷ 0.2231 ≈ 3.1 years. (Check: 1.25³ = 1.953 ≈ 2, so just
over 3 years — consistent.) The draft: 3.0 ÷ 0.25 = 12 years — plausible-looking and
nearly four times too long, the exact failure mode where a margin evaporates years
before its owner expects. Adversarial review caught it because a reviewer wrote the
units of every term; the author's plausible numbers had sailed past everyone. The check
works on authors too.

## §5 The trap catalog, with verified numbers
- **Per-month + per-year in one sum.** Rent $1,800/mo plus insurance $2,400/yr is not
  "$4,200" of anything. Common period first: 1,800 × 12 = 21,600 $/yr;
  21,600 + 2,400 = **$24,000/yr**. The tell: an addition whose terms you cannot write
  with one shared unit.
- **Thousands vs millions.** "Revenue: 2,340" under a "$ thousands" header is
  $2,340,000 = $2.34 M — read raw, the error is 1,000×, and both readings look
  plausible in isolation, which is why plausibility review never catches it. Fix:
  convert k$/M$ explicitly (§1).
- **Percent as a count.** % is a dimensionless unit meaning "per hundred":
  5% = 5/100 = 0.05. Formulas want the 0.05; labels want the 5%. Adjacent trap for the
  road: a move from 4% to 5% is +1 percentage *point* but a 25% *relative* increase
  (1/4 = 0.25) — say "points" when you mean the difference of two percentages.
- **Mixed time bases in a division.** ($/day) ÷ (items/hour) — see §2; convert to one
  base first or the "cost per item" is fiction.
- **×12 on a compounding rate.** 1%/month is ≈12.68%/yr, not 12% (§3).
- **The upside-down factor.** Multiplying by 3600 s/hr when seconds should cancel gives
  units of s²/hr-something — the chain itself flags it, provided the units were written
  down at all. Orientation by cancellation makes this trap structurally impossible.
- **The unitless spreadsheet.** A workbook of bare numbers cannot be unit-checked. Put
  the unit in the column header ("Cost ($/unit)", "Volume (k$)"), and the whole sheet
  becomes checkable at a glance.

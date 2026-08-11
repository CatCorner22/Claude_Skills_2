# KYC / AML reference (educational)

**Educational only — not legal or compliance advice.** Requirements vary by jurisdiction, regulator,
and firm program. **Defer to your compliance / BSA officer** and your written policy. Thresholds and
list names below are illustrative — **confirm the current rules for your jurisdiction.**

## Contents
- The due-diligence tiers (KYC / CDD / EDD)
- Beneficial ownership (UBO)
- Sanctions and watchlist screening
- AML red flags
- Transaction monitoring and SARs
- Correspondent banking risk

## The due-diligence tiers (KYC / CDD / EDD)
- **KYC (Know Your Customer):** the umbrella — establishing and verifying who a counterparty is.
- **CDD (Customer Due Diligence):** the standard tier — identify and verify the customer, identify
  beneficial owners, understand the **nature and purpose** of the relationship to build an expected-
  activity profile, and conduct **ongoing monitoring**.
- **EDD (Enhanced Due Diligence):** the elevated tier for higher-risk relationships — deeper identity
  and ownership verification, **source of funds / source of wealth**, senior-management approval, and
  intensified ongoing monitoring.
- **Risk rating** drives the tier. Common risk factors: customer type (shell/holding structures,
  cash-intensive businesses, money-services businesses), geography (high-risk/sanctioned
  jurisdictions), product/service, and delivery channel (non-face-to-face). **PEPs** (politically
  exposed persons) and correspondent banks are typically EDD by default.

## Beneficial ownership (UBO)
- Identify the **natural persons** who ultimately own or control a legal-entity counterparty.
- **Two prongs:** an **ownership prong** (individuals holding at or above an equity threshold — often
  **25%**, but **confirm for your jurisdiction**) and a **control prong** (an individual with
  significant responsibility to control/manage, e.g. a senior officer).
- **Unwind layers:** ownership through intermediate entities must be traced until you reach real
  people; a UBO hidden two or three entities up is exactly what the rule targets.
- Verify UBO identities and screen them like the counterparty itself.
- Regimes evolve (e.g. US FinCEN CDD rule and beneficial-ownership reporting frameworks; EU AML
  directives; UK PSC register) — **confirm the current regime and thresholds.**

## Sanctions and watchlist screening
- **Strict liability:** dealing with a sanctioned party is prohibited regardless of intent — this is
  categorically stricter than the risk-based rest of the program.
- **Lists:** US Treasury **OFAC**, including the **SDN** (Specially Designated Nationals) list and
  sectoral/consolidated lists; **UN**, **EU**, **UK/OFSI**, and local lists. Plus **PEP** and adverse-
  media lists. Screen against the lists applicable to your jurisdiction and business.
- **When to screen:** at **onboarding**, on an **ongoing** basis (lists change), and on **payments in
  real time** — screening names, addresses, countries, and (for trade finance) vessels and goods.
- **Alerts:** investigate and resolve before proceeding. Distinguish false positives (name similarity)
  from true matches. A true match generally means **block** (freeze/hold and report) or **reject**
  (refuse and return) — **these are different legal actions; confirm which applies with compliance.**
- **50% rule / ownership:** entities owned above a threshold by sanctioned parties can themselves be
  treated as sanctioned even if not named — **confirm the applicable rule.**

## AML red flags
Compare activity to the expected profile from CDD. Common flags (non-exhaustive):
- **Structuring / smurfing:** transactions kept just under reporting thresholds; many small deposits.
- **Rapid movement / pass-through / layering:** funds in and out quickly, or through many accounts.
- **Inconsistent activity:** volume/value/counterparties that don't fit the stated business.
- **Unexplained third parties:** payments to/from parties with no business rationale.
- **High-risk geographies:** counterparties or routing through sanctioned/high-risk jurisdictions.
- **Shell-company traits:** no physical presence, opaque ownership, nominee directors.
- **Behavioral flags:** reluctance to provide information, unusual urgency, or requests to avoid records.
- **Trade-based flags:** over/under-invoicing, mismatched goods/values, circular shipments.

## Transaction monitoring and SARs
- **Transaction monitoring:** rules/scenarios (and increasingly models) that surface activity
  inconsistent with the profile or matching known typologies; alerts are investigated by compliance.
- **SAR (Suspicious Activity Report):** filed with the financial-intelligence unit (e.g. **FinCEN** in
  the US) when activity is suspicious. Filing thresholds, timing, and forms are jurisdiction-specific.
- **No tipping off:** you must not disclose to the customer (or anyone unauthorized) that a SAR is
  being considered or filed, or that an investigation is underway — it is prohibited and defeats the
  purpose. Keep it confidential and route through compliance.
- **The filing decision belongs to compliance / the BSA officer**, not to front-line or treasury staff.

## Correspondent banking risk
- A correspondent holds accounts for **respondent** banks, whose underlying customers you never see —
  so you inherit their risk (**nested** / downstream correspondents amplify this).
- **Shell banks** (no physical presence, not affiliated with a regulated group) are prohibited as
  correspondents under measures such as the USA PATRIOT Act.
- Controls: respondent **due diligence** (ownership, regulation, AML program), the **Wolfsberg
  Correspondent Banking Questionnaire**, restrictions on nested relationships, and enhanced monitoring
  of correspondent flows. Cross-border USD/SWIFT flows concentrate this risk — treat as EDD.

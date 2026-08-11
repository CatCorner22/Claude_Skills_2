# Your cash positioning environment (sanitized template)

Fill this in with your real conventions. If any value is sensitive (account numbers, real balances,
counterparties), keep it in `your-environment.private.md` instead — that suffix is git-ignored.

- **Accounts in scope:** <list account roles: concentration, operating, disbursement, payroll, FBO>
- **Currencies:** <e.g. USD, EUR, GBP — positioned separately>
- **Entities:** <legal entities and which accounts belong to each>
- **Balance positioned to:** <available/collected balance | ledger balance>
- **Cutoff time:** <e.g. 11:00am ET for same-day funding; later items roll to next day>
- **Statement feeds:**
  - Prior-day: <BAI2 | MT940 | CAMT.053>, arrives <time>
  - Intraday: <MT942 | BAI2 intraday>, refresh <frequency>
- **Internal flow sources:** <AP payment run schedule; AR lockbox/card settlement timing; payroll days; tax/debt calendar>
- **Target / minimum balances:** <per account — the level sweeps aim at and the floor to defend>
- **Sweep/funding channels:** <ZBA to concentration; MMF sweep; revolver draw; internal transfer>
- **Systems:** <ERP/treasury, e.g. Oracle Fusion Cash Positioning; bank portals; TMS>
- **Position owner / review time:** <who builds it, by when, who approves funding moves>
- **Recurring known flows:** <standing wires, monthly sweeps, dividend/interco dates, tax estimates>

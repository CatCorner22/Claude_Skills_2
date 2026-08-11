# Your liquidity environment (sanitized template)

Fill this in with your real conventions. If any value is sensitive (real balances, facility terms,
account numbers), keep it in `your-environment.private.md` instead — that suffix is git-ignored.

- **Account hierarchy:** <concentration/master; operating, disbursement, payroll, collection accounts, by entity and currency>
- **Current sweep rules:** <which accounts ZBA vs. target-balance sweep; into which concentration account; timing>
- **Minimum balances:** <per account — the floor to defend, and what drives it>
- **Target balances:** <per account — the level sweeps leave/top up to>
- **Buffer policy:** <how sized — days of outflows | peak shortfall + margin | stress overlay; the amount>
- **Committed facilities:** <revolver limit, commitment fee, covenants, draw process>
- **Uncommitted facilities:** <money-market lines and limits — backup only>
- **Approved surplus instruments & limits:** <MMFs, T-bills, deposits; per-instrument/counterparty caps; max tenor>
- **Deficit coverage order:** <internal transfer → committed draw → other>
- **Pooling:** <physical/notional; cross-entity, with interco and tax notes>
- **Policy owner / review cadence:** <who owns limits and buffer; how often re-sized>

---
name: bank-connectivity
description: >-
  Reasons about the channels that connect an ERP or TMS to banks — host-to-host SFTP, SWIFT (Alliance,
  service bureau, SCORE), bank APIs / open banking, and single-bank portals — weighing cost, effort,
  resilience, and standardization, and covering file security (PGP, SSH keys). Use when integrating
  with a bank, choosing a connectivity channel, or securing bank file transfer. Triggers: host-to-host,
  H2H, SFTP, SWIFT connectivity, service bureau, SCORE, Alliance Lite, bank API, open banking, ERP to
  bank, TMS to bank, bank portal, PGP, connectivity channel.
---

# Bank connectivity

## When to use
- Choosing how an ERP/TMS should exchange payments and statements with one or many banks.
- Comparing host-to-host SFTP, SWIFT, APIs, and portals for a new bank or a rationalization.
- Securing bank file transfer (encryption, keys) or deciding when an API beats file transfer.
- Not for: choosing which payment *rail* to send funds on (ACH/wire/RTP/SWIFT payment) → see
  `banking-skills:payment-rails`. For parsing the statement files that arrive over a channel → see
  `banking-skills:bank-statement-parsing`.

## Do it
1. **State the requirement.** How many banks and countries; what you exchange (payment initiation
   `pain.001`, statements `camt`/BAI2/MT940, acks/status `pain.002`); volume and batch vs real-time
   needs; and your internal system (ERP or TMS) and its native connectors.
2. **Shortlist channels by fit** (see `references/connectivity-channels.md`):
   - **Single-bank portal:** manual web upload/download. Fast to start, no build — but doesn't scale
     past a couple of banks and has no straight-through processing. A fallback, not a strategy.
   - **Host-to-host (H2H) SFTP:** direct file exchange with one bank over SFTP. Automatable and
     cheap per bank, but **bank-specific** formats/mappings and one integration to build per bank.
   - **SWIFT:** one standardized network reaching **many** banks. Access via direct **Alliance**
     (incl. cloud **Alliance Lite2**), a **service bureau** (outsourced infrastructure), or **SCORE**
     (join SWIFT as a corporate to reach member banks). Higher effort/cost, high standardization.
   - **API / open banking:** real-time request/response and push notifications for balances,
     transactions, payment initiation, and status. Best where you need immediacy; standards vary.
3. **Weigh the four trade-offs explicitly:** **cost** (build + run), **effort** (per-bank vs
   one-network), **resilience** (redundancy, no single point of failure), and **standardization**
   (ISO 20022 across banks vs per-bank formats). Score your shortlist against these, not on price
   alone. See the decision guide in `references/connectivity-channels.md`.
4. **Match volume/latency to the channel.** High-volume **batch** (payroll, AP runs, end-of-day
   statements) fits **files** (H2H/SWIFT FileAct). Real-time needs (instant balance, payment status,
   RTP/FedNow initiation, event-driven flows) fit **APIs**. Most treasuries run a hybrid.
5. **Secure the transfer.** For files: **PGP** encryption of payload plus **SSH key** authentication
   for SFTP (not passwords); rotate keys; restrict by IP allowlist; enforce dual control on payment
   files; and add **non-repudiation / digital signatures** (e.g. PKI, personal signing tokens) where
   the bank supports it. For APIs: OAuth/mTLS, scoped credentials, and signed requests.
6. **Standardize the payload.** Prefer **ISO 20022** (`pain.001` payments, `camt.05x` statements) so
   the same message works across banks and channels; keep bank-specific mapping in one place. Confirm
   each bank's ISO version/flavor — banks differ in supported tags. Then pilot, parallel-run against
   the old channel, and cut over once acks and statements reconcile.

## Why / learn
Connectivity is not one decision but a **trade-off across cost, effort, resilience, and
standardization**, and the channels sit at different points on it. A **single-bank portal** is
cheapest and fastest to start and worst to scale — every bank is a separate login and a human in the
loop, so it works for one or two banks and collapses under many. **Host-to-host SFTP** automates that
exchange but pushes the cost into **per-bank integration**: each bank has its own file specs, so ten
banks can mean ten mappings and ten things to maintain — cheap per link, expensive in aggregate,
and only as resilient as each point-to-point pipe. **SWIFT** inverts the equation: you build to
**one standardized network** and reach many banks, so effort and standardization improve dramatically
as bank count grows — which is exactly why it pays off for multi-bank corporates and looks like
overkill for a single-bank shop. **APIs** change a different axis — **latency**. Files move in
scheduled batches with cutoff windows; an API answers *now* and can push events, which is why it
wins for instant balances, payment-status tracking, and initiating instant rails, while files still
win for bulk. The security model follows the channel: file channels lean on **PGP for confidentiality
and SSH keys for authentication** (encrypt the payload, authenticate the pipe, sign for
non-repudiation), APIs on OAuth/mTLS. The through-line is that **standardizing the payload on ISO
20022** decouples *what* you send from *how* you send it, so you can change channels without rewriting
your payment and statement logic. Decide by asking "how many banks, how fast, how resilient, how
standard" — not by price alone.

## Common mistakes
- Defaulting to per-bank H2H for many banks → integration sprawl. Past a few banks, weigh SWIFT's standardization.
- Using bank portals for production payment flows → manual, no STP, error-prone. Automate the channel.
- Password-based SFTP or unencrypted files → security exposure. Use SSH keys **and** PGP, and rotate keys.
- Reaching for an API when you need bulk throughput → files handle high-volume batch better. Match volume to channel.
- Assuming "ISO 20022" is identical everywhere → banks differ in version and supported tags. Confirm each bank's flavor.
- No parallel run at cutover → silent breakage. Run old and new channels together until they reconcile.

## Tailor to your environment
Drop your real setup into `references/your-environment.md` (keep host names, IPs, key fingerprints,
and credentials in `your-environment.private.md`, which is git-ignored — never commit keys or
connection secrets). Capture your ERP/TMS and its connectors, your bank list with the channel and
format each uses, your SWIFT access model if any (direct/bureau/SCORE), your encryption and key-
rotation policy, and your batch windows vs real-time needs. Channel availability, ISO 20022 flavors,
and API coverage differ by bank and country — **confirm for each bank/region.**

## References
- references/connectivity-channels.md — channel options, trade-off matrix, file security, and the API-vs-file decision
- references/your-environment.md — your systems, banks, channels, and security policy (add when supplied)

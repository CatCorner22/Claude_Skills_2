# Merchant economics, chargebacks, and PCI (reference)

Interchange tables, card-brand dispute rules, and PCI-DSS versions change on their own
schedules. This file teaches the **structure**; confirm current specifics with your acquirer,
the card-brand bulletins, or your QSA.

## Contents
- The acquiring stack, precisely
- Fee anatomy and pricing models
- Reading a merchant statement (worked structure)
- Interchange optimization levers
- Chargeback lifecycle and reason-code families
- PCI-DSS: scope, storage rules, SAQ landscape, merchant levels
- Governance artifacts worth keeping

## The acquiring stack, precisely
- **Merchant ID (MID):** the account under which your transactions clear. Large institutions
  use a hierarchy — a chain/parent code with child MIDs per department or channel. Terminal IDs
  (TIDs) sit under MIDs.
- **Gateway:** software that captures the card and routes it for authorization (e.g. a hosted
  payment page for online tuition). Charges its own per-transaction/monthly fees. May be
  independent of the processor.
- **Processor / acquirer:** the entity (and its sponsoring bank) that connects you to the card
  networks, clears the batches, funds your deposits, and holds your merchant agreement — the
  counterparty for fees, reserves, and chargebacks.
- **Card networks:** set interchange and the dispute (chargeback) rules; you don't contract
  with them directly except historically for American Express-style direct agreements.
- **Issuer:** the cardholder's bank; receives interchange; initiates chargebacks on the
  cardholder's behalf.

## Fee anatomy and pricing models
Total card cost has exactly three layers:

| Layer | Set by | Paid to | Negotiable? |
|-------|--------|---------|-------------|
| Interchange | Card networks (published tables, by card type + channel + data quality) | Issuing bank | No — but you influence *which category* you qualify for |
| Assessments / network fees | Card networks | Networks | No |
| Processor markup | Your merchant agreement | Acquirer/processor/gateway | Yes — the only layer to negotiate |

Pricing models repackage those layers:
- **Interchange-plus (pass-through):** interchange + assessments at cost, plus a disclosed
  markup ("IC + X bps + $Y/item"). Transparent; preferred for institutional volume.
- **Tiered (bundled):** transactions bucketed into qualified / mid-qualified / non-qualified
  rates. The bucketing rules are the processor's; downgrades silently migrate volume to the
  expensive tiers.
- **Flat rate:** one blended rate (common with turnkey providers). Simple, usually expensive at
  scale.

**Effective rate** = total fees (all layers, all line items) ÷ gross card volume, per MID per
month. Trend it; investigate step-changes — they are usually downgrades, mix shifts, or new
line-item fees rather than "rate increases."

## Reading a merchant statement (worked structure)
Statements vary by processor, but look for these blocks:
1. **Summary:** gross sales, refunds, chargebacks, fees, net deposit — tie net deposits to the
   bank statement for the month.
2. **Volume by card type:** credit vs debit vs signature debit, by network; the mix drives cost.
3. **Interchange detail (interchange-plus only):** each interchange category with rate and
   volume. Scan for categories containing words like "standard," "EIRF," or "non-qualified" —
   these are downgrade/penalty categories worth root-causing.
4. **Fees section:** per-item fees, monthly/statement fees, gateway fees, PCI program or
   **PCI non-compliance** fees (the latter = your SAQ/scan is overdue — fix the paperwork, save
   the fee), chargeback fees, batch fees.
5. **Chargeback/adjustment activity:** provisional debits and reversals.

## Interchange optimization levers
- **Card-present with EMV/contactless** capture where applicable (rate + fraud-liability).
- **AVS and proper e-commerce indicators** on card-not-present volume.
- **Level II/III data** (tax amount, customer code, line items) on corporate, purchasing, and
  government cards — material at a public institution where B2B/agency payments are common.
- **Settle batches daily** — stale authorizations downgrade.
- **Correct MCC** per merchant activity; some categories carry favorable rates.
- **Debit routing** (where applicable) to lower-cost networks.

## Chargeback lifecycle and reason-code families
Lifecycle (names vary by network): retrieval/inquiry (optional) → **first chargeback**
(provisional debit) → **representment** (merchant evidence) → **pre-arbitration / second
presentment** → **arbitration** (network decides; loser pays fees). Every stage has a short
response window set by brand rules — calendar them; a missed deadline is an automatic loss.

Reason-code families (each network numbers them differently, same taxonomy):
- **Fraud:** "card not present fraud," true-fraud claims. Evidence: AVS/CVV results, device/IP
  data, 3-D Secure results, delivery proof, prior undisputed history.
- **Consumer dispute:** goods/services not received, not as described, cancelled recurring,
  "credit not processed." Evidence: proof of delivery/service, refund policy shown at sale,
  cancellation logs.
- **Processing error:** duplicate processing, wrong amount, currency errors. Evidence: batch
  records; often better to accept and refund correctly.
- **Authorization:** no authorization / declined authorization forced through. Usually a
  process failure on the merchant side; fix the process.
Prevention beats representment: clear billing descriptors, prompt refunds, delivery
confirmation, and recurring-payment cancellation hygiene remove most non-fraud disputes.

## PCI-DSS: scope, storage rules, SAQ landscape, merchant levels
- **Scope:** the cardholder data environment (CDE) = all systems/people/processes that store,
  process, or transmit cardholder data, plus connected systems. Requirements apply to the CDE —
  so scope reduction is the master strategy: **outsource** (hosted/redirect pages), **P2PE**
  (validated point-to-point-encryption terminals), **tokenize** (post-auth references), and
  **segment** networks so card systems don't share flat networks with everything else.
- **Storage rules (stable across versions):** PAN storable only rendered unreadable within a
  validated environment; **sensitive authentication data (CVV/CVC, full track, PIN block) is
  never storable after authorization**, encrypted or not. Practically for treasury: no card
  numbers in spreadsheets, email, ticketing systems, scanned forms, or call recordings.
- **SAQ landscape (conceptual — confirm current criteria):** the Self-Assessment Questionnaire
  type follows the acceptance channel: fully outsourced e-commerce (redirect/iframe) → the
  shortest SAQ (historically "A"); partially outsourced web → A-EP; standalone dial/IP
  terminals → B family; P2PE-validated terminals → the P2PE SAQ; everything else / any
  electronic storage → the full SAQ D. Each department channel maps to a type; the institution
  may file multiple SAQs or one consolidated program — your acquirer/QSA decides the structure.
- **Merchant levels:** transaction volume per brand sets the level; higher levels require
  on-site assessment (ROC by a QSA) instead of self-assessment, plus quarterly ASV scans where
  external-facing systems are in scope. Confirm your level with your acquirer.
- **On compromise:** suspected card-data breach triggers acquirer notification, a PFI
  (forensic investigator), and potential brand fines — have the contact path written down.

## Governance artifacts worth keeping
- **MID inventory:** MID, department owner, channel, gateway, funding DDA, gross/net funding,
  batch cutoff, pricing model, SAQ type, last validation date.
- **Onboarding checklist** for new departmental acceptance (treasury sign-off, PCI scoping,
  GL/deposit mapping) and an offboarding step that actually closes the MID (dormant MIDs still
  bill monthly fees).
- **Annual fee review** per MID (effective-rate trend, downgrade root causes, markup
  benchmark) and a **chargeback log** by department and reason family.

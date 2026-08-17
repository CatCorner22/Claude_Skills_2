/**
 * Dental Notes Standardizer — Curve Hero vocabulary normalization engine.
 *
 * Translates free-form clinical notes from common dental PMS vocabulary into
 * Curve Hero's canonical terms so notes are consistent when imported into or
 * authored within Curve Hero.
 *
 * Curve Hero vocabulary reference (from MEMORY.md):
 *   Recare          ← recall, hygiene recall, maintenance recall
 *   Responsible Party / RP  ← guarantor, account holder, head of household
 *   Invoice         ← walkout, walkout statement, checkout receipt
 *   Carrier         ← insurance company, insurer, payer, plan carrier
 *   Operatory       ← op, treatment room, chair
 *   Sidekick        ← chairside assistant notes, assistant sidebar
 *   SnapShot        ← quick exam, snapshot exam
 *   Fee Guide       ← fee schedule, UCR fee, CDT fee table
 *   Days Owing      ← days outstanding, aging bucket, past-due days
 */

/** @typedef {{ from: RegExp; to: string; note: string }} Rule */

/** @type {Rule[]} */
export const RULES = [
  // Recare
  {
    from: /\bhygiene\s+recall\b/gi,
    to: 'Recare',
    note: 'Curve Hero uses "Recare" instead of "hygiene recall".',
  },
  {
    from: /\bmaintenance\s+recall\b/gi,
    to: 'Recare',
    note: 'Curve Hero uses "Recare" instead of "maintenance recall".',
  },
  {
    from: /\brecall\b/gi,
    to: 'Recare',
    note: 'Curve Hero uses "Recare" instead of "recall".',
  },

  // Responsible Party / RP
  {
    from: /\bguarantor\b/gi,
    to: 'Responsible Party (RP)',
    note: 'Curve Hero uses "Responsible Party" / "RP" instead of "guarantor".',
  },
  {
    from: /\baccount\s+holder\b/gi,
    to: 'Responsible Party (RP)',
    note: 'Curve Hero uses "Responsible Party" / "RP" instead of "account holder".',
  },
  {
    from: /\bhead\s+of\s+household\b/gi,
    to: 'Responsible Party (RP)',
    note: 'Curve Hero uses "Responsible Party" / "RP" instead of "head of household".',
  },

  // Invoice (checkout finalizes an Invoice, no "walkout")
  {
    from: /\bwalkout\s+statement\b/gi,
    to: 'Invoice',
    note: 'Curve Hero calls the checkout document an "Invoice", not "walkout statement".',
  },
  {
    from: /\bcheckout\s+receipt\b/gi,
    to: 'Invoice',
    note: 'Curve Hero calls the checkout document an "Invoice", not "checkout receipt".',
  },
  {
    from: /\bwalkout\b/gi,
    to: 'Invoice',
    note: 'Curve Hero calls the checkout document an "Invoice", not "walkout".',
  },

  // Carrier
  {
    from: /\binsurance\s+company\b/gi,
    to: 'Carrier',
    note: 'Curve Hero uses "Carrier" instead of "insurance company".',
  },
  {
    from: /\bplan\s+carrier\b/gi,
    to: 'Carrier',
    note: 'Curve Hero uses "Carrier" instead of "plan carrier".',
  },
  {
    from: /\bpayer\b/gi,
    to: 'Carrier',
    note: 'Curve Hero uses "Carrier" instead of "payer".',
  },
  {
    from: /\binsurer\b/gi,
    to: 'Carrier',
    note: 'Curve Hero uses "Carrier" instead of "insurer".',
  },

  // Operatory
  {
    from: /\btreatment\s+room\b/gi,
    to: 'Operatory',
    note: 'Curve Hero uses "Operatory" instead of "treatment room".',
  },
  {
    from: /\b(?<!\w)op(?!\w)\b/g,
    to: 'Operatory',
    note: 'Curve Hero uses "Operatory" for the chair/room abbreviation "op".',
  },

  // Fee Guide
  {
    from: /\bfee\s+schedule\b/gi,
    to: 'Fee Guide',
    note: 'Curve Hero uses "Fee Guide" instead of "fee schedule".',
  },
  {
    from: /\bUCR\s+fee\b/gi,
    to: 'Fee Guide',
    note: 'Curve Hero uses "Fee Guide" instead of "UCR fee".',
  },
  {
    from: /\bCDT\s+fee\s+table\b/gi,
    to: 'Fee Guide',
    note: 'Curve Hero uses "Fee Guide" instead of "CDT fee table".',
  },

  // Days Owing
  {
    from: /\bdays?\s+outstanding\b/gi,
    to: 'Days Owing',
    note: 'Curve Hero uses "Days Owing" instead of "days outstanding".',
  },
  {
    from: /\baging\s+bucket\b/gi,
    to: 'Days Owing',
    note: 'Curve Hero uses "Days Owing" instead of "aging bucket".',
  },
  {
    from: /\bpast[- ]due\s+days?\b/gi,
    to: 'Days Owing',
    note: 'Curve Hero uses "Days Owing" instead of "past-due days".',
  },
];

/**
 * @typedef  {Object} Replacement
 * @property {string} original  The matched text
 * @property {string} replacement The Curve Hero term applied
 * @property {string} note      Explanation
 * @property {number} index     Position in the original string
 */

/**
 * @typedef  {Object} StandardizeResult
 * @property {string}        output       Standardized note text
 * @property {Replacement[]} replacements List of substitutions made
 */

/**
 * Standardize a single dental note to Curve Hero vocabulary.
 * @param {string} input Raw clinical note text
 * @returns {StandardizeResult}
 */
export function standardize(input) {
  /** @type {Replacement[]} */
  const replacements = [];
  let output = input;
  let offset = 0; // tracks how position shifts as we replace

  // Process rules in order; collect each match before replacing so indices stay valid
  for (const rule of RULES) {
    // Reset lastIndex for global regexes
    rule.from.lastIndex = 0;

    const interim = output;
    let match;
    const localReplacements = [];

    rule.from.lastIndex = 0;
    while ((match = rule.from.exec(interim)) !== null) {
      localReplacements.push({
        original: match[0],
        replacement: rule.to,
        note: rule.note,
        index: match.index,
      });
    }

    if (localReplacements.length > 0) {
      output = interim.replace(rule.from, rule.to);
      replacements.push(...localReplacements);
    }

    rule.from.lastIndex = 0;
  }

  return { output, replacements };
}

/**
 * Standardize an array of notes.
 * @param {string[]} notes
 * @returns {StandardizeResult[]}
 */
export function standardizeAll(notes) {
  return notes.map(standardize);
}

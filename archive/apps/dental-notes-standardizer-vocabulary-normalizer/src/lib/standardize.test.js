/**
 * Unit tests for the Curve Hero vocabulary normalization engine.
 * Run with: npx vitest
 */
import { describe, it, expect } from 'vitest';
import { standardize, standardizeAll } from './standardize.js';

describe('standardize — Curve Hero vocabulary normalization', () => {
  it('replaces "recall" with "Recare"', () => {
    const { output } = standardize('Patient due for recall in 6 months.');
    expect(output).toContain('Recare');
    expect(output).not.toContain('recall');
  });

  it('replaces "hygiene recall" with "Recare"', () => {
    const { output } = standardize('Scheduled hygiene recall appointment.');
    expect(output).toContain('Recare');
  });

  it('replaces "guarantor" with "Responsible Party (RP)"', () => {
    const { output } = standardize('Discussed balance with guarantor.');
    expect(output).toContain('Responsible Party (RP)');
    expect(output).not.toMatch(/guarantor/i);
  });

  it('replaces "walkout" with "Invoice"', () => {
    const { output } = standardize('Printed walkout statement for patient.');
    expect(output).toContain('Invoice');
    expect(output).not.toMatch(/walkout/i);
  });

  it('replaces "insurance company" with "Carrier"', () => {
    const { output } = standardize('Verified benefits with insurance company.');
    expect(output).toContain('Carrier');
  });

  it('replaces "fee schedule" with "Fee Guide"', () => {
    const { output } = standardize('Reviewed fee schedule for crown.');
    expect(output).toContain('Fee Guide');
  });

  it('replaces "days outstanding" with "Days Owing"', () => {
    const { output } = standardize('Balance 90 days outstanding.');
    expect(output).toContain('Days Owing');
  });

  it('returns a replacements array documenting each change', () => {
    const { replacements } = standardize('Guarantor called re: recall.');
    expect(replacements.length).toBeGreaterThan(0);
    expect(replacements[0]).toHaveProperty('original');
    expect(replacements[0]).toHaveProperty('replacement');
    expect(replacements[0]).toHaveProperty('note');
  });

  it('does not alter text with no matching terms', () => {
    const clean = 'Patient presents with mild sensitivity on #14.';
    const { output, replacements } = standardize(clean);
    expect(output).toBe(clean);
    expect(replacements).toHaveLength(0);
  });

  it('standardizeAll processes multiple notes', () => {
    const results = standardizeAll(['Recall due.', 'Printed walkout.']);
    expect(results).toHaveLength(2);
    expect(results[0].output).toContain('Recare');
    expect(results[1].output).toContain('Invoice');
  });
});

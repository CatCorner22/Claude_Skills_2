import React, { useMemo } from 'react';
import { standardize } from '../lib/standardize.js';

/**
 * NotesStandardizer — two-panel UI: raw input on the left, standardized output
 * on the right, with a change log table below.
 */
export default function NotesStandardizer({ input, onInputChange }) {
  const { output, replacements } = useMemo(() => standardize(input), [input]);

  const unchanged = replacements.length === 0;

  return (
    <div>
      {/* Two-panel editor */}
      <div style={styles.panels}>
        <Panel label="Raw Notes (editable)">
          <textarea
            style={styles.textarea}
            value={input}
            onChange={(e) => onInputChange(e.target.value)}
            placeholder="Paste or type clinical notes here…"
            spellCheck
          />
        </Panel>

        <Panel
          label="Standardized Output"
          badge={unchanged ? null : `${replacements.length} substitution(s)`}
          badgeStyle={unchanged ? null : styles.badgeOrange}
        >
          <pre style={{ ...styles.textarea, ...styles.pre }}>{output}</pre>
        </Panel>
      </div>

      {/* Copy button */}
      <div style={styles.actions}>
        <button
          style={styles.copyBtn}
          onClick={() => navigator.clipboard.writeText(output)}
          title="Copy standardized output to clipboard"
        >
          Copy Output
        </button>
        {!unchanged && (
          <span style={styles.changedHint}>
            {replacements.length} Curve Hero term(s) applied
          </span>
        )}
        {unchanged && (
          <span style={styles.cleanHint}>✓ No non-standard terms found</span>
        )}
      </div>

      {/* Change log */}
      {!unchanged && (
        <section style={styles.logSection}>
          <h2 style={styles.logTitle}>Change Log</h2>
          <table style={styles.table}>
            <thead>
              <tr>
                <th style={styles.th}>#</th>
                <th style={styles.th}>Original term</th>
                <th style={styles.th}>Curve Hero term</th>
                <th style={styles.th}>Reason</th>
              </tr>
            </thead>
            <tbody>
              {replacements.map((r, i) => (
                <tr key={i} style={i % 2 === 0 ? styles.trEven : styles.trOdd}>
                  <td style={styles.td}>{i + 1}</td>
                  <td style={{ ...styles.td, ...styles.tdOriginal }}>{r.original}</td>
                  <td style={{ ...styles.td, ...styles.tdReplacement }}>{r.replacement}</td>
                  <td style={styles.td}>{r.note}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      )}
    </div>
  );
}

function Panel({ label, badge, badgeStyle, children }) {
  return (
    <div style={styles.panel}>
      <div style={styles.panelHeader}>
        <span style={styles.panelLabel}>{label}</span>
        {badge && <span style={{ ...styles.badge, ...badgeStyle }}>{badge}</span>}
      </div>
      {children}
    </div>
  );
}

const styles = {
  panels: {
    display: 'grid',
    gridTemplateColumns: '1fr 1fr',
    gap: '1rem',
  },
  panel: { display: 'flex', flexDirection: 'column', gap: '0.4rem' },
  panelHeader: { display: 'flex', alignItems: 'center', gap: '0.5rem' },
  panelLabel: { fontWeight: 600, fontSize: '0.85rem', color: '#1a5276' },
  badge: {
    fontSize: '0.72rem',
    padding: '0.1rem 0.4rem',
    borderRadius: 4,
    background: '#eaf0fb',
    color: '#1a5276',
  },
  badgeOrange: { background: '#fdf3e3', color: '#b7660a' },
  textarea: {
    width: '100%',
    minHeight: 220,
    boxSizing: 'border-box',
    padding: '0.75rem',
    border: '1px solid #ccc',
    borderRadius: 6,
    fontSize: '0.9rem',
    lineHeight: 1.6,
    resize: 'vertical',
    background: '#fafafa',
    fontFamily: 'inherit',
  },
  pre: {
    overflowX: 'auto',
    whiteSpace: 'pre-wrap',
    wordBreak: 'break-word',
    margin: 0,
    color: '#1a1a2e',
  },
  actions: {
    display: 'flex',
    alignItems: 'center',
    gap: '1rem',
    marginTop: '0.75rem',
  },
  copyBtn: {
    padding: '0.4rem 1rem',
    background: '#1a5276',
    color: '#fff',
    border: 'none',
    borderRadius: 5,
    cursor: 'pointer',
    fontSize: '0.85rem',
  },
  changedHint: { fontSize: '0.82rem', color: '#b7660a' },
  cleanHint: { fontSize: '0.82rem', color: '#1e8449' },
  logSection: { marginTop: '1.5rem' },
  logTitle: { fontSize: '1rem', color: '#1a5276', marginBottom: '0.5rem' },
  table: { width: '100%', borderCollapse: 'collapse', fontSize: '0.82rem' },
  th: {
    textAlign: 'left',
    padding: '0.4rem 0.6rem',
    background: '#eaf0fb',
    color: '#1a5276',
    border: '1px solid #d0ddf0',
  },
  td: { padding: '0.35rem 0.6rem', border: '1px solid #e0e0e0', verticalAlign: 'top' },
  trEven: { background: '#fff' },
  trOdd: { background: '#f7f9fc' },
  tdOriginal: { color: '#922b21', fontStyle: 'italic' },
  tdReplacement: { color: '#1e8449', fontWeight: 600 },
};

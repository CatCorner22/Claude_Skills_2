import React, { useState, useCallback } from 'react';
import NotesStandardizer from './components/NotesStandardizer.jsx';

const SAMPLE_NOTE =
  'Patient due for recall in 6 months. Discussed balance with guarantor. ' +
  'Verified benefits with insurance company — fee schedule updated. ' +
  'Printed walkout statement. Balance 45 days outstanding. Assigned to op 3.';

export default function App() {
  const [input, setInput] = useState(SAMPLE_NOTE);

  return (
    <div style={styles.container}>
      <header style={styles.header}>
        <h1 style={styles.title}>Dental Notes Standardizer</h1>
        <p style={styles.subtitle}>
          Curve Hero vocabulary — real-time normalization of clinical notes
        </p>
      </header>
      <main style={styles.main}>
        <NotesStandardizer input={input} onInputChange={setInput} />
      </main>
      <footer style={styles.footer}>
        Benchmarked against Curve Hero&apos;s canonical terminology &mdash; see{' '}
        <code>docs/curve-hero-benchmark.md</code>
      </footer>
    </div>
  );
}

const styles = {
  container: {
    fontFamily: "'Segoe UI', system-ui, sans-serif",
    maxWidth: 900,
    margin: '0 auto',
    padding: '1.5rem',
    color: '#1a1a2e',
  },
  header: {
    borderBottom: '2px solid #4a90d9',
    paddingBottom: '0.75rem',
    marginBottom: '1.5rem',
  },
  title: { margin: 0, fontSize: '1.6rem', color: '#1a5276' },
  subtitle: { margin: '0.25rem 0 0', fontSize: '0.9rem', color: '#555' },
  main: { minHeight: '60vh' },
  footer: {
    marginTop: '2rem',
    paddingTop: '0.75rem',
    borderTop: '1px solid #ddd',
    fontSize: '0.8rem',
    color: '#777',
  },
};

import { useState } from "react";

interface NoteOutputProps {
  noteText: string | null;
}

export function NoteOutput({ noteText }: NoteOutputProps) {
  const [copied, setCopied] = useState(false);

  if (!noteText) {
    return (
      <div className="flex h-full min-h-[200px] items-center justify-center rounded-lg border border-dashed border-slate-300 bg-slate-50 p-6 text-center">
        <p className="text-sm text-slate-500">
          Fill out a template and click Generate Note to preview standardized output here.
        </p>
      </div>
    );
  }

  const handleCopy = async () => {
    await navigator.clipboard.writeText(noteText);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="flex h-full flex-col rounded-lg border border-slate-200 bg-white">
      <div className="flex items-center justify-between border-b border-slate-100 px-4 py-2">
        <h3 className="text-sm font-semibold text-slate-700">Standardized Note Output</h3>
        <button
          type="button"
          onClick={handleCopy}
          className="rounded-md bg-slate-100 px-3 py-1 text-xs font-medium text-slate-700 hover:bg-slate-200"
        >
          {copied ? "Copied!" : "Copy to clipboard"}
        </button>
      </div>
      <pre className="flex-1 overflow-auto whitespace-pre-wrap p-4 font-mono text-sm leading-relaxed text-slate-800">
        {noteText}
      </pre>
    </div>
  );
}

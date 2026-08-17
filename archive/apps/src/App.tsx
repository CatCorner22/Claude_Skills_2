import { useState } from "react";
import type { NoteTemplate } from "./types/form";
import { TemplatePicker } from "./components/TemplatePicker";
import { FormEngine } from "./components/FormEngine/FormEngine";
import { NoteOutput } from "./components/NoteOutput";
import { recordRecent } from "./hooks/useFavorites";

export default function App() {
  const [selectedTemplate, setSelectedTemplate] = useState<NoteTemplate | null>(null);
  const [noteText, setNoteText] = useState<string | null>(null);

  const handleSelectTemplate = (template: NoteTemplate) => {
    setSelectedTemplate(template);
    setNoteText(null);
    recordRecent(template.id);
  };

  return (
    <div className="min-h-screen">
      <header className="border-b border-slate-200 bg-white px-6 py-4 shadow-sm">
        <h1 className="text-xl font-bold text-slate-900">Dental Notes Standardizer</h1>
        <p className="mt-0.5 text-sm text-slate-600">
          Structured clinical notes benchmarked against Curve Hero templated notes
        </p>
      </header>

      <div className="mx-auto grid max-w-7xl gap-6 p-6 lg:grid-cols-[280px_1fr_340px]">
        <aside className="lg:sticky lg:top-6 lg:self-start">
          <div className="rounded-lg border border-slate-200 bg-white p-4">
            <h2 className="mb-3 text-sm font-semibold text-slate-800">
              Visit Type Templates
            </h2>
            <TemplatePicker
              selectedId={selectedTemplate?.id ?? null}
              onSelect={handleSelectTemplate}
            />
          </div>
        </aside>

        <main>
          {selectedTemplate ? (
            <FormEngine
              key={selectedTemplate.id}
              template={selectedTemplate}
              onNoteGenerated={setNoteText}
            />
          ) : (
            <div className="flex min-h-[400px] items-center justify-center rounded-lg border border-dashed border-slate-300 bg-white p-8 text-center">
              <div>
                <p className="text-lg font-medium text-slate-700">
                  Select a visit type template
                </p>
                <p className="mt-1 text-sm text-slate-500">
                  Choose from Fillings, Crown, Hygiene, or Lab Case to begin documentation.
                </p>
              </div>
            </div>
          )}
        </main>

        <aside className="lg:sticky lg:top-6 lg:self-start">
          <NoteOutput noteText={noteText} />
        </aside>
      </div>
    </div>
  );
}

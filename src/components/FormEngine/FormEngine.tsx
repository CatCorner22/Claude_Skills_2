import { useCallback, useMemo, useState } from "react";
import type { FormValues, NoteTemplate } from "../../types/form";
import { getAllTemplateFields } from "../../utils/validateForm";
import {
  getInitialValues,
  getVisibleFields,
  validateForm,
} from "../../utils/validateForm";
import { generateNoteText } from "../../utils/generateNoteText";
import { FieldRenderer } from "./FieldRenderer";

interface FormEngineProps {
  template: NoteTemplate;
  onNoteGenerated: (text: string) => void;
}

export function FormEngine({ template, onNoteGenerated }: FormEngineProps) {
  const fields = useMemo(() => getAllTemplateFields(template), [template]);
  const [values, setValues] = useState<FormValues>(() => getInitialValues(fields));
  const [errors, setErrors] = useState<Set<string>>(new Set());
  const [submitted, setSubmitted] = useState(false);

  const visibleFields = useMemo(
    () => getVisibleFields(fields, values),
    [fields, values],
  );

  const handleChange = useCallback((fieldId: string, value: unknown) => {
    setValues((prev) => ({ ...prev, [fieldId]: value }));
    setErrors((prev) => {
      const next = new Set(prev);
      next.delete(fieldId);
      return next;
    });
  }, []);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const validationErrors = validateForm(fields, values);
    if (validationErrors.length > 0) {
      setErrors(new Set(validationErrors.map((err) => err.fieldId)));
      setSubmitted(true);
      return;
    }
    setErrors(new Set());
    setSubmitted(false);
    onNoteGenerated(generateNoteText(template.name, fields, values));
  };

  const handleReset = () => {
    setValues(getInitialValues(fields));
    setErrors(new Set());
    setSubmitted(false);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div
        className="rounded-t-lg px-4 py-3 text-white"
        style={{ backgroundColor: template.color }}
      >
        <h2 className="text-lg font-semibold">{template.name}</h2>
        <p className="text-sm opacity-90">{template.description}</p>
      </div>

      <div className="space-y-4 rounded-b-lg border border-t-0 border-slate-200 bg-white p-4">
        {visibleFields.map((field) => (
          <FieldRenderer
            key={field.id}
            field={field}
            values={values}
            errors={errors}
            onChange={handleChange}
          />
        ))}

        {submitted && errors.size > 0 && (
          <div className="rounded-md border border-red-200 bg-red-50 px-3 py-2 text-sm text-red-700">
            Complete all required fields (marked with *) before saving.
          </div>
        )}

        <div className="flex gap-3 border-t border-slate-100 pt-4">
          <button
            type="submit"
            className="rounded-md bg-blue-600 px-4 py-2 text-sm font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
          >
            Generate Note
          </button>
          <button
            type="button"
            onClick={handleReset}
            className="rounded-md border border-slate-300 bg-white px-4 py-2 text-sm font-medium text-slate-700 hover:bg-slate-50"
          >
            Reset
          </button>
        </div>
      </div>
    </form>
  );
}

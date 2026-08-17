import type { FormField, FormValues, RepeaterRowValues } from "../../types/form";
import { isRepeaterField } from "../../types/form";
import { RepeaterFieldComponent } from "./RepeaterField";

interface FieldRendererProps {
  field: FormField;
  values: FormValues;
  errors: Set<string>;
  onChange: (fieldId: string, value: unknown) => void;
}

function RequiredMark({ required }: { required?: boolean }) {
  if (!required) return null;
  return <span className="ml-0.5 text-red-500" aria-label="required">*</span>;
}

function FieldError({ fieldId, errors }: { fieldId: string; errors: Set<string> }) {
  if (!errors.has(fieldId) && ![...errors].some((e) => e.startsWith(`${fieldId}.`))) {
    return null;
  }
  return <p className="mt-1 text-xs text-red-600">Required</p>;
}

export function FieldRenderer({ field, values, errors, onChange }: FieldRendererProps) {
  const value = values[field.id];
  const hasError =
    errors.has(field.id) || [...errors].some((e) => e.startsWith(`${field.id}.`));

  if (field.type === "section-header") {
    return (
      <div className="border-b border-slate-200 pb-1 pt-4 first:pt-0">
        <h3 className="text-sm font-semibold uppercase tracking-wide text-slate-600">
          {field.label}
        </h3>
      </div>
    );
  }

  if (isRepeaterField(field)) {
    return (
      <RepeaterFieldComponent
        field={field}
        value={(value as RepeaterRowValues[] | undefined) ?? [{}]}
        errors={errors}
        onChange={(v) => onChange(field.id, v)}
      />
    );
  }

  const labelEl = (
    <label htmlFor={field.id} className="mb-1 block text-sm font-medium text-slate-700">
      {field.label}
      <RequiredMark required={field.required} />
    </label>
  );

  const inputClass = `w-full rounded-md border px-3 py-2 text-sm outline-none transition-colors ${
    hasError
      ? "border-red-400 bg-red-50 focus:border-red-500 focus:ring-1 focus:ring-red-500"
      : "border-slate-300 bg-white focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
  }`;

  switch (field.type) {
    case "short-answer":
    case "site":
      return (
        <div>
          {labelEl}
          <input
            id={field.id}
            type="text"
            className={inputClass}
            value={(value as string) ?? ""}
            onChange={(e) => onChange(field.id, e.target.value)}
            placeholder={field.type === "site" ? "e.g. #14 MO" : undefined}
          />
          <FieldError fieldId={field.id} errors={errors} />
        </div>
      );

    case "text-box":
      return (
        <div>
          {labelEl}
          <textarea
            id={field.id}
            rows={3}
            className={inputClass}
            value={(value as string) ?? ""}
            onChange={(e) => onChange(field.id, e.target.value)}
          />
          <FieldError fieldId={field.id} errors={errors} />
        </div>
      );

    case "dropdown":
    case "material":
    case "radiographs":
    case "diagnosis-reason": {
      const opts = "options" in field ? field.options : [];
      return (
        <div>
          {labelEl}
          <select
            id={field.id}
            className={inputClass}
            value={(value as string) ?? ""}
            onChange={(e) => onChange(field.id, e.target.value)}
          >
            <option value="">— Select —</option>
            {opts.map((opt) => (
              <option key={opt} value={opt}>{opt}</option>
            ))}
          </select>
          <FieldError fieldId={field.id} errors={errors} />
        </div>
      );
    }

    case "select-boxes":
    case "checkbox": {
      const opts = "options" in field ? field.options : [];
      const selected = (value as string[]) ?? [];
      return (
        <div>
          {labelEl}
          <div className={`space-y-1.5 rounded-md border p-3 ${hasError ? "border-red-400 bg-red-50" : "border-slate-200 bg-slate-50"}`}>
            {opts.map((opt) => (
              <label key={opt} className="flex cursor-pointer items-center gap-2 text-sm">
                <input
                  type="checkbox"
                  checked={selected.includes(opt)}
                  onChange={(e) => {
                    const next = e.target.checked
                      ? [...selected, opt]
                      : selected.filter((s) => s !== opt);
                    onChange(field.id, next);
                  }}
                  className="rounded border-slate-300 text-blue-600 focus:ring-blue-500"
                />
                {opt}
              </label>
            ))}
          </div>
          <FieldError fieldId={field.id} errors={errors} />
        </div>
      );
    }

    case "yes-no":
      return (
        <div>
          {labelEl}
          <div className={`flex gap-4 rounded-md border p-3 ${hasError ? "border-red-400 bg-red-50" : "border-slate-200 bg-slate-50"}`}>
            {(["Yes", "No"] as const).map((opt) => (
              <label key={opt} className="flex cursor-pointer items-center gap-2 text-sm">
                <input
                  type="radio"
                  name={field.id}
                  value={opt}
                  checked={(value as string) === opt}
                  onChange={() => onChange(field.id, opt)}
                  className="border-slate-300 text-blue-600 focus:ring-blue-500"
                />
                {opt}
              </label>
            ))}
          </div>
          <FieldError fieldId={field.id} errors={errors} />
        </div>
      );

    case "scale-4":
      return (
        <div>
          {labelEl}
          <div className={`flex flex-wrap gap-2 ${hasError ? "rounded-md border border-red-400 bg-red-50 p-2" : ""}`}>
            {(["Excellent", "Good", "Fair", "Poor"] as const).map((opt) => (
              <button
                key={opt}
                type="button"
                onClick={() => onChange(field.id, opt)}
                className={`rounded-full px-3 py-1 text-sm font-medium transition-colors ${
                  value === opt
                    ? "bg-blue-600 text-white"
                    : "bg-slate-100 text-slate-700 hover:bg-slate-200"
                }`}
              >
                {opt}
              </button>
            ))}
          </div>
          <FieldError fieldId={field.id} errors={errors} />
        </div>
      );

    case "scale-3":
      return (
        <div>
          {labelEl}
          <div className={`flex flex-wrap gap-2 ${hasError ? "rounded-md border border-red-400 bg-red-50 p-2" : ""}`}>
            {(["Mild", "Moderate", "Severe"] as const).map((opt) => (
              <button
                key={opt}
                type="button"
                onClick={() => onChange(field.id, opt)}
                className={`rounded-full px-3 py-1 text-sm font-medium transition-colors ${
                  value === opt
                    ? "bg-blue-600 text-white"
                    : "bg-slate-100 text-slate-700 hover:bg-slate-200"
                }`}
              >
                {opt}
              </button>
            ))}
          </div>
          <FieldError fieldId={field.id} errors={errors} />
        </div>
      );

    case "distribution": {
      const opts = "options" in field ? field.options : ["Generalized", "Localized", "No bleeding"];
      return (
        <div>
          {labelEl}
          <div className={`flex flex-wrap gap-2 ${hasError ? "rounded-md border border-red-400 bg-red-50 p-2" : ""}`}>
            {opts.map((opt) => (
              <button
                key={opt}
                type="button"
                onClick={() => onChange(field.id, opt)}
                className={`rounded-full px-3 py-1 text-sm font-medium transition-colors ${
                  value === opt
                    ? "bg-blue-600 text-white"
                    : "bg-slate-100 text-slate-700 hover:bg-slate-200"
                }`}
              >
                {opt}
              </button>
            ))}
          </div>
          <FieldError fieldId={field.id} errors={errors} />
        </div>
      );
    }

    default:
      return null;
  }
}

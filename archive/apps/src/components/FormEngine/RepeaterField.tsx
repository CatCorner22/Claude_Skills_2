import type { RepeaterField, RepeaterRowValues } from "../../types/form";
import { FieldRenderer } from "./FieldRenderer";

interface RepeaterFieldProps {
  field: RepeaterField;
  value: RepeaterRowValues[];
  errors: Set<string>;
  onChange: (value: RepeaterRowValues[]) => void;
}

export function RepeaterFieldComponent({
  field,
  value,
  errors,
  onChange,
}: RepeaterFieldProps) {
  const rows = value.length > 0 ? value : [{}];

  const updateRow = (index: number, subFieldId: string, subValue: string | string[]) => {
    const next = rows.map((row, i) =>
      i === index ? { ...row, [subFieldId]: subValue } : row,
    );
    onChange(next);
  };

  const addRow = () => onChange([...rows, {}]);

  const removeRow = (index: number) => {
    if (rows.length <= 1) {
      onChange([{}]);
      return;
    }
    onChange(rows.filter((_, i) => i !== index));
  };

  const hasError =
    errors.has(field.id) || [...errors].some((e) => e.startsWith(`${field.id}.`));

  return (
    <div>
      <div className="mb-2 flex items-center justify-between">
        <span className="text-sm font-medium text-slate-700">
          {field.repeaterLabel}
          {field.required && (
            <span className="ml-0.5 text-red-500" aria-label="required">*</span>
          )}
        </span>
        <button
          type="button"
          onClick={addRow}
          className="rounded-md bg-blue-50 px-2 py-1 text-xs font-medium text-blue-700 hover:bg-blue-100"
        >
          + Add entry
        </button>
      </div>

      <div className={`space-y-3 ${hasError ? "rounded-md border border-red-400 p-2" : ""}`}>
        {rows.map((row, index) => (
          <div
            key={index}
            className="relative rounded-lg border border-slate-200 bg-slate-50 p-3"
          >
            <div className="mb-2 flex items-center justify-between">
              <span className="text-xs font-semibold text-slate-500">
                Entry {index + 1}
              </span>
              {rows.length > 1 && (
                <button
                  type="button"
                  onClick={() => removeRow(index)}
                  className="text-xs text-red-600 hover:text-red-800"
                >
                  Remove
                </button>
              )}
            </div>
            <div className="space-y-3">
              {field.fields.map((subField) => (
                <FieldRenderer
                  key={`${index}-${subField.id}`}
                  field={{ ...subField, id: `${field.id}.${index}.${subField.id}` }}
                  values={{
                    [`${field.id}.${index}.${subField.id}`]: row[subField.id] ?? "",
                  }}
                  errors={errors}
                  onChange={(_, v) => updateRow(index, subField.id, v as string | string[])}
                />
              ))}
            </div>
          </div>
        ))}
      </div>
      {hasError && (
        <p className="mt-1 text-xs text-red-600">
          {errors.has(field.id) ? "At least one complete entry is required" : "Complete all required fields in each entry"}
        </p>
      )}
    </div>
  );
}

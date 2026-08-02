import type { FormField, FormValues, RepeaterField, RepeaterRowValues } from "../types/form";
import { isRepeaterField } from "../types/form";
import { getVisibleFields } from "./validateForm";

function formatValue(value: unknown): string {
  if (value === undefined || value === null || value === "") return "";
  if (Array.isArray(value)) {
    if (value.length === 0) return "";
    if (typeof value[0] === "object") return "";
    return value.join(", ");
  }
  return String(value);
}

function formatRepeaterRows(
  field: RepeaterField,
  rows: RepeaterRowValues[],
): string {
  return rows
    .map((row, i) => {
      const parts = field.fields
        .map((sub) => {
          const v = formatValue(row[sub.id]);
          return v ? `${sub.label}: ${v}` : null;
        })
        .filter(Boolean);
      if (parts.length === 0) return null;
      return `  ${i + 1}. ${parts.join("; ")}`;
    })
    .filter(Boolean)
    .join("\n");
}

export function generateNoteText(
  templateName: string,
  fields: FormField[],
  values: FormValues,
): string {
  const lines: string[] = [`${templateName.toUpperCase()} — CLINICAL NOTE`, ""];

  const visible = getVisibleFields(fields, values);
  let currentSection = "";

  for (const field of visible) {
    if (field.type === "section-header") {
      currentSection = field.label;
      lines.push(`• ${field.label}`);
      lines.push("");
      continue;
    }

    if (isRepeaterField(field)) {
      const rows = (values[field.id] as RepeaterRowValues[] | undefined) ?? [];
      const formatted = formatRepeaterRows(field, rows);
      if (formatted) {
        const prefix = currentSection ? "  " : "";
        lines.push(`${prefix}${field.repeaterLabel}:`);
        lines.push(formatted);
        lines.push("");
      }
      continue;
    }

    const value = formatValue(values[field.id]);
    if (!value) continue;

    const prefix = currentSection ? "  " : "";
    lines.push(`${prefix}${field.label}: ${value}`);
  }

  lines.push("");
  lines.push(`— Generated ${new Date().toLocaleString()}`);
  return lines.join("\n").trim();
}

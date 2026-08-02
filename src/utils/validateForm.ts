import type {
  ConditionalRule,
  FormField,
  FormValues,
  RepeaterField,
  RepeaterRowValues,
  ValidationError,
} from "../types/form";
import { isRepeaterField } from "../types/form";
import { resolveTemplateFields } from "../data/reusableBlocks";
import type { NoteTemplate } from "../types/form";

export function isFieldVisible(
  conditional: ConditionalRule | undefined,
  values: FormValues,
): boolean {
  if (!conditional) return true;
  const triggerValue = values[conditional.whenFieldId];
  if (Array.isArray(triggerValue)) {
    return triggerValue.includes(conditional.hasValue);
  }
  return String(triggerValue ?? "") === conditional.hasValue;
}

export function getVisibleFields(
  fields: FormField[],
  values: FormValues,
): FormField[] {
  return fields.filter((f) => isFieldVisible(f.conditional, values));
}

export function getAllTemplateFields(template: NoteTemplate): FormField[] {
  return resolveTemplateFields(template.reusableBlockIds, template.fields);
}

function isEmpty(value: unknown): boolean {
  if (value === undefined || value === null || value === "") return true;
  if (Array.isArray(value)) return value.length === 0;
  if (typeof value === "object") {
    const rows = value as RepeaterRowValues[];
    return rows.length === 0 || rows.every((row) =>
      Object.values(row).every((v) =>
        Array.isArray(v) ? v.length === 0 : !v,
      ),
    );
  }
  return false;
}

function validateRepeater(
  field: RepeaterField,
  values: FormValues,
  errors: ValidationError[],
): void {
  const rows = (values[field.id] as RepeaterRowValues[] | undefined) ?? [];
  if (field.required && rows.length === 0) {
    errors.push({
      fieldId: field.id,
      label: field.repeaterLabel,
      message: "At least one entry is required",
    });
    return;
  }
  for (let i = 0; i < rows.length; i++) {
    for (const subField of field.fields) {
      if (!subField.required) continue;
      const val = rows[i][subField.id];
      if (isEmpty(val)) {
        errors.push({
          fieldId: `${field.id}.${i}.${subField.id}`,
          label: `${field.repeaterLabel} — row ${i + 1}: ${subField.label}`,
          message: "Required",
        });
      }
    }
  }
}

export function validateForm(
  fields: FormField[],
  values: FormValues,
): ValidationError[] {
  const errors: ValidationError[] = [];
  const visible = getVisibleFields(fields, values);

  for (const field of visible) {
    if (field.type === "section-header") continue;

    if (isRepeaterField(field)) {
      validateRepeater(field, values, errors);
      continue;
    }

    if (!field.required) continue;
    const value = values[field.id];
    if (isEmpty(value)) {
      errors.push({
        fieldId: field.id,
        label: field.label,
        message: "Required",
      });
    }
  }

  return errors;
}

export function getInitialValues(fields: FormField[]): FormValues {
  const values: FormValues = {};
  for (const field of fields) {
    if (field.type === "section-header") continue;
    if (isRepeaterField(field)) {
      values[field.id] = [{}];
      continue;
    }
    if (field.type === "select-boxes" || field.type === "checkbox") {
      values[field.id] = [];
      continue;
    }
    if (field.type === "yes-no") {
      values[field.id] = "";
      continue;
    }
    values[field.id] = "";
  }
  return values;
}

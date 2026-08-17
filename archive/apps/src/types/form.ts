/** Field component types mirroring Curve Forms Tool Box */
export type FieldType =
  | "section-header"
  | "short-answer"
  | "text-box"
  | "dropdown"
  | "select-boxes"
  | "checkbox"
  | "yes-no"
  | "material"
  | "radiographs"
  | "diagnosis-reason"
  | "scale-4"
  | "scale-3"
  | "distribution"
  | "site"
  | "repeater";

export interface ConditionalRule {
  whenFieldId: string;
  hasValue: string;
}

export interface BaseField {
  id: string;
  type: FieldType;
  label: string;
  required?: boolean;
  conditional?: ConditionalRule;
}

export interface OptionField extends BaseField {
  options: string[];
}

export interface RepeaterField extends BaseField {
  type: "repeater";
  repeaterLabel: string;
  fields: FormField[];
}

export type FormField =
  | BaseField
  | OptionField
  | RepeaterField;

export function isRepeaterField(field: FormField): field is RepeaterField {
  return field.type === "repeater";
}

export function hasOptions(
  field: FormField,
): field is OptionField {
  return "options" in field && Array.isArray(field.options);
}

export interface ReusableBlock {
  id: string;
  name: string;
  description: string;
  fields: FormField[];
}

export interface NoteTemplate {
  id: string;
  name: string;
  category: string;
  color: string;
  description: string;
  /** IDs of reusable blocks to prepend */
  reusableBlockIds: string[];
  /** Procedure-specific fields */
  fields: FormField[];
}

export type FormValues = Record<string, unknown>;

export interface RepeaterRowValues {
  [fieldId: string]: string | string[];
}

export interface ValidationError {
  fieldId: string;
  label: string;
  message: string;
}

import type { NoteTemplate } from "../types/form";
import {
  crownsTemplate,
  fillingsTemplate,
  hygieneTemplate,
  labCaseTemplate,
} from "./templates/procedureTemplates";

export const allTemplates: NoteTemplate[] = [
  fillingsTemplate,
  crownsTemplate,
  hygieneTemplate,
  labCaseTemplate,
];

export function getTemplateById(id: string): NoteTemplate | undefined {
  return allTemplates.find((t) => t.id === id);
}

export const templateCategories = [
  ...new Set(allTemplates.map((t) => t.category)),
];

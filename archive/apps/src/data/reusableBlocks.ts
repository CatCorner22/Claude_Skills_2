import type { ReusableBlock } from "../types/form";

export const reusableBlocks: ReusableBlock[] = [
  {
    id: "anesthesia",
    name: "Administered Anesthesia",
    description: "Cross-template anesthesia documentation",
    fields: [
      {
        id: "topical-anesthesia",
        type: "dropdown",
        label: "Topical anesthesia",
        options: ["Benzocaine", "Cetacaine", "None"],
      },
      {
        id: "local-anesthesia-injected",
        type: "select-boxes",
        label: "Local anesthesia injected",
        options: ["Septocaine", "Lidocaine", "Mepivacaine", "Bupivacaine", "None"],
      },
      {
        id: "anesthesia-additional-notes",
        type: "short-answer",
        label: "Additional notes and reactions",
      },
    ],
  },
  {
    id: "provider",
    name: "Provider(s)",
    description: "Treating doctor and hygienist selection",
    fields: [
      {
        id: "providers-for-procedures",
        type: "select-boxes",
        label: "Provider(s) for procedures",
        required: true,
        options: ["Dr. Smith", "Dr. Johnson", "Dr. Williams", "Dr. Davis"],
      },
      {
        id: "hygienist-provider",
        type: "select-boxes",
        label: "Hygienist provider",
        options: ["Sarah H.", "Maria L.", "James K.", "N/A"],
      },
    ],
  },
  {
    id: "patient-behavior",
    name: "Patient Behavior",
    description: "Patient cooperation during appointment",
    fields: [
      {
        id: "patient-behavior-rating",
        type: "dropdown",
        label: "Patient behavior / experience",
        required: true,
        options: [
          "Cooperative",
          "Mildly anxious — tolerated well",
          "Moderately anxious — required reassurance",
          "Difficult — required additional management",
          "Pediatric — parent assisted",
        ],
      },
      {
        id: "behavior-additional-notes",
        type: "short-answer",
        label: "Behavior notes",
        conditional: {
          whenFieldId: "patient-behavior-rating",
          hasValue: "Difficult — required additional management",
        },
      },
    ],
  },
];

export function getReusableBlock(id: string): ReusableBlock | undefined {
  return reusableBlocks.find((b) => b.id === id);
}

export function resolveTemplateFields(
  reusableBlockIds: string[],
  procedureFields: ReusableBlock["fields"],
): ReusableBlock["fields"] {
  const blockFields = reusableBlockIds.flatMap(
    (id) => getReusableBlock(id)?.fields ?? [],
  );
  return [...blockFields, ...procedureFields];
}

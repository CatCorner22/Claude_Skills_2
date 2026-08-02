import type { NoteTemplate } from "../../types/form";

export const fillingsTemplate: NoteTemplate = {
  id: "fillings",
  name: "Fillings",
  category: "Restorative",
  color: "#3B82F6",
  description: "Composite or amalgam restorations — multi-tooth supported",
  reusableBlockIds: ["anesthesia", "provider", "patient-behavior"],
  fields: [
    {
      id: "fillings-section",
      type: "section-header",
      label: "Restorations Performed",
    },
    {
      id: "filling-entries",
      type: "repeater",
      label: "Filling entries",
      repeaterLabel: "Filling information",
      required: true,
      fields: [
        { id: "filling-site", type: "site", label: "Site", required: true },
        {
          id: "filling-material",
          type: "dropdown",
          label: "Material",
          required: true,
          options: ["Composite", "Amalgam", "Glass ionomer", "Resin modified GIC"],
        },
        {
          id: "filling-surface",
          type: "short-answer",
          label: "Surface(s)",
          required: true,
        },
      ],
    },
    {
      id: "fillings-additional-notes",
      type: "text-box",
      label: "Additional notes",
    },
  ],
};

export const crownsTemplate: NoteTemplate = {
  id: "crowns",
  name: "Crown Prep / Delivery",
  category: "Restorative",
  color: "#8B5CF6",
  description: "Crown preparation or delivery documentation",
  reusableBlockIds: ["anesthesia", "provider", "patient-behavior"],
  fields: [
    {
      id: "crowns-section",
      type: "section-header",
      label: "Crown Procedure",
    },
    {
      id: "crown-sites",
      type: "short-answer",
      label: "Site(s)",
      required: true,
    },
    {
      id: "build-up-done",
      type: "yes-no",
      label: "Build up done?",
      required: true,
    },
    {
      id: "crown-material",
      type: "material",
      label: "Material",
      required: true,
      options: [
        "PFM",
        "Full cast gold",
        "Zirconia",
        "E.max",
        "Porcelain",
        "Stainless steel (pedo)",
      ],
    },
    {
      id: "crown-radiographs",
      type: "radiographs",
      label: "Radiographs",
      options: ["PA", "FMX", "Periapical", "BW", "None"],
    },
    {
      id: "crown-replacement",
      type: "yes-no",
      label: "Replacement?",
      required: true,
    },
    {
      id: "crown-diagnosis-reason",
      type: "diagnosis-reason",
      label: "Diagnosis reason",
      required: true,
      options: [
        "Carious lesion",
        "Fractured tooth",
        "Failed restoration",
        "Endodontically treated tooth",
        "Esthetics",
        "Cracked tooth syndrome",
      ],
    },
    {
      id: "original-placement-date",
      type: "short-answer",
      label: "Original placement date",
      conditional: { whenFieldId: "crown-replacement", hasValue: "Yes" },
    },
    {
      id: "crowns-additional-notes",
      type: "text-box",
      label: "Additional notes",
    },
  ],
};

export const hygieneTemplate: NoteTemplate = {
  id: "hygiene",
  name: "Hygiene / Recare",
  category: "Preventive",
  color: "#10B981",
  description: "Adult or child prophy and periodontal screening",
  reusableBlockIds: ["provider"],
  fields: [
    {
      id: "hygiene-section",
      type: "section-header",
      label: "Hygiene Visit",
    },
    {
      id: "hygiene-performed",
      type: "dropdown",
      label: "Performed",
      required: true,
      options: ["Adult prophy", "Child prophy", "Periodontal maintenance", "Debridement"],
    },
    {
      id: "home-care",
      type: "scale-4",
      label: "Home care",
      required: true,
    },
    {
      id: "hygiene-radiographs",
      type: "radiographs",
      label: "Radiographs",
      options: ["PA", "FMX", "Periapical", "BW", "None"],
    },
    {
      id: "hygiene-radiograph-sites",
      type: "short-answer",
      label: "Site(s)",
      conditional: { whenFieldId: "hygiene-radiographs", hasValue: "Periapical" },
    },
    {
      id: "calculus",
      type: "scale-3",
      label: "Calculus",
      required: true,
    },
    {
      id: "bleeding-gums",
      type: "distribution",
      label: "Does the patient have bleeding gums?",
      required: true,
      options: ["Generalized", "Localized", "No bleeding"],
    },
    {
      id: "hygiene-additional-notes",
      type: "text-box",
      label: "Additional notes",
    },
  ],
};

export const labCaseTemplate: NoteTemplate = {
  id: "lab-case",
  name: "Lab Case Slip",
  category: "Lab",
  color: "#F59E0B",
  description: "Crown lab tracking — extensible to dentures, retainers, bridges",
  reusableBlockIds: ["provider"],
  fields: [
    {
      id: "lab-section",
      type: "section-header",
      label: "Lab Case Information",
    },
    {
      id: "lab-sent-to",
      type: "dropdown",
      label: "Lab where case was sent",
      required: true,
      options: ["ABC Dental Lab", "Premier Lab", "In-house", "Other"],
    },
    {
      id: "lab-name-other",
      type: "short-answer",
      label: "Lab name",
      conditional: { whenFieldId: "lab-sent-to", hasValue: "Other" },
    },
    {
      id: "crown-information",
      type: "repeater",
      label: "Crown entries",
      repeaterLabel: "Crown information",
      required: true,
      fields: [
        { id: "lab-crown-site", type: "site", label: "Site", required: true },
        { id: "lab-crown-shade", type: "short-answer", label: "Shade", required: true },
      ],
    },
    {
      id: "lab-material",
      type: "material",
      label: "Material",
      required: true,
      options: ["PFM", "Zirconia", "E.max", "Full cast gold", "Porcelain"],
    },
    {
      id: "lab-due-date",
      type: "short-answer",
      label: "Due date and time",
      required: true,
    },
    {
      id: "lab-additional-notes",
      type: "text-box",
      label: "Additional notes",
    },
  ],
};

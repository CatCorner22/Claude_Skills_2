import { useMemo, useState } from "react";
import type { NoteTemplate } from "../types/form";
import { allTemplates } from "../data/templates";
import { getFavorites, getRecent, toggleFavorite } from "../hooks/useFavorites";

interface TemplatePickerProps {
  selectedId: string | null;
  onSelect: (template: NoteTemplate) => void;
}

export function TemplatePicker({ selectedId, onSelect }: TemplatePickerProps) {
  const [favorites, setFavorites] = useState<string[]>(() => getFavorites());
  const [recent] = useState<string[]>(() => getRecent());
  const [categoryFilter, setCategoryFilter] = useState<string>("all");

  const categories = useMemo(
    () => ["all", ...new Set(allTemplates.map((t) => t.category))],
    [],
  );

  const favoriteTemplates = useMemo(
    () => allTemplates.filter((t) => favorites.includes(t.id)),
    [favorites],
  );

  const recentTemplates = useMemo(
    () =>
      recent
        .map((id) => allTemplates.find((t) => t.id === id))
        .filter((t): t is NoteTemplate => t !== undefined),
    [recent],
  );

  const filteredTemplates = useMemo(() => {
    if (categoryFilter === "all") return allTemplates;
    return allTemplates.filter((t) => t.category === categoryFilter);
  }, [categoryFilter]);

  const handleFavorite = (e: React.MouseEvent, templateId: string) => {
    e.stopPropagation();
    setFavorites(toggleFavorite(templateId));
  };

  const renderCard = (template: NoteTemplate) => {
    const isSelected = selectedId === template.id;
    const isFavorite = favorites.includes(template.id);

    return (
      <button
        key={template.id}
        type="button"
        onClick={() => onSelect(template)}
        className={`group relative w-full rounded-lg border p-3 text-left transition-all ${
          isSelected
            ? "border-blue-500 bg-blue-50 ring-2 ring-blue-500"
            : "border-slate-200 bg-white hover:border-slate-300 hover:shadow-sm"
        }`}
      >
        <div className="flex items-start gap-3">
          <div
            className="mt-0.5 h-4 w-4 shrink-0 rounded-full"
            style={{ backgroundColor: template.color }}
            aria-hidden
          />
          <div className="min-w-0 flex-1">
            <div className="flex items-center justify-between gap-2">
              <span className="font-medium text-slate-900">{template.name}</span>
              <button
                type="button"
                onClick={(e) => handleFavorite(e, template.id)}
                className="shrink-0 text-lg leading-none opacity-60 hover:opacity-100"
                aria-label={isFavorite ? "Remove from favorites" : "Add to favorites"}
                title={isFavorite ? "Remove from favorites" : "Add to favorites"}
              >
                {isFavorite ? "★" : "☆"}
              </button>
            </div>
            <p className="mt-0.5 text-xs text-slate-500">{template.category}</p>
            <p className="mt-1 line-clamp-2 text-xs text-slate-600">
              {template.description}
            </p>
          </div>
        </div>
      </button>
    );
  };

  return (
    <div className="space-y-4">
      {favoriteTemplates.length > 0 && (
        <section>
          <h2 className="mb-2 text-xs font-semibold uppercase tracking-wide text-slate-500">
            Favorites
          </h2>
          <div className="space-y-2">{favoriteTemplates.map(renderCard)}</div>
        </section>
      )}

      {recentTemplates.length > 0 && (
        <section>
          <h2 className="mb-2 text-xs font-semibold uppercase tracking-wide text-slate-500">
            Recently Used
          </h2>
          <div className="space-y-2">{recentTemplates.map(renderCard)}</div>
        </section>
      )}

      <section>
        <div className="mb-2 flex items-center justify-between">
          <h2 className="text-xs font-semibold uppercase tracking-wide text-slate-500">
            All Templates
          </h2>
          <select
            value={categoryFilter}
            onChange={(e) => setCategoryFilter(e.target.value)}
            className="rounded border border-slate-300 bg-white px-2 py-0.5 text-xs text-slate-700"
            aria-label="Filter by category"
          >
            {categories.map((cat) => (
              <option key={cat} value={cat}>
                {cat === "all" ? "All categories" : cat}
              </option>
            ))}
          </select>
        </div>
        <div className="space-y-2">{filteredTemplates.map(renderCard)}</div>
      </section>
    </div>
  );
}

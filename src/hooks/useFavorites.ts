const FAVORITES_KEY = "dental-notes-favorites";
const RECENT_KEY = "dental-notes-recent";

export function getFavorites(): string[] {
  try {
    const raw = localStorage.getItem(FAVORITES_KEY);
    return raw ? (JSON.parse(raw) as string[]) : [];
  } catch {
    return [];
  }
}

export function toggleFavorite(templateId: string): string[] {
  const current = getFavorites();
  const next = current.includes(templateId)
    ? current.filter((id) => id !== templateId)
    : [...current, templateId];
  localStorage.setItem(FAVORITES_KEY, JSON.stringify(next));
  return next;
}

export function getRecent(): string[] {
  try {
    const raw = localStorage.getItem(RECENT_KEY);
    return raw ? (JSON.parse(raw) as string[]) : [];
  } catch {
    return [];
  }
}

export function recordRecent(templateId: string): string[] {
  const current = getRecent().filter((id) => id !== templateId);
  const next = [templateId, ...current].slice(0, 5);
  localStorage.setItem(RECENT_KEY, JSON.stringify(next));
  return next;
}

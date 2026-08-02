# Frontend recipes (reference)

## Contents
- htmx fragment patterns
- TanStack Query setup
- API layer template
- Component checklist

## htmx fragment patterns
```html
<!-- live search: input triggers GET, server returns an HTML fragment, htmx swaps it -->
<input name="q" hx-get="/invoices/search" hx-trigger="input changed delay:300ms"
       hx-target="#results">
<div id="results">{% include "invoices/_table.html" %}</div>

<!-- inline edit: row swaps itself for a form, form swaps back on save -->
<tr hx-get="/invoices/42/edit" hx-target="this" hx-swap="outerHTML">...</tr>
```
Server side: the same route renders the full page (normal request) or just the fragment
(`HX-Request` header) — one template, included both ways. Pattern covers search, pagination,
inline edit, modals, infinite scroll; when a page needs client-held state across many
interactions, that page has outgrown htmx — make it the React island.

## TanStack Query setup
```tsx
const qc = new QueryClient({ defaultOptions: { queries: { staleTime: 30_000 } } });
// <QueryClientProvider client={qc}> at the root

function Invoices() {
  const { data, isPending, error } = useQuery({ queryKey: ["invoices"], queryFn: getInvoices });
  const create = useMutation({
    mutationFn: postInvoice,
    onSuccess: () => qc.invalidateQueries({ queryKey: ["invoices"] }),
  });
  if (isPending) return <Spinner />;
  if (error) return <ErrorBox error={error} />;
  return <InvoiceTable rows={data.items} onCreate={create.mutate} />;
}
```
Keys are the cache's address space: `["invoices"]` for the list, `["invoices", id]` for one.
Invalidate on mutation; don't hand-update copies.

## API layer template
```ts
// api.ts — the only file that knows fetch
const base = import.meta.env.VITE_API_URL ?? "";

async function req<T>(path: string, init?: RequestInit): Promise<T> {
  const r = await fetch(base + path, {
    headers: { "Content-Type": "application/json", ...authHeader() },
    ...init,
  });
  if (!r.ok) throw new ApiError(r.status, (await r.json()).detail ?? r.statusText);
  return r.json();
}

export const getInvoices = () => req<Page<Invoice>>("/invoices");
export const postInvoice = (d: InvoiceIn) => req<Invoice>("/invoices", { method: "POST", body: JSON.stringify(d) });
```
Types: generate from the backend OpenAPI schema (`openapi-typescript`) or mirror by hand for
small APIs — either way the contract lives in one checked place.

## Component checklist
- [ ] Lives in its feature folder; imports flow feature → shared, never feature → feature internals
- [ ] Server data via useQuery; no server data in useState
- [ ] UI state in the lowest component that owns it
- [ ] Semantic elements; inputs labeled; keyboard reachable; focus visible
- [ ] Loading and error states rendered (the query gives them — use them)
- [ ] No raw fetch; API layer functions only
- [ ] Would this be less code as a server-rendered fragment? (If yes — why is it React?)

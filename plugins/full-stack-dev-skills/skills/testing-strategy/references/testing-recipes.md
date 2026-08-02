# Testing recipes (reference)

## Contents
- conftest spine
- Factory helpers
- Level-decision table
- Playwright skeleton
- External-boundary mocks

## conftest spine
```python
# conftest.py
@pytest.fixture(scope="session")
def engine():
    eng = create_engine("sqlite:///./test.db")     # or Postgres URL in CI
    Base.metadata.create_all(eng)
    yield eng
    Base.metadata.drop_all(eng)

@pytest.fixture
def db(engine):
    conn = engine.connect(); tx = conn.begin()
    session = Session(bind=conn)
    yield session                                   # each test in a transaction...
    session.close(); tx.rollback(); conn.close()    # ...rolled back = fast isolation

@pytest.fixture
def client(db):
    app.dependency_overrides[get_db] = lambda: db   # API tests share the test session
    yield TestClient(app)
    app.dependency_overrides.clear()
```

## Factory helpers
```python
def make_customer(db, **kw) -> Customer:
    c = Customer(name=kw.get("name", "Acme"), email=kw.get("email", "a@x.co"))
    db.add(c); db.flush()
    return c
```
Plain functions with keyword overrides beat factory frameworks until relationships get deep.

## Level-decision table
| Behavior | Level | Why |
|---|---|---|
| Endpoint contract (status, shape, auth, validation) | API test | The contract is the value |
| Business rule reachable via API | API test | Covers rule + wiring at once |
| Tricky pure logic (math, parsing, dates) | Unit (no mocks) | Fast, precise failure location |
| Cross-page user flow (login → create → verify) | Playwright E2E | Only level that sees the whole |
| Third-party API interaction | API test + respx mock | Determinism at the real boundary |
| DB constraint behavior | API or db-fixture test | Real engine, real constraint |
| Framework internals, trivial pass-throughs, styling | Don't test | No rentable regression risk |

## Playwright skeleton
```ts
test("create invoice money path", async ({ page }) => {
  await page.goto("/login");
  await page.getByLabel("Email").fill(user.email);
  await page.getByLabel("Password").fill(user.password);
  await page.getByRole("button", { name: "Log in" }).click();
  await page.getByRole("link", { name: "Invoices" }).click();
  await page.getByRole("button", { name: "New invoice" }).click();
  await page.getByLabel("Amount").fill("99.50");
  await page.getByRole("button", { name: "Save" }).click();
  await expect(page.getByText("Invoice created")).toBeVisible();
});
```
Rules: role/label selectors (not CSS classes), seeded test user per run, retry-on-CI once
(flaky twice = fix or delete), cap the whole E2E stage at a few minutes.

## External-boundary mocks
```python
@pytest.fixture
def bank_api(respx_mock):
    respx_mock.get("https://bank.example/balances").respond(json={"available": "1000.00"})
    return respx_mock

def test_position_uses_bank_balance(client, bank_api):
    assert client.get("/cash/position").json()["available"] == "1000.00"
```
Clock: inject `now()` as a dependency/parameter; freeze in tests. Randomness: seed or
inject. Email/SMS: capture via a fake sender fixture, assert on the captured payload.

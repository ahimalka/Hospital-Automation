# Hospital Portal Automation Suite

A Python-based end-to-end automation framework built with [Playwright](https://playwright.dev/python/) and [pytest](https://docs.pytest.org/) to exercise a local hospital portal (`hospital.html`).
Designed as a clean, maintainable example for portfolio use and real-world test automation projects.

---

### ?? Tech Stack

- **Language:** Python�3.13 (tested)
- **Automation:** [Playwright for Python](https://pypi.org/project/playwright/)
- **Test runner:** `pytest` with [pytest-playwright](https://pypi.org/project/pytest-playwright/)
- **Browser engine:** Chromium (bundled via `playwright install`)
- **Page-object model:** custom classes in `pages/`
- **Reporting:** HTML reports via `pytest-html`/Playwright-built-in
- **IDE support:** VS?Code (optional `.vscode/settings.json` included)

---

### ?? Project Structure

```
.
+-- conftest.py                # pytest fixtures (browser, page, etc.)
+-- pages/                     # page-object classes
�   +-- a_login_page.py
�   +-- b_dashboard_page.py
�   +-- c_add_patient.py
+-- tests/
    +-- smoke/
    �   +-- test_smoke.py
    +-- sanity/
        +-- test_negative_login.py
```

*Vendor/virtual-env directories and caches are excluded from source control.*

---

### ?? Installation

1. **Clone the repository**

   ```bash
   git clone <repo-url>
   cd testPlaywright
   ```

2. **Create & activate a virtual environment**

   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1       # Windows PowerShell
   # or
   .venv\Scripts\activate           # Windows CMD / Unix shells
   ```

3. **Install dependencies**

   *(no `requirements.txt` present; install minimal set)*

   ```bash
   pip install --upgrade pip
   pip install pytest playwright pytest-playwright
   # optionally: pip install pytest-html
   ```

4. **Install Playwright browsers**

   ```bash
   playwright install
   ```

5. **(Optional)** freeze the environment:

   ```bash
   pip freeze > requirements.txt
   ```

---

### ?? Running Tests

Run the full suite:

```bash
pytest
```

By default, `pytest` will discover tests under `tests/`.  
The VS?Code configuration in `.vscode/settings.json` already points pytest at the project root.

#### Run specific tests

```bash
pytest tests/smoke/test_smoke.py
pytest tests/sanity/test_negative_login.py
pytest tests/sanity/::test_negative_login[0]   # run one parametrized case
```

#### Add verbosity, reports or markers

```bash
pytest -vv
pytest --html=reports/report.html              # generate an HTML report
pytest -k smoke                                # filter by keyword
```

---

### ?? Environment Setup Notes

- The suite targets a static `hospital.html` file; adjust `hospital_url` fixture in `conftest.py` if the location changes.
- Browsers are managed by Playwright and launched non-headless (`headless=False`) for visibility; change in `conftest.py` as needed.
- Tests assume Python�3.13+. Install a suitable interpreter or adjust to your environment.

---

### ?? Reporting

- HTML reports can be generated with `pytest-html` or by configuring `pytest-playwright` options.
- Example command:

  ```bash
  pytest --html=html-report/index.html --self-contained-html
  ```

- Generated artifacts (e.g. `html-report/`, `reports/`, Playwright�s own `htmlReport/`) are ignored via `.gitignore`.

---

### ?? CI/CD

No CI configuration is included, but the project is CI-ready. A typical pipeline would:

1. Checkout the repo.
2. Set up Python and create/activate a virtualenv.
3. Install dependencies (`pip install �`).
4. Run `playwright install` to provision browsers.
5. Execute `pytest` (with optional report generation).
6. Publish test artifacts (HTML reports, screenshots, traces).

Example GitHub Actions snippet:

```yaml
name: Python Playwright Tests

on: [push, pull_request]

jobs:
  tests:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.13'
      - run: python -m venv .venv
      - run: .venv\\Scripts\\activate && pip install -r requirements.txt
      - run: .venv\\Scripts\\activate && playwright install
      - run: .venv\\Scripts\\activate && pytest --html=report.html
      - uses: actions/upload-artifact@v3
        with:
          name: test-report
          path: report.html
```

Feel free to adapt for GitLab CI, Azure Pipelines, etc.

---

### ?? Example Commands

| Purpose                         | Command                                                                 |
|---------------------------------|-------------------------------------------------------------------------|
| Run all tests                   | `pytest`                                                                |
| Generate HTML report            | `pytest --html=reports/report.html`                                     |
| Execute a single file           | `pytest tests/smoke/test_smoke.py`                                     |
| Install Playwright browsers     | `playwright install`                                                    |
| Activate virtual environment    | `.venv\Scripts\Activate.ps1` (PowerShell)                             |

---

### ?? Portfolio Notes

This repository demonstrates:

- Modular page-object design.
- Parameterized, data-driven tests.
- Playwright sync API usage.
- Consistent pytest fixtures and structure.
- Easy setup and CI integration.

Use it as a reference or starting point for more advanced automation engineering work.

---

> **Next steps:** add a `requirements.txt`, extend with more page objects/tests, and plug in a CI config to showcase full pipeline automation.


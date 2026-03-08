import pytest
from playwright.sync_api import sync_playwright
from pages.a_login_page import LoginPage

# 1. The URL Provider
@pytest.fixture(scope="session")
def hospital_url():
    return "https://qahackeru3.netlify.app/"

# 2. The Browser Lifecycle (Fixes the asyncio error)
@pytest.fixture(scope="session")
def browser_instance():
    with sync_playwright() as p:
        # headless=True is required for GitHub Actions
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

# 3. The Page Creator
@pytest.fixture
def page(browser_instance):
    context = browser_instance.new_context()
    page = context.new_page()
    yield page
    context.close()

# 4. The Page Object Initializer
@pytest.fixture
def login_page(page, hospital_url):
    page.goto(hospital_url)
    return LoginPage(page)
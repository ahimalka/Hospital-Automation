import pytest
from playwright.async_api import async_playwright
from pages.a_login_page import LoginPage

@pytest.fixture
def hospital_url():
    return "https://qahackeru3.netlify.app/"

@pytest.fixture
async def browser():
    """Fixture to create and manage a browser instance"""
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        yield browser

@pytest.fixture
async def page(browser):
    """Fixture to create a page context"""
    page = await browser.new_page()
    yield page
    await page.close()

@pytest.fixture
async def login_page(page, hospital_url):
    """Fixture to initialize login page and navigate to hospital portal"""
    await page.goto("https://qahackeru3.netlify.app/")
    return LoginPage(page)

import pytest
from playwright.sync_api import sync_playwright
from pages.a_login_page import LoginPage
import os

@pytest.fixture
def hospital_url():
    return r"C:\Users\97250\Desktop\Automation\hospital.html"

@pytest.fixture
def browser():
    """Fixture to create and manage a browser instance"""
    playwright = sync_playwright().start()
    headless = os.environ.get('CI') == 'true'
    browser = playwright.chromium.launch(headless=headless)
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture
def page(browser):
    """Fixture to create a page context"""
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture
def login_page(page, hospital_url):
    """Fixture to initialize login page and navigate to hospital portal"""
    page.goto(f"file:///{hospital_url}")
    return LoginPage(page)

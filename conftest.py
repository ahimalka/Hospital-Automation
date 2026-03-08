import pytest
from pages.a_login_page import LoginPage

@pytest.fixture(scope="session")
def hospital_url():
    """Provides the base URL for the hospital application"""
    return "https://qahackeru3.netlify.app/"

@pytest.fixture
def login_page(page, hospital_url):
    """
    This uses the 'page' fixture automatically provided by pytest-playwright.
    No more 'sync_playwright().start()'—that was the cause of the crash!
    """
    page.goto(hospital_url)
    return LoginPage(page)
import pytest
from pages.a_login_page import LoginPage

# 1. Configure the built-in 'browser' fixture to be headless for CI
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
    }

# 2. The URL Provider
@pytest.fixture(scope="session")
def hospital_url():
    return "https://qahackeru3.netlify.app/"

# 3. The Page Object Initializer 
# (Notice we use the built-in 'page' fixture here)
@pytest.fixture
def login_page(page, hospital_url):
    page.goto(hospital_url)
    return LoginPage(page)
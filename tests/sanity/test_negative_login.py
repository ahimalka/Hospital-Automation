import pytest
from pages.a_login_page import LoginPage


@pytest.mark.parametrize("username,password,expected_error", [
    # Scenario 1: Both fields empty
    ("", "", "Invalid credentials"),
    
    # Scenario 2: Empty username with valid password format
    ("", "Password@123", "Invalid credentials"),
    
    # Scenario 3: Empty password with valid username format
    ("user@hospital.com", "", "Invalid credentials"),
    
    # Scenario 4: Whitespace username
    ("   ", "Password@123", "Invalid credentials"),
    
    # Scenario 5: Whitespace password
    ("user@hospital.com", "   ", "Invalid credentials"),
    
    # Scenario 6: Invalid email format (no @)
    ("userhospital.com", "Password@123", "Invalid credentials"),
    
    # Scenario 7: Invalid email format (no domain)
    ("user@", "Password@123", "Invalid credentials"),
    
    # Scenario 8: SQL injection attempt in username
    ("admin' OR '1'='1", "Password@123", "Invalid credentials"),
    
    # Scenario 9: SQL injection attempt in password
    ("user@hospital.com", "' OR '1'='1", "Invalid credentials"),
    
    # Scenario 10: XSS attempt in username
    ("<script>alert('xss')</script>", "Password@123", "Invalid credentials"),
    
    # Scenario 11: XSS attempt in password
    ("user@hospital.com", "<script>alert('xss')</script>", "Invalid credentials"),
    
    # Scenario 12: Special characters in username
    ("user@#$%^&*()hospital.com", "Password@123", "Invalid credentials"),
    
    # Scenario 13: Very long username (>255 characters)
    ("a" * 300 + "@hospital.com", "Password@123", "Invalid credentials"),
    
    # Scenario 14: Very long password (>255 characters)
    ("user@hospital.com", "a" * 300, "Invalid credentials"),
    
    # Scenario 15: Correct username, wrong password
    ("admin@hospital.com", "WrongPassword123", "Invalid credentials"),
    
    # Scenario 16: Wrong username, correct password format but invalid user
    ("invaliduser@hospital.com", "Admin@Password123", "Invalid credentials"),
    
    # Scenario 17: Reversed credentials (password as username)
    ("Password@123", "user@hospital.com", "Invalid credentials"),
    
    # Scenario 18: Extra spaces around credentials
    ("  user@hospital.com  ", "  Password@123  ", "Invalid credentials"),
    
    # Scenario 19: Case sensitivity test (valid email but wrong case in password)
    ("admin@hospital.com", "password@123", "Invalid credentials"),
    
    # Scenario 20: Common weak credentials attempt
    ("test@hospital.com", "123456", "Invalid credentials"),
])
@pytest.mark.asyncio
async def test_negative_login(login_page, username, password, expected_error):
    """
    Test negative login scenarios for the hospital portal.
    
    This test validates that invalid credentials result in the expected error message.
    It covers various edge cases including:
    - Empty fields
    - Whitespace inputs
    - Invalid email formats
    - SQL injection attempts
    - XSS attempts
    - Special characters
    - Extremely long inputs
    - Incorrect credential combinations
    
    Args:
        login_page: Fixture that provides initialized LoginPage with browser context
        username: The username to attempt login with
        password: The password to attempt login with
        expected_error: The expected error message "Invalid credentials"
    """
    # Perform login with invalid credentials
    await login_page.login(username, password)
    
    # Verify that the expected error message is displayed
    error_message = await login_page.get_error_message()
    assert error_message == expected_error, \
        f"Expected error '{expected_error}' but got '{error_message}' for username='{username}' and password='{password}'"

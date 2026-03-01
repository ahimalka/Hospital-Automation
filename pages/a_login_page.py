class LoginPage:
    
    def __init__(self,page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator(".btn-login")
        self.error_message = page.locator(".error-message")


    def login(self, user_text, pass_text):
        self.username_input.fill(user_text)
        self.password_input.fill(pass_text)
        self.login_button.click()

    def get_error_message(self):
        return self.error_message.text_content()


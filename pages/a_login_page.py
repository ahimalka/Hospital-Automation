class LoginPage:
    
    def __init__(self,page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator(".btn-login")
        self.error_message = page.locator(".error-message")


    async def login(self, user_text, pass_text):
        await self.username_input.fill(user_text)
        await self.password_input.fill(pass_text)
        await self.login_button.click()

    async def get_error_message(self):
        return await self.error_message.text_content()


import settings
from pages.base_page import BasePage
from playwright.sync_api import Page


class AuthenticationPage(BasePage):
    url: str = settings.url

    def __init__(self, page: Page):
        super().__init__(page)
        self.signup_text = self.page.locator('//h2[text()="New User Signup!"]')
        self.signup_button = self.page.locator('//button[@data-qa="signup-button"]')
        self.signup_name_input = self.page.locator('//input[@data-qa="signup-name"]')
        self.signup_email_input = self.page.locator('//input[@data-qa="signup-email"]')

import settings
from pages.base_page import BasePage
from playwright.sync_api import Page


class SignUpPage(BasePage):
    url: str = settings.url

    def __init__(
            self, page: Page, day_birth: int = 1, month_birth: int = 1, year_birth: int = 2021, gender: str = "1"
    ):
        super().__init__(page)
        self.gender = self.page.locator(f'label[for="id_gender{gender}"]')
        self.day_birth_selector = self.page.locator('select#days')
        self.month_birth_selector = self.page.locator('select#months')
        self.year_birth_selector = self.page.locator('select#years')
        self.password_input = self.page.locator('input[type="password"]')
        self.first_name_input = self.page.locator('input#first_name')
        self.last_name_input = self.page.locator('input#last_name')
        self.address_input = self.page.locator('input#address1')
        self.state_input = self.page.locator('input#state')
        self.city_input = self.page.locator('input#city')
        self.zipcode_input = self.page.locator('input#zipcode')
        self.mobile_number_input = self.page.locator('input#mobile_number')
        self.create_account_button = self.page.locator('button[data-qa="create-account"]')
        self.newsletter_checkbox = self.page.locator('input#newsletter')
        self.offers_checkbox = self.page.locator('input#optin')
        self.account_created_text = self.page.locator('h2[data-qa="account-created"]')
        self.continue_after_registration_button = self.page.locator('a[data-qa="continue-button"]')

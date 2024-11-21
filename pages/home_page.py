from pages.base_page import BasePage
from playwright.sync_api import Page
import settings


class HomePage(BasePage):
    url: str = settings.url

    def __init__(self, page: Page):
        super().__init__(page)
        self.banner_text = self.page.locator('//h2[text()="Full-Fledged practice website for Automation Engineers"]')

import settings
from pages.base_page import BasePage
from playwright.sync_api import Page


class AuthenticationPage(BasePage):
    url: str = settings.url

    def __init__(self, page: Page):
        super().__init__(page)

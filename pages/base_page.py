from playwright.sync_api import Page
from typing import Literal


class BasePage:
    url: str

    def __init__(self, page: Page):
        self.page: Page = page
        self.header_login = self.page.locator('//div[@class="shop-menu pull-right"] // a', has_text="Signup / Login")
        self.logged_user_header = self.page.locator('//div[@class="shop-menu pull-right"] // a', has_text="Logged in as")

    def open(self):
        self.page.goto(self.url, wait_until="domcontentloaded")


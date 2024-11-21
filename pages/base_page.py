from playwright.sync_api import Page
from typing import Literal


class BasePage:
    url: str

    def __init__(self, page: Page):
        self.page: Page = page
        self.header_element = '//div[@class="shop-menu pull-right"] // a'

    def open(self):
        self.page.goto(self.url, wait_until="domcontentloaded")

    def header_element_click(self,element: Literal["Home", "Products", "Cart", "Signup / Login"]):
        self.page.locator(self.header_element, has_text=f" {element}")



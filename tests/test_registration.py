from pages.authentication_page import AuthenticationPage
from pages.home_page import HomePage
from playwright.sync_api import expect
import allure


class TestAuthentication:
    def test_registration(self, page):
        home_page: HomePage = HomePage(page)
        authentication_page: AuthenticationPage = AuthenticationPage(page)
        with allure.step("Navigate to url 'http://automationexercise.com'"):
            home_page.open()
        with allure.step("Verify that home page is visible successfully"):
            expect(home_page.banner_text.nth(0)).to_be_visible()
        with allure.step("Click on 'Signup / Login' button"):
            home_page.header_element_click(element="Signup / Login")
        with allure.step("Verify 'New User Signup!' is visible"):
            expect(authentication_page.signup_text).to_be_visible()
        # with allure.step("Enter name and email address"):

import time

import allure
from pages.login_page import AuthenticationPage
from pages.signup_page import SignUpPage
from playwright.sync_api import expect
from builders.user import User


class TestAuthentication:
    def test_registration(self, page):
        generated_user: User = User()
        login_page: AuthenticationPage = AuthenticationPage(page)
        signup_page: SignUpPage = SignUpPage(page)
        with allure.step("Navigate to url 'http://automationexercise.com'"):
            login_page.open()
        with allure.step("Click on 'Signup / Login' button"):
            login_page.header_login.click()
        with allure.step("Verify 'New User Signup!' is visible"):
            expect(login_page.signup_text).to_be_visible()
        with allure.step("Enter user_name and email address"):
            login_page.signup_name_input.fill(generated_user.user_name)
            login_page.signup_email_input.fill(generated_user.email)
            login_page.signup_button.click()
        with allure.step("Fill details inputs"):
            signup_page.gender.click()
            signup_page.password_input.fill(generated_user.password)
            signup_page.day_birth_selector.select_option(generated_user.day_birth)
            signup_page.month_birth_selector.select_option(generated_user.month_birth)
            signup_page.year_birth_selector.select_option(generated_user.year_birth)
            signup_page.first_name_input.fill(generated_user.first_name)
            signup_page.last_name_input.fill(generated_user.last_name)
            signup_page.address_input.fill(generated_user.address)
            signup_page.state_input.fill(generated_user.state)
            signup_page.city_input.fill(generated_user.city)
            signup_page.zipcode_input.fill(generated_user.zipcode)
            signup_page.mobile_number_input.fill(generated_user.mobile_number)
        with allure.step("Select checkboxes"):
            signup_page.newsletter_checkbox.check()
            signup_page.offers_checkbox.check()
        with allure.step("Click 'Create Account button'"):
            signup_page.create_account_button.click()
        with allure.step("Verify that 'ACCOUNT CREATED!' is visible"):
            expect(signup_page.account_created_text).to_contain_text('Account Created!')
        with allure.step(""):
            signup_page.continue_after_registration_button.click()
            expect(signup_page.logged_user_header).to_contain_text(f'Logged in as {generated_user.user_name}')

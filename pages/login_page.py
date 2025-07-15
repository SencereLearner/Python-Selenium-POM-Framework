import allure
from pages.base_page import BasePage
from pages.locators import login_locators as loc
from utils.wait_helpers import wait_for_text

class LoginPage(BasePage):
    _page_url = '/customer/account/login'

    @allure.step("Navigating to the login page")
    def open_page(self):
        self._driver.get(f"{self._base_url}{self._page_url}")

    @property
    def email_field(self):
        return self.find(loc.email_field_loc)

    @property
    def password_field(self):
        return self.find(loc.password_field_loc)

    @property
    def login_button(self):
        return self.find(loc.button_loc)

    @allure.step("Filling in login form with email and password")
    def fill_login_form(self, login: str, password: str):
        self.email_field.send_keys(login)
        self.password_field.send_keys(password)
        self.login_button.click()

    @allure.step("Verifying alert message is correct")
    def check_error_alert_text_is(self, expected_text: str):
        wait_for_text(self._driver, loc.error_locator)
        actual_text = self.find(loc.error_locator).text
        assert actual_text == expected_text

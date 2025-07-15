import pytest
import allure
from pages.base_page import BasePage
import utils.wait_helpers

LOGIN_ERROR = "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."

test_data = [
    ("incorrect@test.com", "wrongpass", LOGIN_ERROR),
    ("existint@email.com", "non-existing-pass", LOGIN_ERROR),
]

@BasePage.log_time
@allure.title("Check successful login")
@allure.severity(allure.severity_level.CRITICAL)
def test_successful_login(login_page, valid_sensitive_creds):
    login_page.open_page()
    login_page.fill_login_form(**valid_sensitive_creds)
    utils.wait_helpers.wait_for_element_visibility(login_page.driver, login_page.header_title_loc)
    assert login_page.find(login_page.header_title_loc).text.lower() == "my account"

@BasePage.log_time
@allure.title("Check login error message with parametrized test data")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("email, password, expected_error", test_data)
def test_login_errors(login_page, email, password, expected_error):
    login_page.open_page()
    login_page.fill_login_form(email, password)
    login_page.check_error_alert_text_is(expected_error)


@BasePage.log_time
@allure.title("Check incorrect login error message")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_incorrect_login(login_page):
    # kwargs keys MUST match exact method parameter names: def fill_login_form(self, login, password):
    credentials = {"login": "user@test.com", "password": "badpass"}
    login_page.open_page()
    login_page.fill_login_form(**credentials)
    login_page.check_error_alert_text_is(LOGIN_ERROR)


@BasePage.log_time
@allure.title("Check correct email with incorrect password error message")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_correct_email_with_incorrect_pass(login_page):
    login_page.open_page()
    login_page.fill_login_form('existint@email.com', 'non-existing-pass')
    login_page.check_error_alert_text_is(LOGIN_ERROR)

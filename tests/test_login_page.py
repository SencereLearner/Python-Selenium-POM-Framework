import pytest
import allure


test_data = [
    ("incorrect@test.com", "wrongpass", "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."),
    ("existint@email.com", "non-existing-pass", "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."),
]


@allure.title("Check login error message with parametrized test data")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("email, password, expected_error", test_data)
def test_login_errors(login_page, email, password, expected_error):
    login_page.open_page()
    login_page.fill_login_form(email, password)
    login_page.check_error_alert_text_is(expected_error)

@allure.title("Check incorrect login error message")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_incorrect_login(login_page):
    login_page.open_page()
    login_page.fill_login_form('incorrect@test.com', 'incorrectPass')
    login_page.check_error_alert_text_is(
        'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
    )

@allure.title("Check correct email with incorrect password error message")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_correct_email_with_incorrect_pass(login_page):
    login_page.open_page()
    login_page.fill_login_form('existint@email.com', 'non-existing-pass')
    login_page.check_error_alert_text_is(
        'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
    )

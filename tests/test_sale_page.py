import pytest
import allure
from pages.base_page import BasePage


@BasePage.log_time
@allure.title("Check incorrect login error")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.extended
def test_header_title(sale_page):
    sale_page.open_page()
    sale_page.check_page_header_title_is('Sale')
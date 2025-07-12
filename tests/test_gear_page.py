import allure
import pytest
from pages.base_page import BasePage
from utils.wait_helpers import wait_for_element_visibility


@BasePage.log_time
@allure.title("Check shopping category opens correct url")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.temp_test
def test_clicking_shopping_category(gear_page):
    gear_page.open_page()
    gear_page.click_shopping_category("watches")
    wait_for_element_visibility(gear_page.driver, gear_page.header_title_loc)
    assert gear_page.get_current_url() == "https://magento.softwaretestingboard.com/gear/watches.html"

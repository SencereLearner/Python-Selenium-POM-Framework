import allure
import pytest
from pages.base_page import BasePage
# from utils.wait_helpers import wait_for_element_visibility
import utils.wait_helpers

@BasePage.log_time
@allure.title("Check shopping category opens correct url and Verify specific watch name")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.extended
def test_clicking_shopping_category(gear_page):
    gear_page.open_page()
    gear_page.click_shopping_category("watches")
    utils.wait_helpers.wait_for_element_visibility(gear_page._driver, gear_page._header_title_loc)
    assert gear_page.current_url == "https://magento.softwaretestingboard.com/gear/watches.html"
    gear_page.verify_specific_watch_name('bolo sport watch')



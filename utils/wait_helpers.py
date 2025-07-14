from typing import Tuple

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def text_is_not_empty_in_element(locator):
    def _predicate(driver):
        element = driver.find_element(*locator)
        if len(element.text) > 0:
            return True
        else:
            return False
    return _predicate

def wait_for_text(driver, locator: tuple, timeout=10):
    return WebDriverWait(driver, timeout).until(
        lambda d: d.find_element(*locator).text.strip() != '') # Checks that the resulting string is not empty

def wait_for_element_visibility(driver, locator: Tuple[str, str], timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

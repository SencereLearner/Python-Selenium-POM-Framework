def text_is_not_empty_in_element(locator):
    def _predicate(driver):
        element = driver.find_element(*locator)
        if len(element.text) > 0:
            return True
        else:
            return False
    return _predicate
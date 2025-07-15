import functools
from time import time
from abc import ABC, abstractmethod
from typing import List

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    _base_url = 'https://magento.softwaretestingboard.com'
    _header_title_loc = (By.TAG_NAME, 'h1')


    def __init__(self, driver: WebDriver):
        self._driver = driver


    @abstractmethod
    def open_page(self):
        pass

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    @property
    def page_title(self) -> str:
        return self._driver.title

    @property
    def header_text(self) -> str:
        return self.find(self._header_title_loc).text

    def find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def find_all(self, locator: tuple) -> List[WebElement]:
        return self._driver.find_elements(*locator)

    def check_page_header_title_is(self, expected_text: str):
        actual_text = self.find(self._header_title_loc).text
        assert actual_text == expected_text, f"Expected header: '{expected_text}', but got: '{actual_text}'"

    # turns a method into a static method, not requiring self as its first parameter and doesn’t need access to the instance or class at all
    # used it here to not require self as the decorator could be used for both methods or functions
    @staticmethod
    def log_time(func):
        @functools.wraps(func) # keeps functions original metadata like .__name__ and returns a function name instead of wrapper name
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            duration = time() - start
            print(f"{func.__name__} executed in {duration:.2f}s")
            return result
        return wrapper
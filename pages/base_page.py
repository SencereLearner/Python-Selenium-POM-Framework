import functools
from time import time
from abc import ABC, abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:

    base_url = 'https://magento.softwaretestingboard.com'
    header_title_loc = (By.TAG_NAME, 'h1')


    def __init__(self, driver: WebDriver):
        self.driver = driver


    @abstractmethod
    def open_page(self):
        pass

    def get_current_url(self):
        return self.driver.current_url

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

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
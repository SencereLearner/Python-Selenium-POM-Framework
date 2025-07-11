from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:

    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None
    header_title_loc = (By.TAG_NAME, 'h1')


    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}/{self.page_url}')
        else:
            raise NotImplementedError('Can not open the page')

    def get_current_url(self):
        return self.driver.current_url

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


header_title_loc = (By.TAG_NAME, 'h1')

class SalePage(BasePage):
    page_url = '/sale.html'

    def check_page_header_title_is(self, text):
        header_title = self.find(header_title_loc)
        assert header_title.text == text
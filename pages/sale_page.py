from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure



class SalePage(BasePage):
    page_url = '/sale.html'

    @allure.step("Verifying page header title is correct")
    def check_page_header_title_is(self, text):
        header_title = self.find(self.header_title_loc)
        assert header_title.text == text
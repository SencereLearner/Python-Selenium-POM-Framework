from pages.base_page import BasePage
import allure


class SalePage(BasePage):


    page_url = '/sale.html'

    @allure.step("Navigating to a webpage")
    def open_page(self):
        self.driver.get(f"{self.base_url}/{self.page_url}")

    @allure.step("Verifying page header title is correct")
    def check_page_header_title_is(self, text):
        header_title = self.find(self.header_title_loc)
        assert header_title.text == text
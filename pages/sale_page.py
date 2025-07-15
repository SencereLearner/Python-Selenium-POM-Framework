from pages.base_page import BasePage
import allure


class SalePage(BasePage):


    page_url = '/sale.html'

    @allure.step("Navigating to a webpage")
    def open_page(self):
        self._driver.get(f"{self._base_url}/{self.page_url}")


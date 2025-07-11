from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class GearPage(BasePage):

    page_url = '/gear.html'

    def click_shopping_category(self, shopping_category: str):
        shopping_category_element = (By.XPATH, f"//li[@class='item']/a[contains(@href, '/gear/{shopping_category.lower()}.html')]")
        self.find(shopping_category_element).click()

    # WAY 2
    # category_links = {
    #     "bags": (By.XPATH, "//li[@class='item']/a[contains(@href, '/gear/bags.html')]"),
    #     "fitness-equipment": (By.XPATH, "//li[@class='item']/a[contains(@href, '/gear/fitness-equipment.html')]"),
    #     "watches": (By.XPATH, "//li[@class='item']/a[contains(@href, '/gear/watches.html')]")
    # }
    #
    # def click_shopping_category(self, shopping_category: str):
    #     locator = self.category_links.get(shopping_category.lower())
    #     if locator:
    #         self.find(locator).click()
    #     else:
    #         raise ValueError(f"Unknown shopping category: '{shopping_category}'")

    # WAY 3
    # bags = (By.XPATH, "(//li[@class='item']/a[@href='https://magento.softwaretestingboard.com/gear/bags.html'])[1]")
    # fitnessEquipment = (By.XPATH, "(//li[@class='item']/a[@href='https://magento.softwaretestingboard.com/gear/fitness-equipment.html'])[1]")
    # watches = (By.XPATH, "(//li[@class='item']/a[@href='https://magento.softwaretestingboard.com/gear/watches.html'])[1]")
    #
    # def click_shopping_category(self, shopping_category: str):
    #     match shopping_category.lower():
    #         case "bags":
    #             self.find(self.bags)
    #         case "fitness-equipment":
    #             self.find(self.fitnessEquipment)
    #         case "watches":
    #             self.find(self.watches)
    #         case _:
    #             print("Not a valid shopping category")
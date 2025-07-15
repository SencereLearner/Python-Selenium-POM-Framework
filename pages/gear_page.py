from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class GearPage(BasePage):

    page_url = '/gear.html'
    all_available_watches = (By.XPATH, "//img[@class='product-image-photo']")

    @allure.step(f"Navigating to a webpage")
    def open_page(self):
        self.driver.get(f"{self.base_url}/{self.page_url}")

    def click_shopping_category(self, shopping_category: str):
        shopping_category_element = (By.XPATH, f"//li[@class='item']/a[contains(@href, '/gear/{shopping_category.lower()}.html')]")
        self.find(shopping_category_element).click()

    def verify_specific_watch_name(self, bag_name):
        all_bags = self.find_all(self.all_available_watches)
        formatted_bags_names = [x.get_attribute("alt").strip().lower() for x in all_bags]
        assert bag_name.lower() in formatted_bags_names, f"Bag name: '{bag_name}' is not found in the list of bags: {formatted_bags_names}"

    category_links = {
        "bags": (By.XPATH, "//li[@class='item']/a[contains(@href, '/gear/bags.html')]"),
        "fitness-equipment": (By.XPATH, "//li[@class='item']/a[contains(@href, '/gear/fitness-equipment.html')]"),
        "watches": (By.XPATH, "//li[@class='item']/a[contains(@href, '/gear/watches.html')]")
    }

    def click_shopping_category2(self, shopping_category: str):
        locator = self.category_links.get(shopping_category.lower())
        if locator:
            self.find(locator).click()
        else:
            raise ValueError(f"Unknown shopping category: '{shopping_category}'")


    bags = (By.XPATH, "(//li[@class='item']/a[@href='https://magento.softwaretestingboard.com/gear/bags.html'])[1]")
    fitnessEquipment = (By.XPATH, "(//li[@class='item']/a[@href='https://magento.softwaretestingboard.com/gear/fitness-equipment.html'])[1]")
    watches = (By.XPATH, "(//li[@class='item']/a[@href='https://magento.softwaretestingboard.com/gear/watches.html'])[1]")

    def click_shopping_category3(self, shopping_category: str):
        match shopping_category.lower():
            case "bags":
                self.find(self.bags)
            case "fitness-equipment":
                self.find(self.fitnessEquipment)
            case "watches":
                self.find(self.watches)
            case _:
                print("Not a valid shopping category")
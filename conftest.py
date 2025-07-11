from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pytest

from pages.gear import GearPage
from pages.sale_page import SalePage
from pages.login_page import LoginPage


@pytest.fixture()
def driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service() # closes Webdriver
    driver = webdriver.Chrome(service=service, options=options)
    # driver.implicitly_wait(5)
    yield driver
    driver.quit() # closes browser

@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)

@pytest.fixture()
def gear_page(driver):
    return GearPage(driver)

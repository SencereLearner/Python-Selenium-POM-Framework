from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.gear_page import GearPage
from pages.sale_page import SalePage
from pages.login_page import LoginPage
from dotenv import load_dotenv
import os
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # disables a browser feature that tells websites "I'm being controlled by automation"
    options.add_argument("--disable-blink-features=AutomationControlled")
    # Pretends to be a normal browser used by a human
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36")
    prefs = {"download.default_directory": f"{os.getcwd()}/FileDownloads"}
    options.add_experimental_option("prefs", prefs)
    service = Service() # closes webdriver
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


load_dotenv()

@pytest.fixture
def valid_sensitive_creds():
    print("Email from env:", os.getenv("VALID_EMAIL")) # to make sure .env loads correctly and has the data
    return {
        "login": os.getenv("VALID_EMAIL"),
        "password": os.getenv("VALID_PASS")
    }

# to run the tests: pytest -m temp_test -s or pytest -m-s

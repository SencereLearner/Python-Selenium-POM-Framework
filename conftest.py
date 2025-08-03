from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.gear_page import GearPage
from pages.sale_page import SalePage
from pages.login_page import LoginPage
from dotenv import load_dotenv
import os
import pytest
import allure


@pytest.fixture()
def driver(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36")
    prefs = {"download.default_directory": f"{os.getcwd()}/FileDownloads"}
    options.add_experimental_option("prefs", prefs)
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    # Access the test result and attach a screenshot on fail
    if request.node.rep_call.failed:
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot,
            name=f"Failure Screenshot {datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}",
            attachment_type=allure.attachment_type.PNG)
    driver.quit()


# # Register test outcome to be used in the fixture
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # Execute all other hooks to get the report object
#     outcome = yield
#     rep = outcome.get_result()
#     # Set a report attribute for each phase of a call (setup, call, teardown)
#     setattr(item, f"rep_{rep.when}", rep)


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
# to run with allure: 1)rm -rf allure-results 2) pytest --alluredir=allure-results 3) allure serve allure-results

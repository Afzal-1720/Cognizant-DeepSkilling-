import os
import pytest
from selenium import webdriver


# -------------------------
# Driver Fixture
# -------------------------

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


# -------------------------
# Base URL Fixture
# -------------------------

@pytest.fixture(scope="session")
def base_url():
    return "https://www.lambdatest.com/selenium-playground/"


# -------------------------
# Screenshot on Failure
# -------------------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            os.makedirs("screenshots", exist_ok=True)

            driver.save_screenshot(
                f"screenshots/{item.name}_failure.png"
            )
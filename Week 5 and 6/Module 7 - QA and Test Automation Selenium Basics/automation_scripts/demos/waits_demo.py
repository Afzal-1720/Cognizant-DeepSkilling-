import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")


# -----------------------------------------------------
# Step 36
# Wait for Success button to become clickable
# -----------------------------------------------------

success_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(.,'Success')]")
    )
)

success_button.click()

print("Clicked Success Button")

# Wait for success alert

success_alert = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".alert-success")
    )
)

print("Alert Text :", success_alert.text)

assert "success" in success_alert.text.lower()

print("Assertion Passed")


# -----------------------------------------------------
# Step 37
# Compare sleep() vs Explicit Wait
# -----------------------------------------------------

print("\nComparing waits...\n")

driver.refresh()

start = time.perf_counter()

time.sleep(3)

sleep_time = time.perf_counter() - start

print(f"time.sleep() : {sleep_time:.2f} seconds")


driver.refresh()

start = time.perf_counter()

button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(.,'Success')]")
    )
)

explicit_time = time.perf_counter() - start

print(f"Explicit Wait : {explicit_time:.2f} seconds")


# -----------------------------------------------------
# Step 38
# element_to_be_clickable
# -----------------------------------------------------

button.click()

print("Button clicked using element_to_be_clickable")


# -----------------------------------------------------
# Step 39
# Fluent Wait
# -----------------------------------------------------

fluent_wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=0.5,
    ignored_exceptions=[NoSuchElementException]
)

alert = fluent_wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".alert-success")
    )
)

print("Fluent Wait Successful")
print(alert.text)

driver.quit()
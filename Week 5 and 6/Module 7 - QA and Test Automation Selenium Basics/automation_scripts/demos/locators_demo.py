"""
Hands-On 5 - Task 1
Locator Strategies (Updated for Current LambdaTest Playground)

Demonstrates:
1. ID
2. CLASS_NAME
3. TAG_NAME
4. Relative XPath
5. Absolute XPath
6. CSS Selectors
7. Explicit Wait
8. XPath text() and contains()
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.maximize_window()

wait = WebDriverWait(driver, 10)

# ---------------------------------------------------
# Open Selenium Playground
# ---------------------------------------------------

driver.get("https://www.lambdatest.com/selenium-playground/")

driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

# ---------------------------------------------------
# Explicit Wait
# ---------------------------------------------------

message_box = wait.until(
    EC.visibility_of_element_located((By.ID, "user-message"))
)

print("✓ Explicit Wait Successful")

# ---------------------------------------------------
# Locator 1 : ID
# ---------------------------------------------------

element_id = driver.find_element(By.ID, "user-message")
print("✓ Located using ID")

# ---------------------------------------------------
# Locator 2 : CLASS_NAME
# ---------------------------------------------------

element_class = driver.find_element(By.CLASS_NAME, "form-control")
print("✓ Located using CLASS_NAME")

# ---------------------------------------------------
# Locator 3 : TAG_NAME
# ---------------------------------------------------

element_tag = driver.find_element(By.TAG_NAME, "input")
print("✓ Located using TAG_NAME")

# ---------------------------------------------------
# Locator 4 : Relative XPath
# ---------------------------------------------------

element_xpath = driver.find_element(
    By.XPATH,
    "//input[@id='user-message']"
)

print("✓ Located using Relative XPath")

# ---------------------------------------------------
# Locator 5 : Absolute XPath
# (Generated dynamically)
# ---------------------------------------------------

element_abs = driver.find_element(
    By.XPATH,
    "/html/body//input[@id='user-message']"
)

print("✓ Located using Absolute XPath")

# ---------------------------------------------------
# NAME Locator
# ---------------------------------------------------

name_attr = element_id.get_attribute("name")

if name_attr:
    driver.find_element(By.NAME, name_attr)
    print("✓ Located using NAME")
else:
    print("⚠ NAME locator not available on current website.")

# ---------------------------------------------------
# CSS SELECTORS
# ---------------------------------------------------

driver.find_element(By.CSS_SELECTOR, "#user-message")
print("✓ CSS Selector using ID")

driver.find_element(
    By.CSS_SELECTOR,
    "input.form-control"
)
print("✓ CSS Selector using Class")

driver.find_element(
    By.CSS_SELECTOR,
    "div input"
)
print("✓ CSS Selector using Parent Child")

# ---------------------------------------------------
# Checkbox Demo
# ---------------------------------------------------

driver.get(
    "https://www.lambdatest.com/selenium-playground/checkbox-demo"
)

wait.until(
    EC.visibility_of_element_located(
        (By.ID, "isAgeSelected")
    )
)

# Locate label using text()

label = driver.find_element(
    By.XPATH,
    "//label[contains(.,'Click on check box')]"
)

print("✓ XPath contains() Successful")

# Find all labels

labels = driver.find_elements(
    By.XPATH,
    "//label"
)

print("Total Labels Found:", len(labels))

driver.quit()
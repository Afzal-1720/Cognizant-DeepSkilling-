"""
Hands-On 4 - Task 1
Headless Chrome Example

Headless mode allows Selenium to execute browser automation
without opening a visible browser window. This is useful for
CI/CD pipelines, servers, and faster automated test execution.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configure Chrome options
options = Options()
options.add_argument("--headless=new")      # Run Chrome in headless mode
options.add_argument("--start-maximized")

# Launch Chrome
driver = webdriver.Chrome(options=options)

# Implicit wait
driver.implicitly_wait(10)

# Open website
driver.get("https://www.lambdatest.com/selenium-playground/")

# Print page title
print("Page Title:", driver.title)

# Close browser
driver.quit()
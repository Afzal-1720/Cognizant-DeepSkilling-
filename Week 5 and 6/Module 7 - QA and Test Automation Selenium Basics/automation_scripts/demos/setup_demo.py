"""
Hands-On 4 - Task 1
Selenium Architecture and Environment Setup

Selenium Components:

1. Selenium WebDriver
   - WebDriver is the core Selenium component used to automate web browsers.
   - It communicates directly with browser drivers such as ChromeDriver and executes browser actions.

2. Selenium Grid
   - Selenium Grid is used to run tests on multiple machines and browsers simultaneously.

3. Selenium IDE
   - Selenium IDE is a browser extension used for record-and-playback automation.
"""

from selenium import webdriver

# Selenium Manager automatically downloads the correct ChromeDriver
driver = webdriver.Chrome()

# Implicit wait
driver.implicitly_wait(10)

# Open website
driver.get("https://www.lambdatest.com/selenium-playground/")

# Print title
print("Page Title:", driver.title)

# Close browser
driver.quit()
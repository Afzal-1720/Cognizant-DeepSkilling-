"""
Hands-On 4 - Task 2
WebDriver Navigation and Window Commands

This script demonstrates:
1. Browser navigation
2. URL assertion
3. Opening a new browser tab
4. Switching between windows
5. Taking screenshots
6. Browser window resizing

Window resizing ensures consistent browser dimensions,
making UI automation reliable across different environments.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Launch Chrome
driver = webdriver.Chrome()

# Wait for elements
driver.implicitly_wait(10)

# Open Selenium Playground
driver.get("https://www.lambdatest.com/selenium-playground/")

# Maximize browser
driver.maximize_window()

# Click "Simple Form Demo"
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

# Verify URL contains "simple-form-demo"
assert "simple-form-demo" in driver.current_url
print("URL Verification Passed")

# Navigate back
driver.back()

print("Returned to:", driver.title)

# Open Google in a new tab
driver.execute_script("window.open('https://www.google.com');")

# Print all window handles
print("Window Handles:", driver.window_handles)

# Switch to Google tab
driver.switch_to.window(driver.window_handles[1])

# Print Google title
print("Google Title:", driver.title)

# Switch back to original tab
driver.switch_to.window(driver.window_handles[0])

# Take screenshot
driver.save_screenshot("playground_screenshot.png")

# Verify screenshot exists
if os.path.exists("playground_screenshot.png"):
    print("Screenshot saved successfully.")
else:
    print("Screenshot not found.")

# Resize browser window
driver.set_window_size(1280, 800)

# Print current window size
print("Window Size:", driver.get_window_size())

# Close browser
driver.quit()
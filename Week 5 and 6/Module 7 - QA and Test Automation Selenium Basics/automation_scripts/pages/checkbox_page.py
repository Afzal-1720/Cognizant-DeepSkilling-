from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckboxPage(BasePage):

    CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")

    def check_option(self):

        self.wait_for_element(self.CHECKBOX).click()

    def uncheck_option(self):

        self.driver.find_element(*self.CHECKBOX).click()

    def is_option_checked(self):

        return self.driver.find_element(
            *self.CHECKBOX
        ).is_selected()
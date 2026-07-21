from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class DropdownPage(BasePage):

    DROPDOWN = (By.ID, "select-demo")

    def select_day(self, day):

        dropdown = self.wait_for_element(self.DROPDOWN)

        Select(dropdown).select_by_visible_text(day)

    def get_selected_day(self):

        dropdown = self.driver.find_element(
            *self.DROPDOWN
        )

        return Select(dropdown).first_selected_option.text
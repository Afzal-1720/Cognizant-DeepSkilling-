from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InputFormPage(BasePage):

    # -------------------------
    # Locators
    # -------------------------

    NAME = (By.ID, "name")

    EMAIL = (By.ID, "inputEmail4")

    PASSWORD = (By.NAME, "password")

    COMPANY = (By.NAME, "company")

    WEBSITE = (By.NAME, "website")

    COUNTRY = (By.NAME, "country")

    CITY = (By.NAME, "city")

    ADDRESS1 = (By.NAME, "address_line1")

    ADDRESS2 = (By.NAME, "address_line2")

    STATE = (By.NAME, "state")

    ZIP = (By.NAME, "zip")

    SUBMIT = (By.XPATH, "//button[@type='submit']")

    SUCCESS = (
        By.CSS_SELECTOR,
        ".success-msg, .alert-success, .success-message"
    )

    # -------------------------
    # Methods
    # -------------------------

    def fill_form(
        self,
        name,
        email,
        password,
        company,
        website,
        country,
        city,
        address1,
        address2,
        state,
        zip_code,
    ):

        self.wait_for_element(self.NAME).send_keys(name)

        self.wait_for_element(self.EMAIL).send_keys(email)

        self.wait_for_element(self.PASSWORD).send_keys(password)

        self.wait_for_element(self.COMPANY).send_keys(company)

        self.wait_for_element(self.WEBSITE).send_keys(website)

        country_dropdown = Select(
            self.wait_for_element(self.COUNTRY)
        )

        country_dropdown.select_by_visible_text(country)

        self.wait_for_element(self.CITY).send_keys(city)

        self.wait_for_element(self.ADDRESS1).send_keys(address1)

        self.wait_for_element(self.ADDRESS2).send_keys(address2)

        self.wait_for_element(self.STATE).send_keys(state)

        self.wait_for_element(self.ZIP).send_keys(zip_code)

    def submit_form(self):

        self.wait_for_element(
            self.SUBMIT
        ).click()

    def get_page_title(self):

        return self.driver.title

    def get_success_message(self):

        return self.wait_for_element(
            self.SUCCESS,
            timeout=10
        ).text
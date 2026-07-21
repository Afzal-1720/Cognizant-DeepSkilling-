from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SimpleFormPage(BasePage):

    MESSAGE_INPUT = (By.ID, "user-message")
    SHOW_BUTTON = (By.ID, "showInput")
    OUTPUT_MESSAGE = (By.ID, "message")

    def enter_message(self, message):

        textbox = self.wait_for_element(self.MESSAGE_INPUT)

        textbox.clear()
        textbox.click()
        textbox.send_keys(message)

        # Debug
        print("Input value:", textbox.get_attribute("value"))

    def click_submit(self):

        button = self.wait_for_element(self.SHOW_BUTTON)

        print("Button text:", button.text)
        print("Button enabled:", button.is_enabled())

        button.click()

        print("Button clicked.")
        print("Current input value:",
      self.driver.find_element(*self.MESSAGE_INPUT).get_attribute("value"))

        print("Current output:",
      self.driver.find_element(*self.OUTPUT_MESSAGE).text)

    from selenium.webdriver.common.by import By

    def get_displayed_message(self):

        message_element = self.driver.find_element(By.ID, "message")

        print("Current message text:", repr(message_element.text))

        return message_element.text
    
    def get_input_value(self):
        return self.driver.find_element(
        *self.MESSAGE_INPUT
    ).get_attribute("value")
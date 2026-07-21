from pages.simple_form_page import SimpleFormPage
from pages.checkbox_page import CheckboxPage
from pages.dropdown_page import DropdownPage
from pages.input_form_page import InputFormPage


def test_simple_form(driver, base_url):

    page = SimpleFormPage(driver)

    page.navigate_to(base_url + "simple-form-demo")

    page.enter_message("Hello Selenium")

    page.click_submit()

    assert page.get_input_value() == "Hello Selenium"


def test_checkbox(driver, base_url):

    page = CheckboxPage(driver)

    page.navigate_to(base_url + "checkbox-demo")

    page.check_option()

    assert page.is_option_checked()

    page.uncheck_option()

    assert not page.is_option_checked()


def test_dropdown(driver, base_url):

    page = DropdownPage(driver)

    page.navigate_to(base_url + "select-dropdown-demo")

    page.select_day("Wednesday")

    assert page.get_selected_day() == "Wednesday"


def test_input_form(driver, base_url):

    page = InputFormPage(driver)

    page.navigate_to(
        base_url + "input-form-demo"
    )

    page.fill_form(
        name="Afzal",
        email="afzal@test.com",
        password="Password123",
        company="Cognizant",
        website="https://www.google.com",
        country="India",
        city="Chennai",
        address1="Street 1",
        address2="Street 2",
        state="Tamil Nadu",
        zip_code="600001",
    )

    page.submit_form()

    # Verify form submission
    assert "Selenium" in page.get_page_title()
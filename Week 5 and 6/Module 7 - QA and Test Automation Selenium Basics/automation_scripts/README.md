# Why Page Object Model?

Without POM:

If the Submit button ID changes from

id="submit"

to

id="btn-submit",

every test file using

driver.find_element(By.ID, "submit")

must be updated individually.

With POM:

The locator is defined only once inside the page object.

Example:

SUBMIT = (By.ID, "submit")

If the ID changes, only this one line needs modification.

All test cases continue to work without changing the test logic.

This improves maintainability, readability, and scalability of automation projects.
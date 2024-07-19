from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def extract_info(driver, field_name):
    """
    Extracts the value of a form field from a web page using Selenium WebDriver.

    This function waits up to 20 seconds for the specified field to be present in the
    DOM, and then retrieves its value attribute. If the field is not found, it returns 'N/A'.

    Args:
        driver (webdriver.Edge): The Selenium WebDriver instance used to interact with the web page.
        field_name (str): The name attribute of the form field to be located and whose value is to be extracted.

    Returns:
        str: The value of the form field, or 'N/A' if the field is not found.
    """
    try:
        field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, field_name))
        )
        field_value = field.get_attribute('value')
    except NoSuchElementException:
        field_value = 'N/A'

    return field_value

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def search_nif(driver, nif):
    """
    Searches for a specific NIF (tax identification number) in the SAFTONLINE application and accesses its details.

    This function locates the search field in the SAFTONLINE application, clears any existing input,
    enters the specified NIF, and initiates the search. It then waits for the details button to become clickable
    and clicks on it to access detailed information about the NIF.

    Args:
        driver (webdriver.Edge): The Selenium WebDriver instance used to interact with the web page.
        nif (str): The NIF to search for in the SAFTONLINE application.

    Returns:
        None
    """
    field_filter = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'mvc-grid-value'))
    )
    field_filter.send_keys(Keys.CONTROL + 'a', Keys.DELETE)
    field_filter.send_keys(nif)
    field_filter.send_keys(Keys.ENTER)
    bt_details = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'pe-7s-look'))
    )
    bt_details.click()

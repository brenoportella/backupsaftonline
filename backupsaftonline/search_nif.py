from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def search_nif (driver, nif):
    field_filter = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "mvc-grid-value"))
    )
    field_filter.send_keys(Keys.CONTROL + "a", Keys.DELETE)
    field_filter.send_keys(nif)
    field_filter.send_keys(Keys.ENTER)
    bt_details = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "pe-7s-look"))
    )
    bt_details.click()

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

def extract_info(driver, field_name):
    info_dict = {}
    try:
        field= WebDriverWait(driver,20).until(
          EC.presence_of_element_located((By.NAME, field_name))
        )
        field_value = field.get_attribute("value")
        info_dict[field_name] = field_value
    except NoSuchElementException:
        info_dict[field_name] = "N/A"
      
    return info_dict
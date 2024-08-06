import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from backupsaftonline.accounts_fields import account_fields
from backupsaftonline.details_fields import details_fields
from backupsaftonline.extract_info import extract_info
from backupsaftonline.nifs import nifs
from backupsaftonline.search_nif import search_nif


def scrapy_nif(driver, file, shutdown_flag, update_progress_callback=None):
    """
    Scrapes NIF (tax identification number) details and account information from the SAFTONLINE application.

    Args:
        driver (webdriver.Edge): The Selenium WebDriver instance used to interact with the web page.
        file (str): The path to the text file containing the list of NIFs to be searched.
        shutdown_flag (threading.Event): A flag to signal the shutdown of the process.
        update_progress_callback (function): A callback function to update progress.

    Returns:
        list of dict: A list of dictionaries, each containing details and account information for a NIF.
    """
    info_list = []
    my_nifs = nifs(file)
    quantity_nifs = len(my_nifs)

    for i, nif in enumerate(my_nifs):
        if shutdown_flag.is_set():
            break
        search_nif(driver, nif)

        details = {}
        for field in details_fields:
            details[field] = extract_info(driver, field)

        bt_conta = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'Contas-tab'))
        )
        driver.execute_script('arguments[0].scrollIntoView(true);', bt_conta)
        driver.execute_script('arguments[0].click();', bt_conta)

        accounts = {}
        for field in account_fields:
            accounts[field] = extract_info(driver, field)

        info_dict = {**details, **accounts}
        info_list.append(info_dict)

        driver.get(
            'https://app.saftonline.pt/empresas?gv-emp-page=1&gv-emp-rows=1600'
        )

        # sys.stdout.write(f'\rNIFs processados: {i + 1}/{quantity_nifs}')
        # sys.stdout.flush()
        # time.sleep(0.01)

        if update_progress_callback:
            progress = int((i + 1) / quantity_nifs * 100)
            update_progress_callback(progress, i + 1, quantity_nifs)

    return info_list

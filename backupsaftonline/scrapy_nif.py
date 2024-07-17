from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from backupsaftonline.accounts_fields import account_fields
from backupsaftonline.details_fields import details_fields
from backupsaftonline.extract_info import extract_info
from backupsaftonline.nifs import nifs
from backupsaftonline.search_nif import search_nif


def scrapy_nif(driver):
    info_list = []
    my_nifs = nifs()
    for nif in my_nifs:
        search_nif(driver, nif)
        for field in details_fields:
            details = extract_info(driver, field)

        bt_conta = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'Contas-tab'))
        )
        driver.execute_script('arguments[0].scrollIntoView(true);', bt_conta)
        driver.execute_script('arguments[0].click();', bt_conta)

        for field in account_fields:
            accounts = extract_info(driver, field)

        info_dict = {**details, **accounts}
        info_list.append(info_dict)

        driver.get(
            'https://app.saftonline.pt/empresas?gv-emp-page=1&gv-emp-rows=1600'
        )
        print(nif)

    return info_list

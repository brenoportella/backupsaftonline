import time

import pandas as pd

import backupsaftonline.credentials as credentials
from backupsaftonline.driver import quit_driver
from backupsaftonline.driver import setup_driver as driver
from backupsaftonline.extract_nifs.extract_nifs import (delete_file,
                                                        download_nifs,
                                                        read_xlsx)
from backupsaftonline.login import login
from backupsaftonline.scrapy_nif import scrapy_nif

email = credentials.email
password = credentials.password


class Backup:
    def __init__(self):
        self.driver = driver()

    def core(self):

        login(self.driver, email, password)
        download_nifs(self.driver)
        time.sleep(1)
        read_xlsx('backupsaftonline', 'Empresas_513029818.xls')
        delete_file('backupsaftonline/Empresas_513029818.xls')
        info = scrapy_nif(self.driver, 'backupsaftonline/nif_saft.txt')

        quit_driver(self.driver)

        df = pd.DataFrame(info)
        process_date = time.strftime('%d-%m-%Y')
        xlsx_name = f'backup-saft-{process_date}.xlsx'
        df.to_excel(xlsx_name, index=False)

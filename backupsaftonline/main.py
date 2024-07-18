import time

import pandas as pd

import backupsaftonline.credentials as credentials
from backupsaftonline.driver import setup_driver as driver
from backupsaftonline.driver import quit_driver
from backupsaftonline.login import login
from backupsaftonline.scrapy_nif import scrapy_nif

email = credentials.email
password = credentials.password


class Backup:
    def __init__(self):
        self.driver = driver()

    def core(self):

        login(self.driver, email, password)
        info = scrapy_nif(self.driver)

        quit_driver(self.driver)

        df = pd.DataFrame(info)
        process_date = time.strftime('%d-%m-%Y')
        xlsx_name = f'backup-saft-{process_date}.xlsx'
        df.to_excel(xlsx_name, index=False)

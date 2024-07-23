import time

import pandas as pd

from backupsaftonline import credentials
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
    """
    A class to perform the backup operations for SAFTONLINE.

    This class handles the entire backup process, from logging in to the SAFTONLINE application,
    downloading NIFs, reading and processing data, and saving the final backup to an Excel file.
    """

    def __init__(self):
        """
        Initializes the Backup class by setting up the Selenium WebDriver.
        """
        self.driver = driver()

    def core(self):
        """
        Executes the core backup process.

        This method performs the following steps:
        1. Logs into the SAFTONLINE application using the provided credentials.
        2. Downloads the NIFs (tax identification numbers) data.
        3. Reads the downloaded NIFs data from an Excel file.
        4. Deletes the original downloaded Excel file.
        5. Scrapes additional NIF information.
        6. Quits the WebDriver.
        7. Saves the scraped NIF information into a new Excel file.

        Returns:
            None
        """
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

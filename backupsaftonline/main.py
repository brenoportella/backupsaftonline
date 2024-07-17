import time
import backupsaftonline.credentials as credentials
import pandas as pd
from backupsaftonline.login import login
from backupsaftonline.scrapy_nif import scrapy_nif
from backupsaftonline.driver import setup_driver as driver

email = credentials.email
password = credentials.password

class Backup:
    def __init__(self):
        self.driver = driver()

    def core(self):
        
        login(self.driver, email, password)
        info = scrapy_nif(self.driver)
    
        driver.quit()

        df = pd.DataFrame(info)
        process_date = time.strftime("%d-%m-%Y")
        xlsx_name = f"backup-saft-{process_date}.xlsx"
        df.to_excel(xlsx_name, index=False)    
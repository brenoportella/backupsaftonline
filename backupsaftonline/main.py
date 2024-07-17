import time
import credentials
import pandas as pd
from login import login
from scrapy_nif import scrapy_nif
from driver import setup_driver as driver

email = credentials.email
password = credentials.password

class Backup:
    def main():
        
        login(driver, email, password)
        info = scrapy_nif(driver)
    
        driver.quit()

        df = pd.DataFrame(info)
        process_date = time.strftime("%d-%m-%Y")
        xlsx_name = f"backup-saft-{process_date}.xlsx"
        df.to_excel(xlsx_name, index=False)
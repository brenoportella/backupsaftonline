# ok, basicamente depois do login, devemos extrair o excel.
"""só que para baixar o arquivo, devemos configurar o path to download do browser,
o que pode ser o path do .\resulsts

depois disso precisamos acessar o arquivo, gerar um dataframe do xlsx, salvar em um
txt com o nome nif_saft.txt substituindo o ficheiro antigo, apagar o arquivo xlsx
e a partir dai vamos para iniciar o programa como sempre"""

import os

import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def download_nifs(driver):

    download_bt = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, 'img-responsive.center-block')
        )
    )
    download_bt.click()


def read_xlsx(path, file):
    file_path = os.path.join(path, file)
    df = pd.read_excel(file_path, skiprows=1, usecols=[0])

    output = os.path.join(path, 'nif_saft.txt')
    df.to_csv(output, sep='\t', index=False)


def delete_file(file):
    os.remove(file)

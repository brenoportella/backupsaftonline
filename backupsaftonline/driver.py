from selenium import webdriver


def setup_driver():
    download_dir = r''
    edge_prefs = {
        'download.neverAsk.saveToDisk': 'application/xml, text/anytext, text/plaintext',
        'download.default_directory': str(download_dir),
        'download.directory_upgrade': True,
        'download.prompt_for_download': False,
        'disable-popup-blocking': True,
        'safebrowsing.enabled': False,
        'download_restrictions': 0,
    }

    options = webdriver.EdgeOptions()
    options.add_argument('--safebrowsing-disable-download-protection')
    options.add_argument('--headless')
    options.add_experimental_option('prefs', edge_prefs)

    driver = webdriver.Edge(options=options)
    return driver

def quit_driver(driver):
    driver.quit()
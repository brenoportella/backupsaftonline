from selenium.webdriver.common.by import By

def login (driver, email, password):
    driver.get("https://app.saftonline.pt/empresas?gv-emp-page=1&gv-emp-rows=1600")

    field_email = driver.find_element(By.NAME, "Email")
    field_email.send_keys(email)
    
    field_password = driver.find_element(By.NAME, "Senha")
    field_password.send_keys(password)

    bt_login = driver.find_element(By.CLASS_NAME, "btn-default")
    bt_login.click()
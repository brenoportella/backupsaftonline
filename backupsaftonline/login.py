from selenium.webdriver.common.by import By


def login(driver, email, password):
    """
    Logs into the SAFTONLINE application using the provided email and password.

    This function navigates to the SAFTONLINE login page, enters the email and password
    into the appropriate fields, and clicks the login button.

    Args:
        driver (webdriver.Edge): The Selenium WebDriver instance used to interact with the web page.
        email (str): The email address to use for login.
        password (str): The password to use for login.

    Returns:
        None
    """
    driver.get(
        'https://app.saftonline.pt/empresas?gv-emp-page=1&gv-emp-rows=1600'
    )

    field_email = driver.find_element(By.NAME, 'Email')
    field_email.send_keys(email)

    field_password = driver.find_element(By.NAME, 'Senha')
    field_password.send_keys(password)

    bt_login = driver.find_element(By.CLASS_NAME, 'btn-default')
    bt_login.click()

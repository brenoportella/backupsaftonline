# Backup SAFTOnline Documentation

Welcome to the documentation for the Backup SAFTOnline project. This project provides tools for interacting with the SAFTOnline API and automating various tasks related to data backup and extraction.

## Overview

The Backup SAFTOnline project consists of several components:
- **Driver Setup**: Configuration and management of the web driver used for interaction with the SAFTOnline application.
- **Login**: Automation of the login process to the SAFTOnline platform.
- **Data Extraction**: Extraction of NIFs and other relevant data.
- **File Management**: Handling of files related to data extraction and backup.

## Modules

### Driver

The `backupsaftonline.driver` module handles the setup and teardown of the web driver.

- **`setup_driver`**: Configures and initializes the web driver for use with the SAFTOnline application.
- **`quit_driver`**: Cleans up and closes the web driver.

### Login

The `backupsaftonline.login` module manages the login process.

- **`login(driver, email, password)`**: Logs into the SAFTOnline application using the provided email and password.

### Data Extraction

The `backupsaftonline.extract_nifs` module is responsible for extracting NIFs and managing files.

- **`delete_file(file)`**: Deletes a specified file.
- **`download_nifs(driver)`**: Downloads NIF data using the web driver.
- **`read_xlsx(directory, filename)`**: Reads data from an Excel file.

### NIF Management

The `backupsaftonline.nifs` module manages NIF data.

- **`nifs(file)`**: Reads NIFs from a specified text file.

### Search and Scrape

The `backupsaftonline.search_nif` module handles searching and scraping data for a specific NIF.

- **`search_nif(driver, nif)`**: Searches for a specific NIF in the SAFTOnline application and navigates to the details page.

### Scraping

The `backupsaftonline.scrapy_nif` module scrapes information related to NIFs.

- **`scrapy_nif(driver, file)`**: Scrapes data for multiple NIFs and collects relevant details.

### Backup

The `backupsaftonline.main` module orchestrates the backup process.

- **`Backup` Class**: Manages the entire backup process, including login, data extraction, and file management.

## How to Use

1. **Setup the Environment**: Install requirements and configure the environment.
2. **Set your website credentials**: Set your login and password for saftonline.
3. **Choose your webdriver**: Choose your prefer webbrowser to use.
4. **Start the program**: Use `python backup.py`.

## Additional Information

For more details, refer to the individual module documentation linked above.

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

---

Feel free to reach out with any questions or contributions to the project!

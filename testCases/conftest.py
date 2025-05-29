from pytest_metadata.plugin import metadata_key
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import os


####################### Browser SetUp Code Start #######################

# Pytest hook to add custom command-line options
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Specify the browser: chrome, firefox, or edge"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run tests in headless mode"
    )

# Fixture to read the browser name from command-line options
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# Fixture to read the headless flag from command-line options
@pytest.fixture()
def headless(request):
    return request.config.getoption("--headless")

# Fixture to initialize and return the appropriate WebDriver instance
@pytest.fixture()
def setup(browser, headless):
    global driver

    if browser == "chrome":
        options = ChromeOptions()
        extension_path = os.path.abspath("C:/Users/DELL/PycharmProjects/UI_Elements_Project/Extensions/uBlock_Origin.crx")
        download_dir = os.path.abspath("C:/Users/DELL/PycharmProjects/UI_Elements_Project/Download")

        # These options should be added regardless of headless mode
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_extension(extension_path)

        # Download preferences
        options.add_experimental_option("prefs", {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        if headless:
            options.add_argument("--headless=new")  # Required for headless downloads in new Chrome
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)
        print("Launching Chrome" + (" in headless mode" if headless else ""))



    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(options=options)
        print("Launching Firefox" + (" in headless mode" if headless else ""))

    elif browser == "edge":
        if headless:
            print("Warning: Headless mode for Edge is not officially supported in this script.")
        driver = webdriver.Edge()
        print("Launching Edge")

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()
####################### Browser SetUp Code End #######################



####################### Pytest HTML Report Configuration Start ###########################

# Hook to add custom environment info to the HTML test report
def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] = 'Demo Project'  # Define project name
    config.stash[metadata_key] ['Test Module Name'] = 'Login Tests'  # Define module name
    config.stash[metadata_key] ['Tester Name'] = 'Vishal Hadiyal'  # Define tester name


# Hook to remove unwanted metadata from the HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)  # Remove JAVA_HOME if present
    metadata.pop("Plugins", None)  # Remove Plugin metadata if present

####################### Pytest HTML Report Configuration Start ###########################
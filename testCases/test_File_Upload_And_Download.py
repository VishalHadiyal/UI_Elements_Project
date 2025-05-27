import json
import os
import time
import pytest
from pageObjects.HomePage import HomePage
from pageObjects.ElementsPage import ElementsPage
from unititlies.customlogger import LogGen
from unititlies.readProperties import ReadConfig


class TestFIleUploadAndDownload:
    # Retrieve the base application URL from the configuration file
    baseURL = ReadConfig.get_application_url()

    # Set up logger for the test class
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def setup_method(self, setup):
        """
        Fixture executed automatically before each test method.
        It performs the following setup tasks:
        - Initializes WebDriver
        - Maximizes the window
        - Applies implicit wait
        - Opens the application
        - Closes unwanted tabs
        - Loads test data
        - Navigates to 'Web Tables' via 'Elements'
        """

        self.logger.info("========== Starting Test: TestTableHandling ==========")

        # Assign WebDriver from setup fixture
        self.driver = setup
        self.logger.info("WebDriver instance initialized.")

        # Configure browser
        self.driver.implicitly_wait(10)
        self.logger.info("Implicit wait set to 10 seconds.")

        self.driver.maximize_window()
        self.logger.info("Browser window maximized.")

        self.driver.get(self.baseURL)
        self.logger.info(f"Navigated to application URL: {self.baseURL}")

        # Handle multiple tabs (e.g., close Bing, stay on the main app)
        windows = self.driver.window_handles
        self.logger.info(f"Window handles retrieved: {windows}")

        if len(windows) > 1:
            self.driver.switch_to.window(windows[1])
            self.logger.info("Switched to second tab (index 1).")
            self.driver.close()
            self.logger.info("Closed second tab.")
            self.driver.switch_to.window(windows[0])
            self.logger.info("Switched back to first tab (index 0).")

        # Load test data from JSON file
        try:
            with open("./TestData/elements_page.json", "r") as file:
                self.data = json.load(file)
            self.logger.info("Test data successfully loaded from 'table_data.json'.")
        except Exception as e:
            self.logger.error(f"Failed to load test data: {str(e)}")
            raise

        # Initialize Page Objects
        home_page = HomePage(self.driver)
        elements_page = ElementsPage(self.driver)

        # Navigate through UI to reach web Tables Section
        home_page.click_on_elements_card()
        self.logger.info("Clicked on 'Elements' card on Home Page.")

        elements_page.click_on_file_upload_and_download()
        self.logger.info("Clicked on 'Upload and Download' under the Elements section.")

        yield  # Yield control to the test method

        # ---------- TEAR DOWN ----------
        self.logger.info("Closing browser after test execution.")
        self.driver.quit()
        self.logger.info("Browser closed successfully.")

    @pytest.mark.smoke
    def test_file_upload(self):
        """
        Test case for uploading a file.
        It performs the following steps:
        - Clicks on 'Upload and Download'
        - Uploads a file
        - Verifies the upload success message
        """
        global success_message
        test_name = "test_file_upload"
        elements_page = ElementsPage(self.driver)

        # Step 1: Navigate to the 'Upload and Download' section of the application
        elements_page.click_on_file_upload_and_download()
        self.logger.info("Clicked on 'Upload and Download'.")  # Log the navigation action

        # Step 2: Upload the file using the path provided in test data
        file_path = self.data["UploadAndDownload"]["uploadFilePath"]
        elements_page.upload_file(file_path)
        self.logger.info(f"File uploaded: {file_path}")  # Log the file upload action

        # Step 3: Retrieve and verify the success message after uploading the file
        try:
            success_message = elements_page.get_upload_success_message()
            assert success_message == self.data["UploadAndDownload"]["UploadedMessage"]
            self.logger.info("File upload verified successfully.")  # Log the verification result
        except AssertionError as e:
            # Capture screenshot on failure
            screenshot_path = f"./Screenshots/{test_name}_assertion_failed.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Assertion failed. Screenshot saved at: {screenshot_path}")
            self.logger.error(f"Expected: {self.data['UploadAndDownload']['UploadedMessage']}, Got: {success_message}")
            raise
        except Exception as e:
            # Capture screenshot on any other exception
            screenshot_path = f"./Screenshots/{test_name}_exception.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"An error occurred. Screenshot saved at: {screenshot_path}")
            self.logger.error(f"Error details: {str(e)}")
            raise

    @pytest.mark.smoke
    def test_file_download(self):
        """
        Test case for downloading a file.
        Steps:
        1. Navigate to 'Upload and Download' section.
        2. Initiate file download.
        3. Verify download success by checking the file existence.
        """

        test_name = "test_file_download"
        elements_page = ElementsPage(self.driver)

        try:
            # Step 1: Navigate to the 'Upload and Download' section of the application
            elements_page.click_on_file_upload_and_download()
            self.logger.info("Step 1: Clicked on 'Upload and Download' section.")

            # Step 2: Download the file using the path provided in test data
            file_path = self.data["UploadAndDownload"]["downloadFilePath"]
            elements_page.download_file(file_path)
            self.logger.info(f"Step 2: Initiated file download to path: {file_path}")

            # Wait briefly for the download to complete
            time.sleep(2)

            # Step 3: Verify the file has been downloaded
            if os.path.exists(file_path):
                self.logger.info("Step 3: File download verified successfully.")
            else:
                self.logger.error("Step 3: File download failed. File not found.")
                screenshot_path = f"./Screenshots/{test_name}_assertion_failed.png"
                self.driver.save_screenshot(screenshot_path)
                self.logger.info(f"Screenshot saved at: {screenshot_path}")
                assert False, "Downloaded file does not exist."

        except Exception as e:
            self.logger.exception(f"Exception occurred in {test_name}: {e}")
            screenshot_path = f"./Screenshots/{test_name}_exception.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved at: {screenshot_path}")
            raise

    @pytest.mark.smoke
    def test_after_5_seconds_button_displayed(self):
        """
        Test case to verify that a button appears after 5 seconds.
        Steps:
        1. Navigate to 'Dynamic Properties' section.
        2. Wait for the button to appear.
        3. Assert that the button is displayed.
        """
        test_name = "test_after_5_seconds_button_displayed"
        elements_page = ElementsPage(self.driver)

        try:
            # Step 1: Navigate to 'Dynamic Properties'
            self.logger.info("Step 1: Navigating to 'Dynamic Properties' section.")
            elements_page.Click_on_dynamic_properties()
            self.logger.info("Clicked on 'Dynamic Properties' successfully.")

            # Step 2: Wait for the button and check its visibility
            self.logger.info("Step 2: Waiting for the button to appear (after 5 seconds).")
            is_displayed = elements_page.after_5_seconds_button_is_displayed()
            self.logger.info(f"Button visibility status after 5 seconds: {is_displayed}")

            # Step 3: Assertion
            self.logger.info("Step 3: Asserting button visibility.")
            assert is_displayed, "Button did not appear after 5 seconds."
            self.logger.info("Assertion passed: Button appeared successfully after 5 seconds.")

        except AssertionError as e:
            # Capture screenshot on assertion failure
            screenshot_path = f"./Screenshots/{test_name}_assertion_failed.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Assertion failed: {str(e)}")
            self.logger.error(f"Screenshot saved at: {screenshot_path}")
            raise
        except Exception as e:
            # Log and raise unexpected exceptions
            self.logger.exception(f"An unexpected error occurred: {str(e)}")
            raise

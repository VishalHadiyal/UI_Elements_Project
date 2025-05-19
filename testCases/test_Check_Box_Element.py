import json
import time

import pytest
from selenium.common import NoSuchElementException
from pageObjects.HomePage import HomePage
from pageObjects.ElementsPage import ElementsPage
from unititlies.customlogger import LogGen
from unititlies.readProperties import ReadConfig


class TestCheckBoxElement:
    # Get base URL from configuration
    baseURL = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def setup_method(self, setup):
        """
        Automatically executed before each test method.

        Responsibilities:
        - Logs the start of the test.
        - Initializes the WebDriver with implicit wait and maximized window.
        - Navigates to the application's base URL.
        - Loads test data from a JSON file for use in tests.
        - Navigates to the 'Elements' section of the application.
        """

        self.logger.info("********** Starting Test: TestElementsPage **********")

        # Browser setup
        self.logger.info("Initializing browser setup...")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.logger.info("Set implicit wait to 10 seconds.")
        self.driver.maximize_window()
        self.logger.info("Maximized the browser window.")

        # Navigate to base URL
        self.driver.get(self.baseURL)
        self.logger.info(f"Navigated to base URL: {self.baseURL}")

        # Load test data from JSON file
        try:
            self.logger.info("Loading test data from JSON file: elements_page.json")
            with open("./TestData/elements_page.json", "r") as file:
                self.data = json.load(file)
            self.logger.info("Test data loaded successfully from elements_page.json")
        except Exception as e:
            self.logger.error(f"Failed to load test data from elements_page.json: {str(e)}")
            raise

        # Initialize page object for Home Page and click 'Elements' card
        self.logger.info("Initializing HomePage object.")
        home_page = HomePage(self.driver)

        self.logger.info("Clicking on 'Elements' card on the Home Page.")
        home_page.click_on_elements_card()
        self.logger.info("'Elements' card clicked successfully.")

    @pytest.mark.skip(reason="Skipping test for demonstration purposes.")
    def test_home_check_box_displayed(self):
        """
        Test to verify that the 'Home' checkbox is displayed on the CheckBox page.
        """
        self.logger.info("********** Test Started: test_home_check_box_displayed **********")

        # Step 1: Initialize page object models
        self.logger.info("Initializing ElementsPage objects.")
        elements_page = ElementsPage(self.driver)

        # Step 2: Wait for elements to load (replace with explicit wait in production)
        self.logger.info("Waiting for page to stabilize before interacting with elements.")
        time.sleep(2)  # Temporary wait; not recommended for production use

        # Step 3: Navigate to 'Check Box' section in the Elements Page
        self.logger.info("Clicking on 'Check Box' section in the Elements Page.")
        elements_page.click_on_check_box()
        self.logger.info("Successfully navigated to 'Check Box' section.")

        # Step 4: Verify if the 'Home' checkbox is displayed
        self.logger.info("Verifying visibility of 'Home' checkbox on the page.")
        try:
            # Placeholder assertion
            assert True
            self.logger.info("Initial assertion passed (placeholder).")

            # Actual check for 'Home' checkbox
            elements_page.check_home_check_box_displayed()
            self.logger.info("Success: 'Home' checkbox is displayed.")

        except AssertionError as ae:
            # Handle failed assertion
            screenshot_path = "./Screenshots/test_home_check_box_displayed_assertion_fail.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error("Assertion failed while verifying 'Home' checkbox visibility.")
            self.logger.error(f"AssertionError Details: {ae}")
            self.logger.error(f"Screenshot captured: {screenshot_path}")
            raise

        except NoSuchElementException as nse:
            # Handle scenario where checkbox is not found
            screenshot_path = "./Screenshots/test_home_check_box_displayed_nosuchelement_fail.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error("Element not found: 'Home' checkbox is missing on the page.")
            self.logger.error(f"NoSuchElementException Details: {nse}")
            self.logger.error(f"Screenshot captured: {screenshot_path}")
            raise AssertionError("Home checkbox not found on the page.")

        except Exception as e:
            # Handle any unexpected exception
            screenshot_path = "./Screenshots/test_home_check_box_displayed_unexpected_fail.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error("Unexpected error occurred during test execution.")
            self.logger.error(f"Exception Details: {e}")
            self.logger.error(f"Screenshot captured: {screenshot_path}")
            raise
        finally:
            # Step 5: Close the browser (teardown)
            self.logger.info("Closing the browser.")
            self.driver.quit()
            self.logger.info("Browser closed successfully.")

    @pytest.mark.skip(reason="Skipping test for demonstration purposes.")
    def test_workspace_check_box_displayed_after_expanding(self):
        """
        Test to verify that the 'Workspace' checkbox is displayed on the CheckBox page.
        """

        self.logger.info("========== Test Started: test_workspace_check_box_displayed_after_expanding ==========")

        try:
            # Step 1: Initialize page object for ElementsPage
            self.logger.info("Step 1: Initializing ElementsPage object.")
            elements_page = ElementsPage(self.driver)

            # Step 2: Wait for the page to stabilize before interaction
            self.logger.info("Step 2: Waiting for page to stabilize.")
            time.sleep(2)  # Replace with WebDriverWait in real-world usage

            # Step 3: Navigate to the 'Check Box' section
            self.logger.info("Step 3: Clicking on 'Check Box' section.")
            elements_page.click_on_check_box()
            self.logger.info("Navigated to 'Check Box' section successfully.")
            time.sleep(2)

            # Step 4: Expand the 'Home' node to reveal child elements like 'Workspace'
            self.logger.info("Step 4: Expanding 'Home' checkbox to reveal 'Workspace'.")
            elements_page.click_plus_button()
            self.logger.info("Expanded 'Home' checkbox successfully.")
            time.sleep(2)

            # Step 5: Check if the 'Workspace' checkbox is visible and clickable
            self.logger.info("Step 5: Checking visibility of 'Workspace' checkbox.")

            try:
                # Perform the action or visibility check
                elements_page.click_workspace_check_box()
                self.logger.info("Success: 'Workspace' checkbox is visible and clickable.")

            except NoSuchElementException as nse:
                # Screenshot and detailed logging for missing element
                screenshot_path = "./Screenshots/test_workspace_check_box_displayed_nosuchelement_fail.png"
                self.driver.save_screenshot(screenshot_path)
                self.logger.error("ERROR: 'Workspace' checkbox not found on the page.")
                self.logger.error(f"Exception Details: {nse}")
                self.logger.error(f"Screenshot captured: {screenshot_path}")
                raise AssertionError("Workspace checkbox not found on the page.") from nse

        except Exception as e:
            # Handle any unexpected exception
            screenshot_path = "./Screenshots/test_workspace_check_box_displayed_unexpected_fail.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error("Unexpected error occurred during test execution.")
            self.logger.error(f"Exception Details: {e}")
            self.logger.error(f"Screenshot captured: {screenshot_path}")
            raise

        finally:
            # Step 6: Close the browser (teardown)
            self.logger.info("Step 6: Closing the browser.")
            self.driver.quit()
            self.logger.info("========== Test Completed: test_workspace_check_box_displayed_after_expanding ==========")
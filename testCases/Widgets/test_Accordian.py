import json
import pytest
from pageObjects.WidgetsPage import WidgetsPage
from pageObjects.HomePage import HomePage
from unititlies.customlogger import LogGen
from unititlies.readProperties import ReadConfig


class TestBrowserWindowHandles:
    # Retrieve the base application URL from the configuration file
    baseURL = ReadConfig.get_application_url()

    # Set up logger for the test class
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def setup_method(self, setup):
        """
        Fixture executed automatically before each test method.
        Handles browser setup, test data loading, and navigation.
        """
        self.logger.info("========== Starting Test: TestRegistrationPage ==========")

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
            self.logger.info("Switched to second tab.")
            self.driver.close()
            self.logger.info("Closed second tab.")
            self.driver.switch_to.window(windows[0])
            self.logger.info("Switched back to main tab.")

        # Load test data from JSON file
        try:
            with open("./TestData/Widgets_module.json", "r") as file:
                self.data = json.load(file)
            self.logger.info("Test data successfully loaded from 'registration_form.json'.")
        except Exception as e:
            self.logger.error(f"Failed to load test data: {str(e)}")
            screenshot_path = "./Screenshots/test_data_load_exception.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved at: {screenshot_path}")
            raise

        # Initialize Page Objects
        self.home_page = HomePage(self.driver)
        self.widgets_page = WidgetsPage(self.driver)

        # Navigate to the Registration Form
        self.home_page.click_on_widgets_card()
        self.logger.info("Clicked on 'Forms' card on Home Page.")

        self.widgets_page.click_accordion_option()
        self.logger.info("Clicked on 'Practice Form' under the Forms section.")

        yield  # Run the test method

        # ---------- TEAR DOWN ----------
        self.logger.info("Closing browser after test execution.")
        self.driver.quit()
        self.logger.info("Browser closed successfully.")

    def test_accordion_widget(self):
        test_name = "test_accordion_widget"

        self.logger.info(f"Starting test: {test_name}")

        try:
            # Step 1: Click on the Accordion option
            self.logger.info("Clicking on the Accordion option")
            self.widgets_page.click_accordion_option()

            # Step 2: Click and validate First Accordion section
            self.logger.info("Validating First Accordion section")
            self.widgets_page.clicks_on_first_accordion_section()
            first_text = self.widgets_page.get_first_accordion_content_text()
            assert self.data["TextOfAccordian"]["TextOfAccordianFirst"] in first_text
            self.widgets_page.clicks_on_first_accordion_section()
            self.logger.info("First Accordion section validated successfully")

            # Step 3: Click and validate Second Accordion section
            self.logger.info("Validating Second Accordion section")
            self.widgets_page.clicks_on_second_accordion_section()
            second_text = self.widgets_page.get_second_accordion_content_text()
            assert self.data["TextOfAccordian"]["TextOfAccordianSecond"] in second_text
            self.widgets_page.clicks_on_second_accordion_section()
            self.logger.info("Second Accordion section validated successfully")

            # Step 4: Click and validate Third Accordion section
            self.logger.info("Validating Third Accordion section")
            self.widgets_page.clicks_on_third_accordion_section()
            third_text = self.widgets_page.get_third_accordion_content_text()
            assert self.data["TextOfAccordian"]["TextOfAccordianThird"] in third_text
            self.widgets_page.clicks_on_third_accordion_section()
            self.logger.info("Third Accordion section validated successfully")

            self.logger.info(f"Test {test_name} passed successfully")

        except AssertionError as ae:
            screenshot_path = "./Screenshots/output_assertion_failed.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Assertion failed in {test_name}: {str(ae)}")
            self.logger.error(f"Screenshot saved to {screenshot_path}")
            raise

        except Exception as e:
            screenshot_path = "./Screenshots/output_exception_error.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Exception occurred in {test_name}: {str(e)}")
            self.logger.error(f"Screenshot saved to {screenshot_path}")
            raise

        finally:
            self.logger.info(f"Test {test_name} completed, either passed or failed.")
            self.logger.info("Test execution finished.")

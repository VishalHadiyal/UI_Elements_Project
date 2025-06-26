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

        self.widgets_page.click_auto_complete_option()
        self.logger.info("Clicked on 'Practice Form' under the Forms section.")

        yield  # Run the test method

        # ---------- TEAR DOWN ----------
        self.logger.info("Closing browser after test execution.")
        self.driver.quit()
        self.logger.info("Browser closed successfully.")

    def test_auto_complete(self):
        self.logger.info("Starting test: test_auto_complete")

        try:
            # Step 1: Fetch expected color values from test data
            expected_colors = self.data["MultiColor"]
            self.logger.info(f"Expected colors to select: {expected_colors}")

            # Step 2: Perform color selection using auto-complete input
            self.widgets_page.get_input_multiple_color_auto_complete(expected_colors)
            self.logger.info("Colors selected using the auto-complete field.")

            # Step 3: Get the actual selected colors from the application
            actual_colors = self.widgets_page.get_selected_colors_auto_complete()
            self.logger.info(f"Actual selected colors retrieved: {actual_colors}")

            # Step 4: Validate that both lists have same items, order doesn't matter
            assert sorted(actual_colors) == sorted(expected_colors), \
                f"Expected {expected_colors} but got {actual_colors}"

            self.logger.info("Color selection verified successfully. Test Passed.")

        except AssertionError as ae:
            self.logger.error(f"Assertion failed: {ae}")
            screenshot_path = "./Screenshots/test_auto_complete_failure.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved at {screenshot_path}")
            raise

        except Exception as e:
            self.logger.error(f"An unexpected error occurred: {e}")
            screenshot_path = "./Screenshots/test_auto_complete_exception.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved at {screenshot_path}")
            raise

        finally:
            self.logger.info("Test test_auto_complete completed.")
            self.logger.info("========================================")
            self.logger.info("Test test_auto_complete finished successfully.")
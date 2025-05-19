import json
import pytest
from pageObjects.HomePage import HomePage
from pageObjects.ElementsPage import ElementsPage
from unititlies.customlogger import LogGen
from unititlies.readProperties import ReadConfig


class TestRadioButtonElements:
    # Get base URL from configuration
    baseURL = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def setup_method(self, setup):
        """
        This setup method runs automatically before each test method.
        It initializes the WebDriver, sets implicit wait, maximizes the window,
        and navigates to the base URL. It also loads test data from JSON.
        """
        self.logger.info("********** Starting Test: TestElementsPage **********")
        self.logger.info("Initializing browser setup...")

        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.logger.info(f"Navigated to URL: {self.baseURL}")

        # Load test data from JSON file
        try:
            with open("./TestData/elements_page.json", "r") as file:
                self.data = json.load(file)
                self.logger.info("Test data loaded successfully from home_page.json")
        except Exception as e:
            self.logger.error(f"Failed to load test data: {str(e)}")
            raise
        self.logger.info("Setup method completed.")

    # @pytest.mark.skip(reason="Skipping this test case for now.")
    def test_verify_yes_radio_button(self):
        """
        Test case to verify the functionality of the 'Yes' radio button on the Radio Button page.
        """
        self.logger.info("========== Test Case: test_verify_yes_radio_button ==========")
        self.logger.info("Step 1: Starting test for verifying 'Yes' radio button selection.")

        try:
            # Initialize page objects
            home_page = HomePage(self.driver)
            elements_page = ElementsPage(self.driver)

            # Navigate to 'Elements' section from home page
            home_page.click_on_elements_card()
            self.logger.info("Step 2: Clicked on 'Elements' card.")

            # Click on 'Radio Button' in the side menu
            elements_page.click_on_radio_button()
            self.logger.info("Step 3: Clicked on 'Radio Button' option.")

            # Select 'Yes' radio button
            elements_page.click_on_yes_radio_button()
            self.logger.info("Step 4: Clicked on 'Yes' radio button.")

            # Get the result text displayed after selecting 'Yes'
            actual_message = elements_page.get_success_message_text()
            expected_message = self.data["radioButton"]["selectedYesText"]
            self.logger.info(f"Step 5: Retrieved output message: '{actual_message}'")

            # Assertion to verify the correct message is displayed
            assert actual_message == expected_message, (
                f"Expected message: '{expected_message}', but got: '{actual_message}'"
            )
            self.logger.info("Step 6: 'Yes' radio button text verified successfully.")

        except AssertionError as ae:
            self.logger.error("Assertion failed while verifying 'Yes' radio button selection.")
            screenshot_path = "./Screenshots/test_verify_yes_radio_button_failed.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Screenshot saved at: {screenshot_path}")
            self.logger.error(str(ae))
            raise

        except Exception as e:
            self.logger.error("An unexpected error occurred during the test execution.")
            screenshot_path = "./Screenshots/test_verify_yes_radio_button_unexpected_error.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Screenshot saved at: {screenshot_path}")
            self.logger.exception(str(e))
            raise

        finally:
            # Clean up and close the browser
            self.driver.quit()
            self.logger.info("Browser closed successfully.")
            self.logger.info("Test case execution completed.")
            self.logger.info("========== Test Case: test_verify_yes_radio_button completed ==========")

    # @pytest.mark.skip(reason="Skipping this test case for now.")
    def test_verify_impressive_radio_button(self):
        """
        Test case to verify the functionality of the 'Impressive' radio button
        on the Radio Button page.
        """
        test_name = "test_verify_impressive_radio_button"
        self.logger.info(f"========== Test Case: {test_name} STARTED ==========")

        try:
            # Step 1: Initialize page objects
            self.logger.info("Step 1: Initializing page objects.")
            home_page = HomePage(self.driver)
            elements_page = ElementsPage(self.driver)

            # Step 2: Navigate to 'Elements' section from the Home page
            home_page.click_on_elements_card()
            self.logger.info("Step 2: Clicked on 'Elements' card.")

            # Step 3: Click on 'Radio Button' option in the side menu
            elements_page.click_on_radio_button()
            self.logger.info("Step 3: Clicked on 'Radio Button' option.")

            # Step 4: Click on the 'Impressive' radio button
            elements_page.click_on_impressive_radio_button()
            self.logger.info("Step 4: Clicked on 'Impressive' radio button.")

            # Step 5: Get the displayed result message
            actual_message = elements_page.get_success_message_text()
            expected_message = self.data["radioButton"]["selectedImpressiveText"]
            self.logger.info(f"Step 5: Retrieved success message: '{actual_message}'")

            # Step 6: Validate the success message
            assert actual_message == expected_message, (
                f"Expected message: '{expected_message}', but got: '{actual_message}'"
            )
            self.logger.info("Step 6: 'Impressive' radio button selection verified successfully.")

        except AssertionError as ae:
            self.logger.error("Assertion failed: 'Impressive' radio button message mismatch.")
            screenshot_path = f"./Screenshots/{test_name}_assertion_failed.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Screenshot captured: {screenshot_path}")
            self.logger.error(str(ae))
            raise

        except Exception as e:
            self.logger.error("Unexpected error occurred during test execution.")
            screenshot_path = f"./Screenshots/{test_name}_unexpected_error.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Screenshot captured: {screenshot_path}")
            self.logger.exception(str(e))
            raise

        finally:
            # Step 7: Clean up and close the browser
            self.driver.quit()
            self.logger.info("Step 7: Browser closed successfully.")
            self.logger.info(f"========== Test Case: {test_name} COMPLETED ==========")

    # @pytest.mark.skip(reason="Skipping this test case for now.")
    def test_verify_no_radio_button(self):
        """
        Test case to verify if the 'No' radio button on the Radio Button page is enabled.
        """
        test_name = "test_verify_no_radio_button"
        self.logger.info(f"========== Test Case: {test_name} STARTED ==========")

        try:
            # Step 1: Initialize page objects
            self.logger.info("Step 1: Initializing page objects.")
            home_page = HomePage(self.driver)
            elements_page = ElementsPage(self.driver)

            # Step 2: Navigate to 'Elements' section from the Home page
            home_page.click_on_elements_card()
            self.logger.info("Step 2: Clicked on 'Elements' card.")

            # Step 3: Click on 'Radio Button' option in the side menu
            elements_page.click_on_radio_button()
            self.logger.info("Step 3: Clicked on 'Radio Button' option.")

            # Step 4: Check if the 'No' radio button is enabled
            is_enabled = elements_page.is_no_radio_button_enabled()
            self.logger.info(f"Step 4: Checked if 'No' radio button is enabled: {is_enabled}")

            # Step 5: Assert that the 'No' radio button should NOT be enabled
            assert not is_enabled, "'No' radio button is enabled, but it should be disabled."

            self.logger.info("Step 5: Verified that 'No' radio button is correctly disabled.")
            screenshot_path = f"./Screenshots/{test_name}_success.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot captured: {screenshot_path}")

        except AssertionError as ae:
            self.logger.error("Assertion failed: 'No' radio button state is not as expected.")
            screenshot_path = f"./Screenshots/{test_name}_assertion_failed.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Screenshot captured: {screenshot_path}")
            self.logger.error(str(ae))
            raise

        except Exception as e:
            self.logger.error("Unexpected error occurred during test execution.")
            screenshot_path = f"./Screenshots/{test_name}_unexpected_error.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Screenshot captured: {screenshot_path}")
            self.logger.exception(str(e))
            raise

        finally:
            # Step 6: Clean up and close the browser
            self.driver.quit()
            self.logger.info("Step 6: Browser closed successfully.")
            self.logger.info(f"========== Test Case: {test_name} COMPLETED ==========")

    def test_verify_radio_buttons_flow(self):
        """
        Test case to verify the functionality of all radio buttons ('Yes', 'Impressive', and 'No')
        on the Radio Button page in a single flow.
        """
        test_name = "test_verify_radio_buttons_flow"
        self.logger.info(f"========== Test Case: {test_name} STARTED ==========")

        try:
            # Step 1: Initialize page objects
            self.logger.info("Step 1: Initializing page objects.")
            home_page = HomePage(self.driver)
            elements_page = ElementsPage(self.driver)

            # Step 2: Navigate to 'Elements' section from the Home page
            home_page.click_on_elements_card()
            self.logger.info("Step 2: Clicked on 'Elements' card.")

            # Step 3: Click on 'Radio Button' option in the side menu
            elements_page.click_on_radio_button()
            self.logger.info("Step 3: Clicked on 'Radio Button' option.")

            # Step 4: Click on the 'Yes' radio button and verify the message
            elements_page.click_on_yes_radio_button()
            self.logger.info("Step 4: Clicked on 'Yes' radio button.")
            actual_message_yes = elements_page.get_success_message_text()
            expected_message_yes = self.data["radioButton"]["selectedYesText"]
            self.logger.info(f"Step 5: Retrieved output message for 'Yes': '{actual_message_yes}'")
            assert actual_message_yes == expected_message_yes, (
                f"Expected message: '{expected_message_yes}', but got: '{actual_message_yes}'"
            )
            self.logger.info("Step 6: 'Yes' radio button selection verified successfully.")

            # Step 7: Click on the 'Impressive' radio button and verify the message
            elements_page.click_on_impressive_radio_button()
            self.logger.info("Step 7: Clicked on 'Impressive' radio button.")
            actual_message_impressive = elements_page.get_success_message_text()
            expected_message_impressive = self.data["radioButton"]["selectedImpressiveText"]
            self.logger.info(f"Step 8: Retrieved output message for 'Impressive': '{actual_message_impressive}'")
            assert actual_message_impressive == expected_message_impressive, (
                f"Expected message: '{expected_message_impressive}', but got: '{actual_message_impressive}'"
            )
            self.logger.info("Step 9: 'Impressive' radio button selection verified successfully.")

            # Step 10: Check that the 'No' radio button is disabled
            is_no_enabled = elements_page.is_no_radio_button_enabled()
            self.logger.info(f"Step 10: Checked if 'No' radio button is enabled: {is_no_enabled}")
            assert not is_no_enabled, "'No' radio button is enabled, but it should be disabled."
            self.logger.info("Step 11: Verified that 'No' radio button is correctly disabled.")

            screenshot_path = f"./Screenshots/{test_name}_success.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot captured: {screenshot_path}")

        except AssertionError as ae:
            self.logger.error("Assertion failed during radio button flow verification.")
            screenshot_path = f"./Screenshots/{test_name}_assertion_failed.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Screenshot captured: {screenshot_path}")
            self.logger.error(str(ae))
            raise

        except Exception as e:
            self.logger.error("Unexpected error occurred during test execution.")
            screenshot_path = f"./Screenshots/{test_name}_unexpected_error.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Screenshot captured: {screenshot_path}")
            self.logger.exception(str(e))
            raise

        finally:
            # Step 12: Clean up and close the browser
            self.driver.quit()
            self.logger.info("Step 12: Browser closed successfully.")
            self.logger.info(f"========== Test Case: {test_name} COMPLETED ==========")

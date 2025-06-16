import json
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
from pageObjects.BrowserWindow import BrowserWindowHandle
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
            with open("./TestData/window_handle.json", "r") as file:
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
        self.BWH = BrowserWindowHandle(self.driver)

        # Navigate to the Registration Form
        self.home_page.click_on_alerts_frame_windows_card()
        self.logger.info("Clicked on 'Forms' card on Home Page.")

        self.BWH.click_on_browser_window_option()
        self.logger.info("Clicked on 'Practice Form' under the Forms section.")

        yield  # Run the test method

        # ---------- TEAR DOWN ----------
        self.logger.info("Closing browser after test execution.")
        self.driver.quit()
        self.logger.info("Browser closed successfully.")

    @pytest.mark.smoke
    def test_browser_new_tab(self):
        """
        Test case to verify the functionality of opening a new browser tab,
        switching to it, validating its content, and switching back.
        """
        self.logger.info("========== Starting test: test_browser_new_tab ==========")

        global windows  # Declare windows as global to access it in the finally block

        try:
            # Step 1: Click on the 'New Tab' button
            self.logger.info("Clicking on the 'New Tab' button.")
            self.BWH.click_on_new_tab_button()
            self.logger.info("Clicked on 'New Tab' button successfully.")

            # Step 2: Get the list of current browser window handles
            windows = self.driver.window_handles
            self.logger.info(f"Window handles after opening new tab: {windows}")

            # Step 3: Assert a new tab has been opened
            assert len(windows) == 2, "New tab was not opened successfully."
            self.logger.info("New tab opened successfully.")

            # Step 4: Switch to the newly opened tab
            self.driver.switch_to.window(windows[1])
            self.logger.info("Switched to the new tab.")

            # Step 5: Get the title or text of the new tab
            new_tab_title = self.BWH.get_new_tab_text()
            self.logger.info(f"Retrieved new tab title/text: {new_tab_title}")

            # Step 6: Validate the new tab title/text matches expected data
            assert new_tab_title == self.data["NewTab"], "New tab title does not match expected value."
            self.logger.info("New tab title matches expected value.")

            # Optional: Take a screenshot for documentation
            screenshot_path = "./Screenshots/test_browser_new_tab_success.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot captured at: {screenshot_path}")

        except AssertionError as e:
            # Capture a screenshot in case of assertion failure
            screenshot_path = "./Screenshots/test_browser_new_tab_failure.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Assertion failed: {e}")
            self.logger.error(f"Screenshot captured at: {screenshot_path}")
            raise

        except Exception as e:
            # General exception handling with screenshot
            screenshot_path = "./Screenshots/test_browser_new_tab_exception.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"An unexpected error occurred: {e}")
            self.logger.error(f"Screenshot captured at: {screenshot_path}")
            raise

        finally:
            # Step 7: Cleanup - close the new tab and return to the original tab
            if len(windows) == 2:
                self.driver.close()
                self.logger.info("Closed the new tab.")
                self.driver.switch_to.window(windows[0])
                self.logger.info("Switched back to the original tab.")

        self.logger.info("========== Finished test: test_browser_new_tab ==========")

    @pytest.mark.smoke
    def test_browser_new_window(self):
        """
        Test case to verify the functionality of:
        - Opening a new browser window,
        - Switching to the new window,
        - Validating the content in the new window,
        - Switching back to the original window.
        """
        self.logger.info("========== Starting test: test_browser_new_window ==========")

        windows = []  # Initialize List to store window handles

        try:
            # Step 1: Click on the 'New Window' button
            self.logger.info("Attempting to click on the 'New Window' button.")
            self.BWH.click_on_new_window_button()
            self.logger.info("Clicked on 'New Window' button successfully.")

            # Step 2: Retrieve all current browser window handles
            windows = self.driver.window_handles
            self.logger.info(f"Window handles retrieved: {windows}")

            # Step 3: Validate that a new window was opened
            assert len(windows) == 2, "New window was not opened successfully."
            self.logger.info("Successfully verified that a new browser window is opened.")

            # Step 4: Switch to the newly opened window (index 1)
            self.logger.info("Switching to the newly opened window.")
            self.driver.switch_to.window(windows[1])
            self.logger.info("Switched to the new window successfully.")

            # Step 5: Retrieve and validate the content of the new window
            self.logger.info("Retrieving text content from the new window.")
            actual_text = self.BWH.get_new_window_text()  # Assumes this method is implemented in the BrowserWindowHandle class
            expected_text = self.data["NewWindow"]
            self.logger.info(f"Expected text: '{expected_text}', Actual text: '{actual_text}'")

            assert actual_text == expected_text, \
                f"Text mismatch in new window. Expected: '{expected_text}', Got: '{actual_text}'"
            self.logger.info("New window text content matches the expected value.")

            # Step 6: Capture a screenshot upon success
            screenshot_path = "./Screenshots/test_browser_new_window_success.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot captured successfully at: {screenshot_path}")

        except AssertionError as e:
            # Handle assertion failures
            screenshot_path = "./Screenshots/test_browser_new_window_failure.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Assertion failed: {e}")
            self.logger.error(f"Failure screenshot captured at: {screenshot_path}")
            raise

        except Exception as e:
            # Handle unexpected exceptions
            screenshot_path = "./Screenshots/test_browser_new_window_exception.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"An unexpected exception occurred: {e}")
            self.logger.error(f"Exception screenshot captured at: {screenshot_path}")
            raise

        finally:
            # Step 7: Cleanup - close the new window and return to the original window
            if len(windows) == 2:
                self.logger.info("Closing the new window and switching back to the original window.")
                self.driver.close()  # Closes the current window (i.e., the new one)
                self.logger.info("New window closed successfully.")
                self.driver.switch_to.window(windows[0])  # Switch back to the original window
                self.logger.info("Switched back to the original window successfully.")

        self.logger.info("========== Finished test: test_browser_new_window ==========")

    @pytest.mark.smoke
    def test_all_alerts(self):
        self.BWH = BrowserWindowHandle(self.driver)
        test_name = "test_all_alerts"
        self.logger.info(f"========== Starting test: {test_name} ==========")

        # Load data from JSON
        data = self.data
        confirm_text = data["ConfirmResultText"]
        prompt_input = data["AlertSendText"]
        expected_prompt_result = data["PromptResultText"]

        try:
            # First Alert - Simple alert
            self.logger.info("Clicking on 'Alerts' section.")
            self.BWH.click_on_alerts_option()

            self.logger.info("Clicking on first alert button (simple alert).")
            self.BWH.click_on_click_me_and_see_alert_button()
            alert = self.driver.switch_to.alert
            self.logger.info("Accepting the first alert.")
            alert.accept()

            # Second Alert - Delayed alert
            self.logger.info("Clicking on second alert button (5-second delay).")
            self.BWH.click_on_after_five_seconds_button()
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            self.logger.info("Accepting the delayed alert.")
            alert.accept()

            # Third Alert - Confirmation box
            self.logger.info("Clicking on confirmation box button.")
            self.BWH.click_on_confirm_box_button()
            alert = self.driver.switch_to.alert
            self.logger.info("Accepting the confirmation alert.")
            alert.accept()

            confirm_result = self.BWH.get_confirm_result_text()
            self.logger.info(f"Verifying confirmation result: Expected='{confirm_text}', Actual='{confirm_result}'")
            assert confirm_result == confirm_text, f"Confirmation result mismatch. Expected: '{confirm_text}', Got: '{confirm_result}'"

            # Fourth Alert - Prompt box
            self.logger.info("Clicking on prompt box button.")
            self.BWH.click_on_prompt_box_button()
            alert = self.driver.switch_to.alert
            self.logger.info(f"Sending text to prompt alert: '{prompt_input}'")
            alert.send_keys(prompt_input)
            alert.accept()

            prompt_result = self.BWH.get_prompt_result_text()
            self.logger.info(f"Verifying prompt result: Expected='{expected_prompt_result}', Actual='{prompt_result}'")
            assert prompt_result == expected_prompt_result, f"Prompt result mismatch. Expected: '{expected_prompt_result}', Got: '{prompt_result}'"

        except Exception as e:
            screenshot_path = f"./Screenshots/{test_name}_failure.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"{test_name} failed. Screenshot saved to {screenshot_path}")
            self.logger.exception("Exception occurred during test execution:")
            raise e

        self.logger.info(f"========== Completed test: {test_name} ==========")

    @pytest.mark.sanity
    def test_small_modal(self):
        # Initialize page object for handling modal interactions
        self.BWH = BrowserWindowHandle(self.driver)

        # Define the test name and start logging
        test_name = "test_small_modal"
        self.logger.info(f"========== Starting test: {test_name} ==========")

        try:
            # Step 1: Click on the modal option
            self.logger.info("Clicking on the modal option...")
            self.BWH.click_on_modal_option()

            # Step 2: Click on the button to open small modal
            self.logger.info("Clicking on the small modal button...")
            self.BWH.click_on_small_modal_button()

            # Step 3: Validate the content inside the modal
            actual_modal_text = self.BWH.get_modal_content_text()
            expected_modal_text = self.data["TextOfSmallModal"]
            self.logger.debug(f"Expected modal content: {expected_modal_text}, Actual: {actual_modal_text}")
            assert actual_modal_text == expected_modal_text, "Small modal text does not match"

            # Step 4: Validate the modal title/name
            actual_modal_title = self.BWH.get_name_of_small_modal_text()
            expected_modal_title = self.data["NameOfSmallModal"]
            self.logger.debug(f"Expected modal title: {expected_modal_title}, Actual: {actual_modal_title}")
            assert actual_modal_title == expected_modal_title, "Small modal title does not match"

            # Step 5: Close the small modal
            self.logger.info("Closing the small modal...")
            self.BWH.close_small_modal()

            # Step 6: Verify the page name text after modal is closed
            actual_page_text = self.BWH.get_name_of_the_page_text()
            expected_page_text = self.data["NameOfThePage"]
            self.logger.debug(f"Expected page name: {expected_page_text}, Actual: {actual_page_text}")
            assert actual_page_text == expected_page_text, "Page name text after closing modal does not match"

            self.logger.info(f"========== Test Passed: {test_name} ==========")

        except AssertionError as ae:
            # Capture and log error with screenshot on failure
            screenshot_path = f"./Screenshots/{test_name}_failure.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Assertion failed in {test_name}: {ae}")
            self.logger.error(f"Screenshot saved to: {screenshot_path}")
            raise

        except Exception as e:
            # Handle any unexpected exceptions
            screenshot_path = f"./Screenshots/{test_name}_exception.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Exception occurred in {test_name}: {e}")
            self.logger.error(f"Screenshot saved to: {screenshot_path}")
            raise
        finally:
            # Ensure the modal is closed if it was opened
            try:
                self.BWH.close_small_modal()
                self.logger.info("Small modal closed successfully in finally block.")
            except Exception as e:
                self.logger.error(f"Failed to close small modal in finally block: {e}")
        self.logger.info(f"========== Finished test: {test_name} ==========")

    @pytest.mark.sanity
    def test_large_modal(self):
        # Test name for logging and screenshot purposes
        test_name = "test_large_modal"
        self.logger.info(f"========== Starting test: {test_name} ==========")

        # Initialize page object for modal interactions
        self.BWH = BrowserWindowHandle(self.driver)

        try:
            # Step 1: Click the modal section option on the page
            self.logger.info("Clicking on modal option...")
            self.BWH.click_on_modal_option()

            # Step 2: Open the large modal by clicking the appropriate button
            self.logger.info("Clicking on large modal button...")
            self.BWH.click_on_large_modal_button()

            # Step 3: Validate the large modal's title text
            actual_modal_title = self.BWH.get_name_of_large_modal_text()
            expected_modal_title = self.data["NameOfLargeModal"]
            self.logger.info(
                f"Validating large modal title: Expected='{expected_modal_title}', Actual='{actual_modal_title}'")
            assert actual_modal_title == expected_modal_title, "Large modal title does not match expected value."

            # Step 4: Validate the content inside the large modal
            actual_modal_content = self.BWH.get_content_of_large_modal_text()
            expected_modal_content = self.data["TextOfLargeModal"]
            self.logger.info("Validating content inside the large modal.")
            assert actual_modal_content == expected_modal_content, "Large modal content does not match expected value."

            # Step 5: Close the modal
            self.logger.info("Closing the large modal.")
            self.BWH.close_large_modal()

            # Step 6: Validate that the user is back on the expected page
            actual_page_name = self.BWH.get_name_of_the_page_text()
            expected_page_name = self.data["NameOfThePage"]
            self.logger.info(
                f"Validating page name after closing modal: Expected='{expected_page_name}', Actual='{actual_page_name}'")
            assert actual_page_name == expected_page_name, "Returned page name does not match expected value."

            self.logger.info(f"========== Test Passed: {test_name} ==========")

        except AssertionError as e:
            self.logger.error(f"Assertion failed in {test_name}: {str(e)}")
            screenshot_path = f"./Screenshots/{test_name}_assertion_error.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved to {screenshot_path}")
            raise

        except Exception as e:
            self.logger.error(f"Exception occurred in {test_name}: {str(e)}", exc_info=True)
            screenshot_path = f"./Screenshots/{test_name}_exception.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved to {screenshot_path}")
            raise

        finally:
            # Ensure the large modal is closed if it was opened
            try:
                self.BWH.close_large_modal()
                self.logger.info("Large modal closed successfully in finally block.")
            except Exception as e:
                self.logger.error(f"Failed to close large modal in finally block: {e}")
        self.logger.info(f"========== Finished test: {test_name} ==========")

    @pytest.mark.sanity
    def test_Iframe(self):
        """
        Test case to verify the functionality of switching to an iframe,
        interacting with elements inside it, and switching back to the main content.
        """
        self.logger.info("========== Starting test: test_iframe ==========")

        try:
            # Step 1: Click on the 'IFrame' option
            self.logger.info("Clicking on the IFrame option.")
            self.BWH.click_on_frames_option()

            # Step 2: Switch to the iframe
            self.logger.info("Switching to the iframe.")
            self.BWH.switch_to_frame()

            # Step 3: Validate the text inside the iframe
            actual_text = self.BWH.get_text_from_iframe()
            expected_text = self.data["IFrameText"]
            self.logger.info(f"Validating iframe text: Expected='{expected_text}', Actual='{actual_text}'")
            assert actual_text == expected_text, "IFrame text does not match expected value."

            # Step 4: Switch back to the main content
            self.logger.info("Switching back to the main content.")
            self.BWH.switch_to_default_content()

        except AssertionError as e:
            screenshot_path = "./Screenshots/test_iframe_failure.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Assertion failed: {e}")
            self.logger.error(f"Screenshot captured at: {screenshot_path}")
            raise

        except Exception as e:
            screenshot_path = "./Screenshots/test_iframe_exception.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"An unexpected error occurred: {e}")
            self.logger.error(f"Screenshot captured at: {screenshot_path}")
            raise

        finally:
            # Ensure we switch back to the main content if needed
            try:
                self.BWH.switch_to_default_content()
                self.logger.info("Switched back to main content successfully in finally block.")
            except Exception as e:
                self.logger.error(f"Failed to switch back to main content in finally block: {e}")

        self.logger.info("========== Finished test: test_iframe ==========")

    @pytest.mark.sanity
    def test_nested_iframe(self):
        """
        Test case to verify the functionality of switching to nested iframes,
        interacting with elements inside child frame, and switching back to main content.
        """
        self.logger.info("========== Starting test: test_nested_iframe ==========")

        try:
            # Step 1: Click on the 'Nested Frames' option
            self.logger.info("Clicking on the 'Nested Frames' option.")
            self.BWH.click_on_nested_iframe_option()
            time.sleep(3)

            # Step 2: Validate main header text outside the iframe
            self.logger.info("Validating the main heading text of nested frame page.")
            actual_header = self.BWH.get_main_nested_frame_text()
            expected_header = self.data["NestedFrameHeader"]
            self.logger.info(f"Expected Header='{expected_header}', Actual Header='{actual_header}'")
            assert actual_header == expected_header, "Main nested frame header text does not match."

            # Step 3: Switch to the parent iframe
            self.logger.info("Switching to parent iframe.")
            self.BWH.switch_to_parent_frame()

            # Step 4: Switch to the child iframe inside parent
            self.logger.info("Switching to child iframe inside parent.")
            self.BWH.switch_to_child_frame()

            # Step 5: Validate the text inside child iframe
            expected_child_text = self.data["NestedChildText"]
            self.logger.info("Validating the text inside the child iframe.")
            child_text = self.driver.find_element(By.TAG_NAME, "p").text
            self.logger.info(f"Expected Text='{expected_child_text}', Actual Text='{child_text}'")
            assert child_text == expected_child_text, "Child iframe text does not match expected value."

            # Step 6: Switch back to the main content
            self.logger.info("Switching back to the main content.")
            self.driver.switch_to.default_content()

        except AssertionError as e:
            screenshot_path = "./Screenshots/test_nested_iframe_failure.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Assertion failed: {e}")
            self.logger.error(f"Screenshot captured at: {screenshot_path}")
            raise

        except Exception as e:
            screenshot_path = "./Screenshots/test_nested_iframe_exception.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"An unexpected error occurred: {e}")
            self.logger.error(f"Screenshot captured at: {screenshot_path}")
            raise

        finally:
            try:
                self.driver.switch_to.default_content()
                self.logger.info("Switched back to main content successfully in finally block.")
            except Exception as e:
                self.logger.error(f"Failed to switch back to main content in finally block: {e}")

        self.logger.info("========== Finished test: test_nested_iframe ==========")

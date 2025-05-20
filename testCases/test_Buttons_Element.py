import json
import pytest
from pageObjects.HomePage import HomePage
from pageObjects.ElementsPage import ElementsPage
from unititlies.customlogger import LogGen
from unititlies.readProperties import ReadConfig


class TestButtonElements:
    # Get base URL from configuration
    baseURL = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def setup_method(self, setup):
        """
        This setup method runs automatically before each test method.
        It performs the following actions:
        - Initializes the WebDriver.
        - Sets an implicit wait.
        - Maximizes the browser window.
        - Navigates to the base URL.
        - Loads test data from a JSON file.
        - Initializes page objects.
        - Navigate to the 'Elements' section and click on the 'Buttons' option.
        """

        # Logging the start of the test
        self.logger.info("********** Starting Test: TestElementsPage **********")
        self.logger.info("Initializing browser setup...")

        # Setting up WebDriver
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.logger.info(f"Navigated to URL: {self.baseURL}")

        # Load test data from JSON file
        try:
            with open("./TestData/elements_page.json", "r") as file:
                self.data = json.load(file)
                self.logger.info("Test data loaded successfully from elements_page.json")
        except Exception as e:
            self.logger.error(f"Failed to load test data: {str(e)}")
            raise

        self.logger.info("Setup method completed successfully.")

        # Initialize Page Object Models for Home and Elements pages
        home_page = HomePage(self.driver)
        elements_page = ElementsPage(self.driver)

        # Navigate to 'Elements' section from the home page
        home_page.click_on_elements_card()
        self.logger.info("Step 1: Clicked on 'Elements' card.")

        # Navigate to 'Buttons' option on the Elements page
        elements_page.click_on_buttons()
        self.logger.info("Step 2: Clicked on 'Buttons' option.")

    @pytest.mark.skip(reason="Skipping this test case for now.")
    def test_Double_Click_Button(self):
        """
        Test case to verify the functionality of the 'Double Click' button.
        """

        self.logger.info("********** Test Case: test_Double_Click_Button **********")
        self.logger.info("Step 1: Initializing ElementsPage object...")

        elements_page = ElementsPage(self.driver)

        try:
            self.logger.info("Step 2: Clicking on 'Double Click' button...")
            elements_page.click_on_double_click_button()

            self.logger.info("Step 3: Retrieving success message after double click...")
            success_message = elements_page.get_double_clicks_success_message_text()
            expected_message = self.data["buttonClicked"]["doubleClickMessage"]

            self.logger.info(
                f"Step 4: Verifying success message...\nExpected: '{expected_message}'\nActual: '{success_message}'")
            assert success_message is not None, "No success message found after Double Click."
            assert success_message == expected_message, f"Expected: '{expected_message}', Got: '{success_message}'"

            self.logger.info("Test Passed: Double click button displayed correct success message.")

        except AssertionError as e:
            self.logger.error(f"Test Failed: {e}")
            screenshot_path = "./Screenshots/test_Double_Click_Button_failure.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved at: {screenshot_path}")
            raise

        except Exception as ex:
            self.logger.error(f"An unexpected error occurred: {ex}")
            screenshot_path = "./Screenshots/test_Double_Click_Button_unexpected_error.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved at: {screenshot_path}")
            raise

        finally:
            self.logger.info("Test case completed.")
            self.driver.quit()

    # @pytest.mark.skip(reason="Skipping this test case for now.")
    def test_Right_Click_Button(self):
        """
        Test case to verify the functionality of the 'Right Click' button.
        """

        test_name = "test_Right_Click_Button"
        self.logger.info(f"********** Test Case: {test_name} **********")
        self.logger.info("Step 1: Initializing ElementsPage object...")

        elements_page = ElementsPage(self.driver)

        try:
            # Step 2: Perform right click action
            self.logger.info("Step 2: Performing right click on the 'Right Click' button...")
            elements_page.click_on_right_click_button()

            # Step 3: Retrieve the success message shown after right click
            self.logger.info("Step 3: Retrieving success message after right click...")
            success_message = elements_page.get_right_clicks_success_message_text()
            expected_message = self.data["buttonClicked"]["rightClickMessage"]

            # Step 4: Validate the actual success message with the expected one
            self.logger.info(
                f"Step 4: Verifying success message...\nExpected: '{expected_message}'\nActual: '{success_message}'"
            )
            assert success_message == expected_message, f"Expected: '{expected_message}', Got: '{success_message}'"

            self.logger.info("Test Passed: Right click button displayed the correct success message.")

        except AssertionError as e:
            # Log assertion error and save screenshot
            self.logger.error(f"Test Failed (Assertion Error): {e}")
            screenshot_path = f"./Screenshots/{test_name}_failure.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved at: {screenshot_path}")
            raise

        except Exception as ex:
            # Log unexpected exceptions and save screenshot
            self.logger.error(f"An unexpected error occurred: {ex}")
            screenshot_path = f"./Screenshots/{test_name}_unexpected_error.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved at: {screenshot_path}")
            raise

        finally:
            self.logger.info(f"{test_name} completed.")
            self.driver.quit()

    @pytest.mark.skip(reason="Skipping this test case for now.")
    def test_Dynamic_Click_Button(self):
        """
        Test case to verify the functionality of the 'Dynamic Click' button.
        This test performs a dynamic click (left click) on the target button,
        retrieves the success message, and validates it against the expected result.
        """

        # Set the test name for consistent use in logs and screenshot naming
        test_name = "test_Dynamic_Click_Button"

        # Step 1: Log test start and initialize ElementsPage object
        self.logger.info(f"\n{'*' * 10} Test Case: {test_name} {'*' * 10}")
        self.logger.info("Step 1: Initializing ElementsPage object...")
        elements_page = ElementsPage(self.driver)

        try:
            # Step 2: Perform dynamic click action
            self.logger.info("Step 2: Performing dynamic (left) click on the 'Click Me' button...")
            elements_page.click_on_click_me_button()

            # Step 3: Retrieve the success message shown after the click
            self.logger.info("Step 3: Retrieving success message after the dynamic click...")
            success_message = elements_page.get_dynamic_clicks_success_message_text()

            # Step 4: Load expected message from test data
            expected_message = self.data["buttonClicked"]["dynamicClickMessage"]
            self.logger.info(
                f"Step 4: Validating success message...\nExpected: '{expected_message}'\nActual: '{success_message}'"
            )

            # Step 5: Assertions to validate the success message
            assert success_message is not None, "No success message found after the dynamic click."
            assert success_message == expected_message, (
                f"Success message mismatch.\nExpected: '{expected_message}'\nActual: '{success_message}'"
            )

            # Log test success
            self.logger.info("Test Passed: Dynamic click button displayed the correct success message.")

        except AssertionError as e:
            # Log assertion error and take a screenshot for debugging
            self.logger.error(f"Test Failed (Assertion Error): {e}")
            screenshot_path = f"./Screenshots/{test_name}_failure.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved at: {screenshot_path}")
            raise

        except Exception as ex:
            # Log any unexpected exceptions and take a screenshot
            self.logger.error(f"An unexpected error occurred: {ex}")
            screenshot_path = f"./Screenshots/{test_name}_unexpected_error.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved at: {screenshot_path}")
            raise

        finally:
            # Final log indicating test completion and cleanup
            self.logger.info(f"{test_name} completed. Closing the browser.")
            self.driver.quit()

    @pytest.mark.skip(reason="Skipping this test case for now.")
    def test_All_Click_Buttons(self):
        """
        Consolidated test case to verify the functionality of:
        - Double Click button
        - Right Click button
        - Dynamic Click (Click Me) button
        Each button is clicked, its corresponding success message is retrieved,
        and the message is validated against the expected result.
        """

        test_name = "test_All_Click_Buttons"
        self.logger.info(f"********** Test Case: {test_name} **********")
        self.logger.info("Step 1: Initializing ElementsPage object...")

        elements_page = ElementsPage(self.driver)

        try:
            # Step 2: Click on 'Double Click' button and verify a message
            self.logger.info("Step 2: Clicking on 'Double Click' button...")
            elements_page.click_on_double_click_button()

            self.logger.info("Retrieving success message for 'Double Click'...")
            double_click_message = elements_page.get_double_clicks_success_message_text()
            expected_double_click = self.data["buttonClicked"]["doubleClickMessage"]

            self.logger.info(
                f"Verifying message...\nExpected: '{expected_double_click}'\nActual: '{double_click_message}'")
            assert double_click_message is not None, "No success message for Double Click."
            assert double_click_message == expected_double_click, f"Expected: '{expected_double_click}', Got: '{double_click_message}'"

            # Step 3: Click on 'Right Click' button and verify a message
            self.logger.info("Step 3: Clicking on 'Right Click' button...")
            elements_page.click_on_right_click_button()

            self.logger.info("Retrieving success message for 'Right Click'...")
            right_click_message = elements_page.get_right_clicks_success_message_text()
            expected_right_click = self.data["buttonClicked"]["rightClickMessage"]

            self.logger.info(
                f"Verifying message...\nExpected: '{expected_right_click}'\nActual: '{right_click_message}'")
            assert right_click_message is not None, "No success message for Right Click."
            assert right_click_message == expected_right_click, f"Expected: '{expected_right_click}', Got: '{right_click_message}'"

            # Step 4: Click on 'Click Me' button and verify message
            self.logger.info("Step 4: Clicking on 'Click Me' button...")
            elements_page.click_on_click_me_button()

            self.logger.info("Retrieving success message for 'Click Me'...")
            dynamic_click_message = elements_page.get_dynamic_clicks_success_message_text()
            expected_dynamic_click = self.data["buttonClicked"]["dynamicClickMessage"]

            self.logger.info(
                f"Verifying message...\nExpected: '{expected_dynamic_click}'\nActual: '{dynamic_click_message}'")
            assert dynamic_click_message is not None, "No success message for Dynamic Click."
            assert dynamic_click_message == expected_dynamic_click, f"Expected: '{expected_dynamic_click}', Got: '{dynamic_click_message}'"

            self.logger.info("Test Passed: All click buttons displayed correct success messages.")

        except AssertionError as e:
            self.logger.error(f"Test Failed (Assertion Error): {e}")
            screenshot_path = f"./Screenshots/{test_name}_failure.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved at: {screenshot_path}")
            raise

        except Exception as ex:
            self.logger.error(f"An unexpected error occurred: {ex}")
            screenshot_path = f"./Screenshots/{test_name}_unexpected_error.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved at: {screenshot_path}")
            raise

        finally:
            self.logger.info(f"{test_name} completed. Closing the browser.")
            self.driver.quit()

    #  ============================ Parameterized Tests ===========================
    @pytest.mark.parametrize("click_method, get_message_method, expected_key", [
        ("click_on_double_click_button", "get_double_clicks_success_message_text", "doubleClickMessage"),
        ("click_on_right_click_button", "get_right_clicks_success_message_text", "rightClickMessage"),
        ("click_on_click_me_button", "get_dynamic_clicks_success_message_text", "dynamicClickMessage")
    ])
    @pytest.mark.skip(reason="Skipping this test case for now.")
    def test_Click_Buttons(self, click_method, get_message_method, expected_key):
        """
        Parameterized test case to verify the functionality of:
        - Double Click button
        - Right Click button
        - Dynamic Click (Click Me) button
        Each button is clicked, its corresponding success message is retrieved,
        and the message is validated against the expected result.
        """

        test_name = f"test_Click_Buttons_{expected_key}"
        self.logger.info(f"********** Test Case: {test_name} **********")
        self.logger.info("Step 1: Initializing ElementsPage object...")

        elements_page = ElementsPage(self.driver)

        try:
            # Step 2: Perform the click action
            self.logger.info(f"Step 2: Performing click action using method: {click_method}...")
            getattr(elements_page, click_method)()

            # Step 3: Retrieve the success message
            self.logger.info("Step 3: Retrieving success message...")
            actual_message = getattr(elements_page, get_message_method)()
            expected_message = self.data["buttonClicked"][expected_key]

            # Step 4: Validate the message
            self.logger.info(
                f"Step 4: Verifying message...\nExpected: '{expected_message}'\nActual: '{actual_message}'")
            assert actual_message is not None, f"No success message found for {expected_key}."
            assert actual_message == expected_message, f"Expected: '{expected_message}', Got: '{actual_message}'"

            self.logger.info(f"Test Passed: {expected_key} button displayed correct success message.")

        except AssertionError as e:
            self.logger.error(f"Test Failed (Assertion Error): {e}")
            screenshot_path = f"./Screenshots/{test_name}_failure.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved at: {screenshot_path}")
            raise

        except Exception as ex:
            self.logger.error(f"An unexpected error occurred: {ex}")
            screenshot_path = f"./Screenshots/{test_name}_unexpected_error.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved at: {screenshot_path}")
            raise

        finally:
            self.logger.info(f"{test_name} completed. Closing the browser.")
            self.driver.quit()
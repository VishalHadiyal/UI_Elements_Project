import json
import time
import pytest
from pageObjects.HomePage import HomePage
from pageObjects.ElementsPage import ElementsPage
from unititlies.customlogger import LogGen
from unititlies.readProperties import ReadConfig


class TestLinks:
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

        elements_page.click_on_web_table()
        self.logger.info("Clicked on 'Web Tables' under the Elements section.")

        yield  # Yield control to the test method

        # ---------- TEAR DOWN ----------
        self.logger.info("Closing browser after test execution.")
        self.driver.quit()

    @pytest.mark.smoke
    def test_Count_Of_Links(self):
        test_name = "test_Count_Of_Links"
        self.logger.info(f"Starting test: {test_name}")

        try:
            # Instantiate ElementsPage object
            element_page = ElementsPage(self.driver)

            # Navigate to the 'Links' section
            self.logger.info("Clicking on the 'Links' section")
            element_page.click_on_links()
            time.sleep(2)  # Wait for the page to load (replace with explicit wait in real-world tests)

            # Count all <a> tags on the current page
            self.logger.info("Counting all <a> tags on the current page")
            link_count = element_page.get_links_count()
            self.logger.info(f"Total number of links on the page: {link_count}")

            # Assert the count against expected value
            expected_count = self.data["linksTest"]["totalCountOfLinks"]
            assert link_count == expected_count, f"Expected {expected_count} links, but found {link_count}"

            self.logger.info(f"Test {test_name} passed successfully.")

        except AssertionError as ae:
            # Capture screenshot on assertion failure
            screenshot_path = f"./Screenshots/{test_name}_assertion_failed.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Assertion failed in {test_name}: {ae}")
            self.logger.error(f"Screenshot saved at: {screenshot_path}")
            raise

        except Exception as e:
            # General exception logging
            self.logger.error(f"An unexpected error occurred in {test_name}: {e}")
            raise

        finally:
            self.logger.info(f"Ending test: {test_name}")

    @pytest.mark.smoke
    def test_Simple_Link(self):
        test_name = "test_Simple_Link"
        self.logger.info(f"Starting test: {test_name}")

        try:
            # Instantiate ElementsPage object
            element_page = ElementsPage(self.driver)

            # Navigate to the 'Links' section
            self.logger.info("Clicking on the 'Links' section")
            element_page.click_on_links()
            time.sleep(2)  # Wait for the page to load (replace with explicit wait in real-world tests)

            # Click on the simple link
            self.logger.info("Clicking on the simple link")
            element_page.click_on_simple_link()
            # Switch to the new window/tab
            windows = self.driver.window_handles
            if len(windows) > 1:
                self.driver.switch_to.window(windows[1])
            current_url = self.driver.current_url
            expected_url = self.data["linksTest"]["simpleLinkURL"]
            assert current_url == expected_url, f"Expected URL {expected_url}, but found {current_url}"

            self.logger.info(f"Test {test_name} passed successfully.")

        except AssertionError as ae:
            # Capture screenshot on assertion failure
            screenshot_path = f"./Screenshots/{test_name}_assertion_failed.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Assertion failed in {test_name}: {ae}")
            self.logger.error(f"Screenshot saved at: {screenshot_path}")
            raise

        except Exception as e:
            # General exception logging
            self.logger.error(f"An unexpected error occurred in {test_name}: {e}")
            raise

        finally:
            self.logger.info(f"Ending test: {test_name}")

    @pytest.mark.smoke
    def test_Dynamic_Link(self):
        test_name = "test_Dynamic_Link"
        self.logger.info(f"Starting test: {test_name}")

        try:
            # Instantiate ElementsPage object
            element_page = ElementsPage(self.driver)

            # Navigate to the 'Links' section
            self.logger.info("Clicking on the 'Links' section")
            element_page.click_on_links()
            time.sleep(2)  # Wait for the page to load (replace with explicit wait in real-world tests)

            # Click on the dynamic link
            self.logger.info("Clicking on the dynamic link")
            element_page.click_on_dynamic_link()
            # Switch to the new window/tab
            windows = self.driver.window_handles
            if len(windows) > 1:
                self.driver.switch_to.window(windows[1])
            current_url = self.driver.current_url
            expected_url = self.data["linksTest"]["dynamicLinkURL"]
            assert current_url == expected_url, f"Expected URL {expected_url}, but found {current_url}"

            self.logger.info(f"Test {test_name} passed successfully.")

        except AssertionError as ae:
            # Capture screenshot on assertion failure
            screenshot_path = f"./Screenshots/{test_name}_assertion_failed.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Assertion failed in {test_name}: {ae}")
            self.logger.error(f"Screenshot saved at: {screenshot_path}")
            raise

        except Exception as e:
            # General exception logging
            self.logger.error(f"An unexpected error occurred in {test_name}: {e}")
            raise

        finally:
            self.logger.info(f"Ending test: {test_name}")

    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "link_action, expected_status_key",
        [
            ("create", "Created"),
            ("no_content", "NoContent"),
            ("moved", "Moved"),
            ("bad_request", "BadRequest"),
            ("unauthorized", "Unauthorized"),
            ("forbidden", "Forbidden"),
            ("not_found", "NotFound"),
        ]
    )
    def test_link_responses(self, link_action, expected_status_key):
        test_name = f"test_link_{link_action}"
        self.logger.info(f"========== Starting Test: {test_name} ==========")

        try:
            # Instantiate the ElementsPage object
            self.logger.debug("Instantiating ElementsPage object.")
            element_page = ElementsPage(self.driver)

            # Step 1: Navigate to the Links section
            self.logger.info("Navigating to the 'Links' section.")
            element_page.click_on_links()
            self.logger.debug("Navigation to 'Links' section successful.")

            # Step 2: Perform the action based on the link_action parameter
            self.logger.info(f"Performing action for link: '{link_action}'")
            if link_action == "create":
                element_page.click_on_create_link()
            elif link_action == "no_content":
                element_page.click_on_no_content_link()
            elif link_action == "moved":
                element_page.click_on_moved_link()
            elif link_action == "bad_request":
                element_page.click_on_bad_request_link()
            elif link_action == "unauthorized":
                element_page.click_on_unauthorized_link()
            elif link_action == "forbidden":
                element_page.click_on_forbidden_link()
            elif link_action == "not_found":
                element_page.click_on_not_found_link()
            else:
                error_msg = f"Unsupported link action: {link_action}"
                self.logger.error(error_msg)
                raise ValueError(error_msg)

            # Step 3: Fetch the response status code
            self.logger.info("Fetching response status code from UI.")
            status_code = element_page.get_response_status_code()
            self.logger.debug(f"Received status code: {status_code}")

            # Step 4: Validate the response status code with expected value
            expected_status = self.data["linksTest"][expected_status_key]
            self.logger.info(f"Validating response code. Expected: {expected_status}, Actual: {status_code}")
            assert status_code == expected_status, (
                f"Expected status code {expected_status}, but got {status_code}"
            )

            self.logger.info(f" Test {test_name} passed successfully.")

        except AssertionError as ae:
            # Log assertion errors and take screenshot
            screenshot_path = f"./Screenshots/{test_name}_assertion_failed.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f" Assertion failed in {test_name}: {ae}")
            self.logger.error(f"Screenshot captured at: {screenshot_path}")
            raise

        except Exception as e:
            # Log unexpected exceptions
            self.logger.error(f" Unexpected error occurred in {test_name}: {e}")
            raise

        finally:
            self.logger.info(f"========== Ending Test: {test_name} ==========\n")

    @pytest.mark.smoke
    def test_Image_Is_Displayed(self):
        test_name = "test_Image_Is_Displayed"
        self.logger.info(
            f"[START] {test_name}: Verifying if the image is displayed on the 'Broken Links - Images' page.")

        try:
            # Instantiate ElementsPage object
            element_page = ElementsPage(self.driver)
            self.logger.info("ElementsPage initialized successfully.")

            # Navigate to the 'Broken Links - Images' section
            self.logger.info("Navigating to the 'Broken Links - Images' section.")
            element_page.click_on_broken_links_images()

            # Wait for the page to load (should be replaced with explicit waits in real-world scenarios)
            time.sleep(2)

            # Check if the image is displayed
            self.logger.info("Checking if the image is displayed.")
            image_displayed = element_page.is_image_displayed()

            # Assertion to verify if image is displayed
            assert image_displayed, "Image is not displayed on the page."
            self.logger.info("Image is displayed successfully.")

        except AssertionError as ae:
            # Log assertion error and take screenshot
            screenshot_path = f"./Screenshots/{test_name}_assertion_failed.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"[ASSERTION FAILED] {test_name}: {ae}")
            self.logger.error(f"Screenshot saved at: {screenshot_path}")
            raise

        except Exception as e:
            # Log any other unexpected exceptions
            self.logger.error(f"[EXCEPTION] An unexpected error occurred in {test_name}: {e}")
            raise

        finally:
            self.logger.info(f"[END] {test_name}: Test completed.")

    @pytest.mark.smoke
    def test_Broken_Image_Is_Displayed(self):
        test_name = "test_Broken_Image_Is_Displayed"
        self.logger.info(
            f"[START] {test_name}: Verifying if the image is correctly loaded on the 'Broken Links - Images' page.")

        try:
            # Instantiate ElementsPage object
            element_page = ElementsPage(self.driver)
            self.logger.info("ElementsPage initialized successfully.")

            # Navigate to the 'Broken Links - Images' section
            self.logger.info("Navigating to the 'Broken Links - Images' section.")
            element_page.click_on_broken_links_images()

            # Check if the image is NOT broken (i.e., loaded correctly)
            self.logger.info("Checking if the image is correctly loaded.")
            is_image_broken = element_page.is_broken_image_displayed()

            # Assert that the image is NOT broken
            assert not is_image_broken, "The image appears to be broken on the page."
            self.logger.info("The image is loaded and displayed correctly.")

        except AssertionError as ae:
            screenshot_path = f"./Screenshots/{test_name}_assertion_failed.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"[ASSERTION FAILED] {test_name}: {ae}")
            self.logger.error(f"Screenshot saved at: {screenshot_path}")
            raise

        except Exception as e:
            self.logger.error(f"[EXCEPTION] An unexpected error occurred in {test_name}: {e}")
            raise

        finally:
            self.logger.info(f"[END] {test_name}: Test completed.")

    @pytest.mark.smoke
    def test_Valid_Link(self):
        test_name = "test_Valid_Link"
        self.logger.info(
            f"[START] {test_name}: Verifying if the image is correctly loaded on the 'Broken Links - Images' page.")

        try:
            # Step 1: Instantiate the ElementsPage object
            self.logger.info("Instantiating the ElementsPage object.")
            element_page = ElementsPage(self.driver)
            self.logger.info("ElementsPage initialized successfully.")

            # Step 2: Navigate to the 'Broken Links - Images' section
            self.logger.info("Navigating to the 'Broken Links - Images' section.")
            element_page.click_on_broken_links_images()

            # Step 3: Click on a valid image link to verify its behavior
            self.logger.info("Clicking on a valid image link to verify it redirects to a valid URL.")
            element_page.click_on_valid_link()

            # Step 4: Capture the current URL and compare with expected
            actual_url = self.driver.current_url
            expected_url = self.data["linksTest"]["ValidURL"]
            self.logger.info(f"Expected URL: {expected_url}")
            self.logger.info(f"Actual URL after clicking image: {actual_url}")

            # Assertion: Check if the image redirection works correctly
            assert actual_url == expected_url, f"Expected URL '{expected_url}' but got '{actual_url}'"
            self.logger.info("The image is loaded and displayed correctly (valid link working).")

        except AssertionError as ae:
            # Handle assertion failure with screenshot
            screenshot_path = f"./Screenshots/{test_name}_assertion_failed.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"[ASSERTION FAILED] {test_name}: {ae}")
            self.logger.error(f"Screenshot saved at: {screenshot_path}")
            raise

        except Exception as e:
            # Handle unexpected exceptions
            self.logger.error(f"[EXCEPTION] An unexpected error occurred in {test_name}: {e}")
            raise

        finally:
            # Test end log
            self.logger.info(f"[END] {test_name}: Test completed.")

    @pytest.mark.smoke
    def test_Broken_Link(self):
        test_name = "test_Broken_Link"
        self.logger.info(
            f"[START] {test_name}: Verifying if a valid image link redirects to the correct URL on the 'Broken Links - Images' page.")

        try:
            # Step 1: Instantiate the ElementsPage object
            self.logger.info("Step 1: Instantiating the ElementsPage object.")
            element_page = ElementsPage(self.driver)
            self.logger.info("ElementsPage object created successfully.")

            # Step 2: Navigate to the 'Broken Links - Images' section
            self.logger.info("Step 2: Navigating to the 'Broken Links - Images' section of the application.")
            element_page.click_on_broken_links_images()
            self.logger.info("Successfully navigated to the 'Broken Links - Images' page.")

            # Step 3: Click on a valid image link
            self.logger.info("Step 3: Clicking on a valid image link to test redirection.")
            element_page.click_on_broken_link()
            self.logger.info("Clicked on the image link successfully.")

            # Step 4: Get the current URL after the click
            actual_url = self.driver.current_url
            expected_url = self.data["linksTest"]["BrokenLink"]
            self.logger.info(f"Step 4: Captured actual URL after redirection: {actual_url}")
            self.logger.info(f"Expected URL: {expected_url}")

            # Step 5: Validate the URL
            assert actual_url == expected_url, f"Expected URL '{expected_url}' but got '{actual_url}'"
            self.logger.info(
                "Assertion passed: The image redirected to the correct URL. The link is valid and working.")

        except AssertionError as ae:
            # Capture screenshot on assertion failure
            screenshot_path = f"./Screenshots/{test_name}_assertion_failed.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"[ASSERTION FAILED] {test_name}: {ae}")
            self.logger.error(f"Screenshot saved at: {screenshot_path}")
            raise

        except Exception as e:
            # Log unexpected errors
            self.logger.error(f"[EXCEPTION] An unexpected error occurred during {test_name}: {e}")
            raise

        finally:
            # Final log entry to indicate test completion
            self.logger.info(f"[END] {test_name}: Test execution completed.")

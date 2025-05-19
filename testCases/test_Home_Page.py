import json
import pytest
from selenium.common import NoSuchElementException
from pageObjects.HomePage import HomePage
from unititlies.customlogger import LogGen
from unititlies.readProperties import ReadConfig
from datetime import datetime


class TestHomePage:
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
        self.logger.info("********** Starting Test: TestHomePage **********")
        self.logger.info("Initializing browser setup...")

        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.logger.info(f"Navigated to URL: {self.baseURL}")

        # Load test data from JSON file
        try:
            with open("./TestData/home_page.json", "r") as file:
                self.data = json.load(file)
                self.logger.info("Test data loaded successfully from home_page.json")
        except Exception as e:
            self.logger.error(f"Failed to load test data: {str(e)}")
            raise

    @pytest.mark.ui
    def test_home_page_title(self):
        """
        This test verifies:
        1. That the current URL matches the expected URL from test data.
        2. That the page title matches the expected title from test data.
        """

        # Retrieve expected values from test data
        expected_url = self.data["url"]
        expected_title = self.data["pageTitle"]

        # Capture actual values from the current page
        actual_url = self.driver.current_url
        actual_title = self.driver.title

        # Log the details for debugging purposes
        self.logger.info("Validating Home Page URL and Title...")
        self.logger.info(f"Expected URL: {expected_url} | Actual URL: {actual_url}")
        self.logger.info(f"Expected Title: {expected_title} | Actual Title: {actual_title}")

        # Define directory to store screenshots in case of failure
        screenshot_dir = "./Screenshots"
        # Create a unique timestamp for the screenshot filenames
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # ---------------- URL Validation ----------------
        try:
            # Assert that the actual URL matches the expected URL
            assert actual_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"
            self.logger.info("URL validation PASSED.")
        except AssertionError as ae:
            # If the URL validation fails, take a screenshot and log the error
            screenshot_path = f"{screenshot_dir}/test_homepage_title_url_fail_{timestamp}.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"URL validation FAILED: {ae}")
            self.logger.info(f"Screenshot saved to {screenshot_path}")
            raise  # Re-raise the exception to mark the test as failed

        # ---------------- Title Validation ----------------
        try:
            # Assert that the actual page title matches the expected title
            assert actual_title == expected_title, f"Expected Title: {expected_title}, Actual Title: {actual_title}"
            self.logger.info("Title validation PASSED.")
        except AssertionError as ae:
            # If the title validation fails, take a screenshot and log the error
            screenshot_path = f"{screenshot_dir}/test_homepage_title_title_fail_{timestamp}.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Title validation FAILED: {ae}")
            self.logger.info(f"Screenshot saved to {screenshot_path}")
            raise  # Re-raise the exception to mark the test as failed
        finally:
            # Close the browser after the test
            self.driver.quit()
            self.logger.info("Browser closed.")
            self.logger.info("********** Test Completed: TestHomePage **********")

    @pytest.mark.ui
    def test_home_page_logo_displayed(self):
        """
        This test verifies that the logo is displayed on the home page.
        """
        self.logger.info("Validating Home Page Logo...")

        HP = HomePage(self.driver)
        logo_displayed = HP.logo_is_displayed()
        self.logger.info(f"Logo displayed: {logo_displayed}")
        assert logo_displayed, "Logo is not displayed on the home page."
        self.logger.info("Logo validation PASSED.")
        # Take a screenshot if the logo is not displayed
        if not logo_displayed:
            screenshot_path = f"./Screenshots/test_homepage_logo_fail.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error("Logo validation FAILED.")
            self.logger.info(f"Screenshot saved to {screenshot_path}")
        else:
            self.logger.info("Logo validation PASSED.")

        # Close the browser after the test
        self.driver.quit()
        self.logger.info("Browser closed.")
        self.logger.info("********** Test Completed: TestHomePage **********")

    @pytest.mark.functional
    def test_home_page_join_now_button(self):
        """
        Test Case: Verify 'Join Now' Button on Home Page
        ------------------------------------------------
        This test ensures that the 'Join Now' button is present and clickable on the home page,
        and that clicking it opens a new tab with the correct page title. After validation, the
        new tab is closed and the test confirms the title of the original tab.
        """
        self.logger.info("TEST STARTED: Validate 'Join Now' button on the home page.")

        # Initialize the HomePage object with the current driver instance
        HP = HomePage(self.driver)

        try:
            # Attempt to click the 'Join Now' button
            self.logger.info("Clicking the 'Join Now' button.")
            HP.clicks_on_join_now_button()

            # Fetch all currently open browser tabs
            tabs = self.driver.window_handles
            self.logger.info(f"Number of open tabs after click: {len(tabs)}")

            # Ensure a new tab has opened
            if len(tabs) <= 1:
                raise NoSuchElementException("New tab did not open after clicking 'Join Now'.")

            # Store references to the original and new tabs
            original_tab = tabs[0]
            new_tab = tabs[1]

            # Switch control to the newly opened tab
            self.driver.switch_to.window(new_tab)
            self.logger.info("Switched to the new browser tab successfully.")

            # Get the title of the new tab and validate it against expected title
            actual_title = self.driver.title
            expected_title = self.data["pageTitleJoinNow"]
            self.logger.info(f"Expected page title: '{expected_title}'")
            self.logger.info(f"Actual page title in new tab: '{actual_title}'")

            # Assert title match
            assert actual_title == expected_title, (
                f"Title mismatch: Expected '{expected_title}', but got '{actual_title}'"
            )

            self.logger.info("Title of 'Join Now' tab is as expected.")

            # Close the new tab after validation
            self.driver.close()
            self.logger.info("New tab closed successfully.")

            # Switch back to the original tab
            self.driver.switch_to.window(original_tab)
            self.logger.info("Switched back to the original browser tab.")

            # Log the title of the original tab
            original_tab_title = self.driver.title
            self.logger.info(f"Original tab title after switching back: '{original_tab_title}'")

            self.logger.info("TEST PASSED: 'Join Now' button is functional and redirects correctly.")

        except AssertionError as ae:
            # Handle assertion failures with screenshot and detailed log
            screenshot_path = "./Screenshots/test_homepage_join_now_assertion_fail.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"ASSERTION ERROR: {ae}")
            self.logger.info(f"Screenshot saved at: {screenshot_path}")
            raise

        except NoSuchElementException as ne:
            # Handle element not found error with screenshot and detailed log
            screenshot_path = "./Screenshots/test_homepage_join_now_not_found.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"ELEMENT NOT FOUND: {ne}")
            self.logger.info(f"Screenshot saved at: {screenshot_path}")
            raise

        except Exception as e:
            # Log any other unexpected exceptions
            self.logger.error(f"UNEXPECTED ERROR during 'Join Now' button test: {str(e)}")
            raise

        finally:
            # Final log entries for test completion and cleanup
            self.logger.info("TEST COMPLETED: 'Join Now' button test.")
            self.driver.quit()
            self.logger.info("Browser session closed.")
            self.logger.info("********** Test Completed: TestHomePage **********")

    @pytest.mark.ui
    def test_number_of_links_on_homepage(self):
        """
        Test Case: Verify the number of links on the Home Page
        -------------------------------------------------------
        This test checks if the number of links present on the home page matches the expected value.
        """
        self.logger.info("========== TEST STARTED: Validate number of links on the Home Page ==========")

        # Initialize HomePage object with current driver instance
        homepage = HomePage(self.driver)

        # Retrieve expected link count from data source (e.g., config file, test data, etc.)
        expected_link_count = self.data["totalLinks"]

        try:
            # Fetch actual number of links on the home page
            actual_link_count = homepage.get_total_links_count()
            self.logger.info(f"Actual number of links found on the homepage: {actual_link_count}")
            self.logger.info(f"Expected number of links from test data: {expected_link_count}")

            # Assertion to compare actual and expected link count
            assert actual_link_count == expected_link_count, (
                f"Expected {expected_link_count} links, but found {actual_link_count}."
            )

            self.logger.info("TEST PASSED: Number of links on the home page is as expected.")

        except AssertionError as ae:
            # Capture screenshot on assertion failure
            screenshot_path = "./Screenshots/test_homepage_link_count_assertion_fail.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f" ASSERTION ERROR: {ae}")
            self.logger.info(f"Screenshot captured at: {screenshot_path}")
            raise

        except Exception as e:
            # Handle unexpected exceptions
            self.logger.exception(f" UNEXPECTED ERROR occurred during the link count test: {str(e)}")
            raise

        finally:
            # Clean up actions and logging
            self.logger.info("Closing the browser session.")
            self.driver.quit()
            self.logger.info("========== TEST COMPLETED: Validate number of links on the Home Page ==========")

    @pytest.mark.ui
    def test_home_page_cards_count(self):
        """
        Test Case: Verify the number of cards on the Home Page
        -------------------------------------------------------
        This test checks if the number of cards present on the home page matches the expected value.
        """
        self.logger.info("========== TEST STARTED: Validate number of cards on the Home Page ==========")

        # Initialize HomePage object with current driver instance
        homepage = HomePage(self.driver)

        # Retrieve expected card count from data source (e.g., config file, test data, etc.)
        expected_card_count = self.data["totalCards"]

        try:
            # Fetch actual number of cards on the home page
            actual_card_count = homepage.get_cards_count()
            self.logger.info(f"Actual number of cards found on the homepage: {actual_card_count}")
            self.logger.info(f"Expected number of cards from test data: {expected_card_count}")

            # Assertion to compare actual and expected card count
            assert actual_card_count == expected_card_count, (
                f"Expected {expected_card_count} cards, but found {actual_card_count}."
            )

            self.logger.info("TEST PASSED: Number of cards on the home page is as expected.")

        except AssertionError as ae:
            # Capture screenshot on assertion failure
            screenshot_path = "./Screenshots/test_homepage_cards_count_assertion_fail.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f" ASSERTION ERROR: {ae}")
            self.logger.info(f"Screenshot captured at: {screenshot_path}")
            raise

        except Exception as e:
            # Handle unexpected exceptions
            self.logger.exception(f" UNEXPECTED ERROR occurred during the cards count test: {str(e)}")
            raise

        finally:
            # Clean up actions and logging
            self.logger.info("Closing the browser session.")
            self.driver.quit()
            self.logger.info("========== TEST COMPLETED: Validate number of cards on the Home Page ==========")

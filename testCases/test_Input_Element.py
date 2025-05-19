import json
import time

import pytest
from selenium.common import NoSuchElementException
from pageObjects.HomePage import HomePage
from pageObjects.ElementsPage import ElementsPage
from unititlies.customlogger import LogGen
from unititlies.readProperties import ReadConfig


class TestInputElementsPage:
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

    def test_element_page_text(self):
        """
        Test case to verify the text of the element on the Elements page.
        """
        self.logger.info("********** Test Case: test_element_page_text : STARTING **********")
        self.logger.info("Starting test for element page text...")

        # Initialize HomePage and ElementsPage objects
        self.home_page = HomePage(self.driver)
        self.elements_page = ElementsPage(self.driver)

        # Click on the "Elements" link
        self.home_page.click_on_elements_card()

        # Get the text of the element on the Elements page
        try:
            text_element = self.elements_page.get_text_element_page()
            assert text_element == self.data["elementsPageText"], \
                f"Expected: {self.data['elementsPageText']}, but got: {text_element}"
            self.logger.info("Test passed: Element page text is correct.")
        except NoSuchElementException:
            self.logger.error("Element not found on the page.")
            assert False, "Element not found on the page."
        except AssertionError as ae:
            screenshot_path = "./Screenshots/test_element_page_text_assertion_fail.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"ASSERTION ERROR: {ae}")
            self.logger.info(f"Screenshot captured at: {screenshot_path}")
            assert False, str(ae)
        finally:
            self.logger.info("Test completed for element page text.")
            self.driver.quit()
            self.logger.info("Browser closed.")
            self.logger.info("********** Test Case: test_element_page_text : END **********")

    def test_text_box_element(self):
        """
        Test case to verify the functionality of the Text Box element.
        Fills out the form and checks that submitted data is correctly displayed.
        """
        self.logger.info("********** Test Case: test_text_box_element : STARTING **********")
        self.logger.info("Starting test for Text Box element...")

        # Initialize page objects
        self.home_page = HomePage(self.driver)
        self.elements_page = ElementsPage(self.driver)

        # Step 1: Click on the 'Elements' card
        self.logger.info("Clicking on the 'Elements' card...")
        self.home_page.click_on_elements_card()

        # Step 2: Click on the 'Text Box' option
        self.logger.info("Attempting to click on 'Text Box' option...")
        try:
            self.elements_page.click_on_text_box()
            self.logger.info("Clicked on 'Text Box' option.")
        except NoSuchElementException as e:
            screenshot_path = "./Screenshots/text_box_option_not_found.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error("Text Box option not found.")
            self.logger.info(f"Screenshot captured at: {screenshot_path}")
            assert False, "Text Box option not found."

        # Step 3: Enter user data
        self.logger.info("Filling in user details...")
        try:
            self.elements_page.enter_user_name(self.data["textbox"]["fullName"])
            self.elements_page.enter_user_email(self.data["textbox"]["emailID"])
            self.elements_page.enter_current_address(self.data["textbox"]["currentAddress"])
            self.elements_page.enter_permanent_address(self.data["textbox"]["permanentAddress"])
            self.logger.info("User details entered successfully.")
        except NoSuchElementException as e:
            screenshot_path = "./Screenshots/text_box_fields_not_found.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error("One or more Text Box fields not found.")
            self.logger.info(f"Screenshot captured at: {screenshot_path}")
            assert False, "Text Box fields not found."

        # Step 4: Submit the form
        self.logger.info("Clicking on the 'Submit' button...")
        try:
            self.elements_page.click_on_submit_button()
            self.logger.info("Submit button clicked.")
        except NoSuchElementException as e:
            screenshot_path = "./Screenshots/submit_button_not_found.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error("Submit button not found.")
            self.logger.info(f"Screenshot captured at: {screenshot_path}")
            assert False, "Submit button not found."

        # Step 5: Verify output
        self.logger.info("Verifying output after form submission...")
        try:
            output = self.elements_page.get_output_text()
            assert output == self.data["textbox"], f"Expected: {self.data['textbox']}, but got: {output}"
            self.logger.info("Test passed: Output matches the input data.")
        except NoSuchElementException as e:
            screenshot_path = "./Screenshots/output_element_not_found.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error("Output element not found.")
            self.logger.info(f"Screenshot captured at: {screenshot_path}")
            assert False, "Output element not found."
        except AssertionError as ae:
            screenshot_path = "./Screenshots/output_assertion_failed.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f" ASSERTION ERROR: {ae}")
            self.logger.info(f"Screenshot captured at: {screenshot_path}")
            assert False, str(ae)

        finally:
            self.logger.info("Test completed for Text Box element.")
            self.driver.quit()
            self.logger.info("Browser closed.")
            self.logger.info("********** Test Case: test_text_box_element : END **********")

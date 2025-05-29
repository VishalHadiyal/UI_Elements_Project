import json
import os
import pytest

from pageObjects.RegistrationForm import RegistrationPage
from pageObjects.HomePage import HomePage
from unititlies.customlogger import LogGen
from unititlies.readProperties import ReadConfig


class TestRegistrationPage:
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
            with open("./TestData/registration_form.json", "r") as file:
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
        self.registration_form = RegistrationPage(self.driver)

        # Navigate to the Registration Form
        self.home_page.click_on_forms_card()
        self.logger.info("Clicked on 'Forms' card on Home Page.")

        self.registration_form.click_on_form_option()
        self.logger.info("Clicked on 'Practice Form' under the Forms section.")

        yield  # Run the test method

        # ---------- TEAR DOWN ----------
        self.logger.info("Closing browser after test execution.")
        self.driver.quit()
        self.logger.info("Browser closed successfully.")

    def test_registration_page(self):
        """
        Test case for filling out and submitting the registration form.
        Includes logging, assertions for validation, and error handling.
        """
        self.logger.info("Starting test: test_registration_page")

        try:
            # Extract user data from test input
            user_data = self.data.get("UserOne", {})

            # Step-by-step form interaction
            self.registration_form.enter_first_name(user_data["FirstName"])
            self.logger.info(f"Entered first name: {user_data['FirstName']}")

            self.registration_form.enter_last_name(user_data["LastName"])
            self.logger.info(f"Entered last name: {user_data['LastName']}")

            self.registration_form.enter_email(user_data["UserEmail"])
            self.logger.info(f"Entered email: {user_data['UserEmail']}")

            self.registration_form.select_gender_male()
            self.logger.info("Selected gender: Male")

            self.registration_form.enter_mobile_number(user_data["MobileNumber"])
            self.logger.info(f"Entered mobile number: {user_data['MobileNumber']}")

            self.registration_form.enter_date_of_birth(user_data["DateOfBirth"])
            self.logger.info(f"Entered date of birth: {user_data['DateOfBirth']}")

            for subject in user_data.get("Subjects", {}).values():
                self.registration_form.enter_subject_with_actions(subject)
                self.logger.info(f"Entered subject: {subject}")

            self.registration_form.select_hobby()
            self.logger.info("Selected hobbies.")

            self.registration_form.upload_file(user_data["UploadFile"])
            self.logger.info(f"Uploaded file: {user_data['UploadFile']}")

            self.registration_form.enter_address(user_data["CurrentAddress"])
            self.logger.info(f"Entered address: {user_data['CurrentAddress']}")

            self.registration_form.select_state(user_data["State"])
            self.registration_form.select_city(user_data["City"])
            self.logger.info(f"Selected state and city: {user_data['State']}, {user_data['City']}")

            self.registration_form.click_on_submit_button()
            self.logger.info("Clicked submit button.")

            # Retrieve and verify submitted data
            submit_form_text = self.registration_form.get_submit_form_text()
            self.logger.info(f"Form submission confirmation received. Text: {submit_form_text}")

            submitted_data = dict(zip(submit_form_text[::2], submit_form_text[1::2]))

            expected_data = {
                "Student Name": f"{user_data['FirstName']} {user_data['LastName']}",
                "Student Email": user_data['UserEmail'],
                "Gender": "Male",
                "Mobile": user_data['MobileNumber'],
                "Date of Birth": "17 May,1998",  # Ensure this matches the form display format
                "Subjects": "English, Maths, Physics",
                "Hobbies": "Sports, Reading, Music",
                "Picture": os.path.basename(user_data['UploadFile']),
                "Address": user_data['CurrentAddress'],
                "State and City": f"{user_data['State']} {user_data['City']}"
            }

            for field, expected in expected_data.items():
                actual = submitted_data.get(field)
                self.logger.info(f"Verifying field '{field}': expected '{expected}', got '{actual}'")
                assert actual == expected, f"Mismatch in '{field}': expected '{expected}', got '{actual}'"

            self.logger.info("All field validations passed successfully.")

        except AssertionError as ae:
            self.logger.error(f"Assertion failed: {str(ae)}")
            screenshot_path = "./Screenshots/test_registration_page_assertion_error.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved at: {screenshot_path}")
            raise

        except Exception as e:
            self.logger.error(f"Unexpected exception during test execution: {str(e)}")
            screenshot_path = "./Screenshots/test_registration_page_exception.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved at: {screenshot_path}")
            raise

        finally:
            self.logger.info("Test 'test_registration_page' execution completed.")
            self.logger.info("========================================================")

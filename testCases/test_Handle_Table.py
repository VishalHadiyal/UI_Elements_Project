import json
import time

# import time

import pytest
from pageObjects.HomePage import HomePage
from pageObjects.ElementsPage import ElementsPage
from pageObjects.WebTable import WebTable
from unititlies.customlogger import LogGen
from unititlies.readProperties import ReadConfig


class TestTableHandling:
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
            with open("./TestData/table_data.json", "r") as file:
                self.data = json.load(file)
            self.logger.info("Test data successfully loaded from 'table_data.json'.")
        except Exception as e:
            self.logger.error(f"Failed to load test data: {str(e)}")
            raise

        # Initialize Page Objects
        home_page = HomePage(self.driver)
        elements_page = ElementsPage(self.driver)

        # Navigate through UI to reach Web Tables section
        home_page.click_on_elements_card()
        self.logger.info("Clicked on 'Elements' card on Home Page.")

        elements_page.click_on_web_table()
        self.logger.info("Clicked on 'Web Tables' under the Elements section.")

        yield  # Yield control to the test method

        # ---------- TEAR DOWN ----------
        self.logger.info("Closing browser after test execution.")
        self.driver.quit()

    @pytest.mark.smoke
    def test_find_user_and_delete(self):
        """
        Test case to find a user by email and delete them from the web table.
        """
        self.logger.info("********** Test Case: test_find_user_and_delete **********")

        try:
            self.logger.info("Step 1: Initializing WebTable page object")
            web_table = WebTable(self.driver)

            # Validate and extract email from test data
            self.logger.info("Step 2: Validating and extracting email from test data")
            assert "Users" in self.data and isinstance(self.data["Users"], list), "Key 'Users' missing or not a list"
            assert len(self.data["Users"]) > 0, "No user data at index 0"

            raw_email = self.data["Users"][0].get("Email", "").strip()
            assert raw_email, "Email is missing or empty in test data"
            email = str(raw_email)

            self.logger.info(f"Extracted email: {email}")

            # Search and delete
            self.logger.info(f"Step 3: Searching for user with email: {email}")
            web_table.search(email)
            self.logger.info(f"Step 4: Attempting to click delete for user with email: {email}")
            web_table.click_delete_by_email(email)

            # Verify deletion
            self.logger.info(f"Step 5: Verifying deletion of user with email: {email}")
            assert web_table.find_row_by_email(email) == -1, "User was not deleted successfully."
            self.logger.info(f"User with email {email} deleted successfully.")

        except AssertionError as ae:
            screenshot_path = "./Screenshots/test_find_user_and_delete_fail.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"AssertionError: {ae}")
            raise

        except Exception as e:
            screenshot_path = "./Screenshots/test_find_user_and_delete_fail.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Exception occurred: {e}")
            raise

        finally:
            self.logger.info("********** Ending Test: test_find_user_and_delete **********")

    @pytest.mark.smoke
    def test_add_new_user_find_user_and_delete(self):
        """
        Test case to add a new user to the web table, verify the user is added,
        search and then delete the user, and confirm deletion.
        """
        test_name = "test_add_new_user_find_user_and_delete"
        self.logger.info(f"********** Test Case Started: {test_name} **********")

        try:
            web_table = WebTable(self.driver)
            web_table.click_add_button()
            self.logger.info("Step 1: Clicked on 'Add New Record' button.")

            # Validate and extract user data
            assert "Users" in self.data and isinstance(self.data["Users"], list), "Key 'Users' missing or not a list"
            assert len(self.data["Users"]) > 3, "No user data at index 3"

            user_data = self.data["Users"][3]
            email = str(user_data.get("Email", "")).strip()
            assert email, "Email is missing or empty in test data"

            first_name = str(user_data.get("First Name", "")).strip()
            last_name = str(user_data.get("Last Name", "")).strip()
            age = str(user_data.get("Age", "")).strip()
            salary = str(user_data.get("Salary", "")).strip()
            department = str(user_data.get("Department", "")).strip()

            web_table.fill_add_new_record_form(first_name, last_name, email, age, salary, department)
            self.logger.info(f"Step 2: Filled in user details: {user_data}")
            web_table.click_submit_button()
            self.logger.info("Step 3: Submitted the form.")

            # Verify user added
            assert web_table.find_row_by_email(email) != -1, "User was not added successfully."
            self.logger.info(f"Step 4: Verified user with email '{email}' was added successfully.")

            # Search and delete
            web_table.search(email)
            self.logger.info(f"Step 5: Searched for user with email: {email}")
            web_table.click_delete_by_email(email)
            self.logger.info(f"Step 6: Clicked on delete button for user with email: {email}")

            # Verify deletion
            assert web_table.find_row_by_email(email) == -1, "User was not deleted successfully."
            self.logger.info(f"Step 7: Verified user with email '{email}' was deleted successfully.")

        except AssertionError as ae:
            screenshot_path = f"./Screenshots/{test_name}_assertion_failed.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Assertion failed: {ae}")
            raise

        except Exception as e:
            screenshot_path = f"./Screenshots/{test_name}_unexpected_error.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Unexpected error: {e}")
            raise

        finally:
            self.logger.info(f"********** Ending Test: {test_name} **********")

    @pytest.mark.smoke
    def test_search_and_edit(self):
        """
        Test case to search for a user by email, edit their details, and verify the changes.
        """
        test_name = "test_search_and_edit"
        self.logger.info(f"********** Test Case Started: {test_name} **********")

        try:
            # Step 1: Initialize WebTable Page Object
            self.logger.info("Step 1: Initializing WebTable page object")
            web_table = WebTable(self.driver)

            # Step 2: Extract original email from test data
            self.logger.info("Step 2: Extracting original email from test data")
            updated_data = self.data.get("EditUser", {})
            original_email = str(updated_data.get("Email", "")).strip()
            assert original_email, "Original email is missing in 'EditUser' test data"
            self.logger.info(f"Original email extracted: {original_email}")

            # Step 3: Search user by original email
            self.logger.info(f"Step 3: Searching for user with email: {original_email}")
            web_table.search(original_email)

            # Step 4: Click Edit on the first matched user
            self.logger.info("Step 4: Clicking edit on the first matched result")
            web_table.click_edit_by_index(0)

            # Step 5: Extract updated user data
            self.logger.info("Step 5: Extracting updated user data")
            updated_first_name = updated_data["First Name"]
            updated_last_name = updated_data["Last Name"]
            updated_email = updated_data["Email"]
            updated_age = str(updated_data["Age"])
            updated_salary = str(updated_data["Salary"])
            updated_department = updated_data["Department"]

            # Step 6: Fill in updated details in the form
            self.logger.info("Step 6: Filling in updated user details")
            web_table.fill_add_new_record_form(
                updated_first_name, updated_last_name, updated_email,
                updated_age, updated_salary, updated_department
            )
            self.logger.info(f"Updated user details entered: {updated_first_name}, {updated_last_name}, "
                             f"{updated_email}, {updated_age}, {updated_salary}, {updated_department}")

            # Step 7: Submit the form
            self.logger.info("Step 7: Submitting the form with updated details")
            web_table.click_submit_button()

            # Step 8: Search for the updated user
            self.logger.info(f"Step 8: Searching again for user with updated email: {updated_email}")
            web_table.search(updated_email)
            time.sleep(2)

            # Step 9: Validate updated user details
            self.logger.info("Step 9: Validating updated user details in the table")
            row_index = web_table.find_row_by_email(updated_email)
            assert row_index != -1, f"Updated user with email '{updated_email}' not found"

            row_data = web_table.get_row_data_by_index(row_index)
            self.logger.info(f"Extracted row data: {row_data}")

            expected_data = {
                "First Name": updated_first_name,
                "Last Name": updated_last_name,
                "Age": updated_age,
                "Email": updated_email,
                "Salary": updated_salary,
                "Department": updated_department
            }

            actual_data = {
                "First Name": row_data[0],
                "Last Name": row_data[1],
                "Age": row_data[2],
                "Email": row_data[3],
                "Salary": row_data[4],
                "Department": row_data[5],
            }

            for key in expected_data:
                assert expected_data[key] == actual_data[key], f"{key} did not update correctly"

            self.logger.info("Test passed: User details updated and verified successfully")

        except AssertionError as ae:
            screenshot_path = f"./Screenshots/{test_name}_assertion_failed.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Assertion failed: {ae}")
            self.logger.error(f"Screenshot captured: {screenshot_path}")
            raise

        except Exception as e:
            screenshot_path = f"./Screenshots/{test_name}_unexpected_error.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.error(f"Unexpected error occurred: {e}")
            self.logger.error(f"Screenshot captured: {screenshot_path}")
            raise

        finally:
            self.logger.info(f"********** Ending Test: {test_name} **********")

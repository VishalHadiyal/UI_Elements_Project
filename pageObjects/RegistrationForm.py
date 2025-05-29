# Required Selenium and Python modules
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class RegistrationPage:

    # ========== LOCATORS ==========
    # Page navigation element
    OPTION_FORM_XPATH = "//span[normalize-space()='Practice Form']"

    # Input fields
    TXT_BOX_FIRST_NAME_XPATH = "//input[@id='firstName']"
    TXT_BOX_LAST_NAME_XPATH = "//input[@id='lastName']"
    TXT_BOX_EMAIL_XPATH = "//input[@id='userEmail']"
    RADIO_BUTTON_GENDER_XPATH = "//label[normalize-space()='Male']"
    TXT_BOX_MOBILE_XPATH = "//input[@id='userNumber']"

    # Date of birth section locators
    TXT_BOX_CLICKS_ON_DATE_OF_BIRTH_XPATH = "//input[@id='dateOfBirthInput']"
    DROPDOWN_MONTH_XPATH = "//select[@class='react-datepicker__month-select']"
    DROPDOWN_YEAR_XPATH = "//select[@class='react-datepicker__year-select']"
    DATE_CLICKS_ON_DAY_XPATH = "//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'outside-month')) and text()='{{day}}']"
    TXT_BOX_SUBJECT_CSS_SELECTOR = ".subjects-auto-complete__value-container.subjects-auto-complete__value-container--is-multi.css-1hwfws3"

    # Hobbies checkboxes
    HOBBIES_XPATHS = {
        "Sports": "//label[normalize-space()='Sports']",
        "Reading": "//label[normalize-space()='Reading']",
        "Music": "//label[normalize-space()='Music']"
    }

    # Address and file upload fields
    TXT_BOX_ADDRESS_XPATH = "//textarea[@id='currentAddress']"
    INPUT_FILE_UPLOAD_XPATH = "//input[@id='uploadPicture']"

    # State and city dropdowns
    DROPDOWN_STATE_XPATH = "//div[contains(text(),'Select State')]"
    DROPDOWN_CITY_XPATH = "//div[contains(text(),'Select City')]"

    # Submit button and submitted data
    BUTTON_SUBMIT_XPATH = "//button[@id='submit']"
    TEXT_OF_SUBMIT_FORM_XPATH = "//tbody/tr/td"

    def __init__(self, driver):
        # Initialize with a Selenium WebDriver instance
        self.driver = driver

    def scroll_and_click(self, xpath, element_name, timeout=10, scroll_attempts=5):
        """
        Scroll to an element using JavaScript and click it.
        Retries multiple times in case of failure.
        """
        try:
            for attempt in range(scroll_attempts):
                try:
                    # Wait for element to appear in DOM
                    element = WebDriverWait(self.driver, timeout).until(
                        EC.presence_of_element_located((By.XPATH, xpath))
                    )
                    # Scroll into view
                    self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
                    # Wait until clickable and then click
                    element = WebDriverWait(self.driver, timeout).until(
                        EC.element_to_be_clickable((By.XPATH, xpath))
                    )
                    element.click()
                    return
                except TimeoutException:
                    continue
            print(f"{element_name} card could not be clicked after {scroll_attempts} scroll attempts.")
        except NoSuchElementException:
            print(f"{element_name} card not found.")

    def generate_xpath(self, element):
        """
        Utility to generate dynamic XPath of a given element.
        (Optional for debugging or development use)
        """
        return self.driver.execute_script(""" ... """, element)

    def click_on_form_option(self):
        # Click on the "Practice Form" card
        self.scroll_and_click(self.OPTION_FORM_XPATH, "Form Option")

    def enter_first_name(self, first_name):
        # Enter first name
        self.scroll_and_click(self.TXT_BOX_FIRST_NAME_XPATH, "First Name")
        self.driver.find_element(By.XPATH, self.TXT_BOX_FIRST_NAME_XPATH).send_keys(first_name)

    def enter_last_name(self, last_name):
        # Enter last name
        self.scroll_and_click(self.TXT_BOX_LAST_NAME_XPATH, "Last Name")
        self.driver.find_element(By.XPATH, self.TXT_BOX_LAST_NAME_XPATH).send_keys(last_name)

    def enter_email(self, email):
        # Enter email address
        self.scroll_and_click(self.TXT_BOX_EMAIL_XPATH, "Email")
        self.driver.find_element(By.XPATH, self.TXT_BOX_EMAIL_XPATH).send_keys(email)

    def select_gender_male(self):
        # Select the "Male" radio button for gender
        self.scroll_and_click(self.RADIO_BUTTON_GENDER_XPATH, "Gender Male")

    def enter_mobile_number(self, mobile_number):
        # Enter mobile number
        self.scroll_and_click(self.TXT_BOX_MOBILE_XPATH, "Mobile Number")
        self.driver.find_element(By.XPATH, self.TXT_BOX_MOBILE_XPATH).send_keys(mobile_number)

    def enter_date_of_birth(self, dob):
        """
        Select a date from the calendar widget.
        Format: "dd-Month-yyyy" (e.g., "17-May-1998")
        """
        wait = WebDriverWait(self.driver, 10)
        parsed_dob = datetime.strptime(dob, "%d-%B-%Y")
        year = parsed_dob.year
        month = parsed_dob.strftime("%B")
        day = parsed_dob.day

        # Open calendar
        self.scroll_and_click(self.TXT_BOX_CLICKS_ON_DATE_OF_BIRTH_XPATH, "Date of Birth Input")

        # Set month and year
        month_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, self.DROPDOWN_MONTH_XPATH)))
        Select(month_dropdown).select_by_visible_text(month)

        year_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, self.DROPDOWN_YEAR_XPATH)))
        Select(year_dropdown).select_by_visible_text(str(year))

        # Click specific day
        day_xpath = self.DATE_CLICKS_ON_DAY_XPATH.replace("{{day}}", str(day))
        self.scroll_and_click(day_xpath, f"Day {day}")

    def enter_subject_with_actions(self, subject):
        """
        Enter a subject using keyboard simulation.
        Supports autocomplete feature.
        """
        subject_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.TXT_BOX_SUBJECT_CSS_SELECTOR))
        )
        subject_input.click()

        # Simulate typing with ActionChains
        actions = ActionChains(self.driver)
        actions.move_to_element(subject_input).click().send_keys(subject).pause(1).send_keys(Keys.ENTER).perform()

    def select_hobby(self):
        """
        Select all available hobbies by clicking each checkbox.
        """
        for hobby, xpath in self.HOBBIES_XPATHS.items():
            self.scroll_and_click(xpath, f"Hobby - {hobby}")

    def enter_address(self, address):
        # Enter current address
        self.scroll_and_click(self.TXT_BOX_ADDRESS_XPATH, "Address")
        self.driver.find_element(By.XPATH, self.TXT_BOX_ADDRESS_XPATH).send_keys(address)

    def upload_file(self, file_path):
        """
        Upload a file by sending its path to the file input element.
        Returns the uploaded file name for verification.
        """
        try:
            file_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.INPUT_FILE_UPLOAD_XPATH))
            )
            file_input.send_keys(file_path)
            uploaded_file_name = file_input.get_attribute("value").split("\\")[-1]
            return uploaded_file_name
        except TimeoutException:
            return None

    def select_state(self, state_name):
        """
        Select a state from the dropdown by name.
        """
        try:
            self.scroll_and_click(self.DROPDOWN_STATE_XPATH, "State Dropdown")
            options_xpath = f"//div[contains(text(), '{state_name}')]"
            option_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, options_xpath))
            )
            option_element.click()
        except TimeoutException:
            print(f"State '{state_name}' not found in the dropdown.")

    def select_city(self, city_name):
        """
        Select a city from the dropdown by name.
        """
        try:
            self.scroll_and_click(self.DROPDOWN_CITY_XPATH, "City Dropdown")
            options_xpath = f"//div[contains(text(), '{city_name}')]"
            option_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, options_xpath))
            )
            option_element.click()
        except TimeoutException:
            print(f"City '{city_name}' not found in the dropdown.")

    def click_on_submit_button(self):
        """
        Submit the form by clicking the submit button.
        """
        self.scroll_and_click(self.BUTTON_SUBMIT_XPATH, "Submit Button")

    def get_submit_form_text(self):
        """
        Retrieve all text values from the submitted form result modal.
        Returns list of text entries.
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.TEXT_OF_SUBMIT_FORM_XPATH))
            )
            elements = self.driver.find_elements(By.XPATH, self.TEXT_OF_SUBMIT_FORM_XPATH)
            return [element.text for element in elements]
        except TimeoutException:
            return []

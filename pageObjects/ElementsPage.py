from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ElementsPage:

    # Locators for elements on the Elements page
    TEXT_ELEMENT_PAGE_CSS_SELECTOR = ".col-12.mt-4.col-md-6"

    # TESTING TEXT BOX ELEMENTS
    OPTION_TEXT_BOX_XPATH = "//span[normalize-space()='Text Box']"
    TXT_INPUT_USER_NAME_XPATH = "//input[@id='userName']"
    TXT_INPUT_USER_EMAIL_XPATH = "//input[@id='userEmail']"
    TXT_INPUT_CURRENT_ADDRESS_XPATH = "//textarea[@id='currentAddress']"
    TXT_INPUT_PERMANENT_ADDRESS_XPATH = "//textarea[@id='permanentAddress']"
    BUTTON_SUBMIT_XPATH = "//button[@id='submit']"

    TXT_OUTPUT_NAME_XPATH = "//p[@id='name']"
    TXT_OUTPUT_EMAIL_XPATH = "//p[@id='email']"
    TXT_OUTPUT_CURRENT_ADDRESS_XPATH = "//p[@id='currentAddress']"
    TXT_OUTPUT_PERMANENT_ADDRESS_XPATH = "//p[@id='permanentAddress']"

    # TESTING CHECK BOX ELEMENTS
    OPTION_CHECK_BOX_XPATH = "//span[normalize-space()='Check Box']"
    CHECK_BOX_HOME_XPATH = "//span[text()='Home']"
    BUTTON_PLUE_XPATH = "//button[@title = 'Expand all']"
    CHECK_BOX_WORKSPACE_XPATH = "//span[@class='rct-checkbox' and @xpath='6']"

    # TESTING RADIO BUTTON ELEMENTS
    OPTION_RADIO_BUTTON_XPATH = "//span[normalize-space()='Radio Button']"
    BUTTON_YES_XPATH = "//label[@for='yesRadio']"
    RADIO_NO_XPATH = "//label[normalize-space()='No']"
    TEXT_SUCCESS_MESSAGE_XPATH = "//p[@class='mt-3']"
    RADIO_IMPRESSIVE_XPATH = "//label[@for='impressiveRadio']"


    def __init__(self, driver):
        self.driver = driver

    def get_text_element_page(self):
        """
        Get the text of the element on the Elements page.
        """
        try:
            text_element = self.driver.find_element(By.CSS_SELECTOR, self.TEXT_ELEMENT_PAGE_CSS_SELECTOR)
            return text_element.text
        except NoSuchElementException:
            return None

    # TESTING TEXT BOX ELEMENTS
    def click_on_text_box(self):
        """
        Click on the 'Text Box' option.
        """
        try:
            text_box_option = self.driver.find_element(By.XPATH, self.OPTION_TEXT_BOX_XPATH)
            text_box_option.click()
        except NoSuchElementException:
            print("Text Box option not found.")

    def enter_user_name(self, user_name):
        """
        Enter the user name in the text box.
        """
        try:
            user_name_field = self.driver.find_element(By.XPATH, self.TXT_INPUT_USER_NAME_XPATH)
            user_name_field.send_keys(user_name)
        except NoSuchElementException:
            print("User Name field not found.")

    def enter_user_email(self, user_email):
        """
        Enter the user email in the text box.
        """
        try:
            user_email_field = self.driver.find_element(By.XPATH, self.TXT_INPUT_USER_EMAIL_XPATH)
            user_email_field.send_keys(user_email)
        except NoSuchElementException:
            print("User Email field not found.")

    def enter_current_address(self, current_address):
        """
        Enter the current address in the text box.
        """
        try:
            current_address_field = self.driver.find_element(By.XPATH, self.TXT_INPUT_CURRENT_ADDRESS_XPATH)
            current_address_field.send_keys(current_address)
        except NoSuchElementException:
            print("Current Address field not found.")

    def enter_permanent_address(self, permanent_address):
        """
        Enter the permanent address in the text box.
        """
        try:
            permanent_address_field = self.driver.find_element(By.XPATH, self.TXT_INPUT_PERMANENT_ADDRESS_XPATH)
            permanent_address_field.send_keys(permanent_address)
        except NoSuchElementException:
            print("Permanent Address field not found.")

    def click_on_submit_button(self):
        """
        Click on the 'Submit' button.
        """
        try:
            submit_button = self.driver.find_element(By.XPATH, self.BUTTON_SUBMIT_XPATH)
            submit_button.click()
        except NoSuchElementException:
            print("Submit button not found.")

    def get_output_text(self):
        """
        Get the output text after submitting the form.
        Strips label prefixes like 'Name:', 'Email:' etc.
        """
        try:
            name_output = self.driver.find_element(By.XPATH, self.TXT_OUTPUT_NAME_XPATH).text
            email_output = self.driver.find_element(By.XPATH, self.TXT_OUTPUT_EMAIL_XPATH).text
            current_address_output = self.driver.find_element(By.XPATH, self.TXT_OUTPUT_CURRENT_ADDRESS_XPATH).text
            permanent_address_output = self.driver.find_element(By.XPATH, self.TXT_OUTPUT_PERMANENT_ADDRESS_XPATH).text

            return {
                "fullName": name_output.replace("Name:", "").strip(),
                "emailID": email_output.replace("Email:", "").strip(),
                "currentAddress": current_address_output.replace("Current Address :", "").strip(),
                "permanentAddress": permanent_address_output.replace("Permananet Address :", "").strip(),
            }
        except NoSuchElementException:
            print("Output fields not found.")
            return None

    # TESTING CHECK BOX ELEMENTS
    def click_on_check_box(self):
        """
        Click on the 'Check Box' option.
        """
        try:
            check_box_option = self.driver.find_element(By.XPATH, self.OPTION_CHECK_BOX_XPATH)
            check_box_option.click()
        except NoSuchElementException:
            print("Check Box option not found.")

    def check_home_check_box_displayed(self):
        """
        Click on the 'Check Box' option if it is displayed.
        """
        try:
            check_box_option = self.driver.find_element(By.XPATH, self.CHECK_BOX_HOME_XPATH)
            if check_box_option.is_displayed():
                check_box_option.click()
            else:
                print("Check Box option is not visible.")
        except NoSuchElementException:
            print("Check Box option not found.")

    def click_plus_button(self):
        """
        Click on the plus button to expand the checkbox options.
        """
        try:
            plus_button = self.driver.find_element(By.XPATH, self.BUTTON_PLUE_XPATH)
            plus_button.click()
        except NoSuchElementException:
            print("Plus button not found.")

    def click_workspace_check_box(self):
        """
        Clicks the 'Workspace' checkbox.
        """
        try:
            wait = WebDriverWait(self.driver, 10)
            checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, self.CHECK_BOX_WORKSPACE_XPATH)))
            try:
                checkbox.click()
            except ElementNotInteractableException:
                 self.driver.execute_script("arguments[0].click();", checkbox)
        except NoSuchElementException:
            raise AssertionError("ERROR: Workspace checkbox not found.")
        except ElementNotInteractableException:
            raise AssertionError("ERROR: Workspace checkbox found but not interactable.")

    # TESTING RADIO BUTTON ELEMENTS
    def click_on_radio_button(self):
        """
        Click on the 'Check Box' option.
        """
        try:
            check_box_option = self.driver.find_element(By.XPATH, self.OPTION_RADIO_BUTTON_XPATH)
            check_box_option.click()
        except NoSuchElementException:
            print("Check Box option not found.")

    def click_on_yes_radio_button(self):
        """
        Click on the 'Yes' radio button.
        """
        try:
            yes_radio_button = self.driver.find_element(By.XPATH, self.BUTTON_YES_XPATH)
            yes_radio_button.click()
        except NoSuchElementException:
            print("Yes radio button not found.")

    def get_success_message_text(self):
        """
        Get the text of the 'Yes' radio button.
        """
        try:
            yes_radio_button = self.driver.find_element(By.XPATH, self.TEXT_SUCCESS_MESSAGE_XPATH)
            return yes_radio_button.text
        except NoSuchElementException:
            print("Yes radio button not found.")
            return None

    def click_on_impressive_radio_button(self):
        """
        Click on the 'Impressive' radio button using JavaScript to bypass UI obstructions.
        """
        try:
            wait = WebDriverWait(self.driver, 10)

            # Wait until element is present in DOM (not necessarily clickable visually)
            impressive_radio_button = wait.until(
                EC.presence_of_element_located((By.XPATH, self.RADIO_IMPRESSIVE_XPATH))
            )

            # Scroll into view (optional, for visual confirmation during debug)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", impressive_radio_button)

            # Force JS click to avoid interception
            self.driver.execute_script("arguments[0].click();", impressive_radio_button)

        except TimeoutException:
            print("Timed out waiting for 'Impressive' radio button.")
        except NoSuchElementException:
            print("Impressive radio button not found.")
        except Exception as e:
            print(f"Error clicking on 'Impressive' radio button: {str(e)}")

    def is_no_radio_button_enabled(self):
        """
        Check if the 'No' radio button is disabled.
        """
        try:
            no_radio_button = self.driver.find_element(By.XPATH, self.RADIO_NO_XPATH)
            no_radio_button.is_enabled()
        except NoSuchElementException:
            print("No radio button not found.")
            return False
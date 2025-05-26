from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


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

    # TESTING BUTTONS ELEMENTS
    OPTION_BUTTONS_XPATH = "//span[normalize-space()='Buttons']"
    BUTTON_DOUBLE_CLICK_XPATH = "//button[@id='doubleClickBtn']"
    BUTTON_RIGHT_CLICK_XPATH = "//button[@id='rightClickBtn']"
    BUTTON_CLICK_ME_XPATH = "(//button[normalize-space()='Click Me'])"
    BUTTON_DOUBLE_CLICK_SUCCESS_MESSAGE_XPATH = "//p[@id='doubleClickMessage']"
    BUTTON_RIGHT_CLICK_SUCCESS_MESSAGE_XPATH = "//p[@id='rightClickMessage']"
    BUTTON_DYNAMIC_CLICK_SUCCESS_MESSAGE_XPATH = "//p[@id='dynamicClickMessage']"

    # TESTING WEB TABLE ELEMENTS
    OPTION_WEB_TABLE_XPATH = "//span[normalize-space()='Web Tables']"

    # TESTING LINKS ELEMENTS
    OPTION_LINKS_XPATH = "//span[normalize-space()='Links']"
    LINKS_COUNT_XPATH = "//a"
    LINK_SIMPLE_XPATH = "//a[@id='simpleLink']"
    LINK_DYNAMIC_XPATH = "//a[@id='dynamicLink']"
    # API LINKS
    LINK_CREATE_XPATH = "//a[@id='created']"
    LINK_NO_CONTENT_XPATH = "//a[@id='no-content']"
    LINK_MOVED_XPATH = "//a[@id='moved']"
    LINK_BAD_REQUEST_XPATH = "//a[@id='bad-request']"
    LINK_UNAUTHORIZED_XPATH = "//a[@id='unauthorized']"
    LINK_FORBIDDEN_XPATH = "//a[@id='forbidden']"
    LINK_NOT_FOUND_XPATH = "//a[@id='invalid-url']"
    RESPONSE_STATUS_CODE_XPATH = "//p[@id='linkResponse']"
    OPTION_BROKEN_LINKS_XPATH = "//span[normalize-space()='Broken Links - Images']"
    IMG_IS_DISPLAYED_XPATH = "//div /img[@src='/images/Toolsqa.jpg']"
    IMG_BROKEN_LINKS_XPATH = "//img[@src='/images/Toolsqa_1.jpg']"
    LINK_VALID_LINK_XPATH = "//a[normalize-space()='Click Here for Valid Link']"
    LINK_BROKEN_LINK_XPATH = "//a[normalize-space()='Click Here for Broken Link']"

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

    # TESTING BUTTONS ELEMENTS
    def click_on_buttons(self):
        """
        Click on the 'Buttons' option.
        """
        try:
            buttons_option = self.driver.find_element(By.XPATH, self.OPTION_BUTTONS_XPATH)
            buttons_option.click()
        except NoSuchElementException:
            print("Buttons option not found.")

    def click_on_double_click_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.BUTTON_DOUBLE_CLICK_XPATH))
        )
        action = ActionChains(self.driver)
        action.double_click(button).perform()

    def click_on_right_click_button(self):
        """
        Scroll to the 'Right Click' button and perform a right-click (context click)
        using an explicit wait instead of time.sleep().
        """
        try:
            wait = WebDriverWait(self.driver, 10)

            # Wait until the element is present and clickable
            right_click_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, self.BUTTON_RIGHT_CLICK_XPATH))
            )

            # Scroll the element into view (centered)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", right_click_button)

            # Wait a bit more in case of rendering delays after scrolling (optional but without sleep)
            wait.until(lambda driver: right_click_button.is_displayed())

            # Perform the right-click
            ActionChains(self.driver).context_click(right_click_button).perform()

        except (NoSuchElementException, TimeoutException):
            print("Right Click button not found or not clickable.")

    def click_on_click_me_button(self):
        """
        Click on the 'Click Me' button.
        """
        try:
            click_me_button = self.driver.find_element(By.XPATH, self.BUTTON_CLICK_ME_XPATH)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", click_me_button)
            click_me_button.click()
        except NoSuchElementException:
            print("Click Me button not found.")

    def get_double_clicks_success_message_text(self, timeout=10):
        """
        Get the text of the success message after double clicking the button.
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            success_message = wait.until(
                EC.visibility_of_element_located((By.XPATH, self.BUTTON_DOUBLE_CLICK_SUCCESS_MESSAGE_XPATH))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", success_message)
            return success_message.text.strip()
        except TimeoutException:
            print("Timed out waiting for success message.")
            return None

    def get_right_clicks_success_message_text(self, timeout=10):
        """
        Get the text of the success message after right clicking the button.
        Waits up to `timeout` seconds for the element to appear and then disappear.
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            success_message = wait.until(
                EC.visibility_of_element_located((By.XPATH, self.BUTTON_RIGHT_CLICK_SUCCESS_MESSAGE_XPATH))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", success_message)
            message_text = success_message.text.strip()
            # Wait for the message to disappear
            wait.until(EC.invisibility_of_element_located((By.XPATH, self.BUTTON_RIGHT_CLICK_SUCCESS_MESSAGE_XPATH)))
            return message_text
        except TimeoutException:
            print("Timed out waiting for success message.")
            return None

    def get_dynamic_clicks_success_message_text(self, timeout=10):
        """
        Get the text of the success message after dynamically clicking the button.
        Waits up to `timeout` seconds for the element to appear and then disappear.
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            success_message = wait.until(
                EC.visibility_of_element_located((By.XPATH, self.BUTTON_DYNAMIC_CLICK_SUCCESS_MESSAGE_XPATH))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", success_message)
            message_text = success_message.text.strip()
            # Wait for the message to disappear
            wait.until(EC.invisibility_of_element_located((By.XPATH, self.BUTTON_DYNAMIC_CLICK_SUCCESS_MESSAGE_XPATH)))
            return message_text
        except TimeoutException:
            print("Timed out waiting for success message.")
            return None

    # TESTING WEB TABLE ELEMENTS
    def click_on_web_table(self):
        """
        Click on the 'Web Table' option.
        """
        try:
            web_table_option = self.driver.find_element(By.XPATH, self.OPTION_WEB_TABLE_XPATH)
            web_table_option.click()
        except NoSuchElementException:
            print("Web Table option not found.")

    # TESTING LINKS ELEMENTS
    def click_on_links(self):
        """
        Click on the 'Links' option.
        """
        try:
            links_option = self.driver.find_element(By.XPATH, self.OPTION_LINKS_XPATH)
            links_option.click()
        except NoSuchElementException:
            print("Links option not found.")

    def get_links_count(self):
        """
        Get the count of all links on the page.
        """
        try:
            links = self.driver.find_elements(By.XPATH, self.LINKS_COUNT_XPATH)
            return len(links)
        except NoSuchElementException:
            print("Links not found.")
            return 0

    def click_on_simple_link(self):
        """
        Click on the 'Simple Link'.
        """
        try:
            simple_link = self.driver.find_element(By.XPATH, self.LINK_SIMPLE_XPATH)
            simple_link.click()
        except NoSuchElementException:
            print("Simple Link not found.")

    def click_on_dynamic_link(self):
        """
        Click on the 'Dynamic Link'.
        """
        try:
            dynamic_link = self.driver.find_element(By.XPATH, self.LINK_DYNAMIC_XPATH)
            dynamic_link.click()
        except NoSuchElementException:
            print("Dynamic Link not found.")

    def click_on_create_link(self):
        """
        Click on the 'Create' link.
        """
        try:
            create_link = self.driver.find_element(By.XPATH, self.LINK_CREATE_XPATH)
            create_link.click()
        except NoSuchElementException:
            print("Create Link not found.")

    def click_on_no_content_link(self):
        """
        Click on the 'No Content' link.
        """
        try:
            no_content_link = self.driver.find_element(By.XPATH, self.LINK_NO_CONTENT_XPATH)
            no_content_link.click()
        except NoSuchElementException:
            print("No Content Link not found.")

    def click_on_moved_link(self):
        """
        Click on the 'Moved' link.
        """
        try:
            moved_link = self.driver.find_element(By.XPATH, self.LINK_MOVED_XPATH)
            moved_link.click()
        except NoSuchElementException:
            print("Moved Link not found.")

    def click_on_bad_request_link(self):
        """
        Click on the 'Bad Request' link.
        """
        try:
            bad_request_link = self.driver.find_element(By.XPATH, self.LINK_BAD_REQUEST_XPATH)
            bad_request_link.click()
        except NoSuchElementException:
            print("Bad Request Link not found.")

    def click_on_unauthorized_link(self):
        """
        Click on the 'Unauthorized' link.
        """
        try:
            unauthorized_link = self.driver.find_element(By.XPATH, self.LINK_UNAUTHORIZED_XPATH)
            unauthorized_link.click()
        except NoSuchElementException:
            print("Unauthorized Link not found.")

    def click_on_forbidden_link(self):
        """
        Click on the 'Forbidden' link.
        """
        try:
            forbidden_link = self.driver.find_element(By.XPATH, self.LINK_FORBIDDEN_XPATH)
            forbidden_link.click()
        except NoSuchElementException:
            print("Forbidden Link not found.")

    def click_on_not_found_link(self):
        """
        Click on the 'Not Found' link.
        """
        try:
            not_found_link = self.driver.find_element(By.XPATH, self.LINK_NOT_FOUND_XPATH)
            not_found_link.click()
        except NoSuchElementException:
            print("Not Found Link not found.")

    def get_response_status_code(self):
        """
        Get the response status code after clicking on a link.
        """
        try:
            response_status = self.driver.find_element(By.XPATH, self.RESPONSE_STATUS_CODE_XPATH)
            return response_status.text.strip()
        except NoSuchElementException:
            print("Response status code not found.")
            return None

    def click_on_broken_links_images(self):
        """
        Click on the 'Broken Links - Images' option.
        """
        try:
            broken_links_images_option = self.driver.find_element(By.XPATH, self.OPTION_BROKEN_LINKS_XPATH)
            broken_links_images_option.click()
        except NoSuchElementException:
            print("Broken Links - Images option not found.")

    def is_image_displayed(self):
        """
        Check if the image is displayed on the page.
        """
        try:
            image = self.driver.find_element(By.XPATH, self.IMG_IS_DISPLAYED_XPATH)
            return image.is_displayed()
        except NoSuchElementException:
            print("Image not found.")
            return False

    def is_broken_image_displayed(self):
        """
        Check if the image is broken (failed to load) using naturalWidth property.
        """
        try:
            image_element = self.driver.find_element(By.XPATH, self.IMG_BROKEN_LINKS_XPATH)
            # Execute JavaScript to check if the image is broken
            is_broken = self.driver.execute_script(
                "return arguments[0].naturalWidth === 0", image_element)
            return is_broken
        except NoSuchElementException:
            print("Image element not found.")
            return False

    def click_on_valid_link(self):
        """
        Click on the 'Click Here for Valid Link'.
        """
        try:
            valid_link = self.driver.find_element(By.XPATH, self.LINK_VALID_LINK_XPATH)
            valid_link.click()
        except NoSuchElementException:
            print("Valid Link not found.")

    def click_on_broken_link(self):
        """
        Click on the 'Click Here for Broken Link'.
        """
        try:
            broken_link = self.driver.find_element(By.XPATH, self.LINK_BROKEN_LINK_XPATH)
            broken_link.click()
        except NoSuchElementException:
            print("Broken Link not found.")
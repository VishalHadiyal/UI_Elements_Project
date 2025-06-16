from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class BrowserWindowHandle:

    # LOCATORS
    # Handle for the Browser Windows section
    OPTION_BROWSER_WINDOW_XPATH = "//span[normalize-space()='Browser Windows']"

    BUTTON_NEW_TAB_XPATH = "//button[@id='tabButton']"
    TEXT_NEW_TAB_XPATH = "//h1[@id='sampleHeading']"

    BUTTON_NEW_WINDOW_XPATH = "//button[@id='windowButton']"
    TEXT_NEW_WINDOW_XPATH = "//h1[@id='sampleHeading']"

    BUTTON_NEW_WINDOW_MESSAGE_XPATH = "//button[@id='messageWindowButton']"
    TEXT_NEW_WINDOW_MESSAGE_XPATH = "//body[contains(text(), 'Knowledge increases by')]"

    # Handle for the Alerts section
    OPTION_ALERTS_XPATH = "//span[normalize-space()='Alerts']"
    BUTTON_CLICK_ME_AND_SEE_ALERT_XPATH = "//button[@id='alertButton']"

    BUTTON_AFTER_FIVE_SECONDS_XPATH = "//button[@id='timerAlertButton']"

    BUTTON_CONFIRM_BOX_XPATH = "//button[@id='confirmButton']"
    TEXT_CONFIRM_RESULT_XPATH = "//span[@id='confirmResult']"

    BUTTON_PROMPT_BOX_XPATH = "//button[@id='promtButton']"
    TEXT_PROMPT_RESULT_XPATH = "//span[@id='promptResult']"

    # Handle for the Modal Dialogs section
    # Small Modal Dialogs
    OPTION_MODAL_XPATH = "//span[normalize-space()='Modal Dialogs']"
    BUTTON_SMALL_MODAL_XPATH = "//button[@id='showSmallModal']"
    TEXT_MODAL_CONTENT_XPATH = "//div[@class='modal-body']"
    TEXT_NAME_OF_SMALL_MODAL_XPATH = "//div[@id='example-modal-sizes-title-sm']"
    BUTTON_CLOSE_SMALL_MODAL_XPATH = "//button[@id='closeSmallModal']"
    TEXT_NAME_OF_THE_PAGE_XPATH = "//h1[normalize-space()='Modal Dialogs']"

    # Large Modal Dialogs
    BUTTON_LARGE_MODAL_XPATH = "//button[@id='showLargeModal']"
    NAME_OF_THE_LARGE_MODAL_XPATH = "//div[@id='example-modal-sizes-title-lg']"
    TEXT_CONTENT_OF_THE_LARGE_MODAL_XPATH = "//p[contains(text(),'Lorem Ipsum is simply dummy text of the printing a')]"
    BUTTON_LARGE_MODAL_CLOSE_XPATH = "//button[@id='closeLargeModal']"

    # Iframes Locators
    OPTION_FRAMES_XPATH = "//span[normalize-space()='Frames']"
    SWITCH_FRAME_XPATH = "//iframe[@id='frame1']"
    TEXT_OF_IFRAME_XPATH = "//h1[@id='sampleHeading']"
    TEXT_OF_THE_MAIN_FRAME_XPATH = "//h1[normalize-space()='Frames']"

    # Nested Iframe Locators
    OPTION_NESTED_IFRAME_XPATH = "//span[normalize-space()='Nested Frames']"
    TEXT_OF_THR_MAIN_NESTED_FRAME_XPATH = "//h1[normalize-space()='Nested Frames']"
    PARENT_FRAME_XPATH = "//iframe[@id='frame1']"
    CHILD_FRAME_XPATH = "//iframe[@srcdoc='<p>Child Iframe</p>']"

    def __init__(self, driver):
        # Initialize with a Selenium WebDriver instance
        self.driver = driver

    def click_on_browser_window_option(self):
        """
        Click on the 'Browser Windows' option.
        """
        try:
            browser_window_option = self.driver.find_element(By.XPATH, self.OPTION_BROWSER_WINDOW_XPATH)
            browser_window_option.click()
        except NoSuchElementException:
            print("Browser Windows option not found.")

    def click_on_new_tab_button(self):
        """
        Click on the 'New Tab' button to open a new browser tab.
        """
        try:
            new_tab_button = self.driver.find_element(By.XPATH, self.BUTTON_NEW_TAB_XPATH)
            new_tab_button.click()
        except NoSuchElementException:
            print("New Tab button not found.")

    def get_new_tab_text(self):
        """
        Get the text from the new tab to verify it opened correctly.
        """
        try:
            new_tab_text = self.driver.find_element(By.XPATH, self.TEXT_NEW_TAB_XPATH).text
            return new_tab_text
        except NoSuchElementException:
            print("Text in the new tab not found.")
            return None

    def click_on_new_window_button(self):
        """
        Click on the 'New Window' button to open a new browser window.
        """
        try:
            new_window_button = self.driver.find_element(By.XPATH, self.BUTTON_NEW_WINDOW_XPATH)
            new_window_button.click()
        except NoSuchElementException:
            print("New Window button not found.")

    def get_new_window_text(self):
        """
        Get the text from the new window to verify it opened correctly.
        """
        try:
            new_window_text = self.driver.find_element(By.XPATH, self.TEXT_NEW_WINDOW_XPATH).text
            return new_window_text
        except NoSuchElementException:
            print("Text in the new window not found.")
            return None

    def click_on_new_window_message_button(self):
        """
        Click on the 'New Window Message' button to open a new browser window with a message.
        """
        try:
            new_window_message_button = self.driver.find_element(By.XPATH, self.BUTTON_NEW_WINDOW_MESSAGE_XPATH)
            new_window_message_button.click()
        except NoSuchElementException:
            print("New Window Message button not found.")

    def get_new_window_message_text(self):
        """
        Get the text content from the new window (plain page, no DOM structure).
        """
        try:
            body_text = self.driver.find_element(By.TAG_NAME, "body").text
            return body_text.strip()
        except Exception as e:
            print(f"Failed to get text from new window: {e}")
            return None

    def click_on_alerts_option(self):
        """
        Click on the 'Alerts' option to navigate to the Alerts page.
        """
        try:
            alerts_option = self.driver.find_element(By.XPATH, self.OPTION_ALERTS_XPATH)
            alerts_option.click()
        except NoSuchElementException:
            print("Alerts option not found.")

    def click_on_click_me_and_see_alert_button(self):
        """
        Click on the 'Click Me and See Alert' button to trigger an alert.
        """
        try:
            alert_button = self.driver.find_element(By.XPATH, self.BUTTON_CLICK_ME_AND_SEE_ALERT_XPATH)
            alert_button.click()
        except NoSuchElementException:
            print("Click Me and See Alert button not found.")

    def click_on_after_five_seconds_button(self):
        """
        Click on the 'After Five Seconds' button to trigger a delayed alert.
        """
        try:
            delayed_alert_button = self.driver.find_element(By.XPATH, self.BUTTON_AFTER_FIVE_SECONDS_XPATH)
            delayed_alert_button.click()
        except NoSuchElementException:
            print("After Five Seconds button not found.")

    def click_on_confirm_box_button(self):
        """
        Click on the 'Confirm Box' button to trigger a confirmation dialog.
        Scrolls until the element is visible before clicking.
        """
        try:
            confirm_box_button = self.driver.find_element(By.XPATH, self.BUTTON_CONFIRM_BOX_XPATH)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", confirm_box_button)
            confirm_box_button.click()
        except NoSuchElementException:
            print("Confirm Box button not found.")

    def get_confirm_result_text(self):
        """
        Get the text from the confirmation result element.
        """
        try:
            confirm_result_text = self.driver.find_element(By.XPATH, self.TEXT_CONFIRM_RESULT_XPATH).text
            return confirm_result_text
        except NoSuchElementException:
            print("Confirm Result text not found.")
            return None

    def click_on_prompt_box_button(self):
        """
        Click on the 'Prompt Box' button to trigger a prompt dialog.
        Scrolls until the element is visible before clicking.
        """
        try:
            prompt_box_button = self.driver.find_element(By.XPATH, self.BUTTON_PROMPT_BOX_XPATH)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", prompt_box_button)
            prompt_box_button.click()
        except NoSuchElementException:
            print("Prompt Box button not found.")

    def get_prompt_result_text(self):
        """
        Get the text from the prompt result element.
        """
        try:
            prompt_result_text = self.driver.find_element(By.XPATH, self.TEXT_PROMPT_RESULT_XPATH).text
            return prompt_result_text
        except NoSuchElementException:
            print("Prompt Result text not found.")
            return None

    def click_on_modal_option(self):
        """
        Click on the 'Modal Dialogs' option to navigate to the Modal Dialogs page.
        Scrolls until the element is visible before clicking.
        """
        try:
            modal_option = self.driver.find_element(By.XPATH, self.OPTION_MODAL_XPATH)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", modal_option)
            modal_option.click()
        except NoSuchElementException:
            print("Modal Dialogs option not found.")

    def click_on_small_modal_button(self):
        """
        Click on the 'Small Modal' button to open a small modal dialog.
        """
        try:
            small_modal_button = self.driver.find_element(By.XPATH, self.BUTTON_SMALL_MODAL_XPATH)
            small_modal_button.click()
        except NoSuchElementException:
            print("Small Modal button not found.")

    def get_modal_content_text(self):
        """
        Get the text content from the modal dialog.
        """
        try:
            modal_content_text = self.driver.find_element(By.XPATH, self.TEXT_MODAL_CONTENT_XPATH).text
            return modal_content_text
        except NoSuchElementException:
            print("Modal content text not found.")
            return None

    def get_name_of_small_modal_text(self):
        """
        Get the name of the small modal dialog.
        """
        try:
            small_modal_name = self.driver.find_element(By.XPATH, self.TEXT_NAME_OF_SMALL_MODAL_XPATH).text
            return small_modal_name
        except NoSuchElementException:
            print("Name of small modal text not found.")
            return None

    def close_small_modal(self):
        """
        Close the small modal dialog.
        """
        try:
            close_button = self.driver.find_element(By.XPATH, self.BUTTON_CLOSE_SMALL_MODAL_XPATH)
            close_button.click()
        except NoSuchElementException:
            print("Close Small Modal button not found.")

    def get_name_of_the_page_text(self):
        """
        Get the name of the page from the modal dialogs section.
        """
        try:
            page_name = self.driver.find_element(By.XPATH, self.TEXT_NAME_OF_THE_PAGE_XPATH).text
            return page_name
        except NoSuchElementException:
            print("Name of the page text not found.")
            return None

    # Large Modal Dialogs
    def click_on_large_modal_button(self):
        """
        Click on the 'Large Modal' button to open a large modal dialog.
        """
        try:
            large_modal_button = self.driver.find_element(By.XPATH, self.BUTTON_LARGE_MODAL_XPATH)
            large_modal_button.click()
        except NoSuchElementException:
            print("Large Modal button not found.")

    def get_name_of_large_modal_text(self):
        """
        Get the name of the large modal dialog.
        """
        try:
            large_modal_name = self.driver.find_element(By.XPATH, self.NAME_OF_THE_LARGE_MODAL_XPATH).text
            return large_modal_name
        except NoSuchElementException:
            print("Name of large modal text not found.")
            return None

    def get_content_of_large_modal_text(self):
        """
        Get the content text from the large modal dialog.
        """
        try:
            large_modal_content = self.driver.find_element(By.XPATH, self.TEXT_CONTENT_OF_THE_LARGE_MODAL_XPATH).text
            return large_modal_content
        except NoSuchElementException:
            print("Content of large modal text not found.")
            return None

    def close_large_modal(self):
        """
        Close the large modal dialog.
        """
        try:
            close_button = self.driver.find_element(By.XPATH, self.BUTTON_LARGE_MODAL_CLOSE_XPATH)
            close_button.click()
        except NoSuchElementException:
            print("Close Large Modal button not found.")

    def click_on_frames_option(self):
        """
        Click on the 'Frames' option to navigate to the Frames page.
        """
        try:
            frames_option = self.driver.find_element(By.XPATH, self.OPTION_FRAMES_XPATH)
            frames_option.click()
        except NoSuchElementException:
            print("Frames option not found.")

    def switch_to_frame(self):
        """
        Switch to the iframe with id 'frame1'.
        """
        try:
            frame = self.driver.find_element(By.XPATH, self.SWITCH_FRAME_XPATH)
            self.driver.switch_to.frame(frame)
        except NoSuchElementException:
            print("Frame not found.")
        except Exception as e:
            print(f"Failed to switch to frame: {e}")

    def get_text_from_iframe(self):
        """
        Get the text from the iframe after switching to it.
        """
        try:
            iframe_text = self.driver.find_element(By.XPATH, self.TEXT_OF_IFRAME_XPATH).text
            return iframe_text
        except NoSuchElementException:
            print("Text in the iframe not found.")
            return None
        except Exception as e:
            print(f"Failed to get text from iframe: {e}")
            return None

    def switch_to_default_content(self):
        """
        Switch back to the default content from the iframe.
        """
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print(f"Failed to switch back to default content: {e}")

    #  Nested Frame Locators
    def click_on_nested_iframe_option(self):
        """
        Click on the 'Nested Frames' option.
        """
        try:
            nested_iframe_option = self.driver.find_element(By.XPATH, self.OPTION_NESTED_IFRAME_XPATH)
            nested_iframe_option.click()
        except NoSuchElementException:
            print("Nested Frames option not found.")

    def get_main_nested_frame_text(self):
        """
        Get the text of the main nested frame heading.
        """
        try:
            heading = self.driver.find_element(By.XPATH, self.TEXT_OF_THR_MAIN_NESTED_FRAME_XPATH)
            return heading.text
        except NoSuchElementException:
            print("Main nested frame heading not found.")
            return None

    def switch_to_parent_frame(self):
        """
        Switch to the parent iframe.
        """
        try:
            parent_frame = self.driver.find_element(By.XPATH, self.PARENT_FRAME_XPATH)
            self.driver.switch_to.frame(parent_frame)
        except NoSuchElementException:
            print("Parent iframe not found.")

    def switch_to_child_frame(self):
        """
        Switch to the child iframe inside the parent.
        """
        try:
            child_frame = self.driver.find_element(By.XPATH, self.CHILD_FRAME_XPATH)
            self.driver.switch_to.frame(child_frame)
        except NoSuchElementException:
            print("Child iframe not found.")
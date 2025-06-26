from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class WidgetsPage:

    # Locators for the Widgets page elements
    # Accordion
    TEXT_OPTION_ACCORDION_XPATH = "//span[normalize-space()='Accordian']"

    SECOND_ACCORDION_SECTION_CSS_SELECTOR = "#section2Heading"
    SECOND_ACCORDION_CONTENT_XPATH = "//p[contains(text(),'Contrary to popular belief, Lorem Ipsum is not sim')]"

    FIRST_ACCORDION_SECTION_CSS_SELECTOR = "#section1Heading"
    FIRST_ACCORDION_CONTENT_XPATH = "//p[contains(text(),'Lorem Ipsum is simply dummy text of the printing a')]"

    THIRD_ACCORDION_SECTION_CSS_SELECTOR = "#section3Heading"
    THIRD_ACCORDION_CONTENT_XPATH = "//p[contains(text(),'It is a long established fact that a reader will b')]"

    # Auto Complete
    TEXT_OPTIONS_AUTO_COMPLETE_XPATH = "//span[normalize-space()='Auto Complete']"
    INPUT_MULTIPLE_COLOR_AUTO_COMPLETE_CSS_SELECTOR = ".auto-complete__value-container.auto-complete__value-container--is-multi.css-1hwfws3"
    SELECTED_COLORS_AUTO_COMPLETE_CSS_SELECTOR = "//div[@class = 'css-1rhbuit-multiValue auto-complete__multi-value']"

    def __init__(self, driver):
        """
        Initialize the WidgetsPage object.
        """
        self.driver = driver

    def scroll_until_element_visible(self, by, locator, max_scrolls=10):
        """
        Scrolls the page until the element specified by `by` and `locator` is visible or max_scrolls is reached.
        # """
        for _ in range(max_scrolls):
            try:
                element = self.driver.find_element(by, locator)
                if element.is_displayed():
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                    return element
            except NoSuchElementException:
                pass
            self.driver.execute_script("window.scrollBy(0, 200);")
        raise Exception(f"Element not visible after scrolling: {locator}")

    # Accordion
    def click_accordion_option(self):
        """
        Click on the Accordion element if not already open.
        """
        element = self.scroll_until_element_visible(By.XPATH, self.TEXT_OPTION_ACCORDION_XPATH)
        element.click()

    def clicks_on_second_accordion_section(self):
        """
        Click on the second accordion section.
        """
        element = self.scroll_until_element_visible(By.CSS_SELECTOR, self.SECOND_ACCORDION_SECTION_CSS_SELECTOR)
        element.click()

    def get_second_accordion_content_text(self):
        """
        Get the text of the content in the second accordion section.
        """
        element = self.scroll_until_element_visible(By.XPATH, self.SECOND_ACCORDION_CONTENT_XPATH)
        return element.text

    def clicks_on_first_accordion_section(self):
        """
        Click on the first accordion section.
        """
        element = self.scroll_until_element_visible(By.CSS_SELECTOR, self.FIRST_ACCORDION_SECTION_CSS_SELECTOR)
        element.click()

    def get_first_accordion_content_text(self):
        """
        Get the text of the content in the first accordion section.
        """
        element = self.scroll_until_element_visible(By.XPATH, self.FIRST_ACCORDION_CONTENT_XPATH)
        return element.text

    def clicks_on_third_accordion_section(self):
        """
        Click on the third accordion section.
        """
        element = self.scroll_until_element_visible(By.CSS_SELECTOR, self.THIRD_ACCORDION_SECTION_CSS_SELECTOR)
        element.click()

    def get_third_accordion_content_text(self):
        """
        Get the text of the content in the third accordion section.
        """
        element = self.scroll_until_element_visible(By.XPATH, self.THIRD_ACCORDION_CONTENT_XPATH)
        return element.text

    # Auto Complete
    def click_auto_complete_option(self):
        """
        Click on the Auto Complete element.
        """
        element = self.scroll_until_element_visible(By.XPATH, self.TEXT_OPTIONS_AUTO_COMPLETE_XPATH)
        element.click()

    def get_input_multiple_color_auto_complete(self, colors):
        """
        Inputs multiple color values into a multi-select auto-complete field.

        :param colors: List of color strings to input, e.g., ['Red', 'Blue', 'Green']
        :return: The input WebElement after all colors are entered
        """
        # Scroll to the multi-select auto-complete input container and ensure it is visible
        container = self.scroll_until_element_visible(
            By.CSS_SELECTOR, self.INPUT_MULTIPLE_COLOR_AUTO_COMPLETE_CSS_SELECTOR
        )

        # Locate the actual input field inside the container
        input_element = container.find_element(By.TAG_NAME, "input")

        # Initialize an explicit wait to handle dynamic elements like dropdown suggestions
        wait = WebDriverWait(self.driver, 10)

        # Iterate through the list of colors and enter each one
        for color in colors:
            # Focus on the input field
            input_element.click()

            # Clear any existing text in the input (useful if input retains previous entries)
            input_element.clear()

            # Type the color name into the input field
            input_element.send_keys(color)

            # Wait until the suggestion dropdown becomes visible before proceeding
            wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".auto-complete__menu")  # Ensure this matches your app’s dropdown class
            ))

            # Press ENTER to select the currently highlighted suggestion from the dropdown
            input_element.send_keys(Keys.ENTER)

        # Return the input element in case further actions are needed
        return input_element

    def get_selected_colors_auto_complete(self):
        """
        Get the text of the selected colors in the auto-complete field.

        :return: List of selected color texts
        """
        elements = self.driver.find_elements(By.XPATH, self.SELECTED_COLORS_AUTO_COMPLETE_CSS_SELECTOR)
        return [element.text for element in elements if element.is_displayed()]
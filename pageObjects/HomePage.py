from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    # Locators for elements on the home page
    LOGO_HOME_PAGE_XPATH = "//img[@src='/images/Toolsqa.jpg']"
    LINK_TEXT_JOIN_NOW_XPATH = "//a[@href='https://www.toolsqa.com/selenium-training/']"
    TOTAL_LINKS_TAG_NAME = "a"
    CARDS_COUNT_XPATH = "//div[@class = 'card mt-4 top-card']"
    CARD_ELEMENT_XPATH = "(//div[@class='card mt-4 top-card'])[1]"
    CARD_FORMS_XPATH = "(//div[@class='card mt-4 top-card'])[2]"
    CARD_ALERTS_FRAME_WINDOWS_XPATH = "(//div[@class='card mt-4 top-card'])[3]"
    CARD_WIDGETS_XPATH = "(//div[@class='card mt-4 top-card'])[4]"
    CARD_INTERACTIONS_XPATH = "(//div[@class='card mt-4 top-card'])[5]"
    CARD_BOOK_STORE_APPLICATION_XPATH = "(//div[@class='card mt-4 top-card'])[6]"



    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def logo_is_displayed(self):
        """
        Check if the logo is displayed on the home page.
        """
        try:
            logo = self.driver.find_element(By.XPATH, self.LOGO_HOME_PAGE_XPATH)
            return logo.is_displayed()
        except NoSuchElementException:
            return False

    def clicks_on_join_now_button(self):
        """
        Click on the 'Join Now' button.
        """
        try:
            join_now_button = self.driver.find_element(By.XPATH, self.LINK_TEXT_JOIN_NOW_XPATH)
            join_now_button.click()
        except NoSuchElementException:
            print("Join Now button not found.")

    def get_total_links_count(self):
        """
        Get the total number of links on the home page.
        """
        return len(self.driver.find_elements(By.TAG_NAME, self.TOTAL_LINKS_TAG_NAME))

    def get_cards_count(self):
        """
        Get the count of cards on the home page.
        """
        try:
            cards = self.driver.find_elements(By.XPATH, self.CARDS_COUNT_XPATH)
            return len(cards)
        except NoSuchElementException:
            return 0

    def scroll_and_click(self, xpath, element_name, timeout=10, scroll_attempts=5):
        """
        Scroll to the element and click it after ensuring it is visible and clickable.
        """
        try:
            for attempt in range(scroll_attempts):
                try:
                    # Wait for presence in the DOM
                    element = WebDriverWait(self.driver, timeout).until(
                        EC.presence_of_element_located((By.XPATH, xpath))
                    )

                    # Scroll to the element
                    self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                               element)

                    # Wait until it's visible and clickable
                    element = WebDriverWait(self.driver, timeout).until(
                        EC.element_to_be_clickable((By.XPATH, xpath))
                    )

                    # Click the element
                    element.click()
                    return
                except TimeoutException:
                    # Try again after a short pause if element isn't clickable yet
                    continue

            print(f"{element_name} card could not be clicked after {scroll_attempts} scroll attempts.")
        except NoSuchElementException:
            print(f"{element_name} card not found.")

    def click_on_elements_card(self):
        """Click on the 'Elements' card."""
        self.scroll_and_click(self.CARD_ELEMENT_XPATH, "Elements")

    def click_on_forms_card(self):
        """Click on the 'Forms' card."""
        self.scroll_and_click(self.CARD_FORMS_XPATH, "Forms")

    def click_on_alerts_frame_windows_card(self):
        """Click on the 'Alerts, Frame & Windows' card."""
        self.scroll_and_click(self.CARD_ALERTS_FRAME_WINDOWS_XPATH, "Alerts, Frame & Windows")

    def click_on_widgets_card(self):
        """Click on the 'Widgets' card."""
        self.scroll_and_click(self.CARD_WIDGETS_XPATH, "Widgets")

    def click_on_interactions_card(self):
        """Click on the 'Interactions' card."""
        self.scroll_and_click(self.CARD_INTERACTIONS_XPATH, "Interactions")

    def click_on_book_store_application_card(self):
        """Click on the 'Book Store Application' card."""
        self.scroll_and_click(self.CARD_BOOK_STORE_APPLICATION_XPATH, "Book Store Application")
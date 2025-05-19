from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


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

    def click_on_elements_card(self):
        """
        Click on the 'Elements' card.
        """
        try:
            elements_card = self.driver.find_element(By.XPATH, self.CARD_ELEMENT_XPATH)
            elements_card.click()
        except NoSuchElementException:
            print("Elements card not found.")

    def click_on_forms_card(self):
        """
        Click on the 'Forms' card.
        """
        try:
            forms_card = self.driver.find_element(By.XPATH, self.CARD_FORMS_XPATH)
            forms_card.click()
        except NoSuchElementException:
            print("Forms card not found.")

    def click_on_alerts_frame_windows_card(self):
        """
        Click on the 'Alerts, Frame & Windows' card.
        """
        try:
            alerts_frame_windows_card = self.driver.find_element(By.XPATH, self.CARD_ALERTS_FRAME_WINDOWS_XPATH)
            alerts_frame_windows_card.click()
        except NoSuchElementException:
            print("Alerts, Frame & Windows card not found.")

    def click_on_widgets_card(self):
        """
        Click on the 'Widgets' card.
        """
        try:
            widgets_card = self.driver.find_element(By.XPATH, self.CARD_WIDGETS_XPATH)
            widgets_card.click()
        except NoSuchElementException:
            print("Widgets card not found.")

    def click_on_interactions_card(self):
        """
        Click on the 'Interactions' card.
        """
        try:
            interactions_card = self.driver.find_element(By.XPATH, self.CARD_INTERACTIONS_XPATH)
            interactions_card.click()
        except NoSuchElementException:
            print("Interactions card not found.")

    def click_on_book_store_application_card(self):
        """
        Click on the 'Book Store Application' card.
        """
        try:
            book_store_application_card = self.driver.find_element(By.XPATH, self.CARD_BOOK_STORE_APPLICATION_XPATH)
            book_store_application_card.click()
        except NoSuchElementException:
            print("Book Store Application card not found.")
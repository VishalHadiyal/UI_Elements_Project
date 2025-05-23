from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class WebTable:

    # Locators for elements on the web table page
    ADD_BUTTON = "//button[@id='addNewRecordButton']"
    SEARCH_BOX = "//input[@id='searchBox']"
    ROWS = ".rt-tbody .rt-tr-group"
    TABLE_CELLS = ".rt-td"
    DELETE_BUTTONS = 'span[title="Delete"]'
    EDIT_BUTTONS = 'span[title="Edit"]'

    # Add New Record locators
    TXT_FIRST_NAME_XPATH = "//input[@id='firstName']"
    TXT_LAST_NAME_XPATH = "//input[@id='lastName']"
    TXT_EMAIL_XPATH = "//input[@id='userEmail']"
    TXT_AGE_XPATH = "//input[@id='age']"
    TXT_SALARY_XPATH = "//input[@id='salary']"
    TXT_DEPARTMENT_XPATH = "//input[@id='department']"
    BTN_SUBMIT_XPATH = "//button[@id='submit']"

    def __init__(self, driver):
        self.driver = driver

    def scroll_and_click(self, xpath, element_name, timeout=10, scroll_attempts=5):
        try:
            for attempt in range(scroll_attempts):
                try:
                    element = WebDriverWait(self.driver, timeout).until(
                        EC.presence_of_element_located((By.XPATH, xpath))
                    )
                    self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
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
        # Optional utility: generate unique XPath for dynamic elements if needed
        # This is a placeholder; replace with actual logic or XPath attributes.
        return self.driver.execute_script("""
            function getElementXPath(elt) {
                var path = "";
                for (; elt && elt.nodeType == 1; elt = elt.parentNode) {
                    idx = getElementIdx(elt);
                    xname = elt.tagName;
                    if (idx > 1) xname += "[" + idx + "]";
                    path = "/" + xname + path;
                }
                return path.toLowerCase();
                function getElementIdx(elt) {
                    var count = 1;
                    for (var sib = elt.previousSibling; sib ; sib = sib.previousSibling) {
                        if(sib.nodeType == 1 && sib.tagName == elt.tagName) count++
                    }
                    return count;
                }
            }
            return getElementXPath(arguments[0]);
        """, element)

    def wait_for_table(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.ROWS))
        )

    def get_all_rows(self):
        self.wait_for_table()
        return self.driver.find_elements(By.CSS_SELECTOR, self.ROWS)

    def get_row_data(self, row_index):
        rows = self.get_all_rows()
        if row_index < len(rows):
            cells = rows[row_index].find_elements(By.CSS_SELECTOR, self.TABLE_CELLS)
            return [cell.text.strip() for cell in cells]
        return []

    def find_row_by_email(self, email):
        rows = self.get_all_rows()
        for index, row in enumerate(rows):
            if email in row.text:
                return index
        return -1

    def click_edit_by_email(self, email, timeout=10):
        index = self.find_row_by_email(email)
        if index != -1:
            element = self.get_all_rows()[index].find_element(By.CSS_SELECTOR, self.EDIT_BUTTONS)
            xpath = element.get_attribute("xpath") or self.generate_xpath(element)
            self.scroll_and_click(xpath, "Edit button", timeout)

    def click_edit_by_index(self, index, timeout=10):
        rows = self.get_all_rows()
        if index < len(rows):
            element = rows[index].find_element(By.CSS_SELECTOR, self.EDIT_BUTTONS)
            xpath = element.get_attribute("xpath") or self.generate_xpath(element)
            self.scroll_and_click(xpath, "Edit button", timeout)

    def click_delete_by_email(self, email):
        index = self.find_row_by_email(email)
        if index != -1:
            element = self.get_all_rows()[index].find_element(By.CSS_SELECTOR, self.DELETE_BUTTONS)
            xpath = element.get_attribute("xpath") or self.generate_xpath(element)
            self.scroll_and_click(xpath, "Delete button")

    def search(self, keyword):
        keyword = str(keyword) if keyword is not None else ""
        search_box = self.driver.find_element(By.XPATH, self.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(keyword)

    def click_add_button(self):
        self.scroll_and_click(self.ADD_BUTTON, "Add Button")

    def fill_add_new_record_form(self, first_name, last_name, email, age, salary, department):
        self.driver.find_element(By.XPATH, self.TXT_FIRST_NAME_XPATH).clear()
        self.driver.find_element(By.XPATH, self.TXT_FIRST_NAME_XPATH).send_keys(first_name)
        self.driver.find_element(By.XPATH, self.TXT_LAST_NAME_XPATH).clear()
        self.driver.find_element(By.XPATH, self.TXT_LAST_NAME_XPATH).send_keys(last_name)
        self.driver.find_element(By.XPATH, self.TXT_EMAIL_XPATH).clear()
        self.driver.find_element(By.XPATH, self.TXT_EMAIL_XPATH).send_keys(email)
        self.driver.find_element(By.XPATH, self.TXT_AGE_XPATH).clear()
        self.driver.find_element(By.XPATH, self.TXT_AGE_XPATH).send_keys(age)
        self.driver.find_element(By.XPATH, self.TXT_SALARY_XPATH).clear()
        self.driver.find_element(By.XPATH, self.TXT_SALARY_XPATH).send_keys(salary)
        self.driver.find_element(By.XPATH, self.TXT_DEPARTMENT_XPATH).clear()
        self.driver.find_element(By.XPATH, self.TXT_DEPARTMENT_XPATH).send_keys(department)

    def click_submit_button(self):
        self.scroll_and_click(self.BTN_SUBMIT_XPATH, "Submit Button")

    def get_row_data_by_index(self, row_index):
        rows = self.get_all_rows()
        if row_index < len(rows):
            cells = rows[row_index].find_elements(By.CSS_SELECTOR, self.TABLE_CELLS)
            return [cell.text.strip() for cell in cells]
        return []

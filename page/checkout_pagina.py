from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    POSTAL_CODE_INPUT = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    CANCEL_BUTTON = (By.ID, 'cancel')
    ERROR_MESSAGE = (By.CLASS_NAME, 'error-message-container')

    def __init__(self, driver):
        self.driver = driver

    def is_at_page(self):
        return '/checkout-step-one.html' in self.driver.current_url

    def fill_customer_info(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FIRST_NAME_INPUT)
        ).send_keys(first_name)
        
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(postal_code)

    def continue_to_overview(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

    def cancel_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CANCEL_BUTTON)
        ).click()

    def get_error_message(self):
        try:
            error_element = self.driver.find_element(*self.ERROR_MESSAGE)
            return error_element.text
        except:
            return ""
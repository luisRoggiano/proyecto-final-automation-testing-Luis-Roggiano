from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutCompletePage:
    URL_CURRENT = '/checkout-complete.html'
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'complete-header')
    SUCCESS_TEXT = (By.CLASS_NAME, 'complete-text')
    BACK_HOME_BUTTON = (By.ID, 'back-to-products')
    PONY_EXPRESS_IMAGE = (By.CLASS_NAME, 'pony_express')

    def __init__(self, driver):
        self.driver = driver

    def is_at_page(self):
        return self.URL_CURRENT in self.driver.current_url

    def get_success_message(self):
        try:
            return self.driver.find_element(*self.SUCCESS_MESSAGE).text
        except:
            return ""

    def get_success_text(self):
        try:
            return self.driver.find_element(*self.SUCCESS_TEXT).text
        except:
            return ""

    def back_to_home(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BACK_HOME_BUTTON)
        ).click()

    def is_success_image_displayed(self):
        try:
            return self.driver.find_element(*self.PONY_EXPRESS_IMAGE).is_displayed()
        except:
            return False
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:

    URL_CURRENT = '/inventory.html'
    MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
    LINK_BUTTON = (By.ID, 'logout_sidebar_link')
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')

    def __init__(self , driver):
        self.driver = driver

    def is_at_page( self ):
        return self.URL_CURRENT in self.driver.current_url
    
    def add_product_to_cart(self, product_index=0):
        add_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTON)
        if add_buttons and product_index < len(add_buttons):
            add_buttons[product_index].click()

    def go_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()
    
    def logout( self ):
        self.driver.find_element(*self.MENU_BUTTON).click()
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LINK_BUTTON)
        ).click()
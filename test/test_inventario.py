from page.login import LoginPage
from page.inventario import InventoryPage
import time

def test_inventory( driver ):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    time.sleep(10)

    inventory.is_at_page()

    inventory.logout()
    time.sleep(4)
    assert "https://www.saucedemo.com/" in driver.current_url
   
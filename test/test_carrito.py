import pytest
from page.login import LoginPage
from page.inventario import InventoryPage
from page.paginaCarrito import CartPage
import time

def test_cart_operations(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")
    
    time.sleep(3)
    # Agregar producto y ir al carrito
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    
    assert cart.is_at_page()
    assert cart.get_cart_items_count() == 1
    
    # Continuar comprando
    cart.continue_shopping()
    assert inventory.is_at_page()

def test_remove_from_cart(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")
    time.sleep(3)
    
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    
    initial_count = cart.get_cart_items_count()
    cart.remove_item(0)
    
    assert cart.get_cart_items_count() == initial_count - 1
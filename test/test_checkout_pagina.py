import pytest
from page.login import LoginPage
from page.inventario import InventoryPage
from page.paginaCarrito import CartPage
from page.checkout_pagina import CheckoutPage

import time

def test_checkout_process(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")
    time.sleep(4)
    
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    time.sleep(4)
    cart.go_to_checkout()
    time.sleep(3)
    
    assert checkout.is_at_page()
    
    # Llenar información
    checkout.fill_customer_info("John", "Doe", "12345")
    checkout.continue_to_overview()
    
    assert "checkout-step-two" in driver.current_url

def test_checkout_validation(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    time.sleep(4)
    
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    cart.go_to_checkout()
    
    # Intentar continuar sin información
    checkout.continue_to_overview()
    
    error_message = checkout.get_error_message()
    assert "First Name is required" in error_message
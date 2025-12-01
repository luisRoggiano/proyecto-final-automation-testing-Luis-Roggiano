import pytest
from page.login import LoginPage
from page.inventario import InventoryPage
from page.paginaCarrito import CartPage
from page.checkout_pagina import CheckoutPage
import time
import logging

# Configuración básica del logging para registrar eventos en las pruebas
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_checkout_process(driver):
    """
    Prueba el proceso de checkout: agregar un producto, navegar al carrito, ir a checkout,
    llenar información del cliente y verificar navegación al overview.
    """
    logging.info("Iniciando prueba: test_checkout_process")  # Log 1: Inicio de la prueba
    
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # Abrir la página de login y realizar el inicio de sesión
    login.open()
    login.login("standard_user", "secret_sauce")
    time.sleep(4)  # Espera para que la página cargue completamente (considera reemplazar con waits explícitos)
    
    # Agregar producto, navegar al carrito e ir a checkout
    logging.info("Agregando producto, navegando al carrito e iniciando checkout")  # Log 2: Acción principal
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    time.sleep(4)
    cart.go_to_checkout()
    time.sleep(3)
    
    # Verificar página de checkout y llenar información
    logging.info("Verificando página de checkout y llenando información del cliente")  # Log 3: Verificación y acción secundaria
    assert checkout.is_at_page(), "No se detectó la página de checkout"  # Aserción con mensaje para depuración
    
    # Llenar información y continuar
    checkout.fill_customer_info("John", "Doe", "12345")
    checkout.continue_to_overview()
    
    assert "checkout-step-two" in driver.current_url, "No se navegó al overview de checkout"  # Aserción con mensaje
    
    logging.info("Prueba test_checkout_process completada exitosamente")  # Log 4: Fin de la prueba

def test_checkout_validation(driver):
    """
    Prueba la validación en checkout: intentar continuar sin información y verificar mensaje de error.
    """
    logging.info("Iniciando prueba: test_checkout_validation")  # Log 1: Inicio de la prueba
    
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # Abrir la página de login y realizar el inicio de sesión
    login.open()
    login.login("standard_user", "secret_sauce")
    time.sleep(4)  # Espera para que la página cargue completamente (considera reemplazar con waits explícitos)
    
    # Agregar producto, navegar al carrito e ir a checkout
    logging.info("Agregando producto, navegando al carrito e iniciando checkout")  # Log 2: Acción principal
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    cart.go_to_checkout()
    
    # Intentar continuar sin información y obtener mensaje de error
    logging.info("Intentando continuar sin información y verificando error")  # Log 3: Acción secundaria y verificación
    checkout.continue_to_overview()
    
    error_message = checkout.get_error_message()
    assert "First Name is required" in error_message, "El mensaje de error no coincide"  # Aserción con mensaje
    
    logging.info("Prueba test_checkout_validation completada exitosamente")  # Log 4: Fin de la prueba
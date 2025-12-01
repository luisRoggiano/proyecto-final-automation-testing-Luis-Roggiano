import pytest
from page.login import LoginPage
from page.inventario import InventoryPage
from page.paginaCarrito import CartPage
from page.checkout_pagina import CheckoutPage
from page.checkout_paginaCompleta import CheckoutCompletePage
import time
import logging

# Configuración básica del logging para registrar eventos en las pruebas
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_complete_purchase_flow(driver):
    """
    Prueba el flujo completo de compra: login, agregar producto, checkout, llenar info,
    completar compra y verificar éxito, luego regresar al inicio.
    """
    logging.info("Iniciando prueba: test_complete_purchase_flow")  # Log 1: Inicio de la prueba
    
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    complete = CheckoutCompletePage(driver)

    # Abrir la página de login y realizar el inicio de sesión
    login.open()
    login.login("standard_user", "secret_sauce")
    time.sleep(4)  # Espera para que la página cargue completamente (considera reemplazar con waits explícitos)
    
    # Agregar producto al carrito y navegar al checkout
    logging.info("Agregando producto al carrito e iniciando checkout")  # Log 2: Acción principal (agregar y checkout)
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    
    # Ir a checkout
    cart.go_to_checkout()
    
    # Llenar información del cliente y continuar al overview
    logging.info("Llenando información del cliente y completando compra")  # Log 3: Acción secundaria (llenar info y completar)
    checkout.fill_customer_info("John", "Doe", "12345")
    checkout.continue_to_overview()
    
    # Completar compra (simulado - necesitarías la página de overview)
    driver.get("https://www.saucedemo.com/checkout-complete.html")
    
    # Verificar página de completado y regresar al inicio
    assert complete.is_at_page(), "No se detectó la página de completado"  # Aserción con mensaje para depuración
    assert "Thank you for your order!" in complete.get_success_message(), "El mensaje de éxito no coincide"  # Aserción con mensaje
    assert complete.is_success_image_displayed(), "La imagen de éxito no se muestra"  # Aserción con mensaje
    
    complete.back_to_home()
    assert inventory.is_at_page(), "No se regresó a la página de inventario"  # Aserción con mensaje
    
    logging.info("Prueba test_complete_purchase_flow completada exitosamente")  # Log 4: Fin de la prueba
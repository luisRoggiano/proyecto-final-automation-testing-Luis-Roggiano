import pytest
from page.login import LoginPage
from page.inventario import InventoryPage
from page.paginaCarrito import CartPage
import time
import logging

# Configuración básica del logging para registrar eventos en las pruebas
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_cart_operations(driver):
    """
    Prueba las operaciones básicas del carrito: agregar un producto, verificar presencia en el carrito,
    continuar comprando y verificar regreso al inventario.
    """
    logging.info("Iniciando prueba: test_cart_operations")  # Log 1: Inicio de la prueba
    
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    # Abrir la página de login y realizar el inicio de sesión
    login.open()
    login.login("standard_user", "secret_sauce")
    
    time.sleep(3)  # Espera para que la página cargue completamente (considera reemplazar con waits explícitos)
    
    # Agregar el primer producto al carrito y navegar al carrito
    logging.info("Agregando producto y navegando al carrito")  # Log 2: Acción principal
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    
    # Verificar que estamos en la página del carrito y que hay 1 item
    logging.info("Verificando página y conteo de items en el carrito")  # Log 3: Verificación
    assert cart.is_at_page(), "No se detectó la página del carrito"  # Aserción con mensaje para depuración
    assert cart.get_cart_items_count() == 1, "El conteo de items no es 1"  # Aserción con mensaje
    
    # Continuar comprando y verificar regreso al inventario
    cart.continue_shopping()
    assert inventory.is_at_page(), "No se regresó a la página de inventario"  # Aserción con mensaje
    
    logging.info("Prueba test_cart_operations completada exitosamente")  # Log 4: Fin de la prueba

def test_remove_from_cart(driver):
    """
    Prueba la remoción de un producto del carrito: agregar un producto, navegar al carrito,
    removerlo y verificar que el conteo disminuya.
    """
    logging.info("Iniciando prueba: test_remove_from_cart")  # Log 1: Inicio de la prueba
    
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    # Abrir la página de login y realizar el inicio de sesión
    login.open()
    login.login("standard_user", "secret_sauce")
    time.sleep(3)  # Espera para que la página cargue completamente (considera reemplazar con waits explícitos)
    
    # Agregar el primer producto al carrito y navegar al carrito
    logging.info("Agregando producto y navegando al carrito")  # Log 2: Acción principal
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    
    # Obtener conteo inicial de items y remover el producto
    initial_count = cart.get_cart_items_count()
    logging.info("Removiendo item del carrito")  # Log 3: Acción de remoción
    cart.remove_item(0)
    
    # Verificar que el conteo disminuyó en 1
    assert cart.get_cart_items_count() == initial_count - 1, f"El conteo no disminuyó (esperado: {initial_count - 1}, actual: {cart.get_cart_items_count()})"  # Aserción con mensaje detallado
    
    logging.info("Prueba test_remove_from_cart completada exitosamente")  # Log 4: Fin de la prueba
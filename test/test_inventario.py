import pytest
from page.login import LoginPage
from page.inventario import InventoryPage
import time
import logging

# Configuración básica del logging para registrar eventos en las pruebas
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_inventory(driver):
    """
    Prueba la página de inventario: realizar login, verificar presencia en inventario,
    logout y verificar regreso a la página principal.
    """
    logging.info("Iniciando prueba: test_inventory")  # Log 1: Inicio de la prueba
    
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    # Abrir la página de login y realizar el inicio de sesión
    logging.info("Abriendo página de login e iniciando sesión")  # Log 2: Acción principal (login)
    login.open()
    login.login("standard_user", "secret_sauce")

    time.sleep(10)  # Espera para que la página cargue completamente (considera reemplazar con waits explícitos)

    # Verificar presencia en la página de inventario
    logging.info("Verificando página de inventario y realizando logout")  # Log 3: Verificación y acción secundaria (logout)
    inventory.is_at_page()

    inventory.logout()
    time.sleep(4)
    assert "https://www.saucedemo.com/" in driver.current_url, "No se regresó a la página principal después del logout"  # Aserción con mensaje para depuración
    
    logging.info("Prueba test_inventory completada exitosamente")  # Log 4: Fin de la prueba
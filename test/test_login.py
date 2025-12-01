import pytest
from page.login import LoginPage
from data.data_login import CASOS_LOGIN
from utils.example_json import get_login_json
from utils.faker import get_login_faker
import logging
import time

# Configuración básica del logging (se aplicará a todos los tests)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@pytest.mark.parametrize("username,password,login_bool", CASOS_LOGIN)
def test_login(driver, username, password, login_bool):
    """
    Prueba parametrizada del flujo de login con diferentes usuarios:
    - standard_user → éxito
    - locked_out_user → error
    - usuario malo → error
    """
    logging.info(f"Iniciando prueba de login → usuario: '{username}'")  # Log 1: Inicio de cada caso

    login_page = LoginPage(driver)

    # Paso 1: Abrir página y hacer login
    logging.info("Abriendo página de login y enviando credenciales")  # Log 2: Acción principal
    login_page.open()
    login_page.login(username, password)

    # Paso 2: Validar resultado esperado
    if login_bool:
        logging.info("Caso exitoso → se espera redirección a inventario")  # Log 3: Caso positivo
        assert "inventory.html" in driver.current_url, \
            f"Login falló con usuario válido '{username}' → URL actual: {driver.current_url}"
    else:
        logging.info("Caso fallido → se espera que NO redirija a inventario")  # Log 3: Caso negativo
        assert "inventory.html" not in driver.current_url, \
            f"Login inesperado con credenciales inválidas '{username}' → URL actual: {driver.current_url}"

    logging.info(f"Prueba de login completada → usuario: '{username}' - Resultado: {'PASS' if login_bool else 'FAIL (esperado)'}")  # Log 4: Fin del caso
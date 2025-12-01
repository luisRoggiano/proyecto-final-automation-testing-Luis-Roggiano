from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import os

URL = 'https://www.saucedemo.com/'

def get_driver():
    # Configuración de opciones para deshabilitar pop-ups y gestor de contraseñas
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    
    # Anulamos pop-ups de Chrome y otras notificaciones
    chrome_options.add_argument("--disable-features=OptimizationGuide")
    chrome_options.add_argument("--disable-features=PasswordManagerV1")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-notifications")
    
    # Modo incognito + guest para evitar almacenamiento de credenciales
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--guest")
    
    # Opcional: Si quieres headless (sin ventana), agrégalo aquí (pero quítalo para depurar)
    # chrome_options.add_argument("--headless")

    # Instalación y servicio del driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.implicitly_wait(5)  # Wait implícito de 5 segundos (puedes ajustar)

    return driver

def get_file_path(file_name, folder="data"):
    # Ruta relativa
    current_file = os.path.dirname(__file__)  # El archivo donde estoy
    file_path = os.path.join(current_file, "..", folder, file_name)
    return os.path.abspath(file_path)

# Función adicional para login (puedes usarla en pruebas si quieres centralizar)
def login_saucedemo(driver, username='standard_user', password='secret_sauce'):
    driver.get(URL)
    driver.find_element(By.NAME, 'user-name').send_keys(username)
    time.sleep(1)
    driver.find_element(By.NAME, 'password').send_keys(password)
    time.sleep(1)
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(5)
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import os

# Ruta relativa para screenshots
SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), 'screenshots')

@pytest.fixture(scope="function")
def driver(request):
    # Opciones para deshabilitar pop-ups de contraseña
    options = Options()
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,                # Deshabilita servicio de credenciales
        "profile.password_manager_enabled": False,          # Deshabilita gestor de contraseñas (save password)
        "profile.password_manager_leak_detection": False    # Deshabilita detección de leaks (change password)
    })
    
    # Otros args para evitar pop-ups y notificaciones
    options.add_argument("--disable-features=OptimizationGuide")
    options.add_argument("--disable-features=PasswordManagerV1")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")  # Modo incognito ayuda a evitar almacenamiento de contraseñas
    options.add_argument("--guest")      # Modo guest para no guardar nada
    
    # Activa modo headless (sin ventana visible)
    options.add_argument("--headless")
    
    # Usa webdriver_manager para Chromedriver compatible
    service = Service(ChromeDriverManager().install())
    driver_instance = webdriver.Chrome(service=service, options=options)
    driver_instance.implicitly_wait(10)
    
    yield driver_instance
    
    # Captura screenshot si falló
    if request.session.testsfailed:
        take_screenshot(driver_instance, request.node.name)
    
    driver_instance.quit()

def take_screenshot(driver, test_name):
    if not os.path.exists(SCREENSHOT_DIR):
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y_%m_%d_%H-%M-%S")
    filename = f"{test_name}_{timestamp}.png"
    filepath = os.path.join(SCREENSHOT_DIR, filename)
    try:
        driver.save_screenshot(filepath)
        print(f"\n✅ Captura guardada en: {filepath}")
    except Exception as e:
        print(f"\n❌ Error al guardar la captura de pantalla: {e}")
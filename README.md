# Proyecto Final: Automation Testing

## Descripción
Proyecto final del curso de **Automation Testing** con pruebas automatizadas de **UI** y **API** aplicando las mejores prácticas actuales.

### Pruebas incluidas
- **UI Testing** con **Selenium WebDriver + Pytest**  
  Sitio objetivo: https://www.saucedemo.com  
  Cobertura: Login (éxito y fallo), inventario, carrito, checkout con validaciones y flujo completo de compra.

- **API Testing** con **requests + Pytest**  
  API objetivo: https://jsonplaceholder.typicode.com  
  Casos: GET posts, POST nuevo post y DELETE post.

Se implementa el patrón **Page Object Model (POM)** para mantener el código limpio, reutilizable y fácil de mantener.

## Características destacadas
- Ejecución en modo **headless** (sin ventana del navegador)
- Logs detallados en `logs/historial.log` (4 logs por prueba)
- Capturas de pantalla automáticas en caso de fallo → `test/screenshots/`
- Uso de `webdriver-manager` → no es necesario descargar chromedriver manualmente
- Pruebas parametrizadas (login con múltiples usuarios)
- Configuración centralizada en `conftest.py` y `pytest.ini`
- Manejo de pop-ups de contraseña de Chrome desactivado

## Estructura del proyecto
proyecto-final-automation-testing-Luis-Roggiano/
├── test/
│   ├── test_login.py                  # Pruebas de login parametrizadas
│   ├── test_inventario.py             # Verificación de inventario y logout
│   ├── test_carrito.py                # Agregar y remover productos del carrito
│   ├── test_checkout_pagina.py        # Checkout + validaciones de campos
│   ├── test_checkout_paginaCompleta.py# Flujo completo de compra
│   ├── test_regression_HTML.py        # Pruebas API JSONPlaceholder
│   └── conftest.py                    # Fixture de WebDriver + screenshots + logs
├── page/
│   ├── login.py
│   ├── inventario.py
│   ├── paginaCarrito.py
│   ├── checkout_pagina.py
│   └── checkout_paginaCompleta.py
├── data/
│   └── data_login.py                  # Casos de prueba para login
├── logs/
│   └── historial.log                  # Log automático de todas las ejecuciones
├── test/screenshots/                  # Capturas automáticas en fallos
├── pytest.ini                         # Configuración de logs en archivo
├── requirements.txt
└── README.md

## Requisitos
- Python 3.10 o superior
- Google Chrome instalado (cualquier versión reciente)

## Instalación y ejecución

'''
bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/proyecto-final-automation-testing-Luis-Roggiano.git
cd proyecto-final-automation-testing-Luis-Roggiano

# 2. (Recomendado) Crear entorno virtual
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar todas las pruebas
pytest -v

# Opcional: generar reporte HTML bonito
pytest -v --html=report.html --self-contained-html
'''
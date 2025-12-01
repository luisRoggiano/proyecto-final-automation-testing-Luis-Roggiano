# Proyecto Final: Automation Testing

## Descripción
Este es el proyecto final para el curso de Automation Testing. Incluye pruebas automatizadas para:
- **UI Testing**: Usando Selenium y Pytest para probar el sitio web de demostración SauceDemo (https://www.saucedemo.com/), cubriendo login, visualización de inventario, operaciones de carrito, checkout y validaciones.
- **API Testing**: Pruebas de regresión para la API JSONPlaceholder (https://jsonplaceholder.typicode.com/), incluyendo obtener, crear y eliminar posts.

El proyecto utiliza el patrón Page Object Model (POM) para las pruebas UI, y requests para las API. Las pruebas están parametrizadas donde aplica (e.g., casos de login).

## Estructura del Proyecto
- `test/`: Directorio con los archivos de pruebas.
  - `test_login.py`: Pruebas de login con usuarios válidos e inválidos.
  - `test_inventario.py`: Pruebas para la página de inventario.
  - `test_carrito.py`: Pruebas para agregar y remover items del carrito.
  - `test_checkout_pagina.py`: Pruebas para el proceso de checkout y validaciones.
  - `test_checkout_paginaCompleta.py`: Flujo completo de compra.
  - `test_regression_HTML.py`: Pruebas API para JSONPlaceholder (obtener, crear, eliminar posts).
- `conftest.py`: Fixtures compartidas (e.g., setup de Selenium WebDriver).
- `requirements.txt`: Dependencias del proyecto.
- (Opcional) `pages/`: Clases Page Object para elementos UI.

## Requisitos
- Python 3.10+
- Navegador compatible (e.g., Chrome) y su WebDriver (e.g., chromedriver) en el PATH.
- Dependencias: `pytest`, `selenium`, `requests`, etc.

## Instalación
1. Clona el repositorio:
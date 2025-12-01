from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Definición de la clase que representa la página del carrito (CartPage)
# Sigue el patrón Page Object Model (POM) para organizar y mantener mejor el código de prueba
class CartPage:
    # --- Localizadores (Selectors) ---
    # URL relativa de la página del carrito
    URL_CURRENT = '/cart.html'
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    CONTINUE_SHOPPING_BUTTON = (By.ID, 'continue-shopping')
    CART_ITEM = (By.CLASS_NAME, 'cart_item')
    REMOVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Remove')]")
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')

    # Constructor de la clase
    # Recibe una instancia del driver de Selenium para interactuar con el navegador
    def __init__(self, driver):
        self.driver = driver

    # --- Métodos de la Página ---

    # Verifica si el navegador está actualmente en la página del carrito
    def is_at_page(self):
        # Comprueba si la URL actual del driver contiene la URL relativa definida
        return self.URL_CURRENT in self.driver.current_url

    # Hace clic en el botón de "Checkout" (Pagar)
    def go_to_checkout(self):
        # Espera hasta 10 segundos para que el botón sea cliqueable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        # Luego hace clic en el elemento
        ).click()

    # Hace clic en el botón de "Continue Shopping" (Continuar Comprando)
    def continue_shopping(self):
        # Espera hasta 10 segundos para que el botón sea cliqueable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_SHOPPING_BUTTON)
        # Luego hace clic en el elemento
        ).click()

    # Obtiene la cantidad de artículos visibles en la lista del carrito
    def get_cart_items_count(self):
        # Encuentra todos los elementos que coincidan con el localizador CART_ITEM
        # El '*' desempaqueta la tupla (By.CLASS_NAME, 'cart_item')
        items = self.driver.find_elements(*self.CART_ITEM)
        # Devuelve la cantidad de elementos encontrados (artículos)
        return len(items)

    # Elimina un artículo del carrito haciendo clic en su botón "Remove"
    # item_index=0 por defecto, elimina el primer artículo si no se especifica un índice
    def remove_item(self, item_index=0):
        # Encuentra todos los botones de "Remove" en la página
        remove_buttons = self.driver.find_elements(*self.REMOVE_BUTTON)
        # Verifica si se encontraron botones y si el índice solicitado es válido
        if remove_buttons and item_index < len(remove_buttons):
            # Hace clic en el botón "Remove" en el índice especificado
            remove_buttons[item_index].click()

    # Obtiene el número de artículos indicado en la insignia (badge) del carrito
    def get_cart_badge_count(self):
        try:
            # Intenta encontrar el elemento de la insignia del carrito
            badge = self.driver.find_element(*self.CART_BADGE)
            # Devuelve el texto del elemento (que es el número), convertido a entero
            return int(badge.text)
        except:
            # Si el elemento no se encuentra (por ejemplo, el carrito está vacío y la insignia no existe),
            # devuelve 0
            return 0
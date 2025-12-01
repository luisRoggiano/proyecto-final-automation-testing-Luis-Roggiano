import requests
import pytest
import logging
from faker import Faker
import pathlib
from typing import Dict, Any, List

# --- Configuración Global ---
BASE_URL = "https://jsonplaceholder.typicode.com"
fake = Faker()
LOGS_DIR = pathlib.Path('logs')

# --- Función de Utilidad para Configurar el Logging ---
def setup_logging():
    """Configura el sistema de logging para escribir en un archivo."""
    LOGS_DIR.mkdir(exist_ok=True)
    logging.basicConfig(
        filename=LOGS_DIR / "historial_funcional.log",
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(name)s – %(message)s',
        datefmt='%H:%M:%S'
    )
    return logging.getLogger()

logger = setup_logging()

# --- Clase de Pruebas ---
class TestJSONPlaceholderAPI:
    """
    Clase de tests para la API. Usa setup_method para inicialización de la instancia,
    reemplazando el __init__ no soportado por Pytest.
    """
    
    # Este método de Pytest se ejecuta ANTES de cada método de prueba (test_*)
    # Reemplaza la funcionalidad de __init__ para configurar el estado de la instancia.
    def setup_method(self, method):
        """Inicializa la URL base como atributo de la instancia."""
        # Inicializa un atributo de instancia, tal como lo haría __init__
        self.base_url = BASE_URL
        # Inicializa un atributo para almacenar un dato para usar entre tests (ej. para un POST/GET secuencial)
        self.new_post_id = None 
        
    def _log_test_start(self, test_name: str):
        """Registra el inicio de un test en el log."""
        logger.info(f"\n==========================================")
        logger.info(f"=== INICIO: {test_name} ===")
        print(f"\n=== INICIO: {test_name} ===")
        
    def _log_test_end(self, test_name: str):
        """Registra el final de un test en el log y consola."""
        logger.info(f"=== FIN: {test_name} EXITOSO! ===")
        logger.info(f"==========================================")
        print(f"🎉 Test {test_name} completado exitosamente!")
        
    # TEST 1: GET - Obtener todos los posts
    def test_obtener_posts(self):
        """✅ GET /posts - Obtener lista de posts exitosamente."""
        test_name = "GET /posts - Obtener Posts"
        self._log_test_start(test_name)
        
        # Usamos self.base_url inicializado en setup_method
        response = requests.get(f"{self.base_url}/posts")
        
        # Validaciones de estado
        assert response.status_code == 200
        print("✅ Código de estado 200 - OK")
        
        # Validaciones de estructura
        data: List[Dict[str, Any]] = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        print("✅ Estructura JSON correcta")
        
        self._log_test_end(test_name)

    # TEST 2: POST - Crear un nuevo post
    def test_crear_post(self):
        """➕ POST /posts - Crear un nuevo post exitosamente."""
        test_name = "POST /posts - Crear Post"
        self._log_test_start(test_name)
        
        NUEVO_USER_ID = 99
        post_data = {
            "title": fake.sentence(nb_words=4),
            "body": fake.paragraph(nb_sentences=3),
            "userId": NUEVO_USER_ID
        }
        
        # Usamos self.base_url inicializado en setup_method
        response = requests.post(f"{self.base_url}/posts", json=post_data)
        
        # Validaciones de estado
        assert response.status_code == 201
        print("✅ Código de estado 201 - Created")
        
        # Validaciones de datos
        data: Dict[str, Any] = response.json()
        assert data["title"] == post_data["title"]
        assert data.get("id") == 101 # JSONPlaceholder siempre devuelve 101
        
        # Guardamos el ID si queremos usarlo en un test posterior (aunque Pytest ejecuta tests aislados)
        self.new_post_id = data.get("id") 
        print(f"✅ Nuevo Post Creado con ID: {self.new_post_id}")
        
        self._log_test_end(test_name)
    
    # TEST 3: DELETE - Eliminar un post
    def test_eliminar_post(self):
        """❌ DELETE /posts/{id} - Eliminar un post exitosamente."""
        test_name = "DELETE /posts/{id} - Eliminar Post"
        self._log_test_start(test_name)
        
        # Usamos un ID conocido
        post_id_to_delete = 50
        
        # Usamos self.base_url inicializado en setup_method
        response = requests.delete(f"{self.base_url}/posts/{post_id_to_delete}")
        
        # Validaciones
        assert response.status_code == 200
        assert response.json() == {}
        print(f"✅ Post con ID {post_id_to_delete} eliminado (status 200 OK).")
        
        self._log_test_end(test_name)
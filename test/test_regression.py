import requests
import pytest
import logging
from faker import Faker
import pathlib



# Configuración
BASE_URL = "https://jsonplaceholder.typicode.com"
fake= Faker()

path_dir = pathlib.Path('logs')
path_dir.mkdir(exist_ok=True)


logging.basicConfig(
    filename= path_dir/ "historial.log",
    level= logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s – %(message)s',
    datefmt='%H:%M:%S'
)

logger = logging.getLogger()

class TestJSONPlaceholder:
    """Tests para JSONPlaceholder API - Permite operaciones reales"""
    
    # TEST 1: GET - Obtener todos los posts (Éxito)
    def test_get_posts_success(self):
        """GET /posts - Obtener lista de posts exitosamente"""
        logger.info("\n=== Test 1: GET Posts ===")
        
        # Hacer petición GET
        response = requests.get(f"{BASE_URL}/posts")
        
        # Validar código de estado
        assert response.status_code == 200, f"Esperado 200, Obtenido {response.status_code}"
        print("✅ Código de estado 200 - OK")
        logger.info("✅ Código de estado 200 - OK")
        
        # Convertir a JSON
        data = response.json()
        
        # Validar estructura del JSON
        assert isinstance(data, list), "La respuesta debería ser una lista"
        assert len(data) > 0, "La lista no debería estar vacía"
        print("✅ Estructura JSON correcta")
        
        # Validar estructura del primer post
        first_post = data[0]
        required_fields = ["userId", "id", "title", "body"]
        for field in required_fields:
            assert field in first_post, f"Campo '{field}' no encontrado"
        print("✅ Estructura del post correcta")
        
        # Validar tipos de datos
        assert isinstance(first_post["id"], int)
        #assert isinstance(first_post["title"], str)
        #assert isinstance(first_post["body"], str)
        print("✅ Tipos de datos correctos")
        
        print("🎉 Test GET Posts completado exitosamente!")
    
    # TEST 2: POST - Crear un nuevo post (Éxito)
    def test_create_post_success(self):
        """POST /posts - Crear un nuevo post exitosamente"""
        print("\n=== Test 2: CREATE Post ===")
        
        # Datos para crear el post
        post_data = {
            "title": fake.word(),
            "body": fake.text(),
            "userId": fake.random_int(1,6)
        }
        
        # Hacer petición POST
        response = requests.post(f"{BASE_URL}/posts", json=post_data)
        
        # Validar código de estado
        assert response.status_code == 201, f"Esperado 201, obtenido {response.status_code}"
        print("✅ Código de estado 201 - Created")
        
        # Convertir a JSON
        data = response.json()
        
        # Validar estructura de respuesta
        expected_fields = ["id", "title", "body", "userId"]
        for field in expected_fields:
            assert field in data, f"Campo '{field}' no encontrado en respuesta"
        print("✅ Estructura de respuesta correcta")
        
        # Validar que los datos se guardaron correctamente
        assert data["title"] == post_data["title"]
        #assert data["body"] == post_data["body"]
        #assert data["userId"] == post_data["userId"]
        print("✅ Datos guardados correctamente")
        
        # Validar que se asignó un ID (simulado por JSONPlaceholder)
        assert data["id"] == 101, f"Expected ID 101, got {data['id']}"
        print("✅ ID asignado correctamente")
        
        print("🎉 Test CREATE Post completado exitosamente!")
    
    # TEST 3: DELETE - Eliminar un post (Éxito)
    def test_delete_post_success(self):
        """DELETE /posts/{id} - Eliminar un post exitosamente"""
        print("\n=== Test 3: DELETE Post ===")
        
        # ID del post a eliminar (usamos uno que sabemos que existe)
        post_id = 1
        
        # Hacer petición DELETE
        response = requests.delete(f"{BASE_URL}/posts/{post_id}")
        
        # Validar código de estado
        assert response.status_code == 200, f"Esperado 200, obtenido {response.status_code}"
        print("✅ Código de estado 200 - OK")
        
        # JSONPlaceholder devuelve un objeto vacío para DELETE exitoso
        data = response.json()
        assert data == {}, f"Esperado un diccionario vacio, obtenido {data}"
        print("✅ Respuesta DELETE correcta")
        
        print("🎉 Test DELETE Post completado exitosamente!")
    
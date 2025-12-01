import json
import os # Importar el módulo OS para trabajar con rutas de archivos
from pathlib import Path # Aunque no se usa directamente en esta función, es común para manejo de rutas

def get_login_json(json_file="data_login.json"):
    # Definición de la función para cargar datos de inicio de sesión desde un JSON
    # Toma como argumento el nombre del archivo JSON (por defecto 'data_login.json')

    # 1. Construcción de la ruta al archivo
    
    # Obtiene la ruta del directorio del archivo Python actual (ej. utils/)
    current_file = os.path.dirname(__file__) 
    
    # Construye la ruta relativa: sube un nivel (..) y entra a la carpeta 'data'
    # Ejemplo: /proyecto/utils/ -> /proyecto/data/data_login.json
    json_path_relative = os.path.join(current_file, "..", "data", json_file)
    
    # Convierte la ruta relativa a una ruta absoluta para asegurar que funcione
    # sin importar desde dónde se ejecute el script.
    json_file_path_absolute = os.path.abspath(json_path_relative)
    # Comentario original: #../data/data_login.json=> rel
    
    # Lista vacía donde se almacenarán los datos de prueba como tuplas
    casos = []

    try:
        # 2. Lectura y procesamiento del archivo
        
        # Abre el archivo en modo lectura ('r' implícito) usando la ruta absoluta
        with open(json_file_path_absolute) as j:
            # Carga el contenido del archivo JSON a una variable (generalmente una lista de diccionarios)
            datos = json.load(j)

            # Itera sobre cada diccionario (caso de prueba) en la lista 'datos'
            for i in datos:
                # Extrae los valores de las claves 'username', 'password' y 'login_example'
                username = i["username"]
                password = i["password"]
                login_example = i["login_example"]
                
                # Agrega los valores como una tupla a la lista 'casos'
                # Esto es ideal para usar con bibliotecas como pytest para la parametrización de pruebas
                casos.append((username, password, login_example))
    
    except FileNotFoundError:
        # Manejo de error si el archivo no se encuentra en la ruta especificada
        print(f"Error: El archivo JSON no se encontró en la ruta: {json_file_path_absolute}")
        # En un framework de pruebas real, podrías querer elevar una excepción o devolver una lista vacía.
    except json.JSONDecodeError:
        # Manejo de error si el archivo JSON está mal formado
        print(f"Error: El archivo {json_file} no es un JSON válido.")

    # Devuelve la lista de tuplas con los casos de prueba
    return casos
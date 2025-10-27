import requests
import json

# URL base de tu servicio Flask
BASE_URL = "http://127.0.0.1:5000/api/mesa"

# ----------------------------------------------------
# A. GET -> OBTENER TODAS las mesas
# ----------------------------------------------------
def get_all_mesas():
    print("\nIntentando obtener todas las mesas...")
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            data = response.json()
            print("\nMesas obtenidas con éxito:")
            print(json.dumps(data, indent=4))
        else:
            print(f"\nError al obtener mesas. Código de estado: {response.status_code}")
            print(f"Respuesta del servidor: {response.text}")
    except requests.exceptions.ConnectionError:
        print("\nError de conexión. Asegúrate de que el servicio Flask esté corriendo.")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")

# ----------------------------------------------------
# B. GET -> OBTENER una mesa por ID
# ----------------------------------------------------
def get_mesa_by_id(mesa_id):
    url = f"{BASE_URL}/{mesa_id}"
    print(f"\nIntentando obtener mesa con ID: {mesa_id}...")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"\nMesa (ID: {mesa_id}) encontrada:")
            print(json.dumps(data, indent=4))
        elif response.status_code == 404:
            print(f"\nMesa con ID {mesa_id} no encontrada.")
        else:
            print(f"\nError al obtener la mesa. Código de estado: {response.status_code}")
            print(f"Respuesta del servidor: {response.text}")
    except requests.exceptions.ConnectionError:
        print("\nError de conexión. Asegúrate de que el servicio Flask esté corriendo.")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")

# ----------------------------------------------------
# C. POST -> CREAR una nueva mesa
# ----------------------------------------------------
def create_mesa(capacidad):
    print(f"\nIntentando crear una mesa con capacidad {capacidad}...")
    payload = {"capacidad": capacidad}
    try:
        response = requests.post(BASE_URL, json=payload)
        if response.status_code == 201:
            print("\nMesa creada con éxito.")
        else:
            print(f"\nError al crear la mesa. Código de estado: {response.status_code}")
            print(f"Respuesta del servidor: {response.text}")
    except requests.exceptions.ConnectionError:
        print("\nError de conexión. Asegúrate de que el servicio Flask esté corriendo.")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")

# ----------------------------------------------------
# D. PUT -> ACTUALIZAR una mesa por ID
# ----------------------------------------------------
def update_mesa(mesa_id, capacidad):
    print(f"\nIntentando actualizar la mesa {mesa_id} con capacidad {capacidad}...")
    url = f"{BASE_URL}/{mesa_id}"
    payload = {"capacidad": capacidad}
    try:
        response = requests.put(url, json=payload)
        if response.status_code == 200:
            print("\nMesa actualizada con éxito.")
        else:
            print(f"\nError al actualizar la mesa. Código de estado: {response.status_code}")
            print(f"Respuesta del servidor: {response.text}")
    except requests.exceptions.ConnectionError:
        print("\nError de conexión. Asegúrate de que el servicio Flask esté corriendo.")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")

# ----------------------------------------------------
# E. DELETE -> ELIMINAR una mesa por ID
# ----------------------------------------------------
def delete_mesa(mesa_id):
    print(f"\nIntentando eliminar la mesa con ID: {mesa_id}...")
    url = f"{BASE_URL}/{mesa_id}"
    try:
        response = requests.delete(url)
        if response.status_code == 200:
            print("\nMesa eliminada con éxito.")
        else:
            print(f"\nError al eliminar la mesa. Código de estado: {response.status_code}")
            print(f"Respuesta del servidor: {response.text}")
    except requests.exceptions.ConnectionError:
        print("\nError de conexión. Asegúrate de que el servicio Flask esté corriendo.")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")

# ----------------------------------------------------
# EJECUCIÓN AUTOMÁTICA
# ----------------------------------------------------
if __name__ == '__main__':
    # 1. Crear mesas de ejemplo
    create_mesa(4)
    create_mesa(6)

    # 2. Obtener todas las mesas
    get_all_mesas()

    # 3. Obtener mesa específica
    get_mesa_by_id(24)

    # 4. Actualizar mesa
    update_mesa(25, 20)

    # 5. Eliminar mesa
    delete_mesa(24)

    # 6. Verificar estado final
    get_all_mesas()

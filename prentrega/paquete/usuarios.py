from .manejo_de_datos import guardar_datos

def ingresar_datos(RUTA_BASE_DATOS, base_datos: list):
    usuarios = {}
    usuarios["nombre"] = input("Nombre: ")
    usuarios["password"] = input("Contraseña: ")
    base_datos.append(usuarios)
    guardar_datos(RUTA_BASE_DATOS, base_datos)
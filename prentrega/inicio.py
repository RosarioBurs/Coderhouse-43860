import json
import pathlib


BASE_DIR = pathlib.Path(__file__).resolve().parent
RUTA_BASE_DATOS = BASE_DIR / "base_de_datos.json"
base_datos = []


def ingresar_datos():
    usuarios = {}
    usuarios["nombre"] = input("Nombre: ")
    usuarios["password"] = input("Contraseña: ")
    base_datos.append(usuarios)
    guardar_datos()

def guardar_datos():
    with open(RUTA_BASE_DATOS, "w") as archivo:
        json.dump(base_datos, archivo, indent=4)

def cargar_datos():
    with open(RUTA_BASE_DATOS, "r") as archivo:
        global base_datos
        base_datos = json.load(archivo)

def mostrar_datos():
    print(base_datos)

def main():
    cargar_datos()
    ingresar_datos()
    mostrar_datos()
    
main()
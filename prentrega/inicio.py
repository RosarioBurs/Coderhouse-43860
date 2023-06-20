import pathlib
from paquete.manejo_de_datos import cargar_datos, mostrar_datos
from paquete.usuarios import ingresar_datos

BASE_DIR = pathlib.Path(__file__).resolve().parent
RUTA_BASE_DATOS = BASE_DIR / "base_de_datos.json"

def main():
    base_datos: list = cargar_datos(RUTA_BASE_DATOS)
    ingresar_datos(RUTA_BASE_DATOS, base_datos)
    mostrar_datos(base_datos)
   
main()
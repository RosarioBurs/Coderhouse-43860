import json

def ingresar_datos() -> dict:
    usuarios = {}
    usuarios["nombre"] = input("Nombre: ")
    usuarios["password"] = input("Contraseña: ")
    return usuarios

def guardar_datos():
    ...

def cargar_datos():
    ...

def mostrar_datos():
    ...

def main():
    diccionario_de_datos = ingresar_datos()
    print(diccionario_de_datos)
    
main()
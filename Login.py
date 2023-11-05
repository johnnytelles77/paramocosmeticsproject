import os
import json

CARPETA_BASE_DATOS = 'usuarios'
ARCHIVO_BASE_DATOS = 'usuarios.json'

def cargar_base_datos():
    try:
        with open(os.path.join(CARPETA_BASE_DATOS, ARCHIVO_BASE_DATOS), 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

def crear_carpeta():
    if not os.path.exists(CARPETA_BASE_DATOS):
        os.makedirs(CARPETA_BASE_DATOS)

def guardar_base_datos(base_datos):
    crear_carpeta()
    with open(os.path.join(CARPETA_BASE_DATOS, ARCHIVO_BASE_DATOS), 'w') as archivo:
        json.dump(base_datos, archivo, indent=2)

def registrar_usuario(base_datos):
    nombre_usuario = input("Ingrese nombre de usuario: ")

    if nombre_usuario in base_datos:
        print("El usuario ya existe. Por favor, elija otro nombre de usuario.")
    else:
        contrasena = input("Ingrese contraseña: ")
        base_datos[nombre_usuario] = contrasena
        print(f"Usuario '{nombre_usuario}' registrado exitosamente.")

def mostrar_usuarios(base_datos):
    print("\nUsuarios registrados:")
    for usuario, contrasena in base_datos.items():
        print(f"Usuario: {usuario}, Contraseña: {contrasena}")

def login(base_datos):
    intentos_restantes = 3
    login_incompleto = True
    while login_incompleto:
        if intentos_restantes == 0:
            print("No tiene más intentos disponibles.")
            break
        usuario = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
        if base_datos.get(usuario) == password:
            login_incompleto = False
            print(f"¡Bienvenido, {usuario}!")
        else:
            intentos_restantes -= 1
            print(f"Usuario o contraseña incorrectos. Intentos restantes: {intentos_restantes}")

def main():
    base_de_datos = cargar_base_datos()

    while True:
        print("\n1. Registrar nuevo usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Iniciar sesión")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario(base_de_datos)
        elif opcion == '2':
            mostrar_usuarios(base_de_datos)
        elif opcion == '3':
            login(base_de_datos)
        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            guardar_base_datos(base_de_datos)
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

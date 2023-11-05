import json

ARCHIVO_BASE_DATOS = 'usuarios.json'

def cargar_base_datos():
    try:
        with open(ARCHIVO_BASE_DATOS, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

def guardar_base_datos(base_datos):
    with open(ARCHIVO_BASE_DATOS, 'w') as archivo:
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

def main():
    base_de_datos = cargar_base_datos()

    while True:
        print("\n1. Registrar nuevo usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario(base_de_datos)
        elif opcion == '2':
            mostrar_usuarios(base_de_datos)
        elif opcion == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            guardar_base_datos(base_de_datos)
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main() 
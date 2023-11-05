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

def guardar_informacion(base_datos):
    usuario = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    base_datos[usuario] = password
    print(f"Usuario '{usuario}' registrado exitosamente.")

def leer_informacion(base_datos):
    usuario = input("Ingrese su nombre de usuario: ")
    password = base_datos.get(usuario)
    return password

def login(base_datos):
    intentos_restantes = 3
    login_incompleto = True
    while login_incompleto:
        if intentos_restantes == 0:
            print("Ha excedido el número de intentos permitidos. Acceso denegado.")
            break
        usuario = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        if base_datos.get(usuario) == password:
            login_incompleto = False
            print(f"Bienvenido, {usuario}!")
        else:
            intentos_restantes -= 1
            print(f"Nombre de usuario o contraseña incorrectos. Intentos restantes: {intentos_restantes}")

def main():
    base_de_datos = cargar_base_datos()

    while True:
        print("\n1. Registrar nuevo usuario")
        print("2. Login")
        print("3. Mostrar usuarios registrados")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            guardar_informacion(base_de_datos)
        elif opcion == '2':
            login(base_de_datos)
        elif opcion == '3':
            print("\nUsuarios registrados:")
            for usuario, contrasena in base_de_datos.items():
                print(f"Usuario: {usuario}, Contraseña: {contrasena}")
        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            guardar_base_datos(base_de_datos)
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

import json

localStorage = "users.json"

try:
    with open(localStorage) as f:
        users = json.load(f)
except FileNotFoundError:
    users = {}

def registerUser(username, password):
    if username not in users:
        users[username] = password
        with open(localStorage, "w") as f:
            json.dump(users, f)
        print("Usuario registrado con éxito")
    else:
        print("El nombre de usuario ya está en uso")

def validateUser(username, password):
    if username in users and password == users[username]:
        print("Bienvenido,", username)
    else:
        print("Nombre de usuario o contraseña incorrectos")

while True:
    opcion = input("Elige una opción (1 - Registrarse, 2 - Iniciar sesión): ")
    if opcion == "1":
        username = input("Ingresa tu nombre de usuario: ")
        password = input("Ingresa tu contraseña: ")
        registerUser(username, password)
        break
    elif opcion == "2":
        username = input("Ingresa tu nombre de usuario: ")
        password = input("Ingresa tu contraseña: ")
        validateUser(username, password)
        break
    else:
        print("Opción inválida, intenta de nuevo")
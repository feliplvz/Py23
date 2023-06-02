
users = {'user1': 'pass1', 'user2': 'pass2', 'user3': 'pass3', 'user4': 'pass4', 'user5': 'pass5'}

username = input("Ingresa tu nombre de usuario: ")
password = input("Ingresa tu contraseña: ")

if username in users and password == users[username]:
    print("Bienvenido,", username)
else:
    print("Nombre de usuario o contraseña incorrectos")

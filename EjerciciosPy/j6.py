
num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))
num3 = int(input("Ingresa el tercer número entero: "))

contador = 0

if num1 < 0:
    contador += 1
if num2 < 0:
    contador += 1
if num3 < 0:
    contador += 1

print("Hay", contador, "números menores a 0.")

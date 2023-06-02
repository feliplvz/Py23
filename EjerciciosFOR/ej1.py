numeros = []
mayor_cero = 0
menor_cero = 0
igual_cero = 0

for i in range(5):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)
    if numero > 0:
        mayor_cero += 1
    elif numero < 0:
        menor_cero += 1
    else:
        igual_cero += 1

print("Cantidad de números mayores a cero: ", mayor_cero)
print("Cantidad de números menores a cero: ", menor_cero)
print("Cantidad de números iguales a cero: ", igual_cero)
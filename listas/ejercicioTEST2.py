import random


filas = 3
columnas = 3
rango_min = 0
rango_max = 100
arreglo = [[random.randint(rango_min, rango_max) for _ in range(columnas)] for _ in range(filas)]

elementos = [elemento for fila in arreglo for elemento in fila]
suma_total = sum(elementos)
promedio = suma_total / len(elementos)


suma_total = sum(elementos)

elemento_mayor = max(elementos)


elemento_menor = min(elementos)

diagonal_principal = [arreglo[i][i] for i in range(min(len(arreglo), len(arreglo[0])))]

print("Arreglo bidimensional:")
for fila in arreglo:
    print(fila)
print()
print("Promedio de los elementos:", promedio)
print("Suma de los elementos:", suma_total)
print("Elemento mayor:", elemento_mayor)
print("Elemento menor:", elemento_menor)
print("Elementos de la diagonal principal:", diagonal_principal)

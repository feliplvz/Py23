import random

arreglo_bi = [[random.randint(0, 100) for _ in range(3)] for _ in range(3)]

copia_arreglo_2d = [fila.copy() for fila in arreglo_bi]

elemento_mayor = max(elemento for fila in arreglo_bi for elemento in fila)
elemento_menor = min(elemento for fila in arreglo_bi for elemento in fila)

suma_elementos = sum(elemento for fila in arreglo_bi for elemento in fila)

total_elementos = sum(1 for fila in arreglo_bi for _ in fila)
promedio_elementos = suma_elementos / total_elementos

print("Arreglo bidimensional:")
for fila in arreglo_bi:
    print(fila)
print()
print("Copia del arreglo bidimensional:")
for fila in copia_arreglo_2d:
    print(fila)
print()
print("Elemento mayor:", elemento_mayor)
print("Elemento menor:", elemento_menor)
print("Suma de los elementos:", suma_elementos)
print("Promedio de los elementos:", promedio_elementos)
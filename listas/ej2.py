import random

arreglo_3d = [[[random.randint(0, 100) for _ in range(3)] for _ in range(3)] for _ in range(3)]

copia_arreglo_3d = [[[elemento for elemento in fila] for fila in matriz] for matriz in arreglo_3d]

elemento_mayor = max(elemento for matriz in arreglo_3d for fila in matriz for elemento in fila)
elemento_menor = min(elemento for matriz in arreglo_3d for fila in matriz for elemento in fila)

suma_elementos = sum(elemento for matriz in arreglo_3d for fila in matriz for elemento in fila)

total_elementos = sum(1 for matriz in arreglo_3d for fila in matriz for _ in fila)
promedio_elementos = suma_elementos / total_elementos

print("Arreglo tridimensional:")
for matriz in arreglo_3d:
    for fila in matriz:
        print(fila)
    print()
print("Copia del arreglo tridimensional:")
for matriz in copia_arreglo_3d:
    for fila in matriz:
        print(fila)
    print()
print("Elemento mayor:", elemento_mayor)
print("Elemento menor:", elemento_menor)
print("Suma de los elementos:", suma_elementos)
print("Promedio de los elementos:", promedio_elementos)
print("Suma de los elementos")
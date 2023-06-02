import random

arreglo_2d = [[random.randint(0, 100) for _ in range(3)] for _ in range(3)]

copia_arreglo_2d = [fila.copy() for fila in arreglo_2d]

elemento_mayor = max(max(fila) for fila in arreglo_2d)
elemento_menor = min(min(fila) for fila in arreglo_2d)

suma_elementos = sum(sum(fila) for fila in arreglo_2d)

total_elementos = sum(len(fila) for fila in arreglo_2d)
promedio_elementos = suma_elementos / total_elementos

print("Arreglo bidimensional:")
for fila in arreglo_2d:
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
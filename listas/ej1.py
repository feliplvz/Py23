import random


arreglo = [random.randint(0, 100) for _ in range(10)]


copia_arreglo = arreglo.copy()


elemento_mayor = max(arreglo)
elemento_menor = min(arreglo)


suma_elementos = sum(arreglo)


promedio_elementos = suma_elementos / len(arreglo)


print("Arreglo original:", arreglo)
print("Copia del arreglo:", copia_arreglo)
print("Elemento mayor:", elemento_mayor)
print("Elemento menor:", elemento_menor)
print("Suma de los elementos:", suma_elementos)
print("Promedio de los elementos:", promedio_elementos)
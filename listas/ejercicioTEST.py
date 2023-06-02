import random

def crear_arreglo_bimensional(filas, columnas, rango_min, rango_max):
    arreglo = [[random.randint(rango_min, rango_max) for _ in range(columnas)] for _ in range(filas)]
    return arreglo

def calcular_promedio(arreglo):
    elementos = [elemento for fila in arreglo for elemento in fila]
    suma_total = sum(elementos)
    promedio = suma_total / len(elementos)
    return promedio

def calcular_suma(arreglo):
    elementos = [elemento for fila in arreglo for elemento in fila]
    suma_total = sum(elementos)
    return suma_total

def encontrar_mayor(arreglo):
    elementos = [elemento for fila in arreglo for elemento in fila]
    elemento_mayor = max(elementos)
    return elemento_mayor

def encontrar_menor(arreglo):
    elementos = [elemento for fila in arreglo for elemento in fila]
    elemento_menor = min(elementos)
    return elemento_menor

def obtener_diagonal(arreglo):
    diagonal_principal = [arreglo[i][i] for i in range(min(len(arreglo), len(arreglo[0])))]
    return diagonal_principal

filas = 3
columnas = 3
rango_min = 0
rango_max = 100

arreglo = crear_arreglo_bimensional(filas, columnas, rango_min, rango_max)

promedio = calcular_promedio(arreglo)
suma_total = calcular_suma(arreglo)
elemento_mayor = encontrar_mayor(arreglo)
elemento_menor = encontrar_menor(arreglo)
diagonal_principal = obtener_diagonal(arreglo)

print("Arreglo bidimensional: ")
for fila in arreglo:
    print(fila)
print()
print("Promedio de los elementos: ", promedio)
print("Suma de los elementos: ", suma_total)
print("Elemento mayor: ", elemento_mayor)
print("Elemento menor: ", elemento_menor)
print("Elementos de la diagonal principal: ", diagonal_principal)
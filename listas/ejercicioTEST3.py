import random

filas = 3
columnas = 3
rango_min = 0 
rango_max = 100

arreglo = [[random.randint(rango_min, rango_max) for _ in range(columnas)] for _ in range(filas)]

elementos = [elemento for fila in arreglo for elemento in fila]
suma_total = sum(elementos)
promedio = suma_
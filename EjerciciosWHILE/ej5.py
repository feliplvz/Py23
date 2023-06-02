mayor_cero = 0
suma_pares = 0
i = 0
while i < 5:
    num = int(input("Ingrese un número entero: "))
    if num > 0:
        mayor_cero += 1
    if num % 2 == 0:
        suma_pares += num
    i += 1
print("Cantidad de números mayores a cero:", mayor_cero)
print("Suma de los números pares:", suma_pares)
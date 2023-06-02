suma = 0
i = 0
while i < 5:
    num = int(input(f"Ingrese un número entero positivo: {i} "))
    if num > 0:
        suma += num
        i += 1
print("La suma de los números ingresados es:", suma)

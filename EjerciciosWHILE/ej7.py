num = int(input("Ingrese un número entero mayor a cero: "))
if num > 1:
    i = 1
    suma = 0
    while i < num:
        if num % i == 0:
            suma += i
        i += 1
    if suma == num:
        print(num, "es un número perfecto.")
    else:
        print(num, "no es un número perfecto")
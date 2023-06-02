num = int(input("Ingrese un número mayor a cero: "))
if num > 1:
    i = 2
    while i < num:
        if num % i == 0:
            print(num, "no es primo.")
            break
        i += 1
    else:
        print(num, "es primo.")
else:
    print("El número ingresado debe ser mayor a uno.")
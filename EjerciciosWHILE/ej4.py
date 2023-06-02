num = int(input("Ingrese un número entero positivo entre 103 y 987: "))
if num >= 103 and num <= 987:
    inv = 0
    temp = num
    while temp > 0:
        dig = temp % 10
        inv = inv * 10 + dig
        temp //= 10
    suma = num + inv
    resta = num - inv
    mult = num * inv
    div = num / inv
    print("Número invertido:", inv)
    print("Suma:", suma)
    print("Resta:", resta)
    print("Multiplicación:", mult)
    print("División:", div)
else:
    print("El número ingresado no está dentro del rango permitido.")
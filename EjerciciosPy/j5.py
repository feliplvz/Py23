
num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))
num3 = int(input("Ingresa el tercer número entero: "))


if num1 > 0 and num2 > 0 and num3 > 0 and num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0:
    
    suma = num1 + num2 + num3
    print("La suma de los tres números es:", suma)
else:
    
    print()

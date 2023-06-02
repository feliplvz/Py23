num = int(input("Ingrese un número entero: "))
fact = 1
i = 1
print("------------------------------------------")
print("LOS FACTORIALES DE TU NUMERO SON")
while i <= num:
    fact *= i
    i += 1
print("El factorial de", num, "es:", fact)

print("------------------------------------------")
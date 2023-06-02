num = int(input("Ingrese un numero: "))
fact = 1
print("------------------------------------------")
print("LOS FACTORIALES DE TU NUMERO SON")
while num > 0:
    fact *= num
    num -= 1
    print("El factorial es ", fact)
    
print("------------------------------------------")
print("El factorial total de tu numero es: ", fact)
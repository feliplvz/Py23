cantidad_zapatos = int(input("Ingrese la cantidad de zapatos: "))


total = cantidad_zapatos * 20000
if total < 40000:
    total += 3000


print("El total a pagar es:", total)

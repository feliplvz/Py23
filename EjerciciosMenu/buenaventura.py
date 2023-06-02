
precio_menores = 2500
precio_adultos = 5000
precio_adulto_mayor = 1000
contador_menores = 0
contador_adultos = 0
contador_adulto_mayor = 0
total = 0
opcion = 0

while opcion != 5:
    print("\nBIENVENIDO AL CLUB DE DEPORTES BUENA VENTURA\n")
    print("¿Qué tipo de entrada desea comprar?\n")
    print("1. Menores - (Entre 5 a 12 años) $2500")
    print("2. Adultos - (Entre 13 a 64 años) $5000")
    print("3. Tercera Edad - (Desde 65 años) $1000")
    print("4. Cancelar pedido")
    print("5. Terminar pedido\n")
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        cantidad_menores = int(input("Ingrese la cantidad de entradas de menores que desea comprar: "))
        contador_menores += cantidad_menores
        viernes = input("¿Es viernes? (S/N)")
        if viernes == 's':
            precio_menores *= 0.9
        total += precio_menores * cantidad_menores

    if opcion == 2:
        cantidad_adultos = int(input("Ingrese la cantidad de entradas de adultos que desea comprar: "))
        contador_adultos += cantidad_adultos
        if input("¿Es viernes? (S/N)").upper() == 'S':
            precio_adultos *= 0.95
        total += precio_adultos * cantidad_adultos

    if opcion == 3:
        cantidad_adulto_mayor = int(input("Ingrese la cantidad de entradas de adultos mayores que desea comprar: "))
        contador_adulto_mayor += cantidad_adulto_mayor
        total += precio_adulto_mayor * cantidad_adulto_mayor

    if opcion == 4:
        contador_menores = 0
        contador_adultos = 0
        contador_adulto_mayor = 0
        total = 0

    if opcion == 5:
        print("Gracias por su compra, hasta pronto!")
        print("Resumen de su compra:\n")
        if contador_menores > 0:
            print(f"{contador_menores} Entradas para Menores")
        if contador_adultos > 0:
            print(f"{contador_adultos} Entradas para Adulto")
        if contador_adulto_mayor > 0:
            print(f"{contador_adulto_mayor} Entradas para Adulto Mayor")
        print("Total de la compra: $", total)

    else:
        print("Opción inválida. Por favor ingrese una opción válida.")
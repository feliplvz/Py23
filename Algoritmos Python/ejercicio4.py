clp_usd = 0.0013
ars_usd = 0.0046
mxn_usd = 0.055
pen_usd = 0.26
jpy_usd = 0.0075

opc = int(input("Ingrese la opción requerida para convertir dinero.\n1 - Chileno\n2 - Argentino\n3 - Mexicano\n4 - Peruano\n5 - Yen\n6 - Salir\n"))

if (opc == 1):
    print("-- Ha seleccionado pesos chilenos (CLP) --")
    ing = int(input("Ingrese la cantidad de dinero para convertir a dólares.\n"))
    total = int(clp_usd*ing)
    print("Usted puede comprar",total,"dólares")

elif (opc == 2):
    print("-- Ha seleccionado pesos argentinos (ARS) --")
    ing = int(input("Ingrese la cantidad de dinero para convertir a dólares.\n"))
    total = int(ars_usd*ing)
    print("Usted puede comprar",total,"dólares")

elif (opc == 3):
    print("-- Ha seleccionado pesos mexicanos (MXN) --")
    ing = int(input("Ingrese la cantidad de dinero para convertir a dólares.\n"))
    total = int(mxn_usd*ing)
    print("Usted puede comprar",total,"dólares")

elif (opc == 4):
    print("-- Ha seleccionado soles peruanos (PEN) --")
    ing = int(input("Ingrese la cantidad de dinero para convertir a dólares.\n"))
    total = int(pen_usd*ing)
    print("Usted puede comprar",total,"dólares")

elif (opc == 5):
    print("-- Ha seleccionado soles peruanos (YEN) --")
    ing = int(input("Ingrese la cantidad de dinero para convertir a dólares.\n"))
    total = int(jpy_usd*ing)
    print("Usted puede comprar",total,"dólares")
else:
    print("Adios")
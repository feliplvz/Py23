def calcular_iva():
    monto = float(input("Ingrese el monto de dinero: "))
    iva = monto * 0.19
    opcion = input("Desea mostrar el valor con el IVA agregado? (s/n): ")
    if opcion.lower() == "s":
        total = monto + iva
        print("El monto con IVA es:", total)
    else:
        print("El IVA es:", iva)

def calcular_descuento():
    monto = float(input("Ingrese el monto de dinero: "))
    porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
    descuento = monto * (porcentaje_descuento / 100)
    total = monto - descuento
    print("El monto con descuento es:", total)

def descuento2():
    monto = float(input("Ingrese el monto de dinero: "))
    porcentaje_descuento = float(input("Ingrese el porcentaje de descuento que desea aplicar"))
    

def calcular_imc():
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = peso / (altura ** 2)
    print("Su IMC es:", imc)
    if imc < 18.5:
        print("Estado: Bajo peso")
    elif imc >= 18.5 and imc <= 24.9:
        print("Estado: Adecuado")
    elif imc >= 25.0 and imc <= 29.9:
        print("Estado: Sobrepeso")
    elif imc >= 30.0 and imc <= 34.9:
        print("Estado: Obesidad grado 1")
    elif imc >= 35.0 and imc <= 39.9:
        print("Estado: Obesidad grado 2")
    else:
        print("Estado: Obesidad grado 3")

def menu():
    while True:
        print("\n-- MENÚ --")
        print("1. Calcular IVA")
        print("2. Calcular descuentos")
        print("3. Calcular IMC")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            calcular_iva()
        elif opcion == "2":
            calcular_descuento()
        elif opcion == "3":
            calcular_imc()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()

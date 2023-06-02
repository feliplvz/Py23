opcion = 0

while(opcion != 5):
    print('============================================================')
    print('Bienvenido! Qué opción desea?')
    opcion = int(input('1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir\n'))
    
    if(opcion == 1):
        print('============================================================')
        n1 = int(input('Ha seleccionado la opción suma, ingrese un número: '))
        n2 = int(input('Ahora, ingrese otro número: '))
        suma = n1 + n2
        print('El total de la suma de los números ingresados es',suma)
    elif(opcion == 2):
        print('============================================================')
        n1 = int(input('Ha seleccionado la opción resta, ingrese un número: '))
        n2 = int(input('Ahora, ingrese otro número: '))
        resta = n1 - n2
        print('El total de la resta de los números ingresados es',resta)
    elif(opcion == 3):
        print('============================================================')
        n1 = int(input('Ha seleccionado la opción multiplicación, ingrese un número: '))
        n2 = int(input('Ahora, ingrese otro número: '))
        mult = n1 * n2
        print('El total de la multiplicación de los números ingresados es de',mult)
    elif(opcion == 4):
        print('============================================================')
        n1 = int(input('Ha seleccionado la opción división, ingrese un número: '))
        n2 = int(input('Ahora, ingrese otro número: '))
        div = n1 / n2
        print('El total de la división de los números ingresados es de',div)
    elif(opcion == 5):
        print('============================================================')
        print('Adios!')
        print('============================================================')
    else:
        print('============================================================')
        print('Por favor, ingrese una opción válida.')
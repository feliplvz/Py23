def menu():
    while True:
        try:
            print("¿Qué deseas hacer?")
            print("1. Verificar si un número es par o impar")
            print("2. Mostrar la serie Fibonacci de los primeros 10 números")
            print("3. Salir")
            opcion = int(input("Ingrese una opción: "))
            
            if opcion == 1:
                numero = int(input("Ingrese un número: "))
                if numero % 2 == 0:
                    print("El número es par")
                else:
                    print("El número es impar")
                    
            elif opcion == 2:
                a, b = 0, 1
                print("Serie Fibonacci de los primeros 10 números:")
                for i in range(10):
                    print(a, end=" ")
                    a, b = b, a + b
                print()
                
            elif opcion == 3:
                print("¡Hasta luego!")
                break
                
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")
                
        except ValueError:
            print("Error: Ingrese un valor numérico.")

menu
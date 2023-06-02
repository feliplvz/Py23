numero = int(input("Ingrese un número entero mayor a cero: "))
es_primo = True

if numero <= 1:
    es_primo = False
else:
    for i in range(2, int(numero/2)+1):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print(numero, " es primo.")
else:
    print(numero, " no es primo.")
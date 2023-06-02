i = 0
numero_mayor = 0
numero_menor = 0

while(i < 2):
    i += 1
    ing = int(input('Ingrese un número: '))
    if(ing > numero_mayor):
        numero_mayor = ing
    elif(ing < numero_menor):
        numero_menor = ing

print()
print('El número mayor es',numero_mayor)
print('El número menor es',numero_menor)
letras = input("Ingrese 10 letras: ")
vocales = 0
consonantes = 0

for letra in letras:
    if letra in 'aeiouAEIOU':
        vocales += 1
    else:
        consonantes += 1

print("Cantidad de vocales: ", vocales)
print("Cantidad de consonantes: ", consonantes)
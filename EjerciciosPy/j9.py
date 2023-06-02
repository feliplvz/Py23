
precios = {
    "Churrasco": 1500,
    "Completo": 1000,
    "Vegetariano": 2000,
    "Barros Luco": 3000
}

print("Menú:")
print("Churrasco - 1500")
print("Completo - 1000")
print("Vegetariano - 2000")
print("Barros Luco - 3000")

seleccion = input("Ingrese los ítems que desea comprar separados por comas: ")

seleccion = list(seleccion)

total = 0

i = 0
while i < len(seleccion):
    item = seleccion[i]
    if item == ',':
        i += 1
        continue
    j = i
    while j < len(seleccion) and seleccion[j] != ',':
        j += 1
    item = ''.join(seleccion[i:j])
    i = j
    if item in precios:
        total += precios[item]

descuento = input("Ingrese su código de descuento (si tiene): ")
if descuento == "desc":
    total *= 0.9

print("El total a pagar es:", total)

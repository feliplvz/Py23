
precios = {
    "Churrasco": 1500,
    "Completo": 1000,
    "Vegetariano": 2000,
    "Barros Luco": 3000
}


print("Menú:")
print("Churrasco -", precios["Churrasco"])
print("Completo -", precios["Completo"])
print("Vegetariano -", precios["Vegetariano"])
print("Barros Luco -", precios["Barros Luco"])

seleccion = input("Ingrese el ítem que desea comprar: ")

total = precios[seleccion]

descuento = input("Ingrese su código de descuento (si tiene): ")
if descuento == "desc":
    total *= 0.9

print("El total a pagar es:", total)


precios = {
    "Baguette": 2500,
    "Marraqueta": 1500,
    "Hallulla": 1000,
    "Pan Integral": 2000
}

carrito = {}

print("Tipos de pan:")
print("Churrasco - 1500")
print("Marraqueta - 1000")
print("Hallulla - 2000")
print("Pan Integral - 3000")
print("Ingrese 'terminar' para finalizar la compra")
while True:
    seleccion = input("Ingrese el tipo de pan que desea comprar, para finalizar su compra ingrese TERMINAR :")
    if seleccion == "terminar" or "TERMINAR":
        break
    if seleccion in precios:
        cantidad = int(input("Ingrese la cantidad que desea comprar: "))
        carrito[seleccion] = carrito.get(seleccion, 0) + cantidad

total = sum(cantidad * precios[pan] for pan, cantidad in carrito.items())

descuento = input("Ingrese su código de descuento (si tiene): ")
if descuento == "desc":
    total *= 0.9

print("El total a pagar es:", total)

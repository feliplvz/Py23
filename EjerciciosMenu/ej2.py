def menupan():
    precios = {"amasado": 1500, "molde": 1000, "baguette": 2000, "integral": 3000}
    total = 0
    cantidad_panes = {}

    while True:
        try:
            print("\nBIENVENIDO A LA PANADERÍA FELIPITO")
            print("¿Qué tipo de pan desea comprar?")
            print("1. Amasado - $1500")
            print("2. Molde - $1000")
            print("3. Baguette - $2000")
            print("4. Integral - $3000")
            print("5. Terminar pedido")
            
            opcion = int(input("Ingrese una opción: "))

            if opcion == 1:
                cantidad = int(input("¿Cuántos panes amasados desea comprar?: "))
                cantidad_panes["amasado"] = cantidad_panes.get("amasado", 0) + cantidad
                total += precios["amasado"] * cantidad
                
            elif opcion == 2:
                cantidad = int(input("¿Cuántos panes de molde desea comprar?: "))
                cantidad_panes["molde"] = cantidad_panes.get("molde", 0) + cantidad
                total += precios["molde"] * cantidad
                
            elif opcion == 3:
                cantidad = int(input("¿Cuántas baguettes desea comprar?: "))
                cantidad_panes["baguette"] = cantidad_panes.get("baguette", 0) + cantidad
                total += precios["baguette"] * cantidad
                
            elif opcion == 4:
                cantidad = int(input("¿Cuántos panes integrales desea comprar?: "))
                cantidad_panes["integral"] = cantidad_panes.get("integral", 0) + cantidad
                total += precios["integral"] * cantidad
                
            elif opcion == 5:
                print("Gracias por su compra. ¡Hasta pronto!")
                break
                
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")

        except ValueError:
            print("Error: Ingrese un valor numérico.")

    envio_gratis = False
    if total > 5000:
        envio_gratis = True
    
    precio_envio = 0
    if not envio_gratis:
        precio_envio = total * 0.1
        total += precio_envio

    print("\nResumen de su compra:")
    for pan, cantidad in cantidad_panes.items():
        if cantidad > 0:
            print(f"{cantidad} panes {pan}")
    print(f"\nTotal a pagar: ${total}")
    if envio_gratis:
        print("Envío gratuito")
    else:
        print(f"Precio del envío: ${precio_envio}")
    print("¡Muchas gracias por su compra, vuelva pronto a Panadería Felipito!")

menupan()
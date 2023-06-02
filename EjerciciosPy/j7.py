
a = float(input("Ingresa la longitud del lado a: "))
b = float(input("Ingresa la longitud del lado b: "))
c = float(input("Ingresa la longitud del lado c: "))


if a == b and b == c:
    print("El triángulo es equilátero")

elif a == b or b == c or a == c:
    print("El triángulo es isósceles")
elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("El triángulo es rectángulo")
else:
    print("Es un triangulo cualquiera")

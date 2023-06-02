total = 0
cant_mayor = 0
nombre_mayor = ''
recaudado = 0
bucle = True
while(bucle == True):
    nombre = ''
    tipo_terapia = ''
    total += 1
    while(len(nombre) <= 0):
        nombre = input('Ingrese el nombre del cliente.\n')
        nombre.capitalize()
        if(len(nombre) <= 0):
            print('Ingrese un nombre válido.')
            nombre = ''
    while(len(tipo_terapia) <= 0):
        tipo_terapia = input('Ingrese el tipo de terapia:\nS) Sauna\nM) Masajes\n')
        tipo_terapia = tipo_terapia.upper()
        if(tipo_terapia != 'S' and tipo_terapia != 'M'):
            print('Ingrese un dato válido.')
            tipo_terapia = ''
    valor_terapia = 0
    if(tipo_terapia == 'S'):
        valor_terapia = 25000
    elif(tipo_terapia == 'M'):
        valor_terapia = 15000
    valida = True
    while(valida == True):
        try:
            cantidad_terapias = int(input('Ingrese la cantidad de terapias\n'))
            if(cantidad_terapias < 1):
                print('La cantidad debe ser entera y positiva')
            else:
                valida = False
        except:
            print('Debe ingresar un dato válido!')
    if(cantidad_terapias > cant_mayor):
        cant_mayor = cantidad_terapias
        nombre_mayor = nombre
    recaudado += (valor_terapia*cantidad_terapias)
    x = ''
    while(len(x) <= 0):
        x = input('¿Desea ingresar otro cliente? (S/N)\n')
        x = x.upper()
        if(x != 'S' and x != 'N'):
            print('Debe ingresar S o N')
            x = ''
        elif(x == 'N'):
            bucle = False
        

print('='*40)            
print('El total de clientes es de',total,'personas.')
print('El nombre del cliente con mayor cantidad de terapias es',nombre_mayor.capitalize(),'con',cant_mayor,'terapias.')
print('El total recaudado en el spa es',recaudado)
print('='*40)
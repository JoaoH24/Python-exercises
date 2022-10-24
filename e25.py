'''
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
'''

facturas = {}
pagada = {}
usr = int(input('Qué acción desea realizar con las facturas: \n 1) Agregar factura \t 2) Pagar factura \t 3) Terminar \n'))
while usr == 1 or usr == 2 or usr == 3:
    if usr == 1:
        nf = int(input('Ingrese el numero de factura: '))
        facturas[nf] = int(input('Ingrese el valor de la factura: '))
        print(f'La cantidad que se tiene que pagar en total = {sum(facturas.values())}')
        usr = int(input('Qué acción desea realizar con las facturas: \n 1) Agregar factura \t 2) Pagar factura \t 3) Terminar \n'))
    
    elif usr == 2:
        nf = int(input('Ingrese el numero de factura: '))
        pagada[nf] = facturas[nf]
        del(facturas[nf])
        print(f'La cantidad que pago en total = {sum(pagada.values())}')
        print(f'La cantidad que se tiene que pagar en total = {sum(facturas.values())}')
        usr = int(input('Qué acción desea realizar con las facturas: \n 1) Agregar factura \t 2) Pagar factura \t 3) Terminar \n'))
    else:
        print(facturas)
        break

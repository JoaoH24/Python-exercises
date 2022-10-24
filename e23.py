'''
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
'''

canasta = {}
flag = True

def add(bool):
    if bool == 'sí':
        prod = input('Ingrese un producto: ')
        canasta[prod] = float(input('Ingrese el precio del producto: '))
        return True
    else:
        print("PRODUCTOS".center(50,"="))
        for i,j in canasta.items():
            print(str(i).ljust(25,' ') + '\t' + str(j).rjust(18,' '))
        print(f'El costo total es: {sum(canasta.values())}')
        return False

while flag:
    rpt = input('Quiere agregar un elemento a la canasta: ').lower()
    flag = add(rpt)
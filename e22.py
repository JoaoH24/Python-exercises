'''
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
'''

datos = {}
rpt = input('Desea agregar algun dato extra sobre usted: ').title()

while rpt == 'Sí':
    dat = input('Ingrese el tipo de datos a almacenar: ')
    datos[dat] = input('Ingrese el valor del dato que almacenara: ')
    print(datos)
    rpt = input('Desea agregar algun dato extra sobre usted: ').title()

print(datos)

'''
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
'''

meses = {'enero':1,'febrero':2,'marzo':3,'abril':4,'mayo':5,'junio':6,'julio':7,'agosto':8,'septiembre':9,'octubre':10,'noviembre':11,'diciembre':12}
day = int(input('Ingrese el día: '))
mounth = int(input('Ingrese el mes: '))
year = int(input('Ingrese el año: '))

print(f'{day}/{mounth}/{year}')

def mou():
    m = meses.keys()    
    for i in m:
        if mounth == meses[i]:
            return i

mou()
print(f'{day} de {mou()} de {year}')
'''
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
'''

frutas = {'Plátano':1.35,'Manzana':0.80,'Pera':0.85,'Naranja':0.70}
fav = input('Ingrese el nobre de la fruta que quiere: ')
kg = input('Ingrese el numero de kilos que desea comprar: ')

total = frutas[fav]*int(kg)
print(f'Por {kg} kilos de {fav} tiene que pagar {total}')

# frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
# fruta = input('¿Qué fruta quieres? ').title()
# kg = float(input('¿Cuántos kilos? '))
# if fruta in frutas:
#     print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '€')
# else: 
#     print("Lo siento, la fruta", fruta, "no está disponible.")
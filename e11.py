'''
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
'''


list = []
for i in range(6):
	i = input('ingrese los numero de la loteria')
	list.append(i)

list.sort()

print(list)


# awarded = []
# for i in range(6):
#     awarded.append(int(input("Introduce un número ganador: ")))
# awarded.sort()
# print("Los números ganadores son " + str(awarded))
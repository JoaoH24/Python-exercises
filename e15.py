'''
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
'''

lista1 = [(1,2,3)]
lista2 = [(-1,0,2)]
lista3 = []

def prod(x,y):
    return lista1[x][y] * lista2[x][y]

cont = 0

while cont < 3:
    lista3.append(prod(0,cont))
    cont +=1

print(lista3)
print(sum(lista3))

# a = (1, 2, 3)
# b = (-1, 0, 2)
# product = 0
# for i in range(len(a)):
#     product += a[i]*b[i]
# print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product)) 
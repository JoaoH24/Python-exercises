'''
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
'''

Letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

for i in Letras:
	print(Letras.index(i))
	if Letras.index(i) % 2 == 0:
		Letras.remove(i)
print(Letras)
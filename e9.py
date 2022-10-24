'''
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
'''

word = input('Ingrese una palabra: ')
char = input('Ingrese una letra o caracter: ')
n_char = 0
for i in range(len(word)):
	if char == word[i]:
		n_char += 1
	else:
		continue

print(n_char)


# frase = input("Introduce una frase: ")
# letra = input("Introduce una letra")
# contador = 0
# for i in frase:
#     if i == letra:
#         contador += 1
# print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))
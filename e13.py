'''
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
'''

word = input('Ingrese una palabra: ')
word_reverse = word
word = list(word)
word_reverse = list(word_reverse)
word_reverse.reverse()

if word_reverse == word:
    print('La palabra es un palindromo')
else:
    print('La palabra no es un palindromo')
'''
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
'''

words = {}
n = input('Introduce un grupo de plabras del formato [spanish:english] y separelo por comas \n')

for i in n.split(sep=','):
    clave,valor = i.split(sep=':')
    words[clave] = valor

oration = input('Ingrese una oración que desea traducir: \n')

for e in oration.split():
    if e in words:
        print(words[e], end = ' ')
    else:
        print(i, end = ' ')
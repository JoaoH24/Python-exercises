'''
Escriba un programa que lleve la cuenta de el numero de veces que se encuentra el caracter ingresado por el usuario en una palabra
'''

frase = input('Ingrese una frase: ')
letra = input('Ingrese una letra: ')
contador = 0

for i in frase:
    if i == letra:
        contador += 1
    
print(f'Existen {contador} letras {letra} en la frase')
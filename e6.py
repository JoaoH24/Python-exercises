'''
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “exit” que terminará.
'''

usr = input('>_ ')
while True:
    if usr != 'exit':
        usr = input('>_ ')
    else:
        break
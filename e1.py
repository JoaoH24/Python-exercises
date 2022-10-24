'''
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

    - Ingredientes vegetarianos: Pimiento y tofu.
    - Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
'''

usr = input('¿Desea una pizza vegetariana?\n')
usr2 = ''
if usr == 'si':
    print('La pizza vegetariana puede tener los siguientes ingredientes: \n - mozzarella\n - tomate\n - pimiento(opcion 1)\n - tofu(opcion 2)')
    usr2 = input('Ingrese el ingrediente que desea en su pizza: ')
    if usr2 == 'pimiento' or usr2 == 'tofu':
        print(f'Su pizza contendra los siguientes ingredientes:\n - mozzarella\n - tomate\n - {usr2}')
    else: print('ERROR: El ingrediente ingresado no esta en la lista')
elif usr == 'no':
    print('La pizza no vegetariana puede tener los siguientes ingredientes: \n - mozzarella\n - tomate\n - peperoni(opcion 1)\n - jamon(opcion 2)\n - salmón(opcion 3)')
    usr2 = input('Ingrese el ingrediente que desea en su pizza: ')
    if usr2 == 'peperoni' or usr2 == 'jamon' or usr2 == 'salmon':
        print(f'Su pizza contendra los siguientes ingredientes:\n - mozzarella\n - tomate\n - {usr2}')
    else: print('ERROR: El ingrediente ingresado no esta en la lista')
else: print('ERROR: Ingreso una respuesta invalida')


'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
'''
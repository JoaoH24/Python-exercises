''''
EScriba un programa que muestre por pantalla los numeros de la sucesión de fibonacci
'''

n = int(input('Ingrese un numero: '))
a = 0
b = 1
c = 0
while c <= n:
    print(c)
    c = a + b
    a = b
    b = c

# x = int(input('Cuantos números de la sucesión quieres?: '))
# n1 = 0
# n2 = 1

# print(f'1. {n1} \n 2. {n2}')
# for i in range(3, x+1):
#     s = n1 + n2
#     if n1 < n2:
#         n1 = s
#     else:
#         n2 = s
#     print(f'{i}. {s}')
 
import random
n = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação sera ')
print(lista)

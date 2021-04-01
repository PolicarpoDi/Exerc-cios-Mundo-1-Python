from random import choice
n = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = (n, n2, n3, n4)
escolhido = choice(lista)
print('O aluno sorteado foi {}'.format(escolhido))
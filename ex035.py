r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta '))
r3 = float(input('Digite o comprimento da terceira reta '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: # a soma de 2 medidas não podem ser menor que uma
    print('É possivel formar um triangulo com essas retas')
else:
    print('Não é possivel formar um triangulo com essas retas')

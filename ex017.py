from math import hypot
catetoo = float(input('Qual é o comprimento do Cateto oposto: '))
catetoa = float(input('Qual é o comprimento do Cateto Adjacente: '))
h = math.hypot(catetoo, catetoa)
print('a Hipotenusa vai medir {:.2f}'.format(h))

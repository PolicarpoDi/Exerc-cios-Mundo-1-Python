m = float(input('Digite o valor em metros: '))
c = m * 100
mi = m * 1000
d = m / (10**1)
h = m / (10**2)
k =  m / (10**3)
print('O valor em metros é {}'.format(m))
print('O valor em centimetros é {:.2f}'.format(c))
print('O valor em milimetros é {:.2f}'.format(mi))
print('O valor em Decametro é {:.2f}'.format(d))
print('O valor em hectometro é {:.2f}'.format(h))
print('O valor em kilometro é {:.2f}'.format(k))

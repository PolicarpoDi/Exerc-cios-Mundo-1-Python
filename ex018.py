import math
ang = float(input('Digite o algulo '))
seno = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O angulo de {} tem o Seno de {:.2f}'.format(ang, seno))
print('O angulo de {} tem o Cosseno de {:.2f}'.format(ang, coss))
print("O angulo de {} tem a Tangente de {:.2f}".format(ang, tang))
distancia = int(input('Digite a distancia da viagem em km: '))
if distancia >= 200:
    print('A passagem vai custar {}R$'.format(distancia * 0.45))
else:
    print('A passagem vai custar {}R$'.format(distancia * 0.50))
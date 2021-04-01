qd = int(input('Qual é a quantidade de dias alugados: '))
km = float(input('Quantos KMs foram rodados: '))
pa = qd * 60.00
pk = km * 0.15
print('O preço do aluguel por dia é de {}'.format(pa))
print('O preço do KM é de {}'.format(pk))
print('O valor total do aluguel é de {}'.format(pa+km))

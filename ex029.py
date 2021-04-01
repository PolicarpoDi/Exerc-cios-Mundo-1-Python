vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (vel - 80) * 7 # calcula a velocidade - os 80 permitido, pois a sobra vai ser calculada por 7
    print('Você estava a {}km/h, portanto a sua multa vai ser de {}R$'.format(vel, multa))
print('Tenha um bom dia! DIRIJA COM SEGURANÇA')

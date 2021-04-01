from random import randint
from time import sleep # Importando a biblioteca time e o metodo sleep
print('=' * 60)
print('Vou pensar em um número de 0 a 5. Tente adivinhar........')
print('=' * 60)
computador = randint(0, 5) # randomizador de 0 a 5, onde faz o computador "PENSAR"
jogador = int(input('Que número eu pensei?: ')) # O jogador tenta adivinhar
print('PROCESSANDO......')
sleep(3) #metodo sleep com o tempo em segundos
if computador == jogador: # se o numero do computador for igual do jogador, vc acerta
    print('Eu pensei no numero {}, você ACERTOU!'.format(computador))
else: # se o numero do computador for diferente do jogador, vc erra
    print('Eu pensei no numero {} e você pensou no numero {}, você ERROU!'.format(computador, jogador))




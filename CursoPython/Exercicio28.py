# Escreva um programa que faça o computador pensar em um número de 0 a 5 e peça para o usuário descobrir qual foi o número escolhido pelo computador.
#o programa deve escrever se usuário venceu ou perdeu.

import random
computador = random.randint(0, 5)  # Faz o computador sorteare um numero
print('--=--' *5)
jogador = int(input('Digite um numero de 0 a 5: '))
print('--=--' *5)
print('Vc digitou o número: {}'. format(jogador))
print('O número sorteado pelo computador foi: {}'. format(computador))

if computador == jogador:
    print('Vc ganhou parabéns')
else:
    print('vc perdeu infelizmente')

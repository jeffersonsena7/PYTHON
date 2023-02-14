# O computador vai pensar em um número entre 0 e 10, só que o jogador vai tentar até acertar
#mostrando no final quantos palpites foram necessários para vencer.

tentativa = 0
pessoa = 0
from random import randint
computador = randint(0, 10)
while computador != pessoa:
    pessoa = int(input('Digite o número: '))
    if computador != pessoa:
        tentativa = tentativa + 1
print('Você tentou {} vezes para acertar o número escolhido pelo computador que foi: {}'.format(tentativa + 1, computador))
# O computador vai pensar em um número entre 0 e 10, só que o jogador vai tentar até acertar
#mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0, 10)
print('Sou seu computador ... acabei de pensar em um numero de 0 a 10.')
acertou = False
palpite = 0
while not acertou:
    pessoa = int(input('Qual o seu palpite: '))
    palpite = palpite + 1
    if computador == pessoa:
        acertou = True
    else:
        if pessoa < computador:
            print('Mais... Tente mais uma vez')
        elif pessoa > computador:
            print('Menos... Tente mais uma vez')
print('Você tentou {} vezes para acertar o número escolhido pelo computador que foi: {}'.format(palpite, computador))
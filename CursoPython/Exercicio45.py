#Crie um programa que faça o computador jogar JOKENPô com você.

from random import randint
item = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Escolha uma opção:
[0] Pedra'
[1] Papel'
[2] Tesoura''')
jogador = int(input("Qual é a sua jogada: "))

print('-=' * 12)
print('Computador jogou: {}'.format(item[computador]))
print('Você jogou: {}'.format(item[jogador]))
print('-=' * 12)

if computador == 0:
    if jogador == 0:
        print('Empatou')
    elif jogador == 1:
        print('Você ganhou')
    elif jogador == 2:
        print('Computador ganhou')
    else:
        print("Você Inválida")
if computador == 1:
    if jogador == 0:
        print("computador ganhou")
    elif jogador == 1:
        print('Empatou')
    elif jogador == 2:
        print('Você ganhou')
    else:
        print('Jogada inválida')
if computador == 2:
    if jogador == 0:
        print('Você ganhou')
    elif jogador == 1:
        print('Computador ganhou')
    elif jogador == 2:
        print('Empatou')
    else:
        print('Jogada inválida')

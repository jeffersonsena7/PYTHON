# Faça um programa que jogue par ou ímpar com o computador. O jogador só serar interrompido
# quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final.
import random
from random import randint
print('=-' *20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)

cont = 0
while True:
    numero = int(input('Diga o valor: '))
    computador = randint(0, 10)
    total = numero + computador
    tipo = ' '
    print('--' * 20)
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {numero} e o computador {computador}. total de {total}', end='')
    print('DEU PAR' if total %2 == 0 else 'DEU IMPAR')

    if tipo == 'P':
        if total %2 == 0:
            print('Você venceu!')
            cont = cont+1
        else:
            print('Você perdeu!!')
            break
    if tipo == 'I':
        if total %2 == 1:
            print('Você venceu!!')
            cont = cont +1
        else:
            print('Voce perdeu!!')
            break
print('=-'*20)
print(f'GAME OVER! Você venceu {cont} vez.')
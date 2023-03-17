# Crie um programa que vai gerar cinco numeros aleatorio e colocar em uma tupla. Depois disso mostre a listagem
# de números gerados e também indique p menor e o maior valor que está na tupula.

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),randint(1, 10))
print('Os númeors sorteados foi: ',end='')
for n in numeros:
    print(f'{n}', end=' ')
print('')
print('='*40)
print(f'\nO maior número sorteado foi {max(numeros)}')
print('='*40)
print(f'O menor número sorteado foi {min(numeros)}')
'''Crie um programa que leia um numero Real qualque pelo teclado e mostre na tela o seu valor inteiro.'''

import math
numero = float(input('Digite um numero real: '))
print('Numero digitado foi {} e seu numero inteiro é {}'. format(numero, math.trunc(numero)))
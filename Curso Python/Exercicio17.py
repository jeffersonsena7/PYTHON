''' Faça um programa que leia o comprimento do cateto oposto e do cateto adjacenter de um triângulo retângulo e mostre o comprimento da hipotenusa.'''

import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input(' Digite o valor do cateto adjacente: '))
hi = math.hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'. format(hi))

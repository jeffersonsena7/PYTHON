'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno coseno e tangente desse ângulo.'''

import math
angulo = float(input('Digite o ângulo que vc deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O ângulo de seno {:.2f}\nO ângulo de cosseno {:.2f}\nO ângulo de tangente {:.2f}'. format(seno, cosseno, tangente))
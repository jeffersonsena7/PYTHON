''' Faça um programa que leia o comprimento do cateto oposto e do cateto adjacenter de um triângulo retângulo e mostre o comprimento da hipotenusa.'''

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input(' Digite o valor do cateto adjacente: '))

'''hipotenusa faz cateto oposto ao ² que é ** 2 x cateto adjacente ² que é ** 2, tudo na raiz quadrada que é ** 1/2'''
hi = (co ** 2 + ca ** 2) ** (1/2)


print('A hipotenusa vai medir {:.2f}'. format(hi))

#Faça um programa que leia um número qualquer e mostre o seu fatorial.

#usando o import de fatorial
#from math import factorial
#numero = int(input('Digite um número: '))
#fatorial = factorial(numero)
#print('O fatorial de {} é {}'.format(numero, fatorial))

numero = int(input('Digite um número: '))
c = numero
f = 1
while c > 0:
    print(' {}'.format(c), end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(end=' =')
    f = f * c
    c = c -1

print(' {}'.format(f), end='')
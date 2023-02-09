# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

numero = int(input('Digite um numero inteiro: '))

resultado = numero % 2

if resultado == 0:
    print('O numero digitado foi {}, ele é PAR'. format(numero))
else:
    print('O número digitado foi {}, ele é ÍMPAR'. format(numero))

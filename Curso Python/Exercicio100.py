# Faça um programa que tenha uma lista chamada número e duas funções chamadas sorteio() e somaPar(). A primeira
#função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos
#os valores PARES sorteando pela função anterior
from random import randint
from time import sleep
print('Os valores sorteados foi: ',end='')
def sorteio(lista):


    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}',end=' ')
        sleep(0.3)
    print()
    print('-='*30)
def somaPar(num):
    soma = 0
    for valor in num:
        if valor %2 == 0:
            soma = soma + valor
    print(f'Somando os valores pares de {num}, temos {soma}')


numero = list()
sorteio(numero)
somaPar(numero)
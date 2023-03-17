# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo. Seu
#programa tem que realizar três contagens através da função criada:
# a) De 1 até 10 de 1 em 1.
# b) De 10 até 0 de 2 em 2.
# c) Uma contagem personalizada.
from time import sleep


def lin():
    print('-=' *20)


def contador(inicio, fim, passo):
    if passo < 0:               # isso faz para usar o negativo no números que vai ser digitado
        passo = passo * -1
    if passo == 0:
        passo = 1
    lin()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ')
            sleep(0.3)
            cont = cont + passo
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ')
            sleep(0.3)
            cont = cont - passo
        print('FIM')

#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
lin()
print('Agora é sua vez de personalizar a contagem')
ini = int(input('Inicio: '))
final = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, final, pas)
# Faça um programa que tenha uma função chamada maior(), que receba vários parametros com o valor inteiros. Seu
#programa tem que analisar todos os valores e dizer qual deles é o maior.
def lin():
    print('=-' *20)


def maior(*num):

    cont = 0
    maior = 0
    lin()
    print('\nAnalisando os valores passado...')
    for n in num:
        print(f'{n}' ,end=' ')
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont = cont +1
    print()
    lin()
    print(f'Foram informado {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensor, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá por extenso.

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco','seis', 'sete', 'oito',
        'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')
continuar = ' '
while True:
    print('=' *30)
    num = int(input('Digite um número de 0 a 20: '))
    if num < 0 or num > 20:
        print('=' * 30)
        print('O número não está entre 0 e 20 ')
    else:
        print('=' * 30)
        print(f'Você digitou o número {cont[num]}')
        print('=' * 30)
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar != 'S':
        break
print('**' *20)
print('Fim do programa !!!')
print('**' *20)

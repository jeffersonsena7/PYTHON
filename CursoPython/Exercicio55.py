# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o mennor
# e o maior peso lidos.

maiorpeso = 0
menorpeso = 0

for pessoa in range(1,6):
    peso = float(input('Digite o {}º peso: '.format(pessoa)))

    if pessoa == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print('O maior peso lido foi de {}. kg'.format(maiorpeso))
print('O menor peso lido foi de {} kg.'.format(menorpeso))

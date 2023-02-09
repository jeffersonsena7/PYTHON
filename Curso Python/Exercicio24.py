# Crie um programa que leia o nome de uma cidade e diga se começa ou não com o nome "SANTO".

nome = str(input('Digite o nome da cidade: '))

print('O nome da cidade começa com Santo: {}'.format(nome[:5] == 'Santo'))
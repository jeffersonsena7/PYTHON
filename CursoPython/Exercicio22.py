# Faça um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# A quantidade de letra sem considerar espaços
# A quantidade de letra que tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome toto maiusculo é {} '.format(nome.upper()))
print('Seu nome todo menusculo é {} '. format(nome.lower()))
print('Seu nome tem {} letras: '. format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras  '. format(nome.find(' ')))
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se pode formar um triâmgulo.

l1 = float(int(input('Digite a primeira reta: ')))
l2 = float(int(input('Digite a segunda reta: ')))
l3 = float(int(input('Digite a terceira linha: ')))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 +l2:
    print('\033[1;34;40mOs dados acima forma um triângulo\033[m')
else:
    print('\033[7;31;40m Os dados acima não forma um triângulo\033[m')
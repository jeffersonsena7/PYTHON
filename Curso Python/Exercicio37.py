#Escreva um programa que leia um número inteiro qualquer  e peça para o usuário escolher qual será a base da conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input('Digite o numero interiro: '))
conv = int(input('Digite o númeroro de 1 a 3, para a conversão: '))

binario = bin(num)
octal = oct(num)
hexadecimal = hex(num)

if conv == 1:
    print('O numero escolhido foi Binário {}'. format(binario[2::])) #coloca o [2::] para remover as 2 casas a frente e deixaar so as 4 últimas, se n mostra 0b de binario
elif conv == 2:
    print('O número escolhido foi o 2 Octal {}'. format(octal))
else:
    print('O número escolhido foi o 3 Hexadecimal {}'. format(hexadecimal))



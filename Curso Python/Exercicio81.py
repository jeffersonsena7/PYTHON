# Crie um programa que vai ler vários números e coloca em uma lista. Depois disso mostre:
#Quantos números foram digitados.
#A lista de valores, ordenadas de forma decrescenter.
#Se o valor 5 foi digitado e está ou não na lista.

numeros = []
continuar = ''
cont = 0
nalista = 0

while True:
    numeros.append(int(input('Digite um valor: ')))
    cont = cont + 1
    continuar = str(input('Quer contimuar [S/N]: '))
    if continuar == 'n':
        break
print(f'Você digitou {cont} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrecente são {numeros}')
if 5 in numeros:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista')




# Crie um programa que leia 5 valores númericos e guardeos em uma lista. No final, mostre qual foi
#o maior e o menor valor digitado e as suas respectivas posições na lista.
maximo = 0
minimo = 0
lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite o valor para na Posição {cont}: ')))
    if cont == 0:
        maximo = lista[cont]
        minimo = lista[cont]
    else:
        if lista[cont] > maximo:
            maximo = lista[cont]
        if lista[cont] < minimo:
            minimo = lista[cont]

print('='* 50)
print(f'O valor digitado foi {lista}')
print('='* 50)
print(f'O maior valor digitado foi {maximo} nas posições ',end='')
for c, l in enumerate(lista):
    if l == maximo:
        print(f'{c}...',end='')
print('')
print('='* 50)
print(f'\nO menor numero digitado foi {minimo} nas posições ',end='')
for c, l in enumerate(lista):
    if l == minimo:
        print(f'{c}...', end='' )
print('')
print('='* 50)
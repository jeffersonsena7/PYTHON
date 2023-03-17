# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# Quantas pessoas foram cadastradas.
# Uma lista comas pessoas pesadas.
# Uma lista com as pessoas mais leve.

cadastro = []
dados = []
maior = 0
menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(cadastro) == 0:
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    cadastro.append(dados[:])
    dados.clear()
    opcao = str(input('Quer continuar [S/N]: '))
    if opcao in 'nN':
        break
print('=-' *30)
print(f'Ao todo, você cadastrou {len(cadastro)}')
print(f'O menor peso foi de {menor}kg. peso de ',end=' ')
for p in cadastro:
    if p[1] == menor:
        print(f'[{p[0]}] ',end=' ')
print('')
print(f'O maior peso foi de {maior}kg. peso de ', end=' ')
for p in cadastro:
    if p[1] == maior:
        print(f'[{p[0]}]',end=' ')

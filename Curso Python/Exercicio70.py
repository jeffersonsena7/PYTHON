# Crie um programa que leia o nome e o preço de cada produtos. O programa deverá perguntar se o usuário
#vai continuar. No final, mostre:
#Qual é o total gasto na compra.
#Quantos produtos custa mais e 1000
#qual produto mais barato.

print('-'*20)
print('  LOJA SUPER OFERTAS  ')
print('-'*20)

total = 0
total1000 = 0
menor = 0
cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = int(input('Preço: R$ '))
    cont = cont +1
    total = total + preco
    if preco > 1000:
        total1000 = total1000 +1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    usuario = ' '
    while usuario not in 'SN':
        usuario = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if usuario == 'N':
        break
print('---------- FIM DO PROGRAMA ----------')
print(f'O total da compra foi R${total}')
print(f'Temos {total1000} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa {menor}')
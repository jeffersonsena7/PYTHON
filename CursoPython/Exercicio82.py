# Crie um programa que vai ler vários números e colocar em uma lista. depois disso, crie duas listas extras
#que vão conter apenas valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo
#dos três listas geradas.

lista1 = []
lista2 = []
lista3 = []

while True:
    lista1.append(int(input('Digite um valor: ')))
    opcao = str(input('Você quer continuar [S/N]: '))
    if opcao in 'nN':
        break
for l in lista1:
    if l %2==0:
        lista2.append(l)
    else:
        lista3.append(l)
print('=-'*25)
print(f'A lista completa é: {lista1}.')
print('-'*30)
print(f'A lista de pares é: {lista2}.')
print('-'*30)
print(f'A lista de ímpares é: {lista3}.')
print('-'*30)
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastra em uma lista única, que
#mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

dados = [[], []]
numero = 0
for c in range(1, 8):
    numero = int(input(f'Digite o {c}º Valor: '))
    if numero %2 == 0:
        dados[0].append(numero)
    if numero %2 == 1:
        dados[1].append(numero)
print('=-' *30)
dados[0].sort()
dados[1].sort()
print(f'Os numeros pares são {dados[0]}')
print(f'Os números ímpares são {dados[1]}')



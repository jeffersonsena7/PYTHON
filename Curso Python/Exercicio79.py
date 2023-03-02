# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
#exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em oredem crescente.

continuar = ''
numeros = []
while continuar != 'nN':
    valor = int(input('Digite um valor: '))
    if valor not in numeros:
        numeros.append(valor)
        print(f'O valor {valor} foi adicionado com sucesso.')
    else:
        print(f'O numero {valor} já foi digitado não vou adicionar.')

    continuar = str(input('Quer continuar? [S/N]: '))
    if continuar in 'nN':
        break
print('=-'*30)
print(f'os valores digitados foi:  {sorted(numeros)} ')
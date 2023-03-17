# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# Quantas pessoas cadastradas
# A média de idade
# Uma lista com mulheres
# Uma lista com idade acima da média

pessoas = dict()
galera = list()
soma = 0
media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma = soma + pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apena S ou N.')
    if resp == 'N':
        break
print('-='*30) # até aqui é a leitura dos dados, p baixo é o resultado
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]} ', end='')
print()
print('Lista de pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= media:
        print('         ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()


#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
# deverá perguntar se o usuário quer continuar ou não, no final, mostre:
# Quantas pessoas tem mais de 18 anos.
# Quantos homens foram cadastrados.
# Quantas mulheres tem menos de 20 anos.
totalidade= totalhomem = totalmulher = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo ! [M/F] ')).strip().upper()[0]
    print('-' * 20)
    if idade > 18:
        totalidade = totalidade +1
    if sexo == 'M':
        totalhomem = totalhomem +1
    if idade < 20 and sexo == 'F':
        totalmulher = totalmulher +1

    usuario = ' '
    while usuario not in 'SN':
        usuario = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if usuario == 'N':
        break

print('===== Fim do programa=======')
print(f'Total de pessoas com mais de 18 anos : {totalidade}')
print(f'Ao todo temos {totalhomem} homens cadastrados')
print(f'E temos {totalmulher} mulheres com menos de 20 anos')

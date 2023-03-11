# Faça um programa que leia nome e média de um aluno, guardando tamém a situação em um dicionário. No final
#mostre o conteúdo da estrutura na tela.

lista = {}

lista['nome'] = str(input('Nome: '))
lista['media'] = float(input(f'A média de {lista["nome"]}: '))
if lista['media'] >= 7:
    lista['situação'] = 'Aprovado'
elif lista['media'] >= 5 and lista['media'] < 7:
    lista['situação'] = 'Recuperação'
else:
    lista['situação'] = 'Reprovado'

for k, v in lista.items():
    print('='*30)
    print(f'{k} {v}')
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
#boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individual.

lista = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    resposta = str(input('Quer continuar [S/N]: '))
    lista.append([nome ,[nota1, nota2], media])
    if resposta in 'nN':
        break
print('-='*20)
print('No.    NOME            MÉDIA')
print('-'*30)
for c, l in enumerate(lista):
    print(f'{c}   {l[0]:^10}       {l[2] :^5}')
while True:
    opcao = int(input('Mostrar nota de qual aluno? (999 para o programa): '))
    if opcao == 999:
        print('FINALIZADO...')
        break
    if opcao <= len(lista) -1:
        print(f'Notas de {lista[opcao] [0]} são {lista[opcao][1]}')
    print('--'*30)

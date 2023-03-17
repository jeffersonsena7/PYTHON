# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
#se por acaso acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salario.
#Calcule e acrescente, além da idade, com quantos anos a pessoa falta para se aposentar.
from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
dados['nascimento'] = int(input('Ano de Nascimento: '))
dados['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
dados['idade'] = datetime.now().year - dados['nascimento']
print('=-'*30)
if dados['carteira'] == 0:
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
if dados['carteira'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = 65 - (dados['contratacao'] - dados['nascimento'])
    print('=-' * 30)
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
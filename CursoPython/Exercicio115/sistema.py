# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de
#texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from CursoPython.Exercicio115.lib.arquivo import *
from CursoPython.Exercicio115.lib.interface import *
from time import sleep

arq = 'arquivodados.txt'

if not arquivoExistente(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de lista o conteúdo de u arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabecario('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Digitou um opção errada no menu.
        cabecario('Saindo do Sistema ... até logo!')
        break
    else:
        cabecario('\033[31mERRO!! Digite uma opção válida\033[m')
    sleep(2)

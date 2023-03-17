from CursoPython.Exercicio115.lib.interface import *


def arquivoExistente(nome):
    try:
        a = open(nome, 'rt')  # Ver se tem arquivo criado esse 'rt' r -> ler, t-> texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')  # esse cria o arquivo se não tiver o 'wt+' w-> escrever, t -> texto, + -> criar
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabecario('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at') # coloca o a para adicionar a lista 'at' a -> append -> adicionar, t-> texto
    except:
        print('Houve um ERRO na abertura de arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
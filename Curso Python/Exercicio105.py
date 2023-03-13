# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
#com as seguintes informações:
# - Quantidade de notas - Amaior nota - A menor nota - A média da turma - A siruação (opcional) - Adicine também as
#docstrings.

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n: Uma ou mais notas dos alunos
    :param sit: Valor opcional se deve ou não colocar a situação da turma
    :return: Dicionario com varia informações da situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'Boa'
        elif r['media'] >= 5:
            r['situacao'] = 'Regular'
        else:
            r['situacao'] = 'Ruim'
    return r

#programa principal
res = notas(5.5,3.3, 6, 8.5, sit=True)
print(res)
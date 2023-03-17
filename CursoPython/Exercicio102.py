# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
#a calcular e o outro chamado show, que serar um valor lógico(opcional) indicando se será mostrado ou não
# na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
    -> Calcula o faatorial de um numero
    :param num: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            if c == 1:
                print('=',end=' ')
        f = f * c
    return f


#programa principal

print(fatorial(5,True))

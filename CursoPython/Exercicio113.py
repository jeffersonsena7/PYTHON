# Reescreva a função leiaint() que fizemos no desafio 104, incluindo agoa a possibilidade da digitação de um número
#de tipo invalido. Aproveite e crie tbm uma função leiafloat() com a mesma funcionalidade.

def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!! Por favor digite um numero inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31mO usuário preferiu não digitar nenhum número\033[m')
            return 0
        else:
            return num

def leiafloat(msg):
    while True:
        try:
            num2 = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!! Por favor digite um numero real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31mO usuário preferiu não digitar nenhum número\033[m')
            return 0
        else:
            return num2

num = leiaint('Digite um número Inteiro: ')
num2 = leiafloat('Digite um número Real')
print(f'O valor inteiro foi: {num} e o real foi: {num2}')
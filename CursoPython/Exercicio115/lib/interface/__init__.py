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


def linha(tam=42):
    return '-'*tam


def cabecario(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecario('MENU PRINCIPAL')
    c =1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c = c +1
    print(linha())
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc

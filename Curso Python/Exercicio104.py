# Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante a input() do python,
#só que fazendo a validação para aceitar apenas um valor númerico.
# ex: n = leiaint('dogite um valor')


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero valido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n} ')
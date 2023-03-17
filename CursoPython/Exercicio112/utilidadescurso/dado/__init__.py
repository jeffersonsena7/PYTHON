def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip() #strip remove todos os espaços
        if entrada.isalpha() or entrada == '': # testa se é numerico e se n esta fazio
            print(f'\033[0;31mERRO!! {entrada} é um preço invalido\033[m')
        else:
            valido = True
            return float(entrada)

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
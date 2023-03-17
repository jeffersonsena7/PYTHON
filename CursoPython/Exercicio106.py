# Faça um mini-sistema que utilize o interactive Help do python. O usuário vai digitar o comando e o manual vai aparecer.
#quando o usuário digita a palavra 'FIM', o programa se encerrará. OBS: use cores

c = ('\033[m',          # 0 - sem cor
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m'       # 6 - branco
     )

def ajuda(com):
    titulo(f'Acessando o manualdo comando \'{com}\'', 4)
    print(c[6])
    help(com)
    print(c[0])

def titulo(msg, cor=0):
    tam = len(msg) +4
    print(c[cor], end='')
    print('~' *tam)
    print(f' {msg}')
    print('~' *tam)
    print(c[0], end='')

#programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 1)
    comando = str(input('Função ou Biblioteca > '))
    if comando == 'fim':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)
# Faça um programa que tenha uma função chamada ficha(), que recebe dois parâmetros opcionais: o nome de um jogador
#e quantos gols ele marcou. O programa deverá ser capaz de mostra a ficha do jogador, mesmo que algum dado não tenha
#sido informado corretamente.

def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gols no campeonato')


#programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
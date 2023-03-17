# Aprimore o desafio 93 para que ele funfione com vários jogadores, incluindo um sistema de visualização de
#detalhes do aproveitamento de cada jogador.
time = list()
jogador = dict()
quantgol = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partida = int(input(f'quantas partidas {jogador["nome"]} jogou? '))
    quantgol.clear()
    for c in range(0, partida):
        quantgol.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = quantgol[:]
    jogador['total'] = sum(quantgol) #sum usado para soma
    res = str(input('Quer continuar [S/N]: '))
    time.append(jogador.copy())
    if res in 'n':
        break   #até aqui ler os dados
print('=-'*30)  # aqui p baixo mostra os dados
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('=-'*30)
for k, v in enumerate(time):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('=-'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca > len(time):
        print(f'ERRO! Não existe jogador com codigo {busca}')
    else:
        print(f' --Levantaento do jogador {time[busca]["nome"]}:')
        for i,g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i} fez {g} gols')
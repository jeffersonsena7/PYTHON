# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol,
#na ordem de colocação. Depois mostre:
# Os 5 primeiros
# Os últimos 4 colocados.
# Time em ordem alfabética.
# Em que posição esta o time da chapecoense.

times = ('Corinthias', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo',
         'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí',
         'Ponte Preta', 'Atlético-GO')

print('=-' * 100)
print(f'Lista de times do Brasileirão: {times}')
print('=-' * 100)
print(f'Os cincos primeiros colocados são: {times[0:5]}')
print('=-' * 100)
print(f'Os últimos 4 colocados são: {times[-4:]}')
print('=-' * 100)
print(f'Times em ordem alfabética : {sorted(times)}')
print('=-' * 100)
print(f'Em que posição a chapecoense está: {times.index("Chapecoense")+1} posição')
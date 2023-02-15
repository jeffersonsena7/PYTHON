# Refaça o desafio 51, lendo o termo e a razão de uma PA, mostrando os 10 primeiros termos
#da progressão usando a estrutura while.

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1

while cont <= 10 :
    print('{} ->'.format(termo), end='')
    termo = termo + razao
    cont = cont +1
print('Fim')

# Crie um programa que crie uma matriz da dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.

lista = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite um valor para matriz {[l]}{[c]}:'))
print('=-' *20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]',end='') # :^5, cinco espaço centralizado
    print()
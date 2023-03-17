# Aprimore o desafio anterior, mostrando no final:
#A soma de todos os valores pares digitados.
#A soma dos valores da terceira coluna.
#O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = 0
somaterceira = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para a matriz [{l},{c}] :'))
print('=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]',end='')
        if matriz[l][c] %2 == 0:
            par = par + matriz[l][c]


    print()
print('=-'*30)
print(f'A soma de todos os valores pares é: {par}')
for l in range(0, 3):
    somaterceira = somaterceira + matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {somaterceira}')
for c in range(0, 3):
    if c == 0:
        mior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior}')
#Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três
# e que se encontra no intervalo de 1 a 500.
soma=0
for c in range(0, 501, 2):
    if c %3 == 0:
        soma = soma + c
print(soma)

#Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três
# e que se encontra no intervalo de 1 a 500.
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {}, valores solicitado {}'.format(cont, soma))
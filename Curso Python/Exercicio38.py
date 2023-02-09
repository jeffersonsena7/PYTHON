# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma menssagem.
# O primeiro valor é maior
# o segundo valor é maior
# não existe valor maior os dois são iguais

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if (n1 > n2):
    print('O primeiro valor foi: {} e o segundo valor foi: {}, assim o primeiro é maior que o segundo'. format(n1, n2))
elif (n1 < n2):
    print('O primeiro valor foi: {} e o segundo valor foi: {}, assim o Segundo é maior que o primeiro'. format(n2, n1))
elif n1 == n2:
    print('Não existe valor maior n1 {} e n2 {}, são iguais.'. format(n1, n2))

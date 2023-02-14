#Crie um programa que leia dois valores e mostre um menu na tela: [1]somar,[2]multiplicar, [3]maio,
#[4]novos números, [5]sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.

somar = 0
multiplicar = 0
maior = 0
novo = 0
sair = 0


while sair != 5:
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    if valor1 >=0 and valor2 >= 0:
        operacao = int(input(' [1] Somar \n [2] Multiplicar\n [3] Maior\n [4] Novos números\n [5] Sair \n\n Escolha a operação: '))
        if operacao == 1:
            somar = valor1 + valor2
            print('\nA soma dos valores é : {}\n'.format(somar))
        if operacao == 2:
            multiplicar = valor1 * valor2
            print('\nA multiplicação dos valores é {}\n'.format(multiplicar))
        if operacao == 3:
            if valor1 > valor2:
                maior = valor1
                print('\nO maior número é {}\n'.format(maior))
            else:
                maior = valor2
                print('\nO maior número é {}\n'.format(maior))
        if operacao == 4:
            print('\nDigite novo numeros\n')
        if operacao == 5:
            sair = 5
print('FIM')



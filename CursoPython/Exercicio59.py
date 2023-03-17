#Crie um programa que leia dois valores e mostre um menu na tela: [1]somar,[2]multiplicar, [3]maio,
#[4]novos números, [5]sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
opcao = 0

while opcao != 5:
    print('''    [1] Somar 
    [2] Multiplicar 
    [3] Maior
    [4] Novos números
    [5] Sair''')
    opcao = int(input('>>>>>>>>>Qual é a sua opção? '))
    if opcao == 1:
        somar = valor1 + valor2
        print('\nA soma dos valores é : {}\n'.format(somar))
    if opcao == 2:
        multiplicar = valor1 * valor2
        print('\nA multiplicação dos valores é {}\n'.format(multiplicar))
    if opcao == 3:
        if valor1 > valor2:
            maior = valor1
            print('\nO maior número é {}\n'.format(maior))
        else:
            maior = valor2
            print('\nO maior número é {}\n'.format(maior))
    if opcao == 4:
        print('\nDigite novo numeros\n')
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    if opcao == 5:
        print('Finalizado')
        sair = 5
    else:
        print('Opção inválida. Tente novamente')
    print('-=' * 10)
print('FIM')



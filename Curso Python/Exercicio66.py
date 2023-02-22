#Crie um programa que leia vários números inteiros pello teclado. O programa só vai parar quando o usuário
#digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a
#soma entre eles.(desconsidersndo o flag, que é o 999.


cont = 0
soma = 0
while True:
    num = int(input('Digite um número e [999 para parar]: '))
    if num == 999:
        break
    cont = cont + 1
    soma = soma + num
print(f'Foi digitado {cont} números e a soma entre eles é: {soma}')
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
#o usuiário digitar p valor 999, que é a condição de parar. No final, mostre quantos números foram
#digitados e qual foi a soma entre eles (desconsiderando o flag) que é o 999.
cont = 0
num = 0
total = 0
num = int(input('Digite o número [999 para parar]: ')) # usa um fora e um dentro do while para nã contar e nem somar com o 999
while num != 999:
    cont = cont + 1
    total = total + num
    num = int(input('Digite o número [999 para parar]: '))
print('Foi digitado {} números e a soma de todos os números é:  {}'.format(cont, total))

#Faça um programa que leia um número qualquer e mostre o seu fatorial.
fatorial = 0
num = int(input('Digite o valor: '))
cont = 0
totalfatorial=0
while num > 1:
    num = num - 1
    cont = num + 1
    fatorial = num * cont
    print(num)

print('fim')
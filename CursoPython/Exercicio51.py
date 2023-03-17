#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre
#os 10 primeiros termos dessa progessão.
soma = 0
cont = 0

primeiro = int(input("Primeiro termo: "))
razao = int(input("razão: "))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end='-> ')
print('fim')
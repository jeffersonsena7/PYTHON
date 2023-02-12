#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre
#os 10 primeiros termos dessa progessão.
soma = 0
cont = 0

p1 = int(input("Primeiro termo: "))
r = int(input("razão"))
for c in range(p1, 20, r):
    print('{}'.format(c), end=' -> ')
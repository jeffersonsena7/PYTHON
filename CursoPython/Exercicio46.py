#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos
#de artifício indo de 10 ate 0, com uma pausa de 1 segundo entre elas.

from time import sleep

for c in range(10, 0, -1):
    sleep(1)
    print(c)
    print('-=' * 5)
print('Estourando fogos de artificio')
print('*****************************')
print('|||||||||||||||||||||||||||||')

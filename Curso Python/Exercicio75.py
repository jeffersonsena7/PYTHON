# Desenvolva um programa que leia 4 valores pelo teclado e quadeos em uma tupla. no final moste.
# Quantas vezes apareceu o valor 9.
# Em que posição foi digitado o primeiro valor 3.
# Quais foram os números pares.


pares = 0
numero = (int(input('Digite o primeiro valor: ')), int(input('Digite o primeiro valor: ')),
           int(input('Digite o primeiro valor: ')),int(input('Digite o primeiro valor: ')))

print(f'Você digitou os valores {numero}')
print(f'Quntas vezes apareceu o valor 9, {numero.count(9)} vezes')
if 3 in numero:
    print(f'Em qual posição foi digitado o primeiro valor 3, {numero.index(3) +1} posição')
else:
    print('O número 3 não esta nos valores digitados')
print(f'Os números pares foi: ',end=' ')
for n in numero:
    if n %2 == 0:
        print(n, end=',')



# Faça um programa que leia treis numeros inteiros e mostre o maior e o menor número.

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero:'))

if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('o menor número foi {}'. format(menor))
print('O maior número foi {}'. format (maior))
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
#Faça tambem um programa que importe esses módulo e use alguma dessas função.
import moeda

#principal
p = float(input('Dite o preço: R$ '))
print(f'A metade de R$ {p} é R$ {moeda.metade(p)}')
print(f'O dobro de R$ {p} é R$ {moeda.dobro(p)}')
print(f'Aumento de 10% de R$ {p} é R$ {moeda.aumentar(p, 10)}')
print(f'Reduzido 13% de R$ {p} é R$ {moeda.diminuir(p, 13)}')

'''O mesmo professor do desafio anterior quer sortear a ordem de apresentaçaõ do trabalho de alunos. Faça um programa que leia os
quatros alunos e mostre a ordem sorteada.'''

import random
n1 = str(input('O nome do primeiro aluno: '))
n2 = str(input('O nome do segundo aluno: '))
n3 = str(input('O nome do terceiro aluno: '))
n4 = str(input('O nome do quarto aluno: '))

lista = [n1, n2, n3, n4]

random.shuffle(lista)
print(' A orde de apresentação será')
print(lista)

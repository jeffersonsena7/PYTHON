# Refaça o desafio 035 dos triângulos, acrecentando o recurso de mostrar que tipo de triângulo será formado.
#Equilatero: todos os lados iguais.
#Isóscalas: dois lados iguais.
#Escala: todos os lados diferentes

l1 = float(int(input('Digite a primeira reta: ')))
l2 = float(int(input('Digite a segunda reta: ')))
l3 = float(int(input('Digite a terceira linha: ')))

if l1 == l2 == l3 and l2 == l1 == l3 and l3 == l1 == l2:
    print('\033[1;34;40mTriângulo EQUILATERO, todos os lados iguais\033[m')
elif l1 == l2 != l3 or l1 == l3 !=l2 or l3 == l1 !=l2 or l3 == l2 != l1:
    print('\033[1;33;40mTriângulo ISÓSCALAR, pois tem 2 lados iguais.\033[m')
else:
    print('\033[1;32;40mTriângulo ESCALAR, todos os lados diferentes\033[m')
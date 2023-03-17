# Crie uma programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
#não atigiram a maioridade e quantas já são maior de idade.

from datetime import date # mostra o ano atual
atual = date.today().year
totalmaior = 0
totalmenor = 0

for c in range(1, 8):
    pessoa = int(input('Digite o ano da {}º pessoa: '.format(c)))
    idade = atual - pessoa
    if idade >= 18:
        totalmaior = totalmaior + 1
    else:
        totalmenor = totalmenor + 1
print('Ao total tivemos {} pessoas maiores de idade. '.format(totalmaior))
print('E também tivemos {} pessoas menores de idade. '.format(totalmenor))



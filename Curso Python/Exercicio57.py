# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = 0
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Valor incorreto, digite novamente [M/F]')
print('fim')
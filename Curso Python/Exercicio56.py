# Desenvolva um programa que leia o nome, idade e sexode 4 pessoas. No final do programa mostre:
#A média de idade do grupo / Qual o nome do homem mais velho / Quantas mulheres tem menos de 20 anos.

somaidade = 0
totalidade = 0
maioridadehomem = 0
nomevelho = ''
mulheres20 = 0
for pessoa in range(1,5):
    print('------{} Pessoa ------'.format(pessoa))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: '))

    somaidade = somaidade + idade
    if pessoa == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if idade > maioridadehomem and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome

    if sexo =='F' and idade < 20:
        mulheres20 = mulheres20 +1



media = somaidade / 4
print('A media de idade de todas as pessoas é:  {}'.format(media))
print('O homem mais velho tem {} anos e seu nome é: {}'.format(maioridadehomem, nomevelho))
print('{} Total de mulhers menor de  20 anos'.format(mulheres20))
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
#entre todos os valores e qual foi o maior e o menor valor lidos. O programa deve perguntar ao usuário se ele
#quer ou não continuar a digitar valores.

resp = 's'
soma = 0
media = 0
quantidade = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma = soma + num
    quantidade = quantidade +1

    if quantidade == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('deseja continuar [S/N]'))
media = soma / quantidade
print('Você digitou {} números, o menor número foi {}, o maior número foi {}'
      ' e a media de todos os numeros foi {}'.format(quantidade, menor, maior, media))
# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule o seu IMC e mostre de acor dom a tabela.
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input('Digite o peso da pessoa: '))
altura = float(input('Digite a altura da pessoa: '))

imc = peso / altura ** 2

if imc < 18.5:
    print('A pessoa esta abaixo do peso com IMC {:.2f}'. format(imc))
elif imc <=25:
    print('A pessoa esta no peso ideal IMC {:.2f}'.format(imc))
elif imc <= 30:
    print('A pessoa esta com sobrepeso IMC {:.2f}'. format(imc))
elif imc <= 40:
    print('A pessoa esta com obesidade IMC {:.2f}'. format(imc))
else:
    print('A pessoa esta com obesidade mórbida IMC {:.2f}'. format(imc))
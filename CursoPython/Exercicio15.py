'''Escreva um programa que pergute a quantidade de km percorrido por um carro alugado e a quantidade de dias que ele foi alugado. calcule o preço a pagar, sabendo que o carro custa RS60 por dia e R$ 0.15 por km rodado.'''

km = float(input('Digite a quantidade de km : '))
alugado = float(input('Digite a quantidade de dias: '))

dias = alugado * 60
rodado = km *0.15
total = dias + rodado

print('\033[1;34;40mQuantos km o carro rodou {}km e quantos dias alugado {} dias\033[m'. format(km, alugado))
print('\033[7;34;40mA quantidade de dias vc paga R${} e a quantidade de km vc paga R${}\033[m'.format (dias, rodado))
print('\033[1;31;40mO total a pagar de dias e rodado é R${}\033[m'. format(total))
# Escreva um programa para aprovar um emprestimo bancário para a compra de uma casa. pergunte o valor da casa,
#o salário do comprador e em quantas parcelas ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o emprestimo é negado.

casa = float(input('O valor da casa é: '))
salario = float(input('O salário do comprador é: '))
parcelas = int(input('Quantidade de parcelas: '))

prestacao = casa / parcelas
total = (salario * 30)/ 100

if prestacao < total:
    print('Parabéns seu financiamento foi aprovado o valor das parcelas é  \033[0;34mR${:.2f}\033[m'. format(prestacao))

else:
    print('Infelizmente o seu financiamento não foi aprovado, sua parcela excede o limit \033[0;31m R${:.2f}\033[m'. format(prestacao))



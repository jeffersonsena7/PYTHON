# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condições de pagamento:
# Á vista dinheiro/cheque:10% de desconto
# Á vista no cartão: 5% de desconto
# Em 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

produto = float(input('Digite o valor do produto: '))
pagamento = bool(input('\nDigite 1 pagamento avista:\n'
                       'Digite 2 pagamento no cartão direto:\n'
                       'Digite 3 pagamento dividido em 2x:\n'
                       'Digite 4 pagamento dividido em 3x ou mais:\n'))

din = produto * 10 / 100
dinheiro = produto -din

cart1 = produto * 5 / 100
cartao1 = produto - cart1

cartao2 = produto / 2

cart3 = produto * 20 / 100
cartao3 = (produto + cart3)

if pagamento == 1:
    print('O valo do produto é R${}, com desconto de 10% avista fica R${}'.format(produto, dinheiro))
elif pagamento == 2:
    print('O valor do produto é R${}, com desconto de 5% direto no cartão fica R${}'. format(produto, cartao1))
elif: pagamento == 3:
    print('O valo do produto é R${}, dividido em 2 parcelas de R${}'.format(produto, cartao2)
else:
    print('O valo do produto é R${}, dividido em 3x ou mais parcela fica {}'.format(produto, cartao3)
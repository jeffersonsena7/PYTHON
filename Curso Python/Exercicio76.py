# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados de forma tabular.

lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
         'Tranferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.30,
         'Canetas', 22.30, 'Livros', 34.90)
cont=0
letra = ''
num =''
print('--' * 25)
print('LISTAGEM DE PREÇOS')
print('--' * 25)
for pos in range(0, len(lista)):
    if pos %2==0:
        print(f'{lista[pos] :.<30}',end='') # espaço de 30 caracteres e pontilhado
    else:
        print(f'R$ {lista[pos]:>5.2f}') # espaço de 5 caracteres e 2 casas decimais
print('--' * 25)

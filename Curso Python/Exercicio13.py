'''Faça um algoritimo que leia p salário de um funcionario e mostre o seu novo salário, com 15% de aumento.'''

funcionario = float(input('Digite o salario do funcionario: '))

salario = funcionario * 15 / 100
novo = salario + funcionario

print('O salario do funcionario é\033[0;31m R${}\033[m\n\033[1;41mCom o novo aumento de 15%: R${}\033[m\n\033[1;34mNovo salario é {}R$\033[m'. format(funcionario, salario, novo))
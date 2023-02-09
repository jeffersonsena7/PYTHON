#Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
#Para salário superior a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais , o aumento é de 15%.

salario = float(input('Digite o valor do salário do funcionário da empresa: '))

if salario > 1250:
    aumento = salario + (salario * 10 / 100)
else:
    aumento = salario + (salario * 15 / 100)
print(' O salário do funcionario é R${:.2f}, com o aumento ficou R${:.2f}'. format(salario, aumento))
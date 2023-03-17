# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o nome completo: '))

dividido = nome.split()

print('O primeiro nome é: {}'. format(dividido[0]))
print('O ultimo nome é: {}'. format(dividido[len(dividido)-1]))

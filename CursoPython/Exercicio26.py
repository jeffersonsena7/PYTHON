# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A'.
# Em qual posiçaõ ela aparece a primeira vez.
# E que posicao ela aparece a última vez.

frase = str(input(' Digite uma frase: ')).strip().upper()

print('Quantas vezes aparece a letra a: {}'. format(frase.count('A')))
print('Qual posição ela aparec primeiro: {}'. format(frase.find('A')))
print('Qual posição ela aparece na última vez: {}'. format(frase.rfind('A')))
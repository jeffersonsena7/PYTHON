# A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade
# Até 9anos: MIRIM
# Até 14anos: INFANTIL
# Até 19anos: JUNIOR
# Até 20anos: SÊNIOR
# Acima: MASTER

ano = int(input('Digite o ano de nascimento do atleta: '))

idade = 2022 - ano

if idade <= 9:
    print('O atleta tem {}anos, esta na categoria MIRIM'. format(idade))
elif idade <= 14:
    print('O atleta tem {}anos, esta na categoria INFANTIL'. format(idade))
elif idade <= 19:
    print('O atleta tem {}anos, esta na categoria JUNIOR'. format(idade))
elif idade == 20:
    print('O atleta tem {}anos, esta na categoria SÊNOR'. format(idade))
else:
    print('O atleta tem {}anos, esta na categoria MASTER'. format(idade) )
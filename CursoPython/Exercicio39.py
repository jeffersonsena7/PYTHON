# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade.
# Se ele ainda vai se alistar ao servico militar
# Se é hora de se alistar.
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostra o tempo o tempo que falta ou o tempo q passou do prazo.

ano = int(input('Digite o ano do seu nascimento: '))

idade = 2022 - ano
falta = 18 - idade
passou = idade - 18

if idade == 18:
    print('Chegou a hora de se alistar, vc tem \033[0;34m{} anos \033[m'. format(idade))
elif idade < 18:
    print('Você tem {} anos, falta {}anos para você se alistar'. format(idade, falta))
else:
    print('Você tem {}anos, ja passou {}anos do prazo'. format(idade, passou))
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.
# Média a baixo de 5.0: REPROVADO
# Média entre 5.0 A 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

if media < 5.0:
    print('Aluno reprovado com média {}'. format(media))
elif media <= 6.9:
    print('Aluno em recuperação com media {}'. format(media))
else:
    print('Aluno aprovado com média {}'. format(media))
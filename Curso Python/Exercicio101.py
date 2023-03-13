# Crie um programa que tenha a função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
#retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return  f'Com {idade} anos: NÃO vota.'
    elif 16 <= idade <18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'



#programa principal

nascimento = int(input('Digite seu ano de nascimento: '))
print(voto(nascimento))
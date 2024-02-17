veiculo = ['avião', 'carro', 'navio', 'onibus']
# para colocar em maiusculo usando a função
f_maiusculo = lambda x: str.upper(x)

#usa o map para fazer todo o percurso e colocar colocando em maiusculo cada veiculo
nome_maiusculo = list(map(f_maiusculo, veiculo))

#mostra tudo em maiusculo não ée ccomo for, porem parecido
print(f'nomes maiusculos = {nome_maiusculo}')
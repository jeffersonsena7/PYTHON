# Modifique as funções que foram criadas no desafio 107 para que elas aceite um parâmetro a mais, informando
#se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import moeda

#principal
p = float(input('Dite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumento de 10% de {moeda.moeda(p)} é {(moeda.aumentar(p, 10, True))}')
print(f'Reduzido 13% de {moeda.moeda(p)} é {moeda.diminuir(p, 13, True)}')

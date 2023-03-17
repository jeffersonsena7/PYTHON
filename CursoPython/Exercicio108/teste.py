# Adapte o código do desafio 107, criandouma função adicional chamada moeda() que consiga mostrar os valores
#como um valor monetário formatado.
import moeda

#principal
p = float(input('Dite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumento de 10% de {moeda.moeda(p)} é {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzido 13% de {moeda.moeda(p)} é {moeda.moeda(moeda.diminuir(p, 13))}')

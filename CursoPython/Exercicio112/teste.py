# Crie um pacote chamado utilidadessCeV que tenha dois módulos inteiros chamados moedas e dados. Transfira todos as
#funções utilizadas nos desfios 107,108 e 109 para o primeiro pacote e mantenha tudo funcionando.
from utilidadescurso import moeda
from utilidadescurso import dado

#principal
p = dado.leiaDinheiro('Dite o preço: R$ ')
moeda.resumo(p, 20, 10)
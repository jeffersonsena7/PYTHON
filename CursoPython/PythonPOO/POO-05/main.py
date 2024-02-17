from classes import Cliente
from classes import Pessoa
from classes import Aluno
"""
Associação - Usa outro objeto
Agregação - Tem outro ou outros objetos como parte de se
Composição - É dono  de outro ou outros objetos
Herança - Onde o objeto é outro objeto
"""

c1 = Cliente('Jefferson', 33)
c1.fala()
c1.comprando()

a1 = Aluno('Jamylle', 16)
a1.fala()
a1.estudando()

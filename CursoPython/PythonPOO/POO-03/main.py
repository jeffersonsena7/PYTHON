# Agregação de herança

#importando
from classes import CarrinhoDeCompras
from classes import Produto

carrinho = CarrinhoDeCompras()

#cadastrando produto
p1 = Produto('Camiseta', 50)
p2 = Produto('Iphone', 10000)
p3 = Produto('Caneca', 15)

#para inserir produtos
carrinho.iserir_produto(p1)
carrinho.iserir_produto(p2)
carrinho.iserir_produto(p3)

#mostar a lista dos produtos cadastrados
carrinho.lista_produto()

#para mostrar a soma dos valores
print(carrinho.soma_total())
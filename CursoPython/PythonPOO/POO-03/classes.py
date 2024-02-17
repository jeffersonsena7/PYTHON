class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []   #onde vai ser criado a lista se inicia vazio

    def iserir_produto(self, produto):
        self.produtos.append(produto)  #O append adiciona o produto na lista

    def lista_produto(self):
        for produto in self.produtos:    #para fazer uma lista dos produtos
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total = total + produto.valor
        return total

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
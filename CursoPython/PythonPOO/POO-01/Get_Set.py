class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def nome(self):
        return self.novonome

    # Setter
    @nome.setter
    def nome(self, valor):
        self.novonome = valor.title() # para ficar a prime letra maiuscula title()

    # Getter      get= pega um valor
    @property
    def preco(self):
        return self.novopreco

    # Setter    set = configura um valor
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):    # se o valor é uma string
            valor = float(valor.replace('RS', '')) # filtra transformando em float e retirando o R$ por vazio
        self.novopreco = valor

p1= Produto('Camisa', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('sandalia', 'RS15')
p2.desconto(10)
print(p2.nome, p2.preco)
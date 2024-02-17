class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__  # issoa mostra qual classe esta sendo usada

    def fala(self):   # isso é para todo o codigo
        print(f'{self.nomeclasse} falando....') #para mostrar a classe que eesta sendo usada

class Cliente(Pessoa): # a classe cliente vai ter todods os dados de pessoa
    def comprando(self): #isso é só para o cliente
        print(f'{self.nomeclasse} Comprando....')

class Aluno(Pessoa):  # a classe clieneete vai ter todods os dados de pessoa
    def estudando(self):  #isso ée só para aluno
        print(f'{self.nomeclasse}  Estudando.....')
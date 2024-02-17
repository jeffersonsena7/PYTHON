from random import randint
                 # metodo de instacia
class Pessoa:    # essa class normal precisa da instacia self para funcionar  "um tipo de metodo"
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

                     #"Segundo tipo de metodo metodo de classe" , precisa esta deccorado com @classmethod
    @classmethod     # essa classe não precisa da instancia, porém precisa da classee em sim q foi dada como cls da class pessoa
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

# terceiro tipo de metodo
#metodo statico não precisa nem da instacia que a a self, nem da classe em se que é cls

    @staticmethod
    def gerar_id():
        rand = randint(0, 100)
        return rand

p1 = Pessoa('Jefferson', 33)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gerar_id())
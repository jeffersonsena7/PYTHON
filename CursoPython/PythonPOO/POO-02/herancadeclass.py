class Escritor: # associação de herança
    def __init__(self, nome):
        self.__nome = nome    #como foi colocado em privado, ele não vai ser mostrado fora da classe então tem quee criar um geet
        self.__fermentas = None
    @property
    def nome(self):
        return self.__nome

    @property
    def ferramentas(self):
        return self.__ferramentas
    @ferramentas.setter
    def ferramentas(self, ferramentas):
        self.__ferramentas = ferramentas

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo....')

class MaquinaDeEscrever:
    def escrever(self):
        print('Maquina está escrevendo....')
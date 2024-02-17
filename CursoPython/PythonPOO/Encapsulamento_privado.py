class Pessoa:

    def __init__(self, nome, idade, cpf): #atributos
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf  #coloca 2 anderlaine para mostrar que é privado

    def correr(self):  #metodos
        print('Estou correndo')

    def beber(self, bebida):  #metodos
        if bebida == 'cerveja':
            self.__apresentar_documento()
            print('bebendo....')

    def __apresentar_documento(self):  #metodos
        print(self.__cpf)

jefferson = Pessoa('jefferson', 33, '4567298js')
jefferson.beber('cerveja')
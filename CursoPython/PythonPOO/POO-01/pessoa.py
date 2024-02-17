class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):  # aqui são todos os atributos ou conhecido como construtor
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return
        print(f'{self.nome} está falando sobre, {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não esta falando')
            return           # Sempre usar o return para n entrar o codigo dee baixo, para usar um ou outro,
                             # com isso n precisa usar o else so colocar o codigo p dentro e
        print(f'{self.nome} parou de falar')
        self.falando = False


    def comer(self, alimento):       #aqui são os metodos em outars palavras o q vai fazer
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False

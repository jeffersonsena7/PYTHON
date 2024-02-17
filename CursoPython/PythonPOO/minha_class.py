class ControleRemoto:

    def __init__(self, televisão, comodo):
        self.televisao = televisão
        self.comodo = comodo

    def avacar_canal(self):
        print('Canal Avançar')

    def voltar_canal(self):
        print('Voltar Canal')

    def escolher_canal(self, canal):
        print('Alterado para o calna: {}'. format(canal))

controle_sala = ControleRemoto('Samsung', 'sala')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avacar_canal()
controle_sala.escolher_canal(12)
"""
public, quando usado eeem outras linguagens como php e c++

private em PYTHO é um __ dois anderlaine, com isso ja informa ou desenvolvedor para não modificar

"""

class BaseDeDados:
    def __init__(self):    # o construtor
        self.dados = {}   #criando um dicionario vazio como se fosse uma tabela

    def inserir_cliente(self, id, nome):  # metoddos
        if 'cliente' not in self.dados:   # se a chave esta em dicionario se não estiver, ele cria
            self.dados['cliente'] = {id:nome}
        else:
            self.dados['cliente'].update({id:nome}) # caso a chave exista ele atuaiza update

    def lista_clientes(self):
        for id, nome in self.dados['cliente'].items(): #para mostrar toda a lista de dados dos clientes
            print(id, nome)
    def apagar_clienete(self, id):
        del self.dados['cliente'][id]

db = BaseDeDados()
db.inserir_cliente(1, 'Jefferson')
db.inserir_cliente(2, 'Joseane')
db.inserir_cliente(3,'Jamylle')
db.apagar_clienete(2)
db.lista_clientes()
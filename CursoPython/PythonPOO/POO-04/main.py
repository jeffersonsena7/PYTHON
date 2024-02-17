from classes import Cliente


cliente1 = Cliente('Jefferson', 33)
cliente1.insere_endereco('João Pessoa', 'PB')
print(cliente1.nome)
cliente1.lista_endereco()
print()

cliente2 = Cliente('Jamylle', 16)
cliente2.insere_endereco('Santa Rita', 'PB')
print(cliente2.nome)
cliente2.lista_endereco()
print()

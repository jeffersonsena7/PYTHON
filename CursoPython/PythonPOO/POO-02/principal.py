from herancadeclass import Escritor
from herancadeclass import Caneta
from herancadeclass import MaquinaDeEscrever

escritor = Escritor('Jefferson')
print(escritor.nome)

caneta = Caneta('Bic')
print(caneta.marca)

maquina = MaquinaDeEscrever()
escritor.ferramentas = maquina
escritor.ferramentas.escrever()
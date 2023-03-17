# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
#cobrando R$0,50 por km para viagem de até 200km e R$0,45 para viagem mais longas.

viagem = float(input('Digitete a distância da viagem: '))

distancia = viagem * 0.50
distancialonga = viagem * 0.45
if viagem <= 200:
    print('Sua viagem é de {}KM seu valor é de R${}'. format(viagem, distancia))
else:
    print('Sua viagem é de {}km, seu valor é de R${}'. format(viagem, distancialonga))
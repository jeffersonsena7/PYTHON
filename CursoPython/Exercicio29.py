# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre a mensagem dizendo
#que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.]

carro= float(input('Digite a velocidade do carro: '))
velocidade = (carro - 80)* 7
if carro <= 80:
    print('Velocidade de {}Km/h, boa viagem'. format(carro))
else:
    print('Vc passou na velocidade de {}Km/h, ultrapassando a velocidade normal de 80km/h, sua multa é de R${}'. format(carro, velocidade))
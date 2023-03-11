# Faça um programa que tenha um a função chamada área(), que receba as dimensões de um terreno retangular
#(largura e comprimento) e mostre a área do terreno

def area(largura, comprimento): # função
    a = largura * comprimento
    print(f'A área de um terreno {largura} X {comprimento} é de {a}m²')


#programa principal
print('Controle de Terreno')
print('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
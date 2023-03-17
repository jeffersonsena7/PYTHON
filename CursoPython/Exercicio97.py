# Faça um programa que tenha a função chamada escreva(), que receba um texto qualquer como parâmetro e mostre
#uma mensagem com tamanho adptável.

def escreva(msg):
    tam = len(msg) + 4 # para colocar mais 2 tios na frente e atras
    print('~'* tam)
    print(f'  {msg}.')
    print('~'*tam)


#programa principal
escreva('Jefferson de Sena')
escreva('Joseane')
escreva('Jamylle victória Mendes de Sena')
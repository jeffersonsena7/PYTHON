lista_numeros = [9.56783, 7.57568, 3.00914, 6.2321]

lista_precisao = [2,2,3,3]

# o x ée o número que eu quero arreedondar e o y é a precisão quantos números apos a virgula
# round para arredondar
arredondamento = lambda x,y: round(x,y)

#o map vai o arredondamento para lista de numero e depois qual precisão
reesultado = list(map(arredondamento,lista_numeros, lista_precisao))

print(reesultado)
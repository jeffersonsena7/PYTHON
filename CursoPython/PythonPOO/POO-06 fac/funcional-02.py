lista = [0,1,1,2,3,5,6,7,8,13,21,34]

# testa se é par usando o funcional lambda
fTestePar = lambda x: x % 2 == 0

#isso é só para teste para mostrar quando não é par, não precisa fazer
print(f'teste de fTestePar(5) = {fTestePar(5)}')

#usa o filter para filtrar e pegar so os itens verdadeiros, os que são pares
pares = list(filter(fTestePar, lista))

print(f'lista dee números pares = {pares}')
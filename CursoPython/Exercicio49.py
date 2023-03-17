#Faça uma tabuada de um número usando o laço for

num = int(input('Digite o número para a tabuada: '))
print("-=" * 10)
print("TABUADA USANDO O FOR")
for c in range(0, 10):
    soma = c * num
    print ("{} X {} = {}".format(c, num, soma))

#Crie um programa que leia uma frase qualquer e digite e diga se ela é um políndromo,
#desconsiderando os espaços.

frase = str(input("Digite a frase: ")).strip().upper() #remove espaço antes e depois da frase e coloca tudo em maiusculo
palavra = frase.split()  #vira uma lista de vetor
junto = ''.join(palavra) #junta toda a frase removendo os espaços
inverso = ''
#inverso = junto[::-1]   //isso tbm inverte a frase sem o FOR e sem o inverso sem nada
for letra in range(len(junto) -1, -1, -1): #para inverter o nome
    inverso = inverso + junto[letra]
print(junto)
print(inverso)

if junto == inverso:
    print("Isso é um palíndromo")
else:
    print("Isso não é um palíndromo")
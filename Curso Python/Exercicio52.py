#Faça um programa que leia um número inteiro e diga se ele é ou não númerp primo.

tot = 0
num = int(input("Digite um número: "))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot = tot + 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\n\033[m O número {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('É por isso ele é primo')
else:
    print('É por isso ele não é primo')
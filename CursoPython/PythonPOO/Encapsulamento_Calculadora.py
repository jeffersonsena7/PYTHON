class Calculadora:

    def calcular(self, op, num1, num2):
        if op == '+':
            return self.__adicao(num1, num2)
        elif op == '-':
            return self.__subtracao(num1, num2)
        else:
            print('Operação invalida')

    def __adicao(self, num1, num2):  # deixa privado p o usuario não ver e nem alterar esse metodo
        return num1 + num2

    def __subtracao(self, num1, num2):  # deixa privado p o usuario não ver e nem alterar esse metodo
        return  num1 - num2

total = Calculadora() #deixa só assimm pq nao tem os atributos de construção então a class fica vazia
resultado = total.calcular('-', 3, 2)
print(resultado)
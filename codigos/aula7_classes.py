class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b


# declarando o objeto
calculadora = Calculadora(4, 2)

print("1° valor: "+str(calculadora.valor_a) + " e 2° valor: " + str(calculadora.valor_b))

print("Soma: {}".format(calculadora.soma()))
print("Subtração: {}".format(calculadora.subtracao()))
print("Multiplicação: {}".format(calculadora.multiplicacao()))
print("Divisão: {}".format(calculadora.divisao()))
class Calculadora:
    def __init__(self):
        pass

    # Ou pode deixar sem o:
    # def __init__(self):
    #     pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

if __name__ == "__main__": # Só execute esse trecho se for chaado pelo proprio arquivo. Se for importado por outra classe essa parte não será exibida.
    # declarando o objeto
    calculadora = Calculadora()

    print("Soma: {}".format(calculadora.soma(10, 2)))
    print("Subtração: {}".format(calculadora.subtracao(5, 3)))
    print("Multiplicação: {}".format(calculadora.multiplicacao(100, 2)))
    print("Divisão: {}".format(calculadora.divisao(10, 5)))

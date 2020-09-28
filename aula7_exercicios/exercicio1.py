# Você foi convocado para reparar o liquidificador de uma amiga, por sorte você avalia o produto e percebe que
# ele foi programado em Python, com o seguinte trecho de código:

# REsposta: Tanto #lacuna1 quanto #lacuna2 devem ser substituídos por self.power = True

class Liquidificador:

    def __init__(self):

        self.velocidade = 0

        self.power = False

    def velocidade_A(self):

        # lacuna1
        self.power = True

        if self.power:
            self.velocidade = 1
        else:
            print("desligado!")

    def velocidade_B(self):

        # lacuna2
        self.power = True

        if self.power:
            self.velocidade = 2

    def velocidade_Z(self):

        self.velocidade = 0

        self.power = 0

walita = Liquidificador()
print("Liquidificador está ligado?: {}".format(walita.power))
walita = Liquidificador()
print("Liquidificador está ligado?: {}".format(walita.power))
walita.velocidade_A()
print("Aumentou a velocidade para: {}".format(walita.velocidade))


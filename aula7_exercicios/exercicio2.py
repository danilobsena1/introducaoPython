# Você foi convocado para consertar um ar condicionado de uma amiga, por acaso você avalia
# o produto e percebe que ele foi programado em Python, com o seguinte trecho de código:

# Sua amiga está reclamando que o ar condicionado está marcando 29 graus,
# sendo que não consegue diminuir a temperatura, sendo que ele quebrou porque alguém antes colocou 15 graus,
# portanto ela não quer que o ar condicionado seja regulado menor que 18 graus.

class ArCondicionado:

    def __init__(self):
        self.temperatura = 20

    def aumentarTemperatura(self):
        if self.temperatura < 30:
            self.temperatura += 1

    def diminuirTemperatura(self):
        # lacuna1
           if self.temperatura < 18:
        # lacuna2
            self.temperatura -= 1

ar = ArCondicionado()
ar.diminuirTemperatura()
print("Diminuiu a temperatura para: {}".format(ar.temperatura))
ar.aumentarTemperatura()
print("Aumentou a temperatura para: {}".format(ar.temperatura))

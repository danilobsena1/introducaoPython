# Você foi convocado para reparar uma geladeira de uma amiga,
# que coincidentemente foi programado em Python. Você avalia o seguinte trecho de código:

# Ela está reclamando que a geladeira está congelando demais os alimentos,
# sendo que o ideal é que a temperatura esteja sempre entre -2 e 2 graus.

# Sendo assim, qual das afirmativas abaixo combinariam-se para solucionar este caso?


# I - O if self.temperatura < self.minimo ser substituído por if self.temperatura > self.maximo
# II - O if self.temperatura < self.minimo ser substituído por if self.temperatura > self.minimo
# III - O elif self.temperatura < self.minimo ser substituído por elif self.temperatura > self.maximo
# IV - O elif self.temperatura < self.minimo não requer modificação.

# RESPOSTA: I e IV


class Geladeira:

    def __init__(self):

        self.temperatura = -20

        self.minimo = -2

        self.maximo = 2

    def regularTemperatura(self):

        if self.temperatura < self.minimo:

            self.temperatura -= 1

        elif self.temperatura < self.minimo:

            self.temperatura += 1

    def mostrarTemperatura(self):

        print('Atual: {}.'.format(self.temperatura))

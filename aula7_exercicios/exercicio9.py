# Você foi convocado para reparar um fogão de uma amiga, que, apesar de inesperado,
# foi programado em Python. Você avalia o seguinte código:

# Ela relata que depois que liga o fogão, não desliga mais, vazando gás.
# A solução dela foi ficar cozinhando sem parar para não desperdiçar o gás, mas essa não é a melhor solução.
# Você pensa e avalia a melhor das alternativas abaixo:

# RESSPOSTA: Para cada def acionar (1 a 4), é necessário inserir um if checando o status da variável boca referente (1 a 4)
# na qual irá realizar a inversão do valor da variável tipo 'bool'

class Fogao:

    def __init__(self):
        self.boca1 = False

        self.boca2 = False

        self.boca3 = False

        self.boca4 = False

    def acionar1(self):
        boca1 = True

    def acionar2(self):
        boca2 = True

    def acionar3(self):
        boca3 = True

    def acionar4(self):
        boca4 = True
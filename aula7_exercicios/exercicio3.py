# Você foi convocado para reparar uma torradeira de uma amiga,
# que por algum motivo está sempre passando do ponto e queimando os pães.
# Você avaliou o produto e coincidentemente foi programado em Python com o seguinte trecho de código:

# Resposta: Em def __init__, a variável self.calorMaximo ser igual a 70

class Torradeira:

  def __init__(self, tempo):

    self.tempo = 0

    self.calorAtual = 0

    self.calorMaximo = 70

  def torrar(self):

    self.tempo += 1

    if self.calorAtual < self.calorMaximo:

      self.calorAtual += 1 + self.calorAtual

pao = Torradeira()
pao.torrar()
print("dfdf: {}".format(pao.calorAtual))